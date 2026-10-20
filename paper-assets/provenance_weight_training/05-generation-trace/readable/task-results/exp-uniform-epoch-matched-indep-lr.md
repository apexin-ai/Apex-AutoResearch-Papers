# exp uniform epoch matched indep lr

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_uniform_epoch_matched_indep_lr_20260521T115212_result.json`
- **Structured JSON:** [`460619c2c0920fe0643d.json`](../../sessions/46/460619c2c0920fe0643d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行中。

**总结：**
- **exp_id**: `uniform_epoch_matched_indep_lr_seed42`
- **PID**: 604874, GPU: cuda:2, server: westd-41312
- **total_steps**: 2533 (确认 `0/2533` 进度条)
- **lr_scheduler_type**: cosine (从 config 输出确认)
- **预计耗时**: ~2.08s/step × 2533 ≈ 1.5h
- 给脚本新增了 `--lr_scheduler_type` 参数（默认 linear，本次传 cosine），已同步写入 TrainingArguments 和 config_summary
- Registry 状态: RUNNING

---
