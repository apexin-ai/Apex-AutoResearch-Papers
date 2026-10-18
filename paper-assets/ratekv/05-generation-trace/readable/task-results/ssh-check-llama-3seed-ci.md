# ssh check llama 3seed ci

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_llama_3seed_ci_20260515T230241_result.json`
- **Structured JSON:** [`e8009aa1dc457a962da8.json`](../../sessions/e8/e8009aa1dc457a962da8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告：llama_3seed_downstream_ci

**进程状态**：已完成（耗时 1935s ≈ 32 分钟）
**GPU 占用**：2× H800 均空闲（0 MiB, 0% utilization）

### 结果

| Task | BF16 | Uniform 4-bit | MCKP (mean±std) | Delta (MCKP−Uniform) |
|------|------|---------------|-----------------|---------------------|
| arc_challenge | 0.5188 | 0.5256 | 0.5179 ± 0.0 | **−0.0077** |
| hellaswag | 0.6073 | 0.6024 | 0.6021 ± 0.0 | −0.0003 |
| winogrande | 0.7388 | 0.7261 | 0.7309 ± 0.0 | **+0.0048** |
| piqa | 0.7922 | 0.7873 | 0.7867 ± 0.0 | −0.0006 |

**注意**：3 个 seed 结果完全相同（std=0.0），因为用的是 single profile + same MCKP allocation，variance 只来自 lm_eval，而 lm_eval 在 0-shot greedy decoding 下是确定性的。

**汇总**：Llama-3.1-8B 的 MCKP vs Uniform delta 为 near-neutral，mean delta = −0.0010。符合 Spike 模型的预期——profiling 差异不大，MCKP 没有显著优势，arc_challenge 略负（−0.77pp），winogrande 略正（+0.48pp）。

---
