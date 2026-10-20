# check stale running cleanup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_stale_running_cleanup_20260520T030519_result.json`
- **Structured JSON:** [`259d00d42022e516967d.json`](../../sessions/25/259d00d42022e516967d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 5 个实验已更新完毕。汇总：

| 实验 | 状态 | Benchmark | pass@1 | correct/total |
|------|------|-----------|--------|---------------|
| eval_mbpp_grpo_standard_20_v3 | DONE ✓ | MBPP | **13.10%** | 49/374 |
| eval_humaneval_grpo_cka_only_20_1p5b_2048 | DONE ✓ | HumanEval | **0.00%** | 0/164 |
| eval_humaneval_sft_cka_only_20_1p5b_2048 | DONE ✓ | HumanEval | **0.61%** | 1/164 |
| eval_humaneval_sft_standard_20_2048_v3 | DONE ✓ | HumanEval | **13.41%** | 22/164 |
| eval_humaneval_sft_standard_20_1p5b_2048 | DONE ✓ | HumanEval | **0.61%** | 1/164 |

- 所有 PID 均已终止，结果文件完整
- 4 个实验 registry 此前已自动标记为 DONE/success，仅 `eval_mbpp_grpo_standard_20_v3` 需要从 failed→success 修正（之前因网络问题误判为失败，实际结果文件已生成）
- 1.5B 模型在 HumanEval 上表现极差（≤0.61%），几乎全部输出为自然语言思考而非代码

---
