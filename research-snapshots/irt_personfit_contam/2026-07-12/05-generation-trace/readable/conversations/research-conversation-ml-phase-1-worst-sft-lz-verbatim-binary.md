# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/37473526-c257-40cf-9761-5869389db6d3.jsonl`
- **Structured JSON:** [`c5e5b30d87e6ad3acf3e.json`](../../sessions/c5/c5e5b30d87e6ad3acf3e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T08:41:16.743Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T08:41:16.743Z",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水平污染）不成立，需 reframe。\n核心假设：['SFT 泛化使 partial contamination（5-25%）在 binary response 层面几乎不可区分于能力提升', 'lz* 仅在极端情况下显著：>50% verbatim 污染或 Gemini-1.5 式 100% 全量泄漏', 'Post-RL 完全破坏 person-fit 信号——RL 的 reward shaping 重塑 response pattern', 'Leaderboard per-item logs 不可获取，自跑推理 GPU 预算不足以覆盖有意义规模', 'Power 理论推导发现 4PL 的 d 参数引入不可忽略的 bias，lz* 理论保证在 4PL 下部分失效']\n关键指标范围：{'ctrl_contam_auroc_at_15pct': [0.55, 0.77], 'ctrl_contam_min_detectable_level': [0.3, 0.6], 'ctrl_contam_lz_effect_size_cohens_d': [0.2, 0.8], 'post_rl_power_retention_ratio': [0.05, 0.34], 'power_theory_r_squared': [0.5, 0.79], 'leaderboard_models_scanned': [12, 80], 'leaderboard_flagged_rate': [0.0, 0.03], 'baseline_auroc_advantage_vs_constat': [-0.15, -0.02], 'two_sided_inverted_u_inflection_contam_level': [0.25, 0.5], 'mmlu_power_at_5pct_contam': [0.05, 0.2]}\n叙事方向：核心假设不成立——binary response 的信息量不足以检测现实水平的 SFT 污染。必须 reframe，但不降级 venue。 新 angle：\"IRT person-fit 作为 benchmark integrity 的必要条件检查（necessary but not sufficient）\"。 Reframe 逻辑：(1) 将 lz* 定位为\"极端污染的高置信度筛选器\"而非通用检测器——Gemini-1.5 的 lz*=+34.75 仍是强结果，说明极端 case 的检出是 zero-cost（无需 access）的；(2) 将控制实验的\"负面结果\"本身作为贡献—— \"我们严格量化了 binary response 检测的信息论下界，证明 SFT 泛化是 binary-only 检测的根本瓶颈\"； (3) 用 information-theoretic framing 构建 detection frontier 的完整图景——我们的负面结果 + 文献 正面结果共同刻画了\"信息量 vs 检测力\"的 Pareto 前沿。(4) 发展\"多统计量融合\"方向——lz* + outfit + infit 的联合检验是否能突破单统计量的信息瓶颈。Headline 变为：\"Binary response 检测的信息论极限： IRT person-fit 何时足够、何时不够\"。EMNLP 仍可投——负面结果 + 理论分析 + frontier 框架 对评估方法论社区同样有价值。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_personfit_contam\nfocus: 重点评估：(1) 双侧检测框架是否足够新颖作为独立贡献 (2) 仅 12 模型 + 5 benchmarks 是否 scope 太窄 (3) Gemini-1.5 case study 是否足够有说服力（无 ground truth）(4) 控制实验设计是否能回应 \"no ground truth\" 的审稿意见\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection)**:\nIRT person-fit statistics detect benchmark contamination at the minimal-information operating point on the detection frontier — requiring only binary (correct/incorrect) response patterns, without access to model logits, weights, or training data.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\n\n**Claim 3 (Empirical Prevalence)**:\nApplying IRT-FIT to publicly available LLM benchmark data reveals previously undocumented contamination patterns — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence, and cross-benchmark anomaly consistency across 12 models from PSN-IRT.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics (lz*, outfit, infit) — developed over decades for detecting exam cheating — we answer: \"What can be detected from binary response patterns alone?\" This is a foundational question, not just another detector. We show the method works (97.9% power on MMLU), characterize its limits (power ∝ n_items), and reveal its dual-regime signal structure (partial vs. full contamination).\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT detects benchmark contamination with 97.9% power on MMLU (14K items) and identifies Gemini-1.5's 100% MMLU accuracy as contamination (lz*=+34.75) — a signal invisible to existing detectors that require model internals.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Single-sided test misses full contamination\" | Two-sided detection framework is a core contribution. Gemini-1.5 case study demonstrates. | exp-two-sided |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n\n## Key Narrative Elements (from External Review)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\n4. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n\n## MVP Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed.\n- **Phase B (real data)**: Gemini-1.5 (student_id=3) MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark: GSM8K lz*=-15.71, HumanEval lz*=-12.37. All benchmarks SD >> 0.5.\n- **Key insight from MVP**: Two-sided detection is essential — full contamination produces lz* >> 0 (over-consistent), not lz* << 0 (aberrant).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n- id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点位置。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  notes: CPU only. 修改 simulation.py 参数 + null_check.py 的 NaN 处理。\n- id: exp-ctrl-contam\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 控制实验：在 Qwen3.5-9B 和 Gemma-4-31B 上，用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50%\n    benchmark items，测量微调前后 person-fit 变化。建立 ground-truth contamination → lz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: 'Qwen3.5-9B: 1× RTX 5090 (~8GB). Gemma-4-31B: 1× RTX 5090 (~20GB). 2 模型 ×\n    6 levels × ~3-7 hrs = ~60-80 GPU-hrs.'\n- id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 纯理论推导 + 数值验证。CPU only.\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：获取 per-item response logs（如果 HuggingFace\n    公开了），对所有可用模型计算 person-fit。绘制 per-benchmark 污染率随时间趋势。\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: 主要瓶颈是数据获取。如果 per-item logs 不可用，需要自己跑推理（GPU 预算大幅增加）。先调研数据可用性。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: 与现有方法对比（ConStat, Min-K%++）：在控制实验的 ground-truth contaminated models\n    上，比较 IRT-FIT vs baselines 的 AUROC/Type-I error。\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: 需要 baseline 方法的实现。ConStat 需要 re-test，Min-K%++ 需要 token probabilities。\n- id: exp-multiscale-lzm\n  claim:\n  - 1\n  - 3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim:\n  - 2\n  - 3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T08:41:16.746Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T08:41:16.746Z",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T08:41:16.765Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水平污染）不成立，需 reframe。
核心假设：['SFT 泛化使 partial contamination（5-25%）在 binary response 层面几乎不可区分于能力提升', 'lz* 仅在极端情况下显著：>50% verbatim 污染或 Gemini-1.5 式 100% 全量泄漏', 'Post-RL 完全破坏 person-fit 信号——RL 的 reward shaping 重塑 response pattern', 'Leaderboard per-item logs 不可获取，自跑推理 GPU 预算不足以覆盖有意义规模', 'Power 理论推导发现 4PL 的 d 参数引入不可忽略的 bias，lz* 理论保证在 4PL 下部分失效']
关键指标范围：{'ctrl_contam_auroc_at_15pct': [0.55, 0.77], 'ctrl_contam_min_detectable_level': [0.3, 0.6], 'ctrl_contam_lz_effect_size_cohens_d': [0.2, 0.8], 'post_rl_power_retention_ratio': [0.05, 0.34], 'power_theory_r_squared': [0.5, 0.79], 'leaderboard_models_scanned': [12, 80], 'leaderboard_flagged_rate': [0.0, 0.03], 'baseline_auroc_advantage_vs_constat': [-0.15, -0.02], 'two_sided_inverted_u_inflection_contam_level': [0.25, 0.5], 'mmlu_power_at_5pct_contam': [0.05, 0.2]}
叙事方向：核心假设不成立——binary response 的信息量不足以检测现实水平的 SFT 污染。必须 reframe，但不降级 venue。 新 angle："IRT person-fit 作为 benchmark integrity 的必要条件检查（necessary but not sufficient）"。 Reframe 逻辑：(1) 将 lz* 定位为"极端污染的高置信度筛选器"而非通用检测器——Gemini-1.5 的 lz*=+34.75 仍是强结果，说明极端 case 的检出是 zero-cost（无需 access）的；(2) 将控制实验的"负面结果"本身作为贡献—— "我们严格量化了 binary response 检测的信息论下界，证明 SFT 泛化是 binary-only 检测的根本瓶颈"； (3) 用 information-theoretic framing 构建 detection frontier 的完整图景——我们的负面结果 + 文献 正面结果共同刻画了"信息量 vs 检测力"的 Pareto 前沿。(4) 发展"多统计量融合"方向——lz* + outfit + infit 的联合检验是否能突破单统计量的信息瓶颈。Headline 变为："Binary response 检测的信息论极限： IRT person-fit 何时足够、何时不够"。EMNLP 仍可投——负面结果 + 理论分析 + frontier 框架 对评估方法论社区同样有价值。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_personfit_contam
focus: 重点评估：(1) 双侧检测框架是否足够新颖作为独立贡献 (2) 仅 12 模型 + 5 benchmarks 是否 scope 太窄 (3) Gemini-1.5 case study 是否足够有说服力（无 ground truth）(4) 控制实验设计是否能回应 "no ground truth" 的审稿意见

## paper_framing.md

# Paper Framing — irt_personfit_contam

## Target Venue
- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)
- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)
- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)

## Core Claims (3 条)

**Claim 1 (Minimal-Information Detection)**:
IRT person-fit statistics detect benchmark contamination at the minimal-information operating point on the detection frontier — requiring only binary (correct/incorrect) response patterns, without access to model logits, weights, or training data.

**Claim 2 (Detection Characterization)**:
Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.

**Claim 3 (Empirical Prevalence)**:
Applying IRT-FIT to publicly available LLM benchmark data reveals previously undocumented contamination patterns — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence, and cross-benchmark anomaly consistency across 12 models from PSN-IRT.

## Story Spine

**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.

**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.

**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics (lz*, outfit, infit) — developed over decades for detecting exam cheating — we answer: "What can be detected from binary response patterns alone?" This is a foundational question, not just another detector. We show the method works (97.9% power on MMLU), characterize its limits (power ∝ n_items), and reveal its dual-regime signal structure (partial vs. full contamination).

**Headline result template**: "Using only binary response patterns, IRT-FIT detects benchmark contamination with 97.9% power on MMLU (14K items) and identifies Gemini-1.5's 100% MMLU accuracy as contamination (lz*=+34.75) — a signal invisible to existing detectors that require model internals."

## Venue Fit Risks

- **EMNLP**: NLP evaluation methodology fits well. Risk: "no new NLP model/technique" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).
- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.
- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.

## Anticipated Reviewer Concerns & Planned Responses

| # | Concern | Response Strategy | Supporting Experiment |
|---|---------|------------------|----------------------|
| R1 | "Just applying existing IRT to LLMs" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade "cross-domain" from contribution to background. | — |
| R2 | "No ground truth contamination labels" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |
| R3 | "Power too low for small benchmarks" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |
| R4 | "Only 12 models" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |
| R5 | "SFT generalization smooths signal" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |
| R6 | "Single-sided test misses full contamination" | Two-sided detection framework is a core contribution. Gemini-1.5 case study demonstrates. | exp-two-sided |
| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |

## Key Narrative Elements (from External Review)

1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.
3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).
4. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.

## MVP Evidence Summary

- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed.
- **Phase B (real data)**: Gemini-1.5 (student_id=3) MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark: GSM8K lz*=-15.71, HumanEval lz*=-12.37. All benchmarks SD >> 0.5.
- **Key insight from MVP**: Two-sided detection is essential — full contamination produces lz* >> 0 (over-consistent), not lz* << 0 (aberrant).


## experiment_plan (with registry status)

- id: exp-two-sided
  claim: 2
  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case
    study）。包括 bootstrap confidence interval 和 FDR 控制。
  priority: P0
  gpu_budget_hours: 0
  deps: []
  status: planned
  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。
- id: exp-extended-sim
  claim: 2
  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让
    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点位置。
  priority: P0
  gpu_budget_hours: 0
  deps: []
  status: planned
  notes: CPU only. 修改 simulation.py 参数 + null_check.py 的 NaN 处理。
- id: exp-ctrl-contam
  claim:
  - 1
  - 2
  - 3
  description: 控制实验：在 Qwen3.5-9B 和 Gemma-4-31B 上，用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50%
    benchmark items，测量微调前后 person-fit 变化。建立 ground-truth contamination → lz* 映射。
  priority: P0
  gpu_budget_hours: 80
  deps:
  - exp-two-sided
  status: planned
  notes: 'Qwen3.5-9B: 1× RTX 5090 (~8GB). Gemma-4-31B: 1× RTX 5090 (~20GB). 2 模型 ×
    6 levels × ~3-7 hrs = ~60-80 GPU-hrs.'
- id: exp-power-theory
  claim: 2
  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A
    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-extended-sim
  status: planned
  notes: 纯理论推导 + 数值验证。CPU only.
- id: exp-leaderboard-audit
  claim: 3
  description: Open LLM Leaderboard v1 大规模扫描：获取 per-item response logs（如果 HuggingFace
    公开了），对所有可用模型计算 person-fit。绘制 per-benchmark 污染率随时间趋势。
  priority: P1
  gpu_budget_hours: 20
  deps:
  - exp-two-sided
  status: planned
  notes: 主要瓶颈是数据获取。如果 per-item logs 不可用，需要自己跑推理（GPU 预算大幅增加）。先调研数据可用性。
- id: exp-4pl-ablation
  claim: 1
  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter
    d 对 false alarm 和 detection power 的影响。
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-extended-sim
  status: planned
  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。
- id: exp-baseline-comparison
  claim: 1
  description: 与现有方法对比（ConStat, Min-K%++）：在控制实验的 ground-truth contaminated models
    上，比较 IRT-FIT vs baselines 的 AUROC/Type-I error。
  priority: P1
  gpu_budget_hours: 30
  deps:
  - exp-ctrl-contam
  status: planned
  notes: 需要 baseline 方法的实现。ConStat 需要 re-test，Min-K%++ 需要 token probabilities。
- id: exp-multiscale-lzm
  claim:
  - 1
  - 3
  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化
    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-two-sided
  status: planned
  notes: CPU only. 需要实现 lzm 公式。
- id: exp-post-rl
  claim: 1
  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应
    Wang et al. (2025) 的 MIA 失效问题。
  priority: P2
  gpu_budget_hours: 40
  deps:
  - exp-ctrl-contam
  status: planned
  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。
- id: exp-extra-benchmarks
  claim:
  - 2
  - 3
  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items
    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。
  priority: P2
  gpu_budget_hours: 10
  deps:
  - exp-extended-sim
  status: planned
  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。
- id: exp-domain-analysis
  claim: 3
  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5
    的 MMLU 污染是全面的还是集中在特定 domain。
  priority: P2
  gpu_budget_hours: 0
  deps:
  - exp-two-sided
  status: planned
  notes: CPU only. 需要 MMLU item-to-domain 映射。


## registry (completed experiments)

- exp_id: sim_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    null_check:
      all_pass: true
      gsm8k_ks_p: 0.098
      hellaswag_ks_p: 0.224
      mmlu_ks_p: 0.594
    simulation_power_at_15pct:
      mmlu: 0.979
      hellaswag: 0.733
      gsm8k: 0.578
      arc_c: 0.129
      humaneval: 0.243
    global_pass: false
    inverted_u_all_benchmarks: true
    pass_count_large_80pct: 1/3 (mmlu only)

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "13e3121b-ff3e-4339-9ffa-a4e255bed755",
  "type": "user",
  "uuid": "0532699d-51ad-405f-b661-953dcfa670eb",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T08:41:16.763Z_

```json
{
  "parentUuid": "0532699d-51ad-405f-b661-953dcfa670eb",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "e91698a0-59c8-4fc1-8ea7-42d57320a9ba",
  "timestamp": "2026-05-20T08:41:16.763Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T08:41:16.764Z_

```json
{
  "parentUuid": "e91698a0-59c8-4fc1-8ea7-42d57320a9ba",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "989483e3-9274-4ced-b3a8-ab23a8860a67",
  "timestamp": "2026-05-20T08:41:16.764Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水平污染）不成立，需 reframe。 核心假设：['SFT 泛化使 partial contamination（5-25%）在 binary response…",
  "leafUuid": "989483e3-9274-4ced-b3a8-ab23a8860a67",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe IRT contamination detection as information-theoretic frontier",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3"
}
```

---

### Assistant

_source line 8 · 2026-05-20T08:41:30.569Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all planned experiments in the `experiment_plan`, under the "worst" tier scenario. Let me carefully analyze each experiment and predict what would happen given the worst-case assumptions defined in Phase 1.

Let me re-read the worst tier definition:

- SFT generalization severely smooths signals
- lz* only detectable at near-total contamination or complete verbatim memorization
- Core assumption (binary data sufficient to detect realistic contamination) doesn't hold
- Post-RL completely destroys person-fit signal
- Leaderboard per-item logs unavailable, GPU budget insufficient


- Power theory shows 4PL d parameter introduces non-negligible bias

Now I'm going through each of the nine planned experiments to predict their outcomes under these worst-case conditions. For most of them, I expect severely degraded signal detection, inflated false negatives, and compromised statistical power due to the harsh constraints and assumptions breaking down.

I also need to add two more experiments to the list—extra benchmarks and domain-level analysis—then carefully construct the YAML configuration with realistic worst-tier predictions and supporting rationale for each.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "989483e3-9274-4ced-b3a8-ab23a8860a67",
  "isSidechain": false,
  "requestId": "req_011CbDXEz2PC8G33tSPFEQX9",
  "type": "assistant",
  "uuid": "f051f4cb-a947-49bf-988b-b09789851ccc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErMuXMdUozo6CnXY18cUNH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10633,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10633,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17749,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10633,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10633
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-20T08:46:38.906Z_

```yaml
tier: worst
narrative_guidance: >
  核心假设不成立——binary response 的信息量不足以检测现实水平的 SFT 污染。Reframe 为
  "Binary response 检测的信息论极限：IRT person-fit 何时足够、何时不够"。
  将 lz* 定位为极端污染的高置信度筛选器（Gemini-1.5 case 仍成立），
  将控制实验的负面结果本身作为贡献（严格量化 binary-only 检测的信息论下界），
  用 information-theoretic framing 构建 detection frontier 的完整图景。
  EMNLP 仍可投——负面结果 + 理论分析 + frontier 框架对评估方法论社区有价值。

imagined_experiments:
  - name: "Two-Sided Detection Framework"
    plan_id: "exp-two-sided"
    description: >
      实现 |lz*| > threshold 双侧检测，用 Phase B 数据验证，包括 bootstrap CI 和 FDR 控制。
    expected_results:
      gemini15_mmlu_lz_star: 34.75
      gemini15_mmlu_two_sided_p: 1.0e-12
      gemini15_gsm8k_lz_star: -15.71
      gemini15_humaneval_lz_star: -12.37
      positive_tail_flagged_models: 1
      negative_tail_flagged_models: 2
      total_flagged_at_fdr_05: 3
      bootstrap_ci_width_median: 1.8
      false_discovery_proportion_estimate: 0.0
      two_sided_power_gain_over_one_sided_pct: 8.2
    result_rationale: >
      双侧框架本身在技术上是正确的，Gemini-1.5 的极端 case（lz*=+34.75）仍然被高置信度检出。
      但 worst 档的核心问题不在双侧框架——而在于除了 Gemini-1.5 这种 100% 全量泄漏的极端
      case 外，几乎没有其他模型被 flag。12 个模型中仅 3 个被检出（Gemini-1.5 正侧 +
      2 个负侧的已知异常），说明双侧框架扩展了检测范围但并未带来实质性的新发现。
      Power gain 仅 ~8%，因为正侧检测只在 100% 污染时才产生显著信号。
      Bootstrap CI 较宽（median ~1.8），反映 12 模型的小样本不确定性。
    tables:
      - name: "Table 2: Two-Sided Detection Results on PSN-IRT 12 Models"
        columns: ["model", "benchmark", "accuracy", "theta", "lz_star", "tail", "p_value", "flagged"]
        key_rows:
          - ["Gemini-1.5-Pro", "MMLU", 1.000, 0.78, 34.75, "positive", "<1e-12", "yes"]
          - ["Gemini-1.5-Pro", "GSM8K", 0.924, 2.31, -15.71, "negative", "<1e-10", "yes"]
          - ["Gemini-1.5-Pro", "HumanEval", 0.890, 1.87, -12.37, "negative", "<1e-8", "yes"]
          - ["GPT-4o", "MMLU", 0.887, 3.12, -1.23, "—", 0.109, "no"]
          - ["Claude-3.5-Sonnet", "MMLU", 0.882, 2.98, -0.87, "—", 0.192, "no"]
    figures_description:
      - "Fig 2: lz* 双侧分布图——12 模型 × 5 benchmarks 的 lz* 散点，横轴 theta，纵轴 lz*。双侧阈值线（alpha=0.05 FDR-corrected）标注。仅 Gemini-1.5 的 3 个点落在阈值外。其余模型密集分布在 |lz*| < 2 区域。"
    analysis: >
      双侧框架在方法论上是完善的，Gemini-1.5 的检出是 robust 的。但 worst 档下，
      这本质上是一个"只抓到一条大鱼"的结果——框架的 incremental value 有限。
      需要在 paper 中将此定位为"极端污染的 zero-cost 筛选器"，
      而非通用检测方案。FDR 控制在仅 3 个 flagged 的情况下比较 trivial。

  - name: "Extended Simulation (60-100% Contamination)"
    plan_id: "exp-extended-sim"
    description: >
      扩展 Phase A 模拟至 60%/75%/90%/100% contamination levels，修复 100% NaN，精确刻画 inverted-U 拐点。
    expected_results:
      inverted_u_inflection_mmlu: 0.35
      inverted_u_inflection_hellaswag: 0.40
      inverted_u_inflection_gsm8k: 0.45
      inverted_u_inflection_arc_c: 0.50
      inverted_u_inflection_humaneval: 0.50
      lz_star_at_100pct_mmlu: 28.5
      lz_star_at_100pct_hellaswag: 18.2
      lz_star_at_100pct_gsm8k: 12.1
      power_at_60pct_mmlu: 0.92
      power_at_60pct_hellaswag: 0.61
      power_at_60pct_gsm8k: 0.43
      power_at_75pct_mmlu: 0.78
      power_at_75pct_hellaswag: 0.49
      power_at_75pct_gsm8k: 0.33
      power_at_90pct_mmlu: 0.55
      power_at_90pct_gsm8k: 0.21
      power_at_100pct_mmlu_positive_tail: 0.99
      nan_rate_at_100pct_before_fix: 0.85
      nan_rate_at_100pct_after_fix: 0.0
    result_rationale: >
      Inverted-U 拐点在 worst 档下出现在较低的污染水平（0.25-0.50），因为 SFT 泛化使得
      中等水平污染的 response pattern 与能力提升不可区分。具体机制：当 contamination 从 0%
      增加时，lz* 先变负（aberrant：在难题上异常正确），但 SFT 的泛化效应使模型在
      未污染题目上也表现更好，平滑了 aberrant pattern，导致 lz* 在 ~35-50% 处回归 0 附近。
      继续增加到 60%+ 后，over-consistency 信号开始主导（在简单题上也全对），lz* 转正。
      但在 60-90% 区间，正侧信号也被泛化平滑——模型"学会了"整体做题而非死记硬背，
      导致 power 在 75% 时反而低于 60%（inverted-U 的右半段斜率较缓）。
      只有 100% 时才产生压倒性信号（接近全对 + theta 远低于预期 → 极端 lz*）。
      修复 100% NaN 后确认：极端 case 的 lz* 值巨大（MMLU ~28.5），与 Gemini-1.5
      实测值（34.75）量级一致，validating 模拟的 external validity。
    tables:
      - name: "Table 3: Extended Simulation — Power and lz* by Contamination Level"
        columns: ["benchmark", "n_items", "contam_pct", "mean_lz_star", "power_negative", "power_positive", "power_two_sided"]
        key_rows:
          - ["MMLU", 14042, "60%", -3.2, 0.92, 0.01, 0.92]
          - ["MMLU", 14042, "75%", -1.1, 0.45, 0.33, 0.78]
          - ["MMLU", 14042, "90%", 2.8, 0.02, 0.53, 0.55]
          - ["MMLU", 14042, "100%", 28.5, 0.00, 0.99, 0.99]
          - ["GSM8K", 1319, "60%", -1.5, 0.43, 0.00, 0.43]
          - ["GSM8K", 1319, "75%", -0.4, 0.18, 0.15, 0.33]
          - ["GSM8K", 1319, "100%", 12.1, 0.00, 0.95, 0.95]
          - ["ARC-C", 1172, "60%", -0.8, 0.19, 0.00, 0.19]
          - ["ARC-C", 1172, "100%", 9.3, 0.00, 0.88, 0.88]
    figures_description:
      - "Fig 3: Inverted-U 曲线——每个 benchmark 一条线，横轴 contamination level (0-100%)，纵轴 mean lz*。清晰展示拐点位置随 n_items 减小而右移（MMLU ~35%, ARC-C ~50%）。5 条曲线全部呈现 inverted-U，但拐点后的正侧上升斜率在 worst 档下明显平缓（60-90% 区间 lz* 变化小），仅 100% 处跳跃式上升。"
      - "Fig 4: Detection power heatmap——横轴 contamination level，纵轴 benchmark (按 n_items 排序)。颜色编码 two-sided power。MMLU 行在 15% 和 100% 处亮色，中间 30-80% 暗淡。小 benchmark 行几乎全暗，仅 100% 处亮。视觉上呈"两端亮、中间暗"的 U 形 pattern。"
    analysis: >
      Extended simulation 精确量化了 worst 档的核心发现：binary-only 检测存在一个宽阔的
      "检测盲区"（~30-80% contamination），在此区间内 SFT 泛化使 lz* 信号被严重平滑。
      这构成了 paper 的关键负面结果之一。Inverted-U 的理论意义在于：它证明 contamination
      detection 不是单调的（更多污染≠更容易检测），这违反朴素直觉。
      100% 处的跳跃式信号说明 lz* 在极端 case 仍然有效——这与 Gemini-1.5 实测一致。
      Paper framing：将这个"盲区"quantify 为 binary-only detection 的信息论极限。

  - name: "Controlled Contamination Experiment"
    plan_id: "exp-ctrl-contam"
    description: >
      Qwen3.5-9B 和 Gemma-4-31B 上 QLoRA SFT 注入 0%/5%/10%/15%/25%/50% benchmark items，
      测量 person-fit 变化，建立 ground-truth contamination → lz* 映射。
    expected_results:
      qwen_0pct_lz_star_mmlu: -0.3
      qwen_5pct_lz_star_mmlu: -0.8
      qwen_10pct_lz_star_mmlu: -1.3
      qwen_15pct_lz_star_mmlu: -1.6
      qwen_25pct_lz_star_mmlu: -1.2
      qwen_50pct_lz_star_mmlu: 0.4
      qwen_5pct_lz_star_gsm8k: -0.4
      qwen_15pct_lz_star_gsm8k: -0.7
      qwen_25pct_lz_star_gsm8k: -0.5
      gemma_0pct_lz_star_mmlu: -0.1
      gemma_5pct_lz_star_mmlu: -0.5
      gemma_15pct_lz_star_mmlu: -1.1
      gemma_25pct_lz_star_mmlu: -0.8
      gemma_50pct_lz_star_mmlu: 0.7
      auroc_at_15pct_contam_mmlu: 0.63
      auroc_at_15pct_contam_gsm8k: 0.57
      auroc_at_15pct_contam_overall: 0.60
      min_detectable_contam_level_mmlu: 0.35
      min_detectable_contam_level_gsm8k: 0.55
      lz_effect_size_cohens_d_at_15pct: 0.38
      lz_effect_size_cohens_d_at_25pct: 0.25
      lz_effect_size_cohens_d_at_50pct: 0.55
      accuracy_gain_at_5pct_contam: 0.018
      accuracy_gain_at_15pct_contam: 0.042
      accuracy_gain_at_25pct_contam: 0.061
      contaminated_item_accuracy_at_15pct: 0.82
      uncontaminated_item_accuracy_at_15pct: 0.76
      contaminated_vs_uncontaminated_gap_at_15pct: 0.06
    result_rationale: >
      这是 worst 档最关键的实验——它直接验证了核心负面结论。SFT 泛化机制如下：
      (1) 当用 QLoRA 微调 5-25% benchmark items 时，模型不仅记住了这些 items，
      还学到了 benchmark 的 domain knowledge 和 answer pattern，导致在 uncontaminated items
      上也获得 accuracy gain（~1.8-6.1%）。(2) 这种泛化使得 contaminated 与 uncontaminated
      items 之间的 accuracy gap 很小（仅 ~6% at 15%），远不足以产生强 aberrant pattern。
      (3) 从 lz* 角度看，15% 污染的 lz* 约 -1.6（Qwen/MMLU），刚好在 significant threshold
      (-1.96) 边缘，单次实验难以稳定检出。Effect size (Cohen's d=0.38) 属于 small-to-medium，
      AUROC 仅 0.63——几乎与 random 相当。(4) 更糟的是，25% 污染时 lz* 反而回弹（inverted-U），
      因为泛化效应在此水平开始主导（模型 overall 能力提升 ~6%，pattern 更像高能力而非 aberrant）。
      (5) Gemma-4-31B 的信号略弱于 Qwen3.5-9B，可能因为更大模型的泛化能力更强。
      两个模型的结果一致性（correlation ~0.85）说明这不是模型特异性现象。
    tables:
      - name: "Table 4: Controlled Contamination — lz* by Model × Level × Benchmark"
        columns: ["model", "contam_pct", "benchmark", "accuracy", "delta_acc", "lz_star", "lz_p_value", "flagged_two_sided"]
        key_rows:
          - ["Qwen3.5-9B", "0%", "MMLU", 0.742, 0.000, -0.3, 0.382, "no"]
          - ["Qwen3.5-9B", "5%", "MMLU", 0.760, 0.018, -0.8, 0.212, "no"]
          - ["Qwen3.5-9B", "10%", "MMLU", 0.775, 0.033, -1.3, 0.097, "no"]
          - ["Qwen3.5-9B", "15%", "MMLU", 0.784, 0.042, -1.6, 0.055, "no"]
          - ["Qwen3.5-9B", "25%", "MMLU", 0.803, 0.061, -1.2, 0.115, "no"]
          - ["Qwen3.5-9B", "50%", "MMLU", 0.851, 0.109, 0.4, 0.345, "no"]
          - ["Gemma-4-31B", "0%", "MMLU", 0.801, 0.000, -0.1, 0.460, "no"]
          - ["Gemma-4-31B", "15%", "MMLU", 0.838, 0.037, -1.1, 0.136, "no"]
          - ["Gemma-4-31B", "50%", "MMLU", 0.892, 0.091, 0.7, 0.242, "no"]
      - name: "Table 5: Detection Performance — AUROC at Each Contamination Level"
        columns: ["benchmark", "contam_level", "auroc", "cohens_d", "sensitivity_at_fpr_05"]
        key_rows:
          - ["MMLU", "5%", 0.55, 0.18, 0.08]
          - ["MMLU", "10%", 0.59, 0.29, 0.14]
          - ["MMLU", "15%", 0.63, 0.38, 0.19]
          - ["MMLU", "25%", 0.58, 0.25, 0.12]
          - ["MMLU", "50%", 0.60, 0.55, 0.22]
          - ["GSM8K", "15%", 0.57, 0.22, 0.10]
          - ["GSM8K", "25%", 0.55, 0.17, 0.08]
    figures_description:
      - "Fig 5: Ground-truth contamination → lz* 映射曲线——2 个模型 × 5 benchmarks，每条线一个 model-benchmark pair。横轴 contamination level，纵轴 lz*。所有曲线呈浅 inverted-U，峰值 |lz*| 不超过 2.0。灰色水平带标注 significance zone (|lz*| > 1.96)。几乎没有点进入 significance zone，除了 Qwen-MMLU-15% 勉强触及边缘。"
      - "Fig 6: ROC 曲线——每个 contamination level 一条 ROC curve，MMLU 上。所有曲线紧贴对角线（AUC 0.55-0.63），与 random classifier 视觉上差异甚小。与 simulation 的 power=0.979 形成鲜明对比——annotation 标注 'simulation assumes verbatim memorization; real SFT generalizes'。"
      - "Fig 7: Contaminated vs uncontaminated item accuracy gap——bar chart，每个 contamination level 一组 bar。Gap 从 5% contam 的 ~3% 缓慢增长到 50% contam 的 ~12%。对比虚线标注 'gap needed for lz* significance at n=14042'（约 15%），说明实际 gap 始终低于检测所需阈值。"
    analysis: >
      控制实验产出了本文最核心的负面结果：在现实的 QLoRA SFT 污染条件下，lz* 在 5-25%
      contamination 范围内几乎不可检测（AUROC 0.55-0.63）。根本原因是 SFT 泛化——模型
      不是死记硬背 benchmark items，而是从中学到了 transferable knowledge，导致 response
      pattern 更像"能力提升"而非"作弊"。这直接挑战了 simulation 的核心假设（contaminated items
      被 100% 正确回答而 uncontaminated items 不变）。在 paper 中，这个结果需要被
      frame 为"严格量化了 binary-only detection 的信息论下界"——我们首次用 ground-truth
      实验证明了 SFT 泛化是 binary response 检测的根本瓶颈，而非方法本身的缺陷。
      Worst 档的 reframe 关键：simulation 代表的是 verbatim memorization scenario（对应
      intentional leaderboard gaming 的极端形式），而 QLoRA SFT 代表的是 realistic SFT
      contamination——两者之间的 gap 就是 binary-only detection 的信息论代价。

  - name: "Power-Theory Derivation"
    plan_id: "exp-power-theory"
    description: >
      推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式），验证理论曲线与模拟的拟合，将 inverted-U 升级为理论命题。
    expected_results:
      theory_r_squared_vs_simulation: 0.62
      theory_r_squared_vs_ctrl_contam: 0.38
      predicted_power_mmlu_at_15pct: 0.95
      actual_power_ctrl_at_15pct: 0.19
      theory_simulation_gap: 0.76
      snijders_variance_formula_valid_under_4pl: false
      d_parameter_bias_magnitude: 0.15
      corrected_theory_r_squared: 0.71
      power_formula: "P(n, c) ≈ Φ(√n · δ(c) / σ_lz - z_α)"
      delta_c_at_15pct_verbatim: 0.035
      delta_c_at_15pct_sft: 0.008
      information_gap_ratio: 4.4
      theoretical_min_n_for_80pct_power_at_15pct_sft: 58000
      theoretical_min_n_for_80pct_power_at_15pct_verbatim: 3200
    result_rationale: >
      Worst 档下 power theory 的核心发现是 4PL 的 d 参数引入了不可忽略的 bias。
      Snijders (2001) 的 lz* 方差公式假设 3PL 模型——标准误 Var(lz*) 的解析表达式
      依赖于 item parameters (a, b, c)，不包含 upper asymptote d。当 d < 1 时，
      high-ability examinees 的 expected score ceiling 被压低，lz* 的 null distribution
      产生 systematic shift，导致 theory 预测的 power 偏高。具体表现：
      (1) 理论曲线与 simulation 的 R² 仅 0.62（因为 simulation 用了 4PL 而理论假设 3PL）。
      经 d-parameter correction（用 bootstrap 估计 bias）后 R² 提升到 0.71，但仍非完美。
      (2) 更重要的是，理论预测与控制实验的 R² 仅 0.38——因为理论（即使 corrected）
      仍假设 verbatim memorization，而控制实验是 SFT（泛化效应 theory 无法建模）。
      (3) Information gap ratio = 4.4 意味着 SFT 污染的 per-item 信息量仅为 verbatim 的 ~23%。
      要在 SFT 条件下达到 80% power，需要 ~58K items——远超现有任何 benchmark。
      这个结果为 "binary-only detection 的信息论极限" 提供了理论基础。
    tables:
      - name: "Table 6: Theoretical vs Empirical Power Comparison"
        columns: ["benchmark", "n_items", "contam_15pct_theory_power", "contam_15pct_sim_power", "contam_15pct_ctrl_power", "theory_sim_gap", "theory_ctrl_gap"]
        key_rows:
          - ["MMLU", 14042, 0.95, 0.979, 0.19, -0.03, 0.76]
          - ["HellaSwag", 10042, 0.88, 0.733, "—", 0.15, "—"]
          - ["GSM8K", 1319, 0.52, 0.578, 0.10, -0.06, 0.42]
          - ["ARC-C", 1172, 0.45, 0.129, "—", 0.32, "—"]
          - ["HumanEval", 164, 0.12, 0.243, "—", -0.12, "—"]
      - name: "Table 7: Minimum n_items for 80% Power — Verbatim vs SFT"
        columns: ["contam_level", "min_n_verbatim", "min_n_sft", "ratio"]
        key_rows:
          - ["5%", 18000, ">100K", ">5.6"]
          - ["10%", 6500, 85000, 13.1]
          - ["15%", 3200, 58000, 18.1]
          - ["25%", 1800, 32000, 17.8]
          - ["50%", 900, 12000, 13.3]
    figures_description:
      - "Fig 8: Power 理论曲线 vs 实测——三条曲线叠加：(a) Snijders-3PL 理论（虚线），(b) 4PL-corrected 理论（实线），(c) 模拟实测（圆点）。横轴 n_items (log scale)，纵轴 power。4PL correction 改善了 fit 但 ARC-C 仍偏差大（d 参数效应最强的小 benchmark）。"
      - "Fig 9: Information gap 图——双 Y 轴：左轴 per-item signal strength δ(c)，右轴 required n for 80% power。两条线（verbatim vs SFT）显示 SFT 下所需 n 比 verbatim 高 4-18 倍。标注现有 benchmark 的 n_items 位置，说明除 MMLU 外均落在 SFT-required n 以下。"
    analysis: >
      Power theory 在 worst 档下产出了两个层次的发现：(1) 技术层面——4PL 的 d 参数
      确实引入 bias（~0.15 magnitude），Snijders 方差公式的理论保证在 4PL 下部分失效，
      但 corrected 后仍可用（R²=0.71）。(2) 更深层——即使理论完美，它也只能预测
      verbatim 场景的 power。SFT 泛化创造了一个理论无法 close 的 gap：per-item 信号
      从 δ=0.035 降到 δ=0.008。这个 gap 应被 frame 为 paper 的核心理论贡献——
      "binary response 信息论极限的定量刻画"。

  - name: "Leaderboard Audit"
    plan_id: "exp-leaderboard-audit"
    description: >
      Open LLM Leaderboard v1 大规模扫描：获取 per-item response logs，计算 person-fit，绘制污染率趋势。
    expected_results:
      per_item_logs_available: false
      models_with_inference_run: 12
      models_from_psn_irt_reuse: 12
      total_models_scanned: 12
      additional_models_from_self_inference: 0
      gpu_budget_exceeded: true
      flagged_models_positive_tail: 1
      flagged_models_negative_tail: 2
      flagged_rate: 0.0
      leaderboard_coverage_pct: 0.16
      temporal_trend_computable: false
    result_rationale: >
      Worst 档下 leaderboard audit 面临的致命瓶颈是数据获取。HuggingFace Open LLM
      Leaderboard v1 不公开 per-item response logs——仅公开 aggregate scores。
      要获取 per-item binary responses，必须自行对每个模型跑推理。以 MMLU 14K items 为例，
      单个模型需要 ~2-4 GPU-hours（取决于模型大小），7K+ 模型需要 ~14K-28K GPU-hours，
      远超 20 GPU-hours 预算。因此实际可用数据仅限于 PSN-IRT 已有的 12 个模型。
      在这 12 个模型中，flagged rate = 3/12（都是 Gemini-1.5 的不同 benchmark），
      去重后 flagged model rate = 1/12 ≈ 8.3%，但如果只看 MMLU 则为 1/12。
      如果按"新发现"算（排除已知的 Gemini-1.5），flagged rate = 0%。
      无法绘制时间趋势（12 模型时间分布太稀疏）。
      这个结果需要在 paper 中诚实报告为 scope limitation，但同时指出 IRT-FIT 的
      unique capability：它是唯一能在 per-item logs 可用时进行 retrospective audit 的方法。
    tables:
      - name: "Table 8: Leaderboard Audit Summary"
        columns: ["benchmark", "models_scanned", "flagged_positive", "flagged_negative", "flagged_rate"]
        key_rows:
          - ["MMLU", 12, 1, 0, "8.3%"]
          - ["GSM8K", 12, 0, 1, "8.3%"]
          - ["HumanEval", 12, 0, 1, "8.3%"]
          - ["HellaSwag", 12, 0, 0, "0.0%"]
          - ["ARC-C", 12, 0, 0, "0.0%"]
    figures_description:
      - "Fig 10: Leaderboard audit 结果散点图——12 模型 × 5 benchmarks = 60 个点。横轴 accuracy，纵轴 lz*。Gemini-1.5 的 3 个点是明显 outlier，其余 57 个点密集分布在 |lz*| < 2 区域。注解标明 'Coverage: 12/7K+ models (0.16%) — limited by per-item data availability'。"
    analysis: >
      Leaderboard audit 在 worst 档下严重受限于数据可用性，从预期的 7K+ 模型
      缩减到仅 12 个已有模型。这使得 "leaderboard audit 是 IRT-FIT 的 unique
      capability" 这一论点从实际演示变成了 hypothetical argument。Paper 需要将此
      重新定位为 (1) proof-of-concept（12 模型演示了 pipeline 的可行性），(2) call-to-action
      （呼吁 leaderboard 公开 per-item logs 以 enable retrospective integrity audit）。
      Flagged rate = 0%（排除已知 Gemini-1.5）与 worst 档预期一致——如果 lz* 只能
      检测极端污染，那么 12 个主流模型中不太可能有另一个 Gemini-1.5 级别的 case。

  - name: "4PL vs 3PL Ablation"
    plan_id: "exp-4pl-ablation"
    description: >
      比较 4PL 与 3PL(d=1) 参数化下的检测灵敏度差异，量化 d 参数对 false alarm 和 detection power 的影响。
    expected_results:
      mean_d_parameter_across_items: 0.92
      pct_items_with_d_below_0_95: 0.38
      type1_error_3pl_at_alpha_05: 0.073
      type1_error_4pl_at_alpha_05: 0.052
      type1_inflation_ratio: 1.40
      power_3pl_at_15pct_mmlu: 0.985
      power_4pl_at_15pct_mmlu: 0.979
      power_difference: -0.006
      false_alarm_difference: 0.021
      net_detection_advantage_4pl: "marginal"
      lz_star_shift_mean_3pl_vs_4pl: -0.28
      gemini15_lz_star_3pl: 31.2
      gemini15_lz_star_4pl: 34.75
    result_rationale: >
      4PL 与 3PL 的核心差异在 d 参数（upper asymptote / feasibility parameter）。
      当 d < 1 时，即使 ability 极高的 examinee 也有一定概率答错（"careless error"
      或 item 本身的 ceiling effect）。在 PSN-IRT 校准中，~38% 的 items 有 d < 0.95，
      说明 d 参数确实有实质意义。3PL(d=1) 相当于假设所有 items 都可以被完美回答——
      这导致 high-ability models 的 expected score 被高估，lz* 产生 systematic
      negative shift（~-0.28），进而 inflate Type-I error（从 0.052 到 0.073，inflation
      ratio 1.40）。Power 差异很小（-0.006），因为 contamination 的信号远大于 d-induced bias。
      但在 worst 档的语境下，Type-I error inflation 是重要发现——它说明 lz* 的理论保证
      在 4PL 下确实部分失效（Snijders 2001 假设 3PL），需要 4PL-specific correction。
      Gemini-1.5 的 lz* 在 3PL 下反而更低（31.2 vs 34.75），因为 d<1 的 items 在
      4PL 下降低了 expected score，使 over-consistency 信号更强。
    tables:
      - name: "Table 9: 4PL vs 3PL(d=1) Detection Comparison"
        columns: ["metric", "4PL", "3PL(d=1)", "difference", "interpretation"]
        key_rows:
          - ["Type-I error (α=0.05)", 0.052, 0.073, "+0.021", "3PL inflates false alarms"]
          - ["Power@15% MMLU", 0.979, 0.985, "+0.006", "negligible"]
          - ["Power@15% GSM8K", 0.578, 0.612, "+0.034", "small gain, offset by Type-I inflation"]
          - ["Gemini-1.5 lz* MMLU", 34.75, 31.2, "-3.55", "4PL gives stronger over-consistency signal"]
          - ["Mean lz* shift (null)", 0.00, -0.28, "-0.28", "systematic bias under 3PL"]
    figures_description:
      - "Fig 11: Null distribution 对比——4PL 下 lz* 的 null 分布（蓝色直方图）vs 3PL 下（橙色直方图）。3PL 分布明显左移 ~0.28，尾部超过 -1.96 的面积更大（visual Type-I inflation）。叠加标准正态参考线。"
    analysis: >
      4PL ablation 在 worst 档下产出了一个 technically sound 但影响有限的结果：
      d 参数引入的 bias 是真实的（Type-I inflation 40%），但在 detection power 层面
      差异甚小。Paper 贡献定位：(1) 技术上证明了使用 4PL 参数的必要性，(2) 为 lz*
      在 non-standard IRT 模型下的 calibration 提供了实证基础。但这不是一个改变
      paper narrative 的结果——它更多是一个 methodological detail。

  - name: "Baseline Comparison (ConStat, Min-K%++)"
    plan_id: "exp-baseline-comparison"
    description: >
      在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs Min-K%++ 的 AUROC/Type-I error。
    expected_results:
      irt_fit_auroc_at_15pct: 0.63
      constat_auroc_at_15pct: 0.78
      minkpp_auroc_at_15pct: 0.74
      irt_fit_auroc_at_25pct: 0.58
      constat_auroc_at_25pct: 0.82
      minkpp_auroc_at_25pct: 0.77
      irt_fit_auroc_at_50pct: 0.60
      constat_auroc_at_50pct: 0.88
      minkpp_auroc_at_50pct: 0.83
      irt_fit_type1_error: 0.052
      constat_type1_error: 0.048
      minkpp_type1_error: 0.055
      irt_fit_information_access: "binary responses only"
      constat_information_access: "binary responses + rephrased re-test"
      minkpp_information_access: "token probabilities"
      auroc_advantage_vs_constat_at_15pct: -0.15
      auroc_advantage_vs_minkpp_at_15pct: -0.11
    result_rationale: >
      Worst 档下 IRT-FIT 在 AUROC 上显著落后于两个 baseline，这是预期的——因为
      baselines 使用了更多信息。ConStat 通过 rephrased re-test 获得了 SFT 泛化无法
      平滑的信号（rephrase 后的 accuracy drop 直接反映 verbatim dependence），
      AUROC 0.78-0.88。Min-K%++ 通过 token probabilities 获得了比 binary response
      丰富得多的 per-item 信息，AUROC 0.74-0.83。IRT-FIT 仅 0.58-0.63——这不是
      方法的失败，而是 information access level 的直接后果。论文的 key framing：
      IRT-FIT 在 detection frontier 的最低信息点运作，AUROC 差距精确量化了
      "从 binary 到 rephrased re-test" 和 "从 binary 到 token probs" 的信息增益。
      这构建了 detection frontier 的完整图景：more information → more detection power，
      但 IRT-FIT 是唯一 zero-cost（无需 model access）的方法。
      值得注意的是 IRT-FIT 在 25% 处 AUROC 反而低于 15%（inverted-U 效应），
      而 baselines 单调递增——这进一步说明 binary-only 检测的 fundamental limitation。
    tables:
      - name: "Table 10: Detection Method Comparison — AUROC"
        columns: ["method", "info_access", "auroc_5pct", "auroc_15pct", "auroc_25pct", "auroc_50pct"]
        key_rows:
          - ["IRT-FIT (lz*)", "binary only", 0.55, 0.63, 0.58, 0.60]
          - ["ConStat", "binary + rephrase", 0.62, 0.78, 0.82, 0.88]
          - ["Min-K%++", "token probs", 0.59, 0.74, 0.77, 0.83]
          - ["Random", "—", 0.50, 0.50, 0.50, 0.50]
      - name: "Table 11: Detection Frontier Summary"
        columns: ["info_level", "method", "cost", "access_needed", "auroc_range", "unique_capability"]
        key_rows:
          - ["L0: binary", "IRT-FIT", "zero", "response pattern only", "0.55-0.63", "retrospective leaderboard audit"]
          - ["L1: rephrase", "ConStat", "low", "live model + rephrase set", "0.62-0.88", "SFT-robust detection"]
          - ["L2: token probs", "Min-K%++", "medium", "API with logprobs", "0.59-0.83", "fine-grained per-item signal"]
          - ["L3: weights", "probing", "high", "full model weights", "—", "direct memorization detection"]
    figures_description:
      - "Fig 12: Detection frontier 图——横轴 information access level (L0-L3)，纵轴 AUROC at 15% contamination。每个方法一个点，连线显示 AUROC 随信息量递增的 monotonic improvement。IRT-FIT 在 L0 位置，是 frontier 的左端点。Caption 强调：the gap between L0 and L1 quantifies the information cost of SFT generalization resistance."
      - "Fig 13: AUROC vs contamination level——三条曲线（IRT-FIT, ConStat, Min-K%++）。IRT-FIT 呈 inverted-U（25% 处凹陷），baselines 单调递增。Annotate the divergence point as 'SFT generalization boundary'."
    analysis: >
      Baseline comparison 是 worst 档叙事的 linchpin——它将 IRT-FIT 的"失败"转化为
      detection frontier 的定量刻画。AUROC 差距（0.11-0.15 vs ConStat）不是
      IRT-FIT 的缺陷，而是 binary-only information 的代价。这个结果直接支撑
      paper 的 reframed headline："Binary response 检测的信息论极限"。
      Detection frontier 图（Fig 12）应成为 paper 的核心 figure 之一——它将所有
      现有方法统一到一个框架下，IRT-FIT 的贡献是定义了这个 frontier 的左边界。

  - name: "Multiscale lzm Statistic"
    plan_id: "exp-multiscale-lzm"
    description: >
      实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合标准化 lz* 总分。在 12 模型上验证。
    expected_results:
      gemini15_lzm: 18.4
      gemini15_lzm_p: 1.0e-15
      second_highest_lzm: 2.1
      second_highest_lzm_p: 0.018
      lzm_flagged_at_fdr_05: 1
      lzm_vs_per_benchmark_concordance: 0.95
      lzm_incremental_detection_over_per_benchmark: 0
      lzm_power_at_15pct_sim: 0.82
      lzm_power_at_15pct_ctrl: 0.22
      cross_benchmark_correlation_lz_star: 0.67
    result_rationale: >
      Multiscale lzm 通过聚合跨 benchmark 的 lz* 信号来提高检测力。理论上，如果
      一个模型在多个 benchmark 上都有 mild aberrancy（单个不 significant），聚合后
      可能变 significant。但在 worst 档下：(1) Gemini-1.5 的 lzm 极其显著（18.4），
      但这完全是因为它在每个单独 benchmark 上就已经极端。(2) 第二高的 lzm 为 2.1
      （p=0.018），在 FDR correction 后不再 significant。(3) 在控制实验中，15% 污染的
      lzm power = 0.22——比单 benchmark（MMLU）的 power = 0.19 略有提升，但仍远不够。
      原因是 SFT 泛化在所有 benchmark 上都平滑了信号，聚合 noise 并不能 extract signal。
      Cross-benchmark lz* correlation = 0.67 说明 benchmarks 间有一定 dependence
      （可能因为相同的 SFT 过程影响所有 benchmark），这降低了聚合的 effective sample size。
    tables:
      - name: "Table 12: Multiscale lzm Results"
        columns: ["model", "mmlu_lz", "gsm8k_lz", "hellaswag_lz", "arc_c_lz", "humaneval_lz", "lzm", "lzm_p", "flagged"]
        key_rows:
          - ["Gemini-1.5-Pro", 34.75, -15.71, -2.34, -1.87, -12.37, 18.4, "<1e-15", "yes"]
          - ["GPT-4o", -1.23, -0.89, -0.45, -0.67, -1.12, 2.1, 0.018, "no"]
          - ["Claude-3.5-Sonnet", -0.87, -0.56, -0.33, -0.41, -0.78, 1.4, 0.081, "no"]
          - ["Llama-3.1-405B", -0.45, -0.23, -0.12, -0.55, -0.34, 0.8, 0.212, "no"]
    figures_description:
      - "Fig 14: lzm 分布图——12 模型的 lzm 值 bar chart。Gemini-1.5 远离其余模型（lzm=18.4 vs 次高 2.1）。虚线标注 significance threshold。只有 1 个模型超线。与 per-benchmark 结果完全一致——lzm 未带来新检出。"
    analysis: >
      Multiscale lzm 在 worst 档下没有实质性地改善检测——incremental detection = 0。
      当单个 benchmark 的信号已被 SFT 泛化平滑时，聚合多个弱信号并不能 rescue。
      这是因为 SFT 泛化是 systematic 的（影响所有 benchmark），而非 random noise。
      Paper 贡献：lzm 作为方法论扩展值得报告，但需要诚实说明它在 SFT 泛化条件下
      的局限——"多统计量融合"方向无法突破 binary-only 的信息瓶颈。

  - name: "Post-RL Hypothesis Test"
    plan_id: "exp-post-rl"
    description: >
      Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍可检测。
    expected_results:
      pre_rl_lz_star_at_15pct_mmlu: -1.6
      post_rl_lz_star_at_15pct_mmlu: -0.3
      pre_rl_lz_star_at_25pct_mmlu: -1.2
      post_rl_lz_star_at_25pct_mmlu: -0.1
      pre_rl_lz_star_at_50pct_mmlu: 0.4
      post_rl_lz_star_at_50pct_mmlu: 0.2
      power_retention_ratio_15pct: 0.08
      power_retention_ratio_25pct: 0.05
      power_retention_ratio_50pct: 0.12
      overall_power_retention_ratio: 0.08
      post_rl_accuracy_change: 0.025
      post_rl_pattern_correlation_with_pre_rl: 0.42
      rl_reward_shaping_effect: "strong — reshapes response pattern toward reward-optimal, not memorized"
    result_rationale: >
      Post-RL 实验在 worst 档下产出了最悲观的结果：GRPO 几乎完全破坏了 SFT 污染留下的
      person-fit 信号。机制分析：(1) SFT 污染在 response pattern 中留下的信号是
      "在特定 items 上异常正确"。(2) GRPO 的 reward shaping 重新优化了整个 response
      distribution——reward 基于 correctness 但也考虑 reasoning quality，这导致模型
      在一些 SFT-memorized items 上反而表现变差（reward signal 不一致时 RL 会 unlearn），
      同时在其他 items 上表现变好（能力真正提升）。(3) 结果是 RL 后的 response pattern
      与 RL 前的 correlation 仅 0.42——RL 本质上"洗掉了" SFT 的 item-specific 记忆。
      Power retention ratio = 0.08 意味着 SFT 阶段检测到的信号在 RL 后仅保留 8%。
      这与 Wang et al. (2025) 的 MIA 失效发现一致——RL 是 contamination 信号的
      universal destroyer，不仅对 MIA 如此，对 person-fit 同样如此。
      这个结果进一步收窄了 IRT-FIT 的适用范围：只对 SFT-only 模型有效，post-RL
      模型（即当前主流 RLHF/GRPO 模型）几乎不可检测。
    tables:
      - name: "Table 13: Post-RL Person-Fit Signal Degradation"
        columns: ["contam_level", "pre_rl_lz_star", "post_rl_lz_star", "retention_ratio", "pre_rl_flagged", "post_rl_flagged"]
        key_rows:
          - ["0% (control)", -0.3, -0.2, "—", "no", "no"]
          - ["5%", -0.8, -0.2, 0.10, "no", "no"]
          - ["10%", -1.3, -0.3, 0.09, "no", "no"]
          - ["15%", -1.6, -0.3, 0.08, "no", "no"]
          - ["25%", -1.2, -0.1, 0.05, "no", "no"]
          - ["50%", 0.4, 0.2, 0.12, "no", "no"]
    figures_description:
      - "Fig 15: Pre-RL vs Post-RL lz* 对比——paired bar chart，每个 contamination level 一对 bar（pre-RL 深色，post-RL 浅色）。所有 post-RL bar 都 collapse 到接近 0 的水平。Significance threshold 水平线标注——post-RL 后没有任何 bar 接近 threshold。"
      - "Fig 16: Response pattern correlation decay——scatter plot，横轴 pre-RL item-level accuracy，纵轴 post-RL item-level accuracy。点散布在对角线两侧（r=0.42），说明 RL 大幅重塑了 per-item response pattern。"
    analysis: >
      Post-RL 结果是 worst 档中最具政策意义的发现：当前主流 LLM 训练流程
      （pretrain → SFT → RL/RLHF/GRPO）中的 RL 阶段会系统性地破坏 person-fit 信号。
      这意味着 IRT-FIT 对 post-RL 模型几乎无效——而当前 leaderboard 上的主流模型
      几乎都是 post-RL 的。Paper 需要将此诚实报告为 scope limitation，同时指出：
      (1) 这是所有 binary-only 方法共有的问题，不是 IRT-FIT 特有的；
      (2) RL 破坏信号的机制本身是有趣的发现——reward shaping 是 contamination
      signal 的 universal eraser；(3) 仍有 SFT-only 部署场景（如 leaderboard v1
      早期模型、fine-tuned 模型、domain-specific 微调）where IRT-FIT 仍有价值。

  - name: "Extra Benchmarks (BBH, MATH)"
    plan_id: "exp-extra-benchmarks"
    description: >
      扩展 BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items 的 power gap。
    expected_results:
      bbh_4pl_params_available: false
      math_4pl_params_available: false
      self_calibration_needed: true
      self_calibration_gpu_hours_estimated: 30
      gpu_budget_remaining: 10
      bbh_calibrated: false
      math_calibrated: false
      experiment_completed: false
      fallback_option: "use 3PL approximation from public IRT calibrations"
      fallback_3pl_power_bbh_15pct_sim: 0.68
      fallback_3pl_power_math_15pct_sim: 0.58
    result_rationale: >
      Worst 档下 extra benchmarks 面临双重瓶颈：(1) PSN-IRT 不包含 BBH 和 MATH 的
      4PL 参数（PSN-IRT 仅覆盖 MMLU, HellaSwag, GSM8K, ARC-C, HumanEval），需要
      自行用 mirt/ltm 包校准 4PL，这需要大量模型的 per-item responses 作为校准数据，
      估计需要 30+ GPU-hours 跑推理；(2) 10 GPU-hours 的预算不足以完成校准。
      Fallback 方案是用 public IRT calibrations（如果存在）或 3PL 近似。但 3PL 近似
      引入前述 d-parameter bias，且缺乏与 PSN-IRT 的 comparability。
      如果勉强完成 3PL fallback，simulation power 在 BBH(6511 items) 约 0.68，
      MATH(5000 items) 约 0.58——符合 power ∝ n_items 的趋势，但由于用了 3PL，
      这些数字的 reliability 存疑。最可能的结果是这个实验无法按计划完成。
    tables:
      - name: "Table 14: Benchmark Coverage Gap Analysis"
        columns: ["benchmark", "n_items", "4pl_available", "calibration_cost_gpu_hrs", "status", "sim_power_15pct_3pl"]
        key_rows:
          - ["MMLU", 14042, "yes (PSN-IRT)", 0, "done", 0.979]
          - ["HellaSwag", 10042, "yes (PSN-IRT)", 0, "done", 0.733]
          - ["BBH", 6511, "no", 15, "infeasible", "~0.68 (3PL est.)"]
          - ["MATH", 5000, "no", 15, "infeasible", "~0.58 (3PL est.)"]
          - ["GSM8K", 1319, "yes (PSN-IRT)", 0, "done", 0.578]
          - ["ARC-C", 1172, "yes (PSN-IRT)", 0, "done", 0.129]
          - ["HumanEval", 164, "yes (PSN-IRT)", 0, "done", 0.243]
    figures_description:
      - "Fig (appendix): Power vs n_items 理论曲线 + 实测点。BBH 和 MATH 作为 'projected' 点用虚心圆标注，标明是 3PL 估计。5 个 PSN-IRT benchmark 作为实心点。理论曲线拟合 5 个实测点，BBH/MATH 的投影点大致落在曲线上。"
    analysis: >
      Extra benchmarks 在 worst 档下未能完成——这是 scope limitation 而非方法论缺陷。
      Paper 中应在 power-theory 分析中用理论曲线外推 BBH/MATH 的预期 power，
      而非实测。这实际上强化了 power-theory 的价值——如果理论推导准确，
      就不需要逐个 benchmark 实测。将此作为 future work 提出。

  - name: "Domain-Level Analysis (MMLU)"
    plan_id: "exp-domain-analysis"
    description: >
      按 MMLU subject category 分别计算 person-fit，识别 Gemini-1.5 的 MMLU 污染是全面还是集中在特定 domain。
    expected_results:
      n_mmlu_domains: 57
      n_domains_with_sufficient_items: 42
      gemini15_flagged_domains_positive: 38
      gemini15_flagged_domains_negative: 0
      gemini15_pct_domains_flagged: 0.90
      gemini15_domain_lz_star_min: 1.8
      gemini15_domain_lz_star_max: 8.5
      gemini15_domain_lz_star_mean: 4.2
      gemini15_domain_lz_star_std: 1.5
      other_models_domain_flagged_rate: 0.03
      domain_level_power_at_15pct_sim_mean: 0.35
      domain_level_power_at_15pct_sim_max: 0.62
      min_domain_items: 48
      max_domain_items: 612
      median_domain_items: 185
    result_rationale: >
      Domain-level 分析揭示 Gemini-1.5 的 MMLU 污染是系统性的、跨域的——90% 的 domains
      被 flagged（lz* > 0 正侧）。这与"全量训练集泄漏"假说一致（如果只泄漏了特定
      domain，应该看到 heterogeneous pattern）。Domain lz* 的变异（std=1.5）主要来自
      domain size 差异（更多 items → lz* 更极端）和 domain 难度差异。
      但对于其他 11 个模型，domain-level 分析几乎没有新发现（flagged rate 3%，
      与多重检验下的 random false positive rate 相当）。这是因为 domain-level 的
      n_items 很小（median 185），而 worst 档下 small n → low power。
      Power simulation 验证了这一点：domain-level 平均 power 仅 0.35（vs MMLU 整体 0.979）。
      Paper 贡献：(1) Gemini-1.5 的全域污染是 strong 的 case study evidence，
      (2) domain-level 的 low power 进一步说明了 n_items 是 binary-only detection 的
      binding constraint。
    tables:
      - name: "Table 15: Gemini-1.5 Domain-Level Person-Fit"
        columns: ["domain_category", "n_items", "accuracy", "lz_star", "flagged"]
        key_rows:
          - ["STEM (aggregate)", 4215, 1.000, 6.8, "yes"]
          - ["Humanities (aggregate)", 3892, 1.000, 6.1, "yes"]
          - ["Social Sciences (aggregate)", 3456, 1.000, 5.5, "yes"]
          - ["Other (aggregate)", 2479, 1.000, 4.9, "yes"]
          - ["Abstract Algebra", 100, 1.000, 2.1, "yes"]
          - ["Clinical Knowledge", 265, 1.000, 3.4, "yes"]
          - ["College Physics", 102, 1.000, 2.2, "yes"]
          - ["Moral Scenarios", 895, 1.000, 5.1, "yes"]
      - name: "Table 16: Domain-Level Detection Power (Simulation)"
        columns: ["domain_size_bin", "n_domains", "median_items", "mean_power_15pct", "pct_domains_above_80pct_power"]
        key_rows:
          - ["<100 items", 8, 72, 0.12, "0%"]
          - ["100-200 items", 18, 152, 0.28, "0%"]
          - ["200-400 items", 12, 285, 0.45, "8%"]
          - [">400 items", 4, 520, 0.62, "25%"]
    figures_description:
      - "Fig 17: Gemini-1.5 domain-level lz* heatmap——57 个 MMLU domains 按 category 分组（STEM / Humanities / Social Sciences / Other），颜色编码 lz* 值。几乎全图为正侧暖色（红/橙），少数 tiny domains 为中性灰色（insufficient items）。视觉上呈 'uniform contamination' pattern。"
      - "Fig 18: Domain-level power vs domain size——scatter plot，横轴 n_items per domain，纵轴 simulated power at 15%。清晰的 positive trend 但大部分 domains 在 power < 0.5 区域。标注：'median domain has 185 items → power = 0.28'。"
    analysis: >
      Domain analysis 在 worst 档下贡献了两个层面的发现：(1) 对 Gemini-1.5，
      全域污染 pattern 是 strong converging evidence——这不太可能是巧合或 domain-specific
      泛化，支持了"训练集全量泄漏"的结论。(2) 对一般检测场景，domain-level 的 low
      power 是又一个 negative result——small domain → small n → low power，即使
      总 benchmark 有 14K items，切分到 domain 后信号消失。这强化了核心 message：
      binary-only detection 需要 large, undivided item pools。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f051f4cb-a947-49bf-988b-b09789851ccc",
  "isSidechain": false,
  "requestId": "req_011CbDXEz2PC8G33tSPFEQX9",
  "type": "assistant",
  "uuid": "cb546737-a312-432c-846a-cab7dfdc2dc1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErMuXMdUozo6CnXY18cUNH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10633,
      "cache_read_input_tokens": 11841,
      "output_tokens": 17749,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10633,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 17749,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10633,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10633
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水平污染）不成立，需 reframe。 核心假设：['SFT 泛化使 partial contamination（5-25%）在 binary response…",
  "leafUuid": "cb546737-a312-432c-846a-cab7dfdc2dc1",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe IRT contamination detection as information-theoretic frontier",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水平污染）不成立，需 reframe。 核心假设：['SFT 泛化使 partial contamination（5-25%）在 binary response…",
  "leafUuid": "cb546737-a312-432c-846a-cab7dfdc2dc1",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe IRT contamination detection as information-theoretic frontier",
  "sessionId": "37473526-c257-40cf-9761-5869389db6d3"
}
```

---
