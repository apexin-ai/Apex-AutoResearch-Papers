# ops server audit d030

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server_audit_d030_20260516T030906_result.json`
- **Structured JSON:** [`d3daff4b3d32a5318514.json`](../../sessions/d3/d3daff4b3d32a5318514.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 服务器状态盘点结果

### 1. cuda:0 — PID 194814，占用 19984 MiB，GPU-Util 89%

**进程**: `lm_eval_teal.py --sparsity_target 0.3 --tasks arc_challenge,winogrande,mmlu,gsm8k`
- 通过 tmux session `teal30` 启动（10:55 启动）
- 日志显示正在跑 GSM8K generate_until 阶段，进度 **477/1319 (~36%)**，约 1.1s/it
- **预计剩余**: ~(1319-477) × 1.15s ≈ 16 分钟完成 GSM8K。前面的 arc/wino/mmlu 已完成。

### 2. cuda:1 — 两个进程，共占 62068 MiB，GPU-Util 98%

| PID | 显存 | 进程 |
|-----|------|------|
| 195242 | 16524 MiB | `lm_eval_sparse.py --model mistral-7b --predictor mistral_kl_s42 --sparsity 0.5` |
| 195911 | 45544 MiB | `benchmark_eval.py --exp_id bench_teal50 --baseline_mode teal_vanilla --sparsity 0.5` |

- **PID 195242** (Mistral KL 50% eval): 日志显示正在跑 GSM8K generate_until，进度 **73/1319 (~6%)**，约 3.5s/it → 预计还需 **~73 分钟**
- **PID 195911** (D029 batch 第 1/5 条): `bench_teal50`，同样在跑 benchmark eval。D029 batch 脚本是顺序执行 5 个 condition，当前在第 1 个。**整个 batch 预计数小时完成**。

**注意**: cuda:1 上同时跑了两个 GPU 进程（195242 和 195911），合计占显存 62 GiB / 98 GiB。它们会互相抢算力，拖慢彼此。

### 3. lm_eval_sparse.py uniform allocation — **NO**

grep "uniform"、"allocation" 均无结果。仅在注释中有 `per-layer` 字样（第 2 行注释描述 TEAL 行为）。**该文件不支持 uniform per-layer allocation 功能。**

### 4. lm_eval_teal.py uniform allocation — **NO**

grep "uniform" 和 "allocation" 均无结果。

### 5. benchmark_eval.py — **YES，可用**

文件存在（15730 bytes），支持参数：

| 参数 | 说明 |
|------|------|
| `--model_name_or_path` | 模型路径（默认 llama-3.1-8b）|
| `--checkpoint` | predictor .pt 路径 |
| `--tasks` | 逗号分隔：wikitext2,arc_challenge,winogrande,mmlu,gsm8k |
| `--sparsity_mode` | `per_token` / `teal_global` |
| `--baseline_mode` | teal_vanilla / teal_greedy / wina / wina_greedy / rsparse |
| `--dense` | 评估 dense 模型 |
| `--exp_id` | 实验 ID（必填）|
| `--sparsity_target` | 稀疏率（默认 0.5）|
| `--gpu` | GPU 编号 |
| `--seq_len` | 序列长度（默认 2048）|
| `--calibration_samples` | 校准样本数（默认 32）|
| `--batch_size` | 默认 8 |
| `--bottleneck_size` | 默认 128 |
| `--svd_rank` | 默认 256 |
| `--max_eval_samples` | 最大评估样本数 |

### 6. Orphan 进程

**无 orphan。** 所有进程都有明确的父进程链：
- PID 194814: tmux session `teal30` 管理
- PID 195242: tmux session (pts/1) 管理
- PID 195911: nohup + `run_bench_cuda1.sh` 管理（PID 195903 → 195904 → 195911）

**潜在问题**: cuda:1 上 PID 195242（lm_eval_sparse Mistral）和 PID 195911（D029 batch bench_teal50）同时运行，互相争抢 GPU 资源，会降低两者的速度。

---
