# Empresa Online Portugal — install and start

Updated 10 November 2026. Choose the Portuguese **or** English ZIP: both contain the same `empresa-online-portugal` skill. Do not install both languages simultaneously.

## Direct-source installation for agents

Choose the source URL for your language; both variants have the same skill name. Requires Node.js 22.20+. Append `--list` to discover without installing.

```sh
npx skills add https://github.com/hugo-alves/empresa-online-portugal/tree/main/skills/en/empresa-online-portugal
```

[CLI documentation](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

## Claude

In Claude open **Customize > Skills**, choose **+ > Create skill > Upload a skill** and upload the ZIP. Enable the skill. Availability depends on account capabilities and policies. [Official instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

For local Claude Code extract the `empresa-online-portugal` folder into `~/.claude/skills/` (personal) or the project's `.claude/skills/`. Keep `SKILL.md` and `references/` inside that folder. [Official documentation](https://code.claude.com/docs/en/skills).

## Codex

Extract the `empresa-online-portugal` folder into `~/.agents/skills/` (personal) or `.agents/skills/` in your working directory/project. Preserve its structure. Check that it appears in the skills selector; if it does not, start a new session. [Official documentation](https://learn.chatgpt.com/docs/build-skills).

## First request

> Use empresa-online-portugal to help me incorporate a company in Portugal. Operate the browser where possible, prepare field proposals and ask me for the missing decisions. Save a local working record so we can resume in another session.

The skill supplies instructions, not browser tools or portal access. Without direct browser control the assistant provides manual guidance. The person handles decisions, authentication, signatures and payment.

By default the case record is saved at `.empresa-online/<case>/registo.md` in a private workspace, outside the installed skill. To resume, use the same workspace and ask “Resume the saved case.” Do not include case records or personal documents in the ZIP you share. Another machine or cloud session needs private access to the record to resume; installing the skill alone does not transfer the case.

After approval the assistant saves a follow-up plan and asks whether to continue. The full authenticated real-world journey has not been validated; the documented tests use a local fictional form and documents.
