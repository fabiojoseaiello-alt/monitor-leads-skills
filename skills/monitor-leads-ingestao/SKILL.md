---
name: monitor-leads-ingestao
description: Importa, normaliza e deduplica bases de leads vindas de Google Sheets, CSV, XLSX ou CRM, preservando aba/linha de origem e separando registros, contatos e estabelecimentos. Use na criação ou atualização de um monitor de leads, antes de enriquecimento, auditoria de conversas ou dashboard.
---

# Monitor de Leads — Ingestão

Produzir uma base canônica rastreável sem alterar a fonte original.

## Executar

1. Ler `monitor.config.json` e [references/ingestion-schema.md](references/ingestion-schema.md).
2. Fazer snapshot da fonte com timestamp e hash. Não escrever na planilha.
3. Importar todas as abas configuradas; registrar aba e linha em cada registro.
4. Mapear cabeçalhos por significado, não apenas por grafia. Preservar `raw` para auditoria.
5. Normalizar CNPJ, telefone, e-mail, município/UF, quantidade e tipo de estabelecimento.
6. Validar matematicamente o CNPJ; não consultar CNPJ inválido.
7. Gerar `row_id`, `contact_key` e `business_key` conforme o contrato da skill maestra.
8. Deduplicar apenas para agregações. Manter todas as linhas e um `duplicate_group_id`.
9. Gravar `data/private/leads.ndjson` e `data/private/ingestion-report.json`.
10. Atualizar o estágio `ingestion` no manifesto.

## Regras

- Campo vazio não vira zero, falso ou “não”.
- Faixa de quantidade mantém texto original e valor estimado separado.
- Qualificação da planilha é sinal de origem, nunca evidência de atendimento.
- Não juntar contatos apenas por nome.
- Se telefone/e-mail conflitar entre linhas, registrar conflito; não escolher silenciosamente.

## Gate de saída

Conferir total por aba, total geral, contatos únicos, empresas únicas, CNPJs válidos/inválidos, duplicidades e campos críticos ausentes. A soma por aba deve fechar com a fonte.

