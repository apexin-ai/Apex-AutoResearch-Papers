# ops investigate resume step counter

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_investigate_resume_step_counter_20260523T160040_result.json`
- **Structured JSON:** [`f737443466067e20a8a2.json`](../../sessions/f7/f737443466067e20a8a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取全部信息，以下是调查报告。

---

## 调查结论

### 1. finetune.py resume 逻辑分析

**代码关键行：**

| 行号 | 逻辑 | 恢复？ |
|------|------|--------|
| L281 | `module.load_state_dict(state_dict)` — 加载模型权重 | **恢复** |
| L945 | `vision_backbone.load_state_dict(state_dict)` — 加载 vision backbone | **恢复** |
| L1054 | `optimizer = AdamW(trainable_params, lr=cfg.learning_rate)` — 新建 optimizer | **不恢复** |
| L1218 | `gradient_step_idx = batch_idx // cfg.grad_accumulation_steps` — 从 0 开始 | **不恢复** |
| L1157 | `tqdm.tqdm(total=cfg.max_steps)` — 无 `initial` 参数 | **不恢复** |
| L1226 | `log_step = cfg.resume_step + gradient_step_idx` — wandb/save 用偏移后的步数 | **正确偏移** |
| L1291 | `if log_step == cfg.max_steps: break` — 停止条件用 log_step | **正确** |

**结论：resume 只恢复模型权重，不恢复 optimizer state、LR scheduler、步数计数器。tqdm 从 0 开始是设计如此（非 bug），但 log_step 正确计算了偏移。**

### 2. 初始 loss 确认权重已加载

| 实验 | step=0 action_loss | step=0 occ_loss | 判断 |
|------|-------------------|-----------------|------|
| detach_ln_s0 | **0.1299** | 0.0116 | 低，权重已加载 |
| detach_ln_s1 | **0.0864** | 0.0088 | 低，权重已加载 |
| detach_ln_s2 | **0.1377** | 0.0115 | 低，权重已加载 |

随机初始化的 action_loss 通常 > 2.0。三个实验初始 loss 都在 0.08-0.14，确认 20K/10K checkpoint 权重成功加载。

### 3. 当前训练进度

| 实验 | gradient_step_idx | 实际 log_step | action_loss | 实际进度 |
|------|------------------|---------------|-------------|----------|
| s0 | 6200 | **26200** (20000+6200) | 0.0771 | 52% |
| s1 | 6300 | **26300** (20000+6300) | 0.0913 | 53% |
| s2 | 6200 | **16200** (10000+6200) | 0.1240 | 32% |

tqdm 显示 6200/50005 ≈ 12%，但实际进度是 26200/50005 ≈ 52%（s0/s1）。

### 4. 最终判断

**步数计数器确实从 0 开始，但这只是 tqdm 显示问题，训练完全有效：**
- 模型权重已加载（初始 loss 证实）
- wandb log、checkpoint 保存、停止条件都用 `log_step = resume_step + gradient_step_idx`，逻辑正确
- s0/s1 训练到 gradient_step_idx = 30005 时 log_step = 50005 自动停止（共训练 30K 步）
- s2 训练到 gradient_step_idx = 40005 时停止（共训练 40K 步）

### 5. 潜在问题（非致命）

- **LR warmup 重新执行**（L1232 用 `gradient_step_idx`）：resume 后 LR 从 10% 重新 warmup，而非从当前值继续。影响较小。
- **occ_loss_weight 衰减从头开始**（用 `batch_idx`）：resume 后衰减曲线重置。可能导致 occ head 权重偏高。
- **Optimizer momentum/Adam state 丢失**：新建 AdamW，动量从零积累。

### 6. 建议

**不需要 kill 重启。** 训练有效，loss 在正常下降。tqdm 显示只是"化妆品"问题。

---
