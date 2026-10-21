# ops harvest l2norm k05 w38

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-l2norm-k05-w38_20260527T150501_result.json`
- **Structured JSON:** [`52c9766449426fe843b1.json`](../../sessions/52/52c9766449426fe843b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**π0.5 L2norm k=0.5 Long strict seed42** — westd-38929, 181.6 min

| Task | Description | SR |
|------|-------------|-----|
| T0 | put both alphabet soup and tomato | 58% |
| T1 | put both cream cheese and butter | 50% |
| T2 | turn on stove, put moka pot | **84%** |
| T3 | put black bowl in bottom drawer | 44% |
| T4 | put white mug on left plate | 30% |
| T5 | pick up book, place in back | 56% |
| T6 | put white mug on plate | 22% |
| T7 | put both alphabet soup and cream | 42% |
| T8 | put both moka pots on stove | 22% |
| T9 | put yellow/white mug in microwave | **84%** |
| **Avg** | | **49.2%** |

Total: 246/500。k=0.5 极端压缩下仍保持 49.2%，T2/T9 表现突出（84%），T6/T8 最弱（22%）。

注意：项目根目录下还有一个未完成的日志 `eval_pi05_l2norm_k05_long_seed42_strict_w38.log`（只跑到 T0 ep=10），应该是早期中断的尝试。

---
