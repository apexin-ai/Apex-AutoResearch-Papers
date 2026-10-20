# launch mf5 westd3 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_mf5_westd3_v2_20260522T102708_result.json`
- **Structured JSON:** [`4087c7367f9d76c9d806.json`](../../sessions/40/4087c7367f9d76c9d806.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MF5 pipeline 已经在运行，无需重新启动。

```
排查: 之前 Worker 已成功启动 pipeline，Phase 1 (prune) 已完成，Phase 2 (SFT) 正在运行
Synthetic scores: 已存在 (18KB, May 22 13:14)
Base model: pruned_depth_first_20 已生成 (12.3GB model.safetensors)
PID: 36167 (sft_recovery.py)
nvidia-smi 输出:
  GPU 0: 19251 MiB, 98%  (eval_math500 grpo_standard_20_fair)
  GPU 1: 17651 MiB, 93%  (eval_math500 sft_random_20)
  GPU 2: 0 MiB, 0%
  GPU 3: 51263 MiB, 95%  ← MF5 SFT 正在运行
ps 确认: GPU 3 有 python 进程 (PID 36167, sft_recovery.py)
当前 phase: Phase 2 SFT (10/1870 steps, ~1.64 it/s, 预计 ~19 分钟)
日志关键行: "Starting SFT recovery: 7473 samples, 2 epochs, lr=2e-05, effective_batch=8"
```

Pipeline 状态正常，SFT 刚开始训练（10/1870 steps），后续会自动链式执行 GRPO → Eval GRPO → Eval SFT。

---
