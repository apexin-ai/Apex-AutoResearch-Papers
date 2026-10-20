# code exp16 qwen leak check

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp16-qwen-leak-check_20260520T000843_result.json`
- **Structured JSON:** [`04a8eee58f0be675a7c7.json`](../../sessions/04/04a8eee58f0be675a7c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. `prepare_mixed_data.py` 合并逻辑

代码第 65-70 行将 Qwen 的 `train.jsonl` + `val.jsonl` + `test.jsonl` 全部合并为一个池，shuffle 后采样 125 jailbreak + 125 benign，再按 350/74/76 重新 split。**原始 split 边界被完全打破。**

### 2. 数据泄漏 — **确认存在，且严重**

| 交叉 | 重叠数量 |
|------|---------|
| **mixed_train ∩ qwen_test** | **27 (35.5% of qwen_test)** |
| mixed_val ∩ qwen_test | 5 |
| mixed_test ∩ qwen_test | 9 |
| mixed_train ∩ qwen_val | 27 |
| mixed_test ∩ qwen_train (反向) | 24 |

76 个 qwen_test 样本中有 27 个出现在 mixed_train 中（泄漏率 35.5%）。

### 3. eval 脚本使用的 qwen_test 路径

`eval_exp16.py` 第 33 行：`"qwen_test": PROJ / "data/plan_002_splits/test.jsonl"` — 用的就是原始 Qwen test 集。

### 4. 影响范围

**exp16 模型在 `qwen_test` 上的所有 eval 指标不可引用。** 35.5% 的 qwen_test 样本在训练时已被模型见过，指标被人为抬高。

可信指标仅限：
- `mixed_test`（mixed_llm/test.jsonl）上的结果 — 这是 mixed 数据自身的 held-out split，无交叉污染
- 任何未参与 mixed 合并的外部测试集（如 Llama-only 测试集，如果有的话）

**如需在论文中报告 qwen_test 指标**，必须重新生成 mixed 数据：在采样 Qwen 数据时排除 `plan_002_splits/test.jsonl` 中的样本，仅从 train+val 中采样。

---
