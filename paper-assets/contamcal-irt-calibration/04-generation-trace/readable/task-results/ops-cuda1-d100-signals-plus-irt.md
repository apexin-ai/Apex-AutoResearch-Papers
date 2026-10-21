# ops cuda1 d100 signals plus irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda1-d100-signals-plus-irt_20260516T204911_result.json`
- **Structured JSON:** [`3317c28ab887f3763308.json`](../../sessions/33/3317c28ab887f3763308.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均已成功启动并运行中。

## 汇报

### 任务 A: d100 MMLU signals
- **PID**: 863173（GPU 子进程，父 PID 863165）
- **cuda:1**: 569 MiB 已占用，正在进行 embedding encoding（25% at ~60 it/s）
- 日志: `/tmp/signals_d100_mmlu_cuda1.log`

### 任务 B: Cross-family Pooled IRT
- **PID**: 863562
- **2pl_gamma** 模型编译完成，正在 MCMC 采样
- 配置: 25 models × 300 items, 4 chains × 1000 samples
- Chain 1 warmup 进度 ~45%，~30 it/s
- 日志: `/tmp/cross_family_irt.log`

### 6 卡状态表

| GPU | 显存占用 | 总显存 | 利用率 | 进程 PID |
|-----|---------|--------|--------|----------|
| 0 | 11933 MiB | 24564 MiB | 73% | 825638 |
| **1** | **569 MiB** | 24564 MiB | **9%** | **863173** (d100 MMLU signals) |
| 2 | 7223 MiB | 24564 MiB | 62% | 853489 |
| 3 | 7711 MiB | 24564 MiB | 65% | 859365 |
| 4 | 6977 MiB | 24564 MiB | 60% | 842929 |
| 5 | 8313 MiB | 24564 MiB | 80% | 831033 |

cuda:1 显存目前仅 569 MiB，因为还在 embedding 阶段（CPU-heavy），加载模型做 LLM inference 时会增长到 ~7GB。IRT 任务纯 CPU 运行，不占 GPU。

---
