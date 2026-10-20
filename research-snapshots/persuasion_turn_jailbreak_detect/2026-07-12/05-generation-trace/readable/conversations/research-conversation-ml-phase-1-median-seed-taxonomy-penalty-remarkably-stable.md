# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：方差梯度和大方向成立，但剂量-响应的具体数字跨 seed 波动较大；taxonomy penalty 存在但不再'remarkably stable

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/661f5529-50a9-4342-9058-955d0518bc2a.jsonl`
- **Structured JSON:** [`508a298db777b10146de.json`](../../sessions/50/508a298db777b10146de.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:22:10.127Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:22:10.127Z",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：方差梯度和大方向成立，但剂量-响应的具体数字跨 seed 波动较大；taxonomy penalty 存在但不再'remarkably stable'；统计检验仍为 marginal\n核心假设：['多 seed 剂量-响应显示 threshold-plateau 的大致形状但阈值位置在 10-30% 间漂移', 'taxonomy penalty 跨 seed 均值 ~5-7pp 但个别 dose 点变动 3-9pp', '方差梯度在均值层面成立（Vanilla SD < Random SD < TaxEI SD），但个别 seed 偶尔打破 Random < TaxEI 排序', '训练 loss 曲线显示注入样本 loss 更高，但对 clean 样本的 corruption 效应不明显', 'pooled p 值停留在 0.05-0.15 区间，无法突破 α=0.05']\n关键指标范围：{'taxei_3seed_mean_pct': [55.0, 62.0], 'taxei_3seed_sd_pp': [6.0, 12.0], 'vanilla_3seed_sd_pp': [3.0, 5.0], 'taxonomy_penalty_per_dose_pp': [3.0, 9.0], 'taxonomy_penalty_cross_dose_sd_pp': [1.5, 3.5], 'dose_threshold_drop_pp': [6.0, 16.0], 'pooled_p_taxei_vs_vanilla': [0.05, 0.15], 'paired_t_taxei_vs_random_p': [0.03, 0.1], 'dose_response_cross_seed_agreement': [0.5, 0.85]}\n叙事方向：需要调整 claims 强度。不再称 taxonomy penalty 为 \"remarkably stable constant\"， 改为 \"consistent directional penalty\"（方向一致但幅度有 seed 依赖）。 剂量-响应从 \"universal threshold-plateau\" 降级为 \"tendency toward non-linear degradation\"。 核心叙事从三个 crisp finding 收缩为：(1) 方差梯度作为 primary finding（最 robust）， (2) taxonomy label 作为 amplifier of instability（方向性 claim）， (3) 剂量-响应作为 exploratory evidence with caveats。 论文仍然成立为 cautionary negative result，但 contribution 更多是 \"error injection 不应被默认迁移到 embodied planning\" 而非精确的定量边界条件。 可能需要补一个 qualitative failure analysis 来弥补定量证据的不足。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: tax_error_inject_agent\nvenue: Insights from Negative Results in NLP @ EMNLP 2026\nfocus: Negative result paper with three core findings: (1) variance gradient Vanilla&lt;Random&lt;TaxEI, (2) dose-response threshold-plateau with shared 12.8pp drop at 10-25%, (3) constant ~6.4pp taxonomy label penalty. All statistical comparisons NS (min p=0.054). Single-seed dose-response limitation.\n\n## paper_framing.md\n\n# Paper Framing: Error Injection Helps Tool-Use but Hurts Planning — Boundary Conditions for Failure-Augmented Agent Training\n\n## Target Venue\n**Primary**: Insights from Negative Results in NLP @ EMNLP 2026 (Budapest, Oct 22–29) — short paper track, purpose-built for rigorous negative findings.\n**Backup**: EMNLP 2026 Findings (main conference accepts negative-result contributions per CFP).\n\n## Core Question\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\n\n## Thesis Statement\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training (2.6× variance increase, non-linear dose-response with catastrophic collapse above 10% injection ratio) without improving performance on ALFWorld, suggesting that **task structure** may be the primary factor determining whether failure-augmented training transfers.\n\n## Story Arc\n\n### 1. Motivation: Why error injection should work\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\n- **P1** (step_order_swap): permute action ordering\n- **P2** (sub_goal_deletion): remove sub-goals\n- **C1** (context_truncation): truncate environmental context\n- **C4** (observation_masking): mask observation feedback\n\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\n\n### 3. Finding: No benefit, high instability\n**Clean task performance (3-seed, all methods complete)**:\n- Vanilla SFT: 65.3% ± 3.3pp (seeds 42/0/123) — stable\n- TaxEI SFT: 56.7% ± 8.6pp (seeds 42/0/123) — **2.6× variance, -8.6pp mean but p≈0.32 (NS)**\n- Random SFT: 63.1% ± 7.0pp (seeds 42/0/123) — **2.1× variance, -2.2pp mean (NS)**\n\n**Critical pattern**: TaxEI seeds 42 and 123 both equal vanilla (61.7%), but seed=0 collapses to 46.8%. Error injection doesn't reliably hurt — it makes training a lottery.\n\n**Variance gradient**: Vanilla SD (3.3pp) < Random SD (7.0pp) < TaxEI SD (8.6pp). More structured injection → more training instability. This gradient is itself a finding: taxonomy labels amplify variance beyond what random noise injection introduces.\n\n**Dose-response ablation (fixed-size 4,358 total, seed=42, vs vanilla-seed42=61.7%)**:\n| Dose | TaxEI | Random | Δ(R−T) |\n|------|-------|--------|---------|\n| 0% (vanilla) | 61.7% | 61.7% | 0 |\n| 10% | 61.7% (0pp) | 68.1% (+6.4pp) | +6.4pp |\n| 25% | 48.9% (-12.8pp) | 55.3% (-6.4pp) | +6.4pp |\n| 50% | 51.1% (-10.6pp) | 57.4% (-4.3pp) | +6.3pp |\n\n**Two separable effects**:\n1. **Injection dose threshold** (shared by both methods): 10%→25% both drop exactly 12.8pp (TaxEI: 61.7→48.9, Random: 68.1→55.3). The threshold between 10-25% and subsequent plateau at 50% is a universal property of error injection, not TaxEI-specific. Mechanism: data dilution crosses a critical signal-to-noise boundary.\n2. **Taxonomy label penalty** (constant ~6.4pp additive offset): TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose points. This remarkably stable gap suggests taxonomy labels introduce a systematic bias independent of injection volume — structured error patterns may teach the model specific wrong behaviors that random noise does not.\n\nNote: All dose-response data is single-seed (seed=42). Given 3-seed SD up to 8.6pp, individual point estimates have limited confidence, but the consistency of the ~6.4pp gap across three independent dose points strengthens the finding. The 68.1% for Random 10% falls within vanilla seed variance (61.7-68.1%) and should not be interpreted as a significant improvement over vanilla.\n\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\n\n**Detection Rate**: 0% for all methods.\n\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\n\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\n\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\n|-----------|----------------------|------------------------------|\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\n\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\n\n### 5. Contribution: What this negative result gives the community\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\n2. **Cost savings**: Prevents the community from pursuing error-injection approaches in ALFWorld-style domains without addressing the structural prerequisites we identify.\n3. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp). Two out of three TaxEI seeds match vanilla exactly; the third collapses by 14.9pp. Single-seed evaluations of error injection methods are fundamentally unreliable.\n4. **Dose-response with separable dual effects**: Injection ratio ablation (fixed data size, TaxEI and Random in parallel) reveals: (a) a shared threshold-plateau at 10-25% injection ratio — both methods drop identically by 12.8pp from their 10% baseline; (b) a constant ~6.4pp taxonomy label penalty across all dose levels, suggesting structured error patterns teach specific wrong behaviors that random noise does not. This decomposition — shared dose effect + additive taxonomy penalty — provides actionable guidance: even if injection ratio is optimized, taxonomy-guided injection remains inferior to random injection in embodied planning.\n\n## Core Claims (each backed by experimental evidence)\n\n- **Claim 1**: Taxonomy-guided error injection introduces high training variance and fails to improve clean task performance on ALFWorld.\n  → Support: TaxEI 3-seed mean 56.7%±8.6pp vs Vanilla 65.3%±3.3pp. Gap is -8.6pp. **Paired t-test (n=3 seeds): p≈0.32 (NS). Pooled permutation test (n=141 task-level observations): p=0.054 (NS at α=0.05, marginal).** Even the higher-powered pooled test cannot confirm significant degradation. Critically, 2/3 seeds (42, 123) show TaxEI = Vanilla (both 61.7%); the deficit is driven by seed=0 (46.8%). Gate 3a FAIL (no seed exceeds vanilla mean). TaxEI SD is 2.6× vanilla SD — the primary effect is **dramatically increased training instability**, not systematic degradation.\n\n- **Claim 2**: Taxonomy labels impose a constant ~6.4pp penalty compared to random (unlabeled) injection across all dose levels.\n  → Support: 3-seed clean eval: TaxEI 56.7% vs Random 63.1%, -6.4pp. Paired t p≈0.034 (df=2, suggestive but low power). Pooled permutation test: p=0.170 (NS). **Dose-response ablation provides stronger evidence**: TaxEI trails Random by 6.4/6.4/6.3pp at 10%/25%/50% injection ratios — a remarkably stable gap across three independent experiments, suggesting a systematic rather than stochastic effect. Recovery eval confirms the direction: TaxEI 59.6% < Random 63.8%. TaxEI SD (8.6pp) > Random SD (7.0pp). Caveat: all dose-response points are single-seed; the per-point gap is ~0.9 SE and not individually significant at n=47.\n\n- **Claim 3**: Error injection increases training instability disproportionately — this is the primary negative effect, with a clear variance gradient.\n  → Support: Cross-seed SD: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. TaxEI seed=0 collapses to 46.8% while seeds 42/123 match vanilla at 61.7% — a 14.9pp swing within the same method. The variance gradient (no injection < random injection < taxonomy-guided injection) suggests that more structured perturbation amplifies training instability rather than providing useful curriculum signal. A single favorable seed can mask injection's destabilizing effect, making published single-seed results unreliable.\n\n- **Claim 4**: Injection-trained models do not improve error recovery.\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp).\n\n- **Claim 5**: Detection training via error injection is completely ineffective in this setup.\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random).\n\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Statistical power with 3 seeds is limited.\"**\n   → All three methods now have 3 seeds. TaxEI vs Vanilla: p≈0.32 (NS) — we do not claim a significant mean difference but instead emphasize the variance effect (SD 8.6pp vs 3.3pp, 2.6× ratio). TaxEI vs Random: paired t p≈0.034 (df=2, suggestive). We report all individual seed results transparently. The variance gradient (Vanilla < Random < TaxEI) is directionally consistent across all seeds.\n\n2. **\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\"**\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. We propose a second environment (WebShop) for supplementary validation.\n\n3. **\"Maybe the taxonomy itself is poorly designed.\"**\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\n\n4. **\"The training recipe might be suboptimal for injection data.\"**\n   → The same recipe produces strong Vanilla results (65.3% vs 42.6% baseline, +22.7pp), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\n\n5. **\"50% injection ratio is too high — you're drowning the signal.\"**\n   → Comprehensively addressed with fixed-size dose-response ablation (all 4,358 total samples, seed=42). Results: 10% = 61.7% (0pp), 25% = 48.9% (-12.8pp), 50% = 51.1% (-10.6pp). The pattern is threshold-plateau, not linear: below ~15-20% injection is harmless but provides no benefit; above it, performance collapses and plateaus regardless of further injection increase. Even at the lowest tested ratio (10%), injection provides zero improvement over vanilla — the best case is exact parity. Random injection dose-response (in progress) will determine whether the threshold is specific to taxonomy-guided injection or a general property.\n\n6. **\"Why is detection rate 0%? Evaluation might be flawed.\"**\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\n\n7. **\"Why not compare directly on ToolBench?\"**\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\n\n## Key Differentiators vs PALADIN\n\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\n\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \"go to countertop 2\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\n\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\n\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \"what to do after an error\" fundamentally harder to learn from examples.\n\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\n\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\n## Note on v3→v4 Vanilla Discrepancy\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\n\n## Supplementary Experiments Needed\n\n### Priority 1 (required for submission)\n- ~~**More seeds**~~: ✅ DONE — All 3 methods at 3 seeds. Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\n- **Injection ratio ablation**: ✅ TaxEI dose-response done (10%=61.7%, 25%=48.9%, 50% in progress). Random dose-response in progress (10%, 25%, 50% training). Key finding: non-linear threshold between 10-25%.\n- **Training dynamics analysis**: Plot training loss curves for clean vs. injected samples across epochs. Do injected samples have systematically higher loss? Does the model learn clean patterns before injection patterns corrupt them?\n\n### Priority 2 (strengthens paper significantly)\n- **Second environment**: WebShop or ScienceWorld to test whether the negative result generalizes beyond ALFWorld. If error injection also fails there, the boundary condition claim is stronger.\n- **Qualitative failure analysis**: Manually examine 20+ TaxEI failure cases — does the model produce incoherent plans, or does it simply choose wrong actions at similar rates? This informs the \"noise vs. wrong learning\" distinction.\n\n### Priority 3 (nice to have)\n- **Scale ablation**: Does TaxEI improve if we scale to 25K or 50K trajectories (matching PALADIN's scale)?\n- **Explicit recovery prompting**: Instead of SFT, test whether in-context recovery examples (few-shot) help — this isolates whether the issue is training signal vs. knowledge.\n- **Per-operator deep dive**: Run more seeds on recovery eval to determine if C4 (observation masking) is genuinely easier for TaxEI or if the +9.1pp advantage is noise.\n\n\n## registry (completed experiments)\n\n- exp_id: traj_collect_500\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    successful_trajectories: 501\n    failed_trajectories: 213\n    total_attempts: 714\n    success_rate: 0.702\n    api_cost_usd: 8.86\n    collection_time_sec: 5245\n- exp_id: sft-dryrun-73\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_init: 2.436\n    train_loss_final: 1.543\n    train_loss_avg: 1.894\n    peak_memory_gib: 19.22\n    steps: 8\n    duration_sec: 42\n    data_vanilla: 124\n    data_injected_dryrun: 96\n    injected_failed: 4\n- exp_id: vanilla-react-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_success_rate: 0.426\n    total_tasks: 47\n    successes: 20\n    per_task_type:\n      pick_heat_then_place:\n        success: 5\n        total: 8\n        rate: 0.625\n      look_at_obj_in_light:\n        success: 3\n        total: 6\n        rate: 0.5\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_two_obj_and_place:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_cool_then_place:\n        success: 0\n        total: 7\n        rate: 0\n- exp_id: mini-pipeline-e2e\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mini-taxei-sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.447\n    eval_successes: 21\n    eval_total: 47\n    vs_baseline_pp: 2.1\n    per_task:\n      look_at_obj_in_light: 3/6 (50.0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 1/7 (14.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_two_obj_and_place: 3/7 (42.9%)\n    train_steps: 195\n    train_duration_min: 16.3\n- exp_id: mini-vanilla-sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.149\n    eval_successes: 7\n    eval_total: 47\n    vs_baseline_pp: -27.7\n    per_task:\n      look_at_obj_in_light: 0/6 (0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 2/11 (18.2%)\n      pick_cool_then_place: 0/7 (0%)\n      pick_heat_then_place: 3/8 (37.5%)\n      pick_two_obj_and_place: 0/7 (0%)\n    train_steps: 54\n    train_duration_min: 5\n- exp_id: vanilla_sft_aligned_v1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: vanilla_sft_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mini-vanilla-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 4176\n    train_steps_total: 1566\n    est_duration_min: 58\n    format: aligned_single_turn\n- exp_id: mini-taxei-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 7545\n    train_samples_clean: 4176\n    train_samples_injected: 3369\n    train_steps_total: 2832\n    est_duration_min: 90\n    format: aligned_single_turn\n- exp_id: mini-random-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 9076\n    train_samples_clean: 4176\n    train_samples_injected: 4900\n    train_steps_total: 3405\n    est_duration_min: 110\n    format: aligned_single_turn\n- exp_id: mini-vanilla-sft-v4\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v3-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.745\n    successes: 35\n    total: 47\n    vs_baseline_pp: 31.9\n    vs_baseline: 42.6% → 74.5%\n- exp_id: v3-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_baseline_pp: 23.4\n    vs_vanilla_sft_pp: -8.5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_clean_then_place: 8/11 (72.7%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_cool_then_place: 3/7 (42.9%)\n- exp_id: v3-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_baseline_pp: 8.5\n    vs_vanilla_sft_pp: -23.4\n- exp_id: v4-taxei-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-random-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-random-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-taxei-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-random-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_clean_then_place: 5/11 (45.5%)\n- exp_id: v4-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    vs_vanilla_pp: 0\n    vs_random_pp: -4.3\n    mcnemar_vs_vanilla_p: 1\n    mcnemar_vs_random_p: 0.754\n    gate_3a: FAIL\n    gate_3b: FAIL\n    gate_4: PASS\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 3/7 (42.9%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 2/7 (28.6%)\n- exp_id: v4-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_vanilla_pp: 4.3\n    vs_taxei_pp: 4.3\n    mcnemar_vs_vanilla_p: 0.754\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 4/8 (50%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n- exp_id: v4-vanilla-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.297\n    avg_loss: 0.416\n    token_accuracy: 0.902\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.917\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-random-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.912\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-recovery-eval-dev\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    pipeline_files:\n    - eval/injected_eval.py\n    - scripts/run_injected_eval.sh\n    injected_eval_lines: 463\n    dryrun_result: PASS\n    dryrun_detail: vanilla checkpoint, 1 task, cuda:3, injected error recovered in\n      13 steps\n- exp_id: v4-vanilla-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.288\n    token_accuracy: 0.903\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58.9\n- exp_id: v4-vanilla-seed7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-recovery-dryrun\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    vs_seed42_pp: 6.4\n    mcnemar_vs_seed42_p: 0.375\n    discordant_pairs: 5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 5/7 (71.4%)\n- exp_id: v4-taxei-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.468\n    eval_successes: 22\n    eval_total: 47\n    vs_seed42_pp: -14.9\n- exp_id: v4-random-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_seed42_pp: -10.7\n- exp_id: v4-vanilla-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_seed42_pp: 4.3\n    vs_seed0_pp: -2.1\n    per_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 7\n        total: 8\n        rate: 0.875\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-vanilla-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    successes: 29\n    total: 47\n    recovery_rate: 0.617\n    detection_rate: 0\n- exp_id: v4-taxei-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success_rate: 0.596\n    successes: 28\n    total: 47\n    recovery_rate: 0.596\n    detection_rate: 0\n- exp_id: v4-random-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.638\n    detection_rate: 0\n    successes: 30\n    total: 47\n    source: json-file-verified\n    note: r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\n- exp_id: v4-taxei-recovery-eval-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.596\n    detection_rate: 0\n    total_episodes: 47\n    per_operator:\n      C1_context_truncation:\n        recovered: 8\n        total: 12\n        rate: 0.667\n      C4_observation_masking:\n        recovered: 7\n        total: 11\n        rate: 0.636\n      P1_step_order_swap:\n        recovered: 7\n        total: 12\n        rate: 0.583\n      P2_sub_goal_deletion:\n        recovered: 6\n        total: 12\n        rate: 0.5\n- exp_id: v4-taxei-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.35506879\n    token_accuracy: 0.89978214\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 109.2\n    train_runtime_sec: 6549.432\n    train_speed_s_per_it: 1.934\n    memory_gib: 18.49\n- exp_id: v4-random-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.35484016\n    final_loss: 0.16766574\n    token_accuracy: 0.94187103\n    avg_token_accuracy: 0.90849673\n    train_steps: 3387\n    train_epochs: 3\n    train_runtime_sec: 6609.3556\n    train_duration_min: 110.2\n    train_samples_per_second: 4.098\n    train_steps_per_second: 0.512\n    train_speed_s_per_it: 1.951\n    memory_gib: 18.49\n- exp_id: v4-fixed-inject10\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-fixed-inject25\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.308\n    token_accuracy: 0.888\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject25-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.285\n    token_accuracy: 0.893\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        success: 7\n        total: 11\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.489\n    eval_successes: 23\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 4\n        total: 6\n        rate: 0.667\n      pick_and_place_simple:\n        success: 3\n        total: 8\n        rate: 0.375\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 2\n        total: 7\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-random-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 7\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-taxei-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.259\n    token_accuracy: 0.911\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 53.1\n- exp_id: v4-random-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4226\n    final_step_loss: 0.3079\n    token_accuracy: 0.9\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 57\n- exp_id: v4-random-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-random-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n    train_loss: 0.4338\n    final_step_loss: 0.2618\n    token_accuracy: 0.91\n    train_duration_min: 53.1\n    memory_gib: 18\n    train_speed_s_per_it: 1.95\n- exp_id: v4-taxei-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_vanilla_seed42_pp: -10.6\n- exp_id: v4-random-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-random-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.574\n    eval_successes: 27\n    eval_total: 47\n    vs_vanilla_seed42_pp: -4.3\n    vs_taxei_50_pp: 6.3\n- exp_id: v4-random-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_vanilla_seed42_pp: -6.4\n    vs_taxei_25_pp: 6.4\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T02:22:10.130Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:22:10.130Z",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---

## Round 1

22 recorded events

### User

_source line 3 · 2026-05-15T02:22:10.148Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：方差梯度和大方向成立，但剂量-响应的具体数字跨 seed 波动较大；taxonomy penalty 存在但不再'remarkably stable'；统计检验仍为 marginal
核心假设：['多 seed 剂量-响应显示 threshold-plateau 的大致形状但阈值位置在 10-30% 间漂移', 'taxonomy penalty 跨 seed 均值 ~5-7pp 但个别 dose 点变动 3-9pp', '方差梯度在均值层面成立（Vanilla SD < Random SD < TaxEI SD），但个别 seed 偶尔打破 Random < TaxEI 排序', '训练 loss 曲线显示注入样本 loss 更高，但对 clean 样本的 corruption 效应不明显', 'pooled p 值停留在 0.05-0.15 区间，无法突破 α=0.05']
关键指标范围：{'taxei_3seed_mean_pct': [55.0, 62.0], 'taxei_3seed_sd_pp': [6.0, 12.0], 'vanilla_3seed_sd_pp': [3.0, 5.0], 'taxonomy_penalty_per_dose_pp': [3.0, 9.0], 'taxonomy_penalty_cross_dose_sd_pp': [1.5, 3.5], 'dose_threshold_drop_pp': [6.0, 16.0], 'pooled_p_taxei_vs_vanilla': [0.05, 0.15], 'paired_t_taxei_vs_random_p': [0.03, 0.1], 'dose_response_cross_seed_agreement': [0.5, 0.85]}
叙事方向：需要调整 claims 强度。不再称 taxonomy penalty 为 "remarkably stable constant"， 改为 "consistent directional penalty"（方向一致但幅度有 seed 依赖）。 剂量-响应从 "universal threshold-plateau" 降级为 "tendency toward non-linear degradation"。 核心叙事从三个 crisp finding 收缩为：(1) 方差梯度作为 primary finding（最 robust）， (2) taxonomy label 作为 amplifier of instability（方向性 claim）， (3) 剂量-响应作为 exploratory evidence with caveats。 论文仍然成立为 cautionary negative result，但 contribution 更多是 "error injection 不应被默认迁移到 embodied planning" 而非精确的定量边界条件。 可能需要补一个 qualitative failure analysis 来弥补定量证据的不足。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: tax_error_inject_agent
venue: Insights from Negative Results in NLP @ EMNLP 2026
focus: Negative result paper with three core findings: (1) variance gradient Vanilla&lt;Random&lt;TaxEI, (2) dose-response threshold-plateau with shared 12.8pp drop at 10-25%, (3) constant ~6.4pp taxonomy label penalty. All statistical comparisons NS (min p=0.054). Single-seed dose-response limitation.

## paper_framing.md

# Paper Framing: Error Injection Helps Tool-Use but Hurts Planning — Boundary Conditions for Failure-Augmented Agent Training

## Target Venue
**Primary**: Insights from Negative Results in NLP @ EMNLP 2026 (Budapest, Oct 22–29) — short paper track, purpose-built for rigorous negative findings.
**Backup**: EMNLP 2026 Findings (main conference accepts negative-result contributions per CFP).

## Core Question
Under what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?

## Thesis Statement
Taxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training (2.6× variance increase, non-linear dose-response with catastrophic collapse above 10% injection ratio) without improving performance on ALFWorld, suggesting that **task structure** may be the primary factor determining whether failure-augmented training transfers.

## Story Arc

### 1. Motivation: Why error injection should work
Error injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?

### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning
We designed a 4-operator error taxonomy for ALFWorld embodied planning:
- **P1** (step_order_swap): permute action ordering
- **P2** (sub_goal_deletion): remove sub-goals
- **C1** (context_truncation): truncate environmental context
- **C4** (observation_masking): mask observation feedback

We injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.

### 3. Finding: No benefit, high instability
**Clean task performance (3-seed, all methods complete)**:
- Vanilla SFT: 65.3% ± 3.3pp (seeds 42/0/123) — stable
- TaxEI SFT: 56.7% ± 8.6pp (seeds 42/0/123) — **2.6× variance, -8.6pp mean but p≈0.32 (NS)**
- Random SFT: 63.1% ± 7.0pp (seeds 42/0/123) — **2.1× variance, -2.2pp mean (NS)**

**Critical pattern**: TaxEI seeds 42 and 123 both equal vanilla (61.7%), but seed=0 collapses to 46.8%. Error injection doesn't reliably hurt — it makes training a lottery.

**Variance gradient**: Vanilla SD (3.3pp) < Random SD (7.0pp) < TaxEI SD (8.6pp). More structured injection → more training instability. This gradient is itself a finding: taxonomy labels amplify variance beyond what random noise injection introduces.

**Dose-response ablation (fixed-size 4,358 total, seed=42, vs vanilla-seed42=61.7%)**:
| Dose | TaxEI | Random | Δ(R−T) |
|------|-------|--------|---------|
| 0% (vanilla) | 61.7% | 61.7% | 0 |
| 10% | 61.7% (0pp) | 68.1% (+6.4pp) | +6.4pp |
| 25% | 48.9% (-12.8pp) | 55.3% (-6.4pp) | +6.4pp |
| 50% | 51.1% (-10.6pp) | 57.4% (-4.3pp) | +6.3pp |

**Two separable effects**:
1. **Injection dose threshold** (shared by both methods): 10%→25% both drop exactly 12.8pp (TaxEI: 61.7→48.9, Random: 68.1→55.3). The threshold between 10-25% and subsequent plateau at 50% is a universal property of error injection, not TaxEI-specific. Mechanism: data dilution crosses a critical signal-to-noise boundary.
2. **Taxonomy label penalty** (constant ~6.4pp additive offset): TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose points. This remarkably stable gap suggests taxonomy labels introduce a systematic bias independent of injection volume — structured error patterns may teach the model specific wrong behaviors that random noise does not.

Note: All dose-response data is single-seed (seed=42). Given 3-seed SD up to 8.6pp, individual point estimates have limited confidence, but the consistency of the ~6.4pp gap across three independent dose points strengthens the finding. The 68.1% for Random 10% falls within vanilla seed variance (61.7-68.1%) and should not be interpreted as a significant improvement over vanilla.

**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:
- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%

**Detection Rate**: 0% for all methods.

**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).

### 4. Analysis: Why it fails in embodied planning but works in tool-use

**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.
| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |
|-----------|----------------------|------------------------------|
| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |
| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |
| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |
| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |
| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |
| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |
| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |

**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.

**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.

### 5. Contribution: What this negative result gives the community
1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.
2. **Cost savings**: Prevents the community from pursuing error-injection approaches in ALFWorld-style domains without addressing the structural prerequisites we identify.
3. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp). Two out of three TaxEI seeds match vanilla exactly; the third collapses by 14.9pp. Single-seed evaluations of error injection methods are fundamentally unreliable.
4. **Dose-response with separable dual effects**: Injection ratio ablation (fixed data size, TaxEI and Random in parallel) reveals: (a) a shared threshold-plateau at 10-25% injection ratio — both methods drop identically by 12.8pp from their 10% baseline; (b) a constant ~6.4pp taxonomy label penalty across all dose levels, suggesting structured error patterns teach specific wrong behaviors that random noise does not. This decomposition — shared dose effect + additive taxonomy penalty — provides actionable guidance: even if injection ratio is optimized, taxonomy-guided injection remains inferior to random injection in embodied planning.

## Core Claims (each backed by experimental evidence)

- **Claim 1**: Taxonomy-guided error injection introduces high training variance and fails to improve clean task performance on ALFWorld.
  → Support: TaxEI 3-seed mean 56.7%±8.6pp vs Vanilla 65.3%±3.3pp. Gap is -8.6pp. **Paired t-test (n=3 seeds): p≈0.32 (NS). Pooled permutation test (n=141 task-level observations): p=0.054 (NS at α=0.05, marginal).** Even the higher-powered pooled test cannot confirm significant degradation. Critically, 2/3 seeds (42, 123) show TaxEI = Vanilla (both 61.7%); the deficit is driven by seed=0 (46.8%). Gate 3a FAIL (no seed exceeds vanilla mean). TaxEI SD is 2.6× vanilla SD — the primary effect is **dramatically increased training instability**, not systematic degradation.

- **Claim 2**: Taxonomy labels impose a constant ~6.4pp penalty compared to random (unlabeled) injection across all dose levels.
  → Support: 3-seed clean eval: TaxEI 56.7% vs Random 63.1%, -6.4pp. Paired t p≈0.034 (df=2, suggestive but low power). Pooled permutation test: p=0.170 (NS). **Dose-response ablation provides stronger evidence**: TaxEI trails Random by 6.4/6.4/6.3pp at 10%/25%/50% injection ratios — a remarkably stable gap across three independent experiments, suggesting a systematic rather than stochastic effect. Recovery eval confirms the direction: TaxEI 59.6% < Random 63.8%. TaxEI SD (8.6pp) > Random SD (7.0pp). Caveat: all dose-response points are single-seed; the per-point gap is ~0.9 SE and not individually significant at n=47.

- **Claim 3**: Error injection increases training instability disproportionately — this is the primary negative effect, with a clear variance gradient.
  → Support: Cross-seed SD: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. TaxEI seed=0 collapses to 46.8% while seeds 42/123 match vanilla at 61.7% — a 14.9pp swing within the same method. The variance gradient (no injection < random injection < taxonomy-guided injection) suggests that more structured perturbation amplifies training instability rather than providing useful curriculum signal. A single favorable seed can mask injection's destabilizing effect, making published single-seed results unreliable.

- **Claim 4**: Injection-trained models do not improve error recovery.
  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp).

- **Claim 5**: Detection training via error injection is completely ineffective in this setup.
  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random).

- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.
  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.

## Anticipated Reviewer Concerns

1. **"Statistical power with 3 seeds is limited."**
   → All three methods now have 3 seeds. TaxEI vs Vanilla: p≈0.32 (NS) — we do not claim a significant mean difference but instead emphasize the variance effect (SD 8.6pp vs 3.3pp, 2.6× ratio). TaxEI vs Random: paired t p≈0.034 (df=2, suggestive). We report all individual seed results transparently. The variance gradient (Vanilla < Random < TaxEI) is directionally consistent across all seeds.

2. **"ALFWorld has only 47 test tasks — too small for reliable conclusions."**
   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. We propose a second environment (WebShop) for supplementary validation.

3. **"Maybe the taxonomy itself is poorly designed."**
   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.

4. **"The training recipe might be suboptimal for injection data."**
   → The same recipe produces strong Vanilla results (65.3% vs 42.6% baseline, +22.7pp), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.

5. **"50% injection ratio is too high — you're drowning the signal."**
   → Comprehensively addressed with fixed-size dose-response ablation (all 4,358 total samples, seed=42). Results: 10% = 61.7% (0pp), 25% = 48.9% (-12.8pp), 50% = 51.1% (-10.6pp). The pattern is threshold-plateau, not linear: below ~15-20% injection is harmless but provides no benefit; above it, performance collapses and plateaus regardless of further injection increase. Even at the lowest tested ratio (10%), injection provides zero improvement over vanilla — the best case is exact parity. Random injection dose-response (in progress) will determine whether the threshold is specific to taxonomy-guided injection or a general property.

6. **"Why is detection rate 0%? Evaluation might be flawed."**
   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.

7. **"Why not compare directly on ToolBench?"**
   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.

## Key Differentiators vs PALADIN

PALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:

1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., "go to countertop 2" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.

2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.

3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making "what to do after an error" fundamentally harder to learn from examples.

4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.

**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.

## Note on v3→v4 Vanilla Discrepancy
v3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.

## Supplementary Experiments Needed

### Priority 1 (required for submission)
- ~~**More seeds**~~: ✅ DONE — All 3 methods at 3 seeds. Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.
- **Injection ratio ablation**: ✅ TaxEI dose-response done (10%=61.7%, 25%=48.9%, 50% in progress). Random dose-response in progress (10%, 25%, 50% training). Key finding: non-linear threshold between 10-25%.
- **Training dynamics analysis**: Plot training loss curves for clean vs. injected samples across epochs. Do injected samples have systematically higher loss? Does the model learn clean patterns before injection patterns corrupt them?

### Priority 2 (strengthens paper significantly)
- **Second environment**: WebShop or ScienceWorld to test whether the negative result generalizes beyond ALFWorld. If error injection also fails there, the boundary condition claim is stronger.
- **Qualitative failure analysis**: Manually examine 20+ TaxEI failure cases — does the model produce incoherent plans, or does it simply choose wrong actions at similar rates? This informs the "noise vs. wrong learning" distinction.

### Priority 3 (nice to have)
- **Scale ablation**: Does TaxEI improve if we scale to 25K or 50K trajectories (matching PALADIN's scale)?
- **Explicit recovery prompting**: Instead of SFT, test whether in-context recovery examples (few-shot) help — this isolates whether the issue is training signal vs. knowledge.
- **Per-operator deep dive**: Run more seeds on recovery eval to determine if C4 (observation masking) is genuinely easier for TaxEI or if the +9.1pp advantage is noise.


## registry (completed experiments)

- exp_id: traj_collect_500
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    successful_trajectories: 501
    failed_trajectories: 213
    total_attempts: 714
    success_rate: 0.702
    api_cost_usd: 8.86
    collection_time_sec: 5245
- exp_id: sft-dryrun-73
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss_init: 2.436
    train_loss_final: 1.543
    train_loss_avg: 1.894
    peak_memory_gib: 19.22
    steps: 8
    duration_sec: 42
    data_vanilla: 124
    data_injected_dryrun: 96
    injected_failed: 4
- exp_id: vanilla-react-baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_success_rate: 0.426
    total_tasks: 47
    successes: 20
    per_task_type:
      pick_heat_then_place:
        success: 5
        total: 8
        rate: 0.625
      look_at_obj_in_light:
        success: 3
        total: 6
        rate: 0.5
      pick_and_place_simple:
        success: 4
        total: 8
        rate: 0.5
      pick_clean_then_place:
        success: 5
        total: 11
        rate: 0.455
      pick_two_obj_and_place:
        success: 3
        total: 7
        rate: 0.429
      pick_cool_then_place:
        success: 0
        total: 7
        rate: 0
- exp_id: mini-pipeline-e2e
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: mini-taxei-sft
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.447
    eval_successes: 21
    eval_total: 47
    vs_baseline_pp: 2.1
    per_task:
      look_at_obj_in_light: 3/6 (50.0%)
      pick_and_place_simple: 2/8 (25.0%)
      pick_clean_then_place: 6/11 (54.5%)
      pick_cool_then_place: 1/7 (14.3%)
      pick_heat_then_place: 6/8 (75.0%)
      pick_two_obj_and_place: 3/7 (42.9%)
    train_steps: 195
    train_duration_min: 16.3
- exp_id: mini-vanilla-sft
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_success_rate: 0.149
    eval_successes: 7
    eval_total: 47
    vs_baseline_pp: -27.7
    per_task:
      look_at_obj_in_light: 0/6 (0%)
      pick_and_place_simple: 2/8 (25.0%)
      pick_clean_then_place: 2/11 (18.2%)
      pick_cool_then_place: 0/7 (0%)
      pick_heat_then_place: 3/8 (37.5%)
      pick_two_obj_and_place: 0/7 (0%)
    train_steps: 54
    train_duration_min: 5
- exp_id: vanilla_sft_aligned_v1
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: vanilla_sft_aligned_v2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: mini-vanilla-sft-v3
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    train_samples: 4176
    train_steps_total: 1566
    est_duration_min: 58
    format: aligned_single_turn
- exp_id: mini-taxei-sft-v3
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    train_samples: 7545
    train_samples_clean: 4176
    train_samples_injected: 3369
    train_steps_total: 2832
    est_duration_min: 90
    format: aligned_single_turn
- exp_id: mini-random-sft-v3
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    train_samples: 9076
    train_samples_clean: 4176
    train_samples_injected: 4900
    train_steps_total: 3405
    est_duration_min: 110
    format: aligned_single_turn
- exp_id: mini-vanilla-sft-v4
  name: ''
  status: PREPARING
  conclusion: success
  metrics: {}
- exp_id: v4-vanilla-sft
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: v3-vanilla-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    success_rate: 0.745
    successes: 35
    total: 47
    vs_baseline_pp: 31.9
    vs_baseline: 42.6% → 74.5%
- exp_id: v3-taxei-eval
  name: ''
  status: PREPARING
  conclusion: negative
  metrics:
    eval_success_rate: 0.66
    eval_successes: 31
    eval_total: 47
    vs_baseline_pp: 23.4
    vs_vanilla_sft_pp: -8.5
    per_task:
      look_at_obj_in_light: 5/6 (83.3%)
      pick_clean_then_place: 8/11 (72.7%)
      pick_heat_then_place: 6/8 (75.0%)
      pick_and_place_simple: 5/8 (62.5%)
      pick_two_obj_and_place: 4/7 (57.1%)
      pick_cool_then_place: 3/7 (42.9%)
- exp_id: v3-random-eval
  name: ''
  status: PREPARING
  conclusion: negative
  metrics:
    eval_success_rate: 0.511
    eval_successes: 24
    eval_total: 47
    vs_baseline_pp: 8.5
    vs_vanilla_sft_pp: -23.4
- exp_id: v4-taxei-sft
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: v4-random-sft
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: v4-taxei-sft-r2
  name: ''
  status: PREPARING
  conclusion: success
  metrics: {}
- exp_id: v4-random-sft-r2
  name: ''
  status: PREPARING
  conclusion: success
  metrics: {}
- exp_id: v4-taxei-sft-r3
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: v4-random-sft-r3
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: v4-vanilla-eval
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: v4-vanilla-eval-r2
  name: ''
  status: PREPARING
  conclusion: failed
  metrics: {}
- exp_id: v4-vanilla-eval-r3
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    eval_success_rate: 0.617
    eval_successes: 29
    eval_total: 47
    per_task:
      look_at_obj_in_light: 5/6 (83.3%)
      pick_heat_then_place: 6/8 (75.0%)
      pick_and_place_simple: 5/8 (62.5%)
      pick_cool_then_place: 4/7 (57.1%)
      pick_two_obj_and_place: 4/7 (57.1%)
      pick_clean_then_place: 5/11 (45.5%)
- exp_id: v4-taxei-eval
  name: ''
  status: PREPARING
  conclusion: negative
  metrics:
    eval_success_rate: 0.617
    eval_successes: 29
    eval_total: 47
    vs_vanilla_pp: 0
    vs_random_pp: -4.3
    mcnemar_vs_vanilla_p: 1
    mcnemar_vs_random_p: 0.754
    gate_3a: FAIL
    gate_3b: FAIL
    gate_4: PASS
    per_task:
      look_at_obj_in_light: 6/6 (100%)
      pick_and_place_simple: 5/8 (62.5%)
      pick_clean_then_place: 6/11 (54.5%)
      pick_cool_then_place: 3/7 (42.9%)
      pick_heat_then_place: 7/8 (87.5%)
      pick_two_obj_and_place: 2/7 (28.6%)
- exp_id: v4-random-eval
  name: ''
  status: PREPARING
  conclusion: negative
  metrics:
    eval_success_rate: 0.66
    eval_successes: 31
    eval_total: 47
    vs_vanilla_pp: 4.3
    vs_taxei_pp: 4.3
    mcnemar_vs_vanilla_p: 0.754
    per_task:
      look_at_obj_in_light: 6/6 (100%)
      pick_and_place_simple: 4/8 (50%)
      pick_clean_then_place: 6/11 (54.5%)
      pick_cool_then_place: 4/7 (57.1%)
      pick_heat_then_place: 7/8 (87.5%)
      pick_two_obj_and_place: 4/7 (57.1%)
- exp_id: v4-vanilla-seed0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.297
    avg_loss: 0.416
    token_accuracy: 0.902
    train_steps: 1635
    train_epochs: 3
    train_duration_min: 58
- exp_id: v4-taxei-seed0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.355
    token_accuracy: 0.917
    train_steps: 3387
    train_epochs: 3
    train_duration_min: 110
- exp_id: v4-random-seed0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.355
    token_accuracy: 0.912
    train_steps: 3387
    train_epochs: 3
    train_duration_min: 110
- exp_id: v4-recovery-eval-dev
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    pipeline_files:
    - eval/injected_eval.py
    - scripts/run_injected_eval.sh
    injected_eval_lines: 463
    dryrun_result: PASS
    dryrun_detail: vanilla checkpoint, 1 task, cuda:3, injected error recovered in
      13 steps
- exp_id: v4-vanilla-seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.288
    token_accuracy: 0.903
    train_steps: 1635
    train_epochs: 3
    train_duration_min: 58.9
- exp_id: v4-vanilla-seed7
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: v4-recovery-dryrun
  name: ''
  status: PREPARING
  conclusion: success
  metrics: {}
- exp_id: v4-vanilla-seed0-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.681
    eval_successes: 32
    eval_total: 47
    vs_seed42_pp: 6.4
    mcnemar_vs_seed42_p: 0.375
    discordant_pairs: 5
    per_task:
      look_at_obj_in_light: 5/6 (83.3%)
      pick_and_place_simple: 5/8 (62.5%)
      pick_clean_then_place: 6/11 (54.5%)
      pick_cool_then_place: 4/7 (57.1%)
      pick_heat_then_place: 7/8 (87.5%)
      pick_two_obj_and_place: 5/7 (71.4%)
- exp_id: v4-taxei-seed0-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.468
    eval_successes: 22
    eval_total: 47
    vs_seed42_pp: -14.9
- exp_id: v4-random-seed0-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.553
    eval_successes: 26
    eval_total: 47
    vs_seed42_pp: -10.7
- exp_id: v4-vanilla-seed123-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.66
    eval_successes: 31
    eval_total: 47
    vs_seed42_pp: 4.3
    vs_seed0_pp: -2.1
    per_task:
      look_at_obj_in_light:
        success: 5
        total: 6
        rate: 0.833
      pick_and_place_simple:
        success: 6
        total: 8
        rate: 0.75
      pick_clean_then_place_in_recep:
        success: 5
        total: 11
        rate: 0.455
      pick_cool_then_place_in_recep:
        success: 4
        total: 7
        rate: 0.571
      pick_heat_then_place_in_recep:
        success: 7
        total: 8
        rate: 0.875
      pick_two_obj_and_place:
        success: 4
        total: 7
        rate: 0.571
- exp_id: v4-vanilla-recovery-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.617
    successes: 29
    total: 47
    recovery_rate: 0.617
    detection_rate: 0
- exp_id: v4-taxei-recovery-eval
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    success_rate: 0.596
    successes: 28
    total: 47
    recovery_rate: 0.596
    detection_rate: 0
- exp_id: v4-random-recovery-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.638
    detection_rate: 0
    successes: 30
    total: 47
    source: json-file-verified
    note: r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism
- exp_id: v4-taxei-recovery-eval-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.596
    detection_rate: 0
    total_episodes: 47
    per_operator:
      C1_context_truncation:
        recovered: 8
        total: 12
        rate: 0.667
      C4_observation_masking:
        recovered: 7
        total: 11
        rate: 0.636
      P1_step_order_swap:
        recovered: 7
        total: 12
        rate: 0.583
      P2_sub_goal_deletion:
        recovered: 6
        total: 12
        rate: 0.5
- exp_id: v4-taxei-seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.35506879
    token_accuracy: 0.89978214
    train_steps: 3387
    train_epochs: 3
    train_duration_min: 109.2
    train_runtime_sec: 6549.432
    train_speed_s_per_it: 1.934
    memory_gib: 18.49
- exp_id: v4-random-seed123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.35484016
    final_loss: 0.16766574
    token_accuracy: 0.94187103
    avg_token_accuracy: 0.90849673
    train_steps: 3387
    train_epochs: 3
    train_runtime_sec: 6609.3556
    train_duration_min: 110.2
    train_samples_per_second: 4.098
    train_steps_per_second: 0.512
    train_speed_s_per_it: 1.951
    memory_gib: 18.49
- exp_id: v4-fixed-inject10
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: v4-fixed-inject25
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: v4-taxei-fixed-inject10
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.308
    token_accuracy: 0.888
    train_steps: 1635
    train_epochs: 3
    train_duration_min: 58
- exp_id: v4-taxei-fixed-inject25
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: v4-taxei-fixed-inject25-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.285
    token_accuracy: 0.893
    train_steps: 1635
    train_epochs: 3
    train_duration_min: 58
- exp_id: v4-taxei-seed123-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.617
    eval_successes: 29
    eval_total: 47
    by_task:
      look_at_obj_in_light:
        success: 5
        total: 6
        rate: 0.833
      pick_and_place_simple:
        success: 4
        total: 8
        rate: 0.5
      pick_clean_then_place_in_recep:
        success: 7
        total: 11
        rate: 0.636
      pick_cool_then_place_in_recep:
        success: 3
        total: 7
        rate: 0.429
      pick_heat_then_place_in_recep:
        success: 6
        total: 8
        rate: 0.75
      pick_two_obj_and_place:
        success: 4
        total: 7
        rate: 0.571
- exp_id: v4-taxei-fixed-inject10-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.617
    eval_successes: 29
    eval_total: 47
    by_task:
      look_at_obj_in_light:
        success: 5
        total: 6
        rate: 0.833
      pick_and_place_simple:
        success: 5
        total: 8
        rate: 0.625
      pick_clean_then_place_in_recep:
        success: 5
        total: 11
        rate: 0.455
      pick_cool_then_place_in_recep:
        success: 4
        total: 7
        rate: 0.571
      pick_heat_then_place_in_recep:
        success: 6
        total: 8
        rate: 0.75
      pick_two_obj_and_place:
        success: 4
        total: 7
        rate: 0.571
- exp_id: v4-taxei-fixed-inject25-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.489
    eval_successes: 23
    eval_total: 47
    by_task:
      look_at_obj_in_light:
        success: 4
        total: 6
        rate: 0.667
      pick_and_place_simple:
        success: 3
        total: 8
        rate: 0.375
      pick_clean_then_place_in_recep:
        success: 5
        total: 11
        rate: 0.455
      pick_cool_then_place_in_recep:
        success: 2
        total: 7
        rate: 0.286
      pick_heat_then_place_in_recep:
        success: 5
        total: 8
        rate: 0.625
      pick_two_obj_and_place:
        success: 4
        total: 7
        rate: 0.571
- exp_id: v4-random-seed123-eval
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_success_rate: 0.681
    eval_successes: 32
    eval_total: 47
    by_task:
      look_at_obj_in_light:
        total: 6
        success: 5
        rate: 0.833
      pick_and_place_simple:
        total: 8
        success: 5
        rate: 0.625
      pick_clean_then_place_in_recep:
        total: 11
        success: 7
        rate: 0.636
      pick_cool_then_place_in_recep:
        total: 7
        success: 4
        rate: 0.571
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 5
        rate: 0.714
- exp_id: v4-taxei-fixed-inject50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.259
    token_accuracy: 0.911
    train_steps: 1635
    train_epochs: 3
    train_duration_min: 53.1
- exp_id: v4-random-fixed-inject10
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4226
    final_step_loss: 0.3079
    token_accuracy: 0.9
    train_steps: 1635
    train_epochs: 3
    train_duration_min: 57
- exp_id: v4-random-fixed-inject25
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_steps: 1635
    train_epochs: 3
    data_count: 4358
- exp_id: v4-random-fixed-inject50
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_steps: 1635
    train_epochs: 3
    data_count: 4358
    train_loss: 0.4338
    final_step_loss: 0.2618
    token_accuracy: 0.91
    train_duration_min: 53.1
    memory_gib: 18
    train_speed_s_per_it: 1.95
- exp_id: v4-taxei-fixed-inject50-eval
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    eval_success_rate: 0.511
    eval_successes: 24
    eval_total: 47
    vs_vanilla_seed42_pp: -10.6
- exp_id: v4-random-fixed-inject10-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.681
    eval_successes: 32
    eval_total: 47
    by_task:
      look_at_obj_in_light:
        total: 6
        success: 5
        rate: 0.833
      pick_and_place_simple:
        total: 8
        success: 5
        rate: 0.625
      pick_clean_then_place_in_recep:
        total: 11
        success: 6
        rate: 0.545
      pick_cool_then_place_in_recep:
        total: 7
        success: 4
        rate: 0.571
      pick_heat_then_place_in_recep:
        total: 8
        success: 7
        rate: 0.875
      pick_two_obj_and_place:
        total: 7
        success: 5
        rate: 0.714
- exp_id: v4-random-fixed-inject50-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.574
    eval_successes: 27
    eval_total: 47
    vs_vanilla_seed42_pp: -4.3
    vs_taxei_50_pp: 6.3
- exp_id: v4-random-fixed-inject25-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.553
    eval_successes: 26
    eval_total: 47
    vs_vanilla_seed42_pp: -6.4
    vs_taxei_25_pp: 6.4

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
  "promptId": "80601043-98d5-481c-a1c8-48b07f117a46",
  "type": "user",
  "uuid": "a6d118a5-874d-41a8-89a5-dff3ca4a59a4",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:22:10.146Z_

```json
{
  "parentUuid": "a6d118a5-874d-41a8-89a5-dff3ca4a59a4",
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
  "uuid": "0dece5e6-65bf-413e-8534-d910ea7687f7",
  "timestamp": "2026-05-15T02:22:10.146Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:22:10.147Z_

```json
{
  "parentUuid": "0dece5e6-65bf-413e-8534-d910ea7687f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5a92520e-d68e-45f2-bd09-25b0f08efbc6",
  "timestamp": "2026-05-15T02:22:10.147Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：方差梯度和大方向成立，但剂量-响应的具体数字跨 seed 波动较大；taxonomy penalty 存在但不再'remarkably stable'；统计检验仍为 marginal 核心假设：['多 seed 剂量-响应显示 threshold-plateau 的大致形状但阈值位置在 10-30% 间漂…",
  "leafUuid": "5a92520e-d68e-45f2-bd09-25b0f08efbc6",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier error injection: stability, penalty, and dose-response dynamics",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---

### Assistant

_source line 8 · 2026-05-15T02:22:20.548Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to look at the experiment_plan file to find all planned experiments, then for each one, generate detailed predicted data under the "median" tier definition they've provided.

Let me first find and read the experiment_plan file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a92520e-d68e-45f2-bd09-25b0f08efbc6",
  "isSidechain": false,
  "requestId": "req_011Cb3ZHehKJfNs29JwewyDn",
  "type": "assistant",
  "uuid": "bd6753bc-7c57-4367-abba-bc8381f55af4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ppW25FSqs1fLeh78GFSwk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 173,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18431
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

_source line 9 · 2026-05-15T02:22:21.086Z_

Let me find the experiment plan file first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd6753bc-7c57-4367-abba-bc8381f55af4",
  "isSidechain": false,
  "requestId": "req_011Cb3ZHehKJfNs29JwewyDn",
  "type": "assistant",
  "uuid": "6759b0ae-b9e6-465b-8132-85b3473997d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ppW25FSqs1fLeh78GFSwk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 173,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18431
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

### Tool call

_source line 10 · 2026-05-15T02:22:24.548Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01TDuQwn34HRbsKCew4JPpHz`</summary>

```json
{
  "pattern": "**/*experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6759b0ae-b9e6-465b-8132-85b3473997d6",
  "isSidechain": false,
  "requestId": "req_011Cb3ZHehKJfNs29JwewyDn",
  "type": "assistant",
  "uuid": "d307ba98-9703-4711-9cd8-5da37db008b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ppW25FSqs1fLeh78GFSwk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 173,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18431
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

### Tool result

_source line 11 · 2026-05-15T02:22:24.624Z_

<details><summary>↩ Tool result · `toolu_01W67x7ez6e8DAkMsBJey4xe`</summary>

```text
projects/tax_error_inject_agent/artifacts/injection/planning.py
projects/tax_error_inject_agent/artifacts/injection/__pycache__/planning.cpython-314.pyc
projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml
projects/tax_error_inject_agent/logs/workers/worker_knowledge_write-experiment-plan_20260514T220305.log
projects/tax_error_inject_agent/logs/workers/worker_knowledge_write-experiment-plan_20260514T220305_result.json
projects/tax_error_inject_agent/writing_plan.yaml
projects/tax_error_inject_agent/logs/workers/worker_knowledge_experiment-plan_20260514T221342.log
projects/tax_error_inject_agent/logs/workers/worker_knowledge_experiment-plan_20260514T221342_result.json
projects/tax_error_inject_agent/logs/workers/worker_code_experiment-plan-yaml_20260515T015307.log
projects/tax_error_inject_agent/logs/workers/worker_code_experiment-plan-yaml_20260515T015307_result.json
projects/tax_error_inject_agent/experiment_plan.yaml
projects/tax_error_inject_agent/logs/workers/worker_knowledge_experiment-plan-yaml_20260515T015318.log
projects/tax_error_inject_agent/logs/workers/worker_knowledge_experiment-plan-yaml_20260515T015318_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dbc0018-ca63-4cd4-bf00-6f6a3bb9ddd8",
  "isSidechain": false,
  "promptId": "80601043-98d5-481c-a1c8-48b07f117a46",
  "type": "user",
  "uuid": "43fdb1dc-e076-47e0-ad58-0b5fd36cfa1a",
  "toolUseResult": {
    "filenames": [
      "projects/tax_error_inject_agent/artifacts/injection/planning.py",
      "projects/tax_error_inject_agent/artifacts/injection/__pycache__/planning.cpython-314.pyc",
      "projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml",
      "projects/tax_error_inject_agent/logs/workers/worker_knowledge_write-experiment-plan_20260514T220305.log",
      "projects/tax_error_inject_agent/logs/workers/worker_knowledge_write-experiment-plan_20260514T220305_result.json",
      "projects/tax_error_inject_agent/writing_plan.yaml",
      "projects/tax_error_inject_agent/logs/workers/worker_knowledge_experiment-plan_20260514T221342.log",
      "projects/tax_error_inject_agent/logs/workers/worker_knowledge_experiment-plan_20260514T221342_result.json",
      "projects/tax_error_inject_agent/logs/workers/worker_code_experiment-plan-yaml_20260515T015307.log",
      "projects/tax_error_inject_agent/logs/workers/worker_code_experiment-plan-yaml_20260515T015307_result.json",
      "projects/tax_error_inject_agent/experiment_plan.yaml",
      "projects/tax_error_inject_agent/logs/workers/worker_knowledge_experiment-plan-yaml_20260515T015318.log",
      "projects/tax_error_inject_agent/logs/workers/worker_knowledge_experiment-plan-yaml_20260515T015318_result.json"
    ],
    "durationMs": 6,
    "numFiles": 13,
    "truncated": false
  },
  "sourceToolAssistantUUID": "5dbc0018-ca63-4cd4-bf00-6f6a3bb9ddd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T02:22:24.568Z_

<details><summary>↩ Tool result · `toolu_01TDuQwn34HRbsKCew4JPpHz`</summary>

```text
projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml
projects/tax_error_inject_agent/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d307ba98-9703-4711-9cd8-5da37db008b3",
  "isSidechain": false,
  "promptId": "80601043-98d5-481c-a1c8-48b07f117a46",
  "type": "user",
  "uuid": "aa673c33-0fba-46e0-a219-845a54bf6d04",
  "toolUseResult": {
    "filenames": [
      "projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml",
      "projects/tax_error_inject_agent/experiment_plan.yaml"
    ],
    "durationMs": 14,
    "numFiles": 2,
    "truncated": false
  },
  "sourceToolAssistantUUID": "d307ba98-9703-4711-9cd8-5da37db008b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T02:22:24.615Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01W67x7ez6e8DAkMsBJey4xe`</summary>

```json
{
  "pattern": "**/*plan*.*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa673c33-0fba-46e0-a219-845a54bf6d04",
  "isSidechain": false,
  "requestId": "req_011Cb3ZHehKJfNs29JwewyDn",
  "type": "assistant",
  "uuid": "5dbc0018-ca63-4cd4-bf00-6f6a3bb9ddd8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ppW25FSqs1fLeh78GFSwk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18431,
      "cache_read_input_tokens": 11841,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18431,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 173,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18431,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18431
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

### Tool call

_source line 14 · 2026-05-15T02:22:28.246Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QQT8HVhfcSexnPLFvtHrbd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43fdb1dc-e076-47e0-ad58-0b5fd36cfa1a",
  "isSidechain": false,
  "requestId": "req_011Cb3ZJifxajFKAq8VWLmwR",
  "type": "assistant",
  "uuid": "de23b4f6-0045-48f0-99d6-dfa9a9042c17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GA55o1bo4R1uY2DEMBqChc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 639,
      "cache_read_input_tokens": 30272,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 639,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 30272,
          "cache_creation_input_tokens": 639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 639
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

### Tool result

_source line 15 · 2026-05-15T02:22:28.257Z_

<details><summary>↩ Tool result · `toolu_01QQT8HVhfcSexnPLFvtHrbd`</summary>

```text
1	# experiment_plan.yaml — tax_error_inject_agent (Negative Result Paper)
2	# Updated: 2026-05-15
3	#
4	# Claims (from paper_framing.md):
5	#   C1: TaxEI introduces high variance, fails to improve clean performance
6	#   C2: Taxonomy labels provide no benefit over random injection
7	#   C3: Error injection increases training instability (variance gradient + dose-response)
8	#   C4: Injection-trained models do not improve error recovery
9	#   C5: Detection training via error injection is completely ineffective
10	#   C6: Divergence from PALADIN reveals task-structural boundary conditions
11	
12	experiments:
13	
14	  # ============================================================
15	  # Baselines & Prerequisites
16	  # ============================================================
17	  - plan_id: "baseline"
18	    description: "Qwen3-8B zero-shot ReAct baseline on ALFWorld (47 tasks)"
19	    claim: "context"
20	    priority: 0
21	    status: done
22	    registry_ids:
23	      - vanilla-react-baseline
24	    depends_on: []
25	    results:
26	      accuracy: "42.6% (20/47)"
27	
28	  - plan_id: "data-collection"
29	    description: "GPT-5.2 trajectory collection for SFT training data"
30	    claim: "prerequisite"
31	    priority: 0
32	    status: done
33	    registry_ids:
34	      - traj_collect_500
35	    depends_on: []
36	    results:
37	      success_rate: "70.2% (501/714)"
38	      cost: "$8.86"
39	
40	  # ============================================================
41	  # v3 Pilot (format-aligned, superseded by v4)
42	  # ============================================================
43	  - plan_id: "v3-pilot"
44	    description: "v3 format-aligned pilot: vanilla/TaxEI/random single-seed eval"
45	    claim: "supplement"
46	    priority: 0
47	    status: done
48	    registry_ids:
49	      - mini-vanilla-sft-v3
50	      - mini-taxei-sft-v3
51	      - mini-random-sft-v3
52	      - v3-vanilla-eval
53	      - v3-taxei-eval
54	      - v3-random-eval
55	    depends_on:
56	      - data-collection
57	    results:
58	      vanilla: "74.5%"
59	      taxei: "66.0%"
60	      random: "51.1%"
61	    notes: "Superseded by v4. Vanilla 74.5% vs v4 65.3% discrepancy noted in paper supplement."
62	
63	  # ============================================================
64	  # Core Multi-Seed Experiments (v4) — Priority 1
65	  # ============================================================
66	  - plan_id: "multiseed-vanilla"
67	    description: "Vanilla SFT 3-seed verification (clean data only, 4,358 samples)"
68	    claim: "C1"
69	    priority: 1
70	    status: done
71	    registry_ids:
72	      - mini-vanilla-sft-v4       # train seed=42
73	      - v4-vanilla-seed0          # train seed=0
74	      - v4-vanilla-seed123        # train seed=123
75	      - v4-vanilla-eval-r3        # eval seed=42 → 61.7%
76	      - v4-vanilla-seed0-eval     # eval seed=0  → 68.1%
77	      - v4-vanilla-seed123-eval   # eval seed=123 → 66.0%
78	    depends_on:
79	      - data-collection
80	    results:
81	      seed42: "61.7%"
82	      seed0: "68.1%"
83	      seed123: "66.0%"
84	      mean_sd: "65.3% ± 3.3pp"
85	
86	  - plan_id: "multiseed-taxei"
87	    description: "TaxEI SFT 3-seed verification (clean + taxonomy-tagged injections, 9,029 samples)"
88	    claim: "C1,C2,C3"
89	    priority: 1
90	    status: done
91	    registry_ids:
92	      - v4-taxei-sft-r2           # train seed=42
93	      - v4-taxei-seed0            # train seed=0
94	      - v4-taxei-seed123          # train seed=123
95	      - v4-taxei-eval             # eval seed=42 → 61.7%
96	      - v4-taxei-seed0-eval       # eval seed=0  → 46.8%
97	      - v4-taxei-seed123-eval     # eval seed=123 → 61.7%
98	    depends_on:
99	      - data-collection
100	    results:
101	      seed42: "61.7%"
102	      seed0: "46.8%"
103	      seed123: "61.7%"
104	      mean_sd: "56.7% ± 8.6pp"
105	      vs_vanilla_paired_t_p: "0.32 (NS)"
106	      vs_vanilla_pooled_p: "0.054 (NS at α=0.05)"
107	
108	  - plan_id: "multiseed-random"
109	    description: "Random SFT 3-seed verification (clean + unlabeled injections, 9,029 samples)"
110	    claim: "C2,C3"
111	    priority: 1
112	    status: done
113	    registry_ids:
114	      - v4-random-sft-r2          # train seed=42
115	      - v4-random-seed0           # train seed=0
116	      - v4-random-seed123         # train seed=123
117	      - v4-random-eval            # eval seed=42 → 66.0%
118	      - v4-random-seed0-eval      # eval seed=0  → 55.3%
119	      - v4-random-seed123-eval    # eval seed=123 → 68.1%
120	    depends_on:
121	      - data-collection
122	    results:
123	      seed42: "66.0%"
124	      seed0: "55.3%"
125	      seed123: "68.1%"
126	      mean_sd: "63.1% ± 7.0pp"
127	      vs_taxei_paired_t_p: "0.034 (suggestive, df=2)"
128	      vs_taxei_pooled_p: "0.170 (NS)"
129	
130	  # ============================================================
131	  # Dose-Response Ablation — Priority 1
132	  # ============================================================
133	  - plan_id: "dose-response-taxei"
134	    description: "TaxEI dose-response curve (10%/25%/50% injection, fixed 4,358 total, seed=42)"
135	    claim: "C3"
136	    priority: 1
137	    status: done
138	    registry_ids:
139	      - v4-taxei-fixed-inject10       # train 10%
140	      - v4-taxei-fixed-inject25-r2    # train 25% (r2 after OOM)
141	      - v4-taxei-fixed-inject50       # train 50%
142	      - v4-taxei-fixed-inject10-eval  # eval 10% → 61.7%
143	      - v4-taxei-fixed-inject25-eval  # eval 25% → 48.9%
144	      - v4-taxei-fixed-inject50-eval  # eval 50% → 51.1%
145	    depends_on:
146	      - multiseed-vanilla
147	    results:
148	      inject0_baseline: "61.7% (vanilla seed=42)"
149	      inject10: "61.7% (0pp)"
150	      inject25: "48.9% (-12.8pp)"
151	      inject50: "51.1% (-10.6pp)"
152	      pattern: "threshold-plateau: 10% harmless, 25% catastrophic collapse, 50% no further worsening"
153	
154	  - plan_id: "dose-response-random"
155	    description: "Random dose-response curve (10%/25%/50% injection, fixed 4,358 total, seed=42)"
156	    claim: "C3"
157	    priority: 1
158	    status: in_progress
159	    registry_ids:
160	      - v4-random-fixed-inject10       # train 10%
161	      - v4-random-fixed-inject25       # train 25%
162	      - v4-random-fixed-inject50       # train 50%
163	      - v4-random-fixed-inject10-eval  # eval 10% → 68.1%
164	      - v4-random-fixed-inject25-eval  # eval 25% → RUNNING
165	      - v4-random-fixed-inject50-eval  # eval 50% → RUNNING
166	    depends_on:
167	      - multiseed-vanilla
168	    results:
169	      inject0_baseline: "61.7% (vanilla seed=42)"
170	      inject10: "68.1% (+6.4pp, data augmentation effect)"
171	      inject25: "eval in progress (cuda:0)"
172	      inject50: "eval in progress (cuda:3)"
173	    notes: "Random 10% positive effect contrasts with TaxEI 10% zero effect — taxonomy may limit error diversity at low ratios"
174	
175	  # ============================================================
176	  # Recovery & Detection Eval — Priority 1
177	  # ============================================================
178	  - plan_id: "recovery-eval"
179	    description: "Recovery rate under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)"
180	    claim: "C4,C5"
181	    priority: 1
182	    status: done
183	    registry_ids:
184	      - v4-vanilla-recovery-eval       # vanilla → 61.7% recovery, 0% detection
185	      - v4-taxei-recovery-eval         # taxei r1 (process died 5x)
186	      - v4-taxei-recovery-eval-r2      # taxei r2 → 59.6% recovery, 0% detection
187	      - v4-random-recovery-eval        # random → 63.8% recovery, 0% detection
188	    depends_on:
189	      - multiseed-vanilla
190	      - multiseed-taxei
191	      - multiseed-random
192	    results:
193	      vanilla_recovery: "61.7%"
194	      taxei_recovery: "59.6%"
195	      random_recovery: "63.8%"
196	      detection_rate: "0% (all methods)"
197	      taxei_per_operator: "C1=66.7%, C4=63.6%, P1=58.3%, P2=50.0%"
198	
199	  # ============================================================
200	  # Priority 2 — Strengthens Paper Significantly
201	  # ============================================================
202	  - plan_id: "training-dynamics"
203	    description: "Training loss curve analysis: clean vs injected samples across epochs"
204	    claim: "C3"
205	    priority: 2
206	    status: planned
207	    registry_ids: []
208	    depends_on:
209	      - multiseed-taxei
210	      - multiseed-random
211	    notes: "Plot loss curves to show whether injected samples corrupt clean learning signal"
212	
213	  - plan_id: "second-environment"
214	    description: "WebShop or ScienceWorld replication to test generalization beyond ALFWorld"
215	    claim: "C6"
216	    priority: 2
217	    status: planned
218	    registry_ids: []
219	    depends_on:
220	      - dose-response-random
221	    notes: "Strengthens boundary condition claim if error injection also fails in second environment"
222	
223	  - plan_id: "qualitative-failure-analysis"
224	    description: "Manual examination of 20+ TaxEI failure cases: incoherent plans vs wrong actions"
225	    claim: "C1,C6"
226	    priority: 2
227	    status: planned
228	    registry_ids: []
229	    depends_on:
230	      - multiseed-taxei
231	    notes: "Informs noise-vs-wrong-learning distinction"
232	
233	  # ============================================================
234	  # Priority 3 — Nice-to-Have
235	  # ============================================================
236	  - plan_id: "scale-ablation"
237	    description: "Scale to 25K-50K trajectories to match PALADIN's data scale"
238	    claim: "C6"
239	    priority: 3
240	    status: planned
241	    registry_ids: []
242	    depends_on:
243	      - dose-response-random
244	
245	  - plan_id: "recovery-prompting"
246	    description: "In-context recovery examples (few-shot) to isolate training signal vs knowledge"
247	    claim: "C6"
248	    priority: 3
249	    status: planned
250	    registry_ids: []
251	    depends_on:
252	      - recovery-eval
253	
254	  - plan_id: "per-operator-deepdive"
255	    description: "Multi-seed recovery eval to validate per-operator patterns (esp. C4 +9.1pp)"
256	    claim: "C4"
257	    priority: 3
258	    status: planned
259	    registry_ids: []
260	    depends_on:
261	      - recovery-eval
262	
263	# ============================================================
264	# Failed/Killed Registry Entries (not part of active plan)
265	# ============================================================
266	# Retries, OOM failures, or superseded entries retained for provenance:
267	#   - v4-vanilla-sft (OOM), v4-taxei-sft (failed), v4-random-sft (failed)
268	#   - v4-vanilla-eval (failed), v4-vanilla-eval-r2 (failed)
269	#   - v4-taxei-sft-r3, v4-random-sft-r3 (retries)
270	#   - v4-taxei-fixed-inject25 (OOM, replaced by r2)
271	#   - v4-fixed-inject10, v4-fixed-inject25 (killed duplicates)
272	#   - v4-vanilla-seed7 (killed)
273	#   - v4-recovery-eval-dev, v4-recovery-dryrun (pipeline dev)
274	#   - mini-vanilla-sft (278-sample pilot, 14.9%)
275	#   - mini-taxei-sft (278-sample pilot, 44.7%)
276	#   - mini-pipeline-e2e (failed), sft-dryrun-73 (dryrun)
277	#   - vanilla_sft_aligned_v1, vanilla_sft_aligned_v2 (unfinished)
278	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de23b4f6-0045-48f0-99d6-dfa9a9042c17",
  "isSidechain": false,
  "promptId": "80601043-98d5-481c-a1c8-48b07f117a46",
  "type": "user",
  "uuid": "7987ba19-9b95-473e-8e8a-1507ef3a47e3",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/experiment_plan.yaml",
      "content": "# experiment_plan.yaml — tax_error_inject_agent (Negative Result Paper)\n# Updated: 2026-05-15\n#\n# Claims (from paper_framing.md):\n#   C1: TaxEI introduces high variance, fails to improve clean performance\n#   C2: Taxonomy labels provide no benefit over random injection\n#   C3: Error injection increases training instability (variance gradient + dose-response)\n#   C4: Injection-trained models do not improve error recovery\n#   C5: Detection training via error injection is completely ineffective\n#   C6: Divergence from PALADIN reveals task-structural boundary conditions\n\nexperiments:\n\n  # ============================================================\n  # Baselines & Prerequisites\n  # ============================================================\n  - plan_id: \"baseline\"\n    description: \"Qwen3-8B zero-shot ReAct baseline on ALFWorld (47 tasks)\"\n    claim: \"context\"\n    priority: 0\n    status: done\n    registry_ids:\n      - vanilla-react-baseline\n    depends_on: []\n    results:\n      accuracy: \"42.6% (20/47)\"\n\n  - plan_id: \"data-collection\"\n    description: \"GPT-5.2 trajectory collection for SFT training data\"\n    claim: \"prerequisite\"\n    priority: 0\n    status: done\n    registry_ids:\n      - traj_collect_500\n    depends_on: []\n    results:\n      success_rate: \"70.2% (501/714)\"\n      cost: \"$8.86\"\n\n  # ============================================================\n  # v3 Pilot (format-aligned, superseded by v4)\n  # ============================================================\n  - plan_id: \"v3-pilot\"\n    description: \"v3 format-aligned pilot: vanilla/TaxEI/random single-seed eval\"\n    claim: \"supplement\"\n    priority: 0\n    status: done\n    registry_ids:\n      - mini-vanilla-sft-v3\n      - mini-taxei-sft-v3\n      - mini-random-sft-v3\n      - v3-vanilla-eval\n      - v3-taxei-eval\n      - v3-random-eval\n    depends_on:\n      - data-collection\n    results:\n      vanilla: \"74.5%\"\n      taxei: \"66.0%\"\n      random: \"51.1%\"\n    notes: \"Superseded by v4. Vanilla 74.5% vs v4 65.3% discrepancy noted in paper supplement.\"\n\n  # ============================================================\n  # Core Multi-Seed Experiments (v4) — Priority 1\n  # ============================================================\n  - plan_id: \"multiseed-vanilla\"\n    description: \"Vanilla SFT 3-seed verification (clean data only, 4,358 samples)\"\n    claim: \"C1\"\n    priority: 1\n    status: done\n    registry_ids:\n      - mini-vanilla-sft-v4       # train seed=42\n      - v4-vanilla-seed0          # train seed=0\n      - v4-vanilla-seed123        # train seed=123\n      - v4-vanilla-eval-r3        # eval seed=42 → 61.7%\n      - v4-vanilla-seed0-eval     # eval seed=0  → 68.1%\n      - v4-vanilla-seed123-eval   # eval seed=123 → 66.0%\n    depends_on:\n      - data-collection\n    results:\n      seed42: \"61.7%\"\n      seed0: \"68.1%\"\n      seed123: \"66.0%\"\n      mean_sd: \"65.3% ± 3.3pp\"\n\n  - plan_id: \"multiseed-taxei\"\n    description: \"TaxEI SFT 3-seed verification (clean + taxonomy-tagged injections, 9,029 samples)\"\n    claim: \"C1,C2,C3\"\n    priority: 1\n    status: done\n    registry_ids:\n      - v4-taxei-sft-r2           # train seed=42\n      - v4-taxei-seed0            # train seed=0\n      - v4-taxei-seed123          # train seed=123\n      - v4-taxei-eval             # eval seed=42 → 61.7%\n      - v4-taxei-seed0-eval       # eval seed=0  → 46.8%\n      - v4-taxei-seed123-eval     # eval seed=123 → 61.7%\n    depends_on:\n      - data-collection\n    results:\n      seed42: \"61.7%\"\n      seed0: \"46.8%\"\n      seed123: \"61.7%\"\n      mean_sd: \"56.7% ± 8.6pp\"\n      vs_vanilla_paired_t_p: \"0.32 (NS)\"\n      vs_vanilla_pooled_p: \"0.054 (NS at α=0.05)\"\n\n  - plan_id: \"multiseed-random\"\n    description: \"Random SFT 3-seed verification (clean + unlabeled injections, 9,029 samples)\"\n    claim: \"C2,C3\"\n    priority: 1\n    status: done\n    registry_ids:\n      - v4-random-sft-r2          # train seed=42\n      - v4-random-seed0           # train seed=0\n      - v4-random-seed123         # train seed=123\n      - v4-random-eval            # eval seed=42 → 66.0%\n      - v4-random-seed0-eval      # eval seed=0  → 55.3%\n      - v4-random-seed123-eval    # eval seed=123 → 68.1%\n    depends_on:\n      - data-collection\n    results:\n      seed42: \"66.0%\"\n      seed0: \"55.3%\"\n      seed123: \"68.1%\"\n      mean_sd: \"63.1% ± 7.0pp\"\n      vs_taxei_paired_t_p: \"0.034 (suggestive, df=2)\"\n      vs_taxei_pooled_p: \"0.170 (NS)\"\n\n  # ============================================================\n  # Dose-Response Ablation — Priority 1\n  # ============================================================\n  - plan_id: \"dose-response-taxei\"\n    description: \"TaxEI dose-response curve (10%/25%/50% injection, fixed 4,358 total, seed=42)\"\n    claim: \"C3\"\n    priority: 1\n    status: done\n    registry_ids:\n      - v4-taxei-fixed-inject10       # train 10%\n      - v4-taxei-fixed-inject25-r2    # train 25% (r2 after OOM)\n      - v4-taxei-fixed-inject50       # train 50%\n      - v4-taxei-fixed-inject10-eval  # eval 10% → 61.7%\n      - v4-taxei-fixed-inject25-eval  # eval 25% → 48.9%\n      - v4-taxei-fixed-inject50-eval  # eval 50% → 51.1%\n    depends_on:\n      - multiseed-vanilla\n    results:\n      inject0_baseline: \"61.7% (vanilla seed=42)\"\n      inject10: \"61.7% (0pp)\"\n      inject25: \"48.9% (-12.8pp)\"\n      inject50: \"51.1% (-10.6pp)\"\n      pattern: \"threshold-plateau: 10% harmless, 25% catastrophic collapse, 50% no further worsening\"\n\n  - plan_id: \"dose-response-random\"\n    description: \"Random dose-response curve (10%/25%/50% injection, fixed 4,358 total, seed=42)\"\n    claim: \"C3\"\n    priority: 1\n    status: in_progress\n    registry_ids:\n      - v4-random-fixed-inject10       # train 10%\n      - v4-random-fixed-inject25       # train 25%\n      - v4-random-fixed-inject50       # train 50%\n      - v4-random-fixed-inject10-eval  # eval 10% → 68.1%\n      - v4-random-fixed-inject25-eval  # eval 25% → RUNNING\n      - v4-random-fixed-inject50-eval  # eval 50% → RUNNING\n    depends_on:\n      - multiseed-vanilla\n    results:\n      inject0_baseline: \"61.7% (vanilla seed=42)\"\n      inject10: \"68.1% (+6.4pp, data augmentation effect)\"\n      inject25: \"eval in progress (cuda:0)\"\n      inject50: \"eval in progress (cuda:3)\"\n    notes: \"Random 10% positive effect contrasts with TaxEI 10% zero effect — taxonomy may limit error diversity at low ratios\"\n\n  # ============================================================\n  # Recovery & Detection Eval — Priority 1\n  # ============================================================\n  - plan_id: \"recovery-eval\"\n    description: \"Recovery rate under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)\"\n    claim: \"C4,C5\"\n    priority: 1\n    status: done\n    registry_ids:\n      - v4-vanilla-recovery-eval       # vanilla → 61.7% recovery, 0% detection\n      - v4-taxei-recovery-eval         # taxei r1 (process died 5x)\n      - v4-taxei-recovery-eval-r2      # taxei r2 → 59.6% recovery, 0% detection\n      - v4-random-recovery-eval        # random → 63.8% recovery, 0% detection\n    depends_on:\n      - multiseed-vanilla\n      - multiseed-taxei\n      - multiseed-random\n    results:\n      vanilla_recovery: \"61.7%\"\n      taxei_recovery: \"59.6%\"\n      random_recovery: \"63.8%\"\n      detection_rate: \"0% (all methods)\"\n      taxei_per_operator: \"C1=66.7%, C4=63.6%, P1=58.3%, P2=50.0%\"\n\n  # ============================================================\n  # Priority 2 — Strengthens Paper Significantly\n  # ============================================================\n  - plan_id: \"training-dynamics\"\n    description: \"Training loss curve analysis: clean vs injected samples across epochs\"\n    claim: \"C3\"\n    priority: 2\n    status: planned\n    registry_ids: []\n    depends_on:\n      - multiseed-taxei\n      - multiseed-random\n    notes: \"Plot loss curves to show whether injected samples corrupt clean learning signal\"\n\n  - plan_id: \"second-environment\"\n    description: \"WebShop or ScienceWorld replication to test generalization beyond ALFWorld\"\n    claim: \"C6\"\n    priority: 2\n    status: planned\n    registry_ids: []\n    depends_on:\n      - dose-response-random\n    notes: \"Strengthens boundary condition claim if error injection also fails in second environment\"\n\n  - plan_id: \"qualitative-failure-analysis\"\n    description: \"Manual examination of 20+ TaxEI failure cases: incoherent plans vs wrong actions\"\n    claim: \"C1,C6\"\n    priority: 2\n    status: planned\n    registry_ids: []\n    depends_on:\n      - multiseed-taxei\n    notes: \"Informs noise-vs-wrong-learning distinction\"\n\n  # ============================================================\n  # Priority 3 — Nice-to-Have\n  # ============================================================\n  - plan_id: \"scale-ablation\"\n    description: \"Scale to 25K-50K trajectories to match PALADIN's data scale\"\n    claim: \"C6\"\n    priority: 3\n    status: planned\n    registry_ids: []\n    depends_on:\n      - dose-response-random\n\n  - plan_id: \"recovery-prompting\"\n    description: \"In-context recovery examples (few-shot) to isolate training signal vs knowledge\"\n    claim: \"C6\"\n    priority: 3\n    status: planned\n    registry_ids: []\n    depends_on:\n      - recovery-eval\n\n  - plan_id: \"per-operator-deepdive\"\n    description: \"Multi-seed recovery eval to validate per-operator patterns (esp. C4 +9.1pp)\"\n    claim: \"C4\"\n    priority: 3\n    status: planned\n    registry_ids: []\n    depends_on:\n      - recovery-eval\n\n# ============================================================\n# Failed/Killed Registry Entries (not part of active plan)\n# ============================================================\n# Retries, OOM failures, or superseded entries retained for provenance:\n#   - v4-vanilla-sft (OOM), v4-taxei-sft (failed), v4-random-sft (failed)\n#   - v4-vanilla-eval (failed), v4-vanilla-eval-r2 (failed)\n#   - v4-taxei-sft-r3, v4-random-sft-r3 (retries)\n#   - v4-taxei-fixed-inject25 (OOM, replaced by r2)\n#   - v4-fixed-inject10, v4-fixed-inject25 (killed duplicates)\n#   - v4-vanilla-seed7 (killed)\n#   - v4-recovery-eval-dev, v4-recovery-dryrun (pipeline dev)\n#   - mini-vanilla-sft (278-sample pilot, 14.9%)\n#   - mini-taxei-sft (278-sample pilot, 44.7%)\n#   - mini-pipeline-e2e (failed), sft-dryrun-73 (dryrun)\n#   - vanilla_sft_aligned_v1, vanilla_sft_aligned_v2 (unfinished)\n",
      "numLines": 278,
      "startLine": 1,
      "totalLines": 278
    }
  },
  "sourceToolAssistantUUID": "de23b4f6-0045-48f0-99d6-dfa9a9042c17",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16 · 2026-05-15T02:22:28.344Z_

````json
{
  "parentUuid": "7987ba19-9b95-473e-8e8a-1507ef3a47e3",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**tax_error_inject_agent**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"tax_error_inject_agent\")` 或 `load_project_config(\"tax_error_inject_agent\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——reliability diagrams、ECE heatmap、T* scatter plot、模型对比图，直接在 A6000 服务器上执行，输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成发表级学术统计图——LLM 写 matplotlib 代码 + Critic 迭代 3 轮，输入 CSV/JSON 数据 + 意图描述即可。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/tax_error_inject_agent/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "b12ff710-07ce-41b0-966c-392c651a4fea",
  "timestamp": "2026-05-15T02:22:28.344Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：方差梯度和大方向成立，但剂量-响应的具体数字跨 seed 波动较大；taxonomy penalty 存在但不再'remarkably stable'；统计检验仍为 marginal 核心假设：['多 seed 剂量-响应显示 threshold-plateau 的大致形状但阈值位置在 10-30% 间漂…",
  "leafUuid": "b12ff710-07ce-41b0-966c-392c651a4fea",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier error injection: stability, penalty, and dose-response dynamics",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---

### Assistant

_source line 19 · 2026-05-15T02:24:43.509Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the experiment plan. I need to identify all experiments with `status: planned` and generate detailed predicted data for each under the "median" tier. Let me list them:

1. **training-dynamics** (plan_id: "training-dynamics", priority 2, planned)
2. **second-environment** (plan_id: "second-environment", priority 2, planned)
3. **qualitative-failure-analysis** (plan_id: "qualitative-failure-analysis", priority 2, planned)
4. **scale-ablation** (plan_id: "scale-ablation", priority 3, planned)


5. **recovery-prompting** (plan_id: "recovery-prompting", priority 3, planned)
6. **per-operator-deepdive** (plan_id: "per-operator-deepdive", priority 3, planned)

There's also the in-progress experiment **dose-response-random** at priority 1 that's 10% done with 25% and 50% evals running, so I'll need to generate predictions for its remaining results as well. Now I'm constructing the detailed predictions for each planned experiment under the median tier.

For the median tier, I'm thinking about what the core characteristics would look like: the variance gradient direction generally holds but individual seeds sometimes break the Random < TaxEI ordering, the taxonomy penalty is directional around 5-7pp on average but varies 3-9pp depending on the dose point, dose-response follows a rough threshold-plateau shape with the threshold drifting 10-30%, pooled p stays between 0.05-0.15, and training loss shows injected samples higher while clean corruption effects aren't clearly visible. Starting with dose-response-random, I expect the shared 12.8pp drop from the TaxEI curve won't replicate exactly under median conditions, so with Random at 10% = 68.1%, the drop from 10% to 25% should be smaller than the TaxEI baseline.

Looking at the existing dose-response results in the paper, I can see the actual values already documented across the dose points, which gives me concrete reference points for what median tier predictions should anchor to. I'm checking the experiment plan against the registry results — some experiments marked as "in_progress" already have completed data, so I should focus on the ones explicitly marked as "planned". Looking at the plan, there are six planned experiments across priority levels 2 and 3: training-dynamics, second-environment, qualitative-failure-analysis, scale-ablation, recovery-prompting, and per-operator-deepdive. I need to generate predicted data for each of these.

Now I'm starting to construct the detailed predictions, beginning with training-dynamics, which will show training loss curves comparing clean versus injected samples across different epochs.

For the training-dynamics experiment, the median-tier prediction is that injected samples consistently show higher loss than clean samples early on (around 0.15-0.3 higher at epoch 1), though this gap gradually shrinks as training progresses without fully disappearing. The clean samples in TaxEI and Random setups have slightly elevated loss compared to Vanilla clean samples, but the difference is subtle and noisy—suggesting the corruption effect on clean data exists but isn't clearly distinguishable from normal training variance. Across different seeds, the loss trajectories follow similar patterns though convergence speed varies.

For the second-environment experiment on WebShop, I'm predicting that error injection will also underperform there, though the effect should be weaker than what we see in ALFWorld, with TaxEI showing only marginal improvements.

Now I'm looking at the qualitative failure analysis, examining around 20+ cases where TaxEI failed to understand what's actually going wrong.

The failures split into three categories: roughly half show the model generating incoherent plans that suggest noise corruption, another third display coherent but incorrect action choices indicating the model learned the wrong thing, and the remainder are ambiguous. What's interesting is that both mechanisms seem to be operating simultaneously—some failures reveal recovery behaviors the model picked up from training but applies in the wrong contexts, while others mirror the exact step-ordering errors I injected, suggesting the model absorbed those patterns directly.

For the scale ablation, I'm seeing that at 25K trajectories TaxEI performs slightly better than vanilla but with higher variance, and the trend continues improving at 50K with variance narrowing further.

However, even at 50K trajectories TaxEI still underperforms vanilla, which tells me scale helps but doesn't resolve the underlying structural mismatch. The improvement trajectory does partially support the PALADIN comparison though.

When I test recovery prompting with few-shot examples at inference time, I get modest gains of 3-6 percentage points over vanilla zero-shot on recovery tasks, nowhere near PALADIN's 30 percentage point retrieval boost. This actually confirms the recovery knowledge is there—the bottleneck is in how the SFT training signal shapes it. Combining TaxEI with few-shot recovery shows some complementarity but not enough to reach significance.

Looking at the per-operator analysis with multiple seeds, the C4 advantage appears partially real but smaller than initially thought. I'm clarifying what the user meant by "planned" — they want detailed predictions for experiments with `status: planned`, not the ones already completed. Since dose-response-random already has results in the registry, I'll focus on the 6 truly planned experiments and generate predictions using the median tier parameters as constraints, particularly the taxei performance ranges and standard deviations.

Now I'm working through the specific parameter ranges for the dose-response predictions — the taxonomy penalty effects across different doses, the variability in those penalties, the threshold drop magnitude, and the statistical significance levels I'd expect to see across the seed replicates.

I need to construct predictions for the six planned experiments in YAML format, making sure each one aligns with these median-tier expectations. Let me think through what the results tables and figure descriptions should look like for each experiment, starting with the training dynamics one.

For training-dynamics, I'm expecting loss curves that show TaxEI training starting around 0.45 and dropping to 0.30 by epoch 3, while injected samples stay consistently higher. The clean sample performance between TaxEI and vanilla training should be nearly identical with only marginal differences. I'll need a loss decomposition table broken down by epoch and sample type, plus training curves faceted by method.

Now moving to the WebShop environment setup with its 12K product catalog as the baseline configuration. The variance pattern holds across the board, with TaxEI showing roughly double the standard deviation of vanilla SFT. The taxonomy penalty lands around 2-4 percentage points—smaller than what we saw in ALFWorld since WebShop's errors tend to be more observable. Statistical significance is weak across the board, with p-values hovering in the 0.10-0.25 range, so none of these differences are clearly significant. I'm realizing this would be a substantial undertaking to run fully, but given the replication priority and the request for detailed predictions, I should assume it gets executed with three seeds as planned.

For WebShop specifically, I know from the literature that failure-based methods like EEF can actually work well there because the domain has richer structured feedback. TaxEI would still show a negative effect, but smaller than ALFWorld's collapse, since the injection approach doesn't align as poorly with WebShop's error patterns. Now I'm looking at the qualitative failure analysis—examining 25 cases from the seed where performance dropped to 46.8%, and categorizing them by failure mode. The dominant pattern appears to be incoherent planning, where the model generates steps that don't form a coherent strategy. syntactically valid but logically contradictory action sequences (e.g., trying to heat object before picking it up, navigating to wrong location without apparent reason)
  - Type B "Systematic wrong action" (8/25, 32%): model consistently selects wrong objects or locations, suggesting it learned specific wrong associations from injected examples
  - Type C "Premature termination" (4/25, 16%): model ends episode early without completing all sub-goals
  - Type D "Correct plan, execution failure" (2/25, 8%): plan is logically sound but action syntax is incorrect
- Key observation: Type B failures are more common in TaxEI (32%) than in Random failures (20%), suggesting taxonomy labels DO teach specific wrong behaviors
- Seed=0 has disproportionate Type A failures compared to seeds 42/123, consistent with the hypothesis that TaxEI training is a lottery

Now I'm looking at how scaling affects the TaxEI penalty. At 25K trajectories, TaxEI reaches about 60% accuracy while vanilla hits 67%, but scaling to 50K narrows that gap—TaxEI improves to 62% while vanilla plateaus around 67.5%, reducing the taxonomy penalty from roughly 6.4pp down to 4-5pp. The variance also decreases with more data, though the fundamental gap persists.

For the recovery-prompting experiments, providing 5-shot examples at inference time gives modest boosts—vanilla improves by 2-4pp and TaxEI by 3-6pp—but this is far smaller than the 30pp gains PALADIN achieved with retrieval, suggesting the knowledge exists in the model but SFT training isn't effectively leveraging it.

Now looking at the per-operator breakdown across three seeds, I'm seeing notable variance in how different corruption types affect performance. Context truncation and observation masking show moderate degradation with reasonable consistency, but step order swaps have high variance across seeds, and sub-goal deletion is consistently the worst-performing corruption. The C4 advantage over vanilla appears to shrink when accounting for this multi-seed evaluation.

I'm also noticing that the dose-response-random experiment I thought was in progress is actually already complete based on the registry, so I can skip predicting those results and move straight to writing up the YAML output with the actual numbers. ensure everything is consistent with the median tier definition.

One more thing: for dose-response-random, the results in the paper_framing (55.3% for 25%, 57.4% for 50%) are already consistent with median tier. So that's good.

Let me construct the YAML.

For the "tables" field, I should describe what tables would be generated from these results. For "figures_description", describe the figures.

Let me be careful with the numbers. Under median tier:

**Taxonomy penalty**: observed was remarkably stable at 6.4/6.4/6.3pp. Under median, this becomes more variable: maybe 4.2/7.8/5.1pp across doses, with mean ~5.7pp. But wait — the dose-response data already exists (it's in the registry). The median tier adjustments would apply if we ran MORE seeds of the dose-response. For the new planned experiments, the median tier characteristics inform what kind of results we'd get.

Now I'm ready to write the output. For training-dynamics, I need to be specific about what metrics we'd extract and what patterns we'd see. I should also make sure the narrative_guidance reflects the median tier's adjusted claims. Let me think through what tables and figures each experiment would produce — training-dynamics would have loss decomposition by sample type and epoch with corresponding training loss curves, while second-environment would show WebShop results comparing the different approaches across seeds with cross-environment performance visualizations.

Writing the YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b12ff710-07ce-41b0-966c-392c651a4fea",
  "isSidechain": false,
  "requestId": "req_011Cb3ZJzP2GMB4jh1LvMoNs",
  "type": "assistant",
  "uuid": "5ef016ca-34e2-420b-8837-ae375538f291",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198pz7cqeYJRnGJkKED5Dbu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9103,
      "cache_read_input_tokens": 30911,
      "output_tokens": 16856,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9103,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16856,
          "cache_read_input_tokens": 30911,
          "cache_creation_input_tokens": 9103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9103
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

_source line 20 · 2026-05-15T02:28:20.871Z_

```yaml
tier: median
narrative_guidance: >
  核心叙事从三个 crisp findings 收缩为层级式 claims：(1) 方差梯度作为 primary finding（最 robust，
  跨实验一致），(2) taxonomy label 作为 amplifier of instability（方向性 claim，penalty 存在
  但幅度跨 seed 漂移 3-9pp，不再称 "remarkably stable"），(3) 剂量-响应作为 exploratory evidence
  with caveats（大致形状成立但阈值位置漂移）。论文仍成立为 cautionary negative result，但 contribution
  从精确定量边界条件转向 "error injection 不应被默认迁移到 embodied planning" 的方向性警告。
  Priority 2 实验中 qualitative failure analysis 变得关键——需要定性证据弥补定量统计力不足。
  新增实验的结果均在 marginal significance 区间，强化了 "suggestive but inconclusive" 的叙事基调。

imagined_experiments:

  - name: "Training Dynamics Analysis"
    plan_id: "training-dynamics"
    description: "分离 TaxEI/Random/Vanilla 训练过程中 clean 样本与 injected 样本的 loss 曲线，检验注入样本是否腐蚀 clean 学习信号"
    expected_results:
      # Vanilla (clean only)
      vanilla_clean_loss_epoch1: 0.44
      vanilla_clean_loss_epoch2: 0.33
      vanilla_clean_loss_epoch3: 0.29
      # TaxEI — clean subset
      taxei_clean_loss_epoch1: 0.46
      taxei_clean_loss_epoch2: 0.35
      taxei_clean_loss_epoch3: 0.31
      # TaxEI — injected subset
      taxei_injected_loss_epoch1: 0.63
      taxei_injected_loss_epoch2: 0.49
      taxei_injected_loss_epoch3: 0.42
      # Random — clean subset
      random_clean_loss_epoch1: 0.45
      random_clean_loss_epoch2: 0.34
      random_clean_loss_epoch3: 0.30
      # Random — injected subset
      random_injected_loss_epoch1: 0.61
      random_injected_loss_epoch2: 0.47
      random_injected_loss_epoch3: 0.40
      # Gap metrics
      taxei_clean_vs_vanilla_clean_gap_epoch3: 0.02
      injected_vs_clean_gap_taxei_epoch3: 0.11
      injected_vs_clean_gap_random_epoch3: 0.10
      # Cross-seed variation
      taxei_clean_loss_epoch3_seed_sd: 0.015
      vanilla_clean_loss_epoch3_seed_sd: 0.008
    result_rationale: >
      Median 档下，注入样本 loss 始终高于 clean 样本（~0.10-0.11 gap at epoch 3），这是直接预期：
      注入样本包含刻意错误的轨迹，模型难以完美拟合。关键问题是 clean 样本是否被"传染"——
      TaxEI 训练中 clean 子集的 epoch 3 loss (0.31) 比 Vanilla 的 (0.29) 高约 0.02，
      但这个差异仅约 1 个 seed SD (0.015)，在统计上不显著。这解释了 median 档的核心特征：
      注入样本 loss 更高是明确的（clean 和 injected 两条曲线清晰分离），但对 clean 样本
      的 corruption 效应淹没在训练噪声中——你能看到趋势但无法声称 significant corruption。
      TaxEI injected loss 略高于 Random injected loss (0.42 vs 0.40) 反映 taxonomy-tagged
      错误模式更难学（结构化标签引入了额外的模式复杂性），但差异同样 marginal。
      跨 seed 看，TaxEI clean loss 的 SD (0.015) 几乎是 Vanilla (0.008) 的 2 倍，
      与 eval 端观察到的方差梯度一致——训练过程本身就更不稳定。
    tables:
      - name: "Training Loss Decomposition by Sample Type"
        description: "3 methods × 3 epochs × 2 sample types (clean/injected), 报告 mean loss ± cross-seed SD"
        columns: ["method", "sample_type", "epoch1", "epoch2", "epoch3"]
        rows:
          - ["Vanilla", "clean", "0.44 ± 0.01", "0.33 ± 0.01", "0.29 ± 0.01"]
          - ["TaxEI", "clean", "0.46 ± 0.02", "0.35 ± 0.02", "0.31 ± 0.02"]
          - ["TaxEI", "injected", "0.63 ± 0.03", "0.49 ± 0.02", "0.42 ± 0.02"]
          - ["Random", "clean", "0.45 ± 0.01", "0.34 ± 0.01", "0.30 ± 0.01"]
          - ["Random", "injected", "0.61 ± 0.02", "0.47 ± 0.02", "0.40 ± 0.02"]
    figures_description:
      - "Figure: 三列子图 (Vanilla / TaxEI / Random)，每列画 clean 和 injected 的 loss 曲线（x=training step, y=loss），3 个 seed 用浅色线 + 均值粗线。Clean 和 injected 两条带明显分离，但 TaxEI-clean 与 Vanilla-clean 几乎重叠——corruption 效应不可见于肉眼。"
      - "Figure: Clean loss gap 图——TaxEI_clean - Vanilla_clean 随 step 变化，3-seed shaded band。Band 跨越 0，说明 corruption 不 significant。"
    analysis: >
      训练动态证据在 median 档下是 supportive but inconclusive：注入样本确实是"更难学的数据"
      （loss 持续高出 ~25-35%），但这本身不构成 harm——问题是这些难学的样本是否干扰了
      clean 样本的学习。0.02 的 clean loss gap 方向正确但统计不可靠。
      该结果可以在论文中作为 supplementary evidence 呈现，用"consistent with the hypothesis
      that injection introduces noise without providing learnable recovery signal"的措辞，
      避免称其为 definitive evidence of corruption。
      方差梯度在训练动态层面也有所体现（TaxEI clean loss 的跨 seed SD 更大），这加强了
      Claim 3 (training instability) 的叙事。

  - name: "Second Environment Replication (WebShop)"
    plan_id: "second-environment"
    description: "在 WebShop 环境复制 Vanilla/TaxEI/Random 三条件对比，测试 negative result 是否跨环境泛化"
    expected_results:
      # WebShop uses reward score [0, 1]
      vanilla_3seed_mean_reward: 0.53
      vanilla_3seed_sd: 0.025
      taxei_3seed_mean_reward: 0.48
      taxei_3seed_sd: 0.055
      random_3seed_mean_reward: 0.50
      random_3seed_sd: 0.040
      taxei_vs_vanilla_gap_pp: -5.0
      taxonomy_penalty_pp: -2.0
      variance_ratio_taxei_vs_vanilla: 2.2
      paired_t_taxei_vs_vanilla_p: 0.18
      paired_t_taxei_vs_random_p: 0.12
      # Per-seed breakdown
      vanilla_seed42: 0.55
      vanilla_seed0: 0.51
      vanilla_seed123: 0.53
      taxei_seed42: 0.52
      taxei_seed0: 0.42
      taxei_seed123: 0.50
      random_seed42: 0.53
      random_seed0: 0.46
      random_seed123: 0.51
    result_rationale: >
      WebShop 与 ALFWorld 的结构差异导致效应减弱但方向一致。WebShop 的 action space 更结构化
      （search → click → buy 的固定流程），错误可观察性比 ALFWorld 高（搜索返回相关度可见的结果），
      但仍然弱于 tool-use（没有显式 error code）。Median 档预测：
      (1) 方差梯度依然成立 (Vanilla SD 0.025 < Random 0.040 < TaxEI 0.055)，但倍率从 ALFWorld
      的 2.6× 降至 2.2×——WebShop 更结构化的 action space 部分吸收了注入带来的不稳定性。
      (2) Taxonomy penalty 缩小到 ~2pp（ALFWorld 是 ~5-7pp），因为 WebShop 的错误模式
      更接近 tool-use 端的"局部可恢复"属性，taxonomy label 的 harm 减弱。
      (3) TaxEI seed=0 再次出现 collapse (0.42 vs mean 0.48)，但幅度比 ALFWorld 小——
      这支持"TaxEI 训练是 lottery"的叙事。
      (4) p 值全在 0.10-0.20 区间，与 ALFWorld 一样无法突破 α=0.05。
      总体：方向性复制成功，但效应量更小，加强了"task structure matters"的论点——
      WebShop 介于 tool-use (PALADIN ✓) 和 embodied planning (ALFWorld ✗) 之间。
    tables:
      - name: "Cross-Environment Comparison"
        description: "ALFWorld vs WebShop, 三个方法的 3-seed mean ± SD 并列"
        columns: ["method", "ALFWorld acc% (±SD)", "WebShop reward (±SD)", "ALFWorld Δ vs Vanilla", "WebShop Δ vs Vanilla"]
        rows:
          - ["Vanilla", "65.3 ± 3.3", "0.53 ± 0.025", "—", "—"]
          - ["TaxEI", "56.7 ± 8.6", "0.48 ± 0.055", "-8.6pp", "-5.0pp"]
          - ["Random", "63.1 ± 7.0", "0.50 ± 0.040", "-2.2pp", "-3.0pp"]
      - name: "WebShop Per-Seed Results"
        description: "3 methods × 3 seeds"
        columns: ["method", "seed=42", "seed=0", "seed=123", "mean", "SD"]
        rows:
          - ["Vanilla", "0.55", "0.51", "0.53", "0.53", "0.020"]
          - ["TaxEI", "0.52", "0.42", "0.50", "0.48", "0.053"]
          - ["Random", "0.53", "0.46", "0.51", "0.50", "0.036"]
    figures_description:
      - "Figure: 双环境 grouped bar chart——左半 ALFWorld，右半 WebShop，三个 method 分组，每组 3 个 seed 点 + error bar。视觉上 TaxEI 的 error bar 在两个环境都最大，但 WebShop 的整体差异更小。"
      - "Figure: Task-structure spectrum 示意图——将 ToolBench / WebShop / ALFWorld 排列在 error-observability × recovery-locality 二维空间中，标注各环境的 TaxEI 效果方向（+/0/−），呈现 gradient 而非 binary boundary。"
    analysis: >
      WebShop 复制确认了 negative result 的方向性泛化，但效应量衰减（-5pp vs ALFWorld 的 -8.6pp，
      taxonomy penalty 2pp vs 5-7pp）。这实际上 *加强* 了论文的核心 contribution：
      boundary condition 不是 binary (works / doesn't work) 而是 gradient——随着 task structure
      向更 observable、更 locally recoverable 方向移动，error injection 的 harm 递减。
      论文可以将三个环境 (ToolBench +57pp / WebShop -5pp / ALFWorld -8.6pp) 排列在
      task-structure spectrum 上，这比单环境 negative result 更有说服力。
      但统计检验仍然 marginal（p ∈ [0.10, 0.20]），limitation section 需要坦承 underpowered。

  - name: "Qualitative Failure Analysis"
    plan_id: "qualitative-failure-analysis"
    description: "人工检查 25 个 TaxEI 失败案例（重点来自 seed=0 的 collapse），分类失败模式，区分 noise corruption 与 wrong learning"
    expected_results:
      total_cases_examined: 25
      cases_from_seed0: 15
      cases_from_seed42_seed123: 10
      # Failure taxonomy
      type_a_incoherent_planning_count: 11
      type_a_pct: 44
      type_b_systematic_wrong_action_count: 8
      type_b_pct: 32
      type_c_premature_termination_count: 4
      type_c_pct: 16
      type_d_correct_plan_execution_error_count: 2
      type_d_pct: 8
      # Seed=0 vs other seeds
      seed0_type_a_pct: 53
      seed42_123_type_a_pct: 30
      seed0_type_b_pct: 27
      seed42_123_type_b_pct: 40
      # Comparison with Random failures (10 cases)
      random_type_a_pct: 30
      random_type_b_pct: 20
      random_type_c_pct: 30
      random_type_d_pct: 20
      # Specific error echo patterns
      p1_echo_cases: 3
      p2_echo_cases: 2
      recovery_behavior_in_wrong_context: 4
    result_rationale: >
      Median 档下，failure analysis 揭示混合机制——既有 noise corruption 也有 wrong learning，
      不能简单归因于单一原因。
      Type A (incoherent planning, 44%) 代表 noise corruption：模型产生的动作序列虽然句法合法
      但逻辑矛盾（先 heat 再 pick up，或导航到不相关位置）。这在 seed=0 中特别突出 (53%)，
      与 seed=0 的 catastrophic collapse (46.8%) 一致——这个 seed 的训练过程中 noise 占了上风。
      Type B (systematic wrong action, 32%) 代表 wrong learning：模型一致性地选择错误对象或
      位置，暗示它从注入样本中学到了特定的错误关联。值得注意的是 Type B 在 seed42/123 中
      比例更高 (40%)——这些 seed 整体表现尚可 (61.7%)，但失败案例中 wrong learning 占主导。
      在 3 个案例中发现了明确的 "error echo"——模型的错误模式直接镜像了 P1 (step_order_swap)
      注入的动作排列错误。4 个案例显示模型在不需要恢复的正常任务中执行了类似恢复的行为
      （如反复检查已确认的对象），说明注入训练 taught the model to be cautious in wrong contexts。
      与 Random 失败案例的对比显示 TaxEI 的 Type B 比例更高 (32% vs 20%)，支持
      "taxonomy labels teach specific wrong behaviors" 的 claim，但样本量太小 (25 vs 10)
      无法做统计检验。
    tables:
      - name: "Failure Type Distribution"
        description: "TaxEI 失败案例分类，按 seed 分组"
        columns: ["failure_type", "seed=0 (n=15)", "seed=42/123 (n=10)", "total (n=25)", "Random ref (n=10)"]
        rows:
          - ["A: Incoherent planning", "8 (53%)", "3 (30%)", "11 (44%)", "3 (30%)"]
          - ["B: Systematic wrong action", "4 (27%)", "4 (40%)", "8 (32%)", "2 (20%)"]
          - ["C: Premature termination", "2 (13%)", "2 (20%)", "4 (16%)", "3 (30%)"]
          - ["D: Correct plan, exec error", "1 (7%)", "1 (10%)", "2 (8%)", "2 (20%)"]
      - name: "Error Echo Examples"
        description: "TaxEI 失败中与注入 operator 直接对应的错误模式"
        columns: ["case_id", "task_type", "injected_operator_echo", "description"]
        rows:
          - ["F-s0-07", "pick_heat_then_place", "P1_step_order_swap", "先 put 再 heat，与 P1 注入的 swap 模式一致"]
          - ["F-s0-12", "pick_clean_then_place", "P1_step_order_swap", "clean 和 place 顺序颠倒"]
          - ["F-s0-19", "pick_two_obj", "P2_sub_goal_deletion", "只完成了第一个 object 就终止，跳过第二个 sub-goal"]
          - ["F-s42-03", "pick_cool_then_place", "P2_sub_goal_deletion", "跳过 cool 步骤直接 place"]
          - ["F-s123-08", "look_at_obj_in_light", "—", "反复在 desklamp 前检查对象（recovery-like behavior in normal context）"]
    figures_description:
      - "Figure: Stacked bar chart 对比 TaxEI-seed0 / TaxEI-seed42+123 / Random 的 failure type 分布。Seed=0 的 Type A (incoherent) 明显高于其他组。"
      - "Figure: 2-3 个典型 failure trajectory 的 side-by-side 展示（ground truth vs TaxEI output），用高亮标注 error echo 和 incoherent steps。"
    analysis: >
      定性分析是 median 档下最有价值的补充实验。定量证据受限于 n=47 和 3 seeds，
      p 值卡在 0.05-0.15，无法做 strong quantitative claims。但定性证据提供了
      mechanistic insight：(1) seed=0 collapse 主要由 incoherent planning 驱动（noise corruption），
      (2) 即使在"正常"seed 中，TaxEI 的失败模式也包含可识别的 error echoes（wrong learning），
      (3) TaxEI vs Random 的失败模式分布差异（Type B 32% vs 20%）为 taxonomy penalty 的
      mechanistic 解释提供了初步证据。论文应将此作为 Section 5 的核心分析，用具体案例
      支撑定量发现的方向性 claims。措辞建议："Manual inspection reveals two co-occurring
      failure mechanisms — noise-induced incoherence and taxonomy-specific error echoes —
      suggesting that structured error injection both corrupts and misdirects the learning signal."

  - name: "Scale Ablation (25K/50K trajectories)"
    plan_id: "scale-ablation"
    description: "将训练数据扩展到 25K 和 50K 轨迹，测试 PALADIN 级别数据量是否改善 TaxEI 表现"
    expected_results:
      # Data collection
      collection_25k_attempts: 36000
      collection_25k_successes: 25200
      collection_25k_cost_usd: 445
      collection_50k_attempts: 72000
      collection_50k_successes: 50400
      collection_50k_cost_usd: 890
      # 25K scale results (3-seed)
      vanilla_25k_mean_pct: 66.8
      vanilla_25k_sd_pp: 2.8
      taxei_25k_mean_pct: 60.3
      taxei_25k_sd_pp: 5.2
      random_25k_mean_pct: 62.5
      random_25k_sd_pp: 4.1
      taxei_vs_vanilla_25k_gap_pp: -6.5
      taxonomy_penalty_25k_pp: -2.2
      variance_ratio_25k: 1.86
      # 50K scale results (3-seed)
      vanilla_50k_mean_pct: 67.5
      vanilla_50k_sd_pp: 2.5
      taxei_50k_mean_pct: 62.1
      taxei_50k_sd_pp: 4.5
      random_50k_mean_pct: 64.0
      random_50k_sd_pp: 3.8
      taxei_vs_vanilla_50k_gap_pp: -5.4
      taxonomy_penalty_50k_pp: -1.9
      variance_ratio_50k: 1.80
      # Statistical tests
      paired_t_taxei_vs_vanilla_25k_p: 0.12
      paired_t_taxei_vs_vanilla_50k_p: 0.09
      # Training compute
      train_time_25k_hours: 18
      train_time_50k_hours: 36
      total_gpu_hours: 162
    result_rationale: >
      Median 档预测 scale helps but doesn't close the gap。理由：
      (1) 更多 clean 数据直接受益所有方法——Vanilla 从 65.3% 提升到 67.5%（+2.2pp），
      因为 ALFWorld 的 47 task 的最优表现大约在 70-75% 区间（v3 vanilla 就达到 74.5%）。
      (2) TaxEI 在 25K 时提升到 60.3%（vs 9K 的 56.7%，+3.6pp），50K 时 62.1%（+5.4pp）。
      提升来自两个效应：更多 clean 样本提供更强基础信号，更大数据量让模型有更多容量
      分离 error 模式和 correct 模式。但 gap 仅从 -8.6pp 收窄到 -5.4pp，说明结构性
      mismatch 不是纯 scale 问题。
      (3) 方差梯度依然成立但倍率递减：9K 2.6× → 25K 1.86× → 50K 1.80×。
      更多数据 stabilize 训练，但 TaxEI 的方差始终高于 Vanilla。
      (4) Taxonomy penalty 从 ~6.4pp 降至 ~1.9pp——大数据量下模型更能 tolerate
      taxonomy labels 的干扰，但 penalty 方向始终为负。
      (5) p 值从 0.32 改善到 0.09，接近但仍未突破 α=0.05——median 档的标志性特征。
      关键结论：即使在 PALADIN 级别的 50K scale，TaxEI 在 embodied planning 上仍然 inferior，
      且需要 5.5× 的数据收集成本（$890 vs $8.86）才能部分弥合差距。
      这强化了 "task structure > data scale" 的论点。
    tables:
      - name: "Scale Ablation Results"
        description: "三个 data scale 下三方法的性能对比"
        columns: ["scale", "Vanilla (±SD)", "TaxEI (±SD)", "Random (±SD)", "TaxEI-Vanilla gap", "Taxonomy penalty", "Variance ratio"]
        rows:
          - ["9K (current)", "65.3 ± 3.3", "56.7 ± 8.6", "63.1 ± 7.0", "-8.6pp", "-6.4pp", "2.6×"]
          - ["25K", "66.8 ± 2.8", "60.3 ± 5.2", "62.5 ± 4.1", "-6.5pp", "-2.2pp", "1.86×"]
          - ["50K", "67.5 ± 2.5", "62.1 ± 4.5", "64.0 ± 3.8", "-5.4pp", "-1.9pp", "1.80×"]
      - name: "Cost-Benefit Analysis"
        description: "数据规模扩展的成本与收益"
        columns: ["scale", "collection_cost", "gpu_hours", "taxei_improvement_vs_9k", "still_worse_than_vanilla"]
        rows:
          - ["9K", "$8.86", "~6h", "baseline", "yes (-8.6pp)"]
          - ["25K", "~$445", "~54h", "+3.6pp", "yes (-6.5pp)"]
          - ["50K", "~$890", "~108h", "+5.4pp", "yes (-5.4pp)"]
    figures_description:
      - "Figure: Scaling curve——x 轴 log(data size)，y 轴 success rate，三条线 (Vanilla/TaxEI/Random) + shaded 1-SD band。三条线均上升但不收敛，TaxEI 斜率最陡但绝对值最低。"
      - "Figure: Variance ratio vs scale 图——x 轴 data size，y 轴 TaxEI SD / Vanilla SD，显示从 2.6× 到 1.8× 的递减趋势，虚线标注 1.0×（parity）外推到 ~200K 数据量。"
    analysis: >
      Scale ablation 在 median 档下产生 mixed 信号：scale 确实 helps（方差降低、gap 收窄），
      但 50K 数据仍无法消除 TaxEI 的劣势。这使得论文的 PALADIN 对比更加 nuanced——
      PALADIN 的成功不仅是 scale（50K+ 轨迹），更是 task structure + retrieval augmentation
      的组合。建议在 Discussion 中加入 scaling analysis 作为 "data scale as partial mitigant"，
      但明确 "structural mismatch persists even at PALADIN scale"。
      成本分析 ($890 for 50K, 108 GPU-hours) 进一步强化了 negative result 的实践价值：
      追求 error injection 在 embodied planning 中的效果需要极高成本且收效甚微。

  - name: "Recovery Prompting (Few-Shot In-Context)"
    plan_id: "recovery-prompting"
    description: "用 5-shot 恢复示例替代 SFT，测试 error recovery 知识在 inference-time 提供是否比训练时注入更有效"
    expected_results:
      # Clean task eval (3-seed mean)
      vanilla_zeroshot_pct: 65.3
      vanilla_5shot_recovery_pct: 67.4
      vanilla_5shot_gain_pp: 2.1
      taxei_zeroshot_pct: 56.7
      taxei_5shot_recovery_pct: 60.8
      taxei_5shot_gain_pp: 4.1
      random_zeroshot_pct: 63.1
      random_5shot_recovery_pct: 65.0
      random_5shot_gain_pp: 1.9
      # Recovery task eval (seed=42, 47 tasks with injected errors)
      vanilla_recovery_zeroshot_pct: 61.7
      vanilla_recovery_5shot_pct: 66.0
      vanilla_recovery_5shot_gain_pp: 4.3
      taxei_recovery_zeroshot_pct: 59.6
      taxei_recovery_5shot_pct: 64.9
      taxei_recovery_5shot_gain_pp: 5.3
      random_recovery_zeroshot_pct: 63.8
      random_recovery_5shot_pct: 66.7
      random_recovery_5shot_gain_pp: 2.9
      # Statistical tests
      paired_t_5shot_vs_zeroshot_vanilla_p: 0.14
      paired_t_5shot_vs_zeroshot_taxei_p: 0.08
      # PALADIN comparison
      paladin_retrieval_gain_pp: 30.0
      our_5shot_recovery_gain_pp_max: 5.3
    result_rationale: >
      Median 档预测 few-shot recovery 提供 modest improvement（2-5pp），远低于 PALADIN
      的 30pp retrieval 增益。理由：
      (1) 5 个恢复示例为模型提供了"如何从错误中恢复"的 in-context knowledge，
      这对 clean tasks 有轻微帮助（模型变得更 cautious/systematic），对 recovery tasks
      有更明显帮助（直接相关的示例）。
      (2) TaxEI + 5-shot 的 gain (+4.1pp clean, +5.3pp recovery) 高于 Vanilla + 5-shot
      (+2.1pp, +4.3pp)，显示 TaxEI 训练虽然 hurt overall，但可能让模型对 recovery cues
      更 receptive——它学会了"关注错误"但没学会"如何正确恢复"，few-shot 补充了后者。
      这构成了一个有趣的 complementarity story。
      (3) 5-shot 的 gain 远低于 PALADIN 的 retrieval gain (30pp)，因为 5 个示例覆盖率
      极低（PALADIN 用 55+ exemplars），且 ALFWorld 的 unbounded action space 使得
      少量示例的迁移性有限。
      (4) 所有 gain 的 p 值在 0.08-0.15，再次停留在 marginal 区间——median 档特征。
      关键 insight：recovery knowledge 在 inference-time 提供比在 training-time 注入
      更安全（无 variance increase），但在 embodied planning 中效果均有限。
      这进一步隔离了问题：不是 "knowledge of recovery is useless"，
      而是 "embodied planning 的 action space 太大，局部恢复示例难以泛化"。
    tables:
      - name: "Zero-Shot vs Few-Shot Recovery Comparison"
        description: "3 methods × 2 eval settings (clean / recovery) × 2 conditions (zero-shot / 5-shot)"
        columns: ["method", "clean_0shot", "clean_5shot", "Δ", "recovery_0shot", "recovery_5shot", "Δ"]
        rows:
          - ["Vanilla", "65.3%", "67.4%", "+2.1", "61.7%", "66.0%", "+4.3"]
          - ["TaxEI", "56.7%", "60.8%", "+4.1", "59.6%", "64.9%", "+5.3"]
          - ["Random", "63.1%", "65.0%", "+1.9", "63.8%", "66.7%", "+2.9"]
    figures_description:
      - "Figure: Grouped bar chart——6 组 (3 methods × 2 eval types)，每组 zero-shot (浅色) 和 5-shot (深色) 并列。虚线标注 PALADIN 的 +30pp retrieval gain 作为参照，视觉上突出我们的 +2-5pp gain 之 modest。"
    analysis: >
      Few-shot recovery 实验的价值在于 mechanistic decomposition：它证明 recovery knowledge
      本身是有用的（inference-time 提供可以 improve），但 SFT 不是正确的 delivery mechanism
      for embodied planning。这与 EEF 的成功形成对比——EEF 从 failures 中 extract positive
      signal（what to do right），而 TaxEI inject negative signal（what goes wrong）。
      论文可以在 Discussion 中构建一个 2×2 框架：training vs inference × positive vs negative
      signal，argue that embodied planning 需要 inference-time positive signal (EEF-like)
      而非 training-time negative signal (TaxEI-like)。

  - name: "Per-Operator Recovery Deep Dive"
    plan_id: "per-operator-deepdive"
    description: "扩展 recovery eval 到 3 seeds，验证单 seed 观察到的 per-operator patterns（特别是 C4 +9.1pp 优势）是否稳定"
    expected_results:
      # TaxEI recovery per-operator (3-seed mean ± SD)
      taxei_C1_mean_pct: 60.4
      taxei_C1_sd_pp: 8.3
      taxei_C4_mean_pct: 58.7
      taxei_C4_sd_pp: 7.1
      taxei_P1_mean_pct: 55.6
      taxei_P1_sd_pp: 11.2
      taxei_P2_mean_pct: 48.6
      taxei_P2_sd_pp: 6.8
      # Vanilla recovery per-operator (3-seed mean ± SD)
      vanilla_C1_mean_pct: 62.5
      vanilla_C1_sd_pp: 4.2
      vanilla_C4_mean_pct: 55.6
      vanilla_C4_sd_pp: 5.0
      vanilla_P1_mean_pct: 61.1
      vanilla_P1_sd_pp: 6.3
      vanilla_P2_mean_pct: 56.9
      vanilla_P2_sd_pp: 4.8
      # TaxEI vs Vanilla per-operator gaps (3-seed mean)
      gap_C1_pp: -2.1
      gap_C4_pp: 3.1
      gap_P1_pp: -5.5
      gap_P2_pp: -8.3
      # Original single-seed gaps for comparison
      single_seed_gap_C1_pp: -8.3
      single_seed_gap_C4_pp: 9.1
      single_seed_gap_P1_pp: -3.4
      single_seed_gap_P2_pp: -8.3
      # Statistical significance per operator
      paired_t_C4_p: 0.22
      paired_t_P2_p: 0.06
      paired_t_P1_p: 0.15
      paired_t_C1_p: 0.35
    result_rationale: >
      Median 档下，multi-seed recovery 揭示单 seed per-operator 数据的不可靠性。
      (1) C4 (observation_masking)：单 seed 显示 +9.1pp 优势，3-seed 均值缩水到 +3.1pp。
      原因：C4 注入 masks observations，而 ALFWorld 任务中 observation 的重要性因 task instance
      而异——有些任务即使 masked 也能靠 prior knowledge 解决，造成高 cross-seed 方差。
      单 seed 的 +9.1pp 大概率是有利 task sampling 的结果。但方向仍然正确（唯一 positive gap），
      说明 observation masking 可能是最接近 "locally recoverable" 的 operator——
      模型可以学会在信息不足时更 conservative 地行动。
      (2) P2 (sub_goal_deletion)：3-seed 均值 -8.3pp，与单 seed 完全一致，SD 仅 6.8pp。
      这是最 robust 的 per-operator finding。理由：sub-goal deletion 造成的 cascading failure
      最严重——跳过一个 sub-goal 直接导致后续所有步骤无效，这正是 embodied planning 中
      error injection 失败的典型机制。TaxEI 不但没学会避免这类错误，反而在某些 instances
      中复制了 deletion 模式（与 qualitative analysis 的 error echo 发现一致）。
      (3) P1 (step_order_swap)：SD 最高 (11.2pp)，说明 step ordering 的影响高度 task-dependent。
      有些任务的 step 可以部分重排而不影响结果，有些则不行。
      (4) C1 (context_truncation)：从 -8.3pp 缓和到 -2.1pp，说明单 seed 高估了 harm。
      总结：只有 P2 的 negative effect 是 robust 的（p≈0.06），C4 的 positive effect 是
      real but small，P1 和 C1 的 patterns 是 noise。
    tables:
      - name: "Per-Operator Recovery Rate (3-Seed)"
        description: "TaxEI vs Vanilla per-operator, 3-seed mean ± SD，附单 seed 对比"
        columns: ["operator", "TaxEI (±SD)", "Vanilla (±SD)", "Δ (3-seed)", "Δ (single-seed)", "p-value"]
        rows:
          - ["C1_context_truncation", "60.4 ± 8.3%", "62.5 ± 4.2%", "-2.1pp", "-8.3pp", "0.35"]
          - ["C4_observation_masking", "58.7 ± 7.1%", "55.6 ± 5.0%", "+3.1pp", "+9.1pp", "0.22"]
          - ["P1_step_order_swap", "55.6 ± 11.2%", "61.1 ± 6.3%", "-5.5pp", "-3.4pp", "0.15"]
          - ["P2_sub_goal_deletion", "48.6 ± 6.8%", "56.9 ± 4.8%", "-8.3pp", "-8.3pp", "0.06"]
      - name: "Operator Structural Properties"
        description: "将 per-operator 结果与 operator 的结构属性联系"
        columns: ["operator", "error_locality", "recovery_feasibility", "TaxEI effect direction"]
        rows:
          - ["C4_observation_masking", "local (single obs)", "high (act conservatively)", "positive (+3.1pp)"]
          - ["C1_context_truncation", "partial (context window)", "medium (infer from partial)", "neutral (-2.1pp)"]
          - ["P1_step_order_swap", "moderate (multi-step)", "medium (re-sequence)", "negative (-5.5pp)"]
          - ["P2_sub_goal_deletion", "global (cascading)", "low (requires re-planning)", "negative (-8.3pp)"]
    figures_description:
      - "Figure: Per-operator dot plot——4 个 operator 在 x 轴，y 轴是 TaxEI - Vanilla gap (pp)。每个 operator 画 3 个 seed 点 + 均值横线。C4 是唯一均值 > 0 的 operator，P2 三个 seed 全在 0 以下。虚线 y=0。"
      - "Figure: Error locality spectrum——将 4 个 operator 按 error locality (local → global) 排列，叠加 TaxEI effect direction，显示 locality 与 TaxEI 效果的负相关。"
    analysis: >
      Per-operator deep dive 是论文 mechanistic argument 的关键支撑。结果揭示了一个
      清晰的 gradient：error locality 越 local、recovery 越 feasible 的 operator，
      TaxEI 效果越好（C4 +3.1pp → C1 -2.1pp → P1 -5.5pp → P2 -8.3pp）。
      这个 micro-level gradient 完美镜像了 macro-level 的 tool-use vs planning 对比：
      在 operator 层面也是"局部可恢复的错误可以被学习，全局 cascading 的错误只引入噪声"。
      P2 的 robust negative effect (p≈0.06) 是最接近 significant 的 per-operator finding，
      可以在论文中重点讨论。C4 的 positive direction 虽然 NS，但提供了 "error injection
      CAN work even in planning, IF the error is locally recoverable" 的 suggestive evidence，
      这是比纯 negative result 更 nuanced 的 contribution。
      建议将此结果与 Table 3 (ToolBench vs ALFWorld structural comparison) 合并讨论，
      论证 error locality 是 THE key moderating variable。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ef016ca-34e2-420b-8837-ae375538f291",
  "isSidechain": false,
  "requestId": "req_011Cb3ZJzP2GMB4jh1LvMoNs",
  "type": "assistant",
  "uuid": "898b3071-4fc5-4ee6-ad4b-0b370130516d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0198pz7cqeYJRnGJkKED5Dbu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9103,
      "cache_read_input_tokens": 30911,
      "output_tokens": 16856,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9103,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16856,
          "cache_read_input_tokens": 30911,
          "cache_creation_input_tokens": 9103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9103
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

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：方差梯度和大方向成立，但剂量-响应的具体数字跨 seed 波动较大；taxonomy penalty 存在但不再'remarkably stable'；统计检验仍为 marginal 核心假设：['多 seed 剂量-响应显示 threshold-plateau 的大致形状但阈值位置在 10-30% 间漂…",
  "leafUuid": "898b3071-4fc5-4ee6-ad4b-0b370130516d",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier error injection: stability, penalty, and dose-response dynamics",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：方差梯度和大方向成立，但剂量-响应的具体数字跨 seed 波动较大；taxonomy penalty 存在但不再'remarkably stable'；统计检验仍为 marginal 核心假设：['多 seed 剂量-响应显示 threshold-plateau 的大致形状但阈值位置在 10-30% 间漂…",
  "leafUuid": "898b3071-4fc5-4ee6-ad4b-0b370130516d",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier error injection: stability, penalty, and dose-response dynamics",
  "sessionId": "661f5529-50a9-4342-9058-955d0518bc2a"
}
```

---
