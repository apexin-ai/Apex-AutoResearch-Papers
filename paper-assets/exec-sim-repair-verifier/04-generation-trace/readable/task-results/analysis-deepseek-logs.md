# analysis deepseek logs

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-logs_20260516T080136_result.json`
- **Structured JSON:** [`7e8095f429d9728c374a.json`](../../sessions/7e/7e8095f429d9728c374a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I have all the data needed. Here's the summary:

---

## deepseek-cls-func
- **conclusion**: SUCCESS (EXIT_CODE=0)
- **epochs_completed**: 3/3
- **eval_loss per epoch**: epoch1=0.0701, epoch2=0.0727, epoch3=0.0745
- **train_loss**: 0.0948
- **best_checkpoint**: `/root/autodl-tmp/checkpoints_deepseek_cls_func/best`
- **train_time**: 1h 30m 44s (5444.8s)
- **checkpoints on disk**: `checkpoint-478`, `checkpoint-1434`, `best`
- **notes**: val loss最优在epoch 1，之后略微上升（可能轻微过拟合）。Best model在epoch 3保存。无accuracy metric输出（仅loss）。

## deepseek-cwm-func
- **conclusion**: SUCCESS (EXIT_CODE=0)
- **epochs_completed**: 3/3
- **eval_loss per epoch**: epoch1=0.0458, epoch2=0.0429, epoch3=0.0457
- **train_loss**: 0.0986
- **best_checkpoint**: `/root/autodl-tmp/checkpoints_deepseek_cwm_func/best`
- **train_time**: 1h 26m 55s (5215.2s)
- **checkpoints on disk**: `checkpoint-956`, `checkpoint-1434`, `best`
- **notes**: val loss最优在epoch 2 (0.0429)。Best model在epoch 3保存。

## deepseek-cwm-func-s123
- **conclusion**: SUCCESS (EXIT_CODE=0)
- **epochs_completed**: 3/3
- **eval_loss per epoch**: epoch1=0.0442, epoch2=0.0408, epoch3=0.0451
- **train_loss**: 0.0976
- **best_checkpoint**: `/root/autodl-tmp/checkpoints_deepseek_cwm_func_seed123/best`
- **train_time**: 1h 27m 24s (5244.3s)
- **checkpoints on disk**: `checkpoint-956`, `checkpoint-1434`, `best`
- **notes**: val loss最优在epoch 2 (0.0408)。和seed42 CWM结果一致性好（epoch 2最优，epoch 3回弹）。

## deepseek-cls-repo (running / crashed)
- **conclusion**: FAILED → OOM on initial model load
- **error**: `torch.OutOfMemoryError` — GPU 0 被其他进程占用 19.09 GiB，剩余仅 25.75 MiB
- **data**: train=70748, val=9335 (SWE-Bench full), seq_len=8192, truncated=2.2%
- **progress bars in log**: step 467/6633 (~7%), elapsed ~1h25m, ~11s/step
- **notes**: 初次启动时（15:38）因其他3个实验占用GPU而OOM。日志中后续出现训练进度条（467/6633），说明可能已被重启。若已重启，按11s/step计算，剩余 ~19h 完成。尚未产生任何 eval 结果。

---

**关键发现**：
1. 3个func-level实验全部成功完成，训练时间一致（~1.5h）
2. CWM任务的两个seed结果高度一致（best val_loss: 0.0429 vs 0.0408），验证了可复现性
3. CLS任务val loss从epoch 1开始即轻微上升，暗示epoch 1可能就是最佳——需确认保存逻辑是否基于 eval_loss 还是 last epoch
4. cls-repo 需确认是否已成功重启运行中，否则需要手动重启

---
