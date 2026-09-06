# SEBI Compliance Research

**Skill version:** 2.0.0  
**Author:** DK Mendiratta  
**GitHub:** [d33pm3/SEBI-Compliance-Research](https://github.com/d33pm3/SEBI-Compliance-Research)

Source-first research skill for mapping SEBI, NSE/BSE, and selected Companies Act obligations of Indian listed companies. Method, coverage controls, and evals only — no registers, no client data.

## This is / this is not

**This is**

- A reusable six-phase **AI research skill** (`SKILL.md`) plus reference files and evaluation cases.
- A method for building a **traceable 12-column compliance register** from live primary sources.
- A coverage-and-quality control pack: 19-category MECE checklist, known-omission tripwires, seven pre-delivery gates.

**This is not**

- Legal, regulatory, tax, or investment advice.
- A SEBI circular archive, scraper, monitor, or dataset.
- A filled-in Excel register you can download and file from.
- A substitute for a Company Secretary, compliance officer, or qualified counsel.

Stored URLs in this repository are **discovery seeds**. They are not proof that a rule is current.

## Why this exists (the problem it solves)

Ad-hoc web research and unconstrained AI runs on Indian listed-company compliance fail in predictable ways:

1. They cite a stale consolidated regulation instead of the version on SEBI’s listing page today.
2. They treat law-firm blogs as primary sources.
3. They build coverage from whatever search returns, not from a checklist constructed before searching.
4. They read snippets instead of full regulations and schedules.
5. They skip the last-12-month amendment sweep.
6. They treat NSE/BSE compliance calendars as secondary. Those calendars contain listing-condition items that appear in no SEBI document.
7. They have no domain omission tripwires, so the same filings are missed every time.

An early register produced without these controls **missed 18 filings and contained 5 errors**. This repository exists so the next run is planned, source-first, MECE-complete, exchange-reconciled, and gated before delivery.

## Who it is for

- Company Secretaries and listed-company compliance teams who need a filing register or calendar that can be audited to primary URLs.
- Compliance heads and GRC advisors who must map LODR / PIT / SAST / ICDR / NCS / buyback / delisting / SBEB plus exchange calendars.
- AI-agent builders who want a skill file they can load, evaluate, and run against live web retrieval — not a hallucinated obligation list.

**Not for:** extracting obligations from an uploaded regulatory PDF as the sole source of truth, or analysing a court or tribunal judgment. Those are different workflows. This skill may still supply the MECE checklist and omission tripwires as a completeness audit.

## Required capabilities

To **run the research** (not merely read the method) the host environment must provide:

- Live web search.
- Full-page retrieval of official pages and linked PDFs on `sebi.gov.in`, `nseindia.com`, `bseindia.com`, and `mca.gov.in`.

Optional: a crawler that can extract JavaScript-rendered listing pages. If a primary page cannot be fetched, the skill records the row as `UNVERIFIED`. It must not silently substitute a blog.

Validating the repository files only needs Python 3. It does **not** run the research.

## Who should do what

| You want to… | Do this |
|---|---|
| Understand the method without an agent | Read this README, then `SKILL.md` Parts 0–2 and Phases 1–6, then the four files in `references/` in the order given below. Stop there. Do not treat seed URLs as current law. |
| Run the research | Install or load the skill (next section), confirm live web search + page fetch are available, then use the prompt in **Run the research**. |
| Check that the public tree is intact | `python3 scripts/validate_repo.py` |

## Install / load the skill

Clone the public tree:

```bash
git clone https://github.com/d33pm3/SEBI-Compliance-Research.git
cd SEBI-Compliance-Research
```

Keep this layout together. `SKILL.md` is the entry point. Phase files live under `references/`. Do not load `SKILL.md` alone and expect the checklists to be in context.

**Copy the skill into a skill-compatible host** (create the folder if it does not exist):

```text
sebi-india-compliance-research/
├── SKILL.md
├── references/
│   ├── canonical_sources.md
│   ├── known_omissions.md
│   ├── mece_checklist.md
│   └── output_standards.md
└── evals/
    ├── evals.json
    └── trigger-evals.json
```

Typical drop paths (names vary by product version; use the host’s current skills directory):

- **Claude Skills / Claude Code:** project or user `skills/sebi-india-compliance-research/`
- **Cursor:** `.cursor/skills/sebi-india-compliance-research/` or the project skills folder
- **Grok custom skills:** the configured custom-skills directory, or paste/load `SKILL.md` and open the matching `references/` file when the phase says to
- **Other skill hosts:** any folder the product indexes as a skill, with `SKILL.md` at the root of that folder

Then open a new agent session so the host re-indexes skills.

Viewing on GitHub does not load the skill into an agent. Cloning or copying the files does not grant a copyright license to reuse the materials in a product. See **View vs use**.

## Run the research

1. Confirm the session can search the web and fetch full pages.
2. Load this skill (`SKILL.md`).
3. Fix entity scope before the first fetch: equity-listed / debt-listed / HVDLE / SME / market-cap tier, and the deliverable (register, calendar, gap analysis, or memo).
4. Paste a prompt like the following.

```text
Use the sebi-india-compliance-research skill.

Entity: NSE + BSE equity-listed company, Top 500 by market cap.
Deliverable: 12-column SEBI / NSE / BSE compliance register in Markdown, then XLSX if the environment can write files.

Execute Phases 1–6 in order.
- Phase 1: populate the Canonical Source Table from live listing pages. Seed URLs are search targets only.
- Phase 2: Tier 1 regulator sources, then independent NSE and BSE calendar passes.
- Phase 3: map all 19 MECE categories before broad search.
- Phase 4: audit against known-omission tripwires.
- Phase 5: every row uses the locked 12-column schema.
- Phase 6: run all seven gates. Label each legal value FETCHED or UNVERIFIED.

Do not cite law-firm blogs as Source URL. Do not invent timelines. If a primary page cannot be fetched, mark the row UNVERIFIED and list the URL I should open.
```

5. When the skill names a phase reference, open only that file (`references/canonical_sources.md`, `mece_checklist.md`, `known_omissions.md`, or `output_standards.md`).
6. Treat the output as a research draft. Re-fetch primary sources before operational use. Have a CS or counsel review it.

Repository structure checks (not research):

```bash
python3 scripts/validate_repo.py
```

## Sample 12-column output (illustrative only)

The table below shows the **shape** of the deliverable. Values are **not** current law. Do not copy them into a live register. Every operational row must be re-read from a primary URL fetched in that session.

| S.No. | Category | Filing / Disclosure Name | Regulation Reference | Applicable To | Filing Authority | Frequency | Trigger / Event | Timeline from Trigger | Format / Mode | Penalty for Non-Compliance | Source URL |
| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Financial results | Quarterly financial results | LODR Reg 33(3)(a) | Equity-listed | NSE / BSE | Quarterly | End of each quarter | Outer bound from the fetched consolidated text | XBRL + PDF as specified by the exchange | Exact provision from the fetched text | Live `sebi.gov.in` URL fetched this session |
| 2 | Board / committee | Outcome of board meeting | LODR Reg 30 read with Schedule III | Equity-listed | NSE / BSE | Event-driven | Board decides specified matters | Dual branch: during vs after market hours, as fetched | Exchange portal + PDF | Exact provision from the fetched text | Live `sebi.gov.in` URL fetched this session |
| 3 | Insider trading | Initial disclosure by designated person | PIT Reg 7(1) | Listed company + designated persons | Company / stock exchanges as fetched | One-time / event-driven | Becoming a designated person / joining | Trading-day outer bound from the fetched PIT text (do not use blog timelines) | Prescribed form as fetched | Exact provision from the fetched text | Live `sebi.gov.in` URL fetched this session |
| 4 | Exchange calendar item | Item that appears on the NSE or BSE compliance calendar | Listing condition / circular cited on the calendar | As stated on that calendar row | NSE or BSE | As per calendar | As per calendar | As per calendar, then reconciled to the SEBI instrument | As per calendar | As fetched | Live `nseindia.com` or `bseindia.com` URL fetched this session |

Verification labels used in a real run: **FETCHED** (read from a primary page this session) or **UNVERIFIED** (fetch failed or not yet read). Skill-file text is never a citable legal source.

## What the method does

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
├── LICENSE                         # Viewable-source proprietary terms
├── SECURITY.md                     # Vulnerability and data-exposure reporting
└── SKILL.md                        # Skill entry point and six-phase workflow
```

Reading order if you are not running an agent:

1. This README  
2. `SKILL.md` (Parts 0–2, then Phases 1–6)  
3. At Phase 1: `references/canonical_sources.md`  
4. At Phase 3: `references/mece_checklist.md`  
5. At Phase 4: `references/known_omissions.md`  
6. Before delivery: `references/output_standards.md`

## Scope and limitations

This project supports regulatory research. It does not provide legal advice and does not replace review by qualified legal or compliance professionals. Regulations, circulars, exchange requirements, and enforcement positions change. Any operational use must re-fetch and validate primary sources during the current research session.

The repository contains the research method, coverage controls, source-discovery starting points, and evaluation cases. It intentionally contains no regulatory source documents, client data, credentials, vector stores, embeddings, generated registers, or internal reports.

## Security and privacy

Do not commit confidential documents, customer or client information, audit findings, credentials, private prompts, RAG corpora, vector-store exports, embeddings, or production configuration. See `SECURITY.md` and `.gitignore`.

## View vs use (plain-language license)

**Viewing is allowed. Using is not a granted right.**

- You may open this public repository and read the files.
- Public visibility is not an open-source license.
- You may not copy, modify, distribute, sublicense, sell, or commercially use the contents unless DK Mendiratta has given prior written permission, or applicable law already allows that act.
- Materials are provided “as is”, without warranties. You remain responsible for verifying current primary sources and obtaining professional review.

The governing text is in `LICENSE`.

## GitHub About box (sidebar)

Use these values on the repository About form so search cards match this README:

- **Description:** Source-first research skill for mapping SEBI, NSE/BSE and selected Companies Act obligations of Indian listed companies. Method, coverage controls and evals only — no registers, no client data.
- **Topics:** `sebi` `lodr` `compliance` `india` `grc` `nse` `bse` `listed-companies` `ai-skills` `regulatory-mapping`
- **Website:** leave empty unless a project site is published.
- **License:** proprietary (see `LICENSE`; GitHub will show “Other”).
