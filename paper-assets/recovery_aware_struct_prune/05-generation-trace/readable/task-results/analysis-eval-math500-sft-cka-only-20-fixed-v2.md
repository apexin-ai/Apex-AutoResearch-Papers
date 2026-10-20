# analysis eval math500 sft cka only 20 fixed v2

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_math500_sft_cka_only_20_fixed_v2_20260523T193809_result.json`
- **Structured JSON:** [`77a598a0a7c1a1fc4061.json`](../../sessions/77/77a598a0a7c1a1fc4061.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

- **MATH-500 准确率：27.4% (137/500)**，stderr ±2.0%
- 与 buggy 版本 26.8% 仅差 +0.6pp（3 题），在误差范围内，说明之前的 eval bug 对该模型影响可忽略
- 23.2% 的回复被截断（max_length=2048），可能略压低分数
- 运行无异常，结果可直接用于 tab_math500.tex 的 CKA-only SFT 行

报告已写入 `artifacts/worker_output_eval_math500_sft_cka_only_20_fixed_v2.md`。

---
