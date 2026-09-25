---
name: vigiar-ci
description: Investiga falhas de CI em um Pull Request e comenta a causa provável. É disparada automaticamente por um GitHub Action quando o CI falha; também pode ser usada quando o usuário colar o log de uma falha de CI.
metadata:
  modo: autonoma
  intencao: Vigiar o PR e, quando o CI falha, comentar a causa provável sem intervenção humana.
---

# Vigiar CI (modo autônomo)

Roda sozinha quando o CI falha (gatilho em `.github/workflows/vigiar-ci.yml`).

## Passo a passo

1. Leia o log do job que falhou.
2. Identifique o **tipo** de falha:
   - teste quebrado
   - qualidade de código (por exemplo duplicação ou complexidade apontada pelo SonarCloud)
   - erro de formatação ou lint
   - erro de ambiente ou dependência
3. Aponte o arquivo e a linha mais prováveis, citando a mensagem do log.
4. Comente no PR com `gh pr comment`, neste formato:
   - **O que falhou:** uma frase.
   - **Causa provável:** uma ou duas frases.
   - **Sugestão de correção:** o próximo passo.
5. NÃO altere código e NÃO faça push. Apenas comente.

## Regras

- Se não tiver certeza, diga que é uma hipótese.
- Um comentário por falha. Não repita comentário se a causa for a mesma da anterior.
