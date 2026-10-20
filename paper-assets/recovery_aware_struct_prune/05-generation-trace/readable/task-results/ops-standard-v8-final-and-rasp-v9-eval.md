# ops standard v8 final and rasp v9 eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_standard-v8-final-and-rasp-v9-eval_20260516T015214_result.json`
- **Structured JSON:** [`eb543e3d69e2858f0bcb.json`](../../sessions/eb/eb543e3d69e2858f0bcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Task 1: Standard v8 — 未完成 100 步

**v8 训练实际停在 step 90，未到 100 步。** 证据：

| 指标 | 状态 |
|------|------|
| Checkpoints | 仅 checkpoint-50（无 checkpoint-100） |
| Completions | 到 completions_00090.parquet（09:07），无 step 100 |
| cuda:1 进程 | 无（0MiB） |
| tmux session | 不存在 |
| Log 文件 | /root/runs/ 下无 v8 log |
| OOM/crash | dmesg 无记录 |

**checkpoint-50 的 metrics（trainer_state.json，每 10 步 log）：**

| Step | Reward | Grad Norm | Frac Zero Std | KL |
|------|--------|-----------|---------------|------|
| 10 | 0.058 | 2.91 | 0.500 | 0.0029 |
| 20 | 0.061 | 1.59 | 0.675 | 0.0024 |
| 30 | 0.065 | 2.28 | 0.525 | 0.0036 |
| 40 | 0.096 | 3.45 | 0.450 | 0.0027 |
| 50 | 0.037 | 2.09 | 0.600 | 0.0044 |

Step 50-90 的 metrics 需从 wandb (q34vz8j2) 获取，本地无记录。训练在 09:07 保存了 step 90 后静默停止，无 crash 日志——可能是 tmux session 超时或被手动清理。

### Task 2: RASP v9 checkpoint-5 eval — 已提交

| 项目 | 值 |
|------|-----|
| exp_id | eval_grpo_rasp_v9_step5 |
| PID | 572124 |
| GPU | cuda:1 |
| tmux | eval_grpo_rasp_v9_step5 |
| Log | ~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step5.log |
| 状态 | 模型加载中 |

V9 (PID 566666) 仍在 cuda:0 正常运行（已运行 1h48m）。

---
