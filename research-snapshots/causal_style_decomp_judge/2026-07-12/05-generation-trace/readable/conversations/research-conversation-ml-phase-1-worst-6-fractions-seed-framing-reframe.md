# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：6 fractions 打破核心相关性、跨域/跨规模泛化失败、或多 seed 方差过大导致原始 framing 不可用，需 reframe 核心假设：

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/ea91b0f3-c3d3-4728-a72d-3df599762220.jsonl`
- **Structured JSON:** [`0b62683433058f11d863.json`](../../sessions/0b/0b62683433058f11d863.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T21:05:34.707Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T21:05:34.707Z",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：6 fractions 打破核心相关性、跨域/跨规模泛化失败、或多 seed 方差过大导致原始 framing 不可用，需 reframe\n核心假设：['6 fractions 下 spectral 信号 ρ <0.70（饱和 + 非单调导致），output 信号 ρ 降至 0.65-0.75', '1.5B 信号行为与 0.5B 定性不一致（如 collapse 速度差异导致 gen-level 趋势不同）', 'PubMed 跨域 ρ <0.60，信号排序（哪个最有效）跨域不稳定', '50% self-recovery 仅 0-1/3 seeds 复现，判定为噪声/artifact', 'seed 方差大，多个 config 置信区间跨零，无法做 per-fraction 显著性声明', 'early warning 在 1.5B 上不 robust：分离度 <15% 或仅在 100% fraction 可见', 'stable rank 从 50% fraction 起即饱和，作为 severity monitor 几乎无用']\n关键指标范围：{'cross_frac_rho_spectral_6pt': [0.4, 0.69], 'cross_frac_rho_output_6pt': [0.6, 0.79], 'cross_gen_rho_spectral': [0.5, 0.75], 'early_warning_separation_3pct_progress': [5.0, 15.0], 'self_recovery_reproducibility': [0.0, 0.33], 'cross_domain_rho_preservation': [0.4, 0.64], 'cross_scale_rho_preservation': [0.5, 0.74], 'ppl_collapse_magnitude_100pct_gen4': [8.0, 25.0], 'seed_variance_cv_key_metrics': [0.25, 0.5]}\n叙事方向：原始 \"signals as monitors\" framing 不成立——没有单一信号或信号组合能 reliably track severity across conditions。Reframe 为 \"failure modes of training-time collapse detection\"：系统性展示为什么直觉上应该有效的信号 实际上不够 robust。核心贡献变为：(1) negative result——spectral/output 信号的 monitoring 假设在哪些条件下成立、在哪些条件下失败的完整 empirical map； (2) 信号行为对模型规模和数据域的敏感性分析（现有 collapse 文献未覆盖）； (3) 方差分析揭示 single-seed 实验的误导性（回应整个 collapse 文献的 reproducibility 问题）。Self-recovery 不提。标题改为 \"When Do Training Signals Detect Model Collapse? A Systematic Empirical Study\"。这个 angle 对 NeurIPS 仍有竞争力——well-executed negative/nuanced result 在 D&B track 有先例，但需要 experiment coverage 足够全面来支撑 \"systematic\" 的 claim。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: collapse_severity_monitor\nfocus: 重点关注：(1) analysis paper 定位是否成立——3 个 claim 是否足够支撑 A 类投稿；(2) n=3 fractions 统计效力弱点在 6 fractions 扩展后是否解决；(3) 50pct self-recovery 作为 novel finding 的说服力；(4) stable rank 饱和是否削弱 Claim 1\n\n## paper_framing.md\n\n# Paper Framing — collapse_severity_monitor\n\n## Target Venue\n- Primary: NeurIPS 2026 (Datasets & Benchmarks / Main)\n- Backup: ICLR 2027\n- Deadline: NeurIPS 2026 abstract ~late May 2026, full paper ~early June 2026\n\n## Core Claims (3 条)\n\n1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, with cross-fraction Spearman ρ=1.0 across all generations.\n\n2. **Early Warning Capability**: Collapse can be detected as early as 3% training progress (step 50/1540) via stable rank deviation (34.4% for 100% synthetic), enabling training-time early warning before catastrophic degradation materializes.\n\n3. **Non-Uniform Signal Behavior**: Different signal families exhibit qualitatively different responses to collapse — spectral signals saturate at extreme severity, gradient norm is non-monotonic, downstream task metrics (HellaSwag) fail to detect collapse at small model scale. This taxonomy of signal behavior provides actionable guidance for practitioners choosing monitoring strategies.\n\n## Story Spine\n\n- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.\n\n- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution. Kalinowski (2024) uses topological analysis but is computationally expensive. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.\n\n- **Our framing**: We conduct the first systematic analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × multiple contamination levels × generational iterations, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: spectral signals provide the earliest warning (3% progress) while output signals provide the most reliable severity tracking. The 50% contamination regime reveals a partial self-recovery phenomenon not previously documented.\n\n- **Headline result template**: \"Stable rank deviation detects model collapse at 3% training progress with 34% signal separation, while token entropy and perplexity maintain monotonic severity tracking across 5 generational iterations with ρ=1.0. We identify a previously unreported self-recovery pattern at moderate contamination levels.\"\n\n## Anticipated Reviewer Concerns & Mitigation\n\n| Concern | Severity | Mitigation Experiment |\n|---------|----------|----------------------|\n| Single model (Qwen-0.5B) — can't generalize | HIGH | P0: 1.5B model, P1: cross-architecture (if GPU permits) |\n| Single dataset (WikiText-2) — domain-specific | HIGH | P0: PubMed domain, P1: code domain |\n| Single seed — no variance estimates | HIGH | P0: 3 seeds per config |\n| n=3 fractions — Spearman ρ trivially 1.0 | HIGH | P0: 6 fractions (0/10/25/50/75/100%) |\n| QLoRA only — not representative of full FT | MEDIUM | P1: Full FT comparison on 1 config |\n| \"Not a monitoring system\" — analysis only | LOW | Frame as analysis paper; early warning finding adds practical value |\n| No intervention/mitigation experiments | LOW | Explicit non-goal; frame as \"diagnostic\" contribution, mitigation as future work |\n| Stable rank saturates — limited as severity tracker | LOW | Claim 3 explicitly addresses signal limitations as finding |\n\n## Core Insight (一句话)\n\nTraining dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.\n\n## Novelty Statement\n\nNo prior work systematically compares multiple training-time signal families as collapse severity monitors across contamination levels. The within-generation early warning capability (3% progress) and the self-recovery phenomenon at moderate contamination are novel empirical contributions.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Scale validation: 1.5B model (Qwen2.5-1.5B) × WikiText-2 × 6 fractions\n    (0/10/25/50/75/100%) × 3 seeds. Core experiment proving signal-severity correlation\n    generalizes beyond 0.5B MVP.'\n  priority: P0\n  gpu_budget_hours: 90\n  deps: []\n  registry_id: null\n  notes: 6 fractions × 3 seeds × 5 gens = 90 runs. ~1h/run on A6000 for 1.5B QLoRA.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Cross-domain validation: 1.5B × PubMed × 6 fractions × 1 seed. Proves\n    signals generalize beyond WikiText to biomedical domain.'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Only 1 seed; if results diverge from WikiText, add 2 more seeds.\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Full FT comparison: 0.5B × WikiText-2 × 3 fractions (0/50/100%) ×\n    1 seed with full fine-tuning. Validates signals are not QLoRA-specific.'\n  priority: P1\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  notes: Full FT on 0.5B should fit in single A6000 24GB.\n  status: planned\n- id: plan_004\n  claim: 2\n  description: Within-gen early warning analysis on 1.5B data. Compute signal divergence\n    at step 50/100/200/500 across all fractions and seeds from plan_001. Pure analysis,\n    no GPU.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Extends MVP within-gen analysis to 1.5B with proper statistics.\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Early warning threshold calibration: determine minimum signal deviation\n    that reliably predicts end-of-generation collapse. ROC analysis across all configs.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: null\n  notes: Analysis only. Need sufficient runs for meaningful ROC.\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'Signal taxonomy across severity levels. Using plan_001 data, characterize\n    per-signal-family operating ranges: where each signal is most/least informative.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Core table/figure for Claim 3. Shows stable_rank saturation, gradient non-monotonicity,\n    downstream failure.\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Per-layer collapse analysis: run forward-pass SVD on 1.5B model across\n    gens to show which layers collapse first and how layer-level patterns differ by\n    severity.'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Extends MVP per-layer analysis to 1.5B. Figure 3 candidate.\n  status: planned\n- id: plan_008\n  claim: 3\n  description: 'Self-recovery phenomenon deep dive: 50% contamination partial recovery\n    analysis. Is it consistent across seeds? At what fraction does recovery disappear?'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Analysis of plan_001 data at 25/50/75% fractions.\n  status: planned\n- id: plan_mvp_001\n  claim: 1\n  description: 'MVP: 0.5B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens'\n  priority: P0\n  gpu_budget_hours: 14.1\n  deps: []\n  registry_id: mvp_frac0\n  notes: Control baseline. DONE.\n  status: DONE\n  conclusion: success\n- id: plan_mvp_002\n  claim: 1\n  description: 'MVP: 0.5B × WikiText-2 × 50pct + 100pct × 1 seed × 5 gens'\n  priority: P0\n  gpu_budget_hours: 14.1\n  deps: []\n  registry_id: mvp_frac50_100\n  notes: Main MVP experiment. DONE. Gate check 2/3 PASS.\n  status: DONE\n  conclusion: success\n  metrics:\n    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5\n    gate_check_verdict: PASS (2/3 families)\n    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen\n      rho=0.9 (p=0.037)\n    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;\n      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0\n    gate_check_downstream: FAIL — no hellaswag_acc data (data gap, not signal failure)\n    final_values_0pct_gen4:\n      stable_rank: 23.41\n      spectral_entropy: 0.703\n      token_entropy: 2.259\n      ppl: 15.67\n    final_values_50pct_gen4:\n      stable_rank: 24.79\n      spectral_entropy: 0.716\n      token_entropy: 2.215\n      ppl: 16.95\n    final_values_100pct_gen4:\n      stable_rank: 155.64\n      spectral_entropy: 0.884\n      token_entropy: 0.782\n      ppl: 839.2\n    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%\n    0pct_baseline_stability: all signals <3% variation across 5 gens\n    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training\n      progress)\n- id: plan_mvp_003\n  claim: 2\n  description: MVP within-gen temporal analysis on 0.5B data\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_mvp_002\n  registry_id: within_gen_analysis\n  notes: DONE. Early warning at 3% progress confirmed.\n  status: orphaned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_collapse_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    progress: 0pct_gen0 step 242/1540 (15.7%)\n    speed: 1.19 it/s\n    loss: 2.652\n    perplexity: 14.41\n    stable_rank: 20.5\n    spectral_entropy: 0.673\n    signals_collected: 4\n    checked_at: '2026-05-14T06:38:30Z'\n- exp_id: mvp_collapse_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct_gen0 step 50/1540 (3%)\n    speed: 1.17 it/s\n    gpu_util: 26%\n    gpu_mem: 6314/32607 MiB\n    gen_batch_size: 32\n    gen_num_chunks: 1500\n    checked_at: '2026-05-14T08:21:00Z'\n- exp_id: mvp_collapse_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct_gen0 step 50/1540 (3%)\n    speed: 1.08 it/s\n    gpu_util: 20%\n    gpu_mem: 6314/32607 MiB\n    checked_at: '2026-05-14T09:01:30Z'\n- exp_id: mvp_frac50_100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5\n    gate_check_verdict: PASS (2/3 families)\n    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen\n      rho=0.9 (p=0.037)\n    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;\n      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0\n    gate_check_downstream: FAIL — no hellaswag_acc data (data gap, not signal failure)\n    final_values_0pct_gen4:\n      stable_rank: 23.41\n      spectral_entropy: 0.703\n      token_entropy: 2.259\n      ppl: 15.67\n    final_values_50pct_gen4:\n      stable_rank: 24.79\n      spectral_entropy: 0.716\n      token_entropy: 2.215\n      ppl: 16.95\n    final_values_100pct_gen4:\n      stable_rank: 155.64\n      spectral_entropy: 0.884\n      token_entropy: 0.782\n      ppl: 839.2\n    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%\n    0pct_baseline_stability: all signals <3% variation across 5 gens\n    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training\n      progress)\n- exp_id: mvp_frac0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: per_layer_analysis\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct gen0 1388/1540 (90%), ~2min to finish gen0\n    output_file: outputs/per_layer_analysis.json (incremental save per gen)\n    per_gen_time: ~35 min/gen\n    total_gens: 2 fractions x 5 gens = 10 gens\n    eta_total: ~6h from start (started ~18:19 UTC)\n    signals_safety: 'confirmed: output_dir redirected to _per_layer_tmp, signals_*.jsonl\n      untouched'\n    analysis_method: 'hook all transformer layers, 64 val samples forward pass, compute\n      per-layer SVD: stable_rank, spectral_entropy, SV_ratio(sigma1/sigma2)'\n    gpu: GPU 1, 6314/32607 MiB, 43% util\n    checked_at: '2026-05-14T18:58:00Z'\n- exp_id: per_layer_analysis_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_active\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    progress: 0pct gen0=done, 0pct gen1=in_progress\n    per_gen_time: ~35 min/gen\n    eta_remaining: ~9 gens x 35min = ~5.25h\n    gpu: cuda:1\n    checked_at: '2026-05-14T19:08:00Z'\n- exp_id: per_layer_analysis_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_v5\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T21:05:34.710Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T21:05:34.710Z",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T21:05:34.730Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：6 fractions 打破核心相关性、跨域/跨规模泛化失败、或多 seed 方差过大导致原始 framing 不可用，需 reframe
核心假设：['6 fractions 下 spectral 信号 ρ <0.70（饱和 + 非单调导致），output 信号 ρ 降至 0.65-0.75', '1.5B 信号行为与 0.5B 定性不一致（如 collapse 速度差异导致 gen-level 趋势不同）', 'PubMed 跨域 ρ <0.60，信号排序（哪个最有效）跨域不稳定', '50% self-recovery 仅 0-1/3 seeds 复现，判定为噪声/artifact', 'seed 方差大，多个 config 置信区间跨零，无法做 per-fraction 显著性声明', 'early warning 在 1.5B 上不 robust：分离度 <15% 或仅在 100% fraction 可见', 'stable rank 从 50% fraction 起即饱和，作为 severity monitor 几乎无用']
关键指标范围：{'cross_frac_rho_spectral_6pt': [0.4, 0.69], 'cross_frac_rho_output_6pt': [0.6, 0.79], 'cross_gen_rho_spectral': [0.5, 0.75], 'early_warning_separation_3pct_progress': [5.0, 15.0], 'self_recovery_reproducibility': [0.0, 0.33], 'cross_domain_rho_preservation': [0.4, 0.64], 'cross_scale_rho_preservation': [0.5, 0.74], 'ppl_collapse_magnitude_100pct_gen4': [8.0, 25.0], 'seed_variance_cv_key_metrics': [0.25, 0.5]}
叙事方向：原始 "signals as monitors" framing 不成立——没有单一信号或信号组合能 reliably track severity across conditions。Reframe 为 "failure modes of training-time collapse detection"：系统性展示为什么直觉上应该有效的信号 实际上不够 robust。核心贡献变为：(1) negative result——spectral/output 信号的 monitoring 假设在哪些条件下成立、在哪些条件下失败的完整 empirical map； (2) 信号行为对模型规模和数据域的敏感性分析（现有 collapse 文献未覆盖）； (3) 方差分析揭示 single-seed 实验的误导性（回应整个 collapse 文献的 reproducibility 问题）。Self-recovery 不提。标题改为 "When Do Training Signals Detect Model Collapse? A Systematic Empirical Study"。这个 angle 对 NeurIPS 仍有竞争力——well-executed negative/nuanced result 在 D&B track 有先例，但需要 experiment coverage 足够全面来支撑 "systematic" 的 claim。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: collapse_severity_monitor
focus: 重点关注：(1) analysis paper 定位是否成立——3 个 claim 是否足够支撑 A 类投稿；(2) n=3 fractions 统计效力弱点在 6 fractions 扩展后是否解决；(3) 50pct self-recovery 作为 novel finding 的说服力；(4) stable rank 饱和是否削弱 Claim 1

## paper_framing.md

# Paper Framing — collapse_severity_monitor

## Target Venue
- Primary: NeurIPS 2026 (Datasets & Benchmarks / Main)
- Backup: ICLR 2027
- Deadline: NeurIPS 2026 abstract ~late May 2026, full paper ~early June 2026

## Core Claims (3 条)

1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, with cross-fraction Spearman ρ=1.0 across all generations.

2. **Early Warning Capability**: Collapse can be detected as early as 3% training progress (step 50/1540) via stable rank deviation (34.4% for 100% synthetic), enabling training-time early warning before catastrophic degradation materializes.

3. **Non-Uniform Signal Behavior**: Different signal families exhibit qualitatively different responses to collapse — spectral signals saturate at extreme severity, gradient norm is non-monotonic, downstream task metrics (HellaSwag) fail to detect collapse at small model scale. This taxonomy of signal behavior provides actionable guidance for practitioners choosing monitoring strategies.

## Story Spine

- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.

- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution. Kalinowski (2024) uses topological analysis but is computationally expensive. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.

- **Our framing**: We conduct the first systematic analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × multiple contamination levels × generational iterations, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: spectral signals provide the earliest warning (3% progress) while output signals provide the most reliable severity tracking. The 50% contamination regime reveals a partial self-recovery phenomenon not previously documented.

- **Headline result template**: "Stable rank deviation detects model collapse at 3% training progress with 34% signal separation, while token entropy and perplexity maintain monotonic severity tracking across 5 generational iterations with ρ=1.0. We identify a previously unreported self-recovery pattern at moderate contamination levels."

## Anticipated Reviewer Concerns & Mitigation

| Concern | Severity | Mitigation Experiment |
|---------|----------|----------------------|
| Single model (Qwen-0.5B) — can't generalize | HIGH | P0: 1.5B model, P1: cross-architecture (if GPU permits) |
| Single dataset (WikiText-2) — domain-specific | HIGH | P0: PubMed domain, P1: code domain |
| Single seed — no variance estimates | HIGH | P0: 3 seeds per config |
| n=3 fractions — Spearman ρ trivially 1.0 | HIGH | P0: 6 fractions (0/10/25/50/75/100%) |
| QLoRA only — not representative of full FT | MEDIUM | P1: Full FT comparison on 1 config |
| "Not a monitoring system" — analysis only | LOW | Frame as analysis paper; early warning finding adds practical value |
| No intervention/mitigation experiments | LOW | Explicit non-goal; frame as "diagnostic" contribution, mitigation as future work |
| Stable rank saturates — limited as severity tracker | LOW | Claim 3 explicitly addresses signal limitations as finding |

## Core Insight (一句话)

Training dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.

## Novelty Statement

No prior work systematically compares multiple training-time signal families as collapse severity monitors across contamination levels. The within-generation early warning capability (3% progress) and the self-recovery phenomenon at moderate contamination are novel empirical contributions.


## experiment_plan (with registry status)

- id: plan_001
  claim: 1
  description: 'Scale validation: 1.5B model (Qwen2.5-1.5B) × WikiText-2 × 6 fractions
    (0/10/25/50/75/100%) × 3 seeds. Core experiment proving signal-severity correlation
    generalizes beyond 0.5B MVP.'
  priority: P0
  gpu_budget_hours: 90
  deps: []
  registry_id: null
  notes: 6 fractions × 3 seeds × 5 gens = 90 runs. ~1h/run on A6000 for 1.5B QLoRA.
  status: planned
- id: plan_002
  claim: 1
  description: 'Cross-domain validation: 1.5B × PubMed × 6 fractions × 1 seed. Proves
    signals generalize beyond WikiText to biomedical domain.'
  priority: P0
  gpu_budget_hours: 15
  deps:
  - plan_001
  registry_id: null
  notes: Only 1 seed; if results diverge from WikiText, add 2 more seeds.
  status: planned
- id: plan_003
  claim: 1
  description: 'Full FT comparison: 0.5B × WikiText-2 × 3 fractions (0/50/100%) ×
    1 seed with full fine-tuning. Validates signals are not QLoRA-specific.'
  priority: P1
  gpu_budget_hours: 20
  deps: []
  registry_id: null
  notes: Full FT on 0.5B should fit in single A6000 24GB.
  status: planned
- id: plan_004
  claim: 2
  description: Within-gen early warning analysis on 1.5B data. Compute signal divergence
    at step 50/100/200/500 across all fractions and seeds from plan_001. Pure analysis,
    no GPU.
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: null
  notes: Extends MVP within-gen analysis to 1.5B with proper statistics.
  status: planned
- id: plan_005
  claim: 2
  description: 'Early warning threshold calibration: determine minimum signal deviation
    that reliably predicts end-of-generation collapse. ROC analysis across all configs.'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  - plan_002
  registry_id: null
  notes: Analysis only. Need sufficient runs for meaningful ROC.
  status: planned
- id: plan_006
  claim: 3
  description: 'Signal taxonomy across severity levels. Using plan_001 data, characterize
    per-signal-family operating ranges: where each signal is most/least informative.'
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: null
  notes: Core table/figure for Claim 3. Shows stable_rank saturation, gradient non-monotonicity,
    downstream failure.
  status: planned
- id: plan_007
  claim: 3
  description: 'Per-layer collapse analysis: run forward-pass SVD on 1.5B model across
    gens to show which layers collapse first and how layer-level patterns differ by
    severity.'
  priority: P1
  gpu_budget_hours: 15
  deps:
  - plan_001
  registry_id: null
  notes: Extends MVP per-layer analysis to 1.5B. Figure 3 candidate.
  status: planned
- id: plan_008
  claim: 3
  description: 'Self-recovery phenomenon deep dive: 50% contamination partial recovery
    analysis. Is it consistent across seeds? At what fraction does recovery disappear?'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: null
  notes: Analysis of plan_001 data at 25/50/75% fractions.
  status: planned
- id: plan_mvp_001
  claim: 1
  description: 'MVP: 0.5B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens'
  priority: P0
  gpu_budget_hours: 14.1
  deps: []
  registry_id: mvp_frac0
  notes: Control baseline. DONE.
  status: DONE
  conclusion: success
- id: plan_mvp_002
  claim: 1
  description: 'MVP: 0.5B × WikiText-2 × 50pct + 100pct × 1 seed × 5 gens'
  priority: P0
  gpu_budget_hours: 14.1
  deps: []
  registry_id: mvp_frac50_100
  notes: Main MVP experiment. DONE. Gate check 2/3 PASS.
  status: DONE
  conclusion: success
  metrics:
    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5
    gate_check_verdict: PASS (2/3 families)
    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen
      rho=0.9 (p=0.037)
    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;
      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0
    gate_check_downstream: FAIL — no hellaswag_acc data (data gap, not signal failure)
    final_values_0pct_gen4:
      stable_rank: 23.41
      spectral_entropy: 0.703
      token_entropy: 2.259
      ppl: 15.67
    final_values_50pct_gen4:
      stable_rank: 24.79
      spectral_entropy: 0.716
      token_entropy: 2.215
      ppl: 16.95
    final_values_100pct_gen4:
      stable_rank: 155.64
      spectral_entropy: 0.884
      token_entropy: 0.782
      ppl: 839.2
    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%
    0pct_baseline_stability: all signals <3% variation across 5 gens
    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training
      progress)
- id: plan_mvp_003
  claim: 2
  description: MVP within-gen temporal analysis on 0.5B data
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_mvp_002
  registry_id: within_gen_analysis
  notes: DONE. Early warning at 3% progress confirmed.
  status: orphaned


## registry (completed experiments)

- exp_id: mvp_collapse_001
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    progress: 0pct_gen0 step 242/1540 (15.7%)
    speed: 1.19 it/s
    loss: 2.652
    perplexity: 14.41
    stable_rank: 20.5
    spectral_entropy: 0.673
    signals_collected: 4
    checked_at: '2026-05-14T06:38:30Z'
- exp_id: mvp_collapse_002
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 0pct_gen0 step 50/1540 (3%)
    speed: 1.17 it/s
    gpu_util: 26%
    gpu_mem: 6314/32607 MiB
    gen_batch_size: 32
    gen_num_chunks: 1500
    checked_at: '2026-05-14T08:21:00Z'
- exp_id: mvp_collapse_003
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 0pct_gen0 step 50/1540 (3%)
    speed: 1.08 it/s
    gpu_util: 20%
    gpu_mem: 6314/32607 MiB
    checked_at: '2026-05-14T09:01:30Z'
- exp_id: mvp_frac50_100
  name: ''
  status: DONE
  conclusion: success
  metrics:
    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5
    gate_check_verdict: PASS (2/3 families)
    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen
      rho=0.9 (p=0.037)
    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;
      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0
    gate_check_downstream: FAIL — no hellaswag_acc data (data gap, not signal failure)
    final_values_0pct_gen4:
      stable_rank: 23.41
      spectral_entropy: 0.703
      token_entropy: 2.259
      ppl: 15.67
    final_values_50pct_gen4:
      stable_rank: 24.79
      spectral_entropy: 0.716
      token_entropy: 2.215
      ppl: 16.95
    final_values_100pct_gen4:
      stable_rank: 155.64
      spectral_entropy: 0.884
      token_entropy: 0.782
      ppl: 839.2
    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%
    0pct_baseline_stability: all signals <3% variation across 5 gens
    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training
      progress)
- exp_id: mvp_frac0
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: per_layer_analysis
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: per_layer_analysis_v2
  name: ''
  status: DONE
  conclusion: killed
  metrics:
    progress: 0pct gen0 1388/1540 (90%), ~2min to finish gen0
    output_file: outputs/per_layer_analysis.json (incremental save per gen)
    per_gen_time: ~35 min/gen
    total_gens: 2 fractions x 5 gens = 10 gens
    eta_total: ~6h from start (started ~18:19 UTC)
    signals_safety: 'confirmed: output_dir redirected to _per_layer_tmp, signals_*.jsonl
      untouched'
    analysis_method: 'hook all transformer layers, 64 val samples forward pass, compute
      per-layer SVD: stable_rank, spectral_entropy, SV_ratio(sigma1/sigma2)'
    gpu: GPU 1, 6314/32607 MiB, 43% util
    checked_at: '2026-05-14T18:58:00Z'
- exp_id: per_layer_analysis_v3
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: per_layer_analysis_active
  name: ''
  status: RUNNING
  conclusion: ''
  metrics:
    progress: 0pct gen0=done, 0pct gen1=in_progress
    per_gen_time: ~35 min/gen
    eta_remaining: ~9 gens x 35min = ~5.25h
    gpu: cuda:1
    checked_at: '2026-05-14T19:08:00Z'
- exp_id: per_layer_analysis_v4
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: per_layer_analysis_v5
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}

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
  "promptId": "c093e68e-43cb-43b4-90fa-d1819ecd5d11",
  "type": "user",
  "uuid": "bbb1498e-e06b-4705-89c0-7e96c7e2f01b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T21:05:34.730Z_

```json
{
  "parentUuid": "bbb1498e-e06b-4705-89c0-7e96c7e2f01b",
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
  "uuid": "e783bca6-6acc-4808-a921-d68da05566d8",
  "timestamp": "2026-05-14T21:05:34.730Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T21:05:34.730Z_

```json
{
  "parentUuid": "e783bca6-6acc-4808-a921-d68da05566d8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bcb6d375-161f-4276-bcd5-faac57ff2976",
  "timestamp": "2026-05-14T21:05:34.730Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：6 fractions 打破核心相关性、跨域/跨规模泛化失败、或多 seed 方差过大导致原始 framing 不可用，需 reframe 核心假设：['6 fractions 下 spectral 信号 ρ <0.70（饱和 + 非单调导致），output 信号 ρ 降至 0.65-0.75', '1.5…",
  "leafUuid": "bcb6d375-161f-4276-bcd5-faac57ff2976",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical study of training signal robustness for collapse detection",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220"
}
```

---

### Assistant

_source line 8 · 2026-05-14T21:05:46.717Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier across all planned experiments in the experiment_plan. This is for a model collapse severity monitoring paper, and the "worst" tier means the original framing breaks down - signals fail to reliably track collapse severity.

Let me carefully go through each planned experiment and generate worst-tier predictions with rationales.

Key worst-tier characteristics:
- 6 fractions break core correlations (spectral ρ < 0.70, output ρ 0.65-0.75)


- 1.5B shows qualitatively different behavior from 0.5B, undermining scaling assumptions
- PubMed cross-domain performance degrades significantly (ρ < 0.60) with unstable signal rankings
- Self-recovery appears as noise or artifact with only 0-1 out of 3 seeds reproducing the effect
- High seed variance with confidence intervals crossing zero
- Early warning signals on 1.5B lack robustness, showing less than 15% separation or only emerging at 100% fraction
- Stable rank plateaus from 50% fraction onward, losing discriminative power

Now I'm working through the specific experiments to generate detailed worst-tier predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcb6d375-161f-4276-bcd5-faac57ff2976",
  "isSidechain": false,
  "requestId": "req_011Cb399R6z7QBhW3Y7R7kmR",
  "type": "assistant",
  "uuid": "e4bf82d8-e6b9-4ec1-bbd5-284b38281f92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZxDy76hXecuVsULfMnPhD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10886,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13065,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13065,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10886
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

_source line 9 · 2026-05-14T21:09:50.311Z_

```yaml
tier: worst
narrative_guidance: >
  原始 "signals as monitors" framing 不成立——没有单一信号或信号组合能 reliably track severity across conditions。
  Reframe 为 "failure modes of training-time collapse detection"：系统性展示为什么直觉上应该有效的信号实际上不够 robust。
  核心贡献变为：(1) negative result——spectral/output 信号的 monitoring 假设在哪些条件下成立、在哪些条件下失败的完整 empirical map；
  (2) 信号行为对模型规模和数据域的敏感性分析（现有 collapse 文献未覆盖）；
  (3) 方差分析揭示 single-seed 实验的误导性（回应整个 collapse 文献的 reproducibility 问题）。
  Self-recovery 不提。标题改为 "When Do Training Signals Detect Model Collapse? A Systematic Empirical Study"。

imagined_experiments:
  # ============================================================
  # plan_001: 1.5B × WikiText-2 × 6 fractions × 3 seeds
  # ============================================================
  - name: "Scale validation: 1.5B model, 6 fractions, 3 seeds"
    plan_id: "plan_001"
    description: >
      Qwen2.5-1.5B × WikiText-2 × 6 fractions (0/10/25/50/75/100%) × 3 seeds × 5 gens。
      核心实验，验证 signal-severity correlation 在更大模型和更细粒度 fraction 下是否成立。
    expected_results:
      # Cross-fraction Spearman ρ (6-point) —— 核心指标
      cross_frac_rho_spectral_stable_rank_mean: 0.54
      cross_frac_rho_spectral_stable_rank_std: 0.18
      cross_frac_rho_spectral_entropy_mean: 0.61
      cross_frac_rho_spectral_entropy_std: 0.14
      cross_frac_rho_output_ppl_mean: 0.71
      cross_frac_rho_output_ppl_std: 0.12
      cross_frac_rho_output_token_entropy_mean: -0.68
      cross_frac_rho_output_token_entropy_std: 0.15
      cross_frac_rho_gradient_norm_mean: 0.22
      cross_frac_rho_gradient_norm_std: 0.31
      # Cross-gen Spearman ρ
      cross_gen_rho_spectral_mean: 0.62
      cross_gen_rho_output_mean: 0.71
      # Final values at gen4 (averaged over 3 seeds, ±std)
      stable_rank_0pct_gen4: "28.3 ± 1.2"
      stable_rank_10pct_gen4: "29.1 ± 2.4"
      stable_rank_25pct_gen4: "31.7 ± 4.1"
      stable_rank_50pct_gen4: "33.2 ± 5.8"
      stable_rank_75pct_gen4: "34.0 ± 7.2"
      stable_rank_100pct_gen4: "89.4 ± 22.6"
      ppl_0pct_gen4: "12.8 ± 0.3"
      ppl_10pct_gen4: "13.2 ± 0.5"
      ppl_25pct_gen4: "14.9 ± 1.1"
      ppl_50pct_gen4: "17.3 ± 3.2"
      ppl_75pct_gen4: "28.6 ± 8.4"
      ppl_100pct_gen4: "185.3 ± 62.7"
      token_entropy_0pct_gen4: "2.31 ± 0.02"
      token_entropy_50pct_gen4: "2.18 ± 0.09"
      token_entropy_100pct_gen4: "1.24 ± 0.31"
      # Collapse magnitude (100% gen4 vs 0% gen4)
      collapse_magnitude_ppl_100pct: "14.5x (但 CV=0.34)"
      collapse_magnitude_stable_rank_100pct: "3.2x (远低于 0.5B 的 6.6x)"
      # Seed variance
      seed_variance_cv_stable_rank_mid_fracs: 0.35
      seed_variance_cv_ppl_mid_fracs: 0.28
      seed_variance_cv_token_entropy_mid_fracs: 0.42
      # Per-fraction significance (Kruskal-Wallis vs 0%)
      fractions_significantly_different_from_0pct: "仅 75%, 100% (p<0.05); 10/25/50% 均 p>0.10"
    result_rationale: >
      1.5B 模型的 collapse 动态与 0.5B 定性不同。更大的参数空间提供更多冗余，使得
      10-50% contamination 的影响被模型容量吸收——stable rank 在这些 fraction 几乎不变化，
      导致 6-point Spearman ρ 因中间 4 个 fraction 的"平台效应"而大幅下降。具体来说：
      (1) Stable rank 在 25-75% fraction 区间饱和（1.5B 比 0.5B 更早饱和，因为更多
      参数冗余让 spectral structure 在中等 contamination 下保持稳定），只在 100% 出现
      显著跳跃，形成 step function 而非 monotonic curve，ρ 被拉低到 ~0.54。
      (2) PPL 虽然仍大致单调，但 10-50% 区间的差异（13.2→17.3）被 seed 间方差淹没
      （std 从 0.5 到 3.2），CI 重叠严重，6-point ρ 降到 0.71 且单个 seed 可低至 0.55。
      (3) 1.5B collapse 幅度远小于 0.5B（PPL 185 vs 839，stable rank 3.2x vs 6.6x），
      因为更大模型的 generalization capacity 延缓了 catastrophic collapse 的 onset，
      这意味着 gen4 时 1.5B 可能还在 "pre-catastrophic" 阶段，而 0.5B 在 gen4 已经
      fully collapsed。这是 cross-scale 定性不一致的根本原因。
      (4) Seed 方差在中间 fraction 显著偏大（CV 0.28-0.42），因为这些 regime 处于
      collapse/non-collapse 的 phase boundary，对初始化和数据采样高度敏感。
      多个 fraction 的 CI 跨零使得 per-fraction 显著性声明不可行。
    tables:
      - name: "Table 1: Cross-fraction Spearman ρ (6-point) by signal family, 1.5B"
        description: >
          Rows: signal (stable_rank, spectral_entropy, ppl, token_entropy, gradient_norm, hellaswag_acc)。
          Columns: gen0, gen1, gen2, gen3, gen4, mean±std。
          Key pattern: spectral 信号在所有 gen 均 ρ<0.70；output 信号 gen0-gen2 ρ≈0.75-0.80，
          gen3-gen4 降至 0.65 因为 100% fraction 的 variance 增大；gradient_norm 无一致方向。
        data_preview:
          stable_rank: [0.66, 0.60, 0.49, 0.51, 0.43, "0.54 ± 0.09"]
          spectral_entropy: [0.71, 0.66, 0.60, 0.57, 0.51, "0.61 ± 0.08"]
          ppl: [0.83, 0.77, 0.71, 0.66, 0.60, "0.71 ± 0.09"]
          token_entropy: [-0.80, -0.74, -0.66, -0.60, -0.57, "-0.68 ± 0.10"]
          gradient_norm: [0.37, 0.14, -0.09, 0.31, 0.20, "0.19 ± 0.17"]
      - name: "Table 2: Final values (gen4) by fraction, 1.5B, mean ± std over 3 seeds"
        description: >
          Rows: fraction (0/10/25/50/75/100%)。Columns: stable_rank, spectral_entropy, ppl, token_entropy。
          Key pattern: 0-50% 四列数值相近且 std 大，75% 开始分离，100% 明显异常但 std 极大。
      - name: "Table 3: Per-fraction Kruskal-Wallis test vs 0% baseline"
        description: >
          Rows: fraction (10/25/50/75/100%)。Columns: signal, H-statistic, p-value, significant (α=0.05)。
          Key finding: 仅 75% 和 100% 在 ppl/token_entropy 上显著；spectral 信号仅 100% 显著。
          10/25/50% 在所有信号上 p>0.10，n=3 seeds 统计效力不足。
    figures_description:
      - "Figure 1: 6-fraction severity curves (1.5B, 3 seeds). X=fraction, Y=signal value, 每条线一个 seed, shaded=mean±std。Stable rank 呈现明显 step function（0-75% 平坦，100% 跳跃）而非 0.5B 观测到的 gradual increase。PPL 曲线虽单调但 error bars 在 25-75% 区间严重重叠。"
      - "Figure 2: Cross-fraction ρ 随 generation 的衰退曲线。X=generation, Y=ρ。所有 signal family 的 ρ 从 gen0 到 gen4 持续下降，spectral 从 0.66 降至 0.43，output 从 0.83 降至 0.60。说明 correlation 不仅弱，还不稳定。"
      - "Figure 3: Seed-level 方差热力图。X=fraction, Y=signal, color=CV。中间 fraction (25-75%) 的 CV 集中在 0.25-0.50（热色），两端 (0%, 100%) CV<0.15（冷色），说明 phase boundary 区域的 irreproducibility。"
    analysis: >
      plan_001 的 worst 结果直接瓦解了 Claim 1 的原始 formulation。MVP 中 ρ=1.0 是 n=3 的
      trivial artifact：任何单调信号在 3 点上都能达到 ρ=1.0。扩展到 6 fractions 后，
      中间 fraction 的信号行为暴露了两个 fundamental issue：(a) spectral 信号在 1.5B 上
      因容量冗余而对中等 contamination 不敏感，形成 step function，ρ 降至 0.54；
      (b) output 信号虽仍大致单调（ρ≈0.71），但 seed 方差导致相邻 fraction 不可区分。
      此外，ρ 随 generation 衰退表明 signal-severity 关系本身是非平稳的。
      Reframe 方向：这恰恰是 "failure modes" paper 的核心素材——系统展示 monotonic 假设
      在何种条件下（fraction 密度、模型规模、generation 深度）失效。

  # ============================================================
  # plan_002: 1.5B × PubMed × 6 fractions × 1 seed
  # ============================================================
  - name: "Cross-domain validation: 1.5B × PubMed"
    plan_id: "plan_002"
    description: >
      Qwen2.5-1.5B × PubMed × 6 fractions (0/10/25/50/75/100%) × 1 seed × 5 gens。
      验证信号在 biomedical domain 的泛化能力。
    expected_results:
      cross_frac_rho_spectral_stable_rank: 0.43
      cross_frac_rho_spectral_entropy: 0.49
      cross_frac_rho_output_ppl: 0.60
      cross_frac_rho_output_token_entropy: -0.54
      cross_domain_rho_preservation_spectral: 0.44
      cross_domain_rho_preservation_output: 0.58
      ppl_0pct_gen4: 18.4
      ppl_100pct_gen4: 92.6
      collapse_magnitude_ppl_100pct: "5.0x (WikiText 14.5x)"
      stable_rank_0pct_gen4: 31.2
      stable_rank_100pct_gen4: 52.8
      signal_ranking_match_with_wikitext: "2/5 signals maintain same relative ordering across fractions"
      token_entropy_behavior: "非单调——在 50% fraction 处反弹高于 25%"
    result_rationale: >
      PubMed 域与 WikiText 有根本差异：(1) biomedical text 的词汇分布更窄、repetition
      更多（术语、结构化摘要），base model 在 PubMed 上的 token entropy 本身就低于 WikiText，
      这压缩了 contamination 的可探测 dynamic range；(2) 合成 PubMed 文本更倾向于
      formulaic output（"In this study, we investigated..."），与 real PubMed 的 overlap
      更高，使得 contamination 效应被域特性掩盖；(3) collapse 幅度显著更小（PPL 5x vs 14.5x），
      因为 PubMed 文本本身的 diversity 低于 general-domain WikiText，合成数据和真实数据的
      distributional gap 更小。
      关键 failure mode：signal ranking 跨域不稳定。WikiText 上 ppl 是最强信号（ρ=0.71），
      PubMed 上 spectral_entropy 和 ppl 排序翻转。Token entropy 在 PubMed 上出现非单调行为：
      50% fraction 时模型在 biomedical jargon 上 overfit 导致 entropy 暂时升高（模型生成
      更多 low-frequency 专业术语以"模仿"真实分布），然后在 75-100% 时再次下降。
      这一非单调性使得 token entropy 作为 severity monitor 在 PubMed 上完全不可用。
      Cross-domain ρ preservation（WikiText 信号 ranking 与 PubMed 信号 ranking 的 Spearman
      相关）仅 0.44-0.58，远低于 monitor 所需的 domain-agnostic 标准。
    tables:
      - name: "Table 4: Cross-domain signal behavior comparison (WikiText vs PubMed)"
        description: >
          Rows: signal。Columns: WikiText ρ_6pt, PubMed ρ_6pt, rank_in_WikiText, rank_in_PubMed,
          ρ_preservation。Key finding: 信号强度排序在两个域之间不一致，practitioners 无法
          从一个域的经验推断另一个域应该监控哪个信号。
        data_preview:
          stable_rank: {wikitext_rho: 0.54, pubmed_rho: 0.43, wt_rank: 3, pm_rank: 4}
          spectral_entropy: {wikitext_rho: 0.61, pubmed_rho: 0.49, wt_rank: 2, pm_rank: 2}
          ppl: {wikitext_rho: 0.71, pubmed_rho: 0.60, wt_rank: 1, pm_rank: 1}
          token_entropy: {wikitext_rho: -0.68, pubmed_rho: -0.54, wt_rank: 2, pm_rank: 3}
          gradient_norm: {wikitext_rho: 0.19, pubmed_rho: -0.11, wt_rank: 5, pm_rank: 5}
    figures_description:
      - "Figure 4: PubMed vs WikiText severity curves side by side（paired panel）。同一 signal 在两个域上的 6-fraction 曲线叠加。视觉上可见 PubMed 曲线更平坦、inflection point 不同、token_entropy 在 PubMed 上的非单调 bump。"
      - "Figure 5: Token entropy 的 domain-specific 非单调行为。X=fraction, Y=token_entropy，PubMed 曲线在 50% 处有明显 upward bump，标注解释 biomedical jargon overfit 假说。"
    analysis: >
      PubMed 结果是 "failure modes" paper 的第二个核心证据：信号行为 domain-dependent，
      不存在 universal signal 选择策略。这直接回应了 SIGMA 等工作暗含的 domain-agnostic
      假设。在 reframed paper 中，这构成 "域敏感性" 分析的主要内容。
      单 seed 的限制在 worst tier 下反而不是问题——即使加 seed 也不会改善 ρ，因为底层
      问题是 signal behavior 的 domain dependency，不是 noise。

  # ============================================================
  # plan_003: Full FT comparison, 0.5B × 3 fractions × 1 seed
  # ============================================================
  - name: "Full fine-tuning comparison: 0.5B"
    plan_id: "plan_003"
    description: >
      Qwen2.5-0.5B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens，full fine-tuning。
      验证 QLoRA 结果是否是 adapter 特异的。
    expected_results:
      cross_frac_rho_spectral_stable_rank: 1.0
      cross_frac_rho_output_ppl: 1.0
      collapse_magnitude_ppl_100pct_fullft: "120x (vs QLoRA 53x)"
      collapse_speed_difference: "Full FT 在 gen2 即达到 QLoRA gen4 的 collapse 程度"
      stable_rank_100pct_gen4_fullft: 312.7
      stable_rank_100pct_gen4_qlora: 155.64
      ppl_100pct_gen4_fullft: 2847.3
      ppl_100pct_gen4_qlora: 839.2
      signal_ranking_match_with_qlora: "ranking 一致但 absolute 幅度差 2-3x"
      early_warning_separation_fullft: "58% at step 50 (vs QLoRA 34%)"
    result_rationale: >
      Full FT 更新所有参数（~0.5B），而 QLoRA 仅更新 ~1-2% 的参数。在 worst tier 下，
      Full FT 的 collapse 行为与 QLoRA 定量上差异巨大：(1) collapse 速度更快（更多参数
      可被 corrupted data 修改），gen2 full FT ≈ gen4 QLoRA；(2) 幅度更大（PPL 120x vs 53x），
      因为没有 frozen backbone 提供 inductive bias anchor；(3) spectral 信号变化更剧烈
      （stable rank 312 vs 155），因为所有 layer 的 weight matrix 均被修改。
      然而，n=3 fractions 下 ρ 仍然 trivially 1.0（与 MVP 相同的统计问题），这里虽然
      "看起来正常"但无法证明比 QLoRA 更好或更差。真正的问题是：如果 paper 声称信号是
      training-method agnostic 的，那么 absolute magnitude 差 2-3x 意味着任何 threshold-based
      的 monitoring strategy 都需要 per-method calibration，削弱 "practitioners guidance"
      的实用性。此外，Full FT 的更快 collapse 速度意味着 early warning window 虽然
      percentage 更大，但 absolute time 更短（因为有用的 training steps 更少），实际
      operational value 存疑。
    tables:
      - name: "Table 5: QLoRA vs Full FT signal comparison (0.5B, WikiText-2)"
        description: >
          Rows: metric (ppl, stable_rank, spectral_entropy, token_entropy, 每个 ×3 fractions)。
          Columns: QLoRA value, Full FT value, ratio。
          Key finding: 所有信号方向一致但幅度差 2-3x，threshold 不可迁移。
    figures_description:
      - "Figure 6: Full FT vs QLoRA collapse trajectories。Dual-panel, left=PPL across gens, right=stable_rank across gens。Full FT 曲线更陡峭，gen2 即超过 QLoRA gen4 水平。Shaded region 标注 'QLoRA 的 frozen backbone 延缓了 collapse'。"
    analysis: >
      Full FT 结果本身并不意外（更多可训参数 → 更快 collapse），但在 worst tier 的
      reframed paper 中增加了一个 failure mode dimension：monitoring threshold 对
      training method 敏感。同一 stable_rank 数值在 QLoRA 和 Full FT 下对应不同的
      severity level，使得 "one-size-fits-all" monitoring 策略不可行。
      作为 P1 experiment，这强化了 negative result 的全面性，但不改变核心叙事。

  # ============================================================
  # plan_004: Within-gen early warning on 1.5B
  # ============================================================
  - name: "Within-gen early warning analysis on 1.5B"
    plan_id: "plan_004"
    description: >
      对 plan_001 的 1.5B 数据做 within-generation 早期预警分析。
      计算 step 50/100/200/500 处各 fraction 的 signal deviation from 0% baseline。
    expected_results:
      early_warning_separation_100pct_step50: "12.1% ± 8.4%"
      early_warning_separation_75pct_step50: "4.3% ± 5.1%"
      early_warning_separation_50pct_step50: "2.1% ± 3.8%"
      early_warning_separation_100pct_step100: "16.8% ± 9.2%"
      early_warning_separation_100pct_step200: "21.4% ± 10.1%"
      earliest_reliable_detection_step: "step 200 (13% progress) for 100% only"
      fraction_detectable_at_3pct_progress: "仅 100% 在 1/3 seeds 上 separation >15%"
      cross_seed_agreement_step50: "1/3 seeds show >15% separation for 100%"
      detection_sensitivity_by_fraction: "10-50% fractions never reach 15% separation at any step"
    result_rationale: >
      0.5B MVP 中 3% progress 的 34.4% separation 是在 100% contamination + single seed 上
      观测的。1.5B 上这个信号大幅减弱，原因：(1) 1.5B 的更大容量意味着 early training steps
      中 gradient updates 分散在更多参数上，单个 layer 的 spectral structure 变化更小、
      更慢；(2) training steps 总数相同（1540）但每步更新的是 3x 多的参数，per-parameter
      update magnitude 更小；(3) QLoRA adapter 在 1.5B 上占 total parameters 比例更低
      （~0.7% vs ~1.5%），进一步稀释 early signal。
      关键 failure：step 50 时 separation 的 seed 间方差（±8.4%）与 signal 本身（12.1%）
      量级相当，CV≈0.7，说明 early warning 在 1.5B 上不 reproducible。仅 100% fraction
      在 step 200（13% progress）才 reliably 分离（>15% in 2/3 seeds），且中低 fraction
      （10-50%）在整个 training 过程中从未达到 reliable detection threshold。
      这意味着 "3% progress early warning" claim 是 0.5B-specific 的，不泛化到 1.5B。
    tables:
      - name: "Table 6: Early warning separation (%) by step, fraction, 1.5B (mean ± std, 3 seeds)"
        description: >
          Rows: fraction (10/25/50/75/100%)。Columns: step 50, step 100, step 200, step 500, final。
          每个 cell 是 stable_rank deviation % (mean ± std over seeds)。
          Key pattern: 仅右下角（100% × step 200+）有 consistent >15% separation，
          大部分 cells 的 std 接近或超过 mean。
        data_preview:
          frac_10pct: ["1.2±2.1", "2.0±2.8", "3.1±3.5", "4.2±4.0", "5.8±4.7"]
          frac_25pct: ["1.5±2.4", "2.8±3.1", "4.0±3.9", "5.5±4.6", "8.2±5.3"]
          frac_50pct: ["2.1±3.8", "3.5±4.2", "5.2±4.8", "7.1±5.4", "10.4±6.1"]
          frac_75pct: ["4.3±5.1", "6.8±5.7", "9.4±6.3", "13.2±7.1", "18.7±8.4"]
          frac_100pct: ["12.1±8.4", "16.8±9.2", "21.4±10.1", "28.3±11.5", "42.6±14.2"]
    figures_description:
      - "Figure 7: Early warning 在 0.5B vs 1.5B 上的对比。Dual-panel, X=training progress (%), Y=stable_rank deviation (%)。0.5B 在 3% progress 已有 34% separation (single line)；1.5B 有 3 条 seed lines + shaded mean±std，在 3% progress 时 lines 散布在 0-25% 之间，confidence band 跨越 detection threshold。"
      - "Figure 8: Detection reliability 热力图。X=training step, Y=fraction, color=P(separation>15% | 3 seeds)。仅右下角（100% × step 200+）为深色，大部分区域为白色或浅色。"
    analysis: >
      Early warning 是 MVP 中最 impressive 的 finding，但在 1.5B 上的 worst-tier 表现
      直接将其从 "generalizable finding" 降级为 "scale-specific observation"。
      在 reframed paper 中，这成为 failure mode #2："early warning signals 的 detection
      power 随模型规模下降" ——更大模型的容量冗余 delays signal emergence，恰恰在
      practitioners 最需要 early warning 的大模型场景下，信号最弱。
      这是一个强有力的 negative result：it says something important about why
      intuitive monitoring strategies fail at scale.

  # ============================================================
  # plan_005: Early warning threshold calibration / ROC
  # ============================================================
  - name: "Early warning threshold calibration & ROC analysis"
    plan_id: "plan_005"
    description: >
      对 plan_001 + plan_002 的全部数据做 ROC 分析：给定一个 signal deviation threshold，
      能否可靠区分 "will collapse" vs "safe" runs。
    expected_results:
      auc_stable_rank_1.5B_wikitext: 0.62
      auc_ppl_1.5B_wikitext: 0.68
      auc_stable_rank_1.5B_pubmed: 0.55
      auc_ppl_1.5B_pubmed: 0.58
      optimal_threshold_stable_rank: "无 —— 没有 threshold 同时在两个 domain 上 TPR>0.7 且 FPR<0.3"
      false_positive_rate_at_80pct_recall: "0.45 (WikiText), 0.61 (PubMed)"
      fraction_resolution: "binary (collapsed/not) 可行, severity grading 不可行"
    result_rationale: >
      ROC 分析需要足够的 positive/negative samples 和 clear decision boundary。Worst tier 下：
      (1) 定义 "will collapse" 本身就有问题——在 6 fractions 中，只有 75% 和 100% 有明确的
      end-state collapse，10-50% 的 final state 可能是 "mildly degraded" 而非 "collapsed"，
      binary label 的 assignment 就是 arbitrary 的。
      (2) 即使用 binary label（≥75% = positive），total sample size 小
      （6 fractions × 3 seeds × 5 gens = 90 trajectories for WikiText, 30 for PubMed），
      ROC 的 variance 大。
      (3) AUC 在 0.55-0.68 范围说明信号仅略好于 random（0.50），尤其在 PubMed 上接近 chance。
      (4) 不存在一个 universal threshold 同时适用于 WikiText 和 PubMed——因为 signal 的
      absolute scale 和 dynamic range 都是 domain-dependent 的（PubMed baseline 值不同、
      collapse 幅度不同），threshold 必须 per-domain calibration，消除了 practical utility。
      这意味着 "practitioners 可以设置一个 threshold 来监控 collapse" 的 operational story
      在 worst tier 下完全不成立。
    tables:
      - name: "Table 7: ROC analysis summary"
        description: >
          Rows: signal × domain。Columns: AUC, optimal threshold, TPR@FPR=0.2, FPR@TPR=0.8。
          Key: 所有 AUC < 0.70，no signal achieves TPR>0.7 at FPR<0.3 in both domains.
    figures_description:
      - "Figure 9: ROC curves by signal and domain。2×2 panel (signal × domain)。所有曲线紧贴对角线，PubMed 曲线几乎与对角线重合。标注 AUC 数值。"
    analysis: >
      ROC 分析是 "failure modes" paper 的 quantitative capstone：将 "signals don't work"
      从描述性观察提升为 formal detection theory 框架下的 conclusion。AUC 数字直接告诉
      读者这些信号作为 binary classifier 的 performance，比 Spearman ρ 更容易理解。
      在 reframed paper 中，这替代了原本 "practitioners 应该用 X 信号" 的 prescriptive
      结论，改为 "在这些条件下，没有信号组合达到 operational detection standards"。

  # ============================================================
  # plan_006: Signal taxonomy across severity
  # ============================================================
  - name: "Signal taxonomy across severity levels"
    plan_id: "plan_006"
    description: >
      利用 plan_001 数据，characterize 每个 signal family 在不同 severity level 的
      operating range：何处 informative、何处失效。
    expected_results:
      stable_rank_informative_range: "仅 100% fraction（step function behavior）"
      stable_rank_saturation_onset: "从 25% fraction 起即饱和（1.5B; 0.5B 在 50% 才开始）"
      spectral_entropy_informative_range: "75-100% fraction, gen2+"
      ppl_informative_range: "75-100% fraction（但 seed variance 大）"
      token_entropy_informative_range: "仅 100% fraction reliable"
      gradient_norm_behavior: "非单调: peaks at 50%, decreases at 75-100%"
      gradient_norm_usability: "不可用作 severity monitor——方向在 fraction 间不一致"
      hellaswag_acc_behavior: "所有 fraction 均在 25-27% 范围（~random），无 collapse signal"
      composite_signal_best_rho: 0.73
      composite_signal_description: "PCA on (ppl, token_entropy, spectral_entropy) 的 PC1"
      composite_vs_single_improvement: "marginal (+0.02 over ppl alone)"
    result_rationale: >
      (1) Stable rank 在 1.5B 上更早饱和（25% vs 50%），因为 1.5B 有更多冗余维度，
      中等 contamination 不足以改变 dominant singular value structure。从 25% 起，
      contaminated data 对 spectral structure 的影响被分散到大量 small singular values 中，
      stable rank（sum(σ)/max(σ)）的 numerator 和 denominator 同步缓慢增长，ratio 几乎不变。
      只有 100% contamination 的 distributional shift 足够大才能让 top singular value 显著变化。
      (2) Gradient norm 非单调的原因：50% 混合比时，模型同时收到 real 和 synthetic data 的
      conflicting gradients，gradient magnitude 增大（loss landscape 更 noisy）；
      75-100% 时合成数据占主导，gradients 变得 consistent 但指向 wrong minimum，
      magnitude 下降因为 loss landscape 变 "smooth"（但 degenerate）。
      (3) HellaSwag 在 0.5B 上本就接近 random（~25%），1.5B 上 baseline 约 40%，
      但 collapse 导致 ppl 增加 14.5x 时 HellaSwag 仅从 40% 降到 35%——downstream task
      对 perplexity-level collapse 不敏感，因为 HellaSwag 测试的是 commonsense reasoning
      能力，与 text generation diversity 部分解耦。
      (4) Composite signal (PCA PC1) 仅 marginal improvement，因为 ppl 和 token_entropy
      高度 correlated（r>0.9），加入 spectral_entropy 贡献的 orthogonal variance 很小。
      没有 "silver bullet" combination。
    tables:
      - name: "Table 8: Signal operating range matrix"
        description: >
          Rows: signal (stable_rank, spectral_entropy, ppl, token_entropy, gradient_norm, hellaswag)。
          Columns: informative_range (fraction %), failure_mode, ρ_6pt, recommendation。
          每个 signal 的 failure mode 用一句话概括（e.g., "saturates below 75%",
          "non-monotonic", "near-random at 0.5B scale"）。
        data_preview:
          stable_rank: {range: "100% only", failure: "step-function saturation from 25%", rho: 0.54, rec: "binary collapse detector only"}
          spectral_entropy: {range: "75-100%", failure: "insensitive below 75%", rho: 0.61, rec: "complement to output signals"}
          ppl: {range: "75-100% (noisy)", failure: "seed variance overwhelms signal in 10-50%", rho: 0.71, rec: "best single signal but insufficient alone"}
          token_entropy: {range: "100% only", failure: "non-monotonic on PubMed, high variance", rho: -0.68, rec: "unreliable as standalone"}
          gradient_norm: {range: "none", failure: "non-monotonic across fractions", rho: 0.19, rec: "do not use"}
          hellaswag: {range: "none at 0.5B, minimal at 1.5B", failure: "insensitive to generation-level collapse", rho: 0.31, rec: "do not use for collapse detection"}
      - name: "Table 9: Composite signal exploration"
        description: >
          Rows: signal combination method (PCA PC1, weighted sum, best-subset)。
          Columns: ρ_6pt mean, improvement over best single, cross-domain stable?。
          Key finding: no combination exceeds ρ=0.73, marginal over ppl alone (0.71).
    figures_description:
      - "Figure 10: Signal taxonomy 可视化。6-panel grid, 每个 panel 一个 signal。X=fraction, Y=normalized signal value (z-scored), 3 seed lines + mean。每个 panel 标注 'informative range' (green shading) 和 'failure zone' (red shading)。Visual summary of Table 8."
      - "Figure 11: Gradient norm 非单调性 deep dive。X=fraction, Y=gradient_norm, separate lines per generation。标注 50% peak 和 mechanistic 假说。"
    analysis: >
      Signal taxonomy 是 reframed paper 的 Figure 1 / Table 1 candidate——paper 的
      核心 visual contribution。在 worst tier 下，taxonomy 的结论从 "here's which signal
      to use when" 变为 "here's why no signal works across the full range"：每个信号都有
      blind spots，且 blind spots 的 union 覆盖了 practitioners 最需要 monitoring 的
      中等 contamination 区间（10-50%）。
      这是 reframed paper 的 Contribution (1) 的直接素材。

  # ============================================================
  # plan_007: Per-layer collapse analysis on 1.5B
  # ============================================================
  - name: "Per-layer collapse analysis: 1.5B"
    plan_id: "plan_007"
    description: >
      在 1.5B 模型上对所有 transformer layer 做 forward-pass SVD，分析 layer-level collapse
      patterns 在不同 fraction 和 generation 下的差异。
    expected_results:
      layer_collapse_order: "inconsistent across seeds"
      layer_collapse_order_seed1: "layers 20-24 (deeper) collapse first"
      layer_collapse_order_seed2: "layers 0-4 (embedding-adjacent) collapse first"
      layer_collapse_order_seed3: "layers 12-16 (middle) collapse first"
      per_layer_stable_rank_cv_across_seeds: 0.38
      most_affected_layers_100pct_gen4: "varies by seed; no consistent pattern"
      layer_level_vs_aggregate_correlation: 0.41
      layer_collapse_speed_1.5B_vs_0.5B: "1.5B 没有 consistent layer-wise gradient; 0.5B 有 clear top-down pattern"
    result_rationale: >
      0.5B 上 per-layer analysis 可能显示 clear pattern（e.g., deeper layers collapse first）
      因为模型小、layer 数少（24 layers），每个 layer 的 "responsibility" 更明确。
      1.5B 有 28 layers，且 capacity redundancy 意味着 collapse 可以通过多条"路径"
      在不同 layer 发生，具体路径取决于：(a) weight initialization seed 决定哪些 layer
      的 spectral structure 最 fragile；(b) data sampling order 决定哪些 layer 最先
      收到 conflicting gradients；(c) QLoRA adapter 的 random initialization 引入
      additional stochasticity。
      结果是 layer-level collapse pattern 在 3 seeds 间高度不一致（CV=0.38），
      没有 "universal layer-wise collapse signature"。Aggregate-level signal（whole-model
      stable rank）与 per-layer pattern 的相关性仅 0.41，说明 aggregate 信号丢失了
      layer-level 信息，但 layer-level 信息本身也不 reproducible。
      这削弱了 "per-layer monitoring" 作为 practical tool 的价值——如果 collapse 的
      layer-level manifestation 是 stochastic 的，practitioners 不能 a priori 选择
      哪些 layers 来监控。
    tables:
      - name: "Table 10: Per-layer collapse patterns, 1.5B, 100% fraction, gen4"
        description: >
          Rows: layer group (0-6, 7-13, 14-20, 21-27)。Columns: seed 1/2/3 stable_rank,
          seed 1/2/3 spectral_entropy, mean CV。
          Key: CV 在 0.25-0.50 范围，layer group ranking 不 consistent across seeds。
    figures_description:
      - "Figure 12: Per-layer stable rank heatmap, 1.5B, 3 seeds side by side。X=layer, Y=generation, color=stable_rank deviation from gen0。3 个 panel 显示截然不同的 spatial pattern，visually demonstrate irreproducibility。"
      - "Figure 13: 0.5B vs 1.5B per-layer comparison。0.5B 有相对 clear 的 gradient (deeper→more collapsed)；1.5B 无 consistent pattern。Side-by-side heatmaps。"
    analysis: >
      Per-layer analysis 在 worst tier 下从 "potential Figure 3" 变为 "additional
      negative evidence"：不仅 aggregate signals 不 reliable，layer-level signals
      也不 reproducible。这强化了 seed variance / reproducibility 的 narrative thread，
      并补充 Contribution (3)——single-seed per-layer analysis 尤其 misleading，
      因为任何单 seed 都会显示一个 "convincing" but non-reproducible pattern。

  # ============================================================
  # plan_008: Self-recovery deep dive
  # ============================================================
  - name: "Self-recovery phenomenon analysis"
    plan_id: "plan_008"
    description: >
      对 plan_001 数据中 25/50/75% fraction 的 recovery pattern 做 multi-seed 分析：
      50% contamination 的 partial self-recovery 是否 reproducible。
    expected_results:
      self_recovery_definition: "gen N+1 signal value improves toward baseline relative to gen N"
      self_recovery_detected_50pct_seed1: true
      self_recovery_detected_50pct_seed2: false
      self_recovery_detected_50pct_seed3: false
      self_recovery_reproducibility_50pct: "1/3 seeds (33%)"
      self_recovery_detected_25pct: "0/3 seeds"
      self_recovery_detected_75pct: "0/3 seeds"
      recovery_magnitude_when_detected: "PPL improves by 8% from gen2 to gen3 in seed 1"
      recovery_statistical_significance: "not significant (p=0.42, permutation test)"
      conclusion: "判定为 noise/artifact，不纳入 paper"
    result_rationale: >
      MVP 中 50% fraction 的 self-recovery 是 single-seed 观测，在 worst tier 下这被
      揭示为 noise：(1) 仅 1/3 seeds 复现（33%），低于 majority replication 标准；
      (2) recovery 的 magnitude 小（PPL 8% improvement）相对于 seed 间 variance
      （CV~0.28），不能排除 random fluctuation；(3) 25% 和 75% fraction 均未显示
      recovery，说明 50% 并非特殊的 "mixed regime"——如果 real/synthetic 的 balance
      真的产生 recovery，应该在 adjacent fractions 也有 weaker 版本；(4) permutation
      test（shuffle gen labels within fraction）给出 p=0.42，远未达到任何合理 significance
      threshold。
      Self-recovery 从 "novel finding" 变为 "cautionary tale about single-seed claims"——
      在 reframed paper 中不提 self-recovery 本身，但用其作为 seed variance discussion 的
      illustrative example。
    tables:
      - name: "Table 11: Self-recovery replication test"
        description: >
          Rows: fraction (25/50/75%)。Columns: seed 1/2/3 recovery detected (Y/N),
          recovery magnitude (%), p-value (permutation test)。
          Key: 仅 50% seed 1 显示 recovery，p=0.42 not significant。
    figures_description:
      - "Figure (supplementary): Self-recovery non-replication。50% fraction PPL across gens, 3 seed lines。Seed 1 shows gen2→gen3 dip (annotated)，seeds 2,3 monotonically increase。Illustrates single-seed misleadingness。"
    analysis: >
      Self-recovery 的非复现是 worst tier narrative 的一个 clean example：
      MVP 的 single-seed setup 产生了一个 compelling 但 spurious pattern。
      在 reframed paper 中，这不作为独立发现呈现，而是作为 Contribution (3)
      （seed variance / reproducibility 分析）中的 case study：
      "A pattern observed in a single seed (partial self-recovery at 50% contamination)
      failed to replicate in 2 out of 3 additional seeds (p=0.42), illustrating the
      danger of over-interpreting single-seed experiments in collapse studies."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4bf82d8-e6b9-4ec1-bbd5-284b38281f92",
  "isSidechain": false,
  "requestId": "req_011Cb399R6z7QBhW3Y7R7kmR",
  "type": "assistant",
  "uuid": "5f262265-2ce4-4109-8662-60fa56a5b38d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZxDy76hXecuVsULfMnPhD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10886,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13065,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13065,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10886
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：6 fractions 打破核心相关性、跨域/跨规模泛化失败、或多 seed 方差过大导致原始 framing 不可用，需 reframe 核心假设：['6 fractions 下 spectral 信号 ρ <0.70（饱和 + 非单调导致），output 信号 ρ 降至 0.65-0.75', '1.5…",
  "leafUuid": "5f262265-2ce4-4109-8662-60fa56a5b38d",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical study of training signal robustness for collapse detection",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：6 fractions 打破核心相关性、跨域/跨规模泛化失败、或多 seed 方差过大导致原始 framing 不可用，需 reframe 核心假设：['6 fractions 下 spectral 信号 ρ <0.70（饱和 + 非单调导致），output 信号 ρ 降至 0.65-0.75', '1.5…",
  "leafUuid": "5f262265-2ce4-4109-8662-60fa56a5b38d",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Systematic empirical study of training signal robustness for collapse detection",
  "sessionId": "ea91b0f3-c3d3-4728-a72d-3df599762220"
}
```

---
