# ops check 7b scorer c4

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_7b_scorer_c4_20260520T125213_result.json`
- **Structured JSON:** [`e10769e17a14f8671a0e.json`](../../sessions/e1/e10769e17a14f8671a0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success，cron 已无需清理（无活跃 job）。

## 结果摘要

**7B scorer 不改变 K*，与 1.5B scorer 完全一致。**

| Generator | Scorer | K* | 1v2 AUC | 1v2 CI |
|-----------|--------|---:|--------:|--------|
| Pythia C4 | Qwen-1.5B | 2 | 0.8928 | [0.887, 0.899] |
| Pythia C4 | Qwen-7B | 2 | 0.8943 | [0.888, 0.901] |
| OLMo C4 | Qwen-1.5B | 1 | 0.4977 | [0.487, 0.509] |
| OLMo C4 | Qwen-7B | 1 | 0.4965 | [0.485, 0.508] |

- Pythia: K\*=2（两个 scorer 均如此），1v2 AUC 几乎相同（0.893 vs 0.894）
- OLMo: K\*=1（两个 scorer 均如此），1v2 AUC 均为随机水平（~0.50）
- 结论：K\* 对 scorer 规模鲁棒，4.7x 参数量增加不影响检测结果

---
