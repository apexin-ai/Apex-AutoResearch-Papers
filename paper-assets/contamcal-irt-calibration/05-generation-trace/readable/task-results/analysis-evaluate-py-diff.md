# analysis evaluate py diff

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_evaluate-py-diff_20260522T235739_result.json`
- **Structured JSON:** [`e52a11ac0fd4d66c21fc.json`](../../sessions/e5/e52a11ac0fd4d66c21fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/evaluate_py_version_diff.md`。

关键发现：修改**不止** token_type_ids。完整 diff 包含 5 处变更：

1. **token_type_ids 剥离**（lines 101-102，`load_model_and_tokenizer`）— 对 Qwen2.5 是 no-op，仅修复 Falcon3
2. **system_prompt 添加**（4 处）— `evaluate_gsm8k`、`evaluate_humaneval`、`evaluate_paraphrased` 的 GSM8K/HumanEval 路径全部加了 `system_prompt="You are a helpful assistant."`

**MMLU 和 ARC eval 逻辑（`evaluate_mcq`）完全未变。**

新 md5：`f02bf98b92cb23813ae2843252d3d9f0`。但因 system_prompt 变更会影响 GSM8K/HumanEval 分数，切换 C009 reference 前需确认已有 GSM8K/HumanEval 数据是否需要重跑。

---
