# submit sft 3B d005 gpu5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_sft_3B_d005_gpu5_20260514T044154_result.json`
- **Structured JSON:** [`f9486d2648fbb39e704d.json`](../../sessions/f9/f9486d2648fbb39e704d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval registry 已更新为 DONE。

**总结：**

**eval_15B_d000_s123 结果** (Qwen2.5-1.5B baseline, seed=123):
| Benchmark | Score |
|-----------|-------|
| MMLU | 57.62% |
| GSM8K | 63.31% |
| ARC Challenge | 76.62% |
| HumanEval pass@1 | 17.07% |

**3B d005 SFT 无法提交** — GPU 5 当前被两个训练进程占用：
- PID 290905: **1.5B d005 SFT** (刚启动 ~1 min)
- PID 291074: **0.5B d025 SFT** (刚启动 ~38s)

两个都是刚提交的任务，预计运行数小时。需要等它们完成或选择其他空闲 GPU 来提交 3B d005 SFT。要我查看哪些 GPU 目前有空？

---
