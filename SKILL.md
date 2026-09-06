---
name: sebi-india-compliance-research
description: >
  Specialized skill for researching, compiling, mapping, and auditing compliance
  obligations of public / listed companies in India under SEBI LODR 2015, SEBI PIT 2015,
  SEBI SAST 2011, SEBI ICDR 2018, SEBI NCS 2021, SEBI Buyback 2018, SEBI Delisting 2021,
  SEBI SBEB 2021, Companies Act 2013, and exchange-specific obligations.
  Always use this skill when the user asks about: SEBI filing requirements, listed company
  compliance India, LODR obligations, NSE/BSE filings, compliance calendar India,
  public company filings SEBI, SEBI regulatory mapping, disclosure requirements for
  listed companies, or building a compliance register from live web research on any
  Indian securities-law domain. Do NOT use when the task is limited to extracting
  obligations from an uploaded document or analysing a court/tribunal judgment.
license: Proprietary - DK Mendiratta
metadata:
  version: "2.0.0"
  created: "2026-03-29"
  author: "DK Mendiratta"
  tags: "sebi, lodr, listed-companies, india-compliance, regulatory-mapping, nse-bse, corporate-governance, grc"
---

# SEBI India Compliance Research Skill (v2.0)

## Compatibility

- Required capability: live web search and full-page web retrieval.
- Optional capability: a crawler that can extract JavaScript-rendered pages and linked documents.
- Output capability depends on the requested format, such as Markdown, XLSX, or PPTX.

## Changelog

### v2.0.0 — 2026-07-12

- Restructured the skill for progressive disclosure through a process spine, four
  phase-specific references, and output/trigger evaluation sets.
- Made retrieval tool-agnostic and added environment detection, bounded retry loops,
  calibrated claims, domain generalization, fetch-before-cite checks, verification
  tripwires, and failure-scenario handling.
- Added negative trigger boundaries for document extraction and judgment analysis.

### v1.0.0 — 2026-03-29

Initial release addressing seven failure classes found in comparative benchmark
outputs: stale source versions, secondary-source-first retrieval, missing MECE coverage,
snippet-only reading of primary PDFs, absent amendment-history checks, exchange calendars
treated as secondary, and no domain-specific omission checklist.

## Purpose

This skill governs research into SEBI / NSE / BSE / MCA compliance obligations for
listed and public companies in India — and, via the Generalization Protocol (Part 2),
any adjacent Indian compliance domain researched from live web sources. Outputs are:

- 100% traceable to primary sources fetched live this session
- Anchored to the latest consolidated / last-amended version of every instrument
- Exhaustive against a MECE category checklist built before searching, not from search results
- Cross-validated against exchange compliance calendars as independent primary sources
- Free from the seven root-cause failure modes documented in v1.0.0 (see changelog),
  which caused an early register to miss 18 filings and contain 5 errors

Scope boundary: this skill compiles registers from **live web research**. If the source
of truth is an **uploaded regulatory PDF**, use a document-extraction workflow; this
skill may still supply the MECE checklist and omission tripwires as a completeness audit.

---

## READING ORDER (execute in sequence)

```
START HERE  -> SKILL.md (this file): Parts 0-2 + Phases 1-6
AT PHASE 1  -> view references/canonical_sources.md   (seed URLs + retrieval tiers)
AT PHASE 3  -> view references/mece_checklist.md      (19 categories + instrument list)
AT PHASE 4  -> view references/known_omissions.md     (Tier A/B omission tripwires)
AT DELIVERY -> view references/output_standards.md    (locked output formats + assembly)
```

---

## PART 0 — EXECUTION PLAN & LOOP CONTRACT (read first, applies throughout)

The failure modes of compliance research are rarely bad legal reasoning — they are
unplanned execution: stale sources cited confidently, unbounded search loops, and
coverage claims never actually checked. This contract exists to prevent those.

**0.1 — Plan before research.** Before the first fetch, state in one short block:
the compliance domain and entity scope (equity-listed / debt-listed / HVDLE / SME /
market-cap tier), the instrument universe you expect to cover, the phase sequence
(Phase 1 -> 2 -> 3 -> 4 -> 5 -> 6), and the verification artifact for each phase
(Phase 1: populated Canonical Source Table with live-fetch dates; Phase 2: per-tier
extraction log; Phase 3: MECE coverage map; Phase 4: omission audit result; Phase 6:
gate checklist output). A phase without a named verification artifact is not planned.

**0.2 — Sequencing is strict.** Phases run in order. Research (Phase 2) never starts
before the Source Version Gate (Phase 1) completes — searching from stale versions is
root cause RC1 and poisons everything downstream. The MECE map (Phase 3) is built
before broad searching, so coverage is by construction, not by recall.

**0.3 — Loop bounds.** Every retrieval loop is bounded: a failing fetch is retried at
most twice (once with an alternate tool per Part 1, once via a fresh search for the
current URL); an unresolved item after that is recorded as UNRESOLVED with the attempts
listed — never silently dropped, never filled from memory. A failed quality gate gets
one targeted fix plus one re-validation before escalating to the user with the failing
artifact. Unbounded self-repair burns context and hides root causes.

**0.4 — Calibrated claims.** Every legal value in the output (timeline, threshold,
penalty, applicability) carries exactly one source class, known while writing it:
FETCHED (read from a primary source fetched this session), SKILL-SEED (from this
skill's reference files — allowed only as a search target, never as a citable fact),
or UNVERIFIED (labeled inline). "Verified" in the delivery summary means the value was
read from a live-fetched primary source this session — nothing weaker.

**0.5 — Author/grader separation, as far as the surface allows.** Phase 6 gates are
checklist executions against the actual output, not impressions. Where one context both
researched and validated (all single-context surfaces), say so in the delivery summary.

**0.6 — Copyright discipline.** Registers state obligations in structured, paraphrased
form. Never reproduce long verbatim passages of regulation text in narrative outputs;
quote at most a short operative phrase where exact statutory wording is load-bearing,
and cite the primary URL.

---

## PART 1 — ENVIRONMENT & TOOL DETECTION (before Phase 1)

Determine which retrieval tools exist in this session and map each protocol step
accordingly. Never claim a step "ran" with a tool the surface does not have.

| Protocol step | Preferred (if Firecrawl MCP connected) | Native fallback (always available) |
|---|---|---|
| Navigate SEBI listing pages | firecrawl_scrape / firecrawl_agent | web_fetch on the listing URL |
| Full-text extract of a regulation page | firecrawl_scrape (full page) | web_fetch (paginate long documents; fetch linked PDF pages) |
| Amendment discovery | firecrawl_search | web_search (no site: operator in native web_search — search "SEBI LODR amendment 2026 sebi.gov.in" as plain terms) |
| Exchange calendar tables | firecrawl_scrape | web_fetch each calendar URL |
| Deep multi-page crawl | firecrawl_agent / firecrawl_crawl | Sequential web_fetch of discovered links |

Constraints to respect on native tools: web_fetch can only fetch URLs already present
in the conversation (skill reference files count — they are in context once read) or
returned by a prior search; therefore surface the needed URL via the reference file or
a search result before fetching it. If a fetch fails on a JS-rendered page and no
Firecrawl is connected, record the item UNRESOLVED per 0.3 rather than substituting a
secondary source silently.

---

## PART 2 — DOMAIN GENERALIZATION PROTOCOL (first-principles instantiation)

The six-phase method below is domain-independent. LODR listed-company compliance is
the fully worked instantiation; for any other Indian compliance domain (a PIT-only
task, an ICDR transaction, AIF/PMS obligations, merchant-banker duties, an RBI or
IRDAI framework), instantiate the method rather than improvising:

1. **What is true?** Identify the instrument universe by *exclusion, not recall*:
   fetch the regulator's official regulations/circulars listing page and enumerate
   every instrument touching the domain, then explicitly exclude the out-of-scope
   ones with a one-line reason. Anything not enumerated cannot be silently missing —
   coverage becomes a property of construction.
2. **What is needed?** Fix the entity scope and the deliverable (register / calendar /
   gap analysis / memo) before searching; the deliverable defines which columns of the
   Phase 5 schema are load-bearing.
3. **What should be built?** Construct the domain's MECE category set *deductively
   from the instrument's own structure* (chapters, schedules, obligation types) before
   the first broad search — never inductively from whatever search results return.
4. **What proves it?** Adopt Phase 6 gates, replacing the LODR-specific tripwires in
   Gate 3 with domain equivalents identified during step 1 (every domain has its own
   "everyone gets this wrong" values — find them in the regulator's FAQs and recent
   informal guidance, then verify against primary text).

The seven v1.0.0 root causes are domain-independent failure classes. Re-read the
changelog list before instantiating a new domain: each phase below exists to kill one
of them, and the new domain needs the same seven protections.

---

## PHASE 1 — MANDATORY SOURCE VERSION VERIFICATION GATE

Complete this before any research. No exceptions — RC1 (stale versioning) is the
single most damaging failure class because every downstream citation inherits it.

**Step 1.1 — Go to the regulator's listing pages directly** (not a general search).
The SEBI listing URLs, master-circular listing, and circulars listing are in
`references/canonical_sources.md` — read that file now.

**Step 1.2 — Populate the Canonical Source Table** before researching: one row per
instrument in scope with (a) the latest consolidated URL found on the listing page,
(b) its "last amended" date, (c) the timestamp you fetched it this session. Seed URLs
in the reference file are search targets only — the table is populated from what the
listing page shows today, which supersedes every stored URL.

**Step 1.3 — Full-text extract the primary instruments.** Snippets are insufficient
for exhaustive mapping (RC4). Extract the complete text of each in-scope regulation
including ALL Schedules — Schedule III Parts A and B of LODR contain dozens of
event-driven disclosure triggers never adequately summarised in secondary sources,
and are the single largest source of gaps in event-driven filing registers. Extract
both exchange compliance calendars in full (every row).

**Step 1.4 — Amendment sweep, last 12 months.** Search for amendments and circulars
published after the consolidated version's date (tool mapping per Part 1). Anything
found may contain obligations not yet folded into the consolidated text — log each
and reconcile during Phase 2.

Completion criterion: Canonical Source Table fully populated with live-fetch
timestamps, full texts extracted, amendment log written.

---

## PHASE 2 — PRIMARY-FIRST RETRIEVAL PROTOCOL

Retrieval proceeds in strict tier order; do not drop to a lower tier until the higher
tier is exhausted for the item at hand (RC2).

- **Tier 1 — Official regulator sources** (SEBI regulations, master circulars,
  standalone circulars, SEBI FAQs — FAQs on sebi.gov.in are primary). Full tables of
  instruments and what to extract from each: `references/canonical_sources.md`.
- **Tier 2 — Exchange compliance calendars** (NSE main board, NSE debt, BSE) read as a
  separate, independent pass (RC6). They contain obligations arising from listing
  conditions that appear in no SEBI document. After both passes, reconcile line-by-line
  against the regulation-derived list; every calendar row absent from your list is a
  gap to investigate before Phase 5.
- **Tier 3 — Expert practitioner sources** (named in the reference file) — for
  implementation nuance and cross-validation only, never as the citable source.
  When Tier 3 conflicts with Tier 1, the primary regulation text is always correct
  (documented example: multiple law-firm blogs state the PIT Reg 7(1) initial
  disclosure as 30 days; the regulation text says 7 days).
- **Tier 4 — General web search** — last resort for items unresolved after Tiers 1–3;
  any fact sourced here must still be confirmed against a Tier 1/2 fetch before it
  enters the register, or be labeled UNVERIFIED.

Completion criterion: every register row's source column points at a Tier 1 or Tier 2
URL fetched this session.

---

## PHASE 3 — MECE CATEGORY CHECKLIST (coverage by construction)

Map the task against the 19-category MECE checklist in
`references/mece_checklist.md` **before** broad searching (RC3). Track each category
as covered / not covered / N/A as research progresses. A "not covered" row after
research completes is a gap that must be investigated before delivery, and an N/A
requires a one-line reason. For non-LODR domains, build the equivalent deductive
category set per Part 2 step 3 before searching.

---

## PHASE 4 — KNOWN OMISSIONS AUDIT (historical gap tripwires)

After research completes, audit the output against
`references/known_omissions.md` — Tier A (items missed by nearly all AI research),
Tier B (items frequently under-specified), and the Tier C cross-referenced instrument
checklist. These entries are **tripwires, not answers**: each one names a filing to go
verify against the fetched primary text (RC7). If a tripwire's stored value differs
from what the current primary text says, the primary text wins — and flag the
reference file for update in the delivery summary so the correction persists.

---

## PHASE 5 — OUTPUT SCHEMA FOR COMPLIANCE REGISTERS

Any register (any table of filings) uses exactly these 12 columns in this order;
every field populated in every row:

| # | Column | Rule |
|---|--------|------|
| 1 | S.No. | Sequential |
| 2 | Category | One of the MECE categories from Phase 3 |
| 3 | Filing / Disclosure Name | Plain language, matching exchange-portal terminology |
| 4 | Regulation Reference | Exact regulation + schedule + sub-rule, e.g. "Reg 33(3)(a) LODR 2015" |
| 5 | Applicable To | Precise entity scope (all equity-listed / Top 1000 / Top 500 / Top 250 / Top 150 / Top 100 / equity+debt / debt-only / newly listed only) |
| 6 | Filing Authority | NSE / BSE / SEBI / MCA / combinations / Internal |
| 7 | Frequency | Annual / Half-yearly / Quarterly / Event-driven / One-time / Continuous |
| 8 | Trigger / Event | The specific condition — never a vague "material event" |
| 9 | Timeline from Trigger | Exact outer bound; "promptly"-type words only alongside the regulatory outer bound |
| 10 | Format / Mode | XBRL / XBRL+PDF / PDF / prescribed form number / physical |
| 11 | Penalty for Non-Compliance | Exact provision and amounts |
| 12 | Source URL | Primary sebi.gov.in / nseindia.com / bseindia.com / mca.gov.in link, fetched live this session — never a law-firm blog |

For XLSX/PPTX packaging, sheet architecture, and format standards:
`references/output_standards.md`. Where the task originated from an uploaded PDF,
the selected document-extraction workflow governs the workbook; this skill's Phase 3/4
checklists still apply as the completeness audit.

---

## PHASE 6 — QUALITY GATES (final checklist before delivery)

**Gate 1 — Source currency.** Latest consolidated URLs used (dates checked on the
listing page this session); every Source URL is a primary domain.

**Gate 2 — MECE coverage.** All 19 categories resolved covered/N-A-with-reason; Tier C
instrument checklist fully ticked; every exchange-calendar row reconciled.

**Gate 3 — Known-error tripwires (verify each against the fetched primary text; the
fetched text always wins over the values stored here).** Historically wrong values to
re-check: PIT Reg 7(1) initial disclosure (regulation text says 7 days, blogs say 30);
Reg 40(9) certificate periodicity (annual) vs Reg 7(3) certificate (separate,
half-yearly); BRSR Core assurance phased rollout present; delisting treated under its
own 2021 regulations with the full RBB process; OFS T-1 intimation distinct from
buyback; cyber-incident 6-hour rule distinct from the 24-hour Reg 30 window; Large
Corporates identification and penalty mechanics.

**Gate 4 — Timeline precision.** No row's timeline lacks an outer bound; board-meeting
outcome dual rule (during vs after market hours) stated in both branches; PIT
timelines expressed in trading days.

**Gate 5 — Exchange reconciliation.** NSE and BSE calendars each read independently;
every calendar row present in the register or explicitly noted as a duplicate.

**Gate 6 — URL liveness (v2.0).** Every Source URL in the deliverable was fetched
this session and returned the expected instrument. A URL recalled from this skill's
reference files but not fetched fails this gate.

**Gate 7 — Calibrated delivery summary (v2.0).** The summary states, per 0.4: which
values are FETCHED-verified, which remain UNVERIFIED (with the cheapest resolution
path), the single-context limitation where applicable (0.5), and any reference-file
corrections flagged by Phase 4.

---

## FAILURE HANDLING (minimum scenarios)

- **Primary source unreachable** (site down, fetch blocked, JS-rendered without
  Firecrawl): retry per 0.3 bounds; then mark the affected rows UNVERIFIED with the
  attempted URLs listed, and say exactly what the user should fetch to close them.
  Never substitute a Tier 3 source as if it were primary.
- **Version conflict** (amendment sweep finds instruments newer than the consolidated
  text): the newer amendment governs the affected obligations; annotate those rows
  with both the consolidated citation and the amending circular.
- **Ambiguous scope** (user did not fix entity type / listing status / market-cap
  tier): if exactly one missing detail blocks correctness, ask exactly one question;
  otherwise proceed on the widest defensible scope with the assumption labeled at the
  top of the deliverable and per-row applicability kept precise so the user can filter.

---

## COMPLETION CRITERION FOR THE WHOLE SKILL

The task is complete when: the deliverable exists in the agreed format; all seven
gates show their checklist output; the delivery summary carries the calibrated
verification block; and any tripwire corrections discovered are flagged for
persistence into this skill's reference files.
