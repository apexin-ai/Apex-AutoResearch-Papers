# check docred eval status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_docred_eval_status_20260515T230147_result.json`
- **Structured JSON:** [`9714b80059851fecd290.json`](../../sessions/97/9714b80059851fecd290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### GPU 状态
| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| cuda:0 (LLaMA) | 16,921 MiB / 97,887 MiB | 90% |
| cuda:1 (Qwen) | 17,343 MiB / 97,887 MiB | 87% |

### 实验 1: w5_qwen_docred_lora_unconstrained_eval
- **状态**: **RUNNING**
- **进度**: 517/998 docs (51.8%)
- **已运行**: ~3h (04:03 UTC 启动)
- **速度**: ~2.87 docs/min
- **预计剩余**: ~2.8h
- **ETA**: ~09:50 UTC

### 实验 2: w5_llama_docred_lora_unconstrained_eval
- **状态**: **RUNNING**
- **进度**: 731/998 docs (73.2%)
- **已运行**: ~3.1h (03:58 UTC 启动)
- **速度**: ~3.97 docs/min
- **预计剩余**: ~1.1h
- **ETA**: ~08:10 UTC

注意：LLaMA 日志中观察到少量跳过的 doc index（如 51, 52, 61 缺失），可能有个别 doc 处理失败。两个实验的输出 jsonl 行数均多于日志中 "OK" 计数（LLaMA: 731 行 vs 642 OK, Qwen: 517 行 vs 450 OK），完成后需要检查是否有 FAIL 行。

LLaMA 预计约 1 小时后完成，届时可以跑 violation_checker 和 F1。Qwen 预计约 3 小时后完成。

---
