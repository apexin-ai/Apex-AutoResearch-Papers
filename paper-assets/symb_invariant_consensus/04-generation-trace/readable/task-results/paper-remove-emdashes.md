# paper remove emdashes

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_remove-emdashes_20260525T052845_result.json`
- **Structured JSON:** [`5b55004faa80325aa872.json`](../../sessions/5b/5b55004faa80325aa872.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功。

## 汇总

只有 **1 处** 需要修改（主体文件中的其他 `---` 已在此前被清理）：

| 文件 | 行 | 原文 | 修改后 |
|------|-----|------|--------|
| `diagnosis.tex` | 53 | `...the incorrect majority answer---a bias ratio of $4.97\times$...` | `...the incorrect majority answer, with a bias ratio of $4.97\times$...` |

保留未动的：
- `diagnosis.tex` 37-38: `\textrm{---}`（表格"不适用"标记）
- `appendix.tex` 所有实例（按要求不改附录）
- `abstract.tex`, `analysis.tex`, `discussion.tex`, `experiments.tex`, `introduction.tex`, `solutions.tex`, `method.tex`, `conclusion.tex`, `limitations_content.tex`, `related_work.tex`：无 `---`

---
