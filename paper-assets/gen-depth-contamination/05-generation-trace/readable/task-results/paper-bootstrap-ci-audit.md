# paper bootstrap ci audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_bootstrap-ci-audit_20260518T235735_result.json`
- **Structured JSON:** [`e16d6ff2ebadcc9b9069.json`](../../sessions/e1/e16d6ff2ebadcc9b9069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已写入 `artifacts/bootstrap_audit_report.md`。

**结果摘要：**
- 论文 .tex 源文件中有 **13 处残留 bootstrap 引用**描述我们自己的方法，分布在 `method.tex`(2处)、`experiments_c1.tex`(2处)、`appendix.tex`(5处)、`appendix_extended.tex`(4处)
- **3 处**引用他人方法（related_work.tex 和 references.bib 中的 "importance resampling"），无需修改
- `main.aux` 中约 15 处为编译自动生成，修改源文件后重新编译即可
- 最高优先级：`method.tex:25` 的核心方法论描述，需将 bootstrap resampling 机制改写为 fold-based CI 机制

报告中包含每处的当前文本和建议替换文本。另外提醒：表格中的 CI **数值**和 Figure S1 的 error bars 也需确认已用 fold-based 方法重新计算。

---
