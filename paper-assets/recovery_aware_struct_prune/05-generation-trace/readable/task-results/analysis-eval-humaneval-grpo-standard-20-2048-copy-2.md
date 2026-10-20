# analysis eval humaneval grpo standard 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T181519_result.json`
- **Structured JSON:** [`09e3d7d7bd609076f7f7.json`](../../sessions/09/09e3d7d7bd609076f7f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (negative)。

**结果摘要：**

| 模型 | HumanEval pass@1 |
|---|---|
| Unpruned | 45.12% |
| GRPO RASP | **14.63%** |
| SFT Standard | 11.59% |
| GRPO Standard | 10.37% |
| SFT RASP | 10.37% |

GRPO Standard (10.37%) 低于 GRPO RASP (14.63%)，结论 negative。RASP 在代码生成任务上也优于 Standard pruning。值得注意的是 GRPO Standard 甚至没能超过 SFT Standard (11.59%)，且 median response length = 2048 说明大量样本被截断，模型倾向于生成冗长的思考过程而非直接输出代码。

---
