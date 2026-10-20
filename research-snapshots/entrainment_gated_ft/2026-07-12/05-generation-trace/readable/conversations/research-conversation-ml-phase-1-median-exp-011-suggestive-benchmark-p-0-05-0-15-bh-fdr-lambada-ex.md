# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：exp-011 产出 suggestive 但非显著的第二 benchmark（p=0.05-0.15）；BH-FDR 仅保留 LAMBADA；ex

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/0e7d084f-631d-4c53-ad97-0f6a0bae2ba4.jsonl`
- **Structured JSON:** [`e4d7bd34804c24ca9b08.json`](../../sessions/e4/e4d7bd34804c24ca9b08.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T14:50:48.208Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T14:50:48.208Z",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：exp-011 产出 suggestive 但非显著的第二 benchmark（p=0.05-0.15）；BH-FDR 仅保留 LAMBADA；exp-004 有描述性 attention 差异但相关偏弱；exp-005 无额外架构或结果 mixed。需要调整 claim 强度，但 task-specificity + per-example divergence 的组合故事仍可 Findings。\n核心假设：['exp-011 最佳新 benchmark ρ ≈ -0.7 至 -0.8, p ≈ 0.08-0.15（suggestive, not significant）', 'BH-FDR 仅 LAMBADA 显著；但 LAMBADA + 新 benchmark 的 convergent direction 构成 pattern', 'exp-004 attention-effect correlation 0.15-0.30（可描述，不足以做 strong claim）', 'exp-005 未找到可评估的额外架构，或找到但 convergence 不显著', 'GDN-excluded ARC-Easy 维持在 ρ=-0.9, p≈0.08（suggestive, 补充证据）', 'exp-007 340M rebound 可部分解释但非完全清晰']\n关键指标范围：{'exp011_best_new_rho': [-0.8, -0.6], 'exp011_best_new_p': [0.08, 0.2], 'n_benchmarks_BH_FDR_significant': [1, 1], 'exp004_attn_effect_correlation': [0.15, 0.3], 'lambada_cross_arch_std_reduction_pct': [75, 85], 'per_example_jaccard_range': [0.05, 0.12], 'n_architectures_total': [3, 3], 'n_suggestive_benchmarks_p_below_0_15': [2, 3]}\n叙事方向：Claim 1 从 'task-dependent convergence' 弱化为 'convergence on retrieval-heavy tasks with suggestive evidence on related benchmarks'。LAMBADA 仍是 anchor，但通过 (a) 新 benchmark 的方向一致性（即使不显著），(b) GDN-excluded ARC-Easy 的改善，(c) principled task taxonomy 来构建 converging evidence 叙事。明确承认 Bonferroni failure，用 exact permutation p + percentile CI + 方向一致性作为论证。Claim 3 per-example divergence 成为相对更强的独立贡献。exp-004 以描述性证据出现（'attention patterns differ across architectures on affected samples'），避免 mechanistic language。目标 EMNLP Findings，honest framing。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: entrainment_gated_ft\nvenue: emnlp-2026\nfocus: This is a pivot from a failed entrainment hypothesis to an equalizer effect discovery. Key concerns: (1) only LAMBADA shows clear convergence — is the finding too narrow? (2) n=3 architectures — sufficient? (3) differentiation from Wang et al. who have the model zoo and noted qualitative convergence. (4) no 7B scale yet — two scales enough? Assess whether the equalizer paradox (aggregate convergence + per-example divergence) is novel and interesting enough for EMNLP Findings/Main.\n\n## paper_framing.md\n\n# Paper Framing — entrainment_gated_ft\n\n> Revised 2026-05-19 after Dream review (best case = 2.5/5). Major reframing: drop \"paradox\" narrative, engage related work, add retrieval benchmarks.\n\n## Target Venue\n- Primary: EMNLP 2026 Findings (via ARR)\n- Stretch: EMNLP 2026 Main\n- Deadline: ARR June 2026 cycle (submission ~June 15)\n\n## Paper Type\nEmpirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)\n\n## Core Claims (3 条)\n\n### Claim 1: Task-Dependent Convergence\nAdding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength varies with task type. Convergence is strongest on LAMBADA (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, p=0.233, underpowered at n=5), and absent on reasoning-heavy tasks. **Critical need**: a second high-retrieval benchmark showing significant convergence to survive multi-comparison correction.\n\n### Claim 2: Scale-Dependent Convergence\nThe convergence effect requires sufficient model capacity: monotonically complete at 1.3B (ρ=-1.0, p=0.017 two-tailed) but only partial at 340M with a non-monotonic rebound. Only two scale points (Wang et al. cap at 1.3B). Frame as binary contrast, not extrapolatable trend.\n\n### Claim 3: Per-Example Divergence Under Aggregate Convergence\nDespite aggregate convergence, attention acts on nearly non-overlapping sample subsets per architecture (pairwise Jaccard < 0.10). This is an instance of the well-documented underspecification phenomenon (D'Amour et al. 2022) applied to hybrid architectures. Our contribution is **quantifying** it in this specific context, NOT claiming to discover it. Surface features AND baseline model perplexity do not differentiate helped/hurt samples within an architecture — the effect is opaque to standard features. However, cross-architecture comparison reveals systematic differences in baseline difficulty profiles of affected samples (Kruskal-Wallis p=0.0005 for hurt samples), confirming the architecture-specificity is structured, not random noise.\n\n## Story Spine\n\n### Problem\nHybrid architectures mixing linear recurrence with full attention are becoming standard. While Wang et al. (2025) provide an extensive model zoo, the community lacks quantitative understanding of how attention affects cross-architecture behavioral diversity at the per-example level.\n\n### Related Work Positioning (CRITICAL — Dream W2)\nThe observation that models with similar aggregate performance differ per-example is well-established:\n- **Ensemble diversity**: Krogh & Vedelsby (1995), Kuncheva & Whitaker (2003) — diverse ensemble members err on different examples by construction\n- **Underspecification**: D'Amour et al. (2022) — equivalent aggregate performance masks prediction-level differences\n- **Dataset cartography**: Swayamdipta et al. (2020) — per-example difficulty varies across models\n- **Simpson's paradox / ecological fallacy**: Aggregate-vs-disaggregate discrepancy is a textbook phenomenon\n\nOur contribution is NOT discovering this phenomenon. It IS quantifying how it manifests specifically when attention is added to linear recurrent models, and characterizing its task-dependency and scale-dependency. This is valuable because hybrid architectures are a design choice practitioners make — understanding per-example implications informs that choice.\n\n### Our Framing\nWe provide the first systematic per-example analysis of attention's equalizing effect in hybrid recurrent architectures. Using Wang et al.'s public model zoo (72 models), we quantify (a) task-dependent convergence strength, (b) scale-dependent convergence completeness, and (c) architecture-specific per-example divergence patterns. Our contribution is analytical depth on public infrastructure, not new methods or models.\n\n### Headline Result Template\n\"At 1.3B scale, adding attention to hybrid recurrent models reduces cross-architecture variance by 79% on LAMBADA, yet per-example analysis reveals nearly non-overlapping affected sample subsets (Jaccard < 0.10) — a manifestation of underspecification that has practical implications for architecture selection.\"\n\n## Dream Review Findings (D006) — Must Address\n\n### W1: Single-benchmark significance [MAJOR, blocking]\nAfter Bonferroni (6 benchmarks, α=0.0083), LAMBADA p=0.017 (two-tailed) does NOT survive. Need: (a) FDR correction (Benjamini-Hochberg) as primary reporting, (b) additional high-retrieval benchmarks for a second significant anchor. Candidates: StoryCloze, BoolQ, COPA, closed-book QA tasks available in lm-eval.\n\n### W2: Missing related work [MAJOR, blocking for submission]\nNeed 20+ references engaging ensemble diversity, underspecification, dataset cartography, attention interpretability, hybrid architectures (Jamba, RWKV-6, RecurrentGemma). Paper Agent handles this during writing.\n\n### W3: Mechanistic overclaiming [MAJOR, partially addressed]\nAlready reworded Claim 3 from \"Mechanism\" to \"Effects\". Must NOT use \"mechanistic analysis\" in paper — use \"characterization\" or \"decomposition\" instead. Attention weight analysis (exp-004) is descriptive, not causal. Frame honestly.\n\n### W4: Incremental over Wang et al. [MAJOR]\nMitigate by: (a) engaging related work to show the QUESTION we ask is independently motivated by ensemble/underspecification literature, (b) framing contribution as analytical toolkit + quantitative characterization, not re-analysis. (c) Per-example analysis is genuinely novel for this model family.\n\n## Venue Fit Risks\n(unchanged from previous version, see git history)\n\n## Anticipated Reviewer Concerns\n\n### Concern A: \"This is just a re-analysis of Wang et al.'s models\"\nResponse: Yes, and that's the point — public infrastructure enables community analysis. Our per-example decomposition, task-dependency characterization, and scale-dependency analysis are not in Wang et al. The contribution is analytical, like meta-analyses in medicine.\nRequired: Strong Related Work positioning; frame as \"community analysis\" paper.\n\n### Concern B: \"Only one task shows the effect\" + Bonferroni failure\n**Statistical strategy** (from exp-008, verified by Reviewer with independent reproduction):\n1. **Lead with percentile CI (valid-only)**: BCa degenerates at ρ=-1.0 boundary (z0=-3.86); fall back to percentile CI on valid bootstrap resamples (8875/10000; 11.25% degenerate from n=3 same-architecture redraws). Valid-only percentile CI = **[-1.0, -0.7]**, 100% of valid resamples have ρ<0. Full percentile CI (degenerate-as-zero) = [-1.0, 0.0] touches zero. Paper leads with valid-only CI; BCa degeneracy + degenerate-sample treatment in appendix.\n2. **Report exact permutation p**: LAMBADA p=0.017 (two-tailed, 2/120 permutations). Honest and transparent.\n3. **Bonferroni in supplementary**: adj-p=0.100 (two-tailed). Report honestly as \"does not survive Bonferroni.\" BH-FDR also gives 0.100 (no additional benefit with only 1 small p-value). If exp-011 produces a second significant benchmark, BH-FDR becomes more favorable than Bonferroni.\n4. **GDN-excluded sensitivity**: Excluding GDN (D004 confound): LAMBADA ρ drops to -0.7 (p=0.233); ARC-Easy ρ **improves** from -0.7 to -0.9 (p=0.083, suggestive — D004 noise removed); **⚠️ MMLU ρ FLIPS from -0.7 to +0.6** — MMLU apparent convergence was entirely GDN-driven and MUST NOT appear as convergence evidence anywhere in the paper (D007). Report both full and GDN-excluded analyses. The ARC-Easy improvement after confound removal is itself informative, especially in exp-011 context.\n5. **exp-011**: Additional retrieval benchmarks (StoryCloze/BoolQ/COPA) for a potential second significant anchor. CRITICAL for acceptance — with exp-011 data, BH-FDR could diverge favorably from Bonferroni.\n6. **Effect sizes**: Cohen's d CI crosses zero; omega² near zero. Do NOT lead with effect sizes — lead with BCa CI and convergence magnitude (std 0.024→0.005, 79% reduction).\n\nRequired experiments: exp-011 (additional retrieval benchmarks), exp-008 (robustness with corrected p-values), exp-002 (per-example validation).\n\n### Concern C: \"The per-example divergence is a known phenomenon\"\nResponse: Acknowledge explicitly. Our contribution is quantification in hybrid architectures, not discovery of the phenomenon. Cite ensemble diversity + underspecification.\nRequired: Related Work section (Paper Agent).\n\n### Concern D: \"n=3 architectures is too few\"\nResponse: 3 architectures × 5 ratios × 2 scales = 30 models. Per-example analysis provides 5153 data points per comparison. Check for additional architectures (exp-005).\n\n### Concern E: \"Two scales don't establish a trend\"\nResponse: Binary contrast, not trend. 7B unavailable. Frame as \"scale is a necessary condition.\" exp-007 for 340M rebound mechanism.\n\n### Concern F: \"No causal mechanism\" (NEW from Dream)\nResponse: We do NOT claim causal mechanism. We characterize and describe. Attention weight analysis (exp-004) is descriptive. Interventional experiments (head swaps, ablations) are acknowledged as future work. Honest framing prevents overclaiming.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  title: Task-specificity characterization of equalizer effect\n  description: 'Compute cross-architecture variance (std) at each attention ratio\n    for all 6 benchmarks. Known: only LAMBADA shows significant convergence (p<0.05).\n    Goal: build principled task taxonomy (retrieval-dependent vs reasoning-dependent)\n    explaining WHY convergence is task-specific. LAMBADA = last-word retrieval from\n    context; HellaSwag/ARC = multi-step reasoning. Show the dichotomy is a feature\n    (task-type modulation), not a limitation.\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 0\n  deps: []\n  data_source: existing summary_all_1.3b.csv + 340M results + cross_scale_convergence\n    output\n  pass_fail: Clear task-type dichotomy with principled taxonomy; convergence correlates\n    with retrieval demand\n  reviewer_risk: 'Risk A — reframed per Reviewer warning: single-task convergence\n    → task-specificity as positive finding'\n  status: planned\n- id: exp-002\n  claim: 1\n  title: Multi-benchmark per-example analysis (task-specificity validation)\n  description: 'Re-run lm-eval on 1.3B models with --log_samples for HellaSwag, ARC-easy,\n    ARC-challenge. Two goals: (a) confirm task-specificity — per-example convergence\n    absent on reasoning tasks, (b) characterize HOW attention affects per-example\n    behavior on non-converging tasks (random noise vs systematic but architecture-specific).\n    Strengthens Claim 1 regardless of outcome.\n\n    '\n  priority: P0\n  type: experiment\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  pass_fail: Per-example data collected for ≥3 benchmarks; task-specificity of per-example\n    mechanism confirmed or refuted\n  reviewer_risk: 'Risk B — outcome determines Claim 1 scope: cross-task vs retrieval-specific\n    equalizer'\n  note: 'Budget revised to 20h per Reviewer data audit: need --log_samples for 10×340M\n    (RetNet+HGRN2) + 3×1.3B (GDN h3-1/h6-1/h24-1). Uses freed exp-006 budget.'\n  status: planned\n- id: exp-006\n  claim: 2\n  title: 7B model evaluation — CANCELLED (unavailable)\n  description: 'Wang et al. only have 340M + 1.3B (72 models total). Paper Limitations\n    explicitly excludes 10B+. No 7B models exist. Budget reallocated to exp-002/004/005.\n\n    '\n  priority: cancelled\n  type: experiment\n  gpu_budget_hours: 0\n  deps: []\n  pass_fail: N/A — 7B unavailable, confirmed 2026-05-19\n  status: planned\n- id: exp-007\n  claim: 2\n  title: '340M rebound mechanism analysis (upgraded: compensate 7B absence)'\n  description: 'Deep analysis of 340M non-monotonic rebound at attn=8. Per-example\n    comparison with 1.3B at same attention ratio to identify which samples diverge.\n    Characterize rebound samples. With 7B unavailable, this becomes the primary vehicle\n    for Claim 2 depth — show the binary contrast (340M partial vs 1.3B complete) has\n    mechanistic explanation, not just correlation with scale. Analyze training token\n    count (20B vs 100B) as confound vs scale.\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  data_source: existing 340M results + new 1.3B per-example data\n  pass_fail: Rebound mechanism identified with principled explanation; 340M vs 1.3B\n    contrast characterized beyond aggregate metrics\n  note: Upgraded from P1 to P0 after 7B cancellation. May need 340M per-example rerun\n    (2h GPU).\n  status: planned\n- id: exp-003\n  claim: 3\n  title: Helped/hurt sample characterization\n  description: 'For each architecture''s helped/hurt samples on LAMBADA, compute:\n    (a) target token frequency (unigram rank in training data proxy), (b) context\n    length (token count), (c) last-sentence complexity (perplexity under baseline),\n    (d) topic/domain distribution. Test whether architecture-specific sample subsets\n    differ on these features.\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 1\n  deps: []\n  data_source: existing lambada per-example logprob data\n  pass_fail: ≥1 feature significantly differentiates helped vs hurt samples (p<0.01),\n    AND features differ across architectures\n  status_note: 'Phase 1 (surface features) DONE: all non-significant within-arch (p>0.2).\n    Phase 2 (perplexity) DONE: within-arch perplexity also non-significant (r_rb≈-0.04,\n    p>0.2). PASS on second criterion: cross-arch KW significant (hurt p=0.0005, helped\n    p=0.020). Different archs help/hurt samples with systematically different baseline\n    difficulty profiles. Both negative within-arch results are informative (rules\n    out trivial explanations). Cross-arch finding strengthens Claim 3 (architecture-specificity\n    is structured, not random).\n\n    '\n  status: planned\n- id: exp-004\n  claim: 3\n  title: Attention weight extraction and visualization\n  description: 'Extract attention weight patterns from hybrid models (h3-1 config)\n    for all 3 architectures. Analyze: (a) which positions attention focuses on, (b)\n    whether attention patterns correlate with helped/hurt sample identity, (c) cross-architecture\n    attention pattern similarity.\n\n    '\n  priority: P0\n  type: experiment\n  gpu_budget_hours: 4\n  deps:\n  - exp-003\n  pass_fail: Attention pattern differences documented; correlation with per-example\n    effects > 0.3\n  note: 'Upgraded P1→P0: mechanistic evidence is critical for Claim 3 and Reviewer\n    Concern C'\n  status: planned\n- id: exp-005\n  claim: 1\n  title: Architecture expansion check\n  description: 'Search Wang et al. model zoo and other sources for additional hybrid\n    architectures (Mamba/Mamba2 hybrids, RWKV hybrids, etc.). If found, evaluate on\n    LAMBADA to test whether convergence generalizes beyond GDN/RetNet/HGRN2.\n\n    '\n  priority: P1\n  type: experiment\n  gpu_budget_hours: 6\n  deps: []\n  pass_fail: ≥1 additional architecture evaluated and convergence pattern confirmed/denied\n  status: planned\n- id: exp-008\n  claim: 1\n  title: Statistical robustness framework\n  description: 'Implement bootstrap CIs for convergence metrics. Multi-comparison\n    correction (Bonferroni/FDR) across benchmarks. Sensitivity analysis: does conclusion\n    hold if GDN (with D004 confound) is excluded? Report effect sizes (Cohen''s d\n    / η²).\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  pass_fail: All core claims survive with GDN excluded; bootstrap 95% CIs don't cross\n    zero\n  status: planned\n- id: exp-009\n  claim: 1\n  title: Wang et al. explicit differentiation\n  description: 'Formal side-by-side comparison: what Wang et al. report vs our analysis.\n    Extract their exact convergence-related statements. Quantify the increment: (a)\n    they don''t compute cross-arch std trajectories, (b) no per-example analysis,\n    (c) no scale-dependent convergence characterization, (d) no mechanistic analysis.\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 0\n  deps: []\n  data_source: Wang et al. arXiv 2507.06457\n  pass_fail: Clear 4-point differentiation documented\n  status: planned\n- id: exp-010\n  claim: 3\n  title: Convergence-divergence bridge analysis\n  description: 'For LAMBADA, plot aggregate convergence curve alongside per-example\n    divergence metrics (Jaccard, net effect asymmetry) as function of attention ratio.\n    Show that convergence and divergence co-evolve—more attention = more aggregate\n    convergence BUT also more architecture-specific per-example effects. Core visualization\n    for Claim 3 (underspecification in hybrid architectures).\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-003\n  pass_fail: Convergence-divergence co-evolution demonstrated with significant correlation\n  status: planned\n- id: exp-011\n  claim: 1\n  title: Additional high-retrieval benchmarks (Dream W1 response)\n  description: 'Dream review: LAMBADA alone does not survive Bonferroni (p=0.017 >\n    α=0.0083). Need a second significant anchor point on a high-retrieval task. Run\n    1.3B models on additional retrieval-heavy benchmarks available in lm-eval: (a)\n    StoryCloze (context completion, structurally similar to LAMBADA), (b) BoolQ (passage-based\n    yes/no, context retrieval), (c) COPA (causal reasoning from short narratives).\n    Compute cross-arch std at each attention ratio for each benchmark. Test for convergence\n    (Spearman + exact permutation, two-tailed). If ANY shows significant convergence\n    → second anchor established, W1 substantially mitigated.\n\n    '\n  priority: P0\n  type: experiment\n  gpu_budget_hours: 8\n  deps: []\n  pass_fail: ≥1 additional benchmark shows significant convergence (p<0.05 two-tailed)\n  note: CRITICAL for Findings acceptance. Dream best case = 2.5 without this. Added\n    post-D006.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: hgrn2_eval_1_3b_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: hgrn2_eval_h3_1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval_340m_retnet_hgrn2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    LAMBADA:\n      rho: -1\n      p: 0.008\n      significant: true\n      taxonomy: retrieval-dependent\n    HellaSwag:\n      rho: 0.3\n      p: 0.742\n      significant: false\n      taxonomy: reasoning-dependent\n    ARC-C:\n      rho: 0.6\n      p: 0.883\n      significant: false\n      taxonomy: reasoning-dependent\n    Winogrande:\n      rho: 0.1\n      p: 0.608\n      significant: false\n      taxonomy: reasoning-dependent\n    ARC-Easy:\n      rho: -0.7\n      p: 0.117\n      significant: false\n      taxonomy: mixed\n    MMLU:\n      rho: -0.7\n      p: 0.117\n      significant: false\n      taxonomy: mixed\n    significant_count: 1/6\n    summary: Only LAMBADA shows significant convergence (rho=-1.0, p=0.008). Reasoning\n      tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\n- exp_id: exp-009\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    GDN:\n      helped: 462\n      hurt: 615\n      net: -153\n      surface_features_significant: false\n    HGRN2:\n      helped: 548\n      hurt: 395\n      net: 153\n      surface_features_significant: false\n    RetNet:\n      helped: 426\n      hurt: 495\n      net: -69\n      context_length_p: 0.012\n      context_length_r: -0.096\n      unique_tokens_p: 0.009\n      unique_tokens_r: -0.099\n    cross_arch_difference: not_significant\n    pass_fail: FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for\n      one arch only; criterion 2 (cross-arch difference) fails\n    summary: Surface features do not explain helped/hurt identity. Rules out trivial\n      explanations (frequency, length, diversity). RetNet shows weak context-length\n      signal (p=0.012, r=-0.096).\n- exp_id: exp-003-p2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    GDN:\n      U: 148410\n      p: 0.209189\n      r_rb: -0.0447\n      helped_mean: 3.3695\n      hurt_mean: 3.3382\n    RetNet:\n      U: 107210\n      p: 0.659319\n      r_rb: -0.0168\n      helped_mean: 3.4432\n      hurt_mean: 3.4207\n    HGRN2:\n      U: 112999\n      p: 0.247856\n      r_rb: -0.0441\n      helped_mean: 3.3775\n      hurt_mean: 3.3538\n    cross_arch_helped_KW_p: 0.020136\n    cross_arch_hurt_KW_p: 0.000498\n- exp_id: exp-011\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-008\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    LAMBADA:\n      rho: -1\n      raw_p: 0.0167\n      bonferroni_adj_p: 0.1\n      bh_fdr_adj_p: 0.1\n    HellaSwag:\n      rho: 0.3\n      raw_p: 0.6833\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.82\n    WinoGrande:\n      rho: 0.1\n      raw_p: 0.95\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.95\n    ARC-Easy:\n      rho: -0.7\n      raw_p: 0.2333\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.4667\n    ARC-Challenge:\n      rho: 0.6\n      raw_p: 0.35\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.525\n    MMLU:\n      rho: -0.7\n      raw_p: 0.2333\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.4667\n    method: exact_permutation_test_two_tailed\n    n_permutations: 120\n    bug_fixed: scipy.stats.spearmanr asymptotic p replaced with exact permutation\n    bootstrap_ci:\n      benchmark: LAMBADA\n      method: architecture_resampling_percentile\n      ci_lower: -1\n      ci_upper: -0.7\n      crosses_zero: false\n      n_bootstrap: 10000\n      n_valid: 8875\n      seed: 42\n      p_rho_negative: 1\n      p_rho_positive: 0\n      bca_note: BCa degenerate at rho=-1.0 boundary; percentile CI used\n    gdn_excluded:\n      LAMBADA:\n        rho: -0.7\n        exact_p: 0.2333\n        direction: WEAKER\n      HellaSwag:\n        rho: 0.5\n        exact_p: 0.45\n        direction: STRONGER\n      WinoGrande:\n        rho: 0.3\n        exact_p: 0.6833\n        direction: STRONGER\n      ARC-Easy:\n        rho: -0.9\n        exact_p: 0.0833\n        direction: STRONGER\n      ARC-Challenge:\n        rho: -0.2\n        exact_p: 0.7833\n        direction: WEAKER\n      MMLU:\n        rho: 0.6\n        exact_p: 0.35\n        direction: WEAKER\n      note: ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound\n        — suggestive second anchor\n- exp_id: exp-003-p2v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T14:50:48.211Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T14:50:48.211Z",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-19T14:50:48.232Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：exp-011 产出 suggestive 但非显著的第二 benchmark（p=0.05-0.15）；BH-FDR 仅保留 LAMBADA；exp-004 有描述性 attention 差异但相关偏弱；exp-005 无额外架构或结果 mixed。需要调整 claim 强度，但 task-specificity + per-example divergence 的组合故事仍可 Findings。
核心假设：['exp-011 最佳新 benchmark ρ ≈ -0.7 至 -0.8, p ≈ 0.08-0.15（suggestive, not significant）', 'BH-FDR 仅 LAMBADA 显著；但 LAMBADA + 新 benchmark 的 convergent direction 构成 pattern', 'exp-004 attention-effect correlation 0.15-0.30（可描述，不足以做 strong claim）', 'exp-005 未找到可评估的额外架构，或找到但 convergence 不显著', 'GDN-excluded ARC-Easy 维持在 ρ=-0.9, p≈0.08（suggestive, 补充证据）', 'exp-007 340M rebound 可部分解释但非完全清晰']
关键指标范围：{'exp011_best_new_rho': [-0.8, -0.6], 'exp011_best_new_p': [0.08, 0.2], 'n_benchmarks_BH_FDR_significant': [1, 1], 'exp004_attn_effect_correlation': [0.15, 0.3], 'lambada_cross_arch_std_reduction_pct': [75, 85], 'per_example_jaccard_range': [0.05, 0.12], 'n_architectures_total': [3, 3], 'n_suggestive_benchmarks_p_below_0_15': [2, 3]}
叙事方向：Claim 1 从 'task-dependent convergence' 弱化为 'convergence on retrieval-heavy tasks with suggestive evidence on related benchmarks'。LAMBADA 仍是 anchor，但通过 (a) 新 benchmark 的方向一致性（即使不显著），(b) GDN-excluded ARC-Easy 的改善，(c) principled task taxonomy 来构建 converging evidence 叙事。明确承认 Bonferroni failure，用 exact permutation p + percentile CI + 方向一致性作为论证。Claim 3 per-example divergence 成为相对更强的独立贡献。exp-004 以描述性证据出现（'attention patterns differ across architectures on affected samples'），避免 mechanistic language。目标 EMNLP Findings，honest framing。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: entrainment_gated_ft
venue: emnlp-2026
focus: This is a pivot from a failed entrainment hypothesis to an equalizer effect discovery. Key concerns: (1) only LAMBADA shows clear convergence — is the finding too narrow? (2) n=3 architectures — sufficient? (3) differentiation from Wang et al. who have the model zoo and noted qualitative convergence. (4) no 7B scale yet — two scales enough? Assess whether the equalizer paradox (aggregate convergence + per-example divergence) is novel and interesting enough for EMNLP Findings/Main.

## paper_framing.md

# Paper Framing — entrainment_gated_ft

> Revised 2026-05-19 after Dream review (best case = 2.5/5). Major reframing: drop "paradox" narrative, engage related work, add retrieval benchmarks.

## Target Venue
- Primary: EMNLP 2026 Findings (via ARR)
- Stretch: EMNLP 2026 Main
- Deadline: ARR June 2026 cycle (submission ~June 15)

## Paper Type
Empirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)

## Core Claims (3 条)

### Claim 1: Task-Dependent Convergence
Adding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength varies with task type. Convergence is strongest on LAMBADA (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, p=0.233, underpowered at n=5), and absent on reasoning-heavy tasks. **Critical need**: a second high-retrieval benchmark showing significant convergence to survive multi-comparison correction.

### Claim 2: Scale-Dependent Convergence
The convergence effect requires sufficient model capacity: monotonically complete at 1.3B (ρ=-1.0, p=0.017 two-tailed) but only partial at 340M with a non-monotonic rebound. Only two scale points (Wang et al. cap at 1.3B). Frame as binary contrast, not extrapolatable trend.

### Claim 3: Per-Example Divergence Under Aggregate Convergence
Despite aggregate convergence, attention acts on nearly non-overlapping sample subsets per architecture (pairwise Jaccard < 0.10). This is an instance of the well-documented underspecification phenomenon (D'Amour et al. 2022) applied to hybrid architectures. Our contribution is **quantifying** it in this specific context, NOT claiming to discover it. Surface features AND baseline model perplexity do not differentiate helped/hurt samples within an architecture — the effect is opaque to standard features. However, cross-architecture comparison reveals systematic differences in baseline difficulty profiles of affected samples (Kruskal-Wallis p=0.0005 for hurt samples), confirming the architecture-specificity is structured, not random noise.

## Story Spine

### Problem
Hybrid architectures mixing linear recurrence with full attention are becoming standard. While Wang et al. (2025) provide an extensive model zoo, the community lacks quantitative understanding of how attention affects cross-architecture behavioral diversity at the per-example level.

### Related Work Positioning (CRITICAL — Dream W2)
The observation that models with similar aggregate performance differ per-example is well-established:
- **Ensemble diversity**: Krogh & Vedelsby (1995), Kuncheva & Whitaker (2003) — diverse ensemble members err on different examples by construction
- **Underspecification**: D'Amour et al. (2022) — equivalent aggregate performance masks prediction-level differences
- **Dataset cartography**: Swayamdipta et al. (2020) — per-example difficulty varies across models
- **Simpson's paradox / ecological fallacy**: Aggregate-vs-disaggregate discrepancy is a textbook phenomenon

Our contribution is NOT discovering this phenomenon. It IS quantifying how it manifests specifically when attention is added to linear recurrent models, and characterizing its task-dependency and scale-dependency. This is valuable because hybrid architectures are a design choice practitioners make — understanding per-example implications informs that choice.

### Our Framing
We provide the first systematic per-example analysis of attention's equalizing effect in hybrid recurrent architectures. Using Wang et al.'s public model zoo (72 models), we quantify (a) task-dependent convergence strength, (b) scale-dependent convergence completeness, and (c) architecture-specific per-example divergence patterns. Our contribution is analytical depth on public infrastructure, not new methods or models.

### Headline Result Template
"At 1.3B scale, adding attention to hybrid recurrent models reduces cross-architecture variance by 79% on LAMBADA, yet per-example analysis reveals nearly non-overlapping affected sample subsets (Jaccard < 0.10) — a manifestation of underspecification that has practical implications for architecture selection."

## Dream Review Findings (D006) — Must Address

### W1: Single-benchmark significance [MAJOR, blocking]
After Bonferroni (6 benchmarks, α=0.0083), LAMBADA p=0.017 (two-tailed) does NOT survive. Need: (a) FDR correction (Benjamini-Hochberg) as primary reporting, (b) additional high-retrieval benchmarks for a second significant anchor. Candidates: StoryCloze, BoolQ, COPA, closed-book QA tasks available in lm-eval.

### W2: Missing related work [MAJOR, blocking for submission]
Need 20+ references engaging ensemble diversity, underspecification, dataset cartography, attention interpretability, hybrid architectures (Jamba, RWKV-6, RecurrentGemma). Paper Agent handles this during writing.

### W3: Mechanistic overclaiming [MAJOR, partially addressed]
Already reworded Claim 3 from "Mechanism" to "Effects". Must NOT use "mechanistic analysis" in paper — use "characterization" or "decomposition" instead. Attention weight analysis (exp-004) is descriptive, not causal. Frame honestly.

### W4: Incremental over Wang et al. [MAJOR]
Mitigate by: (a) engaging related work to show the QUESTION we ask is independently motivated by ensemble/underspecification literature, (b) framing contribution as analytical toolkit + quantitative characterization, not re-analysis. (c) Per-example analysis is genuinely novel for this model family.

## Venue Fit Risks
(unchanged from previous version, see git history)

## Anticipated Reviewer Concerns

### Concern A: "This is just a re-analysis of Wang et al.'s models"
Response: Yes, and that's the point — public infrastructure enables community analysis. Our per-example decomposition, task-dependency characterization, and scale-dependency analysis are not in Wang et al. The contribution is analytical, like meta-analyses in medicine.
Required: Strong Related Work positioning; frame as "community analysis" paper.

### Concern B: "Only one task shows the effect" + Bonferroni failure
**Statistical strategy** (from exp-008, verified by Reviewer with independent reproduction):
1. **Lead with percentile CI (valid-only)**: BCa degenerates at ρ=-1.0 boundary (z0=-3.86); fall back to percentile CI on valid bootstrap resamples (8875/10000; 11.25% degenerate from n=3 same-architecture redraws). Valid-only percentile CI = **[-1.0, -0.7]**, 100% of valid resamples have ρ<0. Full percentile CI (degenerate-as-zero) = [-1.0, 0.0] touches zero. Paper leads with valid-only CI; BCa degeneracy + degenerate-sample treatment in appendix.
2. **Report exact permutation p**: LAMBADA p=0.017 (two-tailed, 2/120 permutations). Honest and transparent.
3. **Bonferroni in supplementary**: adj-p=0.100 (two-tailed). Report honestly as "does not survive Bonferroni." BH-FDR also gives 0.100 (no additional benefit with only 1 small p-value). If exp-011 produces a second significant benchmark, BH-FDR becomes more favorable than Bonferroni.
4. **GDN-excluded sensitivity**: Excluding GDN (D004 confound): LAMBADA ρ drops to -0.7 (p=0.233); ARC-Easy ρ **improves** from -0.7 to -0.9 (p=0.083, suggestive — D004 noise removed); **⚠️ MMLU ρ FLIPS from -0.7 to +0.6** — MMLU apparent convergence was entirely GDN-driven and MUST NOT appear as convergence evidence anywhere in the paper (D007). Report both full and GDN-excluded analyses. The ARC-Easy improvement after confound removal is itself informative, especially in exp-011 context.
5. **exp-011**: Additional retrieval benchmarks (StoryCloze/BoolQ/COPA) for a potential second significant anchor. CRITICAL for acceptance — with exp-011 data, BH-FDR could diverge favorably from Bonferroni.
6. **Effect sizes**: Cohen's d CI crosses zero; omega² near zero. Do NOT lead with effect sizes — lead with BCa CI and convergence magnitude (std 0.024→0.005, 79% reduction).

Required experiments: exp-011 (additional retrieval benchmarks), exp-008 (robustness with corrected p-values), exp-002 (per-example validation).

### Concern C: "The per-example divergence is a known phenomenon"
Response: Acknowledge explicitly. Our contribution is quantification in hybrid architectures, not discovery of the phenomenon. Cite ensemble diversity + underspecification.
Required: Related Work section (Paper Agent).

### Concern D: "n=3 architectures is too few"
Response: 3 architectures × 5 ratios × 2 scales = 30 models. Per-example analysis provides 5153 data points per comparison. Check for additional architectures (exp-005).

### Concern E: "Two scales don't establish a trend"
Response: Binary contrast, not trend. 7B unavailable. Frame as "scale is a necessary condition." exp-007 for 340M rebound mechanism.

### Concern F: "No causal mechanism" (NEW from Dream)
Response: We do NOT claim causal mechanism. We characterize and describe. Attention weight analysis (exp-004) is descriptive. Interventional experiments (head swaps, ablations) are acknowledged as future work. Honest framing prevents overclaiming.


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  title: Task-specificity characterization of equalizer effect
  description: 'Compute cross-architecture variance (std) at each attention ratio
    for all 6 benchmarks. Known: only LAMBADA shows significant convergence (p<0.05).
    Goal: build principled task taxonomy (retrieval-dependent vs reasoning-dependent)
    explaining WHY convergence is task-specific. LAMBADA = last-word retrieval from
    context; HellaSwag/ARC = multi-step reasoning. Show the dichotomy is a feature
    (task-type modulation), not a limitation.

    '
  priority: P0
  type: analysis
  gpu_budget_hours: 0
  deps: []
  data_source: existing summary_all_1.3b.csv + 340M results + cross_scale_convergence
    output
  pass_fail: Clear task-type dichotomy with principled taxonomy; convergence correlates
    with retrieval demand
  reviewer_risk: 'Risk A — reframed per Reviewer warning: single-task convergence
    → task-specificity as positive finding'
  status: planned
- id: exp-002
  claim: 1
  title: Multi-benchmark per-example analysis (task-specificity validation)
  description: 'Re-run lm-eval on 1.3B models with --log_samples for HellaSwag, ARC-easy,
    ARC-challenge. Two goals: (a) confirm task-specificity — per-example convergence
    absent on reasoning tasks, (b) characterize HOW attention affects per-example
    behavior on non-converging tasks (random noise vs systematic but architecture-specific).
    Strengthens Claim 1 regardless of outcome.

    '
  priority: P0
  type: experiment
  gpu_budget_hours: 20
  deps:
  - exp-001
  pass_fail: Per-example data collected for ≥3 benchmarks; task-specificity of per-example
    mechanism confirmed or refuted
  reviewer_risk: 'Risk B — outcome determines Claim 1 scope: cross-task vs retrieval-specific
    equalizer'
  note: 'Budget revised to 20h per Reviewer data audit: need --log_samples for 10×340M
    (RetNet+HGRN2) + 3×1.3B (GDN h3-1/h6-1/h24-1). Uses freed exp-006 budget.'
  status: planned
- id: exp-006
  claim: 2
  title: 7B model evaluation — CANCELLED (unavailable)
  description: 'Wang et al. only have 340M + 1.3B (72 models total). Paper Limitations
    explicitly excludes 10B+. No 7B models exist. Budget reallocated to exp-002/004/005.

    '
  priority: cancelled
  type: experiment
  gpu_budget_hours: 0
  deps: []
  pass_fail: N/A — 7B unavailable, confirmed 2026-05-19
  status: planned
- id: exp-007
  claim: 2
  title: '340M rebound mechanism analysis (upgraded: compensate 7B absence)'
  description: 'Deep analysis of 340M non-monotonic rebound at attn=8. Per-example
    comparison with 1.3B at same attention ratio to identify which samples diverge.
    Characterize rebound samples. With 7B unavailable, this becomes the primary vehicle
    for Claim 2 depth — show the binary contrast (340M partial vs 1.3B complete) has
    mechanistic explanation, not just correlation with scale. Analyze training token
    count (20B vs 100B) as confound vs scale.

    '
  priority: P0
  type: analysis
  gpu_budget_hours: 2
  deps:
  - exp-002
  data_source: existing 340M results + new 1.3B per-example data
  pass_fail: Rebound mechanism identified with principled explanation; 340M vs 1.3B
    contrast characterized beyond aggregate metrics
  note: Upgraded from P1 to P0 after 7B cancellation. May need 340M per-example rerun
    (2h GPU).
  status: planned
- id: exp-003
  claim: 3
  title: Helped/hurt sample characterization
  description: 'For each architecture''s helped/hurt samples on LAMBADA, compute:
    (a) target token frequency (unigram rank in training data proxy), (b) context
    length (token count), (c) last-sentence complexity (perplexity under baseline),
    (d) topic/domain distribution. Test whether architecture-specific sample subsets
    differ on these features.

    '
  priority: P0
  type: analysis
  gpu_budget_hours: 1
  deps: []
  data_source: existing lambada per-example logprob data
  pass_fail: ≥1 feature significantly differentiates helped vs hurt samples (p<0.01),
    AND features differ across architectures
  status_note: 'Phase 1 (surface features) DONE: all non-significant within-arch (p>0.2).
    Phase 2 (perplexity) DONE: within-arch perplexity also non-significant (r_rb≈-0.04,
    p>0.2). PASS on second criterion: cross-arch KW significant (hurt p=0.0005, helped
    p=0.020). Different archs help/hurt samples with systematically different baseline
    difficulty profiles. Both negative within-arch results are informative (rules
    out trivial explanations). Cross-arch finding strengthens Claim 3 (architecture-specificity
    is structured, not random).

    '
  status: planned
- id: exp-004
  claim: 3
  title: Attention weight extraction and visualization
  description: 'Extract attention weight patterns from hybrid models (h3-1 config)
    for all 3 architectures. Analyze: (a) which positions attention focuses on, (b)
    whether attention patterns correlate with helped/hurt sample identity, (c) cross-architecture
    attention pattern similarity.

    '
  priority: P0
  type: experiment
  gpu_budget_hours: 4
  deps:
  - exp-003
  pass_fail: Attention pattern differences documented; correlation with per-example
    effects > 0.3
  note: 'Upgraded P1→P0: mechanistic evidence is critical for Claim 3 and Reviewer
    Concern C'
  status: planned
- id: exp-005
  claim: 1
  title: Architecture expansion check
  description: 'Search Wang et al. model zoo and other sources for additional hybrid
    architectures (Mamba/Mamba2 hybrids, RWKV hybrids, etc.). If found, evaluate on
    LAMBADA to test whether convergence generalizes beyond GDN/RetNet/HGRN2.

    '
  priority: P1
  type: experiment
  gpu_budget_hours: 6
  deps: []
  pass_fail: ≥1 additional architecture evaluated and convergence pattern confirmed/denied
  status: planned
- id: exp-008
  claim: 1
  title: Statistical robustness framework
  description: 'Implement bootstrap CIs for convergence metrics. Multi-comparison
    correction (Bonferroni/FDR) across benchmarks. Sensitivity analysis: does conclusion
    hold if GDN (with D004 confound) is excluded? Report effect sizes (Cohen''s d
    / η²).

    '
  priority: P0
  type: analysis
  gpu_budget_hours: 0
  deps:
  - exp-001
  pass_fail: All core claims survive with GDN excluded; bootstrap 95% CIs don't cross
    zero
  status: planned
- id: exp-009
  claim: 1
  title: Wang et al. explicit differentiation
  description: 'Formal side-by-side comparison: what Wang et al. report vs our analysis.
    Extract their exact convergence-related statements. Quantify the increment: (a)
    they don''t compute cross-arch std trajectories, (b) no per-example analysis,
    (c) no scale-dependent convergence characterization, (d) no mechanistic analysis.

    '
  priority: P0
  type: analysis
  gpu_budget_hours: 0
  deps: []
  data_source: Wang et al. arXiv 2507.06457
  pass_fail: Clear 4-point differentiation documented
  status: planned
- id: exp-010
  claim: 3
  title: Convergence-divergence bridge analysis
  description: 'For LAMBADA, plot aggregate convergence curve alongside per-example
    divergence metrics (Jaccard, net effect asymmetry) as function of attention ratio.
    Show that convergence and divergence co-evolve—more attention = more aggregate
    convergence BUT also more architecture-specific per-example effects. Core visualization
    for Claim 3 (underspecification in hybrid architectures).

    '
  priority: P0
  type: analysis
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-003
  pass_fail: Convergence-divergence co-evolution demonstrated with significant correlation
  status: planned
- id: exp-011
  claim: 1
  title: Additional high-retrieval benchmarks (Dream W1 response)
  description: 'Dream review: LAMBADA alone does not survive Bonferroni (p=0.017 >
    α=0.0083). Need a second significant anchor point on a high-retrieval task. Run
    1.3B models on additional retrieval-heavy benchmarks available in lm-eval: (a)
    StoryCloze (context completion, structurally similar to LAMBADA), (b) BoolQ (passage-based
    yes/no, context retrieval), (c) COPA (causal reasoning from short narratives).
    Compute cross-arch std at each attention ratio for each benchmark. Test for convergence
    (Spearman + exact permutation, two-tailed). If ANY shows significant convergence
    → second anchor established, W1 substantially mitigated.

    '
  priority: P0
  type: experiment
  gpu_budget_hours: 8
  deps: []
  pass_fail: ≥1 additional benchmark shows significant convergence (p<0.05 two-tailed)
  note: CRITICAL for Findings acceptance. Dream best case = 2.5 without this. Added
    post-D006.
  status: planned


## registry (completed experiments)

- exp_id: hgrn2_eval_1_3b_all
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: hgrn2_eval_h3_1
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: eval_340m_retnet_hgrn2
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp-001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    LAMBADA:
      rho: -1
      p: 0.008
      significant: true
      taxonomy: retrieval-dependent
    HellaSwag:
      rho: 0.3
      p: 0.742
      significant: false
      taxonomy: reasoning-dependent
    ARC-C:
      rho: 0.6
      p: 0.883
      significant: false
      taxonomy: reasoning-dependent
    Winogrande:
      rho: 0.1
      p: 0.608
      significant: false
      taxonomy: reasoning-dependent
    ARC-Easy:
      rho: -0.7
      p: 0.117
      significant: false
      taxonomy: mixed
    MMLU:
      rho: -0.7
      p: 0.117
      significant: false
      taxonomy: mixed
    significant_count: 1/6
    summary: Only LAMBADA shows significant convergence (rho=-1.0, p=0.008). Reasoning
      tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).
- exp_id: exp-009
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: exp-003
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    GDN:
      helped: 462
      hurt: 615
      net: -153
      surface_features_significant: false
    HGRN2:
      helped: 548
      hurt: 395
      net: 153
      surface_features_significant: false
    RetNet:
      helped: 426
      hurt: 495
      net: -69
      context_length_p: 0.012
      context_length_r: -0.096
      unique_tokens_p: 0.009
      unique_tokens_r: -0.099
    cross_arch_difference: not_significant
    pass_fail: FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for
      one arch only; criterion 2 (cross-arch difference) fails
    summary: Surface features do not explain helped/hurt identity. Rules out trivial
      explanations (frequency, length, diversity). RetNet shows weak context-length
      signal (p=0.012, r=-0.096).
- exp_id: exp-003-p2
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    GDN:
      U: 148410
      p: 0.209189
      r_rb: -0.0447
      helped_mean: 3.3695
      hurt_mean: 3.3382
    RetNet:
      U: 107210
      p: 0.659319
      r_rb: -0.0168
      helped_mean: 3.4432
      hurt_mean: 3.4207
    HGRN2:
      U: 112999
      p: 0.247856
      r_rb: -0.0441
      helped_mean: 3.3775
      hurt_mean: 3.3538
    cross_arch_helped_KW_p: 0.020136
    cross_arch_hurt_KW_p: 0.000498
- exp_id: exp-011
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: exp-008
  name: ''
  status: DONE
  conclusion: success
  metrics:
    LAMBADA:
      rho: -1
      raw_p: 0.0167
      bonferroni_adj_p: 0.1
      bh_fdr_adj_p: 0.1
    HellaSwag:
      rho: 0.3
      raw_p: 0.6833
      bonferroni_adj_p: 1
      bh_fdr_adj_p: 0.82
    WinoGrande:
      rho: 0.1
      raw_p: 0.95
      bonferroni_adj_p: 1
      bh_fdr_adj_p: 0.95
    ARC-Easy:
      rho: -0.7
      raw_p: 0.2333
      bonferroni_adj_p: 1
      bh_fdr_adj_p: 0.4667
    ARC-Challenge:
      rho: 0.6
      raw_p: 0.35
      bonferroni_adj_p: 1
      bh_fdr_adj_p: 0.525
    MMLU:
      rho: -0.7
      raw_p: 0.2333
      bonferroni_adj_p: 1
      bh_fdr_adj_p: 0.4667
    method: exact_permutation_test_two_tailed
    n_permutations: 120
    bug_fixed: scipy.stats.spearmanr asymptotic p replaced with exact permutation
    bootstrap_ci:
      benchmark: LAMBADA
      method: architecture_resampling_percentile
      ci_lower: -1
      ci_upper: -0.7
      crosses_zero: false
      n_bootstrap: 10000
      n_valid: 8875
      seed: 42
      p_rho_negative: 1
      p_rho_positive: 0
      bca_note: BCa degenerate at rho=-1.0 boundary; percentile CI used
    gdn_excluded:
      LAMBADA:
        rho: -0.7
        exact_p: 0.2333
        direction: WEAKER
      HellaSwag:
        rho: 0.5
        exact_p: 0.45
        direction: STRONGER
      WinoGrande:
        rho: 0.3
        exact_p: 0.6833
        direction: STRONGER
      ARC-Easy:
        rho: -0.9
        exact_p: 0.0833
        direction: STRONGER
      ARC-Challenge:
        rho: -0.2
        exact_p: 0.7833
        direction: WEAKER
      MMLU:
        rho: 0.6
        exact_p: 0.35
        direction: WEAKER
      note: ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound
        — suggestive second anchor
- exp_id: exp-003-p2v2
  name: ''
  status: PREPARING
  conclusion: killed
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
  "promptId": "50b564de-81f5-49b6-bcfd-55798e27f08a",
  "type": "user",
  "uuid": "96b3ae4b-53bb-4320-ab24-9cfc152e25ba",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T14:50:48.231Z_

```json
{
  "parentUuid": "96b3ae4b-53bb-4320-ab24-9cfc152e25ba",
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
  "uuid": "4f8704ba-4173-4a73-9e59-6d2c79b49da2",
  "timestamp": "2026-05-19T14:50:48.231Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T14:50:48.231Z_

```json
{
  "parentUuid": "4f8704ba-4173-4a73-9e59-6d2c79b49da2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bfdfbe6c-dee7-4fd1-be37-95ba88d7ad73",
  "timestamp": "2026-05-19T14:50:48.231Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：exp-011 产出 suggestive 但非显著的第二 benchmark（p=0.05-0.15）；BH-FDR 仅保留 LAMBADA；exp-004 有描述性 attention 差异但相关偏弱；exp-005 无额外架构或结果 mixed。需要调整 claim 强度，但 task-specif…",
  "leafUuid": "bfdfbe6c-dee7-4fd1-be37-95ba88d7ad73",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Entrainment gated fine-tuning: median-tier findings experiment plan",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4"
}
```

---

### Assistant

_source line 8 · 2026-05-19T14:51:18.300Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined/predicted experimental data for each planned experiment in the experiment_plan, based on the "median" tier definition provided. Each prediction needs a result_rationale explaining why that result would occur in this tier.

Let me go through each planned experiment and generate median-tier predictions.

Planned experiments (status: planned):
1. exp-001 - DONE already
2. exp-002 - planned, P0
3. exp-006 - cancelled
4. exp-007 - planned, P0
5. exp-003 - DONE already (with exp-003-p2)


6. exp-004 - planned, P0
7. exp-005 - planned, P1
8. exp-008 - DONE already
9. exp-009 - DONE already
10. exp-010 - planned, P0
11. exp-011 - PREPARING

So I need to identify which experiments have "planned" status and generate predictions for those. Looking at the list, the ones I need to create median-tier predictions for are: exp-002, exp-004, exp-005, exp-007, exp-010, and exp-011. Let me verify this against the actual experiment_plan to make sure I'm capturing all the planned experiments correctly. Looking at the experiment_plan, I notice a discrepancy: all experiments are marked as "planned," but several already show completion status in the registry. I need to decide whether to predict outcomes for all planned experiments or focus only on those that haven't run yet. Given that Phase 1 is about establishing median tier baselines, I think the user wants predictions for the experiments still pending—exp-002, exp-004, exp-005, exp-007, exp-010, and exp-011—while noting the actual results for the ones already completed.

Now I'm working through the median tier constraints to anchor my predictions: exp-011 should show a correlation around -0.7 to -0.8 with p-values between 0.08-0.15 (suggestive but not statistically significant), and the pattern across LAMBADA and the new benchmark should show convergent directionality even if only LAMBADA reaches BH-FDR significance.

For the remaining experiments, I'm setting realistic ranges: exp-004's attention-effect correlation should fall between 0.15-0.30 as a descriptive finding, exp-005 likely shows no significant additional architecture effects, the GDN-excluded ARC-Easy result mirrors the suggestive pattern with ρ≈-0.9 and p≈0.08, and exp-007's 340M rebound remains partially explained but with lingering uncertainty.

I'm now defining the specific metric ranges that will structure the full YAML output across all experiments. Now I'm laying out detailed predictions for each experiment, noting which ones are complete and which need specific analytical approaches—attention weight correlations for some, convergence analysis for others, and careful interpretation of borderline significance results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bfdfbe6c-dee7-4fd1-be37-95ba88d7ad73",
  "isSidechain": false,
  "requestId": "req_011CbC7cRCzc94SraA2Fz5Qd",
  "type": "assistant",
  "uuid": "41b7e675-9c4c-45c1-a69c-45a0c838c6dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5YWUUNWQPptZr28o8hmBP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13392,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13378,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13392
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

_source line 9 · 2026-05-19T14:54:56.973Z_

```yaml
tier: median
narrative_guidance: >
  Claim 1 弱化为 'convergence on retrieval-heavy tasks with suggestive evidence on related benchmarks'。
  LAMBADA 仍为唯一 BH-FDR 显著锚点，但 exp-011 新 benchmark 方向一致性 + GDN-excluded ARC-Easy 改善
  构成 converging evidence pattern。exp-004 以描述性证据呈现，避免 mechanistic language。
  exp-005 未扩展架构数量。exp-007 部分解释 340M rebound 但留有未解问题。
  Claim 3 per-example divergence 成为论文相对最强的独立贡献。目标 EMNLP Findings，honest framing。

imagined_experiments:
  - name: "Task-specificity characterization of equalizer effect"
    plan_id: "exp-001"
    description: "计算 6 个 benchmark 在每个 attention ratio 下的 cross-architecture std，建立 task taxonomy"
    expected_results:
      LAMBADA_rho: -1.0
      LAMBADA_p: 0.008
      LAMBADA_taxonomy: "retrieval-dependent"
      LAMBADA_std_reduction_pct: 79
      HellaSwag_rho: 0.3
      HellaSwag_p: 0.742
      HellaSwag_taxonomy: "reasoning-dependent"
      ARC_Challenge_rho: 0.6
      ARC_Challenge_p: 0.883
      ARC_Challenge_taxonomy: "reasoning-dependent"
      Winogrande_rho: 0.1
      Winogrande_p: 0.608
      Winogrande_taxonomy: "reasoning-dependent"
      ARC_Easy_rho: -0.7
      ARC_Easy_p: 0.117
      ARC_Easy_taxonomy: "mixed"
      MMLU_rho: -0.7
      MMLU_p: 0.117
      MMLU_taxonomy: "mixed"
      significant_count: "1/6"
    result_rationale: >
      已完成实验。LAMBADA 作为 last-word-in-context retrieval task，attention 直接增强了从上文提取目标词的能力，
      且三种架构的 baseline 缺陷高度同质（都缺少 global attention），因此 attention 的补偿效应方向一致、
      幅度相近，产生强 convergence。Reasoning tasks (HellaSwag, ARC-C, Winogrande) 依赖多步推理链，
      attention 的增益是架构特异性的（不同 recurrent backbone 的 bottleneck 不同），所以不 converge。
      ARC-Easy 和 MMLU 介于两者之间：含部分 retrieval 成分但也需要 world knowledge，产生 suggestive 但不显著的趋势。
    tables:
      - name: "Table 1: Task-specificity of convergence effect"
        columns: ["Benchmark", "Task Type", "ρ (Spearman)", "p (exact perm.)", "Std Reduction %", "Taxonomy"]
        rows:
          - ["LAMBADA", "last-word retrieval", -1.0, 0.008, "79%", "retrieval-dependent"]
          - ["ARC-Easy", "factual QA", -0.7, 0.117, "42%", "mixed"]
          - ["MMLU", "knowledge QA", -0.7, 0.117, "38%", "mixed"]
          - ["HellaSwag", "commonsense reasoning", 0.3, 0.742, "+15%", "reasoning-dependent"]
          - ["Winogrande", "coreference reasoning", 0.1, 0.608, "+8%", "reasoning-dependent"]
          - ["ARC-Challenge", "multi-step reasoning", 0.6, 0.883, "+22%", "reasoning-dependent"]
    figures_description:
      - "Fig 1: 6-panel grid, 每个 benchmark 一个 panel。X 轴 = attention ratio (h0→h24), Y 轴 = cross-arch std。LAMBADA panel 展示清晰下降趋势，reasoning tasks 平坦或上升。"
    analysis: >
      Taxonomy 清晰分为三档：retrieval-dependent (LAMBADA, 强 convergence)、mixed (ARC-Easy/MMLU, suggestive)、
      reasoning-dependent (HellaSwag/Winogrande/ARC-C, 无 convergence 或反向)。这支持 attention 的 equalizer
      效应是 task-modulated 的解释——当 task 的关键 bottleneck 恰好是 global context retrieval 时，
      attention 对所有架构提供相似的补偿。

  - name: "Multi-benchmark per-example analysis"
    plan_id: "exp-002"
    description: "对 HellaSwag/ARC-Easy/ARC-Challenge 收集 --log_samples per-example 数据，验证 task-specificity 在 per-example 层面的表现"
    expected_results:
      n_models_rerun: 13
      models_340m: ["RetNet×5", "HGRN2×5"]
      models_1_3b: ["GDN h3-1", "GDN h6-1", "GDN h24-1"]
      HellaSwag_per_example_n: 10042
      ARC_Easy_per_example_n: 2376
      ARC_Challenge_per_example_n: 1172
      HellaSwag_cross_arch_jaccard_helped: 0.18
      HellaSwag_cross_arch_jaccard_hurt: 0.15
      ARC_Easy_cross_arch_jaccard_helped: 0.14
      ARC_Easy_cross_arch_jaccard_hurt: 0.11
      ARC_Challenge_cross_arch_jaccard_helped: 0.12
      ARC_Challenge_cross_arch_jaccard_hurt: 0.10
      LAMBADA_reference_jaccard: 0.08
      task_specificity_per_example_confirmed: true
      reasoning_task_pattern: "systematic_but_architecture_specific"
      gpu_hours_actual: 18
    result_rationale: >
      Median 档下，per-example 数据成功收集但揭示了 nuanced pattern：reasoning tasks 的 per-example Jaccard
      比 LAMBADA 高（0.10-0.18 vs 0.05-0.10），说明 attention 在 reasoning tasks 上影响的样本集有更多重叠，
      但这种重叠并不 translate 为 aggregate convergence（因为影响方向和幅度是架构特异的）。
      LAMBADA 的低 Jaccard 反而说明：aggregate convergence 不是因为 attention 帮助了相同的样本，
      而是因为不同样本的帮助在 aggregate 层面恰好相互补偿到相似水平。
      这加强了 Claim 3 的 underspecification 叙事——convergence 和 per-example agreement 是正交的维度。
      Reasoning tasks 展示 "systematic but architecture-specific" pattern：每个架构内 helped/hurt 有结构性，
      但跨架构差异大到无法 aggregate converge。
    tables:
      - name: "Table: Per-example overlap (Jaccard) across benchmarks at h3-1, 1.3B"
        columns: ["Benchmark", "Jaccard (helped)", "Jaccard (hurt)", "LAMBADA ref.", "Interpretation"]
        rows:
          - ["LAMBADA", 0.08, 0.07, "—", "Low overlap → different samples helped per arch"]
          - ["HellaSwag", 0.18, 0.15, "2.3×", "Higher overlap but no aggregate convergence"]
          - ["ARC-Easy", 0.14, 0.11, "1.8×", "Moderate overlap, suggestive convergence"]
          - ["ARC-Challenge", 0.12, 0.10, "1.5×", "Moderate overlap, no convergence"]
    figures_description:
      - "Fig: Jaccard heatmap (3 arch pairs × 4 benchmarks), 颜色编码 per-example overlap。LAMBADA 行最冷（低 overlap），HellaSwag 行最暖。"
      - "Fig: Per-example effect scatter (baseline ppl vs Δ accuracy) for each benchmark × architecture，展示 reasoning tasks 的架构特异性 pattern。"
    analysis: >
      Per-example 数据确认 task-specificity 不仅存在于 aggregate 层面，也存在于 per-example 层面，但方式不同于预期。
      Reasoning tasks 有更高的 per-example overlap（attention 倾向于影响某些 "universally tricky" 样本），
      但影响的方向和幅度架构特异。LAMBADA 的低 overlap + 高 aggregate convergence 构成最强的 underspecification 案例。
      exp-002 的结论：Claim 1 的 task-specificity 在 per-example 层面同样成立但机制更复杂；
      Claim 3 的 per-example divergence 在 LAMBADA 上最极端，但在所有 tasks 上都存在（程度不同）。

  - name: "Attention weight extraction and visualization"
    plan_id: "exp-004"
    description: "提取 3 种架构 h3-1 配置的 attention weights，分析与 helped/hurt sample 的关联"
    expected_results:
      n_models_analyzed: 3
      attention_configs: "h3-1 (1 attention layer in 3-layer block)"
      n_lambada_samples_analyzed: 500
      attn_entropy_GDN_mean: 3.42
      attn_entropy_RetNet_mean: 3.18
      attn_entropy_HGRN2_mean: 3.55
      attn_pattern_helped_hurt_correlation_GDN: 0.22
      attn_pattern_helped_hurt_correlation_RetNet: 0.18
      attn_pattern_helped_hurt_correlation_HGRN2: 0.25
      mean_attn_effect_correlation: 0.22
      cross_arch_attn_similarity_cosine: 0.35
      attn_focus_last_sentence_pct_GDN: 62
      attn_focus_last_sentence_pct_RetNet: 55
      attn_focus_last_sentence_pct_HGRN2: 58
      helped_vs_hurt_attn_entropy_diff_p: 0.08
      gpu_hours_actual: 3.5
    result_rationale: >
      Median 档下，attention-effect correlation 落在 0.15-0.30 区间（实际均值 0.22）。
      这不足以做 strong mechanistic claim，但足以做描述性报告。原因：
      (1) attention weights 只是 model 行为的 partial view——per-example 效果由 attention + recurrent backbone
      的交互决定，单看 attention 只能捕获部分 variance。
      (2) h3-1 配置仅 1 层 attention（在 3 层 block 中），信息密度有限。
      (3) 不同架构的 attention 确实 focus 在不同位置（cross-arch cosine similarity 仅 0.35），
      这与 per-example divergence 一致——架构之间 attention 的 "关注点" 不同。
      (4) 所有架构的 attention 都倾向于 focus on last sentence（55-62%），这与 LAMBADA 的 retrieval nature 一致，
      但具体 token-level focus 差异显著。
      Helped 样本的 attention entropy 略低于 hurt 样本（p=0.08），暗示 attention 在 "知道该看哪里" 时更有效，
      但这只是 suggestive。
    tables:
      - name: "Table: Attention pattern statistics by architecture (h3-1, 1.3B, LAMBADA)"
        columns: ["Architecture", "Mean Entropy", "Last-Sentence Focus %", "Helped-Hurt Corr.", "Helped Entropy", "Hurt Entropy"]
        rows:
          - ["GDN", 3.42, "62%", 0.22, 3.31, 3.52]
          - ["RetNet", 3.18, "55%", 0.18, 3.10, 3.28]
          - ["HGRN2", 3.55, "58%", 0.25, 3.42, 3.65]
      - name: "Table: Cross-architecture attention similarity"
        columns: ["Arch Pair", "Cosine Sim (mean attn)", "Cosine Sim (helped subset)", "Cosine Sim (hurt subset)"]
        rows:
          - ["GDN–RetNet", 0.33, 0.28, 0.31]
          - ["GDN–HGRN2", 0.38, 0.35, 0.33]
          - ["RetNet–HGRN2", 0.34, 0.30, 0.29]
    figures_description:
      - "Fig: Attention heatmap (3 panels, one per arch) on 5 representative LAMBADA examples, showing divergent focus patterns across architectures on the same input."
      - "Fig: Scatter plot of per-sample attention entropy vs Δ accuracy for each architecture. Weak negative trend (r≈0.18-0.25) with wide scatter."
    analysis: >
      Attention patterns 确认三种架构的 attention 在 same input 上 focus 不同位置（cosine sim ≈ 0.35），
      这与 per-example Jaccard < 0.10 一致。但 attention-effect correlation 仅 0.22，不足以说
      "attention pattern 决定了 which samples are helped"——只能说 "attention patterns differ across
      architectures on affected samples"。Paper 中以描述性语言呈现："We observe that attention
      allocation patterns diverge across architectures (mean cosine similarity = 0.35), consistent
      with the per-example divergence reported in Section X. However, the modest correlation between
      attention statistics and per-example effects (r = 0.22) suggests that attention weights alone
      do not fully account for the architecture-specific patterns." 避免 "mechanistic" 一词。

  - name: "Architecture expansion check"
    plan_id: "exp-005"
    description: "搜索 Wang et al. model zoo 和其他来源，寻找额外 hybrid 架构（Mamba hybrids, RWKV hybrids 等）"
    expected_results:
      additional_architectures_found: 0
      wang_et_al_architectures_checked: ["GatedDeltaNet", "RetNet", "HGRN2", "DeltaNet", "RWKV6", "Mamba"]
      hybrid_configs_available: ["GatedDeltaNet", "RetNet", "HGRN2"]
      non_hybrid_only: ["DeltaNet", "RWKV6", "Mamba"]
      reason_no_expansion: "Wang et al. model zoo 中只有 GDN/RetNet/HGRN2 有 attention-hybrid 配置；DeltaNet/RWKV6/Mamba 仅有 pure recurrent。外部无 compatible hybrid checkpoints。"
      n_architectures_final: 3
      gpu_hours_actual: 0
    result_rationale: >
      Median 档核心假设：exp-005 未找到可评估的额外架构。
      Wang et al. 的 model zoo 设计上只为 GDN/RetNet/HGRN2 提供了 hybrid (attention-augmented) 配置，
      因为这三种是他们论文的重点对比对象。DeltaNet、RWKV6、Mamba 等只有 pure recurrent checkpoints，
      没有对应的 hybrid variants。外部开源社区（HuggingFace、GitHub）的 hybrid checkpoints 要么训练设置不同
      （不同数据、不同 tokenizer），要么规模不匹配，无法做 controlled comparison。
      因此 n=3 架构是硬限制。Paper 在 Limitations 中诚实说明："Our analysis is limited to three
      architectures with publicly available hybrid configurations. Extending to Mamba-2 or RWKV-6
      hybrids requires training new models, which we leave to future work."
    tables: []
    figures_description: []
    analysis: >
      未产生新数据。n=3 限制通过两种方式 mitigate：
      (1) 论证 3 architectures × 5 attention ratios × 2 scales = 30 model configurations 提供了足够的统计结构；
      (2) per-example analysis 提供 5153 data points per pairwise comparison，补偿了架构数量的不足。
      Reviewer Concern D 的回应策略不变。

  - name: "7B model evaluation — CANCELLED"
    plan_id: "exp-006"
    description: "7B 模型不可用，已取消。预算重新分配。"
    expected_results:
      status: "cancelled"
      reason: "Wang et al. 仅提供 340M + 1.3B (72 models total)"
    result_rationale: "Wang et al. model zoo 不包含 7B 规模模型。无外部可比较的 hybrid 7B checkpoints。"
    tables: []
    figures_description: []
    analysis: "预算重新分配给 exp-002 和 exp-004。Claim 2 限制为 binary scale contrast。"

  - name: "340M rebound mechanism analysis"
    plan_id: "exp-007"
    description: "分析 340M 在 attn=8 处的 non-monotonic rebound，与 1.3B 做 per-example 对比"
    expected_results:
      rebound_attention_ratio: "h8 (8/24 attention layers)"
      rebound_magnitude_std_increase: "35-40% relative to h6 minimum"
      n_rebound_samples_340m: 280
      n_rebound_samples_overlap_with_1_3b_hurt: 95
      overlap_pct: 34
      rebound_sample_characteristics:
        mean_context_length: 42.3
        mean_target_frequency_rank: 8500
        mean_baseline_ppl: 4.8
      partial_explanation_pct: 60
      capacity_saturation_hypothesis: "supported_but_not_conclusive"
      training_tokens_confound: "acknowledged_not_resolved"
      arch_specific_rebound:
        GDN_340m_rebound: "moderate (std +30%)"
        RetNet_340m_rebound: "strong (std +55%)"
        HGRN2_340m_rebound: "weak (std +20%)"
      gpu_hours_actual: 2
    result_rationale: >
      Median 档核心假设：340M rebound 可部分解释但非完全清晰。
      部分解释（~60%）：340M 模型在 h8 ratio 时，attention 层数已占 1/3 的 model capacity，
      对于小模型来说 attention 的参数开销（QKV projections）挤占了 recurrent backbone 的表达能力，
      导致某些样本从 "helped by attention" 回退到 "hurt by capacity reallocation"。
      具体表现为：rebound 样本与 1.3B 的 hurt 样本有 34% 重叠——这些是 "需要 attention 但也需要
      足够 recurrent capacity 来编码上下文" 的样本。1.3B 有足够 capacity 同时支持两者。
      未解释部分（~40%）：不同架构的 rebound 幅度差异大（RetNet 最强 +55%，HGRN2 最弱 +20%），
      暗示 rebound 不仅是 capacity issue，还与 backbone 的 inductive bias 有关。
      训练 token 数量差异（340M: 20B tokens, 1.3B: 100B tokens）作为 confound 被承认但无法分离——
      需要 controlled training runs 才能解开，超出本文 scope。
    tables:
      - name: "Table: 340M rebound characterization by architecture"
        columns: ["Architecture", "h6 Std", "h8 Std", "Rebound %", "N Rebound Samples", "Overlap with 1.3B Hurt %"]
        rows:
          - ["GDN", 0.018, 0.023, "+30%", 85, "38%"]
          - ["RetNet", 0.015, 0.023, "+55%", 120, "31%"]
          - ["HGRN2", 0.020, 0.024, "+20%", 75, "33%"]
      - name: "Table: Rebound sample characteristics vs non-rebound"
        columns: ["Feature", "Rebound Samples", "Non-Rebound", "p (MW-U)"]
        rows:
          - ["Context length (tokens)", 42.3, 35.1, 0.03]
          - ["Target freq rank", 8500, 6200, 0.07]
          - ["Baseline ppl (340M)", 4.8, 3.5, 0.01]
          - ["Baseline ppl (1.3B)", 3.1, 2.8, 0.22]
    figures_description:
      - "Fig: Cross-arch std trajectory at 340M showing non-monotonic rebound at h8, with 1.3B monotonic curve overlaid for contrast."
      - "Fig: Venn diagram of rebound samples at 340M vs hurt samples at 1.3B, showing 34% overlap."
    analysis: >
      Binary contrast narrative：1.3B 的 monotonic convergence vs 340M 的 non-monotonic rebound
      表明 "convergence requires sufficient capacity"。Rebound 样本是 "harder" samples（higher baseline ppl,
      longer context），这些样本在 340M 下面临 capacity-attention tradeoff。
      Paper framing："The non-monotonic pattern at 340M suggests a capacity threshold: smaller models
      face a tradeoff between recurrent backbone capacity and attention coverage, with the rebound
      at h8 disproportionately affecting longer-context, higher-difficulty examples (baseline ppl 4.8 vs 3.5, p=0.01)."
      诚实承认：training token confound 和 architecture-specific rebound variance 未完全解释。
      这足以支持 Claim 2 的 binary contrast framing，但不足以做 extrapolation 或 general scaling law claim。

  - name: "Helped/hurt sample characterization"
    plan_id: "exp-003"
    description: "分析 LAMBADA 上每种架构的 helped/hurt 样本特征（surface features + perplexity）"
    expected_results:
      phase1_surface_features:
        GDN_helped: 462
        GDN_hurt: 615
        GDN_surface_significant: false
        HGRN2_helped: 548
        HGRN2_hurt: 395
        HGRN2_surface_significant: false
        RetNet_helped: 426
        RetNet_hurt: 495
        RetNet_context_length_p: 0.012
        RetNet_context_length_r: -0.096
        RetNet_unique_tokens_p: 0.009
        RetNet_unique_tokens_r: -0.099
        cross_arch_difference_significant: false
      phase2_perplexity:
        GDN_r_rb: -0.04
        GDN_p: 0.209
        RetNet_r_rb: -0.02
        RetNet_p: 0.659
        HGRN2_r_rb: -0.04
        HGRN2_p: 0.248
        within_arch_significant: false
        cross_arch_hurt_KW_p: 0.0005
        cross_arch_helped_KW_p: 0.020
    result_rationale: >
      已完成实验。Within-architecture：surface features 和 baseline perplexity 均无法区分 helped/hurt
      样本（所有 within-arch p > 0.2，effect size 极小）。这 rules out trivial explanations——
      不是简单的 "长句子被 attention 帮助" 或 "难样本被帮助"。
      Cross-architecture：不同架构 hurt 的样本有 systematically different baseline difficulty profiles
      (KW p=0.0005)。这表明每种架构 "struggle with" 不同难度分布的样本，attention 帮助/伤害的样本
      子集因此不同。这是 structured diversity, not random noise——支持 Claim 3。
    tables:
      - name: "Table: Within-architecture perplexity analysis"
        columns: ["Architecture", "Helped Mean PPL", "Hurt Mean PPL", "U statistic", "p", "r_rb"]
        rows:
          - ["GDN", 3.37, 3.34, 148410, 0.209, -0.045]
          - ["RetNet", 3.44, 3.42, 107210, 0.659, -0.017]
          - ["HGRN2", 3.38, 3.35, 112999, 0.248, -0.044]
      - name: "Table: Cross-architecture Kruskal-Wallis tests"
        columns: ["Sample Type", "KW H", "p", "Interpretation"]
        rows:
          - ["Hurt samples", "—", 0.0005, "Architectures hurt samples with different difficulty profiles"]
          - ["Helped samples", "—", 0.020, "Weaker but significant cross-arch difference"]
    figures_description:
      - "Fig: Violin plots of baseline perplexity distributions for hurt samples, split by architecture. Visually distinct distributions despite non-significant within-arch effects."
    analysis: >
      Two-level finding：(1) within-arch opacity (attention effects 无法用 surface features/perplexity 预测)，
      (2) cross-arch structure (不同架构的 affected samples 有 systematically different profiles)。
      这同时加强 Claim 3 的两个方面——divergence 不是 random noise（structured），
      但也不是 trivially predictable（opaque to standard features）。

  - name: "Statistical robustness framework"
    plan_id: "exp-008"
    description: "Bootstrap CIs、multiple comparison correction、GDN-excluded sensitivity analysis"
    expected_results:
      LAMBADA_rho: -1.0
      LAMBADA_exact_p_two_tailed: 0.0167
      LAMBADA_bonferroni_adj_p: 0.100
      LAMBADA_bh_fdr_adj_p: 0.100
      bootstrap_ci_lower: -1.0
      bootstrap_ci_upper: -0.7
      bootstrap_ci_crosses_zero: false
      bootstrap_n_valid: 8875
      bootstrap_n_total: 10000
      bca_degenerate: true
      gdn_excluded_LAMBADA_rho: -0.7
      gdn_excluded_LAMBADA_p: 0.233
      gdn_excluded_ARC_Easy_rho: -0.9
      gdn_excluded_ARC_Easy_p: 0.083
      gdn_excluded_MMLU_rho: 0.6
      gdn_excluded_MMLU_direction: "FLIPPED — convergence was GDN-driven artifact"
      MMLU_must_exclude_from_convergence_evidence: true
    result_rationale: >
      已完成实验。LAMBADA 不通过 Bonferroni（adj-p=0.100 > 0.0083），BH-FDR 在仅 1 个小 p-value 时
      无额外收益（也是 0.100）。Bootstrap percentile CI [-1.0, -0.7] 不过零，这是论文的 primary
      statistical argument——方向性确定，只是精确 p-value 在 multi-comparison 下失去显著性。
      GDN-excluded 分析揭示两个关键发现：(a) ARC-Easy rho 从 -0.7 改善到 -0.9（p=0.083），
      说明 GDN confound 在 ARC-Easy 上是噪声源，去除后 convergence signal 更强；
      (b) MMLU rho 从 -0.7 翻转到 +0.6，MMLU 的 apparent convergence 完全由 GDN 驱动，是 artifact。
      这要求 paper 严格标记 MMLU 为 non-convergent。
    tables:
      - name: "Table: Multiple comparison correction (6 benchmarks)"
        columns: ["Benchmark", "ρ", "Raw p", "Bonferroni adj-p", "BH-FDR adj-p"]
        rows:
          - ["LAMBADA", -1.0, 0.017, 0.100, 0.100]
          - ["ARC-Easy", -0.7, 0.233, 1.000, 0.467]
          - ["MMLU", -0.7, 0.233, 1.000, 0.467]
          - ["ARC-Challenge", 0.6, 0.350, 1.000, 0.525]
          - ["HellaSwag", 0.3, 0.683, 1.000, 0.820]
          - ["Winogrande", 0.1, 0.950, 1.000, 0.950]
      - name: "Table: GDN-excluded sensitivity"
        columns: ["Benchmark", "Full ρ", "GDN-excl ρ", "GDN-excl p", "Direction"]
        rows:
          - ["LAMBADA", -1.0, -0.7, 0.233, "Weaker (expected — n drops)"]
          - ["ARC-Easy", -0.7, -0.9, 0.083, "Stronger (confound removed)"]
          - ["MMLU", -0.7, 0.6, 0.350, "⚠️ FLIPPED — artifact"]
    figures_description:
      - "Fig: Bootstrap distribution of LAMBADA ρ (10K resamples), with percentile CI marked. 100% of valid resamples have ρ < 0."
    analysis: >
      Statistical strategy for paper：lead with percentile CI (方向性 certain)，report exact permutation p
      (transparent)，Bonferroni failure 在 supplementary 诚实报告。GDN-excluded analysis 作为 robustness check，
      ARC-Easy improvement 作为 additional evidence point。MMLU flipping 是重要 negative result，
      必须在 paper 中报告以避免 cherry-picking 指控。

  - name: "Wang et al. explicit differentiation"
    plan_id: "exp-009"
    description: "与 Wang et al. 的系统性对比，量化 incremental contribution"
    expected_results:
      differentiation_points: 4
      wang_no_cross_arch_std_trajectory: true
      wang_no_per_example_analysis: true
      wang_no_scale_dependent_convergence: true
      wang_no_attention_characterization: true
      wang_qualitative_convergence_mentioned: true
      wang_exact_quote: "models tend to converge in performance as attention ratio increases"
      our_quantification: "ρ=-1.0, std 0.024→0.005 (79% reduction), exact permutation p=0.017"
    result_rationale: >
      已完成实验。Wang et al. 的论文聚焦于 model zoo 的 training recipe 和 architecture comparison，
      convergence 仅作为 qualitative observation 出现（一句话提及）。他们不计算 cross-arch std trajectories，
      不做 per-example analysis，不分析 scale-dependent convergence completeness，不做 attention weight
      characterization。我们的 4-point differentiation 是清晰的。但 Reviewer Concern A 仍需通过
      Related Work positioning 来 mitigate——framing 为 "community analysis enabled by public infrastructure"。
    tables:
      - name: "Table: Contribution differentiation vs Wang et al."
        columns: ["Analysis Dimension", "Wang et al.", "Ours"]
        rows:
          - ["Cross-arch std trajectory", "Not computed", "ρ=-1.0, 79% reduction, permutation p=0.017"]
          - ["Per-example analysis", "Not performed", "Jaccard<0.10, KW p=0.0005 (cross-arch)"]
          - ["Scale-dependent convergence", "Not characterized", "Binary contrast: 1.3B complete, 340M partial rebound"]
          - ["Attention characterization", "Not performed", "Descriptive patterns, cosine sim=0.35"]
    figures_description: []
    analysis: >
      Differentiation 清晰且 defensible。关键在于 framing：不是 "Wang et al. missed this"
      而是 "their public infrastructure enables this analysis, which we contribute."

  - name: "Convergence-divergence bridge analysis"
    plan_id: "exp-010"
    description: "绘制 aggregate convergence 与 per-example divergence 随 attention ratio 的 co-evolution"
    expected_results:
      lambada_attention_ratios: [0, 3, 6, 12, 24]
      cross_arch_std_trajectory: [0.024, 0.018, 0.012, 0.008, 0.005]
      mean_pairwise_jaccard_trajectory: [null, 0.09, 0.08, 0.07, 0.06]
      net_effect_asymmetry_trajectory: [null, 0.15, 0.22, 0.28, 0.35]
      convergence_divergence_correlation_rho: -0.95
      convergence_divergence_correlation_p: 0.05
      co_evolution_confirmed: true
    result_rationale: >
      Median 档下，convergence 和 per-example divergence 的 co-evolution 关系成立但统计边缘性。
      随着 attention ratio 增加：(1) aggregate std 单调下降（convergence 增强），
      (2) pairwise Jaccard 轻微下降（per-example overlap 减少，divergence 增强），
      (3) net effect asymmetry 增加（每种架构的 "helped bias" 越来越不同）。
      这三个轨迹在 attention ratio 维度上高度相关（ρ≈-0.95），但 n=4 datapoints（h0 无 attention，
      无 per-example divergence metric），p=0.05 只是 borderline。
      核心 insight：更多 attention → aggregate 更 similar，但 per-example mechanism 更 different。
      这是 underspecification 的具体量化——"the HOW diverges while the WHAT converges"。
    tables:
      - name: "Table: Convergence-divergence co-evolution (LAMBADA, 1.3B)"
        columns: ["Attn Ratio", "Cross-Arch Std", "Mean Jaccard", "Effect Asymmetry", "N Helped (GDN/RetNet/HGRN2)"]
        rows:
          - ["h0 (pure)", 0.024, "—", "—", "—/—/—"]
          - ["h3", 0.018, 0.09, 0.15, "420/380/490"]
          - ["h6", 0.012, 0.08, 0.22, "445/410/520"]
          - ["h12", 0.008, 0.07, 0.28, "460/425/540"]
          - ["h24", 0.005, 0.06, 0.35, "470/430/555"]
    figures_description:
      - "Fig (CORE PAPER FIGURE): Dual-axis plot. Left Y = cross-arch std (decreasing), Right Y = effect asymmetry (increasing), X = attention ratio. Two curves crossing — the visual 'scissors' of convergence-divergence co-evolution."
      - "Fig: Jaccard heatmaps at each attention ratio, showing per-example overlap decreasing as attention increases."
    analysis: >
      这是论文的 signature visualization——一张图讲述整个故事。Aggregate convergence（左轴下降）和
      per-example divergence（右轴上升）的 "scissors" pattern 直观地传达了 underspecification message。
      统计上 borderline (p=0.05)，paper 用 "co-evolve" 而非 "cause" 的语言。
      在 median 档，这张图足以支撑 Findings 论文的核心叙事。

  - name: "Additional high-retrieval benchmarks"
    plan_id: "exp-011"
    description: "在 StoryCloze/BoolQ/COPA 上运行 1.3B 模型，寻找 second convergence anchor"
    expected_results:
      benchmarks_evaluated: ["StoryCloze", "BoolQ", "COPA"]
      StoryCloze:
        rho: -0.7
        exact_p_two_tailed: 0.117
        std_trajectory: [0.031, 0.025, 0.020, 0.018, 0.015]
        std_reduction_pct: 52
        direction: "consistent with LAMBADA"
        significant: false
        suggestive: true
      BoolQ:
        rho: -0.8
        exact_p_two_tailed: 0.083
        std_trajectory: [0.028, 0.024, 0.018, 0.014, 0.010]
        std_reduction_pct: 64
        direction: "consistent with LAMBADA"
        significant: false
        suggestive: true
      COPA:
        rho: -0.3
        exact_p_two_tailed: 0.550
        std_trajectory: [0.045, 0.042, 0.044, 0.040, 0.038]
        std_reduction_pct: 16
        direction: "weak, inconsistent"
        significant: false
        suggestive: false
      best_new_benchmark: "BoolQ"
      best_new_rho: -0.8
      best_new_p: 0.083
      updated_bh_fdr:
        LAMBADA_adj_p: 0.075
        BoolQ_adj_p: 0.375
        StoryCloze_adj_p: 0.375
        note: "BH-FDR with 9 benchmarks: LAMBADA adj-p improves from 0.100 to 0.075 but still >0.05; BoolQ does not survive"
      n_benchmarks_bh_fdr_significant: 1
      n_suggestive_p_below_0_15: 3
      gpu_hours_actual: 7
    result_rationale: >
      Median 档核心假设：最佳新 benchmark (BoolQ) ρ≈-0.8, p≈0.083（suggestive, not significant）。
      BoolQ 作为 passage-based yes/no task，其核心操作是从给定 passage 中 retrieve 关键信息来判断命题真假，
      与 LAMBADA 的 context retrieval 有结构相似性。因此 attention 的 equalizer 效应方向一致。
      但 BoolQ 的 answer space 是 binary（yes/no），cross-architecture variance 的 baseline 本来就低，
      加上 n=5 attention ratios 的 power limitation，p 值只能达到 suggestive 水平。
      StoryCloze (ρ=-0.7, p=0.117) 也 suggestive——context completion task 的 retrieval 成分支持
      convergence 方向，但效应弱于 LAMBADA。COPA (ρ=-0.3) 虽名为 causal reasoning from narratives，
      实际 sample 太短（1-2 sentences），attention 的增量价值小且架构间差异不大。
      BH-FDR 在 9 benchmarks 下将 LAMBADA adj-p 从 0.100 改善到 0.075——方向好但仍 >0.05，
      所以 formal significance 仍然只有 LAMBADA（且仅在 uncorrected 下）。
      但 3 个 benchmarks (LAMBADA + BoolQ + StoryCloze) 方向一致 + GDN-excluded ARC-Easy (ρ=-0.9, p=0.083)
      构成 converging evidence pattern。Paper 的论证从 "single significant result" 转为
      "consistent directional pattern across retrieval-heavy tasks"。
    tables:
      - name: "Table: Extended benchmark convergence analysis (1.3B)"
        columns: ["Benchmark", "Task Type", "ρ", "Exact p (2-tail)", "Std Reduction %", "Suggestive (p<0.15)?"]
        rows:
          - ["LAMBADA", "last-word retrieval", -1.0, 0.017, "79%", "Yes (significant)"]
          - ["BoolQ", "passage yes/no", -0.8, 0.083, "64%", "Yes"]
          - ["StoryCloze", "context completion", -0.7, 0.117, "52%", "Yes"]
          - ["ARC-Easy*", "factual QA (GDN-excl)", -0.9, 0.083, "—", "Yes"]
          - ["COPA", "causal reasoning", -0.3, 0.550, "16%", "No"]
          - ["HellaSwag", "commonsense reasoning", 0.3, 0.742, "—", "No"]
          - ["ARC-Challenge", "multi-step reasoning", 0.6, 0.883, "—", "No"]
          - ["Winogrande", "coreference reasoning", 0.1, 0.950, "—", "No"]
          - ["MMLU†", "knowledge QA", "—", "—", "—", "Excluded (GDN artifact)"]
      - name: "Table: Updated BH-FDR correction (9 benchmarks)"
        columns: ["Rank", "Benchmark", "Raw p", "BH threshold", "BH adj-p", "Significant?"]
        rows:
          - [1, "LAMBADA", 0.017, 0.006, 0.075, "No (improved from 0.100)"]
          - [2, "BoolQ", 0.083, 0.011, 0.375, "No"]
          - [3, "ARC-Easy", 0.117, 0.017, 0.375, "No"]
          - [4, "StoryCloze", 0.117, 0.022, 0.375, "No"]
          - [5, "ARC-Challenge", 0.350, 0.028, 0.630, "No"]
          - [6, "COPA", 0.550, 0.033, 0.825, "No"]
          - [7, "HellaSwag", 0.683, 0.039, 0.878, "No"]
          - [8, "Winogrande", 0.950, 0.044, 0.950, "No"]
          - [9, "MMLU", "excl", "—", "—", "Excluded"]
    figures_description:
      - "Fig: Forest plot of convergence ρ across all benchmarks, ordered by retrieval demand. Clear gradient: high-retrieval tasks cluster at negative ρ, reasoning tasks at zero/positive."
      - "Fig: Std reduction trajectories for LAMBADA + BoolQ + StoryCloze (converging) vs HellaSwag + ARC-C + COPA (flat/diverging), showing task-type dichotomy."
    analysis: >
      Exp-011 在 median 档下不产生 second significant anchor（BH-FDR 仍仅 LAMBADA 在 uncorrected 下显著），
      但产生有价值的 converging evidence pattern。Paper 的 statistical argument 变为：
      "While no single additional benchmark reaches significance after correction, the consistent
      negative direction across retrieval-heavy tasks (LAMBADA ρ=-1.0, BoolQ ρ=-0.8, StoryCloze ρ=-0.7,
      GDN-excluded ARC-Easy ρ=-0.9) versus null/positive results on reasoning tasks suggests the
      convergence effect is systematically related to task type rather than a LAMBADA-specific artifact."
      这是 honest framing——不 overclaim significance，但通过 direction consistency + task taxonomy
      构建 reasonable evidence。对 EMNLP Findings 足够，但 Main 困难。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41b7e675-9c4c-45c1-a69c-45a0c838c6dc",
  "isSidechain": false,
  "requestId": "req_011CbC7cRCzc94SraA2Fz5Qd",
  "type": "assistant",
  "uuid": "a523410d-262b-4988-b403-562d6b71adb9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5YWUUNWQPptZr28o8hmBP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13392,
      "cache_read_input_tokens": 11841,
      "output_tokens": 13378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13378,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13392
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：exp-011 产出 suggestive 但非显著的第二 benchmark（p=0.05-0.15）；BH-FDR 仅保留 LAMBADA；exp-004 有描述性 attention 差异但相关偏弱；exp-005 无额外架构或结果 mixed。需要调整 claim 强度，但 task-specif…",
  "leafUuid": "a523410d-262b-4988-b403-562d6b71adb9",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Entrainment gated fine-tuning: median-tier findings experiment plan",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：exp-011 产出 suggestive 但非显著的第二 benchmark（p=0.05-0.15）；BH-FDR 仅保留 LAMBADA；exp-004 有描述性 attention 差异但相关偏弱；exp-005 无额外架构或结果 mixed。需要调整 claim 强度，但 task-specif…",
  "leafUuid": "a523410d-262b-4988-b403-562d6b71adb9",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Entrainment gated fine-tuning: median-tier findings experiment plan",
  "sessionId": "0e7d084f-631d-4c53-ad97-0f6a0bae2ba4"
}
```

---
