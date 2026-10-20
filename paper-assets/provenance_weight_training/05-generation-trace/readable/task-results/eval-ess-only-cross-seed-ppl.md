# eval ess only cross seed ppl

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ess_only_cross_seed_ppl_20260517T170614_result.json`
- **Structured JSON:** [`1ce572a847ff713f4592.json`](../../sessions/1c/1ce572a847ff713f4592.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**训练仍在进行中，无法评估 final checkpoint。**

当前状态：

- `ess_only_seed123` (PID 115021, cuda:2): step 999 / ~6103，只有 checkpoint-500
- `ess_only_seed456` (PID 115525, cuda:1): step 999 / ~6103，只有 checkpoint-500
- 两个训练用 `--num_train_tokens 200000000`，batch=4, grad_accum=4, max_length=2048，约需 6103 步
- 当前进度 ~16%，预计还需 ~7-8 小时完成

Python 路径为 `/root/miniconda3/bin/python`。

```
GPU 状态 westd-41312:
cuda:0: 占用 100% | PID 109024 uniform_seed42 训练 (75023MiB)
cuda:1: 占用 100% | PID 115525 ess_only_seed456 训练 (75023MiB)
cuda:2: 占用 100% | PID 115021 ess_only_seed123 训练 (75023MiB)
cuda:3: 空闲 0% | 0MiB

GPU 状态 westd-30476:
cuda:0: 空闲 0% | 0MiB
cuda:1: 占用 100% | PID 22478 python (81678MiB)
cuda:2: 占用 99% | PID 22917 python (46496MiB)
cuda:3: 占用 87% | PID 22108 python (46496MiB)
```

是否要先评估 checkpoint-500（中间 checkpoint，~16% 训练进度）？还是等训练完成后再评估？

---
