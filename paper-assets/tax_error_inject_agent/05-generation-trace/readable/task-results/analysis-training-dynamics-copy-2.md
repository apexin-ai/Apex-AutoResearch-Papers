# analysis training dynamics

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_training-dynamics_20260515T132054_result.json`
- **Structured JSON:** [`136464c12cfe896acc7c.json`](../../sessions/13/136464c12cfe896acc7c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是完整分析报告。

---

## 训练 Log 分析报告

### 1. Per-sample loss：**不存在**

现有 log 每行只有 aggregate 指标：
- `loss`（batch 平均 loss）
- `token_acc`（token 级准确率）
- `grad_norm`, `learning_rate`, `epoch`, `memory`

项目代码中无 `per_sample`、`compute_loss` override、`TrainerCallback` 等自定义追踪逻辑。Swift SFT 默认不区分 clean vs injected samples 的 loss。

**结论：需要 re-train 才能获得 per-sample loss。**

### 2. Aggregate Loss 曲线对比

#### 主实验 v4（seed 42，完整数据集）

| 条件 | 数据量 | Steps | Avg Train Loss | Final Loss | Final Token Acc |
|------|--------|-------|----------------|------------|-----------------|
| **vanilla** | 4,358 | 1,635 | 0.4173 | 0.2942 | 0.8995 |
| **taxei** | 9,029 | 3,387 | 0.3558 | 0.1738 | 0.9139 |
| **random** | 9,029 | 3,387 | 0.3551 | 0.1677 | 0.8987 |

**观察**：taxei 和 random 数据量约为 vanilla 的 2 倍（加了 injected samples），训练步数也多一倍。两者 avg loss 和 final loss 都低于 vanilla，但这主要是因为数据量大、训练步数多。taxei 的 final token_acc (0.9139) 高于 random (0.8987)。

#### 多 Seed 稳定性

| 条件 | seed42 | seed0 | seed123 | Mean±Std |
|------|--------|-------|---------|----------|
| **vanilla** train_loss | 0.4173 | 0.4160 | 0.4159 | 0.4164±0.0008 |
| **taxei** train_loss | 0.3558 | 0.3553 | 0.3551 | 0.3554±0.0004 |
| **random** train_loss | 0.3551 | 0.3551 | 0.3548 | 0.3550±0.0002 |
| **taxei** token_acc | 0.9139 | 0.9172 | 0.8998 | 0.9103±0.0093 |
| **random** token_acc | 0.8987 | 0.9118 | 0.9085 | 0.9063±0.0069 |

**观察**：train_loss 跨 seed 非常稳定。token_acc 波动稍大，taxei 在 seed123 上偏低。

#### Dose-Response（固定数据量 4,358）

| 条件 | Train Loss | Final Loss | Final Token Acc |
|------|-----------|------------|-----------------|
| vanilla (0%) | 0.4173 | 0.2942 | 0.8995 |
| taxei_inject10 (output) | 0.4234 | 0.3077 | 0.8875 |
| taxei_inject25 (output) | 0.4245 | 0.2851 | 0.8926 |
| taxei_inject50 | 0.4335 | 0.2586 | 0.9105 |

**观察**：固定数据量下，随 injection 比例增加，avg train_loss 单调上升（injected samples 更难学），但 final loss 在 50% 时反而最低（0.2586）。

### 3. 收敛速度对比

所有实验初始 loss 约 4.0，前 50 步迅速降到 0.6-0.8（一致）。vanilla 在 ~1000 步后基本收敛（loss ~0.3），taxei/random 在 ~2000 步后收敛到更低水平（loss ~0.17）。收敛速度差异主要由数据量/步数差异驱动，非 injection 类型本身。

### 4. 获取 Per-sample Loss 的方案

如果需要区分 clean vs injected samples 的 loss 差异，有两条路径：

**方案 A：Post-hoc 推理（不需 re-train）**
- 加载已训练好的 checkpoint
- 分别在 clean subset 和 injected subset 上计算 forward pass loss
- 对比两组的 loss 分布

**方案 B：Re-train with custom callback**
- 在训练数据中加标记字段（`is_injected`）
- 自定义 `TrainerCallback.on_log` 分别记录 clean/injected 的 loss
- 需要 override `compute_loss` 或在 data collator 中传递标记

方案 A 更快，能直接利用现有 checkpoint，推荐优先尝试。

---
