# analysis action metrics extended

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_action_metrics_extended_20260518T171335_result.json`
- **Structured JSON:** [`26f8b5d37fdcda609622.json`](../../sessions/26/26f8b5d37fdcda609622.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存至 `/root/autodl-tmp/vla-ssd/results/action_metrics_extended.json`。

**Per-dim MAE ratio (instruction 24h / control 8h):**

| Dim | Inst MAE | Ctrl MAE | Ratio |
|---|---|---|---|
| dx | 0.00189 | 0.00037 | **5.09x** |
| dy | 0.00531 | 0.00125 | **4.26x** |
| dz | 0.00762 | 0.00243 | **3.14x** |
| roll | 0.02059 | 0.00785 | 2.62x |
| pitch | 0.03071 | 0.01387 | 2.21x |
| yaw | 0.03388 | 0.01783 | 1.90x |
| gripper | 0.29072 | 0.14072 | 2.07x |

**关键发现：** 平移维度 (dx/dy/dz) 受 instruction-head ablation 影响的比例最大（3-5x），远高于旋转维度（1.9-2.6x）。这说明 instruction heads 对精细位移控制的影响不成比例地大。

**Cosine similarity 无法计算：** 两个源 JSON 只存了聚合统计（mean/std），没有保存 raw per-sample action vectors。如需 cosine similarity，需重新跑 forward pass 并保存 per-sample (baseline, ablated) action pairs。

---
