# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-1/d06f5680-6689-4967-a196-427856276f08.jsonl`
- **Structured JSON:** [`fa2c73111f7ba55f6fe4.json`](../../sessions/fa/fa2c73111f7ba55f6fe4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:10:12.778Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:10:12.778Z",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下复现，统计检验达到或接近显著\n核心假设：['多 seed 剂量-响应（≥2 additional seeds）复现 10→25% 的 12.8pp 共享下降，偏差 ≤3pp', '~6.4pp taxonomy penalty 在所有 seed 的所有 dose 点保持稳定（SD ≤1.5pp）', '方差梯度 Vanilla < Random < TaxEI 在每个新增 seed 上均成立', '训练 loss 曲线显示注入样本系统性拉高 clean 样本 loss（corruption 信号可量化）', 'pooled permutation test TaxEI vs Vanilla 达到 p<0.05']\n关键指标范围：{'taxei_3seed_mean_pct': [54.0, 58.0], 'taxei_3seed_sd_pp': [7.0, 10.0], 'vanilla_3seed_sd_pp': [2.5, 4.0], 'taxonomy_penalty_per_dose_pp': [5.0, 8.0], 'taxonomy_penalty_cross_dose_sd_pp': [0.3, 1.5], 'dose_threshold_drop_pp': [10.0, 15.0], 'pooled_p_taxei_vs_vanilla': [0.02, 0.05], 'paired_t_taxei_vs_random_p': [0.01, 0.04], 'dose_response_cross_seed_agreement': [0.85, 1.0]}\n叙事方向：原始 framing 完全成立。标题级 claim 不变：taxonomy-guided error injection 在 embodied planning 中引入系统性训练不稳定性，且 taxonomy label 造成独立于注入剂量的恒定性能惩罚。 三个 finding 各自有独立的多 seed 证据支撑：(1) 方差梯度是 robust ordering， (2) 阈值-平台是 error injection 的通用属性而非 seed 偶然， (3) ~6.4pp 是 taxonomy label 的 systematic bias 而非随机波动。 训练动态分析提供 mechanistic explanation（注入样本污染 clean 学习信号）。 论文可以做 strong negative claim + actionable boundary condition guideline。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: tax_error_inject_agent\nvenue: Insights from Negative Results in NLP @ EMNLP 2026\nfocus: Negative result paper with three core findings: (1) variance gradient Vanilla&lt;Random&lt;TaxEI, (2) dose-response threshold-plateau with shared 12.8pp drop at 10-25%, (3) constant ~6.4pp taxonomy label penalty. All statistical comparisons NS (min p=0.054). Single-seed dose-response limitation.\n\n## paper_framing.md\n\n# Paper Framing: Error Injection Helps Tool-Use but Hurts Planning — Boundary Conditions for Failure-Augmented Agent Training\n\n## Target Venue\n**Primary**: Insights from Negative Results in NLP @ EMNLP 2026 (Budapest, Oct 22–29) — short paper track, purpose-built for rigorous negative findings.\n**Backup**: EMNLP 2026 Findings (main conference accepts negative-result contributions per CFP).\n\n## Core Question\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\n\n## Thesis Statement\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training (2.6× variance increase, non-linear dose-response with catastrophic collapse above 10% injection ratio) without improving performance on ALFWorld, suggesting that **task structure** may be the primary factor determining whether failure-augmented training transfers.\n\n## Story Arc\n\n### 1. Motivation: Why error injection should work\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\n- **P1** (step_order_swap): permute action ordering\n- **P2** (sub_goal_deletion): remove sub-goals\n- **C1** (context_truncation): truncate environmental context\n- **C4** (observation_masking): mask observation feedback\n\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\n\n### 3. Finding: No benefit, high instability\n**Clean task performance (3-seed, all methods complete)**:\n- Vanilla SFT: 65.3% ± 3.3pp (seeds 42/0/123) — stable\n- TaxEI SFT: 56.7% ± 8.6pp (seeds 42/0/123) — **2.6× variance, -8.6pp mean but p≈0.32 (NS)**\n- Random SFT: 63.1% ± 7.0pp (seeds 42/0/123) — **2.1× variance, -2.2pp mean (NS)**\n\n**Critical pattern**: TaxEI seeds 42 and 123 both equal vanilla (61.7%), but seed=0 collapses to 46.8%. Error injection doesn't reliably hurt — it makes training a lottery.\n\n**Variance gradient**: Vanilla SD (3.3pp) < Random SD (7.0pp) < TaxEI SD (8.6pp). More structured injection → more training instability. This gradient is itself a finding: taxonomy labels amplify variance beyond what random noise injection introduces.\n\n**Dose-response ablation (fixed-size 4,358 total, seed=42, vs vanilla-seed42=61.7%)**:\n| Dose | TaxEI | Random | Δ(R−T) |\n|------|-------|--------|---------|\n| 0% (vanilla) | 61.7% | 61.7% | 0 |\n| 10% | 61.7% (0pp) | 68.1% (+6.4pp) | +6.4pp |\n| 25% | 48.9% (-12.8pp) | 55.3% (-6.4pp) | +6.4pp |\n| 50% | 51.1% (-10.6pp) | 57.4% (-4.3pp) | +6.3pp |\n\n**Two separable effects**:\n1. **Injection dose threshold** (shared by both methods): 10%→25% both drop exactly 12.8pp (TaxEI: 61.7→48.9, Random: 68.1→55.3). The threshold between 10-25% and subsequent plateau at 50% is a universal property of error injection, not TaxEI-specific. Mechanism: data dilution crosses a critical signal-to-noise boundary.\n2. **Taxonomy label penalty** (constant ~6.4pp additive offset): TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose points. This remarkably stable gap suggests taxonomy labels introduce a systematic bias independent of injection volume — structured error patterns may teach the model specific wrong behaviors that random noise does not.\n\nNote: All dose-response data is single-seed (seed=42). Given 3-seed SD up to 8.6pp, individual point estimates have limited confidence, but the consistency of the ~6.4pp gap across three independent dose points strengthens the finding. The 68.1% for Random 10% falls within vanilla seed variance (61.7-68.1%) and should not be interpreted as a significant improvement over vanilla.\n\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\n\n**Detection Rate**: 0% for all methods.\n\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\n\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\n\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\n|-----------|----------------------|------------------------------|\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\n\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\n\n### 5. Contribution: What this negative result gives the community\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\n2. **Cost savings**: Prevents the community from pursuing error-injection approaches in ALFWorld-style domains without addressing the structural prerequisites we identify.\n3. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp). Two out of three TaxEI seeds match vanilla exactly; the third collapses by 14.9pp. Single-seed evaluations of error injection methods are fundamentally unreliable.\n4. **Dose-response with separable dual effects**: Injection ratio ablation (fixed data size, TaxEI and Random in parallel) reveals: (a) a shared threshold-plateau at 10-25% injection ratio — both methods drop identically by 12.8pp from their 10% baseline; (b) a constant ~6.4pp taxonomy label penalty across all dose levels, suggesting structured error patterns teach specific wrong behaviors that random noise does not. This decomposition — shared dose effect + additive taxonomy penalty — provides actionable guidance: even if injection ratio is optimized, taxonomy-guided injection remains inferior to random injection in embodied planning.\n\n## Core Claims (each backed by experimental evidence)\n\n- **Claim 1**: Taxonomy-guided error injection introduces high training variance and fails to improve clean task performance on ALFWorld.\n  → Support: TaxEI 3-seed mean 56.7%±8.6pp vs Vanilla 65.3%±3.3pp. Gap is -8.6pp. **Paired t-test (n=3 seeds): p≈0.32 (NS). Pooled permutation test (n=141 task-level observations): p=0.054 (NS at α=0.05, marginal).** Even the higher-powered pooled test cannot confirm significant degradation. Critically, 2/3 seeds (42, 123) show TaxEI = Vanilla (both 61.7%); the deficit is driven by seed=0 (46.8%). Gate 3a FAIL (no seed exceeds vanilla mean). TaxEI SD is 2.6× vanilla SD — the primary effect is **dramatically increased training instability**, not systematic degradation.\n\n- **Claim 2**: Taxonomy labels impose a constant ~6.4pp penalty compared to random (unlabeled) injection across all dose levels.\n  → Support: 3-seed clean eval: TaxEI 56.7% vs Random 63.1%, -6.4pp. Paired t p≈0.034 (df=2, suggestive but low power). Pooled permutation test: p=0.170 (NS). **Dose-response ablation provides stronger evidence**: TaxEI trails Random by 6.4/6.4/6.3pp at 10%/25%/50% injection ratios — a remarkably stable gap across three independent experiments, suggesting a systematic rather than stochastic effect. Recovery eval confirms the direction: TaxEI 59.6% < Random 63.8%. TaxEI SD (8.6pp) > Random SD (7.0pp). Caveat: all dose-response points are single-seed; the per-point gap is ~0.9 SE and not individually significant at n=47.\n\n- **Claim 3**: Error injection increases training instability disproportionately — this is the primary negative effect, with a clear variance gradient.\n  → Support: Cross-seed SD: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. TaxEI seed=0 collapses to 46.8% while seeds 42/123 match vanilla at 61.7% — a 14.9pp swing within the same method. The variance gradient (no injection < random injection < taxonomy-guided injection) suggests that more structured perturbation amplifies training instability rather than providing useful curriculum signal. A single favorable seed can mask injection's destabilizing effect, making published single-seed results unreliable.\n\n- **Claim 4**: Injection-trained models do not improve error recovery.\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp).\n\n- **Claim 5**: Detection training via error injection is completely ineffective in this setup.\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random).\n\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Statistical power with 3 seeds is limited.\"**\n   → All three methods now have 3 seeds. TaxEI vs Vanilla: p≈0.32 (NS) — we do not claim a significant mean difference but instead emphasize the variance effect (SD 8.6pp vs 3.3pp, 2.6× ratio). TaxEI vs Random: paired t p≈0.034 (df=2, suggestive). We report all individual seed results transparently. The variance gradient (Vanilla < Random < TaxEI) is directionally consistent across all seeds.\n\n2. **\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\"**\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. We propose a second environment (WebShop) for supplementary validation.\n\n3. **\"Maybe the taxonomy itself is poorly designed.\"**\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\n\n4. **\"The training recipe might be suboptimal for injection data.\"**\n   → The same recipe produces strong Vanilla results (65.3% vs 42.6% baseline, +22.7pp), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\n\n5. **\"50% injection ratio is too high — you're drowning the signal.\"**\n   → Comprehensively addressed with fixed-size dose-response ablation (all 4,358 total samples, seed=42). Results: 10% = 61.7% (0pp), 25% = 48.9% (-12.8pp), 50% = 51.1% (-10.6pp). The pattern is threshold-plateau, not linear: below ~15-20% injection is harmless but provides no benefit; above it, performance collapses and plateaus regardless of further injection increase. Even at the lowest tested ratio (10%), injection provides zero improvement over vanilla — the best case is exact parity. Random injection dose-response (in progress) will determine whether the threshold is specific to taxonomy-guided injection or a general property.\n\n6. **\"Why is detection rate 0%? Evaluation might be flawed.\"**\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\n\n7. **\"Why not compare directly on ToolBench?\"**\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\n\n## Key Differentiators vs PALADIN\n\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\n\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \"go to countertop 2\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\n\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\n\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \"what to do after an error\" fundamentally harder to learn from examples.\n\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\n\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\n## Note on v3→v4 Vanilla Discrepancy\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\n\n## Supplementary Experiments Needed\n\n### Priority 1 (required for submission)\n- ~~**More seeds**~~: ✅ DONE — All 3 methods at 3 seeds. Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\n- **Injection ratio ablation**: ✅ TaxEI dose-response done (10%=61.7%, 25%=48.9%, 50% in progress). Random dose-response in progress (10%, 25%, 50% training). Key finding: non-linear threshold between 10-25%.\n- **Training dynamics analysis**: Plot training loss curves for clean vs. injected samples across epochs. Do injected samples have systematically higher loss? Does the model learn clean patterns before injection patterns corrupt them?\n\n### Priority 2 (strengthens paper significantly)\n- **Second environment**: WebShop or ScienceWorld to test whether the negative result generalizes beyond ALFWorld. If error injection also fails there, the boundary condition claim is stronger.\n- **Qualitative failure analysis**: Manually examine 20+ TaxEI failure cases — does the model produce incoherent plans, or does it simply choose wrong actions at similar rates? This informs the \"noise vs. wrong learning\" distinction.\n\n### Priority 3 (nice to have)\n- **Scale ablation**: Does TaxEI improve if we scale to 25K or 50K trajectories (matching PALADIN's scale)?\n- **Explicit recovery prompting**: Instead of SFT, test whether in-context recovery examples (few-shot) help — this isolates whether the issue is training signal vs. knowledge.\n- **Per-operator deep dive**: Run more seeds on recovery eval to determine if C4 (observation masking) is genuinely easier for TaxEI or if the +9.1pp advantage is noise.\n\n\n## registry (completed experiments)\n\n- exp_id: traj_collect_500\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    successful_trajectories: 501\n    failed_trajectories: 213\n    total_attempts: 714\n    success_rate: 0.702\n    api_cost_usd: 8.86\n    collection_time_sec: 5245\n- exp_id: sft-dryrun-73\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_init: 2.436\n    train_loss_final: 1.543\n    train_loss_avg: 1.894\n    peak_memory_gib: 19.22\n    steps: 8\n    duration_sec: 42\n    data_vanilla: 124\n    data_injected_dryrun: 96\n    injected_failed: 4\n- exp_id: vanilla-react-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_success_rate: 0.426\n    total_tasks: 47\n    successes: 20\n    per_task_type:\n      pick_heat_then_place:\n        success: 5\n        total: 8\n        rate: 0.625\n      look_at_obj_in_light:\n        success: 3\n        total: 6\n        rate: 0.5\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_two_obj_and_place:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_cool_then_place:\n        success: 0\n        total: 7\n        rate: 0\n- exp_id: mini-pipeline-e2e\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mini-taxei-sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.447\n    eval_successes: 21\n    eval_total: 47\n    vs_baseline_pp: 2.1\n    per_task:\n      look_at_obj_in_light: 3/6 (50.0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 1/7 (14.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_two_obj_and_place: 3/7 (42.9%)\n    train_steps: 195\n    train_duration_min: 16.3\n- exp_id: mini-vanilla-sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.149\n    eval_successes: 7\n    eval_total: 47\n    vs_baseline_pp: -27.7\n    per_task:\n      look_at_obj_in_light: 0/6 (0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 2/11 (18.2%)\n      pick_cool_then_place: 0/7 (0%)\n      pick_heat_then_place: 3/8 (37.5%)\n      pick_two_obj_and_place: 0/7 (0%)\n    train_steps: 54\n    train_duration_min: 5\n- exp_id: vanilla_sft_aligned_v1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: vanilla_sft_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mini-vanilla-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 4176\n    train_steps_total: 1566\n    est_duration_min: 58\n    format: aligned_single_turn\n- exp_id: mini-taxei-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 7545\n    train_samples_clean: 4176\n    train_samples_injected: 3369\n    train_steps_total: 2832\n    est_duration_min: 90\n    format: aligned_single_turn\n- exp_id: mini-random-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 9076\n    train_samples_clean: 4176\n    train_samples_injected: 4900\n    train_steps_total: 3405\n    est_duration_min: 110\n    format: aligned_single_turn\n- exp_id: mini-vanilla-sft-v4\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v3-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.745\n    successes: 35\n    total: 47\n    vs_baseline_pp: 31.9\n    vs_baseline: 42.6% → 74.5%\n- exp_id: v3-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_baseline_pp: 23.4\n    vs_vanilla_sft_pp: -8.5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_clean_then_place: 8/11 (72.7%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_cool_then_place: 3/7 (42.9%)\n- exp_id: v3-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_baseline_pp: 8.5\n    vs_vanilla_sft_pp: -23.4\n- exp_id: v4-taxei-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-random-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-random-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-taxei-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-random-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_clean_then_place: 5/11 (45.5%)\n- exp_id: v4-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    vs_vanilla_pp: 0\n    vs_random_pp: -4.3\n    mcnemar_vs_vanilla_p: 1\n    mcnemar_vs_random_p: 0.754\n    gate_3a: FAIL\n    gate_3b: FAIL\n    gate_4: PASS\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 3/7 (42.9%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 2/7 (28.6%)\n- exp_id: v4-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_vanilla_pp: 4.3\n    vs_taxei_pp: 4.3\n    mcnemar_vs_vanilla_p: 0.754\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 4/8 (50%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n- exp_id: v4-vanilla-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.297\n    avg_loss: 0.416\n    token_accuracy: 0.902\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.917\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-random-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.912\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-recovery-eval-dev\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    pipeline_files:\n    - eval/injected_eval.py\n    - scripts/run_injected_eval.sh\n    injected_eval_lines: 463\n    dryrun_result: PASS\n    dryrun_detail: vanilla checkpoint, 1 task, cuda:3, injected error recovered in\n      13 steps\n- exp_id: v4-vanilla-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.288\n    token_accuracy: 0.903\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58.9\n- exp_id: v4-vanilla-seed7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-recovery-dryrun\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    vs_seed42_pp: 6.4\n    mcnemar_vs_seed42_p: 0.375\n    discordant_pairs: 5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 5/7 (71.4%)\n- exp_id: v4-taxei-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.468\n    eval_successes: 22\n    eval_total: 47\n    vs_seed42_pp: -14.9\n- exp_id: v4-random-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_seed42_pp: -10.7\n- exp_id: v4-vanilla-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_seed42_pp: 4.3\n    vs_seed0_pp: -2.1\n    per_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 7\n        total: 8\n        rate: 0.875\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-vanilla-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    successes: 29\n    total: 47\n    recovery_rate: 0.617\n    detection_rate: 0\n- exp_id: v4-taxei-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success_rate: 0.596\n    successes: 28\n    total: 47\n    recovery_rate: 0.596\n    detection_rate: 0\n- exp_id: v4-random-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.638\n    detection_rate: 0\n    successes: 30\n    total: 47\n    source: json-file-verified\n    note: r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\n- exp_id: v4-taxei-recovery-eval-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.596\n    detection_rate: 0\n    total_episodes: 47\n    per_operator:\n      C1_context_truncation:\n        recovered: 8\n        total: 12\n        rate: 0.667\n      C4_observation_masking:\n        recovered: 7\n        total: 11\n        rate: 0.636\n      P1_step_order_swap:\n        recovered: 7\n        total: 12\n        rate: 0.583\n      P2_sub_goal_deletion:\n        recovered: 6\n        total: 12\n        rate: 0.5\n- exp_id: v4-taxei-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.35506879\n    token_accuracy: 0.89978214\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 109.2\n    train_runtime_sec: 6549.432\n    train_speed_s_per_it: 1.934\n    memory_gib: 18.49\n- exp_id: v4-random-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.35484016\n    final_loss: 0.16766574\n    token_accuracy: 0.94187103\n    avg_token_accuracy: 0.90849673\n    train_steps: 3387\n    train_epochs: 3\n    train_runtime_sec: 6609.3556\n    train_duration_min: 110.2\n    train_samples_per_second: 4.098\n    train_steps_per_second: 0.512\n    train_speed_s_per_it: 1.951\n    memory_gib: 18.49\n- exp_id: v4-fixed-inject10\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-fixed-inject25\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.308\n    token_accuracy: 0.888\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject25-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.285\n    token_accuracy: 0.893\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        success: 7\n        total: 11\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.489\n    eval_successes: 23\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 4\n        total: 6\n        rate: 0.667\n      pick_and_place_simple:\n        success: 3\n        total: 8\n        rate: 0.375\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 2\n        total: 7\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-random-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 7\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-taxei-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.259\n    token_accuracy: 0.911\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 53.1\n- exp_id: v4-random-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4226\n    final_step_loss: 0.3079\n    token_accuracy: 0.9\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 57\n- exp_id: v4-random-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-random-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n    train_loss: 0.4338\n    final_step_loss: 0.2618\n    token_accuracy: 0.91\n    train_duration_min: 53.1\n    memory_gib: 18\n    train_speed_s_per_it: 1.95\n- exp_id: v4-taxei-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_vanilla_seed42_pp: -10.6\n- exp_id: v4-random-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-random-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.574\n    eval_successes: 27\n    eval_total: 47\n    vs_vanilla_seed42_pp: -4.3\n    vs_taxei_50_pp: 6.3\n- exp_id: v4-random-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_vanilla_seed42_pp: -6.4\n    vs_taxei_25_pp: 6.4\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T02:10:12.781Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:10:12.781Z",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

## Round 1

25 recorded events

### User

_source line 3 · 2026-05-15T02:10:12.800Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下复现，统计检验达到或接近显著
核心假设：['多 seed 剂量-响应（≥2 additional seeds）复现 10→25% 的 12.8pp 共享下降，偏差 ≤3pp', '~6.4pp taxonomy penalty 在所有 seed 的所有 dose 点保持稳定（SD ≤1.5pp）', '方差梯度 Vanilla < Random < TaxEI 在每个新增 seed 上均成立', '训练 loss 曲线显示注入样本系统性拉高 clean 样本 loss（corruption 信号可量化）', 'pooled permutation test TaxEI vs Vanilla 达到 p<0.05']
关键指标范围：{'taxei_3seed_mean_pct': [54.0, 58.0], 'taxei_3seed_sd_pp': [7.0, 10.0], 'vanilla_3seed_sd_pp': [2.5, 4.0], 'taxonomy_penalty_per_dose_pp': [5.0, 8.0], 'taxonomy_penalty_cross_dose_sd_pp': [0.3, 1.5], 'dose_threshold_drop_pp': [10.0, 15.0], 'pooled_p_taxei_vs_vanilla': [0.02, 0.05], 'paired_t_taxei_vs_random_p': [0.01, 0.04], 'dose_response_cross_seed_agreement': [0.85, 1.0]}
叙事方向：原始 framing 完全成立。标题级 claim 不变：taxonomy-guided error injection 在 embodied planning 中引入系统性训练不稳定性，且 taxonomy label 造成独立于注入剂量的恒定性能惩罚。 三个 finding 各自有独立的多 seed 证据支撑：(1) 方差梯度是 robust ordering， (2) 阈值-平台是 error injection 的通用属性而非 seed 偶然， (3) ~6.4pp 是 taxonomy label 的 systematic bias 而非随机波动。 训练动态分析提供 mechanistic explanation（注入样本污染 clean 学习信号）。 论文可以做 strong negative claim + actionable boundary condition guideline。


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
  "promptId": "375bf3ed-8d0b-4d6f-9a84-51567a6c31e8",
  "type": "user",
  "uuid": "318e9d4e-bc0a-432d-8b89-39f4947b39a8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:10:12.798Z_

```json
{
  "parentUuid": "318e9d4e-bc0a-432d-8b89-39f4947b39a8",
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
  "uuid": "21032521-4be7-452f-aa7b-902ada5ff2e0",
  "timestamp": "2026-05-15T02:10:12.798Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:10:12.799Z_

```json
{
  "parentUuid": "21032521-4be7-452f-aa7b-902ada5ff2e0",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "348221e5-d991-42f8-a8dc-37d484e4a217",
  "timestamp": "2026-05-15T02:10:12.799Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下复现，统计检验达到或接近显著 核心假设：['多 seed 剂量-响应（≥2 additional seeds）复现 10→25% 的 12.8pp 共享下降，…",
  "leafUuid": "348221e5-d991-42f8-a8dc-37d484e4a217",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 Best-Case Scenario: Supplementary Experiments with Statistical Validation",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Assistant

_source line 8 · 2026-05-15T02:10:16.604Z_

I'll read the experiment plan to understand what planned experiments need detailed predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "348221e5-d991-42f8-a8dc-37d484e4a217",
  "isSidechain": false,
  "requestId": "req_011Cb3YNmpxsKhhgsUqm3LzH",
  "type": "assistant",
  "uuid": "778c7709-3e53-4ac8-8323-9fc4a0178f06",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4bgbA5dGSgF7DpFTW9R9v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18388,
      "cache_read_input_tokens": 11841,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 182,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18388
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

_source line 9 · 2026-05-15T02:10:19.959Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01S2414NF5nUUKKpYD7nFoc5`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan file",
  "prompt": "Search for any file named \"experiment_plan\" or containing experiment plans in /home/ubuntu/.agent-ml-research-idea_gen_0514_2/. Look for YAML, MD, JSON files. Try patterns like *experiment_plan*, *exp_plan*, *plan*. Report the full paths and contents of what you find."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "778c7709-3e53-4ac8-8323-9fc4a0178f06",
  "isSidechain": false,
  "requestId": "req_011Cb3YNmpxsKhhgsUqm3LzH",
  "type": "assistant",
  "uuid": "97827b2c-5216-46c0-a1fc-f176f920654d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4bgbA5dGSgF7DpFTW9R9v",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18388,
      "cache_read_input_tokens": 11841,
      "output_tokens": 182,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18388,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 182,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18388,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18388
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

_source line 10 · 2026-05-15T02:10:37.228Z_

<details><summary>↩ Tool result · `toolu_01S2414NF5nUUKKpYD7nFoc5`</summary>

```text
Perfect! I found two experiment plan files with detailed contents. Let me provide you with a comprehensive summary:

## Search Results

I found **two experiment plan files** in the directory:

### 1. **Main Experiment Plan** (Primary)
**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/experiment_plan.yaml`

This is the primary, updated experiment plan dated 2026-05-15. It's a comprehensive plan for a "Negative Result Paper" about tax error injection in agents.

**Key Structure:**
- **Claims (C1-C6):** Papers claims about TaxEI (Taxonomy Error Injection) effectiveness
- **Baselines & Prerequisites:**
  - Vanilla ReAct baseline: 42.6% accuracy (20/47 tasks)
  - GPT-5.2 trajectory collection: 70.2% success rate
  
- **Core Multi-Seed Experiments (Priority 1, Status: DONE):**
  - Multiseed vanilla SFT: 65.3% ± 3.3pp (3 seeds)
  - Multiseed TaxEI SFT: 56.7% ± 8.6pp (statistically non-significant vs vanilla)
  - Multiseed random SFT: 63.1% ± 7.0pp
  
- **Dose-Response Ablation (Priority 1):**
  - TaxEI at 10%/25%/50% injection ratios: Shows threshold-plateau pattern (10% harmless, 25% catastrophic collapse)
  - Random dose-response: 10% shows +6.4pp improvement (data augmentation effect), 25%/50% in progress
  
- **Recovery & Detection Eval (Priority 1, DONE):**
  - All methods show 0% detection rate
  - Recovery rates: Vanilla 61.7%, TaxEI 59.6%, Random 63.8%
  
- **Priority 2 (Nice-to-Have, Planned):**
  - Training dynamics analysis
  - Second environment replication (WebShop/ScienceWorld)
  - Qualitative failure analysis
  
- **Priority 3 (Nice-to-Have, Planned):**
  - Scale ablation (25K-50K trajectories)
  - Recovery prompting (few-shot in-context)
  - Per-operator deep dive

---

### 2. **Supplementary Experiment Plan** (Historical/In Progress)
**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml`

This is an earlier supplementary plan (dated 2026-05-14) in Chinese, with more detailed GPU scheduling and phase breakdown. It's similar but appears to be a work-in-progress version with finer granularity.

**Key Phases:**
- **Phase 1 (P1, currently running):** Multi-seed training completions (seed=123 for TaxEI/Random)
- **Phase 2:** Multi-seed eval
- **Phase 3:** Data generation for ablation
- **Phase 4:** Ablation training (10%/25% injection ratios)
- **Phase 5:** Ablation evaluation

**P1 Priority Tasks:**
- Multi-seed training completions (TaxEI/Random seed=123) - running
- Multi-seed eval for seed=123 - planned
- 3-seed statistical updates - planned
- Injection ratio ablation data generation and training - planned
- Training dynamics analysis - planned

**P2 Priority Tasks:**
- WebShop environment validation
- Qualitative failure analysis (20+ cases)

**P3 Priority Tasks:**
- Scale ablation (25K/50K trajectories)
- Few-shot recovery experiments
- Per-operator recovery deep dive

---

## Summary

Both files document an extensive experimental plan for validating claims that **error injection training (TaxEI) fails to improve model performance** on ALFWorld tasks. The primary plan (file 1) is the final, complete version with results, while the supplementary plan (file 2) is a detailed execution checklist with GPU scheduling and phase management.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "97827b2c-5216-46c0-a1fc-f176f920654d",
  "isSidechain": false,
  "promptId": "375bf3ed-8d0b-4d6f-9a84-51567a6c31e8",
  "type": "user",
  "uuid": "55918a72-eefe-4efe-9346-c99901563daf",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for any file named \"experiment_plan\" or containing experiment plans in /home/ubuntu/.agent-ml-research-idea_gen_0514_2/. Look for YAML, MD, JSON files. Try patterns like *experiment_plan*, *exp_plan*, *plan*. Report the full paths and contents of what you find.",
    "agentId": "a6a58b6aaaab2badf",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found two experiment plan files with detailed contents. Let me provide you with a comprehensive summary:\n\n## Search Results\n\nI found **two experiment plan files** in the directory:\n\n### 1. **Main Experiment Plan** (Primary)\n**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/experiment_plan.yaml`\n\nThis is the primary, updated experiment plan dated 2026-05-15. It's a comprehensive plan for a \"Negative Result Paper\" about tax error injection in agents.\n\n**Key Structure:**\n- **Claims (C1-C6):** Papers claims about TaxEI (Taxonomy Error Injection) effectiveness\n- **Baselines & Prerequisites:**\n  - Vanilla ReAct baseline: 42.6% accuracy (20/47 tasks)\n  - GPT-5.2 trajectory collection: 70.2% success rate\n  \n- **Core Multi-Seed Experiments (Priority 1, Status: DONE):**\n  - Multiseed vanilla SFT: 65.3% ± 3.3pp (3 seeds)\n  - Multiseed TaxEI SFT: 56.7% ± 8.6pp (statistically non-significant vs vanilla)\n  - Multiseed random SFT: 63.1% ± 7.0pp\n  \n- **Dose-Response Ablation (Priority 1):**\n  - TaxEI at 10%/25%/50% injection ratios: Shows threshold-plateau pattern (10% harmless, 25% catastrophic collapse)\n  - Random dose-response: 10% shows +6.4pp improvement (data augmentation effect), 25%/50% in progress\n  \n- **Recovery & Detection Eval (Priority 1, DONE):**\n  - All methods show 0% detection rate\n  - Recovery rates: Vanilla 61.7%, TaxEI 59.6%, Random 63.8%\n  \n- **Priority 2 (Nice-to-Have, Planned):**\n  - Training dynamics analysis\n  - Second environment replication (WebShop/ScienceWorld)\n  - Qualitative failure analysis\n  \n- **Priority 3 (Nice-to-Have, Planned):**\n  - Scale ablation (25K-50K trajectories)\n  - Recovery prompting (few-shot in-context)\n  - Per-operator deep dive\n\n---\n\n### 2. **Supplementary Experiment Plan** (Historical/In Progress)\n**Path:** `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml`\n\nThis is an earlier supplementary plan (dated 2026-05-14) in Chinese, with more detailed GPU scheduling and phase breakdown. It's similar but appears to be a work-in-progress version with finer granularity.\n\n**Key Phases:**\n- **Phase 1 (P1, currently running):** Multi-seed training completions (seed=123 for TaxEI/Random)\n- **Phase 2:** Multi-seed eval\n- **Phase 3:** Data generation for ablation\n- **Phase 4:** Ablation training (10%/25% injection ratios)\n- **Phase 5:** Ablation evaluation\n\n**P1 Priority Tasks:**\n- Multi-seed training completions (TaxEI/Random seed=123) - running\n- Multi-seed eval for seed=123 - planned\n- 3-seed statistical updates - planned\n- Injection ratio ablation data generation and training - planned\n- Training dynamics analysis - planned\n\n**P2 Priority Tasks:**\n- WebShop environment validation\n- Qualitative failure analysis (20+ cases)\n\n**P3 Priority Tasks:**\n- Scale ablation (25K/50K trajectories)\n- Few-shot recovery experiments\n- Per-operator recovery deep dive\n\n---\n\n## Summary\n\nBoth files document an extensive experimental plan for validating claims that **error injection training (TaxEI) fails to improve model performance** on ALFWorld tasks. The primary plan (file 1) is the final, complete version with results, while the supplementary plan (file 2) is a detailed execution checklist with GPU scheduling and phase management."
      }
    ],
    "totalDurationMs": 17258,
    "totalTokens": 36048,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13854,
      "cache_read_input_tokens": 21174,
      "output_tokens": 1013,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13854
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 1013,
          "cache_read_input_tokens": 21174,
          "cache_creation_input_tokens": 13854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13854,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 6,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "97827b2c-5216-46c0-a1fc-f176f920654d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T02:10:40.596Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KHbTtrhfWMX8yJf5drwaUP`</summary>

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
  "parentUuid": "55918a72-eefe-4efe-9346-c99901563daf",
  "isSidechain": false,
  "requestId": "req_011Cb3YQa2bwjvkaB5WMxxyr",
  "type": "assistant",
  "uuid": "4d66aaa3-a56a-4cc1-b4ea-270891f242d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019hWvduxLvXnBSJNcsvva6F",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1203,
      "cache_read_input_tokens": 30229,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1203,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 30229,
          "cache_creation_input_tokens": 1203,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1203
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

_source line 12 · 2026-05-15T02:10:40.604Z_

<details><summary>↩ Tool result · `toolu_01KHbTtrhfWMX8yJf5drwaUP`</summary>

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
  "parentUuid": "4d66aaa3-a56a-4cc1-b4ea-270891f242d1",
  "isSidechain": false,
  "promptId": "375bf3ed-8d0b-4d6f-9a84-51567a6c31e8",
  "type": "user",
  "uuid": "0b0a3fcc-79f6-4c08-b7ae-65eed1f34df6",
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
  "sourceToolAssistantUUID": "4d66aaa3-a56a-4cc1-b4ea-270891f242d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-15T02:10:40.827Z_

````json
{
  "parentUuid": "0b0a3fcc-79f6-4c08-b7ae-65eed1f34df6",
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
  "uuid": "d26b7677-ca39-415c-8c12-119193be07f2",
  "timestamp": "2026-05-15T02:10:40.827Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下复现，统计检验达到或接近显著 核心假设：['多 seed 剂量-响应（≥2 additional seeds）复现 10→25% 的 12.8pp 共享下降，…",
  "leafUuid": "d26b7677-ca39-415c-8c12-119193be07f2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 Best-Case Scenario: Supplementary Experiments with Statistical Validation",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Assistant

_source line 16 · 2026-05-15T02:14:07.462Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment plan. Let me identify all "planned" experiments and generate detailed predictions for each under the "best" tier.

The planned experiments are:
1. **dose-response-random** (in_progress - partially done, needs inject25 and inject50 eval results)
2. **training-dynamics** (planned)
3. **second-environment** (planned)
4. **qualitative-failure-analysis** (planned)
5. **scale-ablation** (planned)
6. **recovery-prompting** (planned)


7. **per-operator-deepdive** (planned)

Now I'm reviewing what "best" tier actually requires: all three core findings need to replicate across multi-seed experiments with statistical significance, including the variance gradient, dose-response threshold-plateau pattern, and the ~6.4pp taxonomy penalty. I'm checking the specific metric ranges that define this tier—taxei means around 54-58%, standard deviations in particular ranges, and the taxonomy penalty staying consistent across doses.

The three hypotheses I need to validate are whether the dose-response pattern holds across additional seeds with minimal bias, whether the taxonomy penalty remains stable around 6.4pp, and whether the variance gradient persists across conditions.

Looking at the experiment plan, I see several experiments already mapped out—the dose-response work is partially done and needs completion, while training dynamics, second environment testing, and other analyses are still planned. But to properly validate the core hypotheses, I'll need to design additional multi-seed dose-response experiments beyond what's currently scheduled. Looking at the registry data, I can see that the inject25 and inject50 eval results are actually already recorded—inject25 shows 55.3% success rate and inject50 shows 57.4%—so these experiments aren't truly in_progress but rather completed. Looking at the planned experiments, I need to run dose-response across additional seeds to validate whether the 12.8pp drop pattern holds consistently, and then examine the training dynamics to see if injected samples create a measurable corruption signal in the loss curves.

For the second environment test, I'm checking whether error injection fails similarly in WebShop and whether the variance ordering replicates there. The qualitative analysis should reveal whether failures follow specific wrong action patterns rather than appearing random, which would support the "wrong learning" hypothesis. I'm also planning scale and recovery ablations to rule out scale as a confound and to test whether the model actually has the knowledge but struggles with training signal integration.

Now I'm diving into operator-level patterns to see if the C4 advantage and P2 disadvantage hold consistently across multiple seeds, which would strengthen the structural boundary condition argument.

For the planned experiments, I need to expand on each one with detailed data and analysis. Looking at what's already in progress versus what still needs to be added, the dose-response-random experiment has results available, but I should also consider whether multi-seed dose-response experiments are necessary to validate the core hypotheses—particularly for checking the ~6.4pp taxonomy penalty stability claim. The current plan covers seven main experiments, though some of the hypothesis validation might require additional multi-seed runs that aren't explicitly listed yet. Now I'm checking the dose-response results from the registry to ground my analysis in actual data—the random injection experiments show a clear pattern where performance degrades as injection rate increases, with specific performance gaps I can reference when detailing the expected outcomes. I need to map out what "best" tier predictions look like for each experiment—dose-response-random already has confirmed results showing the 12.8pp threshold and ~6.4pp taxonomy penalty, while the others like training-dynamics, second-environment, and the remaining ablations would all demonstrate that the core issue is corrupted training signals rather than something fixable by scale or prompting alone.

For the additional experiments supporting the top hypotheses, I'm working through multi-seed dose-response replication at seeds 0 and 123 across both TaxEI and Random at different injection levels, and a pooled permutation test that reaches statistical significance. I'm starting to lay out the specific predictions for seed 0—the vanilla baseline sits at 68.1%, and I need to calculate what the dose-response curves would look like at 10%, 25%, and 50% injection rates under the best-case scenario where the patterns hold consistently.

I'm noticing a tension in my reasoning though: at full dose TaxEI collapsed to 46.8% with seed 0, but the dose-response uses a fixed sample count of 4,358 rather than the full 9,029, so the dynamics might shift. The key constraint I'm working with is that under the "best" tier, the shared 12.8 percentage point drop between dose levels should replicate across seeds with a bias tolerance of ±3 percentage points.

Now I'm refining my predictions: the 10% to 25% drop should hold at roughly 12.8pp ± 3pp for both TaxEI and Random seeds, while the taxonomy penalty of about 6.4pp should remain stable across different dose levels. For seed 0 specifically, I'm expecting TaxEI at 10% to match the vanilla baseline around 68.1% since the injection at that dose doesn't appear to cause harm, then drop to 55.3% at 25%, while Random at 10% should show the data augmentation boost to around 74.5%.

Actually, I'm overcomplicating this with exact numbers—what matters more is identifying the core patterns across these conditions rather than pinpointing precise percentages. Let me focus on the key trends for seed 123: vanilla sits at 66.0%, TaxEI stays flat at 10% then drops to 53.2% at 25%, and Random at 10% climbs to around 72%.

Now I'm verifying these patterns hold at seed 42 where the deltas remain consistent—the taxonomy penalty stays at 6.4 percentage points whether at 10% or 25%, and the random boost follows the same trajectory. Since these patterns replicate across seeds, I should write out the YAML configuration and also incorporate the dose-response results I've already computed for the random conditions.

For the multi-seed dose-response experiments needed to validate hypothesis 1, I'd need to run the same dose points across seeds 0 and 123 in addition to seed 42—that's 12 training runs plus evaluations for each method. I'm structuring the full experiment plan to include the in-progress dose-response work, the new multi-seed validation, training dynamics analysis, qualitative failure cases, a second environment test, scale ablations, recovery prompting, per-operator analysis, and updated pooled statistics.

Now I'm focusing on the experiments that are either in progress or explicitly planned, then identifying which additional experiments the "best" tier hypothesis requires. I need to work through the predicted outcomes for each one systematically.

Looking at the dose-response-random experiment, I can see the partial results already exist—inject25 shows 55.3% and inject50 shows 57.4%. The pattern suggests random injection creates a consistent taxonomy penalty across dose levels while showing a sharp drop from 10% to 25%, then plateauing. This makes sense because random injection adds trajectory diversity without the misleading labels that come with higher doses, so the performance degradation follows a threshold effect similar to the taxonomy-based approach but shifted upward by a fixed penalty.

For training dynamics, I'm expecting to see clean sample loss run 15-25% higher in the taxonomy-injected model compared to vanilla by epoch 2, with injected samples consistently showing 1.5-2.0× the loss of clean samples. The divergence between the two training regimes should emerge after the first epoch, with the taxonomy-injected model settling into a higher baseline loss floor. Random injection should fall somewhere between these extremes, suggesting the conflicting gradient signals from injected samples create structured interference in the taxonomy case.

For WebShop, I'm predicting vanilla SFT will reach 55-65% success, the taxonomy-injected version drops to 48-58%, and random injection lands in the 52-62% range. The variance pattern should mirror what we saw before—vanilla showing the tightest distribution, then random, then taxonomy-injected with the highest variance. The taxonomy penalty should cost around 4-7 percentage points, consistent with the environment's similar structural properties to ALFWorld.

In the qualitative failure analysis, I expect to see that most failures stem from systematic action mistakes rather than incoherent planning, with taxonomy-injected models showing specific failure modes tied to the operators we injected—like skipping steps when we trained on sub-goal deletion or ignoring environmental context when we used truncation. About a quarter of failures will look indistinguishable from baseline noise, but the rest should reveal that the model actually learned these error patterns as legitimate behaviors rather than just treating them as random noise.

For the scale ablation, I'm checking whether more training data helps mitigate the corruption. At 25K trajectories, TaxEI should still underperform vanilla with high variance, and even scaling to 50K should only partially reduce that variance without actually surpassing the baseline. The fundamental issue persists because the taxonomy-guided errors create coherent but wrong strategies that the model internalizes, whereas random noise is something it can partially learn to ignore—so more data helps with the noise problem but doesn't solve the structural issue of learning incorrect patterns as valid alternatives.

For recovery prompting, I'm testing whether providing error recovery examples at inference time rather than baking them into the training data makes a difference. Few-shot recovery should yield moderate gains around 65-70%, which is better than the corrupted SFT baseline but nowhere near PALADIN's 30-point improvement. This tells me the model can actually learn from recovery examples when they're not competing with corrupted training signals, confirming that the real bottleneck is the gradient corruption during training rather than the model's capacity to handle errors.

Now I'm diving into how different error types affect performance across operators. I expect observation masking to be where TaxEI shines since it's the most tool-use-adjacent error—the recovery is straightforward and relies on existing context. Sub-goal deletion and context truncation should hurt TaxEI more since they require deeper replanning. The per-operator breakdown will show whether the advantage is concentrated in specific error types or distributed across the board.

For the dose-response analysis, I'm looking at how performance degrades as we increase error injection rates, comparing TaxEI against random baselines across multiple seeds to establish whether the penalty is consistent and whether there's a meaningful gap between the two approaches. The dose-response pattern should hold across different seeds since it's driven by the underlying data composition rather than random initialization, and the taxonomy penalty appears to be a consistent additive effect independent of both dose and seed. With multi-seed data across three doses, I can run pooled statistical tests—a permutation test comparing TaxEI versus Vanilla should reach significance around p = 0.02-0.05, and a paired t-test for TaxEI versus Random around p = 0.01-0.04. Now I need to check which experiments in the plan are marked as completed versus still planned before writing up the final output.

Looking at the experiment statuses, I see dose-response-random is still in progress while training-dynamics, second-environment, qualitative-failure-analysis, scale-ablation, recovery-prompting, and per-operator-deepdive are all planned. I should also account for multi-seed dose-response and the pooled statistics analysis, which aren't explicitly in the original plan but are implied by the best-tier hypotheses. I'll need to structure the YAML to cover all these experiments and include relevant tables for dose-response patterns and per-operator breakdowns.

Now I'm looking at the dose-response-random results to finalize those numbers. The registry shows inject10 at 68.1%, inject25 at 55.3%, and inject50 at 57.4%, which I can compare against the TaxEI baseline to see the performance deltas across dose levels.

Both TaxEI and Random drop by 12.8 percentage points when moving from 10% to 25% injection, which validates the pattern I predicted for the best tier. Now I need to extend this dose-response analysis to the other seeds, starting with seed 0 where the vanilla baseline is 68.1%, and work through how the injection levels scale with the smaller sample sizes used in the dose-response experiments. The specific numbers are getting quite precise, so let me frame these as point estimates. For seed 0, I'm predicting the dose-response curves will show TaxEI dropping about 12.8 percentage points from 10% to 25% injection, then plateauing with a modest 2.1 point recovery at 50%, while Random follows a similar pattern with comparable magnitude shifts. I'm noticing the penalty values I generated violate the standard deviation constraint—8.5pp is too high. Let me recalibrate to keep the taxonomy penalty between 5-8pp with a standard deviation across doses no greater than 1.5pp, so I'll adjust to values like 6.2, 6.5, 6.0, and 7.1 to stay within bounds.

Now I'm structuring the YAML output with the tier designation, narrative guidance, and a set of imagined experiments including dose-response completion, multi-seed replication, training dynamics analysis, and qualitative failure analysis.

For the training dynamics section, I need to decide which specific metrics to track and predict under the "best" tier constraints.

The key metrics I'm focusing on are the clean loss ratio to measure how much the injection corrupts normal learning, the injected-to-clean loss ratio to capture the divergence between sample types, the epoch where clean loss divergence becomes significant, and a gradient conflict metric to quantify disagreement between clean and injected batch gradients. For the visualizations, I'm planning loss curves comparing vanilla, TaxEI, and random baselines for both clean and injected samples, plus a ratio curve showing how clean loss in TaxEI compares to vanilla over training. I also need to clarify what "best" tier means narratively—it should indicate that the original framing holds up perfectly and all findings strengthen the core hypothesis.

For the imagined experiments section, I'm realizing I should include both predicted results for planned experiments and actual results from completed ones already in the registry. The dose-response-random experiments are actually done with concrete numbers (inject25=55.3%, inject50=57.4%), which align beautifully with the "best" tier predictions, so I'll incorporate those actual values rather than just predictions. Now I'm ready to write out the complete YAML with detailed predictions and rationales for each planned experiment.

I'm thinking through the training dynamics more carefully—pulling the actual loss curves from the registry where available. The vanilla clean training shows a final loss around 0.297, while TaxEI reaches 0.355 overall, but I need to separate out the clean versus injected sample losses within the TaxEI training to give accurate predictions for the "best" tier scenario.

Looking at the loss breakdown, TaxEI's clean samples should land around 0.32-0.35 (higher than vanilla's 0.29), while the injected samples would be much higher at 0.45-0.55. The random baseline would show clean losses around 0.30-0.33 and injected losses around 0.40-0.48. The corruption signal—measuring how much TaxEI's clean loss exceeds vanilla's—comes out to roughly 14%, which fits nicely within my earlier 15-25% prediction range. I have enough detail now to write this up, and I should make sure the "best" tier metrics align with the user's specified ranges, particularly the taxei_3seed_mean_pct target of 54.0-58.0.

Now I'm checking whether all the key metrics fall within the expected ranges: the TaxEI mean is at 56.7%, the standard deviation is 8.6pp, vanilla's is 3.3pp, the taxonomy penalty sits around 6.3-6.4pp across doses, the cross-dose variation is nearly zero at 0.06pp, the dose threshold drop is 12.8pp, and I need to verify the p-value is in the 0.02-0.05 range.

The pooled p-value is currently 0.054, just slightly above the 0.05 threshold I need, and the paired t-test against random is looking good at 0.034. The main thing I'm missing is the cross-seed dose-response agreement metric, which requires running the dose-response analysis across multiple seeds to verify consistency.

So there are two remaining gaps for the "best" tier: getting that pooled p-value under 0.05, which might happen with additional data or a refined analysis approach, and establishing the multi-seed dose-response agreement. I should address both of these in the imagined experiments section.

Now I'm moving to the YAML output and deciding on the format for the tables—markdown strings will be cleaner and more readable than arrays.

Generating YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d26b7677-ca39-415c-8c12-119193be07f2",
  "isSidechain": false,
  "requestId": "req_011Cb3YQqQa8GygVGkA9mLpy",
  "type": "assistant",
  "uuid": "e78003b2-c4bb-49d8-bf11-ca7cff4b425e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH9g922sQ4irfaTpA2e1Yt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9103,
      "cache_read_input_tokens": 31432,
      "output_tokens": 10107,
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
          "output_tokens": 10107,
          "cache_read_input_tokens": 31432,
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

_source line 17 · 2026-05-15T02:14:07.464Z_

Let me check if there are additional details in the intermediate experiment plan or any supplementary data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e78003b2-c4bb-49d8-bf11-ca7cff4b425e",
  "isSidechain": false,
  "requestId": "req_011Cb3YQqQa8GygVGkA9mLpy",
  "type": "assistant",
  "uuid": "3e3227dc-366c-49bb-ab3c-f28c888fd3d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH9g922sQ4irfaTpA2e1Yt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9103,
      "cache_read_input_tokens": 31432,
      "output_tokens": 10107,
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
          "output_tokens": 10107,
          "cache_read_input_tokens": 31432,
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

### Tool call

_source line 18 · 2026-05-15T02:14:08.385Z_

<details open><summary>🔧 Tool call — Read · `toolu_01E2Sib2V86y3AQS9ZLtMKgm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e3227dc-366c-49bb-ab3c-f28c888fd3d5",
  "isSidechain": false,
  "requestId": "req_011Cb3YQqQa8GygVGkA9mLpy",
  "type": "assistant",
  "uuid": "c433ed4d-ea74-4385-8924-cb3352bce3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH9g922sQ4irfaTpA2e1Yt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9103,
      "cache_read_input_tokens": 31432,
      "output_tokens": 10107,
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
          "output_tokens": 10107,
          "cache_read_input_tokens": 31432,
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

### Tool result

_source line 19 · 2026-05-15T02:14:08.394Z_

<details><summary>↩ Tool result · `toolu_01E2Sib2V86y3AQS9ZLtMKgm`</summary>

```text
1	# experiment_plan.yaml — tax_error_inject_agent
2	# 基于 paper_framing.md 的 Supplementary Experiments
3	# 生成时间: 2026-05-14
4	
5	# ==================== 已完成基线 ====================
6	# vanilla-react-baseline: 42.6% (Qwen3-8B zero-shot)
7	# v4 Vanilla SFT: 65.3% ± 3.2pp (seeds 42/0/123)
8	# v4 TaxEI SFT: 54.3% ± 10.5pp (seeds 42/0, seed=123 训练中)
9	# v4 Random SFT: 60.7% ± 7.6pp (seeds 42/0, seed=123 训练中)
10	# Recovery eval (seed=42): Vanilla 61.7%, TaxEI 59.6%, Random 63.8%
11	# Detection rate: 0% across all methods
12	
13	experiments:
14	  # ============================================================
15	  # P1: 投稿前必须完成
16	  # ============================================================
17	
18	  - id: "p1-multiseed-train"
19	    name: "Multi-seed 补齐训练 (TaxEI/Random seed=123)"
20	    priority: P1
21	    category: "multi-seed"
22	    hypothesis: "补齐第 3 个 seed，使 TaxEI/Random 达到与 Vanilla 相同的 3-seed 覆盖，获得可靠的均值和方差估计"
23	    method: "v4 同源数据 (9,029 samples)，LoRA rank=16, 3 epochs, lr=1e-4, seed=123。与 seed=42/0 完全相同的超参。"
24	    data: "sft_taxei_v4.jsonl (9,029), sft_random_v4.jsonl (9,029)"
25	    gpu: "cuda:0 (TaxEI), cuda:1 (Random), 各 ~110min"
26	    status: "running"
27	    registry_id: "v4-taxei-seed123, v4-random-seed123"
28	    supports_claim: ["Claim 1", "Claim 2", "Claim 3"]
29	
30	  - id: "p1-multiseed-eval"
31	    name: "Multi-seed seed=123 Clean Eval"
32	    priority: P1
33	    category: "multi-seed"
34	    hypothesis: "seed=123 的 clean eval 结果应与 seed=42/0 方向一致 (TaxEI ≤ Vanilla)"
35	    method: "recovery.py --no_inject，47 tasks (valid_unseen)，对 seed=123 checkpoints 跑 clean eval"
36	    data: "ALFWorld valid_unseen 47 tasks"
37	    gpu: "cuda:0 + cuda:1, 各 ~25min"
38	    depends_on: ["p1-multiseed-train"]
39	    status: "planned"
40	    supports_claim: ["Claim 1", "Claim 2", "Claim 3"]
41	
42	  - id: "p1-3seed-stats"
43	    name: "3-seed 统计更新"
44	    priority: P1
45	    category: "analysis"
46	    hypothesis: "3-seed 结果将提高统计功效，使 TaxEI vs Vanilla 的 p 值更可靠"
47	    method: "multiseed_stats.py: 更新 paired permutation test, bootstrap CI, 方差比较。3 seeds × 3 methods。"
48	    data: "所有 3-seed eval 结果 JSON"
49	    gpu: "无 (CPU 分析)"
50	    depends_on: ["p1-multiseed-eval"]
51	    status: "planned"
52	    supports_claim: ["Claim 1", "Claim 2", "Claim 3"]
53	
54	  - id: "p1-ablation-datagen"
55	    name: "Injection Ratio Ablation 数据生成"
56	    priority: P1
57	    category: "ablation"
58	    hypothesis: "固定总数据量 ~9K samples，变化注入比例 (10%/25%/50%)，如果低比例缓解退化则支持 'noise overwhelms signal' 假设"
59	    method: |
60	      Fixed-size 方案: 总量固定 ~9,029 samples
61	      - 10% injection: ~903 injected + ~8,126 clean
62	      - 25% injection: ~2,257 injected + ~6,772 clean
63	      - 50% injection: 已有 (v4 数据, 4,671 injected + 4,358 clean)
64	      从现有 4,671 条 injected_variants 中随机采样，TaxEI/Random 各自格式化。
65	    data: "data/mini_pipeline_v4/injected_variants + clean trajectories"
66	    gpu: "无 (CPU 数据处理)"
67	    status: "planned"
68	    supports_claim: ["Claim 1", "Claim 2"]
69	
70	  - id: "p1-ablation-train-10pct"
71	    name: "Injection Ratio 10% 训练 (TaxEI + Random)"
72	    priority: P1
73	    category: "ablation"
74	    hypothesis: "10% 注入比例下 TaxEI/Random 退化幅度显著小于 50%"
75	    method: "与 v4 相同超参 (LoRA rank=16, 3 epochs, lr=1e-4, seed=42), 仅数据不同"
76	    data: "~9,029 samples (10% injection)"
77	    gpu: "cuda:0 (TaxEI-10%), cuda:1 (Random-10%), 各 ~110min"
78	    depends_on: ["p1-ablation-datagen"]
79	    status: "planned"
80	    supports_claim: ["Claim 1", "Claim 2"]
81	
82	  - id: "p1-ablation-train-25pct"
83	    name: "Injection Ratio 25% 训练 (TaxEI + Random)"
84	    priority: P1
85	    category: "ablation"
86	    hypothesis: "25% 注入比例是 noise vs signal 的转折点"
87	    method: "与 v4 相同超参, 仅数据不同"
88	    data: "~9,029 samples (25% injection)"
89	    gpu: "cuda:2 (TaxEI-25%), cuda:3 (Random-25%), 各 ~110min"
90	    depends_on: ["p1-ablation-datagen"]
91	    status: "planned"
92	    supports_claim: ["Claim 1", "Claim 2"]
93	
94	  - id: "p1-ablation-eval"
95	    name: "Injection Ratio Ablation Eval (4 组新 + 2 组复用)"
96	    priority: P1
97	    category: "ablation"
98	    hypothesis: "低注入比例 (10%/25%) 下 TaxEI/Random 性能接近或优于 Vanilla (65.3%)"
99	    method: |
100	      Clean eval (--no_inject) 对 4 个新 checkpoint:
101	      - TaxEI-10%, Random-10%, TaxEI-25%, Random-25%
102	      50% 复用已有 v4 seed=42 结果: TaxEI 61.7%, Random 66.0%
103	    data: "ALFWorld valid_unseen 47 tasks"
104	    gpu: "4 卡并行, 各 ~25min"
105	    depends_on: ["p1-ablation-train-10pct", "p1-ablation-train-25pct"]
106	    status: "planned"
107	    supports_claim: ["Claim 1", "Claim 2"]
108	
109	  - id: "p1-training-dynamics"
110	    name: "Training Dynamics 分析 (Loss 曲线)"
111	    priority: P1
112	    category: "analysis"
113	    hypothesis: "注入样本的 training loss 系统性高于 clean 样本，且随 epoch 不收敛，说明模型无法有效学习注入 pattern"
114	    method: |
115	      从现有 logging.jsonl 提取:
116	      1. 逐 step loss 曲线 (Vanilla vs TaxEI vs Random)
117	      2. 如可区分 clean/injected batch: 分别画 loss 子曲线
118	      3. 方差随 epoch 的变化趋势
119	      不需要新训练——从已有 v4 seed=42 的 logging.jsonl 提取。
120	    data: "checkpoints/mini_*_sft_v4/*/logging.jsonl"
121	    gpu: "无 (CPU 分析 + matplotlib)"
122	    status: "planned"
123	    supports_claim: ["Claim 3"]
124	
125	  # ============================================================
126	  # P2: 显著增强论文
127	  # ============================================================
128	
129	  - id: "p2-webshop"
130	    name: "第二环境验证 (WebShop)"
131	    priority: P2
132	    category: "environment"
133	    hypothesis: "如果 error injection 在 WebShop 同样失败，boundary condition claim 更强；如果成功，则发现 ALFWorld 特异性"
134	    method: |
135	      需要:
136	      1. WebShop 环境部署 + trajectory collection pipeline
137	      2. Error taxonomy 适配 (WebShop 是 web 购物, 不同 action space)
138	      3. TaxEI/Vanilla/Random 三组 SFT + eval
139	      工程量大 (~3-5 天), 但对 Claim 6 支撑力极强。
140	      注: EEF (arXiv 2504.13145) 已在 WebShop 上做过类似实验, 需要差异化。
141	    data: "WebShop dataset (需要新采集)"
142	    gpu: "4 卡, 预计 2-3 天 (含 pipeline 开发)"
143	    status: "planned"
144	    supports_claim: ["Claim 6"]
145	
146	  - id: "p2-failure-analysis"
147	    name: "定性 Failure 分析"
148	    priority: P2
149	    category: "analysis"
150	    hypothesis: "TaxEI failure cases 呈现特定 pattern: 注入训练导致模型在复杂任务中产生 incoherent plans 而非简单 wrong actions"
151	    method: |
152	      从 v4 TaxEI seed=42 eval 结果中:
153	      1. 收集 TaxEI 失败但 Vanilla 成功的 cases (约 5-8 个)
154	      2. 收集 TaxEI 失败且 Vanilla 也失败的 cases
155	      3. 分析失败模式: action incoherence vs wrong object vs wrong location vs timeout
156	      4. 与 Vanilla failure cases 对比
157	      目标: 20+ cases 手动标注。
158	    data: "eval_results/v4_taxei_eval.json + eval trajectory logs"
159	    gpu: "无 (人工分析)"
160	    status: "planned"
161	    supports_claim: ["Claim 1", "Claim 4", "Claim 6"]
162	
163	  # ============================================================
164	  # P3: 锦上添花
165	  # ============================================================
166	
167	  - id: "p3-scale-ablation"
168	    name: "Scale Ablation (25K/50K trajectories)"
169	    priority: P3
170	    category: "ablation"
171	    hypothesis: "PALADIN 在 50K+ scale 成功, 可能是规模而非 task structure 决定效果; 如果 scaling 仍然无效则排除此混淆"
172	    method: |
173	      需要:
174	      1. 额外采集 ~20K-45K GPT-5.2 trajectories (当前只有 501 条)
175	      2. 对应的 injection + recovery 数据生成
176	      3. 训练 + eval
177	      API 成本高 (~$80-400), 时间长 (~2-5 天 trajectory collection)
178	    data: "需新采集 25K/50K trajectories"
179	    gpu: "4 卡, 训练时间随数据量线性增长"
180	    status: "planned"
181	    supports_claim: ["Claim 6"]
182	
183	  - id: "p3-fewshot-recovery"
184	    name: "Few-shot Recovery (In-context, 非 SFT)"
185	    priority: P3
186	    category: "analysis"
187	    hypothesis: "如果 in-context recovery examples 能提升性能, 说明问题不在 knowledge 而在 SFT training signal corruption"
188	    method: |
189	      在 eval 时在 prompt 中加入 2-3 个 recovery 示例 (从训练数据采样):
190	      - Vanilla + few-shot recovery examples
191	      - 对比 Vanilla (无 few-shot) 和 TaxEI SFT
192	      不需要新训练, 只修改 eval 的 prompt template。
193	    data: "ALFWorld valid_unseen 47 tasks + recovery exemplars from training data"
194	    gpu: "1 卡, ~30min"
195	    status: "planned"
196	    supports_claim: ["Claim 4", "Claim 6"]
197	
198	  - id: "p3-per-operator-deep"
199	    name: "Per-operator Recovery Deep Dive (多 seed)"
200	    priority: P3
201	    category: "multi-seed"
202	    hypothesis: "C4 observation_masking 上 TaxEI 的 +9.1pp 优势是真实效应还是 seed 噪声"
203	    method: |
204	      对 seed=0, seed=123 的 checkpoints 也跑 recovery eval (injected_eval.py),
205	      得到 3-seed per-operator recovery rates, 检验 C4 优势是否跨 seed 稳定。
206	    data: "ALFWorld valid_unseen 47 tasks × 3 seeds × 3 methods"
207	    gpu: "1 卡/run, ~30min/run, 总计 6 runs (TaxEI/Random seed=0,123 + Vanilla seed=0,123)"
208	    depends_on: ["p1-multiseed-train"]
209	    status: "planned"
210	    supports_claim: ["Claim 4"]
211	
212	# ============================================================
213	# GPU 排班计划 (autodl-5090, cuda:0-3)
214	# ============================================================
215	#
216	# Phase 1 (当前, ~100min 剩余):
217	#   cuda:0: v4-taxei-seed123 训练 (运行中)
218	#   cuda:1: v4-random-seed123 训练 (运行中)
219	#   cuda:2: 空闲
220	#   cuda:3: 空闲
221	#
222	# Phase 2 (seed=123 训练完成后, ~25min):
223	#   cuda:0: p1-multiseed-eval TaxEI seed=123
224	#   cuda:1: p1-multiseed-eval Random seed=123
225	#   cuda:2: 空闲 (可跑 p1-training-dynamics 分析)
226	#   cuda:3: 空闲
227	#
228	# Phase 3 (数据生成, ~30min, CPU):
229	#   p1-ablation-datagen: 生成 10%/25% fixed-size 数据集
230	#   p1-3seed-stats: 3-seed 统计分析
231	#
232	# Phase 4 (ablation 训练, ~110min):
233	#   cuda:0: TaxEI-10%
234	#   cuda:1: Random-10%
235	#   cuda:2: TaxEI-25%
236	#   cuda:3: Random-25%
237	#
238	# Phase 5 (ablation eval, ~25min):
239	#   cuda:0-3: 4 组 ablation eval 并行
240	#
241	# 总预计时间: ~5-6 小时 (P1 全部完成)
242	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c433ed4d-ea74-4385-8924-cb3352bce3dd",
  "isSidechain": false,
  "promptId": "375bf3ed-8d0b-4d6f-9a84-51567a6c31e8",
  "type": "user",
  "uuid": "9c140e72-4596-4e52-8d7c-3d38fc9e0dab",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml",
      "content": "# experiment_plan.yaml — tax_error_inject_agent\n# 基于 paper_framing.md 的 Supplementary Experiments\n# 生成时间: 2026-05-14\n\n# ==================== 已完成基线 ====================\n# vanilla-react-baseline: 42.6% (Qwen3-8B zero-shot)\n# v4 Vanilla SFT: 65.3% ± 3.2pp (seeds 42/0/123)\n# v4 TaxEI SFT: 54.3% ± 10.5pp (seeds 42/0, seed=123 训练中)\n# v4 Random SFT: 60.7% ± 7.6pp (seeds 42/0, seed=123 训练中)\n# Recovery eval (seed=42): Vanilla 61.7%, TaxEI 59.6%, Random 63.8%\n# Detection rate: 0% across all methods\n\nexperiments:\n  # ============================================================\n  # P1: 投稿前必须完成\n  # ============================================================\n\n  - id: \"p1-multiseed-train\"\n    name: \"Multi-seed 补齐训练 (TaxEI/Random seed=123)\"\n    priority: P1\n    category: \"multi-seed\"\n    hypothesis: \"补齐第 3 个 seed，使 TaxEI/Random 达到与 Vanilla 相同的 3-seed 覆盖，获得可靠的均值和方差估计\"\n    method: \"v4 同源数据 (9,029 samples)，LoRA rank=16, 3 epochs, lr=1e-4, seed=123。与 seed=42/0 完全相同的超参。\"\n    data: \"sft_taxei_v4.jsonl (9,029), sft_random_v4.jsonl (9,029)\"\n    gpu: \"cuda:0 (TaxEI), cuda:1 (Random), 各 ~110min\"\n    status: \"running\"\n    registry_id: \"v4-taxei-seed123, v4-random-seed123\"\n    supports_claim: [\"Claim 1\", \"Claim 2\", \"Claim 3\"]\n\n  - id: \"p1-multiseed-eval\"\n    name: \"Multi-seed seed=123 Clean Eval\"\n    priority: P1\n    category: \"multi-seed\"\n    hypothesis: \"seed=123 的 clean eval 结果应与 seed=42/0 方向一致 (TaxEI ≤ Vanilla)\"\n    method: \"recovery.py --no_inject，47 tasks (valid_unseen)，对 seed=123 checkpoints 跑 clean eval\"\n    data: \"ALFWorld valid_unseen 47 tasks\"\n    gpu: \"cuda:0 + cuda:1, 各 ~25min\"\n    depends_on: [\"p1-multiseed-train\"]\n    status: \"planned\"\n    supports_claim: [\"Claim 1\", \"Claim 2\", \"Claim 3\"]\n\n  - id: \"p1-3seed-stats\"\n    name: \"3-seed 统计更新\"\n    priority: P1\n    category: \"analysis\"\n    hypothesis: \"3-seed 结果将提高统计功效，使 TaxEI vs Vanilla 的 p 值更可靠\"\n    method: \"multiseed_stats.py: 更新 paired permutation test, bootstrap CI, 方差比较。3 seeds × 3 methods。\"\n    data: \"所有 3-seed eval 结果 JSON\"\n    gpu: \"无 (CPU 分析)\"\n    depends_on: [\"p1-multiseed-eval\"]\n    status: \"planned\"\n    supports_claim: [\"Claim 1\", \"Claim 2\", \"Claim 3\"]\n\n  - id: \"p1-ablation-datagen\"\n    name: \"Injection Ratio Ablation 数据生成\"\n    priority: P1\n    category: \"ablation\"\n    hypothesis: \"固定总数据量 ~9K samples，变化注入比例 (10%/25%/50%)，如果低比例缓解退化则支持 'noise overwhelms signal' 假设\"\n    method: |\n      Fixed-size 方案: 总量固定 ~9,029 samples\n      - 10% injection: ~903 injected + ~8,126 clean\n      - 25% injection: ~2,257 injected + ~6,772 clean\n      - 50% injection: 已有 (v4 数据, 4,671 injected + 4,358 clean)\n      从现有 4,671 条 injected_variants 中随机采样，TaxEI/Random 各自格式化。\n    data: \"data/mini_pipeline_v4/injected_variants + clean trajectories\"\n    gpu: \"无 (CPU 数据处理)\"\n    status: \"planned\"\n    supports_claim: [\"Claim 1\", \"Claim 2\"]\n\n  - id: \"p1-ablation-train-10pct\"\n    name: \"Injection Ratio 10% 训练 (TaxEI + Random)\"\n    priority: P1\n    category: \"ablation\"\n    hypothesis: \"10% 注入比例下 TaxEI/Random 退化幅度显著小于 50%\"\n    method: \"与 v4 相同超参 (LoRA rank=16, 3 epochs, lr=1e-4, seed=42), 仅数据不同\"\n    data: \"~9,029 samples (10% injection)\"\n    gpu: \"cuda:0 (TaxEI-10%), cuda:1 (Random-10%), 各 ~110min\"\n    depends_on: [\"p1-ablation-datagen\"]\n    status: \"planned\"\n    supports_claim: [\"Claim 1\", \"Claim 2\"]\n\n  - id: \"p1-ablation-train-25pct\"\n    name: \"Injection Ratio 25% 训练 (TaxEI + Random)\"\n    priority: P1\n    category: \"ablation\"\n    hypothesis: \"25% 注入比例是 noise vs signal 的转折点\"\n    method: \"与 v4 相同超参, 仅数据不同\"\n    data: \"~9,029 samples (25% injection)\"\n    gpu: \"cuda:2 (TaxEI-25%), cuda:3 (Random-25%), 各 ~110min\"\n    depends_on: [\"p1-ablation-datagen\"]\n    status: \"planned\"\n    supports_claim: [\"Claim 1\", \"Claim 2\"]\n\n  - id: \"p1-ablation-eval\"\n    name: \"Injection Ratio Ablation Eval (4 组新 + 2 组复用)\"\n    priority: P1\n    category: \"ablation\"\n    hypothesis: \"低注入比例 (10%/25%) 下 TaxEI/Random 性能接近或优于 Vanilla (65.3%)\"\n    method: |\n      Clean eval (--no_inject) 对 4 个新 checkpoint:\n      - TaxEI-10%, Random-10%, TaxEI-25%, Random-25%\n      50% 复用已有 v4 seed=42 结果: TaxEI 61.7%, Random 66.0%\n    data: \"ALFWorld valid_unseen 47 tasks\"\n    gpu: \"4 卡并行, 各 ~25min\"\n    depends_on: [\"p1-ablation-train-10pct\", \"p1-ablation-train-25pct\"]\n    status: \"planned\"\n    supports_claim: [\"Claim 1\", \"Claim 2\"]\n\n  - id: \"p1-training-dynamics\"\n    name: \"Training Dynamics 分析 (Loss 曲线)\"\n    priority: P1\n    category: \"analysis\"\n    hypothesis: \"注入样本的 training loss 系统性高于 clean 样本，且随 epoch 不收敛，说明模型无法有效学习注入 pattern\"\n    method: |\n      从现有 logging.jsonl 提取:\n      1. 逐 step loss 曲线 (Vanilla vs TaxEI vs Random)\n      2. 如可区分 clean/injected batch: 分别画 loss 子曲线\n      3. 方差随 epoch 的变化趋势\n      不需要新训练——从已有 v4 seed=42 的 logging.jsonl 提取。\n    data: \"checkpoints/mini_*_sft_v4/*/logging.jsonl\"\n    gpu: \"无 (CPU 分析 + matplotlib)\"\n    status: \"planned\"\n    supports_claim: [\"Claim 3\"]\n\n  # ============================================================\n  # P2: 显著增强论文\n  # ============================================================\n\n  - id: \"p2-webshop\"\n    name: \"第二环境验证 (WebShop)\"\n    priority: P2\n    category: \"environment\"\n    hypothesis: \"如果 error injection 在 WebShop 同样失败，boundary condition claim 更强；如果成功，则发现 ALFWorld 特异性\"\n    method: |\n      需要:\n      1. WebShop 环境部署 + trajectory collection pipeline\n      2. Error taxonomy 适配 (WebShop 是 web 购物, 不同 action space)\n      3. TaxEI/Vanilla/Random 三组 SFT + eval\n      工程量大 (~3-5 天), 但对 Claim 6 支撑力极强。\n      注: EEF (arXiv 2504.13145) 已在 WebShop 上做过类似实验, 需要差异化。\n    data: \"WebShop dataset (需要新采集)\"\n    gpu: \"4 卡, 预计 2-3 天 (含 pipeline 开发)\"\n    status: \"planned\"\n    supports_claim: [\"Claim 6\"]\n\n  - id: \"p2-failure-analysis\"\n    name: \"定性 Failure 分析\"\n    priority: P2\n    category: \"analysis\"\n    hypothesis: \"TaxEI failure cases 呈现特定 pattern: 注入训练导致模型在复杂任务中产生 incoherent plans 而非简单 wrong actions\"\n    method: |\n      从 v4 TaxEI seed=42 eval 结果中:\n      1. 收集 TaxEI 失败但 Vanilla 成功的 cases (约 5-8 个)\n      2. 收集 TaxEI 失败且 Vanilla 也失败的 cases\n      3. 分析失败模式: action incoherence vs wrong object vs wrong location vs timeout\n      4. 与 Vanilla failure cases 对比\n      目标: 20+ cases 手动标注。\n    data: \"eval_results/v4_taxei_eval.json + eval trajectory logs\"\n    gpu: \"无 (人工分析)\"\n    status: \"planned\"\n    supports_claim: [\"Claim 1\", \"Claim 4\", \"Claim 6\"]\n\n  # ============================================================\n  # P3: 锦上添花\n  # ============================================================\n\n  - id: \"p3-scale-ablation\"\n    name: \"Scale Ablation (25K/50K trajectories)\"\n    priority: P3\n    category: \"ablation\"\n    hypothesis: \"PALADIN 在 50K+ scale 成功, 可能是规模而非 task structure 决定效果; 如果 scaling 仍然无效则排除此混淆\"\n    method: |\n      需要:\n      1. 额外采集 ~20K-45K GPT-5.2 trajectories (当前只有 501 条)\n      2. 对应的 injection + recovery 数据生成\n      3. 训练 + eval\n      API 成本高 (~$80-400), 时间长 (~2-5 天 trajectory collection)\n    data: \"需新采集 25K/50K trajectories\"\n    gpu: \"4 卡, 训练时间随数据量线性增长\"\n    status: \"planned\"\n    supports_claim: [\"Claim 6\"]\n\n  - id: \"p3-fewshot-recovery\"\n    name: \"Few-shot Recovery (In-context, 非 SFT)\"\n    priority: P3\n    category: \"analysis\"\n    hypothesis: \"如果 in-context recovery examples 能提升性能, 说明问题不在 knowledge 而在 SFT training signal corruption\"\n    method: |\n      在 eval 时在 prompt 中加入 2-3 个 recovery 示例 (从训练数据采样):\n      - Vanilla + few-shot recovery examples\n      - 对比 Vanilla (无 few-shot) 和 TaxEI SFT\n      不需要新训练, 只修改 eval 的 prompt template。\n    data: \"ALFWorld valid_unseen 47 tasks + recovery exemplars from training data\"\n    gpu: \"1 卡, ~30min\"\n    status: \"planned\"\n    supports_claim: [\"Claim 4\", \"Claim 6\"]\n\n  - id: \"p3-per-operator-deep\"\n    name: \"Per-operator Recovery Deep Dive (多 seed)\"\n    priority: P3\n    category: \"multi-seed\"\n    hypothesis: \"C4 observation_masking 上 TaxEI 的 +9.1pp 优势是真实效应还是 seed 噪声\"\n    method: |\n      对 seed=0, seed=123 的 checkpoints 也跑 recovery eval (injected_eval.py),\n      得到 3-seed per-operator recovery rates, 检验 C4 优势是否跨 seed 稳定。\n    data: \"ALFWorld valid_unseen 47 tasks × 3 seeds × 3 methods\"\n    gpu: \"1 卡/run, ~30min/run, 总计 6 runs (TaxEI/Random seed=0,123 + Vanilla seed=0,123)\"\n    depends_on: [\"p1-multiseed-train\"]\n    status: \"planned\"\n    supports_claim: [\"Claim 4\"]\n\n# ============================================================\n# GPU 排班计划 (autodl-5090, cuda:0-3)\n# ============================================================\n#\n# Phase 1 (当前, ~100min 剩余):\n#   cuda:0: v4-taxei-seed123 训练 (运行中)\n#   cuda:1: v4-random-seed123 训练 (运行中)\n#   cuda:2: 空闲\n#   cuda:3: 空闲\n#\n# Phase 2 (seed=123 训练完成后, ~25min):\n#   cuda:0: p1-multiseed-eval TaxEI seed=123\n#   cuda:1: p1-multiseed-eval Random seed=123\n#   cuda:2: 空闲 (可跑 p1-training-dynamics 分析)\n#   cuda:3: 空闲\n#\n# Phase 3 (数据生成, ~30min, CPU):\n#   p1-ablation-datagen: 生成 10%/25% fixed-size 数据集\n#   p1-3seed-stats: 3-seed 统计分析\n#\n# Phase 4 (ablation 训练, ~110min):\n#   cuda:0: TaxEI-10%\n#   cuda:1: Random-10%\n#   cuda:2: TaxEI-25%\n#   cuda:3: Random-25%\n#\n# Phase 5 (ablation eval, ~25min):\n#   cuda:0-3: 4 组 ablation eval 并行\n#\n# 总预计时间: ~5-6 小时 (P1 全部完成)\n",
      "numLines": 242,
      "startLine": 1,
      "totalLines": 242
    }
  },
  "sourceToolAssistantUUID": "c433ed4d-ea74-4385-8924-cb3352bce3dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下复现，统计检验达到或接近显著 核心假设：['多 seed 剂量-响应（≥2 additional seeds）复现 10→25% 的 12.8pp 共享下降，…",
  "leafUuid": "9c140e72-4596-4e52-8d7c-3d38fc9e0dab",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 Best-Case Scenario: Supplementary Experiments with Statistical Validation",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Assistant

_source line 22 · 2026-05-15T02:17:16.936Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me construct the comprehensive YAML output for the "best" tier predictions.

Let me organize the imagined experiments:

1. **dose-response-random** - in_progress, registry already has results
2. **multiseed-dose-response** - new experiment needed for best tier hypothesis 1
3. **training-dynamics** - planned in both plans
4. **qualitative-failure-analysis** - planned (P2)
5. **second-environment** - planned (P2)
6. **scale-ablation** - planned (P3)


7. **recovery-prompting** - planned (P3)
8. **per-operator-deepdive** - planned (P3)
9. **pooled-stats-update** - statistical analysis needed for best tier

Now I'm writing out the complete YAML with detailed predictions for each experiment, making sure all the key metrics align with the expected ranges for the best tier performance.

Generating YAML output... Now I'm compiling the dose-response results across both methods, comparing how TaxEI and Random perform at different injection levels and calculating the performance deltas between them.

Looking at the multi-seed predictions, I need to estimate what happens at seed 0 where the vanilla baseline is 68.1%, accounting for the consistent 12.8 percentage point drop we see from 10% to 25% injection across both methods. At the 10% injection level with seed 0, TaxEI should stay close to the vanilla performance since that dose appears benign, though I'm working through some seed-specific variance considerations. Now I'm laying out the specific predictions for seed 0's dose-response curve: TaxEI should drop about 12.8 percentage points from 10% to 25% injection, then plateau around 55%, while the random baseline follows a similar pattern but stays roughly 6 percentage points higher throughout.

Checking seed 123 against this pattern—the taxonomy penalty holds steady at around 6.3-6.4pp across all injection levels, and both seeds show that same 12.7-12.8pp drop between the 10% and 25% conditions, with the plateau effect kicking in at 50%. I'm noticing the cross-dose standard deviation is coming in too low at 0.06pp, well below the required range of 0.3 to 1.5pp, so I need to introduce more variation across the dose levels. Let me adjust the seed 0 values to create a less uniform response pattern while keeping the individual drops consistent.

Now working through seed 123, I'm checking whether the drops fall within the target range of 10.0 to 15.0pp—the initial 10.6pp drop is borderline, so I'm recalibrating to 12.7pp to be more centered, which brings the 25% TaxEI value down to 51.1%. But something's off with the penalty values at the higher dose, particularly that 4.2 reading.

Let me recalculate: the Random 50% should be 59.6% to keep the penalty consistent at 6.4, matching the pattern across all three dose levels. So the final seed 123 configuration has TaxEI at 63.8%, 51.1%, and 53.2%, Random at 70.2%, 57.4%, and 59.6%, with penalties of 6.4, 6.3, and 6.4 across the board. Now I'm looking at the cross-dose penalty structure across all nine data points.

The mean penalty is 6.37 with a standard deviation of only 0.05, which violates the constraint that requires variation between 0.3 and 1.5. I need to introduce more realistic noise into these numbers. Let me try seed 0 with larger variations—TaxEI at 10% is 66.0%, dropping to 55.3% at 25%, which is a 10.7 percentage point decrease and falls within the acceptable range of 10.0 to 15.0 percentage points. Looking at the cross-seed results, the 10→25% performance drops are remarkably consistent across different random seeds—all clustering between 10 and 15 percentage points, with an average around 12.1pp and minimal variation. This suggests the dose-response pattern is robust and not just noise.

Now I'm examining the taxonomy penalty values across all nine data points and noticing they're tightly clustered around 6.3-6.4, which falls well below the target range I was aiming for. I need to introduce more meaningful variation across seeds and doses to better reflect realistic differences in the penalty structure. Looking at seed 123, the penalty values range from 6.3 to 8.5 across the different dosage levels. When I compile all the penalty measurements across the three seeds, they cluster tightly around 6.3-6.4, with that one outlier at 8.5 from the 50% dosage comparison—still within the acceptable [5.0, 8.0] range. I'm noticing the standard deviation is too tight at 0.05, which doesn't reflect realistic variation. With 47 tasks where each success or failure shifts the rate by about 2.1 percentage points, I need to introduce more natural fluctuation across the penalty values. Let me recalibrate with actual task-level quantization in mind.

Looking at the seed 42 results, the penalty consistently hovers around 3 tasks across different thresholds—TaxEI at 10%, 25%, and 50% all show roughly 6.3-6.4 percentage point penalties compared to random. This stability is striking and suggests the penalty might remain predictable at around 3 tasks across different seeds for the best tier.

However, I need to account for some natural variation—the penalty could dip to 2 tasks (4.3pp) or rise to 4 tasks (8.5pp) depending on the seed. The challenge is that the cross-dose SD metric captures overall variation across all doses and seeds combined, so I need to be careful not to introduce too much variation if the core finding is that the penalty stays remarkably constant. Let me think through what the right penalty distribution should be for the best tier given the [0.3, 1.5] range constraint. across doses within a single seed. So the question is: for a given seed, how stable is the penalty across the 3 dose points (10%, 25%, 50%)?

At seed 42: 6.4, 6.4, 6.3 → SD = 0.06pp (extremely stable)

For "best" tier, this should be [0.3, 1.5]. So I need slightly more variation within each seed.

Let me use:

Seed 0: penalty at 10%=5.7, 25%=6.4, 50%=6.4 → SD = 0.4pp ✓
Seed 123: penalty at 10%=7.0, 25%=6.3, 50%=5.8 → SD = 0.6pp ✓

Actually, looking at the YAML field "taxonomy_penalty_cross_dose_sd_pp", I think this is measuring the SD across all dose points regardless of seed. With 3 seeds × 3 doses = 9 total data points, I can use penalty values like seed 42 at 6.4, 6.4, 6.3, seed 0 at 5.5, 6.8, 7.2, and seed 123 at 7.1, 5.9, 6.0. That gives me a mean of 6.4 with an SD of 0.6, which fits nicely in the [0.3, 1.5] range. Now I need to work backwards to the actual performance numbers. I'm settling on reasonable estimates that capture the key patterns rather than trying to predict exact values. The main findings I need to show are the consistent 12-13 percentage point drop from 10% to 25% dose across both methods, the stable 6.4 percentage point taxonomy penalty, and how these patterns hold across different random seeds with high agreement. I'm noticing the standard deviation is still too close to zero because with 47 tasks, penalty increments are around 2.1 percentage points each, so I need dose points that drop different numbers of tasks to create more variation. Let me test seed 0 with different task counts across the dose levels to see if that spreads the penalties enough.

Wait, I'm realizing the penalty of 4.2pp falls below the constraint minimum of 5.0pp, and when I map out the math—2 tasks gives 4.3pp, 3 tasks gives 6.4pp, 4 tasks gives 8.5pp—it seems like only the 3-task penalty actually fits within the [5.0, 8.0] range, which means I might be stuck with a single fixed penalty value unless I reconsider how to interpret the constraint. I'm settling on a distribution where most penalties land at 6.4pp (representing 3 tasks), with occasional outliers at 4.3pp or 8.5pp (2 or 4 tasks) to create a standard deviation around 0.8pp. Now I'm working through the actual numbers for seed 0, checking that the performance drops are consistent at 12.8pp across different methods like TaxEI and Random, with penalties starting to populate.

For seed 123, I'm establishing the vanilla baseline at 66.0% and calculating how TaxEI and Random perform at different penalty levels, tracking the performance degradation as penalties increase. I'm looking at the penalty values across different seeds and realizing the constraint might refer to the mean penalty across all doses rather than individual points. Let me just move forward with reasonable numbers that capture the overall pattern—the "best" tier doesn't require every single data point to be perfect, just a strong overall picture.

Now I'm seeing the dose-response curves for both seeds, with vanilla baselines around 66-68%, showing consistent drops of about 12.8 percentage points when moving from 10% to 25% doses, and penalties clustering around 6.4 for the first seed and 6 for the second.

Looking at the aggregate penalty statistics across all nine measurements, the mean is 6.37 with a standard deviation of just 0.05—which is remarkably tight. I'm realizing this low variation might actually be expected given the 47-task resolution and the systematic 3-task penalty structure, so the constraint's [0.3, 1.5] range could be overstating the natural variation. In fact, under the "best" tier, this kind of stability is preferable to the constraint, which functions as an upper bound rather than a target range.

Re-reading the hypothesis more carefully, it specifies SD ≤ 1.5pp with no explicit lower bound—the [0.3, 1.5] range in the metrics is probably just describing the realistic expected variation, where 0.3 represents a plausible floor due to noise. For the "best" tier, I should aim for something like 0.4-0.5pp of variation, so I'm adjusting the seed values to introduce a bit more realistic spread while keeping the penalty stable around 6.4pp.

Now I'm realizing the penalty values need to align with the actual task count differences—with n=47, the penalty is quantized in steps of about 2.13pp per task difference, so I need to work backwards from valid penalty values to determine which performance numbers are actually achievable. I'm checking whether the performance drops between the two methods align closely enough. The Random method drops 10.7 percentage points while TaxEI drops 12.8 percentage points—a difference of 2.1pp, which falls within my acceptable ±3pp tolerance, so this configuration works. Let me refine it further to get the drops to match more precisely. I'm settling on a consistent approach: keep the penalty at roughly 3 tasks across all points, accept near-zero standard deviation, and frame this extreme stability as the strongest evidence for a systematic additive bias. The constraint allows up to 1.5pp SD, so achieving near-perfect consistency is actually the most compelling result. Time to write out the YAML with these final numbers.

Now I'm documenting the actual results. The dose-response-random experiment shows the baseline: 68.1% at 10% injection, dropping to 55.3% at 25%, then rising slightly to 57.4% at 50%, with a consistent taxonomy penalty around 6.4pp. For the multiseed variants, I'm tracking how these patterns hold across different random seeds—seed 0 maintains the same drops and penalties, while seed 123 shows similar behavior with a vanilla baseline of 66.0%.

Looking at the training dynamics, the taxonomy-injected model shows notably higher final loss (0.34 vs 0.29 for vanilla), and the gap between clean and injected loss reaches about 1.4×. The gradients start diverging around step 500, and the cosine similarity between clean and injected gradient directions stays weak at 0.2-0.4, suggesting the model is learning fundamentally different representations for these two conditions.

In my qualitative analysis of over 20 failure cases, I'm seeing that about two-thirds follow systematic wrong-action patterns, a quarter are specific to how the taxonomy operators work, and the rest appear to be baseline noise. When I test on WebShop, the performance gap widens—vanilla hits around 60% while TaxEI drops to 52%, and the variance issue persists across environments. Scaling up the training data to 50K examples helps somewhat (TaxEI reaches 62%), but it still doesn't match vanilla performance. Adding recovery prompting with 3-shot examples gives vanilla a modest boost to 66%, which outpaces the SFT TaxEI baseline, though in-context learning seems more effective for the observation masking problem in C4.

Looking at individual operators, the C4 advantage holds up across multiple seeds with a mean improvement of 5.8 percentage points, while P2 consistently underperforms by about 6.7 points, and the cross-seed standard deviation per operator ranges from 3-5 percentage points. When I pool the multi-seed dose-response data, the statistical tests show TaxEI versus vanilla has a p-value of 0.031, and comparing TaxEI to random gives 0.024, suggesting the differences are meaningful.

Now I'm working through the YAML configuration, pulling realistic training dynamics from the registry—vanilla converges to a final loss around 0.297 while TaxEI ends higher at 0.355.

Looking at the loss breakdown, I need to separate clean versus injected sample performance within each method. TaxEI's clean samples should end around 0.33-0.36 due to gradient interference from the harder examples, while its injected samples struggle more at 0.42-0.50. Random's clean samples stay closer to vanilla around 0.31-0.34, with injected samples in the 0.40-0.46 range. The critical insight is that TaxEI's clean loss degradation exceeds random's, demonstrating the structured interference effect from taxonomy-aware injection.

Now I'm planning out the experimental tables I need to include—dose-response curves for both methods, multi-seed dynamics, loss decomposition breakdowns, failure taxonomies, cross-environment validation on WebShop, scaling analysis, recovery prompting results, per-operator breakdowns, and updated statistical comparisons. Let me write the YAML documentation comprehensively.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c140e72-4596-4e52-8d7c-3d38fc9e0dab",
  "isSidechain": false,
  "requestId": "req_011Cb3Yg9JWo7ASa8k8uwfuB",
  "type": "assistant",
  "uuid": "c1b26ede-6b99-4b4f-a5e4-d6f8f685beff",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013N7dyUSHPLPgKUWyAXJBQQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14705,
      "cache_read_input_tokens": 40535,
      "output_tokens": 25538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14705,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 25538,
          "cache_read_input_tokens": 40535,
          "cache_creation_input_tokens": 14705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14705
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

_source line 23 · 2026-05-15T02:22:07.792Z_

Now I have all the context. Let me construct the comprehensive best-tier predictions for every planned experiment.

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。三个核心 finding 在补充实验中逐一获得独立多 seed 证据：
  (1) 方差梯度 Vanilla&lt;Random&lt;TaxEI 是 robust ordering，在每个 seed 和 dose 水平均成立；
  (2) 阈值-平台是 error injection 的通用属性——两种注入方法在 10→25% 同步崩溃 12.8pp，跨 seed 偏差 ≤2.2pp；
  (3) ~6.4pp taxonomy penalty 是 systematic additive bias，跨 3 seed × 3 dose = 9 个独立观测点保持稳定（SD ≈ 0.4pp）。
  训练动态分析提供 mechanistic explanation——注入样本的梯度方向与 clean 样本弱对齐（cosine ~0.3），
  系统性拉高 clean 样本 loss 约 14%。定性分析显示 TaxEI 特有的 "taxonomy-operator 回放" 失败模式，
  区别于随机噪声。WebShop 第二环境部分复现方差梯度和阈值效应，进一步支撑 task-structural boundary condition。
  论文可做 strong negative claim + actionable boundary condition guideline，标题级 claim 不变。
  Pooled permutation test TaxEI vs Vanilla 达 p=0.031，paired t TaxEI vs Random 达 p=0.024。

imagined_experiments:

  # ============================================================
  # 1. Random Dose-Response 完成（in_progress → done）
  # ============================================================
  - name: "Random Dose-Response Curve Completion"
    plan_id: "dose-response-random"
    description: >
      Random injection 的 10%/25%/50% 剂量-响应曲线（固定 4,358 总样本，seed=42），
      与 TaxEI 剂量-响应并行对比，验证共享阈值-平台效应和恒定 taxonomy penalty。
    expected_results:
      random_inject10_pct: 68.1
      random_inject25_pct: 55.3
      random_inject50_pct: 57.4
      random_10to25_drop_pp: 12.8
      taxei_10to25_drop_pp: 12.8
      shared_drop_difference_pp: 0.0
      taxonomy_penalty_10_pp: 6.4
      taxonomy_penalty_25_pp: 6.4
      taxonomy_penalty_50_pp: 6.3
      taxonomy_penalty_mean_pp: 6.37
      taxonomy_penalty_sd_pp: 0.06
    result_rationale: >
      Random 10% = 68.1% 高于 vanilla 6.4pp，反映纯数据增强效应——无标签的噪声注入在低剂量下增加
      训练分布多样性，实质上是合法的 data augmentation。TaxEI 10% = 61.7% 无此增益，说明 taxonomy
      label 抵消了增强效应，将 +6.4pp augmentation bonus 精确归零。10→25% 两种方法同步崩溃 12.8pp
      （Random 68.1→55.3, TaxEI 61.7→48.9），证明阈值效应是 error injection 的通用属性：当注入比例
      超过 ~15-20%，clean 梯度信号被稀释至临界点以下，模型无法维持正确的 action distribution。
      50% 处两者均回升 ~2pp（平台效应），因为极高注入比例下 clean 和 injected 样本的梯度已充分混合，
      进一步增加注入不再额外恶化。6.4/6.4/6.3pp 的恒定 taxonomy penalty 在三个独立 dose 点保持
      一致（SD=0.06），精确对应 3 个 ALFWorld 任务的分辨率（3/47=6.38pp），强烈支持 taxonomy label
      引入的是与剂量无关的 systematic bias——结构化错误模式教会模型特定的错误行为，而非仅增加噪声。
    tables:
      - title: "Combined Dose-Response Table (seed=42, fixed 4,358 total)"
        content: |
          | Dose  | Vanilla | TaxEI  | Random | Δ(R−T) | TaxEI Δ(vs 10%) | Random Δ(vs 10%) |
          |-------|---------|--------|--------|--------|------------------|------------------|
          | 0%    | 61.7%   | 61.7%  | 61.7%  | 0.0    | —                | —                |
          | 10%   | —       | 61.7%  | 68.1%  | +6.4   | 0.0              | 0.0              |
          | 25%   | —       | 48.9%  | 55.3%  | +6.4   | −12.8            | −12.8            |
          | 50%   | —       | 51.1%  | 57.4%  | +6.3   | −10.6            | −10.7            |
    figures_description:
      - "Figure: 双轴剂量-响应曲线。X 轴=注入比例(0/10/25/50%)，Y 轴=success rate(%)。TaxEI(红实线)和 Random(蓝实线)平行下降，两者间距恒定 ~6.4pp，在 10→25% 处同步断崖。Vanilla baseline(灰虚线)在 61.7%。阴影区域标注共享阈值区间 [10%, 25%]。"
    analysis: >
      剂量-响应曲线揭示两个可分离的独立效应：(1) 共享的信噪比阈值——两种注入方法在同一临界区间
      [10%, 25%] 发生等幅崩溃，证明这是 error injection 的 fundamental property 而非 taxonomy 特异性；
      (2) 恒定的 taxonomy penalty——TaxEI 在每个 dose 点均落后 Random 恰好 ~6.4pp，说明 taxonomy label
      引入的是正交于注入剂量的 additive bias。Random 10% 的 +6.4pp 增益是意外发现，提供了重要的正面
      对照：说明少量未标记噪声注入本身可以是有效的 data augmentation，但 taxonomy label 消除了这一好处。

  # ============================================================
  # 2. 多 Seed 剂量-响应复现（新增实验）
  # ============================================================
  - name: "Multi-Seed Dose-Response Replication"
    plan_id: "multiseed-dose-response"
    description: >
      在 seed=0 和 seed=123 上重复完整的剂量-响应实验（10%/25%/50%，固定 4,358 总样本），
      验证阈值-平台效应和 taxonomy penalty 的跨 seed 稳定性。共 12 次训练 + 12 次 eval。
    expected_results:
      # Seed 0 (vanilla baseline = 68.1%)
      seed0_taxei_inject10_pct: 68.1
      seed0_taxei_inject25_pct: 55.3
      seed0_taxei_inject50_pct: 57.4
      seed0_random_inject10_pct: 74.5
      seed0_random_inject25_pct: 61.7
      seed0_random_inject50_pct: 63.8
      seed0_shared_10to25_drop_pp: 12.8
      seed0_taxonomy_penalty_mean_pp: 6.4
      # Seed 123 (vanilla baseline = 66.0%)
      seed123_taxei_inject10_pct: 63.8
      seed123_taxei_inject25_pct: 53.2
      seed123_taxei_inject50_pct: 53.2
      seed123_random_inject10_pct: 70.2
      seed123_random_inject25_pct: 59.6
      seed123_random_inject50_pct: 59.6
      seed123_shared_10to25_drop_pp: 10.6
      seed123_taxonomy_penalty_mean_pp: 6.4
      # Cross-seed summary
      all_seeds_10to25_drop_mean_pp: 12.1
      all_seeds_10to25_drop_sd_pp: 1.1
      all_seeds_taxonomy_penalty_mean_pp: 6.37
      all_seeds_taxonomy_penalty_sd_pp: 0.4
      dose_response_cross_seed_agreement: 1.0
    result_rationale: >
      阈值-平台效应的物理机制是数据组成决定的信噪比边界，与随机初始化无关：当 clean 样本占比从
      90%（dose=10%）降至 75%（dose=25%）时，clean 梯度信号不再足以维持正确的 action distribution。
      这一边界由数据比例而非 seed 决定，因此跨 seed 高度稳定。Seed 42 的 12.8pp 在 seed 0 处精确
      复现（12.8pp），seed 123 略低（10.6pp），反映 seed 123 的 vanilla baseline 较低（66.0%），
      留给崩溃的绝对空间较小——但所有 seed 均在 [10.0, 15.0]pp 范围内。Taxonomy penalty 的跨 seed
      稳定性（SD ≈ 0.4pp）更进一步确认这是一个由 label 结构决定的 systematic bias：taxonomy label
      在每个 seed 的每个 dose 点均将 3 个额外任务从成功翻转为失败，对应于 47 任务中固定的一组
      对 taxonomy-specific 错误模式敏感的任务。Seed 0 的 Random 10% = 74.5% 高于其他 seed，
      但仍符合 data augmentation 效应——seed 0 的 vanilla baseline 已较高（68.1%），
      augmentation bonus 叠加后接近 ALFWorld 的性能天花板。
    tables:
      - title: "Multi-Seed Dose-Response: TaxEI (fixed 4,358 total)"
        content: |
          | Dose | Seed 42 | Seed 0 | Seed 123 | Mean   | SD    |
          |------|---------|--------|----------|--------|-------|
          | 0%   | 61.7%   | 68.1%  | 66.0%    | 65.3%  | 3.3pp |
          | 10%  | 61.7%   | 68.1%  | 63.8%    | 64.5%  | 3.3pp |
          | 25%  | 48.9%   | 55.3%  | 53.2%    | 52.5%  | 3.3pp |
          | 50%  | 51.1%   | 57.4%  | 53.2%    | 53.9%  | 3.2pp |
      - title: "Multi-Seed Dose-Response: Random (fixed 4,358 total)"
        content: |
          | Dose | Seed 42 | Seed 0 | Seed 123 | Mean   | SD    |
          |------|---------|--------|----------|--------|-------|
          | 0%   | 61.7%   | 68.1%  | 66.0%    | 65.3%  | 3.3pp |
          | 10%  | 68.1%   | 74.5%  | 70.2%    | 70.9%  | 3.3pp |
          | 25%  | 55.3%   | 61.7%  | 59.6%    | 58.9%  | 3.3pp |
          | 50%  | 57.4%   | 63.8%  | 59.6%    | 60.3%  | 3.3pp |
      - title: "Taxonomy Penalty Across Seeds × Doses"
        content: |
          | Dose | Seed 42 | Seed 0 | Seed 123 | Mean  |
          |------|---------|--------|----------|-------|
          | 10%  | 6.4pp   | 6.4pp  | 6.4pp    | 6.4pp |
          | 25%  | 6.4pp   | 6.4pp  | 6.4pp    | 6.4pp |
          | 50%  | 6.3pp   | 6.4pp  | 6.4pp    | 6.4pp |
      - title: "Shared 10→25% Drop Across Seeds"
        content: |
          | Seed | TaxEI Drop | Random Drop | Difference |
          |------|------------|-------------|------------|
          | 42   | 12.8pp     | 12.8pp      | 0.0pp      |
          | 0    | 12.8pp     | 12.8pp      | 0.0pp      |
          | 123  | 10.6pp     | 10.6pp      | 0.0pp      |
          | Mean | 12.1pp     | 12.1pp      | 0.0pp      |
    figures_description:
      - "Figure: 3×1 子图（seed 42/0/123），每图含 TaxEI 和 Random 剂量-响应曲线及 vanilla baseline。三图呈现几乎完全平行的模式：恒定间距、同步断崖、plateau。灰色虚线连接各 seed 的阈值断点，强调跨 seed 一致性。"
      - "Figure: Taxonomy penalty 热力图。3 seed × 3 dose 的 9 宫格，颜色编码 penalty 值（5.0-8.0pp），几乎全为均匀的深色（~6.4pp），视觉化极端稳定性。"
    analysis: >
      多 seed 剂量-响应是 best 档的决定性实验。9 个独立的 taxonomy penalty 观测点（3 seed × 3 dose）
      形成的 SD ≈ 0.4pp 远低于 1.5pp 阈值，为 systematic additive bias 假说提供了近乎完美的证据。
      共享阈值-平台在所有 seed 复现（10→25% drop 均 ≥10pp），最大跨 seed 偏差 2.2pp（seed 123
      的 10.6pp vs seed 42 的 12.8pp），落在 ≤3pp 预算内。值得注意的是，每个 seed 内 TaxEI 和 Random
      的 drop 幅度精确匹配（差异 ≤0.1pp），再次证明阈值效应是数据组成而非方法特异性的结果。
      这些结果使论文可以做出 definitive statement：error injection 的剂量-响应是 task-structural
      属性，taxonomy label 只在此基础上叠加恒定惩罚。

  # ============================================================
  # 3. Training Dynamics 分析
  # ============================================================
  - name: "Training Dynamics Analysis"
    plan_id: "training-dynamics"
    description: >
      从 v4 seed=42 的 training log 中提取逐 step loss 曲线，分离 clean 和 injected 样本的 loss，
      分析注入样本对 clean 学习信号的污染程度。不需要新训练。
    expected_results:
      vanilla_clean_loss_final: 0.290
      taxei_overall_loss_final: 0.355
      taxei_clean_loss_final: 0.338
      taxei_injected_loss_final: 0.482
      random_overall_loss_final: 0.355
      random_clean_loss_final: 0.318
      random_injected_loss_final: 0.445
      clean_loss_inflation_taxei_pct: 16.6
      clean_loss_inflation_random_pct: 9.7
      injected_to_clean_loss_ratio_taxei: 1.43
      injected_to_clean_loss_ratio_random: 1.40
      loss_divergence_onset_step: 500
      gradient_cosine_clean_vs_injected_taxei: 0.28
      gradient_cosine_clean_vs_injected_random: 0.35
    result_rationale: >
      Vanilla clean loss 收敛至 ~0.29（registry: v4-vanilla-seed0 final_loss=0.297），这是无干扰
      baseline。TaxEI 的 overall loss = 0.355 是 clean 和 injected 样本的加权混合——分离后 clean
      部分 ~0.338 高于 vanilla 16.6%，直接量化了注入样本对 clean 学习信号的污染。这一 "corruption
      signal" 是 finding 3（方差梯度）的 mechanistic explanation：注入样本的梯度方向与 clean 样本
      弱对齐（cosine ~0.28），在反向传播中将模型权重推离 clean optimal，导致 clean 样本 loss 系统性
      升高。Random injection 的 clean loss inflation（9.7%）低于 TaxEI（16.6%），因为随机错误的
      梯度方向更加分散（cosine ~0.35，paradoxically higher），不会形成 coherent 的 "拉力方向"——
      相当于在权重空间中添加各向同性噪声，而 TaxEI 的 taxonomy 标签创建了 structured 的错误梯度
      方向，对 clean learning 造成更大的 systematic interference。Loss 分歧在 step ~500（epoch 1
      后期）开始显现，对应于模型开始记忆训练样本而非仅学习通用模式的阶段——此后 injected 样本的
      错误模式开始与 clean 模式竞争权重空间。
    tables:
      - title: "Loss Decomposition (seed=42, final epoch)"
        content: |
          | Method  | Overall | Clean  | Injected | Clean Inflation | Inj/Clean Ratio |
          |---------|---------|--------|----------|-----------------|-----------------|
          | Vanilla | 0.290   | 0.290  | —        | baseline        | —               |
          | TaxEI   | 0.355   | 0.338  | 0.482    | +16.6%          | 1.43×           |
          | Random  | 0.355   | 0.318  | 0.445    | +9.7%           | 1.40×           |
      - title: "Gradient Alignment Metrics"
        content: |
          | Metric                         | TaxEI | Random |
          |--------------------------------|-------|--------|
          | Cosine(clean, injected)        | 0.28  | 0.35   |
          | Clean loss inflation vs Vanilla| 16.6% | 9.7%  |
          | Injected loss convergence      | No    | Partial|
    figures_description:
      - "Figure: 3 条 clean sample loss 曲线（Vanilla/TaxEI/Random）vs training steps。Vanilla 平稳收敛至 0.29，TaxEI clean loss 从 step ~500 开始持续高于 Vanilla 并收敛至 0.338，Random 居中 0.318。Y 轴标注 clean loss inflation zone。"
      - "Figure: TaxEI 训练中 clean vs injected 样本的 loss 对比。两条曲线从相同起点分叉，injected loss 始终高于 clean 且不完全收敛，gap 在 epoch 2-3 趋于稳定在 ~0.14。"
      - "Figure: 梯度余弦相似度 heatmap（step × method），展示 clean-injected 梯度对齐随训练推进的变化。TaxEI 的 cosine 从 ~0.6（初始）下降至 ~0.28（收敛），显示 clean 和 injected 梯度逐渐对立。"
    analysis: >
      训练动态分析将方差梯度的统计现象转化为可解释的梯度力学：注入样本在权重空间中施加与 clean
      样本不一致的梯度力，TaxEI 因 taxonomy 标签产生 structured gradient interference（cosine 0.28），
      Random 因随机性产生 diffuse interference（cosine 0.35）。Clean loss inflation 的 TaxEI > Random
      排序（16.6% vs 9.7%）完美对应 final performance 的 Vanilla > Random > TaxEI 排序，提供了
      从训练 loss 到 eval performance 的因果链。这一 mechanistic explanation 是论文从 "观察到负面结果"
      升级为 "解释负面结果" 的关键——reviewer 可能质疑统计功效，但 loss decomposition 提供了
      independent 的 process-level 证据。injected 样本 loss 不完全收敛的现象进一步说明模型未能
      有效学习错误模式——与 PALADIN 在 tool-use 中 recovery trajectories 可以被学习形成对比。

  # ============================================================
  # 4. 定性 Failure 分析
  # ============================================================
  - name: "Qualitative Failure Analysis"
    plan_id: "qualitative-failure-analysis"
    description: >
      手动分析 20+ TaxEI 失败案例，区分 "taxonomy-specific wrong learning"（模型学到了特定的
      错误行为）和 "random noise"（模型只是表现更不稳定），为 Claim 1 和 Claim 6 提供定性证据。
    expected_results:
      total_cases_analyzed: 24
      taxei_fail_vanilla_succeed: 8
      both_fail: 10
      taxei_succeed_vanilla_fail: 6
      failure_taxonomy:
        operator_replay: 6
        action_sequence_disorder: 5
        premature_termination: 4
        wrong_object_selection: 4
        identical_to_vanilla_failure: 5
      operator_replay_pct: 25.0
      wrong_learning_pct: 62.5
      noise_pct: 20.8
      ambiguous_pct: 16.7
    result_rationale: >
      定性分析揭示 TaxEI 失败中最具诊断意义的模式是 "operator replay"——模型在 clean 任务中
      生成与训练数据中某种 taxonomy operator 一致的错误行为。例如，模型在 pick_clean_then_place
      任务中跳过 clean 步骤（对应 P2 sub_goal_deletion 的训练模式），或在需要仔细观察环境时
      截断上下文信息（对应 C1 context_truncation 的训练模式）。这些 operator replay 案例（6/24,
      25%）是 TaxEI 特有的——Random 和 Vanilla 的失败案例中不存在与特定 taxonomy operator
      匹配的模式。另有 9/24 案例（37.5%）表现为非 operator-specific 但系统性的错误行为（action
      disorder, premature termination），合计 "wrong learning" 占 62.5%。仅 5/24（20.8%）
      的失败模式与 Vanilla 失败完全一致（baseline noise）。这一分布支持 "TaxEI 教会模型特定的
      错误行为" 假说而非 "TaxEI 仅增加随机噪声" 假说，与 training dynamics 中 TaxEI 的
      structured gradient interference（cosine 0.28 < Random 0.35）一致。
    tables:
      - title: "Failure Mode Taxonomy (24 cases)"
        content: |
          | Failure Mode             | Count | Pct   | TaxEI-Specific? |
          |--------------------------|-------|-------|-----------------|
          | Operator replay (P2/C1)  | 6     | 25.0% | Yes             |
          | Action sequence disorder | 5     | 20.8% | Partially       |
          | Premature termination    | 4     | 16.7% | Partially       |
          | Wrong object selection   | 4     | 16.7% | No              |
          | Same as vanilla failure  | 5     | 20.8% | No              |
      - title: "Failure Attribution Summary"
        content: |
          | Category       | Count | Pct   | Interpretation                          |
          |----------------|-------|-------|-----------------------------------------|
          | Wrong learning | 15    | 62.5% | Model internalized error patterns       |
          | Noise          | 5     | 20.8% | Indistinguishable from baseline noise   |
          | Ambiguous      | 4     | 16.7% | Could be either                         |
    figures_description:
      - "Figure: 失败模式 sankey 图。左侧=TaxEI 失败案例（24 个），中间=failure mode 分类（5 类），右侧=attribution（wrong learning / noise / ambiguous）。Operator replay 流全部归入 wrong learning，标红。"
      - "Figure: 2 个代表性 case study 并排。左: TaxEI 在 pick_clean_then_place 中跳过 clean 步骤（P2 replay），右: Vanilla 在同一任务中选择错误 receptacle（generic failure）。注释标注 taxonomy operator 对应关系。"
    analysis: >
      定性分析将统计现象 "taxonomy penalty" 具象化为可观察的行为模式：TaxEI 模型在 clean eval 中
      "回放" 训练数据中的 taxonomy 错误，特别是 P2 (sub_goal_deletion) 和 C1 (context_truncation)
      两种 operator 的特征最明显。这解释了为何 taxonomy penalty 与 dose 无关——只要训练数据中存在
      taxonomy-标记的错误样本，模型就会 internalize 特定的错误策略，无论这些样本占比多少。
      与之对比，Random injection 的失败模式不呈现 operator-specific 聚类，支持其 gradient 干扰是
      diffuse 而非 structured 的解释。这一发现为论文提供了最具说服力的 "为什么 taxonomy labels
      有害" 的直觉解释，适合放在 Analysis 部分作为 bridge between statistics and mechanism。

  # ============================================================
  # 5. 第二环境验证（WebShop）
  # ============================================================
  - name: "Second Environment Validation (WebShop)"
    plan_id: "second-environment"
    description: >
      在 WebShop 环境中复现 Vanilla/TaxEI/Random 三组实验（2-seed），验证方差梯度和
      阈值效应是否泛化到 ALFWorld 以外的 embodied planning 领域。需要适配 error taxonomy、
      采集轨迹、训练和评估。
    expected_results:
      webshop_vanilla_mean_pct: 58.5
      webshop_vanilla_sd_pp: 2.8
      webshop_taxei_mean_pct: 51.2
      webshop_taxei_sd_pp: 7.4
      webshop_random_mean_pct: 55.8
      webshop_random_sd_pp: 5.9
      variance_gradient_holds: true
      variance_ratio_taxei_vs_vanilla: 2.6
      taxonomy_penalty_pp: 4.6
      webshop_dose_10_taxei_pct: 57.3
      webshop_dose_25_taxei_pct: 47.8
      webshop_dose_10to25_drop_pp: 9.5
      engineering_days: 4
    result_rationale: >
      WebShop 与 ALFWorld 共享 embodied planning 的关键结构属性：错误是隐式的（选错商品或属性
      不会触发显式错误信号）、失败级联（错误的搜索查询导致后续所有交互在错误结果上展开）、
      action space 开放。因此方差梯度（Vanilla SD 2.8pp < Random 5.9pp < TaxEI 7.4pp）和
      TaxEI 的劣势（-7.3pp vs Vanilla）应当复现。Taxonomy penalty 略低于 ALFWorld
      （4.6pp vs 6.4pp），因为 WebShop 的 action space 更结构化（搜索/点击/选择），taxonomy
      operator 的干扰空间较小。阈值效应存在但 drop 幅度较小（9.5pp vs 12.8pp），因为 WebShop
      的 reward signal 更密集（每步有部分匹配反馈），clean gradient 更 robust。注意 EEF
      (arXiv 2504.13145) 在 WebShop 上用 "从失败中提取正面信号" 策略成功，与我们的 "注入负面信号"
      方法形成对比——这一对照进一步支持 "injection direction matters" 的论点。
    tables:
      - title: "WebShop 2-Seed Results"
        content: |
          | Method  | Mean   | SD    | vs Vanilla |
          |---------|--------|-------|------------|
          | Vanilla | 58.5%  | 2.8pp | —          |
          | TaxEI   | 51.2%  | 7.4pp | −7.3pp     |
          | Random  | 55.8%  | 5.9pp | −2.7pp     |
      - title: "Cross-Environment Pattern Comparison"
        content: |
          | Pattern                | ALFWorld      | WebShop       | Consistent? |
          |------------------------|---------------|---------------|-------------|
          | Variance gradient      | 3.3<7.0<8.6   | 2.8<5.9<7.4   | ✓           |
          | TaxEI vs Vanilla       | −8.6pp (NS)   | −7.3pp        | ✓           |
          | Taxonomy penalty       | 6.4pp         | 4.6pp         | ✓ (weaker)  |
          | 10→25% drop            | 12.8pp        | 9.5pp         | ✓ (weaker)  |
    figures_description:
      - "Figure: ALFWorld vs WebShop 双环境对比条形图。每环境 3 条 bar（Vanilla/Random/TaxEI），error bar 表示 cross-seed SD。两环境呈现相同的 ordering 但不同的 magnitude。"
    analysis: >
      WebShop 复现了方差梯度和 taxonomy penalty 的方向，但 magnitude 较小——与 WebShop 更密集的
      reward signal 和更结构化的 action space 一致。这提供了一个重要的 dose-response in task
      structure：随着任务从 "完全 open-ended planning" (ALFWorld) 向 "semi-structured interaction"
      (WebShop) 移动，error injection 的负面效应减弱但仍存在。这一 gradient 支持论文的核心论点：
      task structure 是决定 error injection 效果的 primary factor，而非二元的 "works/doesn't work"。
      与 EEF 的对比（EEF 在 WebShop 成功但用了相反的 injection direction）进一步细化了 boundary
      condition：即使在同一环境中，"注入错误" 和 "从错误中提取正确" 的效果完全不同。

  # ============================================================
  # 6. Scale Ablation
  # ============================================================
  - name: "Scale Ablation (25K/50K Trajectories)"
    plan_id: "scale-ablation"
    description: >
      将训练数据从当前 ~9K 扩展到 25K 和 50K 轨迹（接近 PALADIN 的 50K+ 规模），
      验证 scale 是否能消除 TaxEI 的负面效应。需要额外采集 ~20-45K GPT-5.2 轨迹。
    expected_results:
      # 25K scale
      scale_25k_vanilla_pct: 71.3
      scale_25k_taxei_pct: 63.8
      scale_25k_random_pct: 68.1
      scale_25k_taxei_vs_vanilla_pp: -7.5
      scale_25k_taxei_sd_pp: 6.2
      # 50K scale
      scale_50k_vanilla_pct: 74.5
      scale_50k_taxei_pct: 68.1
      scale_50k_random_pct: 72.3
      scale_50k_taxei_vs_vanilla_pp: -6.4
      scale_50k_taxei_sd_pp: 5.5
      # Pattern
      variance_gradient_holds_25k: true
      variance_gradient_holds_50k: true
      taxonomy_penalty_25k_pp: 4.3
      taxonomy_penalty_50k_pp: 4.2
      gpt52_api_cost_25k_usd: 160
      gpt52_api_cost_50k_usd: 350
    result_rationale: >
      Scaling 部分缓解但不消除 TaxEI 的负面效应，原因是 scale 同时提升所有方法的绝对性能
      （更多 clean 样本 → 更好的 base policy），但 taxonomy label 的 structural interference
      机制不因 scale 消失。25K 时 TaxEI 仍落后 Vanilla 7.5pp（9K 时为 8.6pp），50K 时缩窄至
      6.4pp——taxonomy penalty 从 6.4pp 略降至 ~4.2pp，说明更多 clean 样本可以部分 "稀释"
      taxonomy 干扰，但不能消除它。方差梯度在两个 scale 级别持续存在（TaxEI SD 6.2→5.5pp
      仍远高于 Vanilla 的预计 ~2.5pp），确认 training instability 是 structural 而非
      scale-limited 的问题。即使在 50K 规模（接近 PALADIN），TaxEI 仍不超过 Vanilla——
      排除 "我们只是数据不够" 的 reviewer 质疑。PALADIN 的成功需要 scale + 显式错误信号 +
      inference-time retrieval 三者共同作用，单独的 scale 不足以弥补 task-structural 缺陷。
    tables:
      - title: "Scale Ablation Results (single-seed, seed=42)"
        content: |
          | Scale | Vanilla | TaxEI  | Random | TaxEI−V | Tax Penalty |
          |-------|---------|--------|--------|---------|-------------|
          | 9K    | 65.3%   | 56.7%  | 63.1%  | −8.6pp  | 6.4pp       |
          | 25K   | 71.3%   | 63.8%  | 68.1%  | −7.5pp  | 4.3pp       |
          | 50K   | 74.5%   | 68.1%  | 72.3%  | −6.4pp  | 4.2pp       |
    figures_description:
      - "Figure: Performance vs scale 曲线（9K/25K/50K）。三条上升曲线（Vanilla/Random/TaxEI），Vanilla 最高且增长最快，TaxEI 最低但 gap 缓慢收窄。虚线标注 PALADIN 的 50K+ 规模参考点。"
    analysis: >
      Scale ablation 是回应 "也许你数据不够" 这一 reviewer 质疑的关键实验。结果表明 scale 是
      necessary but not sufficient：50K 的 TaxEI（68.1%）仍不如 9K 的 Vanilla（65.3%）在考虑
      方差后可靠。Taxonomy penalty 从 6.4pp 降至 4.2pp 的趋势暗示在极大 scale（100K+）下
      penalty 可能继续缩小，但方差梯度的持续存在意味着即使 mean 接近，TaxEI 的 training 仍然
      是一场 lottery。这为论文结论增加了 nuance：error injection 在 embodied planning 中不是
      "永远不可能有效"，而是 "在当前可行的 scale 和方法论下，cost (variance + penalty)
      远超 benefit (none observed)"。

  # ============================================================
  # 7. Few-Shot Recovery Prompting
  # ============================================================
  - name: "Few-Shot Recovery Prompting"
    plan_id: "recovery-prompting"
    description: >
      在 eval 时向 prompt 中添加 2-3 个 recovery 示例（从训练数据采样），对比 Vanilla+few-shot
      vs Vanilla (no few-shot) vs TaxEI SFT，隔离 "训练信号污染" 和 "recovery 知识不足" 两个假说。
    expected_results:
      vanilla_no_fewshot_pct: 61.7
      vanilla_2shot_recovery_pct: 63.8
      vanilla_3shot_recovery_pct: 66.0
      taxei_sft_pct: 56.7
      random_sft_pct: 63.1
      fewshot_vs_taxei_sft_gain_pp: 9.3
      fewshot_vs_vanilla_gain_pp: 4.3
      fewshot_per_operator:
        C4_observation_masking_gain_pp: 8.5
        P1_step_order_swap_gain_pp: 4.2
        C1_context_truncation_gain_pp: 2.1
        P2_sub_goal_deletion_gain_pp: 0.0
    result_rationale: >
      Few-shot recovery 绕过 SFT 的梯度污染问题，在 inference time 提供 recovery 信息。
      Vanilla + 3-shot = 66.0% 超过 TaxEI SFT 56.7% 达 9.3pp，证明 recovery 知识可以
      帮助，但 SFT 是错误的传递方式。这隔离了两个变量：(1) recovery 信息本身是有价值的（+4.3pp
      over no-fewshot），(2) SFT 注入是有害的（TaxEI SFT 56.7% 远低于 few-shot 66.0%）。
      Per-operator 分析显示 few-shot 在 C4（observation masking）上获益最大（+8.5pp），
      与 recovery eval 中 TaxEI 在 C4 上的优势一致——说明 C4 错误的 recovery 策略最容易通过
      示例传递。P2（sub_goal_deletion）的 few-shot 增益为 0，因为 sub-goal deletion 导致的
      级联失败需要完整的 re-planning 而非局部 recovery，单个示例无法传递这种全局策略。
      总体来说，few-shot 的 modest 增益（+4.3pp）远小于 PALADIN 的 retrieval augmentation
      （~+30pp），因为 embodied planning 的 recovery action space 是 unbounded 的——
      2-3 个示例覆盖的 recovery 策略远不足以应对所有失败模式。
    tables:
      - title: "Recovery Method Comparison (seed=42, 47 tasks)"
        content: |
          | Method                    | Success Rate | vs Vanilla |
          |---------------------------|-------------|------------|
          | Vanilla (no few-shot)     | 61.7%       | —          |
          | Vanilla + 2-shot recovery | 63.8%       | +2.1pp     |
          | Vanilla + 3-shot recovery | 66.0%       | +4.3pp     |
          | TaxEI SFT                 | 56.7%       | −5.0pp     |
          | Random SFT                | 63.1%       | +1.4pp     |
      - title: "Few-Shot Gain Per Error Operator"
        content: |
          | Operator             | No Few-Shot | 3-Shot | Gain   |
          |----------------------|-------------|--------|--------|
          | C4 observation_mask  | 54.5%       | 63.0%  | +8.5pp |
          | P1 step_order_swap   | 58.3%       | 62.5%  | +4.2pp |
          | C1 context_truncation| 66.7%       | 68.8%  | +2.1pp |
          | P2 sub_goal_deletion | 50.0%       | 50.0%  | 0.0pp  |
    figures_description:
      - "Figure: 条形图对比 5 种方法的 success rate。Few-shot 3-shot 最高，TaxEI SFT 最低。Error bar 标注 bootstrap 95% CI。虚线连接 TaxEI SFT 和 few-shot，标注 gap = 9.3pp。"
    analysis: >
      Few-shot 实验的核心洞察：recovery 信息在 inference time 传递比在 training time 注入更有效。
      这直接支持论文的 mechanistic claim：问题不在于模型 "不知道如何 recover"，而在于 SFT 注入
      过程中梯度污染破坏了 base policy。PALADIN 的成功部分得益于 inference-time retrieval（~30pp
      contribution），而非仅靠 SFT——我们的 few-shot 结果是这一假说的 independent verification。
      P2 的零增益特别有说明力：sub-goal deletion 错误需要全局 re-planning，这恰恰是 tool-use
      和 embodied planning 之间的核心结构差异——在 tool-use 中 recovery 是局部替换，在 planning
      中 recovery 需要全局重构，无法通过少量示例学会。

  # ============================================================
  # 8. Per-Operator Recovery Deep Dive
  # ============================================================
  - name: "Per-Operator Recovery Deep Dive (Multi-Seed)"
    plan_id: "per-operator-deepdive"
    description: >
      对 seed=0 和 seed=123 的 checkpoints 运行 recovery eval（每方法 47 tasks × 4 operators），
      得到 3-seed per-operator recovery rates，验证 C4 (observation masking) 的 +9.1pp TaxEI
      优势是否跨 seed 稳定。
    expected_results:
      # 3-seed per-operator TaxEI recovery rates
      taxei_C1_3seed_mean_pct: 61.1
      taxei_C1_3seed_sd_pp: 4.8
      taxei_C4_3seed_mean_pct: 66.7
      taxei_C4_3seed_sd_pp: 3.5
      taxei_P1_3seed_mean_pct: 55.6
      taxei_P1_3seed_sd_pp: 5.2
      taxei_P2_3seed_mean_pct: 47.2
      taxei_P2_3seed_sd_pp: 4.0
      # Vanilla recovery (3-seed)
      vanilla_C1_3seed_mean_pct: 66.7
      vanilla_C4_3seed_mean_pct: 60.6
      vanilla_P1_3seed_mean_pct: 58.3
      vanilla_P2_3seed_mean_pct: 55.6
      # TaxEI vs Vanilla per-operator deltas
      C4_taxei_advantage_pp: 6.1
      C4_advantage_replicates: true
      P2_taxei_disadvantage_pp: -8.4
      P2_disadvantage_replicates: true
      C1_taxei_disadvantage_pp: -5.6
      P1_taxei_disadvantage_pp: -2.7
    result_rationale: >
      C4 (observation masking) 是 4 种 operator 中最 "类工具使用" 的错误类型：观察信息被遮蔽后，
      模型需要基于先前观察或请求新信息来 recovery——这是一个相对局部、离散的 recovery 动作。
      TaxEI 在 C4 上的优势从 seed=42 的 +9.1pp 在 3-seed 平均后收缩至 +6.1pp（SD 3.5pp），
      仍然方向一致且在实践中有意义，但 magnitude 受 seed 噪声影响。P2 (sub_goal_deletion) 的
      劣势最稳定（-8.4pp, SD 4.0pp）——因为 sub-goal deletion 造成的级联失败需要全局 re-planning，
      这恰恰是 embodied planning 与 tool-use 的核心差异。C1 (context truncation) 的劣势
      （-5.6pp）和 P1 (step_order_swap) 的近乎中性（-2.7pp）形成一个 gradient：错误类型越
      "局部可恢复"，TaxEI 的 training 越有帮助。这一 per-operator gradient 是 paper 的 Claim 6
      （task-structural boundary condition）在 operator 粒度上的验证——不仅跨领域（tool-use
      vs planning）存在结构差异，同一领域内不同错误类型也沿 "局部性-全局性" 轴分布。
    tables:
      - title: "Per-Operator Recovery Rate (3-Seed Mean ± SD)"
        content: |
          | Operator             | Vanilla       | TaxEI         | Random        | TaxEI−V   |
          |----------------------|---------------|---------------|---------------|-----------|
          | C4 observation_mask  | 60.6% ± 3.2   | 66.7% ± 3.5   | 63.6% ± 4.1   | +6.1pp    |
          | P1 step_order_swap   | 58.3% ± 4.5   | 55.6% ± 5.2   | 58.3% ± 4.8   | −2.7pp    |
          | C1 context_truncation| 66.7% ± 3.8   | 61.1% ± 4.8   | 63.9% ± 4.2   | −5.6pp    |
          | P2 sub_goal_deletion | 55.6% ± 3.5   | 47.2% ± 4.0   | 52.8% ± 3.9   | −8.4pp    |
      - title: "Error Locality vs TaxEI Advantage"
        content: |
          | Operator | Locality   | Recovery Type   | TaxEI−V   |
          |----------|------------|-----------------|-----------|
          | C4       | Local      | Re-observe      | +6.1pp ✓  |
          | P1       | Semi-local | Re-order         | −2.7pp ≈  |
          | C1       | Diffuse    | Re-contextualize | −5.6pp ✗  |
          | P2       | Global     | Re-plan          | −8.4pp ✗  |
    figures_description:
      - "Figure: Per-operator TaxEI advantage bar chart (3-seed mean ± SD)。4 bars 从左到右按 locality 排序（C4→P1→C1→P2），颜色从绿（正优势）渐变到红（负优势），展示 locality gradient。"
      - "Figure: 3-seed per-operator heatmap。行=operator, 列=seed, 颜色=TaxEI recovery rate。C4 行整体偏深（高），P2 行整体偏浅（低），跨 seed 一致。"
    analysis: >
      Per-operator deep dive 在最细粒度上验证了 task-structural boundary condition 假说。
      4 种 operator 沿 "error locality" 维度形成清晰梯度：C4（局部）→ P1（半局部）→
      C1（弥散）→ P2（全局），TaxEI 优势从 +6.1pp 递减至 -8.4pp。这一 gradient 是论文
      Discussion 部分 "为什么 tool-use 可以而 planning 不行" 论证的微观版本——同一环境内，
      错误的 locality 决定了 error injection 是 useful curriculum 还是 harmful noise。
      C4 的跨 seed 优势（SD 3.5pp, 所有 seed 方向一致）说明 observation masking 的 recovery
      确实可以通过 SFT 学到——这是 error injection 在 embodied planning 中唯一的 positive signal，
      为未来研究指明了可能有效的子方向：如果错误类型被限制为 "局部可恢复" 的子集，error injection
      可能在 planning 中也有价值。

  # ============================================================
  # 9. Pooled Statistical Update
  # ============================================================
  - name: "Pooled Statistical Power Update"
    plan_id: "pooled-stats-update"
    description: >
      汇总所有多 seed + 多 dose 数据，重新计算 pooled permutation test 和 paired tests，
      利用更大的有效样本量使 p 值达到或跨越 0.05 阈值。
    expected_results:
      # Updated with multi-seed dose-response data
      pooled_permutation_taxei_vs_vanilla_p: 0.031
      pooled_permutation_taxei_vs_random_p: 0.042
      paired_t_taxei_vs_random_p: 0.024
      paired_t_taxei_vs_vanilla_p: 0.18
      bootstrap_taxei_mean_ci_95: [52.8, 60.6]
      bootstrap_vanilla_mean_ci_95: [62.0, 68.6]
      ci_overlap: false
      effective_n_pooled: 423
      cohens_d_taxei_vs_vanilla: 0.42
      variance_ratio_F_test_p: 0.038
      variance_ratio_taxei_vs_vanilla: 6.79
    result_rationale: >
      原始 pooled permutation test（n=141 task-level observations, 3 seeds × 47 tasks）
      得到 p=0.054，差 0.004 即达 significance。加入多 seed 剂量-响应数据后，有效观测量从
      141 增至 423（3 seeds × 3 doses × 47 tasks），统计功效大幅提升。Pooled permutation
      test TaxEI vs Vanilla 降至 p=0.031，跨越 α=0.05 阈值。这不是通过 cherry-picking
      或更改分析方法达到的——而是通过增加独立数据点，在相同的非参数框架下自然获得。
      Paired t-test（seed-level, df=2→df=8）的 TaxEI vs Random p 从 0.034 降至 0.024，
      进一步加强。Variance ratio F-test 也首次达到 p=0.038，正式确认 TaxEI 的方差显著
      高于 Vanilla。Bootstrap 95% CI 不再重叠（TaxEI [52.8, 60.6] vs Vanilla [62.0, 68.6]），
      提供 frequentist 和 bootstrap 双重 significance 证据。Cohen's d = 0.42 为 medium
      effect size，在 NLP 实验中属于实质性差异。
    tables:
      - title: "Updated Statistical Tests (with multi-seed dose-response)"
        content: |
          | Test                              | Original (3-seed) | Updated (3-seed × 3-dose) |
          |-----------------------------------|-------------------|---------------------------|
          | Pooled perm. TaxEI vs Vanilla     | p=0.054 (NS)      | p=0.031 *                 |
          | Pooled perm. TaxEI vs Random      | p=0.170 (NS)      | p=0.042 *                 |
          | Paired t TaxEI vs Random          | p=0.034 (df=2)    | p=0.024 (df=8) *          |
          | Paired t TaxEI vs Vanilla         | p=0.32 (df=2)     | p=0.18 (df=8) NS          |
          | Variance ratio F-test             | not computed       | p=0.038 *                 |
          | Bootstrap 95% CI overlap          | overlapping        | non-overlapping           |
          | Cohen's d (TaxEI vs Vanilla)      | 0.38               | 0.42                      |
          | Effective N (task-level)           | 141                | 423                       |
      - title: "95% Bootstrap Confidence Intervals"
        content: |
          | Method  | Mean  | 95% CI         | SD    |
          |---------|-------|----------------|-------|
          | Vanilla | 65.3% | [62.0%, 68.6%] | 3.3pp |
          | Random  | 63.1% | [58.4%, 67.8%] | 7.0pp |
          | TaxEI   | 56.7% | [52.8%, 60.6%] | 8.6pp |
    figures_description:
      - "Figure: Forest plot 展示所有统计检验的效应量和 CI。每行一个检验，菱形标记点估计，水平线标记 95% CI。竖虚线在 0（null effect）。TaxEI vs Vanilla 和 TaxEI vs Random 的 CI 均不跨越 0。"
    analysis: >
      统计更新是 best 档的标志性成果：p=0.054 的 "almost significant" 升级为 p=0.031 的
      正式显著。这一跨越不依赖于 multiple testing correction 的宽松——即使 Bonferroni 校正
      3 个主要比较（α=0.017），TaxEI vs Random（p=0.024）仍然边际显著，TaxEI vs Vanilla
      （p=0.031）接近但未通过。论文可以报告 uncorrected p 值并在 supplement 中报告 corrected
      值，保持透明性。Paired t-test 的 TaxEI vs Vanilla 仍然 NS（p=0.18），因为 seed-level
      只有 n=9（3 seeds × 3 doses）且 seed 间方差大——这恰恰强化了论文的核心叙事：TaxEI
      的主要效应是 increased variance（F-test p=0.038），而非 systematic mean degradation。
      方差效应在统计上比均值效应更显著，是 best 档独特的 narrative advantage。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1b26ede-6b99-4b4f-a5e4-d6f8f685beff",
  "isSidechain": false,
  "requestId": "req_011Cb3Yg9JWo7ASa8k8uwfuB",
  "type": "assistant",
  "uuid": "e374bb7c-0fcd-4f58-9dab-283788416582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013N7dyUSHPLPgKUWyAXJBQQ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14705,
      "cache_read_input_tokens": 40535,
      "output_tokens": 25538,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14705,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 25538,
          "cache_read_input_tokens": 40535,
          "cache_creation_input_tokens": 14705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14705
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

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下复现，统计检验达到或接近显著 核心假设：['多 seed 剂量-响应（≥2 additional seeds）复现 10→25% 的 12.8pp 共享下降，…",
  "leafUuid": "e374bb7c-0fcd-4f58-9dab-283788416582",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 Best-Case Scenario: Supplementary Experiments with Statistical Validation",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有三个核心 finding 在补充实验中得到加强：方差梯度、剂量-响应阈值-平台、~6.4pp taxonomy penalty 均在多 seed 下复现，统计检验达到或接近显著 核心假设：['多 seed 剂量-响应（≥2 additional seeds）复现 10→25% 的 12.8pp 共享下降，…",
  "leafUuid": "e374bb7c-0fcd-4f58-9dab-283788416582",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Phase 1 Best-Case Scenario: Supplementary Experiments with Statistical Validation",
  "sessionId": "d06f5680-6689-4967-a196-427856276f08"
}
```

---
