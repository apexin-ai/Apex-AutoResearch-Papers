---
name: distilled-research
description: "Data weighting/mixing for LLM pretraining: baselines, metrics, experimental design consensus from 25 papers (2023-2026)"
scope: project
version: 1
tags: [distilled, auto-generated]
distilled_from:
  paper_count: 25
  paper_keys: [drayson_2025_detection_collapse, feng_2025_beyond_collapse, subramanyam_2025_scaling_quality, amin_2025_escaping_collapse, sow_2025_dynamic_reweighting, ye_2025_data_mixing_laws, he_2024_softdedup, chen_2025_aioli, yang_2026_data_mixing_agent, grangier_2025_crisp, kang_2025_demystifying_synthetic, kazdan_2025_collapse_thrive, alemohammad_2024_mad, dohmatob_2025_strong_collapse, shi_2024_minkprob, xie_2023_doremi, xie_2023_dsir, mitchell_2023_detectgpt, he_2025_golden_ratio, martino_2025_ess_entropy, kimura_2024_iw_survey, vehtari_2024_psis, shumailov_2024_model_collapse, wang_2026_survive_contamination, nait_saada_2025_quality_illusion]
  last_distilled: "2026-05-24T12:00:00Z"
---

## 必选 Baselines

- **DoReMi** (group DRO): 6/8 论文对比。来源：Xie NeurIPS'23。置信度：高
- **Uniform/random**: 7/8 底线。置信度：高
- **DoGE**: 4/8 引用。来源：Sow ICLR'25。置信度：高
- **Hard dedup (MinHashLSH)**: 3/8 对比。来源：SoftDedup ACL'24。置信度：高

## 必报 Metrics

- **Perplexity** (per-domain + aggregate): 8/8。主指标。置信度：高
- **Few-shot accuracy** (5-shot): 5/8。置信度：高
- **Training step efficiency** (steps to match baseline): 4/8。置信度：高

## 核心 Datasets

- **SlimPajama** (7 domains): 4/8 使用。标准多域集。置信度：高
- **FineWeb**: 2/8（大模型实验）。新兴趋势。置信度：中
- **RedPajama/Pile**: 各 2/8。经典但被替代。置信度：中

## 实验设计共识

**模型规模梯度** (7/8, 高): 小(120-300M) → 中(1.3B) → 大(7B+)

**域级+实例级正交** (3/8, 高): LinUpper+DoReMi 叠加有 +0.5-0.7% 额外增益

**Compute-equivalent** (4/8, 高): "达到baseline所需steps" — SoftDedup 26%, DoReMi 2.6×, DML 48%

## 方法论趋势

**上升:** Instance-level reweighting; Scaling law integration (quality/mixing); Verification-based synthetic selection ("curated synthetic > pure human" 范式)

**消退:** 纯 domain-level 固定权重; Binary deduplication; 完全回避 synthetic data

## 竞品核心 Claim

- SoftDedup: "inverse commonness, 26%+ 加速, 零信息丢失"
- LinUpper: "零开销 instance reweighting, 7B +1.35%"
- Aioli: "唯一 consistently beat stratified sampling"
- Data Mixing Laws: "指数形式 L=c+k·exp(Σt·r), 1000× cheaper"

## 共同局限 (≥3篇)

1. 模型规模有限 (6/8): 多数 ≤1.3B
2. 理论与实践 gap (4/8): 凸性/interpolation 假设
3. Synthetic noise ≠ real degradation (3/8)

## 研究空白

1. **Provenance-aware weighting**: 无论文按 human/synthetic 来源做 weighting — 本项目核心机会
2. **Dynamic quality estimation during training**: 仅 LinUpper 做 online instance-level
3. **Synthetic fraction × quality weighting 交互**: 最优比例(~30%) 与 weighting 的联合优化未知
