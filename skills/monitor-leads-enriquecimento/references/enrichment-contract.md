# Contrato de enriquecimento

## Ordem de confiança

1. CNPJ informado e matematicamente válido + cadastro oficial/público.
2. Nome e endereço/município coincidentes.
3. Nome + telefone/site coincidentes.
4. Nome semelhante sem localidade: candidato, nunca confirmado.

## Registro por coletor

```json
{
  "business_key": "...",
  "provider": "google_maps",
  "status": "confirmed",
  "collected_at": "ISO-8601",
  "source_url": "https://...",
  "confidence": 0.94,
  "match_reason": ["nome", "cidade", "endereço"],
  "data": {},
  "error": null
}
```

## Leitura comercial do CNAE

Guardar código e descrição oficial. Produzir `icp_fit` (`high`, `medium`, `low`, `unknown`) e `commercial_reading`, sempre rotulados como interpretação. Manter CNAEs secundários para descoberta de segmentos adjacentes.

