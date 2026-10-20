# Research conversation: Consistency-Regularized RL for Perturbation-Robust Math Reasoning ## Core Problem RL-trained mathematical reasoning mode

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 46
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/f11f911d-ff1c-4027-8486-21befbfcaf17.jsonl`
- **Structured JSON:** [`a17f19f4c9ff09f5ea30.json`](../../sessions/a1/a17f19f4c9ff09f5ea30.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T08:20:19.887Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T08:20:19.887Z",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "content": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning\n\n## Core Problem\n\nRL-trained mathematical reasoning models suffer 47–73% accuracy drops under trivial surface-form perturbations (numerical re-parameterization, variable renaming), revealing a fundamental limitation of outcome-based RLVR: binary reward provides no gradient against surface-form-dependent reasoning patterns. ReasonMaxxer (arXiv 2605.06241) shows RL acts as sparse policy selection at high-entropy tokens rather than capability learning; RLTR (arXiv 2602.08489) demonstrates that robust reasoning requires transferability beyond the producing model. Both imply outcome-only RL is insufficient for genuine robustness. Can we enforce invariance to mathematically irrelevant features during RL training without degrading clean accuracy?\n\n## Research Opportunity\n\nMathematical perturbation space exhibits a structural duality demanding a dual-objective response: equivalence-preserving perturbations (variable renaming, numerical reparameterization) and semantics-altering perturbations (changed constraints, added conditions) are surface-similar but require opposite model behaviors—invariance for the former, discrimination for the latter. Critically, existing methods address at most one side:\n\n- ROMA (arXiv 2605.09262, May 2026): token-level KL consistency during GRPO improves visual robustness by +2.4%/+2.3% on seen/unseen degradations—single-direction invariance only, visual domain only.\n- TA-GRPO (arXiv 2601.22478, Jan 2026): pools advantages across equivalent rephrasings, improving pass@k by up to 9.84 points on competition math—no explicit consistency loss, no robustness evaluation.\n- CLIPO (arXiv 2603.10101, Mar 2026): trajectory-level contrastive learning in GRPO extracts invariant structures across correct reasoning paths—orthogonal invariance dimension (trajectory noise, not input surface-form noise).\n- RULES (arXiv 2602.00998, Feb 2026): explicit eligibility reasoning + section-aware RL to verify lemma applicability before use—addresses discrimination via structured output format change, not via distributional consistency.\n- PPCL (EACL 2024, ACL 2024): JS-divergence consistency regularization achieves 10× sample efficiency over pure augmentation in NLP—validates that distribution-level consistency provides an inductive bias (same structure → same output) that data augmentation alone cannot replicate.\n\nNo method combines perturbation-type-aware dual objectives (invariance + discrimination) with RL-integrated consistency regularization for mathematical reasoning. Moreover, the discrimination side—training models to detect when surface-similar problems require different solution strategies—constitutes implicit mathematical structure verification, directly targeting the \"blind technique application\" failure mode.\n\n## Research Landscape\n\nThe robustness problem is extensively documented: VAR-MATH (arXiv 2507.12885) reports 47.9–72.9% accuracy drops for 7B RL models on symbolically re-parameterized competition math (AMC23/AIME24/AIME25); GSM-Symbolic (ICLR 2025) shows up to 65% drops from a single irrelevant clause; the Robust Reasoning Benchmark (arXiv 2604.08571, Apr 2026) finds up to 54% drops for open-weights models on perturbed AIME problems; MATH-Perturb (ICML 2025) quantifies a critical \"blind technique application\" failure mode—~40% of o1-mini's errors and ~25% of Claude-3.5-Sonnet's errors on hard perturbations stem from mechanically applying memorized strategies without verifying applicability.\n\nTraining-time interventions remain scarce: AbstRaL (ICLR 2026) achieves GSM-level robustness via symbolic abstraction but is explicitly limited to elementary math. TA-GRPO pools advantages across GPT-4-generated rephrasings but lacks equivalence verification, distribution-level consistency, and discrimination capability. ROMA addresses visual robustness only. CLIPO captures trajectory-level reasoning invariance—orthogonal to input-level perturbation invariance. RULES addresses discrimination through explicit output-structure modification (eligibility reasoning sections), requiring format changes incompatible with free-form reasoning; ConsistRL instead achieves discrimination implicitly through distributional constraints, remaining format-agnostic. RLTR (arXiv 2602.08489) improves robustness via transfer reward but does not target perturbation-specific invariance. GRPO-CARE (arXiv 2506.16141) and COPO (arXiv 2508.04138) address multimodal consistency and zero-gradient issues respectively. DAPO (arXiv 2503.14476) and Dr.GRPO improve GRPO training dynamics without robustness mechanisms.\n\n## Proposed Approach\n\nExtend GRPO with dual consistency objectives reflecting mathematical perturbation space's structural duality:\n\n**(1) JS-divergence invariance loss** on math-equivalence-preserving perturbations (variable renaming, numerical reparameterization), generated via a hybrid pipeline: VAR-MATH's symbolic pipeline (arXiv 2507.12885) for algebraic/numerical problem types + LLM-based paraphrasing with SymPy equivalence verification for remaining types. Applied at entropy-gated decision tokens per ReasonMaxxer's insight, with entropy-gating treated as a testable hypothesis (the correspondence between RL policy-selection points and consistency-critical points is not a priori guaranteed).\n\n**(2) Contrastive discrimination loss** penalizing output similarity on semantics-altering hard perturbations—implicit mathematical structure verification targeting MATH-Perturb's \"blind technique application\" failure mode. Unlike RULES' explicit eligibility reasoning (which requires structured output format), this operates via distributional constraints compatible with any reasoning format.\n\n**(3) TA-GRPO-style advantage pooling** across perturbation groups to mitigate GRPO's zero-gradient problem.\n\n**Key hypothesis: cross-perturbation-type transfer robustness.** Training-time perturbations (symbolic reparameterization) differ from evaluation perturbations (MATH-Perturb semantic alterations, RRB structural noise). If ConsistRL generalizes across unseen perturbation types, this evidences learned mathematical structure sensitivity rather than perturbation-specific immunity.\n\n**Why consistency loss, not just augmentation?** Distribution-level consistency provides an explicit inductive bias—same mathematical structure under different surface forms must map to the same reasoning trajectory. This structural constraint cannot emerge from data augmentation alone, which merely broadens training distribution without enforcing distributional invariance. PPCL's 10× sample efficiency over pure augmentation (EACL 2024) provides empirical support; the GRPO+augmentation-only baseline directly tests this claim.\n\nTrain Qwen3-8B (primary) and Qwen3-1.5B (ablation/scaling validation) on MATH/AMC/AIME, 8×H100.\n\n## Detailed Description\n\n**Invariance objective.** JS-divergence enforces output-distribution invariance across equivalence-preserving perturbations, applied at high-entropy decision points (1–3% of tokens per ReasonMaxxer). Perturbation generation uses a hybrid pipeline: VAR-MATH's symbolic pipeline for compatible types (algebra, numerical parameterization) and LLM paraphrasing + SymPy verification for others. Training perturbation quality is validated via: (a) symbolic equivalence verification where applicable, (b) sampled human verification (≥200 problems) reporting equivalence correctness rate, (c) coverage rate reporting across MATH problem types. Entropy gating is validated via explicit ablation: full-sequence vs. entropy-gated application, static base-model entropy vs. dynamic policy entropy, threshold sensitivity analysis.\n\n**Discrimination objective.** Contrastive loss penalizes output similarity on semantics-altering hard perturbations, targeting implicit mathematical structure verification. Training data generated via GPT-4 pipeline following MATH-Perturb's hard perturbation taxonomy (condition change, constraint addition, etc.), with: (a) SymPy verification that generated problems have unique solutions differing from originals, (b) human verification (≥300 problems, 2 annotators, reporting inter-annotator agreement), (c) strict train/eval separation from all evaluation benchmarks. This approaches \"blind technique application\" via implicit distributional constraints, complementing RULES' explicit eligibility reasoning approach.\n\n**Advantage pooling.** TA-GRPO-style pooling across perturbation groups mitigates zero-gradient problems while ensuring mixed reward signals.\n\n## Experimental Design\n\n**Models:** Qwen3-8B (primary), Qwen3-1.5B (ablation + scaling). Two-phase execution: Phase 1 on 1.5B (full ablation + preliminary baselines), Phase 2 on 8B (core baselines + key ablations). Community checkpoints used where available.\n\n**Baselines (8):** (1) Vanilla GRPO, (2) DAPO (arXiv 2503.14476), (3) Dr.GRPO, (4) TA-GRPO (arXiv 2601.22478), (5) COPO (arXiv 2508.04138), (6) GRPO + augmentation-only (same perturbation data, no consistency losses), (7) ReasonMaxxer (arXiv 2605.06241), (8) AbstRaL (ICLR 2026, GSM-level subset only).\n\n**Evaluation benchmarks (grouped by perturbation type):**\n- *Numerical equivalence:* VAR-MATH (AMC23/AIME24/AIME25) — core evaluation\n- *Semantic discrimination:* MATH-Perturb (MATH-P-Simple and MATH-P-Hard, reported separately) — core evaluation\n- *Structural noise (supplementary):* Robust Reasoning Benchmark (arXiv 2604.08571) — out-of-scope for core claim, reported as cross-perturbation transfer observation\n- *Clean accuracy:* MATH-500\n\n**Metrics:** VAR-MATH strict/loose consistency rate with bootstrapping 95% CIs; robustness gap (clean − perturbed accuracy); per-benchmark accuracy with CIs; clean accuracy non-degradation criterion (MATH-500 drop ≤ 1%, paired bootstrap test p < 0.05).\n\n**Targets:** VAR-MATH strict consistency rate absolute improvement ≥10 pp over vanilla GRPO; robustness gap reduction ≥15 pp; MATH-P-Hard accuracy improvement ≥5 pp; clean MATH-500 drop ≤ 1%.\n\n**Ablation matrix:** (1) ConsistRL full, (2) w/o JS-divergence, (3) w/o contrastive discrimination, (4) w/o entropy gating (all tokens), (5) w/o advantage pooling, (6) JS-divergence only + entropy gating (minimal). Extensions (primarily at 1.5B): static vs. dynamic entropy gating, entropy threshold sensitivity, perturbation type separation (variable renaming vs. numerical reparameterization), loss weight sensitivity (λ₁, λ₂ grid).\n\n**Compute fairness:** Dual protocol—Protocol A (step-matched): same training steps, report per-method FLOPs and wall-clock time; Protocol B (FLOP-matched): same total FLOPs, ConsistRL uses fewer steps. Report per-step overhead ratio. Robustness vs. cumulative FLOPs curve.\n\n## Key References\n\n- Reinforcing Multimodal Reasoning Against Visual Degradation / ROMA (arXiv 2605.09262, 2026)\n- Transform-Augmented GRPO Improves Pass@k / TA-GRPO (arXiv 2601.22478, 2026)\n- CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR (arXiv 2603.10101, 2026)\n- RULES: Reliable Use of Lemmas via Eligibility Reasoning (arXiv 2602.00998, 2026)\n- Beyond Correctness: Learning Robust Reasoning via Transfer / RLTR (arXiv 2602.08489, 2026)\n- Prompt Perturbation Consistency Learning / PPCL (EACL Findings 2024, ACL 2024)\n- MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations (ICML 2025)\n- GSM-Symbolic: Understanding Limitations of Mathematical Reasoning in LLMs (ICLR 2025)\n- AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking (ICLR 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2507.12885, 2025)\n- Rethinking RL for LLM Reasoning / ReasonMaxxer (arXiv 2605.06241, 2026)\n- Robust Reasoning Benchmark (arXiv 2604.08571, 2026)\n- GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (arXiv 2506.16141, 2025)\n- COPO: Consistency-Aware Policy Optimization (arXiv 2508.04138, 2025)\n- DAPO: An Open-Source LLM Reinforcement Learning System at Scale (arXiv 2503.14476, 2025)\n- Dr.GRPO: Group Relative Policy Optimization Done Right"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T08:20:19.893Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T08:20:19.893Z",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

## Round 1

44 recorded events

### User

_source line 3 · 2026-05-29T08:20:19.981Z_

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
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "4e7a4dcf-034e-483f-8a8f-5579bdcb28d2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T08:20:19.979Z_

```json
{
  "parentUuid": "4e7a4dcf-034e-483f-8a8f-5579bdcb28d2",
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
  "uuid": "e984587b-ffca-4760-89b0-bc05768e8f5f",
  "timestamp": "2026-05-29T08:20:19.979Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T08:20:19.979Z_

```json
{
  "parentUuid": "e984587b-ffca-4760-89b0-bc05768e8f5f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "cc4c7649-3127-4770-935d-c9d0c5a625c0",
  "timestamp": "2026-05-29T08:20:19.979Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
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
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Assistant

_source line 7 · 2026-05-29T08:20:29.411Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "补救 agent" (remediation agent) to review this research proposal for AAAI 2026 submission. My job is to focus exclusively on experimental design and technical execution completeness — baselines, experimental plan, evaluation metrics, ablation design, and feasibility.

Let me first read the proposal carefully, then conduct web searches to understand the current experimental standards in this field before giving my assessment.

The proposal is about "ConsistRL" — extending GRPO with dual consistency objectives (JS-divergence invariance loss + contrastive discrimination loss) to improve robustness of math reasoning models against surface-form perturbations.


I need to search for current best practices in RL-based math reasoning robustness, verify whether the proposed baselines are still state-of-the-art, check if the evaluation benchmarks align with community standards, and see what experimental approaches similar work has taken.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc4c7649-3127-4770-935d-c9d0c5a625c0",
  "isSidechain": false,
  "requestId": "req_011CbWXvaVxUk1RYbVtwzaLU",
  "type": "assistant",
  "uuid": "1761281e-60fc-47eb-b3c6-ea6d8aeec44b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163VeR8rFuZgxmAS9G99pcx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4649,
      "cache_read_input_tokens": 14080,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4649
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

_source line 8 · 2026-05-29T08:20:29.413Z_

I'll start by carefully reading the proposal and then conducting the required pre-research to understand the current experimental standards in this field. Let me do several targeted web searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1761281e-60fc-47eb-b3c6-ea6d8aeec44b",
  "isSidechain": false,
  "requestId": "req_011CbWXvaVxUk1RYbVtwzaLU",
  "type": "assistant",
  "uuid": "20c5900c-601a-455c-ae20-0b54ea0a4956",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163VeR8rFuZgxmAS9G99pcx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4649,
      "cache_read_input_tokens": 14080,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4649
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

_source line 9 · 2026-05-29T08:20:29.594Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XKGtueK5mqxoHhCyN9WVfD`</summary>

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
  "parentUuid": "20c5900c-601a-455c-ae20-0b54ea0a4956",
  "isSidechain": false,
  "requestId": "req_011CbWXvaVxUk1RYbVtwzaLU",
  "type": "assistant",
  "uuid": "40527dbb-2051-4b3b-902c-8b68afebf042",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0163VeR8rFuZgxmAS9G99pcx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4649,
      "cache_read_input_tokens": 14080,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4649
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

_source line 10 · 2026-05-29T08:20:29.603Z_

<details><summary>↩ Tool result · `toolu_01XKGtueK5mqxoHhCyN9WVfD`</summary>

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
  "parentUuid": "40527dbb-2051-4b3b-902c-8b68afebf042",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "d9df6308-9b33-4560-9053-39159790b25f",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "40527dbb-2051-4b3b-902c-8b68afebf042",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
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
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reasoning models suffer 47–73% accuracy drops under trivial surface-form perturbations (nu…",
  "leafUuid": "d9df6308-9b33-4560-9053-39159790b25f",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Assistant

_source line 13 · 2026-05-29T08:20:32.748Z_

Now let me conduct the required pre-research with multiple parallel searches to understand the experimental standards in this field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9df6308-9b33-4560-9053-39159790b25f",
  "isSidechain": false,
  "requestId": "req_011CbWXwJFvVNj4eoZ5rE3PY",
  "type": "assistant",
  "uuid": "aad81c74-209e-4b97-9e06-1d662955dc8b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013F7xsejeTjdwGWSewtJ1tT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 18729,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 18729,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 872
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

_source line 14 · 2026-05-29T08:20:32.863Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XPBtj7ZoqJUg57hbkr1APv`</summary>

```json
{
  "query": "GRPO math reasoning robustness experimental design baselines 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aad81c74-209e-4b97-9e06-1d662955dc8b",
  "isSidechain": false,
  "requestId": "req_011CbWXwJFvVNj4eoZ5rE3PY",
  "type": "assistant",
  "uuid": "009d2e0c-54bd-4c87-a2e3-2dc0e095e716",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013F7xsejeTjdwGWSewtJ1tT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 18729,
      "output_tokens": 93,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 872,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 93,
          "cache_read_input_tokens": 18729,
          "cache_creation_input_tokens": 872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 872
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

_source line 15 · 2026-05-29T08:20:42.436Z_

<details><summary>↩ Tool result · `toolu_01XPBtj7ZoqJUg57hbkr1APv`</summary>

```text
Web search results for query: "GRPO math reasoning robustness experimental design baselines 2025 2026"

Links: [{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models","url":"https://arxiv.org/html/2504.09696v1"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/html/2505.09655v3"},{"title":"[2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning","url":"https://arxiv.org/abs/2510.19807"},{"title":"[2505.09655] DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/abs/2505.09655"},{"title":"Training-Free Group Relative Policy Optimization","url":"https://arxiv.org/html/2510.08191v1"},{"title":"Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning","url":"https://arxiv.org/html/2602.03190v1"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.287/"},{"title":"DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.09655"}]

Based on the search results, here are several recent research papers on GRPO (Group Relative Policy Optimization) applied to mathematical reasoning with focus on robustness and experimental design:

## Key Papers (2025-2026)

**GRPO-LEAD: Difficulty-Aware Approach**
GRPO, widely adopted by R1-like reasoning models, faces challenges in reward sparsity, verbosity, and inadequate focus on problem difficulty. GRPO-LEAD enhances GRPO with length-regularized rewards, explicit penalties for incorrect solutions, and difficulty-aware advantage reweighting for robust generalization on challenging problems. The 14B-scale experiments achieve state-of-the-art performance by balancing output brevity with high problem-solving accuracy.

**DRA-GRPO: Diverse Reasoning Paths**
DRA-GRPO applies across distinct model backbones including DeepSeek-R1-Distill-Qwen-1.5B and Qwen 3, with empirical evaluations on five mathematical reasoning benchmarks demonstrating consistent effectiveness over strong baselines. The method is robust to different embedding spaces and effectively captures semantic diversity.

**Scaf-GRPO: Scaffolded Approach**
Scaf-GRPO demonstrates effectiveness on challenging mathematics benchmarks, boosting the pass@1 score of Qwen2.5-Math-7B on AIME24 by a relative 44.3% over vanilla GRPO baseline.

**Training-Free GRPO**
Training-Free GRPO achieves substantial gains in mathematical reasoning with clear advantages across tool-use and non-tool-use scenarios, significantly elevating performance on frozen DeepSeek-V3.1-Terminus with zero gradient updates.

**Prompt Augmentation for GRPO**
Recent work identifies a length bias in original GRPO's objective and shows that GRPO training dynamics is sensitive to prompt templates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "009d2e0c-54bd-4c87-a2e3-2dc0e095e716",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "891d9d15-3b57-4a8b-ac2d-846114aa4660",
  "toolUseResult": {
    "query": "GRPO math reasoning robustness experimental design baselines 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013yXNV3D6EHPRvJicVxWget",
        "content": [
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models",
            "url": "https://arxiv.org/html/2504.09696v1"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2505.09655v3"
          },
          {
            "title": "[2510.19807] Scaf-GRPO: Scaffolded Group Relative Policy Optimization for Enhancing LLM Reasoning",
            "url": "https://arxiv.org/abs/2510.19807"
          },
          {
            "title": "[2505.09655] DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2505.09655"
          },
          {
            "title": "Training-Free Group Relative Policy Optimization",
            "url": "https://arxiv.org/html/2510.08191v1"
          },
          {
            "title": "Prompt Augmentation Scales up GRPO Training on Mathematical Reasoning",
            "url": "https://arxiv.org/html/2602.03190v1"
          },
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.287/"
          },
          {
            "title": "DRA-GRPO: Your GRPO Needs to Know Diverse Reasoning Paths for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.09655"
          }
        ]
      },
      "Based on the search results, here are several recent research papers on GRPO (Group Relative Policy Optimization) applied to mathematical reasoning with focus on robustness and experimental design:\n\n## Key Papers (2025-2026)\n\n**GRPO-LEAD: Difficulty-Aware Approach**\nGRPO, widely adopted by R1-like reasoning models, faces challenges in reward sparsity, verbosity, and inadequate focus on problem difficulty. GRPO-LEAD enhances GRPO with length-regularized rewards, explicit penalties for incorrect solutions, and difficulty-aware advantage reweighting for robust generalization on challenging problems. The 14B-scale experiments achieve state-of-the-art performance by balancing output brevity with high problem-solving accuracy.\n\n**DRA-GRPO: Diverse Reasoning Paths**\nDRA-GRPO applies across distinct model backbones including DeepSeek-R1-Distill-Qwen-1.5B and Qwen 3, with empirical evaluations on five mathematical reasoning benchmarks demonstrating consistent effectiveness over strong baselines. The method is robust to different embedding spaces and effectively captures semantic diversity.\n\n**Scaf-GRPO: Scaffolded Approach**\nScaf-GRPO demonstrates effectiveness on challenging mathematics benchmarks, boosting the pass@1 score of Qwen2.5-Math-7B on AIME24 by a relative 44.3% over vanilla GRPO baseline.\n\n**Training-Free GRPO**\nTraining-Free GRPO achieves substantial gains in mathematical reasoning with clear advantages across tool-use and non-tool-use scenarios, significantly elevating performance on frozen DeepSeek-V3.1-Terminus with zero gradient updates.\n\n**Prompt Augmentation for GRPO**\nRecent work identifies a length bias in original GRPO's objective and shows that GRPO training dynamics is sensitive to prompt templates."
    ],
    "durationSeconds": 9.563672629,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "009d2e0c-54bd-4c87-a2e3-2dc0e095e716",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-29T08:20:45.915Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LC3BDG49XvCvsoGw2SucYt`</summary>

```json
{
  "query": "VAR-MATH benchmark MATH-Perturb evaluation robustness math LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "891d9d15-3b57-4a8b-ac2d-846114aa4660",
  "isSidechain": false,
  "requestId": "req_011CbWXxETkZhJnNT9ycgNuP",
  "type": "assistant",
  "uuid": "47bedb19-4466-4dad-9bf9-86ecb066689e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RubJ8sadQNpSiccVqMtqwR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 19601,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 982,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 19601,
          "cache_creation_input_tokens": 982,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 982
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

_source line 17 · 2026-05-29T08:20:54.742Z_

<details><summary>↩ Tool result · `toolu_01LC3BDG49XvCvsoGw2SucYt`</summary>

```text
Web search results for query: "VAR-MATH benchmark MATH-Perturb evaluation robustness math LLM 2025 2026"

Links: [{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571v2"},{"title":"[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/abs/2507.12885"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"},{"title":"Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges","url":"https://arxiv.org/html/2605.19723v1"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in ...","url":"https://arxiv.org/pdf/2507.12885"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview","url":"https://openreview.net/forum?id=M8OLGgYK7e"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/pdf/2508.08833"},{"title":"Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models","url":"https://arxiv.org/pdf/2511.08022"}]

Based on the search results, here's what I found about VAR-MATH and MATH-Perturb:

## VAR-MATH Benchmark

VAR-MATH enforces consistency across structurally equivalent variants, mitigates contamination, and enhances robustness through bootstrapped metrics. VAR-MATH transforms three popular benchmarks, AMC23, AIME24, and AIME25, into their symbolic counterparts, VAR-AMC23, VAR-AIME24, and VAR-AIME25.

Experimental results show substantial performance drops for RL-trained models on these variabilized benchmarks, especially for smaller models, with average declines of 47.9% on AMC23, 58.8% on AIME24, and 72.9% on AIME25. These findings indicate that some existing RL methods rely on superficial heuristics and fail to generalize beyond specific numerical forms.

## MATH-Perturb Benchmark

MATH-Perturb consists of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset. Significant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).

Both benchmarks serve to evaluate the robustness of large language models in mathematical reasoning by testing their ability to handle transformations and perturbations of mathematical problems, revealing limitations in models' true mathematical understanding beyond pattern memorization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47bedb19-4466-4dad-9bf9-86ecb066689e",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "42e1100d-3593-4fc3-86db-9fe7b12db4dc",
  "toolUseResult": {
    "query": "VAR-MATH benchmark MATH-Perturb evaluation robustness math LLM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MAezmaUzKFVSi4hFrdjcc6",
        "content": [
          {
            "title": "Robust Reasoning Benchmark",
            "url": "https://arxiv.org/html/2604.08571v2"
          },
          {
            "title": "[2507.12885] VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/abs/2507.12885"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v1"
          },
          {
            "title": "Mathematical Reasoning in Large Language Models: Benchmarks, Architectures, Evaluation, and Open Challenges",
            "url": "https://arxiv.org/html/2605.19723v1"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in ...",
            "url": "https://arxiv.org/pdf/2507.12885"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=M8OLGgYK7e"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/pdf/2508.08833"
          },
          {
            "title": "Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models",
            "url": "https://arxiv.org/pdf/2511.08022"
          }
        ]
      },
      "Based on the search results, here's what I found about VAR-MATH and MATH-Perturb:\n\n## VAR-MATH Benchmark\n\nVAR-MATH enforces consistency across structurally equivalent variants, mitigates contamination, and enhances robustness through bootstrapped metrics. VAR-MATH transforms three popular benchmarks, AMC23, AIME24, and AIME25, into their symbolic counterparts, VAR-AMC23, VAR-AIME24, and VAR-AIME25.\n\nExperimental results show substantial performance drops for RL-trained models on these variabilized benchmarks, especially for smaller models, with average declines of 47.9% on AMC23, 58.8% on AIME24, and 72.9% on AIME25. These findings indicate that some existing RL methods rely on superficial heuristics and fail to generalize beyond specific numerical forms.\n\n## MATH-Perturb Benchmark\n\nMATH-Perturb consists of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset. Significant performance drops were observed on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%).\n\nBoth benchmarks serve to evaluate the robustness of large language models in mathematical reasoning by testing their ability to handle transformations and perturbations of mathematical problems, revealing limitations in models' true mathematical understanding beyond pattern memorization."
    ],
    "durationSeconds": 8.820229350999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "47bedb19-4466-4dad-9bf9-86ecb066689e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-29T08:20:57.750Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015q6BnHgyMSknU3YcPh2t8H`</summary>

```json
{
  "query": "TA-GRPO transform augmented GRPO experimental setup ablation study baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "42e1100d-3593-4fc3-86db-9fe7b12db4dc",
  "isSidechain": false,
  "requestId": "req_011CbWXy9AHsGkdycXKEXy31",
  "type": "assistant",
  "uuid": "f00e379d-02ef-4b0a-93c6-90a6f4cbdf1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YLoUsavuUtwJouHCJubtnz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 20583,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 956,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 20583,
          "cache_creation_input_tokens": 956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 956
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

_source line 19 · 2026-05-29T08:21:07.031Z_

<details><summary>↩ Tool result · `toolu_015q6BnHgyMSknU3YcPh2t8H`</summary>

```text
Web search results for query: "TA-GRPO transform augmented GRPO experimental setup ablation study baselines"

Links: [{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/html/2601.22478v2"},{"title":"(PDF) Transform-Augmented GRPO Improves Pass@k","url":"https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning","url":"https://arxiv.org/pdf/2508.02833"}]

Based on the search results, here's information about TA-GRPO's experimental setup and ablation study:

## Overview
TA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question via paraphrasing, variable renaming, and format changes, and computes advantages by pooling rewards across the entire group.

## Ablation Study
The ablation study on Pass@32 (Qwen3-1.7B) includes a "TA-GRPO w/o pooling" variant that trains on transforms but computes advantages per-variant rather than pooled. Data augmentation alone does not guarantee success, and without pooling, gains over GRPO are minimal (AIME24: +2, GPQA: +1) or even negative (AIME25: -3).

Only with pooled advantages does TA-GRPO consistently outperform GRPO across all benchmarks. The ablation study confirms that pooled advantages, not merely data augmentation, drive the improvement.

## Experimental Results
On competition-level problems (AMC12 and AIME24), TA-GRPO improves Pass@32 by up to 9.84 points, and on out-of-distribution scientific reasoning (GPQA-Diamond), the improvement reaches 5.05 points.

The key finding is that the pooled advantage computation is essential—data augmentation alone is insufficient for achieving improvements over the baseline GRPO method.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f00e379d-02ef-4b0a-93c6-90a6f4cbdf1d",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "6951145d-02fa-48b3-bf4b-38eb3d8e0f39",
  "toolUseResult": {
    "query": "TA-GRPO transform augmented GRPO experimental setup ablation study baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_017vayaNMQBKuf7LgAaa2BrX",
        "content": [
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/html/2601.22478v2"
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
            "title": "[2601.22478] Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/abs/2601.22478"
          },
          {
            "title": "TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2508.02833"
          }
        ]
      },
      "Based on the search results, here's information about TA-GRPO's experimental setup and ablation study:\n\n## Overview\nTA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question via paraphrasing, variable renaming, and format changes, and computes advantages by pooling rewards across the entire group.\n\n## Ablation Study\nThe ablation study on Pass@32 (Qwen3-1.7B) includes a \"TA-GRPO w/o pooling\" variant that trains on transforms but computes advantages per-variant rather than pooled. Data augmentation alone does not guarantee success, and without pooling, gains over GRPO are minimal (AIME24: +2, GPQA: +1) or even negative (AIME25: -3).\n\nOnly with pooled advantages does TA-GRPO consistently outperform GRPO across all benchmarks. The ablation study confirms that pooled advantages, not merely data augmentation, drive the improvement.\n\n## Experimental Results\nOn competition-level problems (AMC12 and AIME24), TA-GRPO improves Pass@32 by up to 9.84 points, and on out-of-distribution scientific reasoning (GPQA-Diamond), the improvement reaches 5.05 points.\n\nThe key finding is that the pooled advantage computation is essential—data augmentation alone is insufficient for achieving improvements over the baseline GRPO method."
    ],
    "durationSeconds": 9.276685184000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f00e379d-02ef-4b0a-93c6-90a6f4cbdf1d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-29T08:21:09.958Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HsFGc8VevpqP2cicy4TKz3`</summary>

```json
{
  "query": "ROMA GRPO visual robustness consistency regularization multimodal reasoning 2026 experimental design"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6951145d-02fa-48b3-bf4b-38eb3d8e0f39",
  "isSidechain": false,
  "requestId": "req_011CbWXz3eBY5JMorwPHqpVY",
  "type": "assistant",
  "uuid": "92f4a10e-b148-4d77-993f-978f1bb37f4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EKTGYgWSQtGvDrRA8QtptD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 21539,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 21539,
          "cache_creation_input_tokens": 682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 682
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

_source line 21 · 2026-05-29T08:21:18.442Z_

<details><summary>↩ Tool result · `toolu_01HsFGc8VevpqP2cicy4TKz3`</summary>

```text
Web search results for query: "ROMA GRPO visual robustness consistency regularization multimodal reasoning 2026 experimental design"

Links: [{"title":"[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/abs/2605.09262"},{"title":"Reinforcing Multimodal Reasoning Against Visual Degradation","url":"https://arxiv.org/html/2605.09262.pdf"},{"title":"Paper page - Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization","url":"https://huggingface.co/papers/2604.08476"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://arxiv.org/html/2506.16141v1"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning ...","url":"https://arxiv.org/pdf/2506.16141"},{"title":"Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization","url":"https://arxiv.org/pdf/2604.08476"},{"title":"Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization","url":"https://arxiv.org/html/2509.21854"},{"title":"Visual reasoning consistency and robustness analysis of multimodal LLMs - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0031320325014281"},{"title":"REVISOR: Beyond Textual Reflection, Towards Multimodal Introspective Reasoning in Long-Form Video Understanding","url":"https://arxiv.org/html/2511.13026"}]

Based on the web search results, I found highly relevant research on this topic. Here are the key findings:

## ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation

ROMA is an RL fine-tuning approach for MLLMs that enforces robustness to visual degradation. The method addresses a critical challenge in multimodal reasoning models.

**Key Technical Components:**

For distributional consistency, ROMA applies a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories.

**Experimental Design and Results:**

On Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy. More specifically, ROMA matches clean performance (68.7%) while substantially improving robustness, reaching 61.6% on seen (+2.4%) and 56.3% on unseen (+2.3%) perturbations, with consistently smaller clean-to-degraded gaps.

**Motivation:**

Modern RL fine-tuning increasingly relies on critic-free algorithms such as GRPO to avoid memory overhead, though naively rolling out on degraded inputs can obscure perceptual evidence and force the model to hallucinate, destabilizing optimization and inducing policy collapse.

The research was published in May 2026 and represents an important contribution to improving the robustness of multimodal reasoning models under visual degradation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "92f4a10e-b148-4d77-993f-978f1bb37f4a",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "015e42ae-c285-45b4-b882-06e1244c84bf",
  "toolUseResult": {
    "query": "ROMA GRPO visual robustness consistency regularization multimodal reasoning 2026 experimental design",
    "results": [
      {
        "tool_use_id": "srvtoolu_013Tajbvsk9yMy7qDMwZtjTA",
        "content": [
          {
            "title": "[2605.09262] Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/abs/2605.09262"
          },
          {
            "title": "Reinforcing Multimodal Reasoning Against Visual Degradation",
            "url": "https://arxiv.org/html/2605.09262.pdf"
          },
          {
            "title": "Paper page - Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization",
            "url": "https://huggingface.co/papers/2604.08476"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2506.16141v1"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning ...",
            "url": "https://arxiv.org/pdf/2506.16141"
          },
          {
            "title": "Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization",
            "url": "https://arxiv.org/pdf/2604.08476"
          },
          {
            "title": "Perception-Consistency Multimodal Large Language Models Reasoning via Caption-Regularized Policy Optimization",
            "url": "https://arxiv.org/html/2509.21854"
          },
          {
            "title": "Visual reasoning consistency and robustness analysis of multimodal LLMs - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0031320325014281"
          },
          {
            "title": "REVISOR: Beyond Textual Reflection, Towards Multimodal Introspective Reasoning in Long-Form Video Understanding",
            "url": "https://arxiv.org/html/2511.13026"
          }
        ]
      },
      "Based on the web search results, I found highly relevant research on this topic. Here are the key findings:\n\n## ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation\n\nROMA is an RL fine-tuning approach for MLLMs that enforces robustness to visual degradation. The method addresses a critical challenge in multimodal reasoning models.\n\n**Key Technical Components:**\n\nFor distributional consistency, ROMA applies a token-level surrogate KL penalty against the worst-case augmentation; to prevent policy collapse under regularization, an auxiliary policy gradient loss anchored to clean-image advantages preserves a reliable reward signal; and to avoid systematically incorrect invariance, correctness-conditioned regularization restricts enforcement to successful trajectories.\n\n**Experimental Design and Results:**\n\nOn Qwen3-VL 4B/8B across seven multimodal reasoning benchmarks, the method improves robustness by +2.4% on seen and +2.3% on unseen corruptions over GRPO while matching clean accuracy. More specifically, ROMA matches clean performance (68.7%) while substantially improving robustness, reaching 61.6% on seen (+2.4%) and 56.3% on unseen (+2.3%) perturbations, with consistently smaller clean-to-degraded gaps.\n\n**Motivation:**\n\nModern RL fine-tuning increasingly relies on critic-free algorithms such as GRPO to avoid memory overhead, though naively rolling out on degraded inputs can obscure perceptual evidence and force the model to hallucinate, destabilizing optimization and inducing policy collapse.\n\nThe research was published in May 2026 and represents an important contribution to improving the robustness of multimodal reasoning models under visual degradation."
    ],
    "durationSeconds": 8.476327281999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "92f4a10e-b148-4d77-993f-978f1bb37f4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-29T08:21:21.252Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CFHaqbSiLNgr5vbvqLyDmv`</summary>

```json
{
  "query": "ReasonMaxxer rethinking RL LLM reasoning entropy gating policy selection 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "015e42ae-c285-45b4-b882-06e1244c84bf",
  "isSidechain": false,
  "requestId": "req_011CbWXztN79ZYwDgF6wHjoU",
  "type": "assistant",
  "uuid": "f0ef0fe0-a977-4dbc-b464-883e6e3e917b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UzYVpeSqf2MXkYVaisduue",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 22221,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 944,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 22221,
          "cache_creation_input_tokens": 944,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 944
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

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reasoning models suffer 47–73% accuracy drops under trivial surface-form perturbations (nu…",
  "leafUuid": "f0ef0fe0-a977-4dbc-b464-883e6e3e917b",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Tool result

_source line 25 · 2026-05-29T08:21:28.969Z_

<details><summary>↩ Tool result · `toolu_01CFHaqbSiLNgr5vbvqLyDmv`</summary>

```text
Web search results for query: "ReasonMaxxer rethinking RL LLM reasoning entropy gating policy selection 2026"

Links: [{"title":"[2605.06241] Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning","url":"https://arxiv.org/abs/2605.06241"},{"title":"Rethinking RL for LLM Reasoning: It’s Sparse Policy Selection, Not Capability Learning","url":"https://arxiv.org/html/2605.06241v2"},{"title":"Rethinking RL for LLM Reasoning: It's Sparse Policy ...","url":"https://arxiv.org/pdf/2605.06241"},{"title":"The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models | OpenReview","url":"https://openreview.net/forum?id=vXoksdcfqC"},{"title":"Revisiting Entropy in Reinforcement Learning for Large Reasoning Models","url":"https://arxiv.org/html/2511.05993v3"},{"title":"Quantile Advantage Estimation: Stabilizing RLVR for LLM Reasoning","url":"https://arxiv.org/pdf/2509.22611"},{"title":"Revisiting Entropy in Reinforcement Learning for Large Reasoning Models","url":"https://arxiv.org/pdf/2511.05993"}]

I found relevant research on this topic! Here's what the search revealed:

## ReasonMaxxer: Rethinking RL for LLM Reasoning

ReasonMaxxer reframes reasoning improvement as sparse policy selection rather than capability acquisition, using a minimal RL-free method that applies contrastive loss only at entropy-gated decision points, with a few hundred base-model rollouts and no online generation.

The base model's own entropy identifies these decision positions without any RL-trained model, and the entire correction is low-dimensional, representable in a tiny fraction of model parameters.

### Performance and Efficiency

Across three model families, six scales, and six math reasoning benchmarks, ReasonMaxxer matches or exceeds full RL performance while requiring only tens of problems and minutes of single-GPU training, a reduction in training cost of roughly three orders of magnitude.

### Key Technical Approach

Entropy acts as an effective, fully teacher-free proxy for the decision points that RL would correct. ReasonMaxxer is implemented as a rank-32 LoRA adapter on all attention projections, leaving the base model frozen.

The paper was published on arXiv in May 2026 and represents a significant efficiency improvement in training LLMs for reasoning tasks by leveraging entropy-based gating mechanisms for sparse policy selection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0ef0fe0-a977-4dbc-b464-883e6e3e917b",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "4b405052-a7f5-4151-954a-335830691ff0",
  "toolUseResult": {
    "query": "ReasonMaxxer rethinking RL LLM reasoning entropy gating policy selection 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011W3qhihadTrMyBxJLyzngy",
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
            "title": "The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=vXoksdcfqC"
          },
          {
            "title": "Revisiting Entropy in Reinforcement Learning for Large Reasoning Models",
            "url": "https://arxiv.org/html/2511.05993v3"
          },
          {
            "title": "Quantile Advantage Estimation: Stabilizing RLVR for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.22611"
          },
          {
            "title": "Revisiting Entropy in Reinforcement Learning for Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2511.05993"
          }
        ]
      },
      "I found relevant research on this topic! Here's what the search revealed:\n\n## ReasonMaxxer: Rethinking RL for LLM Reasoning\n\nReasonMaxxer reframes reasoning improvement as sparse policy selection rather than capability acquisition, using a minimal RL-free method that applies contrastive loss only at entropy-gated decision points, with a few hundred base-model rollouts and no online generation.\n\nThe base model's own entropy identifies these decision positions without any RL-trained model, and the entire correction is low-dimensional, representable in a tiny fraction of model parameters.\n\n### Performance and Efficiency\n\nAcross three model families, six scales, and six math reasoning benchmarks, ReasonMaxxer matches or exceeds full RL performance while requiring only tens of problems and minutes of single-GPU training, a reduction in training cost of roughly three orders of magnitude.\n\n### Key Technical Approach\n\nEntropy acts as an effective, fully teacher-free proxy for the decision points that RL would correct. ReasonMaxxer is implemented as a rank-32 LoRA adapter on all attention projections, leaving the base model frozen.\n\nThe paper was published on arXiv in May 2026 and represents a significant efficiency improvement in training LLMs for reasoning tasks by leveraging entropy-based gating mechanisms for sparse policy selection."
    ],
    "durationSeconds": 7.711746070000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f0ef0fe0-a977-4dbc-b464-883e6e3e917b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-29T08:21:32.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012dcZxXiMtaezztQnb4MBh1`</summary>

```json
{
  "query": "AbstRaL abstract reasoning reinforcement learning ICLR 2026 experimental design GSM robustness"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b405052-a7f5-4151-954a-335830691ff0",
  "isSidechain": false,
  "requestId": "req_011CbWY1fLJUzRkp5PLmhvwy",
  "type": "assistant",
  "uuid": "cc0cfca9-911c-4e8f-ad9c-fb8036d82ab4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111aU45YXyiFM766aiaRA7y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 23165,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 736,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 23165,
          "cache_creation_input_tokens": 736,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 736
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

_source line 27 · 2026-05-29T08:21:42.340Z_

<details><summary>↩ Tool result · `toolu_012dcZxXiMtaezztQnb4MBh1`</summary>

```text
Web search results for query: "AbstRaL abstract reasoning reinforcement learning ICLR 2026 experimental design GSM robustness"

Links: [{"title":"ABSTRAL: AUGMENTING LLMS' REASONING BY ...","url":"https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"},{"title":"International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-iclr-2026"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/abstral"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/html/2506.07751"},{"title":"[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/abs/2506.07751"}]

Based on the search results, here's what I found about AbstRaL:

## Overview

AbstRaL is a paper under review as a conference paper at ICLR 2026 that addresses the fact that large language models (LLMs), especially smaller ones, often lack robustness in grade school math (GSM) reasoning. The paper is by Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe, and is being presented as a poster at ICLR 2026.

## Problem Addressed

LLMs tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses.

## Approach and Methodology

The work focuses on the strategy of "abstracting" reasoning problems rather than generating synthetic data. The abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions. The method teaches LLMs to generate mathematical abstractions of input GSM problems using granularly-decomposed abstract reasoning data, and on top of supervised fine-tuning, AbstRaL uses reinforcement learning with model-free rewards to further improve the faithfulness of generated abstraction.

## Experimental Results

AbstRaL was tested on two benchmarks that evaluate the robustness of GSM reasoning (GSM-Symbolic and GSM-Plus), and experimental results on various seed LLMs consistently demonstrate that AbstRaL effectively improves the GSM reasoning robustness of LLMs. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cc0cfca9-911c-4e8f-ad9c-fb8036d82ab4",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "e84a10f4-c9d7-4419-a913-3f2d6752bfc7",
  "toolUseResult": {
    "query": "AbstRaL abstract reasoning reinforcement learning ICLR 2026 experimental design GSM robustness",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QNRtMYZef1sPaUiiB4dxGV",
        "content": [
          {
            "title": "ABSTRAL: AUGMENTING LLMS' REASONING BY ...",
            "url": "https://openreview.net/pdf/cc239e2e8102d68f6e31bcda2af53e08d6bb6a91.pdf"
          },
          {
            "title": "International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/updates/apple-at-iclr-2026"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/abstral"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/pdf/2506.07751"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/html/2506.07751"
          },
          {
            "title": "[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/abs/2506.07751"
          }
        ]
      },
      "Based on the search results, here's what I found about AbstRaL:\n\n## Overview\n\nAbstRaL is a paper under review as a conference paper at ICLR 2026 that addresses the fact that large language models (LLMs), especially smaller ones, often lack robustness in grade school math (GSM) reasoning. The paper is by Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe, and is being presented as a poster at ICLR 2026.\n\n## Problem Addressed\n\nLLMs tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses.\n\n## Approach and Methodology\n\nThe work focuses on the strategy of \"abstracting\" reasoning problems rather than generating synthetic data. The abstraction process is better acquired through reinforcement learning (RL) than just supervised fine-tuning, which often fails to produce faithful abstractions. The method teaches LLMs to generate mathematical abstractions of input GSM problems using granularly-decomposed abstract reasoning data, and on top of supervised fine-tuning, AbstRaL uses reinforcement learning with model-free rewards to further improve the faithfulness of generated abstraction.\n\n## Experimental Results\n\nAbstRaL was tested on two benchmarks that evaluate the robustness of GSM reasoning (GSM-Symbolic and GSM-Plus), and experimental results on various seed LLMs consistently demonstrate that AbstRaL effectively improves the GSM reasoning robustness of LLMs. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on out-of-distribution mathematical and general reasoning tasks."
    ],
    "durationSeconds": 9.98712210600001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cc0cfca9-911c-4e8f-ad9c-fb8036d82ab4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-29T08:21:45.617Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RewsCEwMG4GbykPuAtJkZK`</summary>

```json
{
  "query": "COPO consistency-aware policy optimization GRPO zero-gradient 2025 experimental baselines ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e84a10f4-c9d7-4419-a913-3f2d6752bfc7",
  "isSidechain": false,
  "requestId": "req_011CbWY2eXiKLLTjw7pAbsUA",
  "type": "assistant",
  "uuid": "f620ce12-1e4d-41f4-8ac6-88a513722412",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3brEW4BSJGdWVw1Ub1jQC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 23901,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 23901,
          "cache_creation_input_tokens": 847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 847
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

_source line 29 · 2026-05-29T08:21:52.104Z_

<details><summary>↩ Tool result · `toolu_01RewsCEwMG4GbykPuAtJkZK`</summary>

```text
Web search results for query: "COPO consistency-aware policy optimization GRPO zero-gradient 2025 experimental baselines ablation"

Links: [{"title":"COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/html/2508.04138v1"},{"title":"COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,","url":"https://arxiv.org/pdf/2508.04138"},{"title":"Self-Consistency Rewards in GRPO","url":"https://www.emergentmind.com/topics/self-consistency-rewards-group-relative-policy-optimization"},{"title":"COPO: Consistency-Aware Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=JkmKzsMaAu"},{"title":"COPO: Consistency-Aware Policy Optimization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/copo-consistency-aware-policy-optimization"},{"title":"COPO: CONSISTENCY-AWARE POLICY OPTIMIZA- TION","url":"https://openreview.net/pdf?id=JkmKzsMaAu"},{"title":"Paper page - It Takes Two: Your GRPO Is Secretly DPO","url":"https://huggingface.co/papers/2510.00977"},{"title":"[2508.04138] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138"},{"title":"[2508.04138v1] COPO: Consistency-Aware Policy Optimization","url":"https://arxiv.org/abs/2508.04138v1"}]

Based on the search results, here's what I found about COPO and related methods:

## COPO: Consistency-Aware Policy Optimization

COPO is a consistency-aware policy optimization framework that introduces a structured global reward based on outcome consistency. The work builds on the surge of interest following DeepSeek R1 in leveraging rule-based rewards as a low-cost alternative for computing advantage functions and guiding policy optimization.

### The Problem Being Addressed

A common challenge with GRPO-based methods is that when multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero, leading to vanishing gradients and rendering the corresponding samples ineffective for learning.

### Key Features and Approach

COPO incorporates global optimization into the GRPO foundation to mitigate gradient vanishing caused by intra-group consistency. COPO introduces a consistency-entropy-based hybrid mechanism to effectively integrate intra-group local optimization with inter-group global optimization.

### Experimental Results and Baselines

In experiments on MATH-500 and AIME24, GRPO achieves rapid accuracy increase in early stages but suffers performance drop in later steps, while COPO maintains relatively stable performance and achieves the best results in later training stages. DAPO performs poorly compared to GRPO when trained with the same amount of data, achieving only 5.47% maximum accuracy on AIME24, and performs even worse on the 7B model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f620ce12-1e4d-41f4-8ac6-88a513722412",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "3a10a5bf-61b2-40ba-9c45-a451fe263762",
  "toolUseResult": {
    "query": "COPO consistency-aware policy optimization GRPO zero-gradient 2025 experimental baselines ablation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PEv2SqQDuNRd4fxRv5DvH2",
        "content": [
          {
            "title": "COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/html/2508.04138v1"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization Jinghang Han1*, Jiawei Chen1,2*,",
            "url": "https://arxiv.org/pdf/2508.04138"
          },
          {
            "title": "Self-Consistency Rewards in GRPO",
            "url": "https://www.emergentmind.com/topics/self-consistency-rewards-group-relative-policy-optimization"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=JkmKzsMaAu"
          },
          {
            "title": "COPO: Consistency-Aware Policy Optimization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/copo-consistency-aware-policy-optimization"
          },
          {
            "title": "COPO: CONSISTENCY-AWARE POLICY OPTIMIZA- TION",
            "url": "https://openreview.net/pdf?id=JkmKzsMaAu"
          },
          {
            "title": "Paper page - It Takes Two: Your GRPO Is Secretly DPO",
            "url": "https://huggingface.co/papers/2510.00977"
          },
          {
            "title": "[2508.04138] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138"
          },
          {
            "title": "[2508.04138v1] COPO: Consistency-Aware Policy Optimization",
            "url": "https://arxiv.org/abs/2508.04138v1"
          }
        ]
      },
      "Based on the search results, here's what I found about COPO and related methods:\n\n## COPO: Consistency-Aware Policy Optimization\n\nCOPO is a consistency-aware policy optimization framework that introduces a structured global reward based on outcome consistency. The work builds on the surge of interest following DeepSeek R1 in leveraging rule-based rewards as a low-cost alternative for computing advantage functions and guiding policy optimization.\n\n### The Problem Being Addressed\n\nA common challenge with GRPO-based methods is that when multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero, leading to vanishing gradients and rendering the corresponding samples ineffective for learning.\n\n### Key Features and Approach\n\nCOPO incorporates global optimization into the GRPO foundation to mitigate gradient vanishing caused by intra-group consistency. COPO introduces a consistency-entropy-based hybrid mechanism to effectively integrate intra-group local optimization with inter-group global optimization.\n\n### Experimental Results and Baselines\n\nIn experiments on MATH-500 and AIME24, GRPO achieves rapid accuracy increase in early stages but suffers performance drop in later steps, while COPO maintains relatively stable performance and achieves the best results in later training stages. DAPO performs poorly compared to GRPO when trained with the same amount of data, achieving only 5.47% maximum accuracy on AIME24, and performs even worse on the 7B model."
    ],
    "durationSeconds": 6.4798319099999935,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f620ce12-1e4d-41f4-8ac6-88a513722412",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-29T08:21:52.110Z_

```json
{
  "parentUuid": "3a10a5bf-61b2-40ba-9c45-a451fe263762",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "fe24c7fa-a645-4dd7-a4af-b230ae4356f3",
  "timestamp": "2026-05-29T08:21:52.110Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-29T08:21:55.143Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MNu6crQE8rvrCEvRiN8bVT`</summary>

```json
{
  "query": "Qwen3-8B GRPO training math reasoning compute requirements 8xH100 training cost 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe24c7fa-a645-4dd7-a4af-b230ae4356f3",
  "isSidechain": false,
  "requestId": "req_011CbWY3NJRiSTaozLLvsN4f",
  "type": "assistant",
  "uuid": "ac45c917-0029-426a-b430-1fc4d13d504d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H28HrWZ3ucWQQVbd633rfr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 967,
      "cache_read_input_tokens": 24748,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 967,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 24748,
          "cache_creation_input_tokens": 967,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 967
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

_source line 32 · 2026-05-29T08:22:01.878Z_

<details><summary>↩ Tool result · `toolu_01MNu6crQE8rvrCEvRiN8bVT`</summary>

```text
Web search results for query: "Qwen3-8B GRPO training math reasoning compute requirements 8xH100 training cost 2026"

Links: [{"title":"Qwen3-8b-base SFT+GRPO Training Report | My Blog","url":"https://dtianyou.com/en/notes/qwen3-8b-base-training/"},{"title":"Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models","url":"https://arxiv.org/pdf/2507.18014"},{"title":"Post Training Qwen3 for Math Reasoning Using GRPO - PyImageSearch","url":"https://pyimagesearch.com/2025/09/08/post-training-qwen3-for-math-reasoning-using-grpo/"},{"title":"Qwen 3 Mathematical Reasoning Fine Tuning with GRPO Technique #1","url":"https://todatabeyond.substack.com/p/qwen-3-mathematical-reasoning-fine"},{"title":"Qwen3 8B | Open Laboratory","url":"https://openlaboratory.com/models/qwen3-8b/"},{"title":"Qwen3-8B-Base: Open 8B LLM Overview","url":"https://www.emergentmind.com/topics/qwen3-8b-base"},{"title":"Qwen3-8B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-8b"},{"title":"Qwen/Qwen3-8B · Hugging Face","url":"https://huggingface.co/Qwen/Qwen3-8B"}]

I found some relevant information about Qwen3-8B GRPO training for math reasoning. Based on the search results:

**Training Setup:**
For training the Qwen3-8b-base model with SFT and GRPO, eight RTX 4090 GPUs, each with 48GB of VRAM, were used, totaling 384GB, though this differs from your H100 specification.

**Mathematical Reasoning Focus:**
The training process uses SFT (Supervised Fine-tuning) and GRPO to enhance the model's performance on mathematical problem-solving, especially for the GSM8K and AIME24 datasets.

**Compute Efficiency Insights:**
A key finding is that training beyond roughly 80% of a single epoch yields negligible reward gains while consuming a substantial fraction of total computation, and using scaling laws can forecast phase transitions early to substantially reduce GRPO compute without sacrificing final performance.

However, the search results don't contain specific information about 8xH100 training costs or 2026 pricing. For more specific cost estimates with H100 hardware and current 2026 pricing, you may need to consult cloud computing provider pricing pages (AWS, GCP, Azure) or more recent infrastructure cost analysis reports.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac45c917-0029-426a-b430-1fc4d13d504d",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "aef2a43e-5003-471e-b8cd-964e75c6dad1",
  "toolUseResult": {
    "query": "Qwen3-8B GRPO training math reasoning compute requirements 8xH100 training cost 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VcVZRdDPAzEmMqfhmzAw9s",
        "content": [
          {
            "title": "Qwen3-8b-base SFT+GRPO Training Report | My Blog",
            "url": "https://dtianyou.com/en/notes/qwen3-8b-base-training/"
          },
          {
            "title": "Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2507.18014"
          },
          {
            "title": "Post Training Qwen3 for Math Reasoning Using GRPO - PyImageSearch",
            "url": "https://pyimagesearch.com/2025/09/08/post-training-qwen3-for-math-reasoning-using-grpo/"
          },
          {
            "title": "Qwen 3 Mathematical Reasoning Fine Tuning with GRPO Technique #1",
            "url": "https://todatabeyond.substack.com/p/qwen-3-mathematical-reasoning-fine"
          },
          {
            "title": "Qwen3 8B | Open Laboratory",
            "url": "https://openlaboratory.com/models/qwen3-8b/"
          },
          {
            "title": "Qwen3-8B-Base: Open 8B LLM Overview",
            "url": "https://www.emergentmind.com/topics/qwen3-8b-base"
          },
          {
            "title": "Qwen3-8B: Specifications and GPU VRAM Requirements",
            "url": "https://apxml.com/models/qwen3-8b"
          },
          {
            "title": "Qwen/Qwen3-8B · Hugging Face",
            "url": "https://huggingface.co/Qwen/Qwen3-8B"
          }
        ]
      },
      "I found some relevant information about Qwen3-8B GRPO training for math reasoning. Based on the search results:\n\n**Training Setup:**\nFor training the Qwen3-8b-base model with SFT and GRPO, eight RTX 4090 GPUs, each with 48GB of VRAM, were used, totaling 384GB, though this differs from your H100 specification.\n\n**Mathematical Reasoning Focus:**\nThe training process uses SFT (Supervised Fine-tuning) and GRPO to enhance the model's performance on mathematical problem-solving, especially for the GSM8K and AIME24 datasets.\n\n**Compute Efficiency Insights:**\nA key finding is that training beyond roughly 80% of a single epoch yields negligible reward gains while consuming a substantial fraction of total computation, and using scaling laws can forecast phase transitions early to substantially reduce GRPO compute without sacrificing final performance.\n\nHowever, the search results don't contain specific information about 8xH100 training costs or 2026 pricing. For more specific cost estimates with H100 hardware and current 2026 pricing, you may need to consult cloud computing provider pricing pages (AWS, GCP, Azure) or more recent infrastructure cost analysis reports."
    ],
    "durationSeconds": 6.730526668999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ac45c917-0029-426a-b430-1fc4d13d504d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-29T08:22:04.907Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015dbiBa2VGBjYetzKeTg9iR`</summary>

```json
{
  "query": "JS divergence consistency loss RL training stability perturbation robustness NLP PPCL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aef2a43e-5003-471e-b8cd-964e75c6dad1",
  "isSidechain": false,
  "requestId": "req_011CbWY463u7VWJhYrJjisTy",
  "type": "assistant",
  "uuid": "5e5c36c6-4a33-446a-81af-e4e441027cfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JUc9ifqiM5HRdSKEN22QdR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 25715,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 797,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 25715,
          "cache_creation_input_tokens": 797,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 797
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

_source line 34 · 2026-05-29T08:22:10.555Z_

<details><summary>↩ Tool result · `toolu_015dbiBa2VGBjYetzKeTg9iR`</summary>

```text
Web search results for query: "JS divergence consistency loss RL training stability perturbation robustness NLP PPCL 2024"

Links: [{"title":"Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology","url":"https://aclanthology.org/2024.findings-eacl.91/"},{"title":"Published as a conference paper at ICLR 2024","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf"},{"title":"TaiChi: Improving the Robustness of NLP Models by Seeking Common Ground While Reserving Differences - ACL Anthology","url":"https://aclanthology.org/2024.lrec-main.1351/"},{"title":"Achieving Generalizable Robustness of Deep Neural Networks by Stability   Training","url":"https://arxiv.org/pdf/1906.00735"},{"title":"Generalized Jensen-Shannon Divergence Loss for Learning with Noisy   Labels","url":"https://arxiv.org/pdf/2105.04522"},{"title":"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs","url":"https://arxiv.org/pdf/2510.14242"}]

Based on the web search results, I found relevant information about your query:

Prompt Perturbation Consistency Learning (PPCL) is an efficient mitigation approach that works by regularizing the divergence between losses from clean and perturbed samples. PPCL can recover on average 59% and 69% of the performance drop for intent classification and semantic frame tasks, respectively, and beats data augmentation while using ten times fewer augmented data samples.

The approach relates to broader research on robustness in NLP. Jensen-Shannon divergence (JS) has been adopted to encourage consistency of predictions, with previous work showing promise for test-time robustness to domain shift, and demonstrating training-time robustness to label noise.

Additionally, recent work minimizes JS divergence among datapoints within high-confidence consensus groups and KL divergence between other datapoints and that group to promote consistency under prompt perturbations in language models.

These methods collectively address training stability and robustness in NLP through consistency learning mechanisms with divergence-based regularization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5e5c36c6-4a33-446a-81af-e4e441027cfa",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "5f45ecc1-9af2-491f-aee1-b17153994c44",
  "toolUseResult": {
    "query": "JS divergence consistency loss RL training stability perturbation robustness NLP PPCL 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JkBeXrTFDsWEuRrq1pz3sD",
        "content": [
          {
            "title": "Prompt Perturbation Consistency Learning for Robust Language Models - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-eacl.91/"
          },
          {
            "title": "Published as a conference paper at ICLR 2024",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/6246f93ebf4f2d76ad2bcb3158220d34-Paper-Conference.pdf"
          },
          {
            "title": "TaiChi: Improving the Robustness of NLP Models by Seeking Common Ground While Reserving Differences - ACL Anthology",
            "url": "https://aclanthology.org/2024.lrec-main.1351/"
          },
          {
            "title": "Achieving Generalizable Robustness of Deep Neural Networks by Stability   Training",
            "url": "https://arxiv.org/pdf/1906.00735"
          },
          {
            "title": "Generalized Jensen-Shannon Divergence Loss for Learning with Noisy   Labels",
            "url": "https://arxiv.org/pdf/2105.04522"
          },
          {
            "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
            "url": "https://arxiv.org/pdf/2510.14242"
          }
        ]
      },
      "Based on the web search results, I found relevant information about your query:\n\nPrompt Perturbation Consistency Learning (PPCL) is an efficient mitigation approach that works by regularizing the divergence between losses from clean and perturbed samples. PPCL can recover on average 59% and 69% of the performance drop for intent classification and semantic frame tasks, respectively, and beats data augmentation while using ten times fewer augmented data samples.\n\nThe approach relates to broader research on robustness in NLP. Jensen-Shannon divergence (JS) has been adopted to encourage consistency of predictions, with previous work showing promise for test-time robustness to domain shift, and demonstrating training-time robustness to label noise.\n\nAdditionally, recent work minimizes JS divergence among datapoints within high-confidence consensus groups and KL divergence between other datapoints and that group to promote consistency under prompt perturbations in language models.\n\nThese methods collectively address training stability and robustness in NLP through consistency learning mechanisms with divergence-based regularization."
    ],
    "durationSeconds": 5.643925724000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5e5c36c6-4a33-446a-81af-e4e441027cfa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reasoning models suffer 47–73% accuracy drops under trivial surface-form perturbations (nu…",
  "leafUuid": "5f45ecc1-9af2-491f-aee1-b17153994c44",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Tool call

_source line 37 · 2026-05-29T08:22:13.733Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NerXfCwLDcgA1SXfdXHSGP`</summary>

```json
{
  "query": "CLIPO contrastive learning policy optimization GRPO reasoning 2026 experimental setup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f45ecc1-9af2-491f-aee1-b17153994c44",
  "isSidechain": false,
  "requestId": "req_011CbWY4jFnB7Av2e2mFN968",
  "type": "assistant",
  "uuid": "bb0d84eb-a260-4cc8-b913-bd0150477aa8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R5gPyMa2dZVtAbaK2xa6uy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 678,
      "cache_read_input_tokens": 26512,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 678,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 26512,
          "cache_creation_input_tokens": 678,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 678
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

_source line 38 · 2026-05-29T08:22:20.972Z_

<details><summary>↩ Tool result · `toolu_01NerXfCwLDcgA1SXfdXHSGP`</summary>

```text
Web search results for query: "CLIPO contrastive learning policy optimization GRPO reasoning 2026 experimental setup"

Links: [{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/pdf/2603.10101"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://www.researchgate.net/publication/401833359_CLIPO_Contrastive_Learning_in_Policy_Optimization_Generalizes_RLVR"},{"title":"Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models","url":"https://arxiv.org/html/2605.25443"},{"title":"Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://huggingface.co/papers/2603.10101"},{"title":"GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub","url":"https://github.com/Qwen-Applications/CLIPO"},{"title":"[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/abs/2603.10101"},{"title":"Qwen Applications Business Group · GitHub","url":"https://github.com/Qwen-Applications"},{"title":"A Unified Framework for Rethinking Policy Divergence Measures in GRPO","url":"https://arxiv.org/pdf/2602.05494"}]

Based on the search results, I found relevant information about CLIPO and its experimental setup:

## CLIPO Overview

CLIPO incorporates a Contrastive Learning mechanism into Policy Optimization to generalize the RLVR (Reinforcement Learning with Verifiable Rewards) process. CLIPO introduces a lightweight contrastive head and an intra-group contrastive objective into RLVR-style policy optimization.

## Core Mechanism

By optimizing a contrastive loss over successful rollouts, CLIPO steers the LLM to capture the invariant structure shared across correct reasoning paths. By aligning multiple successful reasoning trajectories and contrasting them against incorrect ones, the method extracts invariant reasoning structures shared by correct rollouts, yielding a dense contrastive reward that complements standard outcome-based verifiable rewards.

## Experimental Results

CLIPO gains across GRPO, GSPO, DAPO, and GMPO in overall average scores by +1.35, +0.80, +1.20, and +0.83 respectively. CLIPO attains either the best or second-best performance across all four general reasoning benchmarks. The method improves robustness and generalization, especially under distribution shifts and hard mathematical reasoning benchmarks.

## Relation to GRPO

CLIPO is a GRPO variant that computes contrastive rewards within each rollout group for a prompt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb0d84eb-a260-4cc8-b913-bd0150477aa8",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "d9b4dff5-7621-406f-bed3-2c909f965449",
  "toolUseResult": {
    "query": "CLIPO contrastive learning policy optimization GRPO reasoning 2026 experimental setup",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xpz5YGu5eE1RdWYG9QXLer",
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
            "title": "Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models",
            "url": "https://arxiv.org/html/2605.25443"
          },
          {
            "title": "Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://huggingface.co/papers/2603.10101"
          },
          {
            "title": "GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub",
            "url": "https://github.com/Qwen-Applications/CLIPO"
          },
          {
            "title": "[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/abs/2603.10101"
          },
          {
            "title": "Qwen Applications Business Group · GitHub",
            "url": "https://github.com/Qwen-Applications"
          },
          {
            "title": "A Unified Framework for Rethinking Policy Divergence Measures in GRPO",
            "url": "https://arxiv.org/pdf/2602.05494"
          }
        ]
      },
      "Based on the search results, I found relevant information about CLIPO and its experimental setup:\n\n## CLIPO Overview\n\nCLIPO incorporates a Contrastive Learning mechanism into Policy Optimization to generalize the RLVR (Reinforcement Learning with Verifiable Rewards) process. CLIPO introduces a lightweight contrastive head and an intra-group contrastive objective into RLVR-style policy optimization.\n\n## Core Mechanism\n\nBy optimizing a contrastive loss over successful rollouts, CLIPO steers the LLM to capture the invariant structure shared across correct reasoning paths. By aligning multiple successful reasoning trajectories and contrasting them against incorrect ones, the method extracts invariant reasoning structures shared by correct rollouts, yielding a dense contrastive reward that complements standard outcome-based verifiable rewards.\n\n## Experimental Results\n\nCLIPO gains across GRPO, GSPO, DAPO, and GMPO in overall average scores by +1.35, +0.80, +1.20, and +0.83 respectively. CLIPO attains either the best or second-best performance across all four general reasoning benchmarks. The method improves robustness and generalization, especially under distribution shifts and hard mathematical reasoning benchmarks.\n\n## Relation to GRPO\n\nCLIPO is a GRPO variant that computes contrastive rewards within each rollout group for a prompt."
    ],
    "durationSeconds": 7.234812357999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bb0d84eb-a260-4cc8-b913-bd0150477aa8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-29T08:22:24.048Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MbLvM8y8XCUTfLMs4D27sE`</summary>

```json
{
  "query": "RULES eligibility reasoning RL lemma verification math 2026 arXiv 2602.00998"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d9b4dff5-7621-406f-bed3-2c909f965449",
  "isSidechain": false,
  "requestId": "req_011CbWY5VhUZuKCgDPEeXbiZ",
  "type": "assistant",
  "uuid": "85069168-88e5-4b95-94a0-e9776cc310ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M6uTtNUL9vhueF5dVigtDi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 827,
      "cache_read_input_tokens": 27190,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 827,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 27190,
          "cache_creation_input_tokens": 827,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 827
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

_source line 40 · 2026-05-29T08:22:31.965Z_

<details><summary>↩ Tool result · `toolu_01MbLvM8y8XCUTfLMs4D27sE`</summary>

```text
Web search results for query: "RULES eligibility reasoning RL lemma verification math 2026 arXiv 2602.00998"

Links: [{"title":"[2602.00998] Reliable Use of Lemmas via Eligibility Reasoning and Section$-$Aware Reinforcement Learning","url":"https://arxiv.org/abs/2602.00998"},{"title":"Reliable Use of Lemmas via Eligibility Reasoning and Section$-$Aware Reinforcement Learning","url":"https://arxiv.org/pdf/2602.00998"},{"title":"Reliable Use of Lemmas via Eligibility Reasoning and Section‑Aware Reinforcement Learning","url":"https://arxiv.org/html/2602.00998"},{"title":"From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.22203"},{"title":"TinyV: Reducing False Negatives in Verification Improves RL for LLM Reasoning","url":"https://arxiv.org/pdf/2505.14625"},{"title":"Long-horizon Reasoning Agent for Olympiad-Level ...","url":"https://arxiv.org/pdf/2512.10739"}]

Based on the search results, I found the arXiv paper you're looking for:

**Title:** "Reliable Use of Lemmas via Eligibility Reasoning and Section-Aware Reinforcement Learning" by Zhikun Xu, Xiaodong Yu, Ben Zhou, and others from Arizona State University and Advanced Micro Devices, Inc.

**Overview:**

Recent large language models (LLMs) perform strongly on mathematical benchmarks yet often misapply lemmas, importing conclusions without validating assumptions. 

The paper formalizes lemma-judging as a structured prediction task where given a statement and a candidate lemma, the model must output a precondition check and a conclusion-utility check, from which a usefulness decision is derived. RULES encodes this specification via a two-section output and trains with reinforcement learning plus section-aware loss masking to assign penalty to the section responsible for errors.

**Evaluation:**

Training and evaluation draw on diverse natural-language and formal proof corpora; robustness is assessed with a held-out perturbation suite; and end-to-end evaluation spans competition-style, perturbation-aligned, and theorem-based problems across various LLMs.

Results show consistent in-domain gains over both a vanilla model and a single-label RL baseline, larger improvements on applicability-breaking perturbations, and parity or modest gains on end-to-end tasks; ablations indicate that the two-section outputs and section-aware reinforcement are both necessary for robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85069168-88e5-4b95-94a0-e9776cc310ba",
  "isSidechain": false,
  "promptId": "2967b62a-36fb-4b61-b924-0720a43a0dcf",
  "type": "user",
  "uuid": "4aef23ed-0989-4dec-8cc2-1941c84f1d27",
  "toolUseResult": {
    "query": "RULES eligibility reasoning RL lemma verification math 2026 arXiv 2602.00998",
    "results": [
      {
        "tool_use_id": "srvtoolu_019i3YAAtmkg4MpRDwnrUKw4",
        "content": [
          {
            "title": "[2602.00998] Reliable Use of Lemmas via Eligibility Reasoning and Section$-$Aware Reinforcement Learning",
            "url": "https://arxiv.org/abs/2602.00998"
          },
          {
            "title": "Reliable Use of Lemmas via Eligibility Reasoning and Section$-$Aware Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2602.00998"
          },
          {
            "title": "Reliable Use of Lemmas via Eligibility Reasoning and Section‑Aware Reinforcement Learning",
            "url": "https://arxiv.org/html/2602.00998"
          },
          {
            "title": "From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.22203"
          },
          {
            "title": "TinyV: Reducing False Negatives in Verification Improves RL for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2505.14625"
          },
          {
            "title": "Long-horizon Reasoning Agent for Olympiad-Level ...",
            "url": "https://arxiv.org/pdf/2512.10739"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper you're looking for:\n\n**Title:** \"Reliable Use of Lemmas via Eligibility Reasoning and Section-Aware Reinforcement Learning\" by Zhikun Xu, Xiaodong Yu, Ben Zhou, and others from Arizona State University and Advanced Micro Devices, Inc.\n\n**Overview:**\n\nRecent large language models (LLMs) perform strongly on mathematical benchmarks yet often misapply lemmas, importing conclusions without validating assumptions. \n\nThe paper formalizes lemma-judging as a structured prediction task where given a statement and a candidate lemma, the model must output a precondition check and a conclusion-utility check, from which a usefulness decision is derived. RULES encodes this specification via a two-section output and trains with reinforcement learning plus section-aware loss masking to assign penalty to the section responsible for errors.\n\n**Evaluation:**\n\nTraining and evaluation draw on diverse natural-language and formal proof corpora; robustness is assessed with a held-out perturbation suite; and end-to-end evaluation spans competition-style, perturbation-aligned, and theorem-based problems across various LLMs.\n\nResults show consistent in-domain gains over both a vanilla model and a single-label RL baseline, larger improvements on applicability-breaking perturbations, and parity or modest gains on end-to-end tasks; ablations indicate that the two-section outputs and section-aware reinforcement are both necessary for robustness."
    ],
    "durationSeconds": 7.912231589999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "85069168-88e5-4b95-94a0-e9776cc310ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-29T08:23:27.656Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information from my pre-research to provide a thorough analysis. Let me synthesize what I've found and assess the experimental design of this proposal.

Key findings from research:
1. **GRPO variants landscape**: There are many GRPO variants (GRPO-LEAD, DRA-GRPO, Scaf-GRPO, etc.) that the proposal doesn't include as baselines. Some are quite relevant.
2. **VAR-MATH and MATH-Perturb**: Both are well-established benchmarks for robustness evaluation. The proposal correctly identifies them.


3. **TA-GRPO through AbstRaL**: I'm reviewing several related approaches—TA-GRPO validates that pooling is critical beyond just augmentation, ROMA applies token-level KL consistency for visual robustness which is methodologically closest, CLIPO and COPO are mentioned as baselines addressing contrastive learning and zero-gradient issues respectively, ReasonMaxxer contributes the entropy-gating insight the proposal adopts, and AbstRaL is noted as GSM-level only.

4. **Training and efficiency validation**: The Qwen3-8B GRPO training used 8×RTX 4090s, so 8×H100s would be more than adequate, and PPCL's JS-divergence consistency achieving 10× sample efficiency over augmentation-only validates the core approach.

5. **Baseline coverage check**: I'm systematically assessing the eight baselines—vanilla GRPO, DAPO, Dr.GRPO, TA-GRPO, COPO, augmentation-only GRPO, ReasonMaxxer, and AbstRaL—and noting that CLIPO should potentially be included given how extensively it appears in the related work.

6. **CLIPO as a critical missing baseline**: CLIPO does contrastive learning within GRPO to extract invariant reasoning structures, making it methodologically very similar to ConsistRL's contrastive discrimination loss approach, so its absence from the baseline comparisons is a notable gap.

7. **RLTR should also be included**: Since RLTR improves robustness through transfer rewards and the proposal explicitly targets robustness improvements, this baseline comparison would be expected by reviewers.

For the evaluation, VAR-MATH and MATH-Perturb are solid core benchmarks, with Robust Reasoning Benchmark as a useful supplement. GSM-Symbolic from ICLR 2025 is mentioned in the problem setup but missing from the evaluation plan, even though AbstRaL was tested on it, so that's worth considering.

The ablation study covers the main components well across six configurations, systematically isolating the Jensen-Shannon divergence, contrastive loss, entropy gating, and pooling mechanisms.

One gap I'm noticing: there's no ablation specifically on perturbation quality itself—whether using verified versus unverified perturbations makes a difference, even though the proposal mentions both SymPy and human verification approaches.

The dual evaluation protocol with both step-matched and FLOP-matched comparisons is a real strength here. For feasibility, the 8×H100 setup for Qwen3-8B is reasonable, though the GPT-4 pipeline for generating semantics-altering perturbations raises some cost and quality concerns, and SymPy verification only works for algebraically tractable problems. Human verification at scale (200+ and 300+ problems with dual annotators) is doable but resource-intensive.

Now I'm seeing some critical gaps that reviewers would catch immediately: CLIPO and RLTR are both missing from the baselines, which is a significant oversight. There's also a potential reliability issue with the perturbation pipeline itself—I need to understand what fraction of MATH problems the symbolic component can actually handle, and how well SymPy verification covers the LLM-generated paraphrases, since low coverage could introduce bias toward certain problem types. The discrimination loss training data from GPT-4 also needs verification to ensure quality.

Beyond that, there's a subtle contamination risk even with train/eval separation—since MATH-Perturb is derived from MATH level-5 problems, using perturbations of those problems for training could leak shared problem structures into evaluation. And there's a fundamental issue with entropy gating during GRPO training: the entropy landscape shifts as the policy distribution evolves, so using static entropy thresholds from initialization might not be appropriate throughout training, yet the proposal treats this as just an ablation extension rather than a core design decision.

The target metrics also lack context—a 10 percentage point improvement in consistency sounds concrete, but without knowing whether the baseline is 20% or 50%, it's hard to judge if that's ambitious or modest. Finally, GSM-Symbolic seems like an odd omission from evaluation given that it's a major robustness benchmark and AbstRaL uses it as a baseline, though I'm second-guessing whether it's actually relevant since the proposal targets competition-level math rather than elementary robustness.

The perturbation type separation ablation is buried as an extension at 1.5B tokens, but it's actually crucial for validating that both perturbation approaches contribute meaningfully—this should probably be a core ablation instead. I'm also noticing the proposal doesn't specify how many rollouts or samples per prompt GRPO will use, which is a significant detail since that directly impacts advantage estimation quality and the consistency loss computation. On feasibility, the compute budget of 8×H100 is substantial but reasonable for an academic setting, the perturbation pipeline is complex but doable, and human verification should scale fine, though I'm realizing the numbers trail off here.

The experimental design is solid overall, but reviewers will definitely flag the missing CLIPO baseline as a critical gap. I should also check whether there are any very recent 2026 papers that might be even more relevant comparisons I haven't considered yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aef23ed-0989-4dec-8cc2-1941c84f1d27",
  "isSidechain": false,
  "requestId": "req_011CbWY6JjCWykSrfvWuBWzq",
  "type": "assistant",
  "uuid": "35a50780-96a7-4622-adb9-4d98a09d4b70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyYAqD444P8kNVnoFyF4fS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 28017,
      "output_tokens": 8040,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8040,
          "cache_read_input_tokens": 28017,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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

_source line 42 · 2026-05-29T08:25:27.867Z_

Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **ROMA (arXiv 2605.09262, May 2026):** Token-level KL consistency during GRPO; ablation separates correctness-conditioned regularization, clean-anchor PG loss, and KL penalty; baselines include vanilla GRPO, GRPO+augmentation, DAPO; evaluates on 7 multimodal benchmarks with seen/unseen corruption split; reports clean-to-degraded accuracy gaps. Most methodologically similar to ConsistRL's invariance objective.
- **TA-GRPO (arXiv 2601.22478, Jan 2026):** Core ablation: TA-GRPO w/o pooling (augmentation only) vs. full pooling, demonstrating pooling is essential. Baselines: GRPO, SFT, online DPO. Evaluated on AMC12, AIME24, AIME25, GPQA-Diamond at Pass@32. No robustness metrics reported.
- **CLIPO (arXiv 2603.10101, Mar 2026):** Contrastive head on GRPO rollouts; tested atop GRPO, GSPO, DAPO, GMPO; evaluated on MATH-500, AIME24/25, AMC23, LiveMathBench, OlympiadBench; gains +0.80–1.35 avg. Directly comparable as contrastive loss within GRPO framework.
- **COPO (arXiv 2508.04138, 2025):** Consistency-entropy hybrid mechanism for GRPO zero-gradient fix; evaluated on MATH-500, AIME24; compared against GRPO, DAPO; shows stable later-stage training.
- **ReasonMaxxer (arXiv 2605.06241, May 2026):** Sparse policy selection at entropy-gated decision points; rank-32 LoRA, no online generation; tested across 3 model families, 6 scales, 6 math benchmarks; matches full RL at ~1000× lower cost.
- **AbstRaL (ICLR 2026):** Symbolic abstraction + RL for GSM robustness; tested on GSM-Symbolic, GSM-Plus; limited to elementary math.
- **PPCL (EACL 2024):** JS-divergence regularization for NLP robustness; reports 10× sample efficiency over augmentation; evaluated on intent classification and semantic frame tasks.
- **DRA-GRPO (arXiv 2505.09655, 2025):** Diverse reasoning paths for GRPO; evaluated on 5 math benchmarks across Qwen3-1.7B and other backbones. Not directly robustness-focused but demonstrates augmentation within GRPO.
- **Qwen3-8B GRPO training:** Community reports confirm 8×RTX 4090 (384GB total) sufficient for full GRPO training; 8×H100 (640GB total, higher FLOPS) is comfortably adequate.
- 调研总结: 该领域当前的实验标准要求：(a) augmentation-only ablation 以隔离 consistency loss 的贡献（ROMA、TA-GRPO 都做了此对照），(b) 同族 GRPO 变体的横向对比（CLIPO 对比了 GRPO/GSPO/DAPO/GMPO），(c) compute-normalized comparison（ROMA 报告了 overhead），(d) seen vs. unseen perturbation type 分离评估。审稿人普遍期望将最相近的方法学工作纳入 baseline，且对 contrastive/consistency loss 类工作会特别关注与 CLIPO 的区分度。

---

【缺陷 1】
- 类别: baseline 不足
- 问题: **CLIPO 未纳入 baseline。** Proposal 在 Research Opportunity 部分详细讨论了 CLIPO（"trajectory-level contrastive learning in GRPO extracts invariant structures across correct reasoning paths"），明确将其作为关键 related work 进行差异化分析，但 8 个 baselines 中没有包含 CLIPO。CLIPO 是当前唯一在 GRPO 框架内引入 contrastive loss 的方法，而 ConsistRL 的 discrimination objective 同样是 contrastive loss。审稿人几乎必然会要求此对比——CLIPO 的 trajectory-level contrastive 和 ConsistRL 的 input-level contrastive 到底各自贡献了什么？不比较就无法支撑 ConsistRL discrimination loss 的增量价值。
- 严重度: 可补救
- 补救方案: 将 CLIPO 加入 baseline 列表（升至 9 个 baselines）。若 CLIPO 开源（GitHub: Qwen-Applications/CLIPO 已公开），直接使用其代码在 Qwen3-8B 上复现；若未开源，根据论文描述复现 contrastive head + intra-group contrastive objective。同时新增一个组合 baseline："CLIPO + ConsistRL invariance loss only"以隔离 input-level invariance和 trajectory-level invariance 的互补性。
- 调研依据: CLIPO (arXiv 2603.10101) GitHub 已公开，代码可获取；CLIPO 论文本身对比了 GRPO/GSPO/DAPO/GMPO，是该方向的核心对照。

【缺陷 2】
- 类别: baseline 不足
- 问题: **RLTR 未纳入 baseline。** Proposal 在 Research Landscape 中提到 "RLTR improves robustness via transfer reward but does not target perturbation-specific invariance"，但未将其列为 baseline。RLTR 是当前极少数直接以 robustness 为目标的 RL 训练方法之一，与 ConsistRL 的核心 claim（提升 robustness）直接可比。缺少此对比会削弱 "ConsistRL 是 robustness 的最优 RL 方案" 这一隐含 claim。
- 严重度: 可补救
- 补救方案: 将 RLTR 加入 baseline（升至 10 个）。若计算资源紧张，可在 1.5B 模型上进行 RLTR 对比（Phase 1），8B 上只保留核心 baselines。RLTR 的 transfer reward 机制与 ConsistRL 的 consistency loss 机制正交，对比结果有较高信息量。
- 调研依据: RLTR (arXiv 2602.08489) 被 proposal 自身列为关键 related work，是直接针对 robustness 的 RL 训练方法。

【缺陷 3】
- 类别: 实验设计不足
- 问题: **Entropy gating 的 static vs. dynamic 选择被降级为"extension (primarily at 1.5B)"，但这是核心设计决策。** Proposal 的 invariance loss 依赖 entropy gating 来选择 decision tokens。GRPO 训练过程中 policy distribution 持续变化，step 0 和 step 1000 的 entropy landscape 可能完全不同。如果使用 static base-model entropy（固定 mask），可能在训练后期错误地 gate 掉了真正需要 consistency 约束的 tokens；如果使用 dynamic policy entropy，则每步的 consistency loss 作用域不同，training dynamics 更难控制。这不是 secondary extension，而是直接影响主实验结果的核心设计选择。
- 严重度: 可补救
- 补救方案: 将 static vs. dynamic entropy gating 对比从 extension 提升为核心 ablation matrix（在 8B 上也做）。在主实验中明确选择一种作为 default（建议 dynamic，理由是 ReasonMaxxer 的分析基于训练后的 policy），并在论文中报告两种方案在 VAR-MATH 和 MATH-Perturb 上的完整对比。同时增加一个 training dynamics 分析：绘制 entropy-gated token 比例随 training step 的变化曲线，验证 entropy gating 的稳定性。
- 调研依据: ReasonMaxxer (arXiv 2605.06241) 的分析表明 RL 修改集中在高 entropy decision points，但其分析是在训练完成后的 policy 上做的，不直接等价于训练过程中的 dynamic entropy。

【缺陷 4】
- 类别: 实验设计不足
- 问题: **Perturbation generation pipeline 的覆盖率和质量未作为实验变量控制。** Proposal 描述了 hybrid pipeline（VAR-MATH symbolic + LLM paraphrasing + SymPy verification），并承诺报告 coverage rate 和 human verification，但未将 perturbation quality 作为 ablation 因素。核心问题是：(a) VAR-MATH 的 symbolic pipeline 覆盖 MATH 数据集的比例是多少？如果只覆盖 30% 的问题类型，那么 invariance loss 的训练数据分布严重偏斜；(b) SymPy verification 对 LLM-generated paraphrases 的 pass rate 是多少？如果大量 paraphrases 被过滤掉，实际训练数据量可能不足；(c) discrimination loss 的训练数据依赖 GPT-4 生成 + SymPy 验证"解不同"，但 AIME 等竞赛题很多没有 closed-form symbolic solution，SymPy 验证覆盖率可能很低。
- 严重度: 可补救
- 补救方案: (1) 在实验 setup 中报告 perturbation pipeline 的 coverage statistics：symbolic pipeline 覆盖的 MATH 问题比例、LLM paraphrasing 的 SymPy pass rate、discrimination 数据的 SymPy verification 覆盖率。(2) 增加一个 ablation：在 high-coverage 问题子集 vs. full dataset 上训练，验证 pipeline 覆盖偏差是否影响结果。(3) 对 SymPy 无法验证的 discrimination 数据，补充数值验证方案（对于有 unique numerical answer 的问题，直接比较答案是否不同）。
- 调研依据: VAR-MATH (arXiv 2507.12885) 的 symbolic pipeline 主要针对 algebra/numerical parameterization 类型；MATH-Perturb 的 hard perturbation taxonomy 包括 constraint addition 等非代数类型，SymPy 覆盖率存疑。基于领域实验规范判断。

【缺陷 5】
- 类别: 评估方案缺陷
- 问题: **Perturbation type 分离评估被降级为 extension。** Proposal 将 "perturbation type separation (variable renaming vs. numerical reparameterization)" 列为 extension (primarily at 1.5B)。但 dual-objective 是 ConsistRL 的核心 claim——invariance for equivalence-preserving, discrimination for semantics-altering。如果不分别报告模型在各 perturbation type 上的表现，审稿人无法验证 dual objective 是否分别起作用。聚合指标可能掩盖一种 objective 完全无效的情况（例如 discrimination loss 没有帮助 MATH-P-Hard，但 JS loss 提升了 VAR-MATH 足够多导致聚合数字好看）。
- 严重度: 可补救
- 补救方案: Proposal 的 evaluation 分组已经按 perturbation type 组织了（VAR-MATH 测 numerical equivalence，MATH-Perturb 测 semantic discrimination），这本身就支持分别报告。将"分别报告 invariance objective 对 VAR-MATH 的贡献"和"discrimination objective 对 MATH-Perturb 的贡献"提升为主实验的核心分析（而非 extension）。具体做法：在 ablation 中的 (2) w/o JS 和 (3) w/o contrastive discrimination 变体上，分别在 VAR-MATH 和 MATH-Perturb 上报告完整结果，形成交叉分析表。
- 调研依据: ROMA (arXiv 2605.09262) 区分 seen/unseen corruption types 分别报告，这是 robustness 论文的标准做法。

【缺陷 6】
- 类别: 实验设计不足
- 问题: **GRPO 关键超参数未规定。** Proposal 未指定 per-prompt rollout 数量（GRPO 标准为 8–64 rollouts/prompt）、temperature、KL penalty coefficient、以及 ConsistRL 新增的 λ₁（JS loss 权重）和 λ₂（contrastive loss 权重）的选择策略。GRPO 的 advantage estimation 质量高度依赖 rollout 数量——如果 rollouts 太少，augmented prompt 组的 advantage pooling 噪声大；如果 rollouts 太多，compute 开销可能导致 FLOP-matched comparison 中 ConsistRL 的步数过少。λ₁ 和 λ₂ 的 sensitivity analysis 被列为 extension，但如果 default 值选择不当，主实验结果不可靠。
- 严重度: 可补救
- 补救方案: (1) 在实验 setup 中明确规定 per-prompt rollout 数量，建议 16（与 TA-GRPO 可比），并在 1.5B 上做 rollout 数量 sensitivity（8/16/32）。(2) 将 λ₁/λ₂ sensitivity analysis 从 extension 提升至核心 ablation（至少在 1.5B 上做 grid search，在 8B 上用 1.5B 最优值）。(3) 报告 ConsistRL 每个 training step 的 per-prompt 实际 rollout 数（包括 augmented prompts 的 rollouts）以支撑 compute fairness 分析。
- 调研依据: TA-GRPO (arXiv 2601.22478) 和 COPO (arXiv 2508.04138) 的实验均明确报告了 rollout 数量和 KL 系数；GRPO 对这些超参数的敏感性在 DRA-GRPO (arXiv 2505.09655) 中有讨论。

【缺陷 7】
- 类别: 可行性问题
- 问题: **Discrimination training data 的 GPT-4 生成成本和质量控制存在风险。** Proposal 要求使用 GPT-4 按 MATH-Perturb 的 hard perturbation taxonomy 生成 semantics-altering perturbations，并需要 SymPy 验证 + 300 题人工标注。但 (a) 生成高质量 hard perturbations 的 prompt engineering 难度大，GPT-4 可能生成大量无效扰动（语义实际未改变，或改变后无解），导致 pipeline 的有效产出率低；(b) MATH 训练集有 7500 道题，如果有效产出率仅 30%，最终只有 ~2250 条有效 discrimination 训练数据，可能不足以训练一个有效的 contrastive loss；(c) 300 题人工标注（2 annotators）对 7500 题训练集来说采样率仅 4%，如果 pipeline 质量不均匀，可能遗漏系统性错误。
- 严重度: 可补救
- 补救方案: (1) 进行 pilot study：先在 200 道 MATH level-5 题上运行完整 pipeline，报告有效产出率和常见失败模式。(2) 将人工标注从 300 扩大到 500（或对 pilot study 中发现的高失败率子类别进行重点标注）。(3) 报告 inter-annotator agreement（κ）作为质量指标。(4) 设定质量底线：若 pipeline 有效产出率 < 50%，改为从 MATH-Perturb 的 hard perturbation taxonomy 直接获取公开数据（如有），或缩小 discrimination 训练集但报告 data efficiency 分析。
- 调研依据: MATH-Perturb (ICML 2025) 的 279 道题是人工精心构建的，成本极高；自动化 pipeline 的质量通常远低于人工标注。基于领域实验规范判断。

【缺陷 8】
- 类别: 评估方案缺陷
- 问题: **Clean accuracy 非退化标准（MATH-500 drop ≤ 1%）的统计检验设计不完整。** Proposal 提出 "paired bootstrap test p < 0.05" 来检验 clean accuracy 是否显著下降，但 (a) 未指定 bootstrap 的 resample 次数（标准为 10000+）；(b) 1% 是一个很窄的 margin，在 MATH-500 上（500 道题），1% = 5 道题的差异，统计功效（power）可能不足以检测出真实的微小退化；(c) 未讨论 multiple comparison correction——对 8+ baselines 进行多次 paired test 时需要 Bonferroni 或 FDR 校正。
- 严重度: 可补救
- 补救方案: (1) 指定 bootstrap resample 次数（建议 10000 次）。(2) 报告 clean accuracy 的 95% CI 宽度预估（500 道题、~80% 准确率时，95% CI ≈ ±3.5%），明确 1% 门槛在此 CI 下的可检测性。如果 power 不足，考虑增加 GSM8K 或 Minerva Math 作为补充 clean benchmark 以增大样本量。(3) 对 multiple comparison 使用 Holm-Bonferroni 校正。
- 调研依据: VAR-MATH (arXiv 2507.12885) 使用 bootstrapping 95% CIs 作为标准；ROMA (arXiv 2605.09262) 在 7 个 benchmark 上分别报告 CI。基于统计方法学规范判断。

---

**总结：** 该 proposal 的实验设计整体成熟度较高——dual compute fairness protocol、augmentation-only ablation、entropy gating ablation 等设计体现了对审稿人关切的预判。但存在两个需优先解决的关键缺陷：**(1) CLIPO 作为方法学最近邻必须纳入 baseline**（缺陷 1），(2) **entropy gating static/dynamic 和 perturbation type 分离评估需从 extension 提升为核心实验**（缺陷 3、5）。其余缺陷（2、4、6、7、8）属于补充性改进，不影响 idea 的可执行性但会显著提升审稿说服力。没有发现不可补救的致命缺陷；计算资源（8×H100）、数据可获得性、人工标注规模均在合理范围内。

Sources:
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)
- [CLIPO GitHub Repository](https://github.com/Qwen-Applications/CLIPO)
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation](https://arxiv.org/abs/2605.09262)
- [COPO: Consistency-Aware Policy Optimization](https://arxiv.org/abs/2508.04138)
- [ReasonMaxxer: Rethinking RL for LLM Reasoning](https://arxiv.org/abs/2605.06241)
- [VAR-MATH: Probing True Mathematical Reasoning](https://arxiv.org/abs/2507.12885)
- [MATH-Perturb: Benchmarking LLMs' Math Reasoning (OpenReview)](https://openreview.net/forum?id=M8OLGgYK7e)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [PPCL: Prompt Perturbation Consistency Learning](https://aclanthology.org/2024.findings-eacl.91/)
- [DRA-GRPO: Diverse Reasoning Paths for GRPO](https://arxiv.org/abs/2505.09655)
- [RULES: Reliable Use of Lemmas via Eligibility Reasoning](https://arxiv.org/abs/2602.00998)
- [RLTR: Beyond Correctness: Learning Robust Reasoning via Transfer](https://arxiv.org/abs/2602.08489)
- [Qwen3-8B GRPO Training Report](https://dtianyou.com/en/notes/qwen3-8b-base-training/)
- [GRPO-LEAD: Difficulty-Aware RL for Math Reasoning](https://arxiv.org/html/2504.09696v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35a50780-96a7-4622-adb9-4d98a09d4b70",
  "isSidechain": false,
  "requestId": "req_011CbWY6JjCWykSrfvWuBWzq",
  "type": "assistant",
  "uuid": "ccf3989d-f77e-4245-9e16-bca0b72b5f2f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HyYAqD444P8kNVnoFyF4fS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 28017,
      "output_tokens": 8040,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 747,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 8040,
          "cache_read_input_tokens": 28017,
          "cache_creation_input_tokens": 747,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 747
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
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reasoning models suffer 47–73% accuracy drops under trivial surface-form perturbations (nu…",
  "leafUuid": "ccf3989d-f77e-4245-9e16-bca0b72b5f2f",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Consistency-Regularized RL for Perturbation-Robust Math Reasoning  ## Core Problem  RL-trained mathematical reasoning models suffer 47–73% accuracy drops under trivial surface-form perturbations (nu…",
  "leafUuid": "ccf3989d-f77e-4245-9e16-bca0b72b5f2f",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Consistency-regularized RL for robust math reasoning",
  "sessionId": "f11f911d-ff1c-4027-8486-21befbfcaf17"
}
```

---
