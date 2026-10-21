# analysis exp 100 walker 008a s1

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_100_walker_008a_s1_20260526T075003_result.json`
- **Structured JSON:** [`0fc9094cec9bad2256ad.json`](../../sessions/0f/0fc9094cec9bad2256ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。

---

## 分析摘要

**训练状态**: 正常结束，105K steps，最终 train_return 至 ~700-770 范围

**eval_return trajectory**: 单调上升（除 25K 和 85K 小幅回落），105K 达 750.59

**NVE 分析**:
- ve_ratio 全程 0.035→0.328，**NVE_peak = 0.328，远低于 τ=1.5×**
- 无连续 ≥2 个 eval 点 NVE > 1.5×
- civo/alert 全程 0.0
- **CIVO onset = false**

**与 parent s0 对比**:
| | s0 | s1 |
|---|---|---|
| eval@105K | 777.66 (-15.1%) | 750.59 (-18.0%) |
| ve_ratio range | 0.37–0.54 | 0.035–0.328 |
| CIVO | 无 | 无 |
| Pattern | value suppression | value suppression |

两个 seed 趋势一致，s1 性能略低、value suppression 略强，但均无 CIVO。

**Conclusion**: **success** — value suppression 确认，无 CIVO，符合预期（unexposed dt_emb 不触发 overestimation）

**C3 Walker 008a 2-seed 闭合**: s0+s1 均成功，多 seed 证据一致性确立。

---
