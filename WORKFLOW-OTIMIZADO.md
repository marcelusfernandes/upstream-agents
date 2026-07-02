# Workflow Otimizado — Product Discovery Pipeline v3 (execução nativa Claude Code)

**Padrão de orquestração:** *prompt chaining* com gates programáticos + aprovação humana entre fases
(Anthropic — *Building Effective Agents*; verificação por código conforme *Claude Agent SDK*; contexto mínimo conforme *Effective Context Engineering*).

O pipeline executa **nativamente no Claude Code**: 15 subagentes em `.claude/agents/`, skills de fase em `.claude/skills/` (disparadas pelo humano), hook de guardrail em tempo de escrita e gates por script. A definição canônica de passos, contratos e gates está em **`pipeline.yaml`** — nenhum outro arquivo deve redefinir a sequência.

---

## 1. Princípios de design

1. **Workflow, não agente autônomo.** A decomposição das tarefas é fixa e previsível — o padrão correto é encadeamento com caminhos pré-definidos, não um orquestrador dinâmico. Menos complexidade, mais previsibilidade.
2. **Verificação por código primeiro.** Todo gate roda checagens determinísticas (arquivos existem, não estão vazios, sem métricas inventadas) *antes* de pedir julgamento humano. Prosa do tipo "sempre garanta qualidade" não é guardrail — ou vira script, ou vira rubrica de avaliação, ou é removida.
3. **Menor conjunto de tokens de alto sinal.** Agentes recebem: papel (1-2 frases) + caminhos de entrada + procedimento curto + referência ao template. Material pesado é carregado *just-in-time* pelo caminho, nunca colado no prompt.
4. **Fonte única de verdade.** `pipeline.yaml` define o pipeline. README, orquestrador e agentes *referenciam*; duplicar = garantir drift (foi exatamente o que aconteceu na v2).
5. **O modelo não pula gate humano.** Cada fase é disparada explicitamente pelo humano. A fase N+1 só inicia com o gate N aprovado e registrado em `.gates/` (trilha de auditoria commitável).
6. **Passos idempotentes e retomáveis.** Cada passo lê entradas nomeadas e escreve saídas nomeadas. `status` mostra exatamente onde o pipeline parou; reexecutar um passo sobrescreve apenas as próprias saídas.

---

## 2. Arquitetura do fluxo

```
0-documentation/ (contexto + entrevistas)
        │
┌───────▼───────────────── FASE 1 · Problem Discovery ─────────────────┐
│ context-setup → interview-analysis → painpoint-granularization       │
│   → painpoint-clustering → asis-journey-mapping                      │
│   → journey-consolidation → strategic-report → visual-journey-spec   │
└───────────────┬───────────────────────────────────────────────────────┘
        ═══ GATE G1 ═══  outputs_exist + guardrails_scan + aprovação humana
┌───────▼───────────────── FASE 2 · Solution Development ──────────────┐
│ solution-ideation → experience-design → solution-concepts            │
│   → mvp-prioritization → product-communication                       │
└───────────────┬───────────────────────────────────────────────────────┘
        ═══ GATE G2 ═══  outputs_exist + guardrails_scan + aprovação humana
┌───────▼───────────────── FASE 3 · Delivery Preparation ──────────────┐
│ confluence-structure → jira-structure                                 │
└───────────────┬───────────────────────────────────────────────────────┘
        ═══ GATE G3 ═══  pronto para import em Confluence/Jira
```

Cada passo tem **nome por papel** (ex.: `painpoint-synthesizer`), eliminando a ambiguidade dos dois "Agent 6" — os números permanecem apenas como aliases históricos nos arquivos de instrução.

---

## 3. Como executar

### Preparação
1. Preencha `0-documentation/0a-projectdocs/context.md` (objetivos de negócio).
2. Coloque as entrevistas em `0-documentation/0b-Interviews/`.
3. Confira a prontidão: `python3 scripts/validate-gate.py status`

### Executando uma fase (Claude Code)
Cada fase é uma **skill disparada pelo usuário** (`disable-model-invocation: true` — o modelo nunca avança um gate sozinho):

```
/phase-1-problem      # Fase 1 — Problem Discovery
/phase-2-solution     # Fase 2 — Solution Development (exige G1 aprovado)
/phase-3-delivery     # Fase 3 — Delivery Preparation (exige G2 aprovado)
/pipeline-status      # progresso e próxima ação
```

A skill lê a fase em `pipeline.yaml` e, passo a passo: lança o subagente do campo `role`, confere o contrato de saída ao retorno (reexecuta apontando a lacuna se quebrado) e nunca avança com contrato quebrado. Cada subagente lê apenas os `inputs` declarados e carrega seu template de `_output-structure/` *just-in-time*.

**Enforcement em tempo de escrita:** o hook `PostToolUse` (`.claude/hooks/guardrail-check.py`) escaneia todo Write/Edit em entregáveis; métricas especulativas bloqueiam com exit 2 e o stderr volta ao agente para autocorreção imediata — o erro é corrigido no momento em que nasce, não só no gate.

### Fechando uma fase (o gate)
```bash
# 1. Checagens de máquina (read-only; nunca altera arquivos)
python3 scripts/validate-gate.py check 1

# 2. Se houver métricas especulativas apontadas, auto-fix sob demanda:
python3 _agents/validate-guardrails.py 1-problem/1d-problem-output

# 3. Revisão humana dos outputs e registro da aprovação:
python3 scripts/validate-gate.py approve 1
git add .gates/ && git commit -m "gate: aprova G1"

# 4. A próxima fase só inicia se:
python3 scripts/validate-gate.py can-start 2   # → ✅
```

O comando `approve` **recusa** aprovar se as checagens de máquina falharem — o humano valida conteúdo, a máquina valida contrato.

### Retomando um trabalho interrompido
```bash
python3 scripts/validate-gate.py status
# ✅ = concluído · ▶️ = pronto para executar · ⛔ = bloqueado por dependência
```

---

## 4. Contratos de saída e guardrails

- **Contrato de saída** = lista de arquivos (ou globs com `min_files`) que o passo deve produzir, declarada em `pipeline.yaml`. Um passo sem seus outputs simplesmente não está concluído — não importa o que o agente "disse".
- **Guardrails executáveis**: o gate roda os padrões de `_agents/validation-patterns.json` (métricas financeiras/ROI inventadas) em modo *scan-only* sobre todos os `.md` da fase. Violação = gate reprovado com arquivo e trecho apontados.
- **Guardrails de julgamento** (citações inventadas, atribuição de fonte, tom especulativo): permanecem como critérios da **revisão humana** no gate — declaradamente, sem fingir que prosa bloqueia alguma coisa.

---

## 5. Regras de context engineering para os agentes

Ao editar/criar qualquer agente do pipeline:

| Regra | Racional |
|---|---|
| Prompt ≤ 120 linhas: papel, entradas, procedimento em heurísticas, contrato de saída | Evita "context rot"; altitude certa (nem if-else frágil, nem platitude vaga) |
| **Nunca** embutir o outline do template no prompt — referencie o caminho em `_output-structure/` | Elimina a duplicação que causou drift e o dobro de tokens |
| Guardrails: uma linha apontando para `pipeline.yaml` + scan do gate | Substitui as 4 cópias da tabela de auto-fix |
| Um objetivo por agente; saída de um passo = entrada do próximo via arquivo | Isolamento de contexto entre fases |
| Idioma único por pipeline (recomendado: manter EN nos prompts, PT-BR nos outputs se o projeto for BR) | Consistência de instrução |

---

## 6. Roadmap de migração

**Etapa A — Correções de consistência ✅ (aplicada neste branch)**
Legados arquivados (`_archive/legacy/`), orquestrador migrado para 2A/2B, `workflow-rules.md` com Fase 3 real, README/guardrails/caminhos corrigidos, `.DS_Store` fora do versionamento.

**Etapa B — Manifesto + gates ✅ (aplicada neste branch)**
`pipeline.yaml` (fonte única) + `scripts/validate-gate.py` (`status` / `check` / `approve` / `can-start`), testados ponta-a-ponta, incluindo detecção de violação de guardrail.

**Etapa C — Dieta de prompts ✅ (aplicada — migração v3.1)**
Os 15 agentes foram **destilados** de prompts de 150-850 linhas para ≤120 linhas cada (`.claude/agents/`): papel, entradas, procedimento em heurísticas, contrato de saída referenciando templates por caminho, guardrails em 3 linhas. Metodologia preservada e verificada por rubrica (testes de atomicidade do decomposer, RICE do strategist, ADKAR do communicator etc.); a autocontradição do concept-specialist foi corrigida (agora estritamente conceitual — specs técnicas e user stories pertencem à Fase 3). Idioma unificado em inglês. Redução de ~70-85% de contexto por invocação.

**Etapa D — Execução nativa em Claude Code ✅ (aplicada — migração v3.1)**
- `.claude/agents/<papel>.md` — 15 subagentes com frontmatter (`name`, `description` "use for…", `tools: Read, Grep, Glob, Write`, `model: sonnet` para extração mecânica / `inherit` para síntese).
- `.claude/skills/phase-{1,2,3}-*/SKILL.md` com `disable-model-invocation: true` — o humano dispara cada fase; `approve` é sempre do humano. `/pipeline-status` para progresso.
- Hook `PostToolUse` em `Write|Edit` (`.claude/hooks/guardrail-check.py` via `.claude/settings.json`): exit 2 bloqueia métricas especulativas em entregáveis e devolve o erro ao agente — testado.
- `CLAUDE.md` com fatos e regras duras (~50 linhas); procedimentos vivem nas skills.
- **Aposentados** (em `_archive/`): o espelho `.cursor/` inteiro, os agentes numerados de `_agents/` e a prosa de guardrails (`GUARDRAILS-ENFORCEMENT`, `guardrails-police`, `guardrail-validator`, `validation-readme`) — substituídos por CLAUDE.md + hook + gates.
- **Paralelismo opcional (agent teams):** com `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, trabalho independente dentro de uma fase roda como teammates (um `qualitative-researcher` por entrevista; publishers da Fase 3 lado a lado). Teams paralelizam *dentro* da fase, nunca através de gates.

**Etapa E — Avaliador interno (opcional, próximo passo)**
Subagente crítico (*evaluator-optimizer*) que confere cada entregável contra a rubrica do template antes de apresentá-lo ao humano — útil porque os critérios de aceite por entregável já existem.

---

## 7. Anti-padrões eliminados

| Antes (v2) | Depois (v3) |
|---|---|
| Sequência do pipeline redefinida em 4+ lugares divergentes | `pipeline.yaml` canônico; o resto referencia |
| Gate = "Type 'continue'" (prosa) | `check`/`approve` por script + marcador auditável em `.gates/` |
| "Guardrails-police bloqueia entregas" (impossível) | Scan determinístico no gate; julgamento explícito no humano |
| Agent 8 duplicado, backups vivos, meta-review de 1.773 linhas entre os templates | Arquivados em `_archive/legacy/` |
| Orquestrador executando agente deprecado | Migrado para 2A/2B e apontando para o manifesto |
| Numeração ambígua (dois "Agent 6") | Nomes por papel no manifesto |
| Falha no meio = recomeçar do zero | `status` mostra o ponto exato; passos idempotentes |
| Prompts de 600-850 linhas com templates embutidos | Subagentes ≤120 linhas; templates lidos just-in-time |
| Violação de guardrail descoberta só no fim (ou nunca) | Hook bloqueia no momento da escrita; gate re-escaneia a fase |
| Instruções acopladas a um editor específico (Cursor `.mdc`) | Config nativa `.claude/` versionada; degrada graciosamente como markdown puro |
