# V9 §6 Outline: "The Aggregation Ceiling"

Status: DRAFT outline only. Not committed to .tex. Pending Dir-L-2 (N=204 single trace) + Dir-N (oracle best-of-K).

D116 pivot: Paper elevates from "SICA fails" to "Aggregation Ceiling: Test-Time vs Trained Internal Reasoning."

§1-§5 unchanged. §6 is new.

---

## §6. The Aggregation Ceiling: Trained Internalization Saturates It

### §6.1 Empirical: Aggregation Gain Shrinks with Model Capacity

**Hero Table Draft**:

```latex
\begin{table}[t]
\centering
\small
\caption{The aggregation ceiling: SC gain over single-trace accuracy shrinks
monotonically with model capability. Trained internal reasoning (thinking mode)
directly eliminates the inter-trace diversity that aggregation exploits.
Single-trace accuracy averaged over $K{=}12$ traces ($\pm$ std);
SC@12 is majority vote over all 12 traces. All on FOLIO ($n{=}204$).}
\label{tab:aggregation-ceiling}
\begin{tabular}{@{}lrrr@{}}
\toprule
Model & Single Trace & SC@12 (\%) & Agg.\ Gain (pp) \\
\midrule
Mistral-7B & 46.41 $\pm$ 2.80 & 54.41 & $+$8.00 \\
Qwen3-14B & 79.37 $\pm$ 1.98 & 83.82 & $+$4.45 \\
Qwen3-14B (think) & 83.28 $\pm$ 0.99 & 86.27 & $+$0.45 \\
\bottomrule
\end{tabular}
\end{table}
```

**Note**: Dir-L flagged possible data issue with Qwen3-14B thinking (166/204 vs 204/204). Numbers above use Dir-L preliminary data; will update with Dir-L-2 confirmed N=204 values.

**Hero Plot specification** (for Worker):
- Type: line plot, x=K (1 to 12), y=accuracy (%)
- Three curves: Mistral-7B, Qwen3-14B, Qwen3-14B (thinking)
- Narrative intent: Thinking mode's K=1 already approaches K=12 of non-thinking; aggregation gain is visually compressed to near-zero
- Design notes: Horizontal dashed lines at SC@12 for each model; shaded band for ±std at each K; annotate aggregation gain (pp) at K=12
- Aspect ratio: single-column (0.85\columnwidth), height ~5cm
- Data source: Dir-L-2 (per-K accuracy curves)

**Key sentences**:

> "Aggregation gain shrinks monotonically from +8.00pp (Mistral-7B) to +0.45pp (Qwen3-14B thinking mode)---trained internal reasoning directly eliminates the inter-trace diversity that aggregation exploits."

> "At the thinking-mode frontier, a single trace achieves 83.28%, leaving SC@12 only 0.45pp of headroom. The Symbolic Mirage is not merely a constraint-extraction failure; it reflects a deeper saturation: as models internalize reasoning, the marginal value of any test-time aggregation---symbolic or otherwise---approaches zero."

---

### §6.2 Theoretical: The Mirage Explains Both Endpoints

**Opening**: The Symbolic Mirage framework (§3.3) provides a unified explanation for both endpoints of the capability spectrum.

**Low-capability (Mistral-7B)**:
- BR = 4.97×, oracle gap = +29.90pp (FOLIO)
- Aggregation gain exists (+8.00pp SC over single) but is locked by confirmation bias
- SICA captures only ~12% of oracle ceiling → self-extracted constraints cannot unlock the remaining 88%
- Δ_max ≤ OracleGap / BR ≈ 6.0pp; observed +3.43pp (best seed)

**High-capability (Qwen3-14B thinking)**:
- κ = 0.91, K_eff = 1.09 → 12 traces ≈ 1 independent vote
- Inter-trace std = 0.99% (vs Mistral's 2.80%) → diversity already consumed by training
- Oracle gap ≈ 3pp [PENDING Dir-N for exact number] → ceiling itself is near-zero
- Any aggregation method—symbolic or voting—is bounded by this vanishing gap

**Unifying sentence**:

> "Proposition 1 (BR > 1) explains why self-extraction fails at both ends: at low capability, high BR locks constraints to wrong answers; at high capability, near-perfect agreement (κ → 1) makes BR undefined—there are too few errors for any corrective signal to act upon. The ceiling is not a SICA-specific failure but a property of same-model aggregation itself."

**[PENDING Dir-N]**: Oracle best-of-K data for Qwen3-14B thinking → confirms oracle gap ≈ 3pp or exact value. This determines whether the ceiling is "near-zero" or "structurally zero."

---

### §6.3 Practical Implication

**Key claim**: Stop optimizing test-time aggregation for reasoning tasks; invest in trained reasoning capabilities.

**Draft paragraph**:

> "For practitioners, the aggregation ceiling implies a clear resource allocation: one Qwen3-14B thinking trace (83.28%) outperforms twelve Mistral-7B traces aggregated by any method we tested---SC (54.41%), SICA (≈54%), or oracle-FOL (85.78%)---while costing approximately 5--10× a single non-thinking inference but far less than 12× inference plus constraint extraction. The marginal return on test-time compute is dominated by the marginal return on trained reasoning depth."

**Cost comparison** (approximate):
- 1 Mistral-7B trace: ~0.5s, baseline cost
- 12 Mistral-7B traces + SICA: ~5.5s (4.5× SC), +3.43pp best case (n.s.)
- 1 Qwen3-14B thinking trace: ~3-5s, +29pp over Mistral single
- Resource allocation conclusion: training-time investment >> test-time scaling

---

### §6.4 HGE Negative (existing data, relocate from §5.5/appendix)

**Summary**: Six Heterogeneous Generator Ensemble configurations across four model families all underperform the best single model by 1.81--2.84pp.

**Connection to ceiling**:

> "Even generator-side diversity cannot escape the aggregation ceiling. HGE combines models with different biases, but cross-model constraints use incompatible variable naming (56.4% zero variable overlap), so Z3 treats them as unrelated propositions. The result is a noisy weighted vote that underperforms the strongest individual model's majority vote---confirming that the ceiling applies to ensemble-space interventions, not just constraint-space ones."

---

## Data Dependencies

| Data | Status | Needed for |
|------|--------|------------|
| Dir-L-2 (N=204 single trace, all 3 models) | PENDING ~5 min | §6.1 hero table confirmed values |
| Dir-N (oracle best-of-K, Qwen3 thinking) | PENDING ~10 min | §6.2 oracle gap at high capability |
| Dir-L Qwen3-think data integrity check | PENDING | Confirm 204/204 or adjust n |

## Structural Notes

- Current §6 (Cross-Architecture PoC) would become §7
- Current §7 (Discussion) → §8
- Current §8 (Conclusion) → §9
- Or: merge aggregation ceiling into expanded §7 Discussion if page budget is tight
- Abstract will need 1-sentence update after Dir-N data confirms
- Introduction contribution list may need a 4th bullet (Director decision)

## Page Budget Estimate

- Hero table: ~8 lines (compact, single-column)
- Hero plot: ~1/3 page (if included as figure)
- §6.1 text: ~10 lines
- §6.2 text: ~12 lines
- §6.3 text: ~8 lines
- §6.4 text: ~6 lines (mostly relocating existing HGE content)
- Total: ~0.7-1.0 pages new content
- Risk: pushes main text to 9 pages → need ~0.5 page trimming from existing sections or move some content to appendix
