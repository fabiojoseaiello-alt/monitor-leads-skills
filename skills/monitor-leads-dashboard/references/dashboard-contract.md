# Contrato do dashboard

## Payload público mínimo

```json
{
  "meta": {"client": "", "generated_at": "", "records": 0, "unique_contacts": 0, "unique_businesses": 0},
  "aggregates": {},
  "leads": [{
    "id": "opaco",
    "business_name": "",
    "segment": "",
    "volume_band": "",
    "estimated_units": null,
    "commercial_priority": "P3",
    "opportunity_score": 0,
    "priority_reasons": [],
    "attendance_state": "not_located",
    "handover_without_human": false,
    "cnae": {"main": "", "description": "", "icp_fit": "unknown"},
    "presence": {"maps": null, "site": null, "instagram": null, "linkedin": null},
    "conversation_summary": {"ai_messages": 0, "human_messages": 0, "vault_id": null}
  }]
}
```

## Prioridade comercial

Definir P0–P3 no `monitor.config.json`. Manter a fórmula e os motivos visíveis. Exemplo de score interno: qualificação/conversa da IA, faixa de volume, aderência CNAE, CNPJ ativo, Maps confirmado e presença digital. Não usar atendimento humano como prova de potencial; ele é uma dimensão operacional separada.

## Filtros obrigatórios

Segmento, volume, prioridade, CNAE, atendimento e busca. Maps/presença digital entram quando houver cobertura útil. Todo gráfico acionável deve aplicar o mesmo estado global de filtros.

## Estados vazios

Explicar o que não foi localizado e oferecer próxima ação. Não deixar traço isolado, bloco em branco ou mensagem que pareça dado definitivo.

