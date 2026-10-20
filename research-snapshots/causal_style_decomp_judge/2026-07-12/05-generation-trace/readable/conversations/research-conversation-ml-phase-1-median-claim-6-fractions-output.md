# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心相关性成立但不完美，部分信号/域/规模出现退化，需调整 claim 强度和补充分析 核心假设：['6 fractions 下 output 信号

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/880e8550-bcef-4ebb-806e-92c4749f8a60.jsonl`
- **Structured JSON:** [`80cccb3f7645deab4e98.json`](../../sessions/80/80cccb3f7645deab4e98.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-14T21:00:47.876Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-14T21:00:47.876Z",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心相关性成立但不完美，部分信号/域/规模出现退化，需调整 claim 强度和补充分析\n核心假设：['6 fractions 下 output 信号 ρ 保持 ≥0.80，但 spectral 信号 ρ 降至 0.70-0.85（stable rank 饱和拉低）', '1.5B 定性一致但 collapse 动态更快或更慢，early warning 阈值需重新校准', 'PubMed 跨域 ρ 下降至 0.65-0.80，部分信号（如 gradient norm）跨域失效', '50% self-recovery 在 1-2/3 seeds 中复现，效应不稳定但方向一致', 'stable rank 饱和区间宽（50%→100% 均饱和），Claim 1 需限定 spectral 信号有效范围', 'early warning 在 1.5B 上延迟至 5-10% training progress，或分离度降至 15-25%', 'seed 方差中等，个别 config 置信区间宽但不跨零']\n关键指标范围：{'cross_frac_rho_spectral_6pt': [0.7, 0.89], 'cross_frac_rho_output_6pt': [0.8, 0.94], 'cross_gen_rho_spectral': [0.7, 0.89], 'early_warning_separation_3pct_progress': [12.0, 25.0], 'self_recovery_reproducibility': [0.33, 0.67], 'cross_domain_rho_preservation': [0.65, 0.84], 'cross_scale_rho_preservation': [0.7, 0.89], 'ppl_collapse_magnitude_100pct_gen4': [20.0, 50.0], 'seed_variance_cv_key_metrics': [0.1, 0.25]}\n叙事方向：Claim 1 从 \"reliably track\" 软化为 \"output signals reliably track; spectral signals track within their non-saturated regime\"。需增加 per-signal operating range 表格作为核心贡献（哪个信号在哪个 severity 区间最可靠）。Claim 2 的 early warning 从 \"3% progress\" 调整为 \"≤10% progress\"，依然有实用价值但 headline 弱化。Claim 3 成为论文最强贡献——signal taxonomy 的实用性反而因 信号表现分化而增强。Self-recovery 降级为 observation 段落而非 headline finding（reproducibility 不足以做强 claim）。PubMed 结果作为 \"partial generalization\" 讨论，supplementary 放完整数据。论文重心从 \"universal monitoring\" 转向 \"practitioners' guide to signal selection\"。NeurIPS Datasets & Benchmarks 投稿，main track 风险较大。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: collapse_severity_monitor\nfocus: 重点关注：(1) analysis paper 定位是否成立——3 个 claim 是否足够支撑 A 类投稿；(2) n=3 fractions 统计效力弱点在 6 fractions 扩展后是否解决；(3) 50pct self-recovery 作为 novel finding 的说服力；(4) stable rank 饱和是否削弱 Claim 1\n\n## paper_framing.md\n\n# Paper Framing — collapse_severity_monitor\n\n## Target Venue\n- Primary: NeurIPS 2026 (Datasets & Benchmarks / Main)\n- Backup: ICLR 2027\n- Deadline: NeurIPS 2026 abstract ~late May 2026, full paper ~early June 2026\n\n## Core Claims (3 条)\n\n1. **Signal-Severity Correlation**: Spectral signals (stable rank, spectral entropy) and output signals (token entropy, perplexity) reliably track model collapse severity across synthetic data contamination levels, with cross-fraction Spearman ρ=1.0 across all generations.\n\n2. **Early Warning Capability**: Collapse can be detected as early as 3% training progress (step 50/1540) via stable rank deviation (34.4% for 100% synthetic), enabling training-time early warning before catastrophic degradation materializes.\n\n3. **Non-Uniform Signal Behavior**: Different signal families exhibit qualitatively different responses to collapse — spectral signals saturate at extreme severity, gradient norm is non-monotonic, downstream task metrics (HellaSwag) fail to detect collapse at small model scale. This taxonomy of signal behavior provides actionable guidance for practitioners choosing monitoring strategies.\n\n## Story Spine\n\n- **Problem**: Model collapse from iterative training on synthetic data is a growing concern as LLM-generated text pervades training corpora. While the phenomenon is well-characterized theoretically (Shumailov et al. 2024, Alemohammad et al. 2024), practitioners lack actionable tools to detect and quantify collapse severity during training. Current work focuses on post-hoc analysis or output-level detection, missing the rich signal available in training dynamics.\n\n- **Existing approaches & gaps**: SIGMA (2025) monitors output embedding spectral properties but requires access to a clean reference distribution. Kalinowski (2024) uses topological analysis but is computationally expensive. Neither provides a systematic comparison of which training-time signals best track collapse across severity levels, nor do they examine within-generation temporal dynamics for early warning.\n\n- **Our framing**: We conduct the first systematic analysis of training dynamic signals as collapse severity monitors. Across 4 signal families (spectral, output, gradient, downstream) × multiple contamination levels × generational iterations, we characterize which signals track collapse, when they diverge, and where they fail. Key insight: spectral signals provide the earliest warning (3% progress) while output signals provide the most reliable severity tracking. The 50% contamination regime reveals a partial self-recovery phenomenon not previously documented.\n\n- **Headline result template**: \"Stable rank deviation detects model collapse at 3% training progress with 34% signal separation, while token entropy and perplexity maintain monotonic severity tracking across 5 generational iterations with ρ=1.0. We identify a previously unreported self-recovery pattern at moderate contamination levels.\"\n\n## Anticipated Reviewer Concerns & Mitigation\n\n| Concern | Severity | Mitigation Experiment |\n|---------|----------|----------------------|\n| Single model (Qwen-0.5B) — can't generalize | HIGH | P0: 1.5B model, P1: cross-architecture (if GPU permits) |\n| Single dataset (WikiText-2) — domain-specific | HIGH | P0: PubMed domain, P1: code domain |\n| Single seed — no variance estimates | HIGH | P0: 3 seeds per config |\n| n=3 fractions — Spearman ρ trivially 1.0 | HIGH | P0: 6 fractions (0/10/25/50/75/100%) |\n| QLoRA only — not representative of full FT | MEDIUM | P1: Full FT comparison on 1 config |\n| \"Not a monitoring system\" — analysis only | LOW | Frame as analysis paper; early warning finding adds practical value |\n| No intervention/mitigation experiments | LOW | Explicit non-goal; frame as \"diagnostic\" contribution, mitigation as future work |\n| Stable rank saturates — limited as severity tracker | LOW | Claim 3 explicitly addresses signal limitations as finding |\n\n## Core Insight (一句话)\n\nTraining dynamic signals provide a free, model-agnostic early warning system for model collapse — but different signal families have distinct operating ranges, and practitioners need to know which signal to trust at which severity level.\n\n## Novelty Statement\n\nNo prior work systematically compares multiple training-time signal families as collapse severity monitors across contamination levels. The within-generation early warning capability (3% progress) and the self-recovery phenomenon at moderate contamination are novel empirical contributions.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  claim: 1\n  description: 'Scale validation: 1.5B model (Qwen2.5-1.5B) × WikiText-2 × 6 fractions\n    (0/10/25/50/75/100%) × 3 seeds. Core experiment proving signal-severity correlation\n    generalizes beyond 0.5B MVP.'\n  priority: P0\n  gpu_budget_hours: 90\n  deps: []\n  registry_id: null\n  notes: 6 fractions × 3 seeds × 5 gens = 90 runs. ~1h/run on A6000 for 1.5B QLoRA.\n  status: planned\n- id: plan_002\n  claim: 1\n  description: 'Cross-domain validation: 1.5B × PubMed × 6 fractions × 1 seed. Proves\n    signals generalize beyond WikiText to biomedical domain.'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Only 1 seed; if results diverge from WikiText, add 2 more seeds.\n  status: planned\n- id: plan_003\n  claim: 1\n  description: 'Full FT comparison: 0.5B × WikiText-2 × 3 fractions (0/50/100%) ×\n    1 seed with full fine-tuning. Validates signals are not QLoRA-specific.'\n  priority: P1\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: null\n  notes: Full FT on 0.5B should fit in single A6000 24GB.\n  status: planned\n- id: plan_004\n  claim: 2\n  description: Within-gen early warning analysis on 1.5B data. Compute signal divergence\n    at step 50/100/200/500 across all fractions and seeds from plan_001. Pure analysis,\n    no GPU.\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Extends MVP within-gen analysis to 1.5B with proper statistics.\n  status: planned\n- id: plan_005\n  claim: 2\n  description: 'Early warning threshold calibration: determine minimum signal deviation\n    that reliably predicts end-of-generation collapse. ROC analysis across all configs.'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_002\n  registry_id: null\n  notes: Analysis only. Need sufficient runs for meaningful ROC.\n  status: planned\n- id: plan_006\n  claim: 3\n  description: 'Signal taxonomy across severity levels. Using plan_001 data, characterize\n    per-signal-family operating ranges: where each signal is most/least informative.'\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Core table/figure for Claim 3. Shows stable_rank saturation, gradient non-monotonicity,\n    downstream failure.\n  status: planned\n- id: plan_007\n  claim: 3\n  description: 'Per-layer collapse analysis: run forward-pass SVD on 1.5B model across\n    gens to show which layers collapse first and how layer-level patterns differ by\n    severity.'\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Extends MVP per-layer analysis to 1.5B. Figure 3 candidate.\n  status: planned\n- id: plan_008\n  claim: 3\n  description: 'Self-recovery phenomenon deep dive: 50% contamination partial recovery\n    analysis. Is it consistent across seeds? At what fraction does recovery disappear?'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: null\n  notes: Analysis of plan_001 data at 25/50/75% fractions.\n  status: planned\n- id: plan_mvp_001\n  claim: 1\n  description: 'MVP: 0.5B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens'\n  priority: P0\n  gpu_budget_hours: 14.1\n  deps: []\n  registry_id: mvp_frac0\n  notes: Control baseline. DONE.\n  status: DONE\n  conclusion: success\n- id: plan_mvp_002\n  claim: 1\n  description: 'MVP: 0.5B × WikiText-2 × 50pct + 100pct × 1 seed × 5 gens'\n  priority: P0\n  gpu_budget_hours: 14.1\n  deps: []\n  registry_id: mvp_frac50_100\n  notes: Main MVP experiment. DONE. Gate check 2/3 PASS.\n  status: DONE\n  conclusion: success\n  metrics:\n    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5\n    gate_check_verdict: PASS (2/3 families)\n    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen\n      rho=0.9 (p=0.037)\n    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;\n      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0\n    gate_check_downstream: FAIL — no hellaswag_acc data (data gap, not signal failure)\n    final_values_0pct_gen4:\n      stable_rank: 23.41\n      spectral_entropy: 0.703\n      token_entropy: 2.259\n      ppl: 15.67\n    final_values_50pct_gen4:\n      stable_rank: 24.79\n      spectral_entropy: 0.716\n      token_entropy: 2.215\n      ppl: 16.95\n    final_values_100pct_gen4:\n      stable_rank: 155.64\n      spectral_entropy: 0.884\n      token_entropy: 0.782\n      ppl: 839.2\n    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%\n    0pct_baseline_stability: all signals <3% variation across 5 gens\n    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training\n      progress)\n- id: plan_mvp_003\n  claim: 2\n  description: MVP within-gen temporal analysis on 0.5B data\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_mvp_002\n  registry_id: within_gen_analysis\n  notes: DONE. Early warning at 3% progress confirmed.\n  status: orphaned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_collapse_001\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    progress: 0pct_gen0 step 242/1540 (15.7%)\n    speed: 1.19 it/s\n    loss: 2.652\n    perplexity: 14.41\n    stable_rank: 20.5\n    spectral_entropy: 0.673\n    signals_collected: 4\n    checked_at: '2026-05-14T06:38:30Z'\n- exp_id: mvp_collapse_002\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct_gen0 step 50/1540 (3%)\n    speed: 1.17 it/s\n    gpu_util: 26%\n    gpu_mem: 6314/32607 MiB\n    gen_batch_size: 32\n    gen_num_chunks: 1500\n    checked_at: '2026-05-14T08:21:00Z'\n- exp_id: mvp_collapse_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct_gen0 step 50/1540 (3%)\n    speed: 1.08 it/s\n    gpu_util: 20%\n    gpu_mem: 6314/32607 MiB\n    checked_at: '2026-05-14T09:01:30Z'\n- exp_id: mvp_frac50_100\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    progress: ALL COMPLETE — 0pct 5/5, 50pct 5/5, 100pct 5/5\n    gate_check_verdict: PASS (2/3 families)\n    gate_check_spectral: PASS — stable_rank cross-frac |rho|=1.0 (p=0.0), cross-gen\n      rho=0.9 (p=0.037)\n    gate_check_output: PASS — perplexity cross-frac |rho|=1.0, cross-gen rho=1.0;\n      token_entropy cross-frac |rho|=0.9, cross-gen rho=-1.0\n    gate_check_downstream: FAIL — no hellaswag_acc data (data gap, not signal failure)\n    final_values_0pct_gen4:\n      stable_rank: 23.41\n      spectral_entropy: 0.703\n      token_entropy: 2.259\n      ppl: 15.67\n    final_values_50pct_gen4:\n      stable_rank: 24.79\n      spectral_entropy: 0.716\n      token_entropy: 2.215\n      ppl: 16.95\n    final_values_100pct_gen4:\n      stable_rank: 155.64\n      spectral_entropy: 0.884\n      token_entropy: 0.782\n      ppl: 839.2\n    collapse_magnitude_100pct: stable_rank 6.6x, PPL 53x, token_entropy -65%\n    0pct_baseline_stability: all signals <3% variation across 5 gens\n    within_gen_early_warning: stable_rank 34.4% deviation at step 50 (3% training\n      progress)\n- exp_id: mvp_frac0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: per_layer_analysis\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_v2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics:\n    progress: 0pct gen0 1388/1540 (90%), ~2min to finish gen0\n    output_file: outputs/per_layer_analysis.json (incremental save per gen)\n    per_gen_time: ~35 min/gen\n    total_gens: 2 fractions x 5 gens = 10 gens\n    eta_total: ~6h from start (started ~18:19 UTC)\n    signals_safety: 'confirmed: output_dir redirected to _per_layer_tmp, signals_*.jsonl\n      untouched'\n    analysis_method: 'hook all transformer layers, 64 val samples forward pass, compute\n      per-layer SVD: stable_rank, spectral_entropy, SV_ratio(sigma1/sigma2)'\n    gpu: GPU 1, 6314/32607 MiB, 43% util\n    checked_at: '2026-05-14T18:58:00Z'\n- exp_id: per_layer_analysis_v3\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_active\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics:\n    progress: 0pct gen0=done, 0pct gen1=in_progress\n    per_gen_time: ~35 min/gen\n    eta_remaining: ~9 gens x 35min = ~5.25h\n    gpu: cuda:1\n    checked_at: '2026-05-14T19:08:00Z'\n- exp_id: per_layer_analysis_v4\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: per_layer_analysis_v5\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-14T21:00:47.880Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-14T21:00:47.880Z",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-14T21:00:47.901Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心相关性成立但不完美，部分信号/域/规模出现退化，需调整 claim 强度和补充分析
核心假设：['6 fractions 下 output 信号 ρ 保持 ≥0.80，但 spectral 信号 ρ 降至 0.70-0.85（stable rank 饱和拉低）', '1.5B 定性一致但 collapse 动态更快或更慢，early warning 阈值需重新校准', 'PubMed 跨域 ρ 下降至 0.65-0.80，部分信号（如 gradient norm）跨域失效', '50% self-recovery 在 1-2/3 seeds 中复现，效应不稳定但方向一致', 'stable rank 饱和区间宽（50%→100% 均饱和），Claim 1 需限定 spectral 信号有效范围', 'early warning 在 1.5B 上延迟至 5-10% training progress，或分离度降至 15-25%', 'seed 方差中等，个别 config 置信区间宽但不跨零']
关键指标范围：{'cross_frac_rho_spectral_6pt': [0.7, 0.89], 'cross_frac_rho_output_6pt': [0.8, 0.94], 'cross_gen_rho_spectral': [0.7, 0.89], 'early_warning_separation_3pct_progress': [12.0, 25.0], 'self_recovery_reproducibility': [0.33, 0.67], 'cross_domain_rho_preservation': [0.65, 0.84], 'cross_scale_rho_preservation': [0.7, 0.89], 'ppl_collapse_magnitude_100pct_gen4': [20.0, 50.0], 'seed_variance_cv_key_metrics': [0.1, 0.25]}
叙事方向：Claim 1 从 "reliably track" 软化为 "output signals reliably track; spectral signals track within their non-saturated regime"。需增加 per-signal operating range 表格作为核心贡献（哪个信号在哪个 severity 区间最可靠）。Claim 2 的 early warning 从 "3% progress" 调整为 "≤10% progress"，依然有实用价值但 headline 弱化。Claim 3 成为论文最强贡献——signal taxonomy 的实用性反而因 信号表现分化而增强。Self-recovery 降级为 observation 段落而非 headline finding（reproducibility 不足以做强 claim）。PubMed 结果作为 "partial generalization" 讨论，supplementary 放完整数据。论文重心从 "universal monitoring" 转向 "practitioners' guide to signal selection"。NeurIPS Datasets & Benchmarks 投稿，main track 风险较大。


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
tier: median
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
  "promptId": "1846eb06-5735-4548-99bf-f47ff2906519",
  "type": "user",
  "uuid": "9a01eda9-be38-4149-87ab-c98cddfc61b4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-14T21:00:47.900Z_

```json
{
  "parentUuid": "9a01eda9-be38-4149-87ab-c98cddfc61b4",
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
  "uuid": "e90f3578-c496-4a27-914b-c7b92ec66f77",
  "timestamp": "2026-05-14T21:00:47.900Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-14T21:00:47.900Z_

```json
{
  "parentUuid": "e90f3578-c496-4a27-914b-c7b92ec66f77",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5ec3b34a-b1b0-41e7-add8-622cfcba27e6",
  "timestamp": "2026-05-14T21:00:47.900Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心相关性成立但不完美，部分信号/域/规模出现退化，需调整 claim 强度和补充分析 核心假设：['6 fractions 下 output 信号 ρ 保持 ≥0.80，但 spectral 信号 ρ 降至 0.70-0.85（stable rank 饱和拉低）', '1.5B 定性一致但 collap…",
  "leafUuid": "5ec3b34a-b1b0-41e7-add8-622cfcba27e6",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Collapse severity monitoring with partial signal generalization",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60"
}
```

---

### Assistant

_source line 8 · 2026-05-14T21:01:04.942Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined/predicted experimental results for all "planned" experiments in the experiment plan, under the "median" tier assumptions. Each prediction needs a result_rationale explaining why those results would occur under this tier.

Let me carefully go through each planned experiment and generate median-tier predictions based on the defined characteristics.

The planned experiments are:
- plan_001: 1.5B × WikiText-2 × 6 fractions × 3 seeds


- plan_002: 1.5B × PubMed × 6 fractions × 1 seed
- plan_003: Full FT × 0.5B × WikiText-2 × 3 fractions × 1 seed
- plan_004: Within-gen early warning on 1.5B data (analysis)
- plan_005: Early warning threshold calibration / ROC (analysis)
- plan_006: Signal taxonomy table (analysis)
- plan_007: Per-layer collapse analysis on 1.5B
- plan_008: Self-recovery deep dive (analysis)

Now I'm working through how the median tier assumptions map onto expected outcomes for each of these experiments, considering factors like model size, dataset characteristics, and the specific analyses being performed. I need to see the next thinking to rewrite it. You've provided the current rewritten thinking and instructions, but the "next thinking" section appears to be empty or cut off. Could you share the next thinking that needs to be rewritten?
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ec3b34a-b1b0-41e7-add8-622cfcba27e6",
  "isSidechain": false,
  "requestId": "req_011Cb38nHGMsZg95TbW4dNpq",
  "type": "assistant",
  "uuid": "ed11e643-47a4-4ebb-92c6-d9a7b1a5b512",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KjyqiswN3E2QWKBasqaYm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10834,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13302,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10834
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

_source line 9 · 2026-05-14T21:05:32.212Z_

```yaml
tier: median
narrative_guidance: >
  论文重心从 "universal monitoring framework" 转向 "practitioner's guide to signal selection"。
  Claim 1 软化为 "output signals reliably track; spectral signals track within non-saturated regime"，
  核心贡献变为 per-signal operating range 表格。Claim 2 early warning 从 "3% progress" 放宽至 "≤10% progress"，
  仍有实用价值但 headline 弱化。Claim 3 因信号分化而增强——signal taxonomy 成为最强贡献。
  Self-recovery 降级为 observation 段落。PubMed 作为 partial generalization 讨论。
  投稿定位 NeurIPS Datasets & Benchmarks，main track 风险大。

imagined_experiments:
  - name: "1.5B Scale Validation (6 fractions × 3 seeds)"
    plan_id: "plan_001"
    description: >
      Qwen2.5-1.5B × WikiText-2 × 6 fractions (0/10/25/50/75/100%) × 3 seeds × 5 generations。
      核心实验，验证 signal-severity correlation 在更大模型和更密集 fraction 采样下的泛化性。
    expected_results:
      cross_frac_rho_output_6pt_mean: 0.89
      cross_frac_rho_output_6pt_range: "[0.86, 0.93]"
      cross_frac_rho_spectral_6pt_mean: 0.78
      cross_frac_rho_spectral_6pt_range: "[0.71, 0.85]"
      cross_gen_rho_spectral_mean: 0.78
      cross_gen_rho_output_mean: 0.88
      ppl_0pct_gen4_mean: 12.5
      ppl_50pct_gen4_mean: 14.8
      ppl_100pct_gen4_mean: 420.0
      ppl_collapse_magnitude_100pct_gen4: 33.6
      stable_rank_0pct_gen4: 28.5
      stable_rank_50pct_gen4: 31.2
      stable_rank_75pct_gen4: 98.0
      stable_rank_100pct_gen4: 105.0
      token_entropy_0pct_gen4: 2.45
      token_entropy_50pct_gen4: 2.38
      token_entropy_100pct_gen4: 0.92
      spectral_entropy_0pct_gen4: 0.72
      spectral_entropy_100pct_gen4: 0.87
      seed_variance_cv_ppl: 0.14
      seed_variance_cv_stable_rank: 0.18
      seed_variance_cv_token_entropy: 0.11
      gradient_norm_monotonic: false
      hellaswag_acc_0pct: 0.38
      hellaswag_acc_100pct: 0.35
      hellaswag_sensitivity: "weak — <10% drop even at 100% contamination for 1.5B"
    result_rationale: >
      Output signals (PPL, token entropy) 在 6-point fraction 上仍保持强单调性，因为它们直接反映
      生成分布退化，这一机制与 fraction 采样密度和模型规模无关。ρ 从 MVP 的 1.0 降至 ~0.89，
      主要因为 6 点采样引入了 10% 和 25% 两个低 severity 点，这些点的 signal 变化很小，
      noise 占比增大，拉低了 rank correlation。

      Spectral signals (stable rank) 的 ρ 显著下降至 ~0.78，核心原因是 stable rank 在
      75%→100% 区间饱和——1.5B 模型有更多参数，weight matrix 维度更高，当 collapse 严重时
      singular value 分布趋于极端集中，stable rank 在 75% 和 100% 给出接近的值（98 vs 105），
      破坏了高 severity 端的单调排序。这个饱和效应在 0.5B 上也存在（155.64 at 100%）但
      6-point 采样让它对 ρ 的拖累更明显。

      PPL collapse magnitude (~34x) 低于 0.5B 的 53x，因为 1.5B 模型有更大的参数容量，
      QLoRA 微调影响的参数比例更小（adapter 占总参数比下降），collapse 的绝对幅度被缓冲。
      但方向完全一致——PPL 仍然单调上升。

      Seed variance CV 0.14-0.18 属于中等水平。Stable rank 的 CV 最高（0.18）因为它对
      initialization 和 learning rate 的随机性更敏感——不同 seed 下 weight matrix 的
      spectral structure 演化路径有差异，而 output metrics 是对整个模型行为的聚合，
      天然平滑了 seed 间差异。

      Gradient norm 在 1.5B 上依然非单调（中等 severity 上升，高 severity 反而下降或持平），
      因为 QLoRA adapter 的梯度在 collapse 后期被 loss landscape 的平坦区域压低。
      HellaSwag 在 1.5B 上比 0.5B 好（0.38 baseline），但 collapse sensitivity 依然弱，
      因为 HellaSwag 测试的是 commonsense reasoning，这个能力在 1.5B 规模上更多依赖
      pretrained weights 而非 fine-tuned distribution，collapse 主要影响 generation quality
      而非 discriminative reasoning。
    tables:
      - name: "Table 1: Cross-fraction Spearman ρ by signal family (1.5B, 6 fractions, mean ± std over 3 seeds)"
        columns: ["Signal", "Gen 0", "Gen 1", "Gen 2", "Gen 3", "Gen 4", "Mean"]
        rows:
          - ["Stable Rank", "0.83±0.06", "0.80±0.08", "0.77±0.09", "0.74±0.10", "0.71±0.11", "0.77±0.05"]
          - ["Spectral Entropy", "0.86±0.05", "0.83±0.06", "0.80±0.07", "0.77±0.08", "0.74±0.09", "0.80±0.05"]
          - ["Token Entropy", "0.94±0.03", "0.91±0.04", "0.89±0.04", "0.87±0.05", "0.86±0.05", "0.89±0.03"]
          - ["Perplexity", "0.94±0.02", "0.93±0.03", "0.91±0.03", "0.89±0.04", "0.87±0.05", "0.91±0.03"]
          - ["Gradient Norm", "0.60±0.15", "0.54±0.18", "0.49±0.20", "0.43±0.22", "0.37±0.25", "0.49±0.09"]
          - ["HellaSwag Acc", "0.43±0.12", "0.37±0.15", "0.31±0.18", "0.26±0.20", "0.20±0.22", "0.31±0.09"]
      - name: "Table 2: Seed variance (CV) by signal × fraction"
        columns: ["Signal", "10%", "25%", "50%", "75%", "100%"]
        rows:
          - ["PPL", "0.08", "0.10", "0.12", "0.15", "0.18"]
          - ["Token Entropy", "0.05", "0.07", "0.09", "0.12", "0.14"]
          - ["Stable Rank", "0.10", "0.13", "0.16", "0.20", "0.22"]
          - ["Spectral Entropy", "0.06", "0.08", "0.11", "0.15", "0.19"]
    figures_description:
      - "Fig 1: 6-panel grid (one per generation), x-axis = fraction, y-axis = signal value (normalized). Output signals 保持平滑单调曲线；stable rank 在 75-100% 区间曲线变平（饱和）；gradient norm 呈倒 U 形。每条曲线带 3-seed 的 shaded error band。"
      - "Fig 2: Heatmap — signal × fraction × generation，颜色编码 signal 变化幅度相对 0% baseline 的 z-score。清晰显示 output signals 在全域有效、spectral signals 在 >50% 区间饱和的 pattern。"
    analysis: >
      6 fractions 将 MVP 的 trivial ρ=1.0（3 点必然完美排序）升级为统计上有意义的 correlation。
      Output signals 的 ρ≈0.89 在 6 点 Spearman 检验中 p<0.05（临界值 ~0.83），可做显著性声明。
      Spectral signals 的 ρ≈0.78 处于 p≈0.06-0.08 的边缘，需在论文中诚实报告并讨论 saturation 机制。
      关键发现：stable rank 的 operating range 限于 0-50% contamination（ρ≈0.90+ in this subrange），
      超过 50% 后信息量急剧下降。这直接支撑 Claim 3 的 signal taxonomy 叙事。
      Seed variance 的 CV 随 severity 递增（0.08→0.22），说明 collapse 的随机性在高 severity 时放大，
      但所有 metric 的 CI 不跨零，方向性结论稳固。

  - name: "PubMed Cross-Domain Validation"
    plan_id: "plan_002"
    description: >
      Qwen2.5-1.5B × PubMed × 6 fractions × 1 seed × 5 generations。
      验证 signal behavior 是否跨越 domain boundary。
    expected_results:
      cross_frac_rho_output_6pt: 0.83
      cross_frac_rho_spectral_6pt: 0.71
      cross_domain_rho_preservation_output: 0.78
      cross_domain_rho_preservation_spectral: 0.67
      ppl_0pct_gen4: 18.5
      ppl_100pct_gen4: 280.0
      ppl_collapse_magnitude_100pct: 15.1
      stable_rank_saturation_onset: "50% (earlier than WikiText)"
      gradient_norm_cross_domain_rho: 0.35
      token_entropy_0pct_gen4: 2.10
      token_entropy_100pct_gen4: 1.15
    result_rationale: >
      PubMed 是高度专业化的 biomedical text，vocabulary distribution 与 WikiText 的 general
      encyclopedia text 有本质差异——术语密度高、句式结构更 formulaic、token entropy baseline
      更低（2.10 vs 2.45）。这导致几个效应：

      1) PPL collapse magnitude 降低（15x vs 34x）：PubMed 的 formulaic 结构意味着即使在
      synthetic data contamination 下，模型仍能生成 "看起来像 biomedical text" 的输出（固定短语、
      术语搭配），PPL 不会爆炸到同样程度。Collapse 表现为 diversity 丧失而非 incoherence。

      2) Output signal ρ 下降至 0.83：token entropy 在 PubMed 上的 dynamic range 更窄
      （baseline 已经偏低），低 severity 点（10%, 25%）的 signal 变化被 noise 淹没，
      拉低 rank correlation。

      3) Spectral signal ρ 进一步降至 0.71：PubMed 的 specialized vocabulary 导致 weight matrix
      的 spectral structure 本身就更集中（fewer effective directions needed for domain-specific text），
      stable rank baseline 更低，saturation 更早出现（50% 处即开始而非 WikiText 的 75%）。

      4) Gradient norm 跨域失效（ρ=0.35）：gradient norm 的 non-monotonic behavior 高度依赖
      loss landscape 的具体形状，PubMed 与 WikiText 的 loss landscape 拓扑不同，
      gradient norm 的 peak 位置和幅度均不可迁移。这是 median tier 下最清晰的跨域失效信号。

      5) 只有 1 seed，无法计算 variance，结果可信度有限，需在论文中明确标注。
    tables:
      - name: "Table 3: Cross-domain signal preservation (WikiText vs PubMed, 1.5B)"
        columns: ["Signal", "ρ_WikiText (mean)", "ρ_PubMed", "Preservation Ratio", "Status"]
        rows:
          - ["Perplexity", "0.91", "0.83", "0.91", "Preserved"]
          - ["Token Entropy", "0.89", "0.83", "0.93", "Preserved"]
          - ["Stable Rank", "0.77", "0.71", "0.92", "Marginal"]
          - ["Spectral Entropy", "0.80", "0.71", "0.89", "Marginal"]
          - ["Gradient Norm", "0.49", "0.35", "0.71", "Failed"]
    figures_description:
      - "Fig S1 (supplementary): WikiText vs PubMed side-by-side 曲线图。每个 signal 一个 subplot，x-axis=fraction，两条曲线分别标 domain。标注 saturation onset 差异和 gradient norm 形状差异。"
    analysis: >
      PubMed 结果支持 "partial generalization" 叙事：output signals 跨域保持可用（ρ>0.80），
      但 spectral signals 和 gradient norm 的跨域一致性不足以做 universal claim。
      这恰好强化了 Claim 3 的 signal taxonomy 贡献——practitioners 在新 domain 部署时
      应优先依赖 output signals，spectral signals 需要 domain-specific calibration。
      论文中 PubMed 结果放 main text 的 1-2 段讨论 + supplementary 完整数据。
      单 seed 是明确的 limitation，但方向性结论已有 WikiText 3-seed 数据支撑。

  - name: "Full Fine-Tuning Comparison"
    plan_id: "plan_003"
    description: >
      Qwen2.5-0.5B × WikiText-2 × 3 fractions (0/50/100%) × 1 seed × 5 gens，full fine-tuning。
      验证 signal behavior 不是 QLoRA adapter 的 artifact。
    expected_results:
      cross_frac_rho_output_3pt: 1.0
      cross_frac_rho_spectral_3pt: 1.0
      ppl_0pct_gen4: 13.2
      ppl_50pct_gen4: 18.5
      ppl_100pct_gen4: 1850.0
      ppl_collapse_magnitude_100pct: 140.0
      stable_rank_0pct_gen4: 21.8
      stable_rank_100pct_gen4: 210.0
      collapse_faster_than_qlora: true
      collapse_onset_generation: "gen 2 (vs gen 3 for QLoRA at 100%)"
      self_recovery_50pct: "absent or weaker than QLoRA"
      gradient_norm_pattern: "monotonic increase (different from QLoRA non-monotonic)"
    result_rationale: >
      Full FT 与 QLoRA 的核心差异在于可训练参数数量和梯度流路径：

      1) Collapse 更剧烈（PPL 140x vs QLoRA 53x）：Full FT 更新所有参数，synthetic data 的
      distribution bias 直接刻入整个 weight matrix，没有 frozen pretrained weights 作为
      "锚点" 来缓冲 collapse。QLoRA 的 frozen base + low-rank adapter 结构天然限制了
      collapse 的幅度——adapter 只能在 low-rank subspace 内偏移模型行为。

      2) Collapse 更快（gen 2 vs gen 3）：同样因为 full FT 对 distribution 的拟合更彻底，
      每一代的 distribution shift 被更完整地吸收，cumulative drift 加速。

      3) 50% self-recovery 消失或减弱：QLoRA 下的 self-recovery 机制假设是 frozen pretrained
      weights 在 moderate contamination 时提供了 implicit regularization，拉回模型。
      Full FT 没有这个 anchor，50% contamination 的 partial recovery 失去结构性基础。

      4) Gradient norm 变为单调：Full FT 下梯度直接作用于所有参数，loss landscape 更平滑，
      不会出现 QLoRA 中 adapter 与 frozen weights 交互导致的 non-monotonic gradient behavior。

      5) 3-point ρ 仍为 1.0：只有 3 个 fraction 时，只要方向正确 ρ 必然为 ±1.0，
      统计上无法区分 QLoRA 和 full FT，但这不是此实验的目的——目的是验证 signal behavior 的
      定性一致性（方向一致）和定量差异（幅度不同）。
    tables:
      - name: "Table S1: QLoRA vs Full FT signal comparison (0.5B, WikiText-2)"
        columns: ["Signal", "QLoRA 0%→100% Δ", "Full FT 0%→100% Δ", "Ratio", "Direction Match"]
        rows:
          - ["PPL", "15.67→839 (53x)", "13.2→1850 (140x)", "2.6x", "Yes"]
          - ["Token Entropy", "2.26→0.78 (-65%)", "2.30→0.42 (-82%)", "1.3x", "Yes"]
          - ["Stable Rank", "23.4→155.6 (6.6x)", "21.8→210 (9.6x)", "1.5x", "Yes"]
          - ["Gradient Norm", "non-monotonic", "monotonic ↑", "—", "No (shape differs)"]
    figures_description:
      - "Fig S2: QLoRA vs Full FT overlay plots. x=generation, y=signal, 两条曲线 per subplot。清晰可见 full FT collapse 更快更深，但方向一致。Gradient norm subplot 突出 shape 差异。"
    analysis: >
      Full FT 实验的核心结论是 "signal behavior 的方向（哪些 signals track, 哪些 fail）在
      training method 间保持一致，但幅度和速率不同"。这支撑了 paper 的 practitioner guidance
      定位——signal selection 建议适用于不同 fine-tuning 范式，但 threshold 需要 recalibration。
      Gradient norm 的 shape 差异是重要的负面结果，需在论文中报告：gradient norm 不仅
      non-monotonic（已知），而且其 non-monotonicity 是 QLoRA-specific artifact，
      full FT 下行为完全不同。这进一步降低了 gradient norm 作为 reliable monitor 的推荐度。
      P1 优先级合理——结论锦上添花但不改变核心 claims。

  - name: "1.5B Within-Generation Early Warning Analysis"
    plan_id: "plan_004"
    description: >
      对 plan_001 数据做 within-generation temporal analysis，计算 1.5B 模型在
      step 50/100/200/500 处各 signal 相对 0% baseline 的 deviation。纯分析，无 GPU。
    expected_results:
      early_warning_separation_step50_100pct: "18%"
      early_warning_separation_step100_100pct: "24%"
      early_warning_separation_step200_100pct: "32%"
      early_warning_detection_threshold_5pct: "step 80-120 (~5-8% progress)"
      earliest_reliable_detection_point: "7% training progress (step ~108/1540)"
      signal_first_to_diverge: "stable rank (despite saturation at end)"
      signal_most_reliable_at_step50: "PPL ratio"
      separation_variance_across_seeds: "CV = 0.20"
    result_rationale: >
      1.5B 模型的 early warning 比 0.5B 延迟，核心原因是更大的参数容量提供了更多的
      "buffer capacity"——1.5B 模型在训练初期能更好地吸收 synthetic data 的 distribution
      shift 而不立即表现出 signal deviation。具体地：

      1) Step 50 处 separation 从 0.5B 的 34.4% 降至 18%：0.5B 模型在 step 50 时
      adapter 已经开始显著偏移（因为 adapter 相对于 frozen weights 的 ratio 更大），
      1.5B 模型的 adapter dimension 相同（r=16）但 frozen base 更大，
      adapter 的相对影响力更小，需要更多 steps 才能积累足够的偏移。

      2) Reliable detection 延迟至 ~7% progress（vs 0.5B 的 3%）：这仍然有实用价值——
      在训练的前 10% 检测到 collapse 依然能节省 >90% 的计算开销。但 headline 从
      "3% progress" 弱化为 "≤10% progress"。

      3) Stable rank 依然最早 diverge：虽然 stable rank 在 end-of-generation 有 saturation
      问题，但在 within-generation 的早期 steps 它反而最敏感，因为 weight matrix 的
      spectral structure 对前几个 gradient steps 的方向变化最敏感。这是一个有趣的 nuance——
      同一个 signal 在不同 analysis dimension（cross-fraction vs within-generation）有不同的 operating range。

      4) Seed variance 较大（CV=0.20）：early steps 的 signal 本身噪声大，
      3 seeds 的 variance 在 step 50 处使得某些 seed 的 separation 可能低至 12%，
      需要谨慎设定 detection threshold。
    tables:
      - name: "Table 4: Within-generation signal deviation at key checkpoints (1.5B, 100% synthetic, mean ± std over 3 seeds)"
        columns: ["Step (% progress)", "Stable Rank Dev.", "Spectral Entropy Dev.", "PPL Ratio", "Token Entropy Dev."]
        rows:
          - ["50 (3%)", "18±4%", "8±3%", "1.12±0.04", "5±2%"]
          - ["100 (6.5%)", "24±5%", "14±4%", "1.22±0.06", "10±3%"]
          - ["200 (13%)", "32±6%", "22±5%", "1.45±0.10", "18±4%"]
          - ["500 (32%)", "48±8%", "38±7%", "2.10±0.25", "32±5%"]
          - ["1540 (100%)", "270±40%", "25±8%", "33.6±8.0", "62±7%"]
      - name: "Table 5: Detection reliability at 5% false positive rate (3 seeds)"
        columns: ["Signal", "Earliest reliable step", "% progress", "Separation at detection"]
        rows:
          - ["Stable Rank", "85", "5.5%", "20%"]
          - ["PPL Ratio", "108", "7.0%", "1.18x"]
          - ["Spectral Entropy", "130", "8.4%", "15%"]
          - ["Token Entropy", "155", "10.1%", "12%"]
    figures_description:
      - "Fig 3: Within-generation signal trajectories. x=training step, y=signal value, 6 曲线 per subplot (one per fraction), shaded seed bands. Vertical dashed line 标注 detection point。对比 0.5B 的 detection point (虚线) 显示 scale-dependent delay。"
    analysis: >
      Early warning 在 1.5B 上依然成立但 headline 需调整。关键 reframing：不说 "3% progress"
      而说 "within the first 10% of training across scales"，这仍是有价值的 practical claim。
      有趣的发现是 stable rank 在 early detection 和 end-of-training tracking 两个 use case
      中有相反的表现——early detection 最强，end-of-training severity tracking 最弱（saturation）。
      这为 signal taxonomy 增加了一个 temporal dimension，强化 Claim 3。
      3 seeds 的 variance 是 concern，某些 seed 在 step 50 处 separation <15%，
      论文应报告 "median detection point" 而非 "earliest detection"。

  - name: "Early Warning ROC / Threshold Calibration"
    plan_id: "plan_005"
    description: >
      对 plan_001 + plan_002 全部数据做 ROC 分析，确定 minimum signal deviation threshold
      能 reliably predict end-of-generation collapse。
    expected_results:
      auroc_stable_rank_wikitext: 0.82
      auroc_ppl_ratio_wikitext: 0.88
      auroc_stable_rank_pubmed: 0.74
      auroc_ppl_ratio_pubmed: 0.80
      optimal_threshold_stable_rank_dev: "15% deviation"
      optimal_threshold_ppl_ratio: "1.15x baseline"
      false_positive_rate_at_90_recall: 0.18
      cross_domain_threshold_transferability: "partial — thresholds need 20-30% adjustment for PubMed"
    result_rationale: >
      ROC 分析的 binary label 定义为 "end-of-generation PPL > 2× baseline"（即 collapse 发生）。

      1) PPL ratio 的 AUROC 最高（0.88 WikiText）：PPL ratio 直接预测的就是 PPL，
      属于 same-family prediction，天然有高 correlation。这不是 trivial 的，因为
      early-step PPL ratio 需要在信噪比很低时做出判断，但 PPL 的 noise structure
      比 spectral signals 更 well-behaved（symmetric, roughly Gaussian）。

      2) Stable rank AUROC 略低（0.82）：stable rank 在高 severity 端的 saturation 意味着
      它在 50/75/100% 三个 fraction 给出相近的 early deviation，降低了 discriminability。
      但它在区分 "no collapse" vs "any collapse" 时依然有效。

      3) PubMed AUROC 下降 ~0.08：PubMed 的 domain-specific dynamics 导致 WikiText 上
      calibrated 的 threshold 在 PubMed 上产生更多 false positives（PubMed baseline 本身
      有更大的 step-to-step variance）。需要 domain-specific recalibration。

      4) False positive rate 0.18 at 90% recall 意味着实际部署中约每 5 次 alert 有 1 次
      false alarm——对于 "cheap monitoring, expensive collapse" 的场景来说是 acceptable trade-off，
      但需在论文中 explicitly frame。

      5) 样本量有限（6 fractions × 5 gens × 3 seeds = 90 data points for WikiText，
      30 for PubMed），ROC 曲线的 confidence interval 宽，AUROC 的 95% CI 约 ±0.06。
    tables:
      - name: "Table 6: ROC Analysis Summary"
        columns: ["Signal", "AUROC (WikiText)", "95% CI", "AUROC (PubMed)", "Optimal Threshold"]
        rows:
          - ["PPL Ratio (step 100)", "0.88", "[0.82, 0.94]", "0.80", "1.15x"]
          - ["Stable Rank Dev. (step 100)", "0.82", "[0.75, 0.89]", "0.74", "15%"]
          - ["Spectral Entropy Dev.", "0.78", "[0.70, 0.86]", "0.70", "8%"]
          - ["Token Entropy Dev.", "0.85", "[0.78, 0.92]", "0.77", "6%"]
    figures_description:
      - "Fig S3: ROC curves per signal, WikiText solid lines, PubMed dashed lines. 标注 optimal operating point 和 95% CI band。"
    analysis: >
      ROC analysis 为 Claim 2 提供了 quantitative rigor 但也暴露了 limitations。
      AUROC 0.82-0.88 是 "useful but not production-ready" 的范围——足以支撑 "early warning
      has practical value" 的学术 claim，但 practitioner 不能直接用这些 thresholds 做
      automated stop-training decisions。论文应 frame 为 "human-in-the-loop alert system"。
      Cross-domain threshold 不可迁移是重要发现，增加了 Claim 3 signal taxonomy 的价值——
      不仅需要选择正确的 signal，还需要 per-domain calibration。
      CI 宽度是 honest limitation，n=90 本质上无法做 high-confidence ROC，
      但作为 analysis paper 的 directional evidence 足够。

  - name: "Signal Taxonomy Table (per-signal operating ranges)"
    plan_id: "plan_006"
    description: >
      使用 plan_001 数据构建 per-signal-family operating range 表格。
      每个 signal 标注最有效/最无效的 severity 区间、scale、domain。
      这是 median tier 下论文的核心贡献。
    expected_results:
      stable_rank_effective_range: "0-50% contamination"
      stable_rank_failure_mode: "saturation at ≥50% (75% and 100% indistinguishable)"
      spectral_entropy_effective_range: "0-75% contamination"
      spectral_entropy_failure_mode: "saturation at 100%, less severe than stable rank"
      token_entropy_effective_range: "0-100% (full range)"
      token_entropy_limitation: "lower sensitivity at <25%, noise-dominated"
      ppl_effective_range: "0-100% (full range)"
      ppl_limitation: "scale-dependent magnitude, thresholds not transferable"
      gradient_norm_effective_range: "none — unreliable across conditions"
      gradient_norm_failure_mode: "non-monotonic, shape changes across scale/domain/training method"
      hellaswag_effective_range: "none at ≤1.5B scale"
      hellaswag_failure_mode: "insufficient sensitivity at small scale"
    result_rationale: >
      Signal taxonomy 的 operating range 由每个 signal 的物理机制决定：

      Stable rank = effective numerical dimension of weight matrix。当 collapse 将
      singular value distribution 推向极端集中（dominant direction captures most variance），
      stable rank 趋向一个由 matrix dimension 决定的上界。50% contamination 以上，
      不同 severity 都推向这个上界附近，信息量消失。就像温度计在沸点以上失效。

      Spectral entropy = normalized entropy of singular value distribution。比 stable rank
      更 robust 因为 entropy 对分布 tail 更敏感，但在极端集中时同样饱和，只是阈值更高（75% vs 50%）。

      Token entropy/PPL = 直接测量 output distribution 的 collapse 程度。
      不依赖 weight matrix 的 spectral structure，而是端到端地反映模型行为。
      因此在全 severity range 有效。但 sensitivity 在低 severity（<25%）时弱，
      因为少量 synthetic data 的影响在 output space 被 averaging 稀释。

      Gradient norm = training dynamics signal，高度依赖 optimizer state、learning rate、
      以及 adapter 结构。在 QLoRA 下非单调是因为 adapter 在 moderate severity 时
      loss landscape 变陡（梯度增大），但在 extreme severity 时 loss landscape 反而变平
      （模型已经 collapsed 到局部最优附近）。这个机制在 full FT 和不同 domain 下完全不同，
      所以不可作为 generalizable signal。

      HellaSwag = downstream reasoning task。1.5B 以下模型的 HellaSwag performance
      主要由 pretrained weights 决定（not fine-tuning），所以 collapse of fine-tuning
      几乎不影响它。需要更大模型或更 fine-tuning-sensitive 的 downstream task。
    tables:
      - name: "Table 7: Signal Operating Range Taxonomy (core contribution)"
        columns: ["Signal Family", "Signal", "Effective Range", "Failure Mode", "Cross-Scale", "Cross-Domain", "Recommended Use"]
        rows:
          - ["Spectral", "Stable Rank", "0-50%", "Saturation ≥50%", "Consistent (delay differs)", "Partial (onset shifts)", "Early warning only"]
          - ["Spectral", "Spectral Entropy", "0-75%", "Saturation at extreme", "Consistent", "Partial", "Medium-severity tracking"]
          - ["Output", "Perplexity", "0-100%", "Scale-dependent magnitude", "Consistent", "Preserved (ρ>0.80)", "Primary severity tracker"]
          - ["Output", "Token Entropy", "0-100%", "Low sensitivity <25%", "Consistent", "Preserved", "Primary severity tracker"]
          - ["Training", "Gradient Norm", "Unreliable", "Non-monotonic, method-specific", "Shape changes", "Failed (ρ≈0.35)", "Not recommended"]
          - ["Downstream", "HellaSwag", "Unknown", "Insensitive at ≤1.5B", "Untested at large scale", "N/A", "Not recommended at small scale"]
      - name: "Table 8: Per-signal monotonicity matrix (fraction × generation)"
        columns: ["Signal", "Gen 0", "Gen 1", "Gen 2", "Gen 3", "Gen 4", "Monotonic in all gens?"]
        rows:
          - ["PPL", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes"]
          - ["Token Entropy", "Yes", "Yes", "Yes", "Yes", "Yes*", "Yes (reversed)"]
          - ["Stable Rank", "Yes", "Yes", "No*", "No", "No", "No (saturation)"]
          - ["Spectral Entropy", "Yes", "Yes", "Yes", "No*", "No", "Partial"]
          - ["Gradient Norm", "No", "No", "No", "No", "No", "No"]
    figures_description:
      - "Fig 4 (core figure): 'Traffic light' heatmap — rows = signals, columns = severity bins (0-10%, 10-25%, 25-50%, 50-75%, 75-100%)。Green = signal reliably tracks in this bin, Yellow = noisy but directional, Red = saturated/unreliable。This becomes the paper's signature figure。"
      - "Fig 5: Per-signal response curves across full severity range, with annotated saturation points and operating range brackets。"
    analysis: >
      Signal taxonomy table 是 median tier 论文的核心贡献，因为信号分化使得 "which signal when"
      比 "signals work" 更 actionable。Table 7 的 "Recommended Use" 列直接对应
      practitioner guidance——这是 Datasets & Benchmarks track 审稿人最看重的。
      关键 narrative shift：从 "all signals track collapse" 到 "different signals have
      complementary operating ranges, and practitioners need our taxonomy to choose correctly"。
      Gradient norm 和 HellaSwag 的失败不是论文的弱点而是 contribution——documenting
      what doesn't work is as valuable as documenting what works，特别是在 practitioners
      可能 naively adopt these metrics 的场景。

  - name: "Per-Layer Collapse Analysis (1.5B)"
    plan_id: "plan_007"
    description: >
      对 1.5B 模型做 forward-pass SVD，提取 per-layer stable rank / spectral entropy，
      分析哪些 layers 最先/最严重 collapse。
    expected_results:
      first_collapsing_layers: "final 4-6 layers (closest to output head)"
      collapse_propagation_direction: "top-down (output layers → middle layers)"
      early_layers_preserved_until: "gen 3 at 100% contamination"
      layer_collapse_correlation_with_depth: "ρ ≈ 0.75 (deeper = earlier collapse)"
      per_layer_stable_rank_cv_across_seeds: 0.22
      layer_collapse_pattern_0pct: "uniform — no differential collapse"
      layer_collapse_pattern_50pct: "gradient — mild top-layer degradation, bottom preserved"
      layer_collapse_pattern_100pct: "bimodal — top 30% severely collapsed, bottom 70% partially preserved"
    result_rationale: >
      Per-layer collapse 遵循 top-down propagation 的物理直觉：

      1) Final layers 最先 collapse 因为它们直接连接 LM head，承受 output distribution
      regression target 的直接压力。当 training data 的 distribution 被 synthetic data
      pollute 时，LM head 学到 collapsed distribution，gradient 信号从 LM head 反向传播，
      最先影响最近的 layers。

      2) 1.5B 模型有 ~28 层（Qwen2.5-1.5B），比 0.5B 的 ~24 层更深。
      更多层意味着 gradient signal 在传播过程中有更多衰减，bottom layers 被保护得更好。
      这解释了 "bottom 70% partially preserved" 的 pattern。

      3) 50% contamination 的 gradient pattern（mild top degradation）与 50% self-recovery
      现象一致——top layers 有轻微 collapse 但没有严重到 cascade 到 bottom layers，
      bottom layers 的 preserved representations 为 self-recovery 提供了基础。

      4) Per-layer 分析的 seed variance 较大（CV=0.22）因为 layer-level signals 比
      model-level aggregates 噪声更大——每一层的 activation 只看到模型行为的一个 slice。

      5) 0% 的 uniform pattern 是重要的 negative control——确认 per-layer 差异确实是
      contamination 导致而非 training dynamics 的 natural artifact。
    tables:
      - name: "Table S2: Per-layer collapse summary (1.5B, gen4, 100% synthetic)"
        columns: ["Layer Group", "Layers", "Mean Stable Rank Δ", "Mean Spectral Entropy Δ", "Collapse Severity"]
        rows:
          - ["Bottom (1-7)", "1-7", "+15%", "+5%", "Mild"]
          - ["Lower-mid (8-14)", "8-14", "+35%", "+12%", "Moderate"]
          - ["Upper-mid (15-21)", "15-21", "+85%", "+28%", "Severe"]
          - ["Top (22-28)", "22-28", "+180%", "+45%", "Extreme"]
    figures_description:
      - "Fig 6: Heatmap — x=generation (0-4), y=layer depth (1-28), color=stable rank relative to gen0 baseline. Three panels for 0%/50%/100%。Top-down propagation pattern clearly visible in 100% panel。"
      - "Fig S4: Per-layer spectral entropy trajectories, line plot, one line per layer colored by depth。Shows temporal cascade。"
    analysis: >
      Per-layer analysis 为 Claim 3 增加 depth dimension，使 signal taxonomy 从
      "which signal" 扩展到 "which signal at which layer"。实用建议：practitioners 应
      monitor final 20-30% 的 layers 的 spectral properties 作为 early indicator。
      Top-down propagation finding 也为 future intervention work 提供方向——
      如果 collapse 从 top layers 开始，targeted regularization 或 selective freezing
      可能有效（但这是 future work，不在当前 paper scope）。
      P1 priority 正确——结论增加 depth 但不改变 core claims。

  - name: "Self-Recovery Deep Dive"
    plan_id: "plan_008"
    description: >
      分析 plan_001 数据中 25%/50%/75% fractions 的 self-recovery 现象。
      核心问题：recovery 在多少 seeds 中复现？在哪个 fraction 消失？
    expected_results:
      recovery_definition: "PPL at gen_t < PPL at gen_{t-1} for ≥1 consecutive generation"
      recovery_at_25pct_seeds_reproducing: "2/3"
      recovery_at_50pct_seeds_reproducing: "1-2/3"
      recovery_at_75pct_seeds_reproducing: "0/3"
      recovery_magnitude_50pct_mean: "8-15% PPL reduction in recovery generation"
      recovery_generation_onset: "gen 2 or gen 3 (varies by seed)"
      recovery_duration: "1 generation (transient, not sustained)"
      recovery_mechanism_hypothesis: "frozen pretrained weights provide implicit regularization at moderate contamination"
      recovery_absent_in_full_ft: "consistent with QLoRA regularization hypothesis"
      self_recovery_reproducibility: 0.5
    result_rationale: >
      Self-recovery 的 reproducibility 是 median tier 最核心的 concern：

      1) 50% fraction 只有 1-2/3 seeds 复现：self-recovery 是 "在模型 collapse 趋势中
      出现的暂时性 PPL 改善"。这个现象本质上是两个力的平衡——synthetic data 的 corrupting force
      vs frozen pretrained weights 的 regularizing force。在 50% contamination 时这两个力
      近似平衡，小扰动（seed 决定的 initialization 和 data order）就能决定 balance 倒向哪边。
      这就是为什么 1/3 seed 可能看不到 recovery——那个 seed 的 random trajectory
      让 corruption force 一直略占优势。

      2) 25% 更容易复现（2/3）：因为 clean data 占比更大，regularizing force 更强，
      recovery 更 robust to seed variance。

      3) 75% 完全不复现：corruption force 太强，no seed 的 random trajectory 能翻转 balance。
      这给出了 recovery 消失的 threshold——在 50-75% 之间。

      4) Recovery 是 transient（只持续 1 generation）：因为每一代的 synthetic data
      在 cumulative corruption 上都在增加，frozen weights 的 regularization 是 fixed 的，
      最终 corruption 必然压过 regularization。Recovery 只是延迟了 inevitable collapse，
      不是阻止。

      5) Recovery 在 full FT 中消失（plan_003 数据）：直接支持 "frozen weights as
      regularizer" 假说。这是 mechanistic insight 的重要 evidence，但因为 reproducibility
      不足以独立成 claim，只能作为 observation 段落。
    tables:
      - name: "Table 9: Self-recovery reproducibility summary"
        columns: ["Fraction", "Seeds w/ Recovery", "Mean Recovery Magnitude", "Recovery Generation", "Duration"]
        rows:
          - ["25%", "2/3 (67%)", "12% PPL reduction", "Gen 2", "1 gen"]
          - ["50%", "1-2/3 (33-67%)", "10% PPL reduction", "Gen 2-3 (varies)", "1 gen"]
          - ["75%", "0/3 (0%)", "N/A", "N/A", "N/A"]
          - ["100%", "0/3 (0%)", "N/A", "N/A", "N/A"]
      - name: "Table 10: Per-seed PPL trajectory at 50% contamination (1.5B)"
        columns: ["Seed", "Gen 0", "Gen 1", "Gen 2", "Gen 3", "Gen 4", "Recovery?"]
        rows:
          - ["Seed 1", "14.2", "14.8", "14.5↓", "15.2", "16.1", "Yes (gen 2)"]
          - ["Seed 2", "14.0", "14.9", "15.3", "15.0↓", "16.8", "Yes (gen 3)"]
          - ["Seed 3", "14.5", "15.1", "15.6", "16.2", "17.0", "No"]
    figures_description:
      - "Fig S5: Per-seed PPL trajectories at 25/50/75%, x=generation, y=PPL. Each seed a separate line. Recovery events marked with ↓ arrows. Shaded region indicates 'recovery zone' (gens 2-3)。Clear seed divergence at 50%。"
    analysis: >
      Self-recovery 在 median tier 下不足以做 headline claim。Reproducibility 33-67%
      意味着 "the phenomenon exists but is not reliable"——在论文中作为 Section 4.3
      "Observation: Partial Self-Recovery at Moderate Contamination" 的 1-2 段讨论。
      关键 framing：不是 "we discovered self-recovery" 而是 "we observed a self-recovery
      pattern that appears seed-dependent, consistent with an implicit regularization
      hypothesis that merits further investigation"。配合 plan_003 full FT 数据
      （recovery 消失）增加 mechanistic plausibility。
      这个结果实际上增加了 paper 的 nuance 和 honest reporting，NeurIPS 审稿人
      会 appreciate 不过度 claim unreliable findings。但如果 recovery 在所有 3 seeds
      都不复现（worst case of median），则降级为 footnote。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed11e643-47a4-4ebb-92c6-d9a7b1a5b512",
  "isSidechain": false,
  "requestId": "req_011Cb38nHGMsZg95TbW4dNpq",
  "type": "assistant",
  "uuid": "7e7fb579-1a4e-48a7-bbc8-f42271e5e715",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_4",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013KjyqiswN3E2QWKBasqaYm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10834,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13302,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10834
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心相关性成立但不完美，部分信号/域/规模出现退化，需调整 claim 强度和补充分析 核心假设：['6 fractions 下 output 信号 ρ 保持 ≥0.80，但 spectral 信号 ρ 降至 0.70-0.85（stable rank 饱和拉低）', '1.5B 定性一致但 collap…",
  "leafUuid": "7e7fb579-1a4e-48a7-bbc8-f42271e5e715",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Collapse severity monitoring with partial signal generalization",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心相关性成立但不完美，部分信号/域/规模出现退化，需调整 claim 强度和补充分析 核心假设：['6 fractions 下 output 信号 ρ 保持 ≥0.80，但 spectral 信号 ρ 降至 0.70-0.85（stable rank 饱和拉低）', '1.5B 定性一致但 collap…",
  "leafUuid": "7e7fb579-1a4e-48a7-bbc8-f42271e5e715",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Collapse severity monitoring with partial signal generalization",
  "sessionId": "880e8550-bcef-4ebb-806e-92c4749f8a60"
}
```

---
