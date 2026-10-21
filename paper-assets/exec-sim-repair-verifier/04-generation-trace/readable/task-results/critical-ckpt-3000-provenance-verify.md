# critical ckpt 3000 provenance verify

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_critical_ckpt-3000-provenance-verify_20260514T203043_result.json`
- **Structured JSON:** [`2be87fb891699b6bcdcc.json`](../../sessions/2b/2be87fb891699b6bcdcc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 282772 已终止，GPU 1 显存从 31054MiB 降至 13629MiB，释放 ~17.4GB。

---

## 溯源结论

### Q1: `checkpoints_repo_cls_8b/checkpoint-3000` 的 transformers 版本？
**transformers 5.x（旧 invalid 训练）**。证据：
- training_args.bin 包含 5.x 特有属性：`mixed_precision`, `enable_jit_checkpoint`, `train_sampling_strategy`, `ddp_static_graph`
- 缺少 4.x 遗留属性：`adafactor`, `no_cuda`, `tpu_metrics_debug`, `fp16_backend` 等
- peft_version = **0.19.1**（非 conda 环境）
- 创建时间 = May 14 05:30 +0800 = **May 13 21:30 UTC**，早于 conda 训练

### Q2: `checkpoints_repo_cls_8b_conda/` 下的 checkpoint？
| Checkpoint | 时间 (CST) | peft | transformers |
|---|---|---|---|
| checkpoint-200 | May 14 07:27 | 0.19.0 | 4.x |
| checkpoint-400 | May 14 08:08 | 0.19.0 | 4.x |
| checkpoint-600 | May 14 08:50 | 0.19.0 | 4.x |

训练仅到 checkpoint-600（未完成到 3000）。

### Q3: `checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000` 的 transformers 版本？
**transformers 4.x（正确的 conda 训练）**。证据：
- training_args.bin 包含 4.x 遗留属性（`adafactor`, `no_cuda`, `tpu_metrics_debug` 等）
- peft_version = **0.19.0**
- seed = 123, 创建时间 = May 15 00:55 +0800
- output_dir 指向正确路径

### Q4: 是否有 test eval 进程在跑？
**PID 282772**（已 kill）：用的正是无效 checkpoint `checkpoints_repo_cls_8b/checkpoint-3000`，split=test, max_seq_length=5120。GPU 已释放。

其他仍在运行的有效进程：
- PID 280392: `cls_8b_conda/checkpoint-400` val eval (GPU 0)
- PID 281646: `cls_v5_conda/checkpoint-400` val eval (GPU 0+1)

### Q5: 89.50% val 结果是否 valid？
**INVALID。** 该结果来自 transformers 5.x 旧训练的 checkpoint，不可引用。

**替代方案：** `checkpoints_repo_cls_8b_seed123_conda/checkpoint-3000` 是用正确环境（transformers 4.x, peft 0.19.0, seed=123）训练完成的，可用作 8B ckpt-3000 的有效替代进行 eval。

---
