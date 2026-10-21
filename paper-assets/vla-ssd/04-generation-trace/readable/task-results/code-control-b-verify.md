# code control b verify

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_control-b-verify_20260515T115703_result.json`
- **Structured JSON:** [`a3bec55912b51aa3fcbb.json`](../../sessions/a3/a3bec55912b51aa3fcbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

Control B (Cross-Trajectory Shuffle) on DINO-V2:

| 指标 | 值 |
|------|-----|
| **Global ρ** | **0.6502** |
| R² | 0.4318 |
| MAE | 0.1700 |
| Epochs | 11 (early stopped) |

**Per-task ρ:**

| Task | ρ |
|------|---|
| KITCHEN_SCENE3 (stove + moka pot) | 0.637 |
| KITCHEN_SCENE4 (bowl in drawer) | 0.666 |
| KITCHEN_SCENE6 (mug in microwave) | 0.610 |
| KITCHEN_SCENE8 (both moka pots) | 0.594 |
| LIVING_ROOM_SCENE1 (soup + cheese → basket) | 0.660 |
| LIVING_ROOM_SCENE2 (soup + sauce → basket) | 0.632 |
| LIVING_ROOM_SCENE2 (cheese + butter → basket) | 0.628 |
| LIVING_ROOM_SCENE5 (two mugs on plates) | **0.722** |
| LIVING_ROOM_SCENE6 (mug + pudding) | 0.686 |
| STUDY_SCENE1 (book in caddy) | 0.664 |

**ρ ≈ 0.65，远非预期的 ≈ 0。** 这说明 cross-trajectory shuffle 并没有摧毁 temporal distance 信号。

原因：`sample_cross_trajectory_pairs` 的 target 用的是 `|t_b/T_b - t_a/T_a|`（normalized position difference）。即使 frame 来自不同 trajectory，DINO-V2 特征本身编码了视觉进度（开头场景 vs 结束场景），这种 visual progress 在 trajectory 间是共享的（同一 task 的不同 demo 视觉演变相似，甚至跨 task 的 "早期=物体未动、后期=物体已移动" 模式也通用）。所以 probe 可以通过 visual difference magnitude 预测 temporal distance，即使是跨 trajectory pairs。

这实际上意味着 **Control B 的设计需要重新审视** —— 它没有真正打断 temporal signal，因为 normalized position 本身就和 visual features 相关。要做有效的 negative control，需要在保留 pair 结构的同时 **随机打乱 distance labels**（而不是打乱 trajectory 归属）。

---
