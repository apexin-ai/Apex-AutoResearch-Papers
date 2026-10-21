# code answer extraction fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_answer-extraction-fix_20260515T175510_result.json`
- **Structured JSON:** [`209354feb2d1bbb7ef68.json`](../../sessions/20/209354feb2d1bbb7ef68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

v3 仍在运行，所有导入正常。

## 改动总结

### `sica/trace_generator.py`
- 新增 `extract_answer_fallback()` — 4 层 fallback patterns，按优先级匹配：partial boxed → "the answer is X" → "therefore/thus/hence ... = X" → 末尾 "= X"。先搜最后 1000 字符，再搜全文，取最后一个匹配
- 新增 `extract_answer()` — 统一入口，先 `\boxed{}`，失败走 fallback，返回 `(answer, method)` 
- `VLLMGenerator._generate_n_batch` / `_generate_single` / `APIGenerator.generate` 全部改用 `extract_answer()`，每条 trace 记录 `finish_reason` 和 `extraction_method`
- 非 boxed 提取时输出 warning 日志

### `run_full_mvp.py`
- `--max-tokens` 默认值 10240 → **16384**
- 新增 `--save-intermediates` flag，启用时在输出 JSON 中保留 `raw_constraints` 和 per-trace 详情
- 每道题记录 `trace_extraction_stats`（boxed/fallback/none 计数）和 `truncated_traces`（finish_reason=length 的数量）
- summary 中新增 `answer_extraction_rate`、`answer_extraction_counts`、`truncated_traces` 统计

### 测试
- 14 个 unit test 全部通过，覆盖：标准 boxed、嵌套 boxed、boxed 优先级、"the answer is X"、"the final answer is X"、"Therefore N = X"、"thus = X"、最后匹配优先、负数、小数、无答案、截断 trace、dollar sign 包裹、空 boxed fallback

### 预期影响
- 截断 trace（finish_reason=length）中如果出现了 "the answer is X" 或 "therefore X = N" 等模式，现在可以被提取。结合 max_tokens 提升到 16384，P8/P9/P11 这类长推理题应该能大幅减少截断，预计答案提取率从 ~50% 提升到 >80%。

---
