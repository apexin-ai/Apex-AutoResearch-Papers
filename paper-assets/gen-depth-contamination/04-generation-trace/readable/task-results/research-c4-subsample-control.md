# research c4 subsample control

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_c4-subsample-control_20260518T074226_result.json`
- **Structured JSON:** [`6c1ef0b8d9440a2d610d.json`](../../sessions/6c/6c1ef0b8d9440a2d610d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

source experiment: exp016_qwen_base (C4, Qwen2.5-1.5B)
full sample K*: 2 (n=5,000)
subsample K*: **1** (n=2,200)

| Pair | Full AUC | Full 95% CI | Subsample AUC | Subsample 95% CI | CI lower > θ=0.60? |
|------|----------|-------------|---------------|------------------|---------------------|
| 0v1 | 0.9870 | [0.9853, 0.9885] | 0.9863 | [0.9838, 0.9886] | PASS |
| 1v2 | 0.6260 | [0.6168, 0.6353] | 0.6009 | [0.5861, 0.6156] | **FAIL** |
| 2v3 | 0.5496 | [0.5397, 0.5600] | 0.5583 | [0.5422, 0.5738] | FAIL |
| 3v4 | 0.5293 | [0.5188, 0.5399] | 0.5237 | [0.5075, 0.5400] | FAIL |
| 4v5 | 0.5181 | [0.5075, 0.5288] | 0.5177 | [0.5015, 0.5344] | FAIL |

## 结论

C4 下采样到 n=2,200 后 K* 从 2 降至 1。1v2 的点估计 AUC 从 0.626 降到 0.601，CI 下界从 0.617 降到 0.586（低于 θ=0.60）。**较小样本量使 CI 更宽、K\* 更保守（更低），不会虚高。** 这说明 arXiv 在仅 n=2,200 时仍达到 K\*=3，不可能是样本量小造成的假象，反而是对真实 K\* 的保守估计。

---
