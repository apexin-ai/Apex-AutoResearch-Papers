# code fix extraction parse

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-extraction-parse_20260515T122228_result.json`
- **Structured JSON:** [`26d12c663ec114a778d7.json`](../../sessions/26/26d12c663ec114a778d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

端到端验证通过。提取成功返回 3 个约束，**0 个 JSON parse 失败**。

## 修复总结

**根因**: `_parse_response` 中的正则 `r'```(?:json)?\\s*(.*?)```'` 有 bug — raw string 中 `\\s` 是两个字符 `\` + `s`，在正则中匹配的是字面量反斜杠+s，而非空白字符。导致 code-fenced JSON 永远无法提取，后续 `json.loads` 对包含大量推理文本的原始响应直接 parse 必然失败。

**修复内容** (`constraint_extractor.py`):

| 问题 | 修复 |
|------|------|
| `\\s` regex bug | `\\s` → `\s`（单反斜杠，正确匹配空白） |
| 无 fallback 提取 | 新增 `_extract_json_str`: 先试 code fence，再试 `{...}` 括号匹配 |
| 截断 `&lt;think>` 未处理 | `_strip_thinking` 处理有/无 `&lt;/think>` 两种情况 |
| 无 JSON 修复 | `_repair_json` 处理 trailing comma、单引号 |
| `extract_batch` 对每个失败重试 3 次 LLM 调用 | 移除级联重试（batch 失败不再调 `self.extract()`） |
| `parse_retries=2` 默认太高 | 降为 1 |
| `_retry_with_backoff` 3次/1s base | 降为 2次/0.5s base |

---
