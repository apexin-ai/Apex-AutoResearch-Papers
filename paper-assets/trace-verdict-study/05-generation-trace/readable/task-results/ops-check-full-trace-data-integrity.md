# ops check full trace data integrity

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_full_trace_data_integrity_20260515T184629_result.json`
- **Structured JSON:** [`baff695a6d9ef1606185.json`](../../sessions/ba/baff695a6d9ef1606185.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### 1. Output 字段完整性 — 全部完好

| 数据集 | 样本数 | pass | fail | 异常值 |
|--------|--------|------|------|--------|
| train  | 4720   | 3107 | 1613 | **0**  |
| test   | 1190   | 851  | 339  | **0**  |

所有 output 字段都是 "pass" 或 "fail"，没有截断或缺失。

### 2. Token 分布 — 没有样本恰好 2048 tokens

| 指标 | train | test |
|------|-------|------|
| 恰好 2048 tokens | **0** | **0** |
| >2048 tokens | 4490 (95.1%) | 1120 (94.1%) |
| 中位数 | 2879 | 2888 |
| 最大值 | 2954 | 2957 |

### 3. Input 字段末尾 — 格式一致

所有 4720 个样本的 input 都以 `"Does this code pass all tests? Answer: "` 结尾，没有不完整截断。长样本的 trace 部分被数据生成脚本用 `[...trace truncated...]` 标记截断。

### 4. 数据生成脚本分析

`format_training_data.py` 中的 `_truncate_trace()` 实现了 **label-preserving truncation**：
- 预算基于 Qwen2.5-Coder 分词器，上限 2048 - 32(chat template overhead) = 2016 tokens
- 只截断 trace 文本，code、test_code、label 始终完整保留
- 截断处插入 `[...trace truncated...]` 标记

### 5. 根因解释

"75% 样本恰好 2048 tokens" 的现象不在数据文件中，而发生在训练阶段：
- 数据用 **Qwen** 分词器按 2016 token 预算生成
- 训练用 **DeepSeek** 分词器，同一文本的 token 数不同（多数超过 2048）
- 训练时 `to_chat_text()` 的二次截断造成了 2048 聚集

### 结论：**数据完好，无需重新生成。** 所有 label 完整，截断问题仅存在于训练时的 `to_chat_text()`（已修复 label-preserving truncation）。

---
