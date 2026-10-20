# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/bfdebcca-0257-4d54-98b1-a715797169ba.jsonl`
- **Structured JSON:** [`384d36fd1590191493f1.json`](../../sessions/38/384d36fd1590191493f1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T08:46:40.676Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T08:46:40.676Z",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水平污染）不成立，需 reframe。\n核心假设：['SFT 泛化使 partial contamination（5-25%）在 binary response 层面几乎不可区分于能力提升', 'lz* 仅在极端情况下显著：>50% verbatim 污染或 Gemini-1.5 式 100% 全量泄漏', 'Post-RL 完全破坏 person-fit 信号——RL 的 reward shaping 重塑 response pattern', 'Leaderboard per-item logs 不可获取，自跑推理 GPU 预算不足以覆盖有意义规模', 'Power 理论推导发现 4PL 的 d 参数引入不可忽略的 bias，lz* 理论保证在 4PL 下部分失效']\n关键指标范围：{'ctrl_contam_auroc_at_15pct': [0.55, 0.77], 'ctrl_contam_min_detectable_level': [0.3, 0.6], 'ctrl_contam_lz_effect_size_cohens_d': [0.2, 0.8], 'post_rl_power_retention_ratio': [0.05, 0.34], 'power_theory_r_squared': [0.5, 0.79], 'leaderboard_models_scanned': [12, 80], 'leaderboard_flagged_rate': [0.0, 0.03], 'baseline_auroc_advantage_vs_constat': [-0.15, -0.02], 'two_sided_inverted_u_inflection_contam_level': [0.25, 0.5], 'mmlu_power_at_5pct_contam': [0.05, 0.2]}\n叙事方向：核心假设不成立——binary response 的信息量不足以检测现实水平的 SFT 污染。必须 reframe，但不降级 venue。 新 angle：\"IRT person-fit 作为 benchmark integrity 的必要条件检查（necessary but not sufficient）\"。 Reframe 逻辑：(1) 将 lz* 定位为\"极端污染的高置信度筛选器\"而非通用检测器——Gemini-1.5 的 lz*=+34.75 仍是强结果，说明极端 case 的检出是 zero-cost（无需 access）的；(2) 将控制实验的\"负面结果\"本身作为贡献—— \"我们严格量化了 binary response 检测的信息论下界，证明 SFT 泛化是 binary-only 检测的根本瓶颈\"； (3) 用 information-theoretic framing 构建 detection frontier 的完整图景——我们的负面结果 + 文献 正面结果共同刻画了\"信息量 vs 检测力\"的 Pareto 前沿。(4) 发展\"多统计量融合\"方向——lz* + outfit + infit 的联合检验是否能突破单统计量的信息瓶颈。Headline 变为：\"Binary response 检测的信息论极限： IRT person-fit 何时足够、何时不够\"。EMNLP 仍可投——负面结果 + 理论分析 + frontier 框架 对评估方法论社区同样有价值。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_personfit_contam\nfocus: 重点评估：(1) 双侧检测框架是否足够新颖作为独立贡献 (2) 仅 12 模型 + 5 benchmarks 是否 scope 太窄 (3) Gemini-1.5 case study 是否足够有说服力（无 ground truth）(4) 控制实验设计是否能回应 \"no ground truth\" 的审稿意见\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection)**:\nIRT person-fit statistics detect benchmark contamination at the minimal-information operating point on the detection frontier — requiring only binary (correct/incorrect) response patterns, without access to model logits, weights, or training data.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\n\n**Claim 3 (Empirical Prevalence)**:\nApplying IRT-FIT to publicly available LLM benchmark data reveals previously undocumented contamination patterns — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence, and cross-benchmark anomaly consistency across 12 models from PSN-IRT.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics (lz*, outfit, infit) — developed over decades for detecting exam cheating — we answer: \"What can be detected from binary response patterns alone?\" This is a foundational question, not just another detector. We show the method works (97.9% power on MMLU), characterize its limits (power ∝ n_items), and reveal its dual-regime signal structure (partial vs. full contamination).\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT detects benchmark contamination with 97.9% power on MMLU (14K items) and identifies Gemini-1.5's 100% MMLU accuracy as contamination (lz*=+34.75) — a signal invisible to existing detectors that require model internals.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Single-sided test misses full contamination\" | Two-sided detection framework is a core contribution. Gemini-1.5 case study demonstrates. | exp-two-sided |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n\n## Key Narrative Elements (from External Review)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\n4. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n\n## MVP Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed.\n- **Phase B (real data)**: Gemini-1.5 (student_id=3) MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark: GSM8K lz*=-15.71, HumanEval lz*=-12.37. All benchmarks SD >> 0.5.\n- **Key insight from MVP**: Two-sided detection is essential — full contamination produces lz* >> 0 (over-consistent), not lz* << 0 (aberrant).\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n- id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点位置。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  notes: CPU only. 修改 simulation.py 参数 + null_check.py 的 NaN 处理。\n- id: exp-ctrl-contam\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 控制实验：在 Qwen3.5-9B 和 Gemma-4-31B 上，用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50%\n    benchmark items，测量微调前后 person-fit 变化。建立 ground-truth contamination → lz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: 'Qwen3.5-9B: 1× RTX 5090 (~8GB). Gemma-4-31B: 1× RTX 5090 (~20GB). 2 模型 ×\n    6 levels × ~3-7 hrs = ~60-80 GPU-hrs.'\n- id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 纯理论推导 + 数值验证。CPU only.\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：获取 per-item response logs（如果 HuggingFace\n    公开了），对所有可用模型计算 person-fit。绘制 per-benchmark 污染率随时间趋势。\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: 主要瓶颈是数据获取。如果 per-item logs 不可用，需要自己跑推理（GPU 预算大幅增加）。先调研数据可用性。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: 与现有方法对比（ConStat, Min-K%++）：在控制实验的 ground-truth contaminated models\n    上，比较 IRT-FIT vs baselines 的 AUROC/Type-I error。\n  priority: P1\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: 需要 baseline 方法的实现。ConStat 需要 re-test，Min-K%++ 需要 token probabilities。\n- id: exp-multiscale-lzm\n  claim:\n  - 1\n  - 3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim:\n  - 2\n  - 3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T08:46:40.679Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T08:46:40.679Z",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T08:46:40.700Z_

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
  "promptId": "4f94833d-0fdb-4b5c-8f6e-4657347dc2f5",
  "type": "user",
  "uuid": "cb5f2151-3635-4c84-ac67-a1050fdceca9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T08:46:40.699Z_

```json
{
  "parentUuid": "cb5f2151-3635-4c84-ac67-a1050fdceca9",
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
  "uuid": "90ed21c5-10b0-4cb0-ac2c-be4510b90be2",
  "timestamp": "2026-05-20T08:46:40.699Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T08:46:40.699Z_

```json
{
  "parentUuid": "90ed21c5-10b0-4cb0-ac2c-be4510b90be2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e773233c-1ffd-4790-943b-919267e53ac4",
  "timestamp": "2026-05-20T08:46:40.699Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba",
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
  "leafUuid": "e773233c-1ffd-4790-943b-919267e53ac4",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Binary response contamination detection power theory",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba"
}
```

---

### Assistant

_source line 8 · 2026-05-20T08:47:04.182Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all planned experiments under the "worst" tier scenario. Let me carefully analyze each experiment and produce realistic predictions consistent with the worst-tier definition.

The worst tier means:
- SFT generalization severely smooths the signal
- lz* only detectable at near-total contamination or complete verbatim memorization
- Core hypothesis (binary data sufficient to detect realistic contamination) doesn't hold
- Need reframe

Key metric ranges for worst tier:
- ctrl_contam_auroc_at_15pct: [0.55, 0.77]


- ctrl_contam_min_detectable_level: [0.3, 0.6]
- ctrl_contam_lz_effect_size_cohens_d: [0.2, 0.8]
- post_rl_power_retention_ratio: [0.05, 0.34]
- power_theory_r_squared: [0.5, 0.79]
- leaderboard_models_scanned: [12, 80]
- leaderboard_flagged_rate: [0.0, 0.03]
- baseline_auroc_advantage_vs_constat: [-0.15, -0.02]

Now I'm laying out the expected value ranges across all the key metrics I'll be predicting for each experiment, establishing the bounds within which realistic worst-case results should fall. Looking at the remaining experiments, the controlled contamination setup is where things get tricky—it's the linchpin for validating whether the detection framework actually works in practice. For the two-sided approach, the early inflection point around 0.25-0.5 contamination creates a detection blind spot where the signal becomes ambiguous. The extended simulation confirms the inverted-U pattern but reveals weak power at moderate contamination levels, and while the 100% NaN handling works, it only produces strong signals at extreme contamination on large benchmarks.

The real limitation emerges in the controlled contamination experiment: SFT generalization makes 5-15% contamination nearly invisible with AUROC only reaching 0.55-0.77, pushing the minimum detectable threshold to 30-60%. Theory fits the simulation reasonably but the 4PL model's d parameter introduces calibration bias that the theory doesn't fully capture. When I look at the leaderboard audit, data availability severely limits which models can be scanned and almost none get flagged. The baseline comparison shows IRT-FIT underperforming because methods like ConStat and Min-K%++ leverage more information, and even multiscale aggregation can't overcome the fundamental constraint of working with single benchmarks.

RL training essentially erases the person-fit signal entirely, while BBH and MATH in the 1K-10K range demonstrate moderate detection power that confirms the gap. Gemini-1.5's contamination pattern looks uniform across MMLU domains, suggesting full memorization rather than selective leakage.

Now I'm assembling the full YAML output with detailed rationales for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e773233c-1ffd-4790-943b-919267e53ac4",
  "isSidechain": false,
  "requestId": "req_011CbDXersSJkY6ojRL15D3d",
  "type": "assistant",
  "uuid": "4f468f3d-cee8-4467-a6e5-c537726fe2b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsVdZC9N8vmT7bJGf7UzS2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 22474,
      "output_tokens": 18304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18304,
          "cache_read_input_tokens": 22474,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-20T08:52:12.345Z_

```yaml
tier: worst
narrative_guidance: >
  核心假设不成立——binary response 的信息量不足以检测现实水平的 SFT 污染。SFT 泛化将 partial contamination 的 item-level 信号平滑至与能力提升不可区分。
  lz* 仅在极端情况下有效（>50% verbatim 或 Gemini-1.5 式全量泄漏）。Reframe 为"信息论极限"论文：
  (1) lz* 作为极端污染的高置信度零成本筛选器；(2) 负面结果本身作为贡献——严格量化 binary-only 检测的信息论下界；
  (3) detection frontier 的完整图景——信息量 vs 检测力的 Pareto 前沿；(4) 多统计量融合是否能突破单统计量瓶颈。
  Headline: "Binary Response 检测的信息论极限：IRT Person-Fit 何时足够、何时不够"。EMNLP 仍可投——负面结果 + 理论分析 + frontier 框架。

imagined_experiments:
  - name: "双侧检测框架验证"
    plan_id: "exp-two-sided"
    description: >
      基于 Phase B personfit_matrix.csv，实现 |lz*| > threshold 双侧检测。
      Bootstrap CI + BH-FDR 控制。Gemini-1.5 case study 验证正侧检测。
    expected_results:
      gemini15_mmlu_lz_star: 34.75
      gemini15_mmlu_two_sided_p: 1.0e-12
      gemini15_gsm8k_lz_star: -15.71
      gemini15_humaneval_lz_star: -12.37
      positive_tail_flagged_models: 1
      negative_tail_flagged_models: 3
      total_flagged_after_bh_fdr_005: 2
      bootstrap_ci_coverage_95: 0.93
      two_sided_vs_one_sided_extra_detections: 1
      inverted_u_inflection_contam_level: 0.35
    result_rationale: >
      双侧框架在 Gemini-1.5 极端 case 上完美工作（lz*=+34.75 远超任何阈值），但新增检出仅 1 个模型——
      因为正侧检测要求 near-100% 污染才产生显著 over-consistency 信号。Phase B 12 模型中大多数 lz* 处于
      [-2, +2] 的"不可判定区间"。BH-FDR 校正后，原本 one-sided 已检出的 3 个负侧异常模型中有 1 个被修正为
      不显著（p=0.06 > 0.05 after correction）。实际净增检出有限。inverted-U 拐点在 ~35% contamination，
      意味着 35% 以下的 partial contamination 产生的 lz* < 0 信号与高能力模型的正常负偏重叠，35% 以上开始
      向正侧翻转但在 50% 之前信号仍弱。双侧框架理论上正确，但实际增益受限于 binary 信号的信息瓶颈。
    tables:
      - name: "Table 1: Two-Sided Detection Results (Phase B, 12 Models × 5 Benchmarks)"
        columns: [model, benchmark, accuracy, theta, lz_star, p_lower, p_upper, p_two_sided, flagged_bh_fdr]
        key_rows:
          - [Gemini-1.5-Pro, MMLU, 1.000, 0.78, +34.75, 1.000, "<1e-12", "<1e-12", "Yes (+)"]
          - [Gemini-1.5-Pro, GSM8K, 0.924, 1.32, -15.71, "<1e-12", 1.000, "<1e-12", "Yes (-)"]
          - [Gemini-1.5-Pro, HumanEval, 0.890, 1.18, -12.37, "<1e-12", 1.000, "<1e-12", "Yes (-)"]
          - [Model-X, MMLU, 0.871, 2.14, -2.87, 0.002, 0.998, 0.004, "No (p_adj=0.06)"]
          - [Model-Y, HellaSwag, 0.952, 2.68, -1.34, 0.090, 0.910, 0.180, "No"]
          - [Median-model, MMLU, 0.743, 1.05, -0.42, 0.337, 0.663, 0.674, "No"]
    figures_description:
      - "Fig 1a: lz* 分布直方图（12 models × 5 benchmarks = 60 data points），标注 N(0,1) 参考线和双侧 α=0.05 阈值。大部分点集中在 [-2, +2]，仅 Gemini-1.5 的 3 个点远离中心。"
      - "Fig 1b: Inverted-U 曲线示意（来自 Phase A 模拟），标注拐点位置 ~35%。x 轴 contamination level，y 轴 mean lz*，showing 从负到正的翻转。"
    analysis: >
      双侧框架在极端 case 上有效，但"不可判定区间"覆盖了大部分现实污染场景。
      60 个 model×benchmark 组合中仅 4 个 |lz*| > 3，其中 3 个来自同一模型（Gemini-1.5）。
      这暗示 binary response 的信号量不足以在非极端情况下区分污染与能力。

  - name: "扩展模拟：高污染级别与 inverted-U 精确刻画"
    plan_id: "exp-extended-sim"
    description: >
      在 Phase A 模拟基础上添加 60%/75%/90%/100% 污染级别，修复 100% boundary θ=4.0 的 NaN 处理，
      精确定位 inverted-U 拐点并量化各 benchmark 的 detection power curve。
    expected_results:
      mmlu_power_at_5pct_contam: 0.12
      mmlu_power_at_15pct_contam: 0.68
      mmlu_power_at_25pct_contam: 0.43
      mmlu_power_at_50pct_contam: 0.15
      mmlu_power_at_75pct_contam: 0.52
      mmlu_power_at_100pct_contam_positive_tail: 0.97
      hellaswag_power_at_15pct_contam: 0.41
      gsm8k_power_at_15pct_contam: 0.28
      arc_c_power_at_15pct_contam: 0.09
      humaneval_power_at_15pct_contam: 0.11
      inverted_u_inflection_mmlu: 0.32
      inverted_u_inflection_hellaswag: 0.38
      inverted_u_inflection_gsm8k: 0.41
      inverted_u_inflection_arc_c: 0.28
      inverted_u_inflection_humaneval: 0.30
      detection_gap_25_to_50pct: "power < 0.20 for all benchmarks"
      nan_fix_success: true
      boundary_theta_lz_star_at_100pct_mmlu: 28.4
    result_rationale: >
      扩展模拟揭示了 worst 档的核心困境：inverted-U 的拐点出现在 ~30-40% contamination（因 benchmark 而异），
      这意味着 15-50% 区间是一个"检测死区"——negative-side lz* 已经开始回归零（SFT 泛化使模型在未污染 items 上
      也表现更好，压低了 aberrance 信号），而 positive-side lz* 尚未积累足够的 over-consistency 信号。
      具体机制：SFT 在 15% items 上训练后，模型在相关 domain 的其他 items 上准确率也提升 3-8%（泛化效应），
      这使得 response pattern 的 aberrance 被稀释。Phase A 原始结果 mmlu@15%=97.9% 是在"无泛化"的
      理想模拟下得到的（直接翻转 response bit）；当模拟加入泛化噪声后，power 降至 ~68%。而真实 SFT 的泛化
      远强于模拟中的简单噪声模型，所以控制实验（exp-ctrl-contam）的结果会更差。
      100% contamination 修复后 lz*=+28.4（MMLU），power=97% 在正侧——这是唯一稳健的检测点。
      关键发现：存在一个 25-50% 的"power valley"，所有 benchmark 的 power 都低于 0.20，
      这正是现实中最可能出现的污染水平。
    tables:
      - name: "Table 2: Extended Power Matrix (Two-Sided, α=0.05)"
        columns: [benchmark, n_items, "0%", "5%", "10%", "15%", "25%", "50%", "60%", "75%", "90%", "100%"]
        rows:
          - [MMLU, 14042, 0.05, 0.12, 0.38, 0.68, 0.43, 0.15, 0.29, 0.52, 0.81, 0.97]
          - [HellaSwag, 10042, 0.05, 0.08, 0.22, 0.41, 0.27, 0.10, 0.19, 0.38, 0.64, 0.91]
          - [GSM8K, 1319, 0.05, 0.06, 0.14, 0.28, 0.18, 0.07, 0.12, 0.24, 0.43, 0.72]
          - [ARC-C, 1172, 0.05, 0.05, 0.07, 0.09, 0.07, 0.05, 0.07, 0.13, 0.28, 0.54]
          - [HumanEval, 164, 0.05, 0.05, 0.06, 0.11, 0.08, 0.05, 0.06, 0.09, 0.17, 0.31]
        notes: "Phase A 原始 mmlu@15%=97.9% 是 one-sided ideal simulation；此处为 two-sided + 泛化噪声模拟"
      - name: "Table 3: Inverted-U Inflection Points"
        columns: [benchmark, inflection_contam_level, lz_star_at_inflection, power_at_inflection]
        rows:
          - [MMLU, 0.32, -0.18, 0.08]
          - [HellaSwag, 0.38, -0.12, 0.06]
          - [GSM8K, 0.41, -0.09, 0.05]
          - [ARC-C, 0.28, -0.21, 0.06]
          - [HumanEval, 0.30, -0.15, 0.05]
    figures_description:
      - "Fig 2: Power curves for all 5 benchmarks (x=contamination level 0-100%, y=power)，展示 inverted-U 形状。每条曲线在 25-50% 区间出现明显 valley。MMLU 的 valley 最浅（因 n_items 最大），HumanEval 的 valley 最深。"
      - "Fig 3: Mean lz* as function of contamination level（5 benchmarks），直观展示从 negative 到 positive 的翻转。标注 zero-crossing（inflection）点。"
    analysis: >
      inverted-U 被精确刻画，但其含义对论文是负面的：现实中最常见的 partial contamination (5-25%) 恰好处于
      检测力最弱的区域。100% 的高 power 是一个 degenerate case（Gemini-1.5 式），
      而非方法的通用能力。Reframe 角度：这正是"binary response 信息论极限"的直接证据。

  - name: "控制实验：SFT 污染注入与 ground-truth 映射"
    plan_id: "exp-ctrl-contam"
    description: >
      在 Qwen3.5-9B 和 Gemma-4-31B 上，QLoRA SFT 注入 0%/5%/10%/15%/25%/50% MMLU items，
      测量微调前后的 person-fit 变化，建立 ground-truth contamination → lz* 映射。
    expected_results:
      # Qwen3.5-9B results
      qwen_baseline_mmlu_acc: 0.721
      qwen_baseline_lz_star: -0.34
      qwen_5pct_mmlu_acc: 0.748
      qwen_5pct_lz_star: -0.51
      qwen_5pct_delta_lz: -0.17
      qwen_10pct_mmlu_acc: 0.779
      qwen_10pct_lz_star: -0.83
      qwen_10pct_delta_lz: -0.49
      qwen_15pct_mmlu_acc: 0.812
      qwen_15pct_lz_star: -1.22
      qwen_15pct_delta_lz: -0.88
      qwen_25pct_mmlu_acc: 0.856
      qwen_25pct_lz_star: -1.08
      qwen_25pct_delta_lz: -0.74
      qwen_50pct_mmlu_acc: 0.923
      qwen_50pct_lz_star: 0.45
      qwen_50pct_delta_lz: 0.79
      # Gemma-4-31B results
      gemma_baseline_mmlu_acc: 0.803
      gemma_baseline_lz_star: -0.12
      gemma_5pct_lz_star: -0.29
      gemma_15pct_lz_star: -0.92
      gemma_25pct_lz_star: -0.71
      gemma_50pct_lz_star: 0.68
      # Detection metrics
      ctrl_contam_auroc_at_15pct: 0.63
      ctrl_contam_auroc_at_25pct: 0.58
      ctrl_contam_auroc_at_50pct: 0.71
      ctrl_contam_min_detectable_level: 0.45
      ctrl_contam_lz_effect_size_cohens_d_at_15pct: 0.38
      ctrl_contam_lz_effect_size_cohens_d_at_50pct: 0.72
      contaminated_items_acc_boost: 0.23
      non_contaminated_items_acc_boost_at_15pct: 0.06
      generalization_ratio_at_15pct: 0.26
      lz_star_significance_threshold_crossed_at: "50% (Qwen), 50% (Gemma)"
      type_i_error_at_alpha_005: 0.048
      two_model_agreement_rate: 0.83
    result_rationale: >
      这是 worst 档的核心实验。SFT 泛化效应严重削弱了 person-fit 信号：
      (1) 5% contamination: 模型在 5% 的 MMLU items 上训练后，overall accuracy 提升 2.7pp（Qwen），
      但关键是非污染 items 的 accuracy 也提升了 ~1.5pp（domain transfer），使得 response pattern 的
      aberrance 被大幅稀释。lz* 变化仅 -0.17，完全在正常波动范围内（Cohen's d ≈ 0.12）。
      (2) 15% contamination: accuracy 提升 9.1pp，其中非污染 items 贡献了 ~6pp 的泛化提升
      （generalization ratio = 0.26，即 26% 的 accuracy gain 来自泛化而非记忆）。
      lz* = -1.22，接近但未达 α=0.05 的 one-sided 阈值（-1.645）。这是因为 SFT 的泛化使得
      模型的 response pattern 看起来像"能力真的提升了"而非"记住了特定 items"。
      (3) 25% contamination: 出现 inverted-U 效应——lz* 从 -1.22 回弹到 -1.08。
      泛化效应更强（模型在更多 domain 上提升），进一步平滑了 aberrance 信号。
      (4) 50% contamination: lz* 翻转为正（+0.45），但仍不显著。模型在几乎所有 items 上都表现好，
      pattern 变得 over-consistent，但 binary response 的信息量不足以将 over-consistency
      与"truly high ability"区分开。AUROC@50% = 0.71，刚刚好于随机。
      (5) 两个模型的行为高度一致（agreement 83%），说明这不是模型特异性问题，而是 binary response 的根本限制。
      最小可检测级别在 ~45%（p < 0.05 first crossed），远高于论文原本假设的 15%。
      AUROC@15% = 0.63，仅略好于随机（0.50），这与 worst 档的指标范围 [0.55, 0.77] 一致。
    tables:
      - name: "Table 4: Controlled Contamination Results — Qwen3.5-9B on MMLU"
        columns: [contam_level, mmlu_acc, delta_acc, theta, lz_star, delta_lz, p_two_sided, contam_items_acc, clean_items_acc, generalization_ratio]
        rows:
          - ["0% (baseline)", 0.721, "—", 1.05, -0.34, "—", 0.734, "—", 0.721, "—"]
          - ["5%", 0.748, +0.027, 1.18, -0.51, -0.17, 0.610, 0.89, 0.736, 0.56]
          - ["10%", 0.779, +0.058, 1.34, -0.83, -0.49, 0.407, 0.93, 0.763, 0.28]
          - ["15%", 0.812, +0.091, 1.52, -1.22, -0.88, 0.222, 0.96, 0.787, 0.26]
          - ["25%", 0.856, +0.135, 1.78, -1.08, -0.74, 0.280, 0.97, 0.818, 0.31]
          - ["50%", 0.923, +0.202, 2.31, +0.45, +0.79, 0.653, 0.99, 0.877, 0.23]
      - name: "Table 5: Controlled Contamination Results — Gemma-4-31B on MMLU"
        columns: [contam_level, mmlu_acc, theta, lz_star, p_two_sided]
        rows:
          - ["0%", 0.803, 1.52, -0.12, 0.905]
          - ["5%", 0.824, 1.63, -0.29, 0.772]
          - ["10%", 0.849, 1.79, -0.64, 0.522]
          - ["15%", 0.873, 1.94, -0.92, 0.358]
          - ["25%", 0.904, 2.18, -0.71, 0.478]
          - ["50%", 0.951, 2.72, +0.68, 0.497]
      - name: "Table 6: Detection Performance Summary"
        columns: [metric, "5%", "10%", "15%", "25%", "50%"]
        rows:
          - [AUROC (2 models pooled), 0.52, 0.56, 0.63, 0.58, 0.71]
          - ["Cohen's d (|Δlz*|)", 0.12, 0.34, 0.61, 0.52, 0.72]
          - ["Power (α=0.05, two-sided)", 0.06, 0.11, 0.18, 0.14, 0.32]
    figures_description:
      - "Fig 4: lz* vs contamination level（两个模型，error bars from 3 random seeds each）。清晰展示 inverted-U：lz* 先下降（5-15%），然后回升穿过零（25-50%）。两个模型趋势一致。水平虚线标注 ±1.96 显著性阈值——在 worst 档下，没有任何 partial contamination level 的 lz* 穿过阈值。"
      - "Fig 5: Generalization ratio vs contamination level。展示 SFT 泛化效应：即使在 5% contamination 下，56% 的 accuracy gain 来自非污染 items 的泛化提升。这是 binary-only 检测失败的根本原因。"
      - "Fig 6: ROC curves at each contamination level（baseline vs contaminated 的二分类）。15% 的曲线几乎贴着对角线，50% 的曲线略有偏离但远不如理想检测器。"
    analysis: >
      控制实验提供了 worst 档最关键的证据：SFT 的泛化效应是 binary-only 检测的根本瓶颈。
      generalization ratio 在 23-56% 之间，意味着 SFT 污染的"信号"被泛化"噪声"严重稀释。
      从信息论角度：binary response 的每个 item 仅提供 1 bit 信息，而 SFT 泛化将
      contamination signal 分散到整个 response pattern 中，使得逐 item 的 aberrance 检测失效。
      这直接支持 reframe 叙事——binary response 存在信息论下界。

  - name: "Power 理论推导与数值验证"
    plan_id: "exp-power-theory"
    description: >
      基于 Snijders (2001) lz* 方差公式推导 power 与 n_items 的解析关系。
      验证理论曲线与扩展模拟结果的拟合度。量化 4PL d 参数的 bias 影响。
    expected_results:
      power_formula_derived: true
      theoretical_power_formula: "Power ≈ Φ(√(n·h(p_c)) - z_α) where h(p_c) = contamination info per item"
      theory_vs_sim_r_squared_3pl: 0.89
      theory_vs_sim_r_squared_4pl: 0.67
      d_parameter_bias_magnitude: 0.12
      d_parameter_bias_direction: "conservative (underestimates lz* variance)"
      theoretical_min_items_for_80pct_power_at_15pct_contam: 42000
      theoretical_min_items_for_80pct_power_at_50pct_contam: 8500
      information_per_item_binary: "1 bit"
      information_per_item_logits: "~8-12 bits"
      information_gap_ratio: "8-12x"
      snijders_variance_formula_holds_under_4pl: false
      variance_inflation_factor_4pl: 1.34
    result_rationale: >
      理论推导揭示了 4PL 模型下 lz* 的一个关键问题：Snijders (2001) 的 lz* 标准化假设 3PL 模型，
      其中 Var(lz*) → 1 as n → ∞。但 4PL 的 d 参数（upper asymptote < 1）引入了额外的方差项，
      使得 Var(lz*) ≈ 1.34 而非 1.0。这意味着 lz* 在 4PL 下被系统性地"膨胀"了，导致 null distribution
      比理论 N(0,1) 更宽，从而削弱了检测力（false alarm rate 在 nominal α=0.05 下实际约为 0.08）。
      理论曲线与 3PL 模拟拟合良好（R²=0.89），但与 4PL 模拟拟合度显著下降（R²=0.67），
      表明 4PL 的 d 参数引入了理论框架未捕捉的非线性效应。
      最震撼的结果：要在 15% contamination 下达到 80% power，需要 ~42000 items——
      目前没有任何主流 benchmark 达到这个规模（MMLU 最大也只有 14042）。
      而如果使用 logit-level 信息（~10 bits/item），所需 items 降至 ~4000，
      这直接量化了 binary vs logits 的信息差距，支撑了 detection frontier 叙事。
    tables:
      - name: "Table 7: Theoretical vs Simulated Power (4PL)"
        columns: [benchmark, n_items, "theory_power@15%", "sim_power@15%", residual]
        rows:
          - [MMLU, 14042, 0.74, 0.68, -0.06]
          - [HellaSwag, 10042, 0.58, 0.41, -0.17]
          - [GSM8K, 1319, 0.18, 0.28, +0.10]
          - [ARC-C, 1172, 0.15, 0.09, -0.06]
          - [HumanEval, 164, 0.06, 0.11, +0.05]
        notes: "R² = 0.67; systematic overestimation for medium benchmarks due to 4PL d-parameter bias"
      - name: "Table 8: Minimum Items for Target Power (Theoretical)"
        columns: [contam_level, target_power, min_items_binary, min_items_logits, ratio]
        rows:
          - ["5%", 0.80, ">100K", 12000, ">8x"]
          - ["10%", 0.80, 65000, 6500, "10x"]
          - ["15%", 0.80, 42000, 4200, "10x"]
          - ["25%", 0.80, "N/A (inverted-U valley)", 2800, "—"]
          - ["50%", 0.80, 8500, 950, "9x"]
    figures_description:
      - "Fig 7: Theoretical power surface (x=n_items, y=contamination level, z=power)。3D surface plot 展示 power landscape，清晰可见 inverted-U ridge 和 n_items 的 monotonic scaling。标注 80% power contour line——在 binary response 下，该 contour 仅覆盖 (n>42K, contam>15%) 和 (n>8.5K, contam=50-100%) 两个区域。"
      - "Fig 8: Theory vs Simulation scatter plot（每个点 = 一个 benchmark × contamination level 组合），3PL 和 4PL 分别标注。3PL 点紧贴 y=x 线，4PL 点系统性偏离。"
      - "Fig 9: Detection frontier diagram — information access level (x) vs detectable contamination level (y)。Binary response 在最左端，logits 在中间，weights 在最右端。标注各方法的位置。"
    analysis: >
      理论推导在 worst 档下反而是最有价值的贡献之一——它严格量化了"为什么 binary response 不够"。
      但 4PL 下 R²=0.67 表明理论的精确度有限，需要在论文中明确指出这是 approximate bound 而非 exact result。
      Detection frontier diagram 可以成为论文的 signature figure——即使自己的方法 power 不高，
      它为整个领域提供了思考框架。

  - name: "Open LLM Leaderboard 大规模扫描"
    plan_id: "exp-leaderboard-audit"
    description: >
      尝试获取 HuggingFace Open LLM Leaderboard v1 的 per-item response logs。
      对可用模型计算 person-fit，绘制污染率趋势。
    expected_results:
      per_item_logs_publicly_available: false
      hf_api_provides_aggregate_only: true
      alternative_data_source: "lm-evaluation-harness 自跑推理"
      models_with_existing_per_item_data: 12
      additional_models_self_run: 0
      total_leaderboard_models_scanned: 12
      flagged_models_bh_fdr_005: 1
      flagged_rate: 0.008
      gpu_budget_for_meaningful_scan: "400+ GPU-hours (infeasible)"
      fallback_strategy: "仅使用 PSN-IRT 已有 12 模型数据"
      gemini_15_remains_only_flagged: true
    result_rationale: >
      这是 worst 档中最受限的实验。HuggingFace Open LLM Leaderboard v1 不公开 per-item response logs——
      API 仅返回 per-benchmark aggregate scores。要获取 per-item 数据，必须自己用 lm-evaluation-harness
      跑推理，每个模型在 5 个 benchmarks 上需要 ~3-5 GPU-hours（取决于模型大小）。
      即使只跑 80 个模型（Leaderboard 上有 7000+），也需要 240-400 GPU-hours，远超 20hr 预算。
      最终只能使用 PSN-IRT 已有的 12 个模型数据（这本身就是 Phase B 的数据）。
      在这 12 个模型中，用双侧检测 + BH-FDR 校正后，仅 Gemini-1.5 被 flag（flagged rate = 1/12 ≈ 0.8%）。
      这个结果有两种解读：(1) 其他 11 个模型确实没有显著污染；(2) binary-only 检测的 power 太低，
      无法在 realistic contamination levels 下 flag 任何人。在 worst 档的 framing 下，解读 (2) 更可能。
      论文必须诚实承认 data availability 是核心瓶颈，并将"Leaderboard 审计"从 core contribution
      降级为"pilot study"或"future work with infrastructure support"。
    tables:
      - name: "Table 9: Leaderboard Audit Summary (12 Models, PSN-IRT Data)"
        columns: [model, mmlu_lz_star, hellaswag_lz_star, gsm8k_lz_star, arc_c_lz_star, humaneval_lz_star, n_benchmarks_flagged]
        rows:
          - [Gemini-1.5-Pro, +34.75, -1.24, -15.71, -0.89, -12.37, "3/5"]
          - [GPT-4o, -0.87, -0.42, -1.13, 0.23, -0.67, "0/5"]
          - [Claude-3.5-Sonnet, -0.34, 0.18, -0.78, -0.15, -0.91, "0/5"]
          - [Llama-3.1-405B, -1.12, -0.67, -0.45, -0.34, -0.23, "0/5"]
          - ["... (8 more)", "...", "...", "...", "...", "...", "0/5"]
        notes: "仅 PSN-IRT 已有数据；未能扩展至更多模型"
    figures_description:
      - "Fig 10: lz* heatmap (12 models × 5 benchmarks)。Gemini-1.5 的行明显异常（deep red/blue），其余模型的 lz* 集中在 [-1.5, +1.5] 灰色区域。"
    analysis: >
      Leaderboard audit 在 worst 档下从"核心差异化贡献"退化为"仅 12 模型的 pilot study"。
      这严重削弱了论文的实证贡献。但 Reframe 角度下，数据不可获取性本身强化了论点——
      "即使是最低信息需求的方法也因数据基础设施缺失而无法大规模部署"，
      这可以作为 community call-to-action（呼吁 Leaderboard 公开 per-item logs）。

  - name: "4PL vs 3PL(d=1) 检测灵敏度消融"
    plan_id: "exp-4pl-ablation"
    description: >
      固定 d=1（3PL 等价）重新计算 person-fit，比较 4PL 和 3PL 下的检测灵敏度差异。
      量化 d 参数对 false alarm rate 和 detection power 的影响。
    expected_results:
      n_items_with_d_significantly_below_1: 0.18
      mean_d_parameter_mmlu: 0.91
      mean_d_parameter_humaneval: 0.82
      three_pl_lz_star_variance_empirical: 1.02
      four_pl_lz_star_variance_empirical: 1.34
      false_alarm_rate_3pl_at_alpha_005: 0.052
      false_alarm_rate_4pl_at_alpha_005: 0.083
      power_at_15pct_contam_3pl_mmlu: 0.78
      power_at_15pct_contam_4pl_mmlu: 0.68
      power_difference_3pl_vs_4pl: +0.10
      gemini_lz_star_3pl: 31.2
      gemini_lz_star_4pl: 34.75
      detection_conclusion_changes: 0
      theoretical_lz_star_bias_4pl: -0.12
      recommended_correction: "variance inflation factor = 1.34"
    result_rationale: >
      4PL 的 d 参数（upper asymptote）对 lz* 有系统性影响：当 d < 1 时，高能力 respondent 的期望
      正确率被压低，使得实际 response pattern 相对于期望 pattern 的偏差被放大。这导致 lz* 的 null
      distribution 方差从理论值 1.0 膨胀到 ~1.34。具体后果：
      (1) False alarm rate 从 nominal 5% 升至 8.3%——在 worst 档下这本身就是问题，
      因为已经有限的检测力中一部分是虚假的。
      (2) 3PL 下 MMLU@15% power = 0.78，4PL 下降至 0.68——10pp 的差距。
      这解释了为什么 Phase A 的理想模拟（隐式假设 3PL 行为）给出了 97.9% 的高 power，
      而考虑 4PL 后 power 显著下降。
      (3) 对极端 case（Gemini-1.5）无实质影响——lz*=31.2 (3PL) vs 34.75 (4PL)，
      都远超阈值。4PL 的影响仅在边际 case 上重要。
      18% 的 MMLU items 的 d 显著低于 1（p<0.05），主要集中在 STEM 领域，
      这可能是因为 MCQ 的猜测上限效应（部分知识的考生达不到 100% 正确率）。
      建议：在论文中采用 variance-corrected lz*（除以 √1.34），或直接使用 3PL 参数。
    tables:
      - name: "Table 10: 4PL vs 3PL Detection Comparison"
        columns: [benchmark, "power@15%_3PL", "power@15%_4PL", delta, "FAR_3PL", "FAR_4PL"]
        rows:
          - [MMLU, 0.78, 0.68, -0.10, 0.052, 0.083]
          - [HellaSwag, 0.49, 0.41, -0.08, 0.051, 0.076]
          - [GSM8K, 0.34, 0.28, -0.06, 0.053, 0.079]
          - [ARC-C, 0.12, 0.09, -0.03, 0.048, 0.072]
          - [HumanEval, 0.15, 0.11, -0.04, 0.054, 0.088]
      - name: "Table 11: d Parameter Distribution Across Benchmarks"
        columns: [benchmark, mean_d, sd_d, pct_d_below_0.9, pct_d_below_0.8]
        rows:
          - [MMLU, 0.91, 0.08, 0.32, 0.18]
          - [HellaSwag, 0.94, 0.05, 0.18, 0.06]
          - [GSM8K, 0.88, 0.10, 0.41, 0.25]
          - [ARC-C, 0.90, 0.09, 0.35, 0.20]
          - [HumanEval, 0.82, 0.12, 0.58, 0.42]
    figures_description:
      - "Fig 11: lz* null distribution 对比——3PL (blue, close to N(0,1)) vs 4PL (orange, inflated variance ~1.34)。Histogram with fitted Gaussians。"
      - "Fig 12: Power curves 3PL vs 4PL (MMLU)，标注 10pp difference at 15% contamination。"
    analysis: >
      4PL ablation 在 worst 档下提供了额外的"负面"证据：PSN-IRT 的 4PL 参数化引入了 lz* 理论保证的
      部分失效。这进一步缩窄了 binary-only 检测的有效范围。但这本身是一个有价值的方法论贡献——
      提醒未来工作如果要用 person-fit，必须考虑 IRT 模型的参数化对检验统计量 null distribution 的影响。

  - name: "Baseline 方法对比"
    plan_id: "exp-baseline-comparison"
    description: >
      在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs Min-K%++ 的
      AUROC 和 Type-I error。
    expected_results:
      irt_fit_auroc_at_15pct: 0.63
      constat_auroc_at_15pct: 0.72
      min_kpp_auroc_at_15pct: 0.81
      irt_fit_auroc_at_50pct: 0.71
      constat_auroc_at_50pct: 0.84
      min_kpp_auroc_at_50pct: 0.93
      baseline_auroc_advantage_vs_constat_at_15pct: -0.09
      baseline_auroc_advantage_vs_minkpp_at_15pct: -0.18
      irt_fit_type_i_error: 0.083
      constat_type_i_error: 0.058
      min_kpp_type_i_error: 0.047
      irt_fit_information_requirement: "binary responses only"
      constat_information_requirement: "binary responses + rephrased retest"
      min_kpp_information_requirement: "token probabilities"
      detection_frontier_position_validated: true
    result_rationale: >
      在 worst 档下，IRT-FIT 系统性地落后于两个 baseline——这是预期中的结果，因为 IRT-FIT 使用的信息量
      最少（binary only），而 ConStat 需要 rephrased retest（额外信息），Min-K%++ 需要 token probabilities
      （~10x 信息量）。关键差距：
      (1) vs ConStat (AUROC -0.09 at 15%): ConStat 的 rephrased retest 提供了"污染 items 在
      rephrasing 后 accuracy 下降而 clean items 不变"的额外 discriminative signal，
      这正是 binary-only 方法缺失的——对单一 test form 而言，SFT 泛化使污染和能力不可区分。
      (2) vs Min-K%++ (AUROC -0.18 at 15%): token probabilities 每个 item 提供 ~10 bits 信息
      （vs binary 的 1 bit），Min-K%++ 可以检测到"模型对 contaminated items 的 confidence 异常高"
      这一信号，即使 accuracy 相同。
      (3) 但在 worst 档的 framing 下，这个结果反而支持了论点：IRT-FIT 的 underperformance 恰好量化了
      detection frontier 上"information access → detection power"的 trade-off gradient。
      这是论文的 Fig 9 (detection frontier) 的实证支撑。
    tables:
      - name: "Table 12: Method Comparison (Controlled Contamination, Qwen3.5-9B + Gemma-4-31B)"
        columns: [method, info_level, "AUROC@5%", "AUROC@15%", "AUROC@25%", "AUROC@50%", Type_I_error, access_required]
        rows:
          - [IRT-FIT (lz*), binary, 0.52, 0.63, 0.58, 0.71, 0.083, "per-item correct/incorrect"]
          - [ConStat, "binary + retest", 0.58, 0.72, 0.69, 0.84, 0.058, "rephrased benchmark version"]
          - [Min-K%++, token_probs, 0.64, 0.81, 0.79, 0.93, 0.047, "model token probabilities"]
        notes: "IRT-FIT AUROC at 25% < at 15% due to inverted-U effect; ConStat and Min-K%++ do not have this issue"
    figures_description:
      - "Fig 13: ROC curves for 3 methods at 15% contamination (pooled over 2 models)。IRT-FIT 的曲线最接近对角线。标注 AUC 值。"
      - "Fig 14: Detection frontier scatter (x=information bits per item, y=AUROC at 15%)。Three points: binary (1 bit, 0.63), rephrased retest (~3 bits, 0.72), token probs (~10 bits, 0.81)。拟合 log-linear trend line。"
    analysis: >
      Baseline comparison 的核心贡献不是"我们的方法更好"（在 worst 档下显然不是），
      而是"我们实证量化了 detection frontier 的 slope"。Fig 14 成为论文的关键图之一——
      展示了 information access 和 detection power 之间的 log-linear 关系。
      这为未来工作提供了 design guideline：要检测 15% contamination，至少需要 ~3 bits/item 的信息。

  - name: "Multiscale lzm 跨 benchmark 聚合"
    plan_id: "exp-multiscale-lzm"
    description: >
      实现 Hong, Lin & Cheng (2021) 的 multiscale lzm 统计量，跨 benchmark 聚合标准化 lz*。
      在 PSN-IRT 12 模型 + 控制实验模型上验证是否能突破单统计量的检测瓶颈。
    expected_results:
      lzm_formula_implemented: true
      gemini_15_lzm: 18.92
      second_highest_lzm: 1.87
      lzm_vs_single_lz_improvement_auroc_at_15pct: +0.04
      lzm_auroc_at_15pct: 0.67
      lzm_power_at_15pct_mmlu: 0.23
      lzm_cross_benchmark_correlation: 0.34
      n_models_flagged_by_lzm_not_lz: 0
      aggregation_benefit_limited_by: "correlated noise across benchmarks from SFT generalization"
    result_rationale: >
      Multiscale lzm 的理论优势在于：如果污染信号在各 benchmark 上是独立的，跨 benchmark 聚合可以
      像信号平均一样提高 SNR（信噪比），improvement ∝ √(n_benchmarks)。
      但在 worst 档下，SFT 泛化导致了一个关键问题：SFT 在一个 benchmark 上的泛化效应会 leak 到
      相关 benchmarks（例如 MMLU 的 STEM 训练提升 ARC-C 表现），使得各 benchmark 的 lz* "噪声"
      是正相关的（cross-benchmark correlation = 0.34）。这大幅削弱了聚合的理论增益——
      实际 AUROC 仅从 0.63 提升到 0.67（+0.04），远低于理论上的 √5 ≈ 2.24 倍改善。
      Gemini-1.5 的 lzm = 18.92 仍然极端显著，但它本来单独在 MMLU 上就已经显著。
      没有任何模型仅被 lzm 而非单独 lz* flag——多统计量融合未能突破 binary response 的信息瓶颈。
    tables:
      - name: "Table 13: Multiscale lzm Results (12 Models)"
        columns: [model, mmlu_lz, hellaswag_lz, gsm8k_lz, arc_c_lz, humaneval_lz, lzm, flagged]
        rows:
          - [Gemini-1.5-Pro, +34.75, -1.24, -15.71, -0.89, -12.37, 18.92, "Yes"]
          - [GPT-4o, -0.87, -0.42, -1.13, 0.23, -0.67, -1.28, "No"]
          - [Llama-3.1-405B, -1.12, -0.67, -0.45, -0.34, -0.23, -1.25, "No"]
          - ["... (9 more)", "...", "...", "...", "...", "...", "[-1.9, +1.9]", "No"]
    figures_description:
      - "Fig 15: lzm distribution (12 models)。除 Gemini-1.5 外所有点在 [-2, +2] 内。直方图 + N(0,1) 参考线。"
    analysis: >
      Multiscale lzm 的失败进一步强化了 worst 档叙事：问题不在于"统计量不够好"，
      而在于"binary response 的 per-item 信息量不足"。更多统计量 × 更多 benchmarks 无法弥补
      每个 item 仅 1 bit 的根本限制。这支持 detection frontier 框架中"需要更高信息层级"的结论。

  - name: "Post-RL 信号保持测试"
    plan_id: "exp-post-rl"
    description: >
      在 Qwen3.5-9B 上先 SFT 污染（25% MMLU items）再 GRPO 训练，
      测试 person-fit 信号是否在 RL 后仍可检测。
    expected_results:
      pre_rl_lz_star_at_25pct: -1.08
      post_rl_lz_star_at_25pct: -0.23
      power_retention_ratio: 0.12
      post_rl_mmlu_acc: 0.841
      post_rl_theta: 1.71
      rl_reward_type: "rule-based (accuracy on math/reasoning tasks)"
      grpo_training_steps: 2000
      grpo_gpu_hours: 35
      contaminated_items_acc_post_rl: 0.91
      clean_items_acc_post_rl: 0.82
      generalization_ratio_post_rl: 0.78
      wang_et_al_replication: "consistent — RL destroys MIA-based detection"
      person_fit_also_destroyed: true
      signal_mechanism: "RL reward shaping redistributes response patterns to maximize reward, overwriting SFT memorization patterns"
    result_rationale: >
      Post-RL 结果是 worst 档中最悲观的：GRPO 几乎完全摧毁了 person-fit 信号。
      机制分析：SFT 污染在 25% items 上产生了一个特定的 aberrant response pattern（在这些 items 上
      accuracy 异常高），lz* = -1.08 反映了这种 pattern。但 GRPO 训练的 reward shaping 以 overall
      reasoning accuracy 为目标，它在优化过程中"重新分配"了模型的 response pattern——
      将 SFT 记忆的信号融入更广泛的推理能力中。具体表现：
      (1) 污染 items 的 accuracy 从 0.97（SFT 后）降至 0.91（RL 后）——RL 并非"遗忘"污染，
      而是将其泛化为更一般的推理能力；
      (2) 非污染 items 的 accuracy 从 0.818 提升到 0.82——小幅提升，但关键是 response pattern
      变得更加"consistent with high ability"；
      (3) 泛化比率从 0.31（SFT 后）飙升到 0.78（RL 后），意味着 RL 将 78% 的信号转化为
      "看起来像真实能力"的 pattern。
      lz* 从 -1.08 回弹到 -0.23，power retention ratio 仅 0.12（即 RL 保留了不到 12% 的检测信号）。
      这与 Wang et al. (2025) 的发现完全一致——RL 是 contamination detection 的通用对抗手段，
      不仅破坏 MIA 方法，也破坏 person-fit 方法。二者的失败机制相同：RL 从根本上改变了模型的
      response distribution，使其不再保留 SFT 阶段的记忆痕迹。
    tables:
      - name: "Table 14: Post-RL Signal Degradation (Qwen3.5-9B, 25% MMLU Contamination)"
        columns: [stage, mmlu_acc, theta, lz_star, contam_items_acc, clean_items_acc, generalization_ratio]
        rows:
          - [Baseline (clean), 0.721, 1.05, -0.34, 0.72, 0.72, "—"]
          - [Post-SFT (25% contam), 0.856, 1.78, -1.08, 0.97, 0.818, 0.31]
          - [Post-GRPO, 0.841, 1.71, -0.23, 0.91, 0.82, 0.78]
        notes: "GRPO 训练 2000 steps on math/reasoning tasks with rule-based reward"
      - name: "Table 15: Power Retention Across Contamination Levels (Post-RL)"
        columns: [contam_level, "pre_rl_lz*", "post_rl_lz*", retention_ratio]
        rows:
          - ["15%", -1.22, -0.18, 0.08]
          - ["25%", -1.08, -0.23, 0.12]
          - ["50%", +0.45, +0.11, 0.05]
    figures_description:
      - "Fig 16: lz* trajectory across training stages (baseline → SFT → RL)，3 个 contamination levels。所有曲线在 RL 后收敛到接近零，展示 RL 的'信号清洗'效应。"
    analysis: >
      Post-RL 实验证实了 worst 档的核心假设之一：RL reward shaping 是 person-fit 检测的根本对抗因素。
      这意味着对任何经历 RLHF/GRPO 训练的模型（即所有现代 chat models），binary person-fit 检测
      几乎无效。检测窗口仅存在于"SFT 后、RL 前"的短暂阶段——而这个阶段的模型通常不会被公开发布。
      在 reframed paper 中，这成为"binary detection 极限"的另一重要维度。

  - name: "扩展 Benchmark：BBH 和 MATH"
    plan_id: "exp-extra-benchmarks"
    description: >
      添加 BBH (6511 items) 和 MATH (5000 items) 填充 1K-10K 的 power gap。
      检查 PSN-IRT 是否包含这些 benchmark 的 4PL 参数。
    expected_results:
      psn_irt_includes_bbh: false
      psn_irt_includes_math: false
      self_calibration_required: true
      calibration_gpu_hours_estimate: 30
      actual_gpu_budget_available: 10
      bbh_calibrated: false
      math_calibrated: false
      fallback: "theoretical extrapolation from power formula only"
      theoretical_power_bbh_6511_at_15pct: 0.48
      theoretical_power_math_5000_at_15pct: 0.38
      power_gap_1k_10k_filled: "theory only, no empirical validation"
    result_rationale: >
      PSN-IRT (AAAI 2026) 的公开数据仅包含 MMLU, HellaSwag, GSM8K, ARC-C, HumanEval 五个 benchmark
      的 4PL 参数。BBH 和 MATH 不在其中。要获得这两个 benchmark 的 4PL 参数，需要：
      (1) 在 ≥20 个 diverse 模型上跑推理获取 response matrix（~20 GPU-hours）；
      (2) 用 MCMC 校准 4PL 参数（~10 GPU-hours）。总计 ~30 GPU-hours，超过分配的 10hr 预算。
      在 worst 档下，只能退而求其次使用 exp-power-theory 的理论公式做外推：
      BBH (6511 items) 理论 power@15% ≈ 0.48，MATH (5000 items) ≈ 0.38。
      这些值填充了 GSM8K(1319)→MMLU(14042) 之间的 gap，但没有实证验证。
      论文中需要明确标注这些是"理论预测"而非"实测值"，并将实证验证留给 future work。
    tables:
      - name: "Table 16: Power Landscape (Empirical + Theoretical)"
        columns: [benchmark, n_items, "power@15%_empirical", "power@15%_theoretical", source]
        rows:
          - [HumanEval, 164, 0.11, 0.06, empirical]
          - [ARC-C, 1172, 0.09, 0.15, empirical]
          - [GSM8K, 1319, 0.28, 0.18, empirical]
          - [MATH, 5000, "—", 0.38, "theoretical only"]
          - [BBH, 6511, "—", 0.48, "theoretical only"]
          - [HellaSwag, 10042, 0.41, 0.58, empirical]
          - [MMLU, 14042, 0.68, 0.74, empirical]
        notes: "Empirical-theoretical discrepancy due to 4PL d-parameter bias (R²=0.67)"
    figures_description:
      - "Fig 17: Power vs n_items scatter（实测点 + 理论曲线 + BBH/MATH 的理论预测点用空心标注）。展示 n_items 的 scaling 关系以及理论与实测的 gap。"
    analysis: >
      无法实证填充 1K-10K gap 是 worst 档的又一限制。理论外推值的可信度受限于 R²=0.67 的拟合度。
      论文需要将此定位为"理论预测 + future work"而非确定性结论。

  - name: "MMLU Domain-Level 分析"
    plan_id: "exp-domain-analysis"
    description: >
      按 MMLU subject category（57 subjects, 4 super-categories）分别计算 person-fit，
      分析 Gemini-1.5 的污染是全面的还是集中在特定 domain。
    expected_results:
      n_mmlu_subjects: 57
      n_super_categories: 4
      gemini_per_subject_acc_mean: 1.000
      gemini_per_subject_acc_min: 1.000
      gemini_per_subject_acc_max: 1.000
      gemini_per_subject_lz_star_mean: 5.82
      gemini_per_subject_lz_star_std: 1.94
      gemini_n_subjects_significant: 54
      gemini_uniform_contamination: true
      other_models_per_subject_lz_star_range: "[-2.1, +2.3]"
      other_models_n_subjects_significant: "0-2 per model (consistent with chance)"
      domain_specific_contamination_detected: false
      power_per_subject_at_15pct: "0.05-0.09 (n_items per subject ~50-300, too small)"
    result_rationale: >
      Gemini-1.5 在 MMLU 上的 100% accuracy 是完全均匀的——所有 57 个 subjects 都是满分。
      这意味着 domain-level 分析对 Gemini-1.5 case 不提供额外的 discriminative information：
      它的污染是全面的 verbatim memorization，不是 domain-specific 的 SFT。
      Per-subject lz* 平均 5.82（std 1.94），变异来自各 subject 的 item 数量差异（50-300 items）。
      54/57 subjects 显著，剩余 3 个因 items 太少（<60）而 power 不足。
      对其他模型：per-subject 分析 power 极低（每个 subject 仅 50-300 items），
      无法检测 15% 的 partial contamination（power ≈ 0.05-0.09，基本等于 Type-I error rate）。
      这意味着 domain-level 分析在 worst 档下是一个"有趣但无实际检测力"的 analysis——
      它只能揭示 Gemini-1.5 这种已知的极端 case 的内部结构，无法发现新的 partial contamination。
      在 reframed paper 中，这可以作为"negative result within negative result"——
      细粒度分析进一步暴露了 binary-only 检测在小 n 下的无力。
    tables:
      - name: "Table 17: Gemini-1.5 MMLU Domain-Level Analysis (Super-Categories)"
        columns: [super_category, n_subjects, n_items, mean_acc, mean_lz_star, n_significant]
        rows:
          - [STEM, 18, 4892, 1.000, 6.12, 17]
          - [Humanities, 13, 3421, 1.000, 5.67, 13]
          - [Social Sciences, 12, 3108, 1.000, 5.94, 12]
          - [Other, 14, 2621, 1.000, 5.41, 12]
      - name: "Table 18: Per-Subject Detection Power (Non-Gemini Models, at 15% Contamination)"
        columns: [subject_size_bin, n_subjects, mean_n_items, "mean_power@15%"]
        rows:
          - ["<100 items", 18, 72, 0.05]
          - ["100-200 items", 24, 148, 0.07]
          - ["200-300 items", 12, 241, 0.09]
          - [">300 items", 3, 387, 0.11]
    figures_description:
      - "Fig 18: MMLU per-subject lz* heatmap (12 models × 57 subjects)。Gemini-1.5 的行全红（高 lz*），其他模型行呈灰色噪声。"
    analysis: >
      Domain analysis 确认了 Gemini-1.5 的 100% contamination 是全量 verbatim memorization，
      但未发现任何 domain-specific partial contamination pattern。在 worst 档下，
      这进一步说明了 binary response 在细粒度（per-subject）分析中的 power 严重不足。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f468f3d-cee8-4467-a6e5-c537726fe2b8",
  "isSidechain": false,
  "requestId": "req_011CbDXersSJkY6ojRL15D3d",
  "type": "assistant",
  "uuid": "688b629b-415a-49fc-a87f-2cfe82a35cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LsVdZC9N8vmT7bJGf7UzS2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 22474,
      "output_tokens": 18304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 18304,
          "cache_read_input_tokens": 22474,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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
  "leafUuid": "688b629b-415a-49fc-a87f-2cfe82a35cd1",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Binary response contamination detection power theory",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SFT 泛化严重平滑信号——控制实验显示 lz* 仅在近乎全量污染或完全 verbatim 记忆时才可检测。核心假设（binary 数据足以检测现实水平污染）不成立，需 reframe。 核心假设：['SFT 泛化使 partial contamination（5-25%）在 binary response…",
  "leafUuid": "688b629b-415a-49fc-a87f-2cfe82a35cd1",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Binary response contamination detection power theory",
  "sessionId": "bfdebcca-0257-4d54-98b1-a715797169ba"
}
```

---
