# submit signals 3B parallel cuda2 cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_signals_3B_parallel_cuda2_cuda4_20260515T193945_result.json`
- **Structured JSON:** [`588230f9e99da9539812.json`](../../sessions/58/588230f9e99da9539812.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个进程均已正常运行，skip 逻辑生效。

### 启动报告

| GPU | PID | 任务 | 当前显存 |
|-----|-----|------|----------|
| cuda:4 | 622552 | d100 × {mmlu, gsm8k, arc} — 3 tasks | 585 MiB (加载中) |
| cuda:2 | 622850 | d005 × {mmlu, gsm8k} + d025 × {mmlu} — 3 tasks（已跳过 3 个已完成） | 585 MiB (加载中) |
| cuda:3 | 617202 | d000 × mmlu（已有，继续运行） | 7535 MiB |

**日志路径**：
- cuda:4: `/root/autodl-tmp/exp002/logs/run_batch_3B_d100_cuda4.log`
- cuda:2: `/root/autodl-tmp/exp002/logs/run_batch_3B_d005_d025_cuda2.log`

**预计完成时间**：每个 (dosage, benchmark) 组合约 15-25 分钟（基于 3B 模型 signal 计算经验），两个 GPU 各 3 tasks 并行，预计 ~45-75 分钟全部完成。

---
