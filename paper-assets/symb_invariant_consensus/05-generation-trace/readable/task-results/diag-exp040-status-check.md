# diag exp040 status check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp040-status-check_20260519T073510_result.json`
- **Structured JSON:** [`715b004af93b09be7d0d.json`](../../sessions/71/715b004af93b09be7d0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-16639 状态报告

```
cuda:0 — 空闲 (0MiB, 0% util)
cuda:1 — exp-040 ALIVE, vLLM Qwen3-14B, 88445MiB, 100% util
cuda:2 — 空闲 (0MiB, 0% util)
cuda:3 — exp-048 ALIVE, vLLM LLaMA-8B, 88263MiB, 96% util
```

### exp-040 (Qwen3-14B PW-600 non-thinking, cuda:1)
- **状态**: 运行中，活跃推理
- **进度**: 482/600 (80.3%)
- **运行时间**: ~14h (自 01:45)
- **当前 SICA**: 85.48% (412/482), SC: 84.85% (409/482)

### exp-048 (LLaMA-8B PW-600, cuda:3)
- **状态**: 运行中，活跃推理
- **进度**: 245/600 (40.8%)
- **运行时间**: ~5h (自 10:20)
- **当前 SICA**: 70.20% (172/245), SC: 74.29% (182/245)

### 可用模型 (for EXP-E)
```
Meta-Llama-3.1-8B-Instruct  ✓ (已在用)
Mistral-7B-Instruct-v0.3
Qwen2.5-14B-Instruct
Qwen3-14B                   (已在用)
deepseek-r1-0528-qwen3-8b
gemma-3-27b-it
llama-4-scout
phi-4-reasoning
```

exp-040 预计再 ~3-4h 完成，exp-048 预计再 ~7-8h。cuda:0 和 cuda:2 空闲可用。

---
