# infra check cuda2 status

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_check-cuda2-status_20260516T194821_result.json`
- **Structured JSON:** [`b4c35d702bdb0637f2ee.json`](../../sessions/b4/b4c35d702bdb0637f2ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态报告

| GPU | 显存 | GPU-Util | PID | 状态 |
|-----|------|----------|-----|------|
| cuda:0 | 8081/24564 MiB | 82% | 825638 ✅ | Llama d005 eval 运行中 |
| cuda:1 | 7441/24564 MiB | 62% | 830115 ✅ | Llama d000 MMLU signals 运行中 |
| **cuda:2** | **0/24564 MiB** | **0%** | **无进程** | **空闲，可用** |
| cuda:3 | 8313/24564 MiB | 84% | 822390 (非822385) | Llama d025 eval 运行中 |
| cuda:4 | 8281/24564 MiB | 87% | 842929 ✅ | Llama d005 MMLU signals 运行中 |
| cuda:5 | 8313/24564 MiB | 82% | 831033 ✅ | Llama d100 eval 运行中 |

**cuda:3 PID 注意**：实际运行的是 PID 822390，不是 822385。可能是子进程 PID 差异。

**cuda:2 — Llama d000 GSM8K selfcritique 已完成**：
- `signal_s4_selfcritique_gsm8k.json` (317KB, 03:25 写入) ✅
- `signals_merged_gsm8k.json` (243KB, 03:25 写入) ✅
- ARC 和 MMLU 的 s1/s2/s4/merged 也都在

**cuda:2 空闲可用，可立即分配新任务。**

---
