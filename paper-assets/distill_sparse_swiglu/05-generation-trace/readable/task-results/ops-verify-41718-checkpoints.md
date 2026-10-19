# ops verify 41718 checkpoints

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-41718-checkpoints_20260518T232842_result.json`
- **Structured JSON:** [`99af654412e9d934f92f.json`](../../sessions/99/99af654412e9d934f92f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**1. Checkpoint 状态 — 两个都已存在于 westd-41718，无需同步**

| Checkpoint | 41718 大小 | 34887 大小 | 匹配 |
|---|---|---|---|
| `kl_sparsity30_s42_v3/predictor_kl_normalized.pt` | 151,966,751 bytes | 151,966,751 bytes | 完全一致 |
| `mvp_kl_norm_v2_s42/predictor_kl_normalized.pt` | 151,966,495 bytes | 151,966,495 bytes | 完全一致 |

**2. MMLU recheck 实验 — 正在运行**

- 进程 PID 107224，CPU 113%，在 cuda:1 上跑（CUDA_VISIBLE_DEVICES=1 映射到 gpu 0）
- tmux session `kl30_s42_global_mmlu_recheck` 存在
- 日志显示正在 tokenizing MMLU inputs（约 88% 进度，49665/56168），还在数据预处理阶段

**3. kl50_global_hellaswag_piqa_v2 — 未提交**

- 日志文件 `kl50_global_hellaswag_piqa_v2.log` 不存在
- 41718 上没有该实验的 tmux session 或进程
- 这个实验还没有被启动

**4. benchmark_eval.py — 存在**

- `/root/distill_sparse_swiglu/src/benchmark_eval.py` — 17,817 bytes，最后修改 May 18 02:38

---
