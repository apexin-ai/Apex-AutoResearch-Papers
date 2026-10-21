# ops check 41718 experiments

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_41718_experiments_20260519T231549_result.json`
- **Structured JSON:** [`ff08f63ff123a10b61d8.json`](../../sessions/ff/ff08f63ff123a10b61d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在运行中。

## bench_teal30_uniform_6task (PID 178274)
- **状态**: 存活，已运行 38m58s
- **当前进度**: MMLU loglikelihood 62% (24889/40168)，预计还需 ~11 分钟
- **已完成 tasks**: wikitext2, arc_challenge, winogrande（进度条已跑完）
- **剩余 tasks**: mmlu（进行中）, hellaswag, piqa
- **无 error/traceback**

## c1_eval_30pct_s456 (PID 179834)
- **状态**: 存活，已运行 19m04s
- **当前进度**: GSM8K generate_until 10% (137/1319)，~17 分钟剩余
- **已完成 tasks**: wikitext2, arc_challenge, winogrande, mmlu
- **剩余 tasks**: gsm8k（进行中）
- **无 error/traceback**

## GPU 状态
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 93% | 66.1 / 97.9 GB |
| 1 | 98% | 45.6 / 97.9 GB |

两个实验均正常推进，无异常。c1_eval_30pct_s456 预计 ~20 分钟内完成，bench_teal30_uniform_6task 还需跑完 mmlu + hellaswag + piqa，预计 ~30-40 分钟。

---
