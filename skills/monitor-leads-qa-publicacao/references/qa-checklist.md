# Checklist de QA

## Dados

- [ ] Total por fonte/aba fecha com a origem.
- [ ] Registros, contatos e estabelecimentos não são misturados.
- [ ] CNPJ válido foi validado matematicamente.
- [ ] Agregados fecham com a lista filtrável.
- [ ] Máquina de atendimento é mutuamente exclusiva.
- [ ] Cobertura e erros de coletores estão visíveis.

## Segurança

- [ ] Nenhum segredo no código ou JSON público.
- [ ] Nenhum telefone/e-mail/mensagem literal no payload público.
- [ ] `data/private` excluído do deploy.
- [ ] Vault criptografado e servido apenas após autenticação.
- [ ] Cookies de sessão `HttpOnly`, `Secure` em produção e `SameSite` adequado.
- [ ] Cache desabilitado para dados sensíveis.

## Interface

- [ ] Filtros sincronizam KPIs, gráficos e cards.
- [ ] P0 ordenado por score decrescente.
- [ ] CNAE clicável, descrito e filtrável.
- [ ] Handover sem humano possui alerta.
- [ ] Conversas são roláveis e têm estado vazio explícito.
- [ ] Maps ausente mostra mensagem e busca manual.
- [ ] Favicon, logo e paleta pertencem ao cliente.
- [ ] Desktop e mobile sem overflow indesejado.

## Produção

- [ ] Domínio final responde 200 sem login inesperado do provedor.
- [ ] Login interno funciona.
- [ ] Favicon responde com MIME de imagem.
- [ ] Rotas privadas rejeitam sessão inválida.
- [ ] `qa/report.json` registra deploy e hash do snapshot.

