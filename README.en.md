# Empresa Online Portugal

[Português](README.md)

An agent skill for incorporating a Portuguese Lda. or single-member private limited company through **Empresa Online 2.0**.

The assistant prepares field proposals, operates available browser tools, reviews generated documents and follows the application. The person makes decisions and handles authentication, signatures and payment. After approval the assistant saves a follow-up plan and asks whether to continue.

## Install and start

Choose **Portuguese or English**. Both distributions use the identity `empresa-online-portugal`; install only one.

- [Installation in English](docs/install.en.md)
- [Instalação em português](docs/instalar.pt.md)
- Skill source: [Portuguese](skills/pt/empresa-online-portugal/SKILL.md) · [English](skills/en/empresa-online-portugal/SKILL.md)

To build installation ZIPs from source, run from the repository root:

```sh
python3 scripts/package.py
```

This creates `dist/empresa-online-portugal-pt.zip` and `dist/empresa-online-portugal-en.zip`, ready to install or attach to a release. No additional Python dependencies are required.

First request:

> Use empresa-online-portugal to help me incorporate a company in Portugal. Operate the browser where possible, prepare field proposals and ask me for the missing decisions. Save a local working record so we can resume in another session.

## Operation and privacy

The skill provides instructions, not browser tools, portal access or accounting services. Without direct control the assistant guides the person. Permissions and capabilities depend on the host environment.

A private case record defaults to `.empresa-online/<case>/registo.md` in a suitable workspace, outside the installed skill. Distribution ZIPs do not contain case records. Do not place personal documents, credentials or real applications in this repository. Installing the skill elsewhere does not transfer a case record.

## What was tested

Portuguese and English behavioral exercises used local fictional forms and documents: confirmed-only filling, pending proposals, articles discrepancies, file-based resumption in a fresh session and the post-registration scope boundary. A failure to complete independent work before asking a question was corrected and retested.

The actual public portal was observed through authentication entry. **Real incorporation end to end, digital signatures, payments and IRN submissions were not tested.** Fixtures do not reproduce authenticated portal screens. See [tests, reproduction and limits](docs/testing.md).

## Maintain and contribute

Official sources and review dates are in each language's references. The assistant must refresh applicable information for each live application. This is not an official IRN service and does not replace the person's decisions or necessary professional involvement.

Keep PT and EN equivalent, retain Portuguese field labels and exercise relevant changes. Run the structural distribution tests with:

```sh
python3 -m unittest discover -s tests -v
```

When reporting a problem include only the stage, a redacted message and expected behavior. Do not post NIFs, identity documents, bank receipts, access codes or session URLs in issues.

[MIT license](LICENSE). The license covers repository materials; linked official pages retain their own rights.
