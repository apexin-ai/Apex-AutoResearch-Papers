# paper writing experiments

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260514T211641_result.json`
- **Structured JSON:** [`73e9b2cdad00f9ba3211.json`](../../sessions/73/73e9b2cdad00f9ba3211.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `docs/paper/sections/experiments.tex`，artifact 已注册。

自查结果：
- **1652 words**（含 LaTeX 标记），排版后约 2.5 pages（正文 + 5 tables + 2 figures）
- Circular eval caveat 在 §5 开头段明确声明
- D042 约束：in-domain RF 0.9951，cross-agent GB 0.967（rounded），multi-seed 格式 mean±std
- 10 个 citation keys 全部来自 references.bib
- 未使用 "significantly"（除有 Kruskal-Wallis p 值支撑处）和 "state-of-the-art"
- 所有 table 有 `\label` + `\caption`，structural 指标标注 $^\dagger$ circular caveat 脚注
- Gold set placeholder 在末尾使用 `\goldset{}` 命令
- 负向结果完整报告：LLM-judge 低性能、probe 迁移失败、TLM 全部不优于 MV

---
