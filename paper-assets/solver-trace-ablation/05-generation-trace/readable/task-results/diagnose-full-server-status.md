# diagnose full server status

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_full-server-status_20260513T232703_result.json`
- **Structured JSON:** [`e1fb7c177fd30ceb5a9f.json`](../../sessions/e1/e1fb7c177fd30ceb5a9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
[诊断结果]

- cuda:0: PID 84901, plan001-exec-only-s42-r2, 80314MiB/97887MiB, GPU-Util 91%, RUNNING
- cuda:1: PID 85795, plan005-sta-low-s42, 80346MiB/97887MiB, GPU-Util 90%, RUNNING

- plan001 历史:
  - r1 (plan001-exec-only-s42.log): FAILED — `unrecognized arguments: --max_steps 500` (EXIT_CODE=2)
  - r3 (plan001-exec-only-s42-r3.log): FAILED — torch.OutOfMemoryError: CUDA out of memory (GPU0 94.97GiB 中仅剩 30.19MiB free)
  - r2 (plan001-exec-only-s42-r2.log): RUNNING — step 361/500, reward_log 360行

- plan001 失败根因:
  - r1: 参数名错误，用了 --max_steps 而脚本参数是 --num_steps
  - r3: OOM，当时 cuda:0 被 r2 占用(PID 84901 占 78.43GiB)，两进程冲突

- plan005 状态: RUNNING — step 306/500, reward_log 305行

- plan001 最新 metrics (step 357-361):
  prove_rate: 0.625~1.0, isr_mean: 0.625~1.0, reward_mean: 0.625~1.0

- plan005 最新 metrics (step 302-306):
  prove_rate: 0.5~1.0, isr_mean: 0.03~0.27, reward_mean: 0.45~0.93

[脚本参数]
--model_path, --data_path, --reward_mode {execution_only,execution_sta},
--output_dir, --num_steps, --per_device_batch_size, --gradient_accumulation_steps,
--num_generations, --max_completion_length, --learning_rate,
--exec_weight, --sta_weight, --seed, --solver,
--wandb_project, --wandb_run, --no_wandb, --config

[数据文件]
train_500_seed42.jsonl: 存在, 500行, 484KB

[注意] 有2个 swipl 进程 (PID 95935, 96445) 各占 99.9% CPU，疑似死循环测试残留。
```

---
