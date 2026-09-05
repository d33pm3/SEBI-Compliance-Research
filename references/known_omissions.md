# Known Omissions Register — SEBI India Compliance Research v2.0
*Read at Phase 4, AFTER research completes. Confirmed through comparative evaluation
of multiple independent model outputs on the same SEBI compliance task.*

**Tripwire discipline (governs every row below):** each entry names a filing to go
verify against the primary text fetched this session. The stored timeline/value is
the historically correct answer as of last update — if the current primary text
differs, the primary text wins, and this file must be flagged for update in the
delivery summary so the correction persists (Part 0.4 / Phase 4 of SKILL.md).

## Tier A — Items Missed by Nearly All AI Research (complete omissions)

| Filing | Regulation | Why It's Missed | Timeline to Verify |
|--------|------------|----------------|--------------------|
| BRSR Core with third-party assurance | SEBI BRSR Circular Jul 2023 | Phased rollout makes it look "future" but it is already mandatory for the top market-cap tiers | With Annual Report (phased by market-cap tier) |
| De-listing process (PA + RBB + exit pricing) | SEBI Delisting Regulations 2021 | Separate regulation; never mentioned in LODR summaries | PA within 2 WD; RBB 26 WD; 3–6 months total |
| Offer for Sale (OFS) by promoters | SEBI OFS Framework Circular 2012 | Not in LODR; standalone circular that search ranking ignores | T-1 notice to exchange; OFS on T; settlement T+1 |
| Cyber security incident — critical | SEBI Circular SEBI/HO/ITD/ITD_VAPT/P/CIR/2023/135 | Separate circular, not referenced in LODR | 6 hours for critical; 24 hours for the Reg 30 window |
| Large Corporate (LC) framework | SEBI Circular Nov 2018, amended Oct 2023 | Standalone, penalty-bearing circular outside LODR | Identification by 15 April; annual compliance by 15 April |
| Commercial Paper listing obligations | SEBI NCS Regulations 2021 + RBI Master Direction | CP treated as a money-market instrument; SEBI listing duty overlooked | Listed within 4 WD of allotment |
| NCRPS obligations | SEBI NCS Regulations 2021 | Bundled with NCDs but has distinct listing/filing rules | Separate from NCD; prospectus before issuance |
| ESG rating change disclosure | SEBI ERP Circular Jan 2023 | New category; not yet in most LODR checklists | Within 24 hours of ESG rating action |

## Tier B — Items Frequently Under-Specified (present but incomplete)

| Filing | Common Error | Correct Treatment to Verify |
|--------|-------------|------------------------------|
| PIT initial disclosure (Reg 7(1)) | Stated as "30 days" — wrong | 7 days from appointment; company then files within 2 trading days |
| Reg 40(9) PCS certificate | Classified half-yearly — wrong | Annual, within 30 days of FY end. Reg 7(3) (half-yearly) is a SEPARATE filing |
| Reg 7(3) compliance certificate | Entirely missing | Half-yearly, within 1 month of each half-year end; Compliance Officer + RTA sign |
| Post-listing shareholding pattern | Only quarterly pattern covered | One-time filing 1 WD prior to listing day under Reg 31(1)(a) |
| Capital restructuring >2% pattern | Not included | Within 10 days of >2% change due to capital restructuring |
| RTA appointment / change | Not included | Within 7 days of execution of tripartite agreement |
| BRSR (basic) | Folded into Annual Report description | Mandatory separate disclosure for Top 1000 in XBRL |
| Statement on Impact of Audit Qualifications | Not included | Form A (unmodified) or Form B (qualified) with every annual audited result |
| Revised Annual Report post-AGM | Not included | Within 48 hours of AGM if revisions required — Reg 34(3) |
| Risk Management Committee | Mentioned in passing under CG | Standalone: max 210-day gap between meetings (May 2024 amendment); Top 1000 mandatory |
| Material subsidiary | Mentioned for secretarial audit only | Full framework: annual identification; quarterly CG disclosures; at least 1 ID on the subsidiary board |
| Ex-date intimation | Record date covered; ex-date missing | Exchange sets ex-date at T-1; listed entity ensures the process is followed |

Tier C (cross-referenced instruments) lives with the MECE checklist:
`references/mece_checklist.md`.
