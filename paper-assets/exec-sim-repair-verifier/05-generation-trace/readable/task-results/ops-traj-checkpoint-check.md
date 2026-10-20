# ops traj checkpoint check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-checkpoint-check_20260519T172001_result.json`
- **Structured JSON:** [`94c7cc28725c73f41dd7.json`](../../sessions/94/94c7cc28725c73f41dd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## TRAJ Multi-Seed Checkpoint 汇总

### Qwen3-8B TRAJ

| Seed | Checkpoint 路径 | 内容 | Eval 结果 |
|------|----------------|------|-----------|
| s42 (默认) | `/root/autodl-tmp/checkpoints_qwen3_8b_traj_repo/` | best, checkpoint-147, checkpoint-98 | 无独立 eval 目录 |
| s123 | `/root/autodl-tmp/checkpoints_qwen3_8b_traj_repo_s123/` | best, checkpoint-147, checkpoint-98 | ✅ `eval_results/qwen3_8b_traj_repo_s123/eval_test.json` |
| s456 | `/root/autodl-tmp/checkpoints_qwen3_8b_traj_repo_s456/` | best, checkpoint-147, checkpoint-98 | ✅ `eval_results/qwen3_8b_traj_repo_s456/eval_test.json` |
| v3 | `/root/autodl-tmp/checkpoints_qwen3_8b_traj_repo_v3/` | best, checkpoint-147, checkpoint-98 | — |

**三个 seed（s42/s123/s456）的 checkpoint 全部存在，结构一致。**

### DeepSeek TRAJ (repo 8k)

| Seed | Checkpoint 路径 | 内容 |
|------|----------------|------|
| s42 (默认) | `checkpoints_deepseek_traj_repo_8k/` | best, ckpt-147, ckpt-98 + eval_test_s42.json |
| s0 | `checkpoints_deepseek_traj_repo_8k_s0/` | best, ckpt-147, ckpt-98 |
| s123 | `checkpoints_deepseek_traj_repo_8k_s123/` | best, ckpt-147, ckpt-98 + eval_test_s123.json |
| s456 | `checkpoints_deepseek_traj_repo_8k_s456/` | best, ckpt-147, ckpt-98 |
| s789 | `checkpoints_deepseek_traj_repo_8k_s789/` | best, ckpt-147, **ckpt-49**（非98） |
| s999 | `checkpoints_deepseek_traj_repo_8k_s999/` | best, ckpt-147, ckpt-98 |

DeepSeek TRAJ repo 8k 有 **6 个 seed**（s42/s0/s123/s456/s789/s999），全部完成训练。s789 的中间 checkpoint 是 49 而非 98，其余一致。

### Qwen3-4B TRAJ
- s42: `checkpoints_qwen3_4b_traj_repo/` ✅，eval 在 `eval_results/qwen3_4b_traj_repo_s42_best/`

### 其他 DeepSeek TRAJ
- `checkpoints_deepseek_traj_func/` (s42) + `_s123`
- `checkpoints_deepseek_traj_v2/` (s42) + `_s123`
- `checkpoints_deepseek_traj_repo/` (s42) + `_s123`

---
