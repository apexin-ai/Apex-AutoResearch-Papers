# code plan 010 arch stratified dif

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_010_arch_stratified_dif_20260521T033224_result.json`
- **Structured JSON:** [`f34db878743cd69c0d14.json`](../../sessions/f3/f34db878743cd69c0d14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**METABENCH MMLU 几乎全是 decoder-only 模型**（5226/5227 = 99.98%），唯一被排除的是 `AurelPx/Pegasus-7b-slerp`（名称匹配 encoder-decoder 模式）。

因此 architecture stratification 对 DIF 结果 **没有任何影响**：
- Decoder-only C% = 31.32%，与 full-population 完全一致
- Jaccard overlap = **1.0000**（完美重合，零 item 移动）
- IRT fit 指标（rpb、Lz）在两个群体间无差异
- Sanity check 通过（0.18% C < 5%）

产出文件在 `artifacts/plan_010/`：
- `plan_010_arch_stratified_dif.py` — 分析脚本
- `plan_010_report.md` — 完整报告
- `dif_results_decoder_only_temporal.csv` — 逐 item DIF 结果
- `irt_fit_comparison.csv` — IRT fit 对比
- `architecture_classification.csv` — 模型架构分类

**结论**：审稿人担心的架构异质性不成立。METABENCH 群体本身就是 architecture-homogeneous 的，31.3% ETS C 不是架构混杂的伪影。

---
