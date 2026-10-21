# code atlas analysis prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_atlas_analysis_prep_20260514T160337_result.json`
- **Structured JSON:** [`bf8d7fafe5de3855ed74.json`](../../sessions/bf/bf8d7fafe5de3855ed74.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JT test 修复生效——所有特征的 p-value 接近 0（高度显著），包括之前报 1.0 的递减特征。

产出汇总：

**文件**：
- `src/atlas_analysis.py` — 主分析（5 个分析模块 A-E）
- `src/atlas_plots.py` — 学术级可视化（PDF + PNG）
- `scripts/run_atlas_analysis.sh` — pipeline 脚本

**dry-run 结果**（MVP Pythia 20k 样本）：
- **Top features**: var_surprisal > mean_surprisal > p90_ppl > p75_ppl > hapax_ratio
- **Monotonicity**: 16/19 特征完美单调（|Mono|=1.0），大部分递减，rep_*gram 递增
- **EDD=3**: 所有相邻深度对均可区分（0v1: 0.9996, 1v2: 0.9245, 2v3: 0.8051）
- **PCA**: 两个主成分解释 99.6% 方差（85.4% + 14.2%）
- **JT test**: 所有特征 p < 0.001，深度趋势统计显著
- 13 个输出文件（6 PDF + 6 PNG + 1 JSON）在 `artifacts/atlas/`

多模型分析（Analysis D: 一致性热图）会在各模型 features 提取完成后自动启用——去掉 `--single` 即可。

---
