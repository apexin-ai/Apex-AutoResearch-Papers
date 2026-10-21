# paper r26 fix results

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r26_fix_results_20260522T043732_result.json`
- **Structured JSON:** [`e77ce655c342f5758177.json`](../../sessions/e7/e77ce655c342f5758177.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

四处修改全部完成。修改摘要：

| Task | 文件 | 行号 | 修改内容 |
|------|------|------|----------|
| 3 | `results.tex:52` | §4.3 DocRED段 "shared with centrality." 之后 | 插入 VIF=50.9 标准误膨胀 ~7 倍 caveat + Ridge regression 方向确认 + Appendix ref |
| 4 | `discussion.tex:11` | §Discussion "independently addressable" | 替换为 "approximately additive on the probability scale within the observed accuracy range (0.37–0.86)" + 新增 logit scale inconclusive 句 |
| 7 | `results.tex:78` | §4.4 NER null "absence of evidence rather than evidence of absence." 之后 | 插入 NER error-mode structure 解释（miss/boundary/type channels）+ `\ref{app:relaxed-matching}` (label 已验证存在) |
| 8 | `main.tex:52` | Limitations → Multiple comparisons 段末 | 插入 Bonferroni robustness 声明，标注 logit-scale interaction p=0.047 为唯一临界值结果 |

---
