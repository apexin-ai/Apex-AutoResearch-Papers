# eval cls 8b s42 val sweep

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls-8b-s42-val-sweep_20260514T201841_result.json`
- **Structured JSON:** [`1335ee215a70b918bb15.json`](../../sessions/13/1335ee215a70b918bb15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个问题需要确认：

**1) cuda:0 不空闲。** 当前有 eval 进程在跑：
- PID 280392（已运行 ~5 分钟）：`eval_repo_cls.py` 评估 `checkpoints_repo_cls_8b_conda/checkpoint-400`，Qwen3-8B，`--split val --max_seq_length 8192 --device cuda:0`
- PID 277670（已运行 ~29 分钟）：`eval_repo_cls.py` 评估 `checkpoints_repo_cls_v5_conda/checkpoint-200`，Qwen3-4B，cuda:1（也占了 cuda:0 约 546 MiB）

**2) Checkpoint 路径不存在。** `checkpoints_repo_cls_8b_conda_westd/` 不存在。实际存在的 8B 相关目录：
- `checkpoints_repo_cls_8b_conda/`（当前 cuda:0 上的进程正在用的）
- `checkpoints_repo_cls_8b_seed123_conda/`
- `checkpoints_repo_cls_8b_seed123_resume/`

看起来 `checkpoints_repo_cls_8b_conda/` 就是你要的 seed42 目录，且已经有人在跑 val sweep 了（但参数不同：seq_length 8192 而非 5120，且没有 `--max_new_tokens 512`）。

需要你确认：
1. 是否等 PID 280392 完成后再启动，还是要杀掉它（参数不符合 D078 要求）？
2. Checkpoint 目录用 `checkpoints_repo_cls_8b_conda/` 对吗？

---
