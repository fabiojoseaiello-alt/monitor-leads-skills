# Monitor de Leads — Workflow de Skills

Workflow reutilizável para criar monitores de inteligência comercial a partir de planilhas, enriquecimento público, conversas da IA e atendimento humano no CRM.

O pacote generaliza o modelo aplicado em projetos como Tropical Magic e Jundiá sem incluir dados, credenciais ou identidade de nenhum cliente.

## Skills

| Skill | Responsabilidade |
|---|---|
| `monitor-leads-maestro` | Cria o projeto e orquestra as etapas |
| `monitor-leads-ingestao` | Importa, normaliza e deduplica a base |
| `monitor-leads-enriquecimento` | Pesquisa CNPJ, CNAE, Maps, site e redes |
| `monitor-leads-atendimento` | Cruza IA, lead e atendimento humano |
| `monitor-leads-dashboard` | Constrói o dashboard executivo filtrável |
| `monitor-leads-qa-publicacao` | Valida privacidade, interface e deploy |

## Instalação

### Windows

```powershell
git clone https://github.com/fabiojoseaiello-alt/monitor-leads-skills.git
cd monitor-leads-skills
.\install.ps1
```

### macOS/Linux

```bash
git clone https://github.com/fabiojoseaiello-alt/monitor-leads-skills.git
cd monitor-leads-skills
./install.sh
```

Reinicie a sessão do Codex depois da instalação para atualizar o catálogo de skills.

## Uso

Inicie pelo maestro:

```text
Use $monitor-leads-maestro para criar o monitor do cliente X usando a planilha Y,
Chatwoot como conversa da IA, Kommo como CRM e a identidade visual anexada.
```

O maestro executará:

```text
Ingestão → Enriquecimento → Atendimento → Dashboard → QA/Publicação
```

Cada etapa também pode ser chamada isoladamente para atualizar um monitor existente.

## Entradas esperadas

- Nome e slug do cliente.
- Planilha, CSV, XLSX ou fonte de CRM.
- Logo e referências da identidade visual.
- Critérios de qualificação, segmentos e faixas de volume.
- Plataforma de conversa da IA.
- CRM do atendimento humano.
- Credenciais fornecidas por variáveis de ambiente.
- Domínio desejado para publicação.

## Segurança

- Nunca grave tokens no `monitor.config.json`.
- Dados pessoais e conversas permanecem em `data/private/`.
- O payload público contém somente dados sanitizados e identificadores opacos.
- Conversas no dashboard exigem vault criptografado e autenticação server-side.
- O validador bloqueia publicação com placeholders, etapas incompletas ou indícios de dados privados.

## Utilitários

Criar um projeto:

```powershell
python skills/monitor-leads-maestro/scripts/bootstrap_monitor.py `
  --client "Cliente X" `
  --slug "cliente-x-monitor" `
  --output "C:\Projetos"
```

Validar antes de publicar:

```powershell
python skills/monitor-leads-maestro/scripts/validate_monitor.py "C:\Projetos\cliente-x-monitor"
```

