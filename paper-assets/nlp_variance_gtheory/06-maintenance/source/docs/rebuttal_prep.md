# Rebuttal 预案

> 预期攻击点及应对策略。每个攻击点：攻击要点 → 回应 → 支持证据。
> 所有 section/table/figure 编号和数字均从论文原文确认。

---

## 攻击点 1：C2 的 n=5 benchmark sample size，permutation p=0.10 不显著

**攻击要点**：The format-associated variance pattern (C2) is tested on only five benchmarks with a permutation p=0.10 that does not reach conventional significance. The MC vs. FF distinction may be spurious.

**回应**：

- C2 is explicitly framed as exploratory throughout the paper. The contribution statement (§1) labels it "Format-associated variance patterns (exploratory)" and states "This hypothesis-generating observation warrants confirmation with larger benchmark samples." The section title (§4.3) reads "Exploratory: Format-Associated Variance Patterns."
- The item-level effect size is d=1.73 (§1, contribution C2), which is a very large effect by Cohen's standards (>0.8). The benchmark-level CI spans zero because n=5 benchmarks is inherently low-powered for a between-benchmark test; this is a sample-size limitation, not evidence of absence.
- C2 can be straightforwardly downgraded to a descriptive observation without affecting C1. C1 (variance decomposition + D-study reproducibility budgets) is entirely independent of the MC/FF distinction: Table 4 reports per-benchmark budgets, and the recommended 3-prompt × 3-seed design (178 items, §4.5) is derived from single-model MMLU variance components, not from cross-format comparisons.
- The Limitations section (§5) already explicitly acknowledges: "The benchmark sample (n=5) limits statistical power for format-associated observations (p=0.10); other formats (code generation, multi-turn dialogue) may differ."

**支持证据**：
- §1 (Introduction): "Format-associated variance patterns (exploratory). MC benchmarks concentrate 68–72% of variance in item-related components; FF benchmarks disperse to 31–41% (item-level d=1.73; benchmark-level confirmation limited by sample size). This hypothesis-generating observation warrants confirmation with larger benchmark samples."
- §4.3 title: "Exploratory: Format-Associated Variance Patterns"
- §4.3: "n=5; permutation p=0.10; item-level d=1.73, benchmark-level CI spans zero); we report this as a descriptive observation."
- §5 (Limitations): "The benchmark sample (n=5) limits statistical power for format-associated observations (p=0.10)"

---

## 攻击点 2：为什么 prompt variance 只有 <3% 而 Sclar 报告 50–76% swings

**攻击要点**：Sclar et al. (2024) reported 50–76% accuracy swings from prompt formatting, yet your analysis finds prompt variance <3%. This seems contradictory and may indicate your design under-samples prompt variation.

**回应**：

- Accuracy range and variance share are fundamentally different quantities. Sclar et al. report the max–min accuracy spread across prompts for individual models—a range statistic sensitive to outliers. Our analysis decomposes total variance into proportional contributions—prompt's share of the overall variance budget. These are not comparable metrics; both can be simultaneously true.
- In the single-model baseline (§4.1), prompt main effect is <0.5% of total variance, but prompt×item interaction is 5.5%—the largest facet×item interaction. This means prompts do affect specific items substantially (consistent with Sclar's item-level observations), but their contribution to the overall variance pool is small because item difficulty (58.4%) and residual (23.1%) dominate.
- The cross-model analysis (Table 2) confirms this: prompt×item = 0.9%, while model×item = 30.2%. Models disagree far more about which items are difficult than prompts do.
- G-theory's value is precisely in distinguishing these two effects: a facet can cause large accuracy swings on specific items (high interaction) while contributing negligibly to total variance (low main effect). Reporting only accuracy ranges, as prior work does, conflates these.
- On FF benchmarks, prompt effects are larger: GSM8K prompt main effect = 5.4%, model×prompt = 8.5% (Table 3), consistent with free-form generation being more sensitive to prompt wording.

**支持证据**：
- §1 (Introduction): "item selection drives 34–38% of evaluation variance on multiple-choice tasks while prompt wording is negligible (<3%)"
- §4.1: "prompt template, temperature, seed, and ordering each <0.5% ... prompt×item is the largest at 5.5%"
- Table 2 (§4.2): prompt×item = 0.9%, model×item = 30.2%
- Table 3 (§4.3): GSM8K prompt = 5.4%, model×prompt = 8.5%; MMLU prompt×item = 0.9%
- §1 (Introduction): citing Sclar et al. — "50–76% accuracy swings from prompt formatting"

---

## 攻击点 3：只有 binary scoring，budget recommendations 是否适用于连续指标

**攻击要点**：All experiments use binary (0/1) scoring. Real-world evaluation increasingly uses partial credit, continuous metrics, or LLM-as-judge rubrics. The budget recommendations may not transfer.

**回应**：

- Binary correctness is the dominant metric in current LLM evaluation practice (leaderboards, benchmark papers, model cards). Our budgets address the most common use case.
- §3.4 (Binary Data Assumptions) establishes robustness of the variance decomposition under binary data through multiple checks:
  1. Henderson Method I produces unbiased estimates for balanced designs regardless of outcome distribution (Brennan, 2001, Ch. 12).
  2. REML comparison: all variance components differ by <0.5pp between estimators (Appendix A).
  3. Probit simulation: Henderson Method I recovers variance component rankings from dichotomized data (Spearman ρ=0.732; item_id dominant in all 100 replications; Appendix A).
  4. GLMM complement: marginal logit link preserves all seven grouped component orderings (ρ=1.0; Appendix A).
  5. Accuracy-range stability: item_id variance share stable across accuracy subsets 0.62–0.72 (r=−0.048; Appendix A).
- We explicitly test metric sensitivity with two alternative scoring methods:
  - **Partial-credit scoring** (GSM8K, 8 models, step-level): G_item drops from 0.863 to 0.768; all eight models show G_partial < G_binary (mean ΔG = −0.135). The variance structure changes—residual rises from 39.9% to 64.9%, item falls from 16.9% to 10.3%—but remains item-dominated. This is reported in §3.4 and Appendix A.
  - **Text-exact-match** (§4.1): G_item collapses to 0.007, with temperature dominating at 79.7%. This dramatic shift demonstrates that metric choice can fundamentally reshape variance structure—a finding that *strengthens* our contribution by showing metric conditionality.
- Budget recommendations are explicitly scoped to binary scoring: §3.4 states "All findings in this paper are conditioned on binary correctness scoring"; the Conclusion (§6) states "All budgets assume binary scoring; extending to other model scales and continuous metrics is a priority"; Limitations (§5) reiterates.

**支持证据**：
- §3.4: "Henderson Method I produces unbiased estimates for balanced designs regardless of outcome distribution"
- §3.4: "REML estimates differ by <0.5pp on all components"
- §3.4: "A probit simulation, GLMM complement (ρ=1.0), and accuracy-range analysis all confirm robustness"
- §3.4: "partial-credit analysis on GSM8K (8 models, step-level scoring) ... G_item drops from 0.86 to 0.77 ... mean ΔG = −0.135"
- §4.1: "For text-exact-match scoring ... temperature dominates at 79.7% ... G_item collapses to 0.007"
- §5 (Limitations): "All D-study budgets reported in this paper are strictly valid only under binary correctness scoring"

---

## 攻击点 4：7–9B 模型 budget 是否 scale-invariant

**攻击要点**：All main experiments use 7–9B parameter models. Budget recommendations may not hold for larger (70B+) or smaller (1–3B) models, limiting practical relevance.

**回应**：

- §4.6 (Preliminary Scale Validation) provides evidence across a 24× parameter range within the Qwen2.5 family (3B/7B/72B) on MMLU:
  - Item difficulty dominates at all three scales: 73–83% of variance, all G > 0.95.
  - Facet ranking is consistent across scales: item_id is always the largest component, all main effects are near zero.
  - The proportional increase at 72B is consistent with the Bernoulli variance ceiling: total variance (0.113) matches p(1−p) at grand mean 0.87, compressing all components while preserving item dominance.
- A cross-family check with Llama-3.1-70B-Instruct (different architecture, BF16, TP=4) yields item difficulty = 74.5%, G_item = 0.957, confirming item-dominated structure is not Qwen-specific. The 8.7pp item share gap (74.5% vs. 83.2% for Qwen-72B) reflects accuracy-dependent Bernoulli ceiling compression, not structural divergence.
- The crossed 3B×7B×72B design shows model×item = 38.5% > item = 35.7%, reflecting expected DIF amplification across the 68–87% accuracy range (G_item = 0.720; three models insufficient for reliable G).
- The section title explicitly labels this "Preliminary Scale Validation," and Limitations (§5) states: "Preliminary scale validation (§4.6) with Qwen2.5 (3B/7B/72B) and cross-family Llama-3.1-70B confirms consistent variance structure across two architecture families, but validation beyond these two families is needed before extrapolating budget recommendations to arbitrary architectures."
- Critically, the *structural* finding—that item difficulty and model×item interaction dominate, while methodological facet main effects are negligible—holds across all tested scales. Budget *numbers* may shift, but the qualitative recommendation (multi-facet designs reduce item requirements) is robust.

**支持证据**：
- §4.6: "item difficulty dominates at all three scales (73–83%, all G > 0.95) with consistent facet ranking"
- §4.6: "Llama-3.1-70B-Instruct ... yields item difficulty = 74.5% (G_item = 0.957), confirming the item-dominated structure across architecturally distinct families: all main effects are zero, and the facet ranking matches Qwen2.5-72B"
- §4.6: "The 8.7pp item share gap (74.5% vs. 83.2%) reflects accuracy-dependent Bernoulli ceiling compression, not structural divergence"
- §4.6: "Three MMLU resamples yield CV = 3.1%"
- §5 (Limitations): "validation beyond these two families is needed before extrapolating budget recommendations to arbitrary architectures"

---

## 补充攻击点（低概率但需准备）

### 5. Henderson Method I 对 binary data 的适用性

**攻击要点**：G-theory assumes continuous outcomes; binary data violates normality assumptions.

**回应简要**：§3.4 directly addresses this. Henderson Method I is distribution-free for balanced designs (Brennan 2001, Ch. 12). Five converging robustness checks confirm: REML (<0.5pp difference), probit simulation (ranking ρ=0.732, item_id dominant in 100/100 replications), GLMM (ρ=1.0), accuracy-range stability (r=−0.048), null calibration (ratio=1.0008). Binary scoring inflates residual and produces conservative D-study budgets (~36% overestimate per probit simulation in Appendix A).

### 6. 模型选择偏差（8 models purposive sampling）

**攻击要点**：Eight models are purposively selected, not randomly sampled from all available models. Results may not generalize.

**回应简要**：§3.6 (Model Facet Specification) treats models as quasi-random (Meredith 1993; Putnick & Bornstein 2016). All G values use random-model assumptions (more conservative): G_random = 0.863–0.896 vs. G_fixed = 0.951–0.990 (Table in Appendix A). LOMO analysis across 40 subsets: CV ≤ 1.25%, max |ΔG| = 0.030. Cohen's κ = 0.33–0.46 confirms genuine DIF. Four-model subset consistency: mean |ΔG| = 0.035. Budget estimates are upper bounds regardless of facet classification.

### 7. 数据污染可能夸大 model×item interaction

**攻击要点**：Pre-training contamination on benchmark items could inflate model×item interaction.

**回应简要**：§5 (Limitations) acknowledges this directly. Three counter-arguments: (1) consistent variance structures across three independently constructed MC benchmarks (MMLU, ARC, HellaSwag) provide indirect evidence against contamination as the sole driver; (2) contamination affects absolute budgets but has limited impact on the multi-facet vs. single-condition budget *ratio*, since both designs are equally exposed; (3) the item-dominated structure persists even on recent benchmarks less likely to be contaminated.
