# Máquina de estados de atendimento

Aplicar na ordem:

1. `human_after_ai_qualification`: IA qualificou e existe mensagem humana posterior.
2. `ai_qualified_without_human`: IA qualificou e não existe mensagem humana posterior.
3. `ai_conversation`: IA enviou e o lead respondeu.
4. `ai_outreach_no_reply`: IA enviou e o lead não respondeu.
5. `conversation_match_no_outbound`: contato conciliado, sem saída auditável.
6. `not_located`: nenhum match seguro na ferramenta de conversa.

Campos mínimos:

```json
{
  "row_id": "...",
  "contact_key": "...",
  "conversation_match": {"status": "confirmed", "conversation_ids": [], "confidence": 1.0},
  "ai": {"outbound_count": 0, "lead_reply_count": 0, "qualified": false, "qualified_at": null},
  "human": {"message_count": 0, "first_after_handover_at": null, "lead_replied_after_human": false},
  "attendance_state": "not_located",
  "handover_without_human": false
}
```

Para apresentar conversas no dashboard, gerar vault criptografado e rota autenticada. O payload público recebe somente contagens, estados e identificadores opacos.

