# code paper data consistency fix

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper-data-consistency-fix_20260525T154916_result.json`
- **Structured JSON:** [`bc937dd97f8740dcb813.json`](../../sessions/bc/bc937dd97f8740dcb813.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修复完成。

**修改汇总**（8 个文件，跨 6 个 .tex 文件 + 1 个报告）：

| 修复项 | 文件 | 变更 |
|--------|------|------|
| Abstract | abstract.tex | 移除 "late layers (88%)"，改为 broadly distributed；精简至 149 words |
| Introduction ×2 | introduction.tex | L28→L15, p=0.002→p<0.001；重构 dissociation bullet |
| Experiments ×5 | experiments.tex | 峰值层 L28→L15；fig3/fig5 caption；移除 L28 "probe peak" 标签 |
| Discussion | discussion.tex | p=0.002→p<0.001；L28→L15；MLP ordering 重构 |
| Conclusion | conclusion.tex | 重写 three-way dissociation 叙事；p<0.001；cross-model 证据为主 |
| Appendix D | main.tex | fig6 caption L28→L15 |
| Appendix E | main.tex | AUROC 表移除 peak layer 标注 |
| Appendix F | main.tex | Llama N=136→N=201, probe 76.1%→90.0% |

**验证结果**：0 LaTeX 错误，正文 ≤8 页，abstract 149 words，残留 L28/88%/p=0.002 引用全部合法（数据表行、测试层描述、特定 α 值 p 值）。报告已写入 `data_consistency_fix_report.md`。

---
