# analysis mpl retry cpu

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mpl_retry_cpu_20260515T095901_result.json`
- **Structured JSON:** [`6fc484a9657ecbb8745a.json`](../../sessions/6f/6fc484a9657ecbb8745a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**48 条件 (3 mpl × 16 conditions) 全部计算完成，22 秒。**

关键发现：
- **所有 8 个 importance 条件在 mpl=5/10/20 下均显著** (Bonferroni k=4)，sign consistency 8/8
- mpl=10 → mpl=20 时 n_effective 下降（ds: 496→433, qw: 475→289），但统计结论不变
- 唯一变化：ds_rand_s030 在 mpl=20 失去显著性（bonf_p=0.058），属于 power 下降而非效应消失
- mpl=5 与 mpl=10 结果完全一致（mpl=10 不会遗漏有效 problem）

产出文件：
- 服务器 CSV: `/root/autodl-tmp/pacs/analysis_output/min_phase_length_sensitivity.csv`
- 本地 CSV: `artifacts/n500_analysis/min_phase_length_sensitivity.csv`
- 本地 MD: `artifacts/n500_analysis/min_phase_length_sensitivity.md`

---
