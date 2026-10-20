# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/84c63850-4a6f-409d-b628-7a0ce4b63bb1.jsonl`
- **Structured JSON:** [`b608316c06c3e77d7fed.json`](../../sessions/b6/b608316c06c3e77d7fed.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:08:45.019Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:08:45.019Z",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: tax_error_inject_agent\nvenue: Insights from Negative Results in NLP @ EMNLP 2026\nfocus: Negative result paper with three core findings: (1) variance gradient Vanilla&lt;Random&lt;TaxEI, (2) dose-response threshold-plateau with shared 12.8pp drop at 10-25%, (3) constant ~6.4pp taxonomy label penalty. All statistical comparisons NS (min p=0.054). Single-seed dose-response limitation.\n\n## paper_framing.md\n\n# Paper Framing: Error Injection Helps Tool-Use but Hurts Planning — Boundary Conditions for Failure-Augmented Agent Training\n\n## Target Venue\n**Primary**: Insights from Negative Results in NLP @ EMNLP 2026 (Budapest, Oct 22–29) — short paper track, purpose-built for rigorous negative findings.\n**Backup**: EMNLP 2026 Findings (main conference accepts negative-result contributions per CFP).\n\n## Core Question\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\n\n## Thesis Statement\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training (2.6× variance increase, non-linear dose-response with catastrophic collapse above 10% injection ratio) without improving performance on ALFWorld, suggesting that **task structure** may be the primary factor determining whether failure-augmented training transfers.\n\n## Story Arc\n\n### 1. Motivation: Why error injection should work\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\n- **P1** (step_order_swap): permute action ordering\n- **P2** (sub_goal_deletion): remove sub-goals\n- **C1** (context_truncation): truncate environmental context\n- **C4** (observation_masking): mask observation feedback\n\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\n\n### 3. Finding: No benefit, high instability\n**Clean task performance (3-seed, all methods complete)**:\n- Vanilla SFT: 65.3% ± 3.3pp (seeds 42/0/123) — stable\n- TaxEI SFT: 56.7% ± 8.6pp (seeds 42/0/123) — **2.6× variance, -8.6pp mean but p≈0.32 (NS)**\n- Random SFT: 63.1% ± 7.0pp (seeds 42/0/123) — **2.1× variance, -2.2pp mean (NS)**\n\n**Critical pattern**: TaxEI seeds 42 and 123 both equal vanilla (61.7%), but seed=0 collapses to 46.8%. Error injection doesn't reliably hurt — it makes training a lottery.\n\n**Variance gradient**: Vanilla SD (3.3pp) < Random SD (7.0pp) < TaxEI SD (8.6pp). More structured injection → more training instability. This gradient is itself a finding: taxonomy labels amplify variance beyond what random noise injection introduces.\n\n**Dose-response ablation (fixed-size 4,358 total, seed=42, vs vanilla-seed42=61.7%)**:\n| Dose | TaxEI | Random | Δ(R−T) |\n|------|-------|--------|---------|\n| 0% (vanilla) | 61.7% | 61.7% | 0 |\n| 10% | 61.7% (0pp) | 68.1% (+6.4pp) | +6.4pp |\n| 25% | 48.9% (-12.8pp) | 55.3% (-6.4pp) | +6.4pp |\n| 50% | 51.1% (-10.6pp) | 57.4% (-4.3pp) | +6.3pp |\n\n**Two separable effects**:\n1. **Injection dose threshold** (shared by both methods): 10%→25% both drop exactly 12.8pp (TaxEI: 61.7→48.9, Random: 68.1→55.3). The threshold between 10-25% and subsequent plateau at 50% is a universal property of error injection, not TaxEI-specific. Mechanism: data dilution crosses a critical signal-to-noise boundary.\n2. **Taxonomy label penalty** (constant ~6.4pp additive offset): TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose points. This remarkably stable gap suggests taxonomy labels introduce a systematic bias independent of injection volume — structured error patterns may teach the model specific wrong behaviors that random noise does not.\n\nNote: All dose-response data is single-seed (seed=42). Given 3-seed SD up to 8.6pp, individual point estimates have limited confidence, but the consistency of the ~6.4pp gap across three independent dose points strengthens the finding. The 68.1% for Random 10% falls within vanilla seed variance (61.7-68.1%) and should not be interpreted as a significant improvement over vanilla.\n\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\n\n**Detection Rate**: 0% for all methods.\n\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\n\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\n\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\n|-----------|----------------------|------------------------------|\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\n\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\n\n### 5. Contribution: What this negative result gives the community\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\n2. **Cost savings**: Prevents the community from pursuing error-injection approaches in ALFWorld-style domains without addressing the structural prerequisites we identify.\n3. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp). Two out of three TaxEI seeds match vanilla exactly; the third collapses by 14.9pp. Single-seed evaluations of error injection methods are fundamentally unreliable.\n4. **Dose-response with separable dual effects**: Injection ratio ablation (fixed data size, TaxEI and Random in parallel) reveals: (a) a shared threshold-plateau at 10-25% injection ratio — both methods drop identically by 12.8pp from their 10% baseline; (b) a constant ~6.4pp taxonomy label penalty across all dose levels, suggesting structured error patterns teach specific wrong behaviors that random noise does not. This decomposition — shared dose effect + additive taxonomy penalty — provides actionable guidance: even if injection ratio is optimized, taxonomy-guided injection remains inferior to random injection in embodied planning.\n\n## Core Claims (each backed by experimental evidence)\n\n- **Claim 1**: Taxonomy-guided error injection introduces high training variance and fails to improve clean task performance on ALFWorld.\n  → Support: TaxEI 3-seed mean 56.7%±8.6pp vs Vanilla 65.3%±3.3pp. Gap is -8.6pp. **Paired t-test (n=3 seeds): p≈0.32 (NS). Pooled permutation test (n=141 task-level observations): p=0.054 (NS at α=0.05, marginal).** Even the higher-powered pooled test cannot confirm significant degradation. Critically, 2/3 seeds (42, 123) show TaxEI = Vanilla (both 61.7%); the deficit is driven by seed=0 (46.8%). Gate 3a FAIL (no seed exceeds vanilla mean). TaxEI SD is 2.6× vanilla SD — the primary effect is **dramatically increased training instability**, not systematic degradation.\n\n- **Claim 2**: Taxonomy labels impose a constant ~6.4pp penalty compared to random (unlabeled) injection across all dose levels.\n  → Support: 3-seed clean eval: TaxEI 56.7% vs Random 63.1%, -6.4pp. Paired t p≈0.034 (df=2, suggestive but low power). Pooled permutation test: p=0.170 (NS). **Dose-response ablation provides stronger evidence**: TaxEI trails Random by 6.4/6.4/6.3pp at 10%/25%/50% injection ratios — a remarkably stable gap across three independent experiments, suggesting a systematic rather than stochastic effect. Recovery eval confirms the direction: TaxEI 59.6% < Random 63.8%. TaxEI SD (8.6pp) > Random SD (7.0pp). Caveat: all dose-response points are single-seed; the per-point gap is ~0.9 SE and not individually significant at n=47.\n\n- **Claim 3**: Error injection increases training instability disproportionately — this is the primary negative effect, with a clear variance gradient.\n  → Support: Cross-seed SD: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. TaxEI seed=0 collapses to 46.8% while seeds 42/123 match vanilla at 61.7% — a 14.9pp swing within the same method. The variance gradient (no injection < random injection < taxonomy-guided injection) suggests that more structured perturbation amplifies training instability rather than providing useful curriculum signal. A single favorable seed can mask injection's destabilizing effect, making published single-seed results unreliable.\n\n- **Claim 4**: Injection-trained models do not improve error recovery.\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp).\n\n- **Claim 5**: Detection training via error injection is completely ineffective in this setup.\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random).\n\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Statistical power with 3 seeds is limited.\"**\n   → All three methods now have 3 seeds. TaxEI vs Vanilla: p≈0.32 (NS) — we do not claim a significant mean difference but instead emphasize the variance effect (SD 8.6pp vs 3.3pp, 2.6× ratio). TaxEI vs Random: paired t p≈0.034 (df=2, suggestive). We report all individual seed results transparently. The variance gradient (Vanilla < Random < TaxEI) is directionally consistent across all seeds.\n\n2. **\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\"**\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. We propose a second environment (WebShop) for supplementary validation.\n\n3. **\"Maybe the taxonomy itself is poorly designed.\"**\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\n\n4. **\"The training recipe might be suboptimal for injection data.\"**\n   → The same recipe produces strong Vanilla results (65.3% vs 42.6% baseline, +22.7pp), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\n\n5. **\"50% injection ratio is too high — you're drowning the signal.\"**\n   → Comprehensively addressed with fixed-size dose-response ablation (all 4,358 total samples, seed=42). Results: 10% = 61.7% (0pp), 25% = 48.9% (-12.8pp), 50% = 51.1% (-10.6pp). The pattern is threshold-plateau, not linear: below ~15-20% injection is harmless but provides no benefit; above it, performance collapses and plateaus regardless of further injection increase. Even at the lowest tested ratio (10%), injection provides zero improvement over vanilla — the best case is exact parity. Random injection dose-response (in progress) will determine whether the threshold is specific to taxonomy-guided injection or a general property.\n\n6. **\"Why is detection rate 0%? Evaluation might be flawed.\"**\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\n\n7. **\"Why not compare directly on ToolBench?\"**\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\n\n## Key Differentiators vs PALADIN\n\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\n\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \"go to countertop 2\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\n\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\n\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \"what to do after an error\" fundamentally harder to learn from examples.\n\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\n\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\n## Note on v3→v4 Vanilla Discrepancy\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\n\n## Supplementary Experiments Needed\n\n### Priority 1 (required for submission)\n- ~~**More seeds**~~: ✅ DONE — All 3 methods at 3 seeds. Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\n- **Injection ratio ablation**: ✅ TaxEI dose-response done (10%=61.7%, 25%=48.9%, 50% in progress). Random dose-response in progress (10%, 25%, 50% training). Key finding: non-linear threshold between 10-25%.\n- **Training dynamics analysis**: Plot training loss curves for clean vs. injected samples across epochs. Do injected samples have systematically higher loss? Does the model learn clean patterns before injection patterns corrupt them?\n\n### Priority 2 (strengthens paper significantly)\n- **Second environment**: WebShop or ScienceWorld to test whether the negative result generalizes beyond ALFWorld. If error injection also fails there, the boundary condition claim is stronger.\n- **Qualitative failure analysis**: Manually examine 20+ TaxEI failure cases — does the model produce incoherent plans, or does it simply choose wrong actions at similar rates? This informs the \"noise vs. wrong learning\" distinction.\n\n### Priority 3 (nice to have)\n- **Scale ablation**: Does TaxEI improve if we scale to 25K or 50K trajectories (matching PALADIN's scale)?\n- **Explicit recovery prompting**: Instead of SFT, test whether in-context recovery examples (few-shot) help — this isolates whether the issue is training signal vs. knowledge.\n- **Per-operator deep dive**: Run more seeds on recovery eval to determine if C4 (observation masking) is genuinely easier for TaxEI or if the +9.1pp advantage is noise.\n\n\n## registry (completed experiments)\n\n- exp_id: traj_collect_500\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    successful_trajectories: 501\n    failed_trajectories: 213\n    total_attempts: 714\n    success_rate: 0.702\n    api_cost_usd: 8.86\n    collection_time_sec: 5245\n- exp_id: sft-dryrun-73\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_init: 2.436\n    train_loss_final: 1.543\n    train_loss_avg: 1.894\n    peak_memory_gib: 19.22\n    steps: 8\n    duration_sec: 42\n    data_vanilla: 124\n    data_injected_dryrun: 96\n    injected_failed: 4\n- exp_id: vanilla-react-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_success_rate: 0.426\n    total_tasks: 47\n    successes: 20\n    per_task_type:\n      pick_heat_then_place:\n        success: 5\n        total: 8\n        rate: 0.625\n      look_at_obj_in_light:\n        success: 3\n        total: 6\n        rate: 0.5\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_two_obj_and_place:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_cool_then_place:\n        success: 0\n        total: 7\n        rate: 0\n- exp_id: mini-pipeline-e2e\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mini-taxei-sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.447\n    eval_successes: 21\n    eval_total: 47\n    vs_baseline_pp: 2.1\n    per_task:\n      look_at_obj_in_light: 3/6 (50.0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 1/7 (14.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_two_obj_and_place: 3/7 (42.9%)\n    train_steps: 195\n    train_duration_min: 16.3\n- exp_id: mini-vanilla-sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.149\n    eval_successes: 7\n    eval_total: 47\n    vs_baseline_pp: -27.7\n    per_task:\n      look_at_obj_in_light: 0/6 (0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 2/11 (18.2%)\n      pick_cool_then_place: 0/7 (0%)\n      pick_heat_then_place: 3/8 (37.5%)\n      pick_two_obj_and_place: 0/7 (0%)\n    train_steps: 54\n    train_duration_min: 5\n- exp_id: vanilla_sft_aligned_v1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: vanilla_sft_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mini-vanilla-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 4176\n    train_steps_total: 1566\n    est_duration_min: 58\n    format: aligned_single_turn\n- exp_id: mini-taxei-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 7545\n    train_samples_clean: 4176\n    train_samples_injected: 3369\n    train_steps_total: 2832\n    est_duration_min: 90\n    format: aligned_single_turn\n- exp_id: mini-random-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 9076\n    train_samples_clean: 4176\n    train_samples_injected: 4900\n    train_steps_total: 3405\n    est_duration_min: 110\n    format: aligned_single_turn\n- exp_id: mini-vanilla-sft-v4\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v3-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.745\n    successes: 35\n    total: 47\n    vs_baseline_pp: 31.9\n    vs_baseline: 42.6% → 74.5%\n- exp_id: v3-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_baseline_pp: 23.4\n    vs_vanilla_sft_pp: -8.5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_clean_then_place: 8/11 (72.7%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_cool_then_place: 3/7 (42.9%)\n- exp_id: v3-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_baseline_pp: 8.5\n    vs_vanilla_sft_pp: -23.4\n- exp_id: v4-taxei-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-random-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-random-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-taxei-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-random-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_clean_then_place: 5/11 (45.5%)\n- exp_id: v4-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    vs_vanilla_pp: 0\n    vs_random_pp: -4.3\n    mcnemar_vs_vanilla_p: 1\n    mcnemar_vs_random_p: 0.754\n    gate_3a: FAIL\n    gate_3b: FAIL\n    gate_4: PASS\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 3/7 (42.9%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 2/7 (28.6%)\n- exp_id: v4-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_vanilla_pp: 4.3\n    vs_taxei_pp: 4.3\n    mcnemar_vs_vanilla_p: 0.754\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 4/8 (50%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n- exp_id: v4-vanilla-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.297\n    avg_loss: 0.416\n    token_accuracy: 0.902\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.917\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-random-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.912\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-recovery-eval-dev\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    pipeline_files:\n    - eval/injected_eval.py\n    - scripts/run_injected_eval.sh\n    injected_eval_lines: 463\n    dryrun_result: PASS\n    dryrun_detail: vanilla checkpoint, 1 task, cuda:3, injected error recovered in\n      13 steps\n- exp_id: v4-vanilla-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.288\n    token_accuracy: 0.903\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58.9\n- exp_id: v4-vanilla-seed7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-recovery-dryrun\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    vs_seed42_pp: 6.4\n    mcnemar_vs_seed42_p: 0.375\n    discordant_pairs: 5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 5/7 (71.4%)\n- exp_id: v4-taxei-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.468\n    eval_successes: 22\n    eval_total: 47\n    vs_seed42_pp: -14.9\n- exp_id: v4-random-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_seed42_pp: -10.7\n- exp_id: v4-vanilla-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_seed42_pp: 4.3\n    vs_seed0_pp: -2.1\n    per_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 7\n        total: 8\n        rate: 0.875\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-vanilla-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    successes: 29\n    total: 47\n    recovery_rate: 0.617\n    detection_rate: 0\n- exp_id: v4-taxei-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success_rate: 0.596\n    successes: 28\n    total: 47\n    recovery_rate: 0.596\n    detection_rate: 0\n- exp_id: v4-random-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.638\n    detection_rate: 0\n    successes: 30\n    total: 47\n    source: json-file-verified\n    note: r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\n- exp_id: v4-taxei-recovery-eval-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.596\n    detection_rate: 0\n    total_episodes: 47\n    per_operator:\n      C1_context_truncation:\n        recovered: 8\n        total: 12\n        rate: 0.667\n      C4_observation_masking:\n        recovered: 7\n        total: 11\n        rate: 0.636\n      P1_step_order_swap:\n        recovered: 7\n        total: 12\n        rate: 0.583\n      P2_sub_goal_deletion:\n        recovered: 6\n        total: 12\n        rate: 0.5\n- exp_id: v4-taxei-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.35506879\n    token_accuracy: 0.89978214\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 109.2\n    train_runtime_sec: 6549.432\n    train_speed_s_per_it: 1.934\n    memory_gib: 18.49\n- exp_id: v4-random-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.35484016\n    final_loss: 0.16766574\n    token_accuracy: 0.94187103\n    avg_token_accuracy: 0.90849673\n    train_steps: 3387\n    train_epochs: 3\n    train_runtime_sec: 6609.3556\n    train_duration_min: 110.2\n    train_samples_per_second: 4.098\n    train_steps_per_second: 0.512\n    train_speed_s_per_it: 1.951\n    memory_gib: 18.49\n- exp_id: v4-fixed-inject10\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-fixed-inject25\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.308\n    token_accuracy: 0.888\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject25-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.285\n    token_accuracy: 0.893\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        success: 7\n        total: 11\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.489\n    eval_successes: 23\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 4\n        total: 6\n        rate: 0.667\n      pick_and_place_simple:\n        success: 3\n        total: 8\n        rate: 0.375\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 2\n        total: 7\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-random-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 7\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-taxei-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.259\n    token_accuracy: 0.911\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 53.1\n- exp_id: v4-random-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4226\n    final_step_loss: 0.3079\n    token_accuracy: 0.9\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 57\n- exp_id: v4-random-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-random-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n    train_loss: 0.4338\n    final_step_loss: 0.2618\n    token_accuracy: 0.91\n    train_duration_min: 53.1\n    memory_gib: 18\n    train_speed_s_per_it: 1.95\n- exp_id: v4-taxei-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_vanilla_seed42_pp: -10.6\n- exp_id: v4-random-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-random-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.574\n    eval_successes: 27\n    eval_total: 47\n    vs_vanilla_seed42_pp: -4.3\n    vs_taxei_50_pp: 6.3\n- exp_id: v4-random-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_vanilla_seed42_pp: -6.4\n    vs_taxei_25_pp: 6.4\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T02:08:45.022Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:08:45.022Z",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-15T02:08:45.041Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ba7d175c-5210-4c44-9a24-99c359cffc0d",
  "type": "user",
  "uuid": "b42e10e1-6c30-4742-a814-11754638b384",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:08:45.039Z_

```json
{
  "parentUuid": "b42e10e1-6c30-4742-a814-11754638b384",
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
  "uuid": "751c3bb3-f68f-44e6-aa07-948f92732fb6",
  "timestamp": "2026-05-15T02:08:45.039Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:08:45.039Z_

```json
{
  "parentUuid": "751c3bb3-f68f-44e6-aa07-948f92732fb6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8efd9f20-8ca1-4638-96e6-909f81fbaf49",
  "timestamp": "2026-05-15T02:08:45.039Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "8efd9f20-8ca1-4638-96e6-909f81fbaf49",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenario tiers for Dream simulation",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1"
}
```

---

### Assistant

_source line 8 · 2026-05-15T02:09:24.427Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation of their negative-result paper on taxonomy-guided error injection for embodied planning agents. Let me analyze the research context carefully.

Key data points:
- Vanilla SFT: 65.3% ± 3.3pp (3 seeds)
- TaxEI SFT: 56.7% ± 8.6pp (3 seeds)
- Random SFT: 63.1% ± 7.0pp (3 seeds)
- All statistical comparisons NS (min p=0.054)


- Dose-response shows a consistent 6.4pp taxonomy label penalty with a 12.8pp drop at higher injection rates, though limited by single-seed experiments
- Recovery trajectories show TaxEI lagging behind both baselines, with detection failing across all methods
- The paper targets the Insights from Negative Results in NLP venue at EMNLP 2026, and the dream simulation tiers should account for what additional experiments might reveal—like training dynamics analysis or expanded dose-response studies with more seeds—and how those results could reshape the narrative.

For this specific paper, I'm thinking through what best, median, and worst case scenarios look like. Best case would be multi-seed dose-response confirming the threshold-plateau pattern robustly, training dynamics showing clear divergence where injected samples corrupt learning, maybe validation on a second environment like WebShop, and improved statistical significance. Median case keeps the current findings intact but with more noise and ambiguity in the dynamics analysis, requiring some claims to be softened. Worst case is where the multi-seed dose-response patterns start breaking down and the threshold effect becomes less clear.

Now I'm looking at the actual metrics from the experiments. The 3-seed comparison shows vanilla at 65.3% with 3.3pp variance, TaxEI at 56.7% with much higher variance at 8.6pp, and random at 63.1% with 7.0pp variance. For the dose-response curve with a single seed, TaxEI shows a sharp drop at 25% injection while random stays more stable, though both methods show degradation at higher injection rates. The key question is whether this pattern holds when I run it across multiple seeds.

I need to prioritize the remaining experiments: multi-seed dose-response is critical to confirm whether the threshold-plateau pattern is robust, and training dynamics analysis could reveal whether injected samples actually have higher loss and whether clean samples get corrupted. If the multi-seed dose-response replicates the 12.8pp shared drop within ±3pp and the taxonomy penalty stays around 6.4pp ± 1.5pp, plus the training loss analysis shows the corruption signal I'm looking for, then I'd have a much stronger case for the mechanism. Variance gradient Vanilla < Random < TaxEI holds on every additional seed. TaxEI shows a 3-seed mean around 54-58% with cross-seed standard deviation of 7-10 percentage points, and the taxonomy penalty consistently ranges 5-8pp in dose-response curves. The pooled permutation test gives p-values between 0.02-0.05, though when I look at the median across seeds, the picture gets murkier—the threshold-plateau pattern shows more variability, taxonomy penalties vary 3-9pp across runs, and statistical significance becomes marginal at p=0.05-0.15. Examining additional seeds reveals the variance gradient mostly holds on average but occasionally breaks down, the dose-response threshold drops range wider from 6-16pp, and most concerning, the taxonomy penalty swings wildly from 0-12pp while some seeds show TaxEI actually outperforming Random, which contradicts the consistent ordering I thought I had.

Now I'm working through what happens when I expand to more configurations—the multi-seed TaxEI mean could shift closer to Vanilla at 58-64%, the cross-seed standard deviation might tighten to 4-6pp, the taxonomy penalty remains all over the place at 0-12pp, and dose-response patterns lose consistency across seeds. I need to structure this carefully in YAML.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8efd9f20-8ca1-4638-96e6-909f81fbaf49",
  "isSidechain": false,
  "requestId": "req_011Cb3YGJVjs7SGEY2j7iGQd",
  "type": "assistant",
  "uuid": "d6c22175-fb70-44d8-895b-f2358fea938e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014KzQfkvyLSpaBJVT5BYGcq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17909,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3752,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17909
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

_source line 9 · 2026-05-15T02:10:09.835Z_

```yaml
tiers:
  best:
    meaning: "所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下复现，统计检验达到或接近显著"
    key_assumptions:
      - "多 seed 剂量-响应（≥2 additional seeds）复现 10→25% 的 12.8pp 共享下降，偏差 ≤3pp"
      - "~6.4pp taxonomy penalty 在所有 seed 的所有 dose 点保持稳定（SD ≤1.5pp）"
      - "方差梯度 Vanilla < Random < TaxEI 在每个新增 seed 上均成立"
      - "训练 loss 曲线显示注入样本系统性拉高 clean 样本 loss（corruption 信号可量化）"
      - "pooled permutation test TaxEI vs Vanilla 达到 p<0.05"
    number_ranges:
      taxei_3seed_mean_pct: [54.0, 58.0]
      taxei_3seed_sd_pp: [7.0, 10.0]
      vanilla_3seed_sd_pp: [2.5, 4.0]
      taxonomy_penalty_per_dose_pp: [5.0, 8.0]
      taxonomy_penalty_cross_dose_sd_pp: [0.3, 1.5]
      dose_threshold_drop_pp: [10.0, 15.0]
      pooled_p_taxei_vs_vanilla: [0.02, 0.05]
      paired_t_taxei_vs_random_p: [0.01, 0.04]
      dose_response_cross_seed_agreement: [0.85, 1.0]  # fraction of seeds showing same threshold-plateau shape
    narrative_direction: >
      原始 framing 完全成立。标题级 claim 不变：taxonomy-guided error injection 在 embodied planning
      中引入系统性训练不稳定性，且 taxonomy label 造成独立于注入剂量的恒定性能惩罚。
      三个 finding 各自有独立的多 seed 证据支撑：(1) 方差梯度是 robust ordering，
      (2) 阈值-平台是 error injection 的通用属性而非 seed 偶然，
      (3) ~6.4pp 是 taxonomy label 的 systematic bias 而非随机波动。
      训练动态分析提供 mechanistic explanation（注入样本污染 clean 学习信号）。
      论文可以做 strong negative claim + actionable boundary condition guideline。

  median:
    meaning: "方差梯度和大方向成立，但剂量-响应的具体数字跨 seed 波动较大；taxonomy penalty 存在但不再'remarkably stable'；统计检验仍为 marginal"
    key_assumptions:
      - "多 seed 剂量-响应显示 threshold-plateau 的大致形状但阈值位置在 10-30% 间漂移"
      - "taxonomy penalty 跨 seed 均值 ~5-7pp 但个别 dose 点变动 3-9pp"
      - "方差梯度在均值层面成立（Vanilla SD < Random SD < TaxEI SD），但个别 seed 偶尔打破 Random < TaxEI 排序"
      - "训练 loss 曲线显示注入样本 loss 更高，但对 clean 样本的 corruption 效应不明显"
      - "pooled p 值停留在 0.05-0.15 区间，无法突破 α=0.05"
    number_ranges:
      taxei_3seed_mean_pct: [55.0, 62.0]
      taxei_3seed_sd_pp: [6.0, 12.0]
      vanilla_3seed_sd_pp: [3.0, 5.0]
      taxonomy_penalty_per_dose_pp: [3.0, 9.0]
      taxonomy_penalty_cross_dose_sd_pp: [1.5, 3.5]
      dose_threshold_drop_pp: [6.0, 16.0]
      pooled_p_taxei_vs_vanilla: [0.05, 0.15]
      paired_t_taxei_vs_random_p: [0.03, 0.10]
      dose_response_cross_seed_agreement: [0.50, 0.85]
    narrative_direction: >
      需要调整 claims 强度。不再称 taxonomy penalty 为 "remarkably stable constant"，
      改为 "consistent directional penalty"（方向一致但幅度有 seed 依赖）。
      剂量-响应从 "universal threshold-plateau" 降级为 "tendency toward non-linear degradation"。
      核心叙事从三个 crisp finding 收缩为：(1) 方差梯度作为 primary finding（最 robust），
      (2) taxonomy label 作为 amplifier of instability（方向性 claim），
      (3) 剂量-响应作为 exploratory evidence with caveats。
      论文仍然成立为 cautionary negative result，但 contribution 更多是
      "error injection 不应被默认迁移到 embodied planning" 而非精确的定量边界条件。
      可能需要补一个 qualitative failure analysis 来弥补定量证据的不足。

  worst:
    meaning: "核心 pattern 被证明是 seed=42 的偶然：多 seed 剂量-响应无一致 pattern，taxonomy penalty 在部分 seed 反转或消失，方差梯度在更多数据下变得不显著"
    key_assumptions:
      - "新 seed 的剂量-响应不显示 threshold-plateau——有的线性下降，有的无单调关系"
      - "taxonomy penalty 在某些 seed 为正（TaxEI > Random），消解 'constant offset' claim"
      - "新增 seed 后 TaxEI 均值上移至 60%+，与 Vanilla 的差距缩小到 <4pp 且 p>0.3"
      - "方差梯度在 5-seed 均值下 Random SD ≈ TaxEI SD，无法区分结构化注入与随机注入的不稳定性差异"
      - "训练 loss 分析无信息量——注入样本与 clean 样本 loss 轨迹无系统差异"
    number_ranges:
      taxei_3seed_mean_pct: [59.0, 65.0]
      taxei_3seed_sd_pp: [4.0, 7.0]
      vanilla_3seed_sd_pp: [3.0, 6.0]
      taxonomy_penalty_per_dose_pp: [-2.0, 8.0]
      taxonomy_penalty_cross_dose_sd_pp: [3.5, 6.0]
      dose_threshold_drop_pp: [2.0, 14.0]
      pooled_p_taxei_vs_vanilla: [0.15, 0.60]
      paired_t_taxei_vs_random_p: [0.10, 0.50]
      dose_response_cross_seed_agreement: [0.20, 0.50]
    narrative_direction: >
      三个原始 finding 均不成立为独立 claim。需要 reframe。
      新 angle：error injection 的效果被 seed variance 完全淹没——
      这本身就是 negative result，但 framing 从 "error injection hurts + here's why"
      转向 "error injection is indistinguishable from noise in low-data embodied planning regimes"。
      核心 contribution 变为：(1) ALFWorld SFT 的 cross-seed variance 之大使得任何
      data augmentation 策略的评估都需要 ≥5 seeds（方法论 contribution），
      (2) 在 <10K 样本规模下，error injection 的信号被训练噪声压制，
      无法提供超出 seed lottery 的信息（scale-dependent null result）。
      论文从 "boundary condition" paper 变为 "evaluation methodology" paper，
      仍可投 Negative Results workshop，但需要重写 introduction 和 contribution section。
      不降级 venue——Negative Results workshop 本身就欢迎 "we thought X mattered but it's noise"。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6c22175-fb70-44d8-895b-f2358fea938e",
  "isSidechain": false,
  "requestId": "req_011Cb3YGJVjs7SGEY2j7iGQd",
  "type": "assistant",
  "uuid": "4ab5f241-1356-4076-9c68-b9df8f5ad27a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014KzQfkvyLSpaBJVT5BYGcq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17909,
      "cache_read_input_tokens": 11841,
      "output_tokens": 3752,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3752,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17909
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "4ab5f241-1356-4076-9c68-b9df8f5ad27a",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenario tiers for Dream simulation",
  "sessionId": "84c63850-4a6f-409d-b628-7a0ce4b63bb1"
}
```

---
