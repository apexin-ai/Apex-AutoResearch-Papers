# verify exp018 arc extraction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_exp018-arc-extraction_20260517T052054_result.json`
- **Structured JSON:** [`dcb019b0f80d476b1819.json`](../../sessions/dc/dcb019b0f80d476b1819.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

## 结果总结

**提取函数位置**: `/root/symb_invariant_consensus/scripts/eval_arc.py:44` — `extract_mc_answer()`

**发现并修复了 2 个问题**：

| # | Bug | 修复 |
|---|-----|------|
| 1 | Pattern 2 `[Aa]nswer\s*[:\s]*\(?([A-E])\)?` 无法匹配 "answer is D" 格式（"is" 不在 `[:\s]` 字符类中） | 改为 `[Aa]nswer\s*(?:is\s*)?[:\s]*\(?([A-E])\)?` |
| 2 | Fallback 从文本末尾反向扫描第一个 A-E 字符 → 当答案后面提到其他选项字母时提取错误（如 "D is best. A and B are wrong" → 错误返回 'A'） | 改为正向查找第一个独立 A-E 字母 `\b([A-E])\b` |

同时增强 Pattern 1 支持 "The correct/best answer is X"：`[Tt]he\s+(?:\w+\s+)?answer\s+is\s*...`

**15 个测试用例全部通过**，包括 7 个核心格式 + 4 个边界 + 2 个原 fallback 失败用例 + 2 个 "answer is X" 变体。

**exp-018 可以安全运行。**

---
