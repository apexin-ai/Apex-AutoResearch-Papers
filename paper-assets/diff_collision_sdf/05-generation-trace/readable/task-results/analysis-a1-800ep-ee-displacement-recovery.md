# analysis a1 800ep ee displacement recovery

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a1_800ep_ee_displacement_recovery_20260526T011251_result.json`
- **Structured JSON:** [`d94bd118b51985c6bf1e.json`](../../sessions/d9/d94bd118b51985c6bf1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有了完整的分析。让我写出最终报告。

## 汇报

### 1. 数据文件路径和格式

**文件**: `/root/autodl-tmp/eval_results/a1_rerun_v11_eval_safelibero_object_all_levelII_best_lora_baseline_seed0.json` (239K)

**格式**: 
- 4 tasks × 200 episodes = 800 total
- 每个 episode 字段: `episode`, `success`, `collided`, `collision_step`, `collision_obstacle`, `max_displacement`, `total_steps`, `smoothness`
- `max_displacement` 是 **obstacle displacement**（障碍物位移），不是 EE displacement

### 2. EE displacement 数据不可恢复

**不可行**，三个原因：

1. **旧版 eval 脚本**：800ep 数据由旧版 `eval_safelibero.py` 生成，不含 `max_ee_displacement` 字段（当前版本已添加但在此之后）
2. **无 per-step 轨迹数据**：JSON 中没有 trajectory / EE position，smoothness 是 mean jerk 无法反推位移
3. **Checkpoint 已删除**：`/root/autodl-tmp/checkpoints/a1_sdf_object_pudding/` 目录不存在，无法重跑 eval

### 3. 现有数据分析（最佳间接证据）

| 指标 | 值 |
|------|-----|
| Total episodes | 800 |
| TSR | **0.0%**（全部 task，action collapse 确认）|
| CAR | **91.5%** (732/800 safe) |
| Collided episodes | 68/800 (8.5%) |
| Obstacle disp median | **0.000005mm** |
| Safe episodes obs disp | **全部 < 1mm** |
| Collided episodes obs disp | mean=45.9mm, max=286.5mm |

**关键发现**：所有 732 个 safe episodes 的 obstacle displacement 都 < 1mm。

**但需要注意**：对比 pi05 A1 (SDF-trained) 模型，safe episodes 也是 obstacle displacement < 0.5mm，但 EE displacement 全部 > 238mm。所以 obstacle displacement < 1mm **不能** 直接证明 EE < 100mm——只能证明机器人没碰到障碍物。

**关键区别在于 TSR**：
- Pi05 A1：TSR=4-9%，机器人活跃移动，EE 全部 > 238mm
- A1 baseline：**TSR=0%**，完全 action collapse，smoothness 比活跃模型高 4.5×（更 jerky、更无意义的抖动）

### 4. dfCAR 估计与替代方案

**定性推断**：TSR=0% + action collapse → 大部分 episode EE << 100mm → dfCAR@100mm ≈ 0%。但缺乏精确数据。

**替代方案（按可行性排序）**：

1. **恢复 checkpoint 后重跑**：如果能从 wandb/backup 恢复 `a1_lora_object_pudding_seed0/best/model.safetensors`，用当前 eval 脚本重跑即可得到 `max_ee_displacement`。当前所有 6 张 GPU 都满，最快预计 10 小时后有空闲。

2. **用 pi05 A1 lambda=0 模型替代**：正在训练中的 `a1_sdf_pi05_object_pudding_seed2_l0`（lambda_sdf=0，无 SDF loss）可能也会展现 action collapse。训练完成后可 eval 获取带 EE displacement 的数据。但 pi05 基础模型不同，不一定复现 TSR=0%。

3. **在论文中用 obstacle displacement 代替**：定义 displacement-filtered CAR 时使用 obstacle displacement（已有数据）作为 proxy metric。优点是不需要重跑；缺点是物理含义不同（测量的是碰撞力度不是机器人移动距离）。

---
