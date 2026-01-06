# 📚 Comando Learning - Documentação de Aprendizados

## 🎯 Objetivo
Documente aprendizados importantes na pasta `_context/learnings/` para consulta futura do AI Coding Agent.

## 📁 Estrutura de Arquivos
- **Localização:** `_context/learnings/DD-MM/` (pastas organizadas por data)
- **Formato:** Sempre `.md` (Markdown)
- **Nomenclatura:** `[categoria]_[resumo-do-problema].md`

## 🗓️ Organização por Data

Os learnings são organizados em pastas com formato **DD-MM** (dia-mês):
- `20-10/` - Learnings de 20 de Outubro
- `15-10/` - Learnings de 15 de Outubro
- `15-01/` - Learnings de 15 de Janeiro

### ⚙️ Automação

Ao criar um novo learning:
1. **Obter data atual** no formato DD-MM
2. **Verificar se pasta existe**: `_context/learnings/DD-MM/`
3. **Criar pasta se não existir**: `mkdir -p _context/learnings/DD-MM/`
4. **Criar arquivo**: `_context/learnings/DD-MM/[categoria]_[resumo].md`
5. **Atualizar README.md** da pasta learnings com novo arquivo

### Exemplos de Nomenclatura (adapte conforme o contexto real):
- `airtable_time-conversion-bug.md` - Problema com conversão de tempo
- `react_component-rerender-issue.md` - Problema de re-renderização
- `typescript_generic-constraints.md` - Aprendizado sobre generics
- `backend_service-pattern-refactor.md` - Refatoração de padrão de service
- `ui_responsive-layout-solution.md` - Solução para layout responsivo
- `performance_query-optimization.md` - Otimização de queries
- `deployment_replit-build-fix.md` - Correção de build no Replit
- `integration_claude-api-limits.md` - Limites da API do Claude
- `database_migration-strategy.md` - Estratégia de migração
- `testing_mock-airtable-setup.md` - Setup de mocks para Airtable
- `security_env-variables-leak.md` - Vazamento de variáveis de ambiente
- `ux_loading-states-pattern.md` - Padrão para estados de loading

**Nota:** Estes são apenas exemplos ilustrativos. Crie arquivos de acordo com os problemas/aprendizados reais que surgirem no projeto. A nomenclatura deve refletir o contexto específico do que foi aprendido ou resolvido.

## 📝 Workflow Completo

1. **User solicita:** `/learning [descrição do problema]`
2. **Agent:**
   - Obtém data atual (exemplo: 20 de Outubro = `20-10`)
   - Verifica/cria pasta `_context/learnings/20-10/`
   - Cria arquivo `[categoria]_[resumo].md` dentro da pasta
   - Documenta: problema, solução, exemplos, checklist
   - Atualiza `_context/learnings/README.md` com novo learning

## 🔍 Consulta

Para consultar learnings:
- **Por data:** Navegue em `_context/learnings/DD-MM/`
- **Por categoria:** Veja `_context/learnings/README.md`
- **Mais recentes:** Pastas com DD-MM maiores são mais recentes
