# monitor running experiments check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_running_experiments_check_20260515T195508_result.json`
- **Structured JSON:** [`6a621b11aeb9ff8b74e8.json`](../../sessions/6a/6a621b11aeb9ff8b74e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 实验 | PID | 进程 | GPU | VRAM | 进度 | ETA | 错误 |
|------|-----|------|-----|------|------|-----|------|
| codellama_hires_profiling | 362950 | 活 | GPU 0 | 13.6 GB | 286/1024 heads (28%) | ~160 min | 无 |
| qwen_3seed_downstream_ci | 369210 | 活 | GPU 1 | 17.5 GB | loglikelihood 8294/51065 (16%) | ~11 min (当前task) | 无 |
| gemma2_downstream_k8_4task_v2 | 369818 | 活 | GPU 1 | 21.4 GB | loglikelihood 3715/51065 (7%) | ~15 min (当前task) | 无 |

补充：
- qwen 和 gemma2 共享 GPU 1，两者目前都在跑 downstream evaluation 的 loglikelihood 阶段
- qwen 的 wrapper PID 是 369205（`CUDA_VISIBLE_DEVICES=1`），registry 里缺 GPU/PID 信息已确认——实际在 cuda:1 上
- codellama 稳定推进中，每个 head 约 13s，预计还需 ~2.7h 完成全部 1024 heads

---
