# O(1) Recurrence-Aware KV Eviction — Research Dashboard

> 最后更新: 2026-05-12 17:32 UTC | 更新原因: 修正 KeyDiff 描述（Reviewer 自我修正：kvpress 实现是 centroid-based O(B)，非 pairwise O(B²)）+ 更新时间估计

## 核心方向
O(1) per-token KV cache eviction using EMA similarity scoring。目标 EMNLP 2026 ARR（DDL 2026-05-25）。

**状态：⚠️ MVP FINAL GATE — 等 gamma_sweep 结果决定 continue/archive**

## 当前进展
- **10/10 实验 negative**，EMA centroid similarity 作为 eviction signal 在所有测试条件下未通过 sanity gate
- EMA 被**双向证伪**：原始方向（evict low）≈ random；反转方向（evict high）比 random 差 15%
- 文献确认 EMA smoothing 是根本缺陷（DefensiveKV: mean aggregation 在 importance 突变时灾难性失败）
- **Recency baseline 在 WikiText-2 仅比 full cache 差 0.09%**，signal-based 方法天花板极低
- **KeyDiff 修正**：kvpress 实现是 centroid-based O(B)（exact per-step mean），证明 centroid eviction 思路本身可行。EMA 失败在于 running average 近似导致区分度丧失（exact mean vs decayed EMA）。论文原始算法是 block-wise iterative pairwise O(B²)，两种实现机制不同但都有效

## 最终 Gate：analysis_gamma_sweep
- GPU 0 独占运行中，预计 ~2.5-3h 完成（Reviewer 修正）
- 测试 8 个 gamma 值（0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99）
- 已完成 gamma=0.1: PPL 8.17，比 random 差 7%
- **Gate 标准**：任一 gamma beat random ≥5% → continue；全部 fail → archive
- D003 数据预示高 gamma 也不乐观（ema_0.9 vs random 仅差 1.77%）

## 近期任务
- [ ] 等 gamma_sweep 完成，验证全部 gamma 值 PPL
- [ ] GPU 1: analysis_heatmap（per-layer EMA 可视化）
- [ ] 统一 literature_map.yaml 中 KeyDiff 描述（论文 O(B²) vs kvpress O(B)）
- [ ] inverted_ema_reasoning_v2 registry → CANCELLED

## Phase 1-5 — SUSPENDED
全部挂起，等 gamma_sweep gate 结果。Gate FAIL → 全部取消 → archive。

## GPU 预算
- 分配：2×RTX PRO 6000 96GB @ westd-16980（cuda:0, cuda:1）
- 当前使用：GPU 0 = gamma_sweep; GPU 1 = 空闲（待调度 heatmap）

## Pivot 备忘（仅供 archive 后参考）
如果 gamma_sweep FAIL 后有人要 pivot：用 exact per-step mean 替代 EMA 可把复杂度从 O(1) 升到 O(B)（与 H2O/TOVA 同级），保留 pre-attention + FlashAttention 兼容优势。但这超出当前 DDL，且需要与 kvpress KeyDiff 做差异化。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D010 | 2026-05-12 | D009 修正：gamma=0.99 beat random +1.38%（唯一），但 gate 仍 | analysis_gamma_sweep |
| D009 | 2026-05-12 | D008 gate FAIL: gamma_sweep 全谱扫描无一 beat random, EM | analysis_gamma_sweep, d003_wikitext_32k, inverted_ema_wikitext, analysis_decay_curve |
| D008 | 2026-05-12 | Conditional archive: gamma_sweep is final gate for | analysis_gamma_sweep, inverted_ema_wikitext, d003_wikitext_32k, d003_reasoning_traces, analysis_decay_curve, analysis_attn_vs_ema |
| D007 | 2026-05-12 | Inverted EMA hypothesis doubly negated; skip reaso | inverted_ema_wikitext, inverted_ema_reasoning, analysis_gamma_sweep |
| D006 | 2026-05-12 | Pivot to inverted EMA eviction: evict low-EMA toke | d003_wikitext_32k, analysis_decay_curve, inverted_ema_reasoning, inverted_ema_wikitext |
| D005 | 2026-05-12 | D003 sanity gate FAIL — EMA eviction 劣于 random，γ 模 | d003_wikitext_32k, d003_reasoning_traces |
| D004 | 2026-05-12 | D003 允许最后一次部署尝试 + Plan B contingency 加入实验计划 | d003_reasoning_traces, d003_wikitext_32k |
| D003 | 2026-05-12 | Sanity check FAIL on WikiText-2 4K，但数据/长度条件不匹配动机场景 | sanity_kv_eviction |
| D002 | 2026-05-12 | MVP FAIL → 执行 Path C pivot: 从 CARC cross-axis 转向 O | carc_mvp_seed42, carc_mvp_seed1337 |
| D001 | 2026-05-12 | MVP 定义：cross-axis 假设验证（KV similarity → MLP sparsit | — |

