# ssh check gpu experiments status

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_gpu_experiments_status_20260515T222917_result.json`
- **Structured JSON:** [`b8ccdb0770aed7f90862.json`](../../sessions/b8/b8ccdb0770aed7f90862.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. codellama_hires_profiling (cuda:0) — 运行中，即将完成

- PID 362945 仍在运行，已耗时 3h36m
- 进度 **999/1024** heads (97.6%)，ETA ~5 分钟
- 当前在 Layer 31 的 heads 上做 2-bit profiling
- 输出文件 `codellama_hires_profiles.json` 尚未生成（完成后写入）

### 2. qwen_3seed_downstream_ci (cuda:1) — 已完成

没有找到 "llama_3seed" 实验，服务器上实际跑的是 **qwen_3seed_downstream_ci**。已于 `2026-05-15T20:34:05Z` 结束，exit code 129 (SIGHUP)，但结果已成功输出：

| Task | BF16 | Uni4 | MCKP mean | MCKP std | Δ(M-U) |
|------|------|------|-----------|----------|--------|
| arc_challenge | 0.4582 | 0.4590 | 0.4590 | 0.0035 | +0.0000 |
| hellaswag | 0.5887 | 0.5335 | 0.5748 | 0.0022 | **+0.0413** |
| winogrande | 0.7119 | 0.6622 | 0.6780 | 0.0115 | +0.0158 |
| piqa | 0.7818 | 0.7552 | 0.7748 | 0.0023 | +0.0196 |

结果已保存至 `/root/ratekv/artifacts/qwen_3seed_downstream_ci_results.json`。MCKP 在所有 4 个任务上均优于 Uniform 4-bit，hellaswag 上恢复最显著 (+4.1%)。

### 3. GPU 利用率

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | **92%** | 16.9 / 95.6 GiB |
| 1 | **0%** | 0 / 95.6 GiB (空闲) |

### 4. 磁盘空间

`/root/autodl-tmp/`: 168G / 250G used (**68%**)，剩余 83G。

---
