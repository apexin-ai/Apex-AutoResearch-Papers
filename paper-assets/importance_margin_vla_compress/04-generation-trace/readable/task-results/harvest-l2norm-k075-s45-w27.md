# harvest l2norm k075 s45 w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_l2norm_k075_s45_w27_20260528T023415_result.json`
- **Structured JSON:** [`423596ec45307b797378.json`](../../sessions/42/423596ec45307b797378.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 汇总

**L2norm k=0.75 seed45: SR=68.4%** (342/500)

四 seed 汇总:
| Seed | SR |
|------|----|
| s42 | 73.2% |
| s43 | 70.8% |
| s44 | 67.4% |
| s45 | 68.4% |
| **Mean** | **69.95% ± 2.3pp** |

seed45 与 seed44 接近（68.4% vs 67.4%），拉低均值至 ~70%。四 seed 方差从三 seed 的 ±2.9pp 收窄到 ±2.3pp，seed44 的低值不是孤立噪声，L2norm k=0.75 的稳定表现区间在 67-73%。

---
