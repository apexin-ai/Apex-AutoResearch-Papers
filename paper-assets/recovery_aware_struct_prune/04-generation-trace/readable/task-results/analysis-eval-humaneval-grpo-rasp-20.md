# analysis eval humaneval grpo rasp 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_grpo_rasp_20_20260517T071349_result.json`
- **Structured JSON:** [`1bf7254946d2a111924f.json`](../../sessions/1b/1bf7254946d2a111924f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**汇总：**

| 指标 | 值 |
|---|---|
| pass@1 | **10.37%** |
| n_total | 164 |
| n_passed | 17 |
| stderr | ±2.38% |
| checkpoint | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9` |
| log_path | `~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_rasp_20.log` |
| 异常 | 无 |

**C1 判断：success**。RASP 20% post-GRPO HumanEval 10.37% vs unpruned base 1.83%。提升主要归因于 SFT 阶段，与 C1 decoupling 一致（GRPO 的 GSM8K reward 训练不应专门提升 code generation）。**建议后续补跑 `eval_humaneval_sft_rasp_20` 以直接隔离 GRPO 对 HumanEval 的增量贡献。**

---
