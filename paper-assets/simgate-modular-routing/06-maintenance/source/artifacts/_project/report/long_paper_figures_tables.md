# Long Paper Figures & Tables Plan

基于 short paper 现有内容和 long paper 扩展需求，按 section 列出所有 figures/tables。

---

## Abstract
无 figure/table。

---

## Introduction (§1)

### Figure 1: Motivating Example — Death Cascade in ScienceWorld
- **数据来源**: 可从 plan-012 episode data 中选取典型 episode
- **当前状态**: 需要新建
- **内容**: 一个 ScienceWorld episode 的 step-by-step 对比 (internal vs deterministic)，展示 internal 在某步 hallucinate state transition → 连锁反应 → death。右侧 deterministic 正确执行。
- **建议位置**: 正文 (§1, 占 ~1/3 column)
- **备注**: Long paper 有空间放 motivating figure；short paper 无此图

---

## Related Work (§2)

无 figure/table。纯文字 section。

---

## Method (§3)

### Figure 2: Counterfactual Episode Collection Pipeline
- **数据来源**: 方法描述 (method.tex §3.1–3.3)
- **当前状态**: 需要新建
- **内容**: 流程图 — task instance → fork → pure-internal episode / pure-deterministic episode → (s_int, d_int, s_det, d_det) → labeling rules → episode label。包含 DAF 公式框。
- **建议位置**: 正文 (§3)
- **备注**: Short paper 无 pipeline figure。Long paper 的 Method section 扩展到 1.5 pages，需要可视化。

### Algorithm 1: Episode-Level Counterfactual Labeling
- **数据来源**: method.tex §3.2 的四条 labeling rules
- **当前状态**: 需要新建 (short paper 用 enumerate 而非 algorithm box)
- **内容**: 伪代码，输入 (s_int, s_det, d_int, d_det)，输出 label ∈ {det_preferred, internal_preferred, no_preference}
- **建议位置**: 正文 (§3)
- **备注**: Algorithm box 提升论文形式感，回应 "analysis paper, no method contribution" concern

---

## Experiments (§4)

### §4.1 ScienceWorld Death Decomposition (Core)

#### Figure 3: DAF Scatter Plot — Death Rate Differential vs Δ_full
- **数据来源**: plan-012-full
- **当前状态**: **已有** — short paper Figure 1 (`fig1_daf_scatter.pdf`)
- **内容**: 11 task types scatter, x = death rate diff (int − det), y = Δ_full, Pearson r = 0.9698
- **建议位置**: 正文 (§4.1)
- **需要扩展**: 无重大修改。可加 regression line CI band 和标注 find-non-living-thing 为 outlier。

#### Table 1: Baseline Strategy Comparison
- **数据来源**: plan-003-baseline-245eps, plan-003-bootstrap-95ci
- **当前状态**: **已有** — short paper Table 2 (`tab:baselines`)
- **内容**: Always-Internal / Always-Det / Random / Oracle / Trained Router 的 score, 95% CI, death%
- **建议位置**: 正文 (§4.1)
- **需要扩展**: 无。数据完整。

#### Table 2: Per-Task Death Decomposition
- **数据来源**: plan-012-full
- **当前状态**: **已有** — short paper Appendix A Table 3 (`tab:per-task`)
- **内容**: 11 task types, n, Δ_full, D%_int, D%_det, D/I/N labels
- **建议位置**: **升级到正文** (§4.1) — 这是核心数据表
- **需要扩展**: 可加 Δ_nd 和 per-task DAF 列

#### Figure 4: Per-Task DAF Bar Chart
- **数据来源**: plan-012-full per-task data
- **当前状态**: 需要新建
- **内容**: 11 task types 横轴, DAF 纵轴。find-non-living-thing 显著低于其他 task (bimodal distribution 可视化)
- **建议位置**: 正文 (§4.1)
- **备注**: Short paper 无此图。补充 scatter plot 之外的另一个视角。

### §4.2 Multi-Model Validation (pending)

#### Table 3: Multi-Model DAF Comparison
- **数据来源**: multi-model-pilot (status: RUNNING)
- **当前状态**: 需要新建 (实验进行中)
- **内容**: Model A (Qwen2.5-7B) vs Model B (TBD) 的 DAF, Δ_full, Δ_nd, r 对比
- **建议位置**: 正文 (§4.2)
- **备注**: 实验未完成，表格结构先占位

### §4.3 Cross-Domain Negative Contrast (MATH)

#### Table 4: MATH 300-Problem Results
- **数据来源**: math-negative-contrast
- **当前状态**: 需要新建 (short paper 只在 Limitations 段落提了 50-problem pilot)
- **内容**: N=300, internal accuracy 81.7% vs code 76.7%, diff +5.0% CI [+0.7%, +9.3%], label distribution 266/25/9, by-level breakdown (L4 vs L5)
- **建议位置**: 正文 (§4.3)

#### Figure 5: ScienceWorld vs MATH Signal Direction Comparison
- **数据来源**: plan-012-full + math-negative-contrast
- **当前状态**: 需要新建
- **内容**: 双面柱状图 or paired bar — ScienceWorld (det > int, +29.60) vs MATH (int > code, +5.0%)。视觉化 "signal reversal"。
- **建议位置**: 正文 (§4.3)

### §4.4 Temporal Analysis + Failure Modes (新 section)

#### Figure 6: Death Timing Distribution
- **数据来源**: plan-012 episode data (step-level)
- **当前状态**: 需要新建
- **内容**: Histogram — 在哪个 step 发生 death (internal vs deterministic)。是否 early steps 更致命？
- **建议位置**: 正文 (§4.4) 或 Appendix
- **备注**: 需要回溯 episode 原始数据

#### Table 5: Failure Mode Taxonomy
- **数据来源**: plan-012 episode data，需要人工分类
- **当前状态**: 需要新建
- **内容**: Internal strategy death 的常见原因分类 (hallucinated temperature, wrong container, etc.)，各类频率
- **建议位置**: 正文 (§4.4) 或 Appendix

### §4.5 Ablations

#### Table 6: Router Architecture Comparison
- **数据来源**: plan-004 (v5 + ablation-b)
- **当前状态**: **已有** — short paper Appendix D Table 5 (`tab:hyperparams`) + §4.3 text
- **内容**: Classification head vs Implicit router — logit-level, generation-level metrics, logit-generation gap
- **建议位置**: **升级到正文** (§4.5)
- **需要扩展**: 整合为一张对比表 (architecture / logit acc / gen acc / logit-gen gap / internal recall / degenerate?)

#### Table 7: Gradient Accumulation Effect
- **数据来源**: plan-004-v5 (GA=1) vs plan-004-ablation-b (GA=8)
- **当前状态**: 需要新建 (short paper 只在 Appendix D 文字提及)
- **内容**: GA=1 vs GA=8 对 implicit router 的影响 — balanced acc, internal recall
- **建议位置**: 正文 (§4.5) 或 Appendix
- **备注**: 可合并入 Table 6

#### Table 8: Keyword Routing Structural Failure
- **数据来源**: plan-011-rule-based
- **当前状态**: 需要新建 (short paper 只一句话提及)
- **内容**: v1/v2/v3 keyword lists, match rate, routing behavior, conclusion
- **建议位置**: 正文 (§4.5)

---

## Discussion (§5)

### Table 9: ALFWorld Exploratory Results
- **数据来源**: alfworld-counterfactual-full
- **当前状态**: 需要新建 (short paper 在 Limitations 文字段提及)
- **内容**: 135 games, 6 task types, det/int success rates, label distribution, mechanism comparison with ScienceWorld
- **建议位置**: 正文 (§5 Discussion) 或 Appendix
- **备注**: 作为 "mechanism differs" 的对比证据

---

## Appendix

### Table A1: Labeling Quality Audit Detail
- **数据来源**: plan-013-labeling-quality
- **当前状态**: **已有** — short paper Appendix A
- **内容**: Tie breakdown, genuine vs artifact labels, strict retrain vs full retrain
- **建议位置**: 保留 Appendix (部分核心数据升级到正文 §4.1 或 §4.5)

### Table A2: Correlation Robustness (LOO)
- **数据来源**: plan-012-full LOO analysis
- **当前状态**: **已有** — short paper Appendix B (`tab:loo`)
- **内容**: Leave-one-out Pearson r for each task removed
- **建议位置**: 保留 Appendix

### Table A3: Router Hyperparameters
- **数据来源**: plan-004
- **当前状态**: **已有** — short paper Appendix D (`tab:hyperparams`)
- **内容**: Base model, LoRA config, LR, etc.
- **建议位置**: 保留 Appendix

### Table A4: Penalty Sensitivity
- **数据来源**: plan-012-penalty-sensitivity
- **当前状态**: **已有** — short paper Appendix E (`tab:penalty-sensitivity`)
- **内容**: P vs Δ_full(P) vs DAF(P)
- **建议位置**: 保留 Appendix (可能升级，见 appendix_promotion_plan)

### Table A5: Step-Level Tie Rate by Task
- **数据来源**: plan-012-step-tie-rate
- **当前状态**: 需要新建 (short paper 只报告 aggregate 97.4%)
- **内容**: Per-task step-level tie rate breakdown (11 tasks)
- **建议位置**: Appendix

### Table A6: 30-Task Prescreening Robustness
- **数据来源**: paper_framing.md robustness check data
- **当前状态**: 需要新建
- **内容**: 30 tasks / 249 eps, Δ_full=+38.33, Δ_nd=+0.48, DAF=98.75%, r=0.9864
- **建议位置**: Appendix

### Figure A1: 4-Seed Router Variance
- **数据来源**: plan-004-ablation-b (4 seeds)
- **当前状态**: 需要新建
- **内容**: 4 seeds 的 balanced acc / internal recall / det recall bar chart with error bars
- **建议位置**: Appendix

### Table A7: MATH Per-Level Breakdown
- **数据来源**: math-negative-contrast
- **当前状态**: 需要新建
- **内容**: Level 4 vs Level 5 分开的 accuracy, gap, label distribution
- **建议位置**: Appendix

### Table A8: ALFWorld Per-Task-Type Results
- **数据来源**: alfworld-counterfactual-full
- **当前状态**: 需要新建
- **内容**: 6 task types 各自的 det/int success rate, labels
- **建议位置**: Appendix

---

## Summary Inventory

| ID | Type | Section | Status | Priority |
|---|---|---|---|---|
| Fig 1 | Figure | §1 Intro | 需要新建 | High |
| Fig 2 | Figure | §3 Method | 需要新建 | High |
| Alg 1 | Algorithm | §3 Method | 需要新建 | High |
| Fig 3 | Figure | §4.1 | 已有 (扩展) | Low |
| Tab 1 | Table | §4.1 | 已有 | Low |
| Tab 2 | Table | §4.1 | 已有→升级到正文 | Medium |
| Fig 4 | Figure | §4.1 | 需要新建 | Medium |
| Tab 3 | Table | §4.2 | 需要新建 (pending exp) | High |
| Tab 4 | Table | §4.3 | 需要新建 | High |
| Fig 5 | Figure | §4.3 | 需要新建 | High |
| Fig 6 | Figure | §4.4 | 需要新建 | Medium |
| Tab 5 | Table | §4.4 | 需要新建 | Medium |
| Tab 6 | Table | §4.5 | 已有→扩展升级 | Medium |
| Tab 7 | Table | §4.5 | 需要新建 (可合并) | Low |
| Tab 8 | Table | §4.5 | 需要新建 | Medium |
| Tab 9 | Table | §5 Discussion | 需要新建 | Medium |
| Tab A1–A8, Fig A1 | Mixed | Appendix | 部分已有/部分新建 | Low |

**需要新建**: 10 正文 items + 5 appendix items = 15 total
**已有可复用**: 5 items (Fig 3, Tab 1, Tab A2, Tab A3, Tab A4)
**已有需升级/扩展**: 3 items (Tab 2, Tab 6, Tab A1)
