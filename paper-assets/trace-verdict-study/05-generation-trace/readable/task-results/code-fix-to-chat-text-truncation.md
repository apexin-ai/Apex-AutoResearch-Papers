# code fix to chat text truncation

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_to_chat_text_truncation_20260515T184129_result.json`
- **Structured JSON:** [`ca513271105dbad1b008.json`](../../sessions/ca/ca513271105dbad1b008.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证全部通过：

**5 条真实样本**：全部 OK，label 均保留在序列末尾（当前数据恰好都在 2048 tokens 内，无需截断）。

**人工长样本**（20033 tokens → 2048 tokens）：截断 17985 tokens，label "fail" 完整保留在末尾。

### 改动总结

**修改文件**：`/root/trace-verdict-study/train/train_sft.py`

**改动点**：
1. **`to_chat_text()` (L30-55)**：新增 `max_length` 参数，实现 label-preserving truncation——先测量 chat template + label 的 token overhead，再将 input content 截断到 `max_length - overhead` 以内，保证 label 永远不被切掉。
2. **调用方 (L127-128)**：传入 `max_length=2048`。

**未改动**：`to_prompt_completion()` 未修改（该函数走 `label_only_loss` 分支，用 `completion_only_loss=True`，不受此问题影响）。

**注意**：当前 `full_trace_train.jsonl` 的所有样本 raw token 数 ≤ 2048（75% 恰好等于 2048），说明数据预处理阶段可能已做过截断。如果训练坍塌的根因是数据预处理时的右侧截断（label 在预处理时就丢了），需要从原始 `raw_traces.jsonl` 重新生成 `full_trace_train.jsonl`。

---
