# Paper Agent Input Materials — entrainment_gated_ft

> Generated 2026-05-19. 论文写作启动前的材料清单。

## 1. Paper Framing 摘要

### 3 Core Claims

| Claim | 内容 | 主证据 | 强度 |
|-------|------|--------|------|
| C1: Task-Specific Convergence | Attention 使 hybrid recurrent 架构仅在 LAMBADA 上显著趋同（10 benchmarks 中唯一）。Task-specificity 是核心发现 | ρ=-1.0, BCa CI [-1.0, -0.7], exact permutation p=0.0167 (two-tailed, n=5) | 2.5/5 |
| C2: Scale-Dependent Convergence | 1.3B 完全趋同（79% std reduction），340M 仅部分（56%，non-monotonic rebound） | Binary contrast, 2 scale points only | 2.0/5 |
| C3: Per-Example Divergence | Aggregate convergence 下 per-example Jaccard < 0.10，架构间 helped/hurt 集合几乎不重叠；decoupling — aggregate 渐变 vs per-example 一步饱和 | Jaccard analysis + decoupling_data.csv | 3.5/5 |

### Evidence Chain

1. **Convergence**: 10-benchmark survey → only LAMBADA significant → task-specificity framing
2. **BCa CI**: [-1.0, -0.7] (valid-only, 88.75% valid resamples) as primary evidence; does NOT depend on multiple comparison correction
3. **Bonferroni**: 6-benchmark pre-registered adj-p=0.100 — report honestly as "does not survive strict Bonferroni"
4. **Per-example**: Jaccard ~0.04-0.10, architecture-specific helped/hurt profiles (GDN net−, HGRN2 net+)
5. **Decoupling (D008)**: aggregate σ gradually decreases across 5 attention levels; Jaccard saturates immediately at first level (4%)
6. **GDN sensitivity (D007)**: excluding GDN — LAMBADA ρ→-0.7 (p=0.233), MMLU flips to +0.6

### Statistical Strategy (D009)

1. BCa percentile CI as primary evidence (doesn't depend on multiple comparison)
2. Exact permutation p=0.0167 (two-tailed, 2/120 permutations)
3. 6-benchmark Bonferroni adj-p=0.100 — report honestly
4. 10-benchmark survey in supplementary (task-specificity evidence, NOT for correction)
5. GDN-excluded sensitivity in appendix
6. **Prohibited**: post-hoc subset selection, "2-benchmark Bonferroni", "mechanistic analysis"

## 2. 数据文件位置

### artifacts/paper_data/ (5 files)

| 文件 | 内容 | 对应 Table/Figure |
|------|------|-------------------|
| `convergence_table.csv` | 10 benchmarks × ρ, raw_p, Bonferroni adj-p, std, convergence ratio | Table 1 (main convergence results) |
| `per_example_table.csv` | 3 architectures × helped/hurt counts, net effect, pairwise Jaccard | Table 2 (per-example decomposition) |
| `decoupling_data.csv` | 5 attention ratios × cross_arch_std, Jaccard, net_asymmetry | Table 3 or Figure (decoupling trajectory) |
| `gdn_sensitivity_table.csv` | 6 benchmarks × with/without GDN ρ and p | Appendix (sensitivity analysis) |
| `bca_ci_data.json` | BCa bootstrap details: CI bounds, degenerate %, method notes | Appendix (statistical methodology) |

### 其他 artifacts

| 路径 | 内容 |
|------|------|
| `artifacts/exp-001/data/task_specificity_results.csv` | exp-001 原始数据 |
| `artifacts/exp-003/data/sample_characterization_results.csv` | exp-003 样本特征化数据 |
| `artifacts/exp-003-p2/data/exp-003-p2_summary.txt` | 跨架构 Kruskal-Wallis 检验 |
| `artifacts/wang_et_al_analysis.md` | Wang et al. 模型配置分析 |
| `artifacts/lm_eval_1.3b_results.md` | 1.3B 评估结果汇总 |

### 服务器端数据

| 路径 | 内容 |
|------|------|
| `/root/entrainment_gated_ft/analysis/wang_et_al_differentiation.md` | Wang et al. 差异化分析（已清理 paradox + 更新 p 值） |
| `/root/entrainment_gated_ft/analysis/` | 其他分析脚本和中间结果 |

## 3. 待产出

| 实验 | 状态 | 说明 | 阻塞论文？ |
|------|------|------|------------|
| exp-004-r2 | ✅ 完成 (success) | **Section 4 主文本** (Director 指定)。详见下方 exp-004 数据摘要 | — |
| exp-007 | GPU 运行中 (dtype 修复 + 批处理启动中) | 340M+1.3B LAMBADA logsamples (~2-3h GPU) | 否（Claim 2 补充） |
| COPA 数据不一致 | ✅ 已修复 | summary JSON 修正。Registry 正确 (ρ=-0.667) | — |

### exp-004-r2 数据摘要 (Director 指定进 Section 4 主文本)

**核心发现 1**: GDN ≈ RetNet attention 高度相似（L2 cos=0.995）但 per-example 效应不同 → per-example divergence 不源自 attention 差异，源自 recurrent layer 差异。**Claim 3 decoupling 的直接证据。**

**核心发现 2**: HGRN2 浅层极不同（L2 cos≈0.20）→ 深层收敛（L17-L20>0.93）→ attention 层面也有 convergence gradient，与 aggregate convergence 对应。

**Entropy 假设否定**: attention entropy 无法区分 helped vs hurt（差异 <0.02）。排除 trivial 机制解释。Frame as "descriptive characterization"（符合 W3 约束），不是 mechanistic claim。

**数据文件**:
- 服务器: `/root/entrainment_gated_ft/analysis/attention_weights/`
- 输出: 3×.pt (~126MB), 3×.csv (~59MB), attention_analysis_summary.json, cross_arch_attention_similarity.csv, helped_vs_hurt_entropy.csv

## 4. Related Work 需求

**目标**: 20+ references，覆盖以下 topic areas。Dream review W2 指出当前仅 ~8 references，远低于 EMNLP 标准。

### 必须覆盖的 Topic Areas

| Topic | 关键引用（Paper Agent 需查证） | 与本文关系 |
|-------|-------------------------------|-----------|
| **Ensemble diversity** | Krogh & Vedelsby 1995; Kuncheva & Whitaker 2003 | Per-example divergence 是 ensemble diversity 的已知现象，我们在 hybrid arch 上量化 |
| **Underspecification** | D'Amour et al. 2022 | Aggregate 等价 masks prediction-level 差异——我们的核心 framing anchor |
| **Dataset cartography** | Swayamdipta et al. 2020 | Per-example difficulty varies across models |
| **Hybrid architectures** | Jamba (Lieber et al. 2024); RWKV-6; RecurrentGemma; Wang et al. 2025 | 我们分析的 model family |
| **Attention interpretability** | Jain & Wallace 2019; Clark et al. 2019; Olsson et al. 2022 | exp-004 attention weight 分析的背景 |
| **Simpson's paradox / ecological fallacy** | 统计学教科书 | Aggregate vs disaggregate discrepancy 的经典框架 |
| **Model similarity** | CKA (Kornblith et al. 2019); Fort et al. 2019; McCoy et al. 2020 | 模型行为差异的度量方法 |
| **IRT for NLP** | Lalor et al. 2019; Rodriguez et al. 2021 | Per-example difficulty 建模 |

## 5. 写作约束

### 格式
- **EMNLP 2026**: 8 pages main text (strict), unlimited references
- Limitations + ethics 不计入页数
- ARR 统一审稿，Main/Findings 不分开投稿

### D008 叙事禁令
- **禁止**: "paradox", "paradoxical", "co-evolution", "co-evolve", "paradoxical coexistence"
- **替代**: "divergence", "decoupling", "aggregate-individual decoupling"
- "Simpson's paradox" 仅限 Related Work 引用外部概念，不用于描述本文发现

### D009 统计策略
- BCa CI 为主证据，Bonferroni 如实报告
- 所有 p 值标注方法：exact permutation test, two-tailed, n=5
- 禁止 post-hoc subset selection

### W3 Overclaiming 限制
- 不用 "mechanistic analysis"，用 "characterization" / "decomposition"
- Attention analysis (exp-004) 是 descriptive，不是 causal
- 不声称发现新现象，而是量化已知现象在 hybrid architectures 中的表现

### Task Taxonomy
- 必须在 Method 节 pre-define（不能 post-hoc）
- "Pure context retrieval": next-token prediction requiring long-range context retrieval without reasoning/knowledge
- BoolQ 分类: **comprehension**（非 retrieval）

## 6. 投稿信息

| 项目 | 详情 |
|------|------|
| 目标 | EMNLP 2026 Findings (via ARR) |
| Stretch | EMNLP 2026 Main |
| 提交系统 | ARR June 2026 cycle |
| DDL | ~June 15, 2026（距今 ~27 天） |
| 论文写作启动 | 目标 June 5-7 |
| 当前 Dream 评分 | Best case 2.5/5 |
| 目标评分 | 3.0 (Findings threshold) |
| 最大 leverage | Related Work（0 GPU cost，直接提升评分） |
