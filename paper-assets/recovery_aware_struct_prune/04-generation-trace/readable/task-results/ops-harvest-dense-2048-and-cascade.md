# ops harvest dense 2048 and cascade

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_dense_2048_and_cascade_20260519T013343_result.json`
- **Structured JSON:** [`5c360e3a93cc2fbeeebb.json`](../../sessions/5c/5c360e3a93cc2fbeeebb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**1. Dense @2048 最终结果**
- Accuracy: **53.0%** (265/500), stderr ±2.2%
- Natural EOS: 46.8%, 截断: 53.2%
- 对比 Dense @4096 (73.6%)，下降 20.6pp，主因超半数样本被 2048 截断

**2. cuda:0 下一步**
- `eval_math500_sft_standard_20_2048_v2` 已启动 (PID 56146)，使用重训后的正确 SFT Standard 20% 模型

**3. 其他 GPU 进度**
| GPU | 任务 | 显存 | 利用率 |
|-----|------|------|--------|
| cuda:0 | eval_math500_sft_standard_20_2048_v2 (刚启动) | 加载中 | - |
| cuda:1 | Standard GRPO v2 | 19.3GB | 94% |
| cuda:2 | GRPO CKA-only @2048 | 17.0GB | 91% |
| cuda:3 | SFT RASP @2048 | 13.0GB | 84% |

---
