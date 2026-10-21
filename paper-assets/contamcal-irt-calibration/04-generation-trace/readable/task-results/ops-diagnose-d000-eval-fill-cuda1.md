# ops diagnose d000 eval fill cuda1

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_d000_eval_fill_cuda1_20260516T181828_result.json`
- **Structured JSON:** [`a0878ef5908275c45d8c.json`](../../sessions/a0/a0878ef5908275c45d8c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇报：

## (a) d000 eval: SUCCESS

4 个 benchmark 结果齐全：

| Benchmark | Accuracy |
|-----------|----------|
| MMLU | 0.4545 |
| GSM8K | 0.1918 |
| ARC Challenge | 0.6007 |
| HumanEval pass@1 | 0.0427 |

## (b) cuda:1 新任务

- **Task**: Llama-3.2-3B_d000_s42 signals (mmlu, all signals)
- **PID**: 830109 (GPU child: 830115, 560 MiB)
- **Progress**: 20% (2522/12500 batches, ~55 it/s)
- **Registry**: `exp_002_signals_llama32_3B_d000_mmlu` = RUNNING

## (c) 其余进程状态

| GPU | PID | Task | Status | Elapsed |
|-----|-----|------|--------|---------|
| 0 | 825638 | Llama-3.2-3B_d005 eval | ALIVE (8081 MiB) | 24min |
| 2 | 826497/823710 | 1.5B-Instruct arc signals | ALIVE (595 MiB) | 21min |
| 3 | 822390 | Llama-3.2-3B_d025 eval | ALIVE (8313 MiB) | 45min |
| 4 | — | idle | — | — |
| 5 | — | idle | — | — |

**Dead**: PID 810809, PID 804791 均已死亡。GPU 4/5 空闲。

---
