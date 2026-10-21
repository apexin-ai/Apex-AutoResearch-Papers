# Analysis 4a/4b/4c Results

Date: 2026-04-20

Scripts on server (`autodl-comm-gate`):
- `/root/autodl-tmp/comm_gate_mas/analysis_4a_self_cross_kappa.py`
- `/root/autodl-tmp/comm_gate_mas/analysis_4b_answer_change.py`
- `/root/autodl-tmp/comm_gate_mas/analysis_4c_ack_purity.py`

---

## 4a: Self vs Cross Annotation Cohen's κ

**Question**: Does self-annotation (same model that generated traces) produce systematically higher agreement than cross-annotation?

### Overall κ

| Config | Self Model | Cross Model | κ | Agreement% | N |
|--------|-----------|-------------|------|-----------|------|
| qwen_round_robin | Qwen | Llama | 0.6416 | 78.1% | 1500 |
| llama_round_robin | Llama | Qwen | 0.4585 | 59.0% | 1470 |
| gemma_round_robin | Gemma | Llama | 0.3502 | 64.9% | 1520 |

### Per-Type Binary κ

| Type | Qwen-Llama | Llama-Qwen | Gemma-Llama |
|------|-----------|-----------|-------------|
| reasoning_guidance | 0.8324 | 0.5180 | 0.6226 |
| verification | 0.7472 | 0.5372 | 0.0563 |
| acknowledgment | 0.6652 | 0.4483 | 0.2009 |
| information_provision | 0.0374 | 0.4354 | 0.2899 |
| coordination | 0.0000 | 0.3541 | 0.2166 |

### Systematic Bias (self% − cross%, |diff| > 5% flagged)

**Qwen traces**: Self over-labels info_provision (+6.7%) and reasoning_guidance (+6.1%); cross (Llama) over-labels acknowledgment (+15.9%).

**Llama traces**: Self over-labels acknowledgment (+20.7%); cross (Qwen) over-labels coordination (+14.4%) and reasoning_guidance (+11.6%).

**Gemma traces**: Self over-labels coordination (+16.1%); cross (Llama) over-labels information_provision (+18.7%).

### Interpretation

- **No consistent self-annotation advantage**: κ varies widely (0.35–0.64) and the direction of bias differs per backbone. The highest κ (Qwen-Llama=0.64) has the cross model labeling more acknowledgments, not fewer.
- **Structural bias pattern**: Each model has its own labeling tendencies. Llama as cross-annotator tends to label more messages as acknowledgment. Qwen as cross-annotator tends to label more as coordination.
- **reasoning_guidance is most reliably agreed-upon** across all pairs (κ 0.52–0.83), suggesting this type has the clearest signal.
- **information_provision and coordination show lowest agreement**, indicating these categories may have fuzzy boundaries.
- **For the paper**: Report that self/cross annotation bias is model-specific rather than systematic, and that the taxonomy's main discriminative power comes from reasoning_guidance vs. the rest.

---

## 4b: Answer-Change Rate by Function Type × Backbone

**Question**: When a message is ablated (removed), how often does the extracted numerical answer change? Does this vary by function type?

### Answer-Change Rate Table (5 types × 3 backbones, RR topology)

| Type | Qwen | Llama | Gemma |
|------|------|-------|-------|
| reasoning_guidance | 0.759 [0.687, 0.819] | 0.659 [0.571, 0.736] | 0.371 [0.232, 0.537] |
| information_provision | 0.723 [0.653, 0.784] | 0.650 [0.495, 0.779] | 0.266 [0.233, 0.302] |
| verification | 0.736 [0.647, 0.810] | 0.615 [0.521, 0.701] | 0.118 [0.033, 0.343] |
| acknowledgment | 0.744 [0.702, 0.783] | 0.762 [0.726, 0.794] | 0.521 [0.407, 0.633] |
| coordination | 0.800 [0.376, 0.964] | 0.857 [0.601, 0.960] | 0.127 [0.082, 0.191] |

(95% Wilson confidence intervals in brackets)

### χ² Tests (function_type × answer_change)

| Backbone | χ² | p | dof |
|----------|-----|------|-----|
| Qwen | 0.70 | 0.951 | 4 |
| Llama | 15.79 | 0.003 | 4 |
| Gemma | 41.72 | <0.001 | 4 |

### Action-Level Change Rate (for comparison)

The existing `action_level` metric (any response-level change, not just answer change) shows near-ceiling rates for Qwen and Llama (83–100%), confirming that answer-change is a stricter, more informative metric.

### Interpretation

- **Qwen**: Answer-change rate is uniformly high (~72–76%) across all types; χ² is non-significant (p=0.95). Removing ANY message from Qwen traces is equally disruptive regardless of type.
- **Llama**: Significant type dependence (p=0.003). Acknowledgments have the HIGHEST answer-change rate (76.2%), while verification has the lowest (61.5%). This is noteworthy — even "low-information" messages matter.
- **Gemma**: Strong type dependence (p<0.001). Acknowledgments again have the highest rate (52.1%), while verification (11.8%) and coordination (12.7%) rarely change answers. Gemma traces are more robust to ablation overall.
- **Cross-backbone pattern**: Acknowledgment consistently has among the highest answer-change rates, challenging the assumption that these messages are dispensable.
- **For the paper**: This provides evidence that the functional taxonomy captures real causal differences in how messages affect task outcomes, especially for Llama and Gemma. The uniformity in Qwen suggests its traces are more tightly coupled.

---

## 4c: Acknowledgment Purity Check

**Question**: Among messages labeled "acknowledgment", what fraction contain specific answer information? Does the impact gradient hold after excluding these "impure" acknowledgments?

### Purity Summary

| Backbone | Total Ack | Pure | Impure | Impure% | Pure μ(remove_sim) | Impure μ(remove_sim) |
|----------|----------|------|--------|---------|---------------------|----------------------|
| Qwen | 719 | 0 | 719 | 100.0% | N/A | 0.3518 |
| Llama | 691 | 279 | 412 | 59.6% | 0.3136 | 0.3262 |
| Gemma | 73 | 70 | 3 | 4.1% | 0.3136 | 0.1158 |

### Key Findings

**Qwen**: ALL 719 acknowledgment messages contain numerical answers (e.g., "The answer is 109."). These are essentially answer-confirmation messages, not content-free acknowledgments. This explains Qwen's high answer-change rate for acks.

**Llama**: 59.6% of acks contain numerical answers. Pure vs. impure acks have similar remove similarity (0.31 vs. 0.33, Mann-Whitney p=0.054 — not significant). Impact is driven by structural role, not information content.

**Gemma**: Only 4.1% impure (3 of 73). Most Gemma acks are genuine content-free confirmations ("Your solution is perfectly correct!").

### KW Test: Impact Gradient with Pure-Only Acknowledgments

| Backbone | KW H (pure-only) | p | KW H (all acks) | p |
|----------|------------------|------|-----------------|------|
| Qwen* | 105.18 | <0.001 | 97.22 | <0.001 |
| Llama | 96.88 | <0.001 | 108.72 | <0.001 |
| Gemma | 24.12 | <0.001 | 25.70 | <0.001 |

*Qwen has 0 pure acks, so the pure-only test excludes acknowledgments entirely and tests only among the other 3 types.

### Mean Neutralize Similarity by Type (pure-only acks)

| Type | Qwen | Llama | Gemma |
|------|------|-------|-------|
| reasoning_guidance | 0.1431 | 0.1082 | 0.0387 |
| information_provision | 0.0467 | 0.0941 | 0.0353 |
| verification | 0.2249 | 0.3245 | 0.1080 |
| acknowledgment (pure only) | — | 0.2012 | 0.0483 |

### Interpretation

- **The impact gradient holds after excluding impure acknowledgments** (all KW tests p<0.001). This means the functional hierarchy is not an artifact of answer-bearing messages being mislabeled as acknowledgments.
- **Qwen's ack impurity is a caveat**: All Qwen acks carry explicit answer information, so the high impact of Qwen acks is at least partly explained by information content, not purely structural role. This should be disclosed in the paper.
- **Llama provides the cleanest test**: With 279 pure acks and no significant pure/impure difference in impact (p=0.054), Llama demonstrates that structural position — not information content — drives the impact gradient.
- **Gemma acks are genuinely pure**: 96% content-free, strengthening the structural argument.
- **For the paper**: Report that the gradient is robust to purity filtering, but note the backbone-specific impurity rates as a transparency measure. Llama and Gemma provide the strongest evidence for a structural (vs. informational) explanation.

---

## Caveats

1. **Answer extraction from previews**: Analysis 4b extracts numerical answers from truncated `ablated_preview` fields, not full-trace replays. Some answers may be missed due to truncation.
2. **Gemma annotation distribution differs markedly**: Gemma's self-annotation strongly favors `information_provision` (56.2%), with very few `acknowledgment` labels (4.8%), suggesting Gemma's annotation behavior is qualitatively different from Qwen/Llama.
3. **Coordination sample sizes are small** for Qwen (n=5) and Llama (n=14), limiting statistical power for this type.
4. **Impurity definition**: Uses regex matching for 2+ digit numbers and "answer is X" patterns. Messages containing incidental numbers (e.g., step numbers) may be falsely flagged as impure.
