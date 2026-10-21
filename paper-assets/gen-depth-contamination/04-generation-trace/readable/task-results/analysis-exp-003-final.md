# analysis exp 003 final

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_003_final_20260513T202333_result.json`
- **Structured JSON:** [`d34782a335de5b75ffce.json`](../../sessions/d3/d34782a335de5b75ffce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总：

## exp_003_decoding_ablation 最终结果

| Config | 解码策略 | 1v2 AUC | K*(θ=0.60) |
|--------|---------|---------|------------|
| 1 | Greedy | 0.6893 | **2** |
| 2 | Nucleus p=0.9, T=1.0 | 0.6866 | **2** |
| 3 | Nucleus p=0.95, T=0.7 | 0.6887 | **2** |
| 4 | Nucleus p=0.95, T=1.2 | 0.7039 | **2** |

**结论: success** — 4 种解码策略 K* 一致为 2，支持 D016 universality narrative。

关键发现：
- Config 4 (高温度 T=1.2) 1v2 AUC 最高 (0.7039)，跨所有实验排名第一
- 4 个 config 的 1v2 AUC 极度稳定，极差仅 0.0173
- θ-sensitivity 在 θ∈{0.55, 0.60, 0.65} 时 4 config 完全一致；仅 θ=0.70 时 Config 4 的 K* 多保留 1 级 (K*=2 vs 1)
- 特征排名 Spearman ρ 范围 [0.53, 0.91]，top features 一致为 hapax_ratio, ttr, surp_skew
- 跨实验 D016 检验通过：全部 8 个 config/model 组合的 1v2 AUC 均 > 0.60

分析产物已保存至 `artifacts/exp003_analysis.json`。

---
