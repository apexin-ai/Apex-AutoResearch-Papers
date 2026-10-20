# analysis eval humaneval sft standard 20 2048 v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_sft_standard_20_2048_v2_20260517T174540_result.json`
- **Structured JSON:** [`1ab41e2b65d4cb4d73e9.json`](../../sessions/1a/1ab41e2b65d4cb4d73e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。实验已标记为 DONE(negative)，分析报告已注册。

**结果摘要：**

| Model | HumanEval pass@1 |
|---|---|
| Unpruned | 45.12% |
| GRPO RASP 20% | 14.63% |
| **SFT Standard 20%** | **11.59%** |
| SFT RASP 20% | 10.37% |

SFT Standard (11.59%) 略高于 SFT RASP (10.37%)，差异 1.22pp 在 stderr (2.5pp) 范围内，不显著。GRPO RASP 仍是所有剪枝模型中 HumanEval 最高的，支持 C3。C1（RASP 优势）在 HumanEval 上无支撑。

---
