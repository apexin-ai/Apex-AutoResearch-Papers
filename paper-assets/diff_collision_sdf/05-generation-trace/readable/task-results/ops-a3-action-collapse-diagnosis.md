# ops a3 action collapse diagnosis

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_a3_action_collapse_diagnosis_20260522T092935_result.json`
- **Structured JSON:** [`a61bfc3e68759c2aeb99.json`](../../sessions/a6/a61bfc3e68759c2aeb99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。以下是完整结论。

---

## 诊断结果

### 1. Lambda 值（全部使用默认值，训练命令无覆盖）

| 参数 | 默认值 |
|------|--------|
| `lambda_sdf` | 0.1 |
| `lambda_ee` | 0.01 |
| `lambda_refine` | 0.1 |
| `eikonal_weight` | 0.1 |

### 2. Total Loss 完整公式

```
total = action_loss + 0.1 * sdf_total + 0.01 * ee_loss + 0.1 * refine_loss
```

Phase 2 才加 refine_loss 项。Phase 1 (step 0-5000) 只有前三项。

### 3. Loss 各项量级（训练完成时 step 30000）

| 组件 | 原始值 | Lambda | 加权贡献 | 占比 |
|------|--------|--------|----------|------|
| action_loss | 0.01546 | 1.0 | 0.01546 | **81.4%** |
| sdf_total | ~0.034 | 0.1 | ~0.0034 | 17.9% |
| ee_loss | 0.01213 | 0.01 | 0.000121 | 0.6% |
| refine_loss | ~3e-8 | 0.1 | ~3e-9 | **≈0%** |
| **total_loss** | | | **0.01898** | 100% |

sdf_total 通过反算得出：`(0.01898 - 0.01546 - 0.01*0.01213) / 0.1 ≈ 0.034`

### 4. 关键发现：SDF gradient refinement 几乎无效

**action_shift_mean = 0.00017** — SDF 梯度在 1024 维 suffix 空间中几乎不投影到 32 维 action 空间。refine_loss 贡献为零。

- n_refine = 2.64/32 = 8.25% 样本触发 refinement
- eval 中 refined=0（所有 episode），SDF at EE 始终 0.58-0.85，远高于 margin=0.01
- 运行时 refinement 从未激活

### 5. SDF loss 不是 action collapse 的原因

**证据明确否定 "SDF loss 过大导致 action 坍缩" 的假设：**

- SDF 加权贡献仅 18%，action_loss 占 81%
- refine_loss 实质为零
- 但 v10 eval 所有 4 个 task 全部 TSR=0%，全部跑满 300 步：

| Task | Avg Max Displacement | TSR | CAR |
|------|---------------------|-----|-----|
| orange_juice | **0.0009m** | 0% | 90% |
| chocolate_pudding | 0.0108m | 0% | 88% |
| milk | 0.0168m | 0% | 64% |

**真正的问题是系统性的，影响所有 task，不是 SDF-specific。**

### 6. 真正的根因候选

**A3 action_loss (0.01546) 比 baseline (0.005) 高 3 倍。** 但训练 loss 0.015 本身不该导致近零 displacement。更可能的原因：

1. **LoRA 权重加载顺序错误** — eval 加载 504 个 LoRA 参数，如果 param ordering 与训练时 inject_lora 的遍历顺序不一致，LoRA 输出是垃圾值
2. **Phase 1 的 5000 步冻结** — LoRA 从随机初始化开始，前 5000 步完全不学 action，直接导致 action fitting 不充分（有效训练只有 25000 步 vs baseline 30000 步）
3. **eval inference 通路问题** — 检查 eval 中 LoRA forward 是否真正生效，是否有 dtype/device mismatch 使 lora_out 被丢弃

### 7. 建议方向

**调 lambda 没用**（refine_loss 已经是零了）。应该排查：

1. **验证 eval LoRA 加载** — 在 eval 中打印 `lora_A.mean()` / `lora_B.mean()`，对比 checkpoint 中的值
2. **对比 A3 vs baseline 的 raw action output** — 给相同输入，比较两个模型输出的 action magnitude
3. **考虑从 baseline LoRA checkpoint warm-start** — 而非从随机 LoRA 开始

---
