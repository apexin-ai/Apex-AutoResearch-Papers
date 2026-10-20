# analysis verify tiebreaking seeds

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify-tiebreaking-seeds_20260523T184225_result.json`
- **Structured JSON:** [`813c3ad3472a573b2c60.json`](../../sessions/81/813c3ad3472a573b2c60.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**所有 seeds 123/456/789 均使用 alphabetical tiebreaking，无需修复。**

### SC tiebreaking 验证

| 实验 | N | SC Ties | 全部 alphabetical |
|------|---|---------|-------------------|
| Mistral PW seed123/456/789 | 600/600/600 | 29/21/30 | ✓ |
| LLaMA PW seed123/456/789 | 600/**184**/600 | 32/8/36 | ✓ |
| Qwen2.5 PW seed123/456/789 | 600/600/600 | 18/19/12 | ✓ |
| Mistral FOLIO seed123/456/789 | 204/204/204 | 11/2/10 | ✓ |
| LLaMA FOLIO seed123/456/789 | 204/204/204 | 14/4/7 | ✓ |
| Qwen2.5 FOLIO seed123/456/789 | 204/204/204 | 2/8/5 | ✓ |

SC 使用 `max(sorted(groups.keys()), key=...)` — ties 时取 alphabetically first。18 个实验中 0 个 mismatch。

### SICA tiebreaking 验证

SICA 使用三级 tiebreak：score → frequency → alphabetical。18 个实验中 0 个 bug，行为与代码 `select_answer()` 一致。

### 附注

**LLaMA PW seed456 只有 184/600 条结果**，是一个不完整的实验（但 tiebreaking 本身是正确的）。

---
