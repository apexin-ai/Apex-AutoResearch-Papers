# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2.jsonl`
- **Structured JSON:** [`e3c8d8f0281a829c8b9d.json`](../../sessions/e3/e3c8d8f0281a829c8b9d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-16T15:39:47.947Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-16T15:39:47.947Z",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: tax_error_inject_agent\nfocus: Cross-model validation升级：TaxEI结构化注入跨模型不稳定（Qwen一致退化、LLaMA高方差1/3 catastrophic seed），Random注入跨模型稳定。论文核心从\"单模型负面结果\"升级为\"结构化vs随机注入的训练稳定性差异是跨架构通用的\"。评估新framing能否支撑EMNLP Findings长文。\n\n## paper_framing.md\n\n# Paper Framing: When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning\n\n## Target Venue\n**Primary**: EMNLP 2026 Findings (Budapest, Oct 22–29) — 8-page long paper. Negative-result contributions accepted per CFP.\n**Secondary**: ACL 2026 Findings if timeline permits.\n\n## Core Question\nUnder what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?\n\n## Thesis Statement\nTaxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training without improving performance on ALFWorld. TaxEI and Random injection produce **identical** mean performance (58.3% vs Vanilla 67.3%, 5 seeds each), proving taxonomy labels provide zero benefit. Complete 5-seed dose-response reveals **no safe injection dose**: harm begins at 10% (-6.0pp), peaks at 25% (TaxEI nadir 52.7%), then **saturates** — 50% and Full produce similar harm (~58%) with no marginal worsening. The taxonomy penalty follows an **inverted-U curve**, peaking at 25% (-7.3pp TaxEI-Random gap) and vanishing at higher doses. At every concentration, training outcomes are a **lottery** (19-23pp within-dose range, bimodal seed distributions). Cross-model validation on LLaMA-3.1-8B-Instruct reveals that **structured error injection (TaxEI) causes training instability across model architectures** — TaxEI recovery SD=8.6pp vs Random SD=2.1pp (3-seed), with 1/3 seeds triggering Qwen-like catastrophic degradation (59.6% vs baseline 73.1%). Random injection remains stable and even mildly beneficial (mean 76.6% > Vanilla 73.1%). This confirms the harm is not model-specific but a property of structured error patterns themselves: taxonomy-guided injection creates conflicting learning signals that destabilize training across architectures, while unstructured noise is benign or helpful.\n\n## Story Arc\n\n### 1. Motivation: Why error injection should work\nError injection is a principled data augmentation strategy: expose the model to failure modes during training so it learns to avoid or recover from them. PALADIN (arXiv 2509.25238) demonstrated this for tool-use agents, using a ToolScan taxonomy of 7 failure types to generate 50K+ recovery-annotated trajectories plus inference-time retrieval of 55+ exemplars, boosting Recovery Rate from 32.76% to 89.68% on ToolBench (note: removing retrieval reduces the gain by ~30pp, so the SFT contribution alone is ~+27pp). A natural question: does the error-injection training component transfer to embodied planning, where agents execute multi-step plans in physical environments?\n\n### 2. Method: TaxEI — Taxonomy-guided Error Injection for Embodied Planning\nWe designed a 4-operator error taxonomy for ALFWorld embodied planning:\n- **P1** (step_order_swap): permute action ordering\n- **P2** (sub_goal_deletion): remove sub-goals\n- **C1** (context_truncation): truncate environmental context\n- **C4** (observation_masking): mask observation feedback\n\nWe injected errors into 760 trajectories (from 501 GPT-5.2-generated successful trajectories), producing 4,671 injected variants. Three SFT conditions trained on Qwen3-8B: Vanilla (clean only, 4,358 samples), TaxEI (clean + taxonomy-tagged injections, 9,029 samples), Random (clean + unlabeled injections, 9,029 samples). TaxEI and Random differ only in whether the error tag contains the taxonomy label or a generic marker.\n\n### 3. Finding: Injection harms equally regardless of taxonomy; introduces catastrophic seed vulnerability\n**Clean task performance (all 5-seed complete)**:\n- Vanilla SFT: 67.3% ± 4.7pp (seeds 42/0/123/1/7) — stable, no catastrophic seeds\n- TaxEI SFT: 58.3% ± 6.5pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.039 uncorrected, NS Bonferroni (p>0.017), Cohen's d=1.58**\n- Random SFT: 58.3% ± 8.7pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.089 uncorrected, NS, Cohen's d=1.28**\n\n**CENTRAL FINDING**: TaxEI and Random produce IDENTICAL mean performance (58.3% = 137/235 tasks). Taxonomy labels provide zero benefit over random injection at the mean level. This directly refutes the hypothesis that structured error labeling improves training signal.\n\n**Catastrophic seed vulnerability**: Both injection methods produce exactly one ~47% outlier (TaxEI seed0=46.8%, Random seed1=46.8%). Vanilla never drops below 61.7%. Injection introduces a 1-in-5 risk of catastrophic training failure absent in clean training.\n\n**Variance gradient**: Vanilla SD (4.7pp) < TaxEI SD (6.5pp) < Random SD (8.7pp). Injection amplifies variance; taxonomy labels may mildly stabilize (TaxEI SD < Random SD), but both are worse than Vanilla. This reverses the 3-seed pattern (where TaxEI had highest SD). Formal variance tests needed (Levene's, n=5).\n\n**Dose-response ablation (fixed-size 4,358 total)** (D034+D035+D038: 全部 5 个剂量完整 5-seed):\n| Dose | TaxEI Mean±SD (n) | Random Mean±SD (n) | Vanilla ref | TaxEI-Random Δ |\n|------|-------------------|-------------------|-------------|----------------|\n| 0% (vanilla) | — | — | 67.3±4.7 (5) | — |\n| 10% | 61.3±8.2 (5) | 63.8±5.4 (5) | | -2.5pp |\n| 25% | 52.7±7.6 (5) | 60.0±8.0 (5) | | **-7.3pp** |\n| 50% | 57.4±9.5 (5) | 58.3±11.7 (5) | | -0.9pp |\n| Full | 58.3±6.5 (5) | 58.3±8.7 (5) | | 0pp |\n\nPer-seed data:\n- TaxEI 10%: 61.7/70.2/55.3/51.1/68.1. Random 10%: 68.1/66.0/55.3/68.1/61.7.\n- TaxEI 25%: 48.9/46.8/46.8/63.8/57.4. Random 25%: 55.3/61.7/51.1/72.3/59.6.\n- TaxEI 50%: 51.1/70.2/46.8/63.8/55.3. Random 50%: 57.4/46.8/70.2/70.2/46.8.\n\n**Unified dose-response narrative** (D035+D038, complete 5-seed all doses):\n1. **Non-monotonic harm with 25% nadir + saturation**: Injection at ALL doses reduces mean and increases variance. Harm peaks at 25% (TaxEI nadir 52.7%), then partially rebounds: 50% (57.4%) ≈ Full (58.3%). Doubling injection from 50%→Full has zero marginal effect — ~50% is the saturation point beyond which additional errors no longer worsen outcomes.\n2. **Inverted-U taxonomy penalty**: TaxEI trails Random at every dose, but the gap peaks at 25% (7.3pp), diminishes at 50% (0.9pp, d=-0.08 negligible), and vanishes at Full (0pp). At 10% the gap is 2.5pp. Taxonomy labels actively harm at intermediate doses where clean/injected balance may maximize conflicting learning signals.\n3. **Universal training lottery**: All doses produce extreme seed variance (19-23pp within-dose range). Random 50% shows **bimodal** distribution: {46.8, 46.8, 57.4, 70.2, 70.2} — two distinct failure/success modes, not normal scatter. Report median+IQR alongside mean±SD for robustness.\n4. **Practical implication**: No injection dose is \"safe.\" Even 10% produces measurable harm (-6.0pp TaxEI). Outcomes are unpredictable at every concentration level. The training lottery, not dosage, dominates performance variation.\n\n**Variance pattern** (exploratory, not claimable): SD peaks at 50% (TaxEI 9.5, Random 11.7) then **declines** at Full (6.5, 8.7). This is unexpected — Full dose actually reduces variance vs 50%. Possible explanation: at 50%, the model faces maximum ambiguity between clean and error patterns; at Full, the injection signal dominates and the model consistently adapts (poorly). Levene's test NS at n=5. Do not claim variance patterns without significance tests.\n\n**Training lottery at all doses**: Extreme outliers in every condition — TaxEI 10% s0=70.2% vs s1=51.1% (19pp range), Random 25% s1=72.3% vs s123=51.1% (21pp range), Random 50% bimodal (23pp range). Single-seed evaluations are fundamentally unreliable at any dose.\n\n**Taxonomy label penalty** (task-type-specific): TaxEI trails Random in aggregate. Per-task 3-seed analysis: taxonomy injection specifically harms **multi-step coordination tasks** — pick_cool_then_place (TaxEI 38.1% vs Random 57.1%, -19.0pp) and pick_two_obj_and_place (42.9% vs 57.1%, -14.3pp) — while leaving simple tasks largely unaffected (≤4.2pp gap for other 4 task types).\n\n**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:\n- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%\n\n**Recovery ≈ Resilience (D041)**: Recovery eval rates match normal eval rates for all conditions (V: 61.7%=61.7%, T: 59.6%≈61.7%, R: 63.8%≈66.0%). Models succeed at the same base rate regardless of eval-time error injection — they passively ignore perturbations rather than actively recovering. This is **resilience** (noise tolerance from task competence), not **recovery** (error detection + correction). No training regime instills genuine error awareness.\n\n**Detection Rate**: 0% for all methods.\n\n**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).\n\n**Per-operator local/global split** (recovery eval, seed=42, verified from eval JSON, **exploratory — N=11-12 per operator**): C4_observation_masking (+9.1pp, 6→7/11), P1_step_order_swap (0.0pp, 7→7/12), C1_context_truncation (−8.3pp, 9→8/12), P2_sub_goal_deletion (−8.3pp, 7→6/12). NOT a smooth monotonic gradient — instead a binary split: the most local/observable operator (C4) shows TaxEI advantage; global/cascading operators (C1, P2) show equal disadvantage; P1 is neutral. **Critical caveat**: each delta is driven by ±1 task success/failure at N=11-12 — well within random noise. Fisher exact tests would be NS for all operators. This must be presented as exploratory/hypothesis-generating, not confirmatory. The directional pattern (local positive, global negative) is suggestive but the specific magnitudes (9.1pp, 8.3pp) carry false precision.\n\n**Variance tests**: Observed SD gradient: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. F-test p=0.252 (NS, underpowered at df=2,2), but Levene's test p=0.085 (NS), Brown-Forsythe p=0.842 (NS), bootstrap P(SD_TaxEI > SD_Vanilla) = 0.688. All formal tests NS at n=3 — the variance gradient is a directional observation, not a statistically confirmed effect. Report as \"observed pattern, suggestive but underpowered.\"\n\n**Training-evaluation paradox** (≥25% injection only): At high injection ratios, training loss is lower (taxei_50%: 0.260, random_50%: 0.260 vs vanilla: 0.294) but eval performance is worse (51.1-57.4% vs 61.7%). However, at 10% injection, training loss is actually *higher* (0.308) than vanilla — the paradox only emerges above the dose-response threshold. This is consistent with the threshold effect: low injection doesn't change the training distribution enough to lower loss, while high injection causes the model to memorize error patterns. Literature support: Arpit et al. (2017) memorization dynamics, Zhou et al. (2023 LIMA) superficial alignment hypothesis.\n\n### 4. Analysis: Why it fails in embodied planning but works in tool-use\n\n**Important caveat**: The comparison with PALADIN involves multiple confounding variables beyond task structure (base model, training scale, training recipe, evaluation environment). We hypothesize task structure as the primary factor but cannot rule out other explanations without controlled cross-domain validation. The analysis below identifies the most plausible structural differences.\n| Dimension | Tool-Use (PALADIN ✓) | Embodied Planning (TaxEI ✗) |\n|-----------|----------------------|------------------------------|\n| **Error observability** | Explicit — API returns error codes, timeouts, exceptions | Implicit — wrong action sequences look syntactically valid |\n| **Recovery action space** | Bounded — retry, switch tool, modify arguments | Unbounded — must re-plan entire action sequence |\n| **Error locality** | Single turn — one API call fails | Cascading — one wrong step invalidates all downstream |\n| **Signal-to-noise in training** | 80% recovery / 20% clean (PALADIN) | 50% injected / 50% clean — injection overwhelms signal |\n| **Training scale** | 50K+ trajectories | 9K trajectories (4.7K injected) |\n| **Feedback granularity** | Per-tool success/fail signal | Sparse reward — only task completion |\n| **Inference-time augmentation** | 55+ exemplar retrieval (removes retrieval → RR drops ~30pp) | None — pure SFT, no inference-time augmentation |\n\n**Core hypothesis**: In tool-use, errors are **discrete, observable, and locally recoverable** — making error-injected training a form of targeted curriculum. In embodied planning, errors are **diffuse, silent, and globally cascading** — making injected samples indistinguishable from noise that corrupts the correct action distribution.\n\n**Critical nuance on PALADIN**: PALADIN's +57pp gain includes inference-time retrieval of 55+ exemplars; removing retrieval reduces recovery by ~30pp. This means PALADIN's success is partially attributable to retrieval augmentation, not purely to error-injection training. Our comparison therefore tests error injection in its most isolated form (pure SFT, no retrieval), which may be a stricter — and more informative — test of whether the training signal itself transfers.\n\n### 4b. Cross-Model Validation: TaxEI instability is not model-specific (LLaMA-3.1-8B-Instruct, 3-seed)\n\nTo test whether the TaxEI failure is Qwen-specific or a general property of structured error injection in embodied planning, we replicate the core experiment on LLaMA-3.1-8B-Instruct (3 seeds: 42/0/123). Training setup identical: Vanilla 4,358 samples (1,635 steps), TaxEI/Random 9,029 samples (3,387 steps).\n\n**LLaMA Recovery Rate (injected eval, 47 tasks)**:\n| Condition | s0 (eval=42) | s42 (eval=42) | s123 (eval=123) | Mean±SD |\n|-----------|:------------:|:-------------:|:---------------:|:-------:|\n| Vanilla | 74.5% | 74.5% | 70.2% | 73.1±2.5% |\n| TaxEI | 74.5% | 74.5% | **59.6%** | 69.5±8.6% |\n| Random | 74.5% | 76.6% | **78.7%** | 76.6±2.1% |\n\n**LLaMA Clean Success Rate**:\n| Condition | s0 | s42 | s123 | Mean±SD |\n|-----------|:--:|:---:|:----:|:-------:|\n| Vanilla | 72.3% | 72.3% | 72.3% | 72.3±0.0% |\n| TaxEI | 76.6% | 76.6% | **61.7%** | 71.6±8.6% |\n| Random | 74.5% | 76.6% | 76.6% | 75.9±1.2% |\n\n**Key findings**:\n1. **TaxEI training instability is cross-model**: 1/3 seeds (s123) triggers catastrophic degradation on LLaMA (-13.5pp recovery vs vanilla-s123, -10.6pp clean). Pattern mirrors Qwen's consistent degradation but with higher variance (2/3 seeds appear neutral).\n2. **Random injection is cross-model stable**: SD=2.1% (recovery), no catastrophic seeds, mean slightly above Vanilla (+3.5pp). This is the opposite of Qwen where Random also degraded.\n3. **TaxEI vs Random divergence**: On LLaMA, TaxEI mean (69.5%) < Random mean (76.6%), gap = -7.1pp. The variance difference is stark: TaxEI SD=8.6% vs Random SD=2.1%. Structured error patterns create training instability that unstructured noise does not.\n4. **Model-dependent severity, model-independent direction**: Qwen shows consistent TaxEI harm (-9pp, low variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, high variance with catastrophic 1/3 seed). The *direction* (TaxEI ≤ Random ≤ Vanilla for stability) holds across models; the *severity* varies.\n\n**Implication for paper story**: The finding upgrades from \"negative result on one model\" to \"structured error injection is fundamentally destabilizing for embodied planning across architectures.\" The taxonomy's structured perturbations create systematic biases that some training seed/model combinations amplify into catastrophic failure, while random noise averages out harmlessly.\n\n**Eval seed caveat**: s0/s42 use eval seed=42; s123 uses eval seed=123. Cross-seed aggregation (mean±SD) has a minor eval-seed confound (~2pp from eval randomness). Within each eval-seed group, horizontal (condition) comparisons are fully fair. The critical finding (taxei-s123 collapse) is a within-group horizontal comparison.\n\n### 5. Contribution: What this negative result gives the community\n1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.\n2. **Recovery-pairing disentanglement** (long paper NEW): By testing recovery-paired injection on ALFWorld, we isolate whether the negative result stems from missing recovery pairing or from fundamental task-structure differences. This is the first controlled test of recovery-paired vs unpaired error injection in embodied planning.\n3. **Recovery vs resilience distinction** (long paper NEW): Recovery eval rates match normal eval rates — models passively ignore eval-time errors (resilience) rather than actively recovering (recovery). Combined with 0% detection rate, this shows error injection creates no form of error awareness in embodied planning.\n4. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp, 5-seed confirmed). Single-seed evaluations of error injection methods are fundamentally unreliable.\n7. **Cross-model instability** (long paper NEW): TaxEI structured injection destabilizes training on both Qwen3-8B (consistent -9pp) and LLaMA-3.1-8B-Instruct (intermittent, 1/3 catastrophic seed), while Random injection remains stable across both models. This separates the harm attribution: it is structured error patterns — not model weakness — that cause instability.\n5. **No-safe-threshold dose-response + training lottery**: Complete 5-seed dose-response ablation (fixed data size, all 5 doses × 5 seeds) shows harm at every tested dose: 10% (-6.0pp TaxEI), 25% (nadir, -14.6pp TaxEI), 50% (-9.9pp TaxEI), Full (-9.0pp). Non-monotonic: harm peaks at 25%, partial rebound at higher doses. Taxonomy penalty follows inverted-U curve: 10% (-2.5pp) → 25% (-7.3pp peak) → 50% (-0.9pp) → Full (0pp). No injection dose is \"safe.\" Training lottery (19-23pp within-dose range) operates at all concentration levels.\n6. **Failure mode taxonomy** (long paper NEW): Qualitative failure analysis categorizes how error injection changes model behavior — noise injection (incoherent plans) vs wrong-learning (systematic biases).\n\n## Core Claims (each backed by experimental evidence)\n\n- **Claim 1**: Error injection (both taxonomy-guided and random) degrades embodied planning performance with large effect size but marginal statistical significance.\n  → Support: **5-seed data**: TaxEI 58.3%±6.5pp and Random 58.3%±8.7pp vs Vanilla 67.3%±4.7pp. Both injection methods show -9.0pp gap. Welch t: Vanilla vs TaxEI p≈0.039 (uncorrected), Vanilla vs Random p≈0.089. Bonferroni corrected (3 comparisons, α=0.017): all NS. Cohen's d: 1.58 (TaxEI) and 1.28 (Random) — large effects. Underpowered at n=5; the ~9pp degradation may be a real effect requiring larger N to confirm.\n\n- **Claim 2**: Taxonomy labels provide zero benefit over random injection — structured error labeling does not improve training signal.\n  → Support: **TaxEI = Random = 58.3% = 137/235 tasks (5-seed, identical)**. Welch t: t=0.000, p=1.000. This is the paper's strongest finding: the careful design of a 4-operator error taxonomy with per-error-type labels achieves exactly nothing compared to unlabeled random injection. The taxonomy's structured perturbations are indistinguishable from noise at the mean level. Variance differs: TaxEI SD (6.5pp) < Random SD (8.7pp), suggesting taxonomy may mildly stabilize, but both are worse than Vanilla (4.7pp).\n\n- **Claim 3**: Error injection causes **generalization instability** with catastrophic seed vulnerability — training converges stably but evaluation produces unpredictable outcomes including catastrophic failures.\n  → Support: **5-seed complete**: Training loss is extremely stable across seeds (SD=0.0007), yet eval SD: Vanilla 4.7pp < TaxEI 6.5pp < Random 8.7pp. Both injection methods produce exactly one catastrophic outlier (~47%): TaxEI seed0=46.8%, Random seed1=46.8%. Vanilla never drops below 61.7%. **Memorization-generalization dissociation** (D029/D033): Forward pass v2 (trajectory-level) confirms injected samples have lower loss than clean (all conditions), but eval is worse. Random memorizes 2.1× deeper than TaxEI (gap -0.078 vs -0.037) yet achieves identical eval — deeper memorization does not linearly predict eval harm. Dose-response loss gaps are non-monotonic (25% > 50%), not the monotonic pattern in v1 (which had a classification bug). D026 behavioral evidence (partial update: 3-seed V/T, 1-seed R, NOT balanced — full 5-seed trajectory collection pending): TaxEI produces ~2.2× more loop_repetition failures than Vanilla. Ratio stable across data subsets but absolute rates pending balanced data. **Observed pattern** (correlation, not established causation): memorization of error patterns + loop fixation at eval time + generalization collapse. Per-operator loss ranking is unstable across conditions, precluding strong per-operator causal claims. 1-in-5 catastrophic seed risk is absent from clean training.\n\n- **Claim 4**: Injection-trained models do not improve error recovery — observed \"recovery\" is passive resilience (ignoring errors), not active recovery.\n  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp). **D041 key insight**: Recovery eval rates match normal eval rates across all conditions (Vanilla 61.7%=61.7%, TaxEI 59.6%≈61.7%, Random 63.8%≈66.0%). Models succeed at the same rate whether or not errors are injected at eval time — they passively ignore perturbations rather than actively detecting and recovering from them. This reframes \"no recovery improvement\" as \"no recovery mechanism at all\": the models are **resilient** (robust to noise) rather than **recovery-capable** (able to detect and correct errors). The distinction matters because resilience is a byproduct of task completion ability, while recovery requires explicit error awareness that none of the training regimes instill.\n\n- **Claim 5**: Detection training via error injection is completely ineffective — models show zero error awareness.\n  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random). Combined with D041's recovery≈resilience finding: models neither detect errors explicitly (0% detection) nor respond to them implicitly (recovery rate = normal eval rate). Error injection during training fails to create any form of error awareness in the embodied planning domain.\n\n- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.\n  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.\n\n- **Claim 7** (long paper NEW): Recovery-paired injection actively harms performance, definitively ruling out recovery pairing as PALADIN's missing ingredient.\n  → Support: **TaxEI-RP 4-seed mean 47.9% ± 7.8pp** (s42=38.3%, s0=46.8%, s1=48.9%, s123=57.4%) vs TaxEI 58.3% vs Vanilla 67.3%. Recovery-paired training (14,437 samples = TaxEI 9,029 + recovery continuations 5,408) performs **10pp worse than unpaired TaxEI** and **19pp worse than Vanilla**. Adding recovery demonstrations does not teach active recovery — it adds noise that further corrupts the action distribution. Detection rate remains 0%. This definitively answers the PALADIN recovery-pairing confound: the failure is not due to missing recovery pairs, but to fundamental task-structural incompatibility. (D043)\n\n- **Claim 8** ~~(long paper NEW)~~: **CANCELLED (D040)**. WebShop replication infeasible — P1_StepOrderSwap incompatible with linear action space (search+click), taxonomy 4→3 makes cross-environment comparison inequivalent. Downgraded to Discussion section analysis of ALFWorld vs WebShop structural differences and why cross-environment replication is non-trivial.\n\n- **Claim 9** (long paper NEW): Structured error injection (TaxEI) causes **cross-model training instability**, while random injection remains stable — the harm is a property of structured error patterns, not model-specific.\n  → Support: **LLaMA-3.1-8B-Instruct 3-seed replication**. TaxEI recovery mean 69.5%±8.6pp vs Random 76.6%±2.1pp vs Vanilla 73.1%±2.5pp. TaxEI variance 4× higher than Random (SD 8.6 vs 2.1). 1/3 seeds (s123) shows catastrophic TaxEI collapse: recovery 59.6% (vs vanilla 70.2%, Δ=-10.6pp; vs random 78.7%, Δ=-19.1pp). Other 2 seeds show TaxEI=Vanilla=74.5%. Random is consistently stable or mildly beneficial across all seeds. **Cross-model pattern**: Qwen shows consistent TaxEI harm (mean -9pp, moderate variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, extreme variance with 1/3 catastrophic). Direction (TaxEI ≤ Random for stability) holds across both models. This upgrades the finding from \"Qwen-specific negative result\" to \"structured injection is fundamentally destabilizing for embodied planning.\"\n\n## Anticipated Reviewer Concerns\n\n1. **\"Statistical power is limited.\"**\n   → All three conditions now have **5 seeds**. Welch t: Vanilla vs TaxEI p=0.039 (uncorrected), Bonferroni NS (α=0.017). Cohen's d=1.58 (large). Power at n=5: 45.2%; need n=9 for 80%. We do not claim significance after correction but emphasize the large effect size (-9.0pp) and report all individual seed results. Bootstrap 95% CI: [+3.4, +15.8]pp. Bayes Factor 0.68 (inconclusive). The variance gradient (Vanilla 4.7 < TaxEI 6.5 < Random 8.7) is consistent across seeds.\n\n2. **\"ALFWorld has only 47 test tasks — too small for reliable conclusions.\"**\n   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. With 5 seeds × 47 tasks = 235 episodes per condition, our pooled sample gives adequate power for the observed ~9pp effect (d≈1.4). WebShop replication was planned but cancelled (D040: P1 incompatible with linear action space); the structural incompatibility itself supports our task-structure boundary condition argument.\n\n3. **\"Maybe the taxonomy itself is poorly designed.\"**\n   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.\n\n4. **\"The training recipe might be suboptimal for injection data.\"**\n   → The same recipe produces strong Vanilla results (67.3% ± 4.7pp vs 42.6% zero-shot baseline, +24.7pp, 5 seeds), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.\n\n5. **\"50% injection ratio is too high — you're drowning the signal.\"**\n   → Comprehensively addressed with complete 5-seed fixed-size dose-response ablation at 10%/25%/50%/Full (all 4,358 total samples, all 5 doses × 5 seeds). No safe threshold exists: even 10% injection degrades performance (TaxEI -6.0pp). The harm profile is non-monotonic: monotonic degradation 0%→10%→25% (TaxEI nadir 52.7%), partial rebound 25%→50%→Full driven by training lottery. Taxonomy penalty follows inverted-U curve peaking at 25% (-7.3pp TaxEI-Random gap). The pattern holds for both TaxEI and Random, suggesting it is a general property of error injection.\n\n6. **\"Why is detection rate 0%? Evaluation might be flawed.\"**\n   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.\n\n7. **\"Why not compare directly on ToolBench?\"**\n   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.\n\n8. **\"PALADIN uses error+recovery pairs; TaxEI uses standalone errors. Isn't recovery-pairing the real difference?\"** [Dream M+W]\n   → **Directly tested and refuted** (D043). TaxEI-RP (recovery-paired, 14,437 samples) achieves 47.9% ± 7.8pp — **10pp worse** than unpaired TaxEI (58.3%) and **19pp worse** than Vanilla (67.3%). Recovery pairing not only fails to help, it actively harms. This is the paper's strongest evidence for the task-structure hypothesis: even mimicking PALADIN's recovery-pairing design cannot overcome the fundamental incompatibility of error injection with embodied planning.\n\n9. **\"Power analysis says n=9 needed but you only ran n=5.\"** [Dream W]\n   → We acknowledge n=5 is underpowered (45.2%) for the observed effect at α=0.017 (Bonferroni). We report this transparently with power curves. The large effect size (d=1.58), consistent direction across all 5 seeds, and dose-response replication across 25 independent training runs provide converging evidence despite per-comparison underpowerment.\n\n10. **\"Data volume confound: Vanilla has half the training data.\"** [Dream W]\n    → Vanilla uses 4,358 samples; TaxEI/Random use 9,029. We address this via dose-response ablation at fixed 4,358 total samples. At 10% injection, TaxEI still degrades (-6.0pp, 5-seed), confirming harm is from injection content, not volume. The full-scale comparison's volume asymmetry is acknowledged as a limitation.\n\n11. **\"Only tested on one model — maybe it's a Qwen-specific issue.\"**\n    → Addressed with LLaMA-3.1-8B-Instruct 3-seed replication. TaxEI instability reproduces cross-model (LLaMA SD=8.6pp, 1/3 catastrophic seed). Random injection is stable on both models. The direction (TaxEI harmful/unstable, Random neutral/stable) is consistent across architectures; only severity differs (Qwen: consistent harm; LLaMA: intermittent but catastrophic when triggered). This rules out model-specific explanations and points to structured error patterns as the causal factor.\n\n## Key Differentiators vs PALADIN\n\nPALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:\n\n1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., \"go to countertop 2\" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.\n\n2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.\n\n3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making \"what to do after an error\" fundamentally harder to learn from examples.\n\n4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.\n\n**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.\n\n## Note on v3→v4 Vanilla Discrepancy\nv3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.\n\n## Dream Review Findings (dream_20260515T020837)\n\n**Scores**: Best 2/5 (artifact: dream fabricated experiments), Median 3/5 (Borderline Accept), Worst 2.5/5 (Borderline Revise)\n\n**Confirmed action items (cross-tier consistent)**:\n1. Related work must expand to 15-20 refs. Add: Reflexion (Shinn 2023), McCoy et al. (2020) seed-dependent generalization, Mosbach et al. (2021) fine-tuning stability, Madry et al. (2018) adversarial training, Bengio et al. (2009) curriculum learning, D'Amour et al. (2022) underspecification, ReAct (Yao 2023).\n2. PALADIN recovery-pairing confound must be discussed prominently: PALADIN pairs errors WITH recovery demonstrations; TaxEI injects standalone errors without recovery. This is the most parsimonious alternative explanation.\n3. Formal variance test: F-test p=0.252 (NS) is our strongest stat. Also compute Levene's test for robustness.\n4. Paper structure for 4-page limit: Intro → Method → Main Results (Table 1 + dose-response) → Qualitative/Error Echo → Per-Operator Gradient → Discussion → Conclusion. Move training dynamics, recovery prompting to appendix.\n\n**Observation items (monitor in real reviews)**:\n- Core novelty concern: \"seed variance unreliable\" is known — our per-operator gradient and error echo differentiate us\n- Self-undermining: we use 3 seeds but findings suggest ≥5 needed — prominent limitation, consider power analysis\n- Data volume confound: Vanilla 4,358 vs TaxEI/Random 9,029 — acknowledge in limitations (dose-response at 10% controls for this partially)\n- EEF 2×2 framework: {positive, negative signal} × {tool-use, planning} could sharpen Discussion\n\n## Supplementary Experiments — Long Paper (8-page)\n\n### Done (from short paper phase)\n- ~~**3-seed main conditions**~~: ✅ Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.\n- ~~**Dose-response 3-seed (25%/50%)**~~: ✅ Dual regime confirmed. 10% = seed=42 only.\n- ~~**Recovery eval (seed=42)**~~: ✅ TaxEI 59.6%, Vanilla 61.7%, Random 63.8%. Detection 0%.\n\n### Priority 1 (required for 8-page long paper)\n- ~~**5-seed extension** [Claims 1,3]~~: ✅ Done. Vanilla 67.3±4.7, TaxEI=Random=58.3%. D032.\n- ~~**Training dynamics** [Claim 3]~~: ✅ Done. Forward pass v2 (trajectory-level). D027/D029/D033.\n- ~~**Qualitative failure analysis** [Claims 1,6]~~: ✅ Done. TaxEI loop_repetition 2.2×. D026.\n- ~~**Extended statistics** [Claims 1,3]~~: ✅ Done. Bootstrap CI, power, Bayesian. D030-D032.\n- ~~**Dose-response 5-seed** [Claim 3]~~: ✅ Done. All 5 doses × 5 seeds complete. 10% (D034), 25% (D035/D036), 50% (D038). Inverted-U taxonomy penalty curve. ~24 GPU-h.\n- **Recovery-paired injection** [Claim 7]: 🔄 Training in progress (4 seeds × 4 GPU). Datagen complete (711/760), 14,437 samples. ~16 GPU-h.\n- ~~**WebShop replication** [Claim 8]~~: ❌ CANCELLED (D040). P1 incompatible with linear action space. Downgraded to Discussion.\n- **Recovery eval multi-seed** [Claims 4,5]: 7/15 complete. Remaining 8/15 after TaxEI-RP. ~15 GPU-h.\n\n### Priority 1.5 (cross-model validation)\n- ~~**LLaMA-3.1-8B cross-model replication** [Claim 9]~~: ✅ Done. 3 seeds × 3 conditions, all training + eval complete. TaxEI instability confirmed cross-model (SD=8.6%, 1/3 catastrophic). Random stable (SD=2.1%). ~36 GPU-h.\n\n### Priority 2 (strengthens further)\n- **Scale ablation** [Claim 6]: 25K-50K trajectories. ~$30-50 API + ~20 GPU-h.\n\n### Estimated total: ~120 GPU-hours (~30h wall clock with 4 × 5090)\n\n\n## registry (completed experiments)\n\n- exp_id: traj_collect_500\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    successful_trajectories: 501\n    failed_trajectories: 213\n    total_attempts: 714\n    success_rate: 0.702\n    api_cost_usd: 8.86\n    collection_time_sec: 5245\n- exp_id: sft-dryrun-73\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss_init: 2.436\n    train_loss_final: 1.543\n    train_loss_avg: 1.894\n    peak_memory_gib: 19.22\n    steps: 8\n    duration_sec: 42\n    data_vanilla: 124\n    data_injected_dryrun: 96\n    injected_failed: 4\n- exp_id: vanilla-react-baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_success_rate: 0.426\n    total_tasks: 47\n    successes: 20\n    per_task_type:\n      pick_heat_then_place:\n        success: 5\n        total: 8\n        rate: 0.625\n      look_at_obj_in_light:\n        success: 3\n        total: 6\n        rate: 0.5\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_two_obj_and_place:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_cool_then_place:\n        success: 0\n        total: 7\n        rate: 0\n- exp_id: mini-pipeline-e2e\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: mini-taxei-sft\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.447\n    eval_successes: 21\n    eval_total: 47\n    vs_baseline_pp: 2.1\n    per_task:\n      look_at_obj_in_light: 3/6 (50.0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 1/7 (14.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_two_obj_and_place: 3/7 (42.9%)\n    train_steps: 195\n    train_duration_min: 16.3\n- exp_id: mini-vanilla-sft\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.149\n    eval_successes: 7\n    eval_total: 47\n    vs_baseline_pp: -27.7\n    per_task:\n      look_at_obj_in_light: 0/6 (0%)\n      pick_and_place_simple: 2/8 (25.0%)\n      pick_clean_then_place: 2/11 (18.2%)\n      pick_cool_then_place: 0/7 (0%)\n      pick_heat_then_place: 3/8 (37.5%)\n      pick_two_obj_and_place: 0/7 (0%)\n    train_steps: 54\n    train_duration_min: 5\n- exp_id: vanilla_sft_aligned_v1\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: vanilla_sft_aligned_v2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: mini-vanilla-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 4176\n    train_steps_total: 1566\n    est_duration_min: 58\n    format: aligned_single_turn\n- exp_id: mini-taxei-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 7545\n    train_samples_clean: 4176\n    train_samples_injected: 3369\n    train_steps_total: 2832\n    est_duration_min: 90\n    format: aligned_single_turn\n- exp_id: mini-random-sft-v3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_samples: 9076\n    train_samples_clean: 4176\n    train_samples_injected: 4900\n    train_steps_total: 3405\n    est_duration_min: 110\n    format: aligned_single_turn\n- exp_id: mini-vanilla-sft-v4\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v3-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.745\n    successes: 35\n    total: 47\n    vs_baseline_pp: 31.9\n    vs_baseline: 42.6% → 74.5%\n- exp_id: v3-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_baseline_pp: 23.4\n    vs_vanilla_sft_pp: -8.5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_clean_then_place: 8/11 (72.7%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_cool_then_place: 3/7 (42.9%)\n- exp_id: v3-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_baseline_pp: 8.5\n    vs_vanilla_sft_pp: -23.4\n- exp_id: v4-taxei-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-random-sft\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-random-sft-r2\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-taxei-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-random-sft-r3\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-vanilla-eval\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r2\n  name: ''\n  status: PREPARING\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-vanilla-eval-r3\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_heat_then_place: 6/8 (75.0%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n      pick_clean_then_place: 5/11 (45.5%)\n- exp_id: v4-taxei-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    vs_vanilla_pp: 0\n    vs_random_pp: -4.3\n    mcnemar_vs_vanilla_p: 1\n    mcnemar_vs_random_p: 0.754\n    gate_3a: FAIL\n    gate_3b: FAIL\n    gate_4: PASS\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 3/7 (42.9%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 2/7 (28.6%)\n- exp_id: v4-random-eval\n  name: ''\n  status: PREPARING\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_vanilla_pp: 4.3\n    vs_taxei_pp: 4.3\n    mcnemar_vs_vanilla_p: 0.754\n    per_task:\n      look_at_obj_in_light: 6/6 (100%)\n      pick_and_place_simple: 4/8 (50%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 4/7 (57.1%)\n- exp_id: v4-vanilla-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.297\n    avg_loss: 0.416\n    token_accuracy: 0.902\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.917\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-random-seed0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.355\n    token_accuracy: 0.912\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 110\n- exp_id: v4-recovery-eval-dev\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    pipeline_files:\n    - eval/injected_eval.py\n    - scripts/run_injected_eval.sh\n    injected_eval_lines: 463\n    dryrun_result: PASS\n    dryrun_detail: vanilla checkpoint, 1 task, cuda:3, injected error recovered in\n      13 steps\n- exp_id: v4-vanilla-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.288\n    token_accuracy: 0.903\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58.9\n- exp_id: v4-vanilla-seed7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.295\n    avg_loss: 0.415\n    token_accuracy: 0.898\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 59.4\n    checkpoint_path: checkpoints/mini_vanilla_sft_v4_seed7/v0-20260515-214031/checkpoint-1635\n- exp_id: v4-recovery-dryrun\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-vanilla-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    vs_seed42_pp: 6.4\n    mcnemar_vs_seed42_p: 0.375\n    discordant_pairs: 5\n    per_task:\n      look_at_obj_in_light: 5/6 (83.3%)\n      pick_and_place_simple: 5/8 (62.5%)\n      pick_clean_then_place: 6/11 (54.5%)\n      pick_cool_then_place: 4/7 (57.1%)\n      pick_heat_then_place: 7/8 (87.5%)\n      pick_two_obj_and_place: 5/7 (71.4%)\n- exp_id: v4-taxei-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.468\n    eval_successes: 22\n    eval_total: 47\n    vs_seed42_pp: -14.9\n- exp_id: v4-random-seed0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_seed42_pp: -10.7\n- exp_id: v4-vanilla-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_seed42_pp: 4.3\n    vs_seed0_pp: -2.1\n    per_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 7\n        total: 8\n        rate: 0.875\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-vanilla-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    successes: 29\n    total: 47\n    recovery_rate: 0.617\n    detection_rate: 0\n    per_operator:\n      C1_context_truncation:\n        recovered: 9\n        total: 12\n        rate: 0.75\n      C4_observation_masking:\n        recovered: 6\n        total: 11\n        rate: 0.545\n      P1_step_order_swap:\n        recovered: 7\n        total: 12\n        rate: 0.583\n      P2_sub_goal_deletion:\n        recovered: 7\n        total: 12\n        rate: 0.583\n- exp_id: v4-taxei-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    success_rate: 0.596\n    successes: 28\n    total: 47\n    recovery_rate: 0.596\n    detection_rate: 0\n- exp_id: v4-random-recovery-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.638\n    detection_rate: 0\n    successes: 30\n    total: 47\n    source: json-file-verified\n    note: r1=29/47, r2=30/47, ±2pp run-to-run variance on P1 non-determinism\n- exp_id: v4-taxei-recovery-eval-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.596\n    detection_rate: 0\n    total_episodes: 47\n    per_operator:\n      C1_context_truncation:\n        recovered: 8\n        total: 12\n        rate: 0.667\n      C4_observation_masking:\n        recovered: 7\n        total: 11\n        rate: 0.636\n      P1_step_order_swap:\n        recovered: 7\n        total: 12\n        rate: 0.583\n      P2_sub_goal_deletion:\n        recovered: 6\n        total: 12\n        rate: 0.5\n- exp_id: v4-taxei-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.35506879\n    token_accuracy: 0.89978214\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 109.2\n    train_runtime_sec: 6549.432\n    train_speed_s_per_it: 1.934\n    memory_gib: 18.49\n- exp_id: v4-random-seed123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.35484016\n    final_loss: 0.16766574\n    token_accuracy: 0.94187103\n    avg_token_accuracy: 0.90849673\n    train_steps: 3387\n    train_epochs: 3\n    train_runtime_sec: 6609.3556\n    train_duration_min: 110.2\n    train_samples_per_second: 4.098\n    train_steps_per_second: 0.512\n    train_speed_s_per_it: 1.951\n    memory_gib: 18.49\n- exp_id: v4-fixed-inject10\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-fixed-inject25\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.308\n    token_accuracy: 0.888\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject25-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.285\n    token_accuracy: 0.893\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58\n- exp_id: v4-taxei-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        success: 7\n        total: 11\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        success: 3\n        total: 7\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.617\n    eval_successes: 29\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 6\n        total: 8\n        rate: 0.75\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.489\n    eval_successes: 23\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        success: 4\n        total: 6\n        rate: 0.667\n      pick_and_place_simple:\n        success: 3\n        total: 8\n        rate: 0.375\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 2\n        total: 7\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-random-seed123-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 7\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-taxei-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.259\n    token_accuracy: 0.911\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 53.1\n- exp_id: v4-random-fixed-inject10\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4226\n    final_step_loss: 0.3079\n    token_accuracy: 0.9\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 57\n- exp_id: v4-random-fixed-inject25\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-random-fixed-inject50\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n    train_loss: 0.4338\n    final_step_loss: 0.2618\n    token_accuracy: 0.91\n    train_duration_min: 53.1\n    memory_gib: 18\n    train_speed_s_per_it: 1.95\n- exp_id: v4-taxei-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    eval_success_rate: 0.511\n    eval_successes: 24\n    eval_total: 47\n    vs_vanilla_seed42_pp: -10.6\n- exp_id: v4-random-fixed-inject10-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.681\n    eval_successes: 32\n    eval_total: 47\n    by_task:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-random-fixed-inject50-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.574\n    eval_successes: 27\n    eval_total: 47\n    vs_vanilla_seed42_pp: -4.3\n    vs_taxei_50_pp: 6.3\n- exp_id: v4-random-fixed-inject25-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.553\n    eval_successes: 26\n    eval_total: 47\n    vs_vanilla_seed42_pp: -6.4\n    vs_taxei_25_pp: 6.4\n- exp_id: v4-taxei-fixed-inject25-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4258\n    train_duration_min: 56.1\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-taxei-fixed-inject25-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4253\n    train_duration_min: 55.9\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-taxei-fixed-inject50-s0\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_loss: 0.4342\n    train_duration_min: 52.4\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-taxei-fixed-inject50-s123\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    train_loss: 0.4348\n    train_duration_min: 52.9\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-random-fixed-inject25-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: v4-random-fixed-inject25-s123\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-random-fixed-inject50-s0\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-random-fixed-inject50-s123\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject25-s0-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.468\n    successes: 22\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 4\n        rate: 0.667\n      pick_and_place_simple:\n        total: 8\n        success: 2\n        rate: 0.25\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 5\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 2\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 3\n        rate: 0.429\n- exp_id: v4-taxei-fixed-inject25-s123-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.468\n    successes: 22\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 4\n        rate: 0.667\n      pick_and_place_simple:\n        total: 8\n        success: 3\n        rate: 0.375\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 5\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 1\n        rate: 0.143\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 3\n        rate: 0.429\n- exp_id: v4-taxei-fixed-inject50-s0-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.702\n    eval_successes: 33\n    eval_total: 47\n- exp_id: v4-taxei-fixed-inject50-s123-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.468\n    eval_successes: 22\n    eval_total: 47\n- exp_id: v4-random-fixed-inject25-s0-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    total: 47\n    successes: 29\n    by_task:\n      look_at_obj_in_light: 0.667\n      pick_and_place_simple: 0.625\n      pick_clean_then_place_in_recep: 0.455\n      pick_cool_then_place_in_recep: 0.571\n      pick_heat_then_place_in_recep: 0.75\n      pick_two_obj_and_place: 0.714\n- exp_id: v4-random-fixed-inject25-s123-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.511\n    total: 47\n    successes: 24\n    by_task:\n      look_at_obj_in_light: 0.667\n      pick_and_place_simple: 0.375\n      pick_clean_then_place_in_recep: 0.545\n      pick_cool_then_place_in_recep: 0.143\n      pick_heat_then_place_in_recep: 0.75\n      pick_two_obj_and_place: 0.571\n- exp_id: v4-random-fixed-inject50-s0-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.468\n    successes: 22\n    total: 47\n- exp_id: v4-random-fixed-inject50-s123-eval\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    success_rate: 0.702\n    successes: 33\n    total: 47\n- exp_id: v4-vanilla-recovery-eval-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.681\n    successes: 32\n    total: 47\n    detection_rate: 0\n- exp_id: v4-vanilla-recovery-eval-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.66\n    successes: 31\n    total: 47\n    detection_rate: 0\n- exp_id: v4-taxei-recovery-eval-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.468\n    successes: 22\n    total: 47\n    detection_rate: 0\n- exp_id: v4-taxei-recovery-eval-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.617\n    successes: 29\n    total: 47\n    detection_rate: 0\n- exp_id: v4-random-recovery-eval-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.553\n    detection_rate: 0\n    success_rate: 0.553\n    total_episodes: 47\n    by_operator:\n      C1_context_truncation:\n        total: 12\n        recovered: 7\n        recovery_rate: 0.583\n      C4_observation_masking:\n        total: 11\n        recovered: 6\n        recovery_rate: 0.545\n      P1_step_order_swap:\n        total: 12\n        recovered: 7\n        recovery_rate: 0.583\n      P2_sub_goal_deletion:\n        total: 12\n        recovered: 6\n        recovery_rate: 0.5\n- exp_id: v4-random-recovery-eval-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.66\n    detection_rate: 0\n    total_episodes: 47\n    by_operator:\n      C1_context_truncation:\n        recovery_rate: 0.75\n        recovered: 9\n        total: 12\n      P2_sub_goal_deletion:\n        recovery_rate: 0.75\n        recovered: 9\n        total: 12\n      P1_step_order_swap:\n        recovery_rate: 0.583\n        recovered: 7\n        total: 12\n      C4_observation_masking:\n        recovery_rate: 0.545\n        recovered: 6\n        total: 11\n- exp_id: v4-vanilla-seed1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.292\n    avg_loss: 0.416\n    token_accuracy: 0.903\n    train_steps: 1635\n    train_epochs: 3\n    train_duration_min: 58.8\n    memory_gib: 17.63\n    checkpoint_path: checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635\n- exp_id: v4-taxei-seed1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.1667\n    avg_loss: 0.3561\n    token_accuracy: 0.915\n    final_token_acc: 0.942\n    train_steps: 3387\n    train_epochs: 3\n    train_duration_min: 108.9\n    memory_gib: 18.49\n    checkpoint_path: checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387\n- exp_id: v4-taxei-seed7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    current_step: 3387\n    total_steps: 3387\n    progress_pct: 100\n    train_loss: 0.3568\n    final_step_loss: 0.1753\n    token_acc: 0.9009\n    final_token_acc: 0.9328\n    train_runtime_s: 6591.9\n    epochs: 3\n    peak_memory_gib: 18.49\n    gpu: cuda:3\n    pid: 155145\n- exp_id: v4-training-dynamics-forward\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    vanilla_full:\n      clean_loss: 0.6853\n      clean_n: 4358\n    taxei_full:\n      clean_loss: 0.7712\n      injected_loss: 0.6139\n      clean_n: 8269\n      injected_n: 760\n      per_operator:\n        P1_StepOrderSwap: 0.6165\n        P2_SubGoalDeletion: 0.6161\n        C1_ContextTruncation: 0.5932\n        C4_ObservationMasking: 0.6298\n    random_full:\n      clean_loss: 0.7354\n      injected_loss: 0.5902\n      clean_n: 8269\n      injected_n: 760\n    dose_response:\n      taxei_10pct:\n        clean_loss: 0.6628\n        injected_loss: 0.6464\n        gap: -0.0164\n        injected_n: 70\n      taxei_25pct:\n        clean_loss: 0.701\n        injected_loss: 0.574\n        gap: -0.127\n        injected_n: 168\n      taxei_50pct:\n        clean_loss: 0.8516\n        injected_loss: 0.6547\n        gap: -0.1969\n        injected_n: 370\n    key_findings: 'Clear dose-response: injected-clean gap widens from -0.016 (10%)\n      to -0.127 (25%) to -0.197 (50%). TaxEI operators C1_ContextTruncation consistently\n      lowest loss. Higher injection rates also degrade clean sample loss (0.663→0.701→0.852).'\n- exp_id: v4-recovery-paired-datagen\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_injected_variants: 760\n    successfully_processed: 711\n    skipped_no_source_match: 49\n    operators:\n      C1_ContextTruncation: 182\n      C4_ObservationMasking: 175\n      P1_StepOrderSwap: 170\n      P2_SubGoalDeletion: 184\n    recovery_steps_mean: 7.6\n    recovery_steps_min: 1\n    recovery_steps_max: 46\n    total_recovery_api_calls: 5408\n    output_file: /root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/recovery_paired.jsonl\n    output_lines: 711\n    output_size_mb: 20.8\n    log_file: /root/autodl-tmp/tax_error_inject_agent/logs/recovery_paired_gen.log\n- exp_id: v4-vanilla-seed7-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.745\n    eval_successes: 35\n    eval_total: 47\n    vs_seed42_pp: 12.8\n- exp_id: v4-vanilla-seed1-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    eval_success_rate: 0.66\n    eval_successes: 31\n    eval_total: 47\n    vs_seed42_pp: 4.3\n- exp_id: v4-random-seed1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.167\n    final_token_acc: 0.938\n    initial_loss: 4.017\n    total_steps: 3387\n    epochs: 3\n    total_flos: 697000000000000000\n- exp_id: v4-random-seed7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.173\n    final_token_acc: 0.935\n    initial_loss: 4.017\n    total_steps: 3387\n    epochs: 3\n    total_flos: 697192362530058200\n    train_runtime_sec: 6672\n    memory_gib: 18.49\n- exp_id: v4-taxei-seed1-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.596\n    successes: 28\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 4\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 5\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 2\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-taxei-seed7-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    successes: 29\n    total: 47\n    by_task:\n      look_at_obj_in_light: 4/6 (0.667)\n      pick_and_place_simple: 5/8 (0.625)\n      pick_clean_then_place_in_recep: 5/11 (0.455)\n      pick_cool_then_place_in_recep: 4/7 (0.571)\n      pick_heat_then_place_in_recep: 7/8 (0.875)\n      pick_two_obj_and_place: 4/7 (0.571)\n- exp_id: qualitative-failure-analysis\n  name: ''\n  status: PREPARING\n  conclusion: success\n  metrics:\n    data_source: eval_results/failure_analysis.json\n    taxei_loop_repetition_rate: 0.174\n    vanilla_loop_repetition_rate: 0.078\n    random_loop_repetition_rate: 0.032\n    taxei_loop_count: 49\n    vanilla_loop_count: 22\n    random_loop_count: 6\n    per_operator:\n      P1: 15\n      P2: 14\n      C1: 11\n      C4: 9\n    note: Random data only from seed=42 recovery eval + 3-seed clean eval (188 episodes\n      vs 282). Rates to be updated after 5-seed completion.\n- exp_id: v4-taxei-fixed-inject10-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4238\n    final_loss: 0.3102\n    final_token_acc: 0.8822\n    epochs: 3\n    total_steps: 1635\n    train_runtime_sec: 3494\n    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635\n- exp_id: v4-training-dynamics-forward-v2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    subsets_computed:\n    - vanilla_full\n    - taxei_full\n    - random_full\n    - taxei_inject10\n    - taxei_inject25\n    - taxei_inject50\n    taxei_inject50_injected_mean_loss: 0.8185\n    taxei_inject50_clean_mean_loss: 0.8514\n    per_operator:\n      C1_ContextTruncation:\n        mean: 0.6489\n        n: 101\n      C4_ObservationMasking:\n        mean: 0.6782\n        n: 92\n      P1_StepOrderSwap:\n        mean: 0.6374\n        n: 89\n      P2_SubGoalDeletion:\n        mean: 0.6542\n        n: 88\n    plots:\n    - subset_comparison\n    - operator_breakdown\n    - dose_response\n    output_dir: /root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics_v2/\n- exp_id: v4-random-seed1-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.468\n    successes: 22\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 2\n        total: 8\n        rate: 0.25\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 2\n        total: 7\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        success: 5\n        total: 8\n        rate: 0.625\n      pick_two_obj_and_place:\n        success: 3\n        total: 7\n        rate: 0.429\n- exp_id: v4-random-seed7-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.553\n    successes: 26\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 4\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 3\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_two_obj_and_place:\n        total: 7\n        success: 3\n        rate: 0.429\n- exp_id: v4-taxei-inject10-seed0\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-taxei-inject10-seed123\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-random-inject10-seed0\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject10-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4234\n    final_loss: 0.3097\n    final_token_acc: 0.8882\n    epochs: 3\n    total_steps: 1635\n    train_runtime_sec: 3497\n    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635\n- exp_id: v4-random-fixed-inject10-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4227\n    final_loss: 0.276\n    final_token_acc: 0.9067\n    epochs: 3\n    total_steps: 1635\n    train_runtime_sec: 3531\n    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635\n- exp_id: v4-taxei-fixed-inject10-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.3013\n    train_loss_avg: 0.4225\n    final_token_acc: 0.8947\n    total_steps: 1635\n    epochs: 3\n    train_runtime_sec: 3469\n    memory_gib: 18.13\n    train_speed_s_per_it: 2.121\n- exp_id: v4-random-fixed-inject10-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.3124\n    train_loss_avg: 0.4236\n    final_token_acc: 0.8867\n    total_steps: 1635\n    epochs: 3\n    train_runtime_sec: 3535.7\n    train_samples_per_second: 3.698\n    train_steps_per_second: 0.462\n    memory_gib: 18.95\n- exp_id: v4-taxei-fixed-inject10-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.237\n    train_loss_avg: 0.4212\n    final_token_acc: 0.905\n    total_steps: 1635\n    epochs: 3\n    train_runtime_sec: 3437\n    memory_gib: 18.15\n    train_speed_s_per_it: 2.102\n- exp_id: v4-random-fixed-inject10-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.3096\n    train_loss_avg: 0.4238\n    final_token_acc: 0.8902\n    total_steps: 1635\n    epochs: 3\n    train_runtime_sec: 3488\n    memory_gib: 18.13\n    train_speed_s_per_it: 2.132\n- exp_id: v4-random-fixed-inject10-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_loss: 0.2352\n    train_loss_avg: 0.4209\n    final_token_acc: 0.9066\n    total_steps: 1635\n    epochs: 3\n    train_runtime_sec: 3511.93\n    memory_gib: 18.15\n    train_speed_s_per_it: 2.148\n- exp_id: v4-taxei-fixed-inject10-s123-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: CUDA OOM during model loading on GPU 0\n- exp_id: v4-random-fixed-inject10-s0-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: CUDA OOM during model loading on GPU 0\n- exp_id: v4-taxei-fixed-inject10-s1-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics:\n    error: CUDA OOM during model loading on GPU 0\n- exp_id: v4-taxei-fixed-inject10-s0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.702\n    successes: 33\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 8\n        rate: 0.727\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 4\n        rate: 0.571\n- exp_id: v4-random-fixed-inject10-s123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.553\n    successes: 26\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 5\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 2\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 3\n        rate: 0.429\n- exp_id: v4-taxei-fixed-inject10-s123-eval-r2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-random-fixed-inject10-s0-eval-r2\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject10-s123-eval-r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.553\n    successes: 26\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 4\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 5\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 2\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 4\n        rate: 0.571\n- exp_id: v4-random-fixed-inject10-s0-eval-r3\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.66\n    successes: 31\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        success: 7\n        total: 11\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 7\n        total: 8\n        rate: 0.875\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject10-s1-eval-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.511\n    successes: 24\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 4\n        rate: 0.667\n      pick_and_place_simple:\n        total: 8\n        success: 4\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 5\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 2\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 3\n        rate: 0.429\n- exp_id: v4-taxei-fixed-inject10-s7-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.681\n    successes: 32\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 7\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 4\n        rate: 0.571\n- exp_id: v4-random-fixed-inject10-s1-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.681\n    successes: 32\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 10\n        success: 5\n        rate: 0.5\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 6\n        rate: 0.857\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 4\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject25-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4243\n    train_duration_min: 57.5\n    train_steps: 1635\n    train_epochs: 3\n    data_count: 4358\n- exp_id: v4-random-fixed-inject25-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4261\n    final_step_loss: 0.2442\n    token_accuracy: 0.9123\n    train_steps: 1635\n    train_epochs: 3\n    train_runtime_sec: 3417.56\n    train_duration_min: 56.96\n    train_samples_per_second: 3.826\n    train_steps_per_second: 0.478\n    memory_gib: 18\n    data_count: 4358\n- exp_id: v4-taxei-fixed-inject25-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4242\n    final_step_loss: 0.2571\n    token_accuracy: 0.904\n    train_steps: 1635\n    train_epochs: 3\n    train_runtime_sec: 3430.48\n    train_duration_min: 57.17\n    train_samples_per_second: 3.811\n    train_steps_per_second: 0.477\n    memory_gib: 17.55\n    data_count: 4358\n- exp_id: v4-random-fixed-inject10-s7-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    successes: 29\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        success: 5\n        total: 6\n        rate: 0.833\n      pick_and_place_simple:\n        success: 4\n        total: 8\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        success: 5\n        total: 11\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        success: 4\n        total: 7\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        success: 7\n        total: 8\n        rate: 0.875\n      pick_two_obj_and_place:\n        success: 4\n        total: 7\n        rate: 0.571\n- exp_id: v4-random-fixed-inject25-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4254\n    final_step_loss: 0.265\n    token_acc: 0.899\n    epochs: 3\n    steps: 1635\n    train_runtime_sec: 3407\n- exp_id: v4-taxei-fixed-inject25-s1-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.638\n    successes: 30\n    total: 47\n    eval_split: valid_unseen\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 4\n        rate: 0.667\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 3\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 6\n        rate: 0.857\n- exp_id: v4-taxei-fixed-inject25-s7-eval\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-random-fixed-inject25-s1-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.723\n    successes: 34\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 7\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 7\n        rate: 0.875\n      pick_two_obj_and_place:\n        total: 7\n        success: 6\n        rate: 0.857\n- exp_id: v4-random-fixed-inject25-s7-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.596\n    successes: 28\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 4\n        rate: 0.667\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 3\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 4\n        rate: 0.571\n- exp_id: v4-taxei-fixed-inject25-s1-eval-r2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject25-s7-eval-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.574\n    successes: 27\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 3\n        rate: 0.375\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 5\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 3\n        rate: 0.429\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-taxei-fixed-inject50-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-random-fixed-inject50-s1\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: v4-taxei-fixed-inject50-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4674\n    token_acc: 0.9189\n    train_runtime_sec: 3834\n    memory_gib: 29.94\n- exp_id: v4-random-fixed-inject50-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4672\n    token_acc: 0.9156\n    train_runtime_sec: 3832\n    memory_gib: 29.94\n- exp_id: v4-taxei-fixed-inject50-s1-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4667\n    token_acc: 0.9072\n    train_runtime_sec: 3858\n    memory_gib: 30.37\n- exp_id: v4-random-fixed-inject50-s1-r2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4664\n    token_acc: 0.9012\n    train_runtime_sec: 3928\n    memory_gib: 30.37\n- exp_id: v4-taxei-fixed-inject50-s1-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.638\n    successes: 30\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 6\n        rate: 1\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 7\n        rate: 0.636\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_two_obj_and_place:\n        total: 7\n        success: 3\n        rate: 0.429\n- exp_id: v4-random-fixed-inject50-s1-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.702\n    successes: 33\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 8\n        rate: 0.727\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 4\n        rate: 0.571\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 5\n        rate: 0.714\n- exp_id: v4-taxei-fixed-inject50-s7-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.553\n    successes: 26\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 5\n        rate: 0.833\n      pick_and_place_simple:\n        total: 8\n        success: 4\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 6\n        rate: 0.545\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 2\n        rate: 0.286\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 6\n        rate: 0.75\n      pick_two_obj_and_place:\n        total: 7\n        success: 3\n        rate: 0.429\n- exp_id: v4-random-fixed-inject50-s7-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.468\n    successes: 22\n    total: 47\n    by_task_type:\n      look_at_obj_in_light:\n        total: 6\n        success: 4\n        rate: 0.667\n      pick_and_place_simple:\n        total: 8\n        success: 4\n        rate: 0.5\n      pick_clean_then_place_in_recep:\n        total: 11\n        success: 5\n        rate: 0.455\n      pick_cool_then_place_in_recep:\n        total: 7\n        success: 1\n        rate: 0.143\n      pick_heat_then_place_in_recep:\n        total: 8\n        success: 5\n        rate: 0.625\n      pick_two_obj_and_place:\n        total: 7\n        success: 3\n        rate: 0.429\n- exp_id: v4-taxei-rp-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.38469276\n    eval_loss: null\n    duration_minutes: 226.67\n    token_acc: 0.92487562\n    train_samples_per_second: 3.185\n    peak_memory_gib: 30.68\n- exp_id: v4-taxei-rp-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.3847\n    token_acc: 0.9065\n    duration_min: 231.07\n    peak_memory_gib: 30.37\n    train_samples_per_second: 3.124\n- exp_id: v4-taxei-rp-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.38524182\n    eval_loss: null\n    duration_minutes: 226.5\n    token_acc: 0.91372913\n    train_samples_per_second: 3.187\n    peak_memory_gib: 30.66\n- exp_id: v4-taxei-rp-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.38530399\n    eval_loss: null\n    duration_minutes: 226.3\n    token_acc: 0.91761223\n    train_samples_per_second: 3.19\n    peak_memory_gib: 30.17\n- exp_id: llama31-taxei-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.3366\n    token_acc: 0.9357\n    train_steps: 3387\n    train_duration_s: 7782\n- exp_id: llama31-random-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.3366\n    token_acc: 0.9364\n    train_steps: 3387\n    train_duration_s: 7622\n- exp_id: v4-taxei-rp-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.3855\n    token_acc: 0.9103\n    duration_minutes: 226.6\n    peak_memory_gib: 30.25\n    train_samples_per_second: 3.185\n- exp_id: eval-rp-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.574\n    detection_rate: 0\n    episodes: 47\n    recovered: 27\n- exp_id: eval-rp-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.489\n    detection_rate: 0\n    episodes: 47\n    recovered: 23\n- exp_id: eval-rp-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.468\n    detection_rate: 0\n    episodes: 47\n    recovered: 22\n- exp_id: llama31-vanilla-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.40025\n    token_acc: 0.9067\n    train_steps: 1635\n    train_duration_s: 4157\n- exp_id: eval-rp-s42\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.383\n    recovery_count: 18/47\n    C1_context_truncation: 0.5\n    C4_observation_masking: 0.273\n    P1_step_order_swap: 0.5\n    P2_sub_goal_deletion: 0.25\n    detection_rate: 0\n- exp_id: llama31-vanilla-s42-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.745\n    recovery_count: 35/47\n    detection_rate: 0.213\n    C1_context_truncation: 0.75\n    C4_observation_masking: 0.727\n    P1_step_order_swap: 0.75\n    P2_sub_goal_deletion: 0.75\n- exp_id: recovery-vanilla-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.66\n    recovery_count: 31/47\n    detection_rate: 0\n    C1_context_truncation: 0.667\n    C4_observation_masking: 0.545\n    P1_step_order_swap: 0.667\n    P2_sub_goal_deletion: 0.75\n- exp_id: recovery-vanilla-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.745\n    recovery_count: 35/47\n    detection_rate: 0\n    C1_context_truncation: 0.75\n    C4_observation_masking: 0.727\n    P1_step_order_swap: 0.75\n    P2_sub_goal_deletion: 0.75\n- exp_id: llama31-taxei-s42-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.745\n    recovery_count: 35/47\n    detection_rate: 0.298\n    C1_context_truncation: 0.833\n    C4_observation_masking: 0.727\n    P1_step_order_swap: 0.583\n    P2_sub_goal_deletion: 0.833\n    C1_detection: 0.167\n    C4_detection: 0.364\n    P1_detection: 0.25\n    P2_detection: 0.417\n- exp_id: llama31-random-s42-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.766\n    recovery_count: 36/47\n    detection_rate: 0.298\n    C1_context_truncation: 0.667\n    C4_observation_masking: 0.727\n    P1_step_order_swap: 0.917\n    P2_sub_goal_deletion: 0.75\n    C1_detection: 0.417\n    C4_detection: 0.364\n    P1_detection: 0.333\n    P2_detection: 0.083\n- exp_id: llama31-vanilla-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.398\n    epoch1_loss: 0.481\n    epoch2_loss: 0.362\n    epoch3_loss: 0.273\n    final_token_acc: 0.909\n    train_runtime_sec: 4158.6\n- exp_id: llama31-taxei-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.32\n    final_token_acc: 0.88\n    train_steps: 3387\n    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387\n- exp_id: llama31-random-s0\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    final_train_loss: 0.3368\n    epoch1_loss: 0.452\n    epoch2_loss: 0.238\n    epoch3_loss: 0.134\n    final_token_acc: 0.9357\n    train_runtime_sec: 7622\n    train_steps: 3387\n    peak_memory_gib: 30.74\n    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387\n- exp_id: recovery-taxei-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.617\n    recovery_count: 29/47\n    detection_rate: 0\n    C1_context_truncation: 0.75\n    C4_observation_masking: 0.636\n    P1_step_order_swap: 0.583\n    P2_sub_goal_deletion: 0.5\n- exp_id: eval-rp-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.596\n    recovery_count: 28/47\n    detection_rate: 0\n- exp_id: llama31-vanilla-s0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.745\n    recovery_count: 35/47\n    detection_rate: 0.277\n    eval_type: injected\n    eval_script: injected_eval.py\n    output_file: eval_results/llama31_vanilla_s0_injected.json\n    C1_context_truncation:\n      recovery: 0.667\n      detection: 0.167\n    C4_observation_masking:\n      recovery: 0.727\n      detection: 0.364\n    P1_step_order_swap:\n      recovery: 0.917\n      detection: 0.333\n    P2_sub_goal_deletion:\n      recovery: 0.667\n      detection: 0.25\n- exp_id: llama31-random-s42-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.766\n    eval_type: clean\n    eval_script: eval/recovery.py\n    total_episodes: 47\n    output_file: eval_results/llama31_random_s42_clean.json\n- exp_id: recovery-taxei-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.574\n    detection_rate: 0\n    total_episodes: 47\n- exp_id: llama31-random-s0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.745\n    detection_rate: 0.255\n    success_rate: 0.745\n    total_episodes: 47\n    by_operator:\n      C1_context_truncation:\n        total: 12\n        recovered: 10\n        detected: 1\n        recovery_rate: 0.833\n        detection_rate: 0.083\n      C4_observation_masking:\n        total: 11\n        recovered: 8\n        detected: 4\n        recovery_rate: 0.727\n        detection_rate: 0.364\n      P1_step_order_swap:\n        total: 12\n        recovered: 8\n        detected: 4\n        recovery_rate: 0.667\n        detection_rate: 0.333\n      P2_sub_goal_deletion:\n        total: 12\n        recovered: 9\n        detected: 3\n        recovery_rate: 0.75\n        detection_rate: 0.25\n- exp_id: llama31-vanilla-s42-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.723\n    eval_type: clean\n    eval_script: eval/recovery.py\n    total_episodes: 47\n    output_file: eval_results/llama31_vanilla_s42_clean.json\n- exp_id: llama31-vanilla-s0-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.723\n    eval_type: clean\n    eval_script: eval/recovery.py\n    total_episodes: 47\n    output_file: eval_results/llama31_vanilla_s0_clean.json\n- exp_id: llama31-taxei-s0-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.745\n    success_rate: 0.745\n    total_episodes: 47\n- exp_id: llama31-vanilla-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    train_loss: 0.4\n    final_loss: 0.254\n    token_acc: 0.894\n    steps: 1635\n    epochs: 3\n    runtime_seconds: 4234\n    memory_gib: 29.85\n- exp_id: llama31-taxei-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: llama31-random-s123\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: llama31-taxei-s0-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.766\n    total_episodes: 47\n- exp_id: llama31-taxei-s42-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.766\n    total_episodes: 47\n    eval_type: clean\n    eval_script: eval/recovery.py\n    output_file: eval_results/llama31_taxei_s42_clean.json\n    by_task_type:\n      look_at_obj_in_light: 1\n      pick_and_place_simple: 0.625\n      pick_clean_then_place_in_recep: 0.636\n      pick_cool_then_place_in_recep: 0.714\n      pick_heat_then_place_in_recep: 0.875\n      pick_two_obj_and_place: 0.857\n- exp_id: llama31-random-s0-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.745\n    total_episodes: 47\n    eval_type: clean\n    eval_script: eval/recovery.py\n    output_file: eval_results/llama31_random_s0_clean.json\n    by_task_type:\n      look_at_obj_in_light: 0.667\n      pick_and_place_simple: 0.625\n      pick_clean_then_place_in_recep: 0.636\n      pick_cool_then_place_in_recep: 0.571\n      pick_heat_then_place_in_recep: 1\n      pick_two_obj_and_place: 1\n- exp_id: llama31-vanilla-s123-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.723\n    total_episodes: 47\n    eval_type: clean\n    eval_script: eval/recovery.py\n    output_file: eval_results/llama31_vanilla_s123_clean.json\n    by_task_type:\n      look_at_obj_in_light: 0.833\n      pick_and_place_simple: 0.625\n      pick_clean_then_place_in_recep: 0.545\n      pick_cool_then_place_in_recep: 0.571\n      pick_heat_then_place_in_recep: 1\n      pick_two_obj_and_place: 0.857\n- exp_id: recovery-random-s1\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.511\n    detection_rate: 0\n    total_episodes: 47\n- exp_id: recovery-random-s7\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.532\n    detection_rate: 0\n    total_episodes: 47\n- exp_id: eval-llama31-taxei-s42-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: eval-llama31-random-s0-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: llama31-vanilla-s123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.702\n    detection_rate: 0.213\n    total_episodes: 47\n- exp_id: llama31-taxei-s123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.596\n    detection_rate: 0.362\n    success_rate: 0.596\n    total_episodes: 47\n- exp_id: llama31-taxei-s123-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.617\n    total_episodes: 47\n    eval_type: clean\n    by_task_type:\n      look_at_obj_in_light: 0.667\n      pick_and_place_simple: 0.375\n      pick_clean_then_place_in_recep: 0.455\n      pick_cool_then_place_in_recep: 0.571\n      pick_heat_then_place_in_recep: 0.875\n      pick_two_obj_and_place: 0.857\n- exp_id: llama31-random-s123-clean\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    success_rate: 0.766\n    total_episodes: 47\n    eval_type: clean\n    eval_script: eval/recovery.py\n    output_file: eval_results/llama31_random_s123_clean.json\n    by_task_type:\n      look_at_obj_in_light: 1\n      pick_and_place_simple: 0.625\n      pick_clean_then_place_in_recep: 0.636\n      pick_cool_then_place_in_recep: 0.571\n      pick_heat_then_place_in_recep: 0.875\n      pick_two_obj_and_place: 1\n- exp_id: llama31-random-s123-eval\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    recovery_rate: 0.787\n    detection_rate: 0.255\n    total_episodes: 47\n    by_operator:\n      C1_context_truncation:\n        recovered: 10/12\n        rate: 0.833\n        det_rate: 0.083\n      C4_observation_masking:\n        recovered: 8/11\n        rate: 0.727\n        det_rate: 0.182\n      P1_step_order_swap:\n        recovered: 10/12\n        rate: 0.833\n        det_rate: 0.417\n      P2_sub_goal_deletion:\n        recovered: 9/12\n        rate: 0.75\n        det_rate: 0.333\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-16T15:39:47.951Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-16T15:39:47.951Z",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-16T15:39:47.977Z_

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
focus: Cross-model validation升级：TaxEI结构化注入跨模型不稳定（Qwen一致退化、LLaMA高方差1/3 catastrophic seed），Random注入跨模型稳定。论文核心从"单模型负面结果"升级为"结构化vs随机注入的训练稳定性差异是跨架构通用的"。评估新framing能否支撑EMNLP Findings长文。

## paper_framing.md

# Paper Framing: When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning

## Target Venue
**Primary**: EMNLP 2026 Findings (Budapest, Oct 22–29) — 8-page long paper. Negative-result contributions accepted per CFP.
**Secondary**: ACL 2026 Findings if timeline permits.

## Core Question
Under what task-structural conditions does taxonomy-guided error injection improve vs. degrade LLM agent performance?

## Thesis Statement
Taxonomy-guided error injection — a core component of PALADIN's +57pp Recovery Rate gain on ToolBench (though entangled with inference-time retrieval augmentation) — destabilizes embodied planning agent training without improving performance on ALFWorld. TaxEI and Random injection produce **identical** mean performance (58.3% vs Vanilla 67.3%, 5 seeds each), proving taxonomy labels provide zero benefit. Complete 5-seed dose-response reveals **no safe injection dose**: harm begins at 10% (-6.0pp), peaks at 25% (TaxEI nadir 52.7%), then **saturates** — 50% and Full produce similar harm (~58%) with no marginal worsening. The taxonomy penalty follows an **inverted-U curve**, peaking at 25% (-7.3pp TaxEI-Random gap) and vanishing at higher doses. At every concentration, training outcomes are a **lottery** (19-23pp within-dose range, bimodal seed distributions). Cross-model validation on LLaMA-3.1-8B-Instruct reveals that **structured error injection (TaxEI) causes training instability across model architectures** — TaxEI recovery SD=8.6pp vs Random SD=2.1pp (3-seed), with 1/3 seeds triggering Qwen-like catastrophic degradation (59.6% vs baseline 73.1%). Random injection remains stable and even mildly beneficial (mean 76.6% > Vanilla 73.1%). This confirms the harm is not model-specific but a property of structured error patterns themselves: taxonomy-guided injection creates conflicting learning signals that destabilize training across architectures, while unstructured noise is benign or helpful.

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

### 3. Finding: Injection harms equally regardless of taxonomy; introduces catastrophic seed vulnerability
**Clean task performance (all 5-seed complete)**:
- Vanilla SFT: 67.3% ± 4.7pp (seeds 42/0/123/1/7) — stable, no catastrophic seeds
- TaxEI SFT: 58.3% ± 6.5pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.039 uncorrected, NS Bonferroni (p>0.017), Cohen's d=1.58**
- Random SFT: 58.3% ± 8.7pp (seeds 42/0/123/1/7) — **-9.0pp vs Vanilla, p=0.089 uncorrected, NS, Cohen's d=1.28**

**CENTRAL FINDING**: TaxEI and Random produce IDENTICAL mean performance (58.3% = 137/235 tasks). Taxonomy labels provide zero benefit over random injection at the mean level. This directly refutes the hypothesis that structured error labeling improves training signal.

**Catastrophic seed vulnerability**: Both injection methods produce exactly one ~47% outlier (TaxEI seed0=46.8%, Random seed1=46.8%). Vanilla never drops below 61.7%. Injection introduces a 1-in-5 risk of catastrophic training failure absent in clean training.

**Variance gradient**: Vanilla SD (4.7pp) < TaxEI SD (6.5pp) < Random SD (8.7pp). Injection amplifies variance; taxonomy labels may mildly stabilize (TaxEI SD < Random SD), but both are worse than Vanilla. This reverses the 3-seed pattern (where TaxEI had highest SD). Formal variance tests needed (Levene's, n=5).

**Dose-response ablation (fixed-size 4,358 total)** (D034+D035+D038: 全部 5 个剂量完整 5-seed):
| Dose | TaxEI Mean±SD (n) | Random Mean±SD (n) | Vanilla ref | TaxEI-Random Δ |
|------|-------------------|-------------------|-------------|----------------|
| 0% (vanilla) | — | — | 67.3±4.7 (5) | — |
| 10% | 61.3±8.2 (5) | 63.8±5.4 (5) | | -2.5pp |
| 25% | 52.7±7.6 (5) | 60.0±8.0 (5) | | **-7.3pp** |
| 50% | 57.4±9.5 (5) | 58.3±11.7 (5) | | -0.9pp |
| Full | 58.3±6.5 (5) | 58.3±8.7 (5) | | 0pp |

Per-seed data:
- TaxEI 10%: 61.7/70.2/55.3/51.1/68.1. Random 10%: 68.1/66.0/55.3/68.1/61.7.
- TaxEI 25%: 48.9/46.8/46.8/63.8/57.4. Random 25%: 55.3/61.7/51.1/72.3/59.6.
- TaxEI 50%: 51.1/70.2/46.8/63.8/55.3. Random 50%: 57.4/46.8/70.2/70.2/46.8.

**Unified dose-response narrative** (D035+D038, complete 5-seed all doses):
1. **Non-monotonic harm with 25% nadir + saturation**: Injection at ALL doses reduces mean and increases variance. Harm peaks at 25% (TaxEI nadir 52.7%), then partially rebounds: 50% (57.4%) ≈ Full (58.3%). Doubling injection from 50%→Full has zero marginal effect — ~50% is the saturation point beyond which additional errors no longer worsen outcomes.
2. **Inverted-U taxonomy penalty**: TaxEI trails Random at every dose, but the gap peaks at 25% (7.3pp), diminishes at 50% (0.9pp, d=-0.08 negligible), and vanishes at Full (0pp). At 10% the gap is 2.5pp. Taxonomy labels actively harm at intermediate doses where clean/injected balance may maximize conflicting learning signals.
3. **Universal training lottery**: All doses produce extreme seed variance (19-23pp within-dose range). Random 50% shows **bimodal** distribution: {46.8, 46.8, 57.4, 70.2, 70.2} — two distinct failure/success modes, not normal scatter. Report median+IQR alongside mean±SD for robustness.
4. **Practical implication**: No injection dose is "safe." Even 10% produces measurable harm (-6.0pp TaxEI). Outcomes are unpredictable at every concentration level. The training lottery, not dosage, dominates performance variation.

**Variance pattern** (exploratory, not claimable): SD peaks at 50% (TaxEI 9.5, Random 11.7) then **declines** at Full (6.5, 8.7). This is unexpected — Full dose actually reduces variance vs 50%. Possible explanation: at 50%, the model faces maximum ambiguity between clean and error patterns; at Full, the injection signal dominates and the model consistently adapts (poorly). Levene's test NS at n=5. Do not claim variance patterns without significance tests.

**Training lottery at all doses**: Extreme outliers in every condition — TaxEI 10% s0=70.2% vs s1=51.1% (19pp range), Random 25% s1=72.3% vs s123=51.1% (21pp range), Random 50% bimodal (23pp range). Single-seed evaluations are fundamentally unreliable at any dose.

**Taxonomy label penalty** (task-type-specific): TaxEI trails Random in aggregate. Per-task 3-seed analysis: taxonomy injection specifically harms **multi-step coordination tasks** — pick_cool_then_place (TaxEI 38.1% vs Random 57.1%, -19.0pp) and pick_two_obj_and_place (42.9% vs 57.1%, -14.3pp) — while leaving simple tasks largely unaffected (≤4.2pp gap for other 4 task types).

**Recovery under injected errors (seed=42, 47 tasks, round-robin P1/P2/C1/C4)**:
- Vanilla: 61.7% | TaxEI: 59.6% | Random: 63.8%

**Recovery ≈ Resilience (D041)**: Recovery eval rates match normal eval rates for all conditions (V: 61.7%=61.7%, T: 59.6%≈61.7%, R: 63.8%≈66.0%). Models succeed at the same base rate regardless of eval-time error injection — they passively ignore perturbations rather than actively recovering. This is **resilience** (noise tolerance from task competence), not **recovery** (error detection + correction). No training regime instills genuine error awareness.

**Detection Rate**: 0% for all methods.

**Taxonomy labels show no significant benefit**: TaxEI (56.7%) < Random (63.1%) < Vanilla (65.3%). TaxEI vs Random: paired t p≈0.034 (df=2, directionally consistent but low power).

**Per-operator local/global split** (recovery eval, seed=42, verified from eval JSON, **exploratory — N=11-12 per operator**): C4_observation_masking (+9.1pp, 6→7/11), P1_step_order_swap (0.0pp, 7→7/12), C1_context_truncation (−8.3pp, 9→8/12), P2_sub_goal_deletion (−8.3pp, 7→6/12). NOT a smooth monotonic gradient — instead a binary split: the most local/observable operator (C4) shows TaxEI advantage; global/cascading operators (C1, P2) show equal disadvantage; P1 is neutral. **Critical caveat**: each delta is driven by ±1 task success/failure at N=11-12 — well within random noise. Fisher exact tests would be NS for all operators. This must be presented as exploratory/hypothesis-generating, not confirmatory. The directional pattern (local positive, global negative) is suggestive but the specific magnitudes (9.1pp, 8.3pp) carry false precision.

**Variance tests**: Observed SD gradient: Vanilla 3.3pp < Random 7.0pp < TaxEI 8.6pp. F-test p=0.252 (NS, underpowered at df=2,2), but Levene's test p=0.085 (NS), Brown-Forsythe p=0.842 (NS), bootstrap P(SD_TaxEI > SD_Vanilla) = 0.688. All formal tests NS at n=3 — the variance gradient is a directional observation, not a statistically confirmed effect. Report as "observed pattern, suggestive but underpowered."

**Training-evaluation paradox** (≥25% injection only): At high injection ratios, training loss is lower (taxei_50%: 0.260, random_50%: 0.260 vs vanilla: 0.294) but eval performance is worse (51.1-57.4% vs 61.7%). However, at 10% injection, training loss is actually *higher* (0.308) than vanilla — the paradox only emerges above the dose-response threshold. This is consistent with the threshold effect: low injection doesn't change the training distribution enough to lower loss, while high injection causes the model to memorize error patterns. Literature support: Arpit et al. (2017) memorization dynamics, Zhou et al. (2023 LIMA) superficial alignment hypothesis.

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

### 4b. Cross-Model Validation: TaxEI instability is not model-specific (LLaMA-3.1-8B-Instruct, 3-seed)

To test whether the TaxEI failure is Qwen-specific or a general property of structured error injection in embodied planning, we replicate the core experiment on LLaMA-3.1-8B-Instruct (3 seeds: 42/0/123). Training setup identical: Vanilla 4,358 samples (1,635 steps), TaxEI/Random 9,029 samples (3,387 steps).

**LLaMA Recovery Rate (injected eval, 47 tasks)**:
| Condition | s0 (eval=42) | s42 (eval=42) | s123 (eval=123) | Mean±SD |
|-----------|:------------:|:-------------:|:---------------:|:-------:|
| Vanilla | 74.5% | 74.5% | 70.2% | 73.1±2.5% |
| TaxEI | 74.5% | 74.5% | **59.6%** | 69.5±8.6% |
| Random | 74.5% | 76.6% | **78.7%** | 76.6±2.1% |

**LLaMA Clean Success Rate**:
| Condition | s0 | s42 | s123 | Mean±SD |
|-----------|:--:|:---:|:----:|:-------:|
| Vanilla | 72.3% | 72.3% | 72.3% | 72.3±0.0% |
| TaxEI | 76.6% | 76.6% | **61.7%** | 71.6±8.6% |
| Random | 74.5% | 76.6% | 76.6% | 75.9±1.2% |

**Key findings**:
1. **TaxEI training instability is cross-model**: 1/3 seeds (s123) triggers catastrophic degradation on LLaMA (-13.5pp recovery vs vanilla-s123, -10.6pp clean). Pattern mirrors Qwen's consistent degradation but with higher variance (2/3 seeds appear neutral).
2. **Random injection is cross-model stable**: SD=2.1% (recovery), no catastrophic seeds, mean slightly above Vanilla (+3.5pp). This is the opposite of Qwen where Random also degraded.
3. **TaxEI vs Random divergence**: On LLaMA, TaxEI mean (69.5%) < Random mean (76.6%), gap = -7.1pp. The variance difference is stark: TaxEI SD=8.6% vs Random SD=2.1%. Structured error patterns create training instability that unstructured noise does not.
4. **Model-dependent severity, model-independent direction**: Qwen shows consistent TaxEI harm (-9pp, low variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, high variance with catastrophic 1/3 seed). The *direction* (TaxEI ≤ Random ≤ Vanilla for stability) holds across models; the *severity* varies.

**Implication for paper story**: The finding upgrades from "negative result on one model" to "structured error injection is fundamentally destabilizing for embodied planning across architectures." The taxonomy's structured perturbations create systematic biases that some training seed/model combinations amplify into catastrophic failure, while random noise averages out harmlessly.

**Eval seed caveat**: s0/s42 use eval seed=42; s123 uses eval seed=123. Cross-seed aggregation (mean±SD) has a minor eval-seed confound (~2pp from eval randomness). Within each eval-seed group, horizontal (condition) comparisons are fully fair. The critical finding (taxei-s123 collapse) is a within-group horizontal comparison.

### 5. Contribution: What this negative result gives the community
1. **Empirical boundary condition**: First cross-domain transfer test of taxonomy-guided error injection — and first reported failure. Contrasts with PALADIN's tool-use success and EEF's alternative approach of extracting positive signal from failures.
2. **Recovery-pairing disentanglement** (long paper NEW): By testing recovery-paired injection on ALFWorld, we isolate whether the negative result stems from missing recovery pairing or from fundamental task-structure differences. This is the first controlled test of recovery-paired vs unpaired error injection in embodied planning.
3. **Recovery vs resilience distinction** (long paper NEW): Recovery eval rates match normal eval rates — models passively ignore eval-time errors (resilience) rather than actively recovering (recovery). Combined with 0% detection rate, this shows error injection creates no form of error awareness in embodied planning.
4. **Training variance warning**: Error injection increases cross-seed variance 2.6× (SD 8.6pp vs 3.3pp, 5-seed confirmed). Single-seed evaluations of error injection methods are fundamentally unreliable.
7. **Cross-model instability** (long paper NEW): TaxEI structured injection destabilizes training on both Qwen3-8B (consistent -9pp) and LLaMA-3.1-8B-Instruct (intermittent, 1/3 catastrophic seed), while Random injection remains stable across both models. This separates the harm attribution: it is structured error patterns — not model weakness — that cause instability.
5. **No-safe-threshold dose-response + training lottery**: Complete 5-seed dose-response ablation (fixed data size, all 5 doses × 5 seeds) shows harm at every tested dose: 10% (-6.0pp TaxEI), 25% (nadir, -14.6pp TaxEI), 50% (-9.9pp TaxEI), Full (-9.0pp). Non-monotonic: harm peaks at 25%, partial rebound at higher doses. Taxonomy penalty follows inverted-U curve: 10% (-2.5pp) → 25% (-7.3pp peak) → 50% (-0.9pp) → Full (0pp). No injection dose is "safe." Training lottery (19-23pp within-dose range) operates at all concentration levels.
6. **Failure mode taxonomy** (long paper NEW): Qualitative failure analysis categorizes how error injection changes model behavior — noise injection (incoherent plans) vs wrong-learning (systematic biases).

## Core Claims (each backed by experimental evidence)

- **Claim 1**: Error injection (both taxonomy-guided and random) degrades embodied planning performance with large effect size but marginal statistical significance.
  → Support: **5-seed data**: TaxEI 58.3%±6.5pp and Random 58.3%±8.7pp vs Vanilla 67.3%±4.7pp. Both injection methods show -9.0pp gap. Welch t: Vanilla vs TaxEI p≈0.039 (uncorrected), Vanilla vs Random p≈0.089. Bonferroni corrected (3 comparisons, α=0.017): all NS. Cohen's d: 1.58 (TaxEI) and 1.28 (Random) — large effects. Underpowered at n=5; the ~9pp degradation may be a real effect requiring larger N to confirm.

- **Claim 2**: Taxonomy labels provide zero benefit over random injection — structured error labeling does not improve training signal.
  → Support: **TaxEI = Random = 58.3% = 137/235 tasks (5-seed, identical)**. Welch t: t=0.000, p=1.000. This is the paper's strongest finding: the careful design of a 4-operator error taxonomy with per-error-type labels achieves exactly nothing compared to unlabeled random injection. The taxonomy's structured perturbations are indistinguishable from noise at the mean level. Variance differs: TaxEI SD (6.5pp) < Random SD (8.7pp), suggesting taxonomy may mildly stabilize, but both are worse than Vanilla (4.7pp).

- **Claim 3**: Error injection causes **generalization instability** with catastrophic seed vulnerability — training converges stably but evaluation produces unpredictable outcomes including catastrophic failures.
  → Support: **5-seed complete**: Training loss is extremely stable across seeds (SD=0.0007), yet eval SD: Vanilla 4.7pp < TaxEI 6.5pp < Random 8.7pp. Both injection methods produce exactly one catastrophic outlier (~47%): TaxEI seed0=46.8%, Random seed1=46.8%. Vanilla never drops below 61.7%. **Memorization-generalization dissociation** (D029/D033): Forward pass v2 (trajectory-level) confirms injected samples have lower loss than clean (all conditions), but eval is worse. Random memorizes 2.1× deeper than TaxEI (gap -0.078 vs -0.037) yet achieves identical eval — deeper memorization does not linearly predict eval harm. Dose-response loss gaps are non-monotonic (25% > 50%), not the monotonic pattern in v1 (which had a classification bug). D026 behavioral evidence (partial update: 3-seed V/T, 1-seed R, NOT balanced — full 5-seed trajectory collection pending): TaxEI produces ~2.2× more loop_repetition failures than Vanilla. Ratio stable across data subsets but absolute rates pending balanced data. **Observed pattern** (correlation, not established causation): memorization of error patterns + loop fixation at eval time + generalization collapse. Per-operator loss ranking is unstable across conditions, precluding strong per-operator causal claims. 1-in-5 catastrophic seed risk is absent from clean training.

- **Claim 4**: Injection-trained models do not improve error recovery — observed "recovery" is passive resilience (ignoring errors), not active recovery.
  → Support: Recovery rate TaxEI 59.6% vs Vanilla 61.7% (seed=42, 47 tasks). Head-to-head: TaxEI gained 4, lost 5, net -1. Per-operator: TaxEI advantage only on C4_observation_masking (+9.1pp), disadvantage on C1 (-8.3pp) and P2 (-8.3pp). **D041 key insight**: Recovery eval rates match normal eval rates across all conditions (Vanilla 61.7%=61.7%, TaxEI 59.6%≈61.7%, Random 63.8%≈66.0%). Models succeed at the same rate whether or not errors are injected at eval time — they passively ignore perturbations rather than actively detecting and recovering from them. This reframes "no recovery improvement" as "no recovery mechanism at all": the models are **resilient** (robust to noise) rather than **recovery-capable** (able to detect and correct errors). The distinction matters because resilience is a byproduct of task completion ability, while recovery requires explicit error awareness that none of the training regimes instill.

- **Claim 5**: Detection training via error injection is completely ineffective — models show zero error awareness.
  → Support: Detection rate = 0% across all three methods (Vanilla, TaxEI, Random). Combined with D041's recovery≈resilience finding: models neither detect errors explicitly (0% detection) nor respond to them implicitly (recovery rate = normal eval rate). Error injection during training fails to create any form of error awareness in the embodied planning domain.

- **Claim 6**: The divergence from PALADIN's positive results reveals task-structural boundary conditions for error injection.
  → Support: Qualitative analysis contrasting error observability, recovery action space, error locality, feedback granularity, and inference-time augmentation between tool-use and embodied planning domains. Note: PALADIN's +57pp includes retrieval augmentation (~30pp contribution), making our pure-SFT comparison a stricter isolation of the training signal's value. Additionally, EEF (arXiv 2504.13145) succeeds on WebShop by **extracting good signal from failures** rather than injecting bad signal — suggesting the injection direction itself may be flawed for planning domains.

- **Claim 7** (long paper NEW): Recovery-paired injection actively harms performance, definitively ruling out recovery pairing as PALADIN's missing ingredient.
  → Support: **TaxEI-RP 4-seed mean 47.9% ± 7.8pp** (s42=38.3%, s0=46.8%, s1=48.9%, s123=57.4%) vs TaxEI 58.3% vs Vanilla 67.3%. Recovery-paired training (14,437 samples = TaxEI 9,029 + recovery continuations 5,408) performs **10pp worse than unpaired TaxEI** and **19pp worse than Vanilla**. Adding recovery demonstrations does not teach active recovery — it adds noise that further corrupts the action distribution. Detection rate remains 0%. This definitively answers the PALADIN recovery-pairing confound: the failure is not due to missing recovery pairs, but to fundamental task-structural incompatibility. (D043)

- **Claim 8** ~~(long paper NEW)~~: **CANCELLED (D040)**. WebShop replication infeasible — P1_StepOrderSwap incompatible with linear action space (search+click), taxonomy 4→3 makes cross-environment comparison inequivalent. Downgraded to Discussion section analysis of ALFWorld vs WebShop structural differences and why cross-environment replication is non-trivial.

- **Claim 9** (long paper NEW): Structured error injection (TaxEI) causes **cross-model training instability**, while random injection remains stable — the harm is a property of structured error patterns, not model-specific.
  → Support: **LLaMA-3.1-8B-Instruct 3-seed replication**. TaxEI recovery mean 69.5%±8.6pp vs Random 76.6%±2.1pp vs Vanilla 73.1%±2.5pp. TaxEI variance 4× higher than Random (SD 8.6 vs 2.1). 1/3 seeds (s123) shows catastrophic TaxEI collapse: recovery 59.6% (vs vanilla 70.2%, Δ=-10.6pp; vs random 78.7%, Δ=-19.1pp). Other 2 seeds show TaxEI=Vanilla=74.5%. Random is consistently stable or mildly beneficial across all seeds. **Cross-model pattern**: Qwen shows consistent TaxEI harm (mean -9pp, moderate variance); LLaMA shows intermittent TaxEI harm (mean -3.6pp, extreme variance with 1/3 catastrophic). Direction (TaxEI ≤ Random for stability) holds across both models. This upgrades the finding from "Qwen-specific negative result" to "structured injection is fundamentally destabilizing for embodied planning."

## Anticipated Reviewer Concerns

1. **"Statistical power is limited."**
   → All three conditions now have **5 seeds**. Welch t: Vanilla vs TaxEI p=0.039 (uncorrected), Bonferroni NS (α=0.017). Cohen's d=1.58 (large). Power at n=5: 45.2%; need n=9 for 80%. We do not claim significance after correction but emphasize the large effect size (-9.0pp) and report all individual seed results. Bootstrap 95% CI: [+3.4, +15.8]pp. Bayes Factor 0.68 (inconclusive). The variance gradient (Vanilla 4.7 < TaxEI 6.5 < Random 8.7) is consistent across seeds.

2. **"ALFWorld has only 47 test tasks — too small for reliable conclusions."**
   → Valid concern. We explicitly compute statistical power and report confidence intervals. The 47-task limitation is an ALFWorld constraint shared by all prior work on this benchmark. With 5 seeds × 47 tasks = 235 episodes per condition, our pooled sample gives adequate power for the observed ~9pp effect (d≈1.4). WebShop replication was planned but cancelled (D040: P1 incompatible with linear action space); the structural incompatibility itself supports our task-structure boundary condition argument.

3. **"Maybe the taxonomy itself is poorly designed."**
   → Gate 1 (injection legality ≥ 80%) passed at 100% — all injected trajectories are structurally valid. Gate 2 (recovery quality ≥ 75%) passed at 97.5%. The taxonomy is functional; it just doesn't help training.

4. **"The training recipe might be suboptimal for injection data."**
   → The same recipe produces strong Vanilla results (67.3% ± 4.7pp vs 42.6% zero-shot baseline, +24.7pp, 5 seeds), confirming the recipe works. The degradation is specific to injection augmentation, not training methodology.

5. **"50% injection ratio is too high — you're drowning the signal."**
   → Comprehensively addressed with complete 5-seed fixed-size dose-response ablation at 10%/25%/50%/Full (all 4,358 total samples, all 5 doses × 5 seeds). No safe threshold exists: even 10% injection degrades performance (TaxEI -6.0pp). The harm profile is non-monotonic: monotonic degradation 0%→10%→25% (TaxEI nadir 52.7%), partial rebound 25%→50%→Full driven by training lottery. Taxonomy penalty follows inverted-U curve peaking at 25% (-7.3pp TaxEI-Random gap). The pattern holds for both TaxEI and Random, suggesting it is a general property of error injection.

6. **"Why is detection rate 0%? Evaluation might be flawed."**
   → Current eval checks for explicit error flagging in model output. Models may develop implicit error awareness (e.g., output hedging, re-planning) not captured by binary detection metrics. We discuss this limitation and propose alternative detection measures.

7. **"Why not compare directly on ToolBench?"**
   → Our contribution is precisely the domain contrast. Running PALADIN on ALFWorld or TaxEI on ToolBench would strengthen the paper but requires substantial engineering. We list this as future work.

8. **"PALADIN uses error+recovery pairs; TaxEI uses standalone errors. Isn't recovery-pairing the real difference?"** [Dream M+W]
   → **Directly tested and refuted** (D043). TaxEI-RP (recovery-paired, 14,437 samples) achieves 47.9% ± 7.8pp — **10pp worse** than unpaired TaxEI (58.3%) and **19pp worse** than Vanilla (67.3%). Recovery pairing not only fails to help, it actively harms. This is the paper's strongest evidence for the task-structure hypothesis: even mimicking PALADIN's recovery-pairing design cannot overcome the fundamental incompatibility of error injection with embodied planning.

9. **"Power analysis says n=9 needed but you only ran n=5."** [Dream W]
   → We acknowledge n=5 is underpowered (45.2%) for the observed effect at α=0.017 (Bonferroni). We report this transparently with power curves. The large effect size (d=1.58), consistent direction across all 5 seeds, and dose-response replication across 25 independent training runs provide converging evidence despite per-comparison underpowerment.

10. **"Data volume confound: Vanilla has half the training data."** [Dream W]
    → Vanilla uses 4,358 samples; TaxEI/Random use 9,029. We address this via dose-response ablation at fixed 4,358 total samples. At 10% injection, TaxEI still degrades (-6.0pp, 5-seed), confirming harm is from injection content, not volume. The full-scale comparison's volume asymmetry is acknowledged as a limitation.

11. **"Only tested on one model — maybe it's a Qwen-specific issue."**
    → Addressed with LLaMA-3.1-8B-Instruct 3-seed replication. TaxEI instability reproduces cross-model (LLaMA SD=8.6pp, 1/3 catastrophic seed). Random injection is stable on both models. The direction (TaxEI harmful/unstable, Random neutral/stable) is consistent across architectures; only severity differs (Qwen: consistent harm; LLaMA: intermittent but catastrophic when triggered). This rules out model-specific explanations and points to structured error patterns as the causal factor.

## Key Differentiators vs PALADIN

PALADIN (arXiv 2509.25238) succeeds because tool-use has four structural properties that embodied planning lacks:

1. **Discrete error signals**: Tool calls return explicit success/failure codes. In ALFWorld, a wrong action (e.g., "go to countertop 2" when the object is on shelf 1) produces a valid-looking observation — the agent receives no signal that it erred.

2. **Local recoverability**: A failed API call can be retried or substituted with an alternative tool. In planning, a wrong early step (e.g., heating before picking up) invalidates the entire downstream plan, requiring global re-planning rather than local retry.

3. **Bounded action space for recovery**: ToolBench has a finite API catalog — recovery means selecting from known alternatives. ALFWorld's text-based action space is open-ended, making "what to do after an error" fundamentally harder to learn from examples.

4. **Scale**: PALADIN trains on 50K+ trajectories with 80% recovery focus. TaxEI has 9K total samples with 50% injection. The lower data volume means less room for the model to separate error patterns from noise.

**This contrast IS the paper's core contribution**: error injection is not universally beneficial for LLM agents — it requires discrete, observable, locally recoverable errors to serve as effective training signal rather than noise.

## Note on v3→v4 Vanilla Discrepancy
v3 vanilla SFT achieved 74.5% (seed=42) while v4 three-seed mean is 65.3%. The 9.2pp gap is partially explained by: (1) v3 used different data volume (4,176 vs 4,358 samples due to format alignment changes); (2) seed variance (v4 seed=42 = 61.7%, seed=0 = 68.1%). Paper should briefly note this in supplement to preempt reviewer confusion about different vanilla numbers across experimental rounds.

## Dream Review Findings (dream_20260515T020837)

**Scores**: Best 2/5 (artifact: dream fabricated experiments), Median 3/5 (Borderline Accept), Worst 2.5/5 (Borderline Revise)

**Confirmed action items (cross-tier consistent)**:
1. Related work must expand to 15-20 refs. Add: Reflexion (Shinn 2023), McCoy et al. (2020) seed-dependent generalization, Mosbach et al. (2021) fine-tuning stability, Madry et al. (2018) adversarial training, Bengio et al. (2009) curriculum learning, D'Amour et al. (2022) underspecification, ReAct (Yao 2023).
2. PALADIN recovery-pairing confound must be discussed prominently: PALADIN pairs errors WITH recovery demonstrations; TaxEI injects standalone errors without recovery. This is the most parsimonious alternative explanation.
3. Formal variance test: F-test p=0.252 (NS) is our strongest stat. Also compute Levene's test for robustness.
4. Paper structure for 4-page limit: Intro → Method → Main Results (Table 1 + dose-response) → Qualitative/Error Echo → Per-Operator Gradient → Discussion → Conclusion. Move training dynamics, recovery prompting to appendix.

**Observation items (monitor in real reviews)**:
- Core novelty concern: "seed variance unreliable" is known — our per-operator gradient and error echo differentiate us
- Self-undermining: we use 3 seeds but findings suggest ≥5 needed — prominent limitation, consider power analysis
- Data volume confound: Vanilla 4,358 vs TaxEI/Random 9,029 — acknowledge in limitations (dose-response at 10% controls for this partially)
- EEF 2×2 framework: {positive, negative signal} × {tool-use, planning} could sharpen Discussion

## Supplementary Experiments — Long Paper (8-page)

### Done (from short paper phase)
- ~~**3-seed main conditions**~~: ✅ Vanilla 65.3%±3.3pp, TaxEI 56.7%±8.6pp, Random 63.1%±7.0pp.
- ~~**Dose-response 3-seed (25%/50%)**~~: ✅ Dual regime confirmed. 10% = seed=42 only.
- ~~**Recovery eval (seed=42)**~~: ✅ TaxEI 59.6%, Vanilla 61.7%, Random 63.8%. Detection 0%.

### Priority 1 (required for 8-page long paper)
- ~~**5-seed extension** [Claims 1,3]~~: ✅ Done. Vanilla 67.3±4.7, TaxEI=Random=58.3%. D032.
- ~~**Training dynamics** [Claim 3]~~: ✅ Done. Forward pass v2 (trajectory-level). D027/D029/D033.
- ~~**Qualitative failure analysis** [Claims 1,6]~~: ✅ Done. TaxEI loop_repetition 2.2×. D026.
- ~~**Extended statistics** [Claims 1,3]~~: ✅ Done. Bootstrap CI, power, Bayesian. D030-D032.
- ~~**Dose-response 5-seed** [Claim 3]~~: ✅ Done. All 5 doses × 5 seeds complete. 10% (D034), 25% (D035/D036), 50% (D038). Inverted-U taxonomy penalty curve. ~24 GPU-h.
- **Recovery-paired injection** [Claim 7]: 🔄 Training in progress (4 seeds × 4 GPU). Datagen complete (711/760), 14,437 samples. ~16 GPU-h.
- ~~**WebShop replication** [Claim 8]~~: ❌ CANCELLED (D040). P1 incompatible with linear action space. Downgraded to Discussion.
- **Recovery eval multi-seed** [Claims 4,5]: 7/15 complete. Remaining 8/15 after TaxEI-RP. ~15 GPU-h.

### Priority 1.5 (cross-model validation)
- ~~**LLaMA-3.1-8B cross-model replication** [Claim 9]~~: ✅ Done. 3 seeds × 3 conditions, all training + eval complete. TaxEI instability confirmed cross-model (SD=8.6%, 1/3 catastrophic). Random stable (SD=2.1%). ~36 GPU-h.

### Priority 2 (strengthens further)
- **Scale ablation** [Claim 6]: 25K-50K trajectories. ~$30-50 API + ~20 GPU-h.

### Estimated total: ~120 GPU-hours (~30h wall clock with 4 × 5090)


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
  conclusion: success
  metrics:
    final_loss: 0.295
    avg_loss: 0.415
    token_accuracy: 0.898
    train_steps: 1635
    train_epochs: 3
    train_duration_min: 59.4
    checkpoint_path: checkpoints/mini_vanilla_sft_v4_seed7/v0-20260515-214031/checkpoint-1635
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
    per_operator:
      C1_context_truncation:
        recovered: 9
        total: 12
        rate: 0.75
      C4_observation_masking:
        recovered: 6
        total: 11
        rate: 0.545
      P1_step_order_swap:
        recovered: 7
        total: 12
        rate: 0.583
      P2_sub_goal_deletion:
        recovered: 7
        total: 12
        rate: 0.583
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
- exp_id: v4-taxei-fixed-inject25-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4258
    train_duration_min: 56.1
    train_steps: 1635
    train_epochs: 3
    data_count: 4358
- exp_id: v4-taxei-fixed-inject25-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4253
    train_duration_min: 55.9
    train_steps: 1635
    train_epochs: 3
    data_count: 4358
- exp_id: v4-taxei-fixed-inject50-s0
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    train_loss: 0.4342
    train_duration_min: 52.4
    train_steps: 1635
    train_epochs: 3
    data_count: 4358
- exp_id: v4-taxei-fixed-inject50-s123
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    train_loss: 0.4348
    train_duration_min: 52.9
    train_steps: 1635
    train_epochs: 3
    data_count: 4358
- exp_id: v4-random-fixed-inject25-s0
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: v4-random-fixed-inject25-s123
  name: ''
  status: PREPARING
  conclusion: success
  metrics: {}
- exp_id: v4-random-fixed-inject50-s0
  name: ''
  status: PREPARING
  conclusion: success
  metrics: {}
- exp_id: v4-random-fixed-inject50-s123
  name: ''
  status: PREPARING
  conclusion: success
  metrics: {}
- exp_id: v4-taxei-fixed-inject25-s0-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    success_rate: 0.468
    successes: 22
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 4
        rate: 0.667
      pick_and_place_simple:
        total: 8
        success: 2
        rate: 0.25
      pick_clean_then_place_in_recep:
        total: 11
        success: 5
        rate: 0.455
      pick_cool_then_place_in_recep:
        total: 7
        success: 2
        rate: 0.286
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 3
        rate: 0.429
- exp_id: v4-taxei-fixed-inject25-s123-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    success_rate: 0.468
    successes: 22
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 4
        rate: 0.667
      pick_and_place_simple:
        total: 8
        success: 3
        rate: 0.375
      pick_clean_then_place_in_recep:
        total: 11
        success: 5
        rate: 0.455
      pick_cool_then_place_in_recep:
        total: 7
        success: 1
        rate: 0.143
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 3
        rate: 0.429
- exp_id: v4-taxei-fixed-inject50-s0-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    eval_success_rate: 0.702
    eval_successes: 33
    eval_total: 47
- exp_id: v4-taxei-fixed-inject50-s123-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    eval_success_rate: 0.468
    eval_successes: 22
    eval_total: 47
- exp_id: v4-random-fixed-inject25-s0-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    success_rate: 0.617
    total: 47
    successes: 29
    by_task:
      look_at_obj_in_light: 0.667
      pick_and_place_simple: 0.625
      pick_clean_then_place_in_recep: 0.455
      pick_cool_then_place_in_recep: 0.571
      pick_heat_then_place_in_recep: 0.75
      pick_two_obj_and_place: 0.714
- exp_id: v4-random-fixed-inject25-s123-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    success_rate: 0.511
    total: 47
    successes: 24
    by_task:
      look_at_obj_in_light: 0.667
      pick_and_place_simple: 0.375
      pick_clean_then_place_in_recep: 0.545
      pick_cool_then_place_in_recep: 0.143
      pick_heat_then_place_in_recep: 0.75
      pick_two_obj_and_place: 0.571
- exp_id: v4-random-fixed-inject50-s0-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    success_rate: 0.468
    successes: 22
    total: 47
- exp_id: v4-random-fixed-inject50-s123-eval
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    success_rate: 0.702
    successes: 33
    total: 47
- exp_id: v4-vanilla-recovery-eval-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.681
    successes: 32
    total: 47
    detection_rate: 0
- exp_id: v4-vanilla-recovery-eval-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.66
    successes: 31
    total: 47
    detection_rate: 0
- exp_id: v4-taxei-recovery-eval-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.468
    successes: 22
    total: 47
    detection_rate: 0
- exp_id: v4-taxei-recovery-eval-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.617
    successes: 29
    total: 47
    detection_rate: 0
- exp_id: v4-random-recovery-eval-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.553
    detection_rate: 0
    success_rate: 0.553
    total_episodes: 47
    by_operator:
      C1_context_truncation:
        total: 12
        recovered: 7
        recovery_rate: 0.583
      C4_observation_masking:
        total: 11
        recovered: 6
        recovery_rate: 0.545
      P1_step_order_swap:
        total: 12
        recovered: 7
        recovery_rate: 0.583
      P2_sub_goal_deletion:
        total: 12
        recovered: 6
        recovery_rate: 0.5
- exp_id: v4-random-recovery-eval-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.66
    detection_rate: 0
    total_episodes: 47
    by_operator:
      C1_context_truncation:
        recovery_rate: 0.75
        recovered: 9
        total: 12
      P2_sub_goal_deletion:
        recovery_rate: 0.75
        recovered: 9
        total: 12
      P1_step_order_swap:
        recovery_rate: 0.583
        recovered: 7
        total: 12
      C4_observation_masking:
        recovery_rate: 0.545
        recovered: 6
        total: 11
- exp_id: v4-vanilla-seed1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.292
    avg_loss: 0.416
    token_accuracy: 0.903
    train_steps: 1635
    train_epochs: 3
    train_duration_min: 58.8
    memory_gib: 17.63
    checkpoint_path: checkpoints/mini_vanilla_sft_v4_seed1/v0-20260515-214031/checkpoint-1635
- exp_id: v4-taxei-seed1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.1667
    avg_loss: 0.3561
    token_accuracy: 0.915
    final_token_acc: 0.942
    train_steps: 3387
    train_epochs: 3
    train_duration_min: 108.9
    memory_gib: 18.49
    checkpoint_path: checkpoints/mini_taxei_sft_v4_seed1/v0-20260515-214035/checkpoint-3387
- exp_id: v4-taxei-seed7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    current_step: 3387
    total_steps: 3387
    progress_pct: 100
    train_loss: 0.3568
    final_step_loss: 0.1753
    token_acc: 0.9009
    final_token_acc: 0.9328
    train_runtime_s: 6591.9
    epochs: 3
    peak_memory_gib: 18.49
    gpu: cuda:3
    pid: 155145
- exp_id: v4-training-dynamics-forward
  name: ''
  status: DONE
  conclusion: success
  metrics:
    vanilla_full:
      clean_loss: 0.6853
      clean_n: 4358
    taxei_full:
      clean_loss: 0.7712
      injected_loss: 0.6139
      clean_n: 8269
      injected_n: 760
      per_operator:
        P1_StepOrderSwap: 0.6165
        P2_SubGoalDeletion: 0.6161
        C1_ContextTruncation: 0.5932
        C4_ObservationMasking: 0.6298
    random_full:
      clean_loss: 0.7354
      injected_loss: 0.5902
      clean_n: 8269
      injected_n: 760
    dose_response:
      taxei_10pct:
        clean_loss: 0.6628
        injected_loss: 0.6464
        gap: -0.0164
        injected_n: 70
      taxei_25pct:
        clean_loss: 0.701
        injected_loss: 0.574
        gap: -0.127
        injected_n: 168
      taxei_50pct:
        clean_loss: 0.8516
        injected_loss: 0.6547
        gap: -0.1969
        injected_n: 370
    key_findings: 'Clear dose-response: injected-clean gap widens from -0.016 (10%)
      to -0.127 (25%) to -0.197 (50%). TaxEI operators C1_ContextTruncation consistently
      lowest loss. Higher injection rates also degrade clean sample loss (0.663→0.701→0.852).'
- exp_id: v4-recovery-paired-datagen
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_injected_variants: 760
    successfully_processed: 711
    skipped_no_source_match: 49
    operators:
      C1_ContextTruncation: 182
      C4_ObservationMasking: 175
      P1_StepOrderSwap: 170
      P2_SubGoalDeletion: 184
    recovery_steps_mean: 7.6
    recovery_steps_min: 1
    recovery_steps_max: 46
    total_recovery_api_calls: 5408
    output_file: /root/autodl-tmp/tax_error_inject_agent/data/recovery_paired/recovery_paired.jsonl
    output_lines: 711
    output_size_mb: 20.8
    log_file: /root/autodl-tmp/tax_error_inject_agent/logs/recovery_paired_gen.log
- exp_id: v4-vanilla-seed7-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.745
    eval_successes: 35
    eval_total: 47
    vs_seed42_pp: 12.8
- exp_id: v4-vanilla-seed1-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    eval_success_rate: 0.66
    eval_successes: 31
    eval_total: 47
    vs_seed42_pp: 4.3
- exp_id: v4-random-seed1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.167
    final_token_acc: 0.938
    initial_loss: 4.017
    total_steps: 3387
    epochs: 3
    total_flos: 697000000000000000
- exp_id: v4-random-seed7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.173
    final_token_acc: 0.935
    initial_loss: 4.017
    total_steps: 3387
    epochs: 3
    total_flos: 697192362530058200
    train_runtime_sec: 6672
    memory_gib: 18.49
- exp_id: v4-taxei-seed1-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.596
    successes: 28
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 5
        rate: 0.833
      pick_and_place_simple:
        total: 8
        success: 4
        rate: 0.5
      pick_clean_then_place_in_recep:
        total: 11
        success: 5
        rate: 0.455
      pick_cool_then_place_in_recep:
        total: 7
        success: 2
        rate: 0.286
      pick_heat_then_place_in_recep:
        total: 8
        success: 7
        rate: 0.875
      pick_two_obj_and_place:
        total: 7
        success: 5
        rate: 0.714
- exp_id: v4-taxei-seed7-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.617
    successes: 29
    total: 47
    by_task:
      look_at_obj_in_light: 4/6 (0.667)
      pick_and_place_simple: 5/8 (0.625)
      pick_clean_then_place_in_recep: 5/11 (0.455)
      pick_cool_then_place_in_recep: 4/7 (0.571)
      pick_heat_then_place_in_recep: 7/8 (0.875)
      pick_two_obj_and_place: 4/7 (0.571)
- exp_id: qualitative-failure-analysis
  name: ''
  status: PREPARING
  conclusion: success
  metrics:
    data_source: eval_results/failure_analysis.json
    taxei_loop_repetition_rate: 0.174
    vanilla_loop_repetition_rate: 0.078
    random_loop_repetition_rate: 0.032
    taxei_loop_count: 49
    vanilla_loop_count: 22
    random_loop_count: 6
    per_operator:
      P1: 15
      P2: 14
      C1: 11
      C4: 9
    note: Random data only from seed=42 recovery eval + 3-seed clean eval (188 episodes
      vs 282). Rates to be updated after 5-seed completion.
- exp_id: v4-taxei-fixed-inject10-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4238
    final_loss: 0.3102
    final_token_acc: 0.8822
    epochs: 3
    total_steps: 1635
    train_runtime_sec: 3494
    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s0/v0-20260516-005247/checkpoint-1635
- exp_id: v4-training-dynamics-forward-v2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    subsets_computed:
    - vanilla_full
    - taxei_full
    - random_full
    - taxei_inject10
    - taxei_inject25
    - taxei_inject50
    taxei_inject50_injected_mean_loss: 0.8185
    taxei_inject50_clean_mean_loss: 0.8514
    per_operator:
      C1_ContextTruncation:
        mean: 0.6489
        n: 101
      C4_ObservationMasking:
        mean: 0.6782
        n: 92
      P1_StepOrderSwap:
        mean: 0.6374
        n: 89
      P2_SubGoalDeletion:
        mean: 0.6542
        n: 88
    plots:
    - subset_comparison
    - operator_breakdown
    - dose_response
    output_dir: /root/autodl-tmp/tax_error_inject_agent/artifacts/training_dynamics_v2/
- exp_id: v4-random-seed1-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.468
    successes: 22
    total: 47
    by_task_type:
      look_at_obj_in_light:
        success: 5
        total: 6
        rate: 0.833
      pick_and_place_simple:
        success: 2
        total: 8
        rate: 0.25
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
        success: 3
        total: 7
        rate: 0.429
- exp_id: v4-random-seed7-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.553
    successes: 26
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 5
        rate: 0.833
      pick_and_place_simple:
        total: 8
        success: 4
        rate: 0.5
      pick_clean_then_place_in_recep:
        total: 11
        success: 6
        rate: 0.545
      pick_cool_then_place_in_recep:
        total: 7
        success: 3
        rate: 0.429
      pick_heat_then_place_in_recep:
        total: 8
        success: 5
        rate: 0.625
      pick_two_obj_and_place:
        total: 7
        success: 3
        rate: 0.429
- exp_id: v4-taxei-inject10-seed0
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: v4-taxei-inject10-seed123
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: v4-random-inject10-seed0
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: v4-taxei-fixed-inject10-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4234
    final_loss: 0.3097
    final_token_acc: 0.8882
    epochs: 3
    total_steps: 1635
    train_runtime_sec: 3497
    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_taxei_fixed_inject10_s123/v0-20260516-014833/checkpoint-1635
- exp_id: v4-random-fixed-inject10-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4227
    final_loss: 0.276
    final_token_acc: 0.9067
    epochs: 3
    total_steps: 1635
    train_runtime_sec: 3531
    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/checkpoints/v4_random_fixed_inject10_s0/v0-20260516-014835/checkpoint-1635
- exp_id: v4-taxei-fixed-inject10-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.3013
    train_loss_avg: 0.4225
    final_token_acc: 0.8947
    total_steps: 1635
    epochs: 3
    train_runtime_sec: 3469
    memory_gib: 18.13
    train_speed_s_per_it: 2.121
- exp_id: v4-random-fixed-inject10-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.3124
    train_loss_avg: 0.4236
    final_token_acc: 0.8867
    total_steps: 1635
    epochs: 3
    train_runtime_sec: 3535.7
    train_samples_per_second: 3.698
    train_steps_per_second: 0.462
    memory_gib: 18.95
- exp_id: v4-taxei-fixed-inject10-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.237
    train_loss_avg: 0.4212
    final_token_acc: 0.905
    total_steps: 1635
    epochs: 3
    train_runtime_sec: 3437
    memory_gib: 18.15
    train_speed_s_per_it: 2.102
- exp_id: v4-random-fixed-inject10-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.3096
    train_loss_avg: 0.4238
    final_token_acc: 0.8902
    total_steps: 1635
    epochs: 3
    train_runtime_sec: 3488
    memory_gib: 18.13
    train_speed_s_per_it: 2.132
- exp_id: v4-random-fixed-inject10-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_loss: 0.2352
    train_loss_avg: 0.4209
    final_token_acc: 0.9066
    total_steps: 1635
    epochs: 3
    train_runtime_sec: 3511.93
    memory_gib: 18.15
    train_speed_s_per_it: 2.148
- exp_id: v4-taxei-fixed-inject10-s123-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    error: CUDA OOM during model loading on GPU 0
- exp_id: v4-random-fixed-inject10-s0-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    error: CUDA OOM during model loading on GPU 0
- exp_id: v4-taxei-fixed-inject10-s1-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics:
    error: CUDA OOM during model loading on GPU 0
- exp_id: v4-taxei-fixed-inject10-s0-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.702
    successes: 33
    total: 47
    by_task_type:
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
        success: 8
        rate: 0.727
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
        success: 4
        rate: 0.571
- exp_id: v4-random-fixed-inject10-s123-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.553
    successes: 26
    total: 47
    by_task_type:
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
        success: 5
        rate: 0.455
      pick_cool_then_place_in_recep:
        total: 7
        success: 2
        rate: 0.286
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 3
        rate: 0.429
- exp_id: v4-taxei-fixed-inject10-s123-eval-r2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: v4-random-fixed-inject10-s0-eval-r2
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: v4-taxei-fixed-inject10-s123-eval-r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.553
    successes: 26
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 5
        rate: 0.833
      pick_and_place_simple:
        total: 8
        success: 4
        rate: 0.5
      pick_clean_then_place_in_recep:
        total: 11
        success: 5
        rate: 0.455
      pick_cool_then_place_in_recep:
        total: 7
        success: 2
        rate: 0.286
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 4
        rate: 0.571
- exp_id: v4-random-fixed-inject10-s0-eval-r3
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.66
    successes: 31
    total: 47
    by_task_type:
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
- exp_id: v4-taxei-fixed-inject10-s1-eval-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.511
    successes: 24
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 4
        rate: 0.667
      pick_and_place_simple:
        total: 8
        success: 4
        rate: 0.5
      pick_clean_then_place_in_recep:
        total: 11
        success: 5
        rate: 0.455
      pick_cool_then_place_in_recep:
        total: 7
        success: 2
        rate: 0.286
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 3
        rate: 0.429
- exp_id: v4-taxei-fixed-inject10-s7-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.681
    successes: 32
    total: 47
    by_task_type:
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
        success: 7
        rate: 0.875
      pick_two_obj_and_place:
        total: 7
        success: 4
        rate: 0.571
- exp_id: v4-random-fixed-inject10-s1-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.681
    successes: 32
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 5
        rate: 0.833
      pick_and_place_simple:
        total: 8
        success: 5
        rate: 0.625
      pick_clean_then_place_in_recep:
        total: 10
        success: 5
        rate: 0.5
      pick_cool_then_place_in_recep:
        total: 7
        success: 6
        rate: 0.857
      pick_heat_then_place_in_recep:
        total: 8
        success: 7
        rate: 0.875
      pick_two_obj_and_place:
        total: 7
        success: 4
        rate: 0.571
- exp_id: v4-taxei-fixed-inject25-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4243
    train_duration_min: 57.5
    train_steps: 1635
    train_epochs: 3
    data_count: 4358
- exp_id: v4-random-fixed-inject25-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4261
    final_step_loss: 0.2442
    token_accuracy: 0.9123
    train_steps: 1635
    train_epochs: 3
    train_runtime_sec: 3417.56
    train_duration_min: 56.96
    train_samples_per_second: 3.826
    train_steps_per_second: 0.478
    memory_gib: 18
    data_count: 4358
- exp_id: v4-taxei-fixed-inject25-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4242
    final_step_loss: 0.2571
    token_accuracy: 0.904
    train_steps: 1635
    train_epochs: 3
    train_runtime_sec: 3430.48
    train_duration_min: 57.17
    train_samples_per_second: 3.811
    train_steps_per_second: 0.477
    memory_gib: 17.55
    data_count: 4358
- exp_id: v4-random-fixed-inject10-s7-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.617
    successes: 29
    total: 47
    by_task_type:
      look_at_obj_in_light:
        success: 5
        total: 6
        rate: 0.833
      pick_and_place_simple:
        success: 4
        total: 8
        rate: 0.5
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
- exp_id: v4-random-fixed-inject25-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4254
    final_step_loss: 0.265
    token_acc: 0.899
    epochs: 3
    steps: 1635
    train_runtime_sec: 3407
- exp_id: v4-taxei-fixed-inject25-s1-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.638
    successes: 30
    total: 47
    eval_split: valid_unseen
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 4
        rate: 0.667
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
        success: 3
        rate: 0.429
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 6
        rate: 0.857
- exp_id: v4-taxei-fixed-inject25-s7-eval
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: v4-random-fixed-inject25-s1-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.723
    successes: 34
    total: 47
    by_task_type:
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
        success: 7
        rate: 0.875
      pick_two_obj_and_place:
        total: 7
        success: 6
        rate: 0.857
- exp_id: v4-random-fixed-inject25-s7-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.596
    successes: 28
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 4
        rate: 0.667
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
        success: 3
        rate: 0.429
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 4
        rate: 0.571
- exp_id: v4-taxei-fixed-inject25-s1-eval-r2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: v4-taxei-fixed-inject25-s7-eval-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.574
    successes: 27
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 5
        rate: 0.833
      pick_and_place_simple:
        total: 8
        success: 3
        rate: 0.375
      pick_clean_then_place_in_recep:
        total: 11
        success: 5
        rate: 0.455
      pick_cool_then_place_in_recep:
        total: 7
        success: 3
        rate: 0.429
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 5
        rate: 0.714
- exp_id: v4-taxei-fixed-inject50-s1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: v4-random-fixed-inject50-s1
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: v4-taxei-fixed-inject50-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4674
    token_acc: 0.9189
    train_runtime_sec: 3834
    memory_gib: 29.94
- exp_id: v4-random-fixed-inject50-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4672
    token_acc: 0.9156
    train_runtime_sec: 3832
    memory_gib: 29.94
- exp_id: v4-taxei-fixed-inject50-s1-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4667
    token_acc: 0.9072
    train_runtime_sec: 3858
    memory_gib: 30.37
- exp_id: v4-random-fixed-inject50-s1-r2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4664
    token_acc: 0.9012
    train_runtime_sec: 3928
    memory_gib: 30.37
- exp_id: v4-taxei-fixed-inject50-s1-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.638
    successes: 30
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 6
        rate: 1
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
        success: 5
        rate: 0.625
      pick_two_obj_and_place:
        total: 7
        success: 3
        rate: 0.429
- exp_id: v4-random-fixed-inject50-s1-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.702
    successes: 33
    total: 47
    by_task_type:
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
        success: 8
        rate: 0.727
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
- exp_id: v4-taxei-fixed-inject50-s7-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.553
    successes: 26
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 5
        rate: 0.833
      pick_and_place_simple:
        total: 8
        success: 4
        rate: 0.5
      pick_clean_then_place_in_recep:
        total: 11
        success: 6
        rate: 0.545
      pick_cool_then_place_in_recep:
        total: 7
        success: 2
        rate: 0.286
      pick_heat_then_place_in_recep:
        total: 8
        success: 6
        rate: 0.75
      pick_two_obj_and_place:
        total: 7
        success: 3
        rate: 0.429
- exp_id: v4-random-fixed-inject50-s7-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.468
    successes: 22
    total: 47
    by_task_type:
      look_at_obj_in_light:
        total: 6
        success: 4
        rate: 0.667
      pick_and_place_simple:
        total: 8
        success: 4
        rate: 0.5
      pick_clean_then_place_in_recep:
        total: 11
        success: 5
        rate: 0.455
      pick_cool_then_place_in_recep:
        total: 7
        success: 1
        rate: 0.143
      pick_heat_then_place_in_recep:
        total: 8
        success: 5
        rate: 0.625
      pick_two_obj_and_place:
        total: 7
        success: 3
        rate: 0.429
- exp_id: v4-taxei-rp-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.38469276
    eval_loss: null
    duration_minutes: 226.67
    token_acc: 0.92487562
    train_samples_per_second: 3.185
    peak_memory_gib: 30.68
- exp_id: v4-taxei-rp-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.3847
    token_acc: 0.9065
    duration_min: 231.07
    peak_memory_gib: 30.37
    train_samples_per_second: 3.124
- exp_id: v4-taxei-rp-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.38524182
    eval_loss: null
    duration_minutes: 226.5
    token_acc: 0.91372913
    train_samples_per_second: 3.187
    peak_memory_gib: 30.66
- exp_id: v4-taxei-rp-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.38530399
    eval_loss: null
    duration_minutes: 226.3
    token_acc: 0.91761223
    train_samples_per_second: 3.19
    peak_memory_gib: 30.17
- exp_id: llama31-taxei-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.3366
    token_acc: 0.9357
    train_steps: 3387
    train_duration_s: 7782
- exp_id: llama31-random-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.3366
    token_acc: 0.9364
    train_steps: 3387
    train_duration_s: 7622
- exp_id: v4-taxei-rp-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.3855
    token_acc: 0.9103
    duration_minutes: 226.6
    peak_memory_gib: 30.25
    train_samples_per_second: 3.185
- exp_id: eval-rp-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.574
    detection_rate: 0
    episodes: 47
    recovered: 27
- exp_id: eval-rp-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.489
    detection_rate: 0
    episodes: 47
    recovered: 23
- exp_id: eval-rp-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.468
    detection_rate: 0
    episodes: 47
    recovered: 22
- exp_id: llama31-vanilla-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.40025
    token_acc: 0.9067
    train_steps: 1635
    train_duration_s: 4157
- exp_id: eval-rp-s42
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.383
    recovery_count: 18/47
    C1_context_truncation: 0.5
    C4_observation_masking: 0.273
    P1_step_order_swap: 0.5
    P2_sub_goal_deletion: 0.25
    detection_rate: 0
- exp_id: llama31-vanilla-s42-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.745
    recovery_count: 35/47
    detection_rate: 0.213
    C1_context_truncation: 0.75
    C4_observation_masking: 0.727
    P1_step_order_swap: 0.75
    P2_sub_goal_deletion: 0.75
- exp_id: recovery-vanilla-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.66
    recovery_count: 31/47
    detection_rate: 0
    C1_context_truncation: 0.667
    C4_observation_masking: 0.545
    P1_step_order_swap: 0.667
    P2_sub_goal_deletion: 0.75
- exp_id: recovery-vanilla-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.745
    recovery_count: 35/47
    detection_rate: 0
    C1_context_truncation: 0.75
    C4_observation_masking: 0.727
    P1_step_order_swap: 0.75
    P2_sub_goal_deletion: 0.75
- exp_id: llama31-taxei-s42-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.745
    recovery_count: 35/47
    detection_rate: 0.298
    C1_context_truncation: 0.833
    C4_observation_masking: 0.727
    P1_step_order_swap: 0.583
    P2_sub_goal_deletion: 0.833
    C1_detection: 0.167
    C4_detection: 0.364
    P1_detection: 0.25
    P2_detection: 0.417
- exp_id: llama31-random-s42-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.766
    recovery_count: 36/47
    detection_rate: 0.298
    C1_context_truncation: 0.667
    C4_observation_masking: 0.727
    P1_step_order_swap: 0.917
    P2_sub_goal_deletion: 0.75
    C1_detection: 0.417
    C4_detection: 0.364
    P1_detection: 0.333
    P2_detection: 0.083
- exp_id: llama31-vanilla-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_train_loss: 0.398
    epoch1_loss: 0.481
    epoch2_loss: 0.362
    epoch3_loss: 0.273
    final_token_acc: 0.909
    train_runtime_sec: 4158.6
- exp_id: llama31-taxei-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_train_loss: 0.32
    final_token_acc: 0.88
    train_steps: 3387
    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/output/llama31-taxei-s0/v1-20260516-181826/checkpoint-3387
- exp_id: llama31-random-s0
  name: ''
  status: DONE
  conclusion: success
  metrics:
    final_train_loss: 0.3368
    epoch1_loss: 0.452
    epoch2_loss: 0.238
    epoch3_loss: 0.134
    final_token_acc: 0.9357
    train_runtime_sec: 7622
    train_steps: 3387
    peak_memory_gib: 30.74
    checkpoint_path: /root/autodl-tmp/tax_error_inject_agent/output/llama31-random-s0/v0-20260516-171608/checkpoint-3387
- exp_id: recovery-taxei-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.617
    recovery_count: 29/47
    detection_rate: 0
    C1_context_truncation: 0.75
    C4_observation_masking: 0.636
    P1_step_order_swap: 0.583
    P2_sub_goal_deletion: 0.5
- exp_id: eval-rp-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.596
    recovery_count: 28/47
    detection_rate: 0
- exp_id: llama31-vanilla-s0-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.745
    recovery_count: 35/47
    detection_rate: 0.277
    eval_type: injected
    eval_script: injected_eval.py
    output_file: eval_results/llama31_vanilla_s0_injected.json
    C1_context_truncation:
      recovery: 0.667
      detection: 0.167
    C4_observation_masking:
      recovery: 0.727
      detection: 0.364
    P1_step_order_swap:
      recovery: 0.917
      detection: 0.333
    P2_sub_goal_deletion:
      recovery: 0.667
      detection: 0.25
- exp_id: llama31-random-s42-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.766
    eval_type: clean
    eval_script: eval/recovery.py
    total_episodes: 47
    output_file: eval_results/llama31_random_s42_clean.json
- exp_id: recovery-taxei-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.574
    detection_rate: 0
    total_episodes: 47
- exp_id: llama31-random-s0-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.745
    detection_rate: 0.255
    success_rate: 0.745
    total_episodes: 47
    by_operator:
      C1_context_truncation:
        total: 12
        recovered: 10
        detected: 1
        recovery_rate: 0.833
        detection_rate: 0.083
      C4_observation_masking:
        total: 11
        recovered: 8
        detected: 4
        recovery_rate: 0.727
        detection_rate: 0.364
      P1_step_order_swap:
        total: 12
        recovered: 8
        detected: 4
        recovery_rate: 0.667
        detection_rate: 0.333
      P2_sub_goal_deletion:
        total: 12
        recovered: 9
        detected: 3
        recovery_rate: 0.75
        detection_rate: 0.25
- exp_id: llama31-vanilla-s42-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.723
    eval_type: clean
    eval_script: eval/recovery.py
    total_episodes: 47
    output_file: eval_results/llama31_vanilla_s42_clean.json
- exp_id: llama31-vanilla-s0-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.723
    eval_type: clean
    eval_script: eval/recovery.py
    total_episodes: 47
    output_file: eval_results/llama31_vanilla_s0_clean.json
- exp_id: llama31-taxei-s0-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.745
    success_rate: 0.745
    total_episodes: 47
- exp_id: llama31-vanilla-s123
  name: ''
  status: DONE
  conclusion: success
  metrics:
    train_loss: 0.4
    final_loss: 0.254
    token_acc: 0.894
    steps: 1635
    epochs: 3
    runtime_seconds: 4234
    memory_gib: 29.85
- exp_id: llama31-taxei-s123
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: llama31-random-s123
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: llama31-taxei-s0-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.766
    total_episodes: 47
- exp_id: llama31-taxei-s42-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.766
    total_episodes: 47
    eval_type: clean
    eval_script: eval/recovery.py
    output_file: eval_results/llama31_taxei_s42_clean.json
    by_task_type:
      look_at_obj_in_light: 1
      pick_and_place_simple: 0.625
      pick_clean_then_place_in_recep: 0.636
      pick_cool_then_place_in_recep: 0.714
      pick_heat_then_place_in_recep: 0.875
      pick_two_obj_and_place: 0.857
- exp_id: llama31-random-s0-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.745
    total_episodes: 47
    eval_type: clean
    eval_script: eval/recovery.py
    output_file: eval_results/llama31_random_s0_clean.json
    by_task_type:
      look_at_obj_in_light: 0.667
      pick_and_place_simple: 0.625
      pick_clean_then_place_in_recep: 0.636
      pick_cool_then_place_in_recep: 0.571
      pick_heat_then_place_in_recep: 1
      pick_two_obj_and_place: 1
- exp_id: llama31-vanilla-s123-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.723
    total_episodes: 47
    eval_type: clean
    eval_script: eval/recovery.py
    output_file: eval_results/llama31_vanilla_s123_clean.json
    by_task_type:
      look_at_obj_in_light: 0.833
      pick_and_place_simple: 0.625
      pick_clean_then_place_in_recep: 0.545
      pick_cool_then_place_in_recep: 0.571
      pick_heat_then_place_in_recep: 1
      pick_two_obj_and_place: 0.857
- exp_id: recovery-random-s1
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.511
    detection_rate: 0
    total_episodes: 47
- exp_id: recovery-random-s7
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.532
    detection_rate: 0
    total_episodes: 47
- exp_id: eval-llama31-taxei-s42-clean
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: eval-llama31-random-s0-clean
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: llama31-vanilla-s123-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.702
    detection_rate: 0.213
    total_episodes: 47
- exp_id: llama31-taxei-s123-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.596
    detection_rate: 0.362
    success_rate: 0.596
    total_episodes: 47
- exp_id: llama31-taxei-s123-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.617
    total_episodes: 47
    eval_type: clean
    by_task_type:
      look_at_obj_in_light: 0.667
      pick_and_place_simple: 0.375
      pick_clean_then_place_in_recep: 0.455
      pick_cool_then_place_in_recep: 0.571
      pick_heat_then_place_in_recep: 0.875
      pick_two_obj_and_place: 0.857
- exp_id: llama31-random-s123-clean
  name: ''
  status: DONE
  conclusion: success
  metrics:
    success_rate: 0.766
    total_episodes: 47
    eval_type: clean
    eval_script: eval/recovery.py
    output_file: eval_results/llama31_random_s123_clean.json
    by_task_type:
      look_at_obj_in_light: 1
      pick_and_place_simple: 0.625
      pick_clean_then_place_in_recep: 0.636
      pick_cool_then_place_in_recep: 0.571
      pick_heat_then_place_in_recep: 0.875
      pick_two_obj_and_place: 1
- exp_id: llama31-random-s123-eval
  name: ''
  status: DONE
  conclusion: success
  metrics:
    recovery_rate: 0.787
    detection_rate: 0.255
    total_episodes: 47
    by_operator:
      C1_context_truncation:
        recovered: 10/12
        rate: 0.833
        det_rate: 0.083
      C4_observation_masking:
        recovered: 8/11
        rate: 0.727
        det_rate: 0.182
      P1_step_order_swap:
        recovered: 10/12
        rate: 0.833
        det_rate: 0.417
      P2_sub_goal_deletion:
        recovered: 9/12
        rate: 0.75
        det_rate: 0.333

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
  "promptId": "ec6f37c9-a655-492b-ba31-93aa505ea49c",
  "type": "user",
  "uuid": "c02f4f2b-f795-4378-b12b-d05d79bcaa8e",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-16T15:39:47.975Z_

```json
{
  "parentUuid": "c02f4f2b-f795-4378-b12b-d05d79bcaa8e",
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
  "uuid": "04dc2359-9a4f-4272-ae60-b543c2a57017",
  "timestamp": "2026-05-16T15:39:47.975Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-16T15:39:47.975Z_

```json
{
  "parentUuid": "04dc2359-9a4f-4272-ae60-b543c2a57017",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "f942bad4-088d-4275-8aef-1ffc345b1600",
  "timestamp": "2026-05-16T15:39:47.975Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-16T15:39:47.975Z_

```json
{
  "parentUuid": "f942bad4-088d-4275-8aef-1ffc345b1600",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "43af3567-afa0-4d0a-84a1-71c92fce1549",
  "timestamp": "2026-05-16T15:39:47.975Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "43af3567-afa0-4d0a-84a1-71c92fce1549",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier dream scenarios for TaxEI cross-model validation",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2"
}
```

---

### Assistant

_source line 9 · 2026-05-16T15:41:13.532Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research data carefully to define three tiers (best/median/worst) for a Dream simulation of this paper targeting EMNLP 2026 Findings.

The core paper is about: structured error injection (TaxEI) destabilizing embodied planning agent training across model architectures, while random injection remains stable. The paper is a negative result paper with cross-model validation.

Key data points I have:
- Qwen3-8B (5-seed): Vanilla 67.3±4.7, TaxEI 58.3±6.5, Random 58.3±8.7


- LLaMA-3.1-8B (3-seed): Vanilla 73.1±2.5, TaxEI 69.5±8.6, Random 76.6±2.1
- TaxEI-RP (4-seed): 47.9±7.8
- Dose-response curve shows non-monotonic behavior with a nadir at 25%
- Cross-model validation confirms TaxEI's instability pattern, particularly evident in LLaMA where the standard deviation jumps to 8.6 compared to Random's 2.1
- Detection rates vary significantly across models: 0% on Qwen but 21-36% on LLaMA, suggesting model-dependent sensitivity to structured errors

The paper's central argument is that error injection actually hurts performance in embodied planning tasks, with taxonomy-based labeling providing no meaningful benefit. The core findings show generalization breaks down catastrophically with certain random seeds, structured injection doesn't improve resilience, and detection capabilities are inconsistent across model families. Task structure appears to be the key boundary condition explaining why this approach diverges from prior work like PALADIN, and pairing recovery mechanisms with injection actively worsens outcomes. The best-case scenario would be if remaining experiments solidify this narrative around cross-model instability and task-structural constraints.

Now I'm thinking through what the median and worst outcomes look like. If some results get messier—say the recovery-paired injection shows less dramatic harm, or multi-seed variance muddies the resilience story—the paper still gets accepted but with more hedged claims. The worst case would be if new data actually contradicts the instability hypothesis, like additional LLaMA runs showing TaxEI is more stable than expected, which would force a significant reframing of the core argument.

I'm tracking the key metrics that will determine which scenario plays out: the TaxEI-Vanilla performance gap is already locked in at -9 percentage points across Qwen's five seeds, but the cross-model stability story hinges on comparing standard deviation patterns between structured and random injection approaches. Looking at the registry more carefully, I see that TaxEI-RP actually has all five seeds completed—s42, s0, s1, s123, and s7—with s7 showing 59.6% recovery rate. This means I need to recalculate the mean across all five seeds rather than just the four originally listed.

Now I'm checking the recovery results across both Vanilla and TaxEI variants. The registry shows multiple completed evaluations for each method across different seeds, and I'm tallying up which ones are done versus still running to get a full picture of the progress. Looking at the complete random recovery results, all 15 recovery evals appear to be finished. Computing the 5-seed means across vanilla, TaxEI, and random recovery approaches gives me 67.3%, 57.4%, and 57.9% respectively—vanilla recovery is notably outperforming the other two methods.

The recovery scores match almost perfectly with their clean counterparts, which strongly validates the resilience hypothesis. Now I'm thinking through what could still derail this paper: the narrative might not land with reviewers, the small sample size with Bonferroni correction could be seen as a fundamental limitation, and the cross-model generalization story with LLaMA needs to hold up under scrutiny.

Let me map out the three possible outcomes. In the best case, reviewers see the structured-versus-random divergence as a genuine insight and appreciate the empirical rigor despite the statistical constraints—that gets us to acceptance. More likely, they acknowledge the thoroughness but question whether the findings are surprising enough or whether n=5 is too limiting, pushing for a reframing that emphasizes the core distinction. In the worst case, they dismiss it as an obvious negative result that doesn't warrant publication.

The key variable here is really just how reviewers perceive the novelty and framing, since most of the experiments are already done. The recovery results are in—the 5-seed mean sits around 50.2%, which is solidly below TaxEI—so there's not much left to change the empirical picture.

Let me organize the tiers around what we can actually claim with the current data. I'll use EMNLP Findings acceptance probability, Cohen's d for the main comparison, how well the LLaMA replication holds up, and expected reviewer scores to differentiate between scenarios. Since the experiments are mostly complete, the uncertainty really comes down to how the story lands with reviewers and what additional analyses might strengthen the claims.

The best case is that the 5-seed TaxEI-RP results confirm the instability pattern, the recovery data demonstrates resilience, and the structured-versus-random divergence across models becomes the compelling novel finding. The median scenario has solid data but reviewers push back for more validation—additional seeds, broader model coverage, ToolBench comparisons—and we adjust our claims accordingly. Worst case, reviewers reject the framing entirely and we need to fundamentally restructure the narrative.

Looking at the actual recovery numbers, the match between clean and recovery rates is remarkably tight: Vanilla shows perfect alignment at 67.3%, TaxEI has less than a point gap between 58.3% and 57.4%, and Random is nearly identical at 58.3% versus 57.9%. This consistency is actually quite strong.

Now I'm defining the outcome scenarios in YAML format. The best case assumes the large effect size holds up despite marginal p-values, the cross-model story with Qwen and LLaMA is persuasive, and the structured-versus-random divergence reads as genuinely novel. The median case expects pushback on statistical significance and the 3-seed LLaMA sample size, requiring us to soften our claims and acknowledge the need for broader validation.

Wait, the user actually asked for ranges of key experimental metrics, not just narrative scenarios. Since most of the experiments are already complete, the ranges are pretty tight around what we've already measured. The real uncertainty now is how we frame and report these numbers in the final paper—whether they land as strong evidence or merely suggestive findings depending on how reviewers weigh the statistical concerns.

The key metrics that'll determine our tier are the TaxEI-to-baseline performance gap and its significance, the cross-model consistency measured by standard deviation ratios, the proportion of failure cases, effect sizes, and ultimately the reviewer's subjective judgment on novelty. Let me map out what ranges these metrics could plausibly fall into.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "43af3567-afa0-4d0a-84a1-71c92fce1549",
  "isSidechain": false,
  "requestId": "req_011Cb6VvNdFiSePsPJVn4dU4",
  "type": "assistant",
  "uuid": "9a4d288c-8223-44a0-8f05-64b7a70cbe3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EX55k21btVZPSjmEaFTveu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 41379,
      "cache_read_input_tokens": 11447,
      "output_tokens": 5598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 41379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5598,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 41379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 41379
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

_source line 10 · 2026-05-16T15:41:57.332Z_

```yaml
tiers:
  best:
    meaning: "Cross-model structured-vs-random divergence被认可为新贡献，大effect size胜过marginal p，Findings Accept"
    key_assumptions:
      - "Reviewers接受Cohen's d≥1.5作为evidence（即使Bonferroni-corrected NS）"
      - "3-seed LLaMA被视为sufficient cross-model validation（方向一致性 > 绝对power）"
      - "Structured-vs-random stability divergence被视为novel finding（非obvious negative result）"
      - "Dose-response 25条独立训练run被视为thorough empirical work"
      - "Recovery=Resilience distinction被认为是有价值的conceptual contribution"
      - "TaxEI-RP definitively ruling out recovery-pairing confound被视为strong experimental design"
    number_ranges:
      vanilla_vs_taxei_gap_pp: [8.0, 10.0]
      cohens_d_main: [1.4, 1.8]
      cross_model_taxei_sd_ratio: [3.5, 4.5]  # TaxEI SD / Random SD on LLaMA
      catastrophic_seed_fraction: [0.20, 0.33]  # 1/5 Qwen + 1/3 LLaMA
      taxei_rp_vs_vanilla_gap_pp: [17.0, 20.0]
      recovery_clean_rate_match_pp: [0.0, 2.0]  # |recovery - clean| 所有条件
      dose_response_nadir_depth_pp: [12.0, 15.0]  # 25% TaxEI vs Vanilla
      inverted_u_peak_gap_pp: [6.0, 8.0]  # TaxEI-Random gap at 25%
      reviewer_score_mean: [3.5, 4.0]  # /5 scale
    narrative_direction: "原始framing完全成立——'Structured error injection is fundamentally destabilizing for embodied planning across architectures'。论文贡献从negative result升级为positive finding about injection stability properties。重点：(1)跨模型SD ratio 4:1证明是structured patterns的内在属性；(2)dose-response inverted-U揭示conflicting signal mechanism；(3)recovery=resilience是对整个error-injection-for-recovery范式的conceptual challenge。无需调整claims强度。"

  median:
    meaning: "Core finding方向accepted但statistical rigor被challenge，claims需降级为'suggestive evidence'，Borderline Accept"
    key_assumptions:
      - "Reviewers要求Bonferroni correction后仍显著（当前无法满足，n=5 power=45%）"
      - "3-seed LLaMA被视为preliminary/suggestive（不足以claim 'cross-architecture'）"
      - "Novelty被部分质疑：'injecting noise hurts'被认为not surprising，但structured-vs-random差异有新意"
      - "Data volume confound (4358 vs 9029) 被标记为limitation但dose-response partially controls"
      - "至少一位reviewer认为ALFWorld 47-task太小需要second benchmark"
    number_ranges:
      vanilla_vs_taxei_gap_pp: [8.0, 10.0]  # 同best（数据不变）
      cohens_d_main: [1.4, 1.8]  # 同best
      cross_model_taxei_sd_ratio: [3.5, 4.5]  # 同best
      catastrophic_seed_fraction: [0.20, 0.33]
      taxei_rp_vs_vanilla_gap_pp: [17.0, 20.0]
      recovery_clean_rate_match_pp: [0.0, 2.0]
      dose_response_nadir_depth_pp: [12.0, 15.0]
      inverted_u_peak_gap_pp: [6.0, 8.0]
      reviewer_score_mean: [2.8, 3.2]
    narrative_direction: "Claims需要systematic降级：(1)'Cross-architecture'改为'preliminary cross-model evidence on two architectures'；(2)主finding改为'large effect size suggestive of harm, requiring larger N for confirmation'；(3)增加prominent limitations section承认power不足；(4)structured-vs-random divergence从'proves'改为'suggests'；(5)补充meta-analysis框架（PALADIN+EEF+TaxEI构成{positive/negative signal}×{tool-use/planning} 2×2）来增加conceptual novelty；(6)加入explicit power curve图showing n=9 threshold。论文仍可发Findings但tone从'definitive boundary condition'变为'empirical evidence toward boundary conditions'。"

  worst:
    meaning: "Core novelty被reject为obvious/underpowered，需要reframe核心贡献，但仍冲EMNLP Findings"
    key_assumptions:
      - "Multiple reviewers认为'error injection hurts embodied planning'是trivially expected"
      - "Bonferroni NS被用来dismiss所有statistical claims"
      - "Cross-model 3-seed被视为anecdotal（'one bad seed proves nothing'）"
      - "WebShop replication cancelled被标记为major missing validation"
      - "至少一位reviewer认为paper自相矛盾：claims需要≥5 seeds但只有3-seed LLaMA"
      - "TaxEI=Random=58.3%被读作'both equally useless'而非结构化差异发现"
    number_ranges:
      vanilla_vs_taxei_gap_pp: [8.0, 10.0]  # 数据不变
      cohens_d_main: [1.4, 1.8]  # 数据不变，但reviewers不care
      cross_model_taxei_sd_ratio: [3.5, 4.5]  # reviewers dismiss as n=3 noise
      catastrophic_seed_fraction: [0.20, 0.33]
      taxei_rp_vs_vanilla_gap_pp: [17.0, 20.0]
      recovery_clean_rate_match_pp: [0.0, 2.0]
      dose_response_nadir_depth_pp: [12.0, 15.0]
      inverted_u_peak_gap_pp: [6.0, 8.0]
      reviewer_score_mean: [2.3, 2.8]
    narrative_direction: "核心贡献需要彻底reframe（仍冲同一venue）。三个可行angle：\n(A) **Training Lottery角度**：从'error injection boundary conditions'转向'The Training Lottery: Why Single-Seed Agent Evaluations Are Unreliable'。核心贡献变为：25条独立训练run（5 doses × 5 seeds）证明within-condition variance (19-23pp) > between-condition variance (9pp)，embodied agent SFT结果由seed lottery主导而非method选择。Dose-response bimodality证据支撑。这是一个methodological warning paper而非domain-transfer paper。\n(B) **Resilience-vs-Recovery角度**：从injection harm转向'Do LLM Agents Actually Recover? Separating Resilience from Recovery in Embodied Planning'。核心贡献是recovery=clean rate across ALL conditions + 0% detection = 没有任何training regime能instill error awareness。这challenge整个error-recovery训练范式。\n(C) **Augmentation Stability角度**：从negative result转向'Structured vs Unstructured Data Augmentation Stability for LLM Agent Training'。核心：structured perturbation creates systematic bias that amplifies across seeds/models; unstructured noise averages out. 这是一个关于data augmentation design principles的contribution，不限于error injection。\n选择依赖reviewer feedback方向——如果'obvious negative result'是主要reject reason选(A)或(C)；如果'not novel enough'选(B)。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9a4d288c-8223-44a0-8f05-64b7a70cbe3a",
  "isSidechain": false,
  "requestId": "req_011Cb6VvNdFiSePsPJVn4dU4",
  "type": "assistant",
  "uuid": "3a4d2fe5-6df4-4624-9aa1-c8fb05f8c7be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EX55k21btVZPSjmEaFTveu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 41379,
      "cache_read_input_tokens": 11447,
      "output_tokens": 5598,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 41379,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 5598,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 41379,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 41379
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "3a4d2fe5-6df4-4624-9aa1-c8fb05f8c7be",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier dream scenarios for TaxEI cross-model validation",
  "sessionId": "edf5bdc9-4dac-4a8d-bf4b-3b22a834f9c2"
}
```

---
