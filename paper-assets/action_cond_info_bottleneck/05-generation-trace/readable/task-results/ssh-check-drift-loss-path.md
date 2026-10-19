# ssh check drift loss path

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-drift-loss-path_20260517T104030_result.json`
- **Structured JSON:** [`1b44b2e09ea78c37dfbc.json`](../../sessions/1b/1b44b2e09ea78c37dfbc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

排查结论：

## drift_loss **在计算，但未打印到日志**

### 事实
1. **config 正确**：`config.json` 确认 `lambda_drift=0.1`，`freeze_mode="connector_scorer"`
2. **代码路径被执行**：`acib_policy.py:163` 条件 `freeze_mode == "connector_scorer" and lambda_drift > 0` 满足，`_connector_ref_params` 在 `__init__:29` 初始化
3. **drift_loss 已加入 total loss**：`acib_policy.py:165` 将其加入 `acib_losses["total"]`，并在 `:171` 存入 `loss_dict["connector_drift"]`
4. **`log_dict` 包含 drift**：`train_acib.py:380` 将其记为 `"train/drift_loss"`

### 根因
`train_acib.py:387-395` 的 print 格式字符串**没有包含 drift**，只打印了 `loss/task/ib/div/ctr/β/scorer_mean/std`。wandb 也未启用（`wandb_project` 为空），所以 `log_dict` 中的 `train/drift_loss` 也无处可看。

### 结论
- **drift_loss 在正确计算并参与梯度更新**，只是 logging 遗漏
- **不需要重启训练**
- 需要修复：在 print 格式中加入 `drift=` 字段，并在启动 header 加入 `Lambda drift:` 行。但这不影响当前训练的正确性，可以下次启动时生效

---
