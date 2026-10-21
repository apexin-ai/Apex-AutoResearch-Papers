# code fix gsm8k normalization

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-gsm8k-normalization_20260518T153100_result.json`
- **Structured JSON:** [`54f842a513015727267c.json`](../../sessions/54/54f842a513015727267c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 13/13 测试通过。

**修改内容：**
- 新增 `normalize_numeric_answer()` 函数（line 265），将 `"2.00"` → `"2"`、`"3.50"` → `"3.5"` 等尾零去除，非数字字符串原样返回
- `extract_gsm8k_answer()` 的两个 return 路径均调用 normalize（line 281, 285）
- `evaluate_gsm8k()` 中 gold answer 也做同样 normalize（line 315），确保两端一致

---
