# analysis exp003 config12 deep analysis

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp003_config12_deep_analysis_20260513T172521_result.json`
- **Structured JSON:** [`aadf1965debf21c2ac94.json`](../../sessions/aa/aadf1965debf21c2ac94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部产出已生成。以下是完整分析结论。

---

## 1. Config 1 (Greedy) vs Config 2 (Nuc09) 详细对比

### Pairwise AUC Profile

| Depth-Pair | Greedy | Nuc09 | Δ |
|:---:|:---:|:---:|:---:|
| 0v1 | 0.9797 | **0.9946** | +0.0149 |
| 1v2 | **0.6893** | 0.6866 | −0.0027 |
| 2v3 | 0.5613 | **0.5917** | +0.0304 |
| 3v4 | 0.5404 | **0.5466** | +0.0062 |
| 4v5 | **0.5139** | 0.5068 | −0.0071 |

**关键发现**：1v2 AUC 几乎相同（Δ=0.0027），decoding strategy 对核心区分度影响极小。Nuc09 在 0v1 和 2v3 上略优，但差异在 fold 方差范围内。

### Single-Feature AUC Ranking (1v2) — Spearman ρ

| 对比 | ρ | p-value |
|:---|:---:|:---:|
| Greedy vs Nuc09 | **0.600** | 0.018 |
| Greedy vs T07 | **0.914** | 2×10⁻⁶ |
| Nuc09 vs T07 | **0.782** | 0.00057 |

Greedy 与 Nuc09 的 feature ranking 一致性中等 (ρ=0.60)，与 T07 高度一致 (ρ=0.91)。Nuc09 的 sampling 随机性改变了部分 feature 的相对区分力。

### Top-3 Discriminative Features (single-feature AUC, 1v2)

| Config | #1 | #2 | #3 |
|:---|:---|:---|:---|
| Greedy | self_bleu (0.5961) | hapax_ratio (0.5752) | ttr (0.5462) |
| Nuc09 | hapax_ratio (0.6561) | ttr (0.6043) | surp_skew (0.5997) |
| T07 | hapax_ratio (0.6365) | ttr (0.5867) | low_freq_ratio (0.5805) |

**hapax_ratio 和 ttr 在所有 config 的 top-3 中出现**（词汇多样性指标稳定）。Greedy 的 self_bleu 排第一（greedy 解码产生更多重复模式），而 sampling 方法（Nuc09/T07）的 surpirsal 分布特征更突出。

---

## 2. Cross-Experiment 1v2 AUC 排序 + D016 Universality

| Rank | Config | 1v2 AUC |
|:---:|:---|:---:|
| 1 | MVP-Qwen-Rewrite | **0.6957** |
| 2 | Config1-Greedy | 0.6893 |
| 3 | Config3-T07 | 0.6887 |
| 4 | Config2-Nuc09 | 0.6866 |
| 5 | Exp001-Pythia-Cont | 0.6539 |
| 6 | Exp002-OLMo-Cont | 0.6146 |
| 7 | Exp017-Qwen-Cont | 0.6114 |

**D016 Universality (θ=0.60): YES — 所有 7 个 config 的 1v2 AUC 均 > 0.60。** 最弱环节是 Exp017-Qwen-Cont (0.6114)，仍高于阈值 1.9%。

### θ-Sensitivity (K*)

| Config | θ=0.55 | θ=0.60 | θ=0.65 | θ=0.70 |
|:---|:---:|:---:|:---:|:---:|
| Greedy | K*=3 | K*=2 | K*=2 | K*=1 |
| Nuc09 | K*=3 | K*=2 | K*=2 | K*=1 |
| T07 | K*=3 | K*=2 | K*=2 | K*=1 |

三个 config 的 K* profile 完全一致：θ=0.60 时可检测到 depth 2，θ=0.55 时可检测到 depth 3。

---

## 3. 产出清单

| 产出 | 位置 |
|:---|:---|
| 分析脚本 | `scripts/exp003_analyze_all_configs.py`（已验证可运行，支持 2-4 configs） |
| JSON 结果 | `artifacts/exp003_analysis.json`（当前含 3 configs 数据） |
| Config 4 (t12) | 仅 depth_0 完成，pipeline 运行中。脚本可在 t12 完成后直接重跑出 4-config 结果 |

---
