# code lagrangian kl

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_lagrangian-kl_20260515T131820_result.json`
- **Structured JSON:** [`2f259e991c04aab2e37f.json`](../../sessions/2f/2f259e991c04aab2e37f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练完成，checkpoint 已保存。

## 200-step Quick Test 完整结果

### 每 50 步指标

| Step | kl_loss | constraint | sparsity | lambda | tau |
|------|---------|------------|----------|--------|-----|
| 1 | 2416 | 0.094 | 0.406 | 1.00 | 0.996 |
| 50 | 892 | 0.113 | 0.387 | 1.50 | 0.775 |
| 100 | 636 | 0.316 | 0.289 | 2.25 | 0.550 |
| 150 | 414 | 0.746 | 0.168 | 3.38 | 0.325 |
| 200 | 418 | 1.211 | 0.141 | 5.06 | 0.100 |

### Lambda 增长轨迹
1.00 → 1.50 → 2.25 → 3.38 → 5.06（每 50 步 ×1.5，一直在增长，未收敛）

### 结论：稀疏度仍然坍塌

**sparsity 从 0.406 持续下降到 0.141**，远低于 target 0.5。Lagrangian multiplier 方案失败，根因：

- **数量级悬殊**：KL loss (~418-2416) 比 constraint loss (~0.1-1.2) 大 **3 个数量级**
- **lambda 增长太慢**：×1.5 的乘性更新 + cap=100 完全不够。即使 lambda 到上限 100，constraint = 100 × 0.36 ≈ 36，仍远小于 KL=418
- **梯度信号不足**：`torch.clamp(sparsity_violation, min=0)` 作为约束项的梯度通路太弱——它仅通过 mask 的 mean 值反向传播，信号被 vocab 维度 (128k) 的 KL 梯度淹没

### 代码改动摘要
- `train_kl()` 中移除了固定 `reg_fn`，替换为 Lagrangian multiplier (`lambda_sparse`) 自适应约束
- 每 50 步做 dual gradient ascent：sparsity 不达标时 lambda ×1.5，超标时 ×0.8，clamp [0.1, 100]
- 日志新增 `lambda_sparse` 和 `constraint_loss` 字段
- 已存 checkpoint: `/root/distill_sparse_swiglu/checkpoints/kl_lagrangian_quicktest/predictor_kl.pt`
- 原文件备份: `/root/distill_sparse_swiglu/src/train.py.bak`

---
