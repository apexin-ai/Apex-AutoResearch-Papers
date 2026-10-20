# Idea Brief: IRT-FIT: Person-Fit Statistics as Black-Box Benchmark Contamination Detectors for LLMs


- **Idea ID**: `idea_033`
- **Created**: 2026-05-20
- **Approved**: 2026-05-20
- **Source**: foreign:be-idea-gen-0515-4
- **Level**: solid
- **Target Venues**: AAAI 2027 (abstract: July 21, 2026; full paper: July 28, 2026) — primary target: PSN-IRT was AAAI 2026 Oral, strong psychometrics+AI audience, 10 weeks from today is feasible with focused scope on 6 benchmarks, ICLR 2027 (abstract: ~Sep 19, 2026; full paper: ~Sep 24, 2026) — backup allowing fullest experimental scope including post-RL hypothesis test and expanded baseline comparisons

## Seed Topic

web_research

## Core Problem

Can we detect benchmark contamination in LLMs without any access to training data or model internals, using only the pattern of correct/incorrect responses across benchmark items? Specifically, can psychometric person-fit statistics identify the 'sweet spot' of partial contamination (5-30% of items) where scores are meaningfully inflated but existing detectors fail?

## Opportunity / Why Now

All existing contamination detection methods require either training data access (n-gram overlap), model internals (Min-K% Probability, MIA, Self-Critique entropy sequences), or special probing prompts (Time Travel). Yet psychometrics has long used person-fit statistics like lz* to detect cheating examinees from response patterns alone — a contaminated LLM is functionally analogous to a test-taker with item preknowledge. This cross-domain transfer is newly feasible because IRT infrastructure for LLM evaluation has matured: PSN-IRT (AAAI 2026 Oral) calibrates 4PL item parameters (a, b, c, d) across 11 benchmarks and 41,871 items, providing the calibrated item bank needed to compute person-fit statistics at scale. The 4PL feasibility parameter d is particularly relevant — it accounts for item ambiguity that could otherwise be confused with contamination-induced aberrance, reducing false alarms. Meanwhile, Wang et al. (2025) demonstrate that all existing MIA-based detectors are fragile under reasoning-model contamination where RL post-training conceals SFT contamination signals, creating urgent demand for detection methods operating at a different level of abstraction.

## Landscape (SOTA & Limitations)

Contamination detection circa 2026 relies on five established families: (1) time-based partition, (2) Min-K%/Min-K%++ membership inference (ICLR 2024), (3) Time Travel probing (ICLR 2024 Spotlight), (4) ConStat performance-based testing (NeurIPS 2024), and (5) canary GUIDs. Newer approaches include CoDeC (ICLR 2026), which measures in-context learning effects on memorized vs. unseen data; Cross-Context Verification (arXiv 2603.21454), which uses session-isolated solution diversity; Self-Critique (arXiv 2510.09259, ICLR 2026), which detects post-RL contamination via policy collapse in entropy sequences with ~30% AUC improvement over baselines that perform near chance on RL-contaminated data; and Silicon Bureaucracy (arXiv 2603.21636), which audits score credibility through perturbation sensitivity analysis. Critically, Wang et al. (arXiv 2025) show all MIA-based methods fail under reasoning-model contamination where RL conceals SFT signals. On the IRT side, PSN-IRT (AAAI 2026 Oral) calibrates 4PL parameters (discrimination a, difficulty b, guessing c, feasibility d) across 11 benchmarks and 41,871 items but uses them for measurement quality, not contamination. ATLAS (arXiv 2025) uses IRT for adaptive testing efficiency. Han et al. (EACL 2026 Findings) quantify contamination in psychometric personality inventories but do not employ person-fit statistics. PaCoST (EMNLP 2024 Findings) uses paired confidence for contamination but is not IRT-based. In educational testing, lz* and outfit/infit statistics reliably flag cheating with known Type-I error control, with peak detection power at 10-30% item preknowledge (Sinharay, 2017; Karabatsos, 2003). No published or concurrent work connects IRT person-fit statistics to LLM benchmark contamination detection — an extensive search of arXiv 2025-2026, OpenReview, and GitHub confirms this gap remains open.

## Proposed Approach

We compute four IRT person-fit statistics — lz, lz*, outfit, and infit — for each LLM using calibrated 4PL item parameters (a, b, c, d) from PSN-IRT's public release (41,871 items across 11 benchmarks). The analysis proceeds at two levels:

**Level 1: Per-benchmark person-fit.** To respect the unidimensionality assumption, we compute person-fit statistics separately within each benchmark. Before fitting, we run an exploratory factor analysis (EFA) screen within each benchmark to validate approximate unidimensionality, following psychometric best practice (Crisan, Tendeiro & Meijer, 2017) and recent LLM evaluation precedent (arXiv:2509.24186). We focus on 6 benchmarks spanning diverse capabilities: MMLU (knowledge), GSM8K (math), HumanEval (coding), ARC-Challenge (science reasoning), HellaSwag (commonsense), and TruthfulQA (factuality).

**Level 2: Aggregated contamination score.** We compute the multiscale lzm statistic (Hong, Lin & Cheng, 2021) — the standardized sum of per-benchmark lz* values — providing an overall contamination indicator that respects the multidimensional ability structure.

**Controlled contamination experiment.** We establish ground truth by fine-tuning three open-source models (Llama 4 Scout 17B-16E, Qwen 3.5-9B, Gemma 4 31B) on varying fractions of benchmark items. We use seven contamination levels (0%, 5%, 10%, 15%, 25%, 50%, 100%) to map the detection power curve. Fine-tuning uses QLoRA to manage memory costs, particularly for the MoE-architecture Scout (109B total parameters, 17B active). For each contaminated variant, we compare person-fit signatures against clean baselines.

**Power analysis and simulation.** We conduct a formal power analysis varying contamination fraction, number of contaminated items, and item difficulty distribution. Based on the educational testing literature, we expect an inverted-U detection power curve: undetectable below ~3% contamination (signal drowned in noise), peak detection at 10-30% (clear item-response aberrance), declining above 50% (inflated ability estimate absorbs contamination), and zero power at 100% (uniform high performance is consistent, not aberrant under IRT). We explicitly characterize this operating range and argue that 5-30% is the most policy-relevant detection window — where contamination meaningfully inflates scores but evades simple methods.

**4PL ablation.** We compare person-fit statistics computed under the full 4PL model vs. a 3PL reduction (fixing d=1) to quantify how the feasibility parameter affects contamination detection sensitivity. The 4PL d parameter absorbs some item-level aberrance (Liao et al., 2012), which reduces false alarms from item ambiguity but may also reduce sensitivity to genuine contamination.

**Post-RL hypothesis test.** As a key hypothesis (not a claimed advantage), we test whether person-fit statistics maintain detection power on post-RL reasoning models where Wang et al. (2025) showed existing MIA-based detectors fail. We create post-RL variants by applying GRPO fine-tuning after SFT-based contamination on Qwen 3.5-9B, specifically testing whether RL smooths out response-level aberrance or preserves it.

**Baselines.** We evaluate detection performance (AUROC, Type-I error at fixed thresholds) against ConStat, PaCoST, CoDeC, Min-K%++, and Self-Critique across all contamination levels and training stages (SFT-only, SFT+RL).

**Toolkit.** We release an open-source Python toolkit (built on py-irt and the R mirt package via rpy2, which natively supports 4PL person-fit computation) that takes any binary response matrix and calibrated 4PL item parameters and outputs per-model, per-benchmark contamination flags with calibrated p-values.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$400-600', 'estimated_gpu_cost': '$800-1050', 'gpu_hours': '320-420', 'speed_bottleneck': 'Sequential fine-tuning of contaminated model variants (3 base models × 7 contamination levels = 21 fine-tuning runs, plus 3 post-RL GRPO runs). Llama 4 Scout requires 4× H100 for QLoRA due to 109B total MoE parameters in memory; Gemma 4 31B needs 2× H100. Full-benchmark inference for 30+ models is parallelizable but each large model requires multi-GPU inference.', 'timeline': '5-6 weeks'}
- **cost_breakdown**: {'fine_tuning': 'Qwen 3.5-9B: ~15 GPU-hrs (7 levels × ~2 hrs); Gemma 4 31B: ~50 GPU-hrs (7 levels × ~7 hrs on 2× H100); Llama 4 Scout: ~70 GPU-hrs (7 levels × ~10 hrs on 4× H100). Post-RL GRPO variants: ~30 GPU-hrs. Total fine-tuning: ~165 GPU-hrs.', 'inference': '30+ models × 6 benchmarks × ~1-3 hrs/model depending on size: ~100-150 GPU-hrs.', 'note': "Costs increased ~50% vs. original estimate due to: (a) 7 contamination levels instead of 4, (b) Gemma 4 31B is 2.5× larger than originally assumed '12B', (c) explicit MoE memory overhead for Scout, (d) added simulation study and post-RL GRPO variants.", 'simulation': 'Power analysis simulation (synthetic response matrices, 1000 replications × 7 contamination levels × 6 benchmarks): ~20 GPU-hrs on CPU/light GPU.'}
- **human_in_loop**: {'claude_api_cost': '$200-300', 'estimated_gpu_cost': '$700-875', 'gpu_hours': '280-350', 'timeline': '8-9 weeks'}
- **manual**: {'estimated_gpu_cost': '$750-1000 (H100 at ~$2.50/hr)', 'gpu_hours': '300-400', 'timeline': '12 weeks'}

## Key References

- Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory (AAAI 2026 Oral, arXiv 2505.15055) — calibrates 4PL item parameters for 41,871 items across 11 benchmarks
- Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks (arXiv 2511.04689) — ATLAS, IRT for adaptive testing efficiency
- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024)
- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection (EMNLP 2024 Findings)
- Detecting Pretraining Data from Large Language Models / Min-K% Probability (ICLR 2024)
- Time Travel in LLMs: Tracing Data Contamination in Large Language Models (ICLR 2024 Spotlight)
- On The Fragility of Benchmark Contamination Detection in Reasoning Models (arXiv 2510.02386) — Wang et al., shows MIA-based detectors fail under post-RL contamination
- Detecting Data Contamination in LLMs via In-Context Learning / CoDeC (ICLR 2026)
- Detecting Data Contamination from Reinforcement Learning Post-training / Self-Critique (arXiv 2510.09259, ICLR 2026) — post-RL contamination detection via entropy-sequence policy collapse
- Silicon Bureaucracy and AI Test-Oriented Education: Contamination Sensitivity and Score Confidence (arXiv 2603.21636) — perturbation-based score credibility audit
- Quantifying Data Contamination in Psychometric Evaluations of LLMs (EACL 2026 Findings) — Han et al.
- Cross-Context Verification: Hierarchical Detection of Benchmark Contamination through Session-Isolated Analysis (arXiv 2603.21454)
- Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types (Hong, Lin & Cheng, Psychometrika 2021) — lzm multiscale aggregation
- Investigating the Practical Consequences of Model Misfit in Unidimensional IRT Models (Crisan, Tendeiro & Meijer, Applied Psychological Measurement 2017) — effects of unidimensionality violations on person-fit
- The Four-Parameter Logistic Item Response Theory Model As a Robust Method of Estimating Ability Despite Aberrant Responses (Liao et al., 2012) — 4PL absorbs some aberrance via d parameter
- Which Statistic Should Be Used to Detect Item Preknowledge? (Sinharay, JEBS 2017) — power analysis for preknowledge detection
- Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics (Karabatsos, Applied Measurement in Education 2003)
- PerFit: An R Package for Person-Fit Analysis in IRT (Journal of Statistical Software 2016)
- py-irt: A Scalable Item Response Theory Library for Python (INFORMS Journal on Computing 2023)
- mirt: A Multidimensional Item Response Theory Package for the R Environment (Journal of Statistical Software 2012) — supports 4PL person-fit natively

## Reviewer Evaluation

**Scores**:
  - entry_triage_x: **33.0**/5
  - exit_triage_z: **37.0**/5

## Human Review Note

## External Review — Verdict: PASS

- X (entry triage): 33.0%
- Y (terminal self-eval): 44.0%
- Z (exit triage): 37.0%
- Z interval: [30.0%, 43.0%]
- Real improvement (Z-X): +4.0 pp

### Optimization Suggestions
【优化方案】

**A. 核心 Framing 与 Contribution 结构（影响 Novelty + Significance 天花板）**

1. [标题 + Introduction 第 1-2 段] — 将核心定位从 "a cross-domain psychometric method for contamination detection" 重构为 **"establishing the detection frontier at the minimal-information operating point"**。系统性地将所有现有方法按 information access level 排列（binary response pattern < rephrased-item re-test < token probabilities < logits < full weights），IRT-FIT 处于最底层，回答 "仅凭 binary response pattern 能检测到什么" 这一基础问题。 — 命中 Novelty（从 "yet another detector" 变为 "defines a new operating point on the detection frontier"）+ Significance（回答了一个 foundational question）

2. [Contribution 列表] — 将原 Contribution 4 "cross-domain methodological transfer" **降级为方法论背景**（Section 4 开头一句话即可），不再作为独立贡献列出。原因：2026 年 IRT-for-LLM 已有 PSN-IRT (arXiv:2505.15055, AAAI 2026)、ATLAS (arXiv:2511.04689, AAAI 2027)、MedIRT (arXiv:2509.24186, ICLR 2027)、"Lifting the Benchmark Iceberg" (ICLR 2024) 等多篇工作，"迁移 IRT" 本身不再新颖。Novelty 聚焦于 **person-fit for contamination detection** 这一具体未被探索的应用点。 — 命中 Novelty（避免被 "IRT for LLM is well-studied" 攻击）

3. [Contribution 2 / Section 8] — 将 retroactive leaderboard audit 从 "附带 case study" **提升为论文叙事核心**，重命名为 "Contamination Prevalence Analysis"：对 Open LLM Leaderboard v1 存档数据（7K+ models, HuggingFace open-llm-leaderboard-old/results）中所有可获取 per-item response logs 的模型进行全面扫描，绘制 per-benchmark 污染率随时间变化趋势。这是 IRT-FIT 独有的能力——ConStat 需 re-test, Benchmark Inflation (arXiv:2410.09247) 需构建 holdout set, gray-box 方法需 live model access——应成为论文最大差异化卖点。 — 命中 Significance（方法论 + 实证发现的组合远强于纯方法论论文）

4. [Contribution 3] — 将 inverted-U detection power curve 从 "empirical observation + conjecture" 升级为 **"proposition with proof sketch"**：(a) contamination → 0%: aberrance signal 被有限 item 的 sampling noise 淹没，power → 0（标准假设检验极限）; (b) contamination → 100%: 均匀高表现与真实高能力在 binary response 中不可区分（identifiability collapse）。将此定位为 "characterization of detection limits for all binary-response-pattern methods"，而非仅 person-fit 的经验发现。 — 命中 Novelty（从 observation 升级为 theoretical characterization）

**B. Scope 与 Assumptions 精细化（影响 Soundness 下限）**

5. [Section 3 — Scope] — 新增 **SFT generalization effect 讨论段落**：SFT 在子集 benchmark items 上可能产生 partial generalization 到语义相关的未训练 items（例如 fine-tune 20% MMLU biology 题目，剩余 80% biology 也提升），平滑 aberrance signal。讨论后指出 hard-item-only contamination 条件的理论动机（hard items generalization radius 更小）和 per-domain analysis 的控制作用。 — 命中 Soundness（preemptive defense against "SFT ≠ preknowledge" attack）

6. [Section 3 — Scope] — 将 detection scope 从泛化的 "item-level memorization contamination" 精确化为 **"intentional SFT contamination / leaderboard gaming"** 作为 primary target，明确 pretraining exposure 产生的 smooth distributional ability improvement 不在检测范围内，并解释为何 intentional contamination 恰好是社区最需要检测的场景。 — 命中 Soundness（honest scoping 比含糊 claim 更有力）

**C. Method 层面增强（影响 Soundness + Novelty）**

7. [Section 4.2 — 新增段落 "Why lz* over simple statistics"] — 解释 lz* 评估完整 item-response vector 的联合似然（joint likelihood of the specific correct/incorrect combination give

_Reviewed by external pipeline (batch7), 2026-05-20_


## MVP Validation Results

- **Date**: 2026-05-20
- **Hypothesis Supported**: Yes

### Key Metrics

Phase A: MMLU power@15%=97.9%, HellaSwag=73.3%, GSM8K=57.8%; Null KS p: MMLU=0.594, HellaSwag=0.224, GSM8K=0.098; Phase B: Model 3 MMLU acc=1.000 lz*=+34.75 (θ=0.777), GSM8K lz*=-15.71, HumanEval lz*=-12.37; All benchmarks lz* SD > 2.5

### Summary

两阶段 MVP 验证完成。Phase A（模拟）：Null check 全通过（PSN-IRT 4PL 参数与 lz* N(0,1) 兼容），MMLU power@15%=97.9%，power 与 n_items 强正相关。Phase B（真实数据）：12 模型 lz* 跨模型 SD >> 0.5，多个 benchmark 检测到异常模型。关键发现：Model 3 MMLU acc=1.0/θ=0.777/lz*=+34.75，中等能力模型答对全部 14042 题——全面污染的典型信号。同模型跨 benchmark lz* 显著为负，支持系统性污染假说。方法机制有效，需引入双侧检测。

### Recommendation

GO — 方法机制验证成功，真实数据发现强污染信号。Research 阶段优先：(1) 双侧检测框架 (2) 模型身份确认 (3) 服务器环境配置 (4) paper framing + experiment plan
