# check exp qwen3 4b conll finetune completion

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_qwen3_4b_conll_finetune_completion_20260515T184028_result.json`
- **Structured JSON:** [`cf09a3c5faa6ca608cbb.json`](../../sessions/cf/cf09a3c5faa6ca608cbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练仍在运行，未退出。**

当前状态：
- **进度**: step 3200/4390 (72.89%), epoch 3.64/5.0
- **预计剩余**: ~41 分钟
- **训练 loss**: ~0.018，eval_loss: 0.0254（step 3200）
- **GPU 0**: 14902 MiB, 90% 利用率
- **Checkpoints**: checkpoint-2200 ~ checkpoint-3000（每 200 步保存）
- **日志路径**: `~/runs/` 下无日志文件，实际日志在 `checkpoints/qwen3-4b-conll2003-lora/trainer_log.jsonl`

Loss 收敛正常，无异常。不修改 registry 状态，保留 cron 监控，等训练完成后再诊断。

---
