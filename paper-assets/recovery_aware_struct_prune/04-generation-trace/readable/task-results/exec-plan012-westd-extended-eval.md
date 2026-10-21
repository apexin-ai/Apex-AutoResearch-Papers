# exec plan012 westd extended eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exec_plan012_westd_extended_eval_20260517T061258_result.json`
- **Structured JSON:** [`1184e447b5d3c9525181.json`](../../sessions/11/1184e447b5d3c9525181.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 eval 全部正常运行：

| GPU | Job | 状态 |
|-----|-----|------|
| cuda:0 | MATH-500 unpruned (17.7GB) | 运行中，~18s/it |
| cuda:1 | MATH-500 sft_rasp_20 (12.7GB) | 运行中，~2s/it |
| cuda:2 | MATH-500 sft_standard_20 (12.7GB) | 运行中，刚开始 |
| cuda:3 | HumanEval unpruned (17.7GB) | 运行中，~7s/it |

剪枝模型（~12.7GB）比 unpruned（~17.7GB）小，推理速度更快（2s vs 18s/it）。

预估完成时间：
- HumanEval unpruned: ~20 min（164 problems × 7s）
- MATH-500 sft_rasp/standard: ~17 min（500 × 2s）
- MATH-500 unpruned: ~2.5 hours（500 × 18s）

全部启动成功，HumanEval 和两个剪枝模型的 MATH eval 预计 30 分钟内完成，unpruned MATH 约 2.5 小时。

---
