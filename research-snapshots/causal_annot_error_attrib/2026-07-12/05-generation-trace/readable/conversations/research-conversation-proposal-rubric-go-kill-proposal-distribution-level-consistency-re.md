# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Distribution-Level Consistency Re

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/39e773b4-583e-4a07-b8a8-760547234e93.jsonl`
- **Structured JSON:** [`fa7527b3a8847a0c5b1e.json`](../../sessions/fa/fa7527b3a8847a0c5b1e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:31:19.476Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:31:19.476Z",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling\n\n## Core Problem\n\nRL-trained mathematical reasoning models achieve SOTA on clean benchmarks but suffer severe accuracy drops under trivial surface-form perturbations even after RL training: VAR-MATH (arXiv 2025) reports average declines of 47.9% (AMC23), 58.8% (AIME24), and 72.9% (AIME25) on RL-trained models under numerical substitution. GRPO's reward signal provides no gradient against surface-form-dependent reasoning — the policy is rewarded for correct answers regardless of whether it exploits superficial patterns or genuine mathematical structure.\n\n## Three-Level Framework for Consistency Enforcement in Math RL\n\nWe identify three progressively stronger levels of consistency enforcement:\n\n**Level 1 — Data-level**: Augmenting training with perturbed variants without explicit consistency signal (MathForge ICLR 2026; PrAg-PO arXiv 2026 with 13 prompt templates). TA-GRPO's ablation (arXiv 2601.22478) demonstrates this alone is insufficient: \"augmentation without pooling doesn't help.\"\n\n**Level 2 — Reward-level**: Pooling rewards across original and perturbed variants (TA-GRPO, arXiv 2601.22478). Provides implicit consistency through shared advantages but operates on sparse binary feedback (correct/incorrect). TA-GRPO achieves Pass@k gains (up to +9.84 on AMC12/AIME24) but has not been evaluated on any perturbation robustness benchmark (GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP). **Theoretical limitation**: consider two semantically equivalent problems x, x' where the policy solves x via memorized pattern-matching and x' via genuine derivation — both correct, so reward pooling assigns identical advantages, remaining blind to the fragile reasoning on x. This \"correct but inconsistent reasoning\" failure mode is invisible to reward-level signals.\n\n**Level 3 — Distribution-level** (this work): Explicitly minimizing JS-divergence between policy rollout distributions on original and perturbed problems. This provides continuous gradient signal over the entire reasoning trajectory, detecting and penalizing divergent reasoning processes even when both lead to correct answers. By enforcing reasoning structure invariance — that the model's reasoning process is determined by mathematical structure rather than surface form — this approach implicitly forces the kind of abstraction that AbstRaL (ICLR 2026) achieves explicitly, but through a regularization mechanism rather than a separate abstraction stage.\n\n## Research Landscape\n\n**Training-time math robustness**: AbstRaL (ICLR 2026, Apple) uses RL to train explicit abstraction before solving, limited to GSM-level. TA-GRPO (arXiv 2601.22478, Jan 2026) introduces transform-augmented reward pooling in GRPO with Pass@k improvements on competition math but no robustness evaluation. AIR (arXiv 2605.20994, May 2026) applies asymmetric anchor invariance regularization to GRPO primarily for safety alignment (with auxiliary math evaluation), using stop-gradient anchoring — appropriate when one prompt variant has more reliable feedback, but suboptimal for math perturbation pairs where both sides are symmetric and equally verifiable.\n\n**Contrastive learning in GRPO**: CLIPO (arXiv 2603.10101, Mar 2026) integrates InfoNCE over correct rollouts within GRPO, extracting invariant reasoning structures across different correct solution paths to the same problem. MCPO (arXiv 2605.25443, May 2026) extends cross-domain contrastive policy optimization. Both target same-problem cross-trajectory invariance (aligning different correct reasoning paths). Our cross-perturbation contrastive component targets a different invariance dimension: aligning representations across surface-form-different but semantically-identical problem pairs, directly enforcing perturbation robustness rather than obtaining it as a side effect.\n\n**GRPO variants**: DAPO, DR.GRPO, COPO, DRA-GRPO address stability/diversity/efficiency but none target perturbation invariance. DyJR (arXiv 2603.16157) uses JS-divergence in GRPO as diversity-preserving regularizer between current and historical policies, establishing JS-divergence viability in GRPO and demonstrating JS > Forward KL for this purpose. PrAg-PO (arXiv 2602.03190, Feb 2026) uses prompt templates as implicit regularization with no consistency loss.\n\n**Adjacent work**: GRPO-CARE (Jun 2026) adds consistency bonuses for multimodal video reasoning. CSR (Jan 2026) enforces causal consistency via operator perturbation in SFT, not RL. F²C (arXiv 2025) validates consistency training for NLP robustness (11.6% agreement recovery). BCT (arXiv 2025) validates consistency training for alignment (attack success 67.8% → 2.9%). Reward Under Attack (arXiv 2026) examines PRM robustness. MathForge (ICLR 2026) combines difficulty-weighted GRPO with reformulation (clean accuracy only).\n\n**Why JS-divergence over alternatives**: JS-divergence is chosen over KL-divergence for two reasons: (1) symmetry — perturbation pairs (x, x') have symmetric epistemic status (both equally verifiable), making asymmetric KL(P_x || P_x') arbitrary in direction; (2) boundedness — JS ∈ [0, ln2] while KL can diverge, providing more stable training gradients. DyJR's empirical finding that JS outperforms Forward KL in GRPO regularization provides additional support.\n\n## Proposed Approach\n\n**ConsistGRPO** augments GRPO with distribution-level consistency enforcement as its primary mechanism:\n\n**Primary: Policy-level JS-divergence consistency loss (L_consist).** For each problem x, generate a math-equivalence-preserving perturbation x'. Collect G rollouts from each: {τ₁,...,τ_G} ~ π_θ(·|x) and {τ'₁,...,τ'_G} ~ π_θ(·|x'). Compute sequence-level log-probabilities to form empirical rollout distributions P_x and P_x'. The consistency loss L_consist = JS(P_x || P_x') provides symmetric, continuous gradient toward invariance over the full reasoning process. Unlike TA-GRPO's reward pooling (which transmits only binary outcome signals and is blind to \"correct but inconsistent reasoning\"), L_consist directly penalizes divergent reasoning distributions even when both variants are answered correctly.\n\n**Secondary: Cross-perturbation contrastive loss (L_contrastive).** Extract representations via mean-pooling the last hidden layer, project through a 2-layer MLP head (discarded at inference). Positive pairs: representations from perturbation pair (x, x') rollouts. Negative pairs: in-batch representations from different problems. Loss: InfoNCE. This complements CLIPO's same-problem cross-trajectory contrastive learning (arXiv 2603.10101) with a different invariance dimension — cross-perturbation invariance — directly targeting the \"blind skill application\" failure identified by MATH-Perturb (arXiv 2025). This component is treated as optional; ablations will determine its marginal contribution beyond L_consist.\n\n**Combined objective**: L = L_GRPO + λ₁·L_consist + λ₂·L_contrastive.\n\n**Perturbation generation pipeline**: Adapt GSM-Symbolic/VAR-MATH generators for MATH/AMC/AIME, restricted to algebraic and arithmetic subtypes amenable to automated perturbation (numerical substitution, variable renaming). Apply SymPy-based validity filter verifying solvability and answer computability. For problem types where automated perturbation is unreliable (geometry, certain number theory), use LLM-generated perturbations with symbolic verification. Report perturbation success rates per problem category. Conduct pilot study on 100 MATH-500 problems to validate pipeline coverage before full-scale training.\n\n**Training**: Qwen3-8B (primary) and Qwen3-1.7B (scale validation) on MATH/AMC/AIME with on-the-fly perturbation generation.\n\n## Experimental Design\n\n**Baselines (8 methods):**\n| Method | Consistency Level | Key Feature |\n|--------|------------------|-------------|\n| Vanilla GRPO | None | Same data, no augmentation |\n| GRPO + Aug Only | Data | Same perturbations, no consistency/contrastive loss |\n| TA-GRPO (arXiv 2601.22478) | Reward | Transform-augmented reward pooling |\n| CLIPO (arXiv 2603.10101) | Representation | Same-problem cross-trajectory contrastive |\n| AbstRaL (ICLR 2026) | — | Abstraction-based (GSM-level; best-effort on MATH/AIME) |\n| DR.GRPO | — | GRPO variant for stability |\n| PrAg-PO (arXiv 2026) | Data | 13 prompt templates, implicit regularization |\n| FLOPs-matched GRPO | — | Vanilla GRPO with matched total compute (profiled, not preset) |\n\n**Evaluation benchmarks**: GSM-Symbolic (ICLR 2025), GSM-Plus (ACL 2024), VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM (May 2026) for robustness; MATH-500, AIME 2024/2025 for clean accuracy. Report absolute accuracy, robustness gap (clean − perturbed), and Pass@k (k=1, 8, 64).\n\n**Ablations (5 dimensions):**\n1. Component decomposition: GRPO → +Aug → +L_consist → +L_contrastive → Full (5-row table isolating each component)\n2. Perturbation type: numerical substitution only / variable renaming only / combined\n3. Hyperparameter sensitivity: λ₁, λ₂ weight sweep (5 values each); group size G effect on L_consist\n4. Training dynamics: clean vs. robustness accuracy learning curves; entropy trajectory (cf. PrAg-PO entropy collapse)\n5. Divergence metric comparison: JS-divergence vs. Forward KL vs. Reverse KL vs. Symmetric KL vs. AIR-style asymmetric stop-gradient\n\n**Consistency-diversity tradeoff analysis**: Track Pass@k curves across λ₁ values; report unique correct solution count per problem and pairwise rollout distance as diversity metrics; analyze whether stronger consistency constraints cause diversity collapse (cf. DyJR arXiv 2603.16157).\n\n**Compute fairness**: Profile actual FLOPs overhead of ConsistGRPO vs. vanilla GRPO before setting FLOPs-matched baseline. Report breakdown: rollout generation, JS-divergence computation, contrastive loss overhead. Report wall-clock time and total GPU-hours.\n\n**Scale validation**: Replicate core comparison (ConsistGRPO vs. vanilla GRPO vs. TA-GRPO vs. CLIPO) on Qwen3-1.7B.\n\n## Key References\n\n- GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025)\n- GSM-Plus: Comprehensive Benchmark for Evaluating Robustness of LLMs as Math Problem Solvers (ACL 2024, arXiv 2402.19255)\n- AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking (ICLR 2026)\n- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)\n- Prompt Augmentation Scales up GRPO Training on Math Reasoning (arXiv 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2025)\n- MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations (arXiv 2025)\n- PutnamGAP: Robustness of LLMs via Mathematically-Equivalent Transformation (arXiv 2025)\n- Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations (arXiv 2025)\n- Consistency Training Helps Stop Sycophancy and Jailbreaks (arXiv 2025)\n- Reward Under Attack: Robustness and Hackability of Process Reward Models (arXiv 2026)\n- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478, Jan 2026)\n- AIR: Towards Context-Invariant Safety Alignment for LLMs (arXiv 2605.20994, May 2026)\n- DyJR: Preserving Diversity in RL with Verifiable Rewards via JS-Divergence (arXiv 2603.16157, 2026)\n- CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (arXiv 2603.10101, Mar 2026)\n- MCPO: Harmony in Diversity — Multi-domain Contrastive Policy Optimization (arXiv 2605.25443, May 2026)"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:31:19.484Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:31:19.484Z",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-29T06:31:19.511Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling

## Core Problem

RL-trained mathematical reasoning models achieve SOTA on clean benchmarks but suffer severe accuracy drops under trivial surface-form perturbations even after RL training: VAR-MATH (arXiv 2025) reports average declines of 47.9% (AMC23), 58.8% (AIME24), and 72.9% (AIME25) on RL-trained models under numerical substitution. GRPO's reward signal provides no gradient against surface-form-dependent reasoning — the policy is rewarded for correct answers regardless of whether it exploits superficial patterns or genuine mathematical structure.

## Three-Level Framework for Consistency Enforcement in Math RL

We identify three progressively stronger levels of consistency enforcement:

**Level 1 — Data-level**: Augmenting training with perturbed variants without explicit consistency signal (MathForge ICLR 2026; PrAg-PO arXiv 2026 with 13 prompt templates). TA-GRPO's ablation (arXiv 2601.22478) demonstrates this alone is insufficient: "augmentation without pooling doesn't help."

**Level 2 — Reward-level**: Pooling rewards across original and perturbed variants (TA-GRPO, arXiv 2601.22478). Provides implicit consistency through shared advantages but operates on sparse binary feedback (correct/incorrect). TA-GRPO achieves Pass@k gains (up to +9.84 on AMC12/AIME24) but has not been evaluated on any perturbation robustness benchmark (GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP). **Theoretical limitation**: consider two semantically equivalent problems x, x' where the policy solves x via memorized pattern-matching and x' via genuine derivation — both correct, so reward pooling assigns identical advantages, remaining blind to the fragile reasoning on x. This "correct but inconsistent reasoning" failure mode is invisible to reward-level signals.

**Level 3 — Distribution-level** (this work): Explicitly minimizing JS-divergence between policy rollout distributions on original and perturbed problems. This provides continuous gradient signal over the entire reasoning trajectory, detecting and penalizing divergent reasoning processes even when both lead to correct answers. By enforcing reasoning structure invariance — that the model's reasoning process is determined by mathematical structure rather than surface form — this approach implicitly forces the kind of abstraction that AbstRaL (ICLR 2026) achieves explicitly, but through a regularization mechanism rather than a separate abstraction stage.

## Research Landscape

**Training-time math robustness**: AbstRaL (ICLR 2026, Apple) uses RL to train explicit abstraction before solving, limited to GSM-level. TA-GRPO (arXiv 2601.22478, Jan 2026) introduces transform-augmented reward pooling in GRPO with Pass@k improvements on competition math but no robustness evaluation. AIR (arXiv 2605.20994, May 2026) applies asymmetric anchor invariance regularization to GRPO primarily for safety alignment (with auxiliary math evaluation), using stop-gradient anchoring — appropriate when one prompt variant has more reliable feedback, but suboptimal for math perturbation pairs where both sides are symmetric and equally verifiable.

**Contrastive learning in GRPO**: CLIPO (arXiv 2603.10101, Mar 2026) integrates InfoNCE over correct rollouts within GRPO, extracting invariant reasoning structures across different correct solution paths to the same problem. MCPO (arXiv 2605.25443, May 2026) extends cross-domain contrastive policy optimization. Both target same-problem cross-trajectory invariance (aligning different correct reasoning paths). Our cross-perturbation contrastive component targets a different invariance dimension: aligning representations across surface-form-different but semantically-identical problem pairs, directly enforcing perturbation robustness rather than obtaining it as a side effect.

**GRPO variants**: DAPO, DR.GRPO, COPO, DRA-GRPO address stability/diversity/efficiency but none target perturbation invariance. DyJR (arXiv 2603.16157) uses JS-divergence in GRPO as diversity-preserving regularizer between current and historical policies, establishing JS-divergence viability in GRPO and demonstrating JS > Forward KL for this purpose. PrAg-PO (arXiv 2602.03190, Feb 2026) uses prompt templates as implicit regularization with no consistency loss.

**Adjacent work**: GRPO-CARE (Jun 2026) adds consistency bonuses for multimodal video reasoning. CSR (Jan 2026) enforces causal consistency via operator perturbation in SFT, not RL. F²C (arXiv 2025) validates consistency training for NLP robustness (11.6% agreement recovery). BCT (arXiv 2025) validates consistency training for alignment (attack success 67.8% → 2.9%). Reward Under Attack (arXiv 2026) examines PRM robustness. MathForge (ICLR 2026) combines difficulty-weighted GRPO with reformulation (clean accuracy only).

**Why JS-divergence over alternatives**: JS-divergence is chosen over KL-divergence for two reasons: (1) symmetry — perturbation pairs (x, x') have symmetric epistemic status (both equally verifiable), making asymmetric KL(P_x || P_x') arbitrary in direction; (2) boundedness — JS ∈ [0, ln2] while KL can diverge, providing more stable training gradients. DyJR's empirical finding that JS outperforms Forward KL in GRPO regularization provides additional support.

## Proposed Approach

**ConsistGRPO** augments GRPO with distribution-level consistency enforcement as its primary mechanism:

**Primary: Policy-level JS-divergence consistency loss (L_consist).** For each problem x, generate a math-equivalence-preserving perturbation x'. Collect G rollouts from each: {τ₁,...,τ_G} ~ π_θ(·|x) and {τ'₁,...,τ'_G} ~ π_θ(·|x'). Compute sequence-level log-probabilities to form empirical rollout distributions P_x and P_x'. The consistency loss L_consist = JS(P_x || P_x') provides symmetric, continuous gradient toward invariance over the full reasoning process. Unlike TA-GRPO's reward pooling (which transmits only binary outcome signals and is blind to "correct but inconsistent reasoning"), L_consist directly penalizes divergent reasoning distributions even when both variants are answered correctly.

**Secondary: Cross-perturbation contrastive loss (L_contrastive).** Extract representations via mean-pooling the last hidden layer, project through a 2-layer MLP head (discarded at inference). Positive pairs: representations from perturbation pair (x, x') rollouts. Negative pairs: in-batch representations from different problems. Loss: InfoNCE. This complements CLIPO's same-problem cross-trajectory contrastive learning (arXiv 2603.10101) with a different invariance dimension — cross-perturbation invariance — directly targeting the "blind skill application" failure identified by MATH-Perturb (arXiv 2025). This component is treated as optional; ablations will determine its marginal contribution beyond L_consist.

**Combined objective**: L = L_GRPO + λ₁·L_consist + λ₂·L_contrastive.

**Perturbation generation pipeline**: Adapt GSM-Symbolic/VAR-MATH generators for MATH/AMC/AIME, restricted to algebraic and arithmetic subtypes amenable to automated perturbation (numerical substitution, variable renaming). Apply SymPy-based validity filter verifying solvability and answer computability. For problem types where automated perturbation is unreliable (geometry, certain number theory), use LLM-generated perturbations with symbolic verification. Report perturbation success rates per problem category. Conduct pilot study on 100 MATH-500 problems to validate pipeline coverage before full-scale training.

**Training**: Qwen3-8B (primary) and Qwen3-1.7B (scale validation) on MATH/AMC/AIME with on-the-fly perturbation generation.

## Experimental Design

**Baselines (8 methods):**
| Method | Consistency Level | Key Feature |
|--------|------------------|-------------|
| Vanilla GRPO | None | Same data, no augmentation |
| GRPO + Aug Only | Data | Same perturbations, no consistency/contrastive loss |
| TA-GRPO (arXiv 2601.22478) | Reward | Transform-augmented reward pooling |
| CLIPO (arXiv 2603.10101) | Representation | Same-problem cross-trajectory contrastive |
| AbstRaL (ICLR 2026) | — | Abstraction-based (GSM-level; best-effort on MATH/AIME) |
| DR.GRPO | — | GRPO variant for stability |
| PrAg-PO (arXiv 2026) | Data | 13 prompt templates, implicit regularization |
| FLOPs-matched GRPO | — | Vanilla GRPO with matched total compute (profiled, not preset) |

**Evaluation benchmarks**: GSM-Symbolic (ICLR 2025), GSM-Plus (ACL 2024), VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM (May 2026) for robustness; MATH-500, AIME 2024/2025 for clean accuracy. Report absolute accuracy, robustness gap (clean − perturbed), and Pass@k (k=1, 8, 64).

**Ablations (5 dimensions):**
1. Component decomposition: GRPO → +Aug → +L_consist → +L_contrastive → Full (5-row table isolating each component)
2. Perturbation type: numerical substitution only / variable renaming only / combined
3. Hyperparameter sensitivity: λ₁, λ₂ weight sweep (5 values each); group size G effect on L_consist
4. Training dynamics: clean vs. robustness accuracy learning curves; entropy trajectory (cf. PrAg-PO entropy collapse)
5. Divergence metric comparison: JS-divergence vs. Forward KL vs. Reverse KL vs. Symmetric KL vs. AIR-style asymmetric stop-gradient

**Consistency-diversity tradeoff analysis**: Track Pass@k curves across λ₁ values; report unique correct solution count per problem and pairwise rollout distance as diversity metrics; analyze whether stronger consistency constraints cause diversity collapse (cf. DyJR arXiv 2603.16157).

**Compute fairness**: Profile actual FLOPs overhead of ConsistGRPO vs. vanilla GRPO before setting FLOPs-matched baseline. Report breakdown: rollout generation, JS-divergence computation, contrastive loss overhead. Report wall-clock time and total GPU-hours.

**Scale validation**: Replicate core comparison (ConsistGRPO vs. vanilla GRPO vs. TA-GRPO vs. CLIPO) on Qwen3-1.7B.

## Key References

- GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025)
- GSM-Plus: Comprehensive Benchmark for Evaluating Robustness of LLMs as Math Problem Solvers (ACL 2024, arXiv 2402.19255)
- AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking (ICLR 2026)
- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)
- Prompt Augmentation Scales up GRPO Training on Math Reasoning (arXiv 2026)
- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2025)
- MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations (arXiv 2025)
- PutnamGAP: Robustness of LLMs via Mathematically-Equivalent Transformation (arXiv 2025)
- Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations (arXiv 2025)
- Consistency Training Helps Stop Sycophancy and Jailbreaks (arXiv 2025)
- Reward Under Attack: Robustness and Hackability of Process Reward Models (arXiv 2026)
- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478, Jan 2026)
- AIR: Towards Context-Invariant Safety Alignment for LLMs (arXiv 2605.20994, May 2026)
- DyJR: Preserving Diversity in RL with Verifiable Rewards via JS-Divergence (arXiv 2603.16157, 2026)
- CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (arXiv 2603.10101, Mar 2026)
- MCPO: Harmony in Diversity — Multi-domain Contrastive Policy Optimization (arXiv 2605.25443, May 2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "50084fb3-5e79-4c49-badf-f03d24d1fc81",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:31:19.510Z_

```json
{
  "parentUuid": "50084fb3-5e79-4c49-badf-f03d24d1fc81",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "f57ac70d-5656-4ab1-aed1-a72aa5badde9",
  "timestamp": "2026-05-29T06:31:19.510Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:31:19.510Z_

```json
{
  "parentUuid": "f57ac70d-5656-4ab1-aed1-a72aa5badde9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5486ccb0-ebbd-489c-ad67-fdf7eb2d251b",
  "timestamp": "2026-05-29T06:31:19.510Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency for math RL robustness",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93"
}
```

---

### Assistant

_source line 7 · 2026-05-29T06:31:23.298Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. Let me first do the required web searches to understand the current landscape, then provide my assessment.

Let me search for the key topics and papers mentioned in this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5486ccb0-ebbd-489c-ad67-fdf7eb2d251b",
  "isSidechain": false,
  "requestId": "req_011CbWPcTJgNR4omk19LoYN7",
  "type": "assistant",
  "uuid": "ddd323aa-b351-484d-916c-6ff382a5fb47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y69JUGsEreijtJHzcEScc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7223,
      "cache_read_input_tokens": 11014,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7223
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

_source line 8 · 2026-05-29T06:31:24.463Z_

I'll start by conducting the required literature searches to properly assess this proposal's positioning in the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ddd323aa-b351-484d-916c-6ff382a5fb47",
  "isSidechain": false,
  "requestId": "req_011CbWPcTJgNR4omk19LoYN7",
  "type": "assistant",
  "uuid": "d0dbcff8-a881-4c3c-94ef-c66b4df4a12b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y69JUGsEreijtJHzcEScc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7223,
      "cache_read_input_tokens": 11014,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7223
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

_source line 9 · 2026-05-29T06:31:24.710Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HB9sUpaQMk73GR8HbEJCFp`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0dbcff8-a881-4c3c-94ef-c66b4df4a12b",
  "isSidechain": false,
  "requestId": "req_011CbWPcTJgNR4omk19LoYN7",
  "type": "assistant",
  "uuid": "7663745c-2e69-440c-8da2-85a39c1548d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017Y69JUGsEreijtJHzcEScc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7223,
      "cache_read_input_tokens": 11014,
      "output_tokens": 164,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7223,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 164,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 7223,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7223
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

_source line 10 · 2026-05-29T06:31:24.723Z_

<details><summary>↩ Tool result · `toolu_01HB9sUpaQMk73GR8HbEJCFp`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7663745c-2e69-440c-8da2-85a39c1548d3",
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "c494d847-6d47-413c-8792-cc1817478299",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "7663745c-2e69-440c-8da2-85a39c1548d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling  ## Core…",
  "leafUuid": "c494d847-6d47-413c-8792-cc1817478299",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency for math RL robustness",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93"
}
```

---

### Assistant

_source line 13 · 2026-05-29T06:31:28.649Z_

Now let me conduct the required searches in parallel to understand the research landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c494d847-6d47-413c-8792-cc1817478299",
  "isSidechain": false,
  "requestId": "req_011CbWPcqeMFqZ5uBZJZbBkd",
  "type": "assistant",
  "uuid": "abb14a79-8c51-499f-a434-1e239dd91fa6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHyigM2FiADgLWed7Dcmrt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 18237,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 18237,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 692
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

_source line 14 · 2026-05-29T06:31:29.308Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014erydpdMcVh7aqtqhDXq5m`</summary>

```json
{
  "query": "TA-GRPO transform augmented GRPO reward pooling math reasoning robustness 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "abb14a79-8c51-499f-a434-1e239dd91fa6",
  "isSidechain": false,
  "requestId": "req_011CbWPcqeMFqZ5uBZJZbBkd",
  "type": "assistant",
  "uuid": "4e004dd8-63b2-469a-9c80-803b06f33b09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BHyigM2FiADgLWed7Dcmrt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 692,
      "cache_read_input_tokens": 18237,
      "output_tokens": 91,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 692,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 91,
          "cache_read_input_tokens": 18237,
          "cache_creation_input_tokens": 692,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 692
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

_source line 15 · 2026-05-29T06:31:36.824Z_

<details><summary>↩ Tool result · `toolu_014erydpdMcVh7aqtqhDXq5m`</summary>

```text
Web search results for query: "TA-GRPO transform augmented GRPO reward pooling math reasoning robustness 2026"

Links: [{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"(PDF) Transform-Augmented GRPO Improves Pass@k","url":"https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/html/2505.09655v4"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/html/2602.03190v1"},{"title":"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/pdf/2601.03661"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models","url":"https://arxiv.org/pdf/2504.09696"}]

Based on the search results, here's what I found about TA-GRPO:

## TA-GRPO Overview

TA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.

## Problem it Addresses

Large language models trained via next-token prediction are fundamentally pattern-matchers sensitive to superficial phrasing variations. GRPO was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.

## How TA-GRPO Works

This pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies. TA-GRPO provides theoretical justification showing that it reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.

## Experimental Results

Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).

The paper was published in February 2026 on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e004dd8-63b2-469a-9c80-803b06f33b09",
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "35e9bbfe-2f51-4670-b23d-b5355f583d18",
  "toolUseResult": {
    "query": "TA-GRPO transform augmented GRPO reward pooling math reasoning robustness 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DJY7nYUf1PFvEyhaC7dLJN",
        "content": [
          {
            "title": "[2601.22478] Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/abs/2601.22478"
          },
          {
            "title": "(PDF) Transform-Augmented GRPO Improves Pass@k",
            "url": "https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/pdf/2601.22478"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2505.09655v4"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/html/2602.03190v1"
          },
          {
            "title": "AMIR-GRPO: Inducing Implicit Preference Signals into GRPO",
            "url": "https://arxiv.org/pdf/2601.03661"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          },
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2504.09696"
          }
        ]
      },
      "Based on the search results, here's what I found about TA-GRPO:\n\n## TA-GRPO Overview\n\nTA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question (via paraphrasing, variable renaming, and format changes) and computes advantages by pooling rewards across the entire group.\n\n## Problem it Addresses\n\nLarge language models trained via next-token prediction are fundamentally pattern-matchers sensitive to superficial phrasing variations. GRPO was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.\n\n## How TA-GRPO Works\n\nThis pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies. TA-GRPO provides theoretical justification showing that it reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.\n\n## Experimental Results\n\nExperiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).\n\nThe paper was published in February 2026 on arXiv."
    ],
    "durationSeconds": 7.511538153000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4e004dd8-63b2-469a-9c80-803b06f33b09",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-29T06:31:39.544Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XHCUv5YVeL6AG7ocQAGrJZ`</summary>

```json
{
  "query": "CLIPO contrastive learning policy optimization GRPO InfoNCE math reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35e9bbfe-2f51-4670-b23d-b5355f583d18",
  "isSidechain": false,
  "requestId": "req_011CbWPdj9wsvc2ox6XtFvXw",
  "type": "assistant",
  "uuid": "c90b727d-dc7d-4009-816c-a17a773d3605",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018nXAdbs6oMcnC299wHtxAv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 854,
      "cache_read_input_tokens": 18929,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 18929,
          "cache_creation_input_tokens": 854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 854
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

_source line 17 · 2026-05-29T06:31:47.866Z_

<details><summary>↩ Tool result · `toolu_01XHCUv5YVeL6AG7ocQAGrJZ`</summary>

```text
Web search results for query: "CLIPO contrastive learning policy optimization GRPO InfoNCE math reasoning 2026"

Links: [{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/pdf/2603.10101"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://www.researchgate.net/publication/401833359_CLIPO_Contrastive_Learning_in_Policy_Optimization_Generalizes_RLVR"},{"title":"GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub","url":"https://github.com/Qwen-Applications/CLIPO"},{"title":"Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models","url":"https://arxiv.org/html/2605.25443"},{"title":"Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://huggingface.co/papers/2603.10101"},{"title":"[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/abs/2603.10101"}]

Based on the search results, I found relevant information about CLIPO and the concepts you mentioned:

## CLIPO: Contrastive Learning in Policy Optimization

CLIPO (Contrastive Learning in Policy Optimization) introduces a lightweight contrastive head and an intra-group contrastive objective into RLVR-style policy optimization.

### How It Works

By aligning multiple successful reasoning trajectories and contrasting them against incorrect ones, the method extracts invariant reasoning structures shared by correct rollouts, yielding a dense contrastive reward that complements standard outcome-based verifiable rewards and improves robustness and generalization, especially under distribution shifts and hard mathematical reasoning benchmarks.

### Performance on Math Reasoning

GRPO+CLIPO achieves the highest overall average score of 63.26, consistently outperforming all baselines. Specifically, GRPO+CLIPO improves GSM8K-P1 and GSM8K-P2 by +1.48 and +3.36 points, respectively, and achieves the highest math-average score of 75.35.

### Loss Functions

InfoNCE samples a single correct response as the positive, and InfoNCE loss achieves the highest gains (+1.13) across three average scores on Track I.

The paper addresses a key limitation of RLVR-based approaches: RLVR solely relies on final answers as outcome rewards, neglecting the correctness of intermediate reasoning steps, and training on process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c90b727d-dc7d-4009-816c-a17a773d3605",
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "82ffc997-65b3-41bf-970f-c4e4c7590b85",
  "toolUseResult": {
    "query": "CLIPO contrastive learning policy optimization GRPO InfoNCE math reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HXKTcP9JJZqhjz9ipjAM5U",
        "content": [
          {
            "title": "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/pdf/2603.10101"
          },
          {
            "title": "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://www.researchgate.net/publication/401833359_CLIPO_Contrastive_Learning_in_Policy_Optimization_Generalizes_RLVR"
          },
          {
            "title": "GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub",
            "url": "https://github.com/Qwen-Applications/CLIPO"
          },
          {
            "title": "Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models",
            "url": "https://arxiv.org/html/2605.25443"
          },
          {
            "title": "Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://huggingface.co/papers/2603.10101"
          },
          {
            "title": "[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/abs/2603.10101"
          }
        ]
      },
      "Based on the search results, I found relevant information about CLIPO and the concepts you mentioned:\n\n## CLIPO: Contrastive Learning in Policy Optimization\n\nCLIPO (Contrastive Learning in Policy Optimization) introduces a lightweight contrastive head and an intra-group contrastive objective into RLVR-style policy optimization.\n\n### How It Works\n\nBy aligning multiple successful reasoning trajectories and contrasting them against incorrect ones, the method extracts invariant reasoning structures shared by correct rollouts, yielding a dense contrastive reward that complements standard outcome-based verifiable rewards and improves robustness and generalization, especially under distribution shifts and hard mathematical reasoning benchmarks.\n\n### Performance on Math Reasoning\n\nGRPO+CLIPO achieves the highest overall average score of 63.26, consistently outperforming all baselines. Specifically, GRPO+CLIPO improves GSM8K-P1 and GSM8K-P2 by +1.48 and +3.36 points, respectively, and achieves the highest math-average score of 75.35.\n\n### Loss Functions\n\nInfoNCE samples a single correct response as the positive, and InfoNCE loss achieves the highest gains (+1.13) across three average scores on Track I.\n\nThe paper addresses a key limitation of RLVR-based approaches: RLVR solely relies on final answers as outcome rewards, neglecting the correctness of intermediate reasoning steps, and training on process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying."
    ],
    "durationSeconds": 8.317163118,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c90b727d-dc7d-4009-816c-a17a773d3605",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-29T06:31:50.526Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014pNFKpzX8vK5tYSYd1Kfxa`</summary>

```json
{
  "query": "JS divergence KL divergence consistency regularization reinforcement learning LLM robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82ffc997-65b3-41bf-970f-c4e4c7590b85",
  "isSidechain": false,
  "requestId": "req_011CbWPeYMqjwnBzBfCAjgQ8",
  "type": "assistant",
  "uuid": "35f8eb57-37e1-4b5e-833c-580f5bf1063a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MraaXSYqCpUuatQyMRmVTW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 19783,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 800,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 19783,
          "cache_creation_input_tokens": 800,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 800
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

_source line 19 · 2026-05-29T06:31:58.136Z_

<details><summary>↩ Tool result · `toolu_014pNFKpzX8vK5tYSYd1Kfxa`</summary>

```text
Web search results for query: "JS divergence KL divergence consistency regularization reinforcement learning LLM robustness 2025 2026"

Links: [{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/html/2509.07430v1"},{"title":"KL-Regularized Reinforcement Learning","url":"https://www.emergentmind.com/topics/kl-regularized-reinforcement-learning"},{"title":"Reverse KL Regularization","url":"https://www.emergentmind.com/topics/reverse-kl-regularization"},{"title":"Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS","url":"https://www.arxiv.org/pdf/2512.21852"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/pdf/2509.07430"},{"title":"Off-Policy Reinforcement Learning RL with KL Divergence Yields Superior Reasoning in Large Language Models - MarkTechPost","url":"https://www.marktechpost.com/2025/06/01/off-policy-reinforcement-learning-rl-with-kl-divergence-yields-superior-reasoning-in-large-language-models/"},{"title":"Continual Learning with RL for LLMs","url":"https://cameronrwolfe.substack.com/p/rl-continual-learning"},{"title":"Your Policy Regularizer is Secretly an Adversary","url":"https://arxiv.org/pdf/2203.12592"}]

Based on the search results, here's what I found on these topics:

## Key Research Areas

**Divergence Choice in RL for LLMs:**
Recent work generalizes beyond KL divergence to f-divergences including Jensen-Shannon (JS) divergence and α-divergence, with experiments showing that mass-covering divergences like forward-KL and JS-divergence lead to improvements in both Pass@1 and Pass@k, while maintaining strong out-of-domain performance.

**Diversity Collapse Problem:**
Research on reinforcement learning with verifiable rewards identifies reverse-KL divergence as a primary cause of solution diversity collapse, with its mode-seeking nature suppressing Pass@k performance and exacerbating catastrophic forgetting.

**DPH-RL Framework:**
A novel framework reframes the role of KL divergence from a policy constraint to an active diversity-preserving mechanism, employing mass-covering f-divergences to serve as a rehearsal mechanism.

**KL Regularization in LLM Training:**
KL-regularized reinforcement learning explicitly regularizes policy using KL divergence with respect to a reference policy, and is used as a foundational component in recent advances across robotic control, transfer learning, RLHF, and large-scale LLM fine-tuning.

**Trade-offs in Regularization:**
Recent work discusses hybrid regularization schemes and adaptive penalty coefficients to balance exploitation and generalization, with research noting that reverse KL strongly concentrates on alignment at possible expense of output diversity.

These represent recent advances (2025-2026) in addressing robustness and diversity in LLM training through careful choice of divergence measures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35f8eb57-37e1-4b5e-833c-580f5bf1063a",
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "02b7033d-3ae1-450f-92e6-5088ea0674be",
  "toolUseResult": {
    "query": "JS divergence KL divergence consistency regularization reinforcement learning LLM robustness 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013SezVPznn1663cP7wXE3K4",
        "content": [
          {
            "title": "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward",
            "url": "https://arxiv.org/html/2509.07430v1"
          },
          {
            "title": "KL-Regularized Reinforcement Learning",
            "url": "https://www.emergentmind.com/topics/kl-regularized-reinforcement-learning"
          },
          {
            "title": "Reverse KL Regularization",
            "url": "https://www.emergentmind.com/topics/reverse-kl-regularization"
          },
          {
            "title": "Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS",
            "url": "https://www.arxiv.org/pdf/2512.21852"
          },
          {
            "title": "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward",
            "url": "https://arxiv.org/pdf/2509.07430"
          },
          {
            "title": "Off-Policy Reinforcement Learning RL with KL Divergence Yields Superior Reasoning in Large Language Models - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/06/01/off-policy-reinforcement-learning-rl-with-kl-divergence-yields-superior-reasoning-in-large-language-models/"
          },
          {
            "title": "Continual Learning with RL for LLMs",
            "url": "https://cameronrwolfe.substack.com/p/rl-continual-learning"
          },
          {
            "title": "Your Policy Regularizer is Secretly an Adversary",
            "url": "https://arxiv.org/pdf/2203.12592"
          }
        ]
      },
      "Based on the search results, here's what I found on these topics:\n\n## Key Research Areas\n\n**Divergence Choice in RL for LLMs:**\nRecent work generalizes beyond KL divergence to f-divergences including Jensen-Shannon (JS) divergence and α-divergence, with experiments showing that mass-covering divergences like forward-KL and JS-divergence lead to improvements in both Pass@1 and Pass@k, while maintaining strong out-of-domain performance.\n\n**Diversity Collapse Problem:**\nResearch on reinforcement learning with verifiable rewards identifies reverse-KL divergence as a primary cause of solution diversity collapse, with its mode-seeking nature suppressing Pass@k performance and exacerbating catastrophic forgetting.\n\n**DPH-RL Framework:**\nA novel framework reframes the role of KL divergence from a policy constraint to an active diversity-preserving mechanism, employing mass-covering f-divergences to serve as a rehearsal mechanism.\n\n**KL Regularization in LLM Training:**\nKL-regularized reinforcement learning explicitly regularizes policy using KL divergence with respect to a reference policy, and is used as a foundational component in recent advances across robotic control, transfer learning, RLHF, and large-scale LLM fine-tuning.\n\n**Trade-offs in Regularization:**\nRecent work discusses hybrid regularization schemes and adaptive penalty coefficients to balance exploitation and generalization, with research noting that reverse KL strongly concentrates on alignment at possible expense of output diversity.\n\nThese represent recent advances (2025-2026) in addressing robustness and diversity in LLM training through careful choice of divergence measures."
    ],
    "durationSeconds": 7.604406081999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "35f8eb57-37e1-4b5e-833c-580f5bf1063a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-29T06:32:00.718Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BqGuhh54YrG2hNHhMoLvG6`</summary>

```json
{
  "query": "AIR asymmetric invariance regularization GRPO safety alignment math 2026 arXiv 2605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02b7033d-3ae1-450f-92e6-5088ea0674be",
  "isSidechain": false,
  "requestId": "req_011CbWPfJThiXSnWweLLHz2S",
  "type": "assistant",
  "uuid": "9911618f-6b98-4c61-881c-ce48e21ca8e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WHyZQ9NPTdpTzUgya2HVoV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 915,
      "cache_read_input_tokens": 20583,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 915,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 20583,
          "cache_creation_input_tokens": 915,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 915
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

_source line 21 · 2026-05-29T06:32:07.231Z_

<details><summary>↩ Tool result · `toolu_01BqGuhh54YrG2hNHhMoLvG6`</summary>

```text
Web search results for query: "AIR asymmetric invariance regularization GRPO safety alignment math 2026 arXiv 2605"

Links: [{"title":"Towards Context-Invariant Safety Alignment for Large Language Models","url":"https://arxiv.org/html/2605.20994"},{"title":"[2605.20994] Towards Context-Invariant Safety Alignment for Large Language Models","url":"https://arxiv.org/abs/2605.20994"},{"title":"[2605.05750] RVPO: Risk-Sensitive Alignment via Variance Regularization","url":"https://arxiv.org/abs/2605.05750"},{"title":"SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization","url":"https://arxiv.org/html/2511.12982"},{"title":"Rethinking Invariance Regularization in Adversarial Training to Improve Robustness-Accuracy Trade-off","url":"https://arxiv.org/pdf/2402.14648"},{"title":"Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation","url":"https://arxiv.org/pdf/2602.05548"}]

Based on the search results, I found the paper you're looking for:

The paper addresses that preference-based post-training aligns LLMs with human intent, yet safety behavior often remains brittle. The authors propose Anchor Invariance Regularization (AIR), an asymmetric objective that anchors open-ended generation to verifiable constraints.

The work identifies that symmetric invariance regularization fails in safety alignment. AIR breaks the symmetry of standard invariance objectives by designating verifiable contexts as anchors, and regularizes open-ended generation to match the anchor reference via a stop-gradient target, ensuring the reliable anchor remains fixed.

AIR is practically instantiated by integrating it with group-based preference optimization (GRPO). Across Safety, Moral Reasoning, and Math, AIR improves context invariance, boosting in-distribution group accuracy by 12.71% and out-of-distribution consistency by 33.49%.

The paper is available at arXiv:2605.20994 and was submitted on May 20, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9911618f-6b98-4c61-881c-ce48e21ca8e2",
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "b4444a42-eadb-4679-b11c-23e16e3f4e3b",
  "toolUseResult": {
    "query": "AIR asymmetric invariance regularization GRPO safety alignment math 2026 arXiv 2605",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qtx1uiDtkzZcAfBRgs9Su6",
        "content": [
          {
            "title": "Towards Context-Invariant Safety Alignment for Large Language Models",
            "url": "https://arxiv.org/html/2605.20994"
          },
          {
            "title": "[2605.20994] Towards Context-Invariant Safety Alignment for Large Language Models",
            "url": "https://arxiv.org/abs/2605.20994"
          },
          {
            "title": "[2605.05750] RVPO: Risk-Sensitive Alignment via Variance Regularization",
            "url": "https://arxiv.org/abs/2605.05750"
          },
          {
            "title": "SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization",
            "url": "https://arxiv.org/html/2511.12982"
          },
          {
            "title": "Rethinking Invariance Regularization in Adversarial Training to Improve Robustness-Accuracy Trade-off",
            "url": "https://arxiv.org/pdf/2402.14648"
          },
          {
            "title": "Unveiling Implicit Advantage Symmetry: Why GRPO Struggles with Exploration and Difficulty Adaptation",
            "url": "https://arxiv.org/pdf/2602.05548"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper addresses that preference-based post-training aligns LLMs with human intent, yet safety behavior often remains brittle. The authors propose Anchor Invariance Regularization (AIR), an asymmetric objective that anchors open-ended generation to verifiable constraints.\n\nThe work identifies that symmetric invariance regularization fails in safety alignment. AIR breaks the symmetry of standard invariance objectives by designating verifiable contexts as anchors, and regularizes open-ended generation to match the anchor reference via a stop-gradient target, ensuring the reliable anchor remains fixed.\n\nAIR is practically instantiated by integrating it with group-based preference optimization (GRPO). Across Safety, Moral Reasoning, and Math, AIR improves context invariance, boosting in-distribution group accuracy by 12.71% and out-of-distribution consistency by 33.49%.\n\nThe paper is available at arXiv:2605.20994 and was submitted on May 20, 2026."
    ],
    "durationSeconds": 6.507917816000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9911618f-6b98-4c61-881c-ce48e21ca8e2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-29T06:32:09.777Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011C169JWVgU3ahzNnXejXTG`</summary>

```json
{
  "query": "VAR-MATH MATH-Perturb GSM-Symbolic perturbation robustness math LLM benchmark 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4444a42-eadb-4679-b11c-23e16e3f4e3b",
  "isSidechain": false,
  "requestId": "req_011CbWPfy6QDi4fQ1XfPjT7s",
  "type": "assistant",
  "uuid": "3932a465-32c9-495f-a7c8-39f11cfe0127",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQM9CNqKmFG9eRYikNtkn9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 21498,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 647,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 21498,
          "cache_creation_input_tokens": 647,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 647
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

_source line 23 · 2026-05-29T06:32:19.072Z_

<details><summary>↩ Tool result · `toolu_011C169JWVgU3ahzNnXejXTG`</summary>

```text
Web search results for query: "VAR-MATH MATH-Perturb GSM-Symbolic perturbation robustness math LLM benchmark 2025 2026"

Links: [{"title":"MathRobust-LV: Evaluation of Large Language Models’ Robustness to Linguistic Variations in Mathematical Reasoning","url":"https://arxiv.org/html/2510.06430v1"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/html/2402.19255v1"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2402.19255"},{"title":"VarBench: Robust Language Model Benchmarking Through Dynamic Variable Perturbation","url":"https://arxiv.org/html/2406.17681"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/html/2502.06453v2"},{"title":"Evaluating Robustness of LLMs to Numerical Variations in ...","url":"https://aclanthology.org/2025.insights-1.16.pdf"}]

Based on the search results, I found information about the benchmarks you mentioned:

## MATH-Perturb

MATH-Perturb is a benchmark that extends MATH with controlled surface-form variations, showing that even minor modifications can cause substantial accuracy drops across a wide range of models. The benchmark includes MATH-P-Simple and MATH-P-Hard, each consisting of 279 perturbed math problems that originate from the level-5 (hardest) problems of the MATH dataset, curated by 12 graduate-level experts with rigorous rubrics and cross-checking workflow for quality control.

Recent benchmarking of 18 LLMs shows that all models, including o1-mini and gemini-2.0-flash-thinking, suffer significant performance drops (10%-25%) on MATH-P-Hard.

## GSM-Symbolic

GSM-Symbolic, introduced by Apple researchers, is a benchmark that perturbs math problems by modifying surface features such as names, numbers, and intermediate steps, showing that LLMs are highly sensitive to symbolic or structural shifts.

## VarBench (Related)

Another related benchmark is VarBench, which introduces a variable perturbation process for converting existing benchmarks into forms that are robust to contamination by creating delexicalized questions along with solution functions.

These benchmarks collectively reveal that while LLMs show strong average-case performance on mathematical tasks, they lack robustness when problems are reformulated or perturbed in various ways.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3932a465-32c9-495f-a7c8-39f11cfe0127",
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "20b05094-8458-48ea-bf2e-876ed4066fb7",
  "toolUseResult": {
    "query": "VAR-MATH MATH-Perturb GSM-Symbolic perturbation robustness math LLM benchmark 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RJQHq6RGfNuEWHT2ptrMEB",
        "content": [
          {
            "title": "MathRobust-LV: Evaluation of Large Language Models’ Robustness to Linguistic Variations in Mathematical Reasoning",
            "url": "https://arxiv.org/html/2510.06430v1"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"
          },
          {
            "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers",
            "url": "https://arxiv.org/html/2402.19255v1"
          },
          {
            "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers",
            "url": "https://arxiv.org/pdf/2402.19255"
          },
          {
            "title": "VarBench: Robust Language Model Benchmarking Through Dynamic Variable Perturbation",
            "url": "https://arxiv.org/html/2406.17681"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/html/2502.06453v2"
          },
          {
            "title": "Evaluating Robustness of LLMs to Numerical Variations in ...",
            "url": "https://aclanthology.org/2025.insights-1.16.pdf"
          }
        ]
      },
      "Based on the search results, I found information about the benchmarks you mentioned:\n\n## MATH-Perturb\n\nMATH-Perturb is a benchmark that extends MATH with controlled surface-form variations, showing that even minor modifications can cause substantial accuracy drops across a wide range of models. The benchmark includes MATH-P-Simple and MATH-P-Hard, each consisting of 279 perturbed math problems that originate from the level-5 (hardest) problems of the MATH dataset, curated by 12 graduate-level experts with rigorous rubrics and cross-checking workflow for quality control.\n\nRecent benchmarking of 18 LLMs shows that all models, including o1-mini and gemini-2.0-flash-thinking, suffer significant performance drops (10%-25%) on MATH-P-Hard.\n\n## GSM-Symbolic\n\nGSM-Symbolic, introduced by Apple researchers, is a benchmark that perturbs math problems by modifying surface features such as names, numbers, and intermediate steps, showing that LLMs are highly sensitive to symbolic or structural shifts.\n\n## VarBench (Related)\n\nAnother related benchmark is VarBench, which introduces a variable perturbation process for converting existing benchmarks into forms that are robust to contamination by creating delexicalized questions along with solution functions.\n\nThese benchmarks collectively reveal that while LLMs show strong average-case performance on mathematical tasks, they lack robustness when problems are reformulated or perturbed in various ways."
    ],
    "durationSeconds": 9.289729437999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3932a465-32c9-495f-a7c8-39f11cfe0127",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling  ## Core…",
  "leafUuid": "20b05094-8458-48ea-bf2e-876ed4066fb7",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency for math RL robustness",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93"
}
```

---

### Tool call

_source line 26 · 2026-05-29T06:32:21.438Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PdkTLKUjXeCtGiHXf5oSik`</summary>

```json
{
  "query": "DyJR JS divergence diversity preserving GRPO reinforcement learning verifiable rewards 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20b05094-8458-48ea-bf2e-876ed4066fb7",
  "isSidechain": false,
  "requestId": "req_011CbWPgqm9kVfGEerHvrbDk",
  "type": "assistant",
  "uuid": "9c4e3682-46d9-44f0-aefc-e5584a3120d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013hzdk8YmogdrkpMdgcQeUp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 864,
      "cache_read_input_tokens": 22145,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 864,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 22145,
          "cache_creation_input_tokens": 864,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 864
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

_source line 27 · 2026-05-29T06:32:29.103Z_

<details><summary>↩ Tool result · `toolu_01PdkTLKUjXeCtGiHXf5oSik`</summary>

```text
Web search results for query: "DyJR JS divergence diversity preserving GRPO reinforcement learning verifiable rewards 2026"

Links: [{"title":"DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/pdf/2603.16157"},{"title":"[2603.16157] DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay","url":"https://arxiv.org/abs/2603.16157"},{"title":"DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay","url":"https://arxiv.org/html/2603.16157"},{"title":"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/html/2509.07430"},{"title":"[2509.07430] The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/abs/2509.07430"},{"title":"Divergence and Diversity in RLVR","url":"https://www.emergentmind.com/papers/2509.07430"}]

Based on the search results, I found relevant information about DyJR and related work in this research area:

## DyJR Overview

DyJR (Dynamic Jensen-Shannon Replay) is a regularization framework using a dynamic reference distribution from recent trajectories. The paper was published on March 18, 2026.

## Key Problem Addressed

While Reinforcement Learning enhances Large Language Model reasoning, on-policy algorithms like GRPO are sample-inefficient as they discard past rollouts. GRPO is prone to mode collapse in sparse-reward settings.

## Technical Approach

DyJR introduces a Time-Sensitive Dynamic Buffer that uses FIFO and adaptive sizing to retain only temporally proximal samples, synchronizing with model evolution, and Jensen-Shannon Divergence Regularization, which replaces direct gradient updates with a distributional constraint to prevent diversity collapse.

## Performance Results

Experiments on mathematical reasoning and Text-to-SQL benchmarks demonstrate that DyJR significantly outperforms GRPO as well as baselines such as RLEP and Ex-GRPO, while maintaining training efficiency comparable to the original GRPO.

## Related Work

The search also found related research on Diversity-Preserving Hybrid RL (DPH-RL), which leverages mass-covering f-divergences like forward-KL and JS-divergence to function as a 'rehearsal mechanism'.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c4e3682-46d9-44f0-aefc-e5584a3120d0",
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "a82248fc-7408-4c8d-a0e8-8bf296558a1c",
  "toolUseResult": {
    "query": "DyJR JS divergence diversity preserving GRPO reinforcement learning verifiable rewards 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MdQEeXJiqfPpjYsgDiV33a",
        "content": [
          {
            "title": "DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards",
            "url": "https://arxiv.org/pdf/2603.16157"
          },
          {
            "title": "[2603.16157] DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay",
            "url": "https://arxiv.org/abs/2603.16157"
          },
          {
            "title": "DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay",
            "url": "https://arxiv.org/html/2603.16157"
          },
          {
            "title": "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward",
            "url": "https://arxiv.org/html/2509.07430"
          },
          {
            "title": "[2509.07430] The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward",
            "url": "https://arxiv.org/abs/2509.07430"
          },
          {
            "title": "Divergence and Diversity in RLVR",
            "url": "https://www.emergentmind.com/papers/2509.07430"
          }
        ]
      },
      "Based on the search results, I found relevant information about DyJR and related work in this research area:\n\n## DyJR Overview\n\nDyJR (Dynamic Jensen-Shannon Replay) is a regularization framework using a dynamic reference distribution from recent trajectories. The paper was published on March 18, 2026.\n\n## Key Problem Addressed\n\nWhile Reinforcement Learning enhances Large Language Model reasoning, on-policy algorithms like GRPO are sample-inefficient as they discard past rollouts. GRPO is prone to mode collapse in sparse-reward settings.\n\n## Technical Approach\n\nDyJR introduces a Time-Sensitive Dynamic Buffer that uses FIFO and adaptive sizing to retain only temporally proximal samples, synchronizing with model evolution, and Jensen-Shannon Divergence Regularization, which replaces direct gradient updates with a distributional constraint to prevent diversity collapse.\n\n## Performance Results\n\nExperiments on mathematical reasoning and Text-to-SQL benchmarks demonstrate that DyJR significantly outperforms GRPO as well as baselines such as RLEP and Ex-GRPO, while maintaining training efficiency comparable to the original GRPO.\n\n## Related Work\n\nThe search also found related research on Diversity-Preserving Hybrid RL (DPH-RL), which leverages mass-covering f-divergences like forward-KL and JS-divergence to function as a 'rehearsal mechanism'."
    ],
    "durationSeconds": 7.6542814679999935,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9c4e3682-46d9-44f0-aefc-e5584a3120d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-29T06:32:31.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PbMRoFPwhMhik4eW6yNnBd`</summary>

```json
{
  "query": "consistency training perturbation invariance math reasoning RL GRPO 2026 distribution level"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a82248fc-7408-4c8d-a0e8-8bf296558a1c",
  "isSidechain": false,
  "requestId": "req_011CbWPhag5d3vtLvQRPdWbC",
  "type": "assistant",
  "uuid": "238aca98-a34f-43c3-b7db-07d617f7bdb1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLG5LG3myR5QMTnkVaE7YA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 23009,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 753,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 23009,
          "cache_creation_input_tokens": 753,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 753
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

_source line 29 · 2026-05-29T06:32:39.593Z_

<details><summary>↩ Tool result · `toolu_01PbMRoFPwhMhik4eW6yNnBd`</summary>

```text
Web search results for query: "consistency training perturbation invariance math reasoning RL GRPO 2026 distribution level"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=fDk95XPsCU"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2604.20659"},{"title":"Post-Training in 2026: GRPO, DAPO, RLVR & Beyond","url":"https://llm-stats.com/blog/research/post-training-techniques-2026"},{"title":"GRPO Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/main/en/grpo_trainer"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"},{"title":"Adaptive Group Policy Optimization: Towards Stable Training and Token-Efficient Reasoning","url":"https://arxiv.org/pdf/2503.15952"},{"title":"Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning","url":"https://arxiv.org/pdf/2510.04072"},{"title":"R2PO: Decoupling Training Trajectories from Inference Responses for LLM Reasoning","url":"https://arxiv.org/html/2601.11960"}]

I found relevant research on this topic. Here are the key findings:

## Consistency Training and Perturbation Invariance in Math Reasoning RL

True reasoning competence should reflect invariance that extends beyond the single-view output for consistency. Training signals should remain valid across different data views or persist throughout the temporal evolution of the model, providing a more reliable basis on which self-supervised RL can rely.

## GRPO and Related Methods (2026)

Recent research has focused on improving Group Relative Policy Optimization (GRPO) for mathematical reasoning:

- Methods have been developed that consistently improve both accuracy and reasoning conciseness over GRPO baselines, showing up to 2.6-point accuracy improvements and 13.7% reasoning-length reductions on math tasks.

- GRPO, proposed by DeepSeek, eliminated the value model and achieved high computational efficiency and excellent reasoning performance.

## Perturbation Robustness

Perturbation experiments have been conducted where redundant tags were manually injected into successful trajectories to simulate noise traps, then the model's probability of adopting this erroneous behavior was measured. The baseline GRPO quickly succumbed to the perturbation, indicating that robustness to input variations remains a challenge in these systems.

The research from ICLR 2026 emphasizes that distribution-level consistency and invariance to perturbations are critical for developing more robust reasoning models in RL frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "238aca98-a34f-43c3-b7db-07d617f7bdb1",
  "isSidechain": false,
  "promptId": "802ab2fe-8fad-429e-8d34-5c540307ac6d",
  "type": "user",
  "uuid": "9c3a71a5-ad8c-48eb-9f8f-be76a0409447",
  "toolUseResult": {
    "query": "consistency training perturbation invariance math reasoning RL GRPO 2026 distribution level",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Rx1cdbE3BHHVaEEGHYJDMj",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=fDk95XPsCU"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2604.20659"
          },
          {
            "title": "Post-Training in 2026: GRPO, DAPO, RLVR & Beyond",
            "url": "https://llm-stats.com/blog/research/post-training-techniques-2026"
          },
          {
            "title": "GRPO Trainer · Hugging Face",
            "url": "https://huggingface.co/docs/trl/main/en/grpo_trainer"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          },
          {
            "title": "Adaptive Group Policy Optimization: Towards Stable Training and Token-Efficient Reasoning",
            "url": "https://arxiv.org/pdf/2503.15952"
          },
          {
            "title": "Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2510.04072"
          },
          {
            "title": "R2PO: Decoupling Training Trajectories from Inference Responses for LLM Reasoning",
            "url": "https://arxiv.org/html/2601.11960"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key findings:\n\n## Consistency Training and Perturbation Invariance in Math Reasoning RL\n\nTrue reasoning competence should reflect invariance that extends beyond the single-view output for consistency. Training signals should remain valid across different data views or persist throughout the temporal evolution of the model, providing a more reliable basis on which self-supervised RL can rely.\n\n## GRPO and Related Methods (2026)\n\nRecent research has focused on improving Group Relative Policy Optimization (GRPO) for mathematical reasoning:\n\n- Methods have been developed that consistently improve both accuracy and reasoning conciseness over GRPO baselines, showing up to 2.6-point accuracy improvements and 13.7% reasoning-length reductions on math tasks.\n\n- GRPO, proposed by DeepSeek, eliminated the value model and achieved high computational efficiency and excellent reasoning performance.\n\n## Perturbation Robustness\n\nPerturbation experiments have been conducted where redundant tags were manually injected into successful trajectories to simulate noise traps, then the model's probability of adopting this erroneous behavior was measured. The baseline GRPO quickly succumbed to the perturbation, indicating that robustness to input variations remains a challenge in these systems.\n\nThe research from ICLR 2026 emphasizes that distribution-level consistency and invariance to perturbations are critical for developing more robust reasoning models in RL frameworks."
    ],
    "durationSeconds": 7.7953825199999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "238aca98-a34f-43c3-b7db-07d617f7bdb1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-29T06:32:39.597Z_

```json
{
  "parentUuid": "9c3a71a5-ad8c-48eb-9f8f-be76a0409447",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "59191ce0-ed86-4ee2-a24a-f907f999f443",
  "timestamp": "2026-05-29T06:32:39.597Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 31 · 2026-05-29T06:34:46.434Z_

Now I have sufficient research context. Let me compile the final evaluation.

```
【阶段】: Triage

【领域调研】:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478) (arXiv, Jan 2026): 最直接的竞争者。通过跨perturbation变体pooling reward实现Level-2一致性。取得Pass@k提升(AMC12/AIME24上+9.84)，但**未在任何perturbation robustness benchmark上评估**（GSM-Symbolic, VAR-MATH, MATH-Perturb均未测试）。本proposal精准定位了这一盲区。
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101) (arXiv, Mar 2026): 在GRPO中加入InfoNCE对比学习，对齐同一问题的不同正确rollout。方向是same-problem cross-trajectory invariance。本proposal的对比学习组件（L_contrastive）目标不同——cross-perturbation invariance，是互补而非重复的invariance维度。CLIPO在GSM8K-P1/P2上有改进但幅度有限。
- [AIR: Towards Context-Invariant Safety Alignment](https://arxiv.org/abs/2605.20994) (arXiv, May 2026): 使用非对称stop-gradient anchor invariance regularization整合到GRPO中，但主要面向safety alignment而非math robustness。其非对称设计适合safety场景（一个prompt变体有更可靠反馈），但不适合math perturbation对（双侧对称可验证）。本proposal选择对称JS散度的论证合理。
- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157) (arXiv, Mar 2026): 在GRPO中使用JS散度作为diversity-preserving regularizer（current vs. historical policy），验证了JS散度在GRPO框架中的可行性和优越性（JS > Forward KL）。为本proposal的技术选择提供了经验支持，但DyJR的JS用途是diversity preservation，本proposal的JS用途是cross-perturbation consistency——不同目标。
- [AbstRaL: Augmenting Reasoning by Reinforcing Abstract Thinking](https://openreview.net/forum?id=fDk95XPsCU) (ICLR 2026): 通过RL训练显式抽象再求解，但受限于GSM级别问题。本proposal声称通过分布一致性正则化隐式实现类似抽象效果。
- [MATH-Perturb](https://arxiv.org/abs/2502.06453) (arXiv, 2025): 基准测试显示即使o1-mini等模型在hard perturbation上也有10%-25%准确率下降，验证了perturbation robustness问题的真实性和严重性。
- [GSM-Symbolic](https://arxiv.org/abs/2410.05229) (ICLR 2025, Apple): 开创性工作，揭示LLM在symbolic/structural perturbation下的脆弱性。
- [PrAg-PO: Prompt Augmentation Scales up GRPO](https://arxiv.org/abs/2602.03190) (arXiv, Feb 2026): 使用13种prompt模板作为隐式正则化，属于Data-level (Level 1)。
- [The Choice of Divergence](https://arxiv.org/abs/2509.07430) (arXiv, 2025): 系统研究f-divergence在RLVR中的作用，发现mass-covering divergence（forward KL, JS）优于reverse KL在保持多样性方面。

- **调研总结**: Math reasoning的perturbation robustness是一个已被充分验证的重要问题（GSM-Symbolic, VAR-MATH, MATH-Perturb等多个benchmark证实）。在RL训练方面，TA-GRPO开创了reward-level一致性但缺乏robustness评估，CLIPO/AIR/DyJR各自在GRPO框架中使用了不同的正则化/对比学习但未直接针对perturbation robustness。本proposal所定位的"distribution-level consistency for perturbation invariance"在现有工作中确实是一个未被占据的具体位置，三级框架的分析有见地。但这一位置的"增量"性质也意味着novelty的天花板有限——本质上是将已有技术（JS divergence, contrastive learning）组合应用到一个已有问题上。

【整体印象】:
如果我是审稿人，第一反应是：这是一篇**定位精准、调研扎实、实验设计周全**的工作。三级一致性框架（Data → Reward → Distribution）的提出有清晰的递进逻辑，对TA-GRPO"correct but inconsistent reasoning"盲区的分析切中要害。但第二反应是：**核心技术贡献的深度有限**——本质上是在GRPO loss上加了一个JS散度正则项和一个InfoNCE对比项，这两者都不是新技术。论文的价值更多在于"将对的东西放到对的地方"（right combination for the right problem），而非方法论上的突破。

我会倾向于**weak accept / borderline**——如果实验结果确实显著（尤其在perturbation robustness benchmarks上的提升），有可能跨过accept线；但如果reviewer认为这只是existing techniques的straightforward combination，可能会被borderline reject。

【核心贡献】:
1. **三级一致性框架（Level 1-2-3）**: 对现有math robustness方法的系统性分类（Data/Reward/Distribution），理论上论证了为什么Level 2（reward pooling）不足以捕捉"correct but inconsistent reasoning"。这个框架本身有学术价值。
2. **ConsistGRPO方法**: 在GRPO中加入cross-perturbation JS散度一致性loss和contrastive loss。技术上是incremental（JS divergence + InfoNCE都是成熟工具），但应用场景和组合方式有novelty。
3. **完备的实验设计**: 8个baseline、7+个benchmark、5维ablation的设计本身就是一个贡献，尤其是填补了TA-GRPO未做robustness评估的空白。

对领域的价值：**中等偏上**。如果实验验证了distribution-level > reward-level的假设，这会为math RL robustness社区提供一个有价值的empirical insight和实用方法。但不太可能改变领域的研究方向。

【方法合理性】:
方法整体合理，但有几个需要关注的点：

1. **JS散度计算的实际效果**: proposal使用sequence-level log-probabilities构造empirical rollout distributions P_x和P_x'，然后计算JS(P_x || P_x')。但G个rollout（通常G=8-16）构成的empirical distribution可能非常noisy，JS的估计方差大。这与DyJR使用buffer accumulated distributions不同——DyJR有更多样本来估计分布。proposal需要讨论small-sample JS estimation的问题。

2. **更简单的替代方案**: 一个直接的替代方案是在rollout的token-level logits上做KL/JS对齐（类似knowledge distillation），而非sequence-level。这可能提供更dense的梯度信号。另一个替代方案是直接在TA-GRPO基础上加一个简单的reward consistency bonus（如果x和x'都对则bonus增大），而非引入JS散度——这更简单但可能近似达到类似效果。proposal应明确论证为何distribution-level JS优于这些simpler alternatives。

3. **Perturbation pipeline的reliability**: 对于MATH/AMC/AIME level的问题（竞赛数学），自动化perturbation的正确性验证是一个非平凡的工程问题。proposal提到用SymPy验证，但竞赛数学的很多问题（组合、数论、几何）不容易用SymPy自动验证。这可能限制training数据的覆盖率。proposal提到了这个问题并计划做pilot study，这是好的，但也意味着实际可用的training data可能比预期少。

4. **Consistency-diversity tradeoff**: 这是一个关键问题。强一致性约束可能导致rollout diversity collapse（如果模型被迫让P_x ≈ P_x'，可能会converge到单一推理路径）。proposal意识到了这个问题并计划做tradeoff分析，这很好。但这也意味着最优的λ₁可能需要非常小，此时L_consist的实际贡献就变得很边际。

【5 维度打分】:

1. **研究问题: 强** — Math reasoning模型在perturbation下的脆弱性是一个经GSM-Symbolic (ICLR 2025)、VAR-MATH、MATH-Perturb等多个benchmark验证的真实问题。RL训练（GRPO）不仅未解决反而可能加剧这一问题。TA-GRPO的reward pooling方法未做robustness评估、且理论上对"correct but inconsistent reasoning"存在盲区——这个gap的定位非常精准且有价值。问题的重要性和时效性都很强。

2. **方法与创新: 中** — 三级框架的分析有insight，但核心方法（JS divergence regularization + InfoNCE contrastive loss）都是成熟技术的组合应用，不涉及方法论创新。与CLIPO (arXiv 2603.10101) 相比，对比学习组件的区别仅在于positive pair的构造方式（cross-perturbation vs. cross-trajectory）；与DyJR (arXiv 2603.16157) 相比，JS散度的使用方式不同（cross-perturbation vs. temporal）但技术形式类似；与AIR (arXiv 2605.20994) 相比，区别在于对称vs.非对称——有道理但不构成显著创新。一个苛刻的reviewer可能会认为这是"TA-GRPO + JS regularization"的straightforward extension。proposal需要通过强实验结果来弥补方法novelty的不足。

3. **实验设计: 强** — 这是proposal最突出的优势。8个baseline覆盖了Data/Reward/Representation/None四个consistency level，形成完整的ablation对照；7+个benchmark涵盖robustness和clean accuracy两个维度；5维ablation（component decomposition, perturbation type, hyperparameter sensitivity, training dynamics, divergence metric comparison）非常周全；FLOPs-matched baseline的设计解决了公平性问题；scale validation (1.7B + 8B) 增加了可信度。特别值得肯定的是divergence metric comparison (JS vs. Forward KL vs. Reverse KL vs. Symmetric KL vs. AIR-style)——这直接回应了DyJR和Choice of Divergence等工作的发现，既是ablation也是对领域的贡献。

4. **可行性: 中** — 
   - Qwen3-8B的训练在单节点8×A100/H100上可行（约2-4周）。
   - 主要风险在perturbation pipeline：竞赛数学(AMC/AIME)的自动perturbation + 正确性验证是非平凡的工程任务。proposal限制在algebraic/arithmetic subtypes是务实的，但可能导致training data覆盖率不足。
   - JS散度计算需要对每个问题做2×G次rollout（original + perturbed），计算开销翻倍。proposal承认这一点并计划profile FLOPs，但这可能需要额外的优化（如shared prefix caching）。
   - 整体可行但有工程挑战。

5. **写作与呈现: 强** — proposal的结构清晰、逻辑递进（问题定义 → 三级框架 → 方法 → 实验设计）。相关工作的调研非常全面，对每个相关工作的定位和区分精确。三级框架的提出为读者提供了清晰的conceptual map。"correct but inconsistent reasoning"的例子直观有力。唯一可改进的是：proposal略显冗长，如果能更精炼地呈现核心idea会更好。

【概率估计】: [28% - 42%] 中位 35%

【估计理由】:

**上行因素（推向42%）**:
- 研究问题精准且timely，精确定位了TA-GRPO的理论盲区
- 实验设计极为完备（8 baselines, 7+ benchmarks, 5-dim ablation），这本身是显著加分项
- 三级框架提供了有价值的conceptual contribution
- 领域调研极其全面，reviewer不太会找到"missed related work"这类问题
- Perturbation robustness在2025-2026是热门话题，reviewers对该方向普遍有兴趣

**下行因素（推向28%）**:
- 方法novelty有限——核心是JS divergence + InfoNCE的straightforward combination，AAAI reviewers可能认为technical contribution不足
- 目前没有实验结果。如果distribution-level一致性的提升相对于TA-GRPO的reward pooling是边际的（例如<3%），论文会失去核心论据
- Perturbation pipeline的实际覆盖率和质量是不确定因素
- Consistency-diversity tradeoff可能限制方法的实际增益
- GRPO variants已经非常拥挤（DAPO, DR.GRPO, CLIPO, DyJR, TA-GRPO, PrAg-PO, MCPO, AIR...），reviewer可能对"yet another GRPO variant"产生审美疲劳

**中位35%的理由**: 这是一篇"solid but incremental"的投稿。问题定位好、实验设计完备、写作清晰，但方法novelty的天花板限制了它。在AAAI 2026的competitive pool中，它位于borderline区域。如果实验结果显著（distribution-level显著优于reward-level，尤其在perturbation benchmarks上），概率偏向上界；如果实验结果边际，概率偏向下界。

【主要风险】:
1. **"Insufficient novelty / straightforward combination"**: 最可能的拒稿理由。Reviewer可能认为JS-divergence regularization + InfoNCE contrastive loss的组合缺乏方法论深度，尤其是在GRPO variants已经极度拥挤的当下。三级框架虽好，但框架+combination可能不足以构成AAAI主会级别的贡献。
2. **实验结果不确定性**: Proposal尚无实验结果。如果distribution-level一致性相对于reward-level（TA-GRPO）的提升幅度有限，或者consistency-diversity tradeoff使得最优λ₁很小导致L_consist贡献边际，核心claim（Level 3 > Level 2）将缺乏实证支撑。

【实施评估】:
- **计算资源**: 中高。需要8×A100/H100 GPU节点。每个问题需2×G次rollout（原始+扰动），计算量约为vanilla GRPO的2-2.5倍。JS散度和contrastive loss的额外计算开销相对较小。估计总GPU-hours: 2000-4000（含所有ablation和baseline复现）。
- **数据需求**: MATH/AMC/AIME训练集（公开可用）。关键瓶颈是perturbation pipeline的构建——需要对竞赛数学问题进行自动化扰动并验证正确性。Pilot study (100题) 可在1-2周内完成。
- **人工介入**: 中等。Perturbation pipeline需要人工验证（尤其是geometry/number theory等难以自动验证的题型）。LLM-generated perturbations需要质量抽检。Baseline复现（TA-GRPO, CLIPO, AbstRaL）可能需要调试。
- **训练需求**: 需要完整的RL训练流程（GRPO + 正则化项）。Qwen3-8B约需2-3周训练，Qwen3-1.7B约需1周。总训练时间（含所有variants和ablations）约4-6周。
- **新 Benchmark**: 不需要构建新benchmark——使用现有的GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM。但perturbation pipeline本身可视为一个工程产出。
- **预估周期**: 10-14周（Pilot study 2周 + Perturbation pipeline 2-3周 + 主实验+ablation 4-6周 + 论文写作 2-3周）。假设计算资源充足，一个2-3人团队可在AAAI 2026 deadline前完成。
```

Sources:
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)
- [AIR: Towards Context-Invariant Safety Alignment for LLMs](https://arxiv.org/abs/2605.20994)
- [DyJR: Preserving Diversity via Dynamic Jensen-Shannon Replay](https://arxiv.org/abs/2603.16157)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations](https://arxiv.org/abs/2502.06453)
- [GSM-Plus: A Comprehensive Benchmark for Evaluating Robustness of LLMs](https://arxiv.org/abs/2402.19255)
- [The Choice of Divergence in RLVR](https://arxiv.org/abs/2509.07430)
- [Post-Training in 2026: GRPO, DAPO, RLVR & Beyond](https://llm-stats.com/blog/research/post-training-techniques-2026)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59191ce0-ed86-4ee2-a24a-f907f999f443",
  "isSidechain": false,
  "requestId": "req_011CbWPiMUcLzgmVi8uvTf8T",
  "type": "assistant",
  "uuid": "065bbb3f-44a5-4f84-921f-8ccb752ce17b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UW2WgRpTHzLUmzDtzgTXX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 893,
      "cache_read_input_tokens": 23762,
      "output_tokens": 5210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 893,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5210,
          "cache_read_input_tokens": 23762,
          "cache_creation_input_tokens": 893,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 893
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling  ## Core…",
  "leafUuid": "065bbb3f-44a5-4f84-921f-8ccb752ce17b",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency for math RL robustness",
  "sessionId": "39e773b4-583e-4a07-b8a8-760547234e93"
}
```

---
