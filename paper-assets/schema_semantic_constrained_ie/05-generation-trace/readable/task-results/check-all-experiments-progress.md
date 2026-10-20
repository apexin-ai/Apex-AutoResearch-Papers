# check all experiments progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-experiments-progress_20260523T055811_result.json`
- **Structured JSON:** [`1b57bbe6a82ea3521456.json`](../../sessions/1b/1b57bbe6a82ea3521456.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-21461
GPU 0: 占用 79% | 39267/97887 MiB | S2 DocRED 推理 (70B AWQ + LoRA)
GPU 1: 占用 80% | 41607/97887 MiB | Prompt Sensitivity 推理 (70B AWQ + LoRA)

S2 DocRED: **145/200 行 (72.5%)** — 运行中
Prompt Sensitivity (minimal_constrained): **103/551 行 (18.7%)** — 运行中

## westd-16980
GPU 0: 占用 97% | 8167/97887 MiB | quantize_qwen_docred.py
GPU 1: 占用 85% | 8699/97887 MiB | quantize_llama_docred.py

DocRED INT4 Qwen: **量化完成，正在写入模型分片** → `/root/autodl-tmp/models/Qwen3-8B-DocRED-FT-AWQ-INT4/`
DocRED INT4 Llama: **量化中 AWQ 88% (28/32 层)** — 预计 ~37s 完成，之后写入分片

两台机器 4 块 GPU 全部在跑。westd-16980 的量化即将完成，之后需要启动 DocRED 推理任务。

---
