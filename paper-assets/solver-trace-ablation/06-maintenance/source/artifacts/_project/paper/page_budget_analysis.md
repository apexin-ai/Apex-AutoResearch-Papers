# Page Budget Analysis — EMNLP 2026 (8 page limit)

Date: 2026-05-15
Inputs: latest section artifacts (abstract_c1671f, introduction_176853, related_work_b05493, method_76d073, experiments_76b47a, discussion, conclusion_0cce3f).

## 1. Current word counts

Counted with LaTeX comments stripped (`%`-prefixed registry tags excluded). Numbers include in-text math/citations but not table/figure content.

| Section | Words | Notes |
|---|---|---|
| Abstract | 307 | Abstract does not count against 8 pages in ACL but contributes 1/3 of page 1 |
| Introduction | 874 | 5 paragraphs + itemized contributions |
| Related Work | 900 | 4 paragraphs, very citation-heavy |
| Method | 1140 | 6 subsections, includes formulas + H1–H7 taxonomy |
| Experiments | 2600 | 5 subsections, 4 tables + 3 figures embedded |
| Discussion | 613 | 5 paragraphs + 5-item practical implications list |
| Conclusion | 547 | 3 findings + limitations + future directions |
| **TOTAL body** | **6,674** | Excluding abstract: 6,367 |

Floats present:
- **4 figures**: `fig:sta-overview` (Intro), `fig:isr-collapse` (Exp), `fig:hacking-composition` (Exp), `fig:prolog-comparison` (Exp)
- **4 tables**: `tab:goodhart-landscape`, `tab:beta01-3seed`, `tab:prolog-crosslogic`, `tab:hacking-taxonomy`

## 2. Page budget math (EMNLP/ACL double-column)

- 8 pages × 650 words/page (pure prose ceiling) = **~5,200 words absolute max** if zero floats
- Realistic float footprint:
  - Each single-column figure (with caption): ~0.30 page → 4 × 0.30 = **1.2 page**
  - Each single-column resizebox table (with caption): ~0.28 page → 4 × 0.28 = **1.12 page**
  - Section/subsection headers, equations (eq:advantage, eq:grpo, eq:isr), itemized lists, paragraph indents: **~0.5 page**
- Float + structural overhead total: **~2.8 pages**
- **Prose budget: 8 − 2.8 = 5.2 pages × 650 ≈ 3,380 words**

Current 6,674 → must cut **~3,300 words (~49%)** OR move material to appendix.

This matches the reported "12 pages → 8 pages" gap: ~4 pages over = ~2,600 prose words over, plus float reflow recovers another ~1 page.

## 3. Per-section budgets and cuts

| Section | Current | Target | Cut | Strategy |
|---|---|---|---|---|
| Abstract | 307 | 200–230 | ~80 | Tighten findings 2 & 3 |
| Introduction | 874 | 650 | ~225 | Compress paragraphs 2–4 |
| Related Work | 900 | 450 | ~450 | Single paragraph per theme, fewer citations inline |
| Method | 1140 | 650 | ~490 | Move H1–H7 enumeration + reward-formulation paragraphs to appendix; keep §3.1–§3.4 |
| Experiments | 2600 | 1100 | ~1,500 | Aggressive cut: merge subsections, drop redundant prose around tables, kill cross-seed narrative |
| Discussion | 613 | 250 | ~365 | Drop "Practical Implications" list; merge "Classifier Limitations" into Experiments |
| Conclusion | 547 | 180 | ~365 | One paragraph per finding, drop Limitations (separate unpaginated section) |
| **Total** | **6,674** | **~3,480** | **~3,200** | Hits ~5.4 pages of prose |

## 4. Specific cut recommendations (priority order)

### Priority 1 — Experiments (biggest absolute win: −1,500 words)

**Section 4.1 Setup (currently ~210 words):** Cut footnote on data file (project-internal note, irrelevant to readers). Cut the legacy-filename parenthetical about ProofWriter. Compress evaluation protocol paragraph by 40%. → target 120 words.

**Section 4.2 ISR as Diagnostic (~440 words):**
- "Collapse trajectory" paragraph (lines 31–36): keep first 3 sentences, cut the monotonic-decline restatement at end. → −50 words
- "Cross-seed instability" (lines 38–42): the qualitative-mode description for s42/s43/s44 is now also in Conclusion and Method H1–H7 — keep only the σ=47pp headline and the "diagnostic value" sentence; move per-seed mode descriptions to appendix table. → −90 words
- "SFT baseline" (lines 44–47): the matched-PR caveat (line 47) repeats info already telegraphed by Tab 1 — drop the second sentence about 100-step appendix comparison. → −40 words

**Section 4.3 Meta-Level Goodhart (~750 words):** Largest cut target.
- Lead paragraph (52–54): merge into Tab 1 caption. → −60 words
- "Low-dose ISR β=0.1" (103–109): keep the H7 64.5% vs 0% number and one sentence on H1 conversion. Drop the "Total conclusion embedding…GRPO-universal" parenthetical (already in Conclusion). → −80 words
- "Premise-count confound" (111–117): this is critical for C2 — keep, but tighten by 30%. → −50 words
- "High-dose ISR β=0.3" (119–127): each seed gets 1 sentence currently, cut to a single sentence summarizing the 3-mode split with PR numbers; per-seed Goodhart pathology names move to appendix. → −180 words

**Section 4.4 Cross-Logic Transfer (~620 words):**
- Prolog exec-only paragraph (167–171): the redundancy-vs-gaming interpretation sentence (last 2 lines) duplicates Discussion ¶ "ISR Capability Boundary." Cut from Experiments, keep in Discussion. → −80 words
- Prolog ISR-as-reward (173–179): each seed described in 2 sentences; tighten to one per seed and let Tab 3 do the work. → −180 words
- "FOL vs Prolog comparison" (181–184): keep the 0% vs 16% headline; cut the "broader gaming basin" speculation (move to Discussion or drop). → −60 words

**Section 4.5 Hacking Taxonomy (~430 words):**
- The enumeration of which seed shows which mode (line 221) duplicates Tab 4 and Method H1–H7. Cut the prose enumeration entirely, keep only the table. → −100 words
- "Cross-condition pattern" paragraph (223–225): keep the 80% pooled-hacking number, cut the s42 81%/32% rehash (already in Tab 2). → −80 words
- Final two paragraphs (227–228): "taxonomy is descriptive…" can compress to one sentence. → −60 words

### Priority 2 — Related Work (−450 words)

Current is 4 well-sized paragraphs but ACL accepted papers typically allocate 0.6–0.8 page (≈400–550 words) to related work. Cut strategy:

- **Neurosymbolic Reasoning paragraph (~190 words):** Cut sentence about LoRP/FoVer (line 7) — these are marginal to our claim. Cut the "report 87% conclusion embedding…suggests prove-rate gains may overstate" sentence (line 13) since it duplicates the Intro hook. → −80 words
- **Reward Shaping paragraph (~220 words):** Drop the PROF and ProGRS sentences (lines 22–23) — they're tangential. Keep Lightman, Math-Shepherd, Gao-effective-RL. → −90 words
- **Reward Hacking paragraph (~245 words):** This is the closest cousin literature; keep dense. Drop the Kwa et al. sentence on heavy-tailed misspec (line 30) and the Yang spurious-rewards mention (line 32). → −90 words
- **Mutation Testing paragraph (~200 words):** Drop the Just et al. "synthetic mutants approximate real faults" sentence (line 39) and the LLMorpheus mention (line 40) — neither directly supports STA's novelty claim. → −90 words
- Convert paragraph headings to inline phrases (e.g., "On the neurosymbolic side, ...") to save ~10 words each.

### Priority 3 — Method (−490 words, mostly via appendix migration)

Move to appendix:
- **§3.5 Reward Formulations (lines 65–78):** All four definitions are restated in Experiments §4.1 and Table 1 — keep only the "Additive ISR: r = r_exec·(1 + β·ISR), β ∈ {0.1, 0.3}" inline mention in Experiments. The SFT, additive-random, and convex-combination paragraphs go to appendix. → −180 words
- **§3.6 Reward Hacking Taxonomy (lines 80–95):** The full H1–H7 enumeration belongs in appendix because Tab 4 + Fig 3 already convey the modes. Keep one sentence in Method linking to App §X. → −280 words

Keep tight in main body: §3.1 Task (kept), §3.2 GRPO (compress to one paragraph + Eq 2, drop Eq 1), §3.3 STA protocol, §3.4 ISR definition + premise-count bias note.

### Priority 4 — Discussion (−365 words)

- Drop "Practical Implications" list (lines 38–45): 5-item list, ~140 words. This belongs in Conclusion or as a takeaways box. **Recommended: cut entirely** since each item is already implied by experiments + conclusion findings.
- Compress "Classifier Limitations" (¶4): the s43 uppercase + s44 query-as-fact details are in Experiments §4.4. Drop ¶4, keep one sentence in Experiments. → −100 words
- "Premise Count Confound" and "ISR Capability Boundary": keep both — these are the cleanest contributions of the discussion. Light edits only.
- "Meta-Level Goodhart's Law" ¶: tighten by 25%, drop the "general principle for the reward-shaping community" final sentence (the cautionary note is already in Abstract + Intro + Conclusion). → −60 words

### Priority 5 — Conclusion (−365 words)

- Three findings paragraphs (lines 6–20) all restate Abstract content with slightly more numbers. **Cut each to 1 sentence** that adds the headline number not in Abstract. → −280 words
- Drop "Limitations" paragraph (22–27): standard EMNLP convention is a separate "Limitations" section *after* References (which doesn't count against 8 pages). **Move Limitations to its own section** at end. → recovers 0 prose words from page budget directly, but frees ~80 words from §Conclusion (they become unpaginated content).
- "Future directions" paragraph: keep 2 sentences. → −90 words

### Priority 6 — Introduction (−225 words)

- "The execution-only blind spot" paragraph (9–13): cut the "Process reward models…do not transfer" sentence (line 12) — covered in Related Work. → −40 words
- "Component necessity testing" paragraph (15–20): the NLI ρ=−0.049 caveat (line 20) appears verbatim in Discussion + Conclusion. Keep in Discussion only. → −40 words
- "ISR as diagnostic" (22–25): drop the "Three random seeds diverge…each converging to" sentence — Tab 2 + cross-seed paragraph in Experiments cover it. → −60 words
- "Meta-level Goodhart" (27–33): tighten the β=0.3 enumeration (line 31, three Goodhart pathways) — keep one sentence. → −80 words

### Priority 7 — Abstract (−80 words)

- Sentence 6 (the β=0.1/β=0.3 dose-response): compress to one clause for each dose. → −50 words
- Sentence 8 (7 hacking modes): merge into sentence 9 (asymmetry conclusion). → −30 words

## 5. What MUST stay in main body (non-negotiable)

These are the load-bearing claims and their direct evidence; deleting them weakens the paper:

- **Abstract**: headline ISR 0.642→0.003 collapse number; H7 64.5%/0% contrast; 1.06× premise-matched ratio; cross-logic universal Goodhart.
- **Introduction**: opening hook (93% PR with 87% embedding), all 4 contributions C1–C4, the asymmetry statement.
- **Method §3.3 STA + §3.4 ISR**: full protocol definition + ISR equation; premise-count bias paragraph (critical for §4.3 confound analysis).
- **Experiments**: Fig 2 (collapse trajectory), Tab 1 (Goodhart landscape), Tab 2 (β=0.1 3-seed + n≥3 column — the 1.06× evidence), Tab 3 (Prolog cross-logic), Fig 3 (hacking composition).
- **Discussion**: "ISR Capability Boundary" (exec-low vs ISR-high interpretation, per active constraint C006), "Premise Count Confound" (methodological contribution).
- **Conclusion**: three-finding summary (compressed), pointer to Limitations.

## 6. Appendix migration list (recovers main-body space without losing content)

| Content | Source | Appendix target |
|---|---|---|
| Reward formulation variants (random, convex-combo) | Method §3.5 | App A: Reward Formulations |
| Full H1–H7 mode definitions with examples | Method §3.6 | App B: Hacking Taxonomy |
| Per-seed exec-only traces (s42/s43/s44 descriptions) | Exp §4.2 | App C: Per-Seed Failure Modes |
| β=0.3 per-seed Goodhart pathway details | Exp §4.3 | App D: High-Dose Goodhart |
| 100-step matched-PR SFT comparison | Exp §4.2 | App E: SFT vs RL at Matched PR |
| Prolog s43 uppercase + s44 query-as-fact long-form descriptions | Exp §4.4, Disc | App F: Prolog Mode Mechanics |
| Classifier methodology (text-match + functional cross-check) | Method, Disc | App G: Two-Stage Classifier |

## 7. Float discipline

To maintain 4 figures + 4 tables in 8 pages, all floats should be single-column where possible:
- Tab 1, Tab 2, Tab 4 are already `\resizebox{\columnwidth}{!}` — good.
- Tab 3 is `\resizebox{\columnwidth}{!}` — good but currently 7 columns × 9 rows is dense; consider dropping the "Mode" column (last column is descriptive prose, can be replaced by a footnote keyed to a label).
- Fig 1 (sta-overview): if currently `figure*` (two-column), confirm whether one-column at 0.95\columnwidth suffices.
- Fig 2/3/4: ensure all are `\columnwidth` not `\textwidth`.

**Recommendation: consider merging Tab 1 and Tab 2.** Tab 1 (Goodhart landscape) is a 3-seed mean ± std summary; Tab 2 (β=0.1 3-seed breakdown) is the per-seed version of one row of Tab 1. A single "landscape with per-seed expansion for β=0.1" table would save ~0.25 page. If kept separate, both tables can shrink rows: drop the "Base (0-shot)" row from Tab 1 (the 12% number is already in §3.2 prose).

## 8. Expected outcome

After all cuts:
- Prose: ~3,480 words ≈ 5.4 pages
- Floats: 4 figures + 4 tables (or 3 tables if merged) ≈ 2.4 pages
- Structural overhead: ~0.4 page
- **Projected total: 8.2 pages → trim further in Experiments §4.3/§4.4 if margin negative**

If 8.2 still over, additional 0.2-page cut from Experiments §4.5 (remove Fig 3 hacking-composition — its content is fully captured by Tab 4).

## 9. Open items

- **s43 random β=0.3 placeholder** in Tab 1 footnote (§): Experiments §4.3 currently reports 2-seed random control. Decision deferred per task brief — when s43 data lands, the only edit is updating the footnote and the mean ± std row.
- **Fig 1 sta-overview placement**: not in any of the artifacts I read — currently referenced only in Intro line 16. Confirm the asset exists; if not, this is a separate work item (not a page-budget issue).
