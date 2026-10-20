# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Δlz* 控制实验完全验证——注入已知污染后 lz* 偏移大且单调，三条 Claims 原样成立 核心假设：["SFT 注入污染后 Δlz* 效应量大（

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/602a4653-1334-49b1-919f-e83a76f5ca81.jsonl`
- **Structured JSON:** [`297a920632d3ef1c4af2.json`](../../sessions/29/297a920632d3ef1c4af2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T09:27:52.059Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T09:27:52.059Z",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Δlz* 控制实验完全验证——注入已知污染后 lz* 偏移大且单调，三条 Claims 原样成立\n核心假设：[\"SFT 注入污染后 Δlz* 效应量大（Cohen's d > 2.0），clean vs contaminated 明确可分\", 'Δlz* 与污染比例呈单调关系（dose-response），inverted-U 拐点可复现且与理论推导吻合', '跨模型泛化：Qwen3.5-9B 和 Gemma-4-31B 上趋势一致，非模型特异性', 'Leaderboard per-item data 可用（≥500 模型），大规模审计可执行', 'Baseline 对比：IRT-FIT AUROC 与 ConStat/Min-K%++ 差距 <10%（在 minimal-info 约束下接近 gray-box 表现）']\n关键指标范围：{'delta_lz_star_cohen_d_at_15pct_mmlu': [2.0, 5.0], 'controlled_auroc_at_15pct_mmlu': [0.9, 0.99], 'controlled_auroc_at_5pct_mmlu': [0.7, 0.9], 'power_delta_method_at_15pct_mmlu': [0.85, 0.97], 'baseline_auroc_gap_vs_constat': [-0.05, 0.05], 'leaderboard_models_with_peritem_data': [500, 7000], 'leaderboard_flagged_rate_relative': [0.05, 0.25], 'cross_benchmark_spearman_in_ctrl': [0.6, 0.9], 'inverted_u_theoretical_fit_r2': [0.9, 0.99]}\n叙事方向：原始 framing 完全成立。Claim 1: minimal-information detection 经控制实验验证，Δlz* 提供 可靠的相对检测信号，calibration gap 被 bridged。Claim 2: inverted-U 从经验升级为理论命题， dose-response 曲线在两个模型上复现。Claim 3: leaderboard 大规模审计揭示生态系统级污染趋势， Gemini-1.5 case study 由控制实验的 Δlz* 基线提供定量支撑。Headline: \"IRT-FIT achieves AUROC>0.9 at 15% contamination using only binary responses, and a leaderboard-wide audit reveals X% of models exhibit contamination-consistent misfit.\"\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_personfit_contam\nfocus: 重点评估：(1) 双侧检测框架是否足够新颖作为独立贡献 (2) 仅 12 模型 + 5 benchmarks 是否 scope 太窄 (3) Gemini-1.5 case study 是否足够有说服力（无 ground truth）(4) 控制实验设计是否能回应 \"no ground truth\" 的审稿意见\n\n## paper_framing.md\n\n# Paper Framing — irt_personfit_contam\n\n## Target Venue\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\n\n## Core Claims (3 条)\n\n**Claim 1 (Minimal-Information Detection + Calibration Gap)**:\nIRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks). However, real LLM data exhibits universal IRT model misfit (local independence / unidimensionality violations), making absolute thresholds unreliable. We bridge this calibration gap via controlled contamination experiments that quantify the Δlz* between clean and contaminated models, enabling relative detection through contamination-induced misfit delta rather than absolute person-fit scores.\n\n**Claim 2 (Detection Characterization)**:\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\n\n**Claim 3 (Empirical Prevalence)**:\nApplying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.\n\n## Story Spine\n\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\n\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\n\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: \"What can be detected from binary response patterns alone?\" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks); (2) in real LLM data, universal IRT model misfit creates a calibration gap that prevents absolute threshold detection; (3) controlled contamination experiments bridge this gap by quantifying the misfit delta (Δlz*) between clean and contaminated models. The calibration gap itself is a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns, violating local independence assumptions.\n\n**Headline result template**: \"Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items). Real-world application reveals universal IRT model misfit in LLMs — we bridge this calibration gap via controlled experiments showing contamination induces a measurable Δlz* shift of X SD above natural misfit baseline.\"\n\n## Venue Fit Risks\n\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \"no new NLP model/technique\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\n\n## Anticipated Reviewer Concerns & Planned Responses\n\n| # | Concern | Response Strategy | Supporting Experiment |\n|---|---------|------------------|----------------------|\n| R1 | \"Just applying existing IRT to LLMs\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \"cross-domain\" from contribution to background. | — |\n| R2 | \"No ground truth contamination labels\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\n| R3 | \"Power too low for small benchmarks\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\n| R4 | \"Only 12 models\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\n| R5 | \"SFT generalization smooths signal\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\n| R6 | \"Absolute lz* thresholds don't work on real data\" | Honest finding: universal model misfit makes absolute thresholds unreliable. Controlled calibration (Δlz*) solves this. The calibration gap itself is a contribution. | exp-ctrl-contam |\n| R7 | \"Post-RL contamination?\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\n| R8 | \"4PL vs 3PL — does d parameter matter?\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\n\n## Key Narrative Elements (from External Review)\n\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\n4. **Scope precision** — Target: \"intentional SFT contamination / leaderboard gaming\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\n\n## Evidence Summary\n\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.\n- **Calibration gap (D007)**: Absolute lz* thresholds flag 95% of (model, benchmark) cells — universal IRT model misfit, not contamination. Root cause: LLM responses violate local independence (knowledge clustering) and unidimensionality. Simulation-to-real-data gap is itself a finding.\n- **Path forward**: Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models. Relative delta approach replaces absolute thresholds.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-two-sided\n  claim: 2\n  description: 实现双侧检测框架：|lz*| > threshold 或分别设正/负阈值。用 Phase B 数据验证（Gemini-1.5 case\n    study）。包括 bootstrap confidence interval 和 FDR 控制。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  notes: CPU only. 基于已有 Phase B personfit_matrix.csv 重新分析。\n- id: exp-extended-sim\n  claim: 2\n  description: 扩展 Phase A 模拟：添加 60%/75%/90% contamination levels，修复 100% NaN 处理（让\n    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向\n    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。\n- id: exp-ctrl-contam-pilot\n  claim: 1,2,3\n  description: 快速验证：Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU only。测量 Δlz*(clean→contaminated)\n    是否显著。这是论文 go/no-go 信号——如果 Δlz* 不显著则需 pivot。\n  priority: P0-CRITICAL\n  gpu_budget_hours: 10\n  deps: []\n  status: planned\n  notes: GPU 恢复后第一优先。1× RTX 5090 (~8GB for Qwen3.5-9B QLoRA). 3 runs × ~3 hrs = ~10\n    GPU-hrs. MMLU only 先跑因为 n_items 最大(14K), signal 最强。\n- id: exp-ctrl-contam\n  claim: 1,2,3\n  description: 完整控制实验：在 Qwen3.5-9B 和 Gemma-4-31B 上，用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50%\n    benchmark items，测量 Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - exp-ctrl-contam-pilot\n  status: planned\n  notes: 'Qwen3.5-9B: 1× RTX 5090 (~8GB). Gemma-4-31B: 1× RTX 5090 (~20GB). 2 模型 ×\n    6 levels × ~3-7 hrs = ~60-80 GPU-hrs.'\n- id: exp-power-theory\n  claim: 2\n  description: 推导 power 与 n_items 的解析关系（基于 Snijders 2001 lz* 方差公式）。验证理论曲线与 Phase A\n    模拟结果的拟合度。将 inverted-U 从经验观察升级为理论命题。\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 纯理论推导 + 数值验证。CPU only.\n- id: exp-leaderboard-data-recon\n  claim: 3\n  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results\n    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item\n    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。\n- id: exp-leaderboard-audit\n  claim: 3\n  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark\n    污染率随时间趋势。\n  priority: P1\n  gpu_budget_hours: 20\n  deps:\n  - exp-two-sided\n  - exp-leaderboard-data-recon\n  status: planned\n  notes: GPU 预算取决于 data-recon 结果。如果 per-item logs 可用则 ~20 GPU-hrs（纯计算），不可用则 200+ GPU-hrs（需跑推理）。\n- id: exp-4pl-ablation\n  claim: 1\n  description: 4PL vs 3PL(d=1) ablation：比较两种参数化下的检测灵敏度差异。量化 feasibility parameter\n    d 对 false alarm 和 detection power 的影响。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: CPU only. 用已有 PSN-IRT 参数，固定 d=1 重新计算。\n- id: exp-baseline-comparison\n  claim: 1\n  description: 与现有方法对比（ConStat, Min-K%++）：在控制实验的 ground-truth contaminated models\n    上，比较 IRT-FIT vs baselines 的 AUROC/Type-I error。量化 minimal-information 的代价（power\n    损失）。\n  priority: P0-end\n  gpu_budget_hours: 30\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: Claim 1 的可信度依赖此对比。exp-ctrl-contam 完成后立即执行。ConStat 需要 re-test，Min-K%++ 需要\n    token probabilities。\n- id: exp-multiscale-lzm\n  claim: 1,3\n  description: 实现 multiscale lzm 统计量（Hong, Lin & Cheng, 2021）——跨 benchmark 聚合的标准化\n    lz* 总分，提供整体污染指标。在 PSN-IRT 12 模型 + 控制实验模型上验证。\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要实现 lzm 公式。\n- id: exp-post-rl\n  claim: 1\n  description: Post-RL 假设检验：在 Qwen3.5-9B 上先 SFT 污染再 GRPO 训练，测试 person-fit 是否在 RL 后仍保持检测力。回应\n    Wang et al. (2025) 的 MIA 失效问题。\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-ctrl-contam\n  status: planned\n  notes: GRPO 训练需要 reward model 或 rule-based reward。可能需要 2× RTX 5090。\n- id: exp-extra-benchmarks\n  claim: 2,3\n  description: 扩展 benchmark：BBH (6,511 items) 和 MATH (5,000 items) 填充 1K-10K items\n    的 power gap。需要获取 4PL 参数（PSN-IRT 可能已有）。\n  priority: P2\n  gpu_budget_hours: 10\n  deps:\n  - exp-extended-sim\n  status: planned\n  notes: 取决于 PSN-IRT 是否包含这些 benchmark 的参数。如果没有，需要自己校准 4PL（GPU + 大量推理）。\n- id: exp-domain-analysis\n  claim: 3\n  description: MMLU domain-level 分析：按 subject category 分别计算 person-fit，识别 Gemini-1.5\n    的 MMLU 污染是全面的还是集中在特定 domain。\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - exp-two-sided\n  status: planned\n  notes: CPU only. 需要 MMLU item-to-domain 映射。\n\n\n## registry (completed experiments)\n\n- exp_id: sim_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    null_check:\n      all_pass: true\n      gsm8k_ks_p: 0.098\n      hellaswag_ks_p: 0.224\n      mmlu_ks_p: 0.594\n    simulation_power_at_15pct:\n      mmlu: 0.979\n      hellaswag: 0.733\n      gsm8k: 0.578\n      arc_c: 0.129\n      humaneval: 0.243\n    global_pass: false\n    inverted_u_all_benchmarks: true\n    pass_count_large_80pct: 1/3 (mmlu only)\n- exp_id: phase_b_personfit\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    lz_star_sd_all_gt_0.5: true\n    mmlu_lz_star_mean: 24.19\n    mmlu_lz_star_sd: 16.47\n    hellaswag_lz_star_mean: 20.09\n    hellaswag_lz_star_sd: 17.59\n    gsm8k_lz_star_mean: 8.22\n    gsm8k_lz_star_sd: 8.97\n    gemini15_mmlu_lz_star: 34.75\n    gemini15_mmlu_accuracy: 1\n    gemini15_mmlu_theta: 0.78\n    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)\n    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)\n    n_models: 12\n    n_benchmarks: 5\n- exp_id: exp-two-sided\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    flagged_rate: 57/60 (95.0%)\n    n_boot: 1000\n    fdr_alpha: 0.05\n    flagged_positive: 51\n    flagged_negative: 6\n    unflagged: 3\n    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),\n      Yi-Lightning/humaneval (p=0.181)\n    gemini15_mmlu_lz_star_v2: 31.815\n    gemini15_mmlu_theta_bench: 4\n    gemini15_mmlu_p_emp: 0\n    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.\n      LLMs universally violate 4PL assumptions.\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T09:27:52.069Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T09:27:52.069Z",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T09:27:52.128Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Δlz* 控制实验完全验证——注入已知污染后 lz* 偏移大且单调，三条 Claims 原样成立
核心假设：["SFT 注入污染后 Δlz* 效应量大（Cohen's d > 2.0），clean vs contaminated 明确可分", 'Δlz* 与污染比例呈单调关系（dose-response），inverted-U 拐点可复现且与理论推导吻合', '跨模型泛化：Qwen3.5-9B 和 Gemma-4-31B 上趋势一致，非模型特异性', 'Leaderboard per-item data 可用（≥500 模型），大规模审计可执行', 'Baseline 对比：IRT-FIT AUROC 与 ConStat/Min-K%++ 差距 <10%（在 minimal-info 约束下接近 gray-box 表现）']
关键指标范围：{'delta_lz_star_cohen_d_at_15pct_mmlu': [2.0, 5.0], 'controlled_auroc_at_15pct_mmlu': [0.9, 0.99], 'controlled_auroc_at_5pct_mmlu': [0.7, 0.9], 'power_delta_method_at_15pct_mmlu': [0.85, 0.97], 'baseline_auroc_gap_vs_constat': [-0.05, 0.05], 'leaderboard_models_with_peritem_data': [500, 7000], 'leaderboard_flagged_rate_relative': [0.05, 0.25], 'cross_benchmark_spearman_in_ctrl': [0.6, 0.9], 'inverted_u_theoretical_fit_r2': [0.9, 0.99]}
叙事方向：原始 framing 完全成立。Claim 1: minimal-information detection 经控制实验验证，Δlz* 提供 可靠的相对检测信号，calibration gap 被 bridged。Claim 2: inverted-U 从经验升级为理论命题， dose-response 曲线在两个模型上复现。Claim 3: leaderboard 大规模审计揭示生态系统级污染趋势， Gemini-1.5 case study 由控制实验的 Δlz* 基线提供定量支撑。Headline: "IRT-FIT achieves AUROC>0.9 at 15% contamination using only binary responses, and a leaderboard-wide audit reveals X% of models exhibit contamination-consistent misfit."


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

**Claim 1 (Minimal-Information Detection + Calibration Gap)**:
IRT person-fit statistics provide a principled contamination detection framework at the minimal-information operating point — requiring only binary response patterns. Simulation establishes high theoretical detection power (97.9% on MMLU-scale benchmarks). However, real LLM data exhibits universal IRT model misfit (local independence / unidimensionality violations), making absolute thresholds unreliable. We bridge this calibration gap via controlled contamination experiments that quantify the Δlz* between clean and contaminated models, enabling relative detection through contamination-induced misfit delta rather than absolute person-fit scores.

**Claim 2 (Detection Characterization)**:
Detection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.

**Claim 3 (Empirical Prevalence)**:
Applying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.

## Story Spine

**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.

**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.

**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics — developed over decades for detecting exam cheating — we ask: "What can be detected from binary response patterns alone?" We show: (1) in simulation, person-fit statistics achieve high detection power (97.9% on MMLU-scale benchmarks); (2) in real LLM data, universal IRT model misfit creates a calibration gap that prevents absolute threshold detection; (3) controlled contamination experiments bridge this gap by quantifying the misfit delta (Δlz*) between clean and contaminated models. The calibration gap itself is a contribution — it reveals that LLM response patterns are fundamentally different from classical test-taker patterns, violating local independence assumptions.

**Headline result template**: "Using only binary response patterns, IRT-FIT achieves 97.9% simulated detection power on MMLU (14K items). Real-world application reveals universal IRT model misfit in LLMs — we bridge this calibration gap via controlled experiments showing contamination induces a measurable Δlz* shift of X SD above natural misfit baseline."

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
| R6 | "Absolute lz* thresholds don't work on real data" | Honest finding: universal model misfit makes absolute thresholds unreliable. Controlled calibration (Δlz*) solves this. The calibration gap itself is a contribution. | exp-ctrl-contam |
| R7 | "Post-RL contamination?" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |
| R8 | "4PL vs 3PL — does d parameter matter?" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |

## Key Narrative Elements (from External Review)

1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.
2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.
3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).
4. **Scope precision** — Target: "intentional SFT contamination / leaderboard gaming". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.

## Evidence Summary

- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed. Simulation results stand — they establish theoretical detection capacity within the 4PL model.
- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark anomaly profiles identified.
- **Calibration gap (D007)**: Absolute lz* thresholds flag 95% of (model, benchmark) cells — universal IRT model misfit, not contamination. Root cause: LLM responses violate local independence (knowledge clustering) and unidimensionality. Simulation-to-real-data gap is itself a finding.
- **Path forward**: Controlled experiments (exp-ctrl-contam) measure Δlz* between clean and contaminated models. Relative delta approach replaces absolute thresholds.


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
    MLE boundary θ=4.0 正常计算 lz*），精确刻画 inverted-U 拐点。同时计算 two-sided power curves（正向
    lz*>1.96 和负向 lz*<-1.96 分别的 detection rate），量化 Claim 2 的 dual-regime signal structure。
  priority: P0
  gpu_budget_hours: 0
  deps:
  - exp-two-sided
  status: planned
  notes: CPU only. 依赖 exp-two-sided 的双侧框架定义。
- id: exp-ctrl-contam-pilot
  claim: 1,2,3
  description: 快速验证：Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU only。测量 Δlz*(clean→contaminated)
    是否显著。这是论文 go/no-go 信号——如果 Δlz* 不显著则需 pivot。
  priority: P0-CRITICAL
  gpu_budget_hours: 10
  deps: []
  status: planned
  notes: GPU 恢复后第一优先。1× RTX 5090 (~8GB for Qwen3.5-9B QLoRA). 3 runs × ~3 hrs = ~10
    GPU-hrs. MMLU only 先跑因为 n_items 最大(14K), signal 最强。
- id: exp-ctrl-contam
  claim: 1,2,3
  description: 完整控制实验：在 Qwen3.5-9B 和 Gemma-4-31B 上，用 QLoRA SFT 注入 0%/5%/10%/15%/25%/50%
    benchmark items，测量 Δlz* 全谱。建立 ground-truth contamination → Δlz* 映射。
  priority: P0
  gpu_budget_hours: 80
  deps:
  - exp-ctrl-contam-pilot
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
- id: exp-leaderboard-data-recon
  claim: 3
  description: Open LLM Leaderboard v1 数据可用性调研：确认 HuggingFace open-llm-leaderboard-old/results
    是否包含 per-item binary response logs（不仅是 aggregate scores）。如果可用，评估数据量（多少模型有 per-item
    data）、格式、覆盖的 benchmarks。如果不可用，估算自己跑推理的 GPU 预算增量。
  priority: P0
  gpu_budget_hours: 0
  deps: []
  status: planned
  notes: 纯调研，CPU only。结果直接决定 exp-leaderboard-audit 的可行性和 GPU 预算。
- id: exp-leaderboard-audit
  claim: 3
  description: Open LLM Leaderboard v1 大规模扫描：对所有可用模型计算 person-fit。绘制 per-benchmark
    污染率随时间趋势。
  priority: P1
  gpu_budget_hours: 20
  deps:
  - exp-two-sided
  - exp-leaderboard-data-recon
  status: planned
  notes: GPU 预算取决于 data-recon 结果。如果 per-item logs 可用则 ~20 GPU-hrs（纯计算），不可用则 200+ GPU-hrs（需跑推理）。
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
    上，比较 IRT-FIT vs baselines 的 AUROC/Type-I error。量化 minimal-information 的代价（power
    损失）。
  priority: P0-end
  gpu_budget_hours: 30
  deps:
  - exp-ctrl-contam
  status: planned
  notes: Claim 1 的可信度依赖此对比。exp-ctrl-contam 完成后立即执行。ConStat 需要 re-test，Min-K%++ 需要
    token probabilities。
- id: exp-multiscale-lzm
  claim: 1,3
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
  claim: 2,3
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
- exp_id: phase_b_personfit
  name: ''
  status: DONE
  conclusion: success
  metrics:
    lz_star_sd_all_gt_0.5: true
    mmlu_lz_star_mean: 24.19
    mmlu_lz_star_sd: 16.47
    hellaswag_lz_star_mean: 20.09
    hellaswag_lz_star_sd: 17.59
    gsm8k_lz_star_mean: 8.22
    gsm8k_lz_star_sd: 8.97
    gemini15_mmlu_lz_star: 34.75
    gemini15_mmlu_accuracy: 1
    gemini15_mmlu_theta: 0.78
    gemini15_flagged_benchmarks: 3/5 (HellaSwag, GSM8K, HumanEval negative lz*)
    cross_benchmark_spearman_significant: 1/10 (GSM8K vs HumanEval rho=0.62 p=0.031)
    n_models: 12
    n_benchmarks: 5
- exp_id: exp-two-sided
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    flagged_rate: 57/60 (95.0%)
    n_boot: 1000
    fdr_alpha: 0.05
    flagged_positive: 51
    flagged_negative: 6
    unflagged: 3
    unflagged_cells: Yi-Lightning/arc_c (p=0.098), 360GPT2-Pro/humaneval (p=0.134),
      Yi-Lightning/humaneval (p=0.181)
    gemini15_mmlu_lz_star_v2: 31.815
    gemini15_mmlu_theta_bench: 4
    gemini15_mmlu_p_emp: 0
    key_finding: Benchmark-specific θ + bootstrap + FDR does NOT reduce flagging.
      LLMs universally violate 4PL assumptions.

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
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
  "promptId": "b755e64f-fa82-43a9-bbed-0f13f721a562",
  "type": "user",
  "uuid": "f39fb2c2-b71c-4af5-b242-377c3e6cc4fa",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T09:27:52.126Z_

```json
{
  "parentUuid": "f39fb2c2-b71c-4af5-b242-377c3e6cc4fa",
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
  "uuid": "5aae204b-a59a-4ebe-a16a-ea0487f51302",
  "timestamp": "2026-05-20T09:27:52.126Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T09:27:52.126Z_

```json
{
  "parentUuid": "5aae204b-a59a-4ebe-a16a-ea0487f51302",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bd3ea988-8e64-4aa9-958e-607ff55b6f8a",
  "timestamp": "2026-05-20T09:27:52.126Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Δlz* 控制实验完全验证——注入已知污染后 lz* 偏移大且单调，三条 Claims 原样成立 核心假设：[\"SFT 注入污染后 Δlz* 效应量大（Cohen's d > 2.0），clean vs contaminated 明确可分\", 'Δlz* 与污染比例呈单调关系（dose-response），i…",
  "leafUuid": "bd3ea988-8e64-4aa9-958e-607ff55b6f8a",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Design best-case controlled contamination experiments for IRT-FIT",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81"
}
```

---

### Assistant

_source line 8 · 2026-05-20T09:28:19.312Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined/predicted experimental results for each planned experiment in the experiment plan, under the "best" tier definition. I need to provide specific predicted metrics with rationales for why those results would occur in this best-case scenario.

Let me carefully go through each experiment and generate detailed predictions consistent with the "best" tier definition.

The best tier means:
- Δlz* control experiment fully validated
- Cohen's d > 2.0 for delta_lz_star at 15% MMLU
- Controlled AUROC at 15% MMLU: 0.9-0.99


- Controlled AUROC at 5% MMLU: 0.7-0.9
- Power delta method at 15% MMLU: 0.85-0.97
- Baseline AUROC gap vs ConStat: -0.05 to 0.05
- Leaderboard models with per-item data: 500-7000
- Leaderboard flagged rate relative: 0.05-0.25
- Cross-benchmark Spearman in ctrl: 0.6-0.9
- Inverted-U theoretical fit R²: 0.9-0.99

Now I'm working through each planned experiment to generate specific predicted metrics that align with these best-case parameters. Now I'm working through the best-case predictions for each planned experiment. For the extended simulation, I'm expecting the inverted-U pattern to be clearly visible with the peak around 50-60% contamination, strong separation between positive and negative regimes, and a theoretical fit R² above 0.9. The pilot experiment with Qwen should show highly significant changes in the contamination metric with clear tier separation. For the full controlled experiment across models and contamination levels, I'm targeting Cohen's d greater than 2.0 to demonstrate a strong effect size.

Moving through the remaining experiments, I need the detection method to maintain AUROC above 0.9 at 15% contamination with a monotonic dose-response curve. The analytical power derivation should achieve R² > 0.9 when fitted to simulation data. For the leaderboard reconstruction, I'm aiming to recover per-item data for 500-7000 models, and the large-scale audit should flag 5-25% of entries with meaningful temporal patterns. The 4PL model should show clear advantages over the 3PL variant, and when compared against existing methods like ConStat and Min-K++, the AUROC gap should stay under 5%. The cross-benchmark aggregation should improve consistency, post-RL detection should persist though weakened, and the additional benchmarks should fill power gaps while staying consistent with theory. Finally, domain-level analysis of MMLU should reveal meaningful patterns across different subject areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd3ea988-8e64-4aa9-958e-607ff55b6f8a",
  "isSidechain": false,
  "requestId": "req_011CbDao3dQuwaLmuk5rnw1F",
  "type": "assistant",
  "uuid": "1e1c2e34-5104-4ddd-b447-17de911ed703",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxtQ8MA4et9dNDnep5sajD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11685,
      "cache_read_input_tokens": 11841,
      "output_tokens": 20215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 20215,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11685
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

_source line 9 · 2026-05-20T09:33:43.079Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。Claim 1: minimal-information detection 经控制实验验证，Δlz* 提供
  可靠的相对检测信号，calibration gap 被 bridged。Claim 2: inverted-U 从经验升级为理论命题，
  dose-response 曲线在两个模型上复现。Claim 3: leaderboard 大规模审计揭示生态系统级污染趋势，
  Gemini-1.5 case study 由控制实验的 Δlz* 基线提供定量支撑。
  Headline: "IRT-FIT achieves AUROC>0.9 at 15% contamination using only binary responses,
  and a leaderboard-wide audit reveals ~12% of models exhibit contamination-consistent misfit."

imagined_experiments:

  - name: "Extended Simulation — Inverted-U Full Characterization"
    plan_id: "exp-extended-sim"
    description: >
      在 Phase A 模拟基础上添加 60%/75%/90%/100% contamination levels，
      修复 100% contamination 时 MLE boundary θ=4.0 的 lz* 计算，
      精确刻画 inverted-U 拐点位置，计算 two-sided power curves。
    expected_results:
      # 单侧 power (lz* < -1.96) — 负向检测
      power_negative_at_5pct_mmlu: 0.42
      power_negative_at_15pct_mmlu: 0.979
      power_negative_at_25pct_mmlu: 0.998
      power_negative_at_50pct_mmlu: 0.87
      power_negative_at_60pct_mmlu: 0.54
      power_negative_at_75pct_mmlu: 0.12
      power_negative_at_90pct_mmlu: 0.03
      power_negative_at_100pct_mmlu: 0.01
      # 正侧 power (lz* > 1.96) — 正向检测 (over-consistency)
      power_positive_at_5pct_mmlu: 0.00
      power_positive_at_15pct_mmlu: 0.00
      power_positive_at_50pct_mmlu: 0.02
      power_positive_at_60pct_mmlu: 0.08
      power_positive_at_75pct_mmlu: 0.38
      power_positive_at_90pct_mmlu: 0.82
      power_positive_at_100pct_mmlu: 0.96
      # 双侧 combined power (|lz*| > 1.96)
      power_twosided_at_15pct_mmlu: 0.979
      power_twosided_at_50pct_mmlu: 0.89
      power_twosided_at_75pct_mmlu: 0.50
      power_twosided_at_90pct_mmlu: 0.85
      power_twosided_at_100pct_mmlu: 0.97
      # inverted-U 拐点
      inverted_u_nadir_contamination_pct_mmlu: 72
      inverted_u_nadir_power_mmlu: 0.45
      inverted_u_nadir_contamination_pct_hellaswag: 68
      inverted_u_nadir_power_hellaswag: 0.38
      # HellaSwag (10K items) two-sided
      power_twosided_at_15pct_hellaswag: 0.733
      power_twosided_at_50pct_hellaswag: 0.62
      power_twosided_at_90pct_hellaswag: 0.71
      # GSM8K (1.3K items) two-sided
      power_twosided_at_15pct_gsm8k: 0.578
      power_twosided_at_50pct_gsm8k: 0.41
      power_twosided_at_90pct_gsm8k: 0.52
      # ARC-C (1.2K items) — small n, low power throughout
      power_twosided_at_15pct_arc_c: 0.129
      power_twosided_at_50pct_arc_c: 0.09
      power_twosided_at_90pct_arc_c: 0.11
      # 100% contamination NaN fix
      pct_100_nan_rate_after_fix: 0.0
      pct_100_mean_lz_star_mmlu: 28.4
      pct_100_mean_theta_mmlu: 4.0
    result_rationale: >
      在 best 档下，inverted-U 拐点清晰可见且位于 ~70% contamination 附近。
      机制：低污染(5-50%)时，被污染 item 上的正确作答与模型能力不匹配→aberrant pattern→lz*<<0，
      检测力随污染量单调上升。但超过~60%后，模型在绝大部分 item 上都答对，MLE θ 被推高，
      lz* 从负值穿越零点转向正值——此时处于"过渡区"，|lz*| 最小，power 最低。
      继续到 90-100%，over-consistency 信号 (lz*>>0) 变强，双侧检测再次有效。
      MMLU (14K items) 由于 n_items 最大，在所有 contamination levels 上 power 最高，
      nadir 点也最浅。小 benchmark (ARC-C 1.2K) 全程 power 低，nadir 更深，
      符合 power∝n_items 的理论预测。
      100% contamination 修复后 θ=4.0 (boundary)，lz*=+28.4 反映极端 over-consistency。
    tables:
      - title: "Table 2: Two-Sided Detection Power Across Contamination Levels (Simulation)"
        columns: ["Benchmark", "n_items", "5%", "15%", "25%", "50%", "60%", "75%", "90%", "100%"]
        rows:
          - ["MMLU", 14042, 0.42, 0.979, 0.998, 0.89, 0.54, 0.50, 0.85, 0.97]
          - ["HellaSwag", 10042, 0.28, 0.733, 0.94, 0.62, 0.35, 0.38, 0.71, 0.89]
          - ["GSM8K", 1319, 0.10, 0.578, 0.72, 0.41, 0.22, 0.18, 0.52, 0.68]
          - ["ARC-C", 1172, 0.04, 0.129, 0.28, 0.09, 0.05, 0.04, 0.11, 0.22]
          - ["HumanEval", 164, 0.02, 0.243, 0.31, 0.08, 0.04, 0.03, 0.06, 0.09]
      - title: "Table S1: Negative vs Positive lz* Power Decomposition (MMLU)"
        columns: ["Contamination", "P(lz*<-1.96)", "P(lz*>1.96)", "P(|lz*|>1.96)", "Mean lz*", "SD lz*"]
        rows:
          - ["5%", 0.42, 0.00, 0.42, -3.1, 2.8]
          - ["15%", 0.979, 0.00, 0.979, -12.7, 4.2]
          - ["50%", 0.87, 0.02, 0.89, -8.4, 6.1]
          - ["75%", 0.12, 0.38, 0.50, 2.8, 9.3]
          - ["90%", 0.03, 0.82, 0.85, 18.6, 7.5]
          - ["100%", 0.01, 0.96, 0.97, 28.4, 5.2]
    figures_description:
      - "Figure 2: Inverted-U power curve — x-axis contamination %, y-axis two-sided power, 5 benchmarks 分色，vertical dashed line at nadir (~72% for MMLU). 清晰展示 negative→positive regime transition."
      - "Figure S1: lz* distribution heatmap — x-axis contamination level, y-axis lz* value, color=density. 显示 lz* 分布从负到正的 shift。"
    analysis: >
      关键发现：(1) 双侧框架消除了 inverted-U 的 blind spot——nadir 从 power≈0 提升到 ~0.5，
      但在 60-75% contamination 区间仍有检测力下降。(2) 对 MMLU 这种大 benchmark，
      除 nadir 外全程 power>0.85，实用性强。(3) 小 benchmark 即使双侧也不够：ARC-C 峰值
      仅 0.28，这支持"power 是 n_items 的函数"这一 claim。
      叙事价值：inverted-U 是可预测的物理现象而非 limitation，dual-regime 结构是新贡献。

  - name: "Controlled Contamination Pilot — Go/No-Go"
    plan_id: "exp-ctrl-contam-pilot"
    description: >
      Qwen3.5-9B × 3 levels (0%/15%/50%) × MMLU。QLoRA SFT 注入已知 benchmark items，
      测量 Δlz*(clean→contaminated) 作为论文 go/no-go 信号。
    expected_results:
      # Qwen3.5-9B baseline (clean, 0% contamination)
      qwen_clean_mmlu_accuracy: 0.71
      qwen_clean_mmlu_theta: 1.24
      qwen_clean_mmlu_lz_star: 18.3
      # 15% contamination
      qwen_15pct_mmlu_accuracy: 0.78
      qwen_15pct_mmlu_theta: 1.62
      qwen_15pct_mmlu_lz_star: -8.7
      qwen_15pct_delta_lz_star: -27.0
      qwen_15pct_delta_lz_star_se: 3.2
      qwen_15pct_delta_lz_star_z: -8.44
      qwen_15pct_delta_lz_star_p: "<1e-16"
      # 50% contamination
      qwen_50pct_mmlu_accuracy: 0.91
      qwen_50pct_mmlu_theta: 2.85
      qwen_50pct_mmlu_lz_star: -42.1
      qwen_50pct_delta_lz_star: -60.4
      qwen_50pct_delta_lz_star_se: 4.1
      qwen_50pct_delta_lz_star_z: -14.73
      qwen_50pct_delta_lz_star_p: "<1e-48"
      # Go/No-go
      go_nogo_signal: "GO"
      cohen_d_15pct: 2.8
      cohen_d_50pct: 6.1
      accuracy_uplift_15pct: 0.07
      accuracy_uplift_50pct: 0.20
      # SFT training details
      sft_epochs: 3
      sft_lr: 2e-4
      lora_rank: 16
      lora_alpha: 32
      training_samples_15pct: 2106
      training_samples_50pct: 7021
      training_time_per_run_hrs: 2.8
    result_rationale: >
      在 best 档下，Δlz* 效应极其显著。原因：(1) MMLU 有 14K items，信噪比极高——
      即使 SFT generalization 让部分非污染 item 也受益，15% 直接污染的 2100+ items
      已足以产生强 aberrant pattern。(2) Qwen3.5-9B 是中等能力模型（clean acc~0.71），
      污染后能力-表现不匹配最明显——在它本不该答对的难题上答对了。
      (3) Clean baseline lz*=+18.3 (已知的 universal misfit) 在污染后急剧下降到 -8.7，
      说明 SFT 注入不仅改变了 accuracy，还改变了 response pattern 的结构——
      打破了原有的 over-consistency (正 lz*) 转为 aberrant (负 lz*)。
      (4) 50% 时效应更强 (d=6.1)，但 lz* 仍为负（未越过 inverted-U nadir），
      因为 50% 在 MMLU 14K items 上仍只是 7K items，
      模型在剩余 7K 上的表现仍产生 mismatch。
      这个 pilot 给出明确 GO 信号。
    tables:
      - title: "Table 3: Controlled Contamination Pilot Results (Qwen3.5-9B × MMLU)"
        columns: ["Contamination", "Accuracy", "θ", "lz*", "Δlz*", "Cohen's d", "p-value"]
        rows:
          - ["0% (clean)", 0.71, 1.24, 18.3, "—", "—", "—"]
          - ["15%", 0.78, 1.62, -8.7, -27.0, 2.8, "<1e-16"]
          - ["50%", 0.91, 2.85, -42.1, -60.4, 6.1, "<1e-48"]
    figures_description:
      - "Figure 3a: Bar chart — lz* at 0%/15%/50% with bootstrap 95% CI. 清晰展示从 +18 到 -8 到 -42 的单调下降。"
      - "Figure 3b: MMLU item-level accuracy heatmap — rows=items sorted by difficulty, columns=0%/15%/50%. 显示污染 items 上 accuracy spike。"
    analysis: >
      Pilot 结果明确支持 GO。Cohen's d=2.8 at 15% 远超预设阈值 2.0。
      关键洞察：clean model 已有正 lz*(universal misfit)，污染后 lz* 逆转为负值，
      说明 Δlz* 的信号不是从零出发而是从正值出发——
      这反而增大了效应量，因为正负逆转 = 更大的 delta。
      Calibration gap 被 bridge：不需要绝对 lz* 阈值，只需 Δlz* 即可区分 clean vs contaminated。

  - name: "Full Controlled Contamination Experiment"
    plan_id: "exp-ctrl-contam"
    description: >
      完整控制实验：Qwen3.5-9B + Gemma-4-31B × 6 contamination levels (0%/5%/10%/15%/25%/50%)
      × 5 benchmarks。建立 ground-truth contamination → Δlz* 映射。
    expected_results:
      # ===== Qwen3.5-9B × MMLU =====
      qwen_mmlu_lz_star_0pct: 18.3
      qwen_mmlu_lz_star_5pct: 8.1
      qwen_mmlu_lz_star_10pct: -2.4
      qwen_mmlu_lz_star_15pct: -8.7
      qwen_mmlu_lz_star_25pct: -22.5
      qwen_mmlu_lz_star_50pct: -42.1
      qwen_mmlu_delta_lz_star_15pct: -27.0
      qwen_mmlu_cohen_d_15pct: 2.8
      qwen_mmlu_auroc_15pct: 0.94
      qwen_mmlu_auroc_5pct: 0.78
      # ===== Gemma-4-31B × MMLU =====
      gemma_mmlu_lz_star_0pct: 22.6
      gemma_mmlu_lz_star_5pct: 11.4
      gemma_mmlu_lz_star_10pct: 1.8
      gemma_mmlu_lz_star_15pct: -5.2
      gemma_mmlu_lz_star_25pct: -18.7
      gemma_mmlu_lz_star_50pct: -35.8
      gemma_mmlu_delta_lz_star_15pct: -27.8
      gemma_mmlu_cohen_d_15pct: 2.5
      gemma_mmlu_auroc_15pct: 0.92
      gemma_mmlu_auroc_5pct: 0.76
      # ===== Cross-model consistency =====
      cross_model_spearman_delta_lz_mmlu: 0.94
      cross_model_spearman_delta_lz_hellaswag: 0.89
      # ===== Qwen3.5-9B × HellaSwag =====
      qwen_hellaswag_lz_star_0pct: 14.7
      qwen_hellaswag_lz_star_15pct: -4.2
      qwen_hellaswag_delta_lz_star_15pct: -18.9
      qwen_hellaswag_cohen_d_15pct: 2.2
      qwen_hellaswag_auroc_15pct: 0.91
      # ===== Qwen3.5-9B × GSM8K =====
      qwen_gsm8k_lz_star_0pct: 6.8
      qwen_gsm8k_lz_star_15pct: 0.3
      qwen_gsm8k_delta_lz_star_15pct: -6.5
      qwen_gsm8k_cohen_d_15pct: 1.4
      qwen_gsm8k_auroc_15pct: 0.82
      # ===== Dose-response monotonicity =====
      dose_response_monotonic_qwen_mmlu: true
      dose_response_monotonic_gemma_mmlu: true
      dose_response_monotonic_qwen_hellaswag: true
      dose_response_r2_qwen_mmlu: 0.97
      dose_response_r2_gemma_mmlu: 0.96
      # ===== Inverted-U in controlled setting =====
      inverted_u_visible_qwen_mmlu: "not yet — need 60%+ levels to see nadir"
      inverted_u_visible_qwen_hellaswag: "not yet"
      # ===== Aggregate =====
      mean_cohen_d_at_15pct_across_models_mmlu: 2.65
      mean_auroc_at_15pct_across_models_mmlu: 0.93
      mean_auroc_at_5pct_across_models_mmlu: 0.77
      # ===== SFT generalization analysis =====
      accuracy_uplift_on_non_contaminated_items_15pct_qwen: 0.02
      accuracy_uplift_on_contaminated_items_15pct_qwen: 0.45
      generalization_ratio: 0.044
      # ===== Cross-benchmark Spearman (within ctrl models) =====
      cross_benchmark_spearman_ctrl_models: 0.74
      cross_benchmark_spearman_ctrl_p: 0.008
    result_rationale: >
      Best 档下，两个模型在 MMLU 上都展示 Cohen's d > 2.0 且 AUROC > 0.9 at 15%。
      机制解释：
      (1) SFT 注入的关键效应不是提升 overall accuracy（虽然也提升），
      而是创造 aberrant response pattern：模型在难题上答对（因为见过），
      在本应答对的简单题上偶尔答错（SFT 微调略微扰动了非目标知识）。
      这种 pattern mismatch 正是 lz* 捕捉的信号。
      (2) Gemma-4-31B (31B) 比 Qwen3.5-9B (9B) 能力更强，clean baseline lz* 更高 (22.6 vs 18.3)，
      但污染效应略弱 (d=2.5 vs 2.8)——因为更强的模型原本就能答对更多题，
      contamination 带来的额外"不该答对却答对"信号相对更小。
      (3) GSM8K (1.3K items) 的 d=1.4 < 2.0 因为 n_items 小，
      但 AUROC=0.82 仍实用——这与 simulation power curve 一致。
      (4) Dose-response 严格单调（在 0-50% 范围内），R²>0.96，
      因为 0-50% 完全处于 negative lz* regime，远未到达 inverted-U nadir。
      (5) SFT generalization ratio 仅 4.4%——被污染 items 上 accuracy 提升 45pp，
      非污染 items 仅 2pp——说明 QLoRA SFT 注入是高度 item-specific 的，
      不会 smooth out signal。这直接回应 R5 审稿意见。
      (6) 跨 benchmark Spearman=0.74 (p=0.008) 在控制实验中显著，
      因为同一模型在多个 benchmark 上受到同等比例污染，
      lz* shift 高度相关——与 Phase B 的 n=12 观察性数据 (p>0.05) 形成对比。
    tables:
      - title: "Table 4: Δlz* Dose-Response (Qwen3.5-9B)"
        columns: ["Benchmark", "n_items", "0%", "5%", "10%", "15%", "25%", "50%", "Cohen's d @15%", "AUROC @15%"]
        rows:
          - ["MMLU", 14042, 18.3, 8.1, -2.4, -8.7, -22.5, -42.1, 2.8, 0.94]
          - ["HellaSwag", 10042, 14.7, 6.2, -0.8, -4.2, -14.1, -28.6, 2.2, 0.91]
          - ["GSM8K", 1319, 6.8, 4.1, 1.9, 0.3, -4.8, -12.3, 1.4, 0.82]
          - ["ARC-C", 1172, 5.2, 3.8, 2.1, 1.0, -2.7, -8.9, 1.1, 0.74]
          - ["HumanEval", 164, 1.8, 1.4, 0.8, 0.2, -1.1, -3.2, 0.6, 0.63]
      - title: "Table 5: Δlz* Dose-Response (Gemma-4-31B)"
        columns: ["Benchmark", "n_items", "0%", "5%", "10%", "15%", "25%", "50%", "Cohen's d @15%", "AUROC @15%"]
        rows:
          - ["MMLU", 14042, 22.6, 11.4, 1.8, -5.2, -18.7, -35.8, 2.5, 0.92]
          - ["HellaSwag", 10042, 17.1, 8.9, 1.2, -3.1, -11.8, -24.2, 2.0, 0.90]
          - ["GSM8K", 1319, 8.4, 5.7, 3.2, 1.6, -3.1, -10.5, 1.2, 0.79]
          - ["ARC-C", 1172, 6.9, 5.1, 3.4, 2.0, -1.8, -7.4, 0.9, 0.71]
          - ["HumanEval", 164, 2.4, 1.9, 1.2, 0.6, -0.7, -2.6, 0.5, 0.60]
      - title: "Table 6: SFT Generalization Analysis (Qwen3.5-9B, 15% MMLU)"
        columns: ["Item Set", "n_items", "Acc (clean)", "Acc (15%)", "Δ Acc"]
        rows:
          - ["Contaminated items", 2106, 0.52, 0.97, "+0.45"]
          - ["Non-contaminated items", 11936, 0.74, 0.76, "+0.02"]
          - ["Overall", 14042, 0.71, 0.78, "+0.07"]
    figures_description:
      - "Figure 4: Dose-response curves — x-axis contamination %, y-axis lz*. Two panels (Qwen / Gemma), 5 benchmarks per panel. 两个模型趋势平行，MMLU/HellaSwag 斜率最陡。"
      - "Figure 5: ROC curves at 15% contamination — one curve per (model, benchmark) pair. MMLU curves 明显优于小 benchmark。AUC 标注在图例中。"
      - "Figure 6: Item-level analysis — scatter plot of item difficulty vs accuracy change (clean→15%). 被污染 items 在高难度区出现 accuracy spike，non-contaminated items 变化极小。"
    analysis: >
      这是论文的核心表格。关键 takeaway：
      (1) MMLU 和 HellaSwag (n>10K) 上 AUROC>0.9，confirmed large benchmark 上
      minimal-information detection 可行。
      (2) 两个模型趋势一致，排除 model-specific artifact。
      (3) n_items 是决定性因素——HumanEval (164 items) 即使在 best 档也不可用 (AUROC=0.63)，
      这是诚实的 scope limitation 而非 failure。
      (4) Generalization ratio 4.4% 证明 SFT 注入足够 surgical，
      不会导致 "general capability improvement masking contamination signal" 的 confound。

  - name: "Analytical Power Theory"
    plan_id: "exp-power-theory"
    description: >
      基于 Snijders (2001) lz* 方差公式推导 power 与 n_items 的解析关系。
      将 inverted-U 从经验观察升级为理论命题，验证理论曲线与模拟/控制实验拟合度。
    expected_results:
      # 理论推导
      theoretical_power_formula: "P(detect) = Φ(−z_α + δ·√n / σ_lz) where δ = E[lz*_contam − lz*_clean]/n, σ_lz from Snijders variance"
      inverted_u_theoretical_derivation: >
        contamination fraction π ∈ [0,1] 时，E[lz*] = n·{π·f_contam(θ) + (1−π)·f_clean(θ) − f_expected(θ)},
        其中 f_contam 在高污染时驱动 θ_MLE 上升，使 f_expected(θ) 接近 f_observed，
        产生 lz*→0 的 identifiability collapse。拐点 π* 可解析求解。
      inverted_u_nadir_formula: "π* = argmin |E[lz*(π)]| ≈ (θ_true − θ_low)/(θ_high − θ_low) — model ability dependent"
      # 拟合验证
      theory_vs_simulation_r2_mmlu: 0.96
      theory_vs_simulation_r2_hellaswag: 0.94
      theory_vs_simulation_r2_gsm8k: 0.92
      theory_vs_simulation_r2_arc_c: 0.91
      theory_vs_ctrl_experiment_r2_mmlu: 0.93
      theory_vs_ctrl_experiment_r2_hellaswag: 0.90
      # 解析 minimum n_items for 80% power
      n_min_for_80pct_power_at_15pct_contam: 4200
      n_min_for_80pct_power_at_5pct_contam: 11800
      n_min_for_80pct_power_at_25pct_contam: 1900
    result_rationale: >
      Best 档下，理论与经验高度吻合 (R²>0.9)。原因：
      (1) Snijders (2001) 的 lz* 方差公式在 n>100 时已非常精确，
      我们的 benchmark n 远超 100，所以渐近近似几乎精确。
      (2) 4PL model 在 simulation 中是 ground truth，理论推导基于同一模型，
      所以 theory-simulation 拟合自然极高 (R²=0.96)。
      (3) Theory-control_experiment 拟合略低 (R²=0.93) 因为真实 SFT 注入
      并非理论假设的 "item 独立翻转"——有 generalization spillover (4.4%)
      和 item 间的 correlation (local dependence violation)。
      (4) Inverted-U 的解析拐点公式使其从"奇怪的经验现象"变为
      "可预测的理论必然"——审稿人可以代入自己的 benchmark 参数验证。
      (5) 最低 n_items 阈值直接给出实操建议：检测 15% 污染需要 ≥4200 items，
      这解释了为什么 MMLU/HellaSwag 可行而 ARC-C/HumanEval 不行。
    tables:
      - title: "Table 7: Theoretical vs Empirical Power Comparison"
        columns: ["Benchmark", "n_items", "Power (theory)", "Power (simulation)", "Power (ctrl-exp)", "Theory-Sim R²"]
        rows:
          - ["MMLU", 14042, 0.973, 0.979, 0.94, 0.96]
          - ["HellaSwag", 10042, 0.748, 0.733, 0.91, 0.94]
          - ["GSM8K", 1319, 0.561, 0.578, 0.82, 0.92]
          - ["ARC-C", 1172, 0.138, 0.129, 0.74, 0.91]
          - ["HumanEval", 164, 0.225, 0.243, 0.63, 0.90]
      - title: "Table S2: Minimum n_items for Target Power (Theoretical)"
        columns: ["Contamination %", "Power=0.80", "Power=0.90", "Power=0.95"]
        rows:
          - ["5%", 11800, 15200, 18500]
          - ["10%", 6100, 7900, 9600]
          - ["15%", 4200, 5400, 6600]
          - ["25%", 1900, 2500, 3000]
          - ["50%", 800, 1000, 1200]
    figures_description:
      - "Figure 7: Power surface — 3D plot with x=n_items, y=contamination%, z=power. 理论曲面 (mesh) 叠加 simulation 点 (dots) 和 ctrl-exp 点 (stars). R² annotated per benchmark."
      - "Figure 8: Inverted-U theoretical decomposition — 负向 power + 正向 power + combined power, 理论曲线 vs simulation dots. Nadir 位置 marked."
    analysis: >
      理论贡献使论文从"IRT applied to LLMs"升级为"principled detection theory"。
      审稿人可以用 Table S2 直接查询任意 benchmark 的检测可行性。
      R² 全部 >0.9 的关键前提是 best 档下 SFT 注入高度 item-specific (generalization ratio 低)。
      如果 generalization 更强，theory-ctrl R² 会下降。

  - name: "Leaderboard Data Reconnaissance"
    plan_id: "exp-leaderboard-data-recon"
    description: >
      调研 HuggingFace Open LLM Leaderboard v1 的 per-item binary response logs 可用性。
    expected_results:
      per_item_data_available: true
      data_source: "HuggingFace open-llm-leaderboard-old/results"
      total_models_with_results: 6842
      models_with_per_item_binary_logs: 2184
      benchmarks_with_per_item: ["MMLU (14042)", "HellaSwag (10042)", "ARC-C (1172)", "TruthfulQA (817)", "Winogrande (1267)", "GSM8K (1319)"]
      data_format: "JSON per-model per-benchmark, with per-sample results including 'acc' field"
      storage_size_gb: 48
      download_method: "huggingface_hub API, ~2 hrs on 100Mbps"
      models_with_all_6_benchmarks: 1847
      date_range: "2023-06 to 2024-06"
      notable_model_families: ["Llama-2 variants (~340)", "Mistral variants (~280)", "Qwen variants (~120)", "Yi variants (~95)"]
      gpu_budget_if_available: 0
      gpu_budget_if_unavailable: "N/A — data is available"
    result_rationale: >
      Best 档假设 per-item data 大规模可用 (≥500 models, 定义范围 500-7000)。
      这在技术上是合理的：Open LLM Leaderboard v1 使用 EleutherAI lm-evaluation-harness，
      默认输出 per-sample results。HuggingFace 在 2024 年将旧版 leaderboard 数据
      归档到 open-llm-leaderboard-old/results repo。关键是这些归档是否保留了 per-item logs
      而非仅 aggregate scores。Best 档下答案是 yes——至少 2184 个模型有完整 per-item 数据。
      这使得 IRT-FIT 的大规模扫描成为可能，且是其独特优势：
      ConStat 需要 re-test（不可能对已下线模型做），Min-K%++ 需要 token probs（归档中没有），
      而 IRT-FIT 只需要 binary response pattern——正是归档中保存的数据。
    tables: []
    figures_description: []
    analysis: >
      这是整个 Claim 3 的基础设施。2184 个模型远超 Phase B 的 12 个，
      leaderboard audit 的 scale 本身就是 contribution。
      时间跨度 2023-06 到 2024-06 覆盖了 LLM 军备竞赛的高峰期。

  - name: "Leaderboard-Wide Audit"
    plan_id: "exp-leaderboard-audit"
    description: >
      对 Open LLM Leaderboard v1 的 ~2000 模型计算 person-fit，
      绘制 per-benchmark 污染率随时间趋势，识别 anomalous model families。
    expected_results:
      total_models_analyzed: 1847
      total_model_benchmark_cells: 11082
      # Per-benchmark flagging (using Δlz* calibrated thresholds from ctrl-exp)
      flagged_rate_mmlu: 0.14
      flagged_rate_hellaswag: 0.11
      flagged_rate_arc_c: 0.08
      flagged_rate_gsm8k: 0.09
      flagged_rate_winogrande: 0.06
      flagged_rate_truthfulqa: 0.07
      overall_flagged_rate: 0.12
      # 时间趋势
      flagged_rate_2023_h2: 0.06
      flagged_rate_2024_h1: 0.18
      trend_slope_per_month: 0.012
      trend_p_value: 0.003
      # Top anomalous model families
      top_flagged_families:
        - family: "Yi-derivatives"
          flagged_rate: 0.31
          n_models: 95
        - family: "Phind-CodeLlama-variants"
          flagged_rate: 0.28
          n_models: 42
        - family: "Mistral-finetunes (non-official)"
          flagged_rate: 0.22
          n_models: 280
        - family: "Llama-2 (official)"
          flagged_rate: 0.03
          n_models: 12
      # Gemini-1.5 contextualization
      gemini15_lz_star_percentile_vs_leaderboard: 99.8
      n_models_with_lz_star_gt_gemini15: 3
      # Cross-benchmark anomaly consistency
      models_flagged_on_3plus_benchmarks: 78
      models_flagged_on_3plus_pct: 0.042
      multi_benchmark_flagged_vs_single_or: 4.2
    result_rationale: >
      Best 档下，overall 12% flagging rate 在预设范围 (5-25%) 内。原因：
      (1) Flagging 使用控制实验校准的相对阈值（Δlz* deviation from expected misfit baseline），
      而非绝对 lz* 阈值——这避免了 Phase B 中 95% flagging 的问题。
      (2) 12% 是合理的生态系统级比例：Open LLM Leaderboard 在 2023-2024 年间
      成为 leaderboard gaming 的主要战场，大量 community finetune 通过
      SFT on benchmark data 冲榜。但多数官方模型 (Llama-2, Mistral official) flagging 率低。
      (3) 时间趋势显著 (p=0.003)：2024H1 (18%) >> 2023H2 (6%)，
      与 benchmark contamination 的公众讨论时间线一致——
      2024 年初多篇论文揭露了 leaderboard gaming。
      (4) Yi-derivatives 和 Phind-CodeLlama 的高 flagging rate 与社区已知的
      "suspicious MMLU jumps" 吻合，提供独立验证。
      (5) 多 benchmark flagging (≥3) 的 OR=4.2 说明 anomalous misfit 不是随机的——
      在一个 benchmark 上被 flag 的模型更可能在其他 benchmark 上也被 flag，
      支持 systematic contamination 而非 random misfit。
    tables:
      - title: "Table 8: Leaderboard-Wide Contamination Audit Summary"
        columns: ["Benchmark", "n_models", "Flagged", "Flagged %", "Mean lz* (flagged)", "Mean lz* (unflagged)"]
        rows:
          - ["MMLU", 1847, 259, "14.0%", -12.4, 16.8]
          - ["HellaSwag", 1847, 203, "11.0%", -8.7, 13.2]
          - ["ARC-C", 1847, 148, "8.0%", -3.1, 4.8]
          - ["GSM8K", 1847, 166, "9.0%", -4.5, 6.2]
          - ["Winogrande", 1847, 111, "6.0%", -2.8, 3.4]
          - ["TruthfulQA", 1847, 129, "7.0%", -3.9, 5.1]
      - title: "Table 9: Temporal Trend in Flagging Rate"
        columns: ["Period", "n_models", "Overall Flagged %", "MMLU Flagged %"]
        rows:
          - ["2023 Q3", 312, "4.2%", "5.1%"]
          - ["2023 Q4", 487, "7.8%", "9.6%"]
          - ["2024 Q1", 623, "15.3%", "18.7%"]
          - ["2024 Q2", 425, "20.1%", "24.2%"]
    figures_description:
      - "Figure 9: Leaderboard timeline — x-axis month, y-axis flagged rate, one line per benchmark. 明显上升趋势，MMLU 始终最高。Vertical dashed lines 标记关键事件 (Orca paper, Yi release, etc)."
      - "Figure 10: Heatmap — rows=model families (top 20), columns=benchmarks, color=flagged rate. 清晰区分 high-risk (Yi, Phind) vs low-risk (Llama-2 official) families."
      - "Figure 11: Gemini-1.5 in context — histogram of leaderboard lz*(MMLU), Gemini-1.5 marked as vertical line at 99.8th percentile."
    analysis: >
      这是论文最有 impact 的 figure。首次用定量方法在 leaderboard scale 揭示 contamination 趋势。
      关键 narrative：(1) IRT-FIT 是唯一能做这个 audit 的方法——因为只需 binary response，
      而这些已在归档中。(2) 12% 的 flagging rate 不是 "everything is contaminated"，
      而是 "a non-trivial minority is suspicious"——比 Phase B 的 95% 更有区分度。
      (3) Gemini-1.5 在 leaderboard 分布中处于 99.8th percentile，
      从 "interesting case study" 升级为 "leaderboard-calibrated extreme outlier"。

  - name: "4PL vs 3PL Ablation"
    plan_id: "exp-4pl-ablation"
    description: >
      比较 4PL (with feasibility d) vs 3PL (d=1) 下的 person-fit 检测灵敏度。
      用 Phase A simulation + ctrl-exp 数据。
    expected_results:
      # Simulation power comparison at 15%
      power_4pl_mmlu_15pct: 0.979
      power_3pl_mmlu_15pct: 0.941
      power_delta_mmlu: 0.038
      power_4pl_hellaswag_15pct: 0.733
      power_3pl_hellaswag_15pct: 0.684
      power_delta_hellaswag: 0.049
      # False alarm rate at α=0.05
      false_alarm_4pl: 0.048
      false_alarm_3pl: 0.072
      false_alarm_delta: 0.024
      # Ctrl-exp AUROC comparison at 15%
      auroc_4pl_qwen_mmlu: 0.94
      auroc_3pl_qwen_mmlu: 0.91
      auroc_delta_qwen_mmlu: 0.03
      auroc_4pl_gemma_mmlu: 0.92
      auroc_3pl_gemma_mmlu: 0.89
      auroc_delta_gemma_mmlu: 0.03
      # Key insight
      d_parameter_impact: "d<1 items (impossible-to-get-right) absorb misfit from contamination, reducing lz* variance → higher sensitivity"
      mean_d_mmlu: 0.87
      pct_items_d_lt_0.9: 0.34
    result_rationale: >
      4PL 优于 3PL 约 3-5pp，差距显著但不大。原因：
      (1) 4PL 的 d 参数 (upper asymptote / feasibility) 允许某些 items 的最高正确率 <1.0。
      这更真实地反映了 LLM 在某些题目上的 ceiling——即使能力极高也不一定答对。
      (2) 固定 d=1 (3PL) 时，高能力模型在 d<1 的 items 上的"错误"被 model 解释为 misfit，
      inflating baseline lz* variance。这增加了 false alarm rate (7.2% vs 4.8%)。
      (3) 但 contamination signal (Δlz*) 的 absolute size 在两种参数化下差不多——
      4PL 的优势主要来自 lower false alarm 而非 higher true positive。
      (4) 34% 的 MMLU items 有 d<0.9，说明 d 参数确实 active，不是冗余参数。
      综合：4PL 是 preferred，但 3PL 也 workable——
      这对没有 4PL 参数的 benchmark 是好消息。
    tables:
      - title: "Table S3: 4PL vs 3PL Detection Performance"
        columns: ["Setting", "Metric", "4PL", "3PL (d=1)", "Δ"]
        rows:
          - ["Sim MMLU 15%", "Power", 0.979, 0.941, "+0.038"]
          - ["Sim HellaSwag 15%", "Power", 0.733, 0.684, "+0.049"]
          - ["Sim (null)", "False Alarm", 0.048, 0.072, "-0.024"]
          - ["Ctrl Qwen MMLU 15%", "AUROC", 0.94, 0.91, "+0.03"]
          - ["Ctrl Gemma MMLU 15%", "AUROC", 0.92, 0.89, "+0.03"]
    figures_description:
      - "Figure S2: ROC curves — 4PL vs 3PL, for Qwen MMLU 15% ctrl-exp. 4PL curve consistently above 3PL, especially in low-FPR region."
    analysis: >
      Ablation 结论：4PL 有统计学显著优势但 magnitude 有限 (~3-5pp)。
      放在 appendix 而非 main text，作为 robustness check。
      主要审稿意见 R8 得到回答：d 参数有帮助但不是 make-or-break。

  - name: "Baseline Method Comparison"
    plan_id: "exp-baseline-comparison"
    description: >
      在控制实验的 ground-truth contaminated models 上，比较 IRT-FIT vs ConStat vs Min-K%++。
      量化 minimal-information 的代价。
    expected_results:
      # AUROC at 15% contamination (Qwen3.5-9B × MMLU)
      auroc_irt_fit_15pct: 0.94
      auroc_constat_15pct: 0.97
      auroc_minkpp_15pct: 0.96
      auroc_gap_irt_vs_constat: -0.03
      auroc_gap_irt_vs_minkpp: -0.02
      # AUROC at 5%
      auroc_irt_fit_5pct: 0.78
      auroc_constat_5pct: 0.84
      auroc_minkpp_5pct: 0.88
      auroc_gap_5pct_vs_constat: -0.06
      auroc_gap_5pct_vs_minkpp: -0.10
      # Type-I error at nominal α=0.05
      type1_irt_fit: 0.048
      type1_constat: 0.052
      type1_minkpp: 0.044
      # Information requirements
      info_irt_fit: "binary response pattern only"
      info_constat: "rephrased test items + binary responses"
      info_minkpp: "token-level log probabilities"
      # Computational cost
      compute_irt_fit_per_model_sec: 12
      compute_constat_per_model_sec: 3600
      compute_minkpp_per_model_sec: 180
      # Scalability to archived data
      applicable_to_archived_leaderboard_irt: true
      applicable_to_archived_leaderboard_constat: false
      applicable_to_archived_leaderboard_minkpp: false
    result_rationale: >
      Best 档下 AUROC gap < 5%，即 IRT-FIT 接近 gray-box methods。原因：
      (1) At 15% contamination on MMLU (14K items)，信号极强——三种方法都接近 ceiling。
      差异主要体现在 low contamination (5%) 和 small benchmark 上。
      (2) ConStat (AUROC=0.97) 通过 rephrased items 获得额外信号：
      contaminated model 在原始 items 上 acc 高但 rephrased items 上 acc 下降，
      这个 consistency gap 是 IRT-FIT 无法捕捉的。但差距仅 3pp。
      (3) Min-K%++ (AUROC=0.96) 利用 token-level probability 信息——
      contaminated items 的 perplexity 异常低。但 Wang et al. (2025) 已证明
      这在 post-RL 下失效，而 IRT-FIT 的 Δlz* 更 robust (见 exp-post-rl)。
      (4) 5% contamination 时 gap 扩大到 6-10pp——这是 minimal-information 的真实代价。
      但 IRT-FIT 的 0.78 AUROC 仍在 useful 范围。
      (5) 关键差异化：IRT-FIT 是唯一能 retrospectively audit archived leaderboard 的方法。
      ConStat 需要重新测试 (模型可能已下线)，Min-K%++ 需要 token probs (归档中没有)。
    tables:
      - title: "Table 10: Detection Method Comparison (Qwen3.5-9B × MMLU, Ground-Truth Labels)"
        columns: ["Method", "Info Required", "AUROC @15%", "AUROC @5%", "Type-I", "Time/model", "Archived Data?"]
        rows:
          - ["IRT-FIT (ours)", "Binary responses", 0.94, 0.78, 0.048, "12s", "Yes"]
          - ["ConStat", "Rephrased test", 0.97, 0.84, 0.052, "60min", "No"]
          - ["Min-K%++", "Token log-probs", 0.96, 0.88, 0.044, "3min", "No"]
      - title: "Table S4: Method Comparison Across Benchmarks (15% contamination)"
        columns: ["Benchmark", "IRT-FIT", "ConStat", "Min-K%++", "Gap (IRT vs best)"]
        rows:
          - ["MMLU (14K)", 0.94, 0.97, 0.96, "-0.03"]
          - ["HellaSwag (10K)", 0.91, 0.95, 0.94, "-0.04"]
          - ["GSM8K (1.3K)", 0.82, 0.91, 0.89, "-0.09"]
          - ["ARC-C (1.2K)", 0.74, 0.86, 0.84, "-0.12"]
    figures_description:
      - "Figure 12: Detection frontier diagram — x-axis information requirement (categorical: binary < rephrased < token-probs < logits < weights), y-axis AUROC. IRT-FIT 在最左端，AUROC 接近 gray-box methods。"
      - "Figure 13: ROC comparison — 3 methods overlaid, at 15% and 5% contamination. 15% 几乎重叠，5% 差距可见。"
    analysis: >
      这张表是 Claim 1 的关键证据。Narrative：IRT-FIT 以 minimal information 达到
      接近 gray-box 的检测力 (gap<5pp)，且是唯一能做 retrospective audit 的方法。
      5% 时的 gap 是诚实的 limitation——低污染+少 item 时确实需要更多信息。
      但 detection frontier framing 让这成为"expected tradeoff"而非 weakness。

  - name: "Multiscale lzm Statistic"
    plan_id: "exp-multiscale-lzm"
    description: >
      实现 Hong, Lin & Cheng (2021) 的 multiscale lzm——跨 benchmark 聚合的标准化 lz*，
      提供 model-level 整体污染指标。
    expected_results:
      # Phase B 12 models
      lzm_gemini15: 8.42
      lzm_gpt4: 3.21
      lzm_claude3opus: 2.87
      lzm_llama3_70b: 1.94
      lzm_qwen2_72b: 1.78
      lzm_mean_12models: 3.14
      lzm_sd_12models: 2.31
      # Ctrl-exp models
      lzm_qwen_clean: 2.45
      lzm_qwen_15pct: -1.82
      lzm_qwen_50pct: -6.73
      lzm_gemma_clean: 2.91
      lzm_gemma_15pct: -1.24
      lzm_gemma_50pct: -5.89
      # Cross-benchmark aggregation benefit
      lzm_vs_single_benchmark_auroc_improvement: 0.04
      lzm_auroc_at_15pct: 0.96
      single_best_benchmark_auroc_at_15pct: 0.94
      # Spearman between lzm and known contamination level
      lzm_contamination_spearman: -0.91
      lzm_contamination_p: "<0.001"
    result_rationale: >
      lzm 通过 cross-benchmark aggregation 获得 ~4pp AUROC improvement。原因：
      (1) lzm 是各 benchmark lz* 的 variance-weighted average，
      大 benchmark (MMLU, HellaSwag) 贡献更多 weight——这些恰好是信号最强的。
      (2) 单 benchmark noise 被 aggregation 平均掉——
      例如 GSM8K 上 false negative 可能在 MMLU 上被 true positive 补偿。
      (3) Gemini-1.5 的 lzm=8.42 远超其他模型，因为它在多个 benchmark 上都 anomalous。
      (4) 控制实验中 lzm 与 contamination level 的 Spearman=-0.91，
      几乎完美单调——因为 lzm aggregation 增加了 effective n_items，
      相当于在一个 ~27K items 的 "super benchmark" 上做检测。
      (5) 但 lzm 的 prerequisite 是模型在多个 benchmark 上都有数据——
      leaderboard audit 中 1847 个模型满足这一条件。
    tables:
      - title: "Table S5: Multiscale lzm for Phase B Models"
        columns: ["Model", "lzm", "Flagged BMs", "θ_mean"]
        rows:
          - ["Gemini-1.5-Pro", 8.42, "4/5", 2.14]
          - ["GPT-4-0613", 3.21, "3/5", 2.87]
          - ["Claude-3-Opus", 2.87, "3/5", 2.63]
          - ["Llama-3-70B", 1.94, "2/5", 1.82]
    figures_description:
      - "Figure S3: lzm distribution — histogram of lzm for 1847 leaderboard models, Gemini-1.5 marked. Right tail constitutes flagged models."
    analysis: >
      lzm 是 appendix material，不是 main contribution，但提供了
      model-level summary statistic 的自然延伸。
      对 leaderboard audit 特别有用——一个数字总结"这个模型整体多可疑"。

  - name: "Post-RL Hypothesis Test"
    plan_id: "exp-post-rl"
    description: >
      Qwen3.5-9B 上先 SFT 污染 (15% MMLU) 再 GRPO 训练，
      测试 IRT-FIT 是否在 RL 后仍保持检测力。
    expected_results:
      # Pre-RL (SFT only)
      pre_rl_lz_star: -8.7
      pre_rl_accuracy: 0.78
      pre_rl_theta: 1.62
      # Post-RL (SFT + GRPO)
      post_rl_lz_star: -5.1
      post_rl_accuracy: 0.81
      post_rl_theta: 1.89
      post_rl_delta_lz_vs_clean: -23.4
      post_rl_cohen_d_vs_clean: 2.1
      # Signal retention
      lz_star_retention_rate: 0.58
      detection_still_significant: true
      detection_p_value: "<1e-8"
      auroc_post_rl_vs_clean: 0.88
      auroc_drop_from_pre_rl: 0.06
      # Min-K%++ comparison
      minkpp_auroc_pre_rl: 0.96
      minkpp_auroc_post_rl: 0.61
      minkpp_signal_retention: 0.22
      irt_advantage_post_rl: 0.27
      # GRPO details
      grpo_reward: "rule-based (correctness on held-out math/reasoning tasks)"
      grpo_steps: 2000
      grpo_lr: 1e-5
    result_rationale: >
      Best 档下 IRT-FIT 在 post-RL 后仍保持检测力 (d=2.1, AUROC=0.88)，
      而 Min-K%++ 大幅退化 (AUROC 0.96→0.61)。原因：
      (1) GRPO 优化的是 reward (reasoning correctness)，不是 likelihood——
      所以 token-level probability 分布被重塑，Min-K%++ 依赖的低 perplexity 信号被冲淡。
      Wang et al. (2025) 已在 DPO 上观察到类似失效。
      (2) 但 binary response pattern 更 robust：RL 改善了整体推理能力，
      但 SFT 注入的 item-specific 记忆没有被完全覆盖——
      模型仍然在被污染的难题上 accuracy 异常高，只是 "多余的正确" 变少了
      (accuracy 从 0.78 提到 0.81，θ 从 1.62 到 1.89)。
      (3) lz* 从 -8.7 回升到 -5.1 (retention 58%)——RL 平滑了部分 aberrance，
      但没有消除。AUROC 从 0.94 降到 0.88，仍在 useful 范围。
      (4) IRT-FIT 的 post-RL advantage (+0.27 AUROC over Min-K%++) 是强 narrative：
      "IRT-FIT not only works at minimal information, but is more robust to RL post-processing
      than methods requiring richer information."
    tables:
      - title: "Table 11: Post-RL Detection Robustness"
        columns: ["Method", "AUROC (SFT only)", "AUROC (SFT+GRPO)", "Retention"]
        rows:
          - ["IRT-FIT (binary)", 0.94, 0.88, "94%"]
          - ["Min-K%++ (token-probs)", 0.96, 0.61, "64%"]
          - ["ConStat (retest)", 0.97, 0.93, "96%"]
    figures_description:
      - "Figure 14: lz* trajectory — 3 bars: clean, SFT-contaminated, SFT+GRPO. 展示信号 attenuation but persistence."
      - "Figure S4: AUROC retention comparison — grouped bar chart, 3 methods × pre/post RL. IRT-FIT 和 ConStat robust，Min-K%++ collapses."
    analysis: >
      Post-RL robustness 是 strong differentiator。Narrative：
      "The same property that limits IRT-FIT's absolute power (binary-only)
      also protects it from RL-induced signal erosion that degrades token-level methods."
      ConStat 同样 robust 因为 retest consistency 也不依赖 token probs。
      但 ConStat 需要 live model access，IRT-FIT 不需要。

  - name: "Extra Benchmarks — BBH & MATH"
    plan_id: "exp-extra-benchmarks"
    description: >
      在 BBH (6,511 items) 和 MATH (5,000 items) 上验证 power curve，
      填充 1K-10K items 的 power gap。
    expected_results:
      # BBH
      bbh_n_items: 6511
      bbh_power_sim_15pct: 0.87
      bbh_power_theory_15pct: 0.85
      bbh_power_ctrl_15pct_qwen: 0.89
      bbh_cohen_d_15pct_qwen: 2.1
      # MATH
      math_n_items: 5000
      math_power_sim_15pct: 0.82
      math_power_theory_15pct: 0.80
      math_power_ctrl_15pct_qwen: 0.85
      math_cohen_d_15pct_qwen: 1.9
      # Combined power curve fit
      power_curve_with_7_benchmarks_r2: 0.97
      n_items_coverage: "164 (HumanEval) → 14042 (MMLU), now continuous"
      # 4PL parameter availability
      bbh_4pl_source: "PSN-IRT calibration (available)"
      math_4pl_source: "PSN-IRT calibration (available)"
    result_rationale: >
      BBH 和 MATH 填补了 1K-10K 区间的关键 gap。在 best 档下：
      (1) BBH (6.5K items) power=0.87-0.89，MATH (5K items) power=0.82-0.85，
      都在理论预测的 ±3pp 内——验证了 power ∝ n_items 的解析关系。
      (2) 这两个 benchmark 特别有价值因为它们是 reasoning-heavy (BBH) 和 math-heavy (MATH)，
      与 MMLU 的 knowledge-heavy 不同——跨领域一致性加强了方法的 generality。
      (3) 有了 7 个 benchmark 的数据点，power curve fit R²=0.97，
      Figure 7 的 power surface 变得更加 convincing。
      (4) MATH 上 d=1.9 略低于 2.0 阈值——因为 MATH 的 items 更 heterogeneous
      (部分 items 是 open-ended generation converted to binary)，
      4PL fit 稍差，但 AUROC=0.85 仍实用。
    tables:
      - title: "Table S6: Extended Benchmark Results"
        columns: ["Benchmark", "n_items", "Power (sim)", "Power (theory)", "Power (ctrl)", "d @15%"]
        rows:
          - ["MMLU", 14042, 0.979, 0.973, 0.94, 2.8]
          - ["HellaSwag", 10042, 0.733, 0.748, 0.91, 2.2]
          - ["BBH", 6511, 0.87, 0.85, 0.89, 2.1]
          - ["MATH", 5000, 0.82, 0.80, 0.85, 1.9]
          - ["GSM8K", 1319, 0.578, 0.561, 0.82, 1.4]
          - ["ARC-C", 1172, 0.129, 0.138, 0.74, 1.1]
          - ["HumanEval", 164, 0.243, 0.225, 0.63, 0.6]
    figures_description:
      - "Figure S5: Power vs n_items — 7 benchmark data points with theoretical curve overlay. R²=0.97 annotated."
    analysis: >
      BBH 和 MATH 是 Claim 2 的 supporting evidence，
      不改变 narrative 但显著增强 power theory 的 empirical backing。
      放入 main text 的 power curve figure (Figure 7) 中。

  - name: "Domain-Level Analysis (MMLU)"
    plan_id: "exp-domain-analysis"
    description: >
      按 MMLU subject category 分别计算 person-fit，
      识别 Gemini-1.5 的污染是全面的还是集中在特定 domain。
    expected_results:
      # Gemini-1.5 domain-level lz*
      gemini15_stem_lz_star: 36.2
      gemini15_humanities_lz_star: 33.8
      gemini15_social_sciences_lz_star: 30.1
      gemini15_other_lz_star: 28.4
      gemini15_cross_domain_cv: 0.09
      gemini15_pattern: "uniform across all domains"
      # Domain sizes
      stem_n_items: 4890
      humanities_n_items: 3782
      social_sciences_n_items: 3214
      other_n_items: 2156
      # Ctrl-exp domain-level (Qwen 15%)
      ctrl_qwen_stem_lz_star: -9.2
      ctrl_qwen_humanities_lz_star: -8.4
      ctrl_qwen_social_sciences_lz_star: -7.9
      ctrl_qwen_other_lz_star: -6.8
      ctrl_domain_cv: 0.12
      ctrl_pattern: "roughly uniform — consistent with random 15% sampling across domains"
      # Interesting contrast models
      yi_lightning_stem_lz_star: -12.4
      yi_lightning_humanities_lz_star: 2.1
      yi_lightning_social_sciences_lz_star: -8.7
      yi_lightning_other_lz_star: 1.8
      yi_lightning_pattern: "concentrated in STEM and social sciences — partial domain contamination"
    result_rationale: >
      Best 档下域分析揭示两种不同的 contamination pattern：
      (1) Gemini-1.5 的 lz* 在所有 domain 上均极高 (CV=0.09)，
      说明其 100% accuracy 是 uniform 的——要么全量 item 都被训练过，
      要么模型能力极强到每个 domain 都满分。结合 θ=0.78 (非极高)，
      uniform contamination 是更合理的解释。
      (2) Yi-Lightning 显示 domain-specific pattern——STEM 和 social sciences 极端 aberrant，
      humanities 和 other 正常。这暗示 selective contamination
      (可能通过 domain-specific data collection)。
      (3) 控制实验 (random 15% sampling) 产生 roughly uniform pattern (CV=0.12)，
      与 Gemini-1.5 一致——这支持 Gemini-1.5 的污染是 random/full 而非 domain-targeted。
      (4) Domain-level granularity使 "contamination forensics" 成为可能：
      不仅检测是否污染，还能推断 contamination strategy。
    tables:
      - title: "Table S7: Domain-Level Person-Fit (MMLU)"
        columns: ["Model", "STEM", "Humanities", "Social Sci", "Other", "CV", "Pattern"]
        rows:
          - ["Gemini-1.5-Pro", 36.2, 33.8, 30.1, 28.4, 0.09, "Uniform"]
          - ["Yi-Lightning", -12.4, 2.1, -8.7, 1.8, 1.42, "Domain-specific"]
          - ["Ctrl (Qwen 15%)", -9.2, -8.4, -7.9, -6.8, 0.12, "Uniform (expected)"]
          - ["Ctrl (Qwen clean)", 4.2, 3.8, 4.5, 3.1, 0.14, "Uniform baseline"]
    figures_description:
      - "Figure S6: Radar chart — 4 domains × selected models. Gemini-1.5 uniformly extreme. Yi-Lightning asymmetric."
    analysis: >
      Domain analysis 是 Claim 3 的 supporting evidence，增加了 forensic 价值。
      Gemini-1.5 的 uniform pattern + low θ 组合是 "smoking gun"——
      一个 θ=0.78 的模型不可能在所有 domain 都 100% accuracy 除非 contamination。
      Yi-Lightning 的 domain-specific pattern 提供了 qualitatively different case，
      丰富了 contamination taxonomy。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e1c2e34-5104-4ddd-b447-17de911ed703",
  "isSidechain": false,
  "requestId": "req_011CbDao3dQuwaLmuk5rnw1F",
  "type": "assistant",
  "uuid": "7ebf8f0f-feb2-4b8d-86b9-f6566e08a1a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GxtQ8MA4et9dNDnep5sajD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11685,
      "cache_read_input_tokens": 11841,
      "output_tokens": 20215,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 20215,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11685
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Δlz* 控制实验完全验证——注入已知污染后 lz* 偏移大且单调，三条 Claims 原样成立 核心假设：[\"SFT 注入污染后 Δlz* 效应量大（Cohen's d > 2.0），clean vs contaminated 明确可分\", 'Δlz* 与污染比例呈单调关系（dose-response），i…",
  "leafUuid": "7ebf8f0f-feb2-4b8d-86b9-f6566e08a1a6",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Design best-case controlled contamination experiments for IRT-FIT",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Δlz* 控制实验完全验证——注入已知污染后 lz* 偏移大且单调，三条 Claims 原样成立 核心假设：[\"SFT 注入污染后 Δlz* 效应量大（Cohen's d > 2.0），clean vs contaminated 明确可分\", 'Δlz* 与污染比例呈单调关系（dose-response），i…",
  "leafUuid": "7ebf8f0f-feb2-4b8d-86b9-f6566e08a1a6",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Design best-case controlled contamination experiments for IRT-FIT",
  "sessionId": "602a4653-1334-49b1-919f-e83a76f5ca81"
}
```

---
