# ops collect a3 v11 final

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_collect_a3_v11_final_20260522T144026_result.json`
- **Structured JSON:** [`fe1b4a65db6130342e4b.json`](../../sessions/fe/fe1b4a65db6130342e4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 traceback 或 killed。日志中的 "error" 只是 triton autotuning 的无害警告（OutOfMemoryError 在 kernel 选择阶段，已自动 fallback）。

现在提取 task 3 的摘要数据（JSON 被截断了中间部分，但日志里有完整打印）。从日志可得所有 4 个 task 的完整结果：

## A3 Eval v11 结果 — 完成

Eval 正常完成，4 个 task 各 50 episodes，无异常。

### 每 Task 结果

| Task | Task Name | TSR | CAR | Avg Displacement | Refined Count |
|------|-----------|-----|-----|-------------------|---------------|
| 0 | pick_up_the_orange_juice_and_place_it_in_the_basket | **0.0%** (0/50) | **84.0%** (42/50) | 0.0149m | **0** |
| 1 | pick_up_the_butter_and_place_it_in_the_basket | **0.0%** (0/50) | **48.0%** (24/50) | 0.0388m | **0** |
| 2 | pick_up_the_milk_and_place_it_in_the_basket | **0.0%** (0/50) | **82.0%** (41/50) | 0.0079m | **0** |
| 3 | pick_up_the_bbq_sauce_and_place_it_in_the_basket | **0.0%** (0/50) | **84.0%** (42/50) | 0.0041m | **0** |

### 平均指标

| Metric | A3 v11 | Baseline v11 | Delta |
|--------|--------|-------------|-------|
| **Avg TSR** | 0.0% | 0.5% | -0.5% |
| **Avg CAR** | **74.5%** | 83.0% | **-8.5%** |
| **Avg Displacement** | 0.0164m | 0.027m | **-0.011m** (改善) |

### Refined Count 汇总

**所有 200 个 episode 的 refined_count 均为 0。A3 的 gradient refinement 机制完全未被激活。**

### 关键发现

1. **TSR = 0%**：比 baseline 更差（baseline 0.5%），任务成功率全面崩溃
2. **CAR 下降 8.5%**：碰撞率从 83% 降到 74.5%，safety 反而变差
3. **Displacement 改善**：平均位移从 0.027m 降到 0.016m，但这大概率是因为机械臂根本没有有效移动（TSR=0%）
4. **Refinement 从未触发**：refine_count 全部为 0，说明 SDF 值始终在 margin (0.01) 之上，或 refinement 逻辑存在 bug。从日志看 sdf_min 普遍在 0.46-0.97 范围，远大于 refine_margin=0.01，所以 refinement 条件从未满足

**结论：A3 模型在 v11 object suite 上全面失败。核心问题是 refinement 机制未被激活（margin=0.01 远小于实际 SDF 值），且模型本身的 task 完成能力相比 baseline 严重退化。**

---
