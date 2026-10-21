# D027: Multi-Method Consensus Framework Formalization

## Overview

将 "多方法共识" 从 informal 概念升级为 formal two-stage aggregation framework，用于判定 canary→downstream association 的 robustness。

**定义**: Robust association = 在 K 种独立方法中 ≥ K-1 种判定显著 + ≥ 3/4 seed 一致。

**数据源**: `method_ablation.json` (4 seeds × 16 pairs × 5 methods = 320 seed-level observations)

---

## Sub-task 1: Consensus Classification (≥4/5 methods, ≥3/4 seeds)

**结果**: 6 robust / 10 non-robust

| Canary | Downstream | Methods Agree | Status | Agreeing Methods |
|--------|-----------|:---:|--------|-----------------|
| token_entropy | distinct_1 | 5/5 | **ROBUST** | all 5 |
| token_entropy | distinct_2 | 5/5 | **ROBUST** | all 5 |
| token_entropy | distinct_3 | 5/5 | **ROBUST** | all 5 |
| ece | distinct_1 | 5/5 | **ROBUST** | all 5 |
| ece | distinct_2 | 4/5 | **ROBUST** | all except TY |
| ece | distinct_3 | 4/5 | **ROBUST** | all except TY |
| token_entropy | perplexity | 3/5 | non-robust | naive, diff, threshold |
| ece | perplexity | 3/5 | non-robust | naive, diff, threshold |
| self_bleu | perplexity | 2/5 | non-robust | naive, threshold |
| self_bleu | distinct_2 | 2/5 | non-robust | naive, diff |
| self_bleu | distinct_3 | 2/5 | non-robust | naive, diff |
| effective_rank | perplexity | 2/5 | non-robust | naive, diff |
| effective_rank | distinct_1 | 2/5 | non-robust | naive, diff |
| effective_rank | distinct_2 | 2/5 | non-robust | naive, diff |
| effective_rank | distinct_3 | 2/5 | non-robust | naive, diff |
| self_bleu | distinct_1 | 1/5 | non-robust | naive only |

**核心发现**:
- token_entropy 是最强 canary：→distinct_{1,2,3} 全部 5/5 unanimous
- ece→distinct 系列接近 robust，TY 是唯一 dissenting method（因 T=10 power 不足）
- canary→perplexity 方向一致偏弱，naive+diff+threshold 通过但 TY/permG 不通过
- self_bleu 和 effective_rank 作为 canary 不可靠（仅 naive/diff 通过 = 伪回归嫌疑）

---

## Sub-task 2: Sensitivity Analysis

9 种阈值配置 (method_thresh ∈ {3,4,5} × seed_thresh ∈ {2,3,4}) 下的 robust pair 数：

| Config | # Robust | 备注 |
|--------|:---:|------|
| ≥3/5 methods, ≥2/4 seeds | 12 | 最宽松 |
| ≥3/5 methods, ≥3/4 seeds | 8 | |
| ≥3/5 methods, ≥4/4 seeds | 8 | seed 3→4 无变化 |
| ≥4/5 methods, ≥2/4 seeds | 7 | |
| **≥4/5 methods, ≥3/4 seeds** | **6** | **默认配置** |
| ≥4/5 methods, ≥4/4 seeds | 6 | seed 3→4 无变化 |
| ≥5/5 methods, ≥2/4 seeds | 6 | unanimous + lenient seed |
| ≥5/5 methods, ≥3/4 seeds | 4 | |
| ≥5/5 methods, ≥4/4 seeds | 3 | 最严格 |

### Pair Stability（跨所有 9 种配置）

| Pair | Stability | 分类 |
|------|:---------:|------|
| token_entropy→distinct_{1,2,3} | 9/9 (100%) | **极度稳健** |
| ece→distinct_1 | 8/9 (89%) | **稳健** |
| ece→distinct_{2,3} | 7/9 (78%) | **稳健（borderline）** |
| token_entropy→perplexity | 3/9 (33%) | 阈值敏感 |
| ece→perplexity | 3/9 (33%) | 阈值敏感 |
| effective_rank→distinct_3 | 2/9 (22%) | 不稳健 |
| self_bleu→perplexity | 1/9 (11%) | 不稳健 |
| self_bleu→distinct_{1,2,3} | 0/9 (0%) | **伪回归** |
| effective_rank→{perpl,d1,d2} | 0-1/9 | **伪回归** |

**关键验证**:
- token_entropy→distinct 在所有 9 种配置下都是 robust → 结论极度稳健
- ece→distinct_2/d3 在 7/9 配置下 robust → 预期的 borderline 行为（TY power 不足）
- canary→perplexity 在严格配置下 non-robust → 符合 "差分后信号衰减" 的预期
- self_bleu/effective_rank 几乎在所有配置下 non-robust → 伪回归确认

---

## Sub-task 3: FPR/FNR Table

**Ground truth 定义**:
- FPR: differenced_xcorr 作为 ground truth（seed level, N_neg=9）
- FNR: consensus (≥4/5 methods, ≥3/4 seeds) 作为 ground truth（N_pos=24）

| Method | FPR | FNR | Sig (pair) | Sig (seed) |
|--------|:---:|:---:|:---:|:---:|
| naive_pearson | **100.0%** | 0.0% | 16/16 | 63/64 |
| differenced_xcorr | 0.0% | 0.0% | 14/16 | 55/64 |
| threshold_onset | 11.1% | 0.0% | 9/16 | 35/64 |
| toda_yamamoto | 0.0% | **20.8%** | 4/16 | 26/64 |
| permutation_granger | 11.1% | 0.0% | 6/16 | 34/64 |
| **consensus (≥4/5, ≥3/4)** | **0.0%** | **0.0%** | 6/16 | — |

**核心发现**:
1. **naive_pearson FPR=100%**: 9/9 个 differenced 判定 non-sig 的 seed-level 观测全部被 naive 误判为 sig。这是非平稳伪回归的教科书表现。
2. **toda_yamamoto 是唯一有 FNR 的方法 (20.8%)**: 在 24 个 consensus-positive 观测中，TY 漏掉了 5 个。全部集中在 ece→distinct_2 和 ece→distinct_3（TY 在这两对只有 2/4 seeds sig，不足以通过 3/4 seed threshold）。这印证了 D013/D015 的结论：TY 在 T=10 样本下 power 仅 5-20%。
3. **Consensus 实现了 FPR=0, FNR=0 的平衡**（FNR=0 是 by construction，因 consensus 本身是 FNR ground truth）。
4. threshold_onset 和 permutation_granger 各有 1 个 FP seed（FPR=11.1%），表现介于两极之间。

### 论文叙事

这张表支撑 Option B reframe 的核心论点：
- 单独使用任何一种方法都有缺陷（naive 过于宽松，TY 过于保守）
- 多方法共识提供了一个 **principled** 方式来平衡 Type I / Type II error
- Consensus 的 6/16 robust pairs 远少于 naive 的 16/16，但每一对都经得起独立检验

---

## 产出文件

| 文件 | 内容 |
|------|------|
| `consensus_framework.py` | 可复用 Python 模块（load_sig_matrix, classify_robust, sensitivity_analysis, compute_fpr_fnr） |
| `sensitivity_analysis.json` | 9 种阈值配置的完整 grid 和 per-pair stability |
| `fpr_fnr_table.json` | 5+1 种方法的 FPR/FNR 详细数据 |

服务器端结果: `/root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/consensus/`
