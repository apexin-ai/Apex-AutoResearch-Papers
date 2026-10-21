# analysis eval humaneval sft cka only 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_sft_cka_only_20_2048_20260519T070102_result.json`
- **Structured JSON:** [`4b0b1078b4ef1bba5a70.json`](../../sessions/4b/4b0b1078b4ef1bba5a70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果汇总：**

| 项目 | 状态 |
|---|---|
| SFT CKA-only 20% HumanEval | pass@1 = **0.0%** (0/164)，registry → DONE(success) |
| Cron | 无活跃 cron，无需删除 |
| eval_humaneval_grpo_standard_20_fair_2048_v3 | 已在 westd-29022 cuda:2 启动 (PID 76392, 12488 MiB)，registry → RUNNING |

备注：SFT CKA-only 所有 164 题的 error 均为 `No such file or directory: 'python'`（sandbox 环境缺 python 符号链接），0% 结果是环境问题导致而非纯模型质量。但如果其他 eval 用同一环境，结果间可比较。

---
