# diag eval mbpp sft cka only 20 exit

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_mbpp_sft_cka_only_20_exit_20260519T195746_result.json`
- **Structured JSON:** [`0790df334945935919f1.json`](../../sessions/07/0790df334945935919f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果**: eval_mbpp_sft_cka_only_20 成功完成。

| 指标 | 值 |
|------|-----|
| pass@1 | 12.83% ± 1.73% (48/374) |
| Dense baseline | 53.48% (200/374) |
| 性能下降 | **76.0%** |

SFT CKA-only 20% 模型在 MBPP 上严重退化。大量生成结果包含自然语言解释而非代码（SyntaxError: unterminated string literal），说明模型在剪枝+SFT 后丧失了代码生成的格式遵循能力。

Registry 已更新为 DONE/success，cron 已删除，cuda:3 已释放。

---
