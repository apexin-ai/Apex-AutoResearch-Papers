# paper r26 squeeze 3lines

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r26_squeeze_3lines_20260522T054237_result.json`
- **Structured JSON:** [`60d1a8e4fc5ad39d6ad4.json`](../../sessions/60/60d1a8e4fc5ad39d6ad4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验收通过。

**执行方案汇总**：

| 方案 | 操作 | 效果 |
|------|------|------|
| 方案 1 | discussion.tex "Boundary conditions"：删除重复数字 `$r^2 \approx 1.3\%$`、`($R^2 \approx 22\%$, ~31 pp extreme gap on FewRel)` | ~1 行 |
| 方案 1 | discussion.tex "Practical implications"：删除 `BCS enables pre-hoc diagnostics (flag SCS > 0.85 pairs);`、`(TOST p=0.003 at ±3 pp; logit-scale equivalence inconclusive, p=0.209)`、`on the probability scale`；合并句子结构 | ~3 行 |
| 方案 2 | results.tex §4.1、§4.2 两段加 `\looseness=-1` | 辅助 |
| 方案 2 | sdgd_negative.tex 加 `\looseness=-1` | 辅助 |

**验证结果**：
- Page 8 末尾：Discussion "separability holds on the linear scale but remains open on the logit scale."
- Page 9 开头：`Limitations`
- 0 errors, 0 undefined references

---
