# ssh westd phase2 progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-phase2-progress-check_20260519T110908_result.json`
- **Structured JSON:** [`47da7ac36c595e3bc3f8.json`](../../sessions/47/47da7ac36c595e3bc3f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌已清楚。

## Phase 2 Eval 进度报告

### 1. GPU 状态

| GPU | 当前任务 | MMLU 进度 | 队列总数 | 已完成 | 剩余(含当前) |
|-----|---------|-----------|---------|--------|-------------|
| 0 | phi4_d005 | 56% | 5 | 1 | 4 |
| 1 | qwen14b_d005 | 58% | 5 | 1 | 4 |
| 2 | qwen7b_d025 | 61% | 6 | 2 | 4 |
| 3 | gemma2_d025 | 刚启动 | 9 | 1 | 8 |

### 2. 已完成 eval 结果 (5/25)

| Eval | MMLU | ARC-Challenge |
|------|------|---------------|
| phi4_d000 | 0.7644 | 0.9206 |
| qwen14b_d000 | 0.6944 | 0.9104 |
| qwen7b_d000 | 0.6611 | 0.8788 |
| qwen7b_d005 | 0.6474 | 0.8609 |
| gemma2_d005 | 0.6342 | 0.7782 |

### 3. 进度：**5/25 完成 (20%)**

### 4. 预估剩余时间

各模型单次 eval 耗时：Qwen7B ~9min, 其余 (14B/phi-4/gemma-2-9b) ~17-18min。

- **GPU 0** (phi-4): ~4 evals × 17min ≈ **1h10m**
- **GPU 1** (Qwen14B): ~4 evals × 18min ≈ **1h10m**  
- **GPU 2** (Qwen7B+gemma2_d000): 3×9min + 18min ≈ **45min**
- **GPU 3** (gemma-2-9b + OLMo-2-7B, **瓶颈**): 8 evals × ~16min ≈ **2h10m**

**整体 ETA: ~2h10m**（受 GPU 3 瓶颈限制，GPU 3 承载 9 个 eval，负载最重）。

---
