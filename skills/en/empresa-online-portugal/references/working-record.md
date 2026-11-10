# Local working record

## Save and resume

Default to `.empresa-online/<case>/registo.md` in the private local task workspace. Use a neutral identifier such as `case-2026-11-10-01`, without NIFs or personal names in paths. Do not write inside the installed skill. In a Git repository create `.empresa-online/.gitignore` containing `*` to exclude records; never commit or bundle them for sharing. This prevents version tracking but does not make a shared folder private: in a public, third-party-synced or inappropriately accessible workspace, use an authorized private location. If saving is unavailable, explain the actual blocker without claiming persistence.

On startup look for a record here before asking again. If several cases exist ask only which to resume. Read decisions, evidence, documents and next action. Check current portal status; do not repeat the interview or treat historical status as current. Reuse recorded approvals within their scope, subject to host rules; material changes require review.

Update the same file after decisions, document changes, user interventions, portal outcomes and interruptions. Avoid a click log. Retain the minimum information needed to resume and private document paths, not PINs, temporary codes, session URLs or identity copies. Full identifiers belong only in private storage when indispensable; prefer local document references.

## Template

```markdown
# Case <identifier>
Updated: <date, time and timezone>
Stage: <verified status>
Application: <private reference if present; otherwise not started>
Latest evidence: <portal/document/user statement, dated>

## Worksheet
| Field | Value | Confirmed / proposed / missing | Source/date |
| --- | --- | --- | --- |

## Decisions and authorizations
| Decision/action | Approved content and scope | Who/when | Review needed? |
| --- | --- | --- | --- |

## Documents and tasks
| Document/task | Version/private path | Participant | Status/evidence |
| --- | --- | --- | --- |

## Pending items
| Task | What does it block? | Owner | Next action/deadline and trigger |
| --- | --- | --- | --- |

## Resume here
<Concrete next action; what can continue independently.>

## Post-registration plan
| Obligation | Triggering date | Deadline / unconfirmed | Owner | Evidence/status |
| --- | --- | --- | --- | --- |
Post-registration continuation authorized: <not requested / user's decision and scope>
```

Do not invent values to complete the template. After approval save the plan and ask whether to continue; until that decision, subsequent actions are planned rather than executed.
