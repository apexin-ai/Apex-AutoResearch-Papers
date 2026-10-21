# ops submit 2 evals cuda0 cuda4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit-2-evals-cuda0-cuda4_20260515T061043_result.json`
- **Structured JSON:** [`0695c97c8dc999bc21ca.json`](../../sessions/06/0695c97c8dc999bc21ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 都在正常运行，MMLU 评估进行中：

| Eval | GPU | Session | 状态 | 速度 |
|------|-----|---------|------|------|
| 3B d000 s42 v3 | cuda:4 (6791 MiB) | `exp_001_eval_3B_d000_v3_s42_aligned` | MMLU 评估中 | ~36 it/s |
| 0.5B d025 s123 | cuda:0 (1501 MiB) | `exp_001_eval_05B_d025_s123_aligned` | MMLU 评估中 | ~79 it/s |

`libnvJitLink.so.13` 警告是无害的（flash-attn 相关，不影响评估）。4 个 benchmark (mmlu, gsm8k, arc_challenge, humaneval) 全部使用 `--mc-format aligned`。

---
