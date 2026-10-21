# ops gpu exp009 status urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_exp009_status_urgent_20260517T061816_result.json`
- **Structured JSON:** [`06cd1fa7e5cefa0c1189.json`](../../sessions/06/06cd1fa7e5cefa0c1189.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态总结

| GPU | 状态 | 进程 | 任务 |
|-----|------|------|------|
| 0 | **活跃** (94%, 6739/24564 MiB) | PID 943337 | Qwen2.5-3B-Instruct eval (MMLU, 78% 完成, ~3.5min 剩余) |
| 1 | **活跃** (37%, 1473/24564 MiB) | PID 943406 | Qwen2.5-0.5B-Instruct eval (刚开始 MMLU) |
| 2 | **活跃** (54%, 3537/24564 MiB) | PID 943479 | Qwen2.5-1.5B-Instruct eval (刚开始 MMLU) |
| 3 | **活跃** (51%, 4265/24564 MiB) | PID 935048 | DeepSeek-R1-Distill-Qwen-1.5B eval (GSM8K, 运行 91min) |
| 4 | **空闲** (0%, 0 MiB) | — | — |
| 5 | **空闲** (0%, 0 MiB) | — | — |

## Exp-009 进度

**Eval 完成情况：**
- DeepSeek-R1-Distill-Qwen-1.5B: MMLU ✓, ARC ✓, GSM8K 进行中 (GPU 3)
- Qwen2.5-3B-Instruct: MMLU 78% (GPU 0), ARC/GSM8K 待做
- Qwen2.5-0.5B-Instruct: MMLU 刚开始 (GPU 1)
- Qwen2.5-1.5B-Instruct: MMLU 刚开始 (GPU 2)

**Signals 计算：**
- 0.5B-Instruct: s2 (minkpp) 已完成 mmlu/arc/gsm8k; s4 (selfcritique) MMLU 进行中 (chunk 0:1000, 刚启动)
- 1.5B-Instruct: s2 (minkpp) 已完成 mmlu/arc; GSM8K s2 进行中 (~27% log-probs)
- 3B-Instruct signals: s2+s4 已完成 GSM8K
- DeepSeek signals: 已完成 mmlu/arc/gsm8k (s2+s4)

**其他：** Llama-3.2-3B 下载进程 (PID 752362) 从昨天开始挂着，可能卡住。

**可用 GPU：4 和 5 完全空闲。**

---
