# code contrastive only ablation check

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_contrastive-only-ablation-check_20260516T151806_result.json`
- **Structured JSON:** [`6ed0644aa3b5afcb1705.json`](../../sessions/6e/6ed0644aa3b5afcb1705.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完毕。以下是完整结论：

---

## 1. beta=0 安全性

**安全，无 bug。** 代码路径：

- `train_acib.py:335-338`：`beta_warmup` 逻辑在 `args.beta=0` 时，`beta_current` 始终为 0（`0 * min(...)` = 0），然后写入 `policy.acib_loss_fn.beta = 0.0`
- `losses.py:32`：`total = task_loss + self.alpha * consistency_loss + self.beta * ib_loss`，当 `self.beta=0` 时 IB 项为 0×ib_loss = 0
- `information_bottleneck_loss` 仍会被计算（`forward()` 无条件调用它），但结果乘以 0 不影响梯度
- 无 division-by-zero 风险：IB loss 内部的 `clamp(1e-7, 1-1e-7)` 和 `log` 运算对输入安全

**beta_warmup_steps 在 beta=0 时无问题**：warmup 公式 `0 * min(1.0, ...)` = 0，永远输出 0。

## 2. Contrastive-only 配置

```bash
--alpha 0 --beta 0 --lambda_contrastive 0.1 --diversity_lambda 0.1 --lambda_ent 0.0
```

保留的 loss：
- task_loss（基础策略损失，始终存在）
- contrastive_loss（通过 `lambda_contrastive > 0` 触发，在 `acib_policy.py:forward()` 中加入）
- diversity_regularizer（通过 `diversity_lambda > 0` 触发，在 `train_acib.py` 训练循环中加入）

关闭的 loss：
- IB loss（beta=0）
- consistency loss（alpha=0）
- entropy regularizer（lambda_ent=0）

## 3. 完整 Ablation 参数表

| 配置 | alpha | beta | lambda_contrastive | diversity_lambda | lambda_ent | 保留的 loss |
|------|-------|------|--------------------|------------------|------------|-------------|
| **Full ACIB (v7)** | 0.01 | 0.01 | 0.1 | 0.1 | 0.0 | task + IB + consistency + contrastive + diversity |
| **Contrastive-only** | 0 | 0 | 0.1 | 0.1 | 0.0 | task + contrastive + diversity |
| **IB-only (no contrastive)** | 0.01 | 0.01 | 0.0 | 0.1 | 0.0 | task + IB + consistency + diversity |
| **No-diversity** | 0.01 | 0.01 | 0.1 | 0.0 | 0.0 | task + IB + consistency + contrastive |
| **Task-only baseline** | 0 | 0 | 0.0 | 0.0 | 0.0 | task only（scorer 仍在 forward path 但梯度信号仅来自 task loss） |

## 4. 是否需要改代码

**不需要。** 所有 ablation 配置纯靠命令行参数控制，代码中每个 auxiliary loss 都有 `> 0` 的 guard：
- `lambda_contrastive > 0`（`acib_policy.py:137`）
- `diversity_lambda > 0`（`train_acib.py:311`）
- `lambda_ent > 0`（`train_acib.py:320`）
- `beta` 和 `alpha` 直接乘以对应 loss（`losses.py:32`）

唯一注意：**task-only baseline** 中 scorer 仍在 forward path（hook 不会被跳过），所以 scorer 参数仍然 trainable 且接收来自 task loss 的梯度。如果想要「纯 vanilla baseline，完全不经过 scorer」，需要设 `--train_scorer_only False`（默认就是 False）并考虑用没有 ACIBPolicy wrapper 的原始 SmolVLA。但作为 ablation 对照，保持 scorer 在 path 中（只是无 auxiliary loss）是合理的对比设计。

---
