# Avaliação da Aplicação — Sistema de Agentes de Product Discovery

**Data:** 2026-07-02 · **Escopo:** todo o repositório (~9.600 linhas, ~28 arquivos de agentes/config + espelho `.cursor/rules`)
**Metodologia:** auditoria completa de `_agents/`, `_output-structure/`, `.cursor/` e documentação, cruzada com as práticas atuais de construção de agentes (Anthropic — *Building Effective Agents*, *Effective Context Engineering*, Claude Agent SDK).

---

## 1. Sumário Executivo

A lógica do workflow (Problema → Solução → Entrega, com validação humana) é **sólida e bem concebida**. Porém, a implementação carrega **dívida estrutural significativa**: uma migração inacabada (split do Agent 2 em 2A/2B), um agente legado duplicado (Agent 8), o orquestrador desatualizado em relação à documentação, guardrails ~90% em prosa não-executável e duplicação total entre `_agents/*.md` e `.cursor/rules/*.mdc` com divergência entre as cópias.

| Dimensão | Nota | Justificativa |
|---|---|---|
| Concepção do workflow | ⭐⭐⭐⭐ | Encadeamento com gates humanos é o padrão correto para pipeline sequencial |
| Consistência interna | ⭐⭐ | Orquestrador, READMEs e agentes se contradizem; arquivos referenciados não existem |
| Enforcement de qualidade | ⭐⭐ | Só o scan regex de métricas financeiras é executável; o resto é prosa |
| Eficiência de contexto (tokens) | ⭐⭐ | Templates duplicados dentro dos prompts; guardrails repetidos em 4 lugares |
| Manutenibilidade | ⭐⭐ | Duas fontes de verdade (`_agents` vs `.cursor`) que divergiram na prática |

---

## 2. O que funciona bem

- **Decomposição em fases com gates humanos** — corresponde exatamente ao padrão *prompt chaining with gates* recomendado pela Anthropic para tarefas com decomposição previsível.
- **Split 2A (divergente) / 2B (convergente)** — separar granularização de clusterização é boa engenharia de prompt: um objetivo por agente.
- **Artefatos em disco como memória** — cada agente lê/escreve arquivos nomeados; é a estratégia correta para pipelines longos (retomável, auditável).
- **`validate-guardrails.py` + `validation-patterns.json`** — a única peça de validação verificável por máquina; funcional e bem estruturada.
- **Templates de saída separados** em `_output-structure/` — a base para contratos de saída já existe.

---

## 3. Defeitos encontrados

### Críticos (quebram a execução correta)

| # | Defeito | Local |
|---|---|---|
| C1 | **Agent 8 duplicado e conflitante**: `agent-8-communication-specialist.md` (legado v1) coexiste com `agent-8-solution-concept-specialist.md`, referencia caminhos inexistentes (`2a-ideation/`, `2b-validation/`), exige template inexistente (`change-management-template.md`) e colide com o Agent 10 | `_agents/solution-space/` + espelho `.cursor/` |
| C2 | **Orquestrador nunca migrou para o split 2A/2B**: ainda executa o "Agent 2" único (arquivo `.backup`) e declara "5 agentes" quando a Fase 1 tem 8 passos | `.cursor/rules/agent-workflow-orchestrator.mdc` |
| C3 | **`workflow-rules.md` descreve uma Fase 3 que não existe** (`3-development/` com specs técnicas) em vez da real (`3-delivery/` com Confluence/Jira); a sequência R10 para na Fase 2 | `_output-structure/workflow-rules.md` |
| C4 | **Contradição sobre o output do Agent 0**: README aponta `0a-projectdocs/context.md`; todos os agentes downstream dependem de `0-documentation/broad-context.md` | `README.md` vs todos os agentes |

### Altos (corroem confiabilidade e manutenção)

| # | Defeito | Local |
|---|---|---|
| A1 | **Dupla fonte de verdade divergente**: `.cursor/rules/*.mdc` são cópias manuais de `_agents/*.md` com tamanhos e conteúdos diferentes (ex.: agent-9: 186 vs 842 linhas) | árvores `.cursor/` e `_agents/` |
| A2 | **Guardrails 90% prosa**: `guardrails-police.md` afirma "bloquear entregas", mas nenhum runtime dá esse poder a um LLM; só o regex financeiro é executável — e não está integrado a nada | `_agents/GUARDRAILS-*` |
| A3 | **Arquivos referenciados que não existem**: `improvements.md`, `change-management-template.md`, `.cursorpkg/instructions/...` | README, validation-readme, agent-8 legado |
| A4 | **`GUARDRAILS-ENFORCEMENT.md` descreve papéis antigos** (Agent 7 = "Process Optimization", Agent 8 = "Communication"), contradizendo `guardrails-police.md` | `_agents/GUARDRAILS-ENFORCEMENT.md` |
| A5 | **Agent 8 se autocontradiz**: instruído a ficar "conceitual, não técnico", mas seu próprio outline embutido exige `Requirements`, `User Stories`, `Technical Considerations` | `_agents/solution-space/agent-8-solution-concept-specialist.md` |

### Médios (higiene e precisão)

- README com contagens de templates erradas e atribuição errada (`experience-evolution-template` é do Agent 10, não do 7).
- `.cursor/rules/problem-space/README.md` obsoleto (pré-split); `.cursor/commands/validacao.md` com caminho quebrado; `entrevista.md` e `learning.md` referenciam estruturas de outro projeto.
- Templates órfãos (`guardrail-validation-checklist.md` — zero referências) e meta-review de 1.773 linhas (`template-quality-assessment.md`) dentro do diretório que os agentes varrem.
- `.DS_Store` versionados; dois "Agent 6" com o mesmo número (documentado, mas frágil para qualquer orquestrador que indexe por número); idioma misto (EN/PT) entre agentes do mesmo pipeline.

---

## 4. Aderência às boas práticas atuais de construção de agentes

| Prática (fonte) | Estado no repo | Gap |
|---|---|---|
| *Workflows com gates programáticos* para decomposição previsível (Building Effective Agents) | Gates existem só como prosa ("Type 'continue'") | Nenhuma checagem é executada por código entre fases |
| *Verificação por código primeiro, LLM-judge depois* (Claude Agent SDK) | Só o regex financeiro; nada valida existência/estrutura dos outputs | Um agente pode "concluir" sem gerar os arquivos exigidos |
| *Menor conjunto de tokens de alto sinal* (Effective Context Engineering) | Prompts de 600–850 linhas com outlines duplicando os templates de `_output-structure/` | ~2x de tokens por invocação; "context rot" nas fases longas |
| *Carregamento just-in-time* de referência pesada | Tudo embutido no prompt de cada agente | Templates deveriam ser referenciados por caminho e lidos sob demanda |
| *Fonte única de verdade para o pipeline* | Sequência redefinida em README, orquestrador, workflow-rules e READMEs de espaço — todas divergentes | A definição do pipeline não existia em lugar nenhum de forma canônica |
| *Nomes por papel, não por número* | "Agent 6" colide em duas fases; numeração quebra ao inserir passos | Roteamento ambíguo |
| *Passos idempotentes e retomáveis* | Sem estado de execução; retomar = reler tudo manualmente | Falha no meio = recomeço |
| *Gate humano que o modelo não pode pular* | Trigger único "start workflow" percorre tudo | O anti-padrão do mega-trigger |

---

## 5. Eficiência de tokens (custo real por execução)

- **Outlines embutidos**: Agent 8 carrega ~200 linhas de outline que duplicam `solution-concept-template.md` + `concept-breakdown-template.md`. O mesmo padrão se repete nos agentes 6-12.
- **Guardrails em 4 cópias**: a mesma tabela de auto-fix existe em `GUARDRAILS-ENFORCEMENT.md`, `guardrails-police.md`, `guardrail-validator.md` e `validation-patterns.json` — **~970 linhas de prosa descrevendo o que ~300 linhas de JSON+Python implementam**.
- **Espelho `.cursor/rules`**: dobra a superfície de manutenção inteira do repositório.
- Boilerplate repetido ("Formatting Rules", "Definition of Done", mensagens de conclusão) em todos os 15 agentes.

**Estimativa:** eliminar as duplicações reduz o contexto carregado por invocação em ~40–50% sem perda de capacidade.

---

## 6. Resultado desta entrega

**Correções aplicadas neste branch** (detalhes no diff):
1. Agent 8 legado, backups do Agent 2 pré-split e meta-review de 1.773 linhas movidos para `_archive/legacy/`.
2. Orquestrador migrado para 2A/2B, sequência corrigida (8 passos na Fase 1) e apontando para o manifesto canônico.
3. `workflow-rules.md` corrigido para `3-delivery/` + Agentes 11-12 (v2.3.0).
4. README corrigido (output do Agent 0, contagens, atribuições, referências mortas); `GUARDRAILS-ENFORCEMENT.md` com papéis atuais; caminhos quebrados consertados; `.DS_Store` removidos + `.gitignore`.

**Novo mecanismo de execução** (ver `WORKFLOW-OTIMIZADO.md`):
- `pipeline.yaml` — fonte única de verdade: fases, passos, contratos de entrada/saída, gates.
- `scripts/validate-gate.py` — gates verificáveis por máquina (existência/não-vazio dos outputs + scan read-only de guardrails) com aprovação humana registrada em `.gates/` — testado ponta-a-ponta.

**Pendências recomendadas** (não aplicadas nesta entrega — mudam comportamento dos agentes):
- Dieta de prompts: remover outlines embutidos dos agentes 6-12 e referenciar os templates por caminho (~40% de redução de contexto).
- Resolver a colisão dos dois "Agent 6" renomeando por papel (o manifesto já usa nomes por papel).
- Remover a seção técnica contraditória do Agent 8 (`Requirements`/`User Stories`/`Technical Considerations`).
- Decidir o destino do espelho `.cursor/rules` (gerar a partir de `_agents/` ou eliminar) e unificar o idioma dos prompts.
- Migração opcional para o modelo nativo Claude Code (`.claude/agents` + skills + hooks) — roadmap na etapa C do `WORKFLOW-OTIMIZADO.md`.
