# exp feature ablation overlap and merged

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_feature_ablation_overlap_and_merged_20260519T193520_result.json`
- **Structured JSON:** [`e4501350284a73283fe9.json`](../../sessions/e4/e4501350284a73283fe9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均完成。结果汇总：

## 实验 A: Overlap 6-feature RF (feature_ablation_overlap_001)

仅用 6 个重叠 perplexity 特征 (mean_ppl, var_ppl, p50_ppl, p10_ppl, p90_ppl, skewness_ppl)

| Cell | Accuracy |
|------|----------|
| pythia_nucleus | 76.71% |
| pythia_temp09 | 73.86% |
| pythia_topk50 | 65.27% |
| olmo_nucleus | 76.40% |
| olmo_temp09 | 80.96% |
| olmo_topk50 | 72.48% |
| gpt2xl_nucleus | 81.69% |
| gpt2xl_temp09 | 83.98% |
| gpt2xl_topk50 | 72.06% |
| **9-cell Mean** | **75.93%** |

## 实验 B: Merged 30-feature RF (feature_ablation_merged_001)

合并 19 + 11 Binoculars 特征（含 6 个重复）

| Cell | Accuracy |
|------|----------|
| pythia_nucleus | 83.47% |
| pythia_temp09 | 81.53% |
| pythia_topk50 | 71.18% |
| olmo_nucleus | 84.20% |
| olmo_temp09 | 88.31% |
| olmo_topk50 | 78.36% |
| gpt2xl_nucleus | 88.83% |
| gpt2xl_temp09 | 88.45% |
| gpt2xl_topk50 | 79.09% |
| **9-cell Mean** | **82.60%** |

## 与 Baseline 对比

| 配置 | 9-cell Mean | vs Baseline (78.4%) |
|------|-------------|---------------------|
| 6 overlap features | 75.93% | -2.47 pp |
| 19 features (baseline) | 78.40% | — |
| 30 merged features | 82.60% | **+4.20 pp** |

关键发现：
- 6 个 overlap 特征已能达到 baseline 的 96.8%，说明 perplexity 分布统计量是核心信号
- 合并 Binoculars 特征后提升 +4.2pp，增益主要来自 bino_score、xppl_mean/var/median 等 Binoculars 独有特征

---
