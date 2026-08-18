---
name: monitor-leads-maestro
description: Orquestra a criação e a atualização de monitores de inteligência de leads B2B a partir de planilhas, enriquecimento público, conversas de IA e atendimento humano no CRM. Use quando for replicar para um cliente o modelo Tropical Magic/Jundiá, criar um CRM leve com dashboard, auditar handover IA-humano, enriquecer CNPJ/Google Maps/site/redes ou publicar o monitor completo.
---

# Monitor de Leads — Maestro

Criar um projeto auditável e reutilizável, mantendo aquisição, enriquecimento, atendimento e visualização como dimensões separadas.

## Começar

1. Ler [references/workflow-contract.md](references/workflow-contract.md).
2. Identificar a pasta do cliente e preservar alterações existentes.
3. Se o projeto não existir, executar:

   ```powershell
   python scripts/bootstrap_monitor.py --client "Nome do cliente" --slug "cliente-monitor" --output "CAMINHO_DO_CLIENTE"
   ```

4. Preencher `monitor.config.json`. Guardar apenas nomes de variáveis de ambiente; nunca escrever tokens no arquivo.
5. Registrar cada etapa em `data/run-manifest.json`, inclusive falhas e cobertura parcial.

## Roteamento obrigatório

Executar as skills abaixo na ordem. Pular somente uma etapa comprovadamente fora do escopo e registrar o motivo no manifesto.

1. `$monitor-leads-ingestao`: importar, normalizar, preservar origem e deduplicar.
2. `$monitor-leads-enriquecimento`: consultar CNPJ, CNAE, Maps, site e presença digital com fonte e confiança.
3. `$monitor-leads-atendimento`: cruzar a conversa da IA com o atendimento humano posterior no CRM.
4. `$monitor-leads-dashboard`: construir o painel filtrável, os dossiês e as evidências.
5. `$monitor-leads-qa-publicacao`: verificar números, privacidade, interface, autenticação e deploy.

## Gates entre etapas

- Não enriquecer antes de existir `data/private/leads.ndjson` e relatório de ingestão.
- Não classificar atendimento usando status, e-mail ou “automação enviada” da planilha.
- Não afirmar ausência de Maps/site/rede; afirmar somente “não localizado automaticamente”.
- Não exibir conversa literal no payload público.
- Não publicar antes de `validate_monitor.py` retornar sucesso.
- Não escrever no CRM, criar tarefas ou mover etapas sem autorização explícita. Mudança de etapa exige confirmação específica por lead.

## Atualização de um monitor existente

Detectar a primeira etapa desatualizada pelo manifesto e reexecutar a partir dela. Reutilizar caches por chave estável. Reconstruir sempre os agregados e o payload público depois de qualquer alteração em fonte, regra, classificação ou layout.

## Conclusão

Entregar URL e forma de acesso, totais por entidade, cobertura das fontes, handovers sem humano, limitações, resultado do QA e deploy.

