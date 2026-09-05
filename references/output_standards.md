# Output Standards & Deliverable Assembly — SEBI India Compliance Research v2.0
*Read at delivery time, before assembling the final file(s).*

## Output Standards

All SEBI compliance registers produced with this skill conform to:

- **Colour palette**: BG #EAF0F5 | section bars #1C5277 | accent #29ABE2 | footer
  gradient #1A3A6B -> #00A878 | Segoe UI | 16:9 for PPTX; professional formatting
  for XLSX.
- **Minimum filing count for a "comprehensive" register**: 85+ rows across the 19
  MECE categories (a lower count requires an explicit scope note explaining why).
- **Mandatory sheets (XLSX)**: Filing Register | Gap Analysis (when updating an
  existing register) | Legend & Notes | Cover.
- **Every row carries a primary sebi.gov.in / nseindia.com / bseindia.com /
  mca.gov.in hyperlink, fetched live this session** — law-firm blog links are never
  acceptable as the Source URL (Phase 6 Gates 1 and 6).
- **Quality benchmark**: McKinsey / BCG / Bain / Big Four regulatory due-diligence
  deliverables — board-ready and audit-ready.

## Deliverable Assembly Rules

- **Register in chat**: the 12-column schema (SKILL.md Phase 5) rendered as a table,
  with the calibrated verification block (Gate 7) at the end.
- **XLSX deliverable**: build in a task-scoped working directory and deliver through
  the host environment's supported file mechanism. Keep intermediate data outside the
  skill tree, use reproducible checkpoints, and exclude source documents and generated
  workbooks from version control unless the repository owner expressly approves them.
- **Uploaded-PDF-origin tasks**: when the source of truth is an uploaded regulatory
  PDF rather than live web research, a document-extraction workflow governs extraction
  and assembly; this skill contributes the MECE checklist and omission tripwires as the
  completeness audit layer.
- **PPTX deliverable**: apply the palette above and use a presentation workflow that
  preserves citations, source status, and scope limitations.

## Delivery Summary Template (Gate 7)

```
=== Delivery Summary: <deliverable name> ===
Scope           : <entity scope + domain>
Rows            : <N> across <N> MECE categories (floor: 85 for comprehensive)
Source currency : consolidated versions dated <date(s)>, listing page checked <timestamp>
Gates           : G1 <pass/fail> . G2 <..> . G3 <..> . G4 <..> . G5 <..> . G6 <..> . G7 self
FETCHED-verified: <N> rows (primary source read live this session)
UNVERIFIED      : <N> rows -> <cheapest resolution path>
Limitations     : single-context research+validation (where applicable)
Reference-file corrections flagged: <none | list>
```
