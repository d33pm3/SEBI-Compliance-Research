# SEBI Compliance Research

A reusable, source-first research skill for mapping regulatory obligations of Indian
listed entities across SEBI regulations, NSE/BSE requirements, and selected Companies
Act obligations.

The repository contains the research method, coverage controls, source-discovery
starting points, and evaluation cases. It intentionally contains no regulatory source
documents, client data, credentials, vector stores, embeddings, generated registers,
or internal reports.

## What it does

- Verifies current consolidated regulations and recent amendments before extraction.
- Builds coverage from a 19-category MECE checklist rather than search-result recall.
- Reconciles SEBI-derived obligations against NSE and BSE compliance calendars.
- Produces traceable 12-column compliance registers with explicit verification status.
- Applies known-omission tripwires and seven pre-delivery quality gates.

## Repository structure

```text
.
├── .github/workflows/validate.yml  # Structural and safety checks
├── evals/
│   ├── evals.json                  # Output-behaviour evaluations
│   └── trigger-evals.json          # Invocation-routing evaluations
├── references/
│   ├── canonical_sources.md        # Primary-source discovery starting points
│   ├── known_omissions.md          # Historical omission tripwires
│   ├── mece_checklist.md           # Coverage model
│   └── output_standards.md         # Register and delivery requirements
├── scripts/validate_repo.py        # Local validation entry point
├── .gitignore                      # Public-repository exclusion controls
├── LICENSE                         # Source-visible proprietary terms
├── SECURITY.md                     # Vulnerability and data-exposure reporting
└── SKILL.md                        # Skill entry point and six-phase workflow
```

## Use

Load `SKILL.md` in a skill-compatible AI environment. When the task reaches a routed
phase, read only the reference file named for that phase. The workflow requires live
web retrieval: stored URLs are discovery seeds, never proof that a rule is current.

Run repository checks locally with:

```bash
python3 scripts/validate_repo.py
```

## Scope and limitations

This project supports regulatory research; it does not provide legal advice and does
not replace review by qualified legal or compliance professionals. Regulations,
circulars, exchange requirements, and enforcement positions change. Any operational
use must re-fetch and validate primary sources during the current research session.

## Security and privacy

Do not commit confidential documents, customer or client information, audit findings,
credentials, private prompts, RAG corpora, vector-store exports, embeddings, or
production configuration. See `SECURITY.md` and `.gitignore`.

## License

The repository is publicly viewable but is not offered under an open-source license.
See `LICENSE` for the governing terms.
