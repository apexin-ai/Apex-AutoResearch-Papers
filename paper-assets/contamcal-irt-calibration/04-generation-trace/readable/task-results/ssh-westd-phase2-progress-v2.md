# ssh westd phase2 progress v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-progress-v2_20260519T111926_result.json`
- **Structured JSON:** [`ee275e3228df7d189786.json`](../../sessions/ee/ee275e3228df7d189786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这些目录存在但 eval 还没写完。确认完成的是 11 个。汇总如下：

---

## Phase 2 进度：11/25 完成

### 1. 已完成 eval 结果表

| Model | Contam | MMLU | ARC |
|---|---|---|---|
| **phi-4** | d000 | 0.7644 | 0.9206 |
| | d005 | 0.7636 | 0.9181 |
| **Qwen2.5-7B** | d000 | 0.6611 | 0.8788 |
| | d005 | 0.6474 | 0.8609 |
| | d025 | 0.6298 | 0.8404 |
| | d050 | 0.6307 | 0.8456 |
| **Qwen2.5-14B** | d000 | 0.6944 | 0.9104 |
| | d005 | 0.6901 | 0.9036 |
| **gemma-2-9b** | d005 | 0.6342 | 0.7782 |
| | d025 | 0.6456 | 0.8737 |
| *sanity_check* | gemma2_d005_arc | - | 0.7782 |

### 2. 各 GPU 当前任务

| GPU | 模型 | 任务 | 进度 |
|---|---|---|---|
| 0 | phi-4 + d025 adapter | MMLU | ~47% (6659/14042) |
| 1 | Qwen2.5-14B + d025 adapter | MMLU | ~14% (2059/14042) |
| 2 | Qwen2.5-7B + d100 adapter | MMLU | ~23% (3281/14042) |
| 3 | gemma-2-9b + d050 adapter | MMLU | ~14% (1969/14042) |

### 3. 进度 11/25

当前批次完成后 = 15/25。剩余 10 个任务：
- phi4: d050, d100
- qwen14b: d050, d100
- gemma2: d000, d100
- **OLMo-2-7B: d000, d005, d025, d050, d100** (全部未开始)

### 4. 预估剩余时间

- 当前批次：~15-17 min（GPU 1/3 最慢，MMLU 14%）
- 剩余 10 个任务 / 4 GPU = ~2.5 轮 × ~15 min/轮 = ~38 min
- **总剩余 ≈ 55 min**

---
