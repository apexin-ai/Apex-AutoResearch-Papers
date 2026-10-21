# analysis bootstrap ci nscaling

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_nscaling_20260514T192015_result.json`
- **Structured JSON:** [`7c83d61bd622a14ed26c.json`](../../sessions/7c/7c83d61bd622a14ed26c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both artifacts registered. Here's the summary:

---

## Part 1: Bootstrap CI for N-scaling (B=10000)

**Qwen CoNLL** (n=3453):
| Signal | ρ₈ | ρ₁₆ | Δρ mean | 95% CI | p(Δ>0) |
|---|---|---|---|---|---|
| SJ | 0.125 | 0.145 | +0.020 | [-0.007, +0.048] | 0.927 |
| **FK** | **0.132** | **0.184** | **+0.052** | **[+0.015, +0.087]** | **0.998** |
| EM | 0.102 | 0.106 | +0.004 | [-0.019, +0.028] | 0.641 |
| voting_conf | 0.709 | 0.716 | +0.007 | [-0.007, +0.022] | 0.834 |
| logprob | -0.200 | -0.214 | -0.014 | [-0.028, -0.000] | 0.021 |

**Qwen SciERC** (n=551): SJ and FK show Δρ ≈ +0.054 with CIs mostly above 0 (p=0.95/0.90). Other signals stable.

**LLaMA SciERC** (n=551): No significant improvement for any signal; N=8→N=16 gains are model-dependent.

Key takeaway: FK benefits most from N=16 (only signal with CI fully above 0 on CoNLL). voting_conf is already saturated at N=8 (ρ≈0.71). Logprob becomes slightly more negative with more samples on CoNLL.

## Part 2: LOO-SJ Circularity Check

**Greedy F1 correlation**: max |Δρ| = 0.005 across all 6 dataset×N combinations. SJ-F1 correlation is virtually unchanged when any single sample is removed — no circularity.

**Per-sample analysis**: Full SJ has a slight information advantage (Δρ ≈ 0.03-0.05 for N=8, halves to 0.015-0.026 for N=16), which is expected and diminishes with more samples.

**LOO sensitivity**: mean within-instance SJ std drops from ~0.03 (N=8) to ~0.015 (N=16), confirming SJ stabilizes with more samples.

---
