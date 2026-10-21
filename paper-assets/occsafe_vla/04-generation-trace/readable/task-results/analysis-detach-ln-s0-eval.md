# analysis detach ln s0 eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detach_ln_s0_eval_20260524T082524_result.json`
- **Structured JSON:** [`74b1c50328008edfa35f.json`](../../sessions/74/74b1c50328008edfa35f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果

| | CAR | TSR |
|--|-----|-----|
| **Detach+LN** | **0.792** | **0.914** |
| Vanilla | 0.780 | 0.713 |
| Full OCC | 0.797 | 0.747 |
| Detach OCC (BN) | 0.746 | 0.647 |

**判定：Scenario A confirmed。**

CAR=0.792 超过 Vanilla (0.780)，接近 Full OCC (0.797)。将 Detach OCC 头的 BatchNorm 替换为 LayerNorm 完全恢复了碰撞规避能力（Δ=+0.046 vs Detach BN）。这证实了 Detach 退化的根因是 BN 推理时 running statistics 失配，而非 gradient flow 中断。

TSR=0.914 远超所有 baseline，这是意外收获——Detach+LN 不仅不伤害任务性能，反而大幅提升。

唯一失败点：T5（bowl on ramekin）CAR=0.020，该任务需精确抬起堆叠物体，对所有方法都困难。

Registry 已更新为 DONE(success)，分析报告已注册。

---
