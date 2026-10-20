# ops backfill pertask metrics

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_backfill_pertask_metrics_20260524T195339_result.json`
- **Structured JSON:** [`7e6da0f3c2c68006c95f.json`](../../sessions/7e/7e6da0f3c2c68006c95f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个实验的 per-task breakdown 已成功补录到 registry。

---

## ablation_occ_detach_s2 TSR 异常诊断

**结论：不是 eval crash，是真实的性能退化。**

证据：
1. **全 500 episodes 正常完成**（10 tasks × 50 rollouts），无中断/缺失
2. **退化广泛分布**，不是个别 task 崩溃：T4=0.30, T5=0.16, T9=0.48, T7=0.66, T6=0.66, T0=0.70
3. **T3 CAR=0.0** 是标志性异常——45个成功 episode 全部发生碰撞（0 safe out of 50）

**根因分析：**

对比 3 seeds 的 Detach OCC：
| Seed | TSR | CAR |
|------|-----|-----|
| s0 (42) | 0.914 | — |
| s1 (43) | 0.898 | — |
| s2 (44) | 0.624 | 0.748 |

Seed 44 的 Detach 模型收敛到了一个质量远差的 policy。这与 CKA 分析一致——Detach OCC 导致灾难性表征漂移（CKA 0.31-0.54 vs Vanilla 0.95-0.97），而 seed 44 恰好漂移到了更差的局部最小值。BN forward-pass 干扰在无梯度补偿时 seed-dependent，部分 seed 会触发更严重的崩溃。

**建议**：在报告中将 s2 作为 high-variance 证据保留，说明 Detach 条件的不稳定性本身就是一个 finding（Vanilla/Full OCC/Random OCC 的 3-seed 方差远小于 Detach）。

---
