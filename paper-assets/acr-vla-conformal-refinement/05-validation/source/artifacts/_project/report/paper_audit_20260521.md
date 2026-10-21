# Paper Pre-Submission Audit — 2026-05-21

CoRL 2026 DDL = **2026-05-29** (8 days remaining).

Paper source: `docs/paper/` (main.tex + 7 included .tex files + references.bib + corl_2026.sty/bst).
Build target: `main.pdf` (currently 15 pages, 544 KB, last built 2026-05-21 15:44).

---

## 1. Compilation Status

**Status: BUILDS CLEAN. PDF produced, no errors.** Full latexmk run confirmed.

### Warnings (all cosmetic, none block submission)

| Type | Where | Severity | Action |
|------|-------|---------:|--------|
| `Underfull \hbox` badness 3690 | abstract.tex / keywords line | low | leave (URW Times mid-line break, common) |
| `Underfull \hbox` badness 1194 | related_work.tex L8–9 (paragraph "Training-time methods.") | low | leave |
| `Underfull \hbox` badness 1502 | method.tex L37–38 ("Architecture." paragraph) | low | leave |
| `Underfull \vbox` badness 10000 | output during method.tex page break (×1) | low | leave (page-break artefact) |
| `Underfull \vbox` badness 10000 | output during appendix page break (×1) | low | leave |
| `LaTeX Warning: 'h' float specifier changed to 'ht'` (×3) | appendix.tex L7, L17, L31, L97 figures | low | optionally change `[h]` → `[ht]` in appendix figs to silence |
| `Package hyperref Warning: Token not allowed in PDF string (math shift)` (×4) | appendix section captions containing `$K$` etc. | low | optional: wrap captions with `\texorpdfstring{$K$}{K}` to silence |

**No multiply-defined or undefined references. No "Citation undefined". No missing graphics.** All 6 PDF figures resolve from `figures/`.

---

## 2. Bibliography Audit

- `\cite{}` keys used: **31**, unique.
- `references.bib` entries: **31**.
- **Missing: none.** **Unused: none.** Perfect 1:1.
- BibTeX `main.blg` shows `warning$ — 0` → no bib-style warnings.
- `main.bbl` rebuilds cleanly; thebibliography contains all 31 entries.

Cited keys, verified all resolve:
```
a2c2_2025, angelopoulos2023gentle, black2024pi0, brohan2023rt2, chen2026reconvla,
chi2023diffusion_policy, chun2025dasip, dai2025rover, digflow2025, fei2025liberoplus,
ghosh2024octo, jiang2024transic, johannink2019residual, kim2024openvla, ledoit2004well,
li2025vlapilot, lipman2023flow, liu2023libero, liu2026scvla, liu2026ttvla,
pan2025drc, robustvla2025, ross2011dagger, shukor2025smolvla, silver2018residual,
snell2024scaling, srpo2025, wang2025cploop, xiao2026pld, zhao2024conformalized,
zhou2025acp_cbf
```

---

## 3. Numerical Consistency Check (paper ↔ registry)

I sampled key numbers from Table 1 (main), Table 2 (adaptive Object), Table 3 (adaptive Spatial), Table 4 (K-ablation), Table 6 (π_0.5), and prose. Method: read raw `success_rate` from registry experiments matching each row, recompute mean ± sample std, compare to claim.

### ✅ Verified (match registry exactly within rounding)

| Claim | Paper | Recomputed from registry | Status |
|-------|------:|-------------------------:|:------:|
| Plan A Object SR (n=3) | 18.3 ± 2.1 | 18.33 ± 2.08 (seeds 42/43/44 = 19/16/20) | ✅ |
| Plan A Spatial SR (n=3) | 35.0 ± 1.0 | 35.00 ± 1.00 (seeds 42/43/44 = 34/35/36) | ✅ |
| Random K=5 Object (n=4) | 10.5 ± 2.9 | matches framing seeds 42–45 = 14/11/10/7 | ✅ |
| CRM obs_only K=5 Object (n=7) | 16.0 ± 2.2 | matches framing seeds 42–48 = 14/19/17/15/16/13/18 | ✅ |
| CRM obs_only K=5 Spatial (n=4) | 34.5 ± 2.1 | 34.50 ± 2.08 (seeds 42/43/44/45 = 35/32/37/34) | ✅ |
| Spatial Random K=10 (n=3) | 29.3 ± 4.2 | 29.33 ± 4.16 (seeds 42/43/44 = 34/26/28) | ✅ |
| K=2 L2 vs K=10 var ρ | 0.9979 | matches D076 memo | ✅ |
| LTO heldout vs VLA-only | 2 % vs 14 % | registry: eval-lto-splitA-heldout-v2 = 0.02, eval-lto-splitA-vla-only-{v2,r2,r3} = 0.14 (3 reps identical) | ✅ |
| π_0.5 VLA-only Object (n=3) | 81.5 ± 0.5 | 81.50 ± 0.50 (seeds 42/43/44 = 82/81.5/81, all -r3) | ✅ |
| π_0.5 VLA-only Spatial (n=3) | 84.2 ± 1.0 | 84.17 ± 1.04 (seeds 42/43/45 = 84.5/83/85; note seed 45 not 44) | ⚠️ see §5.4 |
| Object adaptive P25 (n=3) | 14.3 ± 1.2 | 14.33 ± 1.15 (15/13/15) | ✅ |
| Object adaptive P50 (n=3) | 15.3 ± 1.2 | 15.33 ± 1.15 (16/16/14) | ✅ |
| Object adaptive P75 (n=3) | 13.7 ± 2.1 | 13.67 ± 2.08 (12/13/16) | ✅ |
| Object adaptive P90 (n=3) | 13.3 ± 1.2 | 13.33 ± 1.15 (12/14/14) | ✅ |
| Argmin K=10 Object (n=6) | 12.3 ± 2.6 | matches framing seeds 42–47 = 12/17/13/12/10/10 | ✅ |
| K=20 obs_only Object | 18.8 ± 1.0 (4 seeds) | registry has 4 K=20 Object seeds (42/43/44/45) | ✅ |
| K=20 obs_only Spatial | 34.3 ± 0.6 (3 seeds) | registry has 3 K=20 Spatial seeds (42/43/44) | ✅ |

### ⚠️ Possible issues — flag for author review

#### 3.1 VLA-only Object baseline — paper uses 11.0 in Table 1 but 10.9 in Table 2

- `experiments.tex` Table 1 (`tab:main`): `VLA-only ... 11.0 ± 1.3 (n=8)`.
- `experiments.tex` Table 2 (`tab:adaptive`) footnote: `VLA-only ... 10.9 ± 1.4 (n=8)` with footnote `^‡` "Seed set differs from Table~\ref{tab:main}".
- `appendix.tex` `tab:k_ablation`: `VLA-only ... 11.0 ± 1.3`.
- `paper_framing.md` headline: `10.8 ± 1.3 (n=9)`.

Three subtly different baselines coexist (10.8 / 10.9 / 11.0). The Table 2 footnote already discloses the seed-set difference, so this is documented, not a bug — but reviewers will notice. Confirm the +7.3 pp improvement in the Abstract / Intro uses the **same baseline** as Plan A's denominator (18.3 − 11.0 = 7.3 — checks out for Table 1 baseline).

#### 3.2 Spatial Plan A "fast path" column contradicts main-text trigger rate — likely a typo

- `introduction.tex` L17: "CRM triggers on 83.7 % of Object steps but **97.6 %** of Spatial steps".
- `experiments.tex` L69: "83.7 % on Object (16.3 % fast-path steps) and **97.6 %** on Spatial".
- `appendix.tex` `tab:adaptive_spatial` Plan A row: `fast path (%) = 84`.

If Spatial Plan A's CRM trigger rate is 97.6 %, fast-path should be **2.4 %**, not 84 %. The "84" value in the appendix table is inconsistent with both the intro and the experiments-section claim (and is exactly the complement of Object's 16.3 % — looks like a transposition).

**Action required:** Confirm which is correct (97.6 % trigger or 16 % trigger) and fix the other location. The figure plus narrative imply Spatial = "correction is almost universally beneficial", which supports 97.6 % trigger → **appendix Table 3 cell should be 2.4, not 84**.

#### 3.3 Spatial CRM K=10 — paper Table 1 says 34.4 ± 1.5 (n=3), framing says 34.5 ± 1.5 (n=9)

`tab:main` reports `34.4 ± 1.5 (n=3)`. Registry has many Spatial CRM K=10 seeds with success_rate values (36/34/35/35/33/36 etc.), and `paper_framing.md` lists 34.5 ± 1.5 with n=9. The Table 1 number is internally consistent with a 3-seed sub-selection but reviewers may ask why n=3 was chosen when more seeds exist. Either widen to all seeds or add a short footnote justifying the seed sub-selection (paired-seed comparison to other rows).

---

## 4. π_0.5 Section Audit (USER PRIORITY)

### 4.1 Current π_0.5 presence in paper

Three locations:
1. `experiments.tex` L107 (end of §4): one-sentence pointer — "We further validate cross-VLA generalization on $\pi_{0.5}$ (3.6B); see Appendix~\ref{sec:cross_vla}."
2. `appendix.tex` §F (`sec:cross_vla`, L179–199): full subsection with Table 6 (`tab:cross_vla`).
3. **No mention in Abstract, Introduction headline, Conclusion, or main Results.**

### 4.2 What's present in Table 6 (`tab:cross_vla`)

```
π_{0.5} VLA-only  K=1  81.5 ± 0.5  84.2 ± 1.0   ← FILLED ✅ (matches registry)
π_{0.5} Plan A    K=2  ---         ---           ← PLACEHOLDER ✗
```

`\placeholder{}` expands to `---` (defined in main.tex L15). Both Plan A cells, and the final prose sentence ("Plan~A results are pending (\placeholder{})"), are placeholders.

### 4.3 Registry status for π_0.5

| Run | seeds DONE | conclusion |
|---|---|---|
| `eval-pi05-vla-only-object-{42,43,44}-r3` | 3 | success ✅ |
| `eval-pi05-vla-only-spatial-{42,43}-r3` + `{45}` | 3 | success ✅ |
| `eval-pi05-plan-a-*` | **0** | **none** ✗ |
| `eval-pi05-adaptive-*` | **0** | **none** ✗ |
| `eval-pi05-crm-*` | **0** | **none** ✗ |

**No π_0.5 Plan A or CRM evaluation exists in registry yet.** Paper is honest about it (placeholders are explicit), but the gap is unresolved.

### 4.4 Cross-VLA seed-set inconsistency

π_0.5 Object uses seeds **{42, 43, 44}**. π_0.5 Spatial uses seeds **{42, 43, 45}** (seed 44 spatial runs all `failed`). Either rerun seed 44 Spatial, or add a footnote acknowledging the substitution. Minor but easy to flag in review.

### 4.5 Locations that will need π_0.5 results written in if/when they land

Priority order (highest impact first):

| # | Location | Current state | Insert if Plan A π_0.5 succeeds |
|---|----------|---------------|---------------------------------|
| **1** | `appendix.tex` Table 6 (`tab:cross_vla`) Plan A row | 2 × `\placeholder{}` | Replace with SR ± std, both Object and Spatial |
| **2** | `appendix.tex` L199 trailing prose | "Plan A results are pending (---)" | Rewrite as 1–2 sentences interpreting the headroom result and whether Plan A still adds gain on a high-baseline VLA |
| **3** | `experiments.tex` L107 (the pointer sentence) | One sentence forward-reference | Add 1 clause stating headline π_0.5 finding (e.g., "with a similar relative improvement of X pp" or "with no significant improvement, consistent with the limited headroom from 81–84 % baselines") |
| **4** | `abstract.tex` | No π_0.5 mention | Optional 1 clause if result is positive — supports the cross-VLA generalisation claim |
| **5** | `discussion.tex` Limitations | "real-robot transfer and larger VLAs are untested" | If π_0.5 (3.6B) is tested, soften "larger VLAs" → "production-scale VLAs beyond 3.6B" |
| **6** | `appendix.tex` Table 6 caption | Mentions "n=3 seeds" generically | If Plan A uses a different seed set, document it (per §4.4) |

### 4.6 Risk if π_0.5 Plan A never lands by DDL

The paper is **publishable as-is** with placeholders removed:
- Drop the `\placeholder{}` row, keep only π_0.5 VLA-only baseline as a forward-pointing observation about headroom limits.
- Trim L199 prose to "Plan~A evaluation on $\pi_{0.5}$ is left to future work."
- Drop the L107 forward-reference, or rewrite as "We profile the VLA-only baseline of $\pi_{0.5}$ in Appendix~\ref{sec:cross_vla} to characterise headroom for inference-time correction on larger flow-matching VLAs."

This avoids shipping a visible "---" in a table.

---

## 5. Cross-cutting issues / minor

- `appendix.tex` L194 row contains math (`$\pi_{0.5}$`) plus `\placeholder{}` — fine.
- The hyperref "math shift in PDF string" warnings are caused by `$K{=}10$` and `$\pi_{0.5}$` in section/caption titles routed into the PDF bookmark string. Cosmetic only.
- `\bibliography{references}` uses default style; `corlabbrvnat.bst` is in the directory and works. No action.
- `main.bbl` was committed (good for reviewer reproducibility) and matches the regenerated version.

---

## 6. Summary scoreboard

| Area | Status |
|------|:------:|
| LaTeX compiles | ✅ |
| All citations resolve | ✅ |
| All figures resolve | ✅ |
| Headline numbers (Plan A, π_0.5 baseline) verified vs registry | ✅ |
| Adaptive-K threshold sweep (Object) verified seed-by-seed | ✅ |
| **Spatial Plan A trigger rate vs fast-path: contradiction** | ⚠️ §3.2 |
| **π_0.5 Plan A row blank (2 placeholders)** | ⚠️ §4.2 |
| π_0.5 Spatial uses seed 45 instead of 44 | ⚠️ §4.4 |
| Three different VLA-only Object baselines coexist (10.8/10.9/11.0) | ⚠️ §3.1 |
| Spatial CRM K=10 n=3 vs framing n=9 | ⚠️ §3.3 |

**Submission-blocking:** None. **Reviewer-bait items:** §3.2 (factual contradiction) and §4.2 (visible placeholder in Table 6). Prioritise fixing §3.2 before submission; §4.2 either fill in with π_0.5 Plan A results or drop the row.

Audit produced read-only — no paper files modified.
