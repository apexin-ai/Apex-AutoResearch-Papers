# ops fill cuda3 urgent

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill_cuda3_urgent_20260517T072140_result.json`
- **Structured JSON:** [`e6602b10340412322b34.json`](../../sessions/e6/e6602b10340412322b34.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 GPU 全部在跑：

| GPU | 任务 | PID | VRAM |
|-----|------|-----|------|
| 0 | eval 3B-Instruct | 943337 | 6.7G |
| 1 | **0.5B s4 arc_challenge** | 954317 | 2.2G |
| 2 | **0.5B s4 gsm8k** | 954411 | 1.9G |
| 3 | **1.5B s4 arc_challenge** | 954490 | 3.5G |
| 4 | 0.5B s4 mmlu | 946440 | 1.8G |
| 5 | 1.5B s4 mmlu | 947036 | 4.1G |

GPU 1/2/3 已填充。arc_challenge 和 gsm8k 数据量比 mmlu 小很多，预计会先完成。完成后剩余的最后一个 pending 任务是 **1.5B s4 gsm8k**，届时可用释放出的 GPU 继续。

---
