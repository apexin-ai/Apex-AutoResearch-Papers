# eval and train traj 8b s42 eval s123 train

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval-and-train_traj-8b-s42-eval-s123-train_20260517T141241_result.json`
- **Structured JSON:** [`b308654ac94e043c579d.json`](../../sessions/b3/b308654ac94e043c579d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

s123 训练成功启动，wandb 正在同步。

---

## 结果汇总

### Part 1: Qwen3-8B TRAJ s42 Eval

| 指标 | 值 |
|---|---|
| Accuracy | **87.60%** (+34.0pp vs majority baseline) |
| Pass (resolved) F1 | **85.96%** |
| Fail (unresolved) F1 | **88.89%** |
| Unparseable rate | **0.0%** |
| Per-test consistency | 78.78% (813/1032) |
| Checkpoint | `checkpoints_traj_8b_seed42/best` |
| Test set | 1032 samples |

结果已保存到 `artifacts/qwen3_8b_traj_s42_eval.json`，服务器端保存在 `eval_traj_8b_seed42.json`。

### Part 2: s123 训练已启动

| 项目 | 信息 |
|---|---|
| tmux session | `qwen3-8b-traj-func-s123` |
| PID | 3829073 |
| GPU 占用 | 16,324 MiB |
| 总 steps | 756 (3 epochs) |
| wandb run | `traj-qwen3-8b-lora-s123` (run ID: `bfyo1yuo`) |
| 参数 | LR=2e-4, rank=16, alpha=32, bs=2, grad_accum=16, seq_len=2048 |

---
