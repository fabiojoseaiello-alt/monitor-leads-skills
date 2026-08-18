# Contrato do workflow

## Princípio

O monitor cruza quatro fontes independentes: base declarada, cadastro/presença digital pública, conversa da IA e atendimento humano no CRM. Uma fonte nunca substitui outra. Toda conclusão deve manter `source`, `collected_at`, `confidence` e, quando aplicável, `match_reason`.

## Estrutura do projeto

```text
cliente-monitor/
├── monitor.config.json
├── index.html
├── logo.png
├── favicon.ico
├── vercel.json
├── api/
├── data/
│   ├── leads.json
│   ├── run-manifest.json
│   └── private/
│       ├── leads.ndjson
│       ├── ingestion-report.json
│       ├── enrichment/
│       ├── attendance/
│       └── conversations/
├── scripts/
└── qa/report.json
```

## Estado do manifesto

Cada estágio usa `pending`, `running`, `complete`, `partial` ou `failed`. Registrar início, fim, contagens de entrada/saída, erros, cobertura e arquivos produzidos.

## Identidades

- `row_id`: hash de fonte + aba + linha.
- `contact_key`: telefone normalizado, depois e-mail normalizado.
- `business_key`: CNPJ válido, depois nome normalizado + município/UF.
- Manter contagens de registros, contatos únicos e empresas únicas separadas.

## Dados públicos e privados

Privado: telefone, e-mail, mensagens, tokens, cookies e respostas brutas com dados pessoais. Público: identificadores opacos, segmento, faixa de volume, classificação, score, dados empresariais públicos, links públicos e agregados. Transcrições só por rota autenticada e vault criptografado.

## Definições de atendimento

- Ferramenta de conversa: IA + mensagens do lead.
- CRM: humano + mensagens do lead; remover réplicas da IA, bots e respostas automáticas.
- `qualified_at`: instante em que a IA registrou critérios suficientes.
- `human_after_handover`: primeira mensagem humana posterior a `qualified_at`.
- Ausência de mensagem no CRM após o handover gera alerta explícito.

## Dimensões separadas

- `commercial_priority`: P0–P3, oportunidade comercial.
- `attendance_state`: estado auditado do atendimento.
- `opportunity_score`: ranking interno, especialmente dentro de P0.
- `segment`, `volume_band`, `cnae_main`: filtros independentes.

## Critério de pronto

Um cliente está pronto quando os cinco estágios estão completos ou quando qualquer cobertura parcial está claramente exposta no painel e no relatório.

