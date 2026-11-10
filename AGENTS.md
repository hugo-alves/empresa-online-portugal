# Agent entry point

This repository supplies an Agent Skill for company incorporation in Portugal through Empresa Online 2.0. Search terms include criar empresa, abrir empresa, Lda., unipessoal, Portuguese company formation and business registration.

## Helping someone incorporate

Load the language-specific entry and its relative references:

- Portuguese (default for Portuguese requests): [skills/pt/empresa-online-portugal/SKILL.md](skills/pt/empresa-online-portugal/SKILL.md).
- English: [skills/en/empresa-online-portugal/SKILL.md](skills/en/empresa-online-portugal/SKILL.md).

These are translations with the same skill identity. Select one. Installation links are in [README.md](README.md); raw-file links are in [llms.txt](llms.txt). Read the skill rather than treating this routing file as the complete procedure.

The skill does not supply browser tools or grant portal authorization. Keep a person's case record in their private workspace, outside this public repository. Never use the fictional approval pages in tests as evidence of real incorporation.

## Maintaining this repository

Keep PT and EN behavior equivalent. Both variants use `name: empresa-online-portugal`; preserve language-specific installation URLs. Root discovery files are routing/index material, not a third installable skill.

Run relevant distribution checks with `python3 -m unittest discover -s tests -v`; rebuild ZIPs with `python3 scripts/package.py`. The tests do not prove real IRN incorporation. Preserve source review dates and the explicit distinction between public observations and synthetic exercises.
