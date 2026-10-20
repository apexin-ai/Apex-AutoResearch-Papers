# fix exp017 answer extraction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp017-answer-extraction_20260517T040347_result.json`
- **Structured JSON:** [`335962746f3e4b799f44.json`](../../sessions/33/335962746f3e4b799f44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**提取率 100%（5/5）**。修复有效。

总结：

**修改的文件和改动**：

1. **`scripts/eval_strategyqa.py`** - `extract_yesno_answer` 函数：
   - 新增 `text_lower == "true"` → "Yes", `text_lower == "false"` → "No" 的直接映射
   - regex 模式中增加 `true|false` 匹配
   - 新增 `"true" in text_lower` / `"false" in text_lower` 的 fallback
   - SC 答案提取增加 trace 文本 fallback：`t.get("answer", "") or t.get("trace", "")`
   - SICA 答案增加 trace 文本 fallback

2. **`sica/trace_generator.py`** - `extract_answer_fallback` 函数：
   - regex 模式中增加 `Yes|No` 匹配
   - 末尾增加 bare response 检测：当整个 trace 文本只是 "yes"/"no"/"true"/"false" 时直接返回

**Smoke test 结果**：5 题全部成功提取答案，提取率 100%。可以重跑 exp-017。

---
