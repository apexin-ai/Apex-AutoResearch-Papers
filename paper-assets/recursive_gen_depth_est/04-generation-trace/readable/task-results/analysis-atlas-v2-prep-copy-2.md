# analysis atlas v2 prep

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_atlas_v2_prep_20260515T010628_result.json`
- **Structured JSON:** [`07f120ee104198e48f96.json`](../../sessions/07/07f120ee104198e48f96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出汇总：

### 文件清单

| 文件 | 说明 |
|------|------|
| `artifacts/atlas_v2/matrix_data.json` | 7/9 cells 统一格式数据 |
| `src/atlas_v2.py` | 分析框架（5 项分析） |
| `artifacts/atlas_v2/monotonicity_scores.json` | Spearman ρ per feature per cell |
| `artifacts/atlas_v2/edd_analysis.json` | EDD 饱和深度 |
| `artifacts/atlas_v2/cross_model_heatmap.json` | 3×3 热力图矩阵 |
| `artifacts/atlas_v2/feature_trajectory_summary.json` | 特征变化轨迹 |
| `artifacts/atlas_v2/jaccard_matrix.json` | 跨策略 top-5 特征 Jaccard |

### 3×3 矩阵（RF 4-class accuracy）

|  | Nucleus | Temp09 | TopK50 |
|--|---------|--------|--------|
| **Pythia-1.4B** | 78.2% | 76.2% | 69.6% |
| **OLMo-1B** | 78.8% | 82.0% | --- |
| **GPT-2-XL** | 83.3% | 85.4% | --- |

### 关键发现

- **EDD**: 6/7 cells 信号持续到 depth 3 无饱和（d2v3 AUC > 0.7），仅 **Pythia topk50** 在 depth 3 饱和（d2v3 AUC = 0.692）
- **Jaccard**: Pythia 三种策略 top-5 特征完全一致（J=1.0）；OLMo 和 GPT-2 XL 的 nucleus vs temp09 J=0.667（4/5 overlap，差异在 mean_ppl/type_token_ratio vs p50_ppl）
- **Feature trajectory**: p90_ppl、var_surprisal、mean_surprisal 随 depth 单调递减（ρ = -1.0）；rep_2gram/3gram/4gram 单调递增
- **缺失**: olmo_topk50 和 gpt2xl_topk50 仍在运行，完成后填入 matrix_data.json 并重跑 `python src/atlas_v2.py` 即可

---
