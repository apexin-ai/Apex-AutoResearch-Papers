# paper writing experiments

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_20260515T182502_result.json`
- **Structured JSON:** [`1727eeee9e6cfd89a0bf.json`](../../sessions/17/1727eeee9e6cfd89a0bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

**Part 1 — ARR 模板**
- 从 `acl-org/acl-style-files` 下载了 `acl.sty` + `acl_natbib.bst`
- 创建 `main.tex`（`[review]` 匿名模式）+ 6 个章节占位符
- 编译通过，生成 2 页 PDF（仅 `fig:calibration` 和 `fig:cross_model_gap` 两个 figure ref 未定义，等图文件就绪后自动解决）

**Part 2 — experiments.tex**
- 4 个 subsection：Cross-Model Comparison / Component Ablation / Information Density Decomposition / Calibration Analysis
- 4 张表（Table 1-4），所有数字直接来自 registry 数据，精度统一 2 位小数，95% CI 用方括号
- McNemar's test p-values 标注（ae vs exc: p=0.80; exc vs VOTA: p=0.01）
- Seed robustness: σ=0, n=3
- DeepSeek full_trace 标注 N/A 并脚注说明 truncation bug
- `wang2025dcsh` 加入 references.bib，标记 `[CITATION NEEDED]` 待验证作者和标题

---
