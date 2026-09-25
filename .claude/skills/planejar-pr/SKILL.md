---
name: planejar-pr
description: Planeja um Pull Request ANTES de qualquer código, fazendo perguntas ao usuário sobre escopo, arquivos afetados e critério de pronto. Use sempre que o usuário disser que vai começar uma funcionalidade, abrir um PR, "planejar", "por onde começo" ou "o que preciso mexer", mesmo que não peça um plano explicitamente.
metadata:
  modo: interativa
  intencao: Alinhar escopo, arquivos afetados e critério de pronto com o usuário antes de escrever código.
---

# Planejar PR (modo interativo)

Esta skill conversa com o usuário. Ela NÃO escreve código nem altera arquivos.

## Passo a passo

1. Leia a issue ou a descrição da tarefa que o usuário indicar.
2. Pergunte, uma pergunta de cada vez, esperando a resposta:
   - **Escopo:** o que entra neste PR e o que fica de fora?
   - **Arquivos afetados:** quais migrations, serviços, telas e testes provavelmente mudam?
   - **Critério de pronto:** como saberemos que terminou? (testes passando, documentação, revisão)
3. Se a tarefa for grande, proponha dividir em etapas pequenas, cada uma com seu critério de pronto.
4. Ao final, devolva um plano curto com: escopo, lista de arquivos, critério de pronto e riscos.
5. Peça confirmação do usuário. Só depois disso a implementação pode começar.

## Regras

- Nunca assuma respostas. Se faltar informação, pergunte.
- Use linguagem simples.
- Não crie nem edite arquivos de código nesta skill.
