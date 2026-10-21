# analysis d072 paper patch inventory

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d072_paper_patch_inventory_20260515T113312_result.json`
- **Structured JSON:** [`e318b0e1cacc9ffd15ef.json`](../../sessions/e3/e318b0e1cacc9ffd15ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清单已写入并注册。

**汇总**: 7 项可写入发现，5 项 P0 + 2 项 P1。

**P0 关键项**:
1. **Free-form 4-panel 扩展表格** — 替换 appendix 简化表，信息量 4×
2. **RE LP selection flip 机制** — 全部 7 关系类型 universal flip，selective variance reallocation (p<0.0001)，win/loss 从 36:59 翻转到 45:45
3. **Non-tied 子集重洗牌** — Jaccard=0.472，87 个实例新获区分力（LP range 3×），揭示压缩分布的结构性变化
4. **多种子 RE 稳定性** — RE ranking 有轻微 top-3 波动（vs NER 完美稳定），tab:multiseed 需加 RE 行
5. **数据更正** — appendix robustness 中 LLaMA SciERC SJ ρ=0.363 是 contaminated exp_007 值，应更正为 0.325±0.021（exp_018 fresh data）；FK 0.327→0.256±0.024

**预计工时**: P0 ~2.5h，P1 ~20min，总计 ~3h。建议先修数字更正（发现5），再替换表格（发现1）。

---
