---
name: fechar-pr
description: Fecha um Pull Request quando o usuário pede explicitamente (por exemplo "/fechar-pr" ou "feche o PR"). Roda os testes, atualiza a documentação e abre o PR, sem fazer perguntas.
disable-model-invocation: true
metadata:
  modo: reativa
  intencao: Executar o fechamento do PR (testes, documentação, abertura) quando o usuário a chama, sem perguntar nada.
---

# Fechar PR (modo reativo)

Esta skill só roda quando o usuário a chama. Ela executa tudo de uma vez, sem pedir confirmação.

## Passo a passo

1. Rode a suíte de testes do projeto (por exemplo `composer test` ou o comando indicado no README).
   - Se algum teste falhar: pare, mostre quais falharam e NÃO abra o PR.
2. Atualize a documentação afetada pelas mudanças (README, SPEC, comentários de uso).
3. Confira o que mudou com `git status` e `git diff --stat`.
4. Faça o commit final com mensagem clara.
5. Abra o PR com `gh pr create`, usando:
   - **Título:** curto, descrevendo a funcionalidade.
   - **Descrição:** o que foi feito, como testar, resultado dos testes.
6. Mostre o link do PR ao usuário.

## Regras

- Não pergunte nada durante a execução. Se algo impedir (teste falhando, conflito), pare e explique o motivo.
- Nunca faça push forçado (`--force`).
