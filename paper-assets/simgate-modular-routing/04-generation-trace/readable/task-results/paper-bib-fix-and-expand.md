# paper bib fix and expand

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bib-fix-and-expand_20260514T145311_result.json`
- **Structured JSON:** [`5647c696385076c83c4a.json`](../../sessions/56/5647c696385076c83c4a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 bib 文件完全一致。

**完成情况：**

**Part 1 — bib 质量修复：**
- Year 字段：3 个 key-year 不匹配项（`toolformer-2024`/`chameleon-2024`/`retool-2026`）经查 venue 确认 year 字段已正确（分别为 2023/NeurIPS、2023/NeurIPS、2025/arXiv），无需修改
- Entry type：docs/paper 版本中 6 个 arXiv 条目已是 @article；`mixture-of-recursions-2025`（NeurIPS 2025）和 `mtrouter-2026`（ACL 2026）确认为正式会议论文，@inproceedings 正确。artifacts 旧版本已同步为 docs/paper 版本
- `dagger-2011`：conclusion.tex 中有引用，保留

**Part 2 — 新增 3 条引用：**
| Key | Venue | 引用位置 |
|-----|-------|---------|
| `toolkengpt-2023` | NeurIPS 2023 | related_work.tex Tool-Use Learning 段 |
| `alfworld-2021` | ICLR 2021 | related_work.tex Agent Frameworks 段 + conclusion.tex Limitations |
| `voyager-2023` | arXiv 2023 | related_work.tex Agent Frameworks 段 |

**验证：** 20 个 \cite key 与 20 个 bib entry 一一对应，两处 bib 文件同步。总引用数从 12 → 15（加上之前已有的 concurrent work 4 条共 20 条）。

---
