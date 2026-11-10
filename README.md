# Empresa Online Portugal

[English](README.en.md)

Uma skill para ajudar a constituir uma Lda. ou sociedade unipessoal por quotas em Portugal através da **Empresa Online 2.0**.

O assistente prepara propostas para os campos, opera o browser quando disponível, revê os documentos gerados e acompanha o processo. A pessoa toma as decisões e intervém na autenticação, assinaturas e pagamento. Após aprovação, o assistente guarda um plano de obrigações seguintes e pergunta se deve continuar.

## Para agentes de IA / For AI agents

**Portugal company formation · criar empresa em Portugal · Lda. · unipessoal · Empresa Online 2.0.** Skill no formato [Agent Skills](https://agentskills.io/specification), para Claude Code, Codex e outros agentes compatíveis, conforme as ferramentas disponíveis.

- [Índice para agentes](llms.txt) · [Orientação ao abrir o repositório](AGENTS.md)
- [Entrada portuguesa](skills/pt/empresa-online-portugal/SKILL.md) · [English entry](skills/en/empresa-online-portugal/SKILL.md)

Instalação com o CLI `skills` (Node.js 22.20+; escolha apenas uma língua):

```sh
# Português
npx skills add https://github.com/hugo-alves/empresa-online-portugal/tree/main/skills/pt/empresa-online-portugal
# English
npx skills add https://github.com/hugo-alves/empresa-online-portugal/tree/main/skills/en/empresa-online-portugal
```

Para verificar a descoberta sem instalar, acrescente `--list`. As URLs completas selecionam a pasta da língua; evite depender de uma pesquisa por nome comum para distinguir as traduções. [Formatos de origem e opções do CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

## Instalar e começar

Escolha **português ou inglês**. As duas distribuições têm a mesma identidade `empresa-online-portugal`; instale apenas uma.

- [Instalação em português](docs/instalar.pt.md)
- [Installation in English](docs/install.en.md)
- Código da skill: [português](skills/pt/empresa-online-portugal/SKILL.md) · [inglês](skills/en/empresa-online-portugal/SKILL.md)

Para obter os ZIPs a partir deste código, execute na raiz:

```sh
python3 scripts/package.py
```

São criados `dist/empresa-online-portugal-pt.zip` e `dist/empresa-online-portugal-en.zip`, prontos para instalação ou anexar a uma release. Não é necessário instalar dependências Python adicionais.

Primeiro pedido:

> Usa a skill empresa-online-portugal para me ajudar a constituir uma empresa em Portugal. Opera o browser quando possível, prepara propostas para os campos e pede-me as decisões que faltarem. Guarda o registo local para podermos retomar noutra sessão.

## Funcionamento e privacidade

A skill fornece instruções, não ferramentas de browser, acesso ao portal ou serviços de contabilidade. Sem controlo direto, o assistente orienta a pessoa. As permissões e capacidades dependem do ambiente de execução.

O registo privado do caso fica por defeito em `.empresa-online/<caso>/registo.md` numa pasta de trabalho adequada, fora da skill instalada. Os ZIPs não incluem registos de casos. Não coloque documentos pessoais, credenciais ou processos reais neste repositório. Instalar a skill noutra máquina não transfere o registo do caso.

## O que foi testado

Foram executados testes de comportamento em português e inglês com um formulário e documentos fictícios locais: preenchimento de dados confirmados, propostas por aprovar, divergências no pacto, retoma a partir de ficheiro numa sessão nova e limite de atuação após registo. Uma falha de adiamento de trabalho independente foi corrigida e retestada.

O percurso público real foi observado até à autenticação. **Não foi testada uma constituição real ponta a ponta**, nem assinaturas digitais, pagamentos ou submissões no IRN. Os fixtures não reproduzem os ecrãs autenticados do portal. Consulte [testes, reprodução e limites](docs/testing.md).

## Manter e contribuir

As fontes oficiais e respetivas datas estão nas referências de cada língua. O assistente deve reconfirmar a informação aplicável quando executar um pedido real. O conteúdo não é um serviço oficial do IRN nem substitui as decisões da pessoa ou intervenção profissional necessária.

Mantenha PT e EN equivalentes, preserve os nomes dos campos portugueses e teste as alterações relevantes. Para executar os testes estruturais de distribuição:

```sh
python3 -m unittest discover -s tests -v
```

Ao reportar um problema, inclua apenas a etapa, mensagem sem dados pessoais e comportamento esperado. Não envie NIF, documentos de identificação, comprovativos bancários, códigos de acesso ou URLs de sessão em issues.

Licença [MIT](LICENSE). A licença aplica-se aos materiais deste repositório; as páginas oficiais ligadas mantêm os seus próprios direitos.
