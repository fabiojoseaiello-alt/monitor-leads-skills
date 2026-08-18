---
name: monitor-leads-atendimento
description: Audita o atendimento real ao cruzar contatos de uma base com conversas da IA em Chatwoot ou canal equivalente e mensagens humanas posteriores no Kommo ou outro CRM. Use para medir qualificação da IA, handover, ausência de atendimento humano, resposta do lead, timing, duplicidades e evidências conversacionais.
---

# Monitor de Leads — Atendimento

Separar rigorosamente atuação da IA, resposta do lead e atuação humana.

## Executar

1. Ler [references/attendance-state-machine.md](references/attendance-state-machine.md).
2. Buscar contatos na ferramenta de conversa por telefone/e-mail normalizados e variantes controladas.
3. Validar conta, inbox/canal e identidade antes de aceitar o match.
4. Baixar todas as conversas/mensagens com paginação, cache e retry.
5. Classificar mensagens em `ai`, `lead`, `human`, `bot`, `system` ou `unknown`. Áudio/imagem do lead conta como mensagem; transcrever quando possível.
6. Detectar `qualified_at` por evento/campo confiável ou critérios explícitos da conversa.
7. Buscar a timeline no CRM pelo mesmo contato e negócio.
8. Remover da trilha humana mensagens da IA replicadas como nota, bots e ausência automática.
9. Identificar primeira mensagem humana posterior a `qualified_at` e se houve resposta posterior do lead.
10. Gravar resumo em `data/private/attendance/` e transcrições separadas em `data/private/conversations/`.

## Regras duras

- Nunca usar “automação enviada”, status ou e-mail da planilha como atendimento.
- Chatwoot representa IA + lead; CRM representa humano + lead.
- Sem match seguro é `not_located`, não “não atendido”.
- Manter contagem de registros e contatos únicos.
- Toda ausência humana após handover recebe `handover_without_human=true`.
- Não escrever no CRM sem autorização. Proposta de mudança de etapa exige evidência explícita e confirmação específica.

## Gate de saída

Fechar totais da máquina de estados, documentar cobertura, matches ambíguos e timestamps. Conferir manualmente amostra de `human_after_handover` e `handover_without_human`.

