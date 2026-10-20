# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：exp-011 全部新 benchmark 无 convergence 信号（ρ > -0.5 或 p > 0.3）；LAMBADA 是孤立的单点发现

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/2adf5397-5a56-488d-a8d9-974d0752b4cc.jsonl`
- **Structured JSON:** [`785e5e006fcc0e9da6c9.json`](../../sessions/78/785e5e006fcc0e9da6c9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-19T14:54:59.337Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-19T14:54:59.337Z",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：exp-011 全部新 benchmark 无 convergence 信号（ρ > -0.5 或 p > 0.3）；LAMBADA 是孤立的单点发现且不 survive 任何多重校正；exp-004 attention pattern 无解释力（correlation < 0.15）；exp-005 无进展。核心 convergence claim 站不住脚，需要 reframe 为 per-example divergence 分析论文。\n核心假设：['exp-011 所有新 benchmark ρ > -0.5 且 p > 0.25（无 convergence 信号）', 'LAMBADA convergence 被孤立为单一 benchmark 效应，无法泛化', 'exp-004 attention-effect correlation < 0.15（attention 分析无法解释 per-example 差异）', 'GDN-excluded 后 LAMBADA 本身也弱化（ρ=-0.7, p=0.23）——convergence 部分依赖 GDN confound', 'exp-005 无额外架构', 'exp-007 340M rebound 无清晰解释（噪声不可排除）']\n关键指标范围：{'exp011_best_new_rho': [-0.5, 0.0], 'exp011_best_new_p': [0.25, 1.0], 'n_benchmarks_BH_FDR_significant': [0, 1], 'exp004_attn_effect_correlation': [0.0, 0.15], 'lambada_cross_arch_std_reduction_pct': [75, 85], 'per_example_jaccard_range': [0.05, 0.12], 'n_architectures_total': [3, 3], 'gdn_excluded_lambada_rho': [-0.7, -0.7]}\n叙事方向：放弃 convergence 作为主 claim。Reframe 为：'Per-example behavioral divergence in hybrid recurrent architectures — attention induces architecture-specific sample specialization'。核心贡献变为 Claim 3 的 per-example 分析：(a) Jaccard < 0.10 的架构特异性（strongest finding, 不依赖 convergence），(b) cross-arch Kruskal-Wallis p=0.0005 证明差异是结构化的非随机的，(c) surface features + perplexity 均无法解释（rules out trivial explanations）。LAMBADA convergence 降级为 'one-task observation' 放进 discussion，不作为 claim。Claim 2 (scale) 完全降级为 supplementary observation。新的 story spine：practitioners 选择 hybrid architecture 时需要知道 attention 对不同架构的 per-example 影响是不同的 → practical implication for ensemble design / architecture selection。仍冲 Findings——per-example characterization + underspecification framing 对 EMNLP 的 analysis track 有独立价值，但需要 20+ references 的 related work 来证明 question 的 motivated-ness。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: entrainment_gated_ft\nvenue: emnlp-2026\nfocus: This is a pivot from a failed entrainment hypothesis to an equalizer effect discovery. Key concerns: (1) only LAMBADA shows clear convergence — is the finding too narrow? (2) n=3 architectures — sufficient? (3) differentiation from Wang et al. who have the model zoo and noted qualitative convergence. (4) no 7B scale yet — two scales enough? Assess whether the equalizer paradox (aggregate convergence + per-example divergence) is novel and interesting enough for EMNLP Findings/Main.\n\n## paper_framing.md\n\n# Paper Framing — entrainment_gated_ft\n\n> Revised 2026-05-19 after Dream review (best case = 2.5/5). Major reframing: drop \"paradox\" narrative, engage related work, add retrieval benchmarks.\n\n## Target Venue\n- Primary: EMNLP 2026 Findings (via ARR)\n- Stretch: EMNLP 2026 Main\n- Deadline: ARR June 2026 cycle (submission ~June 15)\n\n## Paper Type\nEmpirical analysis paper — quantifying a known phenomenon (per-example divergence under aggregate convergence) in a specific important domain (hybrid recurrent architectures)\n\n## Core Claims (3 条)\n\n### Claim 1: Task-Dependent Convergence\nAdding attention layers to different linear recurrent architectures (GatedDeltaNet, RetNet, HGRN2) induces aggregate performance convergence whose strength varies with task type. Convergence is strongest on LAMBADA (ρ=-1.0, p=0.017 two-tailed, cross-arch std drops 79%), suggestive on ARC-Easy (ρ=-0.7, p=0.233, underpowered at n=5), and absent on reasoning-heavy tasks. **Critical need**: a second high-retrieval benchmark showing significant convergence to survive multi-comparison correction.\n\n### Claim 2: Scale-Dependent Convergence\nThe convergence effect requires sufficient model capacity: monotonically complete at 1.3B (ρ=-1.0, p=0.017 two-tailed) but only partial at 340M with a non-monotonic rebound. Only two scale points (Wang et al. cap at 1.3B). Frame as binary contrast, not extrapolatable trend.\n\n### Claim 3: Per-Example Divergence Under Aggregate Convergence\nDespite aggregate convergence, attention acts on nearly non-overlapping sample subsets per architecture (pairwise Jaccard < 0.10). This is an instance of the well-documented underspecification phenomenon (D'Amour et al. 2022) applied to hybrid architectures. Our contribution is **quantifying** it in this specific context, NOT claiming to discover it. Surface features AND baseline model perplexity do not differentiate helped/hurt samples within an architecture — the effect is opaque to standard features. However, cross-architecture comparison reveals systematic differences in baseline difficulty profiles of affected samples (Kruskal-Wallis p=0.0005 for hurt samples), confirming the architecture-specificity is structured, not random noise.\n\n## Story Spine\n\n### Problem\nHybrid architectures mixing linear recurrence with full attention are becoming standard. While Wang et al. (2025) provide an extensive model zoo, the community lacks quantitative understanding of how attention affects cross-architecture behavioral diversity at the per-example level.\n\n### Related Work Positioning (CRITICAL — Dream W2)\nThe observation that models with similar aggregate performance differ per-example is well-established:\n- **Ensemble diversity**: Krogh & Vedelsby (1995), Kuncheva & Whitaker (2003) — diverse ensemble members err on different examples by construction\n- **Underspecification**: D'Amour et al. (2022) — equivalent aggregate performance masks prediction-level differences\n- **Dataset cartography**: Swayamdipta et al. (2020) — per-example difficulty varies across models\n- **Simpson's paradox / ecological fallacy**: Aggregate-vs-disaggregate discrepancy is a textbook phenomenon\n\nOur contribution is NOT discovering this phenomenon. It IS quantifying how it manifests specifically when attention is added to linear recurrent models, and characterizing its task-dependency and scale-dependency. This is valuable because hybrid architectures are a design choice practitioners make — understanding per-example implications informs that choice.\n\n### Our Framing\nWe provide the first systematic per-example analysis of attention's equalizing effect in hybrid recurrent architectures. Using Wang et al.'s public model zoo (72 models), we quantify (a) task-dependent convergence strength, (b) scale-dependent convergence completeness, and (c) architecture-specific per-example divergence patterns. Our contribution is analytical depth on public infrastructure, not new methods or models.\n\n### Headline Result Template\n\"At 1.3B scale, adding attention to hybrid recurrent models reduces cross-architecture variance by 79% on LAMBADA, yet per-example analysis reveals nearly non-overlapping affected sample subsets (Jaccard < 0.10) — a manifestation of underspecification that has practical implications for architecture selection.\"\n\n## Dream Review Findings (D006) — Must Address\n\n### W1: Single-benchmark significance [MAJOR, blocking]\nAfter Bonferroni (6 benchmarks, α=0.0083), LAMBADA p=0.017 (two-tailed) does NOT survive. Need: (a) FDR correction (Benjamini-Hochberg) as primary reporting, (b) additional high-retrieval benchmarks for a second significant anchor. Candidates: StoryCloze, BoolQ, COPA, closed-book QA tasks available in lm-eval.\n\n### W2: Missing related work [MAJOR, blocking for submission]\nNeed 20+ references engaging ensemble diversity, underspecification, dataset cartography, attention interpretability, hybrid architectures (Jamba, RWKV-6, RecurrentGemma). Paper Agent handles this during writing.\n\n### W3: Mechanistic overclaiming [MAJOR, partially addressed]\nAlready reworded Claim 3 from \"Mechanism\" to \"Effects\". Must NOT use \"mechanistic analysis\" in paper — use \"characterization\" or \"decomposition\" instead. Attention weight analysis (exp-004) is descriptive, not causal. Frame honestly.\n\n### W4: Incremental over Wang et al. [MAJOR]\nMitigate by: (a) engaging related work to show the QUESTION we ask is independently motivated by ensemble/underspecification literature, (b) framing contribution as analytical toolkit + quantitative characterization, not re-analysis. (c) Per-example analysis is genuinely novel for this model family.\n\n## Venue Fit Risks\n(unchanged from previous version, see git history)\n\n## Anticipated Reviewer Concerns\n\n### Concern A: \"This is just a re-analysis of Wang et al.'s models\"\nResponse: Yes, and that's the point — public infrastructure enables community analysis. Our per-example decomposition, task-dependency characterization, and scale-dependency analysis are not in Wang et al. The contribution is analytical, like meta-analyses in medicine.\nRequired: Strong Related Work positioning; frame as \"community analysis\" paper.\n\n### Concern B: \"Only one task shows the effect\" + Bonferroni failure\n**Statistical strategy** (from exp-008, verified by Reviewer with independent reproduction):\n1. **Lead with percentile CI (valid-only)**: BCa degenerates at ρ=-1.0 boundary (z0=-3.86); fall back to percentile CI on valid bootstrap resamples (8875/10000; 11.25% degenerate from n=3 same-architecture redraws). Valid-only percentile CI = **[-1.0, -0.7]**, 100% of valid resamples have ρ<0. Full percentile CI (degenerate-as-zero) = [-1.0, 0.0] touches zero. Paper leads with valid-only CI; BCa degeneracy + degenerate-sample treatment in appendix.\n2. **Report exact permutation p**: LAMBADA p=0.017 (two-tailed, 2/120 permutations). Honest and transparent.\n3. **Bonferroni in supplementary**: adj-p=0.100 (two-tailed). Report honestly as \"does not survive Bonferroni.\" BH-FDR also gives 0.100 (no additional benefit with only 1 small p-value). If exp-011 produces a second significant benchmark, BH-FDR becomes more favorable than Bonferroni.\n4. **GDN-excluded sensitivity**: Excluding GDN (D004 confound): LAMBADA ρ drops to -0.7 (p=0.233); ARC-Easy ρ **improves** from -0.7 to -0.9 (p=0.083, suggestive — D004 noise removed); **⚠️ MMLU ρ FLIPS from -0.7 to +0.6** — MMLU apparent convergence was entirely GDN-driven and MUST NOT appear as convergence evidence anywhere in the paper (D007). Report both full and GDN-excluded analyses. The ARC-Easy improvement after confound removal is itself informative, especially in exp-011 context.\n5. **exp-011**: Additional retrieval benchmarks (StoryCloze/BoolQ/COPA) for a potential second significant anchor. CRITICAL for acceptance — with exp-011 data, BH-FDR could diverge favorably from Bonferroni.\n6. **Effect sizes**: Cohen's d CI crosses zero; omega² near zero. Do NOT lead with effect sizes — lead with BCa CI and convergence magnitude (std 0.024→0.005, 79% reduction).\n\nRequired experiments: exp-011 (additional retrieval benchmarks), exp-008 (robustness with corrected p-values), exp-002 (per-example validation).\n\n### Concern C: \"The per-example divergence is a known phenomenon\"\nResponse: Acknowledge explicitly. Our contribution is quantification in hybrid architectures, not discovery of the phenomenon. Cite ensemble diversity + underspecification.\nRequired: Related Work section (Paper Agent).\n\n### Concern D: \"n=3 architectures is too few\"\nResponse: 3 architectures × 5 ratios × 2 scales = 30 models. Per-example analysis provides 5153 data points per comparison. Check for additional architectures (exp-005).\n\n### Concern E: \"Two scales don't establish a trend\"\nResponse: Binary contrast, not trend. 7B unavailable. Frame as \"scale is a necessary condition.\" exp-007 for 340M rebound mechanism.\n\n### Concern F: \"No causal mechanism\" (NEW from Dream)\nResponse: We do NOT claim causal mechanism. We characterize and describe. Attention weight analysis (exp-004) is descriptive. Interventional experiments (head swaps, ablations) are acknowledged as future work. Honest framing prevents overclaiming.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  title: Task-specificity characterization of equalizer effect\n  description: 'Compute cross-architecture variance (std) at each attention ratio\n    for all 6 benchmarks. Known: only LAMBADA shows significant convergence (p<0.05).\n    Goal: build principled task taxonomy (retrieval-dependent vs reasoning-dependent)\n    explaining WHY convergence is task-specific. LAMBADA = last-word retrieval from\n    context; HellaSwag/ARC = multi-step reasoning. Show the dichotomy is a feature\n    (task-type modulation), not a limitation.\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 0\n  deps: []\n  data_source: existing summary_all_1.3b.csv + 340M results + cross_scale_convergence\n    output\n  pass_fail: Clear task-type dichotomy with principled taxonomy; convergence correlates\n    with retrieval demand\n  reviewer_risk: 'Risk A — reframed per Reviewer warning: single-task convergence\n    → task-specificity as positive finding'\n  status: planned\n- id: exp-002\n  claim: 1\n  title: Multi-benchmark per-example analysis (task-specificity validation)\n  description: 'Re-run lm-eval on 1.3B models with --log_samples for HellaSwag, ARC-easy,\n    ARC-challenge. Two goals: (a) confirm task-specificity — per-example convergence\n    absent on reasoning tasks, (b) characterize HOW attention affects per-example\n    behavior on non-converging tasks (random noise vs systematic but architecture-specific).\n    Strengthens Claim 1 regardless of outcome.\n\n    '\n  priority: P0\n  type: experiment\n  gpu_budget_hours: 20\n  deps:\n  - exp-001\n  pass_fail: Per-example data collected for ≥3 benchmarks; task-specificity of per-example\n    mechanism confirmed or refuted\n  reviewer_risk: 'Risk B — outcome determines Claim 1 scope: cross-task vs retrieval-specific\n    equalizer'\n  note: 'Budget revised to 20h per Reviewer data audit: need --log_samples for 10×340M\n    (RetNet+HGRN2) + 3×1.3B (GDN h3-1/h6-1/h24-1). Uses freed exp-006 budget.'\n  status: planned\n- id: exp-006\n  claim: 2\n  title: 7B model evaluation — CANCELLED (unavailable)\n  description: 'Wang et al. only have 340M + 1.3B (72 models total). Paper Limitations\n    explicitly excludes 10B+. No 7B models exist. Budget reallocated to exp-002/004/005.\n\n    '\n  priority: cancelled\n  type: experiment\n  gpu_budget_hours: 0\n  deps: []\n  pass_fail: N/A — 7B unavailable, confirmed 2026-05-19\n  status: planned\n- id: exp-007\n  claim: 2\n  title: '340M rebound mechanism analysis (upgraded: compensate 7B absence)'\n  description: 'Deep analysis of 340M non-monotonic rebound at attn=8. Per-example\n    comparison with 1.3B at same attention ratio to identify which samples diverge.\n    Characterize rebound samples. With 7B unavailable, this becomes the primary vehicle\n    for Claim 2 depth — show the binary contrast (340M partial vs 1.3B complete) has\n    mechanistic explanation, not just correlation with scale. Analyze training token\n    count (20B vs 100B) as confound vs scale.\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 2\n  deps:\n  - exp-002\n  data_source: existing 340M results + new 1.3B per-example data\n  pass_fail: Rebound mechanism identified with principled explanation; 340M vs 1.3B\n    contrast characterized beyond aggregate metrics\n  note: Upgraded from P1 to P0 after 7B cancellation. May need 340M per-example rerun\n    (2h GPU).\n  status: planned\n- id: exp-003\n  claim: 3\n  title: Helped/hurt sample characterization\n  description: 'For each architecture''s helped/hurt samples on LAMBADA, compute:\n    (a) target token frequency (unigram rank in training data proxy), (b) context\n    length (token count), (c) last-sentence complexity (perplexity under baseline),\n    (d) topic/domain distribution. Test whether architecture-specific sample subsets\n    differ on these features.\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 1\n  deps: []\n  data_source: existing lambada per-example logprob data\n  pass_fail: ≥1 feature significantly differentiates helped vs hurt samples (p<0.01),\n    AND features differ across architectures\n  status_note: 'Phase 1 (surface features) DONE: all non-significant within-arch (p>0.2).\n    Phase 2 (perplexity) DONE: within-arch perplexity also non-significant (r_rb≈-0.04,\n    p>0.2). PASS on second criterion: cross-arch KW significant (hurt p=0.0005, helped\n    p=0.020). Different archs help/hurt samples with systematically different baseline\n    difficulty profiles. Both negative within-arch results are informative (rules\n    out trivial explanations). Cross-arch finding strengthens Claim 3 (architecture-specificity\n    is structured, not random).\n\n    '\n  status: planned\n- id: exp-004\n  claim: 3\n  title: Attention weight extraction and visualization\n  description: 'Extract attention weight patterns from hybrid models (h3-1 config)\n    for all 3 architectures. Analyze: (a) which positions attention focuses on, (b)\n    whether attention patterns correlate with helped/hurt sample identity, (c) cross-architecture\n    attention pattern similarity.\n\n    '\n  priority: P0\n  type: experiment\n  gpu_budget_hours: 4\n  deps:\n  - exp-003\n  pass_fail: Attention pattern differences documented; correlation with per-example\n    effects > 0.3\n  note: 'Upgraded P1→P0: mechanistic evidence is critical for Claim 3 and Reviewer\n    Concern C'\n  status: planned\n- id: exp-005\n  claim: 1\n  title: Architecture expansion check\n  description: 'Search Wang et al. model zoo and other sources for additional hybrid\n    architectures (Mamba/Mamba2 hybrids, RWKV hybrids, etc.). If found, evaluate on\n    LAMBADA to test whether convergence generalizes beyond GDN/RetNet/HGRN2.\n\n    '\n  priority: P1\n  type: experiment\n  gpu_budget_hours: 6\n  deps: []\n  pass_fail: ≥1 additional architecture evaluated and convergence pattern confirmed/denied\n  status: planned\n- id: exp-008\n  claim: 1\n  title: Statistical robustness framework\n  description: 'Implement bootstrap CIs for convergence metrics. Multi-comparison\n    correction (Bonferroni/FDR) across benchmarks. Sensitivity analysis: does conclusion\n    hold if GDN (with D004 confound) is excluded? Report effect sizes (Cohen''s d\n    / η²).\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  pass_fail: All core claims survive with GDN excluded; bootstrap 95% CIs don't cross\n    zero\n  status: planned\n- id: exp-009\n  claim: 1\n  title: Wang et al. explicit differentiation\n  description: 'Formal side-by-side comparison: what Wang et al. report vs our analysis.\n    Extract their exact convergence-related statements. Quantify the increment: (a)\n    they don''t compute cross-arch std trajectories, (b) no per-example analysis,\n    (c) no scale-dependent convergence characterization, (d) no mechanistic analysis.\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 0\n  deps: []\n  data_source: Wang et al. arXiv 2507.06457\n  pass_fail: Clear 4-point differentiation documented\n  status: planned\n- id: exp-010\n  claim: 3\n  title: Convergence-divergence bridge analysis\n  description: 'For LAMBADA, plot aggregate convergence curve alongside per-example\n    divergence metrics (Jaccard, net effect asymmetry) as function of attention ratio.\n    Show that convergence and divergence co-evolve—more attention = more aggregate\n    convergence BUT also more architecture-specific per-example effects. Core visualization\n    for Claim 3 (underspecification in hybrid architectures).\n\n    '\n  priority: P0\n  type: analysis\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-003\n  pass_fail: Convergence-divergence co-evolution demonstrated with significant correlation\n  status: planned\n- id: exp-011\n  claim: 1\n  title: Additional high-retrieval benchmarks (Dream W1 response)\n  description: 'Dream review: LAMBADA alone does not survive Bonferroni (p=0.017 >\n    α=0.0083). Need a second significant anchor point on a high-retrieval task. Run\n    1.3B models on additional retrieval-heavy benchmarks available in lm-eval: (a)\n    StoryCloze (context completion, structurally similar to LAMBADA), (b) BoolQ (passage-based\n    yes/no, context retrieval), (c) COPA (causal reasoning from short narratives).\n    Compute cross-arch std at each attention ratio for each benchmark. Test for convergence\n    (Spearman + exact permutation, two-tailed). If ANY shows significant convergence\n    → second anchor established, W1 substantially mitigated.\n\n    '\n  priority: P0\n  type: experiment\n  gpu_budget_hours: 8\n  deps: []\n  pass_fail: ≥1 additional benchmark shows significant convergence (p<0.05 two-tailed)\n  note: CRITICAL for Findings acceptance. Dream best case = 2.5 without this. Added\n    post-D006.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: hgrn2_eval_1_3b_all\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: hgrn2_eval_h3_1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval_340m_retnet_hgrn2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp-001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    LAMBADA:\n      rho: -1\n      p: 0.008\n      significant: true\n      taxonomy: retrieval-dependent\n    HellaSwag:\n      rho: 0.3\n      p: 0.742\n      significant: false\n      taxonomy: reasoning-dependent\n    ARC-C:\n      rho: 0.6\n      p: 0.883\n      significant: false\n      taxonomy: reasoning-dependent\n    Winogrande:\n      rho: 0.1\n      p: 0.608\n      significant: false\n      taxonomy: reasoning-dependent\n    ARC-Easy:\n      rho: -0.7\n      p: 0.117\n      significant: false\n      taxonomy: mixed\n    MMLU:\n      rho: -0.7\n      p: 0.117\n      significant: false\n      taxonomy: mixed\n    significant_count: 1/6\n    summary: Only LAMBADA shows significant convergence (rho=-1.0, p=0.008). Reasoning\n      tasks show no convergence. Mixed tasks suggestive but underpowered (n=5).\n- exp_id: exp-009\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: exp-003\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    GDN:\n      helped: 462\n      hurt: 615\n      net: -153\n      surface_features_significant: false\n    HGRN2:\n      helped: 548\n      hurt: 395\n      net: 153\n      surface_features_significant: false\n    RetNet:\n      helped: 426\n      hurt: 495\n      net: -69\n      context_length_p: 0.012\n      context_length_r: -0.096\n      unique_tokens_p: 0.009\n      unique_tokens_r: -0.099\n    cross_arch_difference: not_significant\n    pass_fail: FAIL — RetNet context_unique_tokens p=0.009 passes criterion 1 for\n      one arch only; criterion 2 (cross-arch difference) fails\n    summary: Surface features do not explain helped/hurt identity. Rules out trivial\n      explanations (frequency, length, diversity). RetNet shows weak context-length\n      signal (p=0.012, r=-0.096).\n- exp_id: exp-003-p2\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    GDN:\n      U: 148410\n      p: 0.209189\n      r_rb: -0.0447\n      helped_mean: 3.3695\n      hurt_mean: 3.3382\n    RetNet:\n      U: 107210\n      p: 0.659319\n      r_rb: -0.0168\n      helped_mean: 3.4432\n      hurt_mean: 3.4207\n    HGRN2:\n      U: 112999\n      p: 0.247856\n      r_rb: -0.0441\n      helped_mean: 3.3775\n      hurt_mean: 3.3538\n    cross_arch_helped_KW_p: 0.020136\n    cross_arch_hurt_KW_p: 0.000498\n- exp_id: exp-011\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-008\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    LAMBADA:\n      rho: -1\n      raw_p: 0.0167\n      bonferroni_adj_p: 0.1\n      bh_fdr_adj_p: 0.1\n    HellaSwag:\n      rho: 0.3\n      raw_p: 0.6833\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.82\n    WinoGrande:\n      rho: 0.1\n      raw_p: 0.95\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.95\n    ARC-Easy:\n      rho: -0.7\n      raw_p: 0.2333\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.4667\n    ARC-Challenge:\n      rho: 0.6\n      raw_p: 0.35\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.525\n    MMLU:\n      rho: -0.7\n      raw_p: 0.2333\n      bonferroni_adj_p: 1\n      bh_fdr_adj_p: 0.4667\n    method: exact_permutation_test_two_tailed\n    n_permutations: 120\n    bug_fixed: scipy.stats.spearmanr asymptotic p replaced with exact permutation\n    bootstrap_ci:\n      benchmark: LAMBADA\n      method: architecture_resampling_percentile\n      ci_lower: -1\n      ci_upper: -0.7\n      crosses_zero: false\n      n_bootstrap: 10000\n      n_valid: 8875\n      seed: 42\n      p_rho_negative: 1\n      p_rho_positive: 0\n      bca_note: BCa degenerate at rho=-1.0 boundary; percentile CI used\n    gdn_excluded:\n      LAMBADA:\n        rho: -0.7\n        exact_p: 0.2333\n        direction: WEAKER\n      HellaSwag:\n        rho: 0.5\n        exact_p: 0.45\n        direction: STRONGER\n      WinoGrande:\n        rho: 0.3\n        exact_p: 0.6833\n        direction: STRONGER\n      ARC-Easy:\n        rho: -0.9\n        exact_p: 0.0833\n        direction: STRONGER\n      ARC-Challenge:\n        rho: -0.2\n        exact_p: 0.7833\n        direction: WEAKER\n      MMLU:\n        rho: 0.6\n        exact_p: 0.35\n        direction: WEAKER\n      note: ARC-Easy rho improves from -0.7 to -0.9 (p=0.0833) without GDN confound\n        — suggestive second anchor\n- exp_id: exp-003-p2v2\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-19T14:54:59.341Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-19T14:54:59.341Z",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-19T14:54:59.360Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：exp-011 全部新 benchmark 无 convergence 信号（ρ > -0.5 或 p > 0.3）；LAMBADA 是孤立的单点发现且不 survive 任何多重校正；exp-004 attention pattern 无解释力（correlation < 0.15）；exp-005 无进展。核心 convergence claim 站不住脚，需要 reframe 为 per-example divergence 分析论文。
核心假设：['exp-011 所有新 benchmark ρ > -0.5 且 p > 0.25（无 convergence 信号）', 'LAMBADA convergence 被孤立为单一 benchmark 效应，无法泛化', 'exp-004 attention-effect correlation < 0.15（attention 分析无法解释 per-example 差异）', 'GDN-excluded 后 LAMBADA 本身也弱化（ρ=-0.7, p=0.23）——convergence 部分依赖 GDN confound', 'exp-005 无额外架构', 'exp-007 340M rebound 无清晰解释（噪声不可排除）']
关键指标范围：{'exp011_best_new_rho': [-0.5, 0.0], 'exp011_best_new_p': [0.25, 1.0], 'n_benchmarks_BH_FDR_significant': [0, 1], 'exp004_attn_effect_correlation': [0.0, 0.15], 'lambada_cross_arch_std_reduction_pct': [75, 85], 'per_example_jaccard_range': [0.05, 0.12], 'n_architectures_total': [3, 3], 'gdn_excluded_lambada_rho': [-0.7, -0.7]}
叙事方向：放弃 convergence 作为主 claim。Reframe 为：'Per-example behavioral divergence in hybrid recurrent architectures — attention induces architecture-specific sample specialization'。核心贡献变为 Claim 3 的 per-example 分析：(a) Jaccard < 0.10 的架构特异性（strongest finding, 不依赖 convergence），(b) cross-arch Kruskal-Wallis p=0.0005 证明差异是结构化的非随机的，(c) surface features + perplexity 均无法解释（rules out trivial explanations）。LAMBADA convergence 降级为 'one-task observation' 放进 discussion，不作为 claim。Claim 2 (scale) 完全降级为 supplementary observation。新的 story spine：practitioners 选择 hybrid architecture 时需要知道 attention 对不同架构的 per-example 影响是不同的 → practical implication for ensemble design / architecture selection。仍冲 Findings——per-example characterization + underspecification framing 对 EMNLP 的 analysis track 有独立价值，但需要 20+ references 的 related work 来证明 question 的 motivated-ness。

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
  "promptId": "02367909-3851-43a8-925b-d2c0b692ae33",
  "type": "user",
  "uuid": "89eba50a-e283-4113-8db8-135313fa753c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-19T14:54:59.358Z_

```json
{
  "parentUuid": "89eba50a-e283-4113-8db8-135313fa753c",
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
  "uuid": "6ec105f5-34b9-4ffb-b169-9ff3ca52fb7b",
  "timestamp": "2026-05-19T14:54:59.358Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-19T14:54:59.359Z_

```json
{
  "parentUuid": "6ec105f5-34b9-4ffb-b169-9ff3ca52fb7b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c733ce7e-e00c-4ebd-a4fb-4e3690d3a4fc",
  "timestamp": "2026-05-19T14:54:59.359Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：exp-011 全部新 benchmark 无 convergence 信号（ρ > -0.5 或 p > 0.3）；LAMBADA 是孤立的单点发现且不 survive 任何多重校正；exp-004 attention pattern 无解释力（correlation < 0.15）；exp-005 无进…",
  "leafUuid": "c733ce7e-e00c-4ebd-a4fb-4e3690d3a4fc",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-example divergence in hybrid recurrent architectures",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc"
}
```

---

### Assistant

_source line 8 · 2026-05-19T14:55:18.807Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for the "worst" tier for each planned experiment in their experiment plan. I need to carefully go through each experiment and predict what the worst-case results would look like, given the worst-tier definition provided.

Let me go through the worst tier definition again:

**Worst tier meaning:**
- exp-011: ALL new benchmarks show no convergence signal (ρ > -0.5 or p > 0.3)
- LAMBADA is an isolated single-point finding that doesn't survive any multiple comparison correction
- exp-004: attention patterns have no explanatory power (correlation < 0.15)


- exp-005: no progress on the core convergence claim, which would require pivoting toward a per-example divergence analysis instead

Now I'm looking at the specific metric ranges for the worst-case scenario across these experiments. For exp-011, the best new correlation should fall between -0.5 and 0.0 with p-values ranging from 0.25 to 1.0, and only 0 to 1 benchmarks would survive multiple comparison correction. The attention effect correlation for exp-004 needs to stay below 0.15, while LAMBADA's cross-architecture standard deviation reduction should be between 75-85 percent. I'm also tracking the per-example Jaccard similarity range, which appears to start at 0.05.

The key shift here is abandoning convergence as the main narrative and reframing this as a per-example behavioral divergence paper instead. Claim 3's per-example analysis becomes the core contribution. Looking at my experiment plan, I need to skip the ones already completed and focus on the remaining work: multi-benchmark per-example analysis for exp-002, attention weight extraction for exp-004, architecture expansion for exp-005, and the 340M rebound mechanism analysis for exp-007.

I also need to plan the convergence-divergence bridge analysis in exp-010 and prepare additional high-retrieval benchmarks for exp-011. So I'm generating worst-tier predictions for these six planned experiments to understand what could go wrong and how to mitigate those risks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c733ce7e-e00c-4ebd-a4fb-4e3690d3a4fc",
  "isSidechain": false,
  "requestId": "req_011CbC7vvtgbi5sKB4e18c3J",
  "type": "assistant",
  "uuid": "e645d1aa-c00b-425d-9ac0-71c293946944",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsVXZcNHSJbATSqbiE2uT6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13462,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8498,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13462
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

_source line 9 · 2026-05-19T14:57:50.201Z_

```yaml
tier: worst
narrative_guidance: >
  放弃 convergence 作为主 claim。论文 reframe 为 "Per-example behavioral divergence
  in hybrid recurrent architectures — attention induces architecture-specific sample
  specialization"。LAMBADA convergence 降级为 discussion 中的 single-task observation，
  不作为独立 claim。Claim 2 (scale) 完全移入 supplementary。核心贡献变为 Claim 3：
  (a) Jaccard < 0.10 的架构特异性，(b) cross-arch KW p=0.0005 证明结构化非随机，
  (c) surface features + perplexity 均无法解释。新 story spine：practitioners 选择
  hybrid architecture 时需要知道 attention 对不同架构的 per-example 影响是不同的。
  仍冲 EMNLP Findings，但需要 20+ references 的 related work 支撑 question 的
  motivated-ness。per-example characterization + underspecification framing 对
  analysis track 有独立价值。

imagined_experiments:
  - name: "Multi-benchmark per-example analysis (task-specificity validation)"
    plan_id: "exp-002"
    description: >
      Re-run lm-eval on 1.3B models with --log_samples for HellaSwag, ARC-Easy,
      ARC-Challenge。收集 per-example logprob 数据。在 worst 档下，这些
      reasoning-heavy benchmarks 的 per-example 分析不会产生 convergence 信号，
      但会为 per-example divergence 分析提供对比组。
    expected_results:
      hellaswag_pairwise_jaccard_mean: 0.08
      hellaswag_pairwise_jaccard_range: [0.05, 0.11]
      arc_easy_pairwise_jaccard_mean: 0.09
      arc_easy_pairwise_jaccard_range: [0.06, 0.12]
      arc_challenge_pairwise_jaccard_mean: 0.07
      arc_challenge_pairwise_jaccard_range: [0.04, 0.10]
      hellaswag_cross_arch_std_trend_rho: 0.2
      hellaswag_cross_arch_std_trend_p: 0.75
      arc_easy_cross_arch_std_trend_rho: -0.3
      arc_easy_cross_arch_std_trend_p: 0.55
      arc_challenge_cross_arch_std_trend_rho: 0.4
      arc_challenge_cross_arch_std_trend_p: 0.60
      per_example_convergence_any_task: false
      cross_task_jaccard_comparison_KW_p: 0.12
      n_samples_hellaswag: 10042
      n_samples_arc_easy: 2376
      n_samples_arc_challenge: 1172
    result_rationale: >
      Worst 档下，reasoning-heavy tasks 既无 aggregate convergence 也无 per-example
      convergence。但 Jaccard 值仍然低（0.05-0.12 范围内），说明 per-example divergence
      是跨 benchmark 的普遍现象——这实际上 strengthens reframed Claim 3。不同 benchmark
      的 Jaccard 无显著差异（KW p=0.12），意味着 architecture-specific sample
      specialization 是 task-agnostic 的。cross-arch std 趋势在这些 benchmark 上
      无方向性（rho 在 -0.3 到 0.4 之间震荡），确认 convergence 确实是 LAMBADA-specific
      而非 general。这组数据在 reframed narrative 下反而有用：convergence 是
      task-dependent 的（已知），但 per-example divergence 是 universal 的（新发现）。
    tables:
      - name: "Table: Per-example divergence metrics across benchmarks (1.3B)"
        columns: [benchmark, n_samples, mean_jaccard, jaccard_95ci, helped_overlap_pct, hurt_overlap_pct, cross_arch_std_rho, cross_arch_std_p]
        rows:
          - [LAMBADA, 5153, 0.07, "[0.05, 0.09]", 8.2, 6.9, -1.0, 0.017]
          - [HellaSwag, 10042, 0.08, "[0.06, 0.10]", 9.1, 7.5, 0.2, 0.75]
          - [ARC-Easy, 2376, 0.09, "[0.07, 0.11]", 10.3, 8.8, -0.3, 0.55]
          - [ARC-Challenge, 1172, 0.07, "[0.04, 0.10]", 7.8, 6.2, 0.4, 0.60]
    figures_description:
      - "Heatmap: pairwise Jaccard similarity of helped/hurt sets across 4 benchmarks × 3 architectures。所有 off-diagonal 值 < 0.12，视觉上近乎空白，直观展示 per-example divergence 的普遍性。"
      - "Scatter: aggregate convergence (rho) vs per-example divergence (1 - mean Jaccard)。LAMBADA 在左下角（convergence + divergence），其余 benchmarks 在右下角（no convergence + same divergence），支撑 'divergence is universal, convergence is not' narrative。"
    analysis: >
      Worst 档下 exp-002 的核心价值在于建立对比：convergence 是 task-specific 的
      单点现象，但 per-example divergence 是跨 benchmark 的普遍现象。这组数据直接
      支持 reframed narrative——论文的核心发现是 attention 导致的 architecture-specific
      sample specialization，而非 aggregate convergence。即使 convergence claim 完全
      失败，Jaccard < 0.12 的跨 benchmark 一致性为 Claim 3 提供了多 benchmark 验证。
      不过 cross-task Jaccard 比较的 KW p=0.12 意味着不能 claim divergence 程度有
      task dependency——只能说 divergence 存在且 universal。

  - name: "Attention weight extraction and visualization"
    plan_id: "exp-004"
    description: >
      提取 3 个架构 h3-1 配置的 attention weight patterns，分析 attention pattern
      与 helped/hurt sample identity 的相关性。Worst 档下 correlation < 0.15，
      attention patterns 无法解释 per-example 差异。
    expected_results:
      gdn_attn_effect_correlation: 0.08
      retnet_attn_effect_correlation: 0.11
      hgrn2_attn_effect_correlation: 0.06
      max_attn_effect_correlation: 0.11
      cross_arch_attn_pattern_similarity: 0.35
      attn_entropy_helped_vs_hurt_p_gdn: 0.18
      attn_entropy_helped_vs_hurt_p_retnet: 0.09
      attn_entropy_helped_vs_hurt_p_hgrn2: 0.41
      attn_head_specialization_score: 0.12
      position_bias_correlation_with_effect: 0.05
    result_rationale: >
      Worst 档核心假设是 attention patterns 对 per-example 效应无解释力。Correlation
      < 0.15 的原因有几个层面：(1) attention weight 是 input-dependent 的高维对象，
      简单的 aggregated statistics（entropy, max attention, positional bias）丢失了
      太多信息，真正的机制可能在 attention 与 recurrent state 的交互中，单独看
      attention 不够；(2) helped/hurt 的二分类本身粗糙——attention 可能对 logprob
      变化有连续影响但被二值化后信号衰减；(3) h3-1 只有 3 层 attention（每 8 层一层），
      信息瓶颈严重，attention 的角色可能更多是 global routing 而非 sample-specific
      processing，pattern 差异不映射到 per-example outcome 差异。Cross-arch similarity
      0.35 说明不同架构的 attention 做了部分相似的事但不完全相同——既不能说 attention
      导致了 convergence（similarity 不够高），也不能说 attention 解释了 divergence
      （correlation 太低）。
    tables:
      - name: "Table: Attention pattern — per-example effect correlation"
        columns: [architecture, spearman_rho, p_value, n_samples, attn_entropy_diff_p]
        rows:
          - [GatedDeltaNet, 0.08, 0.065, 5153, 0.18]
          - [RetNet, 0.11, 0.014, 5153, 0.09]
          - [HGRN2, 0.06, 0.182, 5153, 0.41]
      - name: "Table: Cross-architecture attention pattern similarity (cosine)"
        columns: [pair, mean_cosine_sim, std, overlap_top10pct_positions]
        rows:
          - [GDN-RetNet, 0.38, 0.15, 0.22]
          - [GDN-HGRN2, 0.31, 0.18, 0.19]
          - [RetNet-HGRN2, 0.36, 0.14, 0.21]
    figures_description:
      - "Attention heatmaps (3 panels): averaged attention patterns for helped vs hurt samples per architecture。视觉上差异微弱，与低 correlation 一致。"
      - "Scatter plot: attention entropy vs logprob change per sample，3 architectures 分面。散点云无明显趋势，r < 0.15。"
    analysis: >
      Worst 档下 exp-004 是一个 informative negative：attention weight patterns 本身
      不能解释 per-example 效应。这并不削弱 Claim 3——反而加强了 "opaque to standard
      features" 的论述。Surface features 不行（exp-003），perplexity 不行
      （exp-003-p2），现在 attention patterns 也不行。Per-example divergence 的来源
      可能在 attention 与 recurrent state 的非线性交互中，这超出了 descriptive
      analysis 的能力范围，诚实地承认并指向 interventional future work（head ablation,
      activation patching）。论文中 frame 为 "characterization of what does NOT
      explain the divergence" 而非失败——negative results 在 analysis paper 中有价值。
      exp-004 从 "mechanistic evidence" 降级为 "descriptive exploration"，放入
      supplementary 或 appendix。

  - name: "Architecture expansion check"
    plan_id: "exp-005"
    description: >
      搜索 Wang et al. model zoo 和其他来源，寻找额外的 hybrid 架构
      （Mamba/Mamba2 hybrids, RWKV hybrids）。Worst 档下无额外架构可用。
    expected_results:
      additional_architectures_found: 0
      n_architectures_total: 3
      mamba_hybrid_available: false
      rwkv_hybrid_available: false
      other_hybrid_available: false
      search_sources_checked: ["wang_et_al_zoo", "huggingface_hub", "github_repos"]
    result_rationale: >
      Wang et al. (2025) 的 model zoo 专注于 GatedDeltaNet、RetNet、HGRN2 三个
      linear recurrent 架构。Mamba/Mamba2 hybrids（如 Jamba）使用不同的 attention
      integration 策略且没有公开的 systematic ratio sweep（Jamba 只有一个固定配置）。
      RWKV-6 hybrids 尚未有公开的 pretrained checkpoints with varying attention ratios。
      RecurrentGemma 是 closed-weight。在 worst 档下，即使找到个别 checkpoint，也
      缺乏 attention ratio sweep（需要 h0/h3-1/h6-1/h12-1/h24-1 五个配置），
      无法做 convergence 分析。训练新模型超出 GPU budget。n=3 的限制在 paper 中
      必须诚实承认为 limitation，但 per-example analysis 的 5153 data points per
      comparison 部分补偿了架构数量的不足。
    tables: []
    figures_description: []
    analysis: >
      Worst 档下 exp-005 确认 n=3 是硬约束。Reviewer Concern D ("n=3 too few") 只能
      通过 framing 来 mitigate：(1) 3 architectures × 5 ratios × 2 scales = 30
      models 的 systematic design，(2) per-example 分析提供 thousands of data points，
      (3) 这三个架构代表了当前 linear recurrent 家族的主要分支（gated delta,
      retention, hierarchical gated），(4) 在 limitations 中诚实承认并指向 future work。
      对 reframed narrative 影响有限——per-example divergence 的 Jaccard < 0.10 在 3
      个架构上已经充分证明了 architecture-specificity。

  - name: "340M rebound mechanism analysis"
    plan_id: "exp-007"
    description: >
      深入分析 340M 在 attn=8 的 non-monotonic rebound。Per-example 比较 340M 与
      1.3B 在相同 attention ratio 下的行为差异。Worst 档下 rebound 无清晰解释，
      噪声不可排除。
    expected_results:
      rebound_effect_size_cohens_d: 0.15
      rebound_sample_overlap_with_1_3b: 0.42
      rebound_explained_by_training_tokens: inconclusive
      capacity_hypothesis_p: 0.28
      per_example_340m_1_3b_correlation_at_h8: 0.18
      rebound_samples_surface_feature_diff_p: 0.35
      rebound_magnitude_std: 0.008
      noise_floor_permutation_p: 0.14
    result_rationale: >
      340M rebound 在 worst 档下无法与噪声区分开，原因：(1) 340M models 用 20B
      tokens 训练 vs 1.3B 用 100B tokens——training token confound 与 scale confound
      完全混淆，无法解缠；(2) rebound effect size 很小（Cohen's d ≈ 0.15），在
      permutation test 下 p=0.14，不能排除采样噪声；(3) 340M 与 1.3B 在 h8 的
      per-example correlation 很低（0.18），说明两个 scale 的 attention 效应作用于
      不同的 sample subsets，但这可能纯粹是因为 340M 容量不足导致的随机差异而非
      有意义的 mechanistic difference；(4) surface features 无法区分 rebound samples
      与 non-rebound samples（p=0.35）。整体结论：340M rebound 是 noisy observation，
      不能支撑 Claim 2 的 "scale is necessary condition" narrative。
    tables:
      - name: "Table: 340M rebound characterization"
        columns: [metric, value, interpretation]
        rows:
          - [rebound_magnitude_attn8, 0.008, "cross-arch std increases from 0.015 to 0.023 at h8"]
          - [cohens_d, 0.15, "small effect, within noise range"]
          - [permutation_p, 0.14, "not significant at any conventional threshold"]
          - [340m_1.3b_per_example_r, 0.18, "near-zero per-example correspondence across scales"]
          - [training_token_ratio, "20B vs 100B", "5x confound, cannot separate from scale"]
    figures_description:
      - "Line plot: cross-arch std vs attention ratio for 340M and 1.3B overlaid。340M 线在 h8 处有微弱上翘但 error bar 大，1.3B 线单调下降。视觉上 rebound 不 compelling。"
    analysis: >
      Worst 档下 Claim 2 (scale-dependent convergence) 几乎完全失效。340M rebound
      既不能被解释也不能被确认为真实信号。在 reframed narrative 下，Claim 2 整体
      降级为 supplementary observation："We observe that convergence appears more
      complete at 1.3B than 340M, but the confound between scale (340M vs 1.3B)
      and training data (20B vs 100B tokens) prevents causal attribution. The 340M
      rebound at high attention ratios is not statistically distinguishable from
      noise (p=0.14)." 这段话放在 supplementary 即可。主论文只需一句话提及 scale
      作为 limitation/future work。

  - name: "Convergence-divergence bridge analysis"
    plan_id: "exp-010"
    description: >
      对 LAMBADA 绘制 aggregate convergence 曲线与 per-example divergence 指标的
      co-evolution。Worst 档下 convergence 本身被质疑（GDN-excluded 弱化），
      bridge 分析的叙事价值降低。
    expected_results:
      convergence_divergence_correlation_rho: -0.8
      convergence_divergence_correlation_p: 0.10
      jaccard_vs_attn_ratio_rho: -0.6
      jaccard_vs_attn_ratio_p: 0.28
      net_effect_asymmetry_trend: weak_negative
      gdn_excluded_bridge_rho: -0.4
      gdn_excluded_bridge_p: 0.50
    result_rationale: >
      在 worst 档下，bridge 分析面临两个问题：(1) 全集 convergence-divergence
      correlation 看似强（rho=-0.8）但 n=5 attention ratios 只有 120 permutations，
      p=0.10 不显著——这和 exp-008 的 LAMBADA 结果一致，小 n 下 rank correlation
      本身 underpowered；(2) 排除 GDN 后 bridge correlation 跌至 rho=-0.4, p=0.50，
      说明 co-evolution 的外观部分依赖 GDN 的 confound-driven convergence。
      Jaccard 随 attention ratio 增加确实趋向更低（divergence 增加），但 n=5
      的 rank correlation 在 p=0.28 不显著。底线：有方向性趋势但统计上不可靠，
      不能作为 claim 的支撑证据。在 reframed narrative 下，这个 bridge 分析从
      "核心可视化" 降级为 "illustrative figure"——展示现象但不做统计 claim。
    tables:
      - name: "Table: Convergence-divergence co-evolution (LAMBADA, 1.3B)"
        columns: [attn_ratio, cross_arch_std, mean_pairwise_jaccard, n_helped_union, n_hurt_union]
        rows:
          - [h0, 0.024, "N/A (baseline)", 0, 0]
          - [h3-1, 0.018, 0.09, 1436, 1505]
          - [h6-1, 0.012, 0.08, 1512, 1580]
          - [h12-1, 0.008, 0.07, 1590, 1648]
          - [h24-1, 0.005, 0.06, 1650, 1710]
    figures_description:
      - "Dual-axis line plot: left axis = cross-arch std (decreasing), right axis = mean pairwise Jaccard (decreasing)。两条线都下降但 confidence bands 宽。GDN-excluded 版本作为 inset，趋势更弱。"
    analysis: >
      Worst 档下 exp-010 的 bridge 分析从论文核心可视化降级为 illustrative/descriptive
      figure。不做 "convergence and divergence co-evolve" 的统计 claim——只描述观察到的
      趋势并注明 underpowered。在 reframed narrative 下，这个图的用途变为展示
      per-example divergence 在不同 attention ratios 下的变化（支撑 Claim 3），而非
      证明 convergence-divergence 的 mechanistic link。图仍然有价值但降级为 Figure 3
      或 4，不再是 Figure 1/2。

  - name: "Additional high-retrieval benchmarks"
    plan_id: "exp-011"
    description: >
      在 StoryCloze, BoolQ, COPA 上运行 1.3B 全部模型。Worst 档下所有新 benchmark
      均无 convergence 信号，LAMBADA 的孤立性被确认。
    expected_results:
      storycloze_rho: -0.3
      storycloze_p: 0.45
      storycloze_cross_arch_std_h0: 0.019
      storycloze_cross_arch_std_h24: 0.016
      storycloze_std_reduction_pct: 16
      boolq_rho: -0.1
      boolq_p: 0.85
      boolq_cross_arch_std_h0: 0.022
      boolq_cross_arch_std_h24: 0.020
      boolq_std_reduction_pct: 9
      copa_rho: 0.2
      copa_p: 0.70
      copa_cross_arch_std_h0: 0.031
      copa_cross_arch_std_h24: 0.035
      copa_std_reduction_pct: -13
      best_new_rho: -0.3
      best_new_p: 0.45
      n_new_significant: 0
      bh_fdr_total_significant: 0
      bonferroni_total_significant: 0
      total_benchmarks_tested: 9
      lambada_bh_fdr_adj_p_9tests: 0.15
      gdn_excluded_storycloze_rho: -0.1
      gdn_excluded_boolq_rho: 0.3
      gdn_excluded_copa_rho: 0.5
    result_rationale: >
      Worst 档的核心预测：所有新 benchmark ρ > -0.5 且 p > 0.25。原因：(1) StoryCloze
      虽然结构类似 LAMBADA（context → completion），但选项是两个完整句子而非单个
      token，architectures 的差异在句子级别的 likelihood ranking 上不缩小——attention
      帮助的方式更分散，不像 LAMBADA 的单 token retrieval 那样有 focal point；
      (2) BoolQ 是 passage-based yes/no，本质上是 reading comprehension，更接近
      reasoning 而非 pure retrieval，convergence 不出现与 HellaSwag/ARC 一致；
      (3) COPA 是 causal reasoning，样本量小（400 test + 100 val），noise floor 高，
      cross-arch std 本身波动大，rho 可以是正的纯粹因为噪声。排除 GDN 后进一步
      恶化——StoryCloze rho 从 -0.3 变成 -0.1，证实 GDN 贡献了大部分微弱的趋势。
      BH-FDR 在 9 个 tests 下对 LAMBADA 的 adj-p 从 0.10 变成 0.15，LAMBADA 本身
      也不再 survive FDR。这是 worst 档最致命的结果：不仅没找到第二个 anchor，
      反而因为增加了 test 数量让 LAMBADA 的多重校正更严格。
    tables:
      - name: "Table: Cross-architecture convergence — all benchmarks (1.3B, 9 tests)"
        columns: [benchmark, task_type, rho, raw_p, bh_fdr_p, bonferroni_p, std_reduction_pct]
        rows:
          - [LAMBADA, retrieval, -1.0, 0.017, 0.150, 0.150, 79]
          - [StoryCloze, completion, -0.3, 0.450, 0.675, 1.000, 16]
          - [BoolQ, comprehension, -0.1, 0.850, 0.956, 1.000, 9]
          - [COPA, causal, 0.2, 0.700, 0.900, 1.000, -13]
          - [ARC-Easy, mixed, -0.7, 0.233, 0.467, 1.000, 42]
          - [ARC-Challenge, reasoning, 0.6, 0.350, 0.563, 1.000, -18]
          - [HellaSwag, reasoning, 0.3, 0.683, 0.900, 1.000, -8]
          - [WinoGrande, reasoning, 0.1, 0.950, 0.950, 1.000, 3]
          - [MMLU, mixed, -0.7, 0.233, 0.467, 1.000, 35]
      - name: "Table: GDN-excluded sensitivity — new benchmarks"
        columns: [benchmark, full_rho, full_p, gdn_excl_rho, gdn_excl_p, direction]
        rows:
          - [StoryCloze, -0.3, 0.450, -0.1, 0.783, WEAKER]
          - [BoolQ, -0.1, 0.850, 0.3, 0.550, WEAKER]
          - [COPA, 0.2, 0.700, 0.5, 0.450, WEAKER]
    figures_description:
      - "Forest plot: 9 benchmarks 的 rho ± CI，按 task type 分组。LAMBADA 孤立在最左端（rho=-1.0），其余 benchmarks CI 全部跨越零线。视觉上 LAMBADA 是明显的 outlier。"
      - "Bar chart: BH-FDR adjusted p-values for 9 benchmarks，α=0.05 水平线。没有任何 bar 低于 α 线，包括 LAMBADA（adj-p=0.15）。"
    analysis: >
      exp-011 的 worst 档结果是整个项目叙事转折的 trigger。三个关键后果：
      (1) Convergence claim 彻底死亡——9 个 benchmarks 中 0 个 survive BH-FDR，
      LAMBADA 自身的 adj-p 从 0.10（6 tests）恶化到 0.15（9 tests），增加 tests
      反而 hurt statistical case。
      (2) Task-specificity taxonomy 失去了正面 anchor——不再是 "retrieval tasks
      converge, reasoning tasks don't"，而是 "nothing converges except maybe LAMBADA
      and that's likely noise or GDN-driven"。
      (3) 但 per-example divergence 分析完全不受影响——Jaccard < 0.10 在 LAMBADA
      上的发现不依赖 convergence，且如果 exp-002 在新 benchmarks 上也发现低 Jaccard，
      那 per-example architecture-specificity 是独立于 convergence 的 robust finding。
      论文的 reframe 路径：Title 变为 per-example divergence 论文，LAMBADA convergence
      在 discussion 中用 1-2 段提及（"on one retrieval benchmark we observe suggestive
      but non-significant convergence"），核心贡献完全转向 Claim 3。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e645d1aa-c00b-425d-9ac0-71c293946944",
  "isSidechain": false,
  "requestId": "req_011CbC7vvtgbi5sKB4e18c3J",
  "type": "assistant",
  "uuid": "a88e96eb-2308-4df2-85b8-72e877dabd28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GsVXZcNHSJbATSqbiE2uT6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13462,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8498,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13462
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：exp-011 全部新 benchmark 无 convergence 信号（ρ > -0.5 或 p > 0.3）；LAMBADA 是孤立的单点发现且不 survive 任何多重校正；exp-004 attention pattern 无解释力（correlation < 0.15）；exp-005 无进…",
  "leafUuid": "a88e96eb-2308-4df2-85b8-72e877dabd28",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Per-example divergence in hybrid recurrent architectures",
  "sessionId": "2adf5397-5a56-488d-a8d9-974d0752b4cc"
}
```

---
