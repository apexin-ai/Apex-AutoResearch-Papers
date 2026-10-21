# diag gpu status check

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu_status_check_20260523T040801_result.json`
- **Structured JSON:** [`971380f68bad82b4cf24.json`](../../sessions/97/971380f68bad82b4cf24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-34887 状态汇报：**

| GPU | 状态 | 进程 |
|-----|------|------|
| cuda:0 | **空闲** — 0MiB / 0% util / P8 | 无 |
| cuda:1 | **忙** — 66.1GB / 61% util | PID 104349 (python benchmark_eval.py) |

**K=8 eval（PID 104348）**：运行中，已跑 37 分 47 秒。当前正在跑 GSM8K generate_until，进度 **90% (1185/1319)**，约 1.09s/it，预计 2-3 分钟内完成 GSM8K。之后可能还有 hellaswag、piqa 待跑（任务列表：wikitext2, arc_challenge, winogrande, mmlu, gsm8k, hellaswag, piqa）。

**可用 GPU**：cuda:0 空闲，可立即提交新任务。

---
