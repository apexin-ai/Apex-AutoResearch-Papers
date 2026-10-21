# ops cwm8b checkpoint eval loss audit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-checkpoint-eval-loss-audit_20260516T005443_result.json`
- **Structured JSON:** [`e4470847f8f2ad684fde.json`](../../sessions/e4/e4470847f8f2ad684fde.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整。以下是结果。

---

## CWM 8B 全部 Eval Loss 历史

| Step | Epoch | eval_loss | 备注 |
|------|-------|-----------|------|
| 100 | 0.05 | 0.4423 | |
| 200 | 0.09 | 0.3070 | |
| 300 | 0.14 | 0.2907 | |
| **400** | **0.18** | **0.2862** | **best_model_checkpoint ✓** |
| 500 | 0.23 | 0.2998 | ↑ 开始上升 |
| 600 | 0.27 | 0.3013 | |
| 700 | 0.32 | 0.3174 | |
| 800 | 0.36 | 0.3243 | |
| 900 | 0.41 | 0.3433 | |
| 1000 | 0.45 | 0.3332 | |
| 1100 | 0.50 | 0.3405 | |
| 1200 | 0.54 | 0.3565 | |
| 1300 | 0.59 | 0.3637 | |
| 1400 | 0.63 | 0.3689 | |
| 1500 | 0.68 | 0.3742 | |
| 1600 | 0.72 | 0.3842 | |
| 1700 | 0.77 | 0.3731 | |
| 1800 | 0.81 | 0.3866 | |
| 1900 | 0.86 | 0.3923 | |
| 2000 | 0.90 | 0.3995 | |
| 2100 | 0.95 | 0.3983 | |
| 2200 | 1.00 | 0.4109 | epoch 1 结束 |
| 2300 | 1.04 | 0.4145 | |
| 2400 | 1.09 | 0.4344 | |
| 2500 | 1.13 | 0.4354 | |
| 2600 | 1.18 | 0.4260 | |
| 2700 | 1.22 | 0.4466 | |
| 2800 | 1.27 | 0.4478 | |
| 2900 | 1.31 | 0.4361 | |
| 3000 | 1.36 | 0.4449 | |
| 3100 | 1.40 | 0.4462 | |
| 3200 | 1.45 | 0.4530 | |
| 3300 | 1.49 | 0.4449 | |
| 3400 | 1.54 | 0.4435 | |
| 3500 | 1.58 | 0.4628 | |
| 3600 | 1.63 | 0.4583 | |
| 3700 | 1.67 | 0.4574 | |
| 3800 | 1.72 | 0.4664 | |
| 3900 | 1.76 | 0.4702 | |
| 4000 | 1.81 | 0.4779 | |
| 4100 | 1.85 | 0.4788 | |
| 4200 | 1.90 | 0.4825 | |
| 4300 | 1.94 | 0.4825 | |
| 4400 | 1.99 | 0.4743 | |
| 4500 | 2.04 | 0.4829 | epoch 2 结束 |
| 4600 | 2.08 | 0.4965 | |
| 4700 | 2.13 | 0.4816 | |
| 4800 | 2.17 | 0.5030 | |
| 4900 | 2.22 | 0.5069 | |
| 5000 | 2.26 | 0.5038 | |
| 5100 | 2.31 | 0.5038 | |
| 5200 | 2.35 | 0.5066 | |
| 5300 | 2.40 | 0.5129 | |
| 5400 | 2.44 | 0.5097 | |
| 5500 | 2.49 | 0.5035 | |
| 5600 | 2.53 | 0.5116 | |
| 5700 | 2.58 | 0.5152 | |
| 5800 | 2.62 | 0.5121 | |
| 5900 | 2.67 | 0.5181 | |
| 6000 | 2.71 | 0.5161 | |
| 6100 | 2.76 | 0.5208 | 最后一个 eval |

## 结论

1. **ckpt-400 是 Trainer 自动选出的 val-best checkpoint**，`best_model_checkpoint` 明确指向它，`best_metric = 0.2862`，是全局最低 eval_loss。

2. **eval_loss 在 step 400 后单调上升**，从 0.286 → 0.521（step 6100），训练约 0.18 epoch 后即开始严重过拟合。train_loss 同期从 4.27 降到 0.0036，过拟合非常明显。

3. **磁盘上只保留了 5 个 checkpoint**（400, 5800, 5900, 6000, 6100），说明训练配置了 `save_total_limit=5`，中间的 checkpoint（500-5700）已被自动删除。ckpt-400 被保留是因为 `load_best_model_at_end=True` 会保护 best checkpoint 不被删除。

4. **不需要 val sweep**——ckpt-400 是唯一合理的选择，step 500 之后 eval_loss 就没再低于 0.286。

---
