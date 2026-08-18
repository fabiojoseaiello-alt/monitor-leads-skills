---
name: monitor-leads-dashboard
description: Constrói ou adapta um dashboard executivo de inteligência de leads com identidade visual do cliente, filtros combináveis, clusters, CNAEs, prioridade comercial, evidência de atendimento IA-humano, dossiês e exportação. Use quando os dados do monitor já estiverem consolidados ou quando o painel precisar de ajustes visuais e funcionais.
---

# Monitor de Leads — Dashboard

Transformar a auditoria em uma ferramenta operacional, não em uma vitrine de métricas.

## Preparar

1. Ler [references/dashboard-contract.md](references/dashboard-contract.md).
2. Inspecionar logo, paleta e referência visual do cliente.
3. Definir uma direção visual coerente com a marca. Evitar aparência genérica de template.
4. Gerar `data/leads.json` sanitizado a partir dos artefatos privados.

## Construir

Usar a ordem visual:

1. Gate/autenticação e header de marca.
2. KPIs executivos com distinção entre registros, contatos e estabelecimentos.
3. Clusters de tipo × volume e filtros de prioridade.
4. Ranking de CNAE principal logo após os clusters, clicável e explicativo.
5. Evidência de atendimento IA × humano com gráfico acionável.
6. Base de leads ordenada por `commercial_priority` e `opportunity_score`.
7. Dossiê do lead com cadastro, CNAE, Maps, site, redes e conversas roláveis.

## Interação

- Sincronizar filtros de segmento, volume, P0–P3, CNAE, atendimento, Maps e busca textual.
- Recalcular KPIs, gráficos, ranking e lista com o mesmo recorte.
- Mostrar filtros ativos e ação clara para limpar.
- Dentro de P0, exibir primeiro os maiores scores e explicar por que são prioritários.
- Abrir conversa da IA e conversa humana lado a lado. Se não houver humano após handover, usar alerta destacado.
- Para Maps não confirmado, mostrar “Google Maps não encontrado” e botão de busca manual bem encaixado.

## Identidade e acessibilidade

- Usar variáveis CSS para marca e status; não codificar cores repetidas nos componentes.
- Preservar semântica: vermelho crítico, âmbar atenção, verde atendido, neutro não localizado.
- Criar favicon quadrado a partir da marca e declarar PNG/ICO/apple-touch-icon.
- Garantir contraste, navegação por teclado, estados de foco e responsividade real.
- Manter gráficos legíveis em tela inteira; evitar porcentagens minúsculas.

## Segurança

Gate client-side é apenas barreira visual. Conversas e dados pessoais exigem autenticação server-side; manter transcrições fora de `data/leads.json`.

## Gate de saída

Testar desktop e mobile, todos os filtros combinados, estados vazios, scroll das conversas, exportação, links e contagens. Atualizar o manifesto somente depois do QA local.

