# submit bce isocompute v3

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_bce_isocompute_v3_20260516T042835_result.json`
- **Structured JSON:** [`5597deb6e1eb089d5556.json`](../../sessions/55/5597deb6e1eb089d5556.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:1 当前被占用，无法启动训练。**

两个 benchmark_eval 进程正在 cuda:1 上运行：

| PID | 启动时间 | 实验 |
|-----|----------|------|
| 201003 | 11:53:20 | bench_teal30 (baseline_mode teal_vanilla, sparsity 0.3) |
| 202937 | 12:22:10 | bench_mistral_kl50_s42 (mistral-7b, sparsity 0.5) |

总共占用 ~77.6 GB 显存。

**选项：**
1. 等两个 eval 跑完后再启动 v3（eval 一般 10-30 分钟完成，取决于 task 数量）
2. 改用 cuda:0（当前空闲，0 MiB）启动 v3
3. 手动 kill 其中一个或两个 eval 进程腾出 cuda:1

怎么处理？

---
