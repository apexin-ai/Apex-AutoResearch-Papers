# diagnose a3 checkpoint loading

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_a3_checkpoint_loading_20260521T195231_result.json`
- **Structured JSON:** [`874e859e68cb82112a8c.json`](../../sessions/87/874e859e68cb82112a8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 1. Checkpoint 加载：**正确，无问题**

| 组件 | 状态 | 详情 |
|------|------|------|
| LoRA params | ✅ | 504 参数加载，非零（mean≈0, std≈0.01），仅 5 个全零 |
| SDF decoder | ✅ | 从 `sdf_decoder.pt` 正确加载 (1024→256) |
| EE extractor | ✅ | 从 `ee_extractor.pt` 正确加载 |
| Base model | ✅ | 从 `pi0_base` 加载（与训练起点一致） |
| Norm stats | ✅ | pi0_base 和 A3 checkpoint 的 norm_stats 完全一致 |
| Key mismatch | ✅ | 日志中无 missing/unexpected keys 警告 |

### 2. 实际根因：**不是 checkpoint 问题**

**关键证据：Baseline 也有同样的失败模式。** westd-35807 上的 baseline spatial_bowl eval 结果：
- `collision_step: 0`
- `max_displacement: 0.822178892934208` — **与 A3 完全一致**
- TSR=0%, CAR=0%

### 3. 发现的三个真实问题

**Bug A：`moka_pot_obstacle_1` 物理不稳定（环境问题）**
- `max_displacement = 0.822m` 在所有模型、所有任务、所有 episode 完全相同 = **桌高**
- 该障碍物在机器人首次移动时就掉落，触发 collision_step=0
- 这不是模型问题，是 SafeLIBERO 环境/障碍物放置问题

**Bug B：`_refine_action_a3` 坐标假设错误（代码 Bug）**

`eval_safelibero.py:314`:
```python
next_ee = current_ee + action[:3]  # ← BUG
```

openpi 的 `AbsoluteActions` output transform 在 inference 时执行 `actions[:6] += state[:6]`，所以 `action[:3]` 已经是**绝对目标位置**。正确写法：
```python
next_ee = action[:3]  # action 本身就是目标位置
```

当前代码导致 SDF 查询位置 = `eef + target_pos`（如 z=0.8m），远高于障碍物，所以 SDF 预测值始终 > margin(0.01)，**refine 从未触发**（15000 步全部 refine_count=0）。

**Bug C：碰撞阈值过于敏感**
- `COLLISION_THRESHOLD = 0.001m` (1mm) L1 displacement
- Safety Level II 障碍物距机器人极近，首步微振就超阈值

### 4. 验证数据

Debug 运行（3 episode）确认：
- Actions 在 episode 间不同（L1 diff=0.3-1.1），模型在响应观测
- 首步后多个障碍物位移：milk 22cm, storage_box 7cm, moka_pot 3-16cm
- Action 量级 [0.1-0.5, -0.3-0.3, 0.5-0.6] 对应绝对目标位置（合理）

### 5. 修复建议

1. **修复 `_refine_action_a3` 中 `next_ee` 计算**：`next_ee = action[:3]`
2. **排查 `moka_pot_obstacle_1` 掉落问题**：确认是否所有任务都存在此物理不稳定
3. **在相同条件下跑 baseline eval** (`object_pudding`, Level II, 50 episodes) 确认 baseline 是否有同样的 TSR=0%/CAR=0%
4. **考虑调高 refine_margin**：当前 0.01 对于 SDF decoder 输出范围过低

---
