# Empresa Online Portugal — instalar e começar

Atualizado em 10 de novembro de 2026. Escolha o ZIP português **ou** inglês; ambos contêm a mesma skill `empresa-online-portugal`. Não instale as duas línguas em simultâneo.

## Instalação por URL para agentes

Escolha a URL da língua pretendida; o nome da skill é igual nas duas. Requer Node.js 22.20+. Acrescente `--list` para listar sem instalar.

```sh
npx skills add https://github.com/hugo-alves/empresa-online-portugal/tree/main/skills/pt/empresa-online-portugal
```

[CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

## Claude

Em Claude, abra **Customize > Skills**, escolha **+ > Create skill > Upload a skill** e carregue o ZIP. Ative a skill. A disponibilidade depende das capacidades e políticas da conta. [Instruções oficiais](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

Em Claude Code local, extraia a pasta `empresa-online-portugal` para `~/.claude/skills/` (pessoal) ou `.claude/skills/` no projeto. Preserve `SKILL.md` e `references/` dentro dessa pasta. [Documentação oficial](https://code.claude.com/docs/en/skills).

## Codex

Extraia a pasta `empresa-online-portugal` para `~/.agents/skills/` (pessoal) ou `.agents/skills/` na pasta de trabalho/projeto. Preserve a estrutura. Confirme que aparece no seletor de skills; se não aparecer, abra uma sessão nova. [Documentação oficial](https://learn.chatgpt.com/docs/build-skills).

## Primeiro pedido

> Usa a skill empresa-online-portugal para me ajudar a constituir uma empresa em Portugal. Opera o browser quando possível, prepara propostas para os campos e pede-me as decisões que faltarem. Guarda o registo local para podermos retomar noutra sessão.

A skill fornece instruções; não instala ferramentas de browser nem concede acesso ao portal. Sem controlo direto, o assistente orienta os passos manuais. A pessoa intervém em decisões, autenticação, assinaturas e pagamento.

O registo do caso fica por defeito em `.empresa-online/<caso>/registo.md` numa pasta de trabalho privada, fora da skill instalada. Para retomar, use a mesma pasta e peça «Retoma o caso guardado». Não inclua esses registos ou documentos pessoais no ZIP que partilhar. Outra máquina ou sessão cloud precisa de acesso privado ao registo para retomar; instalar a skill, por si só, não transfere o caso.

Após aprovação, o assistente guarda um plano de obrigações seguintes e pergunta se deve continuar. O percurso real completo após autenticação ainda não foi validado; os testes documentados usam um formulário e documentos fictícios locais.
