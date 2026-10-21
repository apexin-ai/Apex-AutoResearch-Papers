# infra fix exec only s43 1000step

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_fix-exec-only-s43-1000step_20260516T235237_result.json`
- **Structured JSON:** [`39ef6ac2f01feff9dcdd.json`](../../sessions/39/39ef6ac2f01feff9dcdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已经在跑了。

**`exec-only-s43-1000step-r6` 已在 GPU 0 上运行**（PID 991155，启动于 07:51，已运行约 2 分钟）。Registry 状态为 RUNNING。

命令是：
```
python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 43 --per_device_batch_size 2 --gradient_accumulation_steps 4 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_1000_r2 --no_wandb
```

注意到一个问题：output_dir 是 `_r2` 而不是 `_r6`，可能与之前 r2 的输出冲突。但实验已经正常启动且在训练中（87% GPU util），不需要再重新提交。

当前状态：**无需操作，实验正在正常运行。**

---
