# ops check dr checkpoint optimizer

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_dr_checkpoint_optimizer_20260518T085603_result.json`
- **Structured JSON:** [`de079ded8f46424a3d94.json`](../../sessions/de/de079ded8f46424a3d94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

```
seed123 checkpoint-500:
  files: 不存在（目录仅含 config.json, step_metrics.jsonl，无 checkpoint）
  size: N/A
  has_optimizer: N/A

seed456 checkpoint-500:
  files: model.safetensors (1.1GB), optimizer.pt (2.2GB), scheduler.pt,
         rng_state.pth, trainer_state.json, training_args.bin,
         tokenizer 文件, config.json
  size: 3.4GB
  has_optimizer: yes

结论:
- seed456: 可以安全 resume。checkpoint 完整，包含 optimizer.pt + scheduler.pt，LR schedule 会正确恢复。
- seed123: 无 checkpoint 可用，需要从头训练。该目录只有 config.json 和 step_metrics.jsonl，训练可能未成功保存或已被清理。
```

---
