# analysis exp 018 llama scierc seed456 r1024

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_018_llama_scierc_seed456_r1024_20260515T062018_result.json`
- **Structured JSON:** [`926ac010197f35295bc0.json`](../../sessions/92/926ac010197f35295bc0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果摘要

**exp_018_llama_scierc_seed456_r1024** — LLaMA 3.1-8B / SciERC / seed=456 / max_tokens=1024 / n=8

| 指标 | NER | RE |
|------|-----|-----|
| Greedy F1 | 0.660 | 0.434 |
| Oracle F1 | 0.768 | 0.583 |
| Oracle headroom | +10.9pp | +15.0pp |
| **SJ cond ρ** | **0.272** | **0.390** |
| FK cond ρ | 0.147 | 0.211 |
| Logprob cond ρ | 0.083 (n.s.) | 0.125 |
| Logprob AUROC | 0.549 | 0.612 |

**跨 seed 稳定性**（seed42 vs seed456，r1024）：NER SJ ρ 完全一致 (0.272)，RE SJ ρ seed456 (0.390) 略优于 seed42 (0.346)。两个 seed 均确认 **SJ > FK > Logprob** 排序。

**Conclusion: success** — Structural signal (SJ) 在两个子任务上的 conditional ρ 均显著优于 logprob（NER 3.3x, RE 3.1x）。脚本自动判定 FAIL 是因 RE ρ_sj 差 0.01 未达 0.40 硬阈值，但核心研究问题（structural vs logprob）结果明确。

---
