# debug check control ablation results

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_check_control_ablation_results_20260518T121214_result.json`
- **Structured JSON:** [`3b22d4d83e26e8778d89.json`](../../sessions/3b/3b22d4d83e26e8778d89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Full-scale 实验已完成。** 5 tasks × 10 demos × 50 timesteps = 2500 samples（每 task 500），共 5000 forward passes。

核心结果摘要：

| Metric | Value |
|---|---|
| **Paired Action MSE** | 0.0201 ± 0.0489 (t=20.54, p≈9e-87, Cohen's d=0.41) |
| **Token Divergence Rate** | 29.3% |
| **KL Divergence** | 1.69 ± 3.70 |
| **Wilcoxon p** | 8e-235 |

**Per-dim action shift**（ablation vs baseline 的偏移）：

| Dim | Mean Shift | Std |
|---|---|---|
| dx | 0.00037 | 0.0019 |
| dy | 0.00125 | 0.0042 |
| dz | 0.00243 | 0.0060 |
| rx | 0.00785 | 0.0162 |
| ry | 0.01387 | 0.0241 |
| rz | 0.01783 | 0.0305 |
| **gripper** | **0.1407** | **0.3441** |

**Per-task paired MSE：**

| Task | MSE | Cohen's d | Token Div Rate |
|---|---|---|---|
| open_middle_drawer | 0.0071 | 0.24 | 24.0% |
| open_top_drawer_put_bowl | 0.0258 | 0.48 | 30.4% |
| push_plate_to_stove | 0.0213 | 0.42 | 30.6% |
| put_bowl_on_plate | 0.0227 | 0.44 | 29.9% |
| put_bowl_on_stove | 0.0236 | 0.45 | 31.3% |

关键发现：
- Zeroing 8 个 non-instruction heads 造成**统计显著**的 action 偏移（p≈9e-87），效应量中等（d=0.41）
- **Gripper 维度受影响最大**（shift 0.14，比位移维度高 1-2 个数量级）
- 旋转维度 > 位移维度，说明 non-instruction heads 对精细控制信号影响更大
- KL divergence 在 token position 4-5 最高（3.32, 3.72），最后一个 token（gripper）反而较低（0.55）
- 所有 5 个 task 效果一致，open_middle_drawer 受影响最小（d=0.24）

---
