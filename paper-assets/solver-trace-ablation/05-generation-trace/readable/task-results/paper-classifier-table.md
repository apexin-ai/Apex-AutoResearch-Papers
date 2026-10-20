# paper classifier table

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_classifier-table_20260522T130618_result.json`
- **Structured JSON:** [`9406e451d79e87d99a0f.json`](../../sessions/94/9406e451d79e87d99a0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

插入完成。

**数据来源**: 三轮验证（worker_code_r15-classifier-validation 结果 + appendix 已有文字）:
- 分层验证 82 样本: CE=20, TS=2, PG=20, Contradiction=20, Genuine=20
- 随机 CE∪TS 50 样本 (池比例 374:2)
- 边界案例 20 样本: CE=10, TS=5, Genuine=5

**插入位置**: `docs/paper/appendix.tex` L239–257, Boundary case validation 段落后、PG subsection 前。

**缺失项**: 50 个随机样本未按 CE/TS 分开记录，已用脚注标注池比例。所有 152 样本 precision=1.00。

---
