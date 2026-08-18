---
name: monitor-leads-qa-publicacao
description: Valida e publica monitores de leads, conferindo integridade dos dados, privacidade, autenticação, proteção das conversas, filtros, responsividade, favicon, links e deploy Vercel. Use antes de entregar um monitor novo, após atualização de dados ou depois de ajustes no dashboard.
---

# Monitor de Leads — QA e Publicação

Bloquear a entrega quando números, privacidade ou interface não estiverem confiáveis.

## Validar dados

1. Ler [references/qa-checklist.md](references/qa-checklist.md).
2. Executar o validador da skill maestra:

   ```powershell
   python CAMINHO_DA_SKILL/scripts/validate_monitor.py CAMINHO_DO_PROJETO
   ```

3. Reconciliar total por aba, total geral, contatos únicos e estabelecimentos únicos.
4. Confirmar que a soma da máquina de atendimento fecha com o universo aplicável.
5. Comparar agregados do JSON com contagem recalculada dos leads.

## Validar segurança

- Procurar tokens, cookies, e-mails, telefones e mensagens literais no bundle publicado.
- Confirmar `data/private` e scripts no `.vercelignore`.
- Exigir autenticação server-side para a rota de conversas.
- Testar acesso direto ao vault/arquivos brutos; deve falhar.
- Usar variável de ambiente para chave de criptografia e segredo de sessão.

## Validar interface

Abrir o dashboard em navegador real. Testar login, filtros isolados/combinados, limpeza, ordenação P0, CNAE, alertas de handover, estados vazios, scroll das conversas, exportação, links, desktop e mobile.

## Publicar

1. Executar deploy de produção no projeto configurado.
2. Configurar o domínio/alias solicitado.
3. Se a Vercel adicionar proteção própria inesperada, corrigir sem remover o login interno requerido.
4. Validar no domínio final: HTTP 200, título, favicon/MIME, payload, autenticação e rota de conversas.
5. Registrar deployment ID, domínio, horário, hash do payload e resultado em `qa/report.json` e no manifesto.

## Entregar

Informar URL, senha ou forma de acesso, data do snapshot, cobertura parcial e principais limitações. Nunca enviar token ou chave de criptografia.

