# Paper Patch Audit — D047 (Yi-1.5 FAIL) + D048 (concentration verification)

> Generated: 2026-05-14
> Status: D047 confirmed, D048 pending (float32 rerun in progress)

---

## Overview

The paper currently covers **3 models** (Qwen, Llama, Mistral). The `paper_framing.md` and ROADMAP describe **5 models** including Yi-1.5-9B and Gemma-2-9B. The primary patches are:

1. Expand 3→5 models throughout all text/tables
2. Add Yi-1.5 as GQA counterexample (D047) — highest GQA (8:1) but FAILS
3. Add Gemma-2 as low-heterogeneity anchor
4. Add "spike vs spread" distribution shape analysis
5. Update concentration values if D048 float32 < original bf16 numbers
6. Update/revalidate 0.50 threshold diagnostic

---

## Claim 1 — GQA ratio → heterogeneity

**Current paper status**: The paper does NOT explicitly claim "GQA ratio predicts heterogeneity" — it lists GQA ratios descriptively in model specs and Table 6. However, with only 3 models (GQA 7:1, 4:1, 4:1), there's an implicit monotonic pattern. Adding Yi-1.5 (8:1, FAIL) breaks this and requires explicit discussion.

**paper_framing.md Claim 1**: "Head sensitivity heterogeneity is architecture-dependent and determined by sensitivity *distribution shape*, not GQA ratio alone"

### Patch locations

- [ ] `introduction.tex:39-40` — "On our three architectures, the concentration metric---combined with the absolute magnitude of per-head distortion---separates the beneficial case (Qwen, concentration 0.59--0.66, 27.3\% PPL improvement) from cases where non-uniform allocation provides marginal (Llama) or no benefit (Mistral), across the three tested architectures." — **Need to expand to 5 architectures, add Yi-1.5 (FAIL despite highest GQA) and Gemma-2 (strongest negative). Must add explicit statement that GQA ratio is not a reliable proxy — Yi-1.5 (8:1) counterexample.**

- [ ] `introduction.tex:47-49` — Contribution 3: "We propose a heterogeneity-based diagnostic framework that can indicate whether non-uniform allocation will help a given architecture, validated on three models spanning beneficial, marginal, and counterproductive outcomes" — **Change "three models" to "five models"; add Yi-1.5 as GQA counterexample role.**

- [ ] `analysis.tex:11` — "Table~\ref{tab:heterogeneity} summarizes the results across three architectures at $4\times$ compression." — **Change to five architectures.**

- [ ] `analysis.tex:12-16` — "Qwen2.5-7B exhibits the highest heterogeneity (top-5\% concentration 0.59--0.66)...Llama-3.1-8B shows moderate heterogeneity (0.34--0.59)...Mistral-7B-v0.3 has a concentration of 0.42..." — **Add Yi-1.5 (0.49, spike pattern) and Gemma-2 (0.23, uniform). Add spike vs spread discussion: Yi-1.5 has highest GQA (8:1) but concentration only 0.49 because its heterogeneity is a single-outlier "spike" (L4H3, 34% of total delta) rather than a "spread" cluster like Qwen's Layer-0.**

- [ ] `analysis.tex:18-33` — Table 6 (`tab:heterogeneity`): Only has 3 rows (Qwen, Llama, Mistral). — **Add rows for Yi-1.5-9B (GQA 8:1, Top-5% 0.49, MCKP -1.3%, Recommendation: Uniform/Negative) and Gemma-2-9B (GQA 2:1, Top-5% 0.23, MCKP -0.3%, Recommendation: Uniform).**

- [ ] `analysis.tex:42-43` — "The contrast is stark: Qwen's Layer-0 heads show high distortion...Mistral shows uniformly low distortion..." — **Add Yi-1.5 contrast: high GQA but "spike" pattern, and Gemma-2: lowest GQA and most uniform. Consider updating heatmap figure to include 5 models.**

---

## Claim 3 — concentration threshold diagnostic (0.50)

**paper_framing.md Claim 3**: "Top-5% > 0.50 correctly classifies all 5 models tested (n=5, 5/5 accuracy)"

**D048 dependency**: Qwen hires concentration currently reported as 0.59-0.66. If D048 float32 rerun shows < 0.50, the threshold and Qwen's "above threshold" status collapse. The 0.50 threshold is currently 5/5 correct only if Qwen stays above 0.50.

### Patch locations

- [ ] `analysis.tex:55` — "Concentration ${>}\,0.50$: non-uniform allocation recommended (Qwen case; 27.3\% PPL improvement)." — **D048 >0.50: keep threshold, update concentration value to float32 number, strengthen with 5/5 classification. D048 <0.50: must restructure diagnostic — possibly lower threshold, switch to continuous relationship framing, or use different metric.**

- [ ] `analysis.tex:56-58` — "Concentration $0.30$--$0.50$: marginal benefit...Near-zero absolute distortion..." — **Update ranges to accommodate 5 models. Yi-1.5 at 0.49 sits just below 0.50 threshold — this is the critical boundary case that validates the threshold.**

- [ ] `analysis.tex:63` — "The thresholds above are derived from three architectures and should be validated on a broader set" — **Change to five architectures. With 5/5 classification accuracy, can strengthen language slightly (still directional, not statistical).**

- [ ] `introduction.tex:39-40` — "concentration 0.59--0.66" — **Update to D048 float32 value if changed.**

- [ ] `conclusion.tex:6` — "Qwen2.5-7B (concentration 0.59--0.66)" — **Update to D048 float32 value if changed.**

---

## Numerical Updates (pending D048)

### Concentration values

- [ ] `introduction.tex:40` — "concentration 0.59--0.66" — **Pending D048 float32 result**
- [ ] `analysis.tex:12` — "top-5\% concentration 0.59--0.66" — **Pending D048 float32 result**
- [ ] `analysis.tex:28` — Table 6: "0.59--0.66" in Qwen row — **Pending D048 float32 result**
- [ ] `conclusion.tex:6` — "concentration 0.59--0.66" — **Pending D048 float32 result**

### If D048 concentration drops significantly (e.g. to ~0.42)
- [ ] All 0.50 threshold references become invalid
- [ ] `analysis.tex:55` — threshold needs lowering or removing
- [ ] `paper_framing.md` Claim 3 needs full restructure
- [ ] Yi-1.5 (0.49) and Qwen would both be near same concentration but with opposite outcomes → need alternative explanation (e.g., absolute distortion magnitude, not just concentration)

---

## Model Count Updates (3→5)

### abstract.tex
- [ ] `abstract.tex:5` — "The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures" — **Change "three" to match actual solver-equivalence scope (may stay 3 if solver equivalence only tested on original 3).**
- [ ] `abstract.tex:6` — "on Llama-3.1-8B the improvement is marginal...on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive" — **Add Yi-1.5 and Gemma-2 negative results to this enumeration.**
- [ ] `abstract.tex:7` — "We propose a heterogeneity diagnostic..." — **Add "validated on five architectures" or similar.**

### introduction.tex
- [ ] `introduction.tex:28` — "all 112 heads receive the same bit-width on Qwen2.5-7B, all 256 on Llama-3.1-8B, and 255 of 256 on Mistral-7B-v0.3" — **If solver equivalence tested on Yi-1.5/Gemma-2, add those. Otherwise leave as-is (this is solver equivalence, not heterogeneity).**
- [ ] `introduction.tex:32-36` — "On Llama-3.1-8B, constrained MCKP achieves 8.45...On Mistral-7B-v0.3, it is slightly worse: 7.16 vs. 7.13." — **Add Yi-1.5 (-1.3%) and Gemma-2 (-0.3%) negative results.**
- [ ] `introduction.tex:44-45` — Contribution 1: "reducing Qwen2.5-7B PPL from 32--37 (unconstrained) to 11.23" — **OK as-is (Qwen-specific claim).**
- [ ] `introduction.tex:46-47` — Contribution 2: "across three architectures" — **Update if solver equiv tested on more models.**
- [ ] `introduction.tex:47-49` — Contribution 3: "validated on three models" — **Change to five models.**

### experiments.tex
- [ ] `experiments.tex:8-11` — "We evaluate on three architectures spanning different grouped-query attention (GQA) configurations: Qwen2.5-7B (GQA ratio 7:1...), Llama-3.1-8B (4:1...), and Mistral-7B-v0.3 (4:1...)" — **Expand to five: add Yi-1.5-9B (8:1, 48 layers × 4 KV heads = 192 KV heads) and Gemma-2-9B (2:1, 42 layers × 8 KV heads = 336 KV heads). This now spans GQA 2:1 to 8:1.**
- [ ] `experiments.tex:38-53` — Table 2 (`tab:main_results`): 3 rows → **Add Yi-1.5-9B (baseline=7.22(?), uniform=7.22, MCKP=7.31, -1.3%) and Gemma-2-9B (baseline, uniform, MCKP -0.3%). Need exact numbers from registry.**
- [ ] `experiments.tex:55-69` — Main results text: "On Qwen...On Llama...On Mistral..." — **Add paragraphs for Yi-1.5 and Gemma-2 results.**
- [ ] `experiments.tex:69` — "Unconstrained results for Llama and Mistral are omitted" — **Extend to include Yi-1.5 and Gemma-2.**
- [ ] `experiments.tex:113-128` — Table 4 (`tab:heuristic`): 3 rows — **Add Yi-1.5 and Gemma-2 if heuristic baselines were run on them. If not, note in text.**
- [ ] `experiments.tex:116` — "All methods use per-model optimal $k$..." — **Add Yi-1.5 and Gemma-2 optimal k values.**
- [ ] `experiments.tex:177` — "All three models show ${>}96\%$ bit-assignment agreement" — **Update if cross-dataset run on 5 models. Otherwise note scope.**

### analysis.tex
- [ ] `analysis.tex:11` — "across three architectures" — **five architectures**
- [ ] `analysis.tex:18-33` — Table 6 (`tab:heterogeneity`): 3 rows → **5 rows**
- [ ] `analysis.tex:48` — "based on three architectures" in diagnostic — **five architectures**
- [ ] `analysis.tex:63` — "derived from three architectures" — **five architectures**

### conclusion.tex
- [ ] `conclusion.tex:5` — "across all three architectures ($\Delta = 0.0000$)" — **Keep 3 if solver equiv only on 3, but add parenthetical about 5-model heterogeneity validation.**
- [ ] `conclusion.tex:6-7` — "Qwen2.5-7B (concentration 0.59--0.66) shows large gains, Llama-3.1-8B (0.34--0.59) shows marginal improvement (8.45 vs. 8.47 PPL), and Mistral-7B-v0.3 (0.42) is slightly counterproductive (7.16 vs. 7.13 PPL)." — **Add Yi-1.5-9B (0.49, -1.3%) and Gemma-2-9B (0.23, -0.3%). Highlight Yi-1.5 as GQA counterexample.**
- [ ] `conclusion.tex:11` — "we evaluate only three 7B-scale models" — **Change to five 7-9B-scale models. Limitation about n=5 still valid but strengthened.**

### appendix.tex
- [ ] `appendix.tex:6-8` — Aggressive compression mentions Llama and Mistral only — **Add Yi-1.5 and Gemma-2 aggressive compression results if available.**

---

## Yi-1.5 Specific Additions

Yi-1.5-9B is entirely absent from the current paper. Needed additions:

- [ ] `experiments.tex:8-11` — Add to model list: "Yi-1.5-9B (8:1, 48 × 4 = 192 KV heads)"
- [ ] `experiments.tex` Table 2 — Add row with Yi-1.5 numbers
- [ ] `experiments.tex` main results text — Add paragraph: Yi-1.5 (GQA 8:1, highest in lineup) achieves -1.3% vs uniform, a genuine negative result despite having the highest GQA ratio
- [ ] `analysis.tex` Table 6 — Add row: Yi-1.5, 8:1, 0.49, negative, Uniform
- [ ] `analysis.tex:12-16` — Add spike vs spread discussion: Yi-1.5's L4H3 is a single extreme outlier (34% of total delta, CV=4.79) but MCKP cannot exploit a spike; Qwen's L0 cluster of 4 heads (26× dominance) creates a "spread" that enables differentiated allocation
- [ ] `analysis.tex:42-43` — Add Yi-1.5 to heatmap description or add new figure panel
- [ ] `analysis.tex:48-58` — Update diagnostic: Yi-1.5 (0.49) falls just below 0.50 threshold and correctly classified as negative
- [ ] `introduction.tex:32-36` — Add Yi-1.5 negative result after Mistral paragraph
- [ ] `introduction.tex:35` — "The difference across architectures traces to head sensitivity heterogeneity" — **Strengthen: add that GQA ratio alone does not predict benefit (Yi-1.5 counterexample). Distribution shape matters.**
- [ ] `abstract.tex:6` — Add Yi-1.5 to negative results enumeration
- [ ] `conclusion.tex:6-7` — Add Yi-1.5 to results summary, highlight as counterexample
- [ ] **NEW SUBSECTION or paragraph needed**: "Spike vs Spread" analysis explaining why Yi-1.5 (8:1) fails while Qwen (7:1) succeeds. Best location: `analysis.tex` after heterogeneity characterization (§5.1), as a new §5.1.1 or integrated into §5.1.

---

## Gemma-2 Specific Additions

Also absent. Needed additions:

- [ ] `experiments.tex:8-11` — Add to model list: "Gemma-2-9B (2:1, 42 × 8 = 336 KV heads)"
- [ ] `experiments.tex` Table 2 — Add row with Gemma-2 numbers (baseline ~9.03(?), MCKP -0.3%)
- [ ] `experiments.tex` main results text — Add paragraph: Gemma-2 has lowest heterogeneity (0.23), strongest negative anchor
- [ ] `analysis.tex` Table 6 — Add row: Gemma-2, 2:1, 0.23, negative, Uniform
- [ ] `conclusion.tex:6-7` — Add Gemma-2 to results summary

---

## Figures

- [ ] `figures/fig1_head_delta_heatmap.pdf` — Currently 3 panels (Qwen, Llama, Mistral). **Need to add Yi-1.5 and Gemma-2 panels** (5-panel figure, possibly rearranged).
- [ ] Consider adding a new figure: scatter plot of Top-5% concentration vs MCKP improvement across 5 models, with 0.50 threshold line. This would visually anchor Claim 3.

---

## Summary Priority

| Priority | Category | Items | Blocker |
|----------|----------|-------|---------|
| **P0** | D048 concentration values | 4 locations | D048 result |
| **P0** | 0.50 threshold diagnostic | 3 locations | D048 result |
| **P1** | Yi-1.5 additions (D047) | ~12 locations | None (data ready) |
| **P1** | Gemma-2 additions | ~5 locations | None (data ready) |
| **P1** | 3→5 model count | ~15 locations | None |
| **P2** | Spike vs spread analysis | 1 new section/paragraph | None |
| **P2** | Figure updates | 1-2 figures | None |
| **P3** | Solver equiv scope note | 2-3 locations | Whether solver equiv tested on Yi-1.5/Gemma-2 |
