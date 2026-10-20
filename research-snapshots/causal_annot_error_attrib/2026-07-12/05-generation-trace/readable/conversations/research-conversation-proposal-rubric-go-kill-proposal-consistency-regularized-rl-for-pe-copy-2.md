# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Consistency-Regularized RL for Pe

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/2ecff145-2c2e-49d3-880a-3771a75ee556.jsonl`
- **Structured JSON:** [`3eb520701b74801d2352.json`](../../sessions/3e/3eb520701b74801d2352.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T08:35:44.887Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T08:35:44.887Z",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Consistency-Regularized RL for Perturbation-Robust Math Reasoning\n\n## Core Problem\n\nRL-trained mathematical reasoning models suffer 47–73% accuracy drops under trivial surface-form perturbations (numerical re-parameterization, variable renaming), revealing a fundamental limitation of outcome-based RLVR: binary reward provides no gradient against surface-form-dependent reasoning patterns. ReasonMaxxer (arXiv 2605.06241) shows RL acts as sparse policy selection at high-entropy tokens rather than capability learning; RLTR (arXiv 2602.08489) demonstrates that robust reasoning requires transferability beyond the producing model. Both imply outcome-only RL is insufficient for genuine robustness. Can we enforce invariance to mathematically irrelevant features during RL training without degrading clean accuracy?\n\n## Research Opportunity\n\nMathematical perturbation space exhibits a structural duality demanding a dual-objective response: equivalence-preserving perturbations (variable renaming, numerical reparameterization) and semantics-altering perturbations (changed constraints, added conditions) are surface-similar but require opposite model behaviors—invariance for the former, discrimination for the latter. Critically, existing methods address at most one side:\n\n- ROMA (arXiv 2605.09262, May 2026): token-level KL consistency during GRPO improves visual robustness by +2.4%/+2.3% on seen/unseen degradations—single-direction invariance only, visual domain only.\n- TA-GRPO (arXiv 2601.22478, Jan 2026): pools advantages across equivalent rephrasings, improving pass@k by up to 9.84 points on competition math—no explicit consistency loss, no robustness evaluation.\n- CLIPO (arXiv 2603.10101, Mar 2026): trajectory-level contrastive learning in GRPO extracts invariant structures across correct reasoning paths—orthogonal invariance dimension (trajectory noise, not input surface-form noise).\n- RULES (arXiv 2602.00998, Feb 2026): explicit eligibility reasoning + section-aware RL to verify lemma applicability before use—addresses discrimination via structured output format change, not via distributional consistency.\n- PPCL (EACL 2024, ACL 2024): JS-divergence consistency regularization achieves 10× sample efficiency over pure augmentation in NLP—validates that distribution-level consistency provides an inductive bias (same structure → same output) that data augmentation alone cannot replicate.\n\nNo method combines perturbation-type-aware dual objectives (invariance + discrimination) with RL-integrated consistency regularization for mathematical reasoning. Moreover, the discrimination side—training models to detect when surface-similar problems require different solution strategies—constitutes implicit mathematical structure verification, directly targeting the \"blind technique application\" failure mode.\n\n## Research Landscape\n\nThe robustness problem is extensively documented: VAR-MATH (arXiv 2507.12885) reports 47.9–72.9% accuracy drops for 7B RL models on symbolically re-parameterized competition math (AMC23/AIME24/AIME25); GSM-Symbolic (ICLR 2025) shows up to 65% drops from a single irrelevant clause; the Robust Reasoning Benchmark (arXiv 2604.08571, Apr 2026) finds up to 54% drops for open-weights models on perturbed AIME problems; MATH-Perturb (ICML 2025) quantifies a critical \"blind technique application\" failure mode—~40% of o1-mini's errors and ~25% of Claude-3.5-Sonnet's errors on hard perturbations stem from mechanically applying memorized strategies without verifying applicability.\n\nTraining-time interventions remain scarce: AbstRaL (ICLR 2026) achieves GSM-level robustness via symbolic abstraction but is explicitly limited to elementary math. TA-GRPO pools advantages across GPT-4-generated rephrasings but lacks equivalence verification, distribution-level consistency, and discrimination capability. ROMA addresses visual robustness only. CLIPO captures trajectory-level reasoning invariance—orthogonal to input-level perturbation invariance. RULES addresses discrimination through explicit output-structure modification (eligibility reasoning sections), requiring format changes incompatible with free-form reasoning; ConsistRL instead achieves discrimination implicitly through distributional constraints, remaining format-agnostic. RLTR (arXiv 2602.08489) improves robustness via transfer reward but does not target perturbation-specific invariance. GRPO-CARE (arXiv 2506.16141) and COPO (arXiv 2508.04138) address multimodal consistency and zero-gradient issues respectively. DAPO (arXiv 2503.14476) and Dr.GRPO improve GRPO training dynamics without robustness mechanisms.\n\n## Proposed Approach\n\nExtend GRPO with dual consistency objectives reflecting mathematical perturbation space's structural duality:\n\n**(1) JS-divergence invariance loss** on math-equivalence-preserving perturbations (variable renaming, numerical reparameterization), generated via a hybrid pipeline: VAR-MATH's symbolic pipeline (arXiv 2507.12885) for algebraic/numerical problem types + LLM-based paraphrasing with SymPy equivalence verification for remaining types. Applied at entropy-gated decision tokens per ReasonMaxxer's insight, with entropy-gating treated as a testable hypothesis (the correspondence between RL policy-selection points and consistency-critical points is not a priori guaranteed).\n\n**(2) Contrastive discrimination loss** penalizing output similarity on semantics-altering hard perturbations—implicit mathematical structure verification targeting MATH-Perturb's \"blind technique application\" failure mode. Unlike RULES' explicit eligibility reasoning (which requires structured output format), this operates via distributional constraints compatible with any reasoning format.\n\n**(3) TA-GRPO-style advantage pooling** across perturbation groups to mitigate GRPO's zero-gradient problem.\n\n**Key hypothesis: cross-perturbation-type transfer robustness.** Training-time perturbations (symbolic reparameterization) differ from evaluation perturbations (MATH-Perturb semantic alterations, RRB structural noise). If ConsistRL generalizes across unseen perturbation types, this evidences learned mathematical structure sensitivity rather than perturbation-specific immunity.\n\n**Why consistency loss, not just augmentation?** Distribution-level consistency provides an explicit inductive bias—same mathematical structure under different surface forms must map to the same reasoning trajectory. This structural constraint cannot emerge from data augmentation alone, which merely broadens training distribution without enforcing distributional invariance. PPCL's 10× sample efficiency over pure augmentation (EACL 2024) provides empirical support; the GRPO+augmentation-only baseline directly tests this claim.\n\nTrain Qwen3-8B (primary) and Qwen3-1.5B (ablation/scaling validation) on MATH/AMC/AIME, 8×H100.\n\n## Detailed Description\n\n**Invariance objective.** JS-divergence enforces output-distribution invariance across equivalence-preserving perturbations, applied at high-entropy decision points (1–3% of tokens per ReasonMaxxer). Perturbation generation uses a hybrid pipeline: VAR-MATH's symbolic pipeline for compatible types (algebra, numerical parameterization) and LLM paraphrasing + SymPy verification for others. Training perturbation quality is validated via: (a) symbolic equivalence verification where applicable, (b) sampled human verification (≥200 problems) reporting equivalence correctness rate, (c) coverage rate reporting across MATH problem types. Entropy gating is validated via explicit ablation: full-sequence vs. entropy-gated application, static base-model entropy vs. dynamic policy entropy, threshold sensitivity analysis.\n\n**Discrimination objective.** Contrastive loss penalizes output similarity on semantics-altering hard perturbations, targeting implicit mathematical structure verification. Training data generated via GPT-4 pipeline following MATH-Perturb's hard perturbation taxonomy (condition change, constraint addition, etc.), with: (a) SymPy verification that generated problems have unique solutions differing from originals, (b) human verification (≥300 problems, 2 annotators, reporting inter-annotator agreement), (c) strict train/eval separation from all evaluation benchmarks. This approaches \"blind technique application\" via implicit distributional constraints, complementing RULES' explicit eligibility reasoning approach.\n\n**Advantage pooling.** TA-GRPO-style pooling across perturbation groups mitigates zero-gradient problems while ensuring mixed reward signals.\n\n## Experimental Design\n\n**Models:** Qwen3-8B (primary), Qwen3-1.5B (ablation + scaling). Two-phase execution: Phase 1 on 1.5B (full ablation + preliminary baselines), Phase 2 on 8B (core baselines + key ablations). Community checkpoints used where available.\n\n**Baselines (8):** (1) Vanilla GRPO, (2) DAPO (arXiv 2503.14476), (3) Dr.GRPO, (4) TA-GRPO (arXiv 2601.22478), (5) COPO (arXiv 2508.04138), (6) GRPO + augmentation-only (same perturbation data, no consistency losses), (7) ReasonMaxxer (arXiv 2605.06241), (8) AbstRaL (ICLR 2026, GSM-level subset only).\n\n**Evaluation benchmarks (grouped by perturbation type):**\n- *Numerical equivalence:* VAR-MATH (AMC23/AIME24/AIME25) — core evaluation\n- *Semantic discrimination:* MATH-Perturb (MATH-P-Simple and MATH-P-Hard, reported separately) — core evaluation\n- *Structural noise (supplementary):* Robust Reasoning Benchmark (arXiv 2604.08571) — out-of-scope for core claim, reported as cross-perturbation transfer observation\n- *Clean accuracy:* MATH-500\n\n**Metrics:** VAR-MATH strict/loose consistency rate with bootstrapping 95% CIs; robustness gap (clean − perturbed accuracy); per-benchmark accuracy with CIs; clean accuracy non-degradation criterion (MATH-500 drop ≤ 1%, paired bootstrap test p < 0.05).\n\n**Targets:** VAR-MATH strict consistency rate absolute improvement ≥10 pp over vanilla GRPO; robustness gap reduction ≥15 pp; MATH-P-Hard accuracy improvement ≥5 pp; clean MATH-500 drop ≤ 1%.\n\n**Ablation matrix:** (1) ConsistRL full, (2) w/o JS-divergence, (3) w/o contrastive discrimination, (4) w/o entropy gating (all tokens), (5) w/o advantage pooling, (6) JS-divergence only + entropy gating (minimal). Extensions (primarily at 1.5B): static vs. dynamic entropy gating, entropy threshold sensitivity, perturbation type separation (variable renaming vs. numerical reparameterization), loss weight sensitivity (λ₁, λ₂ grid).\n\n**Compute fairness:** Dual protocol—Protocol A (step-matched): same training steps, report per-method FLOPs and wall-clock time; Protocol B (FLOP-matched): same total FLOPs, ConsistRL uses fewer steps. Report per-step overhead ratio. Robustness vs. cumulative FLOPs curve.\n\n## Key References\n\n- Reinforcing Multimodal Reasoning Against Visual Degradation / ROMA (arXiv 2605.09262, 2026)\n- Transform-Augmented GRPO Improves Pass@k / TA-GRPO (arXiv 2601.22478, 2026)\n- CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (arXiv 2603.10101, 2026)\n- RULES: Reliable Use of Lemmas via Eligibility Reasoning (arXiv 2602.00998, 2026)\n- Beyond Correctness: Learning Robust Reasoning via Transfer / RLTR (arXiv 2602.08489, 2026)\n- Prompt Perturbation Consistency Learning / PPCL (EACL Findings 2024, ACL 2024)\n- MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations (ICML 2025)\n- GSM-Symbolic: Understanding Limitations of Mathematical Reasoning in LLMs (ICLR 2025)\n- AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking (ICLR 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2507.12885, 2025)\n- Rethinking RL for LLM Reasoning / ReasonMaxxer (arXiv 2605.06241, 2026)\n- Robust Reasoning Benchmark (arXiv 2604.08571, 2026)\n- GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (arXiv 2506.16141, 2025)\n- COPO: Consistency-Aware Policy Optimization (arXiv 2508.04138, 2025)\n- DAPO: An Open-Source LLM Reinforcement Learning System at Scale (arXiv 2503.14476, 2025)\n- Dr.GRPO: Group Relative Policy Optimization Done Right"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T08:35:44.891Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T08:35:44.891Z",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-29T08:35:44.938Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Consistency-Regularized RL for Perturbation-Robust Math Reasoning

## Core Problem

RL-trained mathematical reasoning models suffer 47–73% accuracy drops under trivial surface-form perturbations (numerical re-parameterization, variable renaming), revealing a fundamental limitation of outcome-based RLVR: binary reward provides no gradient against surface-form-dependent reasoning patterns. ReasonMaxxer (arXiv 2605.06241) shows RL acts as sparse policy selection at high-entropy tokens rather than capability learning; RLTR (arXiv 2602.08489) demonstrates that robust reasoning requires transferability beyond the producing model. Both imply outcome-only RL is insufficient for genuine robustness. Can we enforce invariance to mathematically irrelevant features during RL training without degrading clean accuracy?

## Research Opportunity

Mathematical perturbation space exhibits a structural duality demanding a dual-objective response: equivalence-preserving perturbations (variable renaming, numerical reparameterization) and semantics-altering perturbations (changed constraints, added conditions) are surface-similar but require opposite model behaviors—invariance for the former, discrimination for the latter. Critically, existing methods address at most one side:

- ROMA (arXiv 2605.09262, May 2026): token-level KL consistency during GRPO improves visual robustness by +2.4%/+2.3% on seen/unseen degradations—single-direction invariance only, visual domain only.
- TA-GRPO (arXiv 2601.22478, Jan 2026): pools advantages across equivalent rephrasings, improving pass@k by up to 9.84 points on competition math—no explicit consistency loss, no robustness evaluation.
- CLIPO (arXiv 2603.10101, Mar 2026): trajectory-level contrastive learning in GRPO extracts invariant structures across correct reasoning paths—orthogonal invariance dimension (trajectory noise, not input surface-form noise).
- RULES (arXiv 2602.00998, Feb 2026): explicit eligibility reasoning + section-aware RL to verify lemma applicability before use—addresses discrimination via structured output format change, not via distributional consistency.
- PPCL (EACL 2024, ACL 2024): JS-divergence consistency regularization achieves 10× sample efficiency over pure augmentation in NLP—validates that distribution-level consistency provides an inductive bias (same structure → same output) that data augmentation alone cannot replicate.

No method combines perturbation-type-aware dual objectives (invariance + discrimination) with RL-integrated consistency regularization for mathematical reasoning. Moreover, the discrimination side—training models to detect when surface-similar problems require different solution strategies—constitutes implicit mathematical structure verification, directly targeting the "blind technique application" failure mode.

## Research Landscape

The robustness problem is extensively documented: VAR-MATH (arXiv 2507.12885) reports 47.9–72.9% accuracy drops for 7B RL models on symbolically re-parameterized competition math (AMC23/AIME24/AIME25); GSM-Symbolic (ICLR 2025) shows up to 65% drops from a single irrelevant clause; the Robust Reasoning Benchmark (arXiv 2604.08571, Apr 2026) finds up to 54% drops for open-weights models on perturbed AIME problems; MATH-Perturb (ICML 2025) quantifies a critical "blind technique application" failure mode—~40% of o1-mini's errors and ~25% of Claude-3.5-Sonnet's errors on hard perturbations stem from mechanically applying memorized strategies without verifying applicability.

Training-time interventions remain scarce: AbstRaL (ICLR 2026) achieves GSM-level robustness via symbolic abstraction but is explicitly limited to elementary math. TA-GRPO pools advantages across GPT-4-generated rephrasings but lacks equivalence verification, distribution-level consistency, and discrimination capability. ROMA addresses visual robustness only. CLIPO captures trajectory-level reasoning invariance—orthogonal to input-level perturbation invariance. RULES addresses discrimination through explicit output-structure modification (eligibility reasoning sections), requiring format changes incompatible with free-form reasoning; ConsistRL instead achieves discrimination implicitly through distributional constraints, remaining format-agnostic. RLTR (arXiv 2602.08489) improves robustness via transfer reward but does not target perturbation-specific invariance. GRPO-CARE (arXiv 2506.16141) and COPO (arXiv 2508.04138) address multimodal consistency and zero-gradient issues respectively. DAPO (arXiv 2503.14476) and Dr.GRPO improve GRPO training dynamics without robustness mechanisms.

## Proposed Approach

Extend GRPO with dual consistency objectives reflecting mathematical perturbation space's structural duality:

**(1) JS-divergence invariance loss** on math-equivalence-preserving perturbations (variable renaming, numerical reparameterization), generated via a hybrid pipeline: VAR-MATH's symbolic pipeline (arXiv 2507.12885) for algebraic/numerical problem types + LLM-based paraphrasing with SymPy equivalence verification for remaining types. Applied at entropy-gated decision tokens per ReasonMaxxer's insight, with entropy-gating treated as a testable hypothesis (the correspondence between RL policy-selection points and consistency-critical points is not a priori guaranteed).

**(2) Contrastive discrimination loss** penalizing output similarity on semantics-altering hard perturbations—implicit mathematical structure verification targeting MATH-Perturb's "blind technique application" failure mode. Unlike RULES' explicit eligibility reasoning (which requires structured output format), this operates via distributional constraints compatible with any reasoning format.

**(3) TA-GRPO-style advantage pooling** across perturbation groups to mitigate GRPO's zero-gradient problem.

**Key hypothesis: cross-perturbation-type transfer robustness.** Training-time perturbations (symbolic reparameterization) differ from evaluation perturbations (MATH-Perturb semantic alterations, RRB structural noise). If ConsistRL generalizes across unseen perturbation types, this evidences learned mathematical structure sensitivity rather than perturbation-specific immunity.

**Why consistency loss, not just augmentation?** Distribution-level consistency provides an explicit inductive bias—same mathematical structure under different surface forms must map to the same reasoning trajectory. This structural constraint cannot emerge from data augmentation alone, which merely broadens training distribution without enforcing distributional invariance. PPCL's 10× sample efficiency over pure augmentation (EACL 2024) provides empirical support; the GRPO+augmentation-only baseline directly tests this claim.

Train Qwen3-8B (primary) and Qwen3-1.5B (ablation/scaling validation) on MATH/AMC/AIME, 8×H100.

## Detailed Description

**Invariance objective.** JS-divergence enforces output-distribution invariance across equivalence-preserving perturbations, applied at high-entropy decision points (1–3% of tokens per ReasonMaxxer). Perturbation generation uses a hybrid pipeline: VAR-MATH's symbolic pipeline for compatible types (algebra, numerical parameterization) and LLM paraphrasing + SymPy verification for others. Training perturbation quality is validated via: (a) symbolic equivalence verification where applicable, (b) sampled human verification (≥200 problems) reporting equivalence correctness rate, (c) coverage rate reporting across MATH problem types. Entropy gating is validated via explicit ablation: full-sequence vs. entropy-gated application, static base-model entropy vs. dynamic policy entropy, threshold sensitivity analysis.

**Discrimination objective.** Contrastive loss penalizes output similarity on semantics-altering hard perturbations, targeting implicit mathematical structure verification. Training data generated via GPT-4 pipeline following MATH-Perturb's hard perturbation taxonomy (condition change, constraint addition, etc.), with: (a) SymPy verification that generated problems have unique solutions differing from originals, (b) human verification (≥300 problems, 2 annotators, reporting inter-annotator agreement), (c) strict train/eval separation from all evaluation benchmarks. This approaches "blind technique application" via implicit distributional constraints, complementing RULES' explicit eligibility reasoning approach.

**Advantage pooling.** TA-GRPO-style pooling across perturbation groups mitigates zero-gradient problems while ensuring mixed reward signals.

## Experimental Design

**Models:** Qwen3-8B (primary), Qwen3-1.5B (ablation + scaling). Two-phase execution: Phase 1 on 1.5B (full ablation + preliminary baselines), Phase 2 on 8B (core baselines + key ablations). Community checkpoints used where available.

**Baselines (8):** (1) Vanilla GRPO, (2) DAPO (arXiv 2503.14476), (3) Dr.GRPO, (4) TA-GRPO (arXiv 2601.22478), (5) COPO (arXiv 2508.04138), (6) GRPO + augmentation-only (same perturbation data, no consistency losses), (7) ReasonMaxxer (arXiv 2605.06241), (8) AbstRaL (ICLR 2026, GSM-level subset only).

**Evaluation benchmarks (grouped by perturbation type):**
- *Numerical equivalence:* VAR-MATH (AMC23/AIME24/AIME25) — core evaluation
- *Semantic discrimination:* MATH-Perturb (MATH-P-Simple and MATH-P-Hard, reported separately) — core evaluation
- *Structural noise (supplementary):* Robust Reasoning Benchmark (arXiv 2604.08571) — out-of-scope for core claim, reported as cross-perturbation transfer observation
- *Clean accuracy:* MATH-500

**Metrics:** VAR-MATH strict/loose consistency rate with bootstrapping 95% CIs; robustness gap (clean − perturbed accuracy); per-benchmark accuracy with CIs; clean accuracy non-degradation criterion (MATH-500 drop ≤ 1%, paired bootstrap test p < 0.05).

**Targets:** VAR-MATH strict consistency rate absolute improvement ≥10 pp over vanilla GRPO; robustness gap reduction ≥15 pp; MATH-P-Hard accuracy improvement ≥5 pp; clean MATH-500 drop ≤ 1%.

**Ablation matrix:** (1) ConsistRL full, (2) w/o JS-divergence, (3) w/o contrastive discrimination, (4) w/o entropy gating (all tokens), (5) w/o advantage pooling, (6) JS-divergence only + entropy gating (minimal). Extensions (primarily at 1.5B): static vs. dynamic entropy gating, entropy threshold sensitivity, perturbation type separation (variable renaming vs. numerical reparameterization), loss weight sensitivity (λ₁, λ₂ grid).

**Compute fairness:** Dual protocol—Protocol A (step-matched): same training steps, report per-method FLOPs and wall-clock time; Protocol B (FLOP-matched): same total FLOPs, ConsistRL uses fewer steps. Report per-step overhead ratio. Robustness vs. cumulative FLOPs curve.

## Key References

- Reinforcing Multimodal Reasoning Against Visual Degradation / ROMA (arXiv 2605.09262, 2026)
- Transform-Augmented GRPO Improves Pass@k / TA-GRPO (arXiv 2601.22478, 2026)
- CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (arXiv 2603.10101, 2026)
- RULES: Reliable Use of Lemmas via Eligibility Reasoning (arXiv 2602.00998, 2026)
- Beyond Correctness: Learning Robust Reasoning via Transfer / RLTR (arXiv 2602.08489, 2026)
- Prompt Perturbation Consistency Learning / PPCL (EACL Findings 2024, ACL 2024)
- MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations (ICML 2025)
- GSM-Symbolic: Understanding Limitations of Mathematical Reasoning in LLMs (ICLR 2025)
- AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking (ICLR 2026)
- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2507.12885, 2025)
- Rethinking RL for LLM Reasoning / ReasonMaxxer (arXiv 2605.06241, 2026)
- Robust Reasoning Benchmark (arXiv 2604.08571, 2026)
- GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (arXiv 2506.16141, 2025)
- COPO: Consistency-Aware Policy Optimization (arXiv 2508.04138, 2025)
- DAPO: An Open-Source LLM Reinforcement Learning System at Scale (arXiv 2503.14476, 2025)
- Dr.GRPO: Group Relative Policy Optimization Done Right

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "37f902eb-8578-49dc-93f5-cce63d8425a9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T08:35:44.937Z_

```json
{
  "parentUuid": "37f902eb-8578-49dc-93f5-cce63d8425a9",
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
  "uuid": "d0ba0b14-2978-4f70-a8a3-a8f8c4af9cc8",
  "timestamp": "2026-05-29T08:35:44.937Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T08:35:44.937Z_

```json
{
  "parentUuid": "d0ba0b14-2978-4f70-a8a3-a8f8c4af9cc8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "dfc00c0c-58aa-4135-9592-20980b8034df",
  "timestamp": "2026-05-29T08:35:44.937Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
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
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Assistant

_source line 7 · 2026-05-29T08:35:49.291Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. I need to first do web searches to understand the current research landscape, then provide a comprehensive evaluation following the specified format.

Let me start by searching for the key topics and papers mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfc00c0c-58aa-4135-9592-20980b8034df",
  "isSidechain": false,
  "requestId": "req_011CbWZ6m9ZCKZ7shKYSsU5u",
  "type": "assistant",
  "uuid": "f82ab6f5-98d3-416c-9767-dd89cce85860",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jpkm5qdpcseisvg9sjhtyP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 18225,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 8 · 2026-05-29T08:35:50.321Z_

I'll start by conducting thorough web searches to understand the research landscape before evaluating this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f82ab6f5-98d3-416c-9767-dd89cce85860",
  "isSidechain": false,
  "requestId": "req_011CbWZ6m9ZCKZ7shKYSsU5u",
  "type": "assistant",
  "uuid": "14914f6d-5790-4c49-ab1c-2c3fe8a5ae74",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jpkm5qdpcseisvg9sjhtyP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 18225,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-29T08:35:50.746Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QLWXxBYNM6esUKDgWKrd8c`</summary>

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
  "parentUuid": "14914f6d-5790-4c49-ab1c-2c3fe8a5ae74",
  "isSidechain": false,
  "requestId": "req_011CbWZ6m9ZCKZ7shKYSsU5u",
  "type": "assistant",
  "uuid": "03102568-48ca-4276-abe6-e63794e1949d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jpkm5qdpcseisvg9sjhtyP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 18225,
      "output_tokens": 171,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 171,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-29T08:35:50.756Z_

<details><summary>↩ Tool result · `toolu_01QLWXxBYNM6esUKDgWKrd8c`</summary>

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
  "parentUuid": "03102568-48ca-4276-abe6-e63794e1949d",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "8cb248c2-224b-4a0e-9912-1157f9f0c5a1",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "03102568-48ca-4276-abe6-e63794e1949d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reas…",
  "leafUuid": "8cb248c2-224b-4a0e-9912-1157f9f0c5a1",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Assistant

_source line 13 · 2026-05-29T08:36:06.160Z_

Now let me conduct the research searches in parallel to understand the landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cb248c2-224b-4a0e-9912-1157f9f0c5a1",
  "isSidechain": false,
  "requestId": "req_011CbWZ7C5zk8SNydy6xmTdJ",
  "type": "assistant",
  "uuid": "417858b5-e7c9-49de-b3c7-bb6b04ba3240",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rrTz3GJE29zVddWiSgbiY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 18225,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 14 · 2026-05-29T08:36:07.228Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YVELvVKm4iYFcrJ6adYwqh`</summary>

```json
{
  "query": "RLVR mathematical reasoning robustness perturbation consistency 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "417858b5-e7c9-49de-b3c7-bb6b04ba3240",
  "isSidechain": false,
  "requestId": "req_011CbWZ7C5zk8SNydy6xmTdJ",
  "type": "assistant",
  "uuid": "89d89066-26f1-4c14-9fcd-bbd676d8e758",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rrTz3GJE29zVddWiSgbiY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 18225,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 15 · 2026-05-29T08:36:08.107Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0158nCt3fWeXdbDLzEFtpF4Q`</summary>

```json
{
  "query": "VAR-MATH symbolic benchmark probing mathematical reasoning perturbation robustness arXiv 2507.12885"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89d89066-26f1-4c14-9fcd-bbd676d8e758",
  "isSidechain": false,
  "requestId": "req_011CbWZ7C5zk8SNydy6xmTdJ",
  "type": "assistant",
  "uuid": "05019710-2824-4337-a075-29b216bbf343",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rrTz3GJE29zVddWiSgbiY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 18225,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 16 · 2026-05-29T08:36:08.643Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ztmLbaEVHmPX24NLHomt4`</summary>

```json
{
  "query": "MATH-Perturb blind technique application LLM reasoning ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05019710-2824-4337-a075-29b216bbf343",
  "isSidechain": false,
  "requestId": "req_011CbWZ7C5zk8SNydy6xmTdJ",
  "type": "assistant",
  "uuid": "cb824c12-3963-4c91-9948-99eaf2660ed7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rrTz3GJE29zVddWiSgbiY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 18225,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 17 · 2026-05-29T08:36:09.608Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HPy7i4ZNevcEuYvkJZpth9`</summary>

```json
{
  "query": "ReasonMaxxer rethinking RL LLM reasoning arXiv 2605.06241 sparse policy selection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb824c12-3963-4c91-9948-99eaf2660ed7",
  "isSidechain": false,
  "requestId": "req_011CbWZ7C5zk8SNydy6xmTdJ",
  "type": "assistant",
  "uuid": "0cbe6225-6bed-4582-b020-d9f56ba47e65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rrTz3GJE29zVddWiSgbiY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 18225,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 18 · 2026-05-29T08:36:09.864Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YA5KHf4UbAPFf4Zg2iRteL`</summary>

```json
{
  "query": "consistency regularization reinforcement learning GRPO robustness math reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cbe6225-6bed-4582-b020-d9f56ba47e65",
  "isSidechain": false,
  "requestId": "req_011CbWZ7C5zk8SNydy6xmTdJ",
  "type": "assistant",
  "uuid": "51ea7cde-4c89-47f3-be2a-a9502dbde557",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012rrTz3GJE29zVddWiSgbiY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 699,
      "cache_read_input_tokens": 18225,
      "output_tokens": 313,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 699,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 313,
          "cache_read_input_tokens": 18225,
          "cache_creation_input_tokens": 699,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 699
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

_source line 19 · 2026-05-29T08:36:14.998Z_

<details><summary>↩ Tool result · `toolu_01YVELvVKm4iYFcrJ6adYwqh`</summary>

```text
Web search results for query: "RLVR mathematical reasoning robustness perturbation consistency 2025 2026"

Links: [{"title":"From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning","url":"https://arxiv.org/html/2505.22203"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038v2"},{"title":"Can LLMs Learn to Reason Robustly under Noisy Supervision?","url":"https://arxiv.org/pdf/2604.03993"},{"title":"Beyond Correctness: Learning Robust Reasoning via Transfer","url":"https://arxiv.org/pdf/2602.08489"},{"title":"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview","url":"https://openreview.net/forum?id=4OsgYD7em5"},{"title":"From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.22203"},{"title":"Limits of Generalization in RLVR: Two Case Studies in Mathematical Reasoning","url":"https://arxiv.org/html/2510.27044v1"}]

Based on the search results, here's what I found about RLVR (Reinforcement Learning with Verifiable Reward) and mathematical reasoning research from 2025-2026:

## Overview of RLVR

Reinforcement Learning with Verifiable Rewards (RLVR) has proven highly effective for training reasoning models in domains with clear ground truth, such as math and code. RLVR replaces learned reward models with rule-based verification of the correctness of final answers, which significantly simplifies the training pipeline and alleviates reward hacking.

## Robustness and Vulnerability Concerns

Recent research has identified significant robustness challenges in RLVR systems:

- The policy model exploits vulnerabilities in the verifier by outputting either single simple characters or long sequences of meaningless text to bypass the verifier, suggesting that introducing a model-based verifier implicitly raises the complexity of the environment and reduces its robustness.

- Current rule-based verifiers are not sufficiently accurate even for widely used open-source mathematical datasets, and while pursuing more accurate model-based verifiers is a promising direction, this approach introduces unique vulnerabilities to hacking.

## Consistency and Generalization

RLVR approaches improve sampling consistency while improving final-answer accuracy, though they require substantial training steps. However, systematic examination of RLVR surprisingly found that it does not elicit fundamentally new reasoning patterns, revealing limitations in how this approach enhances reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89d89066-26f1-4c14-9fcd-bbd676d8e758",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "4dea1821-2fca-4761-b884-529f6086718e",
  "toolUseResult": {
    "query": "RLVR mathematical reasoning robustness perturbation consistency 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GiukQViagV96cUcWdcRoW6",
        "content": [
          {
            "title": "From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning",
            "url": "https://arxiv.org/html/2505.22203"
          },
          {
            "title": "Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/html/2506.05038v2"
          },
          {
            "title": "Can LLMs Learn to Reason Robustly under Noisy Supervision?",
            "url": "https://arxiv.org/pdf/2604.03993"
          },
          {
            "title": "Beyond Correctness: Learning Robust Reasoning via Transfer",
            "url": "https://arxiv.org/pdf/2602.08489"
          },
          {
            "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model? | OpenReview",
            "url": "https://openreview.net/forum?id=4OsgYD7em5"
          },
          {
            "title": "From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.22203"
          },
          {
            "title": "Limits of Generalization in RLVR: Two Case Studies in Mathematical Reasoning",
            "url": "https://arxiv.org/html/2510.27044v1"
          }
        ]
      },
      "Based on the search results, here's what I found about RLVR (Reinforcement Learning with Verifiable Reward) and mathematical reasoning research from 2025-2026:\n\n## Overview of RLVR\n\nReinforcement Learning with Verifiable Rewards (RLVR) has proven highly effective for training reasoning models in domains with clear ground truth, such as math and code. RLVR replaces learned reward models with rule-based verification of the correctness of final answers, which significantly simplifies the training pipeline and alleviates reward hacking.\n\n## Robustness and Vulnerability Concerns\n\nRecent research has identified significant robustness challenges in RLVR systems:\n\n- The policy model exploits vulnerabilities in the verifier by outputting either single simple characters or long sequences of meaningless text to bypass the verifier, suggesting that introducing a model-based verifier implicitly raises the complexity of the environment and reduces its robustness.\n\n- Current rule-based verifiers are not sufficiently accurate even for widely used open-source mathematical datasets, and while pursuing more accurate model-based verifiers is a promising direction, this approach introduces unique vulnerabilities to hacking.\n\n## Consistency and Generalization\n\nRLVR approaches improve sampling consistency while improving final-answer accuracy, though they require substantial training steps. However, systematic examination of RLVR surprisingly found that it does not elicit fundamentally new reasoning patterns, revealing limitations in how this approach enhances reasoning capabilities."
    ],
    "durationSeconds": 7.760904330000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "89d89066-26f1-4c14-9fcd-bbd676d8e758",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T08:36:15.044Z_

<details><summary>↩ Tool result · `toolu_015ztmLbaEVHmPX24NLHomt4`</summary>

```text
Web search results for query: "MATH-Perturb blind technique application LLM reasoning ICML 2025"

Links: [{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview","url":"https://openreview.net/forum?id=OZy70UggXr"},{"title":"Published at ICLR 2025 Workshop on Reasoning and Planning for LLMs","url":"https://openreview.net/pdf?id=M8OLGgYK7e"},{"title":"[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/abs/2502.06453"},{"title":"GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://github.com/Kaffaljidhmah2/MATH-Perturb"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/html/2502.06453v2"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://proceedings.mlr.press/v267/huang25k.html"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard   Perturbations","url":"https://arxiv.org/pdf/2502.06453"},{"title":"MATH-Perturb","url":"https://math-perturb.github.io/"},{"title":"ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://icml.cc/virtual/2025/poster/45435"}]

I found comprehensive information about MATH-Perturb from ICML 2025. Here are the key findings:

## Overview

MATH-Perturb is an ICML 2025 paper that benchmarks LLMs' math reasoning abilities against hard perturbations.

## Research Focus

The research investigates whether LLMs' impressive performance on mathematical reasoning tasks is achieved by true reasoning capability or memorization. While prior work explored simple perturbations, this work constructs MATH-P-Simple and MATH-P-Hard datasets, with each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.

## Key Findings

Significant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).

## Novel Form of Memorization

The research identifies a new form of memorization where models memorize problem-solving techniques from the training set and blindly apply them without judging whether the modified settings are still suitable. Using the original unmodified problem and solution for in-context learning can deteriorate this issue.

## Resources

The project is available at https://math-perturb.github.io/, and the evaluation code and dataset are available on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb824c12-3963-4c91-9948-99eaf2660ed7",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "e37d86e5-0581-408e-b45b-3910a1a121e7",
  "toolUseResult": {
    "query": "MATH-Perturb blind technique application LLM reasoning ICML 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CgUedLKWfZyS56xkNTVLTx",
        "content": [
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=OZy70UggXr"
          },
          {
            "title": "Published at ICLR 2025 Workshop on Reasoning and Planning for LLMs",
            "url": "https://openreview.net/pdf?id=M8OLGgYK7e"
          },
          {
            "title": "[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/abs/2502.06453"
          },
          {
            "title": "GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://github.com/Kaffaljidhmah2/MATH-Perturb"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/html/2502.06453v2"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://proceedings.mlr.press/v267/huang25k.html"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard   Perturbations",
            "url": "https://arxiv.org/pdf/2502.06453"
          },
          {
            "title": "MATH-Perturb",
            "url": "https://math-perturb.github.io/"
          },
          {
            "title": "ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://icml.cc/virtual/2025/poster/45435"
          }
        ]
      },
      "I found comprehensive information about MATH-Perturb from ICML 2025. Here are the key findings:\n\n## Overview\n\nMATH-Perturb is an ICML 2025 paper that benchmarks LLMs' math reasoning abilities against hard perturbations.\n\n## Research Focus\n\nThe research investigates whether LLMs' impressive performance on mathematical reasoning tasks is achieved by true reasoning capability or memorization. While prior work explored simple perturbations, this work constructs MATH-P-Simple and MATH-P-Hard datasets, with each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.\n\n## Key Findings\n\nSignificant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).\n\n## Novel Form of Memorization\n\nThe research identifies a new form of memorization where models memorize problem-solving techniques from the training set and blindly apply them without judging whether the modified settings are still suitable. Using the original unmodified problem and solution for in-context learning can deteriorate this issue.\n\n## Resources\n\nThe project is available at https://math-perturb.github.io/, and the evaluation code and dataset are available on GitHub."
    ],
    "durationSeconds": 6.397340454000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cb824c12-3963-4c91-9948-99eaf2660ed7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-29T08:36:16.164Z_

<details><summary>↩ Tool result · `toolu_0158nCt3fWeXdbDLzEFtpF4Q`</summary>

```text
Web search results for query: "VAR-MATH symbolic benchmark probing mathematical reasoning perturbation robustness arXiv 2507.12885"

Links: [{"title":"[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/abs/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in ...","url":"https://arxiv.org/pdf/2507.12885"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885v1"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/html/2507.12885"},{"title":"Towards Robust Mathematical Reasoning","url":"https://arxiv.org/html/2511.01846v1"},{"title":"A Symbolic Framework for Evaluating Mathematical Reasoning and Generalisation with Transformers","url":"https://arxiv.org/html/2305.12563"}]

I found the paper! Here's what I can tell you about it:

## VAR-MATH: Overview

VAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.

## Key Problem It Addresses

The paper identifies two critical shortcomings in existing evaluation protocols: benchmark contamination from publicly available test problems, and evaluation fragility from reliance on single-instance assessments that are sensitive to stochastic outputs.

## How VAR-MATH Works

VAR-MATH converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each, enforcing consistency across structurally equivalent variants and mitigating contamination through bootstrapped metrics.

## Key Findings

The research reveals significant performance drops when models are evaluated on symbolic variants. For example, several 7B-parameter models that previously achieved scores ranging from 36.9 to 78.6 on AMC23 drop to only 2.5 to 56.4 when evaluated on VAR-AMC23, indicating that much of their apparent success may stem from overfitting to benchmark-specific artifacts.

Even frontier systems like DeepSeek-R1 experience notable degradation on more difficult AIME24 and AIME25 variants, with relative drops up to 28.1%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05019710-2824-4337-a075-29b216bbf343",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "e03f4b02-e3c0-4635-b686-445f2cda3c8f",
  "toolUseResult": {
    "query": "VAR-MATH symbolic benchmark probing mathematical reasoning perturbation robustness arXiv 2507.12885",
    "results": [
      {
        "tool_use_id": "srvtoolu_013NSt1i1ZjjeBW3TFs6Kcmk",
        "content": [
          {
            "title": "[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/abs/2507.12885"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in ...",
            "url": "https://arxiv.org/pdf/2507.12885"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in Large Language Models via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/html/2507.12885v1"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/html/2507.12885"
          },
          {
            "title": "Towards Robust Mathematical Reasoning",
            "url": "https://arxiv.org/html/2511.01846v1"
          },
          {
            "title": "A Symbolic Framework for Evaluating Mathematical Reasoning and Generalisation with Transformers",
            "url": "https://arxiv.org/html/2305.12563"
          }
        ]
      },
      "I found the paper! Here's what I can tell you about it:\n\n## VAR-MATH: Overview\n\nVAR-MATH is a symbolic evaluation framework that systematically variabilizes three widely used benchmarks (AMC23, AIME24, and AIME25), enabling contamination-robust and consistency-based assessment of mathematical reasoning.\n\n## Key Problem It Addresses\n\nThe paper identifies two critical shortcomings in existing evaluation protocols: benchmark contamination from publicly available test problems, and evaluation fragility from reliance on single-instance assessments that are sensitive to stochastic outputs.\n\n## How VAR-MATH Works\n\nVAR-MATH converts fixed numerical problems into parameterized templates and requires models to solve multiple instantiations of each, enforcing consistency across structurally equivalent variants and mitigating contamination through bootstrapped metrics.\n\n## Key Findings\n\nThe research reveals significant performance drops when models are evaluated on symbolic variants. For example, several 7B-parameter models that previously achieved scores ranging from 36.9 to 78.6 on AMC23 drop to only 2.5 to 56.4 when evaluated on VAR-AMC23, indicating that much of their apparent success may stem from overfitting to benchmark-specific artifacts.\n\nEven frontier systems like DeepSeek-R1 experience notable degradation on more difficult AIME24 and AIME25 variants, with relative drops up to 28.1%."
    ],
    "durationSeconds": 8.053003052,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "05019710-2824-4337-a075-29b216bbf343",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-29T08:36:18.647Z_

<details><summary>↩ Tool result · `toolu_01YA5KHf4UbAPFf4Zg2iRteL`</summary>

```text
Web search results for query: "consistency regularization reinforcement learning GRPO robustness math reasoning 2026"

Links: [{"title":"Unifying the GRPO Frameworks with Learnable Token ...","url":"https://www.arxiv.org/pdf/2510.06870"},{"title":"CoRPO: Adding a Correctness Bias to GRPO Improves Generalization","url":"https://arxiv.org/pdf/2511.04439"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning ...","url":"https://arxiv.org/pdf/2506.16141"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://arxiv.org/html/2506.16141"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.17508"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models","url":"https://arxiv.org/pdf/2504.09696"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"},{"title":"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/pdf/2601.03661"}]

I found several relevant research papers from 2025-2026 on this topic. Here's what the search results reveal:

## Consistency-Aware GRPO Methods

Recent work compares consistency-aware reinforcement learning approaches against KL-oriented baselines that modify divergence constraints and reward-based alternatives that replace KL penalties with consistency-aware rewards. The GRPO-CARE method uses sparse consistency rewards and shows that standard KL regularization may hinder performance in some contexts.

## GRPO Improvements for Math Reasoning

Several variants of GRPO have been proposed to enhance mathematical reasoning robustness:

- Group Relative Policy Optimization (GRPO) has emerged as a promising alternative to traditional methods like PPO and DPO, primarily due to its efficiency and compatibility with language model training.

- GRPO-LEAD introduces targeted modifications designed to enhance GRPO's effectiveness for mathematical reasoning tasks.

- DRA-GRPO achieves an average accuracy of 58.2% on DeepSeek-R1-Distill-Qwen-1.5B with only 7,000 training samples, highlighting the role of diversity calibration in data-efficient alignment.

- CoRPO proposes a modification to the GRPO objective with baseline clipping, and when trained on coding tasks, CoRPO outperforms GRPO on math, indicating it learns robust, transferable reasoning patterns.

- AMIR-GRPO augments GRPO with an implicit DPO-style contrastive regularizer and consistently outperforms strong GRPO baselines across mathematical reasoning benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51ea7cde-4c89-47f3-be2a-a9502dbde557",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "09f9405c-240e-4dc3-ba09-4c0710393be7",
  "toolUseResult": {
    "query": "consistency regularization reinforcement learning GRPO robustness math reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018KNM9ntWHBHKbVxhn6HBzf",
        "content": [
          {
            "title": "Unifying the GRPO Frameworks with Learnable Token ...",
            "url": "https://www.arxiv.org/pdf/2510.06870"
          },
          {
            "title": "CoRPO: Adding a Correctness Bias to GRPO Improves Generalization",
            "url": "https://arxiv.org/pdf/2511.04439"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning ...",
            "url": "https://arxiv.org/pdf/2506.16141"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2506.16141"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2505.17508"
          },
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2504.09696"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          },
          {
            "title": "AMIR-GRPO: Inducing Implicit Preference Signals into GRPO",
            "url": "https://arxiv.org/pdf/2601.03661"
          }
        ]
      },
      "I found several relevant research papers from 2025-2026 on this topic. Here's what the search results reveal:\n\n## Consistency-Aware GRPO Methods\n\nRecent work compares consistency-aware reinforcement learning approaches against KL-oriented baselines that modify divergence constraints and reward-based alternatives that replace KL penalties with consistency-aware rewards. The GRPO-CARE method uses sparse consistency rewards and shows that standard KL regularization may hinder performance in some contexts.\n\n## GRPO Improvements for Math Reasoning\n\nSeveral variants of GRPO have been proposed to enhance mathematical reasoning robustness:\n\n- Group Relative Policy Optimization (GRPO) has emerged as a promising alternative to traditional methods like PPO and DPO, primarily due to its efficiency and compatibility with language model training.\n\n- GRPO-LEAD introduces targeted modifications designed to enhance GRPO's effectiveness for mathematical reasoning tasks.\n\n- DRA-GRPO achieves an average accuracy of 58.2% on DeepSeek-R1-Distill-Qwen-1.5B with only 7,000 training samples, highlighting the role of diversity calibration in data-efficient alignment.\n\n- CoRPO proposes a modification to the GRPO objective with baseline clipping, and when trained on coding tasks, CoRPO outperforms GRPO on math, indicating it learns robust, transferable reasoning patterns.\n\n- AMIR-GRPO augments GRPO with an implicit DPO-style contrastive regularizer and consistently outperforms strong GRPO baselines across mathematical reasoning benchmarks."
    ],
    "durationSeconds": 8.779108255999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "51ea7cde-4c89-47f3-be2a-a9502dbde557",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-29T08:36:18.848Z_

<details><summary>↩ Tool result · `toolu_01HPy7i4ZNevcEuYvkJZpth9`</summary>

```text
Web search results for query: "ReasonMaxxer rethinking RL LLM reasoning arXiv 2605.06241 sparse policy selection"

Links: [{"title":"[2605.06241] Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning","url":"https://arxiv.org/abs/2605.06241"},{"title":"Rethinking RL for LLM Reasoning: It’s Sparse Policy Selection, Not Capability Learning","url":"https://arxiv.org/html/2605.06241v2"},{"title":"Rethinking RL for LLM Reasoning: It's Sparse Policy ...","url":"https://arxiv.org/pdf/2605.06241"},{"title":"Don't Overthink it. Preferring Shorter Thinking Chains for Improved LLM Reasoning","url":"https://arxiv.org/pdf/2505.17813"},{"title":"$\\textbf{Re}^{2}$: Unlocking LLM Reasoning via Reinforcement Learning with Re-solving","url":"https://arxiv.org/pdf/2603.07197"}]

Based on the search results, I found the arXiv paper you're looking for. Here's what I found:

## ReasonMaxxer: Rethinking RL for LLM Reasoning

The paper argues that reinforcement learning does not teach new strategies to large language models; instead, it redistributes probability mass over solutions the base model already contains.

### Key Findings

Through token-level analysis across multiple model families and RL algorithms, the researchers found that RL's beneficial impact is a sparse, predictable correction concentrated at high-entropy decision points where the model is uncertain which branch to take. Only 1-3% of token positions are affected, and the promoted token always lies within the base model's top-5 alternatives.

### The ReasonMaxxer Method

ReasonMaxxer is a minimal RL-free method that applies contrastive loss only at entropy-gated decision points, using a few hundred base-model rollouts and no online generation. The method generates a small set of rollouts from the base model, uses entropy gating to locate decision points, and applies an advantage-weighted contrastive loss exclusively at those positions, while anchoring all other tokens to the base distribution.

### Performance Results

Across three model families, six scales, and six math reasoning benchmarks, ReasonMaxxer matches or exceeds full RL performance while requiring only tens of problems and minutes of single-GPU training, a reduction in training cost of roughly three orders of magnitude.

The paper identifies reasoning improvement as "sparse policy selection" rather than capability acquisition, fundamentally changing how we approach improving LLM reasoning abilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0cbe6225-6bed-4582-b020-d9f56ba47e65",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "0ff40932-f804-4bfa-8228-825a63e263a7",
  "toolUseResult": {
    "query": "ReasonMaxxer rethinking RL LLM reasoning arXiv 2605.06241 sparse policy selection",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RmJuNjKriwYtD7Z1vF3ycq",
        "content": [
          {
            "title": "[2605.06241] Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning",
            "url": "https://arxiv.org/abs/2605.06241"
          },
          {
            "title": "Rethinking RL for LLM Reasoning: It’s Sparse Policy Selection, Not Capability Learning",
            "url": "https://arxiv.org/html/2605.06241v2"
          },
          {
            "title": "Rethinking RL for LLM Reasoning: It's Sparse Policy ...",
            "url": "https://arxiv.org/pdf/2605.06241"
          },
          {
            "title": "Don't Overthink it. Preferring Shorter Thinking Chains for Improved LLM Reasoning",
            "url": "https://arxiv.org/pdf/2505.17813"
          },
          {
            "title": "$\\textbf{Re}^{2}$: Unlocking LLM Reasoning via Reinforcement Learning with Re-solving",
            "url": "https://arxiv.org/pdf/2603.07197"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper you're looking for. Here's what I found:\n\n## ReasonMaxxer: Rethinking RL for LLM Reasoning\n\nThe paper argues that reinforcement learning does not teach new strategies to large language models; instead, it redistributes probability mass over solutions the base model already contains.\n\n### Key Findings\n\nThrough token-level analysis across multiple model families and RL algorithms, the researchers found that RL's beneficial impact is a sparse, predictable correction concentrated at high-entropy decision points where the model is uncertain which branch to take. Only 1-3% of token positions are affected, and the promoted token always lies within the base model's top-5 alternatives.\n\n### The ReasonMaxxer Method\n\nReasonMaxxer is a minimal RL-free method that applies contrastive loss only at entropy-gated decision points, using a few hundred base-model rollouts and no online generation. The method generates a small set of rollouts from the base model, uses entropy gating to locate decision points, and applies an advantage-weighted contrastive loss exclusively at those positions, while anchoring all other tokens to the base distribution.\n\n### Performance Results\n\nAcross three model families, six scales, and six math reasoning benchmarks, ReasonMaxxer matches or exceeds full RL performance while requiring only tens of problems and minutes of single-GPU training, a reduction in training cost of roughly three orders of magnitude.\n\nThe paper identifies reasoning improvement as \"sparse policy selection\" rather than capability acquisition, fundamentally changing how we approach improving LLM reasoning abilities."
    ],
    "durationSeconds": 9.237796326,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0cbe6225-6bed-4582-b020-d9f56ba47e65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reas…",
  "leafUuid": "0ff40932-f804-4bfa-8228-825a63e263a7",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Tool call

_source line 26 · 2026-05-29T08:36:22.382Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015uE4v3Z2phct7zYTC55pWZ`</summary>

```json
{
  "query": "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262 GRPO consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ff40932-f804-4bfa-8228-825a63e263a7",
  "isSidechain": false,
  "requestId": "req_011CbWZ9FvV1sp9xFT8uitAF",
  "type": "assistant",
  "uuid": "eda49a1d-d2a5-470a-9f2a-9fbe0fa53a9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGWdBhLpsj69kTo2Cwcev6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 3220,
      "cache_read_input_tokens": 18924,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 776,
          "output_tokens": 195,
          "cache_read_input_tokens": 18924,
          "cache_creation_input_tokens": 3220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3220
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

_source line 27 · 2026-05-29T08:36:23.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BJHEUjtWAfR8BxiK61HAeN`</summary>

```json
{
  "query": "TA-GRPO transform augmented GRPO pass@k arXiv 2601.22478 rephrasings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eda49a1d-d2a5-470a-9f2a-9fbe0fa53a9e",
  "isSidechain": false,
  "requestId": "req_011CbWZ9FvV1sp9xFT8uitAF",
  "type": "assistant",
  "uuid": "ffefb7fe-da1c-49d1-bcd5-c035e9a46c80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGWdBhLpsj69kTo2Cwcev6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 3220,
      "cache_read_input_tokens": 18924,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 776,
          "output_tokens": 195,
          "cache_read_input_tokens": 18924,
          "cache_creation_input_tokens": 3220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3220
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

_source line 28 · 2026-05-29T08:36:24.014Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ScAfZc6BQYtMKjN8mFVeqB`</summary>

```json
{
  "query": "AbstRaL abstract thinking reinforcement learning ICLR 2026 robustness math"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ffefb7fe-da1c-49d1-bcd5-c035e9a46c80",
  "isSidechain": false,
  "requestId": "req_011CbWZ9FvV1sp9xFT8uitAF",
  "type": "assistant",
  "uuid": "76013ded-dd4c-4aba-98d0-9c76b475fe13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGWdBhLpsj69kTo2Cwcev6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 776,
      "cache_creation_input_tokens": 3220,
      "cache_read_input_tokens": 18924,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3220,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 776,
          "output_tokens": 195,
          "cache_read_input_tokens": 18924,
          "cache_creation_input_tokens": 3220,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3220
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

_source line 29 · 2026-05-29T08:36:29.930Z_

<details><summary>↩ Tool result · `toolu_015uE4v3Z2phct7zYTC55pWZ`</summary>

```text
Web search results for query: "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262 GRPO consistency"

Links: [{"title":"[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/abs/2605.09262"},{"title":"Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/pdf/2605.09262"},{"title":"Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization","url":"https://arxiv.org/html/2509.21854"},{"title":"Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization","url":"https://arxiv.org/pdf/2604.08476"},{"title":"Self-Rewarded Multimodal Coherent Reasoning Across Diverse Visual Domains","url":"https://arxiv.org/pdf/2512.22545"},{"title":"Answer-Consistent Chain-of-thought Reinforcement Learning For Multi-modal Large Langauge Models","url":"https://arxiv.org/pdf/2510.10104"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://arxiv.org/pdf/2506.16141"},{"title":"Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework","url":"https://arxiv.org/pdf/2509.23322"}]

Based on the search results, here's what I found about this paper:

## ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation

ROMA is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance.

### Key Technical Approach

The framework employs several key mechanisms:

1. **Dual-Forward-Pass Strategy**: A dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs.

2. **Distributional Consistency**: For distributional consistency, the method applies a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories.

### Performance Results

On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.

The paper demonstrates that ROMA matches clean performance (68.7%) while substantially improving robustness, reaching 61.6% on seen and 56.3% on unseen perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eda49a1d-d2a5-470a-9f2a-9fbe0fa53a9e",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "fd20d374-b92d-48ff-83fb-4972a3b87221",
  "toolUseResult": {
    "query": "ROMA reinforcing multimodal reasoning visual degradation arXiv 2605.09262 GRPO consistency",
    "results": [
      {
        "tool_use_id": "srvtoolu_017qDQraX3Fvan5wkenymD6y",
        "content": [
          {
            "title": "[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/abs/2605.09262"
          },
          {
            "title": "Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/pdf/2605.09262"
          },
          {
            "title": "Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization",
            "url": "https://arxiv.org/html/2509.21854"
          },
          {
            "title": "Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization",
            "url": "https://arxiv.org/pdf/2604.08476"
          },
          {
            "title": "Self-Rewarded Multimodal Coherent Reasoning Across Diverse Visual Domains",
            "url": "https://arxiv.org/pdf/2512.22545"
          },
          {
            "title": "Answer-Consistent Chain-of-thought Reinforcement Learning For Multi-modal Large Langauge Models",
            "url": "https://arxiv.org/pdf/2510.10104"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/pdf/2506.16141"
          },
          {
            "title": "Mitigating Visual Context Degradation in Large Multimodal Models: A Training-Free Decoupled Agentic Framework",
            "url": "https://arxiv.org/pdf/2509.23322"
          }
        ]
      },
      "Based on the search results, here's what I found about this paper:\n\n## ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation\n\nROMA is an RL fine-tuning framework that modifies the optimization dynamics to reinforce reasoning against visual degradation while preserving clean-input performance.\n\n### Key Technical Approach\n\nThe framework employs several key mechanisms:\n\n1. **Dual-Forward-Pass Strategy**: A dual-forward-pass strategy uses teacher forcing to evaluate corrupted views against clean-image trajectories, avoiding new rollouts on degraded inputs.\n\n2. **Distributional Consistency**: For distributional consistency, the method applies a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories.\n\n### Performance Results\n\nOn Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy.\n\nThe paper demonstrates that ROMA matches clean performance (68.7%) while substantially improving robustness, reaching 61.6% on seen and 56.3% on unseen perturbations."
    ],
    "durationSeconds": 7.542087623,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "eda49a1d-d2a5-470a-9f2a-9fbe0fa53a9e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-29T08:36:29.976Z_

<details><summary>↩ Tool result · `toolu_01BJHEUjtWAfR8BxiK61HAeN`</summary>

```text
Web search results for query: "TA-GRPO transform augmented GRPO pass@k arXiv 2601.22478 rephrasings"

Links: [{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"(PDF) Transform-Augmented GRPO Improves Pass@k","url":"https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/html/2601.22478v2"},{"title":"[2601.03661] AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/abs/2601.03661"}]

I found the paper! Here's what the research shows:

TA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question via paraphrasing, variable renaming, and format changes, and computes advantages by pooling rewards across the entire group.

The paper addresses two key problems with standard GRPO: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.

Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).

Regarding the specific rephrasings used: The method employs prompts to rephrase math problems using different wording while preserving mathematical meaning, rename variables and entities while keeping mathematical structure identical, and reformat questions by changing style while preserving exact mathematical content.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ffefb7fe-da1c-49d1-bcd5-c035e9a46c80",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "8979ea06-19ce-4088-a97d-b3910e7685e2",
  "toolUseResult": {
    "query": "TA-GRPO transform augmented GRPO pass@k arXiv 2601.22478 rephrasings",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JsfpDoQo9XjhNEBJhdg8L4",
        "content": [
          {
            "title": "[2601.22478] Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/abs/2601.22478"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/pdf/2601.22478"
          },
          {
            "title": "(PDF) Transform-Augmented GRPO Improves Pass@k",
            "url": "https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/html/2601.22478v2"
          },
          {
            "title": "[2601.03661] AMIR-GRPO: Inducing Implicit Preference Signals into GRPO",
            "url": "https://arxiv.org/abs/2601.03661"
          }
        ]
      },
      "I found the paper! Here's what the research shows:\n\nTA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question via paraphrasing, variable renaming, and format changes, and computes advantages by pooling rewards across the entire group.\n\nThe paper addresses two key problems with standard GRPO: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.\n\nExperiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond).\n\nRegarding the specific rephrasings used: The method employs prompts to rephrase math problems using different wording while preserving mathematical meaning, rename variables and entities while keeping mathematical structure identical, and reformat questions by changing style while preserving exact mathematical content."
    ],
    "durationSeconds": 6.649891847999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ffefb7fe-da1c-49d1-bcd5-c035e9a46c80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-29T08:36:31.986Z_

<details><summary>↩ Tool result · `toolu_01ScAfZc6BQYtMKjN8mFVeqB`</summary>

```text
Web search results for query: "AbstRaL abstract thinking reinforcement learning ICLR 2026 robustness math"

Links: [{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/html/2506.07751"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/abstral"},{"title":"AbstRaL: Teaching LLMs Abstract Reasoning via Reinforcement to Boost Robustness on GSM Benchmarks - MarkTechPost","url":"https://www.marktechpost.com/2025/07/05/abstral-teaching-llms-abstract-reasoning-via-reinforcement-to-boost-robustness-on-gsm-benchmarks/"},{"title":"[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/abs/2506.07751"},{"title":"International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-iclr-2026"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | OpenReview","url":"https://openreview.net/forum?id=49vo7D9LbI"},{"title":"ABSTRAL: AUGMENTING LLMS' REASONING BY ...","url":"https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://arxiv.org/pdf/2507.10624"}]

I found information about AbstRaL! Here's what the search reveals:

## AbstRaL: Abstract Thinking Reinforcement Learning

AbstRaL is a method which promotes abstract reasoning in LLMs using RL on granular abstraction data, and it was presented as a poster at ICLR 2026 (Poster Session 3, Pavilion 4, #4615) with authors Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe.

### Key Findings on Robustness

The method significantly mitigates performance degradation on recent GSM perturbation benchmarks, and improving GSM robustness via AbstRaL also implicitly benefits LLMs' capabilities on OOD mathematical and general reasoning tasks.

The abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions.

### Performance on Math Benchmarks

AbstRaL was tested on GSM-Symbolic and GSM-Plus benchmarks, and experimental results consistently demonstrate that AbstRaL effectively improves the GSM reasoning robustness of LLMs, almost reverting the performance drop caused by variations of relevant input conditions and significantly mitigating the interference of distracting conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76013ded-dd4c-4aba-98d0-9c76b475fe13",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "eb38f42e-5ad2-4dc5-93f1-2d341fc7dbd4",
  "toolUseResult": {
    "query": "AbstRaL abstract thinking reinforcement learning ICLR 2026 robustness math",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KBjYHiZtydxKvyhW4Jrw3v",
        "content": [
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/pdf/2506.07751"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/html/2506.07751"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/abstral"
          },
          {
            "title": "AbstRaL: Teaching LLMs Abstract Reasoning via Reinforcement to Boost Robustness on GSM Benchmarks - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/07/05/abstral-teaching-llms-abstract-reasoning-via-reinforcement-to-boost-robustness-on-gsm-benchmarks/"
          },
          {
            "title": "[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/abs/2506.07751"
          },
          {
            "title": "International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/updates/apple-at-iclr-2026"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking | OpenReview",
            "url": "https://openreview.net/forum?id=49vo7D9LbI"
          },
          {
            "title": "ABSTRAL: AUGMENTING LLMS' REASONING BY ...",
            "url": "https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (11/2025)",
            "url": "https://arxiv.org/pdf/2507.10624"
          }
        ]
      },
      "I found information about AbstRaL! Here's what the search reveals:\n\n## AbstRaL: Abstract Thinking Reinforcement Learning\n\nAbstRaL is a method which promotes abstract reasoning in LLMs using RL on granular abstraction data, and it was presented as a poster at ICLR 2026 (Poster Session 3, Pavilion 4, #4615) with authors Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe.\n\n### Key Findings on Robustness\n\nThe method significantly mitigates performance degradation on recent GSM perturbation benchmarks, and improving GSM robustness via AbstRaL also implicitly benefits LLMs' capabilities on OOD mathematical and general reasoning tasks.\n\nThe abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions.\n\n### Performance on Math Benchmarks\n\nAbstRaL was tested on GSM-Symbolic and GSM-Plus benchmarks, and experimental results consistently demonstrate that AbstRaL effectively improves the GSM reasoning robustness of LLMs, almost reverting the performance drop caused by variations of relevant input conditions and significantly mitigating the interference of distracting conditions."
    ],
    "durationSeconds": 7.969147490999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "76013ded-dd4c-4aba-98d0-9c76b475fe13",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-29T08:36:31.991Z_

```json
{
  "parentUuid": "eb38f42e-5ad2-4dc5-93f1-2d341fc7dbd4",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "07ddc195-cfe9-443c-8c9f-30165cb4dc10",
  "timestamp": "2026-05-29T08:36:31.991Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-29T08:36:34.760Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have a solid understanding of the landscape. Let me do a couple more targeted searches to fill in gaps.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07ddc195-cfe9-443c-8c9f-30165cb4dc10",
  "isSidechain": false,
  "requestId": "req_011CbWZAE8raAnShmgqnq5dA",
  "type": "assistant",
  "uuid": "600ac209-f476-4b71-80bc-011a101250c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjyDBWFqVYdd9DGGuAncKL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 22144,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 22144,
          "cache_creation_input_tokens": 3249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3249
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

_source line 34 · 2026-05-29T08:36:35.206Z_

Let me do a couple more targeted searches to fully understand the competitive landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600ac209-f476-4b71-80bc-011a101250c0",
  "isSidechain": false,
  "requestId": "req_011CbWZAE8raAnShmgqnq5dA",
  "type": "assistant",
  "uuid": "28e4dd24-0c86-440a-824c-9a749ff628ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjyDBWFqVYdd9DGGuAncKL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 22144,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 22144,
          "cache_creation_input_tokens": 3249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3249
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

_source line 35 · 2026-05-29T08:36:36.736Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015mKUJaX1w5E966LAc3mZrf`</summary>

```json
{
  "query": "PPCL prompt perturbation consistency learning JS divergence EACL 2024 sample efficiency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28e4dd24-0c86-440a-824c-9a749ff628ac",
  "isSidechain": false,
  "requestId": "req_011CbWZAE8raAnShmgqnq5dA",
  "type": "assistant",
  "uuid": "f779c77c-c481-4063-b489-2e54f333c139",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjyDBWFqVYdd9DGGuAncKL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 22144,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 22144,
          "cache_creation_input_tokens": 3249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3249
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

_source line 36 · 2026-05-29T08:36:37.600Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xq9C4fjwFJKWXY3GJHjguM`</summary>

```json
{
  "query": "CLIPO contrastive learning policy optimization GRPO arXiv 2603.10101 trajectory invariance"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f779c77c-c481-4063-b489-2e54f333c139",
  "isSidechain": false,
  "requestId": "req_011CbWZAE8raAnShmgqnq5dA",
  "type": "assistant",
  "uuid": "9352fffd-8e21-47fb-9a4f-638d6b2c73e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjyDBWFqVYdd9DGGuAncKL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3249,
      "cache_read_input_tokens": 22144,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3249,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 22144,
          "cache_creation_input_tokens": 3249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3249
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

_source line 37 · 2026-05-29T08:36:43.575Z_

<details><summary>↩ Tool result · `toolu_015mKUJaX1w5E966LAc3mZrf`</summary>

```text
Web search results for query: "PPCL prompt perturbation consistency learning JS divergence EACL 2024 sample efficiency"

Links: [{"title":"Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.91/"},{"title":"[Literature Review] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://www.themoonlight.io/en/review/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Prompt perturbation consistency learning for robust language models - Amazon Science","url":"https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"[2402.15833] Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/abs/2402.15833"},{"title":"Prompt Perturbation Experiments","url":"https://www.emergentmind.com/topics/prompt-perturbation-experiments"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://openreview.net/pdf/6531be6f8b4a39b29dc72a3ad3d4fd6eba931edb.pdf"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models","url":"https://arxiv.org/pdf/2402.15833"},{"title":"Prompt Perturbation Consistency Learning for Robust Language Models | Underline","url":"https://underline.io/lecture/95602-prompt-perturbation-consistency-learning-for-robust-language-models"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/pdf/2510.14242"}]

I found information about the paper you're searching for! Here's what the search reveals:

## PPCL: Prompt Perturbation Consistency Learning

The paper "Prompt Perturbation Consistency Learning for Robust Language Models" was published in Findings of the Association for Computational Linguistics: EACL 2024.

### Key Methodology

PPCL is an efficient mitigation approach that works by regularizing the divergence between losses from clean and perturbed samples. More specifically, PPCL regularizes the divergence (Jensen-Shannon) between the output distributions for clean and perturbed prompts.

### Performance on Sample Efficiency

PPCL beats data augmentation approaches while using ten times fewer augmented data samples. This demonstrates a significant sample efficiency advantage over traditional data augmentation methods.

### Results

PPCL can recover on average 59% and 69% of the performance drop for IC (Intent Classification) and SF (Slot Filling) tasks, respectively, while also beating data augmentation approaches.

### Problem Addressed

The paper analyzes the performance deterioration of fine-tuned models due to three distinct yet relevant types of input perturbations - oronyms, synonyms, and paraphrasing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f779c77c-c481-4063-b489-2e54f333c139",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "e1fbd56e-6e4a-4d0a-bbe8-e7402c553ede",
  "toolUseResult": {
    "query": "PPCL prompt perturbation consistency learning JS divergence EACL 2024 sample efficiency",
    "results": [
      {
        "tool_use_id": "srvtoolu_013GxQVQMRKB7qigw6cY4DSA",
        "content": [
          {
            "title": "Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-eacl.91/"
          },
          {
            "title": "[Literature Review] Prompt Perturbation Consistency Learning for Robust Language Models",
            "url": "https://www.themoonlight.io/en/review/prompt-perturbation-consistency-learning-for-robust-language-models"
          },
          {
            "title": "Prompt perturbation consistency learning for robust language models - Amazon Science",
            "url": "https://www.amazon.science/publications/prompt-perturbation-consistency-learning-for-robust-language-models"
          },
          {
            "title": "[2402.15833] Prompt Perturbation Consistency Learning for Robust Language Models",
            "url": "https://arxiv.org/abs/2402.15833"
          },
          {
            "title": "Prompt Perturbation Experiments",
            "url": "https://www.emergentmind.com/topics/prompt-perturbation-experiments"
          },
          {
            "title": "Prompt Perturbation Consistency Learning for Robust Language Models",
            "url": "https://openreview.net/pdf/6531be6f8b4a39b29dc72a3ad3d4fd6eba931edb.pdf"
          },
          {
            "title": "Prompt Perturbation Consistency Learning for Robust Language Models",
            "url": "https://arxiv.org/pdf/2402.15833"
          },
          {
            "title": "Prompt Perturbation Consistency Learning for Robust Language Models | Underline",
            "url": "https://underline.io/lecture/95602-prompt-perturbation-consistency-learning-for-robust-language-models"
          },
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/pdf/2510.14242"
          }
        ]
      },
      "I found information about the paper you're searching for! Here's what the search reveals:\n\n## PPCL: Prompt Perturbation Consistency Learning\n\nThe paper \"Prompt Perturbation Consistency Learning for Robust Language Models\" was published in Findings of the Association for Computational Linguistics: EACL 2024.\n\n### Key Methodology\n\nPPCL is an efficient mitigation approach that works by regularizing the divergence between losses from clean and perturbed samples. More specifically, PPCL regularizes the divergence (Jensen-Shannon) between the output distributions for clean and perturbed prompts.\n\n### Performance on Sample Efficiency\n\nPPCL beats data augmentation approaches while using ten times fewer augmented data samples. This demonstrates a significant sample efficiency advantage over traditional data augmentation methods.\n\n### Results\n\nPPCL can recover on average 59% and 69% of the performance drop for IC (Intent Classification) and SF (Slot Filling) tasks, respectively, while also beating data augmentation approaches.\n\n### Problem Addressed\n\nThe paper analyzes the performance deterioration of fine-tuned models due to three distinct yet relevant types of input perturbations - oronyms, synonyms, and paraphrasing."
    ],
    "durationSeconds": 6.834705441999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f779c77c-c481-4063-b489-2e54f333c139",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reas…",
  "leafUuid": "e1fbd56e-6e4a-4d0a-bbe8-e7402c553ede",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Tool result

_source line 40 · 2026-05-29T08:36:45.490Z_

<details><summary>↩ Tool result · `toolu_01Xq9C4fjwFJKWXY3GJHjguM`</summary>

```text
Web search results for query: "CLIPO contrastive learning policy optimization GRPO arXiv 2603.10101 trajectory invariance"

Links: [{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/html/2603.10101v1"},{"title":"[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/abs/2603.10101"},{"title":"GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub","url":"https://github.com/Qwen-Applications/CLIPO"},{"title":"Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://huggingface.co/papers/2603.10101"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/pdf/2603.10101"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://www.researchgate.net/publication/401833359_CLIPO_Contrastive_Learning_in_Policy_Optimization_Generalizes_RLVR"},{"title":"Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models","url":"https://arxiv.org/html/2605.25443"}]

I found comprehensive information about CLIPO and the arXiv paper 2603.10101. Here's what the search results reveal:

## CLIPO Overview

CLIPO incorporates a Contrastive Learning mechanism into Policy Optimization to generalize the RLVR (Reinforcement Learning with Verifiable Rewards) process.

## The Problem It Addresses

RLVR solely relies on final answers as outcome rewards, neglecting the correctness of intermediate reasoning steps, and training on process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying, severely undermining the model's generalization and robustness.

## Key Innovation: Trajectory Invariance

By optimizing a contrastive loss over successful rollouts, CLIPO steers the LLM to capture the invariant structure shared across correct reasoning paths. By aligning multiple successful reasoning trajectories and contrasting them against incorrect ones, the method extracts invariant reasoning structures shared by correct rollouts.

## Benefits Over Traditional Approaches

This provides a more robust cross-trajectory regularization than the original single-path supervision in RLVR, effectively mitigating step-level reasoning inconsistencies and suppressing hallucinatory artifacts.

## Implementation

CLIPO introduces a lightweight contrastive head and an intra-group contrastive objective into RLVR-style policy optimization. The framework integrates with group-based policy optimization methods like GRPO and consistently improves multiple RLVR baselines across diverse reasoning benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9352fffd-8e21-47fb-9a4f-638d6b2c73e1",
  "isSidechain": false,
  "promptId": "d4291b93-88b4-4ca5-b70f-a56c6ce58e73",
  "type": "user",
  "uuid": "fd0babca-0669-44ed-8e3e-b819fdaa3c0e",
  "toolUseResult": {
    "query": "CLIPO contrastive learning policy optimization GRPO arXiv 2603.10101 trajectory invariance",
    "results": [
      {
        "tool_use_id": "srvtoolu_018ApaebVwht8B7SagUDAGRy",
        "content": [
          {
            "title": "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/html/2603.10101v1"
          },
          {
            "title": "[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/abs/2603.10101"
          },
          {
            "title": "GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub",
            "url": "https://github.com/Qwen-Applications/CLIPO"
          },
          {
            "title": "Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://huggingface.co/papers/2603.10101"
          },
          {
            "title": "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/pdf/2603.10101"
          },
          {
            "title": "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://www.researchgate.net/publication/401833359_CLIPO_Contrastive_Learning_in_Policy_Optimization_Generalizes_RLVR"
          },
          {
            "title": "Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models",
            "url": "https://arxiv.org/html/2605.25443"
          }
        ]
      },
      "I found comprehensive information about CLIPO and the arXiv paper 2603.10101. Here's what the search results reveal:\n\n## CLIPO Overview\n\nCLIPO incorporates a Contrastive Learning mechanism into Policy Optimization to generalize the RLVR (Reinforcement Learning with Verifiable Rewards) process.\n\n## The Problem It Addresses\n\nRLVR solely relies on final answers as outcome rewards, neglecting the correctness of intermediate reasoning steps, and training on process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying, severely undermining the model's generalization and robustness.\n\n## Key Innovation: Trajectory Invariance\n\nBy optimizing a contrastive loss over successful rollouts, CLIPO steers the LLM to capture the invariant structure shared across correct reasoning paths. By aligning multiple successful reasoning trajectories and contrasting them against incorrect ones, the method extracts invariant reasoning structures shared by correct rollouts.\n\n## Benefits Over Traditional Approaches\n\nThis provides a more robust cross-trajectory regularization than the original single-path supervision in RLVR, effectively mitigating step-level reasoning inconsistencies and suppressing hallucinatory artifacts.\n\n## Implementation\n\nCLIPO introduces a lightweight contrastive head and an intra-group contrastive objective into RLVR-style policy optimization. The framework integrates with group-based policy optimization methods like GRPO and consistently improves multiple RLVR baselines across diverse reasoning benchmarks."
    ],
    "durationSeconds": 7.886531985000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9352fffd-8e21-47fb-9a4f-638d6b2c73e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-29T08:37:22.856Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the research landscape. Let me synthesize my findings and provide the evaluation.

Let me think carefully about this proposal:

**Core Idea:** Extend GRPO with dual consistency objectives for mathematical reasoning robustness:
1. JS-divergence invariance loss for equivalence-preserving perturbations (variable renaming, numerical reparameterization)
2. Contrastive discrimination loss for semantics-altering perturbations
3. TA-GRPO-style advantage pooling

**Strengths I see:**
1. The problem is real and well-documented (VAR-MATH, MATH-Perturb, GSM-Symbolic all document significant drops)


2. The dual objective framing combining invariance with discrimination is genuinely novel—I haven't seen this pairing in existing work
3. The experimental rigor is impressive with eight baselines, multiple evaluation benchmarks, compute fairness protocols, and comprehensive ablations
4. The positioning against related work demonstrates deep understanding of the field
5. The entropy-gating mechanism from ReasonMaxxer integrates cleanly into the approach
6. The computational requirements are realistic for the scope

**Concerns:**
1. **Novelty concern**: While the dual objective combination is fresh, the individual components draw from existing techniques—JS-divergence consistency appears in PPCL, contrastive discrimination is well-established, and advantage pooling comes from TA-GRPO with entropy gating from ReasonMaxxer. The real contribution is synthesizing these for math reasoning robustness in RL, which might be incremental for AAAI. Though to be fair, the insight about math perturbation spaces having a structural duality—where some transformations preserve equivalence while others alter semantics—is a genuine conceptual contribution beyond just combining existing pieces.

2. **Perturbation generation quality**: The hybrid pipeline mixing VAR-MATH symbolic generation with LLM paraphrasing and SymPy verification is intricate, and everything hinges on whether the perturbations are actually high-quality. They mitigate this with human verification across 200+ invariance problems and 300+ discrimination problems, which provides reasonable confidence.

3. **Whether the improvements will actually materialize**—I need to think through whether the gains are likely to be substantial enough. to be significant?** ROMA only gets +2.4%/+2.3% with a similar token-level KL consistency approach (though in visual domain). The targets here are more ambitious (≥10pp consistency improvement, ≥15pp robustness gap reduction, ≥5pp MATH-P-Hard). Are these realistic?
   - The targets seem ambitious but not unreasonable given that the problem is more severe in math (47-73% drops) than in vision.

4. **Method complexity**: Three losses + entropy gating + hybrid perturbation pipeline = a lot of moving parts. The ablation matrix addresses this, but there's risk that the method is overengineered.

5. **ReasonMaxxer challenge**: If ReasonMaxxer can match full RL with just contrastive loss at entropy-gated decision points using a few hundred rollouts and minutes of single-GPU training, why do we need the full ConsistRL framework? This is a strong baseline that the paper must convincingly beat.

6. **Clean accuracy preservation**: The ≤1% drop criterion on MATH-500 is important but may be hard to achieve with the added regularization.

The proposal is well-structured with a clear research question and thorough experimental design, and the dual-objective framing genuinely differentiates it from single-objective approaches. That said, the method largely combines existing techniques—JS-divergence, contrastive learning, advantage pooling, entropy gating—rather than introducing novel components, so the contribution is more in the problem formulation and careful integration. The experimental rigor is a major strength with eight baselines, multiple benchmarks, compute fairness protocols, and comprehensive ablations.

The main risks are modest gains that don't justify the added complexity, ReasonMaxxer being a formidable baseline, and the perturbation pipeline quality being undervalidated. Weighing the important problem and exceptional experimental design against the incremental novelty and strong baseline threats, I'd estimate this around 30-40% probability of acceptance—it's a solid, well-designed proposal with clear contributions, but the core innovation is primarily in problem framing and technique combination rather than fundamental methodological breakthroughs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd0babca-0669-44ed-8e3e-b819fdaa3c0e",
  "isSidechain": false,
  "requestId": "req_011CbWZBDq2rccrFKvrPpPau",
  "type": "assistant",
  "uuid": "4e77fd06-67fa-4b31-9ce6-a7605aa0f20c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiSZ7hnFa92cJYXfq1YD5F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 25393,
      "output_tokens": 6568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6568,
          "cache_read_input_tokens": 25393,
          "cache_creation_input_tokens": 1761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1761
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

_source line 42 · 2026-05-29T08:39:20.500Z_

Now I have a comprehensive understanding of the research landscape. Let me compile my evaluation.

---

```
【阶段】: Triage

【领域调研】:
- [VAR-MATH (arXiv 2507.12885)](https://arxiv.org/abs/2507.12885) (2025): 核心评测基准之一。通过符号化参数模板暴露了 7B RL 模型 47.9–72.9% 的严重一致性下降，直接支撑本 proposal 的 problem statement。同时提供了符号化扰动生成 pipeline，被 proposal 直接复用。
- [MATH-Perturb (ICML 2025)](https://arxiv.org/abs/2502.06453): 核心评测基准之二。发现"blind technique application"失败模式——o1-mini ~40% 的 hard perturbation 错误来自盲目套用记忆策略。proposal 的 discrimination objective 直接针对此失败模式。验证了 proposal 的 problem framing 有实证基础。
- [ReasonMaxxer (arXiv 2605.06241)](https://arxiv.org/abs/2605.06241) (May 2026): **高威胁竞争者**。证明 RL 仅在 1-3% 的高熵 token 上做"稀疏策略选择"，提出 RL-free 的 contrastive loss 方法，用几百个 rollout、几分钟单 GPU 训练即可匹配全量 RL 性能。Proposal 借用了其 entropy-gating insight，但必须在实验中 convincingly beat 这个极简 baseline。
- [ROMA (arXiv 2605.09262)](https://arxiv.org/abs/2605.09262) (May 2026): 最直接的方法论竞争者。在 GRPO 中加入 token-level KL 一致性用于视觉鲁棒性，但增益仅 +2.4%/+2.3%（seen/unseen）。与 proposal 的 JS-divergence invariance loss 高度同构，仅域不同（视觉 vs 数学文本）。
- [TA-GRPO (arXiv 2601.22478)](https://arxiv.org/abs/2601.22478) (Jan 2026): proposal 直接借用其 advantage pooling 机制。该方法在竞赛数学上 pass@k 提升至 9.84 points，但没有显式 consistency loss，也未评估鲁棒性。
- [CLIPO (arXiv 2603.10101)](https://arxiv.org/abs/2603.10101) (Mar 2026): 在 GRPO 中引入 trajectory-level contrastive learning，提取正确推理路径的不变结构。与 proposal 正交——CLIPO 处理 trajectory 噪声，ConsistRL 处理 input surface-form 噪声。
- [AbstRaL (ICLR 2026)](https://arxiv.org/abs/2506.07751): 通过 RL 强化抽象思维实现 GSM-level 鲁棒性，但明确限于初等数学。Proposal 正确地将其定位为 GSM-only baseline。
- [PPCL (EACL Findings 2024)](https://aclanthology.org/2024.findings-eacl.91/): JS-divergence 一致性正则化在 NLP 任务上比纯数据增强高 10× 样本效率。Proposal 借此为"consistency loss 优于 augmentation"提供理论支撑。
- [GRPO-CARE (arXiv 2506.16141)](https://arxiv.org/abs/2506.16141): 多模态推理的 consistency-aware RL，使用稀疏一致性奖励。与 proposal 有方法论重叠但目标域不同（多模态 vs 纯文本数学）。
- [RLTR (arXiv 2602.08489)](https://arxiv.org/abs/2602.08489): 通过 transfer reward 改善鲁棒性但不针对特定扰动类型的不变性。

- **调研总结**: 数学推理鲁棒性是 2025-2026 年的热门方向，benchmark 端已较为成熟（VAR-MATH, MATH-Perturb, GSM-Symbolic, RRB），但 training-time 干预方案仍稀缺且碎片化。现有方法要么只做单向（invariance-only 或 discrimination-only），要么限于特定域（视觉、初等数学）。Proposal 的"双目标"定位确实填补了一个真实的方法论空白，但其核心组件（JS-divergence、contrastive loss、advantage pooling、entropy gating）均非原创，贡献主要在于问题框架化和组件整合。ReasonMaxxer 的 RL-free 方案构成对 RL-based 方法的根本性挑战。

【整体印象】:
作为审稿人，我的第一反应是：这是一篇 problem framing 和实验设计都远高于平均水平的 proposal，但方法论创新有限。proposal 对领域文献的掌握堪称全面，相关工作定位精准；"等价保持扰动需要不变性、语义改变扰动需要区分性"的双目标框架是一个真实且有价值的 insight。实验设计（8 baselines、compute fairness 双协议、6 项消融、人工验证流程）显著优于多数投稿。然而，核心方法是 4 个已有技术的组合应用（JS-divergence from PPCL + contrastive from CLIPO/MATH-Perturb + pooling from TA-GRPO + entropy gating from ReasonMaxxer），没有任何单一组件是新的。此外，ROMA 在视觉域用高度同构方法仅获 +2.4% 的增益令人担忧——如果数学域的增益同样有限，method complexity 将难以 justify。我的倾向是 borderline，偏向 weak accept，前提是实验结果 convincing。

【核心贡献】:
1. **问题框架化**：提出数学扰动空间的"结构二元性"——等价保持扰动（需要不变性）vs 语义改变扰动（需要区分性），这是一个清晰且有价值的概念贡献。
2. **双目标 RL 框架**：将上述二元性转化为可操作的 dual consistency objectives 并整合进 GRPO 训练流程。
3. **跨扰动类型迁移假说**：训练时扰动 ≠ 评估时扰动，如果方法仍然有效则证明了数学结构敏感性的习得而非扰动特异性免疫。

核心贡献对领域的价值：中等偏上。如果实验验证了双目标的必要性（invariance-only 和 discrimination-only 都不够）以及 augmentation-only 的不足，这将是对 RL-based math reasoning robustness 的实质推进。

【方法合理性】:
方法整体合理，各组件有明确的理论动机：
- JS-divergence invariance → 来自 PPCL 的 empirical support（10× 样本效率）
- Contrastive discrimination → 直接针对 MATH-Perturb 的 blind technique application
- Entropy gating → 来自 ReasonMaxxer 的 empirical insight
- Advantage pooling → 来自 TA-GRPO 的 zero-gradient 解决方案

**更简单的替代方案**是 proposal 本身提出的 GRPO+augmentation-only baseline——用相同的扰动数据但不加 consistency losses。如果这个 baseline 已经足够好，那 consistency losses 就是多余的。PPCL 的 10× 效率优势是在 NLP 分类任务上观察到的，能否迁移到生成式数学推理的 RL 训练中是一个 open question。

另一个重要竞争方案是 ReasonMaxxer 的 RL-free 路线——如果稀疏 contrastive loss 不需要在线 RL 即可匹配性能，那在其基础上加 perturbation-aware 机制可能比从 GRPO 出发更高效。

方法的一个潜在弱点：扰动生成 pipeline 的复杂性（VAR-MATH symbolic pipeline + LLM paraphrasing + SymPy verification）可能引入噪声，而方法对扰动质量的依赖很高。proposal 设计了人工验证（≥200 + ≥300 样本）来 mitigate 这一风险，但这增加了可重复性的门槛。

【5 维度打分】:

1. 研究问题: 【强】— RL 训练的数学推理模型在表面扰动下 47-73% 的准确率下降是一个被 VAR-MATH、MATH-Perturb、GSM-Symbolic 等多项工作反复验证的严重问题。Training-time 干预方案的稀缺性也被调研所确认。问题重要、时机好、定义清晰。唯一的小疑虑是：随着模型规模增大（如 DeepSeek-R1-671B），这个问题是否会自然缓解？但至少在 7B-8B 级别，问题仍然严峻。

2. 方法与创新: 【中】— 双目标框架（invariance + discrimination）的概念贡献是真实的，且在已有文献中没有被提出过。但四个核心技术组件（JS-divergence, contrastive loss, advantage pooling, entropy gating）均直接借用自 PPCL、TA-GRPO、ReasonMaxxer 等已有工作，没有任何组件层面的创新。与 ROMA（arXiv 2605.09262）的 token-level KL consistency in GRPO 方法论重叠度高——本质差异仅在于：(a) 增加了 discrimination 方向，(b) 从视觉域迁移到文本数学域。Reviewers 很可能会质疑"组合 = 创新？"。

3. 实验设计: 【强】— 这是 proposal 最突出的优势。8 个 baselines 覆盖了 GRPO variants（Vanilla GRPO, DAPO, Dr.GRPO, TA-GRPO, COPO）、同域方法（ReasonMaxxer, AbstRaL）和关键 ablation baseline（augmentation-only）。Compute fairness 双协议（step-matched + FLOP-matched）在 RL 论文中非常罕见且值得赞赏。消融矩阵全面。评测涵盖三类扰动 + clean accuracy，且明确区分了 core claims 和 supplementary observations。人工验证流程（200+300 样本，2 annotators，报告 IAA）体现了严谨性。显式的 numerical targets（≥10pp consistency, ≥15pp gap reduction, ≤1% clean drop）使得 contributions 可证伪。

4. 可行性: 【中偏强】— 8×H100 对 Qwen3-8B 的 GRPO 训练是合理的。两阶段执行（1.5B 先行 + 8B 跟进）降低了风险。扰动生成 pipeline 可复用 VAR-MATH 和 MATH-Perturb 的现有资源。但复杂的 hybrid perturbation pipeline、多损失函数的超参调优（λ₁, λ₂）和人工验证流程增加了实施复杂度。预估周期未明确但 8-12 周可完成。主要风险在于扰动质量控制和多损失函数的稳定训练。

5. 写作与呈现: 【强】— proposal 结构清晰，逻辑链完整：problem（47-73% drop）→ diagnosis（outcome-only RL 的局限 + perturbation space 的二元性）→ solution（dual consistency objectives）→ validation plan。对每个相关工作的定位都精准指出其覆盖的维度和遗留的 gap。Entropy gating 被诚实地标注为"testable hypothesis"而非 established fact。唯一的写作问题是信息密度偏高，AAAI 8 页限制下需要大幅压缩。

【概率估计】: [28% - 40%] 中位 34%

【估计理由】:
向上因素：(1) 研究问题重要且时机好，处于 2025-2026 的热点交汇期；(2) 实验设计质量远超平均投稿，compute fairness 双协议和 augmentation-only ablation 直接回应了最可能的审稿质疑；(3) 双目标框架（invariance + discrimination）确实填补了方法论空白；(4) 文献覆盖极其全面，positioning 精准。

向下因素：(1) 方法论创新主要是已有组件的组合，没有 surprise factor——四个组件均有明确来源，reviewers 可能判定为 incremental；(2) ROMA 用高度同构方法仅获 +2.4% 增益，暗示 consistency regularization 在 GRPO 中的效果上限可能有限；(3) ReasonMaxxer 作为 RL-free baseline 具有根本性挑战——如果几分钟单 GPU 训练能匹配全量 RL，那增加 consistency losses 的边际收益需要非常 convincing；(4) 方法复杂度高（3 个 loss + entropy gating + hybrid pipeline），ablation 虽完善但如果每个组件的边际贡献都不大，综合效果可能不 justify complexity；(5) 跨扰动类型迁移是核心 claim 之一但证据最弱（RRB 仅作 supplementary observation）。

综合判断：这是一篇 solid borderline paper。如果实验结果强劲（尤其是显著 beat augmentation-only 和 ReasonMaxxer），可以到 40%+。如果增益有限（类似 ROMA 的 +2-3%），可能跌到 25% 以下。中位 34% 反映了"问题好、设计好、但创新有限且结果未知"的现实。

【主要风险】:
1. **Novelty 不足被判 incremental**：四个核心组件均为直接借用，双目标框架虽是概念贡献但可被视为"显而易见的组合"。ROMA 的存在进一步削弱了 invariance loss 部分的新颖性。如果 2-3 位 reviewer 同时判定 novelty insufficient，这将是最主要的拒稿原因。
2. **效果不足以 justify 复杂度**：ROMA 在视觉域的 +2.4% 增益先例暗示 consistency regularization 可能只带来 marginal improvement。如果 ConsistRL 相对 augmentation-only baseline 的提升不显著（<5pp），或者 ReasonMaxxer 在鲁棒性上也 surprisingly competitive，三个额外 loss 的工程复杂度将无法被 justify。

【实施评估】:
  - 计算资源: 8×H100（~1 节点），Qwen3-8B GRPO 训练合理。Dual forward pass（类似 ROMA）增加约 30-50% 的计算开销。总计估计需要 2000-4000 GPU-hours。
  - 数据需求: MATH/AMC/AIME 训练集（公开可用）+ VAR-MATH 扰动模板（开源）+ MATH-Perturb 数据集（开源）+ GPT-4 生成的 hard perturbations（需 API 费用，估计 $500-1000）。
  - 人工介入: 扰动质量验证需要人工标注 ≥500 道题（200 invariance + 300 discrimination），需要具备数学背景的标注员，2 人 2-3 周工作量。
  - 训练需求: 需要从头训练 RL（不能直接用现有 checkpoint），Qwen3-1.5B（Phase 1）+ Qwen3-8B（Phase 2），每个 phase 含多轮消融。
  - 新 Benchmark: 不需要构建新 benchmark，但需要构建训练用扰动数据集（~5000-10000 题对），这本身是 non-trivial 的工程工作。
  - 预估周期: 10-14 周。Phase 1（1.5B 消融 + pipeline 搭建）4-5 周；Phase 2（8B 核心实验）3-4 周；扰动数据生成 + 人工验证 2-3 周（可与 Phase 1 并行）；写作 2 周。
```

Sources:
- [VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks](https://arxiv.org/abs/2507.12885)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations](https://arxiv.org/abs/2502.06453)
- [ReasonMaxxer: Rethinking RL for LLM Reasoning](https://arxiv.org/abs/2605.06241)
- [ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation](https://arxiv.org/abs/2605.09262)
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [PPCL: Prompt Perturbation Consistency Learning for Robust Language Models](https://aclanthology.org/2024.findings-eacl.91/)
- [GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning](https://arxiv.org/abs/2506.16141)
- [RLTR: Beyond Correctness: Learning Robust Reasoning via Transfer](https://arxiv.org/abs/2602.08489)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e77fd06-67fa-4b31-9ce6-a7605aa0f20c",
  "isSidechain": false,
  "requestId": "req_011CbWZBDq2rccrFKvrPpPau",
  "type": "assistant",
  "uuid": "da466d17-d44e-4203-95a6-68380f766001",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PiSZ7hnFa92cJYXfq1YD5F",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1761,
      "cache_read_input_tokens": 25393,
      "output_tokens": 6568,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1761,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6568,
          "cache_read_input_tokens": 25393,
          "cache_creation_input_tokens": 1761,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1761
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

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reas…",
  "leafUuid": "da466d17-d44e-4203-95a6-68380f766001",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reas…",
  "leafUuid": "da466d17-d44e-4203-95a6-68380f766001",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "2ecff145-2c2e-49d3-880a-3771a75ee556"
}
```

---
