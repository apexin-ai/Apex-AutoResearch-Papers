# MVP II Profiling v3 — Analysis Report

**Date**: 2026-05-14  
**Experiment**: `mvp_ii_profiling_v3`  
**Conclusion**: **negative** — measurement method valid, hypothesis not supported  

## 实验配置

| 参数 | 值 |
|------|-----|
| Model | DeepSeek-R1-Distill-Qwen-7B |
| Data | MATH500 (stratified sample, n=50) |
| Sparsity levels | 0.1, 0.2 (v2: 0.3, 0.5) |
| Phase segmentation | Quantile-based on attention sparsity (v2: KDE) |
| Bootstrap | 1000 iterations |
| GPU hours | 0.91h |

## v3 改进点 vs v2

| 问题 | v2 | v3 | 效果 |
|------|-----|-----|------|
| 数值爆炸 | ii_execution_0.3=Inf | 无 NaN/Inf | ✅ 解决 |
| Phase 分布偏斜 | exec 1.2%, reas 8.1%, trans 90.7% | high 30%, mid 32.5%, low 37.5% | ✅ 解决 |
| Segmentation 方法 | KDE (失败 fallback) | Quantile (三等分) | ✅ 稳定 |

## Phase Segmentation 分布

| Phase | Tokens | % | Segments |
|-------|--------|---|----------|
| high_sparsity (≈execution) | 25,862 | 30.0% | 511 |
| mid_sparsity (≈transition) | 27,996 | 32.5% | 391 |
| low_sparsity (≈reasoning) | 32,349 | 37.5% | 454 |
| **Total** | **86,207** | **100%** | **1,356** |

Quantile segmentation 产生了均匀的三分法，彻底解决了 v2 的极端偏斜问题。

## Interaction Index (II) 结果

### Per-phase × sparsity

| Phase | Sparsity | II Mean | 95% CI Low | 95% CI High | Direction |
|-------|----------|---------|------------|-------------|-----------|
| high_sparsity | 0.1 | +0.2317 | +0.1338 | +0.3418 | super-additive |
| high_sparsity | 0.2 | +2.1574 | +1.0605 | +3.5491 | super-additive |
| mid_sparsity | 0.1 | +0.1607 | +0.0886 | +0.2489 | super-additive |
| mid_sparsity | 0.2 | +0.3049 | -1.0635 | +1.3044 | inconclusive (CI crosses 0) |
| low_sparsity | 0.1 | +0.1711 | +0.0782 | +0.2768 | super-additive |
| low_sparsity | 0.2 | +1.1294 | +0.4368 | +1.9593 | super-additive |

### Perplexity breakdown

| Phase | Sparsity | Dense | Attn-only | KV-only | Both |
|-------|----------|-------|-----------|---------|------|
| high_sparsity | 0.1 | 1.146 | 1.368 | 2.151 | 2.505 |
| high_sparsity | 0.2 | 1.146 | 2.258 | 4.310 | 8.673 |
| mid_sparsity | 0.1 | 1.123 | 1.184 | 2.031 | 2.302 |
| mid_sparsity | 0.2 | 1.123 | 3.450 | 4.195 | 7.442 |
| low_sparsity | 0.1 | 1.111 | 1.282 | 2.587 | 3.004 |
| low_sparsity | 0.2 | 1.111 | 1.996 | 4.701 | 8.077 |

## MVP Pass 条件判定

| 条件 | 结果 | 说明 |
|------|------|------|
| CI nonoverlap (任一 phase 对) | ❌ FAIL | sparsity=0.1 三个 phase CI 全部重叠; sparsity=0.2 high vs mid 勉强重叠 (1.06 vs 1.30) |
| Sign reversal (super↔sub) | ❌ FAIL | 所有 II mean > 0，均为 super-additive。mid_sparsity@0.2 CI 虽跨零但 mean 仍正 |
| **Overall** | **❌ FAIL** | |

## 与 v2 对比

| 指标 | v2 | v3 | 解读 |
|------|-----|-----|------|
| Verdict | FAIL (technical) | FAIL (negative) | v2 因技术问题不可信，v3 是真实的 negative |
| CI nonoverlap | true (但基于偏斜分布) | false | v2 的 nonoverlap 是偏斜分布的 artifact |
| Sign reversal | false | false | 一致 |
| Phase 分布 | 极度偏斜 | 均匀 | v3 segmentation 有效 |
| NaN/Inf | Inf at execution | 无 | v3 数值稳定 |
| II 方向 | 全 super-additive | 全 super-additive | 一致 |

## 结论

1. **技术层面 v3 成功**：quantile segmentation 修复了 v2 的两个核心 bug（KDE 失败导致分布偏斜 + 高 sparsity 导致数值爆炸），测量框架现在是可信的。

2. **假设层面 negative**：compound sparsity 的交互强度在不同 attention sparsity regime 间**没有**显著差异。所有 phase 的 II 均为正（super-additive），amplitude 差异不大且 CI 重叠。这意味着 attention head pruning 和 KV cache eviction 的交互效应在推理的不同阶段基本一致，不存在原假设中预期的"方向反转"。

3. **v2 的 CI nonoverlap 是假阳性**：v2 报告的 CI nonoverlap 源于 90.7% 样本被归为 transition（KDE 失败），使得其他 phase 样本极少、CI 极宽。修复分布后效应消失。

## 下一步建议

- **M1 假设可能需要根本性重新审视**：三次迭代（v1/v2/v3）均未发现 phase-dependent interaction。可能的方向：
  - 改用 task-level（而非 token-level）的 phase 定义
  - 考虑 II 的 non-linearity 是否需要更高的 sparsity 才能显现（但 v2 已证明高 sparsity 会导致数值问题）
  - 重新考虑 compound sparsity 是否真的存在 phase-dependent 行为，还是 uniform super-additive 就是真实模式
- **考虑 pivot**：如果 compound sparsity 交互确实是 phase-invariant 的，PACS 的核心前提（phase-gated sparsity allocation）的收益上界可能较低
