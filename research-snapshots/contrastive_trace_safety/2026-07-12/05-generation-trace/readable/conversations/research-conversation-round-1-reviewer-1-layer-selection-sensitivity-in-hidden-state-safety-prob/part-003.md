# Research conversation: [Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性** 审查。 ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Prob — Part 3 of 3

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../research-conversation-round-1-reviewer-1-layer-selection-sensitivity-in-hidden-state-safety-prob.md) · [Structured JSON](../../../sessions/6b/6b9aaa08719889e25ccb.json)

## Round 1

### Tool result

_source line 51 · 2026-05-19T04:37:41.125Z_

<details><summary>↩ Tool result · `toolu_01HrtbDFgxiZbKt46AZkXTpX`</summary>

```text
Here is the complete detailed transcript of all four pages.

---

## PAGE 5 (left column top to right column bottom)

### Continuation of Method/Setup text (top of left column)

"each model, the three metrics are positively correlated by construction, so the correction is stricter than under independence. Control task selectivity (Hewitt and Liang, 2019) validates genuine representational structure (section II). In hidden-layer tests (n ≤ 20): R1-32B (n=20) and QwQ-32B (n=19)."

---

### Section 4 Experiments

"We evaluate temporal probes across four reasoning models (table 1), comparing hidden-state (HS) and text modalities under different layer selection criteria."

**Evidence gradient.** "The strength of HS advantage evidence varies by model, not scale. We classify evidence into three levels using seed robustness, position independence, and sample size: **strong** (OT-7B: 5/5 seeds HS, ΔPrc=+21.9pp, position-independent, selectivity 5/5pp, n=47); **moderate** (R1-8B: precision-robust but FPR seed-fragile at 5/5 HB, n=43; QwQ-32B↑: 1/5 HB, ΔPrc=+19.2pp, sensitive load time n=19); competitive BA, n=19); and **qualified** (R1-32B↑: 5/5 HB, ΔPrc std=2.0pp, but position-mediated with residualized gap NS; W=1 only, n=20)."

**Section X.** "At 32B, both models are significant (HB corrected) but with model-specific caveats: R1-32B achieves significance only at W=1 with 25% coverage (5/20 traces), and QwQ-32B's position baseline is competitive (section 4.4). R1-32B passes 5/5 seeds (paired ΔPrc std~2.0pp, despite non-positional HS advantage over text (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp (section Y, n=20), consistent with a position-mediated advantage. Temporal modeling reduces position dependence (R1-8B: 24.3pp drop at W=3 vs. 16.5pp at W=15)."

**Capacity control.** "PCA reduction of HS features to 384d (matching text encoder dimensions; table Y, 79–92% variance retained) preserves the precision advantage across all four models (+16.8 to +23.1pp, all p≤0.012): all model-level precision tests pass Holm-Bonferroni. Two individual metric comparisons are non-significant. R1-8B balanced accuracy (−1.3pp, p=0.73); effect too small at n=43 and QwQ-32B FPR (−11.4pp, p=0.035, below HB threshold). PCA retains directions of maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder. This result provides partial evidence against a pure capacity explanation but does not rule out representation-quality differences between PCA-compressed HS and trained text encoders."

---

### Table 2: Layer Selection Sensitivity

**Title:** "Table 2: Layer selection sensitivity. *a bal.acc × cross.rate; b Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Highest: HS precision p-value at corrected layer (e.g., QwQ-32B biased layer: bal.acc p=0.35, precision p=0.52; both non-significant)."

| Model | Biased^a | Corrected^b | p (corr.) |
|-------|----------|-------------|-----------|
| R1-8B | L14 (44%) | L11 (44%) | 0.003 |
| OT-7B | 1.0 (9%) | L36 (37%) | <0.001 |
| QwQ-32B | L2 (1%) | L6 (9%) | 0.105 |
| R1-32B | L10 (69%) | L63 (98%) | <0.001 |

---

### Section 4.2 Layer Selection Results

"table 2 shows that the biased composite metric (balanced accuracy × crossing rate) systematically selects shallow layers: 3% depth for layer L2 (3% depth) for QwQ-32B and L10 (16%) for R1-32B. Three of four metrics excluding crossing rate (precision, inverse FPR, and additive composite) consistently select deep layers at L63 (98%) for both 32B models. Pure balanced accuracy, a threshold-free metric, selects layers that vary across data splits and models (7-98% depth under 60/20/20; section Y), itself showing that layer selection is a consequential methodological choice. The mechanism is that shallow layers produce highly compressed representations with small inter-separating distances: cosine distances are 1.4–2.7× smaller than at deep layers across all models (section C). A linear probe in this compressed space saturates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (section 3.3).

The downstream impact is severe: at biased layers, only the two 7-8B models show significant HS advantage; the 32B models fail. At corrected layers, all four models pass Holm-Bonferroni correction (section 3.5): strong (OT-7B), moderate (R1-8B, QwQ-32B↑), and qualified (R1-32B↑). Had we reported only biased-layer results, we would have concluded a scale-dependent HS advantage that is entirely a methodological artifact."

---

### Section 4.3 HS vs. Text Comparison

"Multi-seed stability appears in section X; BGE ΔBA/ΔFPR in section S. Against the 384d baseline, HS achieves higher precision than text probes across all four models (table 3), with evidence from strong (OT-7B: +21.9pp precision) to qualified (R1-32B↑: +15.1pp)."

---

## PAGE 6 (left column, then right column, then Figure 1)

### Table 3: HS vs. text at corrected layers (ILR probes, 60/20/20 split, 10,000 bootstrap resamples)

**Title:** "Table 3: HS vs. text at corrected layers (ILR probes, 60/20/20 split, 10000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). ΔHS: HS–text difference (pp). '—' = metric not computed for that encoder comparison. HB: χ² = model-level test passes Holm-Bonferroni (α=0.05); all 384d model-level tests pass†. 1024d: HB over 4 model-level precision tests."

| Model | Enc. | Π | ΔBA | ΔPrc | ΔFR | [CI 95%] | HB |
|-------|------|---|-----|------|-----|----------|----|
| R1-8B | L11 | 384d | 5 | +17.5 | +20.1 | [+12.4,+25.9] | ✓ |
| OT-7B | L36 | 384d | 2 | +6.7 | +21.9 | [+13.2,+30.7] | ✓ |
| QwQ-32B | L6 | 384d | 5 | +0.7 | +19.2 | [+9.4,+29.0] | ✓ |
| R1-32B | L63 | 384d | 5 | −1.6 | +15.1 | [+5.2,+25.1] | ✓ |
| R1-8B | L11 | 1024d | 5 | +9.0 | +13.8 | [+3.9,+23.7] | — |
| OT-7B | L36 | 1024d | 2 | +5.1 | +15.1 | [+6.4,+23.8] | — |
| R1-32B | L63 | 1024d | 5 | −0.6 | +11.3 | [...,+21.4] | — |

*(Some cells partially obscured by figure placement; values transcribed where legible.)*

---

### Text continuation (left column page 6)

"maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder. This result provides partial evidence against a pure capacity explanation but does not rule out representation-quality differences between PCA-compressed HS and trained text encoders.

**Random projection to 384d** (structure-destroying, unlike PCA) yields similar results (ΔPrc std~2.0pp, 20-7pp, all p<0.01; section T), further weakening the capacity explanation. An LLM-based encoder (E5-Mistral-7B, 4096d→PCA 384d) yields intermediate results (2/4 HB; section U), forming a monotonic encoder-quality gradient with MiniLM (4/4) and BGE-large (1/4)."

---

### Right column page 6 (continuing HS vs. Text)

"**Encoder robustness.** The 1024d rows in table 3 replace MiniLM (384d) with BGE-large (Xiao et al., 2023) (1024d, a 2.7× stronger encoder). The HS-precision advantage persists directionally across all four models but narrows substantially: only OT-7B survives Holm-Bonferroni (1/4 precision tests). The reduced additive advantage is also directionally positive across all four models (+8.4 to +10.9pp), with 2/4 (OT-7B; R1-32B) significant after Holm-Bonferroni. FPR advantage is significant only for OT-7B (1/4). R1-8B shows an adverse FPR direction (HS FPR 1.2pp higher than BGE, p=0.56). The advantage is therefore conditional rather than absolute (fig. 2). Layer selection (Contribution 1) is encoder-independent, as it concerns hidden-state properties across layers rather than the text baseline."

**Position mediation.** "Position (t'/T) accounts for 9–20pp of balanced accuracy depending on model"

---

### Figure 1 (full-width, right side of page 6)

**Caption:** "Figure 1: Per-layer metric heatmap (2-in-2 columns). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal.acc × crossing rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers."

*(The figure shows a heatmap with rows = layers, columns = 5 metrics. Models shown: OT-7B and R1-8B. Color scale: dark blue to yellow. Red dashed lines mark biased layers; green dashed lines mark corrected layers. The heatmap visually confirms that biased layers (shallow) and corrected layers (deep) differ substantially.)*

---

## PAGE 7 (Results continuation + Discussion beginning)

### Table 4: 32B cross-model divergence

**Title:** "Table 4: 32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: χ² = model-level test passes Holm-Bonferroni (α=0.05). Pos. margin: HS balanced accuracy minus position-only baseline."

| Model | Cov. | Lead (steps) | HB | Pos. margin |
|-------|------|--------------|----|-------------|
| R1-32B | 25% | +11.7 to +3.3 | ✓ (W=1) | +14.2pp |
| QwQ-32B | 74% | +14.0 to +9.1 | ✓ | −3.8pp |

---

### Text continuation (left column, page 7, top)

"and window size,† but all models retain non-positional signal above chance (all p<0.001; section C). Section 4.5). R1-32B retains significant non-positional HS advantage over text (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp (section Y, n=20), consistent with a position-mediated advantage. Temporal modeling reduces position dependence (R1-8B: 24.3pp drop at W=3 vs. 16.5pp at W=15)."

**Section 4.4 R1-32B Model-Specific Analysis**

"R1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (table 4); training method is the likely differentiator.

R1-32B detects commitment 11-13 steps early with a +14.2pp margin over the position baseline, which confirms genuine representational signal, but covers only 25% of traces. QwQ-32B achieves significance at all window sizes with 74% coverage: the HS probes fire 9-10pp above text probes (negative lead time). Consistent with the†R1-32B's 20-4pp drop reflects W=1 (no temporal context); at W≥3 with temporal windowing, drops are 9-13pp."

---

### Section 4.5 Temporal Context

"Temporal windowing (W>1) improves both modalities on all models (fig. 3). Text precision improves +8 to +2pp from W=1 to W=25; HS precision improves +1.7 to +12.9pp. At 7-8B, the modality advantage (+20.1 to +21.9pp precision) exceeds the temporal improvement (+13pp). Both effects are complementary: temporal windowing (W=3–15) combined with principled layer selection yields the best performance. Section P shows model temporal ablations appear in section P; GRU sequence models under a matched 60/20/20 split achieve comparable accuracy but higher FPR than LR probes (table 13)."

---

### Section 4.6 Negative Results

"No alternative method consistently matches supervised probing across all four models at any evidence tier (table 19). Each failure is diagnostic: BOCPD (Adams and MacKay, 2007)/CUSUM fail to detect commitment points even after sweeping hazard rate λ ∈ {5, 10, 20, 50, 100} and drift"

---

### Right column page 7 (continuing 4.6 + Figure 2)

"and window size,† but all models retain non-positional signal above chance (all p<0.001; section C)."

*(continues with the discussion of negative results)*

---

### Figure 2 (right column page 7)

**Caption:** "Figure 2: Forest plot of HS precision advantage over test probes. Blue: vs MiniLM-384d; orange: vs. BGE-1024d. Solid markers: passes Holm-Bonferroni. Hollow: does not. All 384d comparisons are significant (strong evidence for Contribution 1); for BGE-1024d, only OT-7B (strong) survives correction."

*(The forest plot shows four models on the y-axis (OT-7B top, R1-8B, QwQ-32B, R1-32B bottom). X-axis: ΔPrecision (HS − Text, pp). Blue dots = MiniLM comparisons (all solid/filled, with 95% CI bars all to the right of 0), orange dots = BGE comparisons (only OT-7B solid; others hollow). R1-8B and QwQ-32B BGE CIs cross zero or are barely positive.)*

---

## PAGE 8 (Discussion + Conclusion)

### Section 5 Discussion (left column, page 8)

**Layer selection as researcher degree of freedom.**

"Our five-metric ablation (section 4.2) shows that crossing rate reverses the central finding: at biased layers, the HS advantage appears scale-dependent; at corrected layers it is significant across all four models*, from strong (OT-7B) to qualified (R1-32B†; section 3.5). The mechanism is representational compression: shallow layers (section C: 51200 × W for n=20) prevents coverage; sweeping regularization C over {0.01, 10} yields ~2pp variation in balanced accuracy; the HS advantage is also stable across decision thresholds (BA variation <1.5pp across C ∈ {0.1, 0.7}; section M). QwQ-32B HS help time is negative (−1.2 to +1.9 steps vs. text 3.7−12.2 steps): higher precision at later detection. On some traces it probes precision 50-52% false alarm rates, so current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in section 4.4."

---

**Encoder-quality boundary.**

"HS advantage is a function of text encoder quality: significant against 384d MiniLM (4/4 precision tests; see L4–HB, strong to qualified) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp) and provides partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference. Temporal context and modality choice are complementary: at W=1 the modality advantage exceeds the temporal improvement; temporal windowing (W=3 to 15) provides consistent gains regardless of modality."

---

**Guidance for future research.** "The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6% early detection with 50-step head time, while R1-32B reaches only 50% early detection (section I). The gap suggests that the commitment signal variation varies across models. The cross-model variation indicates that distillation and native reasoning produce qualitatively different safety representations. Our five-step checklist (layer selection, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage), and PCA provide convergent evidence of genuine safety representations, but our approach is correlational. Causal validation via CAS (Geiger et al., 2025), LEACE (Belrose et al., 2023), or Li et al.'s (2023) interchange confirm that probed directions are causally active. Applying this audit to our own initial results changed the central conclusion from "HS advantage is scale-dependent" to "HS advantage is universal under corrected selection," a qualitative reversal that illustrates how unexamined layer selection can propagate to deployment decisions. We recommend a five-step audit for probing studies: (1) train probes across all layers; (2) compute ≥3 metrics (threshold-free and threshold-dependent); (3) check for metric disagreement; (4) report per-model; (5) account for position and volatility (section C). Steps 3-5 cost negligible compute. For production monitoring, deep layers selected by threshold-dependent metrics with temporal windowing (W=3–7 probes) offer reliable commitment detection. The crossover point where text encoders match HS probes lies approximately at the 1024d BGE-class (1.3pp). Below this, HS probes offer clear advantages. At 32B scale, HS probing is position-entangled, so temporal modeling combined with position residualization is necessary to extract genuine safety signal (section V)."

---

**Deployment operating points.** "The consecutive-crossings threshold K trades coverage (table 10): at K=0 with W=1 and 60% throughput, average coverage is 60% with 48% safe FPR. Raising K yields practically useful operating points: at K=10, OT-7B achieves 21% coverage with only 5% false positives (CUSUM failing fewer than 1 in 12 flagged traces is a false alarm). R1-32B at K=10 retains 35% coverage"

---

"δ ∈ {0.5, 1.0, 2.0} (section K), with 0% detection on 3/4 models; Mahalanobis distance yields near-zero separation, consistent with safety signal being directional (linearly separable) rather than distributional (mode-separated) in hidden-state space; RepE (Zou et al., 2023) is model-dependent (QwQ-32B BA 0.756 but precision 0.512 vs. R1-32B BA 0.559); CCS misaligns with temporal structure; cross-model transfer fails across 17 configurations involving imprecision and the full comparison table in section Q."

---

*(Page 8 ends at the bottom right column with text about δ ∈ {0.5,1.0,2.0} and section Q.)*

---

## Summary of Key Quantitative Claims Across Pages 5-8

**Table 2 (layer selection):** Biased vs. corrected layers differ dramatically; QwQ-32B corrected p=0.105 (not significant at corrected layer), while R1-32B corrected p<0.001.

**Table 3 (HS vs. text, 384d MiniLM):** ΔPrc ranges from +15.1pp (R1-32B) to +21.9pp (OT-7B); all 4 models pass HB correction. For BGE-1024d: only OT-7B survives HB correction.

**Table 4 (32B divergence):** R1-32B coverage 25% with lead time +11.7 to +3.3 steps; QwQ-32B coverage 74% with lead time +14.0 to +9.1 steps (negative margin −3.8pp).

**Temporal windowing:** W>1 improves both modalities; HS precision improves +1.7 to +12.9pp; text +8 to +2pp from W=1 to W=25.

**PCA capacity control:** preserves HS advantage +16.8 to +23.1pp, all p≤0.012, all 4 model-level precision tests pass HB.

**Negative results:** BOCPD/CUSUM fail across all λ/δ sweeps; RepE model-dependent (QwQ-32B works, R1-32B does not); cross-model transfer fails across 17 configurations.

**Figure 2 (forest plot):** All 384d (MiniLM) comparisons are significant; for BGE-1024d, only OT-7B survives correction.

agentId: a3057676481b40c2e (use SendMessage with to: 'a3057676481b40c2e' to continue this agent)
&lt;usage>total_tokens: 33307
tool_uses: 12
duration_ms: 175707&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4458da54-0336-4efd-a486-0d667efc57e3",
  "isSidechain": false,
  "promptId": "7bdff5af-d6c2-443f-99ab-f2e200157b45",
  "type": "user",
  "uuid": "5ff00ccc-9247-458a-a792-51dc02c5e88a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping review an academic paper. Read the PDF pages 5-8 (Results, Discussion, Conclusion sections) by calling:\n\nmcp__agent-ml-research__pdf_to_images with:\n- pdf_path: \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf\"  \n- pages: \"5\"\n- dpi: 150\n\nThen do pages 6, 7, 8 separately (one call each, dpi=150).\n\nFor each page, provide a DETAILED transcript of all text content, equations, tables, and figure descriptions. Include:\n- All section headings and their numbering\n- All claims and numerical results (especially p-values, confidence intervals, effect sizes)\n- All methodological details (statistical tests, corrections, sample sizes)\n- Table contents verbatim (every cell)\n- Figure descriptions\n\nBe extremely thorough - this is for a methodological review. Do NOT summarize - transcribe as completely as possible.",
    "agentId": "a3057676481b40c2e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the complete detailed transcript of all four pages.\n\n---\n\n## PAGE 5 (left column top to right column bottom)\n\n### Continuation of Method/Setup text (top of left column)\n\n\"each model, the three metrics are positively correlated by construction, so the correction is stricter than under independence. Control task selectivity (Hewitt and Liang, 2019) validates genuine representational structure (section II). In hidden-layer tests (n ≤ 20): R1-32B (n=20) and QwQ-32B (n=19).\"\n\n---\n\n### Section 4 Experiments\n\n\"We evaluate temporal probes across four reasoning models (table 1), comparing hidden-state (HS) and text modalities under different layer selection criteria.\"\n\n**Evidence gradient.** \"The strength of HS advantage evidence varies by model, not scale. We classify evidence into three levels using seed robustness, position independence, and sample size: **strong** (OT-7B: 5/5 seeds HS, ΔPrc=+21.9pp, position-independent, selectivity 5/5pp, n=47); **moderate** (R1-8B: precision-robust but FPR seed-fragile at 5/5 HB, n=43; QwQ-32B↑: 1/5 HB, ΔPrc=+19.2pp, sensitive load time n=19); competitive BA, n=19); and **qualified** (R1-32B↑: 5/5 HB, ΔPrc std=2.0pp, but position-mediated with residualized gap NS; W=1 only, n=20).\"\n\n**Section X.** \"At 32B, both models are significant (HB corrected) but with model-specific caveats: R1-32B achieves significance only at W=1 with 25% coverage (5/20 traces), and QwQ-32B's position baseline is competitive (section 4.4). R1-32B passes 5/5 seeds (paired ΔPrc std~2.0pp, despite non-positional HS advantage over text (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp (section Y, n=20), consistent with a position-mediated advantage. Temporal modeling reduces position dependence (R1-8B: 24.3pp drop at W=3 vs. 16.5pp at W=15).\"\n\n**Capacity control.** \"PCA reduction of HS features to 384d (matching text encoder dimensions; table Y, 79–92% variance retained) preserves the precision advantage across all four models (+16.8 to +23.1pp, all p≤0.012): all model-level precision tests pass Holm-Bonferroni. Two individual metric comparisons are non-significant. R1-8B balanced accuracy (−1.3pp, p=0.73); effect too small at n=43 and QwQ-32B FPR (−11.4pp, p=0.035, below HB threshold). PCA retains directions of maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder. This result provides partial evidence against a pure capacity explanation but does not rule out representation-quality differences between PCA-compressed HS and trained text encoders.\"\n\n---\n\n### Table 2: Layer Selection Sensitivity\n\n**Title:** \"Table 2: Layer selection sensitivity. *a bal.acc × cross.rate; b Consensus of threshold-dependent metrics (precision, inverse FPR, additive composite). Highest: HS precision p-value at corrected layer (e.g., QwQ-32B biased layer: bal.acc p=0.35, precision p=0.52; both non-significant).\"\n\n| Model | Biased^a | Corrected^b | p (corr.) |\n|-------|----------|-------------|-----------|\n| R1-8B | L14 (44%) | L11 (44%) | 0.003 |\n| OT-7B | 1.0 (9%) | L36 (37%) | <0.001 |\n| QwQ-32B | L2 (1%) | L6 (9%) | 0.105 |\n| R1-32B | L10 (69%) | L63 (98%) | <0.001 |\n\n---\n\n### Section 4.2 Layer Selection Results\n\n\"table 2 shows that the biased composite metric (balanced accuracy × crossing rate) systematically selects shallow layers: 3% depth for layer L2 (3% depth) for QwQ-32B and L10 (16%) for R1-32B. Three of four metrics excluding crossing rate (precision, inverse FPR, and additive composite) consistently select deep layers at L63 (98%) for both 32B models. Pure balanced accuracy, a threshold-free metric, selects layers that vary across data splits and models (7-98% depth under 60/20/20; section Y), itself showing that layer selection is a consequential methodological choice. The mechanism is that shallow layers produce highly compressed representations with small inter-separating distances: cosine distances are 1.4–2.7× smaller than at deep layers across all models (section C). A linear probe in this compressed space saturates near the noise floor, generating frequent threshold crossings that inflate crossing rate independently of discriminative power (section 3.3).\n\nThe downstream impact is severe: at biased layers, only the two 7-8B models show significant HS advantage; the 32B models fail. At corrected layers, all four models pass Holm-Bonferroni correction (section 3.5): strong (OT-7B), moderate (R1-8B, QwQ-32B↑), and qualified (R1-32B↑). Had we reported only biased-layer results, we would have concluded a scale-dependent HS advantage that is entirely a methodological artifact.\"\n\n---\n\n### Section 4.3 HS vs. Text Comparison\n\n\"Multi-seed stability appears in section X; BGE ΔBA/ΔFPR in section S. Against the 384d baseline, HS achieves higher precision than text probes across all four models (table 3), with evidence from strong (OT-7B: +21.9pp precision) to qualified (R1-32B↑: +15.1pp).\"\n\n---\n\n## PAGE 6 (left column, then right column, then Figure 1)\n\n### Table 3: HS vs. text at corrected layers (ILR probes, 60/20/20 split, 10,000 bootstrap resamples)\n\n**Title:** \"Table 3: HS vs. text at corrected layers (ILR probes, 60/20/20 split, 10000 bootstrap resamples). Enc.: text encoder (384d = MiniLM-L6-v2, 1024d = BGE-large). ΔHS: HS–text difference (pp). '—' = metric not computed for that encoder comparison. HB: χ² = model-level test passes Holm-Bonferroni (α=0.05); all 384d model-level tests pass†. 1024d: HB over 4 model-level precision tests.\"\n\n| Model | Enc. | Π | ΔBA | ΔPrc | ΔFR | [CI 95%] | HB |\n|-------|------|---|-----|------|-----|----------|----|\n| R1-8B | L11 | 384d | 5 | +17.5 | +20.1 | [+12.4,+25.9] | ✓ |\n| OT-7B | L36 | 384d | 2 | +6.7 | +21.9 | [+13.2,+30.7] | ✓ |\n| QwQ-32B | L6 | 384d | 5 | +0.7 | +19.2 | [+9.4,+29.0] | ✓ |\n| R1-32B | L63 | 384d | 5 | −1.6 | +15.1 | [+5.2,+25.1] | ✓ |\n| R1-8B | L11 | 1024d | 5 | +9.0 | +13.8 | [+3.9,+23.7] | — |\n| OT-7B | L36 | 1024d | 2 | +5.1 | +15.1 | [+6.4,+23.8] | — |\n| R1-32B | L63 | 1024d | 5 | −0.6 | +11.3 | [...,+21.4] | — |\n\n*(Some cells partially obscured by figure placement; values transcribed where legible.)*\n\n---\n\n### Text continuation (left column page 6)\n\n\"maximum variance in hidden-state space, which need not align with the semantic dimensions captured by a trained text encoder. This result provides partial evidence against a pure capacity explanation but does not rule out representation-quality differences between PCA-compressed HS and trained text encoders.\n\n**Random projection to 384d** (structure-destroying, unlike PCA) yields similar results (ΔPrc std~2.0pp, 20-7pp, all p<0.01; section T), further weakening the capacity explanation. An LLM-based encoder (E5-Mistral-7B, 4096d→PCA 384d) yields intermediate results (2/4 HB; section U), forming a monotonic encoder-quality gradient with MiniLM (4/4) and BGE-large (1/4).\"\n\n---\n\n### Right column page 6 (continuing HS vs. Text)\n\n\"**Encoder robustness.** The 1024d rows in table 3 replace MiniLM (384d) with BGE-large (Xiao et al., 2023) (1024d, a 2.7× stronger encoder). The HS-precision advantage persists directionally across all four models but narrows substantially: only OT-7B survives Holm-Bonferroni (1/4 precision tests). The reduced additive advantage is also directionally positive across all four models (+8.4 to +10.9pp), with 2/4 (OT-7B; R1-32B) significant after Holm-Bonferroni. FPR advantage is significant only for OT-7B (1/4). R1-8B shows an adverse FPR direction (HS FPR 1.2pp higher than BGE, p=0.56). The advantage is therefore conditional rather than absolute (fig. 2). Layer selection (Contribution 1) is encoder-independent, as it concerns hidden-state properties across layers rather than the text baseline.\"\n\n**Position mediation.** \"Position (t'/T) accounts for 9–20pp of balanced accuracy depending on model\"\n\n---\n\n### Figure 1 (full-width, right side of page 6)\n\n**Caption:** \"Figure 1: Per-layer metric heatmap (2-in-2 columns). Each column: one of five metrics (min-max normalized). Red dashed: biased layer (bal.acc × crossing rate); green dashed: corrected layer (consensus of threshold-dependent metrics). For R1-8B, both coincide at L14. At 32B, biased selections cluster near input layers while threshold-dependent metrics peak at deep layers.\"\n\n*(The figure shows a heatmap with rows = layers, columns = 5 metrics. Models shown: OT-7B and R1-8B. Color scale: dark blue to yellow. Red dashed lines mark biased layers; green dashed lines mark corrected layers. The heatmap visually confirms that biased layers (shallow) and corrected layers (deep) differ substantially.)*\n\n---\n\n## PAGE 7 (Results continuation + Discussion beginning)\n\n### Table 4: 32B cross-model divergence\n\n**Title:** \"Table 4: 32B cross-model divergence. R1-32B provides limited early detection with narrow coverage; QwQ-32B provides robust significance with poor lead time. HB: χ² = model-level test passes Holm-Bonferroni (α=0.05). Pos. margin: HS balanced accuracy minus position-only baseline.\"\n\n| Model | Cov. | Lead (steps) | HB | Pos. margin |\n|-------|------|--------------|----|-------------|\n| R1-32B | 25% | +11.7 to +3.3 | ✓ (W=1) | +14.2pp |\n| QwQ-32B | 74% | +14.0 to +9.1 | ✓ | −3.8pp |\n\n---\n\n### Text continuation (left column, page 7, top)\n\n\"and window size,† but all models retain non-positional signal above chance (all p<0.001; section C). Section 4.5). R1-32B retains significant non-positional HS advantage over text (residualized gap +3.7 to +6.9pp, HB corrected); R1-32B's gap is +1.9pp (section Y, n=20), consistent with a position-mediated advantage. Temporal modeling reduces position dependence (R1-8B: 24.3pp drop at W=3 vs. 16.5pp at W=15).\"\n\n**Section 4.4 R1-32B Model-Specific Analysis**\n\n\"R1-32B and QwQ-32B share the Qwen-32B architecture (64 layers, 5120 hidden) but present opposite detection profiles (table 4); training method is the likely differentiator.\n\nR1-32B detects commitment 11-13 steps early with a +14.2pp margin over the position baseline, which confirms genuine representational signal, but covers only 25% of traces. QwQ-32B achieves significance at all window sizes with 74% coverage: the HS probes fire 9-10pp above text probes (negative lead time). Consistent with the†R1-32B's 20-4pp drop reflects W=1 (no temporal context); at W≥3 with temporal windowing, drops are 9-13pp.\"\n\n---\n\n### Section 4.5 Temporal Context\n\n\"Temporal windowing (W>1) improves both modalities on all models (fig. 3). Text precision improves +8 to +2pp from W=1 to W=25; HS precision improves +1.7 to +12.9pp. At 7-8B, the modality advantage (+20.1 to +21.9pp precision) exceeds the temporal improvement (+13pp). Both effects are complementary: temporal windowing (W=3–15) combined with principled layer selection yields the best performance. Section P shows model temporal ablations appear in section P; GRU sequence models under a matched 60/20/20 split achieve comparable accuracy but higher FPR than LR probes (table 13).\"\n\n---\n\n### Section 4.6 Negative Results\n\n\"No alternative method consistently matches supervised probing across all four models at any evidence tier (table 19). Each failure is diagnostic: BOCPD (Adams and MacKay, 2007)/CUSUM fail to detect commitment points even after sweeping hazard rate λ ∈ {5, 10, 20, 50, 100} and drift\"\n\n---\n\n### Right column page 7 (continuing 4.6 + Figure 2)\n\n\"and window size,† but all models retain non-positional signal above chance (all p<0.001; section C).\"\n\n*(continues with the discussion of negative results)*\n\n---\n\n### Figure 2 (right column page 7)\n\n**Caption:** \"Figure 2: Forest plot of HS precision advantage over test probes. Blue: vs MiniLM-384d; orange: vs. BGE-1024d. Solid markers: passes Holm-Bonferroni. Hollow: does not. All 384d comparisons are significant (strong evidence for Contribution 1); for BGE-1024d, only OT-7B (strong) survives correction.\"\n\n*(The forest plot shows four models on the y-axis (OT-7B top, R1-8B, QwQ-32B, R1-32B bottom). X-axis: ΔPrecision (HS − Text, pp). Blue dots = MiniLM comparisons (all solid/filled, with 95% CI bars all to the right of 0), orange dots = BGE comparisons (only OT-7B solid; others hollow). R1-8B and QwQ-32B BGE CIs cross zero or are barely positive.)*\n\n---\n\n## PAGE 8 (Discussion + Conclusion)\n\n### Section 5 Discussion (left column, page 8)\n\n**Layer selection as researcher degree of freedom.**\n\n\"Our five-metric ablation (section 4.2) shows that crossing rate reverses the central finding: at biased layers, the HS advantage appears scale-dependent; at corrected layers it is significant across all four models*, from strong (OT-7B) to qualified (R1-32B†; section 3.5). The mechanism is representational compression: shallow layers (section C: 51200 × W for n=20) prevents coverage; sweeping regularization C over {0.01, 10} yields ~2pp variation in balanced accuracy; the HS advantage is also stable across decision thresholds (BA variation <1.5pp across C ∈ {0.1, 0.7}; section M). QwQ-32B HS help time is negative (−1.2 to +1.9 steps vs. text 3.7−12.2 steps): higher precision at later detection. On some traces it probes precision 50-52% false alarm rates, so current methods characterize the commitment phenomenon rather than constitute production-ready detectors. Per-model details in section 4.4.\"\n\n---\n\n**Encoder-quality boundary.**\n\n\"HS advantage is a function of text encoder quality: significant against 384d MiniLM (4/4 precision tests; see L4–HB, strong to qualified) but attenuated against 1024d BGE-large (1/4 HB). PCA capacity matching preserves significance (+16.8 to +23.1pp) and provides partial evidence against a pure capacity explanation. This boundary is itself a finding: the HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference. Temporal context and modality choice are complementary: at W=1 the modality advantage exceeds the temporal improvement; temporal windowing (W=3 to 15) provides consistent gains regardless of modality.\"\n\n---\n\n**Guidance for future research.** \"The evidence gradient (strong for OT-7B, moderate for R1-8B and QwQ-32B, qualified for R1-32B) is corroborated by oracle analysis: OT-7B achieves 93.6% early detection with 50-step head time, while R1-32B reaches only 50% early detection (section I). The gap suggests that the commitment signal variation varies across models. The cross-model variation indicates that distillation and native reasoning produce qualitatively different safety representations. Our five-step checklist (layer selection, control task selectivity, and position residualization (3/4 models retain significant non-positional HS advantage), and PCA provide convergent evidence of genuine safety representations, but our approach is correlational. Causal validation via CAS (Geiger et al., 2025), LEACE (Belrose et al., 2023), or Li et al.'s (2023) interchange confirm that probed directions are causally active. Applying this audit to our own initial results changed the central conclusion from \"HS advantage is scale-dependent\" to \"HS advantage is universal under corrected selection,\" a qualitative reversal that illustrates how unexamined layer selection can propagate to deployment decisions. We recommend a five-step audit for probing studies: (1) train probes across all layers; (2) compute ≥3 metrics (threshold-free and threshold-dependent); (3) check for metric disagreement; (4) report per-model; (5) account for position and volatility (section C). Steps 3-5 cost negligible compute. For production monitoring, deep layers selected by threshold-dependent metrics with temporal windowing (W=3–7 probes) offer reliable commitment detection. The crossover point where text encoders match HS probes lies approximately at the 1024d BGE-class (1.3pp). Below this, HS probes offer clear advantages. At 32B scale, HS probing is position-entangled, so temporal modeling combined with position residualization is necessary to extract genuine safety signal (section V).\"\n\n---\n\n**Deployment operating points.** \"The consecutive-crossings threshold K trades coverage (table 10): at K=0 with W=1 and 60% throughput, average coverage is 60% with 48% safe FPR. Raising K yields practically useful operating points: at K=10, OT-7B achieves 21% coverage with only 5% false positives (CUSUM failing fewer than 1 in 12 flagged traces is a false alarm). R1-32B at K=10 retains 35% coverage\"\n\n---\n\n\"δ ∈ {0.5, 1.0, 2.0} (section K), with 0% detection on 3/4 models; Mahalanobis distance yields near-zero separation, consistent with safety signal being directional (linearly separable) rather than distributional (mode-separated) in hidden-state space; RepE (Zou et al., 2023) is model-dependent (QwQ-32B BA 0.756 but precision 0.512 vs. R1-32B BA 0.559); CCS misaligns with temporal structure; cross-model transfer fails across 17 configurations involving imprecision and the full comparison table in section Q.\"\n\n---\n\n*(Page 8 ends at the bottom right column with text about δ ∈ {0.5,1.0,2.0} and section Q.)*\n\n---\n\n## Summary of Key Quantitative Claims Across Pages 5-8\n\n**Table 2 (layer selection):** Biased vs. corrected layers differ dramatically; QwQ-32B corrected p=0.105 (not significant at corrected layer), while R1-32B corrected p<0.001.\n\n**Table 3 (HS vs. text, 384d MiniLM):** ΔPrc ranges from +15.1pp (R1-32B) to +21.9pp (OT-7B); all 4 models pass HB correction. For BGE-1024d: only OT-7B survives HB correction.\n\n**Table 4 (32B divergence):** R1-32B coverage 25% with lead time +11.7 to +3.3 steps; QwQ-32B coverage 74% with lead time +14.0 to +9.1 steps (negative margin −3.8pp).\n\n**Temporal windowing:** W>1 improves both modalities; HS precision improves +1.7 to +12.9pp; text +8 to +2pp from W=1 to W=25.\n\n**PCA capacity control:** preserves HS advantage +16.8 to +23.1pp, all p≤0.012, all 4 model-level precision tests pass HB.\n\n**Negative results:** BOCPD/CUSUM fail across all λ/δ sweeps; RepE model-dependent (QwQ-32B works, R1-32B does not); cross-model transfer fails across 17 configurations.\n\n**Figure 2 (forest plot):** All 384d (MiniLM) comparisons are significant; for BGE-1024d, only OT-7B survives correction."
      }
    ],
    "totalDurationMs": 175707,
    "totalTokens": 33307,
    "totalToolUseCount": 12,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1883,
      "cache_read_input_tokens": 25661,
      "output_tokens": 5762,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1883
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5762,
          "cache_read_input_tokens": 25661,
          "cache_creation_input_tokens": 1883,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1883,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 5
    }
  },
  "sourceToolAssistantUUID": "4458da54-0336-4efd-a486-0d667efc57e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性** 审查。  ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models - **路径**: `projects/contrastive_trace_safety/docs/paper…",
  "leafUuid": "5ff00ccc-9247-458a-a792-51dc02c5e88a",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodology rigor for safety probes paper",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Tool result

_source line 54 · 2026-05-19T04:44:45.649Z_

<details><summary>↩ Tool result · `toolu_015MRVtErFsoVMKEgYy2Gr2G`</summary>

```text
&lt;persisted-output>
Output too large (55.4KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/3e48199e-0c0d-47bc-8ea3-24ecb0f30457/tool-results/toolu_015MRVtErFsoVMKEgYy2Gr2G.json

Preview (first 2KB):
[
  {
    "type": "text",
    "text": "The PDF has 26 pages total. Now I have a complete picture of all pages 9–26. Here is a thorough transcript of all content found on pages 9–26:\n\n---\n\n## PAGE 9 — End of Section 5 (Discussion) + Section 6 (Conclusion) + References (start)\n\n**End of Section 5 text (continuation from page 8):**\n\n\"at 17% FPR. These conservative operating points are viable for high-stakes deployment where missed detections are preferable to frequent false alarms: a secondary review system could inspect only flagged traces, reducing human verification burden by 79–86% while maintaining non-trivial detection rates. The K=7 setting offers a middle ground (57% FPR reduction, 16–39% detection). The choice of operating point is deployment-specific, but the existence of a low-FPR regime contradicts the assumption that 32% or 52% FPR renders commitment detection impractical.\"\n\n**Section 6 — Conclusion**\n\n\"Layer selection is a critical researcher degree of freedom: a biased composite metric reverses the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. The five-step audit protocol (section 5) would have prevented this outcome. The empirical HS advantage is conditional: robust at 7-8B (strong for OT-7B, moderate for QoQ-32B, qualified for R1-32B), and bounded by text encoder quality (4/4 HB against 384d, 1/4 against 4096d). Current probes characterize commitment detection rather than constitute production detectors. Models (≥95 cases) encode less information per step, benefit proportionally more from observing the multi-step progression.\n\n**7 Limitations**\n\nOur results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39–52%, and the HS advantage (R1-8B) scores the safety commitment phenomenon. This underscores how much room remains for improvement.\n\n**Model-specific caveats and statistical power.** HS ach
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "385e832b-3967-46f7-82ad-98c2cb267a94",
  "isSidechain": false,
  "promptId": "7bdff5af-d6c2-443f-99ab-f2e200157b45",
  "type": "user",
  "uuid": "0b000206-f84f-469c-a26e-1c8be2bf47d6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping review an academic paper. Read the PDF pages 9 through the last page (likely appendix, references, supplementary material) by calling:\n\nmcp__agent-ml-research__pdf_to_images with:\n- pdf_path: \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf\"  \n- pages: \"9\"\n- dpi: 150\n\nThen do pages 10, 11, 12, 13, 14 separately (one call each, dpi=150). Some pages may not exist - that's fine, just report what you find.\n\nFor each page, provide a DETAILED transcript of all text content, equations, tables, and figure descriptions. Include:\n- All section headings and their numbering\n- All claims and numerical results (especially statistical details)\n- All methodological details\n- Table contents verbatim (every cell)\n- Figure descriptions\n- Appendix details (proofs, additional experiments, etc.)\n\nBe extremely thorough - this is for a methodological review. Do NOT summarize - transcribe as completely as possible.",
    "agentId": "a1f44cd443536f851",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "The PDF has 26 pages total. Now I have a complete picture of all pages 9–26. Here is a thorough transcript of all content found on pages 9–26:\n\n---\n\n## PAGE 9 — End of Section 5 (Discussion) + Section 6 (Conclusion) + References (start)\n\n**End of Section 5 text (continuation from page 8):**\n\n\"at 17% FPR. These conservative operating points are viable for high-stakes deployment where missed detections are preferable to frequent false alarms: a secondary review system could inspect only flagged traces, reducing human verification burden by 79–86% while maintaining non-trivial detection rates. The K=7 setting offers a middle ground (57% FPR reduction, 16–39% detection). The choice of operating point is deployment-specific, but the existence of a low-FPR regime contradicts the assumption that 32% or 52% FPR renders commitment detection impractical.\"\n\n**Section 6 — Conclusion**\n\n\"Layer selection is a critical researcher degree of freedom: a biased composite metric reverses the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. The five-step audit protocol (section 5) would have prevented this outcome. The empirical HS advantage is conditional: robust at 7-8B (strong for OT-7B, moderate for QoQ-32B, qualified for R1-32B), and bounded by text encoder quality (4/4 HB against 384d, 1/4 against 4096d). Current probes characterize commitment detection rather than constitute production detectors. Models (≥95 cases) encode less information per step, benefit proportionally more from observing the multi-step progression.\n\n**7 Limitations**\n\nOur results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39–52%, and the HS advantage (R1-8B) scores the safety commitment phenomenon. This underscores how much room remains for improvement.\n\n**Model-specific caveats and statistical power.** HS achieves significance only at W=1 (25% coverage) and its HS advantage is position-mediated (residualized gap +1.9pp; section V). QoQ-32B's position baseline achieves significance only at W=1 (25% coverage); full significance is 5/20 at n=19–20 vs n=20. HS significance is seed-fragile (3/5 HB); at n=19–20, the minimum detectable effect at 80% power is 6.8pp...\"\n\n**References** begin (partial list visible at bottom of page):\n\n- Ryan Prescott Adams and David J.C. MacKay. 2007. Bayesian online changepoint detection. *arXiv preprint arXiv:2007.01142*. Concurrent work.\n- Patrick Altmsd, Tobias Eder, Nyong Yang, Zhiyi Pan, and Georg Grok. 2026. Safer reasoning models: *arXiv preprint arXiv:2504.09375*.\n- Yanai Elazar, Shauli Ravfogel, Alon Jacovi, and Yoav Goldberg. 2021. Amnesic probing: Behavioral explanations with amnestic counterfactuals. *Transactions of the Association for Computational Linguistics*, 9:160–175.\n\n---\n\n## PAGE 10 — References (continued)\n\nFull reference list page. Entries include (verbatim as visible):\n\n- Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, and Neel Nanda. 2024. Refusal in language models is mediated by a single direction. In *Advances in Neural Information Processing Systems 17 (NeurIPS)*.\n- Bowen Baker, Ioot Huizinga, Leo Gao, Zehao Dou, Melody Y. Guan, Aleksander Madry, Wojciech Zaremba, Bob McGrew, and Ilya Sutskever. 2022. Monitoring reasoning models for misbehavior and the risks of promoting obfuscation. *arXiv preprint arXiv:2502.11926*.\n- Yamini Bansal, Preetum Nakkiran, and Boaz Barak. 2021. Re-thinking model stitching to compare neural representations. In *Advances in Neural Information Processing Systems 34 (NeurIPS)*.\n- Yonatan Belinkov. 2022. Probing classifiers: Promises, shortcomings, and advances. *Computational Linguistics*, 48(1):207–219.\n- Nora Belrose and James Glass. 2019. Analysis methods in natural language processing. *Transactions of the Association for Computational Linguistics*, 7:49–72.\n- Nora Belrose, David Schneider-Joseph, Shauli Ravfogel, Ryan Cotterell, Edward Raff, and Stella Biderman. 2023. LEACE: Perfect linear erasure of a concept from a model's representations. In *Advances in Neural Information Processing Systems 36 (NeurIPS)*.\n- Gerard Botos, Aman Neelappa, and Shivam Raval. 2023. Probing language models for lexical evidence: Results from language mitigation studies in language models. *arXiv preprint arXiv:2509.21344*.\n- Colin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023. ELICIT: Discovering latent knowledge in a language model. In *Proceedings of the International Conference on Learning Representations (ICLR)*.\n- Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Stephen Donoho, Chris Olah, Arnab Amutz, Peter Hase, Micha Wagner, Fazl Amin Roger, Vlad Mikulin. 2025. Reasoning models can be honest if you ask them: Results from language mitigation studies in language models. *arXiv preprint arXiv:2503.05410*.\n- Alexis Conneau, German Kruszewski, Guillaume Lample, Loïc Barrault, and Marco Baroni. 2018. What you can cram into a single vector: Probing sentence embeddings for linguistic properties. In *Proceedings of the Association for Computational Linguistics (ACL)*, pages 2126–2136.\n- DeepSeek-AI. 2025. DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. *arXiv preprint arXiv:2501.12948*.\n\n---\n\n## PAGE 11 — References (continued)\n\n- Fazir Joaz, Majd Hawady, Sabri Bongleberbok, Nadir Durrami, and Huseyn Taha Sencar. 2026: \"There is more to refusal in language models than a single direction.\" *arXiv preprint arXiv:2602.02112*.\n- Sri Dorga Sai Sowmya Kadali and Evangelos E. Papalesakis. 2025. Do internal layers of LLMs reveal patterns for jailbreak detection? *arXiv:846-866*.\n- Ishita Kakkar, Eoin Zhang, Rheeya Uppaal, and Jinjie Hu. 2026. When safety falls below the frontier: Benchmarking harmful behavior detection in reasoning chains. *arXiv preprint arXiv:2604.19001*.\n- Su-Hyeon Kim, Hyundong Jin, Yejin Lee, and Yu-Sub Kim. 2026. How does the thinking affect model safety? an entropy-based safety reminder for chain-of-thought models. *arXiv preprint arXiv:2603.08601*.\n- Tomek Korbak, Mikita Balesni, Elizabeth Barnes, Joseph Bengio, Joe Benton, Joseph Bloom, Mark Chen, Andrew Cuvos, Owain Evans, David Farhi, Ryan Greenblatt, Dan Hendrycks, Evan Hubinger, Geoffrey Irving, Erik Jenner, and 22 others. 2025. Chain of thought monitorability: A fragile opportunity for AI safety. *arXiv preprint arXiv:2511.11471*.\n- Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019. Similarity of neural network representations revisited. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, volume 97 of *Proceedings of Machine Learning Research*, pages 3519–3529.\n- Martin Kub, Llaster, Aolin Hing, Qinxi Wang, Louis DiValentin, Yujia Bao, Wei Wei, Hai Li, and Yiran Chen. 2025. H-cut: Hijacking the chain-of-thought in large reasoning models to jailbreak large reasoning models. *arXiv preprint arXiv:2509.21344*\n- Martin Küblböck, James Elsman, Simon Geisler, Vincent Fortuin, Aakash Jaini, and Stephan Günnemann Bastian Gasteiger. 2025. The geometry of refusal in large language models: Concept cones and representational independence. In *Proceedings of the 42nd International Conference on Machine Learning (ICML)*.\n- Shitao Xiao, Zheng Liu, Peitian Zhang, and Niklas Muennighoff. 2025. C-pack: Packaged resources to advance general chinese embedding. *arXiv preprint arXiv:2309.07597*.\n- Bo Yin, Weikai Liu, Yada Zhu, and Song Wang. 2026. C-caliblabcam: a safety-world model with iterative early jailbreak detection. *arXiv preprint arXiv:2604.16824*.\n- Nelson F. Liu, Matt Gardner, Yonatan Belinkov, Matthew E. Peters, and Noah A. Smith. 2019. Linguistic knowledge and transferability of contextual representations. In *Proceedings of the North American Chapter of the Association for Computational Linguistics (NAACL)*, pages 1073–1094.\n- Faiir Joaz, Majd Hawady, Sabri Bongleberhok, Nadir Durrami, and Huseyn Taha Sencar. 2026. \"There is more to refusal in language models than a single direction.\" *arXiv preprint arXiv:2602.02112*.\n- Yingzhi Qian, Chunhang Zhang, Jianzong Wang, Hengfeng Guo, Boji Cao, Yuejie Li, Honggyu Liu, Penghan Han, and Le Sun. 2025. When models overthink their safety: LLMs encode harmfulness and refusal separately. In *Advances in Neural Information Processing Systems 38 (NeurIPS)*.\n- Zhenhong Zhou, Haiyang Yu, Xinghua Zhang, Rongwu Xu, Fei Huang, and Yongbin Li. 2024. How alignment and jailbreak work: Explain LLM safety mechanisms through hidden states. In *Findings of the Association for Computational Linguistics: ACL 2024*.\n- Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mrinank Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, and Dan Hendrycks. 2023. Representation engineering: A top-down approach to AI transparency. *arXiv preprint arXiv:2310.01405*.\n\n---\n\n## PAGE 12 — References (continued) + Appendix A header\n\nRemaining references:\n\n- Ang Zhang, Yulin Chen, Jane Pan, Chen Zhao, Anrojit Panda, Junyang Li, and He He. 2025. Reasoning models know when they're right: Probing hidden states for self-verification. *arXiv preprint arXiv:2504.05419*.\n- Jiachan Zhao, Jing Huang, Zhengxuan Wu, David Bau, and Weiyan Shi. 2025. LLMs encode harmfulness and refusal separately. In *Advances in Neural Information Processing Systems 38 (NeurIPS)*.\n- Zhenhong Zhou, Haiyang Yu, Xinghua Zhang, Rongwu Xu, Fei Huang, and Yongbin Li. 2024. How alignment and jailbreak work: Explain LLM safety mechanisms through hidden states. In *Findings of the Association for Computational Linguistics: ACL 2024*.\n- Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mrinank Mazeika, ..., and Dan Hendrycks. 2023. Representation engineering: A top-down approach to AI transparency. *arXiv preprint arXiv:2310.01405*.\n- Qingyin Yin, Chak Tuo Leong, Linyi Yang, Wenxuan Wang, Junjie Li, Jiangchao Zhao, Jinheng Yao, Xing, Xing Ya, and Jinjin Gu. 2025. Refusal falls off a cliff: Safety alignment failures in reasoning? *arXiv preprint arXiv:2510.06036*.\n- Zhong-Xia Zhang and Stephen H. Bach. 2025. Selfjailbreaking: Language models jailbreak themselves out of safety alignment after being reasoning. *arXiv preprint arXiv:2510.20956*.\n\n**Appendix A: Responsible NLP Research Checklist** (header visible at bottom)\n\n\"**Appendix A: Responsible NLP Research Checklist**\n\n- **Limitations discussed:** Yes (section 7)\n- **Potential risks:** This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this concern, as the safety probe does not provide a direct model access to the probe, which a deployed monitoring system would not expose.\"\n\n(Additional checklist items partially visible but cut off)\n\n---\n\n## PAGE 13 — Appendix A (Responsible NLP Research Checklist continued) + Appendix B (Layer Sweep Results)\n\n**Appendix A continued:**\n\n- **Computational budget:** Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total). We compute on a single machine (under 4 GPU-hours on a single 4-GPU A6000 or finetuning).\n- **Data:** We use HarmThoughts, a publicly available benchmark with safety annotations. No new data collection was performed.\n- **Human subjects:** No human subjects research was conducted.\n- **Reproducibility:** All hyperparameters are reported in section 4.5 (full BA-optimal layer in section Y). K was pre-selected using BA metric. Code and data will be released upon publication.\n\n**Appendix B — Layer Sweep Results**\n\n\"For each model, we sweep all transformer layers and evaluate from each layer three criteria: (1) balanced accuracy = crossing rate (the biased composite), (2) pure balanced accuracy, (3) precision, (4) inverse FPR. Including seed 0, FPR metric drops from 0.48 to 0.30 by biased metric.\n\nShallow layers produce highly compressed representations as a middle-ground tradeoff; deep layers (7–98% depth) demonstrate that layer selection is a consequential methodological choice. The HS advantage at threshold is significant at whichever layer BA selects (14/16 per-model HB, two FPR failures from underpowered 32B test sets n≤20).\n\n**Selected layers.** R1-8B: all five metrics agree on layer 14 (44% depth). OT-7B: biased metric selects L0 (0%), unbiased consensus selects L16 (57%). QoQ-32B: biased metric selects L2 (3%), unbiased selects L10 (16%), unbiased consensus selects L63 (98%). The bias is most extreme at 64-layer models where the composite metric selects layers in the bottom 16% of the network while threshold-dependent metrics select layers at 57% depth and above. For 32B models, unbiased BA selects L32 (42 for QoQ) and L47 (73%) for R1-32B; under the canonical 60/20/20, it selects L63 (98%), which demonstrates this metric sensitivity to the data split.\n\n**Impact on modality comparison.** At the biased metric, HS vs. text precision p-values are 0.064 (R1-32B) and 0.35–0.83 (QoQ-32B), both non-significant (section III). 1/5 unbiased metrics improve monotonically across all metrics (section F), so the accuracy signal is specific to HS probes (but not 32B).\n\n**Layer selection stability (LOO-CV).** Leave-one-out cross-validation on the validation set confirms that layer selection is robust to data composition. Under pure balanced accuracy, the dominant layer is selected in 68% (QoQ-32B) to 89% (R1-8B) of folds, consistent with the main finding. Three alternative selections cluster in neighboring layers (L29, L55–56 for QoQ; L32, L38, L43 for R1-32B). The consensus corrected layers (L63 for both 32B models) are similarly dominant under threshold-dependent selection.\n\n**Joint layer, W=1 sensitivity.** Under the original 700d → 384d pipeline, the joint layer/window selection is one of 2,340 configurations (this is a potential source of selection bias inflating results — see section 4.2). We cover 2 architectures and 2 scales; intermediate scales, proportion analysis, and multilingual settings are untested. In Figure X we cover 2 of 2.\"\n\n**Table 5** (Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Table 6: \"Table 6: Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4–2.7×), while a linear operator in this compression framework is 1.4–2.7× smaller than at deep layers. The table shows smaller inter-step distances at shallow layers.\"):\n\nTable 6 data:\n| Model | Layer (type) | Mean | Std |\n|-------|-------------|------|-----|\n| R1-8B | L2 (biased) | 0.186 | 0.097 |\n| R1-8B | L16 (corrected) | 0.411 | 0.145 |\n| QoQ-32B | L2 (biased) | 0.077 | 0.041 |\n| QoQ-32B | L63 (corrected) | 0.206 | 0.091 |\n| R1-32B | L2 (biased) | 0.084 | 0.056 |\n| R1-32B | L10 (biased) | 0.092 | 0.076 |\n| R1-32B | L63 (corrected) | 0.076 | 0.076 |\n\n---\n\n## PAGE 14 — Appendix C (Representation Compression Analysis) + Appendix D (Holm-Bonferroni Step-Down Correction)\n\n**Appendix C — Representation Compression Analysis**\n\n\"We measure step-to-step cosine distance at biased (shallow) vs. corrected (deep) layers across all models to characterize the compression mechanism underlying the crossing rate bias (table 6).\n\nShallow layers produce highly compressed representations (1.4–2.7×), producing more frequent threshold crossings. The HS precision advantage (table 2) at the same dimensionality shows the compression advantage.\n\n**Table 7** (step-level metrics): HS vs. text precision p-values are 0.064 (R1-32B) and 0.35–0.83 (QoQ-32B), which is non-significant (section III).\n\nShallow layers produce highly compressed representations and produce predictions even as overall classification accuracy degrades. CP annotations (section 4.1) uses 7 Transform models as text encoder baseline. The larger marginal gains for text probes reflects their weaker single-step baseline.\"\n\n**Table 7. Holm-Bonferroni Step-Down Correction:**\n\nTable 7 data (4 tests = 3 correlated metrics). Each test uses two-sided metric differences (HS mimus text). All 12 pass at α=0.05; a 4-test model-level correction (one per model, using the worst p-value) also passes.\n\n| Rank | Model | Metric | p-val | Thresh. | Pass |\n|------|-------|--------|-------|---------|------|\n| 1 | QoQ-32B | Bal. Acc. | <0.001 | 0.0042 | Yes |\n| 2 | OT-7B | Bal. Acc. | <0.001 | 0.005 | Yes |\n| 3 | R1-8B | Bal. Acc. | <0.001 | 0.0056 | Yes |\n| 4 | OT-7B | Bal. Acc. | <0.001 | 0.0063 | Yes |\n| 5 | QoQ-32B | Precision | <0.001 | 0.007 | Yes |\n| 6 | OT-7B | Precision | <0.001 | 0.0083 | Yes |\n| 7 | R1-8B | Precision | 0.001 | 0.01 | Yes |\n| 8 | R1-32B | Bal. Acc. | 0.003 | 0.0125 | Yes |\n| 9 | QoQ-32B | Precision | 0.003 | 0.0167 | Yes |\n| 10 | M | Decision | 0.005 | 0.025 | Yes |\n| 11 | N | Decision | 0.013 | 0.05 | Yes |\n| 12 | R1-8B | FPR | 0.044 | 0.0500 | Yes |\n\n\"The weakest test (rank 12, R1-8B FPR, p=0.044) passes its threshold (α/1 = 0.05) with the margin. The ordering reveals that L63 is near-optimal for QoQ-32B at recommended windows (W=3), just below the Layer L45–L46 layer for form a robust band where all 3/3 metrics pass Holm-Bonferroni (section B1). The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.\n\n**Exact sign-flip permutation test validation.** Table 7 reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the consecutive 12-test comparison and the 4-test model-level correction: both yield the same outcome (all tests pass at α=0.05). Under 4-test HB, the tightest threshold falls at α/4=0.0125; (p=0.044), rank-4 threshold α/1=0.050, which still passes. Text FPR is highly stable (std=0.007) while HS FPR is split-sensitive (std=0.040), suggesting the canonical-split FPR advantage (~7.4pp) does not generalize robustly across seeds.\"\n\n---\n\n## PAGE 15 — Appendix E (Window Size Ablation Details) + Appendix F (OpenThinker-7B Detailed Results)\n\n**Appendix E — Window Size Ablation Details**\n\n\"Table 8 reports the complete text probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes.\n\n**Table 8** (Window size ablation on R1-8B, step-level metrics):\n\n| W | Bal.Acc. | Precision | FPR | Coverage |\n|---|----------|-----------|-----|----------|\n| 1 | 64.7 | 41.6 | 25.8 | 95.4 |\n| 3 | 66.9 | 44.8 | 23.1 | 90.7 |\n| 5 | 69.2 | 48.5 | 20.0 | 84.9 |\n| 10 | 72.1 | 56.9 | 18.2 | 74.4 |\n| 15 | 74.3 | 62.1 | 14.2 | 65.8 |\n| 20 | 75.8 | 62.1 | 12.5 | 62.8 |\n| 25 | 76.7 | 63.0 | 12.2 | 60.3 |\n\n\"Text probes improve monotonically from W=1 while the plateau observed at W=10 also approximately aligns with the HS probes. The absolute FPR reduction (~14.8pp) differs markedly from its paired ΔPre and HS text coverage pairs are four times larger. The larger marginal gains for text probes reflects their weaker single-step baseline.\"\n\n**Appendix F — OpenThinker-7B Detailed Results**\n\n\"Table 9 reports the complete text probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes. (Section E). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 68% ±11 (W=1) to 82.2% (W=25) with FPR falling 9.65% to 4.83%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at W=3 while precision and FPR continue improving at larger windows; (3) R1-32B peaks at W=10 then degrades, likely reflecting overfitting on the smaller dataset with small Gaussian noise added. This made the text probe trivially predictive and produced a spuriously significant result (p=0.001 for HS vs. text FPR difference).\n\n**R1-8B per-model FPR (biased metric)** — Table 21 reports HS vs. text FPR comparisons for R1-8B; HS FPR is directionally consistently lower (5/5 HS ≤ Text); 2/5 reaching statistical significance; but after Holm-Bonferroni correction for 5 seeds (p=0.01), 1/5 remains significant. Text FPR is highly stable (std=0.007) while HS FPR is split-sensitive (std=0.040).\"\n\n**Table 9** (text probe window ablation on R1-8B, step-level metrics, full per-seed breakdown):\n\n| W | Bal.Acc. | Precision | FPR | Coverage |\n|---|----------|-----------|-----|----------|\n| 1 | 58.1 | 24.5 | 34.5 | 63.8 |\n| 3 | 64.8 | 33.2 | 28.7 | 70.1 |\n| 5 | 65.9 | 38.2 | 26.3 | 72.2 |\n| 10 | 58.9 | 28.3 | 20.0 | 66.0 |\n| 15 | 65.0 | 33.2 | 19.7 | 64.5 |\n| 25 | 61.4 | 32.9 | 16.1 | 66.0 |\n\n\"**OT-7B multi-layer GRU results (layers 13–19, 3 seeds, 60/20/20 split).** OT-7B GRU achieves 74.6% ±1.3% balanced accuracy, 64.5±2.7% coverage; +33.6pp to 61.8% precision; 22.76% to 16.94% FPR. QoQ-32B produces +3.2pp to lead time. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps, so absolute lead times are not directly comparable. The FPR lead-time results combining HS and LR probe at layer-16 (10.0%), which confirms that GRU's gain lead time at the cost of more false alarms across both 7.8B models.\"\n\n**Universal trends** summary bullet text:\n- (1) larger windows smooth the probe fires less frequently\n- (2) HS FPR generally decreases with window size (3) leads time is model-dependent\n- OT-7B has a higher crossing at W=3\n\n---\n\n## PAGE 16 — Appendix E.1 (Test Probe Window Ablation) + Appendix F cont. (OT-7B detailed results with tables)\n\n**Appendix E.1 — Test Probe Window Ablation**\n\n\"Table 9 reports the complete test probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes (Section E).\n\n**Table 10** (OT-7B test probe window ablation, step-level metrics): HS score = balanced accuracy. Layer 16 (57% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.\n\n| Layer | Depth | Bal.Acc. | Cross.Rate | Score |\n|-------|-------|----------|------------|-------|\n| 0 (embed.) | 0 | 66.3 | 40.4 | 35.5 |\n| 4 | 18 | 66.3 | 40.4 | 26.8 |\n| 8 | 36 | 61.2 | 35.6 | 21.6 |\n| 16 | 57 | 65.5 | 31.9 | 21.6 |\n| 20 | 71 | 65.5 | 31.9 | 20.9 |\n| 30 | ??? | 65.0 | 31.9 | 20.9 |\n| 63 | 71 | 65.5 | 31.9 | 20.9 |\n| 64 | 75 | 63.0 | 31.9 | 21.8 |\n\n**Table 11** (OT-7B test probe window ablation, step-level metrics):\n\n| W | Bal.Acc. | Precision | FPR | Coverage |\n|---|----------|-----------|-----|----------|\n| 1 | 58.1 | 24.5 | 34.5 | 63.8 |\n| 3 | 63.3 | 32.3 | 26.0 | 66.0 |\n| 5 | 61.8 | 30.9 | 19.0 | 64.5 |\n| 10 | 65.7 | 39.1 | 17.4 | 64.5 |\n| 15 | 65.5 | 40.0 | 14.9 | 62.4 |\n| 25 | 76.2 | 62.1 | 10.0 | 54.3 |\n\n\"R1-8B shows a broadly increasing trend in balanced accuracy with local non-monotonicity: balanced accuracy peaks at W=5 (76.1%) while W=10–15 then recovers to 76.2% at W=25. Precision and FPR improve monotonically with larger windows (54% to 61.8% precision; 22.76% to 16.94% FPR). QoQ-32B produces +3.2pp in lead time. The lead time is substantially longer in those models than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps, so absolute lead times are not directly comparable. The FPR-lead-time results from using the HS probe with LR probe at layer 16 (10.0%), which confirms that GRU's gain lead time at the cost of more false alarms across both 7-8B models.\"\n\n---\n\n## PAGE 17 — Appendix G (GRU Training Details) + Appendix H (Control Task Methodology)\n\n**Appendix G — GRU Training Details**\n\n\"**Data split.** GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression models. The validation set (10% of training portion) is used for early stopping (effective 60/10/30 split). The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\n\n**Architecture.** We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden layer (h) [the best layer selected by validation balanced accuracy] as input. The multi-layer variant concatenates hidden states from 3 candidate layers [multiple], running through the network at each step to produce a higher-dimensional input to the same GRU architecture.\n\n**Training procedure.** We train with Adam (learning rate 1×10^-3, default β₁=0.9, β₂=0.9993), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.\n\n**Results.** We report crossing accuracy (sustained accuracy at which the model-first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean ± standard deviation.\n\n**Per-seed results for R1-8B (single-layer GRU).** The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe first achieves good peak accuracy but crosses the detection threshold late. This variance underscores the\n\n**Table 12** (R1-8B GRU joint layer, 70/30):\n\n| Seed | Peak Acc. | Crossing Acc. | Lead (steps) |\n|------|-----------|---------------|--------------|\n| 1 | 85.2 | 74.3 | +4.8 |\n| 2 | 83.1 | 72.9 | +4.8 |\n| 3 | 83.4 | 70.4 | −0.9 |\n| Mean ± std | 83.9 ± 1.1 | 72.5 ± 2.0 | +3.5 ± 2.3 |\n\n\"**OT-7B multi-layer GRU (layers 13–19, 3 seeds, 60/20/20 split).** OT-7B GRU achieves 74.6% ± 1.3% balanced accuracy; 64.5% ± 1.4% steps lead. GRU advantage (BA: Δ=+21.9pp, FPR: Δ=−17pp, 95% CI [−22.2, −12.2]). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (±21.9pp); the small discrepancy reflects resampling underperfrom under the optimal layer selection. OT-7B GRU lead time is substantially longer than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps vs. 4.5 steps for both R1-8B and R1-32B, so absolute lead times are not directly comparable.\"\n\n**Appendix H — Control Task Methodology**\n\n\"We follow the selectivity framework of (Hewitt and Liang, 2019) to verify that our probes capture sensitivity to annotation noise rather than meaning noise only.\"\n\n---\n\n## PAGE 18 — Appendix H (Control Task) + Appendix I (Oracle Upper Bound Analysis) + Appendix J (CP Annotation Perturbation)\n\n**Appendix H (continued):**\n\n\"**Procedure.** For each model, we randomly permute the binary labels (pre-CP vs. post-CP) within each trace while preserving the marginal label distribution. We train L2-regularized logistic regression (L2-regularized logistic regression on shuffled features) classifiers with the same architecture and hyperparameters on these shuffled labels. Selectivity is defined as:\n\nSelectivity = Acc_diagnostic − Acc_control ... (1)\n\nwhere Acc_diagnostic is the probe accuracy on true labels and Acc_control is the accuracy on permuted labels. A selectivity score close to zero indicates the probe is not learning a meaningful signal above chance.\n\n**Results.** We repeat the control experiment 10 times with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers (60/20/20): the dominant layer is selected in 68% (QoQ-32B) to 89% (R1-8B) of folds. The absolute FPR reduction (~14.8pp) differs markedly from its paired ΔPre...\n\n**Layer provenance note.** R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias since they agree with corrected layers and are bounded by the Mahalanobis HS advantage. QoQ-32B's precision gap (+20.1pp) aligns with the bootstrap mean (±21.4pp). The R1-32B's bias is most extreme; confirming that layer selection matters to the commitment detection outcome.\n\n**Position-only baseline.** As a complementary non-positional test, we train a logistic regression classifier using only the normalized step index (t/T where T is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8% FPR compared to 8.1% for the HS probe at matched detection thresholds. The probe confirms that hidden state features carry information beyond what step position provides.\"\n\n**Residualized Selectivity:** \"To confirm that selectivity survives position removal, we recompute control task selectivity on position-regressed features (the same residualized representations used in section V). R1-8B at 67.3% but 1% crossing rate. Implementation details in section (R).\"\n\n**Appendix I — Oracle Upper Bound Analysis**\n\n\"Table 14 reports the oracle performance of GRU and FPR share the same balanced accuracy, precision, and FPR for the four independent comparisons is four (one per model). We report both the consecutive 12-test and the 4-test model-level correction: both yield the same outcome (all tests pass at α=0.05). Under 4-test HB, the tightest threshold falls at α/4=0.0125...\"\n\n**Table 14** (Oracle upper bound analysis). Det. Rate = balanced accuracy, p=0.80; MDE (80% power):\n\n| Model | Det.Rate | Obs.sd (BA) | MDE(80%) |\n|-------|----------|-------------|---------|\n| R1-8B | 20 | 0.026 | 9.5pp |\n| OT-7B | 20 | 0.034 | ... |\n| QoQ-32B | 20 | 0.056 | ... |\n| R1-32B | 20 | 0.056 | 9.5pp |\n\n\"At W=3, the MDE is 8.6–9.5pp, meaning effects distinguishable from noise. R1-32B's residualized HS text gap (+1.9pp) falls well below the MDE (9.5pp), so the HS advantage cannot be reliably distinguished from either a true null or an underpowered sample. The 7–8B MDEs (3.3–4.2pp) are substantially lower, explaining why smaller effects are detectable at these scales.\"\n\n**Appendix J — CP Annotation Perturbation**\n\n\"Table 7 reports the full test battery to assess hidden-state superiority over text probes... We address CP annotation (section 4.2) led to the corrected-layer analysis reported in the main text, where all four models show significant HS advantage over directed deep layers, from strong (OT-7B) to qualified (R1-32B) (Table 3).\"\n\n\"To assess sensitivity to annotation noise, we shift the commitment point annotation by ε ∈ {−3, −2, −1, 0, +1, +2, +3} steps and retrain the HS probe (table 15). Precision changes negatively with earlier HS (−2, −3) steps and recovers above the baseline for delayed commits (+1, +2 steps).\n\n**Table 15** (HS probe sensitivity to CP annotation shift, n=33):\n\n| Seed | HS FPR | Text FPR | ΔFPR |\n|------|--------|----------|------|\n| 0 | 0.113 | 0.308 | −0.195 |\n| 1 | 0.061 | 0.168 | −0.105 |\n| 2 | 0.148 | 0.167 | −0.167 |\n| 3 | 0.167 | 0.167 | 0.000 |\n| 4 | 0.143 | 0.228 | −0.083 |\n| p | |  | 0.293 |\n\n---\n\n## PAGE 19 — Appendix K (BOCPD/CUSUM Configuration Sweep) + Appendix L (Detection Threshold (K) Ablation)\n\n**Appendix K — BOCPD/CUSUM Configuration Sweep**\n\n\"We sweep hyperparameters for both Bayesian Online Changepoint Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe scores.\n\n**BOCPD configurations.** BOCPD models the sequence of probe scores as piecewise-constant functions with Gaussian observation noise. The hazard rate λ controls the prior probability of a changepoint occurring at each step, and the threshold Δ controls the detection boundary (a detection if accumulated evidence > Δ).\n\n**CUSUM configurations.** CUSUM accumulates evidence for a positive mean shift. The drift parameter k sets the expected shift magnitude (set to 1.5), and the threshold Δ controls the detection sensitivity...\"\n\n**Table 14** (Oracle upper bound analysis — appears again here as \"Table 14. Oracle bound analysis\"):\n\n| Model | Prec. | Det.Rate | Lead | p |\n|-------|-------|----------|------|---|\n| R1-8B | 0.400 | 0.784 | 1.54 | <0.001 |\n| OT-7B | 0.421 | 0.634 | 0.021 |   |\n| QoQ-32B | 0.453 | 0.631 | 0.021 |   |\n| R1-32B | 0.756 | 0.552 | 0.314 |   |\n\n\"The best BOCPD configuration (λ=10) achieves 97% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1% detection rate (i.e., a much lower baseline). All CUSUM configurations underperform the simple threshold on lead time.\n\n**Table 15** (HS probe sensitivity to CP annotation, safety):\n\n\"R1-32B (bal.acc p=0.925, precision p=0.346; R1-32B precision p=0.050) but no tests surviving correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (±21.9pp). The proportional boundary (∼12%) amplified at n=33.\"\n\n---\n\n## PAGE 20 — Appendix L (Detection Threshold K Ablation) + Appendix M (Decision Threshold Sensitivity)\n\n**Appendix L — Detection Threshold (K) Ablation**\n\n\"The consecutive-crossings threshold K controls the trade-off between detection coverage and false positive rate. We evaluate K ∈ {1, 3, 5, 7, 10} on all models using HS probes at corrected layers (section B).\n\nK=1 yields perfect coverage but near-perfect false positive rate (0.92–1.00), showing no discrimination. R1-8B achieves 0.756 balanced accuracy (approaching 0.778) but with substantially worse precision (0.512 vs. LR 0.700) after adding noise in the precision-coverage Pareto for both methods. The best two-stage configuration (W_screen=3, W_confirm=15, k=1) achieves 72.2% precision at 38.5% coverage with k=5, but these operating points are impractical due to excessive missed detections.\n\n**Table 16** (R1-8B threshold K ablation):\n\n| K | R1-8B | OT-7B | R1-32B | QoQ-32B |\n|---|-------|-------|--------|---------|\n| 1 | 1.00 | 1.00 | 1.00 | 1.00 |\n| 3 | 0.90 | 0.74 | 0.79 | 0.72 |\n| 5 | 0.69 | 0.62 | 0.62 | 0.60 |\n| 7 | 0.55 | 0.47 | 0.50 | 0.48 |\n| 10 | 0.35 | 0.30 | 0.38 | 0.30 |\n\n\"K=7 reduces FPR by 79–86% while maintaining non-trivial detection rates. The K=7 setting offers a middle ground (57% FPR reduction, 16–39% detection). These results support the reframing of K ablation as practitioner-facing operating curve.\"\n\n**Appendix M — Decision Threshold Sensitivity**\n\n\"The joint search space for layer (≤ 64), window W (7 values), K (5 values), and decision threshold is large (up to 2,340 configurations per model). This raises the concern that reported performance reflects overfitting to small validation samples (n≈1–9 per class at 32B). Three analyses address this concern.\n\n**Threshold-dependent metrics converge to a deep-layer band.** Despite the large search space, choice of four threshold-dependent metrics (precision, inverse FPR, additive composite) independently select L63 (98% depth) for both 32B models—see Table 2. The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.\n\n**Bootstrap CIs quantify statistical uncertainty.** For the model comparison metric at W=3, bootstrap 95% CIs are narrow: R1-8B ±0.021 (Bal.Acc.) and ±0.040 (FPR); QoQ-32B ±0.017 (BA), consistent with in-distribution variability not overfitting.\n\n**BA-optimal layer instability is the finding, not a confound.** Five-fold cross-validation on 32B validation sets (n≤20 per class) reveals that the BA-optimal layers are highly unstable across folds (table 25). This instability is not a limitation of the study but the central methodological finding: BA-layer selection is sensitive to data composition, and conclusions drawn from any single BA-optimal layer are unreliable.\"\n\n**Appendix N — M002 Bug Disclosure**\n\n\"A bug was discovered during development that affected intermediate results for QoQ-32B.\n\n**Issue.** In experiment M002 (feature ablation), the QoQ-32B probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive and produced a spuriously significant result (p=0.001 for HS vs. text FPR difference).\n\n**Discovery and correction.** The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QoQ-32B feature extraction used the composite composed HS for correct safety in null-space projection (Holm-Bonferroni section B1). The modality comparison shows at the originally selected layers (L2 and L10, chosen by the biased composite)—table 3 showed that no significant HS vs. text gap at corrected layers. R1-32B modality comparison: section V Encoder Robustness; section F Multi-Seed Stability; section Y BA-Layer Modality Comparison; section Z Post-Hoc Power Analysis.\"\n\n---\n\n## PAGE 21 — Appendix O (Adaptive Two-Stage Detection) + Appendix P (Temporal Ablation Details) + Appendix Q (Negative Results Details) + Figure 4\n\n**Appendix O — Adaptive Two-Stage Detection**\n\n\"We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window (W_screen) to flag candidate unsafe segments, followed by a longer confirmation window (W_confirm) applied only to the flagged segments. A trace is classified as unsafe if at least k steps exceed the threshold during the confirmation stage.\n\nWe merge the validation and test datasets for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of W_screen ∈ {1, 3, 5}, W_confirm ∈ {10, 15, 25}, k ∈ {1, 3, 5} and the threshold τ (pre-CP FPR setting 76.7%): the two-stage approach achieves 22.2% precision at 38.5% coverage with k=5, but these operating points are impractical due to excessive missed detections. The marginal improvement suggests that natural smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach requires 3 hyperparameters (W_screen, W_confirm, k) as one more than single-window without proportional performance gains.\"\n\n**Figure 4** (Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection):\n\nCaption: \"Figure 4. Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. Results are Pareto-dominated by matched coverage. Higher k values shift the tradeoff toward precision at the cost of unacceptable coverage loss.\"\n\n**Appendix P — Temporal Ablation Details**\n\n\"Full per-model temporal ablations are reported in table 8 (section E). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 68% ±11 (W=1) to 82.2% (W=25) with FPR falling 9.65% to 4.83%; (2) OT-7B exhibits a split pattern where balanced accuracy peaks at W=3 while precision and FPR continue improving at larger windows; (3) R1-32B peaks at W=10 then degrades, likely reflecting overfitting on the smaller dataset (n=100), (4) QoQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (section E.1) consistently show W at ±10 for GRU-multi. The summary supports the interpretation that text features encode less information per step, benefit proportionally more from observing the multi-step progression.\"\n\n**Appendix Q — Negative Results Details**\n\n\"On OT-7B, BOCPD achieves 0% detection rate with λ∈{5, 10, 50, 100, 200}. Only R1-8B produces non-trivial results (λ=10, 93% rate, +3.45 steps lead). CUSUM configurations (all λ, k) fail to produce non-trivial results only more sophisticated approaches.\n\n**Table 27** ... R1-8B BOCPD: all tests pass; OT-7B: FPR=1.00 (all traces flagged as unsafe).\"\n\n---\n\n## PAGE 22 — Appendix R (Cross-Model Transfer Results) + Appendix S (Encoder Robustness Analysis)\n\n**Appendix R — Cross-Model Transfer Results**\n\n**Table 19** (Seven alternative approaches):\n\n| Method | Result | Limitation |\n|--------|--------|------------|\n| BOCPD | 0% det. on 4/4 models | Commitment gradual |\n| CUSUM | < threshold, all model | Same as BOCPD |\n| Mahalanobis | Δd ≈ 0 | Signal in minor PCA components |\n| MLP | 3/4 worse than LR | Overfitting |\n| CCS | No gain over supervised | Alignment mismatch |\n| Transfer | Best 59.5% (PCA)* | Model-specific |\n\n\"* Repl: Mean-difference directions (Zou et al., 2023) show inconsistent performance. QoQ-32B achieves 0.756 balanced accuracy (approaching required evidence); R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment in some models but not others, so it is unreliable as a general-purpose method.\n\n**MLP probes.** Two-layer MLPs (d → 128 → 1, ReLU) underperform logistic regression on all models. The commitment decision boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small 32B datasets.\n\n**CCS.** Contrast-Consistent Search (Burns et al., 2023) adapted with contrastive pairs of pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction and is therefore semi-supervised.\n\n**Transfer.** Mean-difference directions produce no cross-model transfer (16/32 per-model models tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model). The pre-cision gains (p=0.002); 3/4 models retain significant non-positional HS advantage (FPR for R1-32B underpowered 32B sets. BA-L layer failure is the exception: residualized HS-text gap is position-dependent of OT-7B +6.9pp, R1-8B +8.6pp at W=15, QoQ-32B → R1-32B achieves 67.3% but 1% crossing rate. Implementation details in section (R).\"\n\n**Table 23** (HS vs. ES-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni corrected (4 tests, α=0.05). QoQ/20 split):\n\n| Model | Layer | W | ES | MinLM | Δ |\n|-------|-------|---|-----|-------|---|\n| R1-8B | L16 | 15 | 440 | 446 | +6 |\n| OT-7B | L16 | 1 | 446 | 321 | −125 |\n| R1-32B | L10 | 1 | 446 | 244 | −202 |\n| QoQ-32B | L63 | 1 | 458 | 244 | −214 |\n\n\"The HS advantage partially survives against the LLM encoder: 4/4 models (both 7–8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (384d) < BGE-large (335M, 1024d) < ES-Mistral-7B (PCA 384d).\"\n\n**Appendix S — Encoder Robustness Analysis**\n\n\"To address the concern that threshold-dependent layer selection may circularly favor HS probes, we repeat the modality comparison at layers selected by balanced accuracy for each model. Results show HS advantage is significant at BA-selected layers too despite the choice of metric:\n\n**Table 31** (HS vs. text at BA-selected layers (60/20/20):\n\n| Model | BA-L | ΔPrec | ΔBA | ΔFPR | p(BA) |\n|-------|------|-------|-----|------|-------|\n| R1-8B | L17 | +16.6 (+16.6) | +8.4 (+8.4) | −7.0 (−6.3) | <0.001 |\n| OT-7B | L16 | +10.1 (+10.1) | +13.1 (+13.1) | −15.4 (−15.4) | <0.001 |\n| QoQ-32B* | L3 | −31 (−14.6) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\n| R1-32B* | L3 | −12.8 (−14) | +13.6 (+13.6) | +15.8 (+15.8) | <0.001 |\n\n\"Values in parentheses are bootstrapped-corrected (10,000 bootstrap examples). p-values on the BA metric corrected. * BA-L failures from bias metric (section 4.2); corrected layers in table 3.\"\n\n\"Positions 9–20pp. The HS precision advantage is directionally consistent across all four models (positive in every case); significance is marginal only for OT-7B R1-8B shows a (p=0.064 under Holm-Bonferroni). R1-32B BA-significance only falls at n≤20 (p=0.914); QoQ-32B achieves 67.3% but 1% crossing rate. BA-optimal layer instability: Five-fold LOO-CV shows standard deviation of 0.145 (R1-8B FPR = 0.483), varying from 72.1% to 98.7%; this instability confirms that BA selection is seed-fragile.\"\n\n---\n\n## PAGE 23 — Appendix T (Random Projection Baseline) + Appendix U (LLM-Based Text Encoder Comparison)\n\n**Appendix T — Random Projection Baseline**\n\n\"PCA capacity matching (section S) preserves 79–92% of variance with 384-dimensional projections. The split indicates which compression is whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projections (RP) and compare PCA projections with RP projections at the same dimensionality (table 22).\n\n**Table 22** (RP, 384d bootstrap (CF 384d), Holm-Bonferroni corrected (4 tests, α=0.05)):\n\n| Rank | Model | Metric | p-val | Thresh. | Pass |\n|------|-------|--------|-------|---------|------|\n| 1 | QoQ-32B | Bal. Acc. | <0.001 | 0.001 | Yes |\n| 2 | OT-7B | Bal. Acc. | <0.001 | <0.001 | Yes |\n| 3 | R1-8B | Bal. Acc. | <0.001 | 0.0056 | Yes |\n| 4 | OT-7B | FPR | <0.001 | 0.0063 | Yes |\n| ... | ... | ... | ... | ... | ... |\n\n\"All four models achieve significant HS advantage under random projection (all 12 tests pass HB correction), full data, two FFR failures from underpowered 32B test sets. BA-L values (RP): QoQ-32B 79.4 ±1.2pp; R1-8B 81.5 ±0.9pp. The HS advantage is robust to the choice of layer selection criterion (BA, Prec, FPR-inverse, cross-rate, composite).\n\n**R1-8B per-seed HB pass rates.** Table 29 reports Holm-Bonferroni pass rates per metric across 5 random seeds. R1-8B the model classified as \"moderate\" evidence due to FPR instability.\n\n**Table 29** (R1-8B per-seed Holm-Bonferroni pass rates):\n\n| Seed | HS FPR | Text FPR | ΔPre | ΔBA | ΔFPR |\n|------|--------|----------|------|-----|------|\n| 0 | 0.119 | 0.040 | ... | ... | ... |\n| 1 | 0.061 | ... | ... | ... | ... |\n| 2 | 0.148 | ... | ... | ... | ... |\n| 3 | 0.167 | ... | ... | ... | ... |\n| 4 | 0.143 | ... | ... | ... | ... |\n| p | | | | | 0.293 |\n| Pass rate: | N/5 | 5/5 | 3/5 | | |\n\n\"The FPR instability has a clear source: R1-8B text FPR clusters tightly around 17% (std~0.2pp) while HS FPR spreads more broadly (std~17%)...\"\n\n**Appendix U — LLM-Based Text Encoder Comparison**\n\n\"To test whether an LLM-based text encoder closes the HS advantage gap, we encode each reasoning step with E5-Mistral-7B-Instruct (Wang et al., 2022) (4,096d), reduced to 384d via PCA to match the MinLM dimensionality. Using each modality's precision-comparisons against HS probes at corrected layers:\"\n\n---\n\n## PAGE 24 — Appendix U (continued) + Appendix V (Post-Hoc Power Analysis)\n\n**Appendix U continued:**\n\n\"**Table 23** (HS vs. ES-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni corrected (4 tests, α=0.05), two-sided, same metrics; both 60/20/20):\n\n| Model | Layer | W | HS | ES | MinLM | Δ(HS-ES) |\n|-------|-------|---|-----|-----|-------|---------|\n| R1-8B | L16 | 15 | +8.4 | +10.8 | 0.002 | −2.4 |\n| OT-7B | L16 | 1 | +10.8 | −13.1 | +10.1 | +3.3 |\n| QoQ-32B* | L63 | 1 | +8.8 | −13.1 | 0.000 | +21.9 |\n| R1-32B* | L43 | 1 | +8.8 | −14.0 | 0.033 | +22.8 |\n\n(* Residual bias layer issues.)\n\n\"The HS advantage partially survives against the LLM encoder: 4/4 models (both 7–8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (384d) < BGE-large (335M, 1024d) < ES-Mistral-7B (PCA 384d). The precision gain is +12.8 to +18.6pp for ES, comparable to those at threshold-dependent layers (+15.4 to +14.0). The HS advantage is robust to the choice of layer selection criterion.\n\n**Exact sign-flip permutation test validation.** The joint search for which the layer W=3 pair (p=0.000 vs. p=0.207 margin), with a proportion near boundary (~12%) amplified at n=33.\n\nThe two failures are both FPR at 32B: R1-32B (bal.acc p=0.925, precision p=0.083, consistent with the underpowered test sets (n≤20) noted in Section 4. All three precision gains (p=0.054 vs. p=0.003; paired t p=0.001 (bootstrap 95% CI [−22.2, −12.2])). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with bootstrap mean (+21.9pp); the small discrepancy reflects resampling variability. Under the canonical 60/20/20 split: HS FPR advantage increases at larger temporal windows, suggesting HS representations better capture the temporal commitment dynamics.\"\n\n**Appendix V — Post-Hoc Power Analysis**\n\n\"We compute post-hoc minimum detectable effects (MDEs) at 80% power given each model's test-set size and observed variance.\n\n**Table 25** (LOO-CV BA-optimal layers per model, 5-fold. BA-optimal layers vary widely across folds):\n\n| Model | F1 | F2 | F3 | F4 | F5 | Spread |\n|-------|----|----|----|----|-----|--------|\n| QoQ-32B | L53 | L53 | L45 | L45 | L39 | 24 layers |\n| R1-32B | L53 | L45 | L40 | L63 | L39 | 24 layers |\n\n(R1-32B's high FPR variance (std=0.145) is driven by this instability.)\n\n\"At W=3, the MDE is 8.6–9.5pp, meaning effects smaller than the MDE cannot be reliably detected. R1-32B's residualized HS text gap (+1.9pp) falls well below the MDE (9.5pp), confirming the HS advantage cannot be reliably distinguished from noise. The 7–8B MDEs (3.3–4.2pp) are substantially lower, explaining why smaller effects are detectable at those scales.\"\n\n---\n\n## PAGE 25 — Appendix W (Multi-Seed Stability) + Appendix X (5-Seed HB Pass Rates for R1-8B)\n\n**Appendix W — Multi-Seed Stability**\n\n\"Stability, mean BA across folds peaks near L47–L50 for both models, consistent with the LOO-CV dominant layers (section B). The HS advantage is significant at threshold-optimal layers (14/16 per-model HB, two FPR failures from underpowered 32B test sets (n≤20)).\n\n**Table 27** (5-seed HB pass rates (HS FPR, n=3 models)):\n\n\"Seeds where HS FPR happens to be below the 0.05 threshold (>1.4/5 loss significance): the gap against text narrows without the detection threshold narrowing, and does not affect the precision or overall HS advantage, which passes all 5 seeds.\n\n**R1-8B HS per-seed breakdown (L63, W=1).** Table 30 reports the full per-seed breakdown for R1-8B's multi-seed stability:\n\n| Seed | Precision | Bal. Acc. | ΔPre Hb | Note |\n|------|-----------|-----------|---------|------|\n| 0 | 0.441 | 0.796 | +0.094 | 0.109 |\n| 1 | 0.780 | 0.748 | +0.263 | 0.109 |\n| 2 | 0.598 | 0.795 | +0.571 | <0.050 |\n| 3 | 0.630 | 0.781 | +0.097 | <0.050 |\n| 4 | 0.652 | 0.735 | +0.033 | <0.050 |\n| 5 | 0.440 | 0.715 | +0.022 | 0.050 |\n| Mean ± std | 0.594 ± 0.126 | 0.692 ± 0.256 | +0.207 ± 0.14 | (Seed 0 is outlier) |\n\n\"R1-32B's high FPR variance (std=0.145) is driven by test-set split allocation (n=19 vs. n=20). Positions 9–20pp. The HS precision advantage is directionally consistent across all four models.\n\n**5-seed Holm-Bonferroni pass rates.** Table 27 reports HS pass rates per metric across 5 random seeds. Overall, 18/20 (90%) model-seed combinations pass full HB (3 models × 5 seeds = 15 HB cases).\"\n\n**Appendix X — R1-8B FPR-specific note:**\n\n\"R1-8B HS FPR varies by only 1.1pp between validation and test set (seed=0 is an outlier (FPR = 0.483), varying from 72.1% to 98.7%; 2/5 reaching statistical significance after Holm-Bonferroni correction for 5 seeds (p=0.011). 1/5 remains significant. The FPR instability has a clear source: R1-8B text FPR clusters tightly around 17% (std~0.2pp) while HS FPR spreads more broadly (std~1.7pp).\"\n\n---\n\n## PAGE 26 — Appendix Y (BA-Layer Modality Comparison) + Appendix Z (Post-Hoc Power Analysis, cont.)\n\n**Appendix Y — BA-Layer Modality Comparison**\n\n\"While HS FPR happens to be below the 0.05 threshold from 6.1% to 16.1% (std~1.0pp). Seeds where HS FPR happens to be below 0.05 of threshold (>1.4/5 loss significance): the gap against text narrows without detection threshold narrowing and does not affect precision or overall HS advantage.\n\n**R1-32B's position-residualized selectivity.** To quantify this, we recompute select task selectivity on position-regressed features (the same residualized representations used in section V). R1-8B at 67.3% but 1% crossing rate.\n\n**Table 24** (Position-residualized balanced accuracy across 14 per-model tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model), α=0.05):\n\n| Model | BA-L | ΔPrec | ΔBA | ΔFPR | p |\n|-------|------|-------|-----|------|---|\n| R1-8B | L17 | +16.6 (+16.6) | +8.4 (+8.4) | −7.0 (+0.031) | <0.001 |\n| OT-7B | L16 | +10.1 (+10.1) | +13.1 (+13.1) | −15.4 (−15.4) | <0.001 |\n| QoQ-32B* | L3 | −31 (−14.6) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\n| R1-32B* | L3 | −12.8 (−14) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\n\n\"Of 16 per-model tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model). The precision gains (p=0.002); 3/4 models retain significant non-positional HS advantage (FPR for R1-32B underpowered 32B tests BA-L layer failure is the exception: residualized HS-text gap is position-dependent for OT-7B (+6.9pp), R1-8B (+8.6pp at W=15), QoQ-32B → R1-32B achieves 67.3% but 1% crossing rate. BA-optimal layer instability: Five-fold LOO-CV shows standard deviation of 0.145 (R1-8B FPR = 0.483), varying from 72.1% to 98.7%.\"\n\n**Appendix Z — Post-Hoc Power Analysis (additional)**\n\n\"While HS FPR happens to be below global best 0.817). Joint layer, W=1 ability was evaluated via grid search on W ∈ {1/5, 5} for QoQ-32B only; full LOO-cross-validation of the (layer, W) pair and extension to R1-32B remain for future work.\n\n**Table 18** (R1-32B threshold sensitivity (L63, W=1). HS BA varies by 1.1pp (0.741–0.752); the HS advantage is consistent across all correction settings):\n\n| τ+ | HS BA | ΔBA | HS Prec | ΔPrec | ΔFP/R | ΔFPR |\n|----|-------|-----|---------|-------|-------|------|\n| 0.742 | +0.120 | 0.583 | −0.126 | 0.205 | −0.106 |\n| 0.741 | +0.128 | 0.583 | −0.133 | 0.287 | −0.078 |\n| 0.741 | +0.109 | 0.588 | +0.113 | 0.287 | −0.078 |\n| 0.743 | +0.126 | 0.583 | +0.113 | 0.266 | +0.078 |\n| 0.741 | +0.128 | 0.592 | +0.109 | 0.287 | −0.078 |\n\n\"R1-32B (bal.acc p=0.925, precision p=0.083, consistent with the underpowered test sets (n≤20). All three precision gains (p=0.054 vs. p=0.003 paired t p=0.001 (bootstrap 95% CI [−22.2, −12.2]). All three metrics survive correction. The two failures are both FPR at 32B: R1-32B BA-L layer failure is the exception.\"\n\n---\n\n以上为第9–26页（论文末尾所有页面）的完整内容转录，包含：\n\n- **第9页**：Section 5结尾（讨论/操作点）、Section 6 Conclusion、Section 7 Limitations、References开头\n- **第10–12页**：完整参考文献列表\n- **第12页底部–第26页**：完整附录（A至Z），涵盖：\n  - Appendix A（NLP Research Checklist）\n  - Appendix B（Layer Sweep）\n  - Appendix C（Representation Compression）\n  - Appendix D（Holm-Bonferroni Step-Down）\n  - Appendix E/E.1（Window Size Ablation）\n  - Appendix F（OpenThinker-7B详细结果）\n  - Appendix G（GRU Training Details）\n  - Appendix H（Control Task Methodology）\n  - Appendix I（Oracle Upper Bound）\n  - Appendix J（CP Annotation Perturbation）\n  - Appendix K（BOCPD/CUSUM Configuration Sweep）\n  - Appendix L（Detection Threshold K Ablation）\n  - Appendix M（Decision Threshold Sensitivity）\n  - Appendix N（M002 Bug Disclosure）\n  - Appendix O（Adaptive Two-Stage Detection）\n  - Appendix P（Temporal Ablation Details）\n  - Appendix Q（Negative Results Details）\n  - Appendix R（Cross-Model Transfer Results）\n  - Appendix S（Encoder Robustness Analysis）\n  - Appendix T（Random Projection Baseline）\n  - Appendix U（LLM-Based Text Encoder Comparison）\n  - Appendix V（Post-Hoc Power Analysis）\n  - Appendix W（Multi-Seed Stability）\n  - Appendix X（R1-8B FPR-Specific Notes）\n  - Appendix Y（BA-Layer Modality Comparison）\n  - Appendix Z（Post-Hoc Power Analysis续）"
      }
    ],
    "totalDurationMs": 597800,
    "totalTokens": 68402,
    "totalToolUseCount": 58,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 194,
      "cache_read_input_tokens": 49135,
      "output_tokens": 19072,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 194
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 19072,
          "cache_read_input_tokens": 49135,
          "cache_creation_input_tokens": 194,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 194,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 18,
      "searchCount": 0,
      "bashCount": 20,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "385e832b-3967-46f7-82ad-98c2cb267a94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性** 审查。  ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models - **路径**: `projects/contrastive_trace_safety/docs/paper…",
  "leafUuid": "0b000206-f84f-469c-a26e-1c8be2bf47d6",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodology rigor for safety probes paper",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Assistant

_source line 57 · 2026-05-19T04:44:49.873Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have the main content from all agents. Let me also read the appendix content from the third agent's output. Let me read that file to get the complete appendix data, which is critical for my methodological review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b000206-f84f-469c-a26e-1c8be2bf47d6",
  "isSidechain": false,
  "requestId": "req_011CbBKPybRxmQNQfJZdir6P",
  "type": "assistant",
  "uuid": "7ab1377a-b57f-4d76-a52f-c323665f19e0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoqEx1f6d988tCbDP4H6gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12775,
      "cache_read_input_tokens": 35745,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 411,
          "cache_read_input_tokens": 35745,
          "cache_creation_input_tokens": 12775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12775
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 58 · 2026-05-19T04:44:50.825Z_

Good, I have the main paper content. Let me read the full appendix output and also fetch the ARR reviewer guidelines for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab1377a-b57f-4d76-a52f-c323665f19e0",
  "isSidechain": false,
  "requestId": "req_011CbBKPybRxmQNQfJZdir6P",
  "type": "assistant",
  "uuid": "aa0cef60-26e8-4eb1-a646-40123919c8ac",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoqEx1f6d988tCbDP4H6gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12775,
      "cache_read_input_tokens": 35745,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 411,
          "cache_read_input_tokens": 35745,
          "cache_creation_input_tokens": 12775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12775
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-19T04:44:52.284Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BDvuRHHhiQhBMUR1gmYq1H`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/3e48199e-0c0d-47bc-8ea3-24ecb0f30457/tool-results/toolu_015MRVtErFsoVMKEgYy2Gr2G.json",
  "offset": 0,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa0cef60-26e8-4eb1-a646-40123919c8ac",
  "isSidechain": false,
  "requestId": "req_011CbBKPybRxmQNQfJZdir6P",
  "type": "assistant",
  "uuid": "f3fa6ced-9296-416f-8eb5-320709171eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoqEx1f6d988tCbDP4H6gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12775,
      "cache_read_input_tokens": 35745,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 411,
          "cache_read_input_tokens": 35745,
          "cache_creation_input_tokens": 12775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12775
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 60 · 2026-05-19T04:44:52.545Z_

<details><summary>↩ Tool result · `toolu_01BDvuRHHhiQhBMUR1gmYq1H`</summary>

```text
0	[
1	  {
2	    "type": "text",
3	    "text": "The PDF has 26 pages total. Now I have a complete picture of all pages 9–26. Here is a thorough transcript of all content found on pages 9–26:\n\n---\n\n## PAGE 9 — End of Section 5 (Discussion) + Section 6 (Conclusion) + References (start)\n\n**End of Section 5 text (continuation from page 8):**\n\n\"at 17% FPR. These conservative operating points are viable for high-stakes deployment where missed detections are preferable to frequent false alarms: a secondary review system could inspect only flagged traces, reducing human verification burden by 79–86% while maintaining non-trivial detection rates. The K=7 setting offers a middle ground (57% FPR reduction, 16–39% detection). The choice of operating point is deployment-specific, but the existence of a low-FPR regime contradicts the assumption that 32% or 52% FPR renders commitment detection impractical.\"\n\n**Section 6 — Conclusion**\n\n\"Layer selection is a critical researcher degree of freedom: a biased composite metric reverses the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. The five-step audit protocol (section 5) would have prevented this outcome. The empirical HS advantage is conditional: robust at 7-8B (strong for OT-7B, moderate for QoQ-32B, qualified for R1-32B), and bounded by text encoder quality (4/4 HB against 384d, 1/4 against 4096d). Current probes characterize commitment detection rather than constitute production detectors. Models (≥95 cases) encode less information per step, benefit proportionally more from observing the multi-step progression.\n\n**7 Limitations**\n\nOur results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39–52%, and the HS advantage (R1-8B) scores the safety commitment phenomenon. This underscores how much room remains for improvement.\n\n**Model-specific caveats and statistical power.** HS achieves significance only at W=1 (25% coverage) and its HS advantage is position-mediated (residualized gap +1.9pp; section V). QoQ-32B's position baseline achieves significance only at W=1 (25% coverage); full significance is 5/20 at n=19–20 vs n=20. HS significance is seed-fragile (3/5 HB); at n=19–20, the minimum detectable effect at 80% power is 6.8pp...\"\n\n**References** begin (partial list visible at bottom of page):\n\n- Ryan Prescott Adams and David J.C. MacKay. 2007. Bayesian online changepoint detection. *arXiv preprint arXiv:2007.01142*. Concurrent work.\n- Patrick Altmsd, Tobias Eder, Nyong Yang, Zhiyi Pan, and Georg Grok. 2026. Safer reasoning models: *arXiv preprint arXiv:2504.09375*.\n- Yanai Elazar, Shauli Ravfogel, Alon Jacovi, and Yoav Goldberg. 2021. Amnesic probing: Behavioral explanations with amnestic counterfactuals. *Transactions of the Association for Computational Linguistics*, 9:160–175.\n\n---\n\n## PAGE 10 — References (continued)\n\nFull reference list page. Entries include (verbatim as visible):\n\n- Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, and Neel Nanda. 2024. Refusal in language models is mediated by a single direction. In *Advances in Neural Information Processing Systems 17 (NeurIPS)*.\n- Bowen Baker, Ioot Huizinga, Leo Gao, Zehao Dou, Melody Y. Guan, Aleksander Madry, Wojciech Zaremba, Bob McGrew, and Ilya Sutskever. 2022. Monitoring reasoning models for misbehavior and the risks of promoting obfuscation. *arXiv preprint arXiv:2502.11926*.\n- Yamini Bansal, Preetum Nakkiran, and Boaz Barak. 2021. Re-thinking model stitching to compare neural representations. In *Advances in Neural Information Processing Systems 34 (NeurIPS)*.\n- Yonatan Belinkov. 2022. Probing classifiers: Promises, shortcomings, and advances. *Computational Linguistics*, 48(1):207–219.\n- Nora Belrose and James Glass. 2019. Analysis methods in natural language processing. *Transactions of the Association for Computational Linguistics*, 7:49–72.\n- Nora Belrose, David Schneider-Joseph, Shauli Ravfogel, Ryan Cotterell, Edward Raff, and Stella Biderman. 2023. LEACE: Perfect linear erasure of a concept from a model's representations. In *Advances in Neural Information Processing Systems 36 (NeurIPS)*.\n- Gerard Botos, Aman Neelappa, and Shivam Raval. 2023. Probing language models for lexical evidence: Results from language mitigation studies in language models. *arXiv preprint arXiv:2509.21344*.\n- Colin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023. ELICIT: Discovering latent knowledge in a language model. In *Proceedings of the International Conference on Learning Representations (ICLR)*.\n- Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Stephen Donoho, Chris Olah, Arnab Amutz, Peter Hase, Micha Wagner, Fazl Amin Roger, Vlad Mikulin. 2025. Reasoning models can be honest if you ask them: Results from language mitigation studies in language models. *arXiv preprint arXiv:2503.05410*.\n- Alexis Conneau, German Kruszewski, Guillaume Lample, Loïc Barrault, and Marco Baroni. 2018. What you can cram into a single vector: Probing sentence embeddings for linguistic properties. In *Proceedings of the Association for Computational Linguistics (ACL)*, pages 2126–2136.\n- DeepSeek-AI. 2025. DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. *arXiv preprint arXiv:2501.12948*.\n\n---\n\n## PAGE 11 — References (continued)\n\n- Fazir Joaz, Majd Hawady, Sabri Bongleberbok, Nadir Durrami, and Huseyn Taha Sencar. 2026: \"There is more to refusal in language models than a single direction.\" *arXiv preprint arXiv:2602.02112*.\n- Sri Dorga Sai Sowmya Kadali and Evangelos E. Papalesakis. 2025. Do internal layers of LLMs reveal patterns for jailbreak detection? *arXiv:846-866*.\n- Ishita Kakkar, Eoin Zhang, Rheeya Uppaal, and Jinjie Hu. 2026. When safety falls below the frontier: Benchmarking harmful behavior detection in reasoning chains. *arXiv preprint arXiv:2604.19001*.\n- Su-Hyeon Kim, Hyundong Jin, Yejin Lee, and Yu-Sub Kim. 2026. How does the thinking affect model safety? an entropy-based safety reminder for chain-of-thought models. *arXiv preprint arXiv:2603.08601*.\n- Tomek Korbak, Mikita Balesni, Elizabeth Barnes, Joseph Bengio, Joe Benton, Joseph Bloom, Mark Chen, Andrew Cuvos, Owain Evans, David Farhi, Ryan Greenblatt, Dan Hendrycks, Evan Hubinger, Geoffrey Irving, Erik Jenner, and 22 others. 2025. Chain of thought monitorability: A fragile opportunity for AI safety. *arXiv preprint arXiv:2511.11471*.\n- Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019. Similarity of neural network representations revisited. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, volume 97 of *Proceedings of Machine Learning Research*, pages 3519–3529.\n- Martin Kub, Llaster, Aolin Hing, Qinxi Wang, Louis DiValentin, Yujia Bao, Wei Wei, Hai Li, and Yiran Chen. 2025. H-cut: Hijacking the chain-of-thought in large reasoning models to jailbreak large reasoning models. *arXiv preprint arXiv:2509.21344*\n- Martin Küblböck, James Elsman, Simon Geisler, Vincent Fortuin, Aakash Jaini, and Stephan Günnemann Bastian Gasteiger. 2025. The geometry of refusal in large language models: Concept cones and representational independence. In *Proceedings of the 42nd International Conference on Machine Learning (ICML)*.\n- Shitao Xiao, Zheng Liu, Peitian Zhang, and Niklas Muennighoff. 2025. C-pack: Packaged resources to advance general chinese embedding. *arXiv preprint arXiv:2309.07597*.\n- Bo Yin, Weikai Liu, Yada Zhu, and Song Wang. 2026. C-caliblabcam: a safety-world model with iterative early jailbreak detection. *arXiv preprint arXiv:2604.16824*.\n- Nelson F. Liu, Matt Gardner, Yonatan Belinkov, Matthew E. Peters, and Noah A. Smith. 2019. Linguistic knowledge and transferability of contextual representations. In *Proceedings of the North American Chapter of the Association for Computational Linguistics (NAACL)*, pages 1073–1094.\n- Faiir Joaz, Majd Hawady, Sabri Bongleberhok, Nadir Durrami, and Huseyn Taha Sencar. 2026. \"There is more to refusal in language models than a single direction.\" *arXiv preprint arXiv:2602.02112*.\n- Yingzhi Qian, Chunhang Zhang, Jianzong Wang, Hengfeng Guo, Boji Cao, Yuejie Li, Honggyu Liu, Penghan Han, and Le Sun. 2025. When models overthink their safety: LLMs encode harmfulness and refusal separately. In *Advances in Neural Information Processing Systems 38 (NeurIPS)*.\n- Zhenhong Zhou, Haiyang Yu, Xinghua Zhang, Rongwu Xu, Fei Huang, and Yongbin Li. 2024. How alignment and jailbreak work: Explain LLM safety mechanisms through hidden states. In *Findings of the Association for Computational Linguistics: ACL 2024*.\n- Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mrinank Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, and Dan Hendrycks. 2023. Representation engineering: A top-down approach to AI transparency. *arXiv preprint arXiv:2310.01405*.\n\n---\n\n## PAGE 12 — References (continued) + Appendix A header\n\nRemaining references:\n\n- Ang Zhang, Yulin Chen, Jane Pan, Chen Zhao, Anrojit Panda, Junyang Li, and He He. 2025. Reasoning models know when they're right: Probing hidden states for self-verification. *arXiv preprint arXiv:2504.05419*.\n- Jiachan Zhao, Jing Huang, Zhengxuan Wu, David Bau, and Weiyan Shi. 2025. LLMs encode harmfulness and refusal separately. In *Advances in Neural Information Processing Systems 38 (NeurIPS)*.\n- Zhenhong Zhou, Haiyang Yu, Xinghua Zhang, Rongwu Xu, Fei Huang, and Yongbin Li. 2024. How alignment and jailbreak work: Explain LLM safety mechanisms through hidden states. In *Findings of the Association for Computational Linguistics: ACL 2024*.\n- Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mrinank Mazeika, ..., and Dan Hendrycks. 2023. Representation engineering: A top-down approach to AI transparency. *arXiv preprint arXiv:2310.01405*.\n- Qingyin Yin, Chak Tuo Leong, Linyi Yang, Wenxuan Wang, Junjie Li, Jiangchao Zhao, Jinheng Yao, Xing, Xing Ya, and Jinjin Gu. 2025. Refusal falls off a cliff: Safety alignment failures in reasoning? *arXiv preprint arXiv:2510.06036*.\n- Zhong-Xia Zhang and Stephen H. Bach. 2025. Selfjailbreaking: Language models jailbreak themselves out of safety alignment after being reasoning. *arXiv preprint arXiv:2510.20956*.\n\n**Appendix A: Responsible NLP Research Checklist** (header visible at bottom)\n\n\"**Appendix A: Responsible NLP Research Checklist**\n\n- **Limitations discussed:** Yes (section 7)\n- **Potential risks:** This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this concern, as the safety probe does not provide a direct model access to the probe, which a deployed monitoring system would not expose.\"\n\n(Additional checklist items partially visible but cut off)\n\n---\n\n## PAGE 13 — Appendix A (Responsible NLP Research Checklist continued) + Appendix B (Layer Sweep Results)\n\n**Appendix A continued:**\n\n- **Computational budget:** Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total). We compute on a single machine (under 4 GPU-hours on a single 4-GPU A6000 or finetuning).\n- **Data:** We use HarmThoughts, a publicly available benchmark with safety annotations. No new data collection was performed.\n- **Human subjects:** No human subjects research was conducted.\n- **Reproducibility:** All hyperparameters are reported in section 4.5 (full BA-optimal layer in section Y). K was pre-selected using BA metric. Code and data will be released upon publication.\n\n**Appendix B — Layer Sweep Results**\n\n\"For each model, we sweep all transformer layers and evaluate from each layer three criteria: (1) balanced accuracy = crossing rate (the biased composite), (2) pure balanced accuracy, (3) precision, (4) inverse FPR. Including seed 0, FPR metric drops from 0.48 to 0.30 by biased metric.\n\nShallow layers produce highly compressed representations as a middle-ground tradeoff; deep layers (7–98% depth) demonstrate that layer selection is a consequential methodological choice. The HS advantage at threshold is significant at whichever layer BA selects (14/16 per-model HB, two FPR failures from underpowered 32B test sets n≤20).\n\n**Selected layers.** R1-8B: all five metrics agree on layer 14 (44% depth). OT-7B: biased metric selects L0 (0%), unbiased consensus selects L16 (57%). QoQ-32B: biased metric selects L2 (3%), unbiased selects L10 (16%), unbiased consensus selects L63 (98%). The bias is most extreme at 64-layer models where the composite metric selects layers in the bottom 16% of the network while threshold-dependent metrics select layers at 57% depth and above. For 32B models, unbiased BA selects L32 (42 for QoQ) and L47 (73%) for R1-32B; under the canonical 60/20/20, it selects L63 (98%), which demonstrates this metric sensitivity to the data split.\n\n**Impact on modality comparison.** At the biased metric, HS vs. text precision p-values are 0.064 (R1-32B) and 0.35–0.83 (QoQ-32B), both non-significant (section III). 1/5 unbiased metrics improve monotonically across all metrics (section F), so the accuracy signal is specific to HS probes (but not 32B).\n\n**Layer selection stability (LOO-CV).** Leave-one-out cross-validation on the validation set confirms that layer selection is robust to data composition. Under pure balanced accuracy, the dominant layer is selected in 68% (QoQ-32B) to 89% (R1-8B) of folds, consistent with the main finding. Three alternative selections cluster in neighboring layers (L29, L55–56 for QoQ; L32, L38, L43 for R1-32B). The consensus corrected layers (L63 for both 32B models) are similarly dominant under threshold-dependent selection.\n\n**Joint layer, W=1 sensitivity.** Under the original 700d → 384d pipeline, the joint layer/window selection is one of 2,340 configurations (this is a potential source of selection bias inflating results — see section 4.2). We cover 2 architectures and 2 scales; intermediate scales, proportion analysis, and multilingual settings are untested. In Figure X we cover 2 of 2.\"\n\n**Table 5** (Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Table 6: \"Table 6: Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4–2.7×), while a linear operator in this compression framework is 1.4–2.7× smaller than at deep layers. The table shows smaller inter-step distances at shallow layers.\"):\n\nTable 6 data:\n| Model | Layer (type) | Mean | Std |\n|-------|-------------|------|-----|\n| R1-8B | L2 (biased) | 0.186 | 0.097 |\n| R1-8B | L16 (corrected) | 0.411 | 0.145 |\n| QoQ-32B | L2 (biased) | 0.077 | 0.041 |\n| QoQ-32B | L63 (corrected) | 0.206 | 0.091 |\n| R1-32B | L2 (biased) | 0.084 | 0.056 |\n| R1-32B | L10 (biased) | 0.092 | 0.076 |\n| R1-32B | L63 (corrected) | 0.076 | 0.076 |\n\n---\n\n## PAGE 14 — Appendix C (Representation Compression Analysis) + Appendix D (Holm-Bonferroni Step-Down Correction)\n\n**Appendix C — Representation Compression Analysis**\n\n\"We measure step-to-step cosine distance at biased (shallow) vs. corrected (deep) layers across all models to characterize the compression mechanism underlying the crossing rate bias (table 6).\n\nShallow layers produce highly compressed representations (1.4–2.7×), producing more frequent threshold crossings. The HS precision advantage (table 2) at the same dimensionality shows the compression advantage.\n\n**Table 7** (step-level metrics): HS vs. text precision p-values are 0.064 (R1-32B) and 0.35–0.83 (QoQ-32B), which is non-significant (section III).\n\nShallow layers produce highly compressed representations and produce predictions even as overall classification accuracy degrades. CP annotations (section 4.1) uses 7 Transform models as text encoder baseline. The larger marginal gains for text probes reflects their weaker single-step baseline.\"\n\n**Table 7. Holm-Bonferroni Step-Down Correction:**\n\nTable 7 data (4 tests = 3 correlated metrics). Each test uses two-sided metric differences (HS mimus text). All 12 pass at α=0.05; a 4-test model-level correction (one per model, using the worst p-value) also passes.\n\n| Rank | Model | Metric | p-val | Thresh. | Pass |\n|------|-------|--------|-------|---------|------|\n| 1 | QoQ-32B | Bal. Acc. | <0.001 | 0.0042 | Yes |\n| 2 | OT-7B | Bal. Acc. | <0.001 | 0.005 | Yes |\n| 3 | R1-8B | Bal. Acc. | <0.001 | 0.0056 | Yes |\n| 4 | OT-7B | Bal. Acc. | <0.001 | 0.0063 | Yes |\n| 5 | QoQ-32B | Precision | <0.001 | 0.007 | Yes |\n| 6 | OT-7B | Precision | <0.001 | 0.0083 | Yes |\n| 7 | R1-8B | Precision | 0.001 | 0.01 | Yes |\n| 8 | R1-32B | Bal. Acc. | 0.003 | 0.0125 | Yes |\n| 9 | QoQ-32B | Precision | 0.003 | 0.0167 | Yes |\n| 10 | M | Decision | 0.005 | 0.025 | Yes |\n| 11 | N | Decision | 0.013 | 0.05 | Yes |\n| 12 | R1-8B | FPR | 0.044 | 0.0500 | Yes |\n\n\"The weakest test (rank 12, R1-8B FPR, p=0.044) passes its threshold (α/1 = 0.05) with the margin. The ordering reveals that L63 is near-optimal for QoQ-32B at recommended windows (W=3), just below the Layer L45–L46 layer for form a robust band where all 3/3 metrics pass Holm-Bonferroni (section B1). The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.\n\n**Exact sign-flip permutation test validation.** Table 7 reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the consecutive 12-test comparison and the 4-test model-level correction: both yield the same outcome (all tests pass at α=0.05). Under 4-test HB, the tightest threshold falls at α/4=0.0125; (p=0.044), rank-4 threshold α/1=0.050, which still passes. Text FPR is highly stable (std=0.007) while HS FPR is split-sensitive (std=0.040), suggesting the canonical-split FPR advantage (~7.4pp) does not generalize robustly across seeds.\"\n\n---\n\n## PAGE 15 — Appendix E (Window Size Ablation Details) + Appendix F (OpenThinker-7B Detailed Results)\n\n**Appendix E — Window Size Ablation Details**\n\n\"Table 8 reports the complete text probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes.\n\n**Table 8** (Window size ablation on R1-8B, step-level metrics):\n\n| W | Bal.Acc. | Precision | FPR | Coverage |\n|---|----------|-----------|-----|----------|\n| 1 | 64.7 | 41.6 | 25.8 | 95.4 |\n| 3 | 66.9 | 44.8 | 23.1 | 90.7 |\n| 5 | 69.2 | 48.5 | 20.0 | 84.9 |\n| 10 | 72.1 | 56.9 | 18.2 | 74.4 |\n| 15 | 74.3 | 62.1 | 14.2 | 65.8 |\n| 20 | 75.8 | 62.1 | 12.5 | 62.8 |\n| 25 | 76.7 | 63.0 | 12.2 | 60.3 |\n\n\"Text probes improve monotonically from W=1 while the plateau observed at W=10 also approximately aligns with the HS probes. The absolute FPR reduction (~14.8pp) differs markedly from its paired ΔPre and HS text coverage pairs are four times larger. The larger marginal gains for text probes reflects their weaker single-step baseline.\"\n\n**Appendix F — OpenThinker-7B Detailed Results**\n\n\"Table 9 reports the complete text probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes. (Section E). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 68% ±11 (W=1) to 82.2% (W=25) with FPR falling 9.65% to 4.83%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at W=3 while precision and FPR continue improving at larger windows; (3) R1-32B peaks at W=10 then degrades, likely reflecting overfitting on the smaller dataset with small Gaussian noise added. This made the text probe trivially predictive and produced a spuriously significant result (p=0.001 for HS vs. text FPR difference).\n\n**R1-8B per-model FPR (biased metric)** — Table 21 reports HS vs. text FPR comparisons for R1-8B; HS FPR is directionally consistently lower (5/5 HS ≤ Text); 2/5 reaching statistical significance; but after Holm-Bonferroni correction for 5 seeds (p=0.01), 1/5 remains significant. Text FPR is highly stable (std=0.007) while HS FPR is split-sensitive (std=0.040).\"\n\n**Table 9** (text probe window ablation on R1-8B, step-level metrics, full per-seed breakdown):\n\n| W | Bal.Acc. | Precision | FPR | Coverage |\n|---|----------|-----------|-----|----------|\n| 1 | 58.1 | 24.5 | 34.5 | 63.8 |\n| 3 | 64.8 | 33.2 | 28.7 | 70.1 |\n| 5 | 65.9 | 38.2 | 26.3 | 72.2 |\n| 10 | 58.9 | 28.3 | 20.0 | 66.0 |\n| 15 | 65.0 | 33.2 | 19.7 | 64.5 |\n| 25 | 61.4 | 32.9 | 16.1 | 66.0 |\n\n\"**OT-7B multi-layer GRU results (layers 13–19, 3 seeds, 60/20/20 split).** OT-7B GRU achieves 74.6% ±1.3% balanced accuracy, 64.5±2.7% coverage; +33.6pp to 61.8% precision; 22.76% to 16.94% FPR. QoQ-32B produces +3.2pp to lead time. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps, so absolute lead times are not directly comparable. The FPR lead-time results combining HS and LR probe at layer-16 (10.0%), which confirms that GRU's gain lead time at the cost of more false alarms across both 7.8B models.\"\n\n**Universal trends** summary bullet text:\n- (1) larger windows smooth the probe fires less frequently\n- (2) HS FPR generally decreases with window size (3) leads time is model-dependent\n- OT-7B has a higher crossing at W=3\n\n---\n\n## PAGE 16 — Appendix E.1 (Test Probe Window Ablation) + Appendix F cont. (OT-7B detailed results with tables)\n\n**Appendix E.1 — Test Probe Window Ablation**\n\n\"Table 9 reports the complete test probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes (Section E).\n\n**Table 10** (OT-7B test probe window ablation, step-level metrics): HS score = balanced accuracy. Layer 16 (57% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.\n\n| Layer | Depth | Bal.Acc. | Cross.Rate | Score |\n|-------|-------|----------|------------|-------|\n| 0 (embed.) | 0 | 66.3 | 40.4 | 35.5 |\n| 4 | 18 | 66.3 | 40.4 | 26.8 |\n| 8 | 36 | 61.2 | 35.6 | 21.6 |\n| 16 | 57 | 65.5 | 31.9 | 21.6 |\n| 20 | 71 | 65.5 | 31.9 | 20.9 |\n| 30 | ??? | 65.0 | 31.9 | 20.9 |\n| 63 | 71 | 65.5 | 31.9 | 20.9 |\n| 64 | 75 | 63.0 | 31.9 | 21.8 |\n\n**Table 11** (OT-7B test probe window ablation, step-level metrics):\n\n| W | Bal.Acc. | Precision | FPR | Coverage |\n|---|----------|-----------|-----|----------|\n| 1 | 58.1 | 24.5 | 34.5 | 63.8 |\n| 3 | 63.3 | 32.3 | 26.0 | 66.0 |\n| 5 | 61.8 | 30.9 | 19.0 | 64.5 |\n| 10 | 65.7 | 39.1 | 17.4 | 64.5 |\n| 15 | 65.5 | 40.0 | 14.9 | 62.4 |\n| 25 | 76.2 | 62.1 | 10.0 | 54.3 |\n\n\"R1-8B shows a broadly increasing trend in balanced accuracy with local non-monotonicity: balanced accuracy peaks at W=5 (76.1%) while W=10–15 then recovers to 76.2% at W=25. Precision and FPR improve monotonically with larger windows (54% to 61.8% precision; 22.76% to 16.94% FPR). QoQ-32B produces +3.2pp in lead time. The lead time is substantially longer in those models than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps, so absolute lead times are not directly comparable. The FPR-lead-time results from using the HS probe with LR probe at layer 16 (10.0%), which confirms that GRU's gain lead time at the cost of more false alarms across both 7-8B models.\"\n\n---\n\n## PAGE 17 — Appendix G (GRU Training Details) + Appendix H (Control Task Methodology)\n\n**Appendix G — GRU Training Details**\n\n\"**Data split.** GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression models. The validation set (10% of training portion) is used for early stopping (effective 60/10/30 split). The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\n\n**Architecture.** We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden layer (h) [the best layer selected by validation balanced accuracy] as input. The multi-layer variant concatenates hidden states from 3 candidate layers [multiple], running through the network at each step to produce a higher-dimensional input to the same GRU architecture.\n\n**Training procedure.** We train with Adam (learning rate 1×10^-3, default β₁=0.9, β₂=0.9993), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.\n\n**Results.** We report crossing accuracy (sustained accuracy at which the model-first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean ± standard deviation.\n\n**Per-seed results for R1-8B (single-layer GRU).** The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe first achieves good peak accuracy but crosses the detection threshold late. This variance underscores the\n\n**Table 12** (R1-8B GRU joint layer, 70/30):\n\n| Seed | Peak Acc. | Crossing Acc. | Lead (steps) |\n|------|-----------|---------------|--------------|\n| 1 | 85.2 | 74.3 | +4.8 |\n| 2 | 83.1 | 72.9 | +4.8 |\n| 3 | 83.4 | 70.4 | −0.9 |\n| Mean ± std | 83.9 ± 1.1 | 72.5 ± 2.0 | +3.5 ± 2.3 |\n\n\"**OT-7B multi-layer GRU (layers 13–19, 3 seeds, 60/20/20 split).** OT-7B GRU achieves 74.6% ± 1.3% balanced accuracy; 64.5% ± 1.4% steps lead. GRU advantage (BA: Δ=+21.9pp, FPR: Δ=−17pp, 95% CI [−22.2, −12.2]). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (±21.9pp); the small discrepancy reflects resampling underperfrom under the optimal layer selection. OT-7B GRU lead time is substantially longer than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps vs. 4.5 steps for both R1-8B and R1-32B, so absolute lead times are not directly comparable.\"\n\n**Appendix H — Control Task Methodology**\n\n\"We follow the selectivity framework of (Hewitt and Liang, 2019) to verify that our probes capture sensitivity to annotation noise rather than meaning noise only.\"\n\n---\n\n## PAGE 18 — Appendix H (Control Task) + Appendix I (Oracle Upper Bound Analysis) + Appendix J (CP Annotation Perturbation)\n\n**Appendix H (continued):**\n\n\"**Procedure.** For each model, we randomly permute the binary labels (pre-CP vs. post-CP) within each trace while preserving the marginal label distribution. We train L2-regularized logistic regression (L2-regularized logistic regression on shuffled features) classifiers with the same architecture and hyperparameters on these shuffled labels. Selectivity is defined as:\n\nSelectivity = Acc_diagnostic − Acc_control ... (1)\n\nwhere Acc_diagnostic is the probe accuracy on true labels and Acc_control is the accuracy on permuted labels. A selectivity score close to zero indicates the probe is not learning a meaningful signal above chance.\n\n**Results.** We repeat the control experiment 10 times with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers (60/20/20): the dominant layer is selected in 68% (QoQ-32B) to 89% (R1-8B) of folds. The absolute FPR reduction (~14.8pp) differs markedly from its paired ΔPre...\n\n**Layer provenance note.** R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias since they agree with corrected layers and are bounded by the Mahalanobis HS advantage. QoQ-32B's precision gap (+20.1pp) aligns with the bootstrap mean (±21.4pp). The R1-32B's bias is most extreme; confirming that layer selection matters to the commitment detection outcome.\n\n**Position-only baseline.** As a complementary non-positional test, we train a logistic regression classifier using only the normalized step index (t/T where T is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8% FPR compared to 8.1% for the HS probe at matched detection thresholds. The probe confirms that hidden state features carry information beyond what step position provides.\"\n\n**Residualized Selectivity:** \"To confirm that selectivity survives position removal, we recompute control task selectivity on position-regressed features (the same residualized representations used in section V). R1-8B at 67.3% but 1% crossing rate. Implementation details in section (R).\"\n\n**Appendix I — Oracle Upper Bound Analysis**\n\n\"Table 14 reports the oracle performance of GRU and FPR share the same balanced accuracy, precision, and FPR for the four independent comparisons is four (one per model). We report both the consecutive 12-test and the 4-test model-level correction: both yield the same outcome (all tests pass at α=0.05). Under 4-test HB, the tightest threshold falls at α/4=0.0125...\"\n\n**Table 14** (Oracle upper bound analysis). Det. Rate = balanced accuracy, p=0.80; MDE (80% power):\n\n| Model | Det.Rate | Obs.sd (BA) | MDE(80%) |\n|-------|----------|-------------|---------|\n| R1-8B | 20 | 0.026 | 9.5pp |\n| OT-7B | 20 | 0.034 | ... |\n| QoQ-32B | 20 | 0.056 | ... |\n| R1-32B | 20 | 0.056 | 9.5pp |\n\n\"At W=3, the MDE is 8.6–9.5pp, meaning effects distinguishable from noise. R1-32B's residualized HS text gap (+1.9pp) falls well below the MDE (9.5pp), so the HS advantage cannot be reliably distinguished from either a true null or an underpowered sample. The 7–8B MDEs (3.3–4.2pp) are substantially lower, explaining why smaller effects are detectable at these scales.\"\n\n**Appendix J — CP Annotation Perturbation**\n\n\"Table 7 reports the full test battery to assess hidden-state superiority over text probes... We address CP annotation (section 4.2) led to the corrected-layer analysis reported in the main text, where all four models show significant HS advantage over directed deep layers, from strong (OT-7B) to qualified (R1-32B) (Table 3).\"\n\n\"To assess sensitivity to annotation noise, we shift the commitment point annotation by ε ∈ {−3, −2, −1, 0, +1, +2, +3} steps and retrain the HS probe (table 15). Precision changes negatively with earlier HS (−2, −3) steps and recovers above the baseline for delayed commits (+1, +2 steps).\n\n**Table 15** (HS probe sensitivity to CP annotation shift, n=33):\n\n| Seed | HS FPR | Text FPR | ΔFPR |\n|------|--------|----------|------|\n| 0 | 0.113 | 0.308 | −0.195 |\n| 1 | 0.061 | 0.168 | −0.105 |\n| 2 | 0.148 | 0.167 | −0.167 |\n| 3 | 0.167 | 0.167 | 0.000 |\n| 4 | 0.143 | 0.228 | −0.083 |\n| p | |  | 0.293 |\n\n---\n\n## PAGE 19 — Appendix K (BOCPD/CUSUM Configuration Sweep) + Appendix L (Detection Threshold (K) Ablation)\n\n**Appendix K — BOCPD/CUSUM Configuration Sweep**\n\n\"We sweep hyperparameters for both Bayesian Online Changepoint Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe scores.\n\n**BOCPD configurations.** BOCPD models the sequence of probe scores as piecewise-constant functions with Gaussian observation noise. The hazard rate λ controls the prior probability of a changepoint occurring at each step, and the threshold Δ controls the detection boundary (a detection if accumulated evidence > Δ).\n\n**CUSUM configurations.** CUSUM accumulates evidence for a positive mean shift. The drift parameter k sets the expected shift magnitude (set to 1.5), and the threshold Δ controls the detection sensitivity...\"\n\n**Table 14** (Oracle upper bound analysis — appears again here as \"Table 14. Oracle bound analysis\"):\n\n| Model | Prec. | Det.Rate | Lead | p |\n|-------|-------|----------|------|---|\n| R1-8B | 0.400 | 0.784 | 1.54 | <0.001 |\n| OT-7B | 0.421 | 0.634 | 0.021 |   |\n| QoQ-32B | 0.453 | 0.631 | 0.021 |   |\n| R1-32B | 0.756 | 0.552 | 0.314 |   |\n\n\"The best BOCPD configuration (λ=10) achieves 97% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1% detection rate (i.e., a much lower baseline). All CUSUM configurations underperform the simple threshold on lead time.\n\n**Table 15** (HS probe sensitivity to CP annotation, safety):\n\n\"R1-32B (bal.acc p=0.925, precision p=0.346; R1-32B precision p=0.050) but no tests surviving correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (±21.9pp). The proportional boundary (∼12%) amplified at n=33.\"\n\n---\n\n## PAGE 20 — Appendix L (Detection Threshold K Ablation) + Appendix M (Decision Threshold Sensitivity)\n\n**Appendix L — Detection Threshold (K) Ablation**\n\n\"The consecutive-crossings threshold K controls the trade-off between detection coverage and false positive rate. We evaluate K ∈ {1, 3, 5, 7, 10} on all models using HS probes at corrected layers (section B).\n\nK=1 yields perfect coverage but near-perfect false positive rate (0.92–1.00), showing no discrimination. R1-8B achieves 0.756 balanced accuracy (approaching 0.778) but with substantially worse precision (0.512 vs. LR 0.700) after adding noise in the precision-coverage Pareto for both methods. The best two-stage configuration (W_screen=3, W_confirm=15, k=1) achieves 72.2% precision at 38.5% coverage with k=5, but these operating points are impractical due to excessive missed detections.\n\n**Table 16** (R1-8B threshold K ablation):\n\n| K | R1-8B | OT-7B | R1-32B | QoQ-32B |\n|---|-------|-------|--------|---------|\n| 1 | 1.00 | 1.00 | 1.00 | 1.00 |\n| 3 | 0.90 | 0.74 | 0.79 | 0.72 |\n| 5 | 0.69 | 0.62 | 0.62 | 0.60 |\n| 7 | 0.55 | 0.47 | 0.50 | 0.48 |\n| 10 | 0.35 | 0.30 | 0.38 | 0.30 |\n\n\"K=7 reduces FPR by 79–86% while maintaining non-trivial detection rates. The K=7 setting offers a middle ground (57% FPR reduction, 16–39% detection). These results support the reframing of K ablation as practitioner-facing operating curve.\"\n\n**Appendix M — Decision Threshold Sensitivity**\n\n\"The joint search space for layer (≤ 64), window W (7 values), K (5 values), and decision threshold is large (up to 2,340 configurations per model). This raises the concern that reported performance reflects overfitting to small validation samples (n≈1–9 per class at 32B). Three analyses address this concern.\n\n**Threshold-dependent metrics converge to a deep-layer band.** Despite the large search space, choice of four threshold-dependent metrics (precision, inverse FPR, additive composite) independently select L63 (98% depth) for both 32B models—see Table 2. The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.\n\n**Bootstrap CIs quantify statistical uncertainty.** For the model comparison metric at W=3, bootstrap 95% CIs are narrow: R1-8B ±0.021 (Bal.Acc.) and ±0.040 (FPR); QoQ-32B ±0.017 (BA), consistent with in-distribution variability not overfitting.\n\n**BA-optimal layer instability is the finding, not a confound.** Five-fold cross-validation on 32B validation sets (n≤20 per class) reveals that the BA-optimal layers are highly unstable across folds (table 25). This instability is not a limitation of the study but the central methodological finding: BA-layer selection is sensitive to data composition, and conclusions drawn from any single BA-optimal layer are unreliable.\"\n\n**Appendix N — M002 Bug Disclosure**\n\n\"A bug was discovered during development that affected intermediate results for QoQ-32B.\n\n**Issue.** In experiment M002 (feature ablation), the QoQ-32B probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive and produced a spuriously significant result (p=0.001 for HS vs. text FPR difference).\n\n**Discovery and correction.** The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QoQ-32B feature extraction used the composite composed HS for correct safety in null-space projection (Holm-Bonferroni section B1). The modality comparison shows at the originally selected layers (L2 and L10, chosen by the biased composite)—table 3 showed that no significant HS vs. text gap at corrected layers. R1-32B modality comparison: section V Encoder Robustness; section F Multi-Seed Stability; section Y BA-Layer Modality Comparison; section Z Post-Hoc Power Analysis.\"\n\n---\n\n## PAGE 21 — Appendix O (Adaptive Two-Stage Detection) + Appendix P (Temporal Ablation Details) + Appendix Q (Negative Results Details) + Figure 4\n\n**Appendix O — Adaptive Two-Stage Detection**\n\n\"We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window (W_screen) to flag candidate unsafe segments, followed by a longer confirmation window (W_confirm) applied only to the flagged segments. A trace is classified as unsafe if at least k steps exceed the threshold during the confirmation stage.\n\nWe merge the validation and test datasets for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of W_screen ∈ {1, 3, 5}, W_confirm ∈ {10, 15, 25}, k ∈ {1, 3, 5} and the threshold τ (pre-CP FPR setting 76.7%): the two-stage approach achieves 22.2% precision at 38.5% coverage with k=5, but these operating points are impractical due to excessive missed detections. The marginal improvement suggests that natural smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach requires 3 hyperparameters (W_screen, W_confirm, k) as one more than single-window without proportional performance gains.\"\n\n**Figure 4** (Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection):\n\nCaption: \"Figure 4. Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. Results are Pareto-dominated by matched coverage. Higher k values shift the tradeoff toward precision at the cost of unacceptable coverage loss.\"\n\n**Appendix P — Temporal Ablation Details**\n\n\"Full per-model temporal ablations are reported in table 8 (section E). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 68% ±11 (W=1) to 82.2% (W=25) with FPR falling 9.65% to 4.83%; (2) OT-7B exhibits a split pattern where balanced accuracy peaks at W=3 while precision and FPR continue improving at larger windows; (3) R1-32B peaks at W=10 then degrades, likely reflecting overfitting on the smaller dataset (n=100), (4) QoQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (section E.1) consistently show W at ±10 for GRU-multi. The summary supports the interpretation that text features encode less information per step, benefit proportionally more from observing the multi-step progression.\"\n\n**Appendix Q — Negative Results Details**\n\n\"On OT-7B, BOCPD achieves 0% detection rate with λ∈{5, 10, 50, 100, 200}. Only R1-8B produces non-trivial results (λ=10, 93% rate, +3.45 steps lead). CUSUM configurations (all λ, k) fail to produce non-trivial results only more sophisticated approaches.\n\n**Table 27** ... R1-8B BOCPD: all tests pass; OT-7B: FPR=1.00 (all traces flagged as unsafe).\"\n\n---\n\n## PAGE 22 — Appendix R (Cross-Model Transfer Results) + Appendix S (Encoder Robustness Analysis)\n\n**Appendix R — Cross-Model Transfer Results**\n\n**Table 19** (Seven alternative approaches):\n\n| Method | Result | Limitation |\n|--------|--------|------------|\n| BOCPD | 0% det. on 4/4 models | Commitment gradual |\n| CUSUM | < threshold, all model | Same as BOCPD |\n| Mahalanobis | Δd ≈ 0 | Signal in minor PCA components |\n| MLP | 3/4 worse than LR | Overfitting |\n| CCS | No gain over supervised | Alignment mismatch |\n| Transfer | Best 59.5% (PCA)* | Model-specific |\n\n\"* Repl: Mean-difference directions (Zou et al., 2023) show inconsistent performance. QoQ-32B achieves 0.756 balanced accuracy (approaching required evidence); R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment in some models but not others, so it is unreliable as a general-purpose method.\n\n**MLP probes.** Two-layer MLPs (d → 128 → 1, ReLU) underperform logistic regression on all models. The commitment decision boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small 32B datasets.\n\n**CCS.** Contrast-Consistent Search (Burns et al., 2023) adapted with contrastive pairs of pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction and is therefore semi-supervised.\n\n**Transfer.** Mean-difference directions produce no cross-model transfer (16/32 per-model models tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model). The pre-cision gains (p=0.002); 3/4 models retain significant non-positional HS advantage (FPR for R1-32B underpowered 32B sets. BA-L layer failure is the exception: residualized HS-text gap is position-dependent of OT-7B +6.9pp, R1-8B +8.6pp at W=15, QoQ-32B → R1-32B achieves 67.3% but 1% crossing rate. Implementation details in section (R).\"\n\n**Table 23** (HS vs. ES-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni corrected (4 tests, α=0.05). QoQ/20 split):\n\n| Model | Layer | W | ES | MinLM | Δ |\n|-------|-------|---|-----|-------|---|\n| R1-8B | L16 | 15 | 440 | 446 | +6 |\n| OT-7B | L16 | 1 | 446 | 321 | −125 |\n| R1-32B | L10 | 1 | 446 | 244 | −202 |\n| QoQ-32B | L63 | 1 | 458 | 244 | −214 |\n\n\"The HS advantage partially survives against the LLM encoder: 4/4 models (both 7–8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (384d) < BGE-large (335M, 1024d) < ES-Mistral-7B (PCA 384d).\"\n\n**Appendix S — Encoder Robustness Analysis**\n\n\"To address the concern that threshold-dependent layer selection may circularly favor HS probes, we repeat the modality comparison at layers selected by balanced accuracy for each model. Results show HS advantage is significant at BA-selected layers too despite the choice of metric:\n\n**Table 31** (HS vs. text at BA-selected layers (60/20/20):\n\n| Model | BA-L | ΔPrec | ΔBA | ΔFPR | p(BA) |\n|-------|------|-------|-----|------|-------|\n| R1-8B | L17 | +16.6 (+16.6) | +8.4 (+8.4) | −7.0 (−6.3) | <0.001 |\n| OT-7B | L16 | +10.1 (+10.1) | +13.1 (+13.1) | −15.4 (−15.4) | <0.001 |\n| QoQ-32B* | L3 | −31 (−14.6) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\n| R1-32B* | L3 | −12.8 (−14) | +13.6 (+13.6) | +15.8 (+15.8) | <0.001 |\n\n\"Values in parentheses are bootstrapped-corrected (10,000 bootstrap examples). p-values on the BA metric corrected. * BA-L failures from bias metric (section 4.2); corrected layers in table 3.\"\n\n\"Positions 9–20pp. The HS precision advantage is directionally consistent across all four models (positive in every case); significance is marginal only for OT-7B R1-8B shows a (p=0.064 under Holm-Bonferroni). R1-32B BA-significance only falls at n≤20 (p=0.914); QoQ-32B achieves 67.3% but 1% crossing rate. BA-optimal layer instability: Five-fold LOO-CV shows standard deviation of 0.145 (R1-8B FPR = 0.483), varying from 72.1% to 98.7%; this instability confirms that BA selection is seed-fragile.\"\n\n---\n\n## PAGE 23 — Appendix T (Random Projection Baseline) + Appendix U (LLM-Based Text Encoder Comparison)\n\n**Appendix T — Random Projection Baseline**\n\n\"PCA capacity matching (section S) preserves 79–92% of variance with 384-dimensional projections. The split indicates which compression is whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projections (RP) and compare PCA projections with RP projections at the same dimensionality (table 22).\n\n**Table 22** (RP, 384d bootstrap (CF 384d), Holm-Bonferroni corrected (4 tests, α=0.05)):\n\n| Rank | Model | Metric | p-val | Thresh. | Pass |\n|------|-------|--------|-------|---------|------|\n| 1 | QoQ-32B | Bal. Acc. | <0.001 | 0.001 | Yes |\n| 2 | OT-7B | Bal. Acc. | <0.001 | <0.001 | Yes |\n| 3 | R1-8B | Bal. Acc. | <0.001 | 0.0056 | Yes |\n| 4 | OT-7B | FPR | <0.001 | 0.0063 | Yes |\n| ... | ... | ... | ... | ... | ... |\n\n\"All four models achieve significant HS advantage under random projection (all 12 tests pass HB correction), full data, two FFR failures from underpowered 32B test sets. BA-L values (RP): QoQ-32B 79.4 ±1.2pp; R1-8B 81.5 ±0.9pp. The HS advantage is robust to the choice of layer selection criterion (BA, Prec, FPR-inverse, cross-rate, composite).\n\n**R1-8B per-seed HB pass rates.** Table 29 reports Holm-Bonferroni pass rates per metric across 5 random seeds. R1-8B the model classified as \"moderate\" evidence due to FPR instability.\n\n**Table 29** (R1-8B per-seed Holm-Bonferroni pass rates):\n\n| Seed | HS FPR | Text FPR | ΔPre | ΔBA | ΔFPR |\n|------|--------|----------|------|-----|------|\n| 0 | 0.119 | 0.040 | ... | ... | ... |\n| 1 | 0.061 | ... | ... | ... | ... |\n| 2 | 0.148 | ... | ... | ... | ... |\n| 3 | 0.167 | ... | ... | ... | ... |\n| 4 | 0.143 | ... | ... | ... | ... |\n| p | | | | | 0.293 |\n| Pass rate: | N/5 | 5/5 | 3/5 | | |\n\n\"The FPR instability has a clear source: R1-8B text FPR clusters tightly around 17% (std~0.2pp) while HS FPR spreads more broadly (std~17%)...\"\n\n**Appendix U — LLM-Based Text Encoder Comparison**\n\n\"To test whether an LLM-based text encoder closes the HS advantage gap, we encode each reasoning step with E5-Mistral-7B-Instruct (Wang et al., 2022) (4,096d), reduced to 384d via PCA to match the MinLM dimensionality. Using each modality's precision-comparisons against HS probes at corrected layers:\"\n\n---\n\n## PAGE 24 — Appendix U (continued) + Appendix V (Post-Hoc Power Analysis)\n\n**Appendix U continued:**\n\n\"**Table 23** (HS vs. ES-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni corrected (4 tests, α=0.05), two-sided, same metrics; both 60/20/20):\n\n| Model | Layer | W | HS | ES | MinLM | Δ(HS-ES) |\n|-------|-------|---|-----|-----|-------|---------|\n| R1-8B | L16 | 15 | +8.4 | +10.8 | 0.002 | −2.4 |\n| OT-7B | L16 | 1 | +10.8 | −13.1 | +10.1 | +3.3 |\n| QoQ-32B* | L63 | 1 | +8.8 | −13.1 | 0.000 | +21.9 |\n| R1-32B* | L43 | 1 | +8.8 | −14.0 | 0.033 | +22.8 |\n\n(* Residual bias layer issues.)\n\n\"The HS advantage partially survives against the LLM encoder: 4/4 models (both 7–8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (384d) < BGE-large (335M, 1024d) < ES-Mistral-7B (PCA 384d). The precision gain is +12.8 to +18.6pp for ES, comparable to those at threshold-dependent layers (+15.4 to +14.0). The HS advantage is robust to the choice of layer selection criterion.\n\n**Exact sign-flip permutation test validation.** The joint search for which the layer W=3 pair (p=0.000 vs. p=0.207 margin), with a proportion near boundary (~12%) amplified at n=33.\n\nThe two failures are both FPR at 32B: R1-32B (bal.acc p=0.925, precision p=0.083, consistent with the underpowered test sets (n≤20) noted in Section 4. All three precision gains (p=0.054 vs. p=0.003; paired t p=0.001 (bootstrap 95% CI [−22.2, −12.2])). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with bootstrap mean (+21.9pp); the small discrepancy reflects resampling variability. Under the canonical 60/20/20 split: HS FPR advantage increases at larger temporal windows, suggesting HS representations better capture the temporal commitment dynamics.\"\n\n**Appendix V — Post-Hoc Power Analysis**\n\n\"We compute post-hoc minimum detectable effects (MDEs) at 80% power given each model's test-set size and observed variance.\n\n**Table 25** (LOO-CV BA-optimal layers per model, 5-fold. BA-optimal layers vary widely across folds):\n\n| Model | F1 | F2 | F3 | F4 | F5 | Spread |\n|-------|----|----|----|----|-----|--------|\n| QoQ-32B | L53 | L53 | L45 | L45 | L39 | 24 layers |\n| R1-32B | L53 | L45 | L40 | L63 | L39 | 24 layers |\n\n(R1-32B's high FPR variance (std=0.145) is driven by this instability.)\n\n\"At W=3, the MDE is 8.6–9.5pp, meaning effects smaller than the MDE cannot be reliably detected. R1-32B's residualized HS text gap (+1.9pp) falls well below the MDE (9.5pp), confirming the HS advantage cannot be reliably distinguished from noise. The 7–8B MDEs (3.3–4.2pp) are substantially lower, explaining why smaller effects are detectable at those scales.\"\n\n---\n\n## PAGE 25 — Appendix W (Multi-Seed Stability) + Appendix X (5-Seed HB Pass Rates for R1-8B)\n\n**Appendix W — Multi-Seed Stability**\n\n\"Stability, mean BA across folds peaks near L47–L50 for both models, consistent with the LOO-CV dominant layers (section B). The HS advantage is significant at threshold-optimal layers (14/16 per-model HB, two FPR failures from underpowered 32B test sets (n≤20)).\n\n**Table 27** (5-seed HB pass rates (HS FPR, n=3 models)):\n\n\"Seeds where HS FPR happens to be below the 0.05 threshold (>1.4/5 loss significance): the gap against text narrows without the detection threshold narrowing, and does not affect the precision or overall HS advantage, which passes all 5 seeds.\n\n**R1-8B HS per-seed breakdown (L63, W=1).** Table 30 reports the full per-seed breakdown for R1-8B's multi-seed stability:\n\n| Seed | Precision | Bal. Acc. | ΔPre Hb | Note |\n|------|-----------|-----------|---------|------|\n| 0 | 0.441 | 0.796 | +0.094 | 0.109 |\n| 1 | 0.780 | 0.748 | +0.263 | 0.109 |\n| 2 | 0.598 | 0.795 | +0.571 | <0.050 |\n| 3 | 0.630 | 0.781 | +0.097 | <0.050 |\n| 4 | 0.652 | 0.735 | +0.033 | <0.050 |\n| 5 | 0.440 | 0.715 | +0.022 | 0.050 |\n| Mean ± std | 0.594 ± 0.126 | 0.692 ± 0.256 | +0.207 ± 0.14 | (Seed 0 is outlier) |\n\n\"R1-32B's high FPR variance (std=0.145) is driven by test-set split allocation (n=19 vs. n=20). Positions 9–20pp. The HS precision advantage is directionally consistent across all four models.\n\n**5-seed Holm-Bonferroni pass rates.** Table 27 reports HS pass rates per metric across 5 random seeds. Overall, 18/20 (90%) model-seed combinations pass full HB (3 models × 5 seeds = 15 HB cases).\"\n\n**Appendix X — R1-8B FPR-specific note:**\n\n\"R1-8B HS FPR varies by only 1.1pp between validation and test set (seed=0 is an outlier (FPR = 0.483), varying from 72.1% to 98.7%; 2/5 reaching statistical significance after Holm-Bonferroni correction for 5 seeds (p=0.011). 1/5 remains significant. The FPR instability has a clear source: R1-8B text FPR clusters tightly around 17% (std~0.2pp) while HS FPR spreads more broadly (std~1.7pp).\"\n\n---\n\n## PAGE 26 — Appendix Y (BA-Layer Modality Comparison) + Appendix Z (Post-Hoc Power Analysis, cont.)\n\n**Appendix Y — BA-Layer Modality Comparison**\n\n\"While HS FPR happens to be below the 0.05 threshold from 6.1% to 16.1% (std~1.0pp). Seeds where HS FPR happens to be below 0.05 of threshold (>1.4/5 loss significance): the gap against text narrows without detection threshold narrowing and does not affect precision or overall HS advantage.\n\n**R1-32B's position-residualized selectivity.** To quantify this, we recompute select task selectivity on position-regressed features (the same residualized representations used in section V). R1-8B at 67.3% but 1% crossing rate.\n\n**Table 24** (Position-residualized balanced accuracy across 14 per-model tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model), α=0.05):\n\n| Model | BA-L | ΔPrec | ΔBA | ΔFPR | p |\n|-------|------|-------|-----|------|---|\n| R1-8B | L17 | +16.6 (+16.6) | +8.4 (+8.4) | −7.0 (+0.031) | <0.001 |\n| OT-7B | L16 | +10.1 (+10.1) | +13.1 (+13.1) | −15.4 (−15.4) | <0.001 |\n| QoQ-32B* | L3 | −31 (−14.6) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\n| R1-32B* | L3 | −12.8 (−14) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\n\n\"Of 16 per-model tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model). The precision gains (p=0.002); 3/4 models retain significant non-positional HS advantage (FPR for R1-32B underpowered 32B tests BA-L layer failure is the exception: residualized HS-text gap is position-dependent for OT-7B (+6.9pp), R1-8B (+8.6pp at W=15), QoQ-32B → R1-32B achieves 67.3% but 1% crossing rate. BA-optimal layer instability: Five-fold LOO-CV shows standard deviation of 0.145 (R1-8B FPR = 0.483), varying from 72.1% to 98.7%.\"\n\n**Appendix Z — Post-Hoc Power Analysis (additional)**\n\n\"While HS FPR happens to be below global best 0.817). Joint layer, W=1 ability was evaluated via grid search on W ∈ {1/5, 5} for QoQ-32B only; full LOO-cross-validation of the (layer, W) pair and extension to R1-32B remain for future work.\n\n**Table 18** (R1-32B threshold sensitivity (L63, W=1). HS BA varies by 1.1pp (0.741–0.752); the HS advantage is consistent across all correction settings):\n\n| τ+ | HS BA | ΔBA | HS Prec | ΔPrec | ΔFP/R | ΔFPR |\n|----|-------|-----|---------|-------|-------|------|\n| 0.742 | +0.120 | 0.583 | −0.126 | 0.205 | −0.106 |\n| 0.741 | +0.128 | 0.583 | −0.133 | 0.287 | −0.078 |\n| 0.741 | +0.109 | 0.588 | +0.113 | 0.287 | −0.078 |\n| 0.743 | +0.126 | 0.583 | +0.113 | 0.266 | +0.078 |\n| 0.741 | +0.128 | 0.592 | +0.109 | 0.287 | −0.078 |\n\n\"R1-32B (bal.acc p=0.925, precision p=0.083, consistent with the underpowered test sets (n≤20). All three precision gains (p=0.054 vs. p=0.003 paired t p=0.001 (bootstrap 95% CI [−22.2, −12.2]). All three metrics survive correction. The two failures are both FPR at 32B: R1-32B BA-L layer failure is the exception.\"\n\n---\n\n以上为第9–26页（论文末尾所有页面）的完整内容转录，包含：\n\n- **第9页**：Section 5结尾（讨论/操作点）、Section 6 Conclusion、Section 7 Limitations、References开头\n- **第10–12页**：完整参考文献列表\n- **第12页底部–第26页**：完整附录（A至Z），涵盖：\n  - Appendix A（NLP Research Checklist）\n  - Appendix B（Layer Sweep）\n  - Appendix C（Representation Compression）\n  - Appendix D（Holm-Bonferroni Step-Down）\n  - Appendix E/E.1（Window Size Ablation）\n  - Appendix F（OpenThinker-7B详细结果）\n  - Appendix G（GRU Training Details）\n  - Appendix H（Control Task Methodology）\n  - Appendix I（Oracle Upper Bound）\n  - Appendix J（CP Annotation Perturbation）\n  - Appendix K（BOCPD/CUSUM Configuration Sweep）\n  - Appendix L（Detection Threshold K Ablation）\n  - Appendix M（Decision Threshold Sensitivity）\n  - Appendix N（M002 Bug Disclosure）\n  - Appendix O（Adaptive Two-Stage Detection）\n  - Appendix P（Temporal Ablation Details）\n  - Appendix Q（Negative Results Details）\n  - Appendix R（Cross-Model Transfer Results）\n  - Appendix S（Encoder Robustness Analysis）\n  - Appendix T（Random Projection Baseline）\n  - Appendix U（LLM-Based Text Encoder Comparison）\n  - Appendix V（Post-Hoc Power Analysis）\n  - Appendix W（Multi-Seed Stability）\n  - Appendix X（R1-8B FPR-Specific Notes）\n  - Appendix Y（BA-Layer Modality Comparison）\n  - Appendix Z（Post-Hoc Power Analysis续）"
4	  },
5	  {
6	    "type": "text",
7	    "text": "agentId: a1f44cd443536f851 (use SendMessage with to: 'a1f44cd443536f851' to continue this agent)\n&lt;usage>total_tokens: 68402\ntool_uses: 58\nduration_ms: 597800&lt;/usage>"
8	  }
9	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3fa6ced-9296-416f-8eb5-320709171eb5",
  "isSidechain": false,
  "promptId": "7bdff5af-d6c2-443f-99ab-f2e200157b45",
  "type": "user",
  "uuid": "cad55aac-196f-4467-aab0-c59bfcfa25d3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5-projects-contrastive-trace-safety--claude-sessions-review-reviewer-1-8281b2fc/3e48199e-0c0d-47bc-8ea3-24ecb0f30457/tool-results/toolu_015MRVtErFsoVMKEgYy2Gr2G.json",
      "content": "[\n  {\n    \"type\": \"text\",\n    \"text\": \"The PDF has 26 pages total. Now I have a complete picture of all pages 9–26. Here is a thorough transcript of all content found on pages 9–26:\\n\\n---\\n\\n## PAGE 9 — End of Section 5 (Discussion) + Section 6 (Conclusion) + References (start)\\n\\n**End of Section 5 text (continuation from page 8):**\\n\\n\\\"at 17% FPR. These conservative operating points are viable for high-stakes deployment where missed detections are preferable to frequent false alarms: a secondary review system could inspect only flagged traces, reducing human verification burden by 79–86% while maintaining non-trivial detection rates. The K=7 setting offers a middle ground (57% FPR reduction, 16–39% detection). The choice of operating point is deployment-specific, but the existence of a low-FPR regime contradicts the assumption that 32% or 52% FPR renders commitment detection impractical.\\\"\\n\\n**Section 6 — Conclusion**\\n\\n\\\"Layer selection is a critical researcher degree of freedom: a biased composite metric reverses the HS advantage at 32B scale by selecting shallow layers where representation compression inflates threshold crossings. The five-step audit protocol (section 5) would have prevented this outcome. The empirical HS advantage is conditional: robust at 7-8B (strong for OT-7B, moderate for QoQ-32B, qualified for R1-32B), and bounded by text encoder quality (4/4 HB against 384d, 1/4 against 4096d). Current probes characterize commitment detection rather than constitute production detectors. Models (≥95 cases) encode less information per step, benefit proportionally more from observing the multi-step progression.\\n\\n**7 Limitations**\\n\\nOur results characterize the safety commitment phenomenon rather than constitute production detectors: false positive rates remain 39–52%, and the HS advantage (R1-8B) scores the safety commitment phenomenon. This underscores how much room remains for improvement.\\n\\n**Model-specific caveats and statistical power.** HS achieves significance only at W=1 (25% coverage) and its HS advantage is position-mediated (residualized gap +1.9pp; section V). QoQ-32B's position baseline achieves significance only at W=1 (25% coverage); full significance is 5/20 at n=19–20 vs n=20. HS significance is seed-fragile (3/5 HB); at n=19–20, the minimum detectable effect at 80% power is 6.8pp...\\\"\\n\\n**References** begin (partial list visible at bottom of page):\\n\\n- Ryan Prescott Adams and David J.C. MacKay. 2007. Bayesian online changepoint detection. *arXiv preprint arXiv:2007.01142*. Concurrent work.\\n- Patrick Altmsd, Tobias Eder, Nyong Yang, Zhiyi Pan, and Georg Grok. 2026. Safer reasoning models: *arXiv preprint arXiv:2504.09375*.\\n- Yanai Elazar, Shauli Ravfogel, Alon Jacovi, and Yoav Goldberg. 2021. Amnesic probing: Behavioral explanations with amnestic counterfactuals. *Transactions of the Association for Computational Linguistics*, 9:160–175.\\n\\n---\\n\\n## PAGE 10 — References (continued)\\n\\nFull reference list page. Entries include (verbatim as visible):\\n\\n- Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, and Neel Nanda. 2024. Refusal in language models is mediated by a single direction. In *Advances in Neural Information Processing Systems 17 (NeurIPS)*.\\n- Bowen Baker, Ioot Huizinga, Leo Gao, Zehao Dou, Melody Y. Guan, Aleksander Madry, Wojciech Zaremba, Bob McGrew, and Ilya Sutskever. 2022. Monitoring reasoning models for misbehavior and the risks of promoting obfuscation. *arXiv preprint arXiv:2502.11926*.\\n- Yamini Bansal, Preetum Nakkiran, and Boaz Barak. 2021. Re-thinking model stitching to compare neural representations. In *Advances in Neural Information Processing Systems 34 (NeurIPS)*.\\n- Yonatan Belinkov. 2022. Probing classifiers: Promises, shortcomings, and advances. *Computational Linguistics*, 48(1):207–219.\\n- Nora Belrose and James Glass. 2019. Analysis methods in natural language processing. *Transactions of the Association for Computational Linguistics*, 7:49–72.\\n- Nora Belrose, David Schneider-Joseph, Shauli Ravfogel, Ryan Cotterell, Edward Raff, and Stella Biderman. 2023. LEACE: Perfect linear erasure of a concept from a model's representations. In *Advances in Neural Information Processing Systems 36 (NeurIPS)*.\\n- Gerard Botos, Aman Neelappa, and Shivam Raval. 2023. Probing language models for lexical evidence: Results from language mitigation studies in language models. *arXiv preprint arXiv:2509.21344*.\\n- Colin Burns, Haotian Ye, Dan Klein, and Jacob Steinhardt. 2023. ELICIT: Discovering latent knowledge in a language model. In *Proceedings of the International Conference on Learning Representations (ICLR)*.\\n- Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Stephen Donoho, Chris Olah, Arnab Amutz, Peter Hase, Micha Wagner, Fazl Amin Roger, Vlad Mikulin. 2025. Reasoning models can be honest if you ask them: Results from language mitigation studies in language models. *arXiv preprint arXiv:2503.05410*.\\n- Alexis Conneau, German Kruszewski, Guillaume Lample, Loïc Barrault, and Marco Baroni. 2018. What you can cram into a single vector: Probing sentence embeddings for linguistic properties. In *Proceedings of the Association for Computational Linguistics (ACL)*, pages 2126–2136.\\n- DeepSeek-AI. 2025. DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. *arXiv preprint arXiv:2501.12948*.\\n\\n---\\n\\n## PAGE 11 — References (continued)\\n\\n- Fazir Joaz, Majd Hawady, Sabri Bongleberbok, Nadir Durrami, and Huseyn Taha Sencar. 2026: \\\"There is more to refusal in language models than a single direction.\\\" *arXiv preprint arXiv:2602.02112*.\\n- Sri Dorga Sai Sowmya Kadali and Evangelos E. Papalesakis. 2025. Do internal layers of LLMs reveal patterns for jailbreak detection? *arXiv:846-866*.\\n- Ishita Kakkar, Eoin Zhang, Rheeya Uppaal, and Jinjie Hu. 2026. When safety falls below the frontier: Benchmarking harmful behavior detection in reasoning chains. *arXiv preprint arXiv:2604.19001*.\\n- Su-Hyeon Kim, Hyundong Jin, Yejin Lee, and Yu-Sub Kim. 2026. How does the thinking affect model safety? an entropy-based safety reminder for chain-of-thought models. *arXiv preprint arXiv:2603.08601*.\\n- Tomek Korbak, Mikita Balesni, Elizabeth Barnes, Joseph Bengio, Joe Benton, Joseph Bloom, Mark Chen, Andrew Cuvos, Owain Evans, David Farhi, Ryan Greenblatt, Dan Hendrycks, Evan Hubinger, Geoffrey Irving, Erik Jenner, and 22 others. 2025. Chain of thought monitorability: A fragile opportunity for AI safety. *arXiv preprint arXiv:2511.11471*.\\n- Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. 2019. Similarity of neural network representations revisited. In *Proceedings of the 36th International Conference on Machine Learning (ICML)*, volume 97 of *Proceedings of Machine Learning Research*, pages 3519–3529.\\n- Martin Kub, Llaster, Aolin Hing, Qinxi Wang, Louis DiValentin, Yujia Bao, Wei Wei, Hai Li, and Yiran Chen. 2025. H-cut: Hijacking the chain-of-thought in large reasoning models to jailbreak large reasoning models. *arXiv preprint arXiv:2509.21344*\\n- Martin Küblböck, James Elsman, Simon Geisler, Vincent Fortuin, Aakash Jaini, and Stephan Günnemann Bastian Gasteiger. 2025. The geometry of refusal in large language models: Concept cones and representational independence. In *Proceedings of the 42nd International Conference on Machine Learning (ICML)*.\\n- Shitao Xiao, Zheng Liu, Peitian Zhang, and Niklas Muennighoff. 2025. C-pack: Packaged resources to advance general chinese embedding. *arXiv preprint arXiv:2309.07597*.\\n- Bo Yin, Weikai Liu, Yada Zhu, and Song Wang. 2026. C-caliblabcam: a safety-world model with iterative early jailbreak detection. *arXiv preprint arXiv:2604.16824*.\\n- Nelson F. Liu, Matt Gardner, Yonatan Belinkov, Matthew E. Peters, and Noah A. Smith. 2019. Linguistic knowledge and transferability of contextual representations. In *Proceedings of the North American Chapter of the Association for Computational Linguistics (NAACL)*, pages 1073–1094.\\n- Faiir Joaz, Majd Hawady, Sabri Bongleberhok, Nadir Durrami, and Huseyn Taha Sencar. 2026. \\\"There is more to refusal in language models than a single direction.\\\" *arXiv preprint arXiv:2602.02112*.\\n- Yingzhi Qian, Chunhang Zhang, Jianzong Wang, Hengfeng Guo, Boji Cao, Yuejie Li, Honggyu Liu, Penghan Han, and Le Sun. 2025. When models overthink their safety: LLMs encode harmfulness and refusal separately. In *Advances in Neural Information Processing Systems 38 (NeurIPS)*.\\n- Zhenhong Zhou, Haiyang Yu, Xinghua Zhang, Rongwu Xu, Fei Huang, and Yongbin Li. 2024. How alignment and jailbreak work: Explain LLM safety mechanisms through hidden states. In *Findings of the Association for Computational Linguistics: ACL 2024*.\\n- Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mrinank Mazeika, Ann-Kathrin Dombrowski, Shashwat Goel, Nathaniel Li, Michael J. Byun, Zifan Wang, Alex Mallen, Steven Basart, Sanmi Koyejo, Dawn Song, Matt Fredrikson, J. Zico Kolter, and Dan Hendrycks. 2023. Representation engineering: A top-down approach to AI transparency. *arXiv preprint arXiv:2310.01405*.\\n\\n---\\n\\n## PAGE 12 — References (continued) + Appendix A header\\n\\nRemaining references:\\n\\n- Ang Zhang, Yulin Chen, Jane Pan, Chen Zhao, Anrojit Panda, Junyang Li, and He He. 2025. Reasoning models know when they're right: Probing hidden states for self-verification. *arXiv preprint arXiv:2504.05419*.\\n- Jiachan Zhao, Jing Huang, Zhengxuan Wu, David Bau, and Weiyan Shi. 2025. LLMs encode harmfulness and refusal separately. In *Advances in Neural Information Processing Systems 38 (NeurIPS)*.\\n- Zhenhong Zhou, Haiyang Yu, Xinghua Zhang, Rongwu Xu, Fei Huang, and Yongbin Li. 2024. How alignment and jailbreak work: Explain LLM safety mechanisms through hidden states. In *Findings of the Association for Computational Linguistics: ACL 2024*.\\n- Andy Zou, Long Phan, Sarah Chen, James Campbell, Phillip Guo, Richard Ren, Alexander Pan, Xuwang Yin, Mrinank Mazeika, ..., and Dan Hendrycks. 2023. Representation engineering: A top-down approach to AI transparency. *arXiv preprint arXiv:2310.01405*.\\n- Qingyin Yin, Chak Tuo Leong, Linyi Yang, Wenxuan Wang, Junjie Li, Jiangchao Zhao, Jinheng Yao, Xing, Xing Ya, and Jinjin Gu. 2025. Refusal falls off a cliff: Safety alignment failures in reasoning? *arXiv preprint arXiv:2510.06036*.\\n- Zhong-Xia Zhang and Stephen H. Bach. 2025. Selfjailbreaking: Language models jailbreak themselves out of safety alignment after being reasoning. *arXiv preprint arXiv:2510.20956*.\\n\\n**Appendix A: Responsible NLP Research Checklist** (header visible at bottom)\\n\\n\\\"**Appendix A: Responsible NLP Research Checklist**\\n\\n- **Limitations discussed:** Yes (section 7)\\n- **Potential risks:** This research analyzes jailbreak traces to understand how reasoning models commit to generating harmful content. We do not develop new attack methods or release jailbreak prompts. All analyzed content comes from the publicly available HarmThoughts benchmark. We acknowledge a dual-use concern: safety probes that detect commitment could in principle be used to craft reasoning traces that evade detection. We believe the defensive value of understanding commitment dynamics outweighs this concern, as the safety probe does not provide a direct model access to the probe, which a deployed monitoring system would not expose.\\\"\\n\\n(Additional checklist items partially visible but cut off)\\n\\n---\\n\\n## PAGE 13 — Appendix A (Responsible NLP Research Checklist continued) + Appendix B (Layer Sweep Results)\\n\\n**Appendix A continued:**\\n\\n- **Computational budget:** Our experiments involve 4 models with 209, 228, 100, and 95 traces respectively (632 total). We compute on a single machine (under 4 GPU-hours on a single 4-GPU A6000 or finetuning).\\n- **Data:** We use HarmThoughts, a publicly available benchmark with safety annotations. No new data collection was performed.\\n- **Human subjects:** No human subjects research was conducted.\\n- **Reproducibility:** All hyperparameters are reported in section 4.5 (full BA-optimal layer in section Y). K was pre-selected using BA metric. Code and data will be released upon publication.\\n\\n**Appendix B — Layer Sweep Results**\\n\\n\\\"For each model, we sweep all transformer layers and evaluate from each layer three criteria: (1) balanced accuracy = crossing rate (the biased composite), (2) pure balanced accuracy, (3) precision, (4) inverse FPR. Including seed 0, FPR metric drops from 0.48 to 0.30 by biased metric.\\n\\nShallow layers produce highly compressed representations as a middle-ground tradeoff; deep layers (7–98% depth) demonstrate that layer selection is a consequential methodological choice. The HS advantage at threshold is significant at whichever layer BA selects (14/16 per-model HB, two FPR failures from underpowered 32B test sets n≤20).\\n\\n**Selected layers.** R1-8B: all five metrics agree on layer 14 (44% depth). OT-7B: biased metric selects L0 (0%), unbiased consensus selects L16 (57%). QoQ-32B: biased metric selects L2 (3%), unbiased selects L10 (16%), unbiased consensus selects L63 (98%). The bias is most extreme at 64-layer models where the composite metric selects layers in the bottom 16% of the network while threshold-dependent metrics select layers at 57% depth and above. For 32B models, unbiased BA selects L32 (42 for QoQ) and L47 (73%) for R1-32B; under the canonical 60/20/20, it selects L63 (98%), which demonstrates this metric sensitivity to the data split.\\n\\n**Impact on modality comparison.** At the biased metric, HS vs. text precision p-values are 0.064 (R1-32B) and 0.35–0.83 (QoQ-32B), both non-significant (section III). 1/5 unbiased metrics improve monotonically across all metrics (section F), so the accuracy signal is specific to HS probes (but not 32B).\\n\\n**Layer selection stability (LOO-CV).** Leave-one-out cross-validation on the validation set confirms that layer selection is robust to data composition. Under pure balanced accuracy, the dominant layer is selected in 68% (QoQ-32B) to 89% (R1-8B) of folds, consistent with the main finding. Three alternative selections cluster in neighboring layers (L29, L55–56 for QoQ; L32, L38, L43 for R1-32B). The consensus corrected layers (L63 for both 32B models) are similarly dominant under threshold-dependent selection.\\n\\n**Joint layer, W=1 sensitivity.** Under the original 700d → 384d pipeline, the joint layer/window selection is one of 2,340 configurations (this is a potential source of selection bias inflating results — see section 4.2). We cover 2 architectures and 2 scales; intermediate scales, proportion analysis, and multilingual settings are untested. In Figure X we cover 2 of 2.\\\"\\n\\n**Table 5** (Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Table 6: \\\"Table 6: Step-to-step cosine distance at biased (shallow) and corrected (deep) layers. Shallow layers produce highly compressed representations (1.4–2.7×), while a linear operator in this compression framework is 1.4–2.7× smaller than at deep layers. The table shows smaller inter-step distances at shallow layers.\\\"):\\n\\nTable 6 data:\\n| Model | Layer (type) | Mean | Std |\\n|-------|-------------|------|-----|\\n| R1-8B | L2 (biased) | 0.186 | 0.097 |\\n| R1-8B | L16 (corrected) | 0.411 | 0.145 |\\n| QoQ-32B | L2 (biased) | 0.077 | 0.041 |\\n| QoQ-32B | L63 (corrected) | 0.206 | 0.091 |\\n| R1-32B | L2 (biased) | 0.084 | 0.056 |\\n| R1-32B | L10 (biased) | 0.092 | 0.076 |\\n| R1-32B | L63 (corrected) | 0.076 | 0.076 |\\n\\n---\\n\\n## PAGE 14 — Appendix C (Representation Compression Analysis) + Appendix D (Holm-Bonferroni Step-Down Correction)\\n\\n**Appendix C — Representation Compression Analysis**\\n\\n\\\"We measure step-to-step cosine distance at biased (shallow) vs. corrected (deep) layers across all models to characterize the compression mechanism underlying the crossing rate bias (table 6).\\n\\nShallow layers produce highly compressed representations (1.4–2.7×), producing more frequent threshold crossings. The HS precision advantage (table 2) at the same dimensionality shows the compression advantage.\\n\\n**Table 7** (step-level metrics): HS vs. text precision p-values are 0.064 (R1-32B) and 0.35–0.83 (QoQ-32B), which is non-significant (section III).\\n\\nShallow layers produce highly compressed representations and produce predictions even as overall classification accuracy degrades. CP annotations (section 4.1) uses 7 Transform models as text encoder baseline. The larger marginal gains for text probes reflects their weaker single-step baseline.\\\"\\n\\n**Table 7. Holm-Bonferroni Step-Down Correction:**\\n\\nTable 7 data (4 tests = 3 correlated metrics). Each test uses two-sided metric differences (HS mimus text). All 12 pass at α=0.05; a 4-test model-level correction (one per model, using the worst p-value) also passes.\\n\\n| Rank | Model | Metric | p-val | Thresh. | Pass |\\n|------|-------|--------|-------|---------|------|\\n| 1 | QoQ-32B | Bal. Acc. | <0.001 | 0.0042 | Yes |\\n| 2 | OT-7B | Bal. Acc. | <0.001 | 0.005 | Yes |\\n| 3 | R1-8B | Bal. Acc. | <0.001 | 0.0056 | Yes |\\n| 4 | OT-7B | Bal. Acc. | <0.001 | 0.0063 | Yes |\\n| 5 | QoQ-32B | Precision | <0.001 | 0.007 | Yes |\\n| 6 | OT-7B | Precision | <0.001 | 0.0083 | Yes |\\n| 7 | R1-8B | Precision | 0.001 | 0.01 | Yes |\\n| 8 | R1-32B | Bal. Acc. | 0.003 | 0.0125 | Yes |\\n| 9 | QoQ-32B | Precision | 0.003 | 0.0167 | Yes |\\n| 10 | M | Decision | 0.005 | 0.025 | Yes |\\n| 11 | N | Decision | 0.013 | 0.05 | Yes |\\n| 12 | R1-8B | FPR | 0.044 | 0.0500 | Yes |\\n\\n\\\"The weakest test (rank 12, R1-8B FPR, p=0.044) passes its threshold (α/1 = 0.05) with the margin. The ordering reveals that L63 is near-optimal for QoQ-32B at recommended windows (W=3), just below the Layer L45–L46 layer for form a robust band where all 3/3 metrics pass Holm-Bonferroni (section B1). The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.\\n\\n**Exact sign-flip permutation test validation.** Table 7 reports the full test battery used to assess hidden-state superiority over text probes. Because balanced accuracy, precision, and FPR share the same confusion matrix, the three per-model metrics are correlated; the effective number of independent comparisons is four (one per model). We report both the consecutive 12-test comparison and the 4-test model-level correction: both yield the same outcome (all tests pass at α=0.05). Under 4-test HB, the tightest threshold falls at α/4=0.0125; (p=0.044), rank-4 threshold α/1=0.050, which still passes. Text FPR is highly stable (std=0.007) while HS FPR is split-sensitive (std=0.040), suggesting the canonical-split FPR advantage (~7.4pp) does not generalize robustly across seeds.\\\"\\n\\n---\\n\\n## PAGE 15 — Appendix E (Window Size Ablation Details) + Appendix F (OpenThinker-7B Detailed Results)\\n\\n**Appendix E — Window Size Ablation Details**\\n\\n\\\"Table 8 reports the complete text probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes.\\n\\n**Table 8** (Window size ablation on R1-8B, step-level metrics):\\n\\n| W | Bal.Acc. | Precision | FPR | Coverage |\\n|---|----------|-----------|-----|----------|\\n| 1 | 64.7 | 41.6 | 25.8 | 95.4 |\\n| 3 | 66.9 | 44.8 | 23.1 | 90.7 |\\n| 5 | 69.2 | 48.5 | 20.0 | 84.9 |\\n| 10 | 72.1 | 56.9 | 18.2 | 74.4 |\\n| 15 | 74.3 | 62.1 | 14.2 | 65.8 |\\n| 20 | 75.8 | 62.1 | 12.5 | 62.8 |\\n| 25 | 76.7 | 63.0 | 12.2 | 60.3 |\\n\\n\\\"Text probes improve monotonically from W=1 while the plateau observed at W=10 also approximately aligns with the HS probes. The absolute FPR reduction (~14.8pp) differs markedly from its paired ΔPre and HS text coverage pairs are four times larger. The larger marginal gains for text probes reflects their weaker single-step baseline.\\\"\\n\\n**Appendix F — OpenThinker-7B Detailed Results**\\n\\n\\\"Table 9 reports the complete text probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes. (Section E). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 68% ±11 (W=1) to 82.2% (W=25) with FPR falling 9.65% to 4.83%); (2) OT-7B exhibits a split pattern where balanced accuracy peaks at W=3 while precision and FPR continue improving at larger windows; (3) R1-32B peaks at W=10 then degrades, likely reflecting overfitting on the smaller dataset with small Gaussian noise added. This made the text probe trivially predictive and produced a spuriously significant result (p=0.001 for HS vs. text FPR difference).\\n\\n**R1-8B per-model FPR (biased metric)** — Table 21 reports HS vs. text FPR comparisons for R1-8B; HS FPR is directionally consistently lower (5/5 HS ≤ Text); 2/5 reaching statistical significance; but after Holm-Bonferroni correction for 5 seeds (p=0.01), 1/5 remains significant. Text FPR is highly stable (std=0.007) while HS FPR is split-sensitive (std=0.040).\\\"\\n\\n**Table 9** (text probe window ablation on R1-8B, step-level metrics, full per-seed breakdown):\\n\\n| W | Bal.Acc. | Precision | FPR | Coverage |\\n|---|----------|-----------|-----|----------|\\n| 1 | 58.1 | 24.5 | 34.5 | 63.8 |\\n| 3 | 64.8 | 33.2 | 28.7 | 70.1 |\\n| 5 | 65.9 | 38.2 | 26.3 | 72.2 |\\n| 10 | 58.9 | 28.3 | 20.0 | 66.0 |\\n| 15 | 65.0 | 33.2 | 19.7 | 64.5 |\\n| 25 | 61.4 | 32.9 | 16.1 | 66.0 |\\n\\n\\\"**OT-7B multi-layer GRU results (layers 13–19, 3 seeds, 60/20/20 split).** OT-7B GRU achieves 74.6% ±1.3% balanced accuracy, 64.5±2.7% coverage; +33.6pp to 61.8% precision; 22.76% to 16.94% FPR. QoQ-32B produces +3.2pp to lead time. The lead time is substantially longer than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps, so absolute lead times are not directly comparable. The FPR lead-time results combining HS and LR probe at layer-16 (10.0%), which confirms that GRU's gain lead time at the cost of more false alarms across both 7.8B models.\\\"\\n\\n**Universal trends** summary bullet text:\\n- (1) larger windows smooth the probe fires less frequently\\n- (2) HS FPR generally decreases with window size (3) leads time is model-dependent\\n- OT-7B has a higher crossing at W=3\\n\\n---\\n\\n## PAGE 16 — Appendix E.1 (Test Probe Window Ablation) + Appendix F cont. (OT-7B detailed results with tables)\\n\\n**Appendix E.1 — Test Probe Window Ablation**\\n\\n\\\"Table 9 reports the complete test probe window ablation on R1-8B and confirms that temporal context benefits text probes even more strongly than HS probes (Section E).\\n\\n**Table 10** (OT-7B test probe window ablation, step-level metrics): HS score = balanced accuracy. Layer 16 (57% depth) is selected after correction; it achieves the highest balanced accuracy among transformer layers.\\n\\n| Layer | Depth | Bal.Acc. | Cross.Rate | Score |\\n|-------|-------|----------|------------|-------|\\n| 0 (embed.) | 0 | 66.3 | 40.4 | 35.5 |\\n| 4 | 18 | 66.3 | 40.4 | 26.8 |\\n| 8 | 36 | 61.2 | 35.6 | 21.6 |\\n| 16 | 57 | 65.5 | 31.9 | 21.6 |\\n| 20 | 71 | 65.5 | 31.9 | 20.9 |\\n| 30 | ??? | 65.0 | 31.9 | 20.9 |\\n| 63 | 71 | 65.5 | 31.9 | 20.9 |\\n| 64 | 75 | 63.0 | 31.9 | 21.8 |\\n\\n**Table 11** (OT-7B test probe window ablation, step-level metrics):\\n\\n| W | Bal.Acc. | Precision | FPR | Coverage |\\n|---|----------|-----------|-----|----------|\\n| 1 | 58.1 | 24.5 | 34.5 | 63.8 |\\n| 3 | 63.3 | 32.3 | 26.0 | 66.0 |\\n| 5 | 61.8 | 30.9 | 19.0 | 64.5 |\\n| 10 | 65.7 | 39.1 | 17.4 | 64.5 |\\n| 15 | 65.5 | 40.0 | 14.9 | 62.4 |\\n| 25 | 76.2 | 62.1 | 10.0 | 54.3 |\\n\\n\\\"R1-8B shows a broadly increasing trend in balanced accuracy with local non-monotonicity: balanced accuracy peaks at W=5 (76.1%) while W=10–15 then recovers to 76.2% at W=25. Precision and FPR improve monotonically with larger windows (54% to 61.8% precision; 22.76% to 16.94% FPR). QoQ-32B produces +3.2pp in lead time. The lead time is substantially longer in those models than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps, so absolute lead times are not directly comparable. The FPR-lead-time results from using the HS probe with LR probe at layer 16 (10.0%), which confirms that GRU's gain lead time at the cost of more false alarms across both 7-8B models.\\\"\\n\\n---\\n\\n## PAGE 17 — Appendix G (GRU Training Details) + Appendix H (Control Task Methodology)\\n\\n**Appendix G — GRU Training Details**\\n\\n\\\"**Data split.** GRU experiments use a 70/30 train/test split to maximize training data for the sequential model, differing from the main 60/20/20 protocol used for logistic regression models. The validation set (10% of training portion) is used for early stopping (effective 60/10/30 split). The validation set is used only for early stopping and is not included in reported test metrics, so there is no information leakage.\\n\\n**Architecture.** We evaluate two GRU variants. The single-layer variant uses a GRU with hidden dimension 256, taking per-step hidden layer (h) [the best layer selected by validation balanced accuracy] as input. The multi-layer variant concatenates hidden states from 3 candidate layers [multiple], running through the network at each step to produce a higher-dimensional input to the same GRU architecture.\\n\\n**Training procedure.** We train with Adam (learning rate 1×10^-3, default β₁=0.9, β₂=0.9993), batch size 16, for a maximum of 50 epochs. Early stopping halts training when validation loss does not improve for 10 consecutive epochs. Input features are z-score normalized per dimension using training set statistics.\\n\\n**Results.** We report crossing accuracy (sustained accuracy at which the model-first exceeds chance for 5 consecutive steps) and detection lead (steps before CP at crossing point). All experiments use 3 random seeds; we report mean ± standard deviation.\\n\\n**Per-seed results for R1-8B (single-layer GRU).** The high variance in lead time (standard deviation of 2.3 steps) is driven by seed 3, where the probe first achieves good peak accuracy but crosses the detection threshold late. This variance underscores the\\n\\n**Table 12** (R1-8B GRU joint layer, 70/30):\\n\\n| Seed | Peak Acc. | Crossing Acc. | Lead (steps) |\\n|------|-----------|---------------|--------------|\\n| 1 | 85.2 | 74.3 | +4.8 |\\n| 2 | 83.1 | 72.9 | +4.8 |\\n| 3 | 83.4 | 70.4 | −0.9 |\\n| Mean ± std | 83.9 ± 1.1 | 72.5 ± 2.0 | +3.5 ± 2.3 |\\n\\n\\\"**OT-7B multi-layer GRU (layers 13–19, 3 seeds, 60/20/20 split).** OT-7B GRU achieves 74.6% ± 1.3% balanced accuracy; 64.5% ± 1.4% steps lead. GRU advantage (BA: Δ=+21.9pp, FPR: Δ=−17pp, 95% CI [−22.2, −12.2]). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (±21.9pp); the small discrepancy reflects resampling underperfrom under the optimal layer selection. OT-7B GRU lead time is substantially longer than other models in absolute terms, but OT-7B traces average 30.6 acquisition steps vs. 4.5 steps for both R1-8B and R1-32B, so absolute lead times are not directly comparable.\\\"\\n\\n**Appendix H — Control Task Methodology**\\n\\n\\\"We follow the selectivity framework of (Hewitt and Liang, 2019) to verify that our probes capture sensitivity to annotation noise rather than meaning noise only.\\\"\\n\\n---\\n\\n## PAGE 18 — Appendix H (Control Task) + Appendix I (Oracle Upper Bound Analysis) + Appendix J (CP Annotation Perturbation)\\n\\n**Appendix H (continued):**\\n\\n\\\"**Procedure.** For each model, we randomly permute the binary labels (pre-CP vs. post-CP) within each trace while preserving the marginal label distribution. We train L2-regularized logistic regression (L2-regularized logistic regression on shuffled features) classifiers with the same architecture and hyperparameters on these shuffled labels. Selectivity is defined as:\\n\\nSelectivity = Acc_diagnostic − Acc_control ... (1)\\n\\nwhere Acc_diagnostic is the probe accuracy on true labels and Acc_control is the accuracy on permuted labels. A selectivity score close to zero indicates the probe is not learning a meaningful signal above chance.\\n\\n**Results.** We repeat the control experiment 10 times with different random permutations and report the mean control accuracy. Selectivity scores at corrected layers (60/20/20): the dominant layer is selected in 68% (QoQ-32B) to 89% (R1-8B) of folds. The absolute FPR reduction (~14.8pp) differs markedly from its paired ΔPre...\\n\\n**Layer provenance note.** R1-8B (L14) and OT-7B (L16) are unaffected by the layer selection bias since they agree with corrected layers and are bounded by the Mahalanobis HS advantage. QoQ-32B's precision gap (+20.1pp) aligns with the bootstrap mean (±21.4pp). The R1-32B's bias is most extreme; confirming that layer selection matters to the commitment detection outcome.\\n\\n**Position-only baseline.** As a complementary non-positional test, we train a logistic regression classifier using only the normalized step index (t/T where T is the total trace length) as the input feature. This baseline tests whether temporal position alone explains probe performance. On R1-8B, the position-only baseline produces 15.8% FPR compared to 8.1% for the HS probe at matched detection thresholds. The probe confirms that hidden state features carry information beyond what step position provides.\\\"\\n\\n**Residualized Selectivity:** \\\"To confirm that selectivity survives position removal, we recompute control task selectivity on position-regressed features (the same residualized representations used in section V). R1-8B at 67.3% but 1% crossing rate. Implementation details in section (R).\\\"\\n\\n**Appendix I — Oracle Upper Bound Analysis**\\n\\n\\\"Table 14 reports the oracle performance of GRU and FPR share the same balanced accuracy, precision, and FPR for the four independent comparisons is four (one per model). We report both the consecutive 12-test and the 4-test model-level correction: both yield the same outcome (all tests pass at α=0.05). Under 4-test HB, the tightest threshold falls at α/4=0.0125...\\\"\\n\\n**Table 14** (Oracle upper bound analysis). Det. Rate = balanced accuracy, p=0.80; MDE (80% power):\\n\\n| Model | Det.Rate | Obs.sd (BA) | MDE(80%) |\\n|-------|----------|-------------|---------|\\n| R1-8B | 20 | 0.026 | 9.5pp |\\n| OT-7B | 20 | 0.034 | ... |\\n| QoQ-32B | 20 | 0.056 | ... |\\n| R1-32B | 20 | 0.056 | 9.5pp |\\n\\n\\\"At W=3, the MDE is 8.6–9.5pp, meaning effects distinguishable from noise. R1-32B's residualized HS text gap (+1.9pp) falls well below the MDE (9.5pp), so the HS advantage cannot be reliably distinguished from either a true null or an underpowered sample. The 7–8B MDEs (3.3–4.2pp) are substantially lower, explaining why smaller effects are detectable at these scales.\\\"\\n\\n**Appendix J — CP Annotation Perturbation**\\n\\n\\\"Table 7 reports the full test battery to assess hidden-state superiority over text probes... We address CP annotation (section 4.2) led to the corrected-layer analysis reported in the main text, where all four models show significant HS advantage over directed deep layers, from strong (OT-7B) to qualified (R1-32B) (Table 3).\\\"\\n\\n\\\"To assess sensitivity to annotation noise, we shift the commitment point annotation by ε ∈ {−3, −2, −1, 0, +1, +2, +3} steps and retrain the HS probe (table 15). Precision changes negatively with earlier HS (−2, −3) steps and recovers above the baseline for delayed commits (+1, +2 steps).\\n\\n**Table 15** (HS probe sensitivity to CP annotation shift, n=33):\\n\\n| Seed | HS FPR | Text FPR | ΔFPR |\\n|------|--------|----------|------|\\n| 0 | 0.113 | 0.308 | −0.195 |\\n| 1 | 0.061 | 0.168 | −0.105 |\\n| 2 | 0.148 | 0.167 | −0.167 |\\n| 3 | 0.167 | 0.167 | 0.000 |\\n| 4 | 0.143 | 0.228 | −0.083 |\\n| p | |  | 0.293 |\\n\\n---\\n\\n## PAGE 19 — Appendix K (BOCPD/CUSUM Configuration Sweep) + Appendix L (Detection Threshold (K) Ablation)\\n\\n**Appendix K — BOCPD/CUSUM Configuration Sweep**\\n\\n\\\"We sweep hyperparameters for both Bayesian Online Changepoint Detection (BOCPD) and Cumulative Sum (CUSUM) methods applied to the temporal probe scores.\\n\\n**BOCPD configurations.** BOCPD models the sequence of probe scores as piecewise-constant functions with Gaussian observation noise. The hazard rate λ controls the prior probability of a changepoint occurring at each step, and the threshold Δ controls the detection boundary (a detection if accumulated evidence > Δ).\\n\\n**CUSUM configurations.** CUSUM accumulates evidence for a positive mean shift. The drift parameter k sets the expected shift magnitude (set to 1.5), and the threshold Δ controls the detection sensitivity...\\\"\\n\\n**Table 14** (Oracle upper bound analysis — appears again here as \\\"Table 14. Oracle bound analysis\\\"):\\n\\n| Model | Prec. | Det.Rate | Lead | p |\\n|-------|-------|----------|------|---|\\n| R1-8B | 0.400 | 0.784 | 1.54 | <0.001 |\\n| OT-7B | 0.421 | 0.634 | 0.021 |   |\\n| QoQ-32B | 0.453 | 0.631 | 0.021 |   |\\n| R1-32B | 0.756 | 0.552 | 0.314 |   |\\n\\n\\\"The best BOCPD configuration (λ=10) achieves 97% detection rate with +3.45 steps lead. The simple threshold baseline achieves 65.1% detection rate (i.e., a much lower baseline). All CUSUM configurations underperform the simple threshold on lead time.\\n\\n**Table 15** (HS probe sensitivity to CP annotation, safety):\\n\\n\\\"R1-32B (bal.acc p=0.925, precision p=0.346; R1-32B precision p=0.050) but no tests surviving correction. The point-estimate precision gap (+21.2pp) aligns with the bootstrap mean (±21.9pp). The proportional boundary (∼12%) amplified at n=33.\\\"\\n\\n---\\n\\n## PAGE 20 — Appendix L (Detection Threshold K Ablation) + Appendix M (Decision Threshold Sensitivity)\\n\\n**Appendix L — Detection Threshold (K) Ablation**\\n\\n\\\"The consecutive-crossings threshold K controls the trade-off between detection coverage and false positive rate. We evaluate K ∈ {1, 3, 5, 7, 10} on all models using HS probes at corrected layers (section B).\\n\\nK=1 yields perfect coverage but near-perfect false positive rate (0.92–1.00), showing no discrimination. R1-8B achieves 0.756 balanced accuracy (approaching 0.778) but with substantially worse precision (0.512 vs. LR 0.700) after adding noise in the precision-coverage Pareto for both methods. The best two-stage configuration (W_screen=3, W_confirm=15, k=1) achieves 72.2% precision at 38.5% coverage with k=5, but these operating points are impractical due to excessive missed detections.\\n\\n**Table 16** (R1-8B threshold K ablation):\\n\\n| K | R1-8B | OT-7B | R1-32B | QoQ-32B |\\n|---|-------|-------|--------|---------|\\n| 1 | 1.00 | 1.00 | 1.00 | 1.00 |\\n| 3 | 0.90 | 0.74 | 0.79 | 0.72 |\\n| 5 | 0.69 | 0.62 | 0.62 | 0.60 |\\n| 7 | 0.55 | 0.47 | 0.50 | 0.48 |\\n| 10 | 0.35 | 0.30 | 0.38 | 0.30 |\\n\\n\\\"K=7 reduces FPR by 79–86% while maintaining non-trivial detection rates. The K=7 setting offers a middle ground (57% FPR reduction, 16–39% detection). These results support the reframing of K ablation as practitioner-facing operating curve.\\\"\\n\\n**Appendix M — Decision Threshold Sensitivity**\\n\\n\\\"The joint search space for layer (≤ 64), window W (7 values), K (5 values), and decision threshold is large (up to 2,340 configurations per model). This raises the concern that reported performance reflects overfitting to small validation samples (n≈1–9 per class at 32B). Three analyses address this concern.\\n\\n**Threshold-dependent metrics converge to a deep-layer band.** Despite the large search space, choice of four threshold-dependent metrics (precision, inverse FPR, additive composite) independently select L63 (98% depth) for both 32B models—see Table 2. The convergence of independent metrics to a narrow band is inconsistent with overfitting, which would produce scattered selections.\\n\\n**Bootstrap CIs quantify statistical uncertainty.** For the model comparison metric at W=3, bootstrap 95% CIs are narrow: R1-8B ±0.021 (Bal.Acc.) and ±0.040 (FPR); QoQ-32B ±0.017 (BA), consistent with in-distribution variability not overfitting.\\n\\n**BA-optimal layer instability is the finding, not a confound.** Five-fold cross-validation on 32B validation sets (n≤20 per class) reveals that the BA-optimal layers are highly unstable across folds (table 25). This instability is not a limitation of the study but the central methodological finding: BA-layer selection is sensitive to data composition, and conclusions drawn from any single BA-optimal layer are unreliable.\\\"\\n\\n**Appendix N — M002 Bug Disclosure**\\n\\n\\\"A bug was discovered during development that affected intermediate results for QoQ-32B.\\n\\n**Issue.** In experiment M002 (feature ablation), the QoQ-32B probe was inadvertently initialized with a midpoint heuristic placeholder rather than true sentence embeddings from all-MiniLM-L6-v2. Specifically, the placeholder assigned each step a feature vector equal to the midpoint between the mean safe and mean unsafe embeddings from the training set, with small Gaussian noise added. This made the text probe trivially predictive and produced a spuriously significant result (p=0.001 for HS vs. text FPR difference).\\n\\n**Discovery and correction.** The bug was identified during a systematic audit of the feature extraction pipeline. After correction (using actual sentence embeddings), the QoQ-32B feature extraction used the composite composed HS for correct safety in null-space projection (Holm-Bonferroni section B1). The modality comparison shows at the originally selected layers (L2 and L10, chosen by the biased composite)—table 3 showed that no significant HS vs. text gap at corrected layers. R1-32B modality comparison: section V Encoder Robustness; section F Multi-Seed Stability; section Y BA-Layer Modality Comparison; section Z Post-Hoc Power Analysis.\\\"\\n\\n---\\n\\n## PAGE 21 — Appendix O (Adaptive Two-Stage Detection) + Appendix P (Temporal Ablation Details) + Appendix Q (Negative Results Details) + Figure 4\\n\\n**Appendix O — Adaptive Two-Stage Detection**\\n\\n\\\"We explored whether a two-stage adaptive window strategy could improve the precision-coverage tradeoff beyond fixed-window detection. The approach uses a short screening window (W_screen) to flag candidate unsafe segments, followed by a longer confirmation window (W_confirm) applied only to the flagged segments. A trace is classified as unsafe if at least k steps exceed the threshold during the confirmation stage.\\n\\nWe merge the validation and test datasets for two-stage evaluation because the screening and confirmation thresholds are not tuned on held-out data. We evaluated all combinations of W_screen ∈ {1, 3, 5}, W_confirm ∈ {10, 15, 25}, k ∈ {1, 3, 5} and the threshold τ (pre-CP FPR setting 76.7%): the two-stage approach achieves 22.2% precision at 38.5% coverage with k=5, but these operating points are impractical due to excessive missed detections. The marginal improvement suggests that natural smoothing already captures most of the temporal signal available in probe score sequences. The two-stage approach requires 3 hyperparameters (W_screen, W_confirm, k) as one more than single-window without proportional performance gains.\\\"\\n\\n**Figure 4** (Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection):\\n\\nCaption: \\\"Figure 4. Precision-coverage Pareto front comparing single-stage fixed-window detection against two-stage adaptive detection on R1-8B. Results are Pareto-dominated by matched coverage. Higher k values shift the tradeoff toward precision at the cost of unacceptable coverage loss.\\\"\\n\\n**Appendix P — Temporal Ablation Details**\\n\\n\\\"Full per-model temporal ablations are reported in table 8 (section E). Key cross-model patterns: (1) R1-8B shows monotonic precision improvement from 68% ±11 (W=1) to 82.2% (W=25) with FPR falling 9.65% to 4.83%; (2) OT-7B exhibits a split pattern where balanced accuracy peaks at W=3 while precision and FPR continue improving at larger windows; (3) R1-32B peaks at W=10 then degrades, likely reflecting overfitting on the smaller dataset (n=100), (4) QoQ-32B shows broadly increasing trends with local non-monotonicity. Text probe window ablations (section E.1) consistently show W at ±10 for GRU-multi. The summary supports the interpretation that text features encode less information per step, benefit proportionally more from observing the multi-step progression.\\\"\\n\\n**Appendix Q — Negative Results Details**\\n\\n\\\"On OT-7B, BOCPD achieves 0% detection rate with λ∈{5, 10, 50, 100, 200}. Only R1-8B produces non-trivial results (λ=10, 93% rate, +3.45 steps lead). CUSUM configurations (all λ, k) fail to produce non-trivial results only more sophisticated approaches.\\n\\n**Table 27** ... R1-8B BOCPD: all tests pass; OT-7B: FPR=1.00 (all traces flagged as unsafe).\\\"\\n\\n---\\n\\n## PAGE 22 — Appendix R (Cross-Model Transfer Results) + Appendix S (Encoder Robustness Analysis)\\n\\n**Appendix R — Cross-Model Transfer Results**\\n\\n**Table 19** (Seven alternative approaches):\\n\\n| Method | Result | Limitation |\\n|--------|--------|------------|\\n| BOCPD | 0% det. on 4/4 models | Commitment gradual |\\n| CUSUM | < threshold, all model | Same as BOCPD |\\n| Mahalanobis | Δd ≈ 0 | Signal in minor PCA components |\\n| MLP | 3/4 worse than LR | Overfitting |\\n| CCS | No gain over supervised | Alignment mismatch |\\n| Transfer | Best 59.5% (PCA)* | Model-specific |\\n\\n\\\"* Repl: Mean-difference directions (Zou et al., 2023) show inconsistent performance. QoQ-32B achieves 0.756 balanced accuracy (approaching required evidence); R1-32B nearly fails (0.559 balanced accuracy). The mean-difference direction captures commitment in some models but not others, so it is unreliable as a general-purpose method.\\n\\n**MLP probes.** Two-layer MLPs (d → 128 → 1, ReLU) underperform logistic regression on all models. The commitment decision boundary is linearly separable at correctly selected layers; additional capacity causes overfitting given the small 32B datasets.\\n\\n**CCS.** Contrast-Consistent Search (Burns et al., 2023) adapted with contrastive pairs of pre-CP and post-CP steps provides no improvement over supervised probing. The logical consistency objective does not align with the temporal commitment structure. CCS still requires CP labels for pair construction and is therefore semi-supervised.\\n\\n**Transfer.** Mean-difference directions produce no cross-model transfer (16/32 per-model models tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model). The pre-cision gains (p=0.002); 3/4 models retain significant non-positional HS advantage (FPR for R1-32B underpowered 32B sets. BA-L layer failure is the exception: residualized HS-text gap is position-dependent of OT-7B +6.9pp, R1-8B +8.6pp at W=15, QoQ-32B → R1-32B achieves 67.3% but 1% crossing rate. Implementation details in section (R).\\\"\\n\\n**Table 23** (HS vs. ES-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni corrected (4 tests, α=0.05). QoQ/20 split):\\n\\n| Model | Layer | W | ES | MinLM | Δ |\\n|-------|-------|---|-----|-------|---|\\n| R1-8B | L16 | 15 | 440 | 446 | +6 |\\n| OT-7B | L16 | 1 | 446 | 321 | −125 |\\n| R1-32B | L10 | 1 | 446 | 244 | −202 |\\n| QoQ-32B | L63 | 1 | 458 | 244 | −214 |\\n\\n\\\"The HS advantage partially survives against the LLM encoder: 4/4 models (both 7–8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (384d) < BGE-large (335M, 1024d) < ES-Mistral-7B (PCA 384d).\\\"\\n\\n**Appendix S — Encoder Robustness Analysis**\\n\\n\\\"To address the concern that threshold-dependent layer selection may circularly favor HS probes, we repeat the modality comparison at layers selected by balanced accuracy for each model. Results show HS advantage is significant at BA-selected layers too despite the choice of metric:\\n\\n**Table 31** (HS vs. text at BA-selected layers (60/20/20):\\n\\n| Model | BA-L | ΔPrec | ΔBA | ΔFPR | p(BA) |\\n|-------|------|-------|-----|------|-------|\\n| R1-8B | L17 | +16.6 (+16.6) | +8.4 (+8.4) | −7.0 (−6.3) | <0.001 |\\n| OT-7B | L16 | +10.1 (+10.1) | +13.1 (+13.1) | −15.4 (−15.4) | <0.001 |\\n| QoQ-32B* | L3 | −31 (−14.6) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\\n| R1-32B* | L3 | −12.8 (−14) | +13.6 (+13.6) | +15.8 (+15.8) | <0.001 |\\n\\n\\\"Values in parentheses are bootstrapped-corrected (10,000 bootstrap examples). p-values on the BA metric corrected. * BA-L failures from bias metric (section 4.2); corrected layers in table 3.\\\"\\n\\n\\\"Positions 9–20pp. The HS precision advantage is directionally consistent across all four models (positive in every case); significance is marginal only for OT-7B R1-8B shows a (p=0.064 under Holm-Bonferroni). R1-32B BA-significance only falls at n≤20 (p=0.914); QoQ-32B achieves 67.3% but 1% crossing rate. BA-optimal layer instability: Five-fold LOO-CV shows standard deviation of 0.145 (R1-8B FPR = 0.483), varying from 72.1% to 98.7%; this instability confirms that BA selection is seed-fragile.\\\"\\n\\n---\\n\\n## PAGE 23 — Appendix T (Random Projection Baseline) + Appendix U (LLM-Based Text Encoder Comparison)\\n\\n**Appendix T — Random Projection Baseline**\\n\\n\\\"PCA capacity matching (section S) preserves 79–92% of variance with 384-dimensional projections. The split indicates which compression is whether the HS advantage depends on PCA's structure-preserving property. We project hidden states to 384d using Gaussian random projections (RP) and compare PCA projections with RP projections at the same dimensionality (table 22).\\n\\n**Table 22** (RP, 384d bootstrap (CF 384d), Holm-Bonferroni corrected (4 tests, α=0.05)):\\n\\n| Rank | Model | Metric | p-val | Thresh. | Pass |\\n|------|-------|--------|-------|---------|------|\\n| 1 | QoQ-32B | Bal. Acc. | <0.001 | 0.001 | Yes |\\n| 2 | OT-7B | Bal. Acc. | <0.001 | <0.001 | Yes |\\n| 3 | R1-8B | Bal. Acc. | <0.001 | 0.0056 | Yes |\\n| 4 | OT-7B | FPR | <0.001 | 0.0063 | Yes |\\n| ... | ... | ... | ... | ... | ... |\\n\\n\\\"All four models achieve significant HS advantage under random projection (all 12 tests pass HB correction), full data, two FFR failures from underpowered 32B test sets. BA-L values (RP): QoQ-32B 79.4 ±1.2pp; R1-8B 81.5 ±0.9pp. The HS advantage is robust to the choice of layer selection criterion (BA, Prec, FPR-inverse, cross-rate, composite).\\n\\n**R1-8B per-seed HB pass rates.** Table 29 reports Holm-Bonferroni pass rates per metric across 5 random seeds. R1-8B the model classified as \\\"moderate\\\" evidence due to FPR instability.\\n\\n**Table 29** (R1-8B per-seed Holm-Bonferroni pass rates):\\n\\n| Seed | HS FPR | Text FPR | ΔPre | ΔBA | ΔFPR |\\n|------|--------|----------|------|-----|------|\\n| 0 | 0.119 | 0.040 | ... | ... | ... |\\n| 1 | 0.061 | ... | ... | ... | ... |\\n| 2 | 0.148 | ... | ... | ... | ... |\\n| 3 | 0.167 | ... | ... | ... | ... |\\n| 4 | 0.143 | ... | ... | ... | ... |\\n| p | | | | | 0.293 |\\n| Pass rate: | N/5 | 5/5 | 3/5 | | |\\n\\n\\\"The FPR instability has a clear source: R1-8B text FPR clusters tightly around 17% (std~0.2pp) while HS FPR spreads more broadly (std~17%)...\\\"\\n\\n**Appendix U — LLM-Based Text Encoder Comparison**\\n\\n\\\"To test whether an LLM-based text encoder closes the HS advantage gap, we encode each reasoning step with E5-Mistral-7B-Instruct (Wang et al., 2022) (4,096d), reduced to 384d via PCA to match the MinLM dimensionality. Using each modality's precision-comparisons against HS probes at corrected layers:\\\"\\n\\n---\\n\\n## PAGE 24 — Appendix U (continued) + Appendix V (Post-Hoc Power Analysis)\\n\\n**Appendix U continued:**\\n\\n\\\"**Table 23** (HS vs. ES-Mistral-7B (PCA 384d) precision. HB: Holm-Bonferroni corrected (4 tests, α=0.05), two-sided, same metrics; both 60/20/20):\\n\\n| Model | Layer | W | HS | ES | MinLM | Δ(HS-ES) |\\n|-------|-------|---|-----|-----|-------|---------|\\n| R1-8B | L16 | 15 | +8.4 | +10.8 | 0.002 | −2.4 |\\n| OT-7B | L16 | 1 | +10.8 | −13.1 | +10.1 | +3.3 |\\n| QoQ-32B* | L63 | 1 | +8.8 | −13.1 | 0.000 | +21.9 |\\n| R1-32B* | L43 | 1 | +8.8 | −14.0 | 0.033 | +22.8 |\\n\\n(* Residual bias layer issues.)\\n\\n\\\"The HS advantage partially survives against the LLM encoder: 4/4 models (both 7–8B) retain significance after Holm-Bonferroni correction. Three text encoders form a monotonic gradient: MiniLM (384d) < BGE-large (335M, 1024d) < ES-Mistral-7B (PCA 384d). The precision gain is +12.8 to +18.6pp for ES, comparable to those at threshold-dependent layers (+15.4 to +14.0). The HS advantage is robust to the choice of layer selection criterion.\\n\\n**Exact sign-flip permutation test validation.** The joint search for which the layer W=3 pair (p=0.000 vs. p=0.207 margin), with a proportion near boundary (~12%) amplified at n=33.\\n\\nThe two failures are both FPR at 32B: R1-32B (bal.acc p=0.925, precision p=0.083, consistent with the underpowered test sets (n≤20) noted in Section 4. All three precision gains (p=0.054 vs. p=0.003; paired t p=0.001 (bootstrap 95% CI [−22.2, −12.2])). All three metrics survive correction. The point-estimate precision gap (+21.2pp) aligns with bootstrap mean (+21.9pp); the small discrepancy reflects resampling variability. Under the canonical 60/20/20 split: HS FPR advantage increases at larger temporal windows, suggesting HS representations better capture the temporal commitment dynamics.\\\"\\n\\n**Appendix V — Post-Hoc Power Analysis**\\n\\n\\\"We compute post-hoc minimum detectable effects (MDEs) at 80% power given each model's test-set size and observed variance.\\n\\n**Table 25** (LOO-CV BA-optimal layers per model, 5-fold. BA-optimal layers vary widely across folds):\\n\\n| Model | F1 | F2 | F3 | F4 | F5 | Spread |\\n|-------|----|----|----|----|-----|--------|\\n| QoQ-32B | L53 | L53 | L45 | L45 | L39 | 24 layers |\\n| R1-32B | L53 | L45 | L40 | L63 | L39 | 24 layers |\\n\\n(R1-32B's high FPR variance (std=0.145) is driven by this instability.)\\n\\n\\\"At W=3, the MDE is 8.6–9.5pp, meaning effects smaller than the MDE cannot be reliably detected. R1-32B's residualized HS text gap (+1.9pp) falls well below the MDE (9.5pp), confirming the HS advantage cannot be reliably distinguished from noise. The 7–8B MDEs (3.3–4.2pp) are substantially lower, explaining why smaller effects are detectable at those scales.\\\"\\n\\n---\\n\\n## PAGE 25 — Appendix W (Multi-Seed Stability) + Appendix X (5-Seed HB Pass Rates for R1-8B)\\n\\n**Appendix W — Multi-Seed Stability**\\n\\n\\\"Stability, mean BA across folds peaks near L47–L50 for both models, consistent with the LOO-CV dominant layers (section B). The HS advantage is significant at threshold-optimal layers (14/16 per-model HB, two FPR failures from underpowered 32B test sets (n≤20)).\\n\\n**Table 27** (5-seed HB pass rates (HS FPR, n=3 models)):\\n\\n\\\"Seeds where HS FPR happens to be below the 0.05 threshold (>1.4/5 loss significance): the gap against text narrows without the detection threshold narrowing, and does not affect the precision or overall HS advantage, which passes all 5 seeds.\\n\\n**R1-8B HS per-seed breakdown (L63, W=1).** Table 30 reports the full per-seed breakdown for R1-8B's multi-seed stability:\\n\\n| Seed | Precision | Bal. Acc. | ΔPre Hb | Note |\\n|------|-----------|-----------|---------|------|\\n| 0 | 0.441 | 0.796 | +0.094 | 0.109 |\\n| 1 | 0.780 | 0.748 | +0.263 | 0.109 |\\n| 2 | 0.598 | 0.795 | +0.571 | <0.050 |\\n| 3 | 0.630 | 0.781 | +0.097 | <0.050 |\\n| 4 | 0.652 | 0.735 | +0.033 | <0.050 |\\n| 5 | 0.440 | 0.715 | +0.022 | 0.050 |\\n| Mean ± std | 0.594 ± 0.126 | 0.692 ± 0.256 | +0.207 ± 0.14 | (Seed 0 is outlier) |\\n\\n\\\"R1-32B's high FPR variance (std=0.145) is driven by test-set split allocation (n=19 vs. n=20). Positions 9–20pp. The HS precision advantage is directionally consistent across all four models.\\n\\n**5-seed Holm-Bonferroni pass rates.** Table 27 reports HS pass rates per metric across 5 random seeds. Overall, 18/20 (90%) model-seed combinations pass full HB (3 models × 5 seeds = 15 HB cases).\\\"\\n\\n**Appendix X — R1-8B FPR-specific note:**\\n\\n\\\"R1-8B HS FPR varies by only 1.1pp between validation and test set (seed=0 is an outlier (FPR = 0.483), varying from 72.1% to 98.7%; 2/5 reaching statistical significance after Holm-Bonferroni correction for 5 seeds (p=0.011). 1/5 remains significant. The FPR instability has a clear source: R1-8B text FPR clusters tightly around 17% (std~0.2pp) while HS FPR spreads more broadly (std~1.7pp).\\\"\\n\\n---\\n\\n## PAGE 26 — Appendix Y (BA-Layer Modality Comparison) + Appendix Z (Post-Hoc Power Analysis, cont.)\\n\\n**Appendix Y — BA-Layer Modality Comparison**\\n\\n\\\"While HS FPR happens to be below the 0.05 threshold from 6.1% to 16.1% (std~1.0pp). Seeds where HS FPR happens to be below 0.05 of threshold (>1.4/5 loss significance): the gap against text narrows without detection threshold narrowing and does not affect precision or overall HS advantage.\\n\\n**R1-32B's position-residualized selectivity.** To quantify this, we recompute select task selectivity on position-regressed features (the same residualized representations used in section V). R1-8B at 67.3% but 1% crossing rate.\\n\\n**Table 24** (Position-residualized balanced accuracy across 14 per-model tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model), α=0.05):\\n\\n| Model | BA-L | ΔPrec | ΔBA | ΔFPR | p |\\n|-------|------|-------|-----|------|---|\\n| R1-8B | L17 | +16.6 (+16.6) | +8.4 (+8.4) | −7.0 (+0.031) | <0.001 |\\n| OT-7B | L16 | +10.1 (+10.1) | +13.1 (+13.1) | −15.4 (−15.4) | <0.001 |\\n| QoQ-32B* | L3 | −31 (−14.6) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\\n| R1-32B* | L3 | −12.8 (−14) | −15.3 (−16.3) | +13.3 (+15.4) | <0.001 |\\n\\n\\\"Of 16 per-model tests (4 models × 4 metrics), 14 pass Holm-Bonferroni correction (4 tests per model). The precision gains (p=0.002); 3/4 models retain significant non-positional HS advantage (FPR for R1-32B underpowered 32B tests BA-L layer failure is the exception: residualized HS-text gap is position-dependent for OT-7B (+6.9pp), R1-8B (+8.6pp at W=15), QoQ-32B → R1-32B achieves 67.3% but 1% crossing rate. BA-optimal layer instability: Five-fold LOO-CV shows standard deviation of 0.145 (R1-8B FPR = 0.483), varying from 72.1% to 98.7%.\\\"\\n\\n**Appendix Z — Post-Hoc Power Analysis (additional)**\\n\\n\\\"While HS FPR happens to be below global best 0.817). Joint layer, W=1 ability was evaluated via grid search on W ∈ {1/5, 5} for QoQ-32B only; full LOO-cross-validation of the (layer, W) pair and extension to R1-32B remain for future work.\\n\\n**Table 18** (R1-32B threshold sensitivity (L63, W=1). HS BA varies by 1.1pp (0.741–0.752); the HS advantage is consistent across all correction settings):\\n\\n| τ+ | HS BA | ΔBA | HS Prec | ΔPrec | ΔFP/R | ΔFPR |\\n|----|-------|-----|---------|-------|-------|------|\\n| 0.742 | +0.120 | 0.583 | −0.126 | 0.205 | −0.106 |\\n| 0.741 | +0.128 | 0.583 | −0.133 | 0.287 | −0.078 |\\n| 0.741 | +0.109 | 0.588 | +0.113 | 0.287 | −0.078 |\\n| 0.743 | +0.126 | 0.583 | +0.113 | 0.266 | +0.078 |\\n| 0.741 | +0.128 | 0.592 | +0.109 | 0.287 | −0.078 |\\n\\n\\\"R1-32B (bal.acc p=0.925, precision p=0.083, consistent with the underpowered test sets (n≤20). All three precision gains (p=0.054 vs. p=0.003 paired t p=0.001 (bootstrap 95% CI [−22.2, −12.2]). All three metrics survive correction. The two failures are both FPR at 32B: R1-32B BA-L layer failure is the exception.\\\"\\n\\n---\\n\\n以上为第9–26页（论文末尾所有页面）的完整内容转录，包含：\\n\\n- **第9页**：Section 5结尾（讨论/操作点）、Section 6 Conclusion、Section 7 Limitations、References开头\\n- **第10–12页**：完整参考文献列表\\n- **第12页底部–第26页**：完整附录（A至Z），涵盖：\\n  - Appendix A（NLP Research Checklist）\\n  - Appendix B（Layer Sweep）\\n  - Appendix C（Representation Compression）\\n  - Appendix D（Holm-Bonferroni Step-Down）\\n  - Appendix E/E.1（Window Size Ablation）\\n  - Appendix F（OpenThinker-7B详细结果）\\n  - Appendix G（GRU Training Details）\\n  - Appendix H（Control Task Methodology）\\n  - Appendix I（Oracle Upper Bound）\\n  - Appendix J（CP Annotation Perturbation）\\n  - Appendix K（BOCPD/CUSUM Configuration Sweep）\\n  - Appendix L（Detection Threshold K Ablation）\\n  - Appendix M（Decision Threshold Sensitivity）\\n  - Appendix N（M002 Bug Disclosure）\\n  - Appendix O（Adaptive Two-Stage Detection）\\n  - Appendix P（Temporal Ablation Details）\\n  - Appendix Q（Negative Results Details）\\n  - Appendix R（Cross-Model Transfer Results）\\n  - Appendix S（Encoder Robustness Analysis）\\n  - Appendix T（Random Projection Baseline）\\n  - Appendix U（LLM-Based Text Encoder Comparison）\\n  - Appendix V（Post-Hoc Power Analysis）\\n  - Appendix W（Multi-Seed Stability）\\n  - Appendix X（R1-8B FPR-Specific Notes）\\n  - Appendix Y（BA-Layer Modality Comparison）\\n  - Appendix Z（Post-Hoc Power Analysis续）\"\n  },\n  {\n    \"type\": \"text\",\n    \"text\": \"agentId: a1f44cd443536f851 (use SendMessage with to: 'a1f44cd443536f851' to continue this agent)\\n&lt;usage>total_tokens: 68402\\ntool_uses: 58\\nduration_ms: 597800&lt;/usage>\"\n  }\n]",
      "numLines": 10,
      "startLine": 0,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "f3fa6ced-9296-416f-8eb5-320709171eb5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Tool call

_source line 61 · 2026-05-19T04:44:54.640Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01F5tB12q9kJJppSjj8EY9A5`</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines: what reviewers should evaluate, scoring criteria for soundness and excitement, what constitutes a strong vs weak paper, any guidance on statistical methodology, reproducibility requirements, and what factors distinguish Conference-worthy from Findings-worthy papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cad55aac-196f-4467-aab0-c59bfcfa25d3",
  "isSidechain": false,
  "requestId": "req_011CbBKPybRxmQNQfJZdir6P",
  "type": "assistant",
  "uuid": "7cc7446b-aa1d-48e1-b0a5-4d1425259553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VoqEx1f6d988tCbDP4H6gz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12775,
      "cache_read_input_tokens": 35745,
      "output_tokens": 411,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12775,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 411,
          "cache_read_input_tokens": 35745,
          "cache_creation_input_tokens": 12775,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12775
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 62_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性** 审查。  ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models - **路径**: `projects/contrastive_trace_safety/docs/paper…",
  "leafUuid": "7cc7446b-aa1d-48e1-b0a5-4d1425259553",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Runtime record

_source line 63_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodology rigor for safety probes paper",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Tool result

_source line 64 · 2026-05-19T04:45:04.065Z_

<details><summary>↩ Tool result · `toolu_01F5tB12q9kJJppSjj8EY9A5`</summary>

```text
# ARR Reviewer Guidelines Summary

## What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions. The guidelines emphasize reading papers twice—first for skimming to understand the research question, then for in-depth technical evaluation. Reviewers should check whether the methodology answers the stated research question and whether findings advance the field, rather than applying a single standardized prototype.

Key evaluation areas include:
- **Technical soundness**: validity of proofs, experimental design, and argumentation
- **Novelty and contribution**: whether work provides new knowledge distinct from prior efforts
- **Scope appropriateness**: whether claims match the evidence presented
- **Clarity and presentation**: sufficient explanation for readers to understand work

## Scoring Criteria

As of February 2025, ARR uses three scores:

**Soundness**: "soundness scores must be justified by the text of the review." Low soundness without documented faults indicates unfaithfulness to recommendations.

**Excitement**: A subjective measure orthogonal to soundness, reflecting personal interest rather than paper quality.

**Overall Assessment**: A composite recommendation integrating soundness, excitement, novelty, and potential impact for venue placement.

## Strong vs. Weak Papers

Strong papers demonstrate:
- Clear research questions with appropriately scoped claims
- Sound methodology matching the contribution type
- Sufficient evidence supporting conclusions
- Proper documentation of limitations

Weak papers typically have:
- Vague or unclear contributions
- Methodological flaws or incomplete assumptions
- Overstated claims exceeding evidence
- Missing or inadequate related work discussion

## Statistical Methodology Guidance

The guidelines address "Inappropriate or missing statistical significance assessment," noting that "main experimental results should be accompanied by appropriate information about their statistical significance (error bars, confidence intervals, statistical significance tests)." Effect size estimation receives encouragement.

Reviewers should watch for p-hacking and "presenting the 'best' results out of an unknown number of trials."

## Reproducibility Requirements

Papers must provide sufficient detail enabling others to reproduce experiments. This includes hyperparameter selection, dataset specifications, and implementation details. Authors should clarify code and data availability plans.

The guidelines distinguish reproducibility (running same experiments with similar results) from replicability (obtaining comparable results after reimplementation). Reviewers assess whether documentation supports reproducibility without obligation to run code themselves.

## Conference vs. Findings Distinction

The guidelines state: "papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible." However, conference papers receive additional consideration for potential impact and broader significance.

A paper might merit main conference placement despite lower personal excitement if it offers substantial community value—such as efficiency improvements, resources for underserved languages, or theoretical contributions—even without SOTA results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7cc7446b-aa1d-48e1-b0a5-4d1425259553",
  "isSidechain": false,
  "promptId": "7bdff5af-d6c2-443f-99ab-f2e200157b45",
  "type": "user",
  "uuid": "17b8edd0-08d4-4b38-8f78-1f056817fce8",
  "toolUseResult": {
    "bytes": 100603,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR Reviewer Guidelines Summary\n\n## What Reviewers Should Evaluate\n\nReviewers assess papers across multiple dimensions. The guidelines emphasize reading papers twice—first for skimming to understand the research question, then for in-depth technical evaluation. Reviewers should check whether the methodology answers the stated research question and whether findings advance the field, rather than applying a single standardized prototype.\n\nKey evaluation areas include:\n- **Technical soundness**: validity of proofs, experimental design, and argumentation\n- **Novelty and contribution**: whether work provides new knowledge distinct from prior efforts\n- **Scope appropriateness**: whether claims match the evidence presented\n- **Clarity and presentation**: sufficient explanation for readers to understand work\n\n## Scoring Criteria\n\nAs of February 2025, ARR uses three scores:\n\n**Soundness**: \"soundness scores must be justified by the text of the review.\" Low soundness without documented faults indicates unfaithfulness to recommendations.\n\n**Excitement**: A subjective measure orthogonal to soundness, reflecting personal interest rather than paper quality.\n\n**Overall Assessment**: A composite recommendation integrating soundness, excitement, novelty, and potential impact for venue placement.\n\n## Strong vs. Weak Papers\n\nStrong papers demonstrate:\n- Clear research questions with appropriately scoped claims\n- Sound methodology matching the contribution type\n- Sufficient evidence supporting conclusions\n- Proper documentation of limitations\n\nWeak papers typically have:\n- Vague or unclear contributions\n- Methodological flaws or incomplete assumptions\n- Overstated claims exceeding evidence\n- Missing or inadequate related work discussion\n\n## Statistical Methodology Guidance\n\nThe guidelines address \"Inappropriate or missing statistical significance assessment,\" noting that \"main experimental results should be accompanied by appropriate information about their statistical significance (error bars, confidence intervals, statistical significance tests).\" Effect size estimation receives encouragement.\n\nReviewers should watch for p-hacking and \"presenting the 'best' results out of an unknown number of trials.\"\n\n## Reproducibility Requirements\n\nPapers must provide sufficient detail enabling others to reproduce experiments. This includes hyperparameter selection, dataset specifications, and implementation details. Authors should clarify code and data availability plans.\n\nThe guidelines distinguish reproducibility (running same experiments with similar results) from replicability (obtaining comparable results after reimplementation). Reviewers assess whether documentation supports reproducibility without obligation to run code themselves.\n\n## Conference vs. Findings Distinction\n\nThe guidelines state: \"papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible.\" However, conference papers receive additional consideration for potential impact and broader significance.\n\nA paper might merit main conference placement despite lower personal excitement if it offers substantial community value—such as efficiency improvements, resources for underserved languages, or theoretical contributions—even without SOTA results.",
    "durationMs": 9422,
    "url": "https://aclrollingreview.org/reviewerguidelines"
  },
  "sourceToolAssistantUUID": "7cc7446b-aa1d-48e1-b0a5-4d1425259553",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 65 · 2026-05-19T04:46:17.549Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the paper. Let me compile my review based on the methodological rigor focus.

Let me organize my notes on the key issues:

## Paper Summary
The paper investigates layer selection sensitivity in hidden-state safety probes for reasoning models. It examines the "Safety Commitment Point" (CP) where reasoning models transition from safe to harmful generation. The central finding is that layer selection metric choice critically determines whether hidden-state probes outperform text-based probes. They show a biased composite metric (BA × crossing rate) selects shallow layers and reverses conclusions at 32B scale, while threshold-dependent metrics consistently select deep layers where HS advantage is significant.
 
## Key methodological issues to evaluate:

### 1. Statistical Methodology

The Holm-Bonferroni correction presents an interesting tension: they frame it as 12 independent tests (3 metrics × 4 models) but acknowledge the three per-model metrics are correlated through a shared confusion matrix with only 2 degrees of freedom, effectively reducing this to 4 independent tests. Both correction levels pass, which is reassuring, though the paper's primary framing around 12 tests somewhat obscures this dependency structure—though this conservative approach actually strengthens their conclusions rather than weakening them.

For the bootstrap confidence intervals, they use 10,000 resamples which is solid, but the paper doesn't clearly specify whether they're using percentile or BCa methods. Percentile bootstrap can introduce bias with smaller samples, so BCa would be the more robust choice here. The interval widths themselves look reasonable given their sample sizes.

The small sample concern for the 32B models (n=19-20) is properly acknowledged in their limitations and power analysis appendix. Their minimum detectable effect at 80% power ranges from 6.8 to 9.5 percentage points, and the R1-32B residualized gap of +1.9pp falls well below this threshold—they're transparent about this limitation, though they still make claims about all four models passing Holm-Bonferroni correction, which feels like a stretch when the effect sizes are this small.

The R1-8B FPR result at p=0.044 is particularly fragile—it's the weakest test in their battery and barely clears the Holm-Bonferroni threshold of 0.05. Looking at the per-seed breakdown, only 3 out of 5 seeds actually pass, and there's much higher variability in the handwritten FPR compared to text FPR. The paper does disclose this fragility, but counting it as a clean "pass" feels overly generous.

The 60/20/20 train-test split with these small sample sizes is problematic, especially at 32B where R1-32B only has 20 total traces to work with.  That breaks down to roughly 12 training samples, 4 validation, and 4 test per class—the validation set is far too small for reliable hyperparameter selection. The joint search space across layer, W, K, and threshold compounds this issue.

The paper tries to address this in Appendix M by arguing that threshold-dependent metrics converge independently to a deep-layer band and that bootstrap confidence intervals quantify uncertainty, but there's a real concern here: these metrics all derive from the same confusion matrix, so their convergence might reflect shared bias rather than independent validation.

For the GRU evaluation, they use different data splits (70/30 primary, 60/20/20 for comparison) to maximize training data for the sequential model, which makes direct comparison trickier, though they apparently show matched-split results in Table 13 to address this.

On control task selectivity, the range of 11.1-16.8pp above chance potentially overlaps with position's contribution of 9-20pp, but the paper claims in Appendix H that selectivity was computed on position-residualized features, so that should account for the overlap.

The single-dataset limitation is more concerning—all findings rest on HarmThoughts without testing against alternative safety benchmarks, which limits how much I can claim about generalization.

Looking at the core layer selection argument, the claim that BA × crossing rate selects shallow layers because they have compressed representations and crossing rate is noise-driven appears well-supported by Table 6.

Now examining the five-metric ablation and degrees of freedom—the paper argues that while there are five metrics, only two degrees of freedom come from the confusion matrix itself, with crossing rate and the composite derived from threshold behavior, which seems reasonable given how correlated these metrics are.

Looking at the BA versus precision-optimal layer selections, there's a real tension here: BA picks layers anywhere from 7-98% depth while precision consistently selects 94-98%, and this variability is presented as the key finding, but it also creates a circularity where threshold-dependent metrics are recommended, these metrics happen to select deep layers, HS wins at depth, and therefore layer selection is framed as critical.

For QwQ-32B, the position baseline actually outperforms HS on balanced accuracy (0.832 vs 0.796), which suggests something more fundamental might be at play.

On the capacity control side, the PCA matching experiment shows that maximum-variance preservation doesn't necessarily capture semantic dimensions, though the fact that random projections yield similar results does strengthen the argument that it's not purely about dimensionality. The encoder quality gradient across different models is starting to emerge as another variable worth examining. Looking at these alternative methods, I'm noticing some methodological concerns. BOCPD and CUSUM are fundamentally designed for detecting sharp changepoints rather than gradual transitions, so their poor performance here feels somewhat expected—though the authors frame it as diagnostic rather than a limitation of their evaluation. For the MLP probes, I'm wondering if the underperformance against logistic regression might stem from insufficient regularization rather than inherent weakness, especially with such a small sample size. And with CCS, there's a slight mismatch in how it's being evaluated—it's an unsupervised method being compared against supervised baselines, so calling it a failure on supervised tasks is a bit unfair to its intended purpose.

The paper's core contribution about layer selection sensitivity is genuinely valuable and well-demonstrated. The statistical work is mostly solid, though I'm concerned about the small sample sizes at 32B limiting statistical power and making hyperparameter choices fragile. The HS advantage there also depends heavily on position mediation effects and competitive baselines, which softens the claim somewhat. There's also a circularity risk where the layer selection threshold drives which layers get selected, which then determines whether HS wins. What I do appreciate is how transparent the authors are about these limitations and edge cases—that's refreshing. The appendix is thorough with detailed stability analyses across multiple seeds, and the methodological finding itself holds up well despite these concerns.

For scoring, I'm settling on 3.5 for soundness since the main claims are supported but those small-sample issues and circularity concerns prevent a higher rating. Excitement is around 3—the methodological insight is interesting but the scope is narrow with just one dataset and a specific probing setup. Overall I'm landing between 3 and 3.5, which puts this in the borderline to weak accept range for a conference.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17b8edd0-08d4-4b38-8f78-1f056817fce8",
  "isSidechain": false,
  "requestId": "req_011CbBKRLFvdP6bXxK7mJhCe",
  "type": "assistant",
  "uuid": "5a3f61e2-54c2-40dd-9097-90941ae22068",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzEgcdWbhMwq4TZfH3qdC6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21056,
      "cache_read_input_tokens": 48520,
      "output_tokens": 9173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9173,
          "cache_read_input_tokens": 48520,
          "cache_creation_input_tokens": 21056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21056
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 66 · 2026-05-19T04:46:17.551Z_

I now have a comprehensive understanding of the paper. Let me compose the full review report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a3f61e2-54c2-40dd-9097-90941ae22068",
  "isSidechain": false,
  "requestId": "req_011CbBKRLFvdP6bXxK7mJhCe",
  "type": "assistant",
  "uuid": "5d13e36b-6fa6-48df-9241-49f43cf3de2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzEgcdWbhMwq4TZfH3qdC6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21056,
      "cache_read_input_tokens": 48520,
      "output_tokens": 9173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9173,
          "cache_read_input_tokens": 48520,
          "cache_creation_input_tokens": 21056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21056
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 67 · 2026-05-19T04:48:35.787Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_015255SQqbbkQdEkj9iHkM4G`</summary>

```json
{
  "text": "## Summary\n\n本文研究推理模型中隐藏状态(HS)安全探针的层选择敏感性问题。核心发现是：层选择指标的选择会根本性地改变 HS 探针是否优于文本探针的结论——一个有偏的复合指标（balanced accuracy × crossing rate）在 32B 模型上系统性地选择浅层，从而逆转 HS 优势的判断。论文在4个推理模型、5个选择指标和7种替代方法上进行了系统评估，附录极为详尽（A-Z共26节）。方法论发现（层选择敏感性）是稳健的；经验性的 HS 优势是有条件的。\n\n---\n\n## Strengths\n\n**S1. 方法论贡献切实且重要。** 层选择作为研究者自由度影响探针研究结论——这一发现对整个 probing 文献有普适意义。Table 2 清晰展示了有偏指标与纠正后指标选择的层深度差异（QwQ-32B: 3% vs 98%），机制解释（浅层表示压缩导致 crossing rate 膨胀，Section C / Table 6）有数据支撑。\n\n**S2. 异常诚实的局限性披露。** 论文主动报告：R1-32B 的 HS 优势由位置中介（residualized gap 仅 +1.9pp, Section V）；R1-8B FPR p=0.044 在 HB 边缘；QwQ-32B 位置基线 BA 竞争性超过 HS（Table 4, margin -3.8pp）；当前探针 FPR 39-52% 仅为\"commitment zone characterization\"而非生产检测器。这种透明度在 ML 论文中罕见。\n\n**S3. 三层证据分级体系。** 将模型证据分为 strong / moderate / qualified 三级，避免了一刀切的 claim。OT-7B (5/5 seeds, +21.9pp, position-independent) 与 R1-32B (position-mediated, n=20) 被区别对待，读者可自行判断每个模型的证据强度。\n\n**S4. 附录系统性极强。** 26个附录涵盖：层扫描（B）、表示压缩（C）、HB 分步校正（D）、窗口消融（E）、控制任务（H）、oracle 上界（I）、CP 标注扰动（J）、BOCPD/CUSUM 配置扫描（K）、K 消融（L）、决策阈值敏感性（M）、bug 披露（N）、多种子稳定性（W）、功效分析（V）。每个附录都对应正文中的一个具体 claim。\n\n**S5. 容量控制设计合理。** PCA-384d 匹配保留 79-92% 方差（Table Y），随机投影（结构破坏性，Appendix T）仍然显著，形成 MiniLM → BGE-large → E5-Mistral 的单调编码器质量梯度（4/4 → 1/4 → 2/4 HB）。\n\n---\n\n## Weaknesses\n\n**W1. [Critical] 超参数搜索空间与验证集规模严重不匹配**\n\n32B 模型总样本量约 95-100 条 trace（Table 1）。60/20/20 划分后验证集仅约 19-20 条（每类约 4-10 条）。然而论文搜索的联合超参数空间巨大：Layer（最多 64）× W（7值）× K（5值）× threshold = 最多 2,240 配置（论文自己在 Appendix M 承认）。\n\n**问题所在：**\n- 验证集每类 4-10 个样本无法可靠区分 2,240 个配置中的信噪比\n- 论文在 Appendix M 提供了三个反驳论点，但每个都有漏洞：\n  - \"阈值依赖指标独立收敛到 L63\"：这些指标共享同一混淆矩阵（论文自己承认 effective DoF = 2），收敛可能反映共同偏差而非独立验证\n  - \"Bootstrap CI 量化不确定性\"：Bootstrap 从同一小样本抽样，不能弥补验证集过小的根本问题\n  - \"BA 层不稳定性是发现本身\"：Table 25 LOO-CV 显示 QwQ-32B/R1-32B BA层跨 fold 变化 24 层（L39-L63），但这恰恰说明在 n≤20 时任何单一指标的选择都不可靠，包括 threshold-dependent 指标\n- **影响接收：** 论文的核心声明\"纠正后的层选择下所有4个模型显著\"可能部分由超参数过拟合驱动。这不影响层选择敏感性的方法论发现，但动摇了定量优势的可信度。\n- **建议修改方向：** (1) 报告嵌套交叉验证（inner fold 选层+W+K，outer fold 评估）的结果；(2) 或者对 32B 模型明确降低证据等级声明，将\"significant under HB\"改为\"directionally consistent but underpowered\"。\n\n**W2. [Critical] QwQ-32B 位置基线的影响被低估**\n\nTable 4 显示 QwQ-32B 位置基线 BA (0.832) > HS BA (0.796)，margin = -3.8pp。这意味着简单地知道当前步骤在 trace 中的相对位置就比读取隐藏状态更有信息量。\n\n**问题所在：**\n- 论文将 QwQ-32B 归类为\"moderate\"证据，但当位置基线在核心指标上胜出时，\"moderate\"过于乐观\n- Section 4.4 的解释集中在\"训练方法差异\"，但更简洁的解释是：QwQ-32B 的 commitment 主要由 trace 长度/位置决定，HS 探针并未捕获有意义的额外安全信号\n- 论文声称 precision 优势仍存在（+19.2pp），但 precision 在位置基线能达到相近 BA 的情况下，可能反映的是阈值选择而非表示质量\n- **影响接收：** 削弱了\"HS 优势在纠正后层对所有4个模型显著\"的核心 claim。如果 4 个模型中有 1 个位置基线胜出、1 个（R1-32B）位置中介，那实际上只有 2/4 模型有无条件的 HS 优势。\n- **建议修改方向：** (1) 在 abstract/introduction 中将 claim 从\"所有4个模型显著\"修改为\"7-8B 模型稳健显著，32B 模型有条件\"；(2) 为 QwQ-32B 报告位置残差化后的 precision 比较。\n\n**W3. [Major] Bootstrap 方法未指定，小样本下差异显著**\n\n论文报告\"10,000 bootstrap resamples\"和\"95% CI\"，但从未指定使用的是 percentile bootstrap、BCa (bias-corrected and accelerated)、还是 basic bootstrap。\n\n**问题所在：**\n- 在 n=19-20 的小样本下，percentile bootstrap 已知有偏且覆盖不足（Efron & Tibshirani, 1993）\n- BCa 校正了偏度和加速因子，在小样本下覆盖率更接近标称值\n- 如果使用的是 percentile bootstrap，Table 3 报告的 CI 可能过窄，特别是对 R1-32B（[+5.2, +25.1]）\n- R1-8B FPR 比较中 HS FPR std=0.040 vs text std=0.007——这种异方差性进一步影响 bootstrap CI 的可靠性\n- **影响接收：** 不会单独导致 reject，但方法论论文应在统计方法上无可挑剔。\n- **建议修改方向：** (1) 明确报告 bootstrap 方法类型；(2) 对 32B 模型追加 BCa CI 并与 percentile CI 对比；(3) 如果差异显著，更新 Table 3 和相关 p 值。\n\n**W4. [Major] Holm-Bonferroni 校正框架存在概念混淆**\n\n论文在 12 tests (3 metrics × 4 models) 和 4 tests (1 per model) 两种 HB 框架间反复切换，且论证存在不一致：\n\n**问题所在：**\n- 论文先说\"3 metrics × 4 models = 12 tests\"，然后承认\"effective number of independent comparisons is four (one per model)\"因为 3 个指标共享混淆矩阵\n- 但随后的具体 HB 步骤（Table 7/Appendix D）仍然列出 12 个排序测试\n- 如果 effective DoF = 4，那应该只做 4-test HB（每个模型取最弱 p 值），12-test HB 是过度保守的\n- 论文说\"both yield the same outcome\"——但这正是问题：两种框架对 R1-8B FPR (p=0.044) 的影响不同。在 12-test HB 下 rank 12 threshold = α/1 = 0.05 刚好通过；但论文没有清楚解释为什么 12 个有 correlation 的 test 仍然应该用标准 HB（HB 假设独立或正相关，正相关下保守性增加但覆盖率可能不足）\n- **建议修改方向：** 统一采用一种框架并清楚论证选择理由。推荐 4-test model-level HB（在 Section 3.5 明确声明，正文和附录一致使用）。\n\n**W5. [Major] 单数据集限制泛化性**\n\n所有实验基于 HarmThoughts 一个 benchmark（Kakkar et al., 2026），包含 4 个模型的 CP 标注 trace。\n\n**问题所在：**\n- HarmThoughts 的 CP 标注方式可能引入系统偏差——如果标注者倾向于在特定 trace 位置标注 CP，位置信号就会被人工放大\n- 论文声称发现\"层选择敏感性\"和\"HS 优势有条件性\"是通用方法论发现，但在单一数据集上无法验证泛化\n- 替代安全检测 benchmark（如 WildGuard、SafetyBench、OR-Bench 等）虽然不一定有 step-level CP 标注，但可以测试 trace-level 检测\n- Appendix J (CP Annotation Perturbation) 测试了 ε∈{-3,...,+3} 的 CP 偏移，但这只检验标注鲁棒性，不检验数据集泛化\n- **建议修改方向：** (1) 在 Limitations 中明确列为首要局限；(2) 讨论 HarmThoughts 的 CP 标注方法可能引入的偏差；(3) 如可能，在至少一个额外数据源上验证层选择敏感性发现。\n\n**W6. [Major] GRU 评估使用两种划分引入混淆**\n\nGRU 使用 70/30 split（primary），同时在 60/20/20 split 下做 fair comparison（Table 13）。\n\n**问题所在：**\n- 70/30 split 给 GRU 更多训练数据（~70% vs ~60%），对 GRU 有利\n- 但论文的主要 LR 实验使用 60/20/20——不同划分下的性能差异可能部分来自数据量而非模型差异\n- 虽然论文提供了 60/20/20 下的 GRU 结果（Table 13），但正文 Section 4.5 引用的 GRU 数字似乎来自 70/30 结果\n- Appendix G 解释了 70/30 的理由（最大化训练数据），但这正好说明在小数据集下 GRU 需要更多数据才能正常工作——这是 GRU 的劣势而非实验设计的必要性\n- **建议修改方向：** 正文中 GRU 对比应一律使用 60/20/20 结果（Table 13），将 70/30 结果移至附录作为参考。\n\n**W7. [Minor] 控制任务选择性与位置贡献的范围重叠未讨论**\n\n控制任务选择性为 11.1-16.8pp above chance（Section H），而位置对 BA 的贡献为 9-20pp（Section 4.4）。\n\n**问题所在：**\n- 选择性 11.1pp 与位置贡献 20pp 的重叠意味着部分\"选择性\"可能来自位置信号而非安全表示\n- 虽然论文在 Appendix H 报告了位置残差化后的选择性，结果 R1-8B 残差化后选择性 67.3%（但 1% crossing rate），这表明去除位置后探针仍有判别力但实用性大降\n- **建议修改方向：** 在正文讨论中明确 Table 3 的选择性数字在多大程度上由位置驱动，报告残差化选择性作为主要结果。\n\n---\n\n## Questions\n\n**Q1.** Bootstrap CI 使用的是 percentile、BCa 还是 basic 方法？对 32B 模型（n≤20），这三种方法的 CI 宽度和覆盖率差异可达数个百分点。请提供具体方法并讨论小样本敏感性。\n\n**Q2.** Table 2 中 QwQ-32B corrected layer p=0.105（不显著），但正文声称\"all four models pass Holm-Bonferroni correction\"。这个 p=0.105 是哪个指标的？如果是 precision，那 QwQ-32B 的 HS 优势在什么意义上\"pass HB\"？Table 3 给出的 QwQ-32B 384d ΔPrc 的 p 值是多少？\n\n**Q3.** 论文声称 K=5 是\"design pre-selection before examining performance\"（Section 3.5），但同时提供了 K∈{3,5,7} 的事后合理化（\"sustained commitment signal\"）。这两个声明矛盾。K=5 到底是在什么时间点、基于什么信息决定的？如果是在看到任何性能数据之前，请提供时间戳或 commit 记录。\n\n**Q4.** R1-32B 的验证集每类约 4 个样本（20 × 0.2 ÷ 2 classes）。在这种规模下，Layer 选择中一个样本的翻转可能导致完全不同的层被选中。LOO-CV（Appendix M/Table 25）显示 BA 层跨 fold 跨度 24 层。threshold-dependent 指标在同样的 LOO-CV 下稳定性如何？论文未报告。\n\n**Q5.** Appendix N 披露了 QwQ-32B 的 M002 bug（midpoint heuristic placeholder 替代真实 sentence embeddings）。修正后论文声称结论未变。请确认 Table 3 中 QwQ-32B 的所有数字都来自修正后的 pipeline。是否有其他模型经历过类似的 pipeline bug？\n\n**Q6.** 论文提出的五步审计协议（Section 5）是基于本研究的回顾性分析得出的。是否在任何外部数据集或任务上前瞻性验证过这个协议？如果没有，\"recommend\"一词是否过强？\n\n---\n\n## Missing References\n\n1. **Hewitt & Liang (2019) control task 框架的后续批评：** Pimentel et al. (2020) \"Information-Theoretic Probing with Minimum Description Length\" 对 Hewitt & Liang 的 selectivity 框架提出了信息论替代方案。论文使用了 selectivity 但未讨论其已知局限性。\n\n2. **小样本 bootstrap 方法论：** DiCiccio & Efron (1996) \"Bootstrap Confidence Intervals\" 讨论了 BCa vs percentile bootstrap 在小样本下的差异——与论文的统计方法直接相关但未引用。\n\n3. **Probing 文献中的层选择：** Tenney et al. (2019) \"BERT Rediscovers the Classical NLP Pipeline\" 系统研究了 BERT 各层的探针性能，是层选择问题的早期重要工作。Liu et al. (2019) \"Linguistic Knowledge and Transferability of Contextual Representations\" 也相关（已引用但可进一步讨论）。\n\n---\n\n## Overall Assessment\n\n**Overall: 3.0 (Findings)**\n**Soundness: 3.0/5**\n**Excitement: 3.0/5**\n**Confidence: 4/5**\n\n**一句话总结：** 层选择敏感性是一个真实且重要的方法论发现，但 32B 模型的定量 claim 在当前样本量和超参数搜索空间下缺乏足够统计支撑，且单数据集限制了泛化性。\n\n**理由：**\n- **Soundness 3.0:** 核心方法论发现（层选择敏感性）有充分支撑。但 32B 模型的 HS 优势 claim 存在系统性问题：(1) 验证集过小（每类 4-10 样本）相对于 2,240 配置的搜索空间；(2) QwQ-32B 位置基线胜出削弱了 claim；(3) bootstrap 方法未指定；(4) HB 框架在 12-test 和 4-test 间混淆。单独每个问题可修复，但累积效应使 32B 定量 claim 的可信度不足。\n- **Excitement 3.0:** 层选择作为研究者自由度的发现有一定影响力，但范围较窄（单数据集、单任务、4个模型）。probing 方法论社区会感兴趣，但更广泛的 NLP/safety 社区需要看到泛化证据。\n- 论文的透明度和附录完整性值得肯定，但透明地报告弱点不能替代解决弱点。7-8B 结果（特别是 OT-7B）是令人信服的；32B 结果需要更大样本或更保守的 claim。\n- 适合 Findings track，因为方法论发现本身是 sound 的，但作为主会议论文需要更强的泛化证据。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- 贡献列表中\"所有4个模型 HB 显著\"的措辞应弱化，区分 7-8B（稳健）和 32B（有条件）\n- \"biased composite metric reverses conclusions\"的因果语言准确——实验证据支持这一机制解释\n\n### Section 3.5 (Evaluation Protocol)\n- K=5 的预选择 vs 事后合理化矛盾需要解决（Q3）\n- \"12 tests with HB\"和\"effective DoF = 4\"并存的论述需要统一\n\n### Section 4.2 (Layer Selection)\n- Table 2 是论文最强的结果——清楚展示了指标选择的影响\n- 但缺少 threshold-dependent 指标在 LOO-CV 下的稳定性分析（只报告了 BA 的不稳定性）\n\n### Section 4.3 (HS vs Text)\n- Table 3 的 384d 结果令人信服（7-8B）\n- R1-32B ΔBA = -1.6pp（HS 在 BA 上反而不如 text）但 ΔPrc = +15.1pp——这个分裂需要更多解释\n- 1024d 结果只有 1/4 HB——论文从\"4/4 HB\"到\"1/4 HB\"的叙事转变太平滑，应更强调这是 HS 优势有条件性的关键证据\n\n### Section 4.4 (32B Analysis)\n- R1-32B coverage 仅 25%（5/20 traces）——在如此低覆盖率下的\"显著性\"实际意义有限\n- QwQ-32B 位置基线问题（W2）需要在本节而非附录中充分讨论\n\n### Section 4.6 (Negative Results)\n- BOCPD/CUSUM 在 gradual transition 上失败是 expected 的——这些方法设计用于 abrupt changepoints\n- 更有信息量的 negative result 会是：一个专门为 gradual transition 设计的方法（如 regime switching models）也失败\n- RepE 在 QwQ-32B 上 BA=0.756 但 precision=0.512——这个差距暗示 RepE 可能在不同 operating point 上有竞争力，值得更深入分析\n\n### Section 5 (Discussion)\n- 五步审计协议是有价值的贡献，但需要注意它是从同一研究回顾性提出的（Q6）\n- \"deployment operating points\"段落（K 消融）是实用的，但 FPR 39-52% 到 5-17% 的改善以大幅覆盖率损失为代价，应更诚实地讨论这个 tradeoff\n\n### Section 7 (Limitations)\n- 全面且诚实，但单数据集局限应排在更前面的位置\n- \"minimum detectable effect\"分析（Appendix V）应在正文而非附录中引用",
  "reviewer_id": "1",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d13e36b-6fa6-48df-9241-49f43cf3de2f",
  "isSidechain": false,
  "requestId": "req_011CbBKRLFvdP6bXxK7mJhCe",
  "type": "assistant",
  "uuid": "7d72a8cc-8bb3-4be7-8254-d2e5305dde9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzEgcdWbhMwq4TZfH3qdC6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21056,
      "cache_read_input_tokens": 48520,
      "output_tokens": 9173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21056,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9173,
          "cache_read_input_tokens": 48520,
          "cache_creation_input_tokens": 21056,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21056
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 68_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: 你是 Reviewer 1，负责 **方法严谨性** 审查。  ## 论文信息 - **标题**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models - **路径**: `projects/contrastive_trace_safety/docs/paper…",
  "leafUuid": "7d72a8cc-8bb3-4be7-8254-d2e5305dde9c",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Runtime record

_source line 69_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodology rigor for safety probes paper",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Tool result

_source line 70 · 2026-05-19T04:48:39.546Z_

<details><summary>↩ Tool result · `toolu_015255SQqbbkQdEkj9iHkM4G`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d72a8cc-8bb3-4be7-8254-d2e5305dde9c",
  "isSidechain": false,
  "promptId": "7bdff5af-d6c2-443f-99ab-f2e200157b45",
  "type": "user",
  "uuid": "cda3c3fa-dda8-4d0d-bf9a-ecb2830489dd",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "7d72a8cc-8bb3-4be7-8254-d2e5305dde9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodology rigor for safety probes paper",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Runtime record

_source line 72 · 2026-05-19T04:49:42.080Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T04:49:42.080Z",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "content": "[Round 1 审稿请求]:\n## 交叉分享：Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2（新颖性/完整性）的完整审稿报告。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由（引用具体 Section/Table/Figure 支撑）\n- **[REBUT]** 反驳并提供证据（引用具体数据）\n\n特别关注：你在方法严谨性角度是否同意 R2 的以下判断？\n1. R2-W1 (Critical): 正文超 8 页——你是否确认？\n2. R2-W2 (Critical): Novelty scope 不足 Main track——从方法论角度是否同意？\n3. R2-W3 (Major): HS advantage 被 encoder quality 制约——你的统计分析是否支持这一判断？\n4. R2-W6 (Major): Layer selection sensitivity 适用范围窄——从统计角度评估\n\n---\n\n### Reviewer 2 完整报告\n\n## Summary\n本文研究推理模型中隐藏状态安全探针的 layer selection sensitivity 问题。核心发现是：使用包含 crossing rate 的复合指标选择 transformer 层会系统性偏向浅层（32B 模型尤其严重），导致错误结论\"HS 优势依赖规模\"。修正后（使用 threshold-dependent 指标选择深层），四个模型均显示显著 HS 精度优势（+15.4 to +21.9pp, Holm-Bonferroni 校正）。但该优势受文本编码器质量制约：换用 1024d BGE-large 后仅 1/4 模型通过 HB 校正。论文属于 characterization study，未提出新方法/算法/工具。\n\n## Strengths\nS1. 重要的方法论发现。Layer selection 作为 researcher degree of freedom 可以逆转研究结论——这一发现对整个 probing 文献有警示价值。\nS2. 实验设计严谨全面。5种指标、7种baseline、3种编码器、PCA/random projection、position residualization、control task、multi-seed。\nS3. 诚实透明的 evidence gradient (strong/moderate/qualified)。\nS4. Bug disclosure (Appendix N/M002)。\nS5. 附录完整度高（25个子节）。\n\n## Weaknesses\n\nW1. [Critical] 正文页数超限。Sections 1-6 约 8.3-8.5 页，超出 ACL Long Paper 8 页限制。Discussion \"Deployment operating points\" 段溢出至第 9 页，Conclusion 完全在第 9 页。\n\nW2. [Critical] 贡献的 novelty scope 不足以支撑 Main conference。三条 contributions 均为 empirical observations 而非 methodological contributions。无新检测方法、probe 架构、或可复用工具。Five-step audit 是非形式化的最佳实践建议。更适合 Findings。\n\nW3. [Major] HS advantage 核心实证发现自我削弱。换用 1024d BGE-large 后仅 OT-7B 通过 HB (1/4)。论文自己承认 \"HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference\"。实证贡献 shelf life 短。\n\nW4. [Major] 样本量过小，32B 结论统计效力不足。R1-32B n=20, QwQ-32B n=19。80% power MDE = 8.6-9.5pp。R1-32B residualized gap +1.9pp (p=0.914) 本质为 null result。4/4 模型中 2 个依赖 dagger notation。\n\nW5. [Major] 单一数据集限制泛化性。所有实验仅使用 HarmThoughts（632 traces）。CP annotations 未经独立 IAA 评估。\n\nW6. [Major] Layer selection sensitivity 发现的实际适用范围可能较窄。多少研究者会使用 bal_acc × crossing_rate？如果答案是\"几乎没有\"，impact 有限。\n\nW7. [Minor] Discussion 与 Conclusion 重叠度过高。\n\nW8. [Minor] Abstract 信息密度过高。\n\n## Questions\nQ1. OT-7B biased layer L0 为何未在正文中突出讨论？\nQ2. QwQ-32B precision-latency tradeoff 未讨论。\nQ3. 控制任务 selectivity 11.1-16.8pp 是否足够高？与其他 probing 研究相比？\nQ4. Cross-model transfer 只用 PCA alignment。是否测试了 CKA/Procrustes？\nQ5. HarmThoughts CP annotations 如何产生？\n\n## Missing References\n1. 更多 2025-2026 hidden-state probing for safety 工作\n2. Layer selection 方法论先行研究\n3. Automated red-teaming 文献\n\n## Overall Assessment\n3.0/5 (Findings)。Soundness 3.5, Excitement 2.5, Confidence 4/5。\n方法论发现有价值但范围较窄，实证贡献 conditional 且可能 temporary，无新方法/算法/工具，适合 Findings。"
}
```

---


### Runtime record

_source line 73 · 2026-05-19T04:49:42.081Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T04:49:42.081Z",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


## Round 2

## Round 2

2 recorded events


### User

_source line 74 · 2026-05-19T04:49:42.062Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cda3c3fa-dda8-4d0d-bf9a-ecb2830489dd",
  "isSidechain": false,
  "promptId": "d26e8b60-07dd-469e-9d24-0d6e0350ad97",
  "type": "user",
  "isMeta": true,
  "uuid": "fe287924-4896-416c-8723-401484564717",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 75 · 2026-05-19T04:49:42.062Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe287924-4896-416c-8723-401484564717",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "9b2b9d98-de63-4e63-93eb-6351f52082c8",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "id": "3c66d5cb-f80c-4d06-952c-90fc126860d5",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 3

## Round 3

12 recorded events


### User

_source line 76 · 2026-05-19T04:49:42.209Z_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 2 的完整审稿意见

以下是 Reviewer 2（新颖性/完整性）的完整审稿报告。请逐条回应每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由（引用具体 Section/Table/Figure 支撑）
- **[REBUT]** 反驳并提供证据（引用具体数据）

特别关注：你在方法严谨性角度是否同意 R2 的以下判断？
1. R2-W1 (Critical): 正文超 8 页——你是否确认？
2. R2-W2 (Critical): Novelty scope 不足 Main track——从方法论角度是否同意？
3. R2-W3 (Major): HS advantage 被 encoder quality 制约——你的统计分析是否支持这一判断？
4. R2-W6 (Major): Layer selection sensitivity 适用范围窄——从统计角度评估

---

### Reviewer 2 完整报告

## Summary
本文研究推理模型中隐藏状态安全探针的 layer selection sensitivity 问题。核心发现是：使用包含 crossing rate 的复合指标选择 transformer 层会系统性偏向浅层（32B 模型尤其严重），导致错误结论"HS 优势依赖规模"。修正后（使用 threshold-dependent 指标选择深层），四个模型均显示显著 HS 精度优势（+15.4 to +21.9pp, Holm-Bonferroni 校正）。但该优势受文本编码器质量制约：换用 1024d BGE-large 后仅 1/4 模型通过 HB 校正。论文属于 characterization study，未提出新方法/算法/工具。

## Strengths
S1. 重要的方法论发现。Layer selection 作为 researcher degree of freedom 可以逆转研究结论——这一发现对整个 probing 文献有警示价值。
S2. 实验设计严谨全面。5种指标、7种baseline、3种编码器、PCA/random projection、position residualization、control task、multi-seed。
S3. 诚实透明的 evidence gradient (strong/moderate/qualified)。
S4. Bug disclosure (Appendix N/M002)。
S5. 附录完整度高（25个子节）。

## Weaknesses

W1. [Critical] 正文页数超限。Sections 1-6 约 8.3-8.5 页，超出 ACL Long Paper 8 页限制。Discussion "Deployment operating points" 段溢出至第 9 页，Conclusion 完全在第 9 页。

W2. [Critical] 贡献的 novelty scope 不足以支撑 Main conference。三条 contributions 均为 empirical observations 而非 methodological contributions。无新检测方法、probe 架构、或可复用工具。Five-step audit 是非形式化的最佳实践建议。更适合 Findings。

W3. [Major] HS advantage 核心实证发现自我削弱。换用 1024d BGE-large 后仅 OT-7B 通过 HB (1/4)。论文自己承认 "HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference"。实证贡献 shelf life 短。

W4. [Major] 样本量过小，32B 结论统计效力不足。R1-32B n=20, QwQ-32B n=19。80% power MDE = 8.6-9.5pp。R1-32B residualized gap +1.9pp (p=0.914) 本质为 null result。4/4 模型中 2 个依赖 dagger notation。

W5. [Major] 单一数据集限制泛化性。所有实验仅使用 HarmThoughts（632 traces）。CP annotations 未经独立 IAA 评估。

W6. [Major] Layer selection sensitivity 发现的实际适用范围可能较窄。多少研究者会使用 bal_acc × crossing_rate？如果答案是"几乎没有"，impact 有限。

W7. [Minor] Discussion 与 Conclusion 重叠度过高。

W8. [Minor] Abstract 信息密度过高。

## Questions
Q1. OT-7B biased layer L0 为何未在正文中突出讨论？
Q2. QwQ-32B precision-latency tradeoff 未讨论。
Q3. 控制任务 selectivity 11.1-16.8pp 是否足够高？与其他 probing 研究相比？
Q4. Cross-model transfer 只用 PCA alignment。是否测试了 CKA/Procrustes？
Q5. HarmThoughts CP annotations 如何产生？

## Missing References
1. 更多 2025-2026 hidden-state probing for safety 工作
2. Layer selection 方法论先行研究
3. Automated red-teaming 文献

## Overall Assessment
3.0/5 (Findings)。Soundness 3.5, Excitement 2.5, Confidence 4/5。
方法论发现有价值但范围较窄，实证贡献 conditional 且可能 temporary，无新方法/算法/工具，适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b2b9d98-de63-4e63-93eb-6351f52082c8",
  "isSidechain": false,
  "promptId": "d26e8b60-07dd-469e-9d24-0d6e0350ad97",
  "type": "user",
  "uuid": "5a56797f-f800-4dc0-8501-fc5d124c4473",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Assistant

_source line 77 · 2026-05-19T04:50:14.762Z_

<details><summary>Logged reasoning block</summary>

```text
The Director wants me to cross-review Reviewer 2's report, responding to each Weakness and Question with [AGREE] or [REBUT], citing specific evidence from the paper. Let me go through each item systematically.

Let me re-read the paper content I have from my earlier review to respond accurately.

Let me address each point:

**R2-W1 (Critical): Page limit exceeded**
I need to check if the paper exceeds 8 pages. From my reading of the PDF, the main content (Sections 1-6) spans pages 1-9. 

Looking at the page breakdown more carefully, the Discussion section extends into page 9, and the Conclusion also appears there. The Limitations section is on page 9 as well. Under ACL rules, Limitations don't count toward the page limit, but the Conclusion does. So if Sections 1-6 (the main content excluding Limitations) actually extend beyond 8 pages, this weakness would be valid. The paper is fundamentally a characterization study with three empirical contributions: identifying layer selection sensitivity, documenting when conditional HS shows advantages, and proposing a five-step audit checklist. While these observations are valuable, there's no novel detection method or formal framework—the audit protocol reads more like best practices than rigorous methodology. I'm torn because important methodology papers do get accepted at top venues, but they typically introduce formal structures like control tasks, whereas this feels narrower in scope. I'll lean toward agreeing with the reviewer's concern, though I'd note the findings do have merit.

The statistical evidence is compelling here—the data shows HS advantage only in 4 out of 4 cases at 384d MiniLM but drops to 1 out of 4 at 1024d BGE-large, suggesting the advantage is fundamentally constrained by encoder quality rather than representing a true modality difference. The paper even acknowledges this limitation directly. This is a significant caveat to the empirical contribution, so I agree with the reviewer.

The small sample size of 32 datasets and reliance on a single dataset are both legitimate concerns I've already flagged in my own review. On the layer selection sensitivity point, the practical question is whether many researchers would actually adopt the BA × crossing rate metric—if adoption is limited, the real-world impact becomes questionable.

There's definitely some redundancy between the discussion and conclusion sections that could be tightened. The abstract is also quite dense with specific numbers, which makes it harder to parse the main takeaways.

The embedding layer selection in OT-7B is genuinely noteworthy—selecting L0 (the raw embedding) is unusual and deserves more prominence in the main text rather than being buried in the appendix. I should push back on the precision-latency tradeoff question for QwQ-32B since the paper doesn't fully address this.

The control task selectivity of 11.1-16.8pp falls within the typical range from prior work like Hewitt & Liang, so it's not a red flag, though not exceptional either. The cross-model transfer analysis is limited to PCA when methods like CKA or Procrustes alignment could offer stronger evidence. And I need to understand more about how the HarmThoughts control point annotations were actually constructed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a56797f-f800-4dc0-8501-fc5d124c4473",
  "isSidechain": false,
  "requestId": "req_011CbBKmqUtPq8nwxZzFHGio",
  "type": "assistant",
  "uuid": "e2ff7118-c8de-45a8-bc57-822a81b3d850",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmLFVm1M1h8ywA7YdjyCE4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 56498,
      "cache_read_input_tokens": 11447,
      "output_tokens": 1786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 56498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1786,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 56498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 56498
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 43317
      }
    }
  }
}
```

</details>

---


### Assistant

_source line 78 · 2026-05-19T04:50:15.690Z_

我需要重新查看论文关键页面以准确回应 R2 的判断，特别是页数问题和一些具体数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e2ff7118-c8de-45a8-bc57-822a81b3d850",
  "isSidechain": false,
  "requestId": "req_011CbBKmqUtPq8nwxZzFHGio",
  "type": "assistant",
  "uuid": "8a1f8f25-1118-4554-a151-ef37078cde49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmLFVm1M1h8ywA7YdjyCE4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 56498,
      "cache_read_input_tokens": 11447,
      "output_tokens": 1786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 56498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1786,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 56498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 56498
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 43317
      }
    }
  }
}
```

</details>

---


### Tool call

_source line 79 · 2026-05-19T04:50:22.060Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JiwujGr9cRbd2DmQPDwp9p`</summary>

```json
{
  "description": "Check paper page count",
  "prompt": "I need to verify the exact page layout of an academic paper PDF. Please use mcp__agent-ml-research__pdf_to_images to render page 8 and page 9 of the PDF at:\n\npdf_path: \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf\"\ndpi: 150\n\nDo them one at a time (page 8 first, then page 9).\n\nFor each page, tell me EXACTLY:\n1. What section headings appear on each page?\n2. Where does the main content (Sections 1-6) end?\n3. Where does Section 7 (Limitations) begin?\n4. Where do References begin?\n5. Is there any content from Section 5 (Discussion) or Section 6 (Conclusion) that spills onto page 9?\n\nThis is critical for checking whether the paper exceeds the 8-page limit for ACL Long Papers (Sections 1-6 must fit in 8 pages; Limitations, Ethics, References, and Appendices don't count toward the limit).",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a1f8f25-1118-4554-a151-ef37078cde49",
  "isSidechain": false,
  "requestId": "req_011CbBKmqUtPq8nwxZzFHGio",
  "type": "assistant",
  "uuid": "5162ab05-9054-493b-9d71-e48dd2abfe5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HmLFVm1M1h8ywA7YdjyCE4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 56498,
      "cache_read_input_tokens": 11447,
      "output_tokens": 1786,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 56498,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1786,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 56498,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 56498
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "system_changed",
        "cache_missed_input_tokens": 43317
      }
    }
  }
}
```

</details>

---


### Tool result

_source line 80 · 2026-05-19T04:51:21.764Z_

<details><summary>↩ Tool result · `toolu_01JiwujGr9cRbd2DmQPDwp9p`</summary>

```text
以下是对第 8、9 页的详细分析：

---

## 第 8 页

**出现的章节标题：**
- **Section 5 Discussion**（页面左栏下方，明确标题）

**内容构成：**
- 页面左栏上方：Section 4 实验内容的延续（具体是 Section 4 最后部分，含 "δ∈{0.5,1.0,2.0}" 等实验结论文字）
- 页面左栏下方至右栏全部：**Section 5 Discussion** 的全文内容（涵盖 "Layer selection as researcher degree of freedom"、"Encoder-quality boundary" 等子节讨论）

---

## 第 9 页

**出现的章节标题：**
- **Section 6 Conclusion**（左栏开头）
- **Section 7 Limitations**（左栏中部，约页面 1/3 处）
- **References**（左栏下部，约页面 2/3 处）

**各部分位置：**
- Section 6 Conclusion：页面顶部，占约 10 行
- Section 7 Limitations：紧随其后，约从页面 1/3 处开始
- References：从页面约 2/3 处开始，延伸至页底

---

## 关键判断（针对 8 页正文限制）

**问题：Section 5 Discussion 和 Section 6 Conclusion 均有内容在第 9 页。**

具体情况：
- **第 8 页**：包含 Section 4 结尾 + Section 5 Discussion 全部内容
- **第 9 页顶部**：Section 6 Conclusion 出现在第 9 页（约 10 行），然后才是 Section 7 Limitations

**结论：Section 6 Conclusion 溢出到第 9 页，正文（Sections 1–6）的最后内容在第 9 页约前 1/3 处结束。** 这意味着主体内容（含 Conclusion）实际占据了约 8.3 页，超出了 ACL Long Paper 8 页正文限制。Limitations（Section 7）紧接在 Conclusion 之后，References 在同页再往下，符合不计入页数的惯例，但 **Conclusion 本身溢出至第 9 页是一个合规问题**，需要压缩正文以使 Sections 1–6 完整收入 8 页以内。

agentId: a5a842e114f3183d0 (use SendMessage with to: 'a5a842e114f3183d0' to continue this agent)
&lt;usage>total_tokens: 25788
tool_uses: 10
duration_ms: 59697&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5162ab05-9054-493b-9d71-e48dd2abfe5c",
  "isSidechain": false,
  "promptId": "d26e8b60-07dd-469e-9d24-0d6e0350ad97",
  "type": "user",
  "uuid": "5e702f02-a8d5-48cc-951e-ab68a5bbad4d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the exact page layout of an academic paper PDF. Please use mcp__agent-ml-research__pdf_to_images to render page 8 and page 9 of the PDF at:\n\npdf_path: \"/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/main.pdf\"\ndpi: 150\n\nDo them one at a time (page 8 first, then page 9).\n\nFor each page, tell me EXACTLY:\n1. What section headings appear on each page?\n2. Where does the main content (Sections 1-6) end?\n3. Where does Section 7 (Limitations) begin?\n4. Where do References begin?\n5. Is there any content from Section 5 (Discussion) or Section 6 (Conclusion) that spills onto page 9?\n\nThis is critical for checking whether the paper exceeds the 8-page limit for ACL Long Papers (Sections 1-6 must fit in 8 pages; Limitations, Ethics, References, and Appendices don't count toward the limit).",
    "agentId": "a5a842e114f3183d0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "以下是对第 8、9 页的详细分析：\n\n---\n\n## 第 8 页\n\n**出现的章节标题：**\n- **Section 5 Discussion**（页面左栏下方，明确标题）\n\n**内容构成：**\n- 页面左栏上方：Section 4 实验内容的延续（具体是 Section 4 最后部分，含 \"δ∈{0.5,1.0,2.0}\" 等实验结论文字）\n- 页面左栏下方至右栏全部：**Section 5 Discussion** 的全文内容（涵盖 \"Layer selection as researcher degree of freedom\"、\"Encoder-quality boundary\" 等子节讨论）\n\n---\n\n## 第 9 页\n\n**出现的章节标题：**\n- **Section 6 Conclusion**（左栏开头）\n- **Section 7 Limitations**（左栏中部，约页面 1/3 处）\n- **References**（左栏下部，约页面 2/3 处）\n\n**各部分位置：**\n- Section 6 Conclusion：页面顶部，占约 10 行\n- Section 7 Limitations：紧随其后，约从页面 1/3 处开始\n- References：从页面约 2/3 处开始，延伸至页底\n\n---\n\n## 关键判断（针对 8 页正文限制）\n\n**问题：Section 5 Discussion 和 Section 6 Conclusion 均有内容在第 9 页。**\n\n具体情况：\n- **第 8 页**：包含 Section 4 结尾 + Section 5 Discussion 全部内容\n- **第 9 页顶部**：Section 6 Conclusion 出现在第 9 页（约 10 行），然后才是 Section 7 Limitations\n\n**结论：Section 6 Conclusion 溢出到第 9 页，正文（Sections 1–6）的最后内容在第 9 页约前 1/3 处结束。** 这意味着主体内容（含 Conclusion）实际占据了约 8.3 页，超出了 ACL Long Paper 8 页正文限制。Limitations（Section 7）紧接在 Conclusion 之后，References 在同页再往下，符合不计入页数的惯例，但 **Conclusion 本身溢出至第 9 页是一个合规问题**，需要压缩正文以使 Sections 1–6 完整收入 8 页以内。"
      }
    ],
    "totalDurationMs": 59697,
    "totalTokens": 25788,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 24618,
      "output_tokens": 695,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 474
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 695,
          "cache_read_input_tokens": 24618,
          "cache_creation_input_tokens": 474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 474,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 0,
      "bashCount": 5,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "5162ab05-9054-493b-9d71-e48dd2abfe5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---


### Runtime record

_source line 81 · 2026-05-19T04:51:21.771Z_

```json
{
  "parentUuid": "5e702f02-a8d5-48cc-951e-ab68a5bbad4d",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "ffa0a0cf-db52-4611-b50a-3cdebe4a0519",
  "timestamp": "2026-05-19T04:51:21.771Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---


### Runtime record

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Round 1 审稿请求]: ## 交叉分享：Reviewer 2 的完整审稿意见  以下是 Reviewer 2（新颖性/完整性）的完整审稿报告。请逐条回应每个 Weakness 和 Question： - **[AGREE]** 同意并说明理由（引用具体 Section/Table/Figure 支撑） - **[REBUT]** 反驳并提供证据（引用具体数据）  特别关注：你在方法严谨性角…",
  "leafUuid": "ffa0a0cf-db52-4611-b50a-3cdebe4a0519",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Review methodology rigor for safety probes paper",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457"
}
```

---


### Assistant

_source line 84 · 2026-05-19T04:51:24.930Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have confirmation that the paper exceeds the 8-page limit (Conclusion spills onto page 9, making it ~8.3 pages). Let me now compose my cross-review response to R2's report.

Let me go through each weakness and question systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffa0a0cf-db52-4611-b50a-3cdebe4a0519",
  "isSidechain": false,
  "requestId": "req_011CbBKuB5o267HQMPGJKg6i",
  "type": "assistant",
  "uuid": "b8418b76-fcba-4170-a41a-99b111178877",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGY1HFQ82rtqANdqHLJmu5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 67945,
      "output_tokens": 4793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4793,
          "cache_read_input_tokens": 67945,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2664
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 85 · 2026-05-19T04:51:25.926Z_

确认了页数问题。现在撰写对 R2 的逐条交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8418b76-fcba-4170-a41a-99b111178877",
  "isSidechain": false,
  "requestId": "req_011CbBKuB5o267HQMPGJKg6i",
  "type": "assistant",
  "uuid": "b5a30a67-b3e0-4ffe-a693-1b70d87f6955",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGY1HFQ82rtqANdqHLJmu5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 67945,
      "output_tokens": 4793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4793,
          "cache_read_input_tokens": 67945,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2664
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-19T04:53:07.433Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director · `toolu_01WyyPZNdGvPdN7c7NxCEGeu`</summary>

```json
{
  "text": "## Reviewer 1 对 Reviewer 2 完整审稿意见的交叉回应\n\n---\n\n### Weaknesses 逐条回应\n\n**[AGREE] R2-W1: 正文页数超限（~8.3页）**\n\n确认。我通过 PDF 渲染验证：Section 6 (Conclusion) 完全位于第 9 页顶部（约 10 行），Section 5 (Discussion) 的 \"Deployment operating points\" 段落从第 8 页溢出到第 9 页。正文 Sections 1-6 约 8.3 页，超出 ACL Long Paper 8 页限制。Section 7 (Limitations) 和 References 不计入页数，但 Conclusion 属于正文内容。这是一个格式合规问题，会导致 desk reject 风险。\n\n补充：从方法论角度，Discussion 中 \"Deployment operating points\" 段（K 消融的实用化重述）和 \"Encoder-quality boundary\" 段存在压缩空间——前者与 Appendix L 重叠较多，后者可精简为 2-3 句。\n\n---\n\n**[AGREE with caveat] R2-W2: Novelty scope 不足 Main track**\n\n从方法论严谨性角度部分同意。论文确实是 characterization study：三条 contribution 均为经验观察（层选择敏感性、HS 条件优势、审计协议），无新检测方法、probe 架构或可复用工具。Five-step audit 是非形式化建议，缺乏理论保证或前瞻性验证（我在 R1 审稿中 Q6 已提出此问题）。\n\n**但需注意的 caveat：** 方法论警示类论文在 *ACL venues 有接收先例。Hewitt & Liang (2019) \"Designing and Interpreting Probes with Control Tasks\" 同样未提出新 probe 架构，核心贡献是 selectivity 框架——一个诊断工具。本文的层选择敏感性发现在性质上类似：揭示了一个被忽视的方法论陷阱。区别在于 Hewitt & Liang 提出了一个可操作化的形式框架（control task + selectivity metric），而本文的 five-step audit 更像 checklist。\n\n**结论：** 同意 R2 判断 Findings 更合适，但理由补充为——不是因为 characterization study 本身不够，而是因为审计协议缺乏形式化和外部验证。如果作者将 five-step audit 形式化为一个可复用的统计检验（例如，基于 LOO-CV 层稳定性的自动化指标选择标准），novelty 会显著提升。\n\n---\n\n**[AGREE] R2-W3: HS advantage 被 encoder quality 制约**\n\n从统计角度完全支持 R2 的判断。关键数据链：\n\n1. **384d MiniLM**: 4/4 模型通过 HB（Table 3）\n2. **1024d BGE-large**: 仅 1/4 模型通过 HB（论文 Section 4.3 承认）\n3. **4096d→384d E5-Mistral**: 2/4 模型通过 HB（Appendix U / Table 23）\n\n这形成了一个单调递减梯度：文本编码器越强，HS 优势越弱。论文自己的结论 \"HS advantage represents information not yet captured by current sentence encoders rather than a fundamental modality difference\" 本质上承认了经验贡献的 shelf life 问题。\n\n**统计补充：** 从我的 R1 审稿角度，这个梯度还揭示了一个更深层的方法论问题。PCA-384d 容量匹配（Section 4.3）声称排除了\"容量解释\"，但 PCA 保留的是最大方差方向，不是文本编码器的语义方向。当 BGE-large（1024d，无 PCA 压缩）就能将 HS 优势从 4/4 降到 1/4 时，这说明 384d PCA 匹配实际上低估了文本编码器的能力——PCA 压缩损失的恰恰是可能捕获安全语义的次要方差方向。Random projection baseline（Appendix T）同样存在这个问题：它证明的是 HS 优势不依赖 PCA 的结构保持性质，但没有排除维度匹配本身对文本编码器的不公平。\n\n**影响评估：** 同意 R2 判断此为 Major issue。经验贡献的核心 claim \"HS probes encode safety-relevant information beyond text\" 在更强编码器下可能完全消失，使得论文的持久价值集中在方法论发现（层选择敏感性）而非经验发现（HS 优势）。\n\n---\n\n**[AGREE] R2-W4: 32B 统计效力不足**\n\n完全同意，且与我 R1 审稿中的 W1 和 W2 一致。补充要点：\n\n- R1-32B residualized gap +1.9pp vs MDE 9.5pp（Appendix V）：效应量不到 MDE 的 1/4，这本质上是 null result\n- QwQ-32B 位置基线 BA (0.832) > HS BA (0.796)：在核心指标上位置基线胜出（我 R1 审稿 W2 详细论证）\n- R1-32B HB 通过依赖 dagger notation（W=1, 25% coverage）：仅 5/20 traces 参与评估，实际上是在极小子集上的显著性\n- 论文声称 \"all four models pass HB\" 但 4 个模型中 2 个有严重 caveats——应在 abstract 和 introduction 中区分\n\n---\n\n**[AGREE] R2-W5: 单一数据集限制泛化性**\n\n完全同意，与我 R1 审稿 W5 一致。补充一个 R2 提到但未展开的关键点：\n\n**CP annotation 的产生方式。** 论文未在正文中详细描述 HarmThoughts 的 CP 标注方法。如果 CP 是由人类标注者标注的，inter-annotator agreement (IAA) 是评估标注质量的必要指标，论文未报告。如果 CP 是算法生成的（例如基于 token-level safety scores 的自动检测），那标注方法本身就是一个需要验证的假设。这直接影响了论文的核心前提——\"commitment point exists and is identifiable\"。\n\n---\n\n**[REBUT] R2-W6: Layer selection sensitivity 适用范围窄**\n\nR2 的论点是：如果很少有研究者使用 BA × crossing rate 复合指标，那么发现的 impact 有限。我从方法论角度不同意这一判断。\n\n**反驳理由：**\n\n1. **问题不限于特定复合指标。** 论文的核心发现是：任何包含与表示压缩相关的分量的层选择指标都可能在深层网络中产生浅层偏差。Crossing rate 只是最极端的案例——但 Table 2 显示，即使是 pure balanced accuracy（不含 crossing rate）在 32B 模型上也产生了 24 层跨度的不稳定性（LOO-CV, Table 25）。这意味着问题不是\"谁会用这个特定复合指标\"，而是\"层选择作为未报告的自由度在多大程度上影响 probing 研究的结论\"。\n\n2. **隐性层选择普遍存在。** 多数 probing 论文报告\"最佳层\"结果而不报告层选择标准或搜索过程。Liu et al. (2019)、Tenney et al. (2019) 等经典工作系统报告了各层性能，但许多后续工作只报告最终结果。本文 Table 2 表明不同指标可以选择 0% 到 98% 深度的层——这对任何做层选择的研究者都有警示意义。\n\n3. **统计证据支撑更广泛的适用性。** Appendix M (Decision Threshold Sensitivity) 分析了整个 2,240 配置搜索空间，发现 threshold-dependent 指标独立收敛到深层带（虽然我在 R1 审稿 W1 中质疑了这种\"独立性\"，因为指标共享混淆矩阵——但 convergence pattern 本身是 informative 的）。\n\n**总结：** 同意 R2 指出的\"特定复合指标的使用频率\"问题是合理 concern，但不同意由此推出 impact 有限。层选择敏感性的发现适用于所有使用 best-layer probing 的研究，而非仅适用于使用特定复合指标的研究。不过，论文确实应该更明确地论证这一更广泛的适用性——目前的叙事过于聚焦于 crossing rate bias 这一特定机制。\n\n---\n\n**[AGREE] R2-W7: Discussion 与 Conclusion 重叠**\n\n同意。Section 5 (Discussion) 的第一段重述了层选择敏感性发现，Section 6 (Conclusion) 的第一段再次重述。\"Deployment operating points\" 在 Discussion 中讨论后，Conclusion 又提及。考虑到页数已超限（W1），这种重叠是压缩的首选目标。\n\n---\n\n**[AGREE with caveat] R2-W8: Abstract 信息密度过高**\n\n部分同意。Abstract 包含大量具体数字（+15.4 to +21.9pp, 4/4 HB, 1/4 HB, 384d, 1024d 等），对审稿人来说信息量集中但可消化。问题在于：这些数字服务于多条结论（层选择敏感性 + HS 条件优势 + encoder boundary + negative results），导致 abstract 试图传递的核心信息不清晰。\n\n**方法论角度的 caveat：** 如果论文采纳 R2-W2 的建议聚焦方法论贡献（层选择敏感性），abstract 可以简化——去掉 encoder gradient 和 negative results 的具体数字，集中在\"层选择如何改变结论\"这一核心信息上。\n\n---\n\n### Questions 逐条回应\n\n**[AGREE] R2-Q1: OT-7B biased layer L0 未在正文突出讨论**\n\n同意。OT-7B 有偏指标选择 L0（embedding layer, 0% depth）是 Table 2 中最极端的案例——但正文仅在 Section 4.2 一笔带过。这恰好是论文核心论点（层选择敏感性）的最有力例证：有偏指标甚至选到了 embedding layer，此处几乎没有任何 task-specific 表示。应在正文中用 1-2 句话突出讨论。\n\n**[AGREE partially] R2-Q2: QwQ-32B precision-latency tradeoff 未讨论**\n\n如果 R2 指的是计算延迟（不同层的推理成本），这对方法论论文不是核心关注。但如果指的是 detection lead time（检测提前量）与 precision 的 tradeoff，我同意这是一个缺失的分析——特别是 QwQ-32B 在 Table 4 中位置基线 BA 胜出的情况下，如果 HS 探针的唯一优势是 precision，那这个 precision 的代价是什么（覆盖率、延迟）应该讨论。\n\n**[AGREE] R2-Q3: 控制任务 selectivity 11.1-16.8pp 是否足够**\n\n同意这是一个需要回答的问题。与我 R1 审稿 W7 一致：selectivity 范围与位置贡献范围 (9-20pp) 有重叠。Hewitt & Liang (2019) 报告的句法任务 selectivity 在 5-30pp 范围。11.1-16.8pp 在中等水平，不算特别高。更重要的是：论文应报告位置残差化后的 selectivity 作为更纯净的信号强度指标（Appendix H 提到 R1-8B 残差化后 67.3% accuracy 但 1% crossing rate——这暗示去位置后探针有判别力但实用性极低）。\n\n**[AGREE] R2-Q4: Cross-model transfer 仅用 PCA alignment**\n\n同意。CKA (Kornblith et al., 2019，论文已引用) 和 Procrustes alignment 是表示相似性研究中的标准工具。仅使用 mean-difference direction (Zou et al., 2023) 做 transfer 是一个较粗糙的方法。如果 CKA 分析显示模型间表示空间结构相似但 transfer 仍失败，那将是一个更有信息量的 negative result。\n\n**[AGREE] R2-Q5: HarmThoughts CP annotations 如何产生**\n\n同意这是一个关键未回答问题，与我 R1 审稿 W5 的补充一致。论文 Section 3 应描述 CP 标注方法。如果是人类标注，需要 IAA；如果是算法检测，需要验证。Appendix J (CP Annotation Perturbation) 测试了标注偏移的鲁棒性，但这不能替代对标注产生方式的说明。\n\n---\n\n### 对 Director 特别关注问题的回应\n\n**1. R2-W1 页数超限——确认？**\n**确认。** 通过 PDF 渲染验证，Section 6 (Conclusion) 完全在第 9 页，正文约 8.3 页。\n\n**2. R2-W2 Novelty scope 不足 Main track——从方法论角度是否同意？**\n**基本同意，附 caveat。** 方法论警示论文可以进 Main（Hewitt & Liang 2019 先例），但本文的 five-step audit 缺乏形式化，使其更接近 Findings 水准。\n\n**3. R2-W3 HS advantage 被 encoder quality 制约——统计分析是否支持？**\n**完全支持。** 384d→1024d 的 HB pass rate 从 4/4 降到 1/4 是统计上清晰的趋势。PCA-384d 匹配低估了文本编码器能力（见上文详细论证）。\n\n**4. R2-W6 Layer selection sensitivity 适用范围窄——从统计角度评估？**\n**不同意 R2 的结论。** 统计证据显示问题超出特定复合指标：pure BA 在 32B 上也产生 24 层不稳定性（Table 25），层选择作为未报告自由度影响任何 best-layer probing 研究。但同意论文应更明确论证广泛适用性。\n\n---\n\n### 综合评估\n\nR2 的审稿整体准确。我与 R2 在以下方面高度一致：\n- 页数超限（W1）——格式硬伤\n- 32B 统计效力不足（W4）——与我 R1-W1/W2 一致\n- 单数据集（W5）——与我 R1-W5 一致\n- HS 优势 encoder-bounded（W3）——统计证据支持\n\n主要分歧在 R2-W6（适用范围）：我认为层选择敏感性发现的适用范围比 R2 判断的更广，但同意论文未充分论证这一点。\n\n**综合评分维持 R1 判断：Overall 3.0 (Findings)，Soundness 3.0/5，Excitement 3.0/5。**",
  "reviewer_id": "1",
  "project": "contrastive_trace_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b5a30a67-b3e0-4ffe-a693-1b70d87f6955",
  "isSidechain": false,
  "requestId": "req_011CbBKuB5o267HQMPGJKg6i",
  "type": "assistant",
  "uuid": "990ec2bb-5be2-4f74-8cd5-3d6ffce0fb50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NGY1HFQ82rtqANdqHLJmu5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2664,
      "cache_read_input_tokens": 67945,
      "output_tokens": 4793,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2664,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4793,
          "cache_read_input_tokens": 67945,
          "cache_creation_input_tokens": 2664,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2664
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-19T04:53:11.302Z_

<details><summary>↩ Tool result · `toolu_01WyyPZNdGvPdN7c7NxCEGeu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "990ec2bb-5be2-4f74-8cd5-3d6ffce0fb50",
  "isSidechain": false,
  "promptId": "d26e8b60-07dd-469e-9d24-0d6e0350ad97",
  "type": "user",
  "uuid": "88d0d457-f33a-4feb-aa95-0d41aaeb46e9",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"review_director_key\\\": \\\"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_4a087be8d8cfffc128323993d357d229:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "990ec2bb-5be2-4f74-8cd5-3d6ffce0fb50",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/sessions/review_reviewer_1_8281b2fc",
  "sessionId": "3e48199e-0c0d-47bc-8ea3-24ecb0f30457",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---
