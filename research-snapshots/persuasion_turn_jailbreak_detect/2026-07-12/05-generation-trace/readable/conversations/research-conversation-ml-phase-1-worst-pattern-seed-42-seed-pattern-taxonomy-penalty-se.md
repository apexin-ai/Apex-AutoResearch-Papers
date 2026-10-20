# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：核心 pattern 被证明是 seed=42 的偶然：多 seed 剂量-响应无一致 pattern，taxonomy penalty 在部分 se

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/2b57ccaa-648a-4b79-b1d8-f74354c4838b.jsonl`
- **Structured JSON:** [`0ae6de9cce0547f1ef39.json`](../../sessions/0a/0ae6de9cce0547f1ef39.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T02:28:23.137Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T02:28:23.137Z",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：核心 pattern 被证明是 seed=42 的偶然：多 seed 剂量-响应无一致 pattern，taxonomy penalty 在部分 seed 反转或消失，方差梯度在更多数据下变得不显著\n核心假设：['新 seed 的剂量-响应不显示 threshold-plateau——有的线性下降，有的无单调关系', \"taxonomy penalty 在某些 seed 为正（TaxEI > Random），消解 'constant offset' claim\", '新增 seed 后 TaxEI 均值上移至 60%+，与 Vanilla 的差距缩小到 <4pp 且 p>0.3', '方差梯度在 5-seed 均值下 Random SD ≈ TaxEI SD，无法区分结构化注入与随机注入的不稳定性差异', '训练 loss 分析无信息量——注入样本与 clean 样本 loss 轨迹无系统差异']\n关键指标范围：{'taxei_3seed_mean_pct': [59.0, 65.0], 'taxei_3seed_sd_pp': [4.0, 7.0], 'vanilla_3seed_sd_pp': [3.0, 6.0], 'taxonomy_penalty_per_dose_pp': [-2.0, 8.0], 'taxonomy_penalty_cross_dose_sd_pp': [3.5, 6.0], 'dose_threshold_drop_pp': [2.0, 14.0], 'pooled_p_taxei_vs_vanilla': [0.15, 0.6], 'paired_t_taxei_vs_random_p': [0.1, 0.5], 'dose_response_cross_seed_agreement': [0.2, 0.5]}\n叙事方向：三个原始 finding 均不成立为独立 claim。需要 reframe。 新 angle：error injection 的效果被 seed variance 完全淹没—— 这本身就是 negative result，但 framing 从 \"error injection hurts + here's why\" 转向 \"error injection is indistinguishable from noise in low-data embodied planning regimes\"。 核心 contribution 变为：(1) ALFWorld SFT 的 cross-seed variance 之大使得任何 data augmentation 策略的评估都需要 ≥5 seeds（方法论 contribution）， (2) 在 <10K 样本规模下，error injection 的信号被训练噪声压制， 无法提供超出 seed lottery 的信息（scale-dependent null result）。 论文从 \"boundary condition\" paper 变为 \"evaluation methodology\" paper， 仍可投 Negative Results workshop，但需要重写 introduction 和 contribution section。 不降级 venue——Negative Results workshop 本身就欢迎 \"we thought X mattered but it's noise\"。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: tax_error_inject_agent\nvenue: Insights from Negative Results in NLP @ EMNLP 2026\nfocus: Negative result paper with three core findings: (1) variance gradient Vanilla&lt;Random&lt;TaxEI, (2) dose-response threshold-plateau with shared 12.8pp drop at 10-25%, (3) constant ~6.4pp taxonomy label penalty. All statistical comparisons NS (min p=0.054). Single-seed dose-response limitation.\n\n## paper_framing.md\n\n# Paper Framing: Error Injection Helps Tool-Use but Hurts Planning — Boundary Conditions for Failure-Augmented Agent Training\n\n## Target Venue\n**Primary**: Insights from Negative Results in NLP @ EMNLP 2026 (Budapest, Oct 22–29) — short paper track, purpose-built for rigorous negative findings.\n**Backup**: EMNLP 2026 Findings (main conference accepts negative-result contributions per CFP).\n\n## Core Question\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\n\n## Thesis Statement\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training (2.6× variance increase, non-linear dose-response with catastrophic collapse above 10% injection ratio) without improving performance on ALFWorld, suggesting that **task structure** may be the primary factor determining whether failure-augmented training transfers.\n\n## Story Arc\n\n### 1. Motivation: Why error injection should work\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\n- **P1** (step_order_swap): permute action ordering\n- **P2** (sub_goal_deletion): remove sub-goals\n- **C1** (context_truncation): truncate environmental context\n- **C4** (observation_masking): mask observation feedback\n\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\n\n### 3. Finding: No benefit, high instability\n**Clean task performance (3-seed, all methods complete)**:\n- Vanilla SFT: 65.3% ± 3.3pp (seeds 42/0/123) — stable\n- TaxEI SFT: 56.7% ± 8.6pp (seeds 42/0/123) — **2.6× variance, -8.6pp mean but p≈0.32 (NS)**\n- Random SFT: 63.1% ± 7.0pp (seeds 42/0/123) — **2.1× variance, -2.2pp mean (NS)**\n\n**Critical pattern**: TaxEI seeds 42 and 123 both equal vanilla (61.7%), but seed=0 collapses to 46.8%. Error injection doesn't reliably hurt — it makes training a lottery.\n\n**Variance gradient**: Vanilla SD (3.3pp) < Random SD (7.0pp) < TaxEI SD (8.6pp). More structured injection → more training instability. This gradient is itself a finding: taxonomy labels amplify variance beyond what random noise injection introduces.\n\n**Dose-response ablation (fixed-size 4,358 total, seed=42, vs vanilla-seed42=61.7%)**:\n| Dose | TaxEI | Random | Δ(R−T) |\n|------|-------|--------|---------|\n| 0% (vanilla) | 61.7% | 61.7% | 0 |\n| 10% | 61.7% (0pp) | 68.1% (+6.4pp) | +6.4pp |\n| 25% | 48.9% (-12.8pp) | 55.3% (-6.4pp) | +6.4pp |\n| 50% | 51.1% (-10.6pp) | 57.4% (-4.3pp) | +6.3pp |\n\n**Two separable effects**:\n1. **Injection dose threshold** (shared by both methods): 10%→25% both drop exactly 12.8pp (TaxEI: 61.7→48.9, Random: 68.1→55.3). The threshold between 10-25% and subsequent plateau at 50% is a universal property of error injection, not TaxEI-specific. Mechanism: data dilution crosses a critical signal-to-noise boundary.\n2. **Taxonomy label penalty** (constant ~6.4pp additive offset): TaxEI underperforms Random by 6.4/6.4/6.3pp across all three dose points. This remarkably stable gap suggests taxonomy labels introduce a systematic bias independent of injection volume — structured error patterns may teach the model specific wrong behaviors that random noise does not.\n\nNote: All dose-response data is single-seed (seed=42). Given 3-seed SD up to 8.6pp, individual point estimates have limited confidence, but the consistency of the ~6.4pp gap across three independent dose points strengthens the finding. The 68.1% for Random 10% falls within vanilla seed variance (61.7-68.1%) and should not be interpreted as a significant improvement over vanilla.\n\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\n\n**Detection Rate**: 0% for all methods.\n\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\n\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\n\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\n|-----------|----------------------|------------------------------|\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\n\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\n\n### 5. Contribution: What this negative result gives the community\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\n2. **Cost savings**: Prevents the community from pursuing error-injection approaches in ALFWorld-style domains without addressing the structural prerequisites we identify.\n3. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp). Two out of three TaxEI seeds match vanilla exactly; the third collapses by 14.9pp. Single-seed evaluations of error injection methods are fundamentally unreliable.\n4. **Dose-response with separable dual effects**: Injection ratio ablation (fixed data size, TaxEI and Random in parallel) reveals: (a) a shared threshold-plateau at 10-25% injection ratio — both methods drop identically by 12.8pp from their 10% baseline; (b) a constant ~6.4pp taxonomy label penalty across all dose levels, suggesting structured error patterns teach specific wrong behaviors that random noise does not. This decomposition — shared dose effect + additive taxonomy penalty — provides actionable guidance: even if injection ratio is optimized, taxonomy-guided injection remains inferior to random injection in embodied planning.\n\n## Core Claims (each backed by experimental evidence)\n\n- **Claim 1**: Taxonomy-guided error injection introduces high training variance and fails to improve clean task performance on ALFWorld.\n  → Support: TaxEI 3-seed mean 56.7%±8.6pp vs Vanilla 65.3%±3.3pp. Gap is -8.6pp. **Paired t-test (n=3 seeds): p≈0.32 (NS). Pooled permutation test (n=141 task-level observations): p=0.054 (NS at α=0.05, marginal).** Even the higher-powered pooled test cannot confirm significant degradation. Critically, 2/3 seeds (42, 123) show TaxEI = Vanilla (both 61.7%); the deficit is driven by seed=0 (46.8%). Gate 3a FAIL (no seed exceeds vanilla mean). TaxEI SD is 2.6× vanilla SD — the primary effect is **dramatically increased training instability**, not systematic degradation.\n\n- **Claim 2**: Taxonomy labels impose a constant ~6.4pp penalty compared to random (unlabeled) injection across all dose levels.\n  → Support: 3-seed clean eval: TaxEI 56.7% vs Random 63.1%, -6.4pp. Paired t p≈0.034 (df=2, suggestive but low power). Pooled permutation test: p=0.170 (NS). **Dose-response ablation provides stronger evidence**: TaxEI trails Random by 6.4/6.4/6.3pp at 10%/25%/50% injection ratios — a remarkably stable gap across three independent experiments, suggesting a systematic rather than stochastic effect. Recovery eval confirms the direction: TaxEI 59.6% < Random 63.8%. TaxEI SD (8.6pp) > Random SD (7.0pp). Caveat: all dose-response points are single-seed; the per-point gap is ~0.9 SE and not individually significant at n=47.\n\n- **Claim 3**: Error injection increases training instability disproportionately — this is the primary negative effect, with a clear variance gradient.\n  → Support: Cross-seed SD: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. TaxEI seed=0 collapses to 46.8% while seeds 42/123 match vanilla at 61.7% — a 14.9pp swing within the same method. The variance gradient (no injection < random injection < taxonomy-guided injection) suggests that more structured perturbation amplifies training instability rather than providing useful curriculum signal. A single favorable seed can mask injection's destabilizing effect, making published single-seed results unreliable.\n\n- **Claim 4**: Injection-trained models do not improve error recovery.\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp).\n\n- **Claim 5**: Detection training via error injection is completely ineffective in this setup.\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random).\n\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\n\n## Anticipated Reviewer Concerns\n\n1. **\"Statistical power with 3 seeds is limited.\"**\n   → All three methods now have 3 seeds. TaxEI vs Vanilla: p≈0.32 (NS) — we do not claim a significant mean difference but instead emphasize the variance effect (SD 8.6pp vs 3.3pp, 2.6× ratio). TaxEI vs Random: paired t p≈0.034 (df=2, suggestive). We report all individual seed results transparently. The variance gradient (Vanilla < Random < TaxEI) is directionally consistent across all seeds.\n\n2. **\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\"**\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. We propose a second environment (WebShop) for supplementary validation.\n\n3. **\"Maybe the taxonomy itself is poorly designed.\"**\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\n\n4. **\"The training recipe might be suboptimal for injection data.\"**\n   → The same recipe produces strong Vanilla results (65.3% vs 42.6% baseline, +22.7pp), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\n\n5. **\"50% injection ratio is too high — you're drowning the signal.\"**\n   → Comprehensively addressed with fixed-size dose-response ablation (all 4,358 total samples, seed=42). Results: 10% = 61.7% (0pp), 25% = 48.9% (-12.8pp), 50% = 51.1% (-10.6pp). The pattern is threshold-plateau, not linear: below ~15-20% injection is harmless but provides no benefit; above it, performance collapses and plateaus regardless of further injection increase. Even at the lowest tested ratio (10%), injection provides zero improvement over vanilla — the best case is exact parity. Random injection dose-response (in progress) will determine whether the threshold is specific to taxonomy-guided injection or a general property.\n\n6. **\"Why is detection rate 0%? Evaluation might be flawed.\"**\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\n\n7. **\"Why not compare directly on ToolBench?\"**\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\n\n## Key Differentiators vs PALADIN\n\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\n\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \"go to countertop 2\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\n\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\n\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \"what to do after an error\" fundamentally harder to learn from examples.\n\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\n\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\n## Note on v3→v4 Vanilla Discrepancy\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\n\n## Supplementary Experiments Needed\n\n### Priority 1 (required for submission)\n- ~~**More seeds**~~: ✅ DONE — All 3 methods at 3 seeds. Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\n- **Injection ratio ablation**: ✅ TaxEI dose-response done (10%=61.7%, 25%=48.9%, 50% in progress). Random dose-response in progress (10%, 25%, 50% training). Key finding: non-linear threshold between 10-25%.\n- **Training dynamics analysis**: Plot training loss curves for clean vs. injected samples across epochs. Do injected samples have systematically higher loss? Does the model learn clean patterns before injection patterns corrupt them?\n\n### Priority 2 (strengthens paper significantly)\n- **Second environment**: WebShop or ScienceWorld to test whether the negative result generalizes beyond ALFWorld. If error injection also fails there, the boundary condition claim is stronger.\n- **Qualitative failure analysis**: Manually examine 20+ TaxEI failure cases — does the model produce incoherent plans, or does it simply choose wrong actions at similar rates? This informs the \"noise vs. wrong learning\" distinction.\n\n### Priority 3 (nice to have)\n- **Scale ablation**: Does TaxEI improve if we scale to 25K or 50K trajectories (matching PALADIN's scale)?\n- **Explicit recovery prompting**: Instead of SFT, test whether in-context recovery examples (few-shot) help — this isolates whether the issue is training signal vs. knowledge.\n- **Per-operator deep dive**: Run more seeds on recovery eval to determine if C4 (observation masking) is genuinely easier for TaxEI or if the +9.1pp advantage is noise.\n\n\n## registry (completed experiments)\n\n- exp_id: traj_collect_500\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    successful_trajectories: 501\n    failed_trajectories: 213\n    total_attempts: 714\n    success_rate: 0.702\n    api_cost_usd: 8.86\n    collection_time_sec: 5245\n- exp_id: sft-dryrun-73\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_init: 2.436\n    train_loss_final: 1.543\n    train_loss_avg: 1.894\n    peak_memory_gib: 19.22\n    steps: 8\n    duration_sec: 42\n    data_vanilla: 124\n    data_injected_dryrun: 96\n    injected_failed: 4\n- exp_id: vanilla-react-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_success_rate: 0.426\n    total_tasks: 47\n    successes: 20\n    per_task_type:\n      pick_heat_then_place:\n        success: 5\n        total: 8\n        rate: 0.625\n      look_at_obj_in_light:\n        success: 3\n        total: 6\n        rate: 0.5\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_two_obj_and_place:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_cool_then_place:\n        success: 0\n        total: 7\n        rate: 0\n- exp_id: mini-pipeline-e2e\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mini-taxei-sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.447\n    eval_successes: 21\n    eval_total: 47\n    vs_baseline_pp: 2.1\n    per_task:\n      look_at_obj_in_light: 3/6 (50.0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 1/7 (14.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_two_obj_and_place: 3/7 (42.9%)\n    train_steps: 195\n    train_duration_min: 16.3\n- exp_id: mini-vanilla-sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.149\n    eval_successes: 7\n    eval_total: 47\n    vs_baseline_pp: -27.7\n    per_task:\n      look_at_obj_in_light: 0/6 (0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 2/11 (18.2%)\n      pick_cool_then_place: 0/7 (0%)\n      pick_heat_then_place: 3/8 (37.5%)\n      pick_two_obj_and_place: 0/7 (0%)\n    train_steps: 54\n    train_duration_min: 5\n- exp_id: vanilla_sft_aligned_v1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: vanilla_sft_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mini-vanilla-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 4176\n    train_steps_total: 1566\n    est_duration_min: 58\n    format: aligned_single_turn\n- exp_id: mini-taxei-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 7545\n    train_samples_clean: 4176\n    train_samples_injected: 3369\n    train_steps_total: 2832\n    est_duration_min: 90\n    format: aligned_single_turn\n- exp_id: mini-random-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 9076\n    train_samples_clean: 4176\n    train_samples_injected: 4900\n    train_steps_total: 3405\n    est_duration_min: 110\n    format: aligned_single_turn\n- exp_id: mini-vanilla-sft-v4\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v3-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.745\n    successes: 35\n    total: 47\n    vs_baseline_pp: 31.9\n    vs_baseline: 42.6% → 74.5%\n- exp_id: v3-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_baseline_pp: 23.4\n    vs_vanilla_sft_pp: -8.5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_clean_then_place: 8/11 (72.7%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_cool_then_place: 3/7 (42.9%)\n- exp_id: v3-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_baseline_pp: 8.5\n    vs_vanilla_sft_pp: -23.4\n- exp_id: v4-taxei-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-random-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-random-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-taxei-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-random-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_clean_then_place: 5/11 (45.5%)\n- exp_id: v4-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    vs_vanilla_pp: 0\n    vs_random_pp: -4.3\n    mcnemar_vs_vanilla_p: 1\n    mcnemar_vs_random_p: 0.754\n    gate_3a: FAIL\n    gate_3b: FAIL\n    gate_4: PASS\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 3/7 (42.9%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 2/7 (28.6%)\n- exp_id: v4-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_vanilla_pp: 4.3\n    vs_taxei_pp: 4.3\n    mcnemar_vs_vanilla_p: 0.754\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 4/8 (50%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n- exp_id: v4-vanilla-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.297\n    avg_loss: 0.416\n    token_accuracy: 0.902\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.917\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-random-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.912\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-recovery-eval-dev\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    pipeline_files:\n    - eval/injected_eval.py\n    - scripts/run_injected_eval.sh\n    injected_eval_lines: 463\n    dryrun_result: PASS\n    dryrun_detail: vanilla checkpoint, 1 task, cuda:3, injected error recovered in\n      13 steps\n- exp_id: v4-vanilla-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.288\n    token_accuracy: 0.903\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58.9\n- exp_id: v4-vanilla-seed7\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-recovery-dryrun\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    vs_seed42_pp: 6.4\n    mcnemar_vs_seed42_p: 0.375\n    discordant_pairs: 5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 5/7 (71.4%)\n- exp_id: v4-taxei-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.468\n    eval_successes: 22\n    eval_total: 47\n    vs_seed42_pp: -14.9\n- exp_id: v4-random-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_seed42_pp: -10.7\n- exp_id: v4-vanilla-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_seed42_pp: 4.3\n    vs_seed0_pp: -2.1\n    per_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 7\n        total: 8\n        rate: 0.875\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-vanilla-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    successes: 29\n    total: 47\n    recovery_rate: 0.617\n    detection_rate: 0\n- exp_id: v4-taxei-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success_rate: 0.596\n    successes: 28\n    total: 47\n    recovery_rate: 0.596\n    detection_rate: 0\n- exp_id: v4-random-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.638\n    detection_rate: 0\n    successes: 30\n    total: 47\n    source: json-file-verified\n    note: r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\n- exp_id: v4-taxei-recovery-eval-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.596\n    detection_rate: 0\n    total_episodes: 47\n    per_operator:\n      C1_context_truncation:\n        recovered: 8\n        total: 12\n        rate: 0.667\n      C4_observation_masking:\n        recovered: 7\n        total: 11\n        rate: 0.636\n      P1_step_order_swap:\n        recovered: 7\n        total: 12\n        rate: 0.583\n      P2_sub_goal_deletion:\n        recovered: 6\n        total: 12\n        rate: 0.5\n- exp_id: v4-taxei-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.35506879\n    token_accuracy: 0.89978214\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 109.2\n    train_runtime_sec: 6549.432\n    train_speed_s_per_it: 1.934\n    memory_gib: 18.49\n- exp_id: v4-random-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.35484016\n    final_loss: 0.16766574\n    token_accuracy: 0.94187103\n    avg_token_accuracy: 0.90849673\n    train_steps: 3387\n    train_epochs: 3\n    train_runtime_sec: 6609.3556\n    train_duration_min: 110.2\n    train_samples_per_second: 4.098\n    train_steps_per_second: 0.512\n    train_speed_s_per_it: 1.951\n    memory_gib: 18.49\n- exp_id: v4-fixed-inject10\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-fixed-inject25\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.308\n    token_accuracy: 0.888\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject25-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.285\n    token_accuracy: 0.893\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        success: 7\n        total: 11\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.489\n    eval_successes: 23\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 4\n        total: 6\n        rate: 0.667\n      pick_and_place_simple:\n        success: 3\n        total: 8\n        rate: 0.375\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 2\n        total: 7\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-random-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 7\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-taxei-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.259\n    token_accuracy: 0.911\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 53.1\n- exp_id: v4-random-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4226\n    final_step_loss: 0.3079\n    token_accuracy: 0.9\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 57\n- exp_id: v4-random-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-random-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n    train_loss: 0.4338\n    final_step_loss: 0.2618\n    token_accuracy: 0.91\n    train_duration_min: 53.1\n    memory_gib: 18\n    train_speed_s_per_it: 1.95\n- exp_id: v4-taxei-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_vanilla_seed42_pp: -10.6\n- exp_id: v4-random-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-random-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.574\n    eval_successes: 27\n    eval_total: 47\n    vs_vanilla_seed42_pp: -4.3\n    vs_taxei_50_pp: 6.3\n- exp_id: v4-random-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_vanilla_seed42_pp: -6.4\n    vs_taxei_25_pp: 6.4\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T02:28:23.140Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T02:28:23.140Z",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-15T02:28:23.160Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：核心 pattern 被证明是 seed=42 的偶然：多 seed 剂量-响应无一致 pattern，taxonomy penalty 在部分 seed 反转或消失，方差梯度在更多数据下变得不显著
核心假设：['新 seed 的剂量-响应不显示 threshold-plateau——有的线性下降，有的无单调关系', "taxonomy penalty 在某些 seed 为正（TaxEI > Random），消解 'constant offset' claim", '新增 seed 后 TaxEI 均值上移至 60%+，与 Vanilla 的差距缩小到 <4pp 且 p>0.3', '方差梯度在 5-seed 均值下 Random SD ≈ TaxEI SD，无法区分结构化注入与随机注入的不稳定性差异', '训练 loss 分析无信息量——注入样本与 clean 样本 loss 轨迹无系统差异']
关键指标范围：{'taxei_3seed_mean_pct': [59.0, 65.0], 'taxei_3seed_sd_pp': [4.0, 7.0], 'vanilla_3seed_sd_pp': [3.0, 6.0], 'taxonomy_penalty_per_dose_pp': [-2.0, 8.0], 'taxonomy_penalty_cross_dose_sd_pp': [3.5, 6.0], 'dose_threshold_drop_pp': [2.0, 14.0], 'pooled_p_taxei_vs_vanilla': [0.15, 0.6], 'paired_t_taxei_vs_random_p': [0.1, 0.5], 'dose_response_cross_seed_agreement': [0.2, 0.5]}
叙事方向：三个原始 finding 均不成立为独立 claim。需要 reframe。 新 angle：error injection 的效果被 seed variance 完全淹没—— 这本身就是 negative result，但 framing 从 "error injection hurts + here's why" 转向 "error injection is indistinguishable from noise in low-data embodied planning regimes"。 核心 contribution 变为：(1) ALFWorld SFT 的 cross-seed variance 之大使得任何 data augmentation 策略的评估都需要 ≥5 seeds（方法论 contribution）， (2) 在 <10K 样本规模下，error injection 的信号被训练噪声压制， 无法提供超出 seed lottery 的信息（scale-dependent null result）。 论文从 "boundary condition" paper 变为 "evaluation methodology" paper， 仍可投 Negative Results workshop，但需要重写 introduction 和 contribution section。 不降级 venue——Negative Results workshop 本身就欢迎 "we thought X mattered but it's noise"。

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
  "promptId": "8e561846-914e-4b3d-8046-bbcfe7a5c427",
  "type": "user",
  "uuid": "f3d65ea3-8c8e-49b4-8e73-4ced92d849d1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T02:28:23.159Z_

```json
{
  "parentUuid": "f3d65ea3-8c8e-49b4-8e73-4ced92d849d1",
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
  "uuid": "a318d105-fa4c-4b3b-a1f4-fbd32a0e694e",
  "timestamp": "2026-05-15T02:28:23.159Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T02:28:23.159Z_

```json
{
  "parentUuid": "a318d105-fa4c-4b3b-a1f4-fbd32a0e694e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "06ecd73e-8997-42ca-8437-3ac6ec96ecf8",
  "timestamp": "2026-05-15T02:28:23.159Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心 pattern 被证明是 seed=42 的偶然：多 seed 剂量-响应无一致 pattern，taxonomy penalty 在部分 seed 反转或消失，方差梯度在更多数据下变得不显著 核心假设：['新 seed 的剂量-响应不显示 threshold-plateau——有的线性下降，有的无单…",
  "leafUuid": "06ecd73e-8997-42ca-8437-3ac6ec96ecf8",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Error injection fails on embodied planning",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---

### Assistant

_source line 8 · 2026-05-15T02:28:26.933Z_

Let me first read the experiment plan to understand what planned experiments need predictions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06ecd73e-8997-42ca-8437-3ac6ec96ecf8",
  "isSidechain": false,
  "requestId": "req_011Cb3Zm9UBpHb5CRSeqBJbR",
  "type": "assistant",
  "uuid": "aa7e9b30-23cd-4ec2-a79d-82cb88db58e8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhwAWVroYF8oggiKAxrd5g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18484,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18484
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

_source line 9 · 2026-05-15T02:28:30.817Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UjkcHscV1FwU8dUEmRsyGU`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan file",
  "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_2 for files named \"experiment_plan\" or containing \"experiment_plan\" in the name. Also look for any YAML or markdown files that might contain planned experiments with status \"planned\". Search broadly - try patterns like *experiment_plan*, *exp_plan*, *plan*.yaml, *plan*.md, and also grep for \"status: planned\" or \"planned\" in yaml files."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa7e9b30-23cd-4ec2-a79d-82cb88db58e8",
  "isSidechain": false,
  "requestId": "req_011Cb3Zm9UBpHb5CRSeqBJbR",
  "type": "assistant",
  "uuid": "bd635ed7-a1f1-4b11-b903-efc92536c65a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhwAWVroYF8oggiKAxrd5g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 18484,
      "cache_read_input_tokens": 11841,
      "output_tokens": 212,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 212,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18484
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

_source line 10 · 2026-05-15T02:28:54.745Z_

<details><summary>↩ Tool result · `toolu_01UjkcHscV1FwU8dUEmRsyGU`</summary>

```text
Now let me create a comprehensive summary of my findings.

## Summary of Search Results

I've successfully searched the directory `/home/ubuntu/.agent-ml-research-idea_gen_0514_2` and found comprehensive experiment planning files with planned experiments. Here are my findings:

### Files Found

**Primary experiment plan files:**
1. `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/experiment_plan.yaml` (Main - 235 lines)
2. `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml` (Intermediate version - 242 lines)
3. `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/writing_plan.yaml` (Writing/experiment status plan - 248 lines)
4. `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/decisions.yaml` (Decision log with 17 decisions)

### Planned Experiments Found

**In `experiment_plan.yaml` (main file):**
The file tracks 12+ experiments with status "planned":
- `training-dynamics`: Training loss curve analysis (Priority 2, lines 165-173)
- `second-environment`: WebShop replication test (Priority 2, lines 175-182)
- `qualitative-failure-analysis`: Manual failure case examination (Priority 2, lines 184-191)
- `scale-ablation`: Scale to 25K-50K trajectories (Priority 3, lines 196-202)
- `recovery-prompting`: In-context recovery examples (Priority 3, lines 204-210)
- `per-operator-deepdive`: Multi-seed recovery eval (Priority 3, lines 212-218)

**In `writing_plan.yaml`:**
Contains 18 planned experiments across different priority levels:
- Priority high (blocks writing): 7 experiments including ablation ratios, fixed-size ablations, stats updates
- Priority medium: 3 experiments (recovery evals for seeds 0 and 123)
- Priority low: 4 per-operator ablation experiments

Key planned experiments include:
- `ablation-taxei-inject10` and `ablation-taxei-inject25` (injection ratio ablations)
- `ablation-taxei-fixed-size` and `ablation-random-fixed-size`
- `recovery-eval-seed0` and `recovery-eval-seed123`
- Per-operator ablations (P1, P2, C1, C4 operators)
- Statistical analysis updates (`multiseed-stats-update`, `fix-permutation-test`)

### Key Details

**Project Context:** tax_error_inject_agent - A negative result paper investigating when error injection helps vs hurts in LLM agents

**Experiment Plan Structure:** 
- Claims being tested: C1-C6 (about error injection effectiveness in ALFWorld)
- Dependencies tracked
- GPU hour estimates
- Execution phases and parallelization plan

**Status Tracking:**
- "done": Baseline and core multi-seed experiments completed
- "running": seed=123 TaxEI/Random training (as of 2026-05-14)
- "planned": All Priority 2/3 experiments plus supplementary analyses

The files are comprehensive ML research experiment planning documents with detailed metadata, dependency graphs, and statistical testing standards.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd635ed7-a1f1-4b11-b903-efc92536c65a",
  "isSidechain": false,
  "promptId": "8e561846-914e-4b3d-8046-bbcfe7a5c427",
  "type": "user",
  "uuid": "ac85cc28-13ea-4f3b-8124-7efd5194c865",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the directory /home/ubuntu/.agent-ml-research-idea_gen_0514_2 for files named \"experiment_plan\" or containing \"experiment_plan\" in the name. Also look for any YAML or markdown files that might contain planned experiments with status \"planned\". Search broadly - try patterns like *experiment_plan*, *exp_plan*, *plan*.yaml, *plan*.md, and also grep for \"status: planned\" or \"planned\" in yaml files.",
    "agentId": "a9b55ba11ebfa5993",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Now let me create a comprehensive summary of my findings.\n\n## Summary of Search Results\n\nI've successfully searched the directory `/home/ubuntu/.agent-ml-research-idea_gen_0514_2` and found comprehensive experiment planning files with planned experiments. Here are my findings:\n\n### Files Found\n\n**Primary experiment plan files:**\n1. `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/experiment_plan.yaml` (Main - 235 lines)\n2. `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/artifacts/_project/intermediate/experiment_plan.yaml` (Intermediate version - 242 lines)\n3. `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/writing_plan.yaml` (Writing/experiment status plan - 248 lines)\n4. `/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/decisions.yaml` (Decision log with 17 decisions)\n\n### Planned Experiments Found\n\n**In `experiment_plan.yaml` (main file):**\nThe file tracks 12+ experiments with status \"planned\":\n- `training-dynamics`: Training loss curve analysis (Priority 2, lines 165-173)\n- `second-environment`: WebShop replication test (Priority 2, lines 175-182)\n- `qualitative-failure-analysis`: Manual failure case examination (Priority 2, lines 184-191)\n- `scale-ablation`: Scale to 25K-50K trajectories (Priority 3, lines 196-202)\n- `recovery-prompting`: In-context recovery examples (Priority 3, lines 204-210)\n- `per-operator-deepdive`: Multi-seed recovery eval (Priority 3, lines 212-218)\n\n**In `writing_plan.yaml`:**\nContains 18 planned experiments across different priority levels:\n- Priority high (blocks writing): 7 experiments including ablation ratios, fixed-size ablations, stats updates\n- Priority medium: 3 experiments (recovery evals for seeds 0 and 123)\n- Priority low: 4 per-operator ablation experiments\n\nKey planned experiments include:\n- `ablation-taxei-inject10` and `ablation-taxei-inject25` (injection ratio ablations)\n- `ablation-taxei-fixed-size` and `ablation-random-fixed-size`\n- `recovery-eval-seed0` and `recovery-eval-seed123`\n- Per-operator ablations (P1, P2, C1, C4 operators)\n- Statistical analysis updates (`multiseed-stats-update`, `fix-permutation-test`)\n\n### Key Details\n\n**Project Context:** tax_error_inject_agent - A negative result paper investigating when error injection helps vs hurts in LLM agents\n\n**Experiment Plan Structure:** \n- Claims being tested: C1-C6 (about error injection effectiveness in ALFWorld)\n- Dependencies tracked\n- GPU hour estimates\n- Execution phases and parallelization plan\n\n**Status Tracking:**\n- \"done\": Baseline and core multi-seed experiments completed\n- \"running\": seed=123 TaxEI/Random training (as of 2026-05-14)\n- \"planned\": All Priority 2/3 experiments plus supplementary analyses\n\nThe files are comprehensive ML research experiment planning documents with detailed metadata, dependency graphs, and statistical testing standards."
      }
    ],
    "totalDurationMs": 23923,
    "totalTokens": 44319,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 948,
      "cache_read_input_tokens": 42531,
      "output_tokens": 834,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 948
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 834,
          "cache_read_input_tokens": 42531,
          "cache_creation_input_tokens": 948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 948,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 7,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "bd635ed7-a1f1-4b11-b903-efc92536c65a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T02:28:59.991Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Si3NTMZrSAWm2PqmTognSH`</summary>

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
  "parentUuid": "ac85cc28-13ea-4f3b-8124-7efd5194c865",
  "isSidechain": false,
  "requestId": "req_011Cb3ZoUSG8oBBBT3MKKQZP",
  "type": "assistant",
  "uuid": "112f8460-9d68-47db-b816-0bbb3a3c57a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JzC7LRuMZacs5BWnLsAReE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1054,
      "cache_read_input_tokens": 30325,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1054,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 30325,
          "cache_creation_input_tokens": 1054,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1054
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

_source line 12 · 2026-05-15T02:28:59.994Z_

<details><summary>↩ Tool result · `toolu_01Si3NTMZrSAWm2PqmTognSH`</summary>

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
17	  - id: "baseline"
18	    description: "Qwen3-8B zero-shot ReAct baseline on ALFWorld (47 tasks)"
19	    claim: "context"
20	    priority: 0
21	    status: done
22	    registry_id: "vanilla-react-baseline"
23	    depends_on: []
24	    results:
25	      accuracy: "42.6% (20/47)"
26	
27	  - id: "data-collection"
28	    description: "GPT-5.2 trajectory collection for SFT training data"
29	    claim: "prerequisite"
30	    priority: 0
31	    status: done
32	    registry_id: "traj_collect_500"
33	    depends_on: []
34	    results:
35	      success_rate: "70.2% (501/714)"
36	      cost: "$8.86"
37	
38	  # ============================================================
39	  # v3 Pilot (format-aligned, superseded by v4)
40	  # ============================================================
41	  - id: "v3-pilot"
42	    description: "v3 format-aligned pilot: vanilla/TaxEI/random single-seed eval"
43	    claim: "supplement"
44	    priority: 0
45	    status: done
46	    registry_id: "v3-vanilla-eval"
47	    depends_on:
48	      - data-collection
49	    results:
50	      vanilla: "74.5%"
51	      taxei: "66.0%"
52	      random: "51.1%"
53	    notes: "Superseded by v4. All registry: mini-vanilla-sft-v3, mini-taxei-sft-v3, mini-random-sft-v3, v3-vanilla-eval, v3-taxei-eval, v3-random-eval"
54	
55	  # ============================================================
56	  # Core Multi-Seed Experiments (v4) — Priority 1
57	  # ============================================================
58	  - id: "multiseed-vanilla"
59	    description: "Vanilla SFT 3-seed verification (clean data only, 4,358 samples)"
60	    claim: "C1"
61	    priority: 1
62	    status: done
63	    registry_id: "v4-vanilla-eval-r3"
64	    depends_on:
65	      - data-collection
66	    results:
67	      seed42: "61.7%"
68	      seed0: "68.1%"
69	      seed123: "66.0%"
70	      mean_sd: "65.3% ± 3.3pp"
71	    notes: "Train: mini-vanilla-sft-v4, v4-vanilla-seed0, v4-vanilla-seed123. Eval: v4-vanilla-eval-r3, v4-vanilla-seed0-eval, v4-vanilla-seed123-eval"
72	
73	  - id: "multiseed-taxei"
74	    description: "TaxEI SFT 3-seed verification (clean + taxonomy-tagged injections, 9,029 samples)"
75	    claim: "C1,C2,C3"
76	    priority: 1
77	    status: done
78	    registry_id: "v4-taxei-eval"
79	    depends_on:
80	      - data-collection
81	    results:
82	      seed42: "61.7%"
83	      seed0: "46.8%"
84	      seed123: "61.7%"
85	      mean_sd: "56.7% ± 8.6pp"
86	      vs_vanilla_paired_t_p: "0.32 (NS)"
87	      vs_vanilla_pooled_p: "0.054 (NS at α=0.05)"
88	    notes: "Train: v4-taxei-sft-r2, v4-taxei-seed0, v4-taxei-seed123. Eval: v4-taxei-eval, v4-taxei-seed0-eval, v4-taxei-seed123-eval"
89	
90	  - id: "multiseed-random"
91	    description: "Random SFT 3-seed verification (clean + unlabeled injections, 9,029 samples)"
92	    claim: "C2,C3"
93	    priority: 1
94	    status: done
95	    registry_id: "v4-random-eval"
96	    depends_on:
97	      - data-collection
98	    results:
99	      seed42: "66.0%"
100	      seed0: "55.3%"
101	      seed123: "68.1%"
102	      mean_sd: "63.1% ± 7.0pp"
103	      vs_taxei_paired_t_p: "0.034 (suggestive, df=2)"
104	      vs_taxei_pooled_p: "0.170 (NS)"
105	    notes: "Train: v4-random-sft-r2, v4-random-seed0, v4-random-seed123. Eval: v4-random-eval, v4-random-seed0-eval, v4-random-seed123-eval"
106	
107	  # ============================================================
108	  # Dose-Response Ablation — Priority 1
109	  # ============================================================
110	  - id: "dose-response-taxei"
111	    description: "TaxEI dose-response curve (10%/25%/50% injection, fixed 4,358 total, seed=42)"
112	    claim: "C3"
113	    priority: 1
114	    status: done
115	    registry_id: "v4-taxei-fixed-inject50-eval"
116	    depends_on:
117	      - multiseed-vanilla
118	    results:
119	      inject0_baseline: "61.7% (vanilla seed=42)"
120	      inject10: "61.7% (0pp)"
121	      inject25: "48.9% (-12.8pp)"
122	      inject50: "51.1% (-10.6pp)"
123	      pattern: "threshold-plateau: 10% harmless, 25% catastrophic collapse, 50% no further worsening"
124	    notes: "Train: v4-taxei-fixed-inject10, v4-taxei-fixed-inject25-r2, v4-taxei-fixed-inject50. Eval: v4-taxei-fixed-inject10-eval, v4-taxei-fixed-inject25-eval, v4-taxei-fixed-inject50-eval"
125	
126	  - id: "dose-response-random"
127	    description: "Random dose-response curve (10%/25%/50% injection, fixed 4,358 total, seed=42)"
128	    claim: "C3"
129	    priority: 1
130	    status: done
131	    registry_id: "v4-random-fixed-inject50-eval"
132	    depends_on:
133	      - multiseed-vanilla
134	    results:
135	      inject0_baseline: "61.7% (vanilla seed=42)"
136	      inject10: "68.1% (32/47, +6.4pp)"
137	      inject25: "55.3% (26/47, -6.4pp)"
138	      inject50: "57.4% (27/47, -4.3pp)"
139	    notes: "Train: v4-random-fixed-inject10, v4-random-fixed-inject25, v4-random-fixed-inject50. Eval: v4-random-fixed-inject10-eval, v4-random-fixed-inject25-eval, v4-random-fixed-inject50-eval. Random 10% positive effect contrasts with TaxEI 10% zero effect."
140	
141	  # ============================================================
142	  # Recovery & Detection Eval — Priority 1
143	  # ============================================================
144	  - id: "recovery-eval"
145	    description: "Recovery rate under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)"
146	    claim: "C4,C5"
147	    priority: 1
148	    status: done
149	    registry_id: "v4-taxei-recovery-eval-r2"
150	    depends_on:
151	      - multiseed-vanilla
152	      - multiseed-taxei
153	      - multiseed-random
154	    results:
155	      vanilla_recovery: "61.7%"
156	      taxei_recovery: "59.6%"
157	      random_recovery: "63.8%"
158	      detection_rate: "0% (all methods)"
159	      taxei_per_operator: "C1=66.7%, C4=63.6%, P1=58.3%, P2=50.0%"
160	    notes: "All registry: v4-vanilla-recovery-eval, v4-taxei-recovery-eval, v4-taxei-recovery-eval-r2, v4-random-recovery-eval"
161	
162	  # ============================================================
163	  # Priority 2 — Strengthens Paper Significantly
164	  # ============================================================
165	  - id: "training-dynamics"
166	    description: "Training loss curve analysis: clean vs injected samples across epochs"
167	    claim: "C3"
168	    priority: 2
169	    status: planned
170	    depends_on:
171	      - multiseed-taxei
172	      - multiseed-random
173	    notes: "Plot loss curves to show whether injected samples corrupt clean learning signal"
174	
175	  - id: "second-environment"
176	    description: "WebShop or ScienceWorld replication to test generalization beyond ALFWorld"
177	    claim: "C6"
178	    priority: 2
179	    status: planned
180	    depends_on:
181	      - dose-response-random
182	    notes: "Strengthens boundary condition claim if error injection also fails in second environment"
183	
184	  - id: "qualitative-failure-analysis"
185	    description: "Manual examination of 20+ TaxEI failure cases: incoherent plans vs wrong actions"
186	    claim: "C1,C6"
187	    priority: 2
188	    status: planned
189	    depends_on:
190	      - multiseed-taxei
191	    notes: "Informs noise-vs-wrong-learning distinction"
192	
193	  # ============================================================
194	  # Priority 3 — Nice-to-Have
195	  # ============================================================
196	  - id: "scale-ablation"
197	    description: "Scale to 25K-50K trajectories to match PALADIN's data scale"
198	    claim: "C6"
199	    priority: 3
200	    status: planned
201	    depends_on:
202	      - dose-response-random
203	
204	  - id: "recovery-prompting"
205	    description: "In-context recovery examples (few-shot) to isolate training signal vs knowledge"
206	    claim: "C6"
207	    priority: 3
208	    status: planned
209	    depends_on:
210	      - recovery-eval
211	
212	  - id: "per-operator-deepdive"
213	    description: "Multi-seed recovery eval to validate per-operator patterns (esp. C4 +9.1pp)"
214	    claim: "C4"
215	    priority: 3
216	    status: planned
217	    depends_on:
218	      - recovery-eval
219	
220	# ============================================================
221	# Failed/Killed Registry Entries (not part of active plan)
222	# ============================================================
223	# Retries, OOM failures, or superseded entries retained for provenance:
224	#   - v4-vanilla-sft (OOM), v4-taxei-sft (failed), v4-random-sft (failed)
225	#   - v4-vanilla-eval (failed), v4-vanilla-eval-r2 (failed)
226	#   - v4-taxei-sft-r3, v4-random-sft-r3 (retries)
227	#   - v4-taxei-fixed-inject25 (OOM, replaced by r2)
228	#   - v4-fixed-inject10, v4-fixed-inject25 (killed duplicates)
229	#   - v4-vanilla-seed7 (killed)
230	#   - v4-recovery-eval-dev, v4-recovery-dryrun (pipeline dev)
231	#   - mini-vanilla-sft (278-sample pilot, 14.9%)
232	#   - mini-taxei-sft (278-sample pilot, 44.7%)
233	#   - mini-pipeline-e2e (failed), sft-dryrun-73 (dryrun)
234	#   - vanilla_sft_aligned_v1, vanilla_sft_aligned_v2 (unfinished)
235	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "112f8460-9d68-47db-b816-0bbb3a3c57a6",
  "isSidechain": false,
  "promptId": "8e561846-914e-4b3d-8046-bbcfe7a5c427",
  "type": "user",
  "uuid": "dcde0dd0-3b4c-4ae2-984e-2d398d3d89f7",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/experiment_plan.yaml",
      "content": "# experiment_plan.yaml — tax_error_inject_agent (Negative Result Paper)\n# Updated: 2026-05-15\n#\n# Claims (from paper_framing.md):\n#   C1: TaxEI introduces high variance, fails to improve clean performance\n#   C2: Taxonomy labels provide no benefit over random injection\n#   C3: Error injection increases training instability (variance gradient + dose-response)\n#   C4: Injection-trained models do not improve error recovery\n#   C5: Detection training via error injection is completely ineffective\n#   C6: Divergence from PALADIN reveals task-structural boundary conditions\n\nexperiments:\n\n  # ============================================================\n  # Baselines & Prerequisites\n  # ============================================================\n  - id: \"baseline\"\n    description: \"Qwen3-8B zero-shot ReAct baseline on ALFWorld (47 tasks)\"\n    claim: \"context\"\n    priority: 0\n    status: done\n    registry_id: \"vanilla-react-baseline\"\n    depends_on: []\n    results:\n      accuracy: \"42.6% (20/47)\"\n\n  - id: \"data-collection\"\n    description: \"GPT-5.2 trajectory collection for SFT training data\"\n    claim: \"prerequisite\"\n    priority: 0\n    status: done\n    registry_id: \"traj_collect_500\"\n    depends_on: []\n    results:\n      success_rate: \"70.2% (501/714)\"\n      cost: \"$8.86\"\n\n  # ============================================================\n  # v3 Pilot (format-aligned, superseded by v4)\n  # ============================================================\n  - id: \"v3-pilot\"\n    description: \"v3 format-aligned pilot: vanilla/TaxEI/random single-seed eval\"\n    claim: \"supplement\"\n    priority: 0\n    status: done\n    registry_id: \"v3-vanilla-eval\"\n    depends_on:\n      - data-collection\n    results:\n      vanilla: \"74.5%\"\n      taxei: \"66.0%\"\n      random: \"51.1%\"\n    notes: \"Superseded by v4. All registry: mini-vanilla-sft-v3, mini-taxei-sft-v3, mini-random-sft-v3, v3-vanilla-eval, v3-taxei-eval, v3-random-eval\"\n\n  # ============================================================\n  # Core Multi-Seed Experiments (v4) — Priority 1\n  # ============================================================\n  - id: \"multiseed-vanilla\"\n    description: \"Vanilla SFT 3-seed verification (clean data only, 4,358 samples)\"\n    claim: \"C1\"\n    priority: 1\n    status: done\n    registry_id: \"v4-vanilla-eval-r3\"\n    depends_on:\n      - data-collection\n    results:\n      seed42: \"61.7%\"\n      seed0: \"68.1%\"\n      seed123: \"66.0%\"\n      mean_sd: \"65.3% ± 3.3pp\"\n    notes: \"Train: mini-vanilla-sft-v4, v4-vanilla-seed0, v4-vanilla-seed123. Eval: v4-vanilla-eval-r3, v4-vanilla-seed0-eval, v4-vanilla-seed123-eval\"\n\n  - id: \"multiseed-taxei\"\n    description: \"TaxEI SFT 3-seed verification (clean + taxonomy-tagged injections, 9,029 samples)\"\n    claim: \"C1,C2,C3\"\n    priority: 1\n    status: done\n    registry_id: \"v4-taxei-eval\"\n    depends_on:\n      - data-collection\n    results:\n      seed42: \"61.7%\"\n      seed0: \"46.8%\"\n      seed123: \"61.7%\"\n      mean_sd: \"56.7% ± 8.6pp\"\n      vs_vanilla_paired_t_p: \"0.32 (NS)\"\n      vs_vanilla_pooled_p: \"0.054 (NS at α=0.05)\"\n    notes: \"Train: v4-taxei-sft-r2, v4-taxei-seed0, v4-taxei-seed123. Eval: v4-taxei-eval, v4-taxei-seed0-eval, v4-taxei-seed123-eval\"\n\n  - id: \"multiseed-random\"\n    description: \"Random SFT 3-seed verification (clean + unlabeled injections, 9,029 samples)\"\n    claim: \"C2,C3\"\n    priority: 1\n    status: done\n    registry_id: \"v4-random-eval\"\n    depends_on:\n      - data-collection\n    results:\n      seed42: \"66.0%\"\n      seed0: \"55.3%\"\n      seed123: \"68.1%\"\n      mean_sd: \"63.1% ± 7.0pp\"\n      vs_taxei_paired_t_p: \"0.034 (suggestive, df=2)\"\n      vs_taxei_pooled_p: \"0.170 (NS)\"\n    notes: \"Train: v4-random-sft-r2, v4-random-seed0, v4-random-seed123. Eval: v4-random-eval, v4-random-seed0-eval, v4-random-seed123-eval\"\n\n  # ============================================================\n  # Dose-Response Ablation — Priority 1\n  # ============================================================\n  - id: \"dose-response-taxei\"\n    description: \"TaxEI dose-response curve (10%/25%/50% injection, fixed 4,358 total, seed=42)\"\n    claim: \"C3\"\n    priority: 1\n    status: done\n    registry_id: \"v4-taxei-fixed-inject50-eval\"\n    depends_on:\n      - multiseed-vanilla\n    results:\n      inject0_baseline: \"61.7% (vanilla seed=42)\"\n      inject10: \"61.7% (0pp)\"\n      inject25: \"48.9% (-12.8pp)\"\n      inject50: \"51.1% (-10.6pp)\"\n      pattern: \"threshold-plateau: 10% harmless, 25% catastrophic collapse, 50% no further worsening\"\n    notes: \"Train: v4-taxei-fixed-inject10, v4-taxei-fixed-inject25-r2, v4-taxei-fixed-inject50. Eval: v4-taxei-fixed-inject10-eval, v4-taxei-fixed-inject25-eval, v4-taxei-fixed-inject50-eval\"\n\n  - id: \"dose-response-random\"\n    description: \"Random dose-response curve (10%/25%/50% injection, fixed 4,358 total, seed=42)\"\n    claim: \"C3\"\n    priority: 1\n    status: done\n    registry_id: \"v4-random-fixed-inject50-eval\"\n    depends_on:\n      - multiseed-vanilla\n    results:\n      inject0_baseline: \"61.7% (vanilla seed=42)\"\n      inject10: \"68.1% (32/47, +6.4pp)\"\n      inject25: \"55.3% (26/47, -6.4pp)\"\n      inject50: \"57.4% (27/47, -4.3pp)\"\n    notes: \"Train: v4-random-fixed-inject10, v4-random-fixed-inject25, v4-random-fixed-inject50. Eval: v4-random-fixed-inject10-eval, v4-random-fixed-inject25-eval, v4-random-fixed-inject50-eval. Random 10% positive effect contrasts with TaxEI 10% zero effect.\"\n\n  # ============================================================\n  # Recovery & Detection Eval — Priority 1\n  # ============================================================\n  - id: \"recovery-eval\"\n    description: \"Recovery rate under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)\"\n    claim: \"C4,C5\"\n    priority: 1\n    status: done\n    registry_id: \"v4-taxei-recovery-eval-r2\"\n    depends_on:\n      - multiseed-vanilla\n      - multiseed-taxei\n      - multiseed-random\n    results:\n      vanilla_recovery: \"61.7%\"\n      taxei_recovery: \"59.6%\"\n      random_recovery: \"63.8%\"\n      detection_rate: \"0% (all methods)\"\n      taxei_per_operator: \"C1=66.7%, C4=63.6%, P1=58.3%, P2=50.0%\"\n    notes: \"All registry: v4-vanilla-recovery-eval, v4-taxei-recovery-eval, v4-taxei-recovery-eval-r2, v4-random-recovery-eval\"\n\n  # ============================================================\n  # Priority 2 — Strengthens Paper Significantly\n  # ============================================================\n  - id: \"training-dynamics\"\n    description: \"Training loss curve analysis: clean vs injected samples across epochs\"\n    claim: \"C3\"\n    priority: 2\n    status: planned\n    depends_on:\n      - multiseed-taxei\n      - multiseed-random\n    notes: \"Plot loss curves to show whether injected samples corrupt clean learning signal\"\n\n  - id: \"second-environment\"\n    description: \"WebShop or ScienceWorld replication to test generalization beyond ALFWorld\"\n    claim: \"C6\"\n    priority: 2\n    status: planned\n    depends_on:\n      - dose-response-random\n    notes: \"Strengthens boundary condition claim if error injection also fails in second environment\"\n\n  - id: \"qualitative-failure-analysis\"\n    description: \"Manual examination of 20+ TaxEI failure cases: incoherent plans vs wrong actions\"\n    claim: \"C1,C6\"\n    priority: 2\n    status: planned\n    depends_on:\n      - multiseed-taxei\n    notes: \"Informs noise-vs-wrong-learning distinction\"\n\n  # ============================================================\n  # Priority 3 — Nice-to-Have\n  # ============================================================\n  - id: \"scale-ablation\"\n    description: \"Scale to 25K-50K trajectories to match PALADIN's data scale\"\n    claim: \"C6\"\n    priority: 3\n    status: planned\n    depends_on:\n      - dose-response-random\n\n  - id: \"recovery-prompting\"\n    description: \"In-context recovery examples (few-shot) to isolate training signal vs knowledge\"\n    claim: \"C6\"\n    priority: 3\n    status: planned\n    depends_on:\n      - recovery-eval\n\n  - id: \"per-operator-deepdive\"\n    description: \"Multi-seed recovery eval to validate per-operator patterns (esp. C4 +9.1pp)\"\n    claim: \"C4\"\n    priority: 3\n    status: planned\n    depends_on:\n      - recovery-eval\n\n# ============================================================\n# Failed/Killed Registry Entries (not part of active plan)\n# ============================================================\n# Retries, OOM failures, or superseded entries retained for provenance:\n#   - v4-vanilla-sft (OOM), v4-taxei-sft (failed), v4-random-sft (failed)\n#   - v4-vanilla-eval (failed), v4-vanilla-eval-r2 (failed)\n#   - v4-taxei-sft-r3, v4-random-sft-r3 (retries)\n#   - v4-taxei-fixed-inject25 (OOM, replaced by r2)\n#   - v4-fixed-inject10, v4-fixed-inject25 (killed duplicates)\n#   - v4-vanilla-seed7 (killed)\n#   - v4-recovery-eval-dev, v4-recovery-dryrun (pipeline dev)\n#   - mini-vanilla-sft (278-sample pilot, 14.9%)\n#   - mini-taxei-sft (278-sample pilot, 44.7%)\n#   - mini-pipeline-e2e (failed), sft-dryrun-73 (dryrun)\n#   - vanilla_sft_aligned_v1, vanilla_sft_aligned_v2 (unfinished)\n",
      "numLines": 235,
      "startLine": 1,
      "totalLines": 235
    }
  },
  "sourceToolAssistantUUID": "112f8460-9d68-47db-b816-0bbb3a3c57a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13 · 2026-05-15T02:29:00.061Z_

````json
{
  "parentUuid": "dcde0dd0-3b4c-4ae2-984e-2d398d3d89f7",
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
  "uuid": "9d99ef6d-d427-4a4f-9ec0-c85bfef94891",
  "timestamp": "2026-05-15T02:29:00.061Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心 pattern 被证明是 seed=42 的偶然：多 seed 剂量-响应无一致 pattern，taxonomy penalty 在部分 seed 反转或消失，方差梯度在更多数据下变得不显著 核心假设：['新 seed 的剂量-响应不显示 threshold-plateau——有的线性下降，有的无单…",
  "leafUuid": "9d99ef6d-d427-4a4f-9ec0-c85bfef94891",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Error injection fails on embodied planning",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---

### Assistant

_source line 16 · 2026-05-15T02:29:39.416Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full experiment plan. There are 6 planned experiments:

1. **training-dynamics** (Priority 2) - Training loss curve analysis
2. **second-environment** (Priority 2) - WebShop/ScienceWorld replication
3. **qualitative-failure-analysis** (Priority 2) - Manual failure case examination
4. **scale-ablation** (Priority 3) - Scale to 25K-50K trajectories
5. **recovery-prompting** (Priority 3) - In-context recovery examples


6. **per-operator-deepdive** (Priority 3) - Multi-seed recovery eval

Now I'm working through what the worst-case scenario would look like for each experiment—where the seed=42 results were just noise and multi-seed validation reveals no consistent patterns. I need to think through how each experiment would fail under this tier: the taxonomy penalty effect disappears across different seeds, the variance gradient loses significance with more data, and the training dynamics show no meaningful differences.

Generating the YAML output with these worst-tier predictions...

For training-dynamics, the worst case is that clean and injected loss curves are indistinguishable—the injected samples just blend into the training signal without creating any detectable learning signature. With second-environment, the worst tier would show WebShop results contradicting the ALFWorld findings, suggesting the original failure was just seed variance and sample size rather than something fundamental about task structure. WebShop shows similar seed-dominated variance, making the result uninformative — OR error injection works somewhat on WebShop, making the boundary condition claim weaker (you can't say "embodied planning" is the issue if another planning task works). Let me think again.

The worst tier narrative is: "error injection is indistinguishable from noise in low-data embodied planning regimes." So for second-environment, worst would be:
- WebShop shows similar pattern: error injection neither helps nor hurts, high seed variance dominates
- This means the finding is not specific to ALFWorld task structure but rather to low-data regimes in general
- The "task structure" hypothesis (C6) is not supported; it's just a scale/data issue

For the failure analysis, if TaxEI and Vanilla produce identical error patterns—same branching-point mistakes, no systematic incoherence—then error injection isn't teaching wrong behaviors, just failing to teach anything useful. At larger scales (25K-50K), if TaxEI closes the gap with Vanilla, that undermines the structural incompatibility claim entirely; the problem was data volume, not task design. And if few-shot recovery prompting performs similarly across methods or doesn't help at all, it won't clarify whether the core issue is training signal versus model knowledge.

Now I'm working through the per-operator analysis. With more seeds, the C4 advantage disappears and per-operator recovery rates become indistinguishable with high variance—no operator shows consistent TaxEI benefit. I need to construct the detailed metrics carefully, setting realistic worst-tier ranges for the key values.

Constructing the YAML with these metric ranges...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d99ef6d-d427-4a4f-9ec0-c85bfef94891",
  "isSidechain": false,
  "requestId": "req_011Cb3Zos7mQLMhqeApr8v8y",
  "type": "assistant",
  "uuid": "b7ff647f-3325-4f14-b4fe-f23296195266",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcD21KxnsrQc8YsQP87bDu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8631,
      "cache_read_input_tokens": 31379,
      "output_tokens": 10365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10365,
          "cache_read_input_tokens": 31379,
          "cache_creation_input_tokens": 8631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8631
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

_source line 17 · 2026-05-15T02:32:35.511Z_

Now I have all the context. The experiment plan has 6 planned experiments. Let me generate the worst-tier predictions.

```yaml
tier: worst
narrative_guidance: >
  三个原始 finding（variance gradient, threshold-plateau dose-response, constant ~6.4pp taxonomy penalty）
  均被证明是 seed=42 的偶然产物。扩展 seed 后 TaxEI 均值上移至 ~62%，与 Vanilla 差距缩至 <4pp（p>0.3）；
  taxonomy penalty 在新 seed 出现正值（TaxEI > Random），cross-dose SD 达 4-5pp，"constant offset" 不成立；
  variance gradient 在 5-seed 均值下 Random SD ≈ TaxEI SD，无法区分结构化注入与随机注入的不稳定性差异。
  论文需要彻底 reframe：从 "error injection hurts + here's why" 转为
  "error injection is indistinguishable from noise in low-data embodied planning regimes"。
  核心 contribution 变为 (1) ALFWorld SFT 的 cross-seed variance 之大使任何 data augmentation
  评估需 ≥5 seeds（方法论 contribution），(2) <10K 样本下 error injection 信号被训练噪声压制
  （scale-dependent null result）。论文从 boundary condition paper 变为 evaluation methodology paper。

imagined_experiments:

  # ================================================================
  # Priority 2 — Strengthens Paper Significantly
  # ================================================================

  - name: "Training Dynamics Analysis"
    plan_id: "training-dynamics"
    description: >
      对 TaxEI 和 Random 的训练过程进行 loss curve 分解：分别追踪 clean 样本和 injected 样本
      在每个 epoch 的平均 loss，跨 3 个 seed 绘制均值±SE 曲线。目的是检验 injected 样本
      是否系统性地具有更高 loss（即模型是否「抵抗」学习错误 pattern）。
    expected_results:
      taxei_clean_loss_epoch3: 0.29
      taxei_injected_loss_epoch3: 0.31
      random_clean_loss_epoch3: 0.30
      random_injected_loss_epoch3: 0.30
      clean_vs_injected_loss_gap_taxei: 0.02
      clean_vs_injected_loss_gap_random: 0.01
      loss_gap_significant: false
      cross_seed_loss_curve_overlap: true
      clean_loss_trajectory_divergence_epoch: null
      injected_loss_reduction_rate_vs_clean: 0.97
    result_rationale: >
      在 worst 档下，injected 样本的 loss 轨迹与 clean 样本几乎完全重叠。
      TaxEI 的 clean-injected gap 仅 ~0.02（约 6% 相对差异），Random 几乎为零。
      这意味着模型以相同速率吸收了 clean 和 injected 样本——error injection
      既没有被模型「抵抗」（高 loss 不降），也没有造成 clean 样本 loss 反弹。
      模型把 taxonomy-tagged 错误当作普通数据学习了，没有产生可检测的学习动态差异。
      跨 seed 的 loss 曲线方差远大于 clean vs injected 的均值差，意味着
      seed lottery 的影响力完全碾压了数据类型的影响力。
      结论：training loss 分析无信息量——这本身支持 "error injection = noise" 的 reframing，
      但不再支持 "injected samples corrupt clean learning" 的原始叙事。
    tables:
      - title: "Training Loss by Sample Type (3-seed mean ± SE)"
        columns: ["Method", "Sample Type", "Epoch 1", "Epoch 2", "Epoch 3", "Cross-seed SD"]
        rows:
          - ["TaxEI", "Clean", "0.58 ± 0.03", "0.38 ± 0.02", "0.29 ± 0.02", "0.04"]
          - ["TaxEI", "Injected", "0.61 ± 0.04", "0.40 ± 0.03", "0.31 ± 0.03", "0.05"]
          - ["Random", "Clean", "0.57 ± 0.03", "0.37 ± 0.02", "0.30 ± 0.02", "0.04"]
          - ["Random", "Injected", "0.59 ± 0.03", "0.38 ± 0.02", "0.30 ± 0.02", "0.04"]
          - ["Vanilla", "Clean (all)", "0.56 ± 0.02", "0.36 ± 0.01", "0.29 ± 0.01", "0.03"]
    figures_description:
      - >
        Loss curve plot (2×1 panel): 左 TaxEI, 右 Random。每 panel 画 clean（蓝）和 injected（橙）
        的 3-seed mean ± shaded SE。两条线几乎完全重叠，SE band 互相覆盖。
        标注 "Cross-seed SD >> Clean-Injected gap" 以强调 seed variance 主导。
      - >
        Violin plot: 每个 seed 在 epoch 3 的 per-sample loss 分布，clean vs injected 分开。
        分布高度重叠，无系统偏移。个别 seed（如 seed=0）整体 loss 偏高，
        但 clean 和 injected 同步偏高，说明是 seed-level 效应而非 sample-type 效应。
    analysis: >
      该实验在 worst 档下提供了 "noise hypothesis" 的直接证据：模型无差别地学习了 clean 和
      injected 样本，error injection 未在训练动态层面产生可检测的信号。这与 PALADIN 形成鲜明对比——
      PALADIN 中 recovery 样本的 loss 显著低于 error 样本，说明模型学会了区分正确和错误行为。
      在 ALFWorld 中，这种区分不存在：embodied planning 的错误在 token 层面与正确行为无法区分
      （语法合法的错误步骤 loss 与正确步骤相当），模型缺乏从 loss 信号中提取 error pattern 的能力。
      Paper 中应将此定位为 "模型无法从 loss 信号区分正确与错误的 embodied planning 步骤"，
      这支持了 error observability 假设但削弱了 "injected samples corrupt training" 的原始叙事。
      在 worst 档下，这个实验的结论从 "证明 corruption mechanism" 变为 "证明 no mechanism at all"。

  - name: "Second Environment (WebShop) Replication"
    plan_id: "second-environment"
    description: >
      在 WebShop 环境复制核心实验：收集成功 trajectories，构建 Vanilla/TaxEI/Random 三组训练数据，
      3-seed SFT + eval。WebShop 是 web navigation 任务，介于 tool-use 和 embodied planning 之间——
      有部分 discrete feedback（页面内容变化），但也有 multi-step planning 特性。
      用于检验 negative result 是否泛化到 ALFWorld 之外的 planning 域。
    expected_results:
      webshop_vanilla_3seed_mean: 0.58
      webshop_vanilla_3seed_sd_pp: 5.2
      webshop_taxei_3seed_mean: 0.56
      webshop_taxei_3seed_sd_pp: 6.8
      webshop_random_3seed_mean: 0.57
      webshop_random_3seed_sd_pp: 6.1
      webshop_taxei_vs_vanilla_gap_pp: -2.0
      webshop_taxei_vs_vanilla_p: 0.55
      webshop_taxei_vs_random_gap_pp: -1.0
      webshop_taxei_vs_random_p: 0.72
      webshop_cross_seed_variance_ratio: 1.3
      alfworld_vs_webshop_pattern_match: "partial"
    result_rationale: >
      在 worst 档下，WebShop 呈现与 ALFWorld 类似的高 seed variance、方法间差异不显著的 pattern。
      TaxEI 在 WebShop 上也没有显著劣于 Vanilla（p=0.55），但也没有明显的 variance gradient——
      三种方法的 SD 差距仅 5.2 vs 6.8 vs 6.1pp，远不如 ALFWorld 的 3.3 vs 7.0 vs 8.6pp 那么分明。
      这使得 "task structure determines error injection effectiveness" 的 C6 假设难以成立：
      如果一个更接近 tool-use 的环境也表现出相同的 null result，那原因更可能是 data scale
      而非 task structure。worst 档强化了 "低数据量下 error injection 就是 noise" 的叙事，
      但削弱了 task-structural boundary condition 的 claim。
      WebShop 本身的高 seed variance（5.2pp）也支持了 "≥5 seeds 方法论" 的 contribution，
      说明这不是 ALFWorld 的特有问题而是 small-sample SFT 的通病。
    tables:
      - title: "WebShop 3-Seed Results"
        columns: ["Method", "Seed 42", "Seed 0", "Seed 123", "Mean ± SD"]
        rows:
          - ["Vanilla", "55.2%", "63.4%", "55.8%", "58.1% ± 5.2pp"]
          - ["TaxEI", "53.1%", "62.0%", "52.7%", "55.9% ± 6.8pp"]
          - ["Random", "54.8%", "62.5%", "53.4%", "56.9% ± 6.1pp"]
      - title: "Cross-Environment Comparison"
        columns: ["Metric", "ALFWorld", "WebShop"]
        rows:
          - ["Vanilla SD", "3.3pp", "5.2pp"]
          - ["TaxEI SD", "8.6pp", "6.8pp"]
          - ["TaxEI-Vanilla gap", "-8.6pp (p=0.32)", "-2.2pp (p=0.55)"]
          - ["Variance ratio TaxEI/Vanilla", "2.6×", "1.3×"]
          - ["Taxonomy penalty (TaxEI-Random)", "-6.4pp", "-1.0pp"]
    figures_description:
      - >
        Side-by-side bar chart: ALFWorld vs WebShop 的 3-seed mean ± SD。
        ALFWorld 的 error bars 较大且 TaxEI 明显低于 Vanilla；
        WebShop 三组几乎持平，error bars 大小相近。
        标注 "variance ratio 2.6× → 1.3×" 说明 ALFWorld 的 extreme variance gradient 不泛化。
    analysis: >
      WebShop 结果在 worst 档下瓦解了 C6 的 task-structural 论证：(1) WebShop 更接近 tool-use
      但同样显示 null result，说明 task structure 不是主因；(2) WebShop 缺乏 ALFWorld 的 extreme
      variance gradient（1.3× vs 2.6×），说明 variance gradient 可能是 ALFWorld 的数据特异性
      而非 error injection 的普遍效应；(3) 两个环境一致的 null result 反而强化了 data-scale 假设。
      Paper reframing 方向：不再声称 "task structure determines outcome"，
      而是 "在 <10K 样本的 agent SFT 中，error injection 的信号被 seed lottery 淹没，
      这在多个 planning 环境中一致成立"。这是更弱但更站得住脚的 claim。

  - name: "Qualitative Failure Analysis"
    plan_id: "qualitative-failure-analysis"
    description: >
      人工审查 ≥20 个 TaxEI 失败 case 和 ≥20 个 Vanilla 失败 case（seed=42 和 seed=0），
      按失败模式分类：(a) 错误物品选择、(b) 错误容器/位置、(c) 步骤顺序错误、(d) 无限循环/重复、
      (e) 其他。比较两组的失败模式分布，检验 TaxEI 是否产生了「结构性错误学习」
      （如 taxonomy operator 对应的特定错误 pattern 频率升高）。
    expected_results:
      n_taxei_failures_reviewed: 25
      n_vanilla_failures_reviewed: 20
      taxei_failure_mode_distribution:
        wrong_object: 0.28
        wrong_location: 0.24
        step_order: 0.16
        infinite_loop: 0.20
        other: 0.12
      vanilla_failure_mode_distribution:
        wrong_object: 0.30
        wrong_location: 0.25
        step_order: 0.15
        infinite_loop: 0.20
        other: 0.10
      failure_mode_distribution_chi2_p: 0.91
      taxonomy_operator_correlated_errors: 0
      taxei_produces_incoherent_plans: false
      taxei_failure_length_vs_vanilla: "comparable (mean 12.3 vs 11.8 steps)"
    result_rationale: >
      在 worst 档下，TaxEI 和 Vanilla 的失败模式分布几乎完全一致（chi2 p=0.91），
      无法区分两者。TaxEI 没有产生与 taxonomy operator 相关的特定错误 pattern——
      例如 P1（step_order_swap）训练并未导致 TaxEI 在 step_order 错误上的频率升高。
      TaxEI 的失败也不是 "incoherent plans"——步骤序列在语法和逻辑上与 Vanilla 的失败等价，
      只是在关键决策点（选哪个物品、去哪个位置）做出了错误选择。
      这直接支持 "error injection = noise" 的结论：injected 样本既没有教会模型特定的错误行为
      （wrong learning），也没有破坏模型的规划连贯性（corruption）。
      模型在所有条件下以相同的方式失败，说明 error injection 对模型的行为分布没有可检测的影响。
    tables:
      - title: "Failure Mode Distribution (TaxEI vs Vanilla)"
        columns: ["Failure Mode", "TaxEI (n=25)", "Vanilla (n=20)", "Δ"]
        rows:
          - ["Wrong object selection", "28%", "30%", "-2pp"]
          - ["Wrong location/container", "24%", "25%", "-1pp"]
          - ["Step order error", "16%", "15%", "+1pp"]
          - ["Infinite loop/repetition", "20%", "20%", "0pp"]
          - ["Other", "12%", "10%", "+2pp"]
          - ["Chi-squared test p-value", "", "", "0.91"]
      - title: "Taxonomy Operator → Error Pattern Correlation"
        columns: ["Operator", "Expected Error Mode", "TaxEI Rate", "Vanilla Rate", "Elevated?"]
        rows:
          - ["P1 (step_order_swap)", "Step order errors", "16%", "15%", "No"]
          - ["P2 (sub_goal_deletion)", "Missing sub-goals", "8%", "10%", "No"]
          - ["C1 (context_truncation)", "Wrong location", "24%", "25%", "No"]
          - ["C4 (observation_masking)", "Repeated actions", "12%", "10%", "No"]
    figures_description:
      - >
        Stacked bar chart: TaxEI vs Vanilla 的失败模式分布对比。
        两根 bar 的颜色分布几乎一致，视觉上无法区分。
        旁边标注 chi2 p=0.91 和 "failure modes indistinguishable"。
    analysis: >
      定性分析在 worst 档下彻底消解了 "wrong learning" 假说。如果 taxonomy labels 真的教会了模型
      特定的错误行为（如 paper_framing 中 "structured error patterns may teach the model
      specific wrong behaviors"），那么 TaxEI 应该在 taxonomy operator 对应的失败模式上
      显示升高。但事实是零相关。TaxEI 和 Vanilla 以完全相同的方式失败——
      错误选择的物品、去错误的位置、在相同的任务类型上挣扎。
      这意味着原始 C2 中 "constant ~6.4pp taxonomy label penalty" 的机制解释
      （"structured error patterns teach wrong behaviors"）不成立。
      在 worst 档下，6.4pp 差距本身就是 seed noise，所以无需解释机制。
      Paper 应删除所有关于 "taxonomy labels teach wrong behaviors" 的推测性论述。

  # ================================================================
  # Priority 3 — Nice-to-Have
  # ================================================================

  - name: "Scale Ablation (25K-50K trajectories)"
    plan_id: "scale-ablation"
    description: >
      将训练数据扩展到 25K 和 50K 轨迹（通过更多 GPT-5.2 trajectory 收集 + 更大规模注入），
      在 25K/50K 规模下重跑 Vanilla/TaxEI 3-seed 对比，
      检验 negative result 是否在匹配 PALADIN 数据规模后消失。
    expected_results:
      trajectories_collected_25k: 2500
      trajectories_collected_50k: 5000
      collection_cost_usd: 120.0
      scale_25k_vanilla_mean: 0.72
      scale_25k_vanilla_sd_pp: 2.8
      scale_25k_taxei_mean: 0.70
      scale_25k_taxei_sd_pp: 3.5
      scale_25k_gap_pp: -2.0
      scale_25k_p: 0.35
      scale_50k_vanilla_mean: 0.76
      scale_50k_vanilla_sd_pp: 2.1
      scale_50k_taxei_mean: 0.75
      scale_50k_taxei_sd_pp: 2.6
      scale_50k_gap_pp: -1.0
      scale_50k_p: 0.52
      variance_ratio_25k: 1.25
      variance_ratio_50k: 1.24
      scale_closes_gap: true
      variance_gradient_persists: false
    result_rationale: >
      在 worst 档下，scale-up 会同时做两件事：(1) 缩小所有方法的 cross-seed SD
      （从 ~3-8pp 降至 ~2-3pp），因为更多数据减少了训练随机性对最终性能的影响；
      (2) TaxEI-Vanilla gap 从 -8.6pp 缩至 25K 的 -2.0pp 和 50K 的 -1.0pp（p>0.3）。
      variance gradient 在 25K 时变为 1.25×（vs 原始 2.6×），在 50K 时进一步降至 1.24×，
      不再具有统计或实际意义。
      这意味着原始 finding 的 root cause 是 data scale 而非 task structure：
      在足够数据下，error injection 的信号不被噪声淹没，但也不提供超出 vanilla 的改进——
      它就是中性的。这彻底削弱了 C6 的 "task-structural boundary condition" claim，
      因为 PALADIN 的成功可能完全归因于 50K+ 的数据规模（+ inference-time retrieval），
      而非 tool-use vs planning 的结构差异。
      但这反过来强化了 worst 档的 reframed contribution：
      "<10K 样本下 error injection 信号被压制" 得到了 scale 实验的正面验证。
    tables:
      - title: "Scale Ablation Results (3-seed)"
        columns: ["Scale", "Vanilla Mean±SD", "TaxEI Mean±SD", "Gap (pp)", "p-value", "Var Ratio"]
        rows:
          - ["9K (original)", "65.3% ± 3.3pp", "56.7% ± 8.6pp", "-8.6", "0.32", "2.6×"]
          - ["25K", "72.0% ± 2.8pp", "70.0% ± 3.5pp", "-2.0", "0.35", "1.25×"]
          - ["50K", "76.0% ± 2.1pp", "75.0% ± 2.6pp", "-1.0", "0.52", "1.24×"]
    figures_description:
      - >
        Line plot: x=data scale (9K/25K/50K), y=3-seed mean accuracy, 两条线（Vanilla 蓝, TaxEI 橙）
        逐渐收敛。Error bars 也逐渐缩小。标注 "gap: -8.6pp → -2.0pp → -1.0pp"。
        在 9K 处两线有明显间距（但 error bars 重叠），25K/50K 处几乎合并。
      - >
        Bar chart: variance ratio (TaxEI SD / Vanilla SD) at each scale。
        9K = 2.6×, 25K = 1.25×, 50K = 1.24×。标注 threshold line at 1.5×
        说明 ≥25K 后 variance gradient 不再有实际意义。
    analysis: >
      Scale ablation 在 worst 档下是最具破坏力的实验：它直接证明所有原始 finding
      都是 low-data artifact。9K 规模下看到的 2.6× variance gradient、-8.6pp gap、
      threshold-plateau dose-response 等 pattern 在 25K 时已大幅消退，50K 时消失。
      这使得 paper 无法声称发现了 "task-structural boundary condition"——
      真正的 boundary condition 是 data scale。
      然而，这恰好支持了 worst 档的 reframed contribution：
      paper 可以说 "在 community 常用的 <10K 样本规模下，error injection 评估是不可靠的，
      需要 ≥5 seeds 且 ≥25K 样本才能得出有意义的结论"。
      这是一个更窄但更扎实的方法论 contribution。
      代价是 paper 的 novelty 进一步降低——从 "发现 boundary condition"
      降级为 "发现 evaluation pitfall"——但对 Negative Results workshop 仍然适合。

  - name: "Recovery Prompting (Few-Shot In-Context)"
    plan_id: "recovery-prompting"
    description: >
      不通过 SFT，直接在推理时给模型 3-5 个 error-recovery 示例（few-shot），
      测试模型是否能从 in-context examples 学会 recovery——
      隔离 "训练信号无效" vs "模型本身无法学习 recovery" 两种假说。
    expected_results:
      vanilla_0shot_recovery: 0.617
      vanilla_3shot_recovery: 0.62
      vanilla_5shot_recovery: 0.64
      taxei_0shot_recovery: 0.596
      taxei_3shot_recovery: 0.60
      taxei_5shot_recovery: 0.62
      few_shot_gain_pp: 2.0
      few_shot_gain_significant: false
      few_shot_vs_sft_recovery_gap_pp: 0.0
    result_rationale: >
      在 worst 档下，few-shot recovery prompting 带来的改进微乎其微（+2pp, NS），
      且对 Vanilla 和 TaxEI 的提升幅度相同。这意味着两个假说都部分成立：
      (1) 训练信号确实无效（SFT recovery 没有帮助），但 (2) in-context 信号同样无效——
      模型在 embodied planning 中根本无法从错误示例（无论是训练时还是推理时）中提取
      有用的 recovery 策略。这支持了 "error observability" 假设的更强版本：
      不仅是训练信号被噪声淹没，而是 embodied planning 错误在表示层面就不可观测，
      模型无论通过什么途径接触到错误示例，都无法从中学习。
      但由于 few-shot 本身 gain 极小（2pp），实验的区分力有限——
      它既不支持也不反驳任何特定假说，信息量低。
    tables:
      - title: "Recovery Rate: SFT vs Few-Shot Prompting"
        columns: ["Method", "0-shot", "3-shot", "5-shot", "Max Gain"]
        rows:
          - ["Vanilla SFT", "61.7%", "62.0%", "64.0%", "+2.3pp"]
          - ["TaxEI SFT", "59.6%", "60.0%", "62.0%", "+2.4pp"]
          - ["Random SFT", "63.8%", "64.0%", "65.0%", "+1.2pp"]
    figures_description:
      - >
        Grouped bar chart: 3 组（Vanilla/TaxEI/Random）× 3 条件（0/3/5-shot）。
        所有 bar 高度相近（59-65%），few-shot 提升肉眼难辨。
        Error bars（基于 47 task 的 binomial CI）完全重叠。
    analysis: >
      Recovery prompting 在 worst 档下是低信息量实验。Few-shot 几乎不影响 recovery，
      说明 embodied planning 的 error recovery 不是一个可以通过示例（无论 SFT 还是 ICL）
      学会的能力——至少在当前模型和环境规模下如此。
      这对 paper reframing 有间接价值：支持 "error injection 在 embodied planning 中
      根本无效" 的 null result，但不提供关于 "为什么无效" 的新 insight。
      建议在 paper 中用 1-2 句话提及，不值得展开为独立 finding。

  - name: "Per-Operator Recovery Deep Dive (Multi-Seed)"
    plan_id: "per-operator-deepdive"
    description: >
      对 recovery eval 扩展到 3 个 seed（42/0/123），每个 seed 跑 47 tasks × 4 operators，
      目的是验证 seed=42 观察到的 per-operator 差异（C4 +9.1pp, C1 -8.3pp）是否跨 seed 稳定。
    expected_results:
      n_seeds: 3
      n_tasks_per_seed: 47
      taxei_per_operator_3seed:
        C1_context_truncation:
          mean: 0.62
          sd_pp: 5.5
          vs_vanilla_pp: -1.0
        C4_observation_masking:
          mean: 0.60
          sd_pp: 7.2
          vs_vanilla_pp: 0.0
        P1_step_order_swap:
          mean: 0.58
          sd_pp: 6.8
          vs_vanilla_pp: -2.0
        P2_sub_goal_deletion:
          mean: 0.54
          sd_pp: 8.1
          vs_vanilla_pp: -3.0
      c4_advantage_seed42_only: true
      c4_advantage_3seed_pp: 0.0
      per_operator_any_significant: false
      operator_variance_dominates: true
    result_rationale: >
      在 worst 档下，seed=42 观察到的 per-operator 差异完全被新 seed 消解。
      C4 在 seed=42 的 +9.1pp 优势在 seed=0 变为 -5pp、seed=123 变为 -4pp，
      3-seed 均值归零。所有 operator 的 TaxEI vs Vanilla 差异在 3-seed 均值下
      均落入 ±3pp 内（SD 5-8pp），无一显著。
      P2（sub_goal_deletion）在 3-seed 均值下 TaxEI 低 3pp，是最大负差，
      但 SD=8.1pp 意味着不显著。
      Cross-operator 的方差远大于 method 间差异：每个 operator 的 cross-seed SD
      在 5.5-8.1pp，而 method 间 gap 在 ±3pp——再次印证 seed lottery 主导。
      原始报告中 "TaxEI advantage only on C4_observation_masking (+9.1pp)"
      被证明是 seed=42 的偶然，不应作为论文 finding。
    tables:
      - title: "Per-Operator Recovery Rate (TaxEI, 3-seed mean ± SD)"
        columns: ["Operator", "Seed 42", "Seed 0", "Seed 123", "Mean ± SD", "vs Vanilla"]
        rows:
          - ["C1 (context_trunc)", "66.7%", "58.3%", "61.5%", "62.2% ± 5.5pp", "-1.0pp"]
          - ["C4 (obs_masking)", "72.7%", "50.0%", "56.0%", "59.6% ± 7.2pp", "0.0pp"]
          - ["P1 (step_swap)", "58.3%", "50.0%", "65.0%", "57.8% ± 6.8pp", "-2.0pp"]
          - ["P2 (subgoal_del)", "50.0%", "42.0%", "70.0%", "54.0% ± 8.1pp", "-3.0pp"]
      - title: "Per-Operator Vanilla Baseline (3-seed mean)"
        columns: ["Operator", "Mean", "SD"]
        rows:
          - ["C1", "63.2%", "4.8pp"]
          - ["C4", "59.6%", "5.0pp"]
          - ["P1", "59.8%", "4.2pp"]
          - ["P2", "57.0%", "5.5pp"]
    figures_description:
      - >
        Heatmap: rows = operators (C1/C4/P1/P2), columns = seeds (42/0/123)。
        Cell 颜色 = TaxEI 与 Vanilla 的差值 (pp)。seed=42 列有明显的
        C4 深绿（+9.1pp）和 C1/P2 深红（-8.3pp），但其他列颜色分布随机，
        无行级或列级一致 pattern。标注 "no operator shows consistent advantage"。
      - >
        Forest plot: 每个 operator 的 3-seed mean TaxEI-Vanilla difference ± 95% CI。
        所有 CI 都跨零线，没有任何 operator 的 CI 完全位于正或负侧。
    analysis: >
      Per-operator deep dive 在 worst 档下彻底消解了所有 operator-level 的定向 finding。
      原始论文中暗示 "C4 (observation masking) 是 TaxEI 唯一有优势的 operator" 的叙事
      被证明是 seed=42 的偶然。3-seed 均值下没有任何 operator 显示 TaxEI 的一致优势或劣势。
      这对 C4 的原始叙事（"TaxEI advantage only on C4_observation_masking"）和
      潜在的 "某些 error type 更适合 injection training" 的研究方向都是坏消息。
      Paper 应删除所有 per-operator 的定向 claim，仅保留 "per-operator 分析在 3-seed
      下无显著 pattern" 的一句话总结。如果要保留 per-operator 数据，放 appendix。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7ff647f-3325-4f14-b4fe-f23296195266",
  "isSidechain": false,
  "requestId": "req_011Cb3Zos7mQLMhqeApr8v8y",
  "type": "assistant",
  "uuid": "49bdc9e4-ce83-409c-82f6-f69678fe3df9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcD21KxnsrQc8YsQP87bDu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8631,
      "cache_read_input_tokens": 31379,
      "output_tokens": 10365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8631,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10365,
          "cache_read_input_tokens": 31379,
          "cache_creation_input_tokens": 8631,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8631
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心 pattern 被证明是 seed=42 的偶然：多 seed 剂量-响应无一致 pattern，taxonomy penalty 在部分 seed 反转或消失，方差梯度在更多数据下变得不显著 核心假设：['新 seed 的剂量-响应不显示 threshold-plateau——有的线性下降，有的无单…",
  "leafUuid": "49bdc9e4-ce83-409c-82f6-f69678fe3df9",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Error injection fails on embodied planning",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：核心 pattern 被证明是 seed=42 的偶然：多 seed 剂量-响应无一致 pattern，taxonomy penalty 在部分 seed 反转或消失，方差梯度在更多数据下变得不显著 核心假设：['新 seed 的剂量-响应不显示 threshold-plateau——有的线性下降，有的无单…",
  "leafUuid": "49bdc9e4-ce83-409c-82f6-f69678fe3df9",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Error injection fails on embodied planning",
  "sessionId": "2b57ccaa-648a-4b79-b1d8-f74354c4838b"
}
```

---
