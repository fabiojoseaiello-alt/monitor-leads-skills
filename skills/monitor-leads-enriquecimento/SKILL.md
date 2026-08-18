---
name: monitor-leads-enriquecimento
description: Enriquece estabelecimentos de uma base de leads com dados públicos de CNPJ, CNAE, Google Maps/Google Business Profile, site, LinkedIn, Instagram e outros sinais digitais, usando APIs públicas, Playwright, Firecrawl ou Apify com cache, fonte e confiança. Use após a ingestão ou quando a pesquisa pública de um monitor precisar ser refeita.
---

# Monitor de Leads — Enriquecimento

Encontrar sinais públicos verificáveis sem transformar candidatos ambíguos em fatos.

## Executar

1. Ler `data/private/leads.ndjson` e [references/enrichment-contract.md](references/enrichment-contract.md).
2. Criar fila por `business_key`, priorizando qualificados e estabelecimentos com CNPJ/nome.
3. Para CNPJ válido, consultar fonte pública primária; usar fallbacks somente com registro de origem.
4. Extrair situação, razão social, nome fantasia, endereço, CNAE principal/secundários e descrições oficiais.
5. Buscar Google Maps por combinações de nome, cidade, bairro, CEP e endereço. Usar Playwright/serviço compatível e salvar candidatos.
6. Confirmar perfil somente quando identidade e localidade atingirem o limiar configurado.
7. Capturar URL compartilhável, categoria, endereço, telefone público, site, nota, avaliações e Plus Code quando disponíveis.
8. Buscar site, LinkedIn e Instagram. Visitar site para descrição, schema.org, contatos públicos e links sociais.
9. Usar Firecrawl/Apify quando disponível; manter fallback por HTTP/navegador e cache retomável.
10. Gravar NDJSON separado por coletor em `data/private/enrichment/`.

## Regras

- Toda evidência leva `source_url`, `collected_at`, `confidence`, `match_reason` e `status`.
- `confirmed`, `candidate`, `not_found` e `error` são estados distintos.
- Resultado ausente significa “não localizado automaticamente”, não “não existe”.
- CNAE indica aderência cadastral; não prova intenção, volume ou operação atual.
- Não raspar áreas autenticadas, burlar bloqueios ou coletar dado pessoal desnecessário.
- Respeitar rate limit, termos aplicáveis, retry com backoff e cache.

## Gate de saída

Reportar cobertura por fonte e estado, erros, candidatos ambíguos e data do cache. Amostrar manualmente confirmações de alta prioridade antes de liberar o dashboard.

