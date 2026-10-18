# analyze eval openvla random k09 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_random_k09_goal_seed42_20260525T101529_result.json`
- **Structured JSON:** [`b7e7bea60e6634814085.json`](../../sessions/b7/b7e7bea60e6634814085.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

## OpenVLA Random k=0.9 Goal 结果

| 指标 | 值 |
|------|-----|
| **总体成功率** | **79.6%** (398/500) |
| vs Baseline (74.8%) | **+4.8pp** |
| vs L2norm k=0.9 (74.8%) | **+4.8pp** |
| vs Attn k=0.9 (73.2%) | **+6.4pp** |

**Conclusion: success** — 超过 baseline 4.8pp。

### Goal suite k=0.9 三方 crossover 对比

| 方法 | SR | vs Baseline |
|------|-----|-------------|
| Random | **79.6%** | +4.8pp |
| L2norm | 74.8% | 0pp |
| Attention | 73.2% | -1.6pp |

在 Goal suite k=0.9 下，Random 反而表现最好。这与 OpenVLA 在高 keep ratio（仅剪 10%）时的特征一致：剪掉哪些 token 影响不大，importance-based 方法在此压缩率下没有优势。Random +4.8pp 可能是单 seed 的方差（只有 seed42），需要更多 seed 确认是否统计显著。

---
