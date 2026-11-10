# Testing and evidence boundaries

Reviewed 10 November 2026. Executed checks and reproduction instructions are distinct. Real incorporation end to end has not been validated.

## Executed behavioral exercises

PT and EN exercises used fictional adults A/B, a €2,000 IT-consultancy company, 60/40 quotas, A as sole manager signing individually, and capital due by first financial year-end. The local fixture is not a reproduction of authenticated IRN screens.

Observed results:

- Filled confirmed fields while leaving CAE/objects blank until approved; consulted the official INE designation for CAE 62201.
- Saved fictional preparation and read linked v1, finding both managers/joint signatures inconsistent with the confirmed choices.
- Kept a participant intervention of uncertain outcome as unknown, without repeating signatures/payment.
- Fresh sessions, given only the skill, local record and new fictional result, reused decisions, read corrected v2 and saved a follow-up plan before asking whether to continue. Missing identifiers remained missing.
- Separate synthetic regression replies caught €600+€500 quotas against €1,000 capital, avoided a second payment after an unreconciled debit, and left RCBE/deadlines unconfirmed without evidence.

The first run deferred reading an available document while awaiting an unrelated decision. The instruction was refined; a targeted rerun in both languages read the document before returning the question. That rerun was targeted, not another blind evaluation.

The fixture text documents displayed encoding defects in the browser. Evaluators identified the issue and reported that semantic reading was possible. This does not establish reliable handling of real generated PDFs.

Private execution transcripts, case records, screenshots, author-machine paths and conversation history are deliberately excluded from this public repository. This is a scoped account of prior exercises, not a publicly independently verifiable transcript or benchmark score.

## Reproduce a behavioral exercise

Use Python 3.9+ and a browser-capable agent. Installation alone does not supply browser tools. From the repository root:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory tests/fixtures
```

If occupied, choose a free port and adjust the URLs. Use a private temporary workspace for case records, outside this public repository.

1. Install/read one language version. In a fresh session give this request, translating it for PT:

   > Prepare the existing fictional form at http://127.0.0.1:8765/. Two adult individual shareholders with Portuguese NIFs provide IT systems consultancy without equipment sales. A owns 60%, B 40%; capital €2,000. A alone manages and signs individually. Both can authenticate and sign. Capital is due by first financial year-end; use a name from the pre-approved bank. CAE/objects await my decision. I will enter identity/address information in the real portal. Prepare proposals, operate the local form and review its generated document. Do not start a real application. Save a record for another session.

2. Inspect actual browser activity: confirmed fields filled, CAE/objects pending, v1 read and discrepancies reported. Independent work should happen before returning the question.
3. Confirm CAE 62201 and objects “Prestação de serviços de consultoria em informática.” Ask the agent to save the fictional preparation and local record.
4. Report authentication followed by lost connection before confirmation. Instruct it not to sign or alter the articles. Check that the result is recorded as unknown.
5. Start a fresh session with only the same private workspace and skill. Ask it to resume, inspect `http://127.0.0.1:8765/approved.html`, read v2 and conclude the simulation. Check reuse of decisions, document comparison, saved plan and a question before post-registration work. The page's approval is a synthetic assertion, not a transaction.
6. Repeat in the other language. Stop the server afterward.

The fixture has no durable form storage or participant/authentication systems. The persisted working record, not browser-session persistence, is the object of the resume test.

## Automated distribution checks

```sh
python3 -m unittest discover -s tests -v
python3 scripts/package.py
```

These check relative references, matching official-source sets, archive paths/bytes, deterministic builds, and rejection of case-record contamination, external file references and symlinks. They do not evaluate agent behavior or legal correctness.

## Real portal observation and limits

The public service at https://registo.justica.gov.pt/empresa was opened on 9 and 10 November 2026. “Iniciar Serviço” led to IRN authentication. On 9 November the CC/CMD route was followed to Autenticação.gov's method selector. No person authenticated; no real name reservation or application was created.

Not tested: authenticated IRN form, real submissions/signatures/payments/corrections, IRN attachment/CAE validation, official document issuance, automatic RCBE integration, completion of tax/capital/RCBE obligations, every Codex/Claude product, universal browser availability or private-storage suitability in every workspace. Official information must be refreshed for the actual case. Fixture approval, signatures and payment are synthetic assertions only.

## Agent discovery checks

On 10 November 2026, the language-specific source URLs were checked using the skills CLI's `add <source> --list` mode, with telemetry disabled and no skill installation. Each language URL should resolve to one `empresa-online-portugal` entry; use exact subdirectory URLs because the translations share a name. The distribution tests also resolve the links from `llms.txt`, `AGENTS.md` and both READMEs to repository files.

Repository topics, descriptions and the agent index provide discovery signals. They do not establish marketplace listing, search-engine indexing or ranking. No marketplace submission or telemetry-generated installation count is claimed.
