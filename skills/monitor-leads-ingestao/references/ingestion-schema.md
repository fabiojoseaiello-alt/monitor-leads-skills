# Schema canônico de ingestão

Campos mínimos por linha:

```json
{
  "row_id": "sha256-curto",
  "source": {"type": "google_sheets", "document": "...", "tab": "...", "row": 2, "snapshot_at": "ISO-8601"},
  "lead": {"name": "", "email": "", "phone": ""},
  "business": {"declared_name": "", "cnpj_raw": "", "cnpj": "", "cnpj_valid": false, "city": "", "state": ""},
  "qualification": {"source_value": "", "is_qualified": false, "segment": "", "volume_band": "", "estimated_units": null},
  "contact_key": "",
  "business_key": "",
  "duplicate_group_id": "",
  "raw": {}
}
```

Normalizar telefone em E.164 quando país for conhecido e manter o valor original. Normalizar CNPJ em 14 dígitos. Usar o centro da faixa somente para estimativa agregada e nunca substituir a faixa declarada.

