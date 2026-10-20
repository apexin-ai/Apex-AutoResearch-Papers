# paper writing appendix

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_appendix_20260514T221502_result.json`
- **Structured JSON:** [`6852ac07138c7454999c.json`](../../sessions/68/6852ac07138c7454999c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `docs/paper/sections/appendix.tex` 并注册为 artifact。

6 个 subsection 全部完成：
- **A. Encoder Ablation** — 3 encoder × multi-seed 表格，含 BGE-M3 seed 123 outlier 说明
- **B. Window Size** — k=3/5/7 完整指标 + delta
- **C. LF Temporal Dynamics** — lag 分布表 + Kruskal-Wallis + Bonferroni 校正 pairwise 表
- **D. Structural Features** — 30 features 按类别分组列出，注明 importance ranking pending
- **E. Data Scaling** — embedding probe 四档 + structural baseline 四档（后者带 circular eval caveat 加粗警告）
- **F. Error Analysis** — 两张表：按 confidence/outcome/position 分层统计 + LF conflict/FP pattern/error concentration

所有数字与 registry 数据一致。

---
