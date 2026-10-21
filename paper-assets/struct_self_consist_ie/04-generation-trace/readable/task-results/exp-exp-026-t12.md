# exp exp 026 t12

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp_026_t12_20260516T125546_result.json`
- **Structured JSON:** [`37082b6f0570164165eb.json`](../../sessions/37/37082b6f0570164165eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_026_t12 完成。结果汇总：

| 指标 | T=0.5 | T=0.8 | **T=1.2** |
|------|-------|-------|-----------|
| Greedy F1 | 0.6647 | 0.6633 | 0.6615 |
| Oracle F1 | 0.7423 | 0.7684 | **0.7914** |
| Oracle headroom | +0.078 | +0.105 | **+0.130** |
| Fleiss' κ (mean) | 0.577 | 0.451 | 0.356 |
| Soft Jaccard (mean) | 0.833 | 0.749 | 0.645 |
| ρ(κ, F1) full | 0.256 | 0.250 | **0.338** |
| ρ(SJ, F1) full | 0.297 | 0.359 | **0.377** |
| ρ(SJ, F1) cond | 0.278 | 0.312 | **0.355** |
| Sample F1 mean | 0.636 | 0.622 | 0.594 |
| Logprob ρ full | 0.218 | 0.253 | 0.196 |
| Verdict | FAIL | MARGINAL | **MARGINAL** |

T=1.2 的 consistency-quality 相关性（SJ ρ=0.377）是三个温度中最高的，oracle headroom 也最大（+0.130）。代价是 sample F1 均值下降至 0.594 且 F1=0 比例升至 13.9%。logprob baseline 的 ρ 在 T=1.2 下反而最低（0.196），说明高温度下 structural consistency 信号的相对优势更大。

---
