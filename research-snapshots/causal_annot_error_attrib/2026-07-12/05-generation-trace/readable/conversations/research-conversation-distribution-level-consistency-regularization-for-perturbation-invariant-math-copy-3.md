# Research conversation: Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling ## Core Problem 

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/29ae946e-9ea6-4d7b-8932-f18ef42e5983.jsonl`
- **Structured JSON:** [`0e0baf68c8a6b5bb15cc.json`](../../sessions/0e/0e0baf68c8a6b5bb15cc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T06:07:54.827Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T06:07:54.827Z",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "content": "# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling\n\n## Core Problem\n\nRL-trained mathematical reasoning models achieve SOTA on clean benchmarks but suffer 47-73% accuracy drops under trivial surface-form perturbations (numerical substitution, variable renaming) even after RL training, as demonstrated by VAR-MATH (arXiv 2025) on RL-trained models across AMC23 (47.9%), AIME24 (58.8%), and AIME25 (72.9%). GRPO's reward signal provides no gradient against surface-form-dependent reasoning — the policy is rewarded for correct answers regardless of whether it exploits superficial patterns or genuine mathematical structure.\n\n## Research Opportunity and Three-Level Framework\n\nWe identify three levels of consistency enforcement in RL-based math training, each providing progressively stronger invariance guarantees:\n\n1. **Data-level**: Augmenting training with perturbed variants but no explicit consistency signal (MathForge ICLR 2026; PrAg-PO arXiv 2026 using 13 prompt templates as implicit regularization). TA-GRPO's ablation (arXiv 2601.22478) shows this alone is insufficient — \"augmentation without pooling doesn't help.\"\n\n2. **Reward-level**: Pooling rewards across original and perturbed variants to compute advantages (TA-GRPO, arXiv 2601.22478). This provides implicit consistency through shared reward signals but operates on sparse binary feedback (correct/incorrect), constraining only the outcome distribution, not the reasoning process. TA-GRPO demonstrates Pass@k gains (up to +9.84 on AMC12/AIME24) but does not evaluate perturbation robustness on any robustness benchmark (GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP).\n\n3. **Distribution-level** (this work): Explicitly minimizing JS-divergence between policy rollout distributions on original and perturbed problems, providing continuous gradient signal over the entire reasoning trajectory. This constrains not just what answer the model produces but how it reasons — enforcing that semantically equivalent problems induce similar reasoning distributions.\n\nThe diagnostic-benchmark side is saturated (GSM-Symbolic ICLR 2025, VAR-MATH 2025, MATH-Perturb 2025, PutnamGAP 2025, GSM-SEM May 2026) but training-time fixes remain sparse. AbstRaL (ICLR 2026) teaches abstraction before solving (GSM-level only). AIR (arXiv 2605.20994, May 2026) combines anchor-based invariance regularization with GRPO for safety alignment (with auxiliary math evaluation), but uses asymmetric stop-gradient anchoring — appropriate when one prompt variant has verifiable feedback, but inappropriate for math perturbation pairs where both sides are symmetric and equally verifiable. Consistency regularization is independently validated in NLP (F²C recovering 11.6% agreement, Oct 2025) and alignment (BCT reducing attack success from 67.8% to 2.9%, 2025). No prior work applies distribution-level consistency enforcement within RL for mathematical reasoning.\n\n## Research Landscape\n\n**Training-time math robustness**: AbstRaL (ICLR 2026, Apple) uses RL to train abstraction before solving, limited to GSM-level benchmarks. TA-GRPO (arXiv 2601.22478, Jan 2026) introduces transform-augmented reward pooling across semantic-equivalent variants in GRPO, demonstrating Pass@k improvements on competition math but without robustness evaluation. AIR (arXiv 2605.20994, May 2026) applies asymmetric anchor invariance regularization to GRPO primarily for safety, with math as secondary evaluation.\n\n**GRPO variants**: DAPO, DR.GRPO, COPO, DRA-GRPO address stability/diversity/efficiency but none target perturbation invariance. DyJR (arXiv 2603.16157) uses JS-divergence within GRPO as a diversity-preserving mechanism between current and historical policies, establishing JS-divergence as a viable regularizer in GRPO frameworks. PrAg-PO (arXiv 2602.03190, Feb 2026) uses 13 prompt templates during GRPO as implicit regularization with no consistency loss and no perturbation evaluation. MathForge (ICLR 2026) combines difficulty-weighted GRPO with reformulation but evaluates only clean accuracy.\n\n**Adjacent consistency work**: GRPO-CARE (Jun 2026) adds consistency bonuses via reasoning-to-answer likelihood for multimodal video reasoning. CSR (Jan 2026) enforces causal consistency via operator perturbation in SFT, not RL. Reward Under Attack (arXiv 2026) examines robustness of process reward models.\n\n**Key differentiation from TA-GRPO**: TA-GRPO's reward pooling operates on binary outcome signals (correct/incorrect), providing no gradient on the reasoning trajectory when both original and perturbed problems yield the same correctness. Distribution-level JS-divergence provides continuous gradient signal that constrains the full rollout distribution, enforcing invariance even when outcomes agree. Our central hypothesis: reward-level pooling is necessary but insufficient for perturbation invariance; distribution-level enforcement is required.\n\n## Proposed Approach\n\n**ConsistGRPO** augments GRPO with two auxiliary losses:\n\n**(1) Policy-level JS-divergence consistency loss.** For each problem x, generate a math-equivalence-preserving perturbation x'. Collect G rollouts from each: {τ₁,...,τ_G} ~ π_θ(·|x) and {τ'₁,...,τ'_G} ~ π_θ(·|x'). Compute sequence-level log-probabilities log π_θ(τ|x) and log π_θ(τ'|x') to form empirical rollout distributions. The consistency loss is L_consist = JS(P_x || P_x'), where P_x and P_x' are the normalized probability distributions over rollout sequences. This provides symmetric, continuous gradient toward invariance over the full reasoning process, unlike TA-GRPO's reward pooling which only transmits binary outcome signals.\n\n**(2) Contrastive discrimination loss.** Extract representations via mean-pooling the last hidden layer across rollout tokens. Apply a 2-layer MLP projection head (discarded at inference). Positive pairs: representations from (x, x') rollouts. Negative pairs: in-batch representations from different problems. Loss: standard InfoNCE. This targets the representation-level \"blind skill application\" failure identified by MATH-Perturb (arXiv 2025), encouraging the model to encode semantically equivalent problems similarly regardless of surface form.\n\n**Combined objective**: L = L_GRPO + λ₁·L_consist + λ₂·L_contrastive.\n\n**Perturbation generation pipeline**: Adapt GSM-Symbolic/VAR-MATH generators for MATH/AMC/AIME, restricted to algebraic and arithmetic problem subtypes amenable to automated perturbation. For each generated perturbation, apply a SymPy-based validity filter verifying solvability and answer computability. Report perturbation success rates per problem category. For problem types where automated perturbation is unreliable (geometry with diagram-dependent reasoning, certain number theory problems), use LLM-generated perturbations with symbolic verification. This hybrid pipeline addresses the gap between GSM-level template perturbation (GSM-Symbolic, ICLR 2025) and competition-level manual perturbation (PutnamGAP, arXiv 2025, which requires 5 human-crafted variants per problem).\n\n**Training**: Qwen3-8B and Qwen3-1.7B on MATH/AMC/AIME with on-the-fly perturbation generation.\n\n## Experimental Design\n\n**Baselines (7 methods):**\n| Method | Level | Description |\n|--------|-------|-------------|\n| Vanilla GRPO | — | Qwen3-8B, same data, no augmentation |\n| GRPO + Aug Only | Data | Same perturbation data, no consistency/contrastive loss |\n| TA-GRPO (arXiv 2601.22478) | Reward | Transform-augmented reward pooling |\n| AbstRaL (ICLR 2026) | — | Abstraction-based robustness |\n| DR.GRPO | — | GRPO variant for stability |\n| PrAg-PO (arXiv 2026) | Data | 13 prompt templates, implicit regularization |\n| FLOPs-matched GRPO | — | Vanilla GRPO with 2× training steps (same total compute as ConsistGRPO) |\n\n**Evaluation**: GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM (May 2026) for robustness; MATH-500, AIME 2024/2025 for clean accuracy. Report both absolute accuracy and robustness gap (clean − perturbed).\n\n**Ablations (4 dimensions):**\n1. Component decomposition: GRPO → +Aug → +JS consistency → +Contrastive → Full model (5-row table)\n2. Perturbation type: numerical substitution only / variable renaming only / combined\n3. Hyperparameter sensitivity: λ₁, λ₂ weight sweep (5 values each); group size G effect on consistency loss\n4. Training dynamics: learning curves for clean vs. robustness accuracy; entropy trajectory (compare with PrAg-PO's entropy collapse findings)\n\n**Compute-normalized comparison**: FLOPs-matched vanilla GRPO baseline (2× training steps or 2× rollouts per question, matching ConsistGRPO's total compute). Report wall-clock time and total GPU-hours for all methods.\n\n**Scale validation**: Primary experiments on Qwen3-8B; replicate core comparison (ConsistGRPO vs. vanilla GRPO vs. TA-GRPO) on Qwen3-1.7B to verify scale-independent effectiveness.\n\n## Key References\n\n- GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025)\n- AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking (ICLR 2026)\n- MathForge: Difficulty-Aware GRPO and Multi-Aspect Reformulation (ICLR 2026)\n- Prompt Augmentation Scales up GRPO Training on Math Reasoning (arXiv 2026)\n- VAR-MATH: Probing True Mathematical Reasoning via Symbolic Benchmarks (arXiv 2025)\n- MATH-Perturb: Benchmarking LLMs' Math Reasoning against Hard Perturbations (arXiv 2025)\n- PutnamGAP: Robustness of LLMs via Mathematically-Equivalent Transformation (arXiv 2025)\n- Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations (arXiv 2025)\n- Consistency Training Helps Stop Sycophancy and Jailbreaks (arXiv 2025)\n- Reward Under Attack: Robustness and Hackability of Process Reward Models (arXiv 2026)\n- TA-GRPO: Transform-Augmented GRPO Improves Pass@k (arXiv 2601.22478, Jan 2026)\n- AIR: Towards Context-Invariant Safety Alignment for LLMs (arXiv 2605.20994, May 2026)\n- DyJR: Preserving Diversity in RL with Verifiable Rewards via JS-Divergence (arXiv 2603.16157, 2026)"
}
```

---

### Runtime record

_source line 2 · 2026-05-29T06:07:54.833Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T06:07:54.833Z",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

## Round 1

52 recorded events

### User

_source line 3 · 2026-05-29T06:07:54.851Z_

# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling

## Core Problem

RL-trained mathematical reasoning models achieve SOTA on clean benchmarks but suffer 47-73% accuracy drops under trivial surface-form perturbations (numerical substitution, variable renaming) even after RL training, as demonstrated by VAR-MATH (arXiv 2025) on RL-trained models across AMC23 (47.9%), AIME24 (58.8%), and AIME25 (72.9%). GRPO's reward signal provides no gradient against surface-form-dependent reasoning — the policy is rewarded for correct answers regardless of whether it exploits superficial patterns or genuine mathematical structure.

## Research Opportunity and Three-Level Framework

We identify three levels of consistency enforcement in RL-based math training, each providing progressively stronger invariance guarantees:

1. **Data-level**: Augmenting training with perturbed variants but no explicit consistency signal (MathForge ICLR 2026; PrAg-PO arXiv 2026 using 13 prompt templates as implicit regularization). TA-GRPO's ablation (arXiv 2601.22478) shows this alone is insufficient — "augmentation without pooling doesn't help."

2. **Reward-level**: Pooling rewards across original and perturbed variants to compute advantages (TA-GRPO, arXiv 2601.22478). This provides implicit consistency through shared reward signals but operates on sparse binary feedback (correct/incorrect), constraining only the outcome distribution, not the reasoning process. TA-GRPO demonstrates Pass@k gains (up to +9.84 on AMC12/AIME24) but does not evaluate perturbation robustness on any robustness benchmark (GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP).

3. **Distribution-level** (this work): Explicitly minimizing JS-divergence between policy rollout distributions on original and perturbed problems, providing continuous gradient signal over the entire reasoning trajectory. This constrains not just what answer the model produces but how it reasons — enforcing that semantically equivalent problems induce similar reasoning distributions.

The diagnostic-benchmark side is saturated (GSM-Symbolic ICLR 2025, VAR-MATH 2025, MATH-Perturb 2025, PutnamGAP 2025, GSM-SEM May 2026) but training-time fixes remain sparse. AbstRaL (ICLR 2026) teaches abstraction before solving (GSM-level only). AIR (arXiv 2605.20994, May 2026) combines anchor-based invariance regularization with GRPO for safety alignment (with auxiliary math evaluation), but uses asymmetric stop-gradient anchoring — appropriate when one prompt variant has verifiable feedback, but inappropriate for math perturbation pairs where both sides are symmetric and equally verifiable. Consistency regularization is independently validated in NLP (F²C recovering 11.6% agreement, Oct 2025) and alignment (BCT reducing attack success from 67.8% to 2.9%, 2025). No prior work applies distribution-level consistency enforcement within RL for mathematical reasoning.

## Research Landscape

**Training-time math robustness**: AbstRaL (ICLR 2026, Apple) uses RL to train abstraction before solving, limited to GSM-level benchmarks. TA-GRPO (arXiv 2601.22478, Jan 2026) introduces transform-augmented reward pooling across semantic-equivalent variants in GRPO, demonstrating Pass@k improvements on competition math but without robustness evaluation. AIR (arXiv 2605.20994, May 2026) applies asymmetric anchor invariance regularization to GRPO primarily for safety, with math as secondary evaluation.

**GRPO variants**: DAPO, DR.GRPO, COPO, DRA-GRPO address stability/diversity/efficiency but none target perturbation invariance. DyJR (arXiv 2603.16157) uses JS-divergence within GRPO as a diversity-preserving mechanism between current and historical policies, establishing JS-divergence as a viable regularizer in GRPO frameworks. PrAg-PO (arXiv 2602.03190, Feb 2026) uses 13 prompt templates during GRPO as implicit regularization with no consistency loss and no perturbation evaluation. MathForge (ICLR 2026) combines difficulty-weighted GRPO with reformulation but evaluates only clean accuracy.

**Adjacent consistency work**: GRPO-CARE (Jun 2026) adds consistency bonuses via reasoning-to-answer likelihood for multimodal video reasoning. CSR (Jan 2026) enforces causal consistency via operator perturbation in SFT, not RL. Reward Under Attack (arXiv 2026) examines robustness of process reward models.

**Key differentiation from TA-GRPO**: TA-GRPO's reward pooling operates on binary outcome signals (correct/incorrect), providing no gradient on the reasoning trajectory when both original and perturbed problems yield the same correctness. Distribution-level JS-divergence provides continuous gradient signal that constrains the full rollout distribution, enforcing invariance even when outcomes agree. Our central hypothesis: reward-level pooling is necessary but insufficient for perturbation invariance; distribution-level enforcement is required.

## Proposed Approach

**ConsistGRPO** augments GRPO with two auxiliary losses:

**(1) Policy-level JS-divergence consistency loss.** For each problem x, generate a math-equivalence-preserving perturbation x'. Collect G rollouts from each: {τ₁,...,τ_G} ~ π_θ(·|x) and {τ'₁,...,τ'_G} ~ π_θ(·|x'). Compute sequence-level log-probabilities log π_θ(τ|x) and log π_θ(τ'|x') to form empirical rollout distributions. The consistency loss is L_consist = JS(P_x || P_x'), where P_x and P_x' are the normalized probability distributions over rollout sequences. This provides symmetric, continuous gradient toward invariance over the full reasoning process, unlike TA-GRPO's reward pooling which only transmits binary outcome signals.

**(2) Contrastive discrimination loss.** Extract representations via mean-pooling the last hidden layer across rollout tokens. Apply a 2-layer MLP projection head (discarded at inference). Positive pairs: representations from (x, x') rollouts. Negative pairs: in-batch representations from different problems. Loss: standard InfoNCE. This targets the representation-level "blind skill application" failure identified by MATH-Perturb (arXiv 2025), encouraging the model to encode semantically equivalent problems similarly regardless of surface form.

**Combined objective**: L = L_GRPO + λ₁·L_consist + λ₂·L_contrastive.

**Perturbation generation pipeline**: Adapt GSM-Symbolic/VAR-MATH generators for MATH/AMC/AIME, restricted to algebraic and arithmetic problem subtypes amenable to automated perturbation. For each generated perturbation, apply a SymPy-based validity filter verifying solvability and answer computability. Report perturbation success rates per problem category. For problem types where automated perturbation is unreliable (geometry with diagram-dependent reasoning, certain number theory problems), use LLM-generated perturbations with symbolic verification. This hybrid pipeline addresses the gap between GSM-level template perturbation (GSM-Symbolic, ICLR 2025) and competition-level manual perturbation (PutnamGAP, arXiv 2025, which requires 5 human-crafted variants per problem).

**Training**: Qwen3-8B and Qwen3-1.7B on MATH/AMC/AIME with on-the-fly perturbation generation.

## Experimental Design

**Baselines (7 methods):**
| Method | Level | Description |
|--------|-------|-------------|
| Vanilla GRPO | — | Qwen3-8B, same data, no augmentation |
| GRPO + Aug Only | Data | Same perturbation data, no consistency/contrastive loss |
| TA-GRPO (arXiv 2601.22478) | Reward | Transform-augmented reward pooling |
| AbstRaL (ICLR 2026) | — | Abstraction-based robustness |
| DR.GRPO | — | GRPO variant for stability |
| PrAg-PO (arXiv 2026) | Data | 13 prompt templates, implicit regularization |
| FLOPs-matched GRPO | — | Vanilla GRPO with 2× training steps (same total compute as ConsistGRPO) |

**Evaluation**: GSM-Symbolic, VAR-MATH, MATH-Perturb, PutnamGAP, GSM-SEM (May 2026) for robustness; MATH-500, AIME 2024/2025 for clean accuracy. Report both absolute accuracy and robustness gap (clean − perturbed).

**Ablations (4 dimensions):**
1. Component decomposition: GRPO → +Aug → +JS consistency → +Contrastive → Full model (5-row table)
2. Perturbation type: numerical substitution only / variable renaming only / combined
3. Hyperparameter sensitivity: λ₁, λ₂ weight sweep (5 values each); group size G effect on consistency loss
4. Training dynamics: learning curves for clean vs. robustness accuracy; entropy trajectory (compare with PrAg-PO's entropy collapse findings)

**Compute-normalized comparison**: FLOPs-matched vanilla GRPO baseline (2× training steps or 2× rollouts per question, matching ConsistGRPO's total compute). Report wall-clock time and total GPU-hours for all methods.

**Scale validation**: Primary experiments on Qwen3-8B; replicate core comparison (ConsistGRPO vs. vanilla GRPO vs. TA-GRPO) on Qwen3-1.7B to verify scale-independent effectiveness.

## Key References

- GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs (ICLR 2025)
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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "63d6a2c3-4be8-421d-83f7-f24ffc29c4c8",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T06:07:54.849Z_

```json
{
  "parentUuid": "63d6a2c3-4be8-421d-83f7-f24ffc29c4c8",
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
  "uuid": "c3ef5db7-7fe0-435c-a686-85f90da1e5a5",
  "timestamp": "2026-05-29T06:07:54.849Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T06:07:54.849Z_

```json
{
  "parentUuid": "c3ef5db7-7fe0-435c-a686-85f90da1e5a5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3a514000-db09-45c0-b9fd-90abc38c86d6",
  "timestamp": "2026-05-29T06:07:54.849Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
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
  "aiTitle": "Distribution-level consistency regularization for math RL",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Assistant

_source line 7 · 2026-05-29T06:08:05.635Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "补救 agent" (remedy agent) to review this research proposal for AAAI 2026 submission. My job is to focus exclusively on experimental design and technical execution completeness — baselines, experimental plan, evaluation metrics, ablation design, and feasibility.

Let me first read the proposal carefully, then do WebSearch to understand the current experimental standards in this area before giving my assessment.

The proposal is about "ConsistGRPO" — adding distribution-level consistency regularization (JS-divergence + contrastive loss) to GRPO for making math reasoning models robust to surface-form perturbations.


I need to search for recent work on math reasoning robustness, the specific baselines they mention like TA-GRPO and AIR, and what the current state-of-the-art evaluation practices look like in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a514000-db09-45c0-b9fd-90abc38c86d6",
  "isSidechain": false,
  "requestId": "req_011CbWMpuf3jbcEPkjtaJ2KZ",
  "type": "assistant",
  "uuid": "257d717d-5038-4705-a6ef-5ed093d74724",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188He3m5enndkTjqZ9Ta9xK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 14080,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4242
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

_source line 8 · 2026-05-29T06:08:06.212Z_

I'll start by doing thorough pre-research on the experimental standards in this area before making any assessments. Let me search for the key related works and their experimental designs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "257d717d-5038-4705-a6ef-5ed093d74724",
  "isSidechain": false,
  "requestId": "req_011CbWMpuf3jbcEPkjtaJ2KZ",
  "type": "assistant",
  "uuid": "24b7fa9d-c4ab-4809-8bc3-dc4e55ef88b3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188He3m5enndkTjqZ9Ta9xK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 14080,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4242
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

_source line 9 · 2026-05-29T06:08:06.787Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017dnodDjpA5k1Ha6NAAh2NW`</summary>

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
  "parentUuid": "24b7fa9d-c4ab-4809-8bc3-dc4e55ef88b3",
  "isSidechain": false,
  "requestId": "req_011CbWMpuf3jbcEPkjtaJ2KZ",
  "type": "assistant",
  "uuid": "914a7798-c80a-4690-8db6-1f28e63b028a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188He3m5enndkTjqZ9Ta9xK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4242,
      "cache_read_input_tokens": 14080,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 344,
          "cache_read_input_tokens": 14080,
          "cache_creation_input_tokens": 4242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4242
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

_source line 10 · 2026-05-29T06:08:06.795Z_

<details><summary>↩ Tool result · `toolu_017dnodDjpA5k1Ha6NAAh2NW`</summary>

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
  "parentUuid": "914a7798-c80a-4690-8db6-1f28e63b028a",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "2e9b06d5-3570-4272-9150-12bee76411f7",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "914a7798-c80a-4690-8db6-1f28e63b028a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-29T06:08:14.345Z_

Now let me conduct my pre-research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e9b06d5-3570-4272-9150-12bee76411f7",
  "isSidechain": false,
  "requestId": "req_011CbWMqnro2oXwecyiY5iBV",
  "type": "assistant",
  "uuid": "b6b40878-9fd0-4c49-8638-1d77beec6754",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfkWmfhukRMXaFCWSemtpU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 18322,
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
          "cache_read_input_tokens": 18322,
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

_source line 12 · 2026-05-29T06:08:14.614Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NU3vAh3o2okx1k5wFitb61`</summary>

```json
{
  "query": "TA-GRPO transform augmented GRPO arXiv 2601.22478 experimental design baselines evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6b40878-9fd0-4c49-8638-1d77beec6754",
  "isSidechain": false,
  "requestId": "req_011CbWMqnro2oXwecyiY5iBV",
  "type": "assistant",
  "uuid": "65738043-dbf5-4f12-a01b-288a414a2bde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfkWmfhukRMXaFCWSemtpU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 872,
      "cache_read_input_tokens": 18322,
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
          "cache_read_input_tokens": 18322,
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

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling  ## Core Problem  RL-trained mathematical reasoning models achieve SOTA on clean benchmarks bu…",
  "leafUuid": "65738043-dbf5-4f12-a01b-288a414a2bde",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency regularization for math RL",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Tool result

_source line 15 · 2026-05-29T06:08:23.088Z_

<details><summary>↩ Tool result · `toolu_01NU3vAh3o2okx1k5wFitb61`</summary>

```text
Web search results for query: "TA-GRPO transform augmented GRPO arXiv 2601.22478 experimental design baselines evaluation"

Links: [{"title":"[2601.22478] Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/abs/2601.22478"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/html/2601.22478"},{"title":"(PDF) Transform-Augmented GRPO Improves Pass@k","url":"https://www.researchgate.net/publication/400340183_Transform-Augmented_GRPO_Improves_Passk"},{"title":"Transform-Augmented GRPO Improves Pass@k","url":"https://arxiv.org/pdf/2601.22478"},{"title":"[2603.12648] From Sparse to Dense: Multi-View GRPO for Flow Models via Augmented Condition Space","url":"https://arxiv.org/abs/2603.12648"},{"title":"[2601.03661] AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/abs/2601.03661"}]

Based on the search results, I found comprehensive information about the TA-GRPO paper:

## Overview

TA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question via paraphrasing, variable renaming, and format changes, and computes advantages by pooling rewards across the entire group.

## Problem Statement

Large language models trained via next-token prediction are fundamentally pattern-matchers: sensitive to superficial phrasing variations even when the underlying problem is identical. Group Relative Policy Optimization (GRPO) was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.

## Approach

The pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies.

## Theoretical Justification

The paper provides theoretical justification showing that TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.

## Experimental Results

Experiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond). TA-GRPO consistently reduces zero-gradient questions compared to GRPO, maintaining a 12–16 percentage point advantage throughout training (e.g., 75% vs 86% at convergence).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "65738043-dbf5-4f12-a01b-288a414a2bde",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "fe7400f3-5ec2-4a32-a360-abc25d10fba9",
  "toolUseResult": {
    "query": "TA-GRPO transform augmented GRPO arXiv 2601.22478 experimental design baselines evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_018v1qJag5aYiMNTRLfvHx36",
        "content": [
          {
            "title": "[2601.22478] Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/abs/2601.22478"
          },
          {
            "title": "Transform-Augmented GRPO Improves Pass@k",
            "url": "https://arxiv.org/html/2601.22478"
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
            "title": "[2603.12648] From Sparse to Dense: Multi-View GRPO for Flow Models via Augmented Condition Space",
            "url": "https://arxiv.org/abs/2603.12648"
          },
          {
            "title": "[2601.03661] AMIR-GRPO: Inducing Implicit Preference Signals into GRPO",
            "url": "https://arxiv.org/abs/2601.03661"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the TA-GRPO paper:\n\n## Overview\n\nTA-GRPO (Transform-Augmented GRPO) generates semantically equivalent transformed variants of each question via paraphrasing, variable renaming, and format changes, and computes advantages by pooling rewards across the entire group.\n\n## Problem Statement\n\nLarge language models trained via next-token prediction are fundamentally pattern-matchers: sensitive to superficial phrasing variations even when the underlying problem is identical. Group Relative Policy Optimization (GRPO) was designed to improve reasoning, but in fact it worsens this situation through two failure modes: diversity collapse, where training amplifies a single solution strategy while ignoring alternatives of gradient signal, and gradient diminishing, where a large portion of questions yield zero gradients because all rollouts receive identical rewards.\n\n## Approach\n\nThe pooled computation ensures mixed rewards even when the original question is too easy or too hard, while training on diverse phrasings promotes multiple solution strategies.\n\n## Theoretical Justification\n\nThe paper provides theoretical justification showing that TA-GRPO reduces zero-gradient probability and improves generalization via reduced train-test distribution shift.\n\n## Experimental Results\n\nExperiments on mathematical reasoning benchmarks show consistent Pass@k improvements, with gains up to 9.84 points on competition math (AMC12, AIME24) and 5.05 points on out-of-distribution scientific reasoning (GPQA-Diamond). TA-GRPO consistently reduces zero-gradient questions compared to GRPO, maintaining a 12–16 percentage point advantage throughout training (e.g., 75% vs 86% at convergence)."
    ],
    "durationSeconds": 8.464292627999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "65738043-dbf5-4f12-a01b-288a414a2bde",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-29T06:08:30.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AiuBEsdvX3S5a8JqBbav28`</summary>

```json
{
  "query": "AIR anchor invariance regularization GRPO arXiv 2605.20994 math robustness experimental setup"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe7400f3-5ec2-4a32-a360-abc25d10fba9",
  "isSidechain": false,
  "requestId": "req_011CbWMsEjpE9ST46irjQMvY",
  "type": "assistant",
  "uuid": "63a65802-50cb-4b67-b7b9-a6aec6d3b336",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WLy9N3CAAKJHZNbWe3Jwoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 19194,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 19194,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
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

_source line 17 · 2026-05-29T06:08:41.229Z_

<details><summary>↩ Tool result · `toolu_01AiuBEsdvX3S5a8JqBbav28`</summary>

```text
Web search results for query: "AIR anchor invariance regularization GRPO arXiv 2605.20994 math robustness experimental setup"

Links: [{"title":"[2605.20994] Towards Context-Invariant Safety Alignment for Large Language Models","url":"https://arxiv.org/abs/2605.20994"},{"title":"Towards Context-Invariant Safety Alignment for Large Language Models","url":"https://arxiv.org/html/2605.20994"},{"title":"AMIR-GRPO: Inducing Implicit Preference Signals into GRPO","url":"https://arxiv.org/pdf/2601.03661"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients","url":"https://arxiv.org/pdf/2601.23135"},{"title":"Rethinking Invariance Regularization in Adversarial Training to Improve Robustness-Accuracy Trade-off","url":"https://arxiv.org/pdf/2402.14648"},{"title":"DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward Reinforcement Learning","url":"https://arxiv.org/html/2605.25604"}]

Based on the search results, I found the paper you're looking for. Here's information about AIR (Anchor Invariance Regularization) from arXiv paper 2605.20994:

## Overview
Anchor Invariance Regularization (AIR) treats verifiable prompts as anchors and uses a stop-gradient target to regularize only the open-ended variants toward the anchor performance, implemented as a plug-in auxiliary loss and combined with group-based preference optimization (e.g., GRPO) via heterogeneous prompt grouping.

## Problem It Addresses
Robust safety requires context-invariant alignment, where behavior depends on the underlying intent rather than surface form, though enforcing invariance is difficult because not all training signals are equally trustworthy; some prompt variants can obtain verifiable feedback (e.g., multiple-choice), while open-ended variants typically rely on noisy, gameable reward proxies.

## Key Innovation
AIR breaks the symmetry of standard invariance objectives by designating verifiable contexts as anchors, regularizing open-ended generation to match the anchor reference via a stop-gradient target, ensuring the reliable anchor remains fixed.

## Experimental Results
Across Safety, Moral Reasoning, and Math, AIR improves context invariance, boosting in-distribution group accuracy by 12.71% and out-of-distribution consistency by 33.49%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63a65802-50cb-4b67-b7b9-a6aec6d3b336",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "18af8051-5d8d-47d0-a881-792a30bd0918",
  "toolUseResult": {
    "query": "AIR anchor invariance regularization GRPO arXiv 2605.20994 math robustness experimental setup",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UxHmEFnqNnKZ7BAfhdPVm9",
        "content": [
          {
            "title": "[2605.20994] Towards Context-Invariant Safety Alignment for Large Language Models",
            "url": "https://arxiv.org/abs/2605.20994"
          },
          {
            "title": "Towards Context-Invariant Safety Alignment for Large Language Models",
            "url": "https://arxiv.org/html/2605.20994"
          },
          {
            "title": "AMIR-GRPO: Inducing Implicit Preference Signals into GRPO",
            "url": "https://arxiv.org/pdf/2601.03661"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/pdf/2503.06639"
          },
          {
            "title": "Why GRPO Needs Normalization: A Local-Curvature Perspective on Adaptive Gradients",
            "url": "https://arxiv.org/pdf/2601.23135"
          },
          {
            "title": "Rethinking Invariance Regularization in Adversarial Training to Improve Robustness-Accuracy Trade-off",
            "url": "https://arxiv.org/pdf/2402.14648"
          },
          {
            "title": "DVAO: Dynamic Variance-adaptive Advantage Optimization for Multi-reward Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.25604"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's information about AIR (Anchor Invariance Regularization) from arXiv paper 2605.20994:\n\n## Overview\nAnchor Invariance Regularization (AIR) treats verifiable prompts as anchors and uses a stop-gradient target to regularize only the open-ended variants toward the anchor performance, implemented as a plug-in auxiliary loss and combined with group-based preference optimization (e.g., GRPO) via heterogeneous prompt grouping.\n\n## Problem It Addresses\nRobust safety requires context-invariant alignment, where behavior depends on the underlying intent rather than surface form, though enforcing invariance is difficult because not all training signals are equally trustworthy; some prompt variants can obtain verifiable feedback (e.g., multiple-choice), while open-ended variants typically rely on noisy, gameable reward proxies.\n\n## Key Innovation\nAIR breaks the symmetry of standard invariance objectives by designating verifiable contexts as anchors, regularizing open-ended generation to match the anchor reference via a stop-gradient target, ensuring the reliable anchor remains fixed.\n\n## Experimental Results\nAcross Safety, Moral Reasoning, and Math, AIR improves context invariance, boosting in-distribution group accuracy by 12.71% and out-of-distribution consistency by 33.49%."
    ],
    "durationSeconds": 11.085734121000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "63a65802-50cb-4b67-b7b9-a6aec6d3b336",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-29T06:08:45.741Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RQuDD6CzWdWBCFCsTpNZrV`</summary>

```json
{
  "query": "GSM-Symbolic VAR-MATH MATH-Perturb robustness evaluation benchmarks LLM math reasoning 2025 2026 experimental methodology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18af8051-5d8d-47d0-a881-792a30bd0918",
  "isSidechain": false,
  "requestId": "req_011CbWMtKrRJPq8pvM7k5gVJ",
  "type": "assistant",
  "uuid": "80f0597d-f9df-4b08-9257-f55ab13056ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DnZJvRtWh2hPmV6nP3BctB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 760,
      "cache_read_input_tokens": 20004,
      "output_tokens": 88,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 760,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 88,
          "cache_read_input_tokens": 20004,
          "cache_creation_input_tokens": 760,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 760
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

_source line 19 · 2026-05-29T06:08:54.250Z_

<details><summary>↩ Tool result · `toolu_01RQuDD6CzWdWBCFCsTpNZrV`</summary>

```text
Web search results for query: "GSM-Symbolic VAR-MATH MATH-Perturb robustness evaluation benchmarks LLM math reasoning 2025 2026 experimental methodology"

Links: [{"title":"GSM-Symbolic: A Rigorous LLM Math Benchmark","url":"https://www.emergentmind.com/topics/gsm-symbolic-benchmark"},{"title":"Published as a conference paper at ICLR 2025 GSM-SYMBOLIC: UNDERSTANDING","url":"https://arxiv.org/pdf/2410.05229"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2402.19255"},{"title":"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=AjXkRZIvjB"},{"title":"VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks","url":"https://arxiv.org/pdf/2507.12885"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/html/2402.19255v1"}]

I found comprehensive information about these robustness evaluation benchmarks for LLM mathematical reasoning. Here's what the search reveals:

## GSM-Symbolic

GSM-Symbolic is an improved benchmark created from symbolic templates that allow for the generation of diverse questions and enables more controllable evaluations, providing key insights and more reliable metrics for measuring reasoning capabilities of models. The benchmark's metrics explicitly quantify (1) sensitivity to numeric or lexical perturbations, (2) fragility under increased surface complexity, and (3) model susceptibility to distractor content.

LLMs exhibit more robustness to changes in superficial elements like proper names but are very sensitive to changes in numerical values. Additionally, by adding seemingly relevant but ultimately irrelevant information to problems, substantial performance drops (up to 65%) are demonstrated across all state-of-the-art models.

## VAR-MATH

VAR-MATH's design enforces consistency across structurally equivalent variants, mitigates contamination, and enhances robustness through bootstrapped metrics, and has been applied to transform three popular benchmarks—AMC23, AIME24, and AIME25—into their symbolic counterparts. Experimental results show substantial performance drops for RL-trained models on these variabilized benchmarks, with average declines of 47.9% on AMC23, 58.8% on AIME24, and 72.9% on AIME25.

## GSM-Plus

GSM-Plus is an extension of GSM8K augmented with various mathematical perturbations, with experiments on 25 LLMs and 4 prompting techniques showing that while LLMs exhibit different levels of math reasoning abilities, their performances are far from robust.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80f0597d-f9df-4b08-9257-f55ab13056ae",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "4af7304c-6c75-4fcd-b4db-b42f20396cbf",
  "toolUseResult": {
    "query": "GSM-Symbolic VAR-MATH MATH-Perturb robustness evaluation benchmarks LLM math reasoning 2025 2026 experimental methodology",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KF1bg9REvUzHPrUjSPnB9U",
        "content": [
          {
            "title": "GSM-Symbolic: A Rigorous LLM Math Benchmark",
            "url": "https://www.emergentmind.com/topics/gsm-symbolic-benchmark"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 GSM-SYMBOLIC: UNDERSTANDING",
            "url": "https://arxiv.org/pdf/2410.05229"
          },
          {
            "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers",
            "url": "https://arxiv.org/pdf/2402.19255"
          },
          {
            "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=AjXkRZIvjB"
          },
          {
            "title": "VAR-MATH: Probing True Mathematical Reasoning in LLMS via Symbolic Multi-Instance Benchmarks",
            "url": "https://arxiv.org/pdf/2507.12885"
          },
          {
            "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers",
            "url": "https://arxiv.org/html/2402.19255v1"
          }
        ]
      },
      "I found comprehensive information about these robustness evaluation benchmarks for LLM mathematical reasoning. Here's what the search reveals:\n\n## GSM-Symbolic\n\nGSM-Symbolic is an improved benchmark created from symbolic templates that allow for the generation of diverse questions and enables more controllable evaluations, providing key insights and more reliable metrics for measuring reasoning capabilities of models. The benchmark's metrics explicitly quantify (1) sensitivity to numeric or lexical perturbations, (2) fragility under increased surface complexity, and (3) model susceptibility to distractor content.\n\nLLMs exhibit more robustness to changes in superficial elements like proper names but are very sensitive to changes in numerical values. Additionally, by adding seemingly relevant but ultimately irrelevant information to problems, substantial performance drops (up to 65%) are demonstrated across all state-of-the-art models.\n\n## VAR-MATH\n\nVAR-MATH's design enforces consistency across structurally equivalent variants, mitigates contamination, and enhances robustness through bootstrapped metrics, and has been applied to transform three popular benchmarks—AMC23, AIME24, and AIME25—into their symbolic counterparts. Experimental results show substantial performance drops for RL-trained models on these variabilized benchmarks, with average declines of 47.9% on AMC23, 58.8% on AIME24, and 72.9% on AIME25.\n\n## GSM-Plus\n\nGSM-Plus is an extension of GSM8K augmented with various mathematical perturbations, with experiments on 25 LLMs and 4 prompting techniques showing that while LLMs exhibit different levels of math reasoning abilities, their performances are far from robust."
    ],
    "durationSeconds": 8.504685462999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "80f0597d-f9df-4b08-9257-f55ab13056ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-29T06:08:58.549Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RE9PWc4e5S1QdyUiTpBzLd`</summary>

```json
{
  "query": "GRPO mathematical reasoning consistency regularization JS divergence KL divergence ablation study 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4af7304c-6c75-4fcd-b4db-b42f20396cbf",
  "isSidechain": false,
  "requestId": "req_011CbWMuHfEcQwsqqXhcLZsf",
  "type": "assistant",
  "uuid": "ada08801-9e60-4c63-a25a-93228458d022",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ShbhExFB22FX4wAsFAgYqt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 20764,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 20764,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 21 · 2026-05-29T06:09:06.871Z_

<details><summary>↩ Tool result · `toolu_01RE9PWc4e5S1QdyUiTpBzLd`</summary>

```text
Web search results for query: "GRPO mathematical reasoning consistency regularization JS divergence KL divergence ablation study 2025 2026"

Links: [{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models","url":"https://arxiv.org/html/2504.09696v1"},{"title":"Token-Level Policy Optimization: Linking Group-Level Rewards to Token-Level Aggregation via Sequence-Level Likelihood","url":"https://arxiv.org/html/2604.12736"},{"title":"Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification","url":"https://arxiv.org/pdf/2503.06639"},{"title":"Beyond KL Divergence: Policy Optimization with Flexible Bregman Divergences for LLM Reasoning","url":"https://arxiv.org/pdf/2602.04380"},{"title":"Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS","url":"https://www.arxiv.org/pdf/2512.21852"},{"title":"A Unified Framework for Rethinking Policy Divergence Measures in GRPO","url":"https://arxiv.org/pdf/2602.05494"},{"title":"Geometric-Mean Policy Optimization","url":"https://arxiv.org/pdf/2507.20673"},{"title":"GTPO: Trajectory-Based Policy Optimization in Large Language Models","url":"https://arxiv.org/html/2508.03772v3"},{"title":"GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models","url":"https://arxiv.org/pdf/2504.09696"}]

I found several relevant research papers on GRPO and related policy optimization methods for mathematical reasoning. Here are the key findings:

## GRPO Overview

GRPO (Group Relative Policy Optimization) is a recently proposed algorithm designed for fine-tuning language models with group-level normalization of rewards, which modifies the standard policy gradient objective by introducing a relative advantage within sets of responses corresponding to the same question, stabilizing updates and promoting consistent learning signals.

## KL Divergence and Regularization Studies

Despite extensive exploration of reward processing strategies and training dynamics, all existing group-based methods exclusively use KL divergence for policy regularization, leaving the choice of divergence function unexplored. However, recent research has begun addressing this gap:

- Group-Based Mirror Policy Optimization (GBMPO) extends group-based policy optimization to flexible Bregman divergences, with ProbL2-GRPO achieving 86.7% accuracy on GSM8K mathematical reasoning, improving +5.5 points over the Dr. GRPO baseline.

- The KL3 estimator serves as the pivotal policy divergence constraint, and it is mathematically equivalent to an asymmetric ratio-based clipping.

## Ablation Studies and Mathematical Reasoning

Panel analyses demonstrate the fragility of undifferentiated KL-Divergence and its performance degradation effect, while entropy regularization yields marginal improvements, and KL-Divergence control validates optimal token-level KL-Divergence management.

Empirical evaluations and comprehensive ablation studies confirm that GRPO-LEAD effectively addresses previous GRPO shortcomings, leading to more concise, accurate, and efficiently trainable models capable of robust performance across mathematical reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ada08801-9e60-4c63-a25a-93228458d022",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "4fdad8f0-b6dc-4539-b52d-692d8475f6fd",
  "toolUseResult": {
    "query": "GRPO mathematical reasoning consistency regularization JS divergence KL divergence ablation study 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ENFq2tcr35QEAbMjy1nSSJ",
        "content": [
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models",
            "url": "https://arxiv.org/html/2504.09696v1"
          },
          {
            "title": "Token-Level Policy Optimization: Linking Group-Level Rewards to Token-Level Aggregation via Sequence-Level Likelihood",
            "url": "https://arxiv.org/html/2604.12736"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards: GRPO's Effective Loss, Dynamics, and Success Amplification",
            "url": "https://arxiv.org/pdf/2503.06639"
          },
          {
            "title": "Beyond KL Divergence: Policy Optimization with Flexible Bregman Divergences for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.04380"
          },
          {
            "title": "Preprint. A COMEDY OF ESTIMATORS: ON KL REGULARIZATION IN RL TRAINING OF LLMS",
            "url": "https://www.arxiv.org/pdf/2512.21852"
          },
          {
            "title": "A Unified Framework for Rethinking Policy Divergence Measures in GRPO",
            "url": "https://arxiv.org/pdf/2602.05494"
          },
          {
            "title": "Geometric-Mean Policy Optimization",
            "url": "https://arxiv.org/pdf/2507.20673"
          },
          {
            "title": "GTPO: Trajectory-Based Policy Optimization in Large Language Models",
            "url": "https://arxiv.org/html/2508.03772v3"
          },
          {
            "title": "GRPO-LEAD: A Difficulty-Aware Reinforcement Learning Approach for Concise Mathematical Reasoning in Language Models",
            "url": "https://arxiv.org/pdf/2504.09696"
          }
        ]
      },
      "I found several relevant research papers on GRPO and related policy optimization methods for mathematical reasoning. Here are the key findings:\n\n## GRPO Overview\n\nGRPO (Group Relative Policy Optimization) is a recently proposed algorithm designed for fine-tuning language models with group-level normalization of rewards, which modifies the standard policy gradient objective by introducing a relative advantage within sets of responses corresponding to the same question, stabilizing updates and promoting consistent learning signals.\n\n## KL Divergence and Regularization Studies\n\nDespite extensive exploration of reward processing strategies and training dynamics, all existing group-based methods exclusively use KL divergence for policy regularization, leaving the choice of divergence function unexplored. However, recent research has begun addressing this gap:\n\n- Group-Based Mirror Policy Optimization (GBMPO) extends group-based policy optimization to flexible Bregman divergences, with ProbL2-GRPO achieving 86.7% accuracy on GSM8K mathematical reasoning, improving +5.5 points over the Dr. GRPO baseline.\n\n- The KL3 estimator serves as the pivotal policy divergence constraint, and it is mathematically equivalent to an asymmetric ratio-based clipping.\n\n## Ablation Studies and Mathematical Reasoning\n\nPanel analyses demonstrate the fragility of undifferentiated KL-Divergence and its performance degradation effect, while entropy regularization yields marginal improvements, and KL-Divergence control validates optimal token-level KL-Divergence management.\n\nEmpirical evaluations and comprehensive ablation studies confirm that GRPO-LEAD effectively addresses previous GRPO shortcomings, leading to more concise, accurate, and efficiently trainable models capable of robust performance across mathematical reasoning tasks."
    ],
    "durationSeconds": 8.317081627,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ada08801-9e60-4c63-a25a-93228458d022",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-29T06:09:10.174Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G22sd2TDcJxwUZzps6TQAg`</summary>

```json
{
  "query": "contrastive learning representation consistency math reasoning LLM robustness InfoNCE 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4fdad8f0-b6dc-4539-b52d-692d8475f6fd",
  "isSidechain": false,
  "requestId": "req_011CbWMvDbCPL4d7QmTvY3TQ",
  "type": "assistant",
  "uuid": "88c50e0e-7550-451a-a485-1f8d33494591",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NafwN9ESZV8DB1hY1mZoh5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 929,
      "cache_read_input_tokens": 21604,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 929,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 21604,
          "cache_creation_input_tokens": 929,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 929
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

_source line 23 · 2026-05-29T06:09:17.399Z_

<details><summary>↩ Tool result · `toolu_01G22sd2TDcJxwUZzps6TQAg`</summary>

```text
Web search results for query: "contrastive learning representation consistency math reasoning LLM robustness InfoNCE 2025 2026"

Links: [{"title":"InfoNCE: Contrastive Loss for Representation Learning","url":"https://www.emergentmind.com/topics/infonce"},{"title":"InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning","url":"https://arxiv.org/html/2505.06282v1"},{"title":"Contrastive Learning with Consistent Representations","url":"https://arxiv.org/pdf/2302.01541"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/pdf/2603.10101"},{"title":"Robust Contrastive Learning against Noisy Views","url":"https://arxiv.org/pdf/2201.04309"},{"title":"ReNCE: Learning to Reason by Noise Contrastive Estimation","url":"https://arxiv.org/pdf/2601.22432"}]

I've found several relevant results on contrastive learning, representation consistency, and related topics. Here's what the search revealed:

## Key Findings:

**InfoNCE and Robustness:**
Recent research shows that classical InfoNCE loss lacks robustness to label noise, but Symmetric InfoNCE (SymNCE) adds a reverse term to ensure robustness. This framework unifies prior heuristics like nearest neighbor sample selection (Cui et al., January 2025).

**Representation Consistency:**
A method called Contrastive Learning with Consistent Representations (CoCor) proposes a novel "DA consistency" metric that governs how augmented data maps to representation space, ensuring instances are positioned optimally consistent with data augmentation intensity.

**LLM Reasoning:**
Recent work on "ReNCE: Learning to Reason by Noise Contrastive Estimation" demonstrates competitive performance on challenging math benchmarks against strong baselines like DAPO and online DPO (as of February 2026).

**Contrastive Learning Against Noise:**
A robust contrastive learning approach provides a drop-in replacement for InfoNCE loss and shows consistent improvements on image, video, and graph contrastive learning benchmarks with real-world noise patterns.

The search results show active research in these areas through 2025-2026, particularly at major venues like SIGIR 2025 and ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88c50e0e-7550-451a-a485-1f8d33494591",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "10143b86-7b03-4a5c-a013-f942f9b2e9f7",
  "toolUseResult": {
    "query": "contrastive learning representation consistency math reasoning LLM robustness InfoNCE 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014tCDmpvKc54kACTB3mzVrW",
        "content": [
          {
            "title": "InfoNCE: Contrastive Loss for Representation Learning",
            "url": "https://www.emergentmind.com/topics/infonce"
          },
          {
            "title": "InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning",
            "url": "https://arxiv.org/html/2505.06282v1"
          },
          {
            "title": "Contrastive Learning with Consistent Representations",
            "url": "https://arxiv.org/pdf/2302.01541"
          },
          {
            "title": "CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/pdf/2603.10101"
          },
          {
            "title": "Robust Contrastive Learning against Noisy Views",
            "url": "https://arxiv.org/pdf/2201.04309"
          },
          {
            "title": "ReNCE: Learning to Reason by Noise Contrastive Estimation",
            "url": "https://arxiv.org/pdf/2601.22432"
          }
        ]
      },
      "I've found several relevant results on contrastive learning, representation consistency, and related topics. Here's what the search revealed:\n\n## Key Findings:\n\n**InfoNCE and Robustness:**\nRecent research shows that classical InfoNCE loss lacks robustness to label noise, but Symmetric InfoNCE (SymNCE) adds a reverse term to ensure robustness. This framework unifies prior heuristics like nearest neighbor sample selection (Cui et al., January 2025).\n\n**Representation Consistency:**\nA method called Contrastive Learning with Consistent Representations (CoCor) proposes a novel \"DA consistency\" metric that governs how augmented data maps to representation space, ensuring instances are positioned optimally consistent with data augmentation intensity.\n\n**LLM Reasoning:**\nRecent work on \"ReNCE: Learning to Reason by Noise Contrastive Estimation\" demonstrates competitive performance on challenging math benchmarks against strong baselines like DAPO and online DPO (as of February 2026).\n\n**Contrastive Learning Against Noise:**\nA robust contrastive learning approach provides a drop-in replacement for InfoNCE loss and shows consistent improvements on image, video, and graph contrastive learning benchmarks with real-world noise patterns.\n\nThe search results show active research in these areas through 2025-2026, particularly at major venues like SIGIR 2025 and ICLR 2026."
    ],
    "durationSeconds": 7.218821481000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "88c50e0e-7550-451a-a485-1f8d33494591",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
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
  "lastPrompt": "# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling  ## Core Problem  RL-trained mathematical reasoning models achieve SOTA on clean benchmarks bu…",
  "leafUuid": "10143b86-7b03-4a5c-a013-f942f9b2e9f7",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency regularization for math RL",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Tool call

_source line 26 · 2026-05-29T06:09:19.577Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CwSeVoyvxJjdPdZQJMvUwN`</summary>

```json
{
  "query": "CLIPO contrastive learning policy optimization GRPO math reasoning arXiv 2603.10101"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10143b86-7b03-4a5c-a013-f942f9b2e9f7",
  "isSidechain": false,
  "requestId": "req_011CbWMvzUggDMWyNwuT6F7M",
  "type": "assistant",
  "uuid": "6a64c334-813c-46c1-8aa0-2a121b37e6cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015JZKW6x9pgc4LoBBYnFtqn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 22533,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 685,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 22533,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 685
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

_source line 27 · 2026-05-29T06:09:26.533Z_

<details><summary>↩ Tool result · `toolu_01CwSeVoyvxJjdPdZQJMvUwN`</summary>

```text
Web search results for query: "CLIPO contrastive learning policy optimization GRPO math reasoning arXiv 2603.10101"

Links: [{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/pdf/2603.10101"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://www.researchgate.net/publication/401833359_CLIPO_Contrastive_Learning_in_Policy_Optimization_Generalizes_RLVR"},{"title":"[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/abs/2603.10101"},{"title":"Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://huggingface.co/papers/2603.10101"},{"title":"Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models","url":"https://arxiv.org/html/2605.25443"},{"title":"GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub","url":"https://github.com/Qwen-Applications/CLIPO"}]

I found the paper! Here's what the search reveals:

**CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR** (arXiv 2603.10101)

The paper addresses Reinforcement Learning with Verifiable Rewards (RLVR), which has advanced LLM reasoning capacity but relies solely on final answers as outcome rewards, neglecting intermediate reasoning steps. Training on process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying.

**The Approach:**

CLIPO incorporates a contrastive learning mechanism into policy optimization. By optimizing a contrastive loss over successful rollouts, it steers the LLM to capture invariant structures shared across correct reasoning paths, providing more robust cross-trajectory regularization than single-path supervision.

**Results on Math Reasoning:**

On GSM8K math benchmarks, GRPO+CLIPO improves GSM8K-P1 and GSM8K-P2 by +1.48 and +3.36 points respectively, achieving a math-average score of 75.35.

The paper was published in March 2026 and includes a GitHub repository with implementations available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a64c334-813c-46c1-8aa0-2a121b37e6cd",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "868de886-ffcd-47ba-8eba-1a5adf80e108",
  "toolUseResult": {
    "query": "CLIPO contrastive learning policy optimization GRPO math reasoning arXiv 2603.10101",
    "results": [
      {
        "tool_use_id": "srvtoolu_01T1JHPASSDzDidBE9a22kPE",
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
            "title": "[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/abs/2603.10101"
          },
          {
            "title": "Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://huggingface.co/papers/2603.10101"
          },
          {
            "title": "Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models",
            "url": "https://arxiv.org/html/2605.25443"
          },
          {
            "title": "GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub",
            "url": "https://github.com/Qwen-Applications/CLIPO"
          }
        ]
      },
      "I found the paper! Here's what the search reveals:\n\n**CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR** (arXiv 2603.10101)\n\nThe paper addresses Reinforcement Learning with Verifiable Rewards (RLVR), which has advanced LLM reasoning capacity but relies solely on final answers as outcome rewards, neglecting intermediate reasoning steps. Training on process-wrong but outcome-correct rollouts can lead to hallucination and answer-copying.\n\n**The Approach:**\n\nCLIPO incorporates a contrastive learning mechanism into policy optimization. By optimizing a contrastive loss over successful rollouts, it steers the LLM to capture invariant structures shared across correct reasoning paths, providing more robust cross-trajectory regularization than single-path supervision.\n\n**Results on Math Reasoning:**\n\nOn GSM8K math benchmarks, GRPO+CLIPO improves GSM8K-P1 and GSM8K-P2 by +1.48 and +3.36 points respectively, achieving a math-average score of 75.35.\n\nThe paper was published in March 2026 and includes a GitHub repository with implementations available."
    ],
    "durationSeconds": 6.951260054999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6a64c334-813c-46c1-8aa0-2a121b37e6cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-29T06:09:30.861Z_

<details><summary>Logged reasoning block</summary>

```text
This is a critical finding! CLIPO (arXiv 2603.10101, March 2026) is very closely related to this proposal — it also adds contrastive learning to GRPO for math reasoning. This is a very important baseline that the proposal doesn't mention. Let me search for more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "868de886-ffcd-47ba-8eba-1a5adf80e108",
  "isSidechain": false,
  "requestId": "req_011CbWMwfXSAEiK9dkX5SDqN",
  "type": "assistant",
  "uuid": "6758e6d5-9c82-4f72-8f06-f5c80db04eba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bcrU7Q3Cst3Amj1Vr94qf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23218,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 23218,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 29 · 2026-05-29T06:09:31.819Z_

This is a critical finding — CLIPO is highly relevant and not mentioned in the proposal. Let me search for more details and continue my research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6758e6d5-9c82-4f72-8f06-f5c80db04eba",
  "isSidechain": false,
  "requestId": "req_011CbWMwfXSAEiK9dkX5SDqN",
  "type": "assistant",
  "uuid": "50ef9a84-3d92-4942-9047-d2b30062981f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bcrU7Q3Cst3Amj1Vr94qf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23218,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 23218,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 30 · 2026-05-29T06:09:32.320Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016MYbhuBEBPgrHysw3mqq1S`</summary>

```json
{
  "query": "CLIPO contrastive policy optimization GRPO experimental baselines ablation math benchmarks evaluation details 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50ef9a84-3d92-4942-9047-d2b30062981f",
  "isSidechain": false,
  "requestId": "req_011CbWMwfXSAEiK9dkX5SDqN",
  "type": "assistant",
  "uuid": "5eb9612d-d72b-434b-a7bd-bbd3a22f978c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017bcrU7Q3Cst3Amj1Vr94qf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 23218,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 23218,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 31 · 2026-05-29T06:09:43.247Z_

<details><summary>↩ Tool result · `toolu_016MYbhuBEBPgrHysw3mqq1S`</summary>

```text
Web search results for query: "CLIPO contrastive policy optimization GRPO experimental baselines ablation math benchmarks evaluation details 2026"

Links: [{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/pdf/2603.10101"},{"title":"CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://www.researchgate.net/publication/401833359_CLIPO_Contrastive_Learning_in_Policy_Optimization_Generalizes_RLVR"},{"title":"GitHub - Qwen-Applications/CLIPO: CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR · GitHub","url":"https://github.com/Qwen-Applications/CLIPO"},{"title":"Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://huggingface.co/papers/2603.10101"},{"title":"DCPO: Dynamic Clipping Policy Optimization","url":"https://arxiv.org/html/2509.02333v1"},{"title":"[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR","url":"https://arxiv.org/abs/2603.10101"},{"title":"Single-stream Policy Optimization","url":"https://arxiv.org/pdf/2509.13232"},{"title":"A Unified Framework for Rethinking Policy Divergence Measures in GRPO","url":"https://arxiv.org/pdf/2602.05494"}]

Based on the search results, I found comprehensive information about CLIPO and its experimental evaluation. Here's what I found:

## Overview

CLIPO incorporates a Contrastive Learning mechanism into Policy Optimization to generalize the RLVR process. By optimizing a contrastive loss over successful rollouts, CLIPO steers the LLM to capture the invariant structure shared across correct reasoning paths.

## Experimental Baselines

Integrating CLIPO leads to performance gains across GRPO, GSPO, DAPO, and GMPO in overall average scores by +1.35, +0.80, +1.20, and +0.83 respectively. These represent the main baseline policy optimization methods tested in the ablation study.

## Math Benchmark Results

GRPO+CLIPO improves GSM8K-P1 and GSM8K-P2 by +1.48 and +3.36 points, respectively, and achieves the highest math-average score of 75.35. Additionally, DAPO+CLIPO achieves the highest average score of 44.05, surpassing all baselines.

Across GRPO, GSPO, DAPO, and GMPO, CLIPO yields average improvements of +1.50, +0.34, +0.59, and +1.28 respectively, demonstrating effectiveness in enhancing reasoning capabilities under perturbations and distribution shifts.

## Overall Performance

CLIPO consistently improves multiple RLVR baselines across diverse reasoning benchmarks, demonstrating uniform improvements in generalization and robustness for policy optimization of LLMs. CLIPO attains either the best or second-best performance across all four general reasoning benchmarks.

The research paper is available at arXiv (2603.10101) and was published in March 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5eb9612d-d72b-434b-a7bd-bbd3a22f978c",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "84ce863a-bbf2-41aa-bb57-9ed6fc1cd5cb",
  "toolUseResult": {
    "query": "CLIPO contrastive policy optimization GRPO experimental baselines ablation math benchmarks evaluation details 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QUM3s157UUWfLqggqbzKip",
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
            "title": "Paper page - CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://huggingface.co/papers/2603.10101"
          },
          {
            "title": "DCPO: Dynamic Clipping Policy Optimization",
            "url": "https://arxiv.org/html/2509.02333v1"
          },
          {
            "title": "[2603.10101] CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR",
            "url": "https://arxiv.org/abs/2603.10101"
          },
          {
            "title": "Single-stream Policy Optimization",
            "url": "https://arxiv.org/pdf/2509.13232"
          },
          {
            "title": "A Unified Framework for Rethinking Policy Divergence Measures in GRPO",
            "url": "https://arxiv.org/pdf/2602.05494"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about CLIPO and its experimental evaluation. Here's what I found:\n\n## Overview\n\nCLIPO incorporates a Contrastive Learning mechanism into Policy Optimization to generalize the RLVR process. By optimizing a contrastive loss over successful rollouts, CLIPO steers the LLM to capture the invariant structure shared across correct reasoning paths.\n\n## Experimental Baselines\n\nIntegrating CLIPO leads to performance gains across GRPO, GSPO, DAPO, and GMPO in overall average scores by +1.35, +0.80, +1.20, and +0.83 respectively. These represent the main baseline policy optimization methods tested in the ablation study.\n\n## Math Benchmark Results\n\nGRPO+CLIPO improves GSM8K-P1 and GSM8K-P2 by +1.48 and +3.36 points, respectively, and achieves the highest math-average score of 75.35. Additionally, DAPO+CLIPO achieves the highest average score of 44.05, surpassing all baselines.\n\nAcross GRPO, GSPO, DAPO, and GMPO, CLIPO yields average improvements of +1.50, +0.34, +0.59, and +1.28 respectively, demonstrating effectiveness in enhancing reasoning capabilities under perturbations and distribution shifts.\n\n## Overall Performance\n\nCLIPO consistently improves multiple RLVR baselines across diverse reasoning benchmarks, demonstrating uniform improvements in generalization and robustness for policy optimization of LLMs. CLIPO attains either the best or second-best performance across all four general reasoning benchmarks.\n\nThe research paper is available at arXiv (2603.10101) and was published in March 2026."
    ],
    "durationSeconds": 10.920052903000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5eb9612d-d72b-434b-a7bd-bbd3a22f978c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-29T06:09:43.259Z_

```json
{
  "parentUuid": "84ce863a-bbf2-41aa-bb57-9ed6fc1cd5cb",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "419d907e-bf37-4de1-b590-924aa495bdf4",
  "timestamp": "2026-05-29T06:09:43.259Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 33 · 2026-05-29T06:09:46.263Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01La8zLgTNfSjpgyqVTK9W5h`</summary>

```json
{
  "query": "GSM-SEM semantic robustness math reasoning benchmark May 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "419d907e-bf37-4de1-b590-924aa495bdf4",
  "isSidechain": false,
  "requestId": "req_011CbWMxu8mM3YRgVGeGb2VU",
  "type": "assistant",
  "uuid": "b094f4e5-b896-46e1-8aef-ee6c5d64ac11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sv3QBWiLTZzQoaRfM3sMd7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1143,
      "cache_read_input_tokens": 23942,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1143,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 23942,
          "cache_creation_input_tokens": 1143,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1143
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

_source line 34 · 2026-05-29T06:09:59.344Z_

<details><summary>↩ Tool result · `toolu_01La8zLgTNfSjpgyqVTK9W5h`</summary>

```text
Web search results for query: "GSM-SEM semantic robustness math reasoning benchmark May 2026"

Links: [{"title":"[2605.07053] GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations","url":"https://arxiv.org/abs/2605.07053"},{"title":"GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations","url":"https://arxiv.org/html/2605.07053v1"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2402.19255"},{"title":"[PDF] GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GSM-Symbolic:-Understanding-the-Limitations-of-in-Mirzadeh-Alizadeh-Vahid/05506581cade1a8ef6372616cec20b81a3d5c366"},{"title":"GSM-Symbolic: Evaluating LLM Mathematical Reasoning","url":"https://www.emergentmind.com/topics/gsm-symbolic-approach"},{"title":"Benchmarking Reasoning Robustness in Large Language Models","url":"https://arxiv.org/pdf/2503.04550"},{"title":"[PDF] GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GSM-Plus:-A-Comprehensive-Benchmark-for-Evaluating-Li-Cui/bed35010543191bf57a09a6058e75332702d7afa"}]

Based on the search results, I found relevant information about GSM-SEM:

GSM-SEM is a reusable and stochastic framework for generating semantically diverse benchmark variants with substantially higher semantic variance than prior approaches.

The benchmark addresses limitations in existing benchmarks like GSM8K, which are popular measures of mathematical reasoning, but leaderboard gains can overstate true capability due to memorization of fixed test sets.

GSM-SEM perturbs problem statements by modifying entities, attributes, and/or relationships, frequently altering underlying facts and requiring models to recompute solutions under new conditions, while constraining generation to preserve the original calculations/answer and approximate problem difficulty.

The paper was submitted to arXiv on May 8, 2026. This appears to be a recent research paper that addresses the semantic robustness of mathematical reasoning benchmarks through a novel framework for generating semantically variant augmentations of existing math problems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b094f4e5-b896-46e1-8aef-ee6c5d64ac11",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "0d483a79-3412-488c-a9f3-04ce866324e5",
  "toolUseResult": {
    "query": "GSM-SEM semantic robustness math reasoning benchmark May 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RJLVd4LodbQbCAQWey9cFA",
        "content": [
          {
            "title": "[2605.07053] GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations",
            "url": "https://arxiv.org/abs/2605.07053"
          },
          {
            "title": "GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations",
            "url": "https://arxiv.org/html/2605.07053v1"
          },
          {
            "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers",
            "url": "https://arxiv.org/pdf/2402.19255"
          },
          {
            "title": "[PDF] GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GSM-Symbolic:-Understanding-the-Limitations-of-in-Mirzadeh-Alizadeh-Vahid/05506581cade1a8ef6372616cec20b81a3d5c366"
          },
          {
            "title": "GSM-Symbolic: Evaluating LLM Mathematical Reasoning",
            "url": "https://www.emergentmind.com/topics/gsm-symbolic-approach"
          },
          {
            "title": "Benchmarking Reasoning Robustness in Large Language Models",
            "url": "https://arxiv.org/pdf/2503.04550"
          },
          {
            "title": "[PDF] GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/GSM-Plus:-A-Comprehensive-Benchmark-for-Evaluating-Li-Cui/bed35010543191bf57a09a6058e75332702d7afa"
          }
        ]
      },
      "Based on the search results, I found relevant information about GSM-SEM:\n\nGSM-SEM is a reusable and stochastic framework for generating semantically diverse benchmark variants with substantially higher semantic variance than prior approaches.\n\nThe benchmark addresses limitations in existing benchmarks like GSM8K, which are popular measures of mathematical reasoning, but leaderboard gains can overstate true capability due to memorization of fixed test sets.\n\nGSM-SEM perturbs problem statements by modifying entities, attributes, and/or relationships, frequently altering underlying facts and requiring models to recompute solutions under new conditions, while constraining generation to preserve the original calculations/answer and approximate problem difficulty.\n\nThe paper was submitted to arXiv on May 8, 2026. This appears to be a recent research paper that addresses the semantic robustness of mathematical reasoning benchmarks through a novel framework for generating semantically variant augmentations of existing math problems."
    ],
    "durationSeconds": 13.07244023800001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b094f4e5-b896-46e1-8aef-ee6c5d64ac11",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-29T06:10:03.135Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AGckWSeE6vtSkCaYHWrCxA`</summary>

```json
{
  "query": "DyJR JS divergence diversity GRPO arXiv 2603.16157 experimental setup baselines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d483a79-3412-488c-a9f3-04ce866324e5",
  "isSidechain": false,
  "requestId": "req_011CbWMz5si8MQvHWJwfK7rw",
  "type": "assistant",
  "uuid": "954ad478-278a-40ae-a467-6aa7c2ba834c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVtBhpzpB5eyXCRZuwMv6o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 755,
      "cache_read_input_tokens": 25085,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 755,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 25085,
          "cache_creation_input_tokens": 755,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 755
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

_source line 36 · 2026-05-29T06:10:11.141Z_

<details><summary>↩ Tool result · `toolu_01AGckWSeE6vtSkCaYHWrCxA`</summary>

```text
Web search results for query: "DyJR JS divergence diversity GRPO arXiv 2603.16157 experimental setup baselines"

Links: [{"title":"[2603.16157] DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay","url":"https://arxiv.org/abs/2603.16157"},{"title":"DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay","url":"https://arxiv.org/html/2603.16157"},{"title":"DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/pdf/2603.16157"},{"title":"DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO","url":"https://arxiv.org/pdf/2512.21514"},{"title":"[2505.09655v2] DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of Large Language Models","url":"https://arxiv.org/abs/2505.09655v2"},{"title":"Advances in GRPO for Generation Models: A Survey","url":"https://arxiv.org/html/2603.06623v1"},{"title":"DRA-GRPO: Exploring Diversity-Aware Reward ...","url":"https://arxiv.org/abs/2505.09655"},{"title":"The Representation Jensen-R\\'enyi Divergence","url":"https://arxiv.org/pdf/2112.01583"}]

I found relevant information about the DyJR paper (arXiv 2603.16157). Here's what I found regarding the experimental setup and baselines:

## Paper Overview

DyJR (Dynamic Jensen-Shannon Replay) is a regularization framework using a dynamic reference distribution from recent trajectories, introducing a Time-Sensitive Dynamic Buffer that uses FIFO and adaptive sizing, and Jensen-Shannon Divergence Regularization which prevents diversity collapse.

## Experimental Baselines

The experiments compared with replay buffer-based methods including RLEP (which required storing approximately 28k QA pairs), while DyJR theoretically requires storing only 2k pairs. 

Ex-GRPO was also tested as a baseline, which outperformed RLEP by selecting samples based on entropy to indirectly preserve diversity.

## Jensen-Shannon Divergence Validation

The paper justified the selection of JS divergence as the regularization metric by comparing it against the standard Forward KL divergence approach, with the JS-based DyJR significantly outperforming the Forward KL variant (34.1% vs. lower performance).

The paper appears to focus on LLM reasoning tasks with experiments involving QA pairs and demonstrates the efficiency advantages of the proposed method over existing replay-based approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "954ad478-278a-40ae-a467-6aa7c2ba834c",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "924bc2ae-b49b-4fd1-9320-403f7b2e9721",
  "toolUseResult": {
    "query": "DyJR JS divergence diversity GRPO arXiv 2603.16157 experimental setup baselines",
    "results": [
      {
        "tool_use_id": "srvtoolu_017LM5NNLihCVrfCsYbPf1Gg",
        "content": [
          {
            "title": "[2603.16157] DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay",
            "url": "https://arxiv.org/abs/2603.16157"
          },
          {
            "title": "DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards via Dynamic Jensen-Shannon Replay",
            "url": "https://arxiv.org/html/2603.16157"
          },
          {
            "title": "DyJR: Preserving Diversity in Reinforcement Learning with Verifiable Rewards",
            "url": "https://arxiv.org/pdf/2603.16157"
          },
          {
            "title": "DiverseGRPO: Mitigating Mode Collapse in Image Generation via Diversity-Aware GRPO",
            "url": "https://arxiv.org/pdf/2512.21514"
          },
          {
            "title": "[2505.09655v2] DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of Large Language Models",
            "url": "https://arxiv.org/abs/2505.09655v2"
          },
          {
            "title": "Advances in GRPO for Generation Models: A Survey",
            "url": "https://arxiv.org/html/2603.06623v1"
          },
          {
            "title": "DRA-GRPO: Exploring Diversity-Aware Reward ...",
            "url": "https://arxiv.org/abs/2505.09655"
          },
          {
            "title": "The Representation Jensen-R\\'enyi Divergence",
            "url": "https://arxiv.org/pdf/2112.01583"
          }
        ]
      },
      "I found relevant information about the DyJR paper (arXiv 2603.16157). Here's what I found regarding the experimental setup and baselines:\n\n## Paper Overview\n\nDyJR (Dynamic Jensen-Shannon Replay) is a regularization framework using a dynamic reference distribution from recent trajectories, introducing a Time-Sensitive Dynamic Buffer that uses FIFO and adaptive sizing, and Jensen-Shannon Divergence Regularization which prevents diversity collapse.\n\n## Experimental Baselines\n\nThe experiments compared with replay buffer-based methods including RLEP (which required storing approximately 28k QA pairs), while DyJR theoretically requires storing only 2k pairs. \n\nEx-GRPO was also tested as a baseline, which outperformed RLEP by selecting samples based on entropy to indirectly preserve diversity.\n\n## Jensen-Shannon Divergence Validation\n\nThe paper justified the selection of JS divergence as the regularization metric by comparing it against the standard Forward KL divergence approach, with the JS-based DyJR significantly outperforming the Forward KL variant (34.1% vs. lower performance).\n\nThe paper appears to focus on LLM reasoning tasks with experiments involving QA pairs and demonstrates the efficiency advantages of the proposed method over existing replay-based approaches."
    ],
    "durationSeconds": 7.997377234999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "954ad478-278a-40ae-a467-6aa7c2ba834c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-29T06:10:14.084Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01URZ7aar5H6MikDhncjJzcb`</summary>

```json
{
  "query": "Qwen3-8B GRPO training compute requirements GPU hours math reasoning RL 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "924bc2ae-b49b-4fd1-9320-403f7b2e9721",
  "isSidechain": false,
  "requestId": "req_011CbWMzxN3j2K9ot7bqhFHw",
  "type": "assistant",
  "uuid": "f7d46a6a-e619-4437-b64e-3c0509a20099",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkJGMK6RAUyvQkSiQr4v2L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 796,
      "cache_read_input_tokens": 25840,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 796,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 25840,
          "cache_creation_input_tokens": 796,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 796
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

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling  ## Core Problem  RL-trained mathematical reasoning models achieve SOTA on clean benchmarks bu…",
  "leafUuid": "f7d46a6a-e619-4437-b64e-3c0509a20099",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency regularization for math RL",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Tool result

_source line 40 · 2026-05-29T06:10:21.224Z_

<details><summary>↩ Tool result · `toolu_01URZ7aar5H6MikDhncjJzcb`</summary>

```text
Web search results for query: "Qwen3-8B GRPO training compute requirements GPU hours math reasoning RL 2026"

Links: [{"title":"Qwen3 Best Practices — swift 3.7.3 documentation","url":"https://swift.readthedocs.io/en/v3.7/BestPractices/Qwen3-Best-Practice.html"},{"title":"Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models","url":"https://arxiv.org/pdf/2507.18014"},{"title":"Comprehensive Hardware Requirements Report for Qwen3 (Part I) - DEV Community","url":"https://dev.to/ai4b/comprehensive-hardware-requirements-report-for-qwen-3-a5g"},{"title":"Qwen3-8B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen3-8b"},{"title":"Qwen3.5-0.8B: Specifications and GPU VRAM Requirements","url":"https://apxml.com/models/qwen35-08b"},{"title":"Comprehensive Hardware Requirements Report for Qwen3 (Part II) - DEV Community","url":"https://dev.to/ai4b/comprehensive-hardware-requirements-report-for-qwen3-part-ii-4i5l"},{"title":"Qwen 3 GPU Requirements — Original Family (0.6B–235B) VRAM Guide (2026) | Will It Run AI Blog","url":"https://willitrunai.com/blog/qwen-3-gpu-requirements"},{"title":"GPU Requirements 2026: Llama 4 = 1× H100 ($2.50/hr), DeepSeek V3.2 = 8× H200 ($36/hr), Qwen 3.5 27B = 1× H100 | Spheron Blog","url":"https://www.spheron.network/blog/gpu-requirements-cheat-sheet-2026/"}]

Based on the search results, I found some relevant information about Qwen3-8B GRPO training:

## GRPO Training Configuration for Qwen3-8B

A best practice configuration for Qwen3-8B GRPO training uses 8 GPUs (70GB each) with specific hyperparameters including a batch size of 2 per device, 16 generations per sample, and uses vLLM for efficient generation with DeepSpeed zero3 optimization.

## GRPO Training Efficiency Research

Research has been conducted on GRPO fine-tuning across open-source models including Qwen 3B/7B, examining scaling laws that predict reward trajectories during training. A key finding is that training beyond roughly 80% of a single epoch yields negligible reward gains while consuming a substantial fraction of total computation.

## General Training Costs

Training costs vary widely from $50–$500+ per hour depending on GPU count and cloud provider.

The search results don't contain specific information about exact GPU hours or detailed mathematical reasoning RL compute requirements for Qwen3-8B GRPO training. For more detailed specifications about total compute hours needed for full training runs with specific math reasoning datasets, you may want to consult the official Alibaba Cloud/Qwen documentation or academic papers on GRPO scaling laws.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7d46a6a-e619-4437-b64e-3c0509a20099",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "a560bbcb-d6b8-42ef-b3b4-14bf4561a1bc",
  "toolUseResult": {
    "query": "Qwen3-8B GRPO training compute requirements GPU hours math reasoning RL 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LZRuq1AtiKi8aqDGGAX5Kn",
        "content": [
          {
            "title": "Qwen3 Best Practices — swift 3.7.3 documentation",
            "url": "https://swift.readthedocs.io/en/v3.7/BestPractices/Qwen3-Best-Practice.html"
          },
          {
            "title": "Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models",
            "url": "https://arxiv.org/pdf/2507.18014"
          },
          {
            "title": "Comprehensive Hardware Requirements Report for Qwen3 (Part I) - DEV Community",
            "url": "https://dev.to/ai4b/comprehensive-hardware-requirements-report-for-qwen-3-a5g"
          },
          {
            "title": "Qwen3-8B: Specifications and GPU VRAM Requirements",
            "url": "https://apxml.com/models/qwen3-8b"
          },
          {
            "title": "Qwen3.5-0.8B: Specifications and GPU VRAM Requirements",
            "url": "https://apxml.com/models/qwen35-08b"
          },
          {
            "title": "Comprehensive Hardware Requirements Report for Qwen3 (Part II) - DEV Community",
            "url": "https://dev.to/ai4b/comprehensive-hardware-requirements-report-for-qwen3-part-ii-4i5l"
          },
          {
            "title": "Qwen 3 GPU Requirements — Original Family (0.6B–235B) VRAM Guide (2026) | Will It Run AI Blog",
            "url": "https://willitrunai.com/blog/qwen-3-gpu-requirements"
          },
          {
            "title": "GPU Requirements 2026: Llama 4 = 1× H100 ($2.50/hr), DeepSeek V3.2 = 8× H200 ($36/hr), Qwen 3.5 27B = 1× H100 | Spheron Blog",
            "url": "https://www.spheron.network/blog/gpu-requirements-cheat-sheet-2026/"
          }
        ]
      },
      "Based on the search results, I found some relevant information about Qwen3-8B GRPO training:\n\n## GRPO Training Configuration for Qwen3-8B\n\nA best practice configuration for Qwen3-8B GRPO training uses 8 GPUs (70GB each) with specific hyperparameters including a batch size of 2 per device, 16 generations per sample, and uses vLLM for efficient generation with DeepSpeed zero3 optimization.\n\n## GRPO Training Efficiency Research\n\nResearch has been conducted on GRPO fine-tuning across open-source models including Qwen 3B/7B, examining scaling laws that predict reward trajectories during training. A key finding is that training beyond roughly 80% of a single epoch yields negligible reward gains while consuming a substantial fraction of total computation.\n\n## General Training Costs\n\nTraining costs vary widely from $50–$500+ per hour depending on GPU count and cloud provider.\n\nThe search results don't contain specific information about exact GPU hours or detailed mathematical reasoning RL compute requirements for Qwen3-8B GRPO training. For more detailed specifications about total compute hours needed for full training runs with specific math reasoning datasets, you may want to consult the official Alibaba Cloud/Qwen documentation or academic papers on GRPO scaling laws."
    ],
    "durationSeconds": 7.1326553960000165,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f7d46a6a-e619-4437-b64e-3c0509a20099",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-29T06:10:23.889Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FnyMgoQNSMurJjw5SF7pmb`</summary>

```json
{
  "query": "\"Harmony in Diversity\" multi-domain contrastive policy optimization reasoning 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a560bbcb-d6b8-42ef-b3b4-14bf4561a1bc",
  "isSidechain": false,
  "requestId": "req_011CbWN1hqChz7HUxvy1uGCd",
  "type": "assistant",
  "uuid": "959345dd-3816-42d3-9cf3-4e6c2a7801a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V6PkPH6Pdzbi7nDLaM3k9n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 26636,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 886,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26636,
          "cache_creation_input_tokens": 886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 886
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

_source line 42 · 2026-05-29T06:10:35.827Z_

<details><summary>↩ Tool result · `toolu_01FnyMgoQNSMurJjw5SF7pmb`</summary>

```text
Web search results for query: ""Harmony in Diversity" multi-domain contrastive policy optimization reasoning 2026 arXiv"

Links: [{"title":"Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models","url":"https://arxiv.org/html/2605.25443"},{"title":"[2605.25443] Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models","url":"https://arxiv.org/abs/2605.25443"},{"title":"Diversity-Aware Policy Optimization for Large Language Model Reasoning | OpenReview","url":"https://openreview.net/forum?id=5eZ0iykpDU"},{"title":"[2505.23433] Diversity-Aware Policy Optimization for Large Language Model Reasoning","url":"https://arxiv.org/abs/2505.23433"},{"title":"SetPO: Set-Level Policy Optimization for Diversity-Preserving LLM Reasoning","url":"https://arxiv.org/pdf/2602.01062"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** "Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models"

**arXiv ID:** 2605.25443 (published 4 days ago, which would be late May 2026)

**Main Contribution:** The paper proposes Multi-domain Contrastive Policy Optimization (MCPO), which analyzes the structural relationships among rollouts and promotes cross-domain knowledge sharing and in-domain knowledge consolidation in a contrastive manner.

**Key Method Details:** For a given prompt, MCPO identifies transferable reasoning trajectories from other domains as positive examples, while treating incorrect rollouts as negative ones, encouraging consistent representations for positive pairs and pushing negative pairs apart.

**Problem Addressed:** GRPO-style RL methods in multi-domain settings often fail to achieve consistent improvements across all domains due to inherent interference in policy optimization, with prior studies focusing on alleviating cross-domain interference while neglecting the pivotal role of knowledge sharing.

You can access the full paper at https://arxiv.org/abs/2605.25443.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "959345dd-3816-42d3-9cf3-4e6c2a7801a9",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "bd0a935c-275b-4f80-bdf4-63a541c36189",
  "toolUseResult": {
    "query": "\"Harmony in Diversity\" multi-domain contrastive policy optimization reasoning 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EQeK9n36LqaaEoRUksAUP2",
        "content": [
          {
            "title": "Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models",
            "url": "https://arxiv.org/html/2605.25443"
          },
          {
            "title": "[2605.25443] Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models",
            "url": "https://arxiv.org/abs/2605.25443"
          },
          {
            "title": "Diversity-Aware Policy Optimization for Large Language Model Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=5eZ0iykpDU"
          },
          {
            "title": "[2505.23433] Diversity-Aware Policy Optimization for Large Language Model Reasoning",
            "url": "https://arxiv.org/abs/2505.23433"
          },
          {
            "title": "SetPO: Set-Level Policy Optimization for Diversity-Preserving LLM Reasoning",
            "url": "https://arxiv.org/pdf/2602.01062"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper Title:** \"Harmony in Diversity: Multi-domain Contrastive Policy Optimization for Large Reasoning Models\"\n\n**arXiv ID:** 2605.25443 (published 4 days ago, which would be late May 2026)\n\n**Main Contribution:** The paper proposes Multi-domain Contrastive Policy Optimization (MCPO), which analyzes the structural relationships among rollouts and promotes cross-domain knowledge sharing and in-domain knowledge consolidation in a contrastive manner.\n\n**Key Method Details:** For a given prompt, MCPO identifies transferable reasoning trajectories from other domains as positive examples, while treating incorrect rollouts as negative ones, encouraging consistent representations for positive pairs and pushing negative pairs apart.\n\n**Problem Addressed:** GRPO-style RL methods in multi-domain settings often fail to achieve consistent improvements across all domains due to inherent interference in policy optimization, with prior studies focusing on alleviating cross-domain interference while neglecting the pivotal role of knowledge sharing.\n\nYou can access the full paper at https://arxiv.org/abs/2605.25443."
    ],
    "durationSeconds": 11.921100548999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "959345dd-3816-42d3-9cf3-4e6c2a7801a9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-29T06:10:39.166Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to provide a thorough review. Let me also search for one more thing - the GRPO-CARE paper and CSR paper mentioned in the proposal to understand if there are any other recent works that might be relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd0a935c-275b-4f80-bdf4-63a541c36189",
  "isSidechain": false,
  "requestId": "req_011CbWN2mv3fwoJWzZjk9v6x",
  "type": "assistant",
  "uuid": "0aecf896-712d-42e7-a279-466591d3bde0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Djb5TM1FqfKXiHCLxfuBKr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 27522,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 27522,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 44 · 2026-05-29T06:10:39.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NpNRZGScyCeTiiUzaWHndx`</summary>

```json
{
  "query": "GRPO-CARE consistency bonus reasoning answer likelihood multimodal video reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0aecf896-712d-42e7-a279-466591d3bde0",
  "isSidechain": false,
  "requestId": "req_011CbWN2mv3fwoJWzZjk9v6x",
  "type": "assistant",
  "uuid": "d31dba51-1d27-4ffe-83dd-e9c90aac3d93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Djb5TM1FqfKXiHCLxfuBKr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 27522,
      "output_tokens": 136,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 625,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 136,
          "cache_read_input_tokens": 27522,
          "cache_creation_input_tokens": 625,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 625
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

_source line 45 · 2026-05-29T06:10:49.180Z_

<details><summary>↩ Tool result · `toolu_01NpNRZGScyCeTiiUzaWHndx`</summary>

```text
Web search results for query: "GRPO-CARE consistency bonus reasoning answer likelihood multimodal video reasoning 2026"

Links: [{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning | OpenReview","url":"https://openreview.net/forum?id=XoUJk0aDCN"},{"title":"[2506.16141] GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://arxiv.org/abs/2506.16141"},{"title":"(PDF) GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://www.researchgate.net/publication/392917728_GRPO-CARE_Consistency-Aware_Reinforcement_Learning_for_Multimodal_Reasoning"},{"title":"Paper page - GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://huggingface.co/papers/2506.16141"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning | Latest Papers | HyperAI超神经","url":"https://hyper.ai/en/papers/2506.16141"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250616141C/abstract"},{"title":"GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning","url":"https://arxiv.org/html/2506.16141v1"},{"title":"GitHub - TencentARC/GRPO-CARE","url":"https://github.com/TencentARC/GRPO-CARE"}]

The search found comprehensive information about GRPO-CARE. Here are the key findings:

## Overview

GRPO-CARE addresses the challenge of adapting outcome-supervised GRPO, a reinforcement learning approach that has advanced Chain-of-Thought reasoning in large language models, to multimodal LLMs (MLLMs), which has remained unexplored.

## Consistency Bonus and Reasoning-to-Answer Likelihood

GRPO-CARE introduces a two-tiered reward: (1) a base reward for accuracy, and (2) an adaptive consistency bonus derived from a slowly evolving reference model that calibrates reasoning-to-answer likelihoods within peer groups. The key insight is that a stable reference model—when conditioned on the online model's reasoning trace—should assign a higher likelihood to the correct answer if the reasoning is logically grounded in the multimodal input.

## Multimodal Video Reasoning Benchmark

To enable rigorous analysis, researchers reorganized prior benchmarks featuring complex real-world videos that demand intricate visual understanding and commonsense planning into SEED-Bench-R1, a structured testbed with large-scale training data and hierarchical evaluation across in-distribution, cross-environment, and cross-environment-task scenarios.

## Performance Results

Experiments on SEED-Bench-R1 show that GRPO-CARE consistently outperforms standard GRPO, achieving a 6.7% gain on the hardest evaluation level and a 24.5% increase in reasoning consistency. Standard GRPO, while improving answer accuracy, often reduces logical coherence between reasoning steps and answers, with only a 57.9% consistency rate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d31dba51-1d27-4ffe-83dd-e9c90aac3d93",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "6e95a428-b078-4c66-83b4-8b023fd4373f",
  "toolUseResult": {
    "query": "GRPO-CARE consistency bonus reasoning answer likelihood multimodal video reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RZk8UHdRTungoTTYNDkB7m",
        "content": [
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=XoUJk0aDCN"
          },
          {
            "title": "[2506.16141] GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/abs/2506.16141"
          },
          {
            "title": "(PDF) GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://www.researchgate.net/publication/392917728_GRPO-CARE_Consistency-Aware_Reinforcement_Learning_for_Multimodal_Reasoning"
          },
          {
            "title": "Paper page - GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://huggingface.co/papers/2506.16141"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning | Latest Papers | HyperAI超神经",
            "url": "https://hyper.ai/en/papers/2506.16141"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250616141C/abstract"
          },
          {
            "title": "GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning",
            "url": "https://arxiv.org/html/2506.16141v1"
          },
          {
            "title": "GitHub - TencentARC/GRPO-CARE",
            "url": "https://github.com/TencentARC/GRPO-CARE"
          }
        ]
      },
      "The search found comprehensive information about GRPO-CARE. Here are the key findings:\n\n## Overview\n\nGRPO-CARE addresses the challenge of adapting outcome-supervised GRPO, a reinforcement learning approach that has advanced Chain-of-Thought reasoning in large language models, to multimodal LLMs (MLLMs), which has remained unexplored.\n\n## Consistency Bonus and Reasoning-to-Answer Likelihood\n\nGRPO-CARE introduces a two-tiered reward: (1) a base reward for accuracy, and (2) an adaptive consistency bonus derived from a slowly evolving reference model that calibrates reasoning-to-answer likelihoods within peer groups. The key insight is that a stable reference model—when conditioned on the online model's reasoning trace—should assign a higher likelihood to the correct answer if the reasoning is logically grounded in the multimodal input.\n\n## Multimodal Video Reasoning Benchmark\n\nTo enable rigorous analysis, researchers reorganized prior benchmarks featuring complex real-world videos that demand intricate visual understanding and commonsense planning into SEED-Bench-R1, a structured testbed with large-scale training data and hierarchical evaluation across in-distribution, cross-environment, and cross-environment-task scenarios.\n\n## Performance Results\n\nExperiments on SEED-Bench-R1 show that GRPO-CARE consistently outperforms standard GRPO, achieving a 6.7% gain on the hardest evaluation level and a 24.5% increase in reasoning consistency. Standard GRPO, while improving answer accuracy, often reduces logical coherence between reasoning steps and answers, with only a 57.9% consistency rate."
    ],
    "durationSeconds": 9.447093779999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d31dba51-1d27-4ffe-83dd-e9c90aac3d93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-29T06:10:51.985Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y6RYqooX1c39HiJg6EgYU1`</summary>

```json
{
  "query": "AbstRaL ICLR 2026 Apple abstraction reinforcement learning math robustness baselines evaluation benchmarks"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e95a428-b078-4c66-83b4-8b023fd4373f",
  "isSidechain": false,
  "requestId": "req_011CbWN3kuodhMe88nrvXueZ",
  "type": "assistant",
  "uuid": "0770690a-8846-4437-995d-f036305227b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpXVZLAa9azj9SFNtyGcYg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1007,
      "cache_read_input_tokens": 28147,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1007,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 28147,
          "cache_creation_input_tokens": 1007,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1007
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

_source line 47 · 2026-05-29T06:10:58.602Z_

<details><summary>↩ Tool result · `toolu_01Y6RYqooX1c39HiJg6EgYU1`</summary>

```text
Web search results for query: "AbstRaL ICLR 2026 Apple abstraction reinforcement learning math robustness baselines evaluation benchmarks"

Links: [{"title":"International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research","url":"https://machinelearning.apple.com/updates/apple-at-iclr-2026"},{"title":"AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/abstral"},{"title":"Learning to Reason as Action Abstractions with Scalable Mid-Training RL - Apple Machine Learning Research","url":"https://machinelearning.apple.com/research/action-abstractions"},{"title":"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/pdf/2506.07751"},{"title":"[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking","url":"https://arxiv.org/abs/2506.07751"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"ICLR 2026","url":"https://iclr.cc/"}]

Based on the search results, here's what I found about AbstRaL at ICLR 2026:

## Overview

AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking was presented at ICLR 2026 as a poster by Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe.

## Motivation and Approach

Large language models (LLMs), especially smaller ones, often lack robustness in their reasoning and tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses. AbstRaL focuses on "abstracting" reasoning problems, which not only helps counteract distribution shifts but also facilitates the connection to symbolic tools for deriving solutions.

## Key Finding

The abstraction process is better acquired through reinforcement learning (RL) than just supervised finetuning, which often fails to produce faithful abstractions.

## Results and Benchmarks

AbstRaL significantly mitigates performance degradation on recent GSM perturbation benchmarks. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on OOD mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0770690a-8846-4437-995d-f036305227b6",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "f839f4d5-849f-457b-be01-3478ea641c68",
  "toolUseResult": {
    "query": "AbstRaL ICLR 2026 Apple abstraction reinforcement learning math robustness baselines evaluation benchmarks",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RFsvBdrSixB2BoVFKmnRKS",
        "content": [
          {
            "title": "International Conference on Learning Representations (ICLR) 2026 - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/updates/apple-at-iclr-2026"
          },
          {
            "title": "AbstRaL: Augmenting LLMs’ Reasoning by Reinforcing Abstract Thinking - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/abstral"
          },
          {
            "title": "Learning to Reason as Action Abstractions with Scalable Mid-Training RL - Apple Machine Learning Research",
            "url": "https://machinelearning.apple.com/research/action-abstractions"
          },
          {
            "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/pdf/2506.07751"
          },
          {
            "title": "[2506.07751] AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
            "url": "https://arxiv.org/abs/2506.07751"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          }
        ]
      },
      "Based on the search results, here's what I found about AbstRaL at ICLR 2026:\n\n## Overview\n\nAbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking was presented at ICLR 2026 as a poster by Silin Gao (EPFL), Antoine Bosselut (EPFL), Samy Bengio, and Emmanuel Abbe.\n\n## Motivation and Approach\n\nLarge language models (LLMs), especially smaller ones, often lack robustness in their reasoning and tend to experience performance drops when faced with distribution shifts, such as changes to numerical or nominal variables, or insertions of distracting clauses. AbstRaL focuses on \"abstracting\" reasoning problems, which not only helps counteract distribution shifts but also facilitates the connection to symbolic tools for deriving solutions.\n\n## Key Finding\n\nThe abstraction process is better acquired through reinforcement learning (RL) than just supervised finetuning, which often fails to produce faithful abstractions.\n\n## Results and Benchmarks\n\nAbstRaL significantly mitigates performance degradation on recent GSM perturbation benchmarks. Improving GSM robustness via AbstRaL is shown to also implicitly benefit LLMs' capabilities on OOD mathematical and general reasoning tasks, indicating that abstract thinking broadly enables better generalizability."
    ],
    "durationSeconds": 6.55278744700001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0770690a-8846-4437-995d-f036305227b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-29T06:11:01.693Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UDknqV1xfpDh4vn2g4siaM`</summary>

```json
{
  "query": "PutnamGAP benchmark math robustness evaluation LLM 2025 arXiv experimental design perturbation types"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f839f4d5-849f-457b-be01-3478ea641c68",
  "isSidechain": false,
  "requestId": "req_011CbWN4TDDG6cMTbQwccEDB",
  "type": "assistant",
  "uuid": "5af99a1f-582d-4edf-9d64-ffa9ba8ab138",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GNtX3YEkSXn6KsA5MNvxbY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 752,
      "cache_read_input_tokens": 29154,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 752,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 29154,
          "cache_creation_input_tokens": 752,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 752
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

_source line 49 · 2026-05-29T06:11:11.235Z_

<details><summary>↩ Tool result · `toolu_01UDknqV1xfpDh4vn2g4siaM`</summary>

```text
Web search results for query: "PutnamGAP benchmark math robustness evaluation LLM 2025 arXiv experimental design perturbation types"

Links: [{"title":"[2508.08833] An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/abs/2508.08833"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v2"},{"title":"An Investigation of Robustness of LLMs in Mathematical ...","url":"https://arxiv.org/pdf/2508.08833"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038"},{"title":"[2509.04013] On Robustness and Reliability of Benchmark-Based Evaluation of LLMs","url":"https://arxiv.org/abs/2509.04013"},{"title":"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2402.19255"},{"title":"Putnam-AXIOM: A Functional and Static Benchmark for ...","url":"https://arxiv.org/pdf/2508.08292"}]

Based on the search results, I found comprehensive information about PutnamGAP. Here are the key findings:

## PutnamGAP Benchmark Overview

PutnamGAP is a new benchmark dataset with multiple mathematically-equivalent variations of competition-level math problems. The dataset provides multiple mathematically-equivalent variations of competition-level math problems.

## Experimental Design and Perturbation Types

The paper introduces a systematic framework to assess LLMs' mathematical-reasoning robustness by stress-testing them on advanced math problems that are mathematically equivalent but with linguistic and parametric variation. These transformations allow researchers to measure the sensitivity of LLMs to non-mathematical perturbations.

The perturbation types specifically include:
- **Surface-renaming variants**: OpenAI's flagship reasoning model, O3, scores 51.5% on the originals but drops by 4.7 percentage points on surface-renaming variants
- **Parametric variants**: O3 drops by 12.9 percentage points on parametric variants

## Evaluation Results

The dataset evaluates multiple families of representative LLMs and examines their robustness, with across 18 commercial and open-source models showing sharp performance degradation on the variants.

## Dataset Characteristics

The dataset has broad mathematical coverage including Algebra (641), Analysis (521), Number Theory (392), Combinatorics (286), and Geometry (239), with 803 of the questions being proofs and 248 being calculations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5af99a1f-582d-4edf-9d64-ffa9ba8ab138",
  "isSidechain": false,
  "promptId": "c64ca2f9-b315-44c7-bcfb-a85aab0121d6",
  "type": "user",
  "uuid": "9d407255-c906-4a33-ab4a-965ce9ba0c4a",
  "toolUseResult": {
    "query": "PutnamGAP benchmark math robustness evaluation LLM 2025 arXiv experimental design perturbation types",
    "results": [
      {
        "tool_use_id": "srvtoolu_01351CxWSZRATkAiambPUn27",
        "content": [
          {
            "title": "[2508.08833] An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/abs/2508.08833"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v2"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical ...",
            "url": "https://arxiv.org/pdf/2508.08833"
          },
          {
            "title": "Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/html/2506.05038"
          },
          {
            "title": "[2509.04013] On Robustness and Reliability of Benchmark-Based Evaluation of LLMs",
            "url": "https://arxiv.org/abs/2509.04013"
          },
          {
            "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of   LLMs as Mathematical Problem Solvers",
            "url": "https://arxiv.org/pdf/2402.19255"
          },
          {
            "title": "Putnam-AXIOM: A Functional and Static Benchmark for ...",
            "url": "https://arxiv.org/pdf/2508.08292"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about PutnamGAP. Here are the key findings:\n\n## PutnamGAP Benchmark Overview\n\nPutnamGAP is a new benchmark dataset with multiple mathematically-equivalent variations of competition-level math problems. The dataset provides multiple mathematically-equivalent variations of competition-level math problems.\n\n## Experimental Design and Perturbation Types\n\nThe paper introduces a systematic framework to assess LLMs' mathematical-reasoning robustness by stress-testing them on advanced math problems that are mathematically equivalent but with linguistic and parametric variation. These transformations allow researchers to measure the sensitivity of LLMs to non-mathematical perturbations.\n\nThe perturbation types specifically include:\n- **Surface-renaming variants**: OpenAI's flagship reasoning model, O3, scores 51.5% on the originals but drops by 4.7 percentage points on surface-renaming variants\n- **Parametric variants**: O3 drops by 12.9 percentage points on parametric variants\n\n## Evaluation Results\n\nThe dataset evaluates multiple families of representative LLMs and examines their robustness, with across 18 commercial and open-source models showing sharp performance degradation on the variants.\n\n## Dataset Characteristics\n\nThe dataset has broad mathematical coverage including Algebra (641), Analysis (521), Number Theory (392), Combinatorics (286), and Geometry (239), with 803 of the questions being proofs and 248 being calculations."
    ],
    "durationSeconds": 9.537869105999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5af99a1f-582d-4edf-9d64-ffa9ba8ab138",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling  ## Core Problem  RL-trained mathematical reasoning models achieve SOTA on clean benchmarks bu…",
  "leafUuid": "9d407255-c906-4a33-ab4a-965ce9ba0c4a",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency regularization for math RL",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Assistant

_source line 52 · 2026-05-29T06:13:04.990Z_

Now I have sufficient research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **[CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)** (arXiv, Mar 2026): 将对比学习（InfoNCE）集成到 GRPO 中，用于捕获正确推理路径间的不变结构。在 GSM8K-P1/P2 上分别 +1.48/+3.36。对比 GRPO/GSPO/DAPO/GMPO 等多个 baseline，有 GitHub 开源实现。**与本 proposal 的 contrastive 组件高度重合**。
- **[Harmony in Diversity: MCPO](https://arxiv.org/abs/2605.25443)** (arXiv, May 2026): 在 GRPO 中引入跨域对比策略优化，利用正确推理轨迹作为正例、错误轨迹作为负例做对比学习。进一步验证了 contrastive + GRPO 的范式。
- **[TA-GRPO](https://arxiv.org/abs/2601.22478)** (arXiv, Jan 2026): 对语义等价变体做 reward pooling，验证 zero-gradient 问题减少 12-16pp。实验仅报告 Pass@k，无任何 robustness benchmark 评测。Ablation 证明 "augmentation without pooling doesn't help"。
- **[AIR](https://arxiv.org/abs/2605.20994)** (arXiv, May 2026): 非对称 stop-gradient anchor 正则化 + GRPO，主要面向 safety alignment，math 为辅助评测。实验含 in-distribution/OOD 一致性。
- **[AbstRaL](https://arxiv.org/abs/2506.07751)** (ICLR 2026): RL 训练抽象思维，在 GSM perturbation benchmarks 上显著缓解性能退化，但限于 GSM 级别。
- **[DyJR](https://arxiv.org/abs/2603.16157)** (arXiv, Mar 2026): 用 JS-divergence 做动态 replay 正则化防止 diversity collapse，验证 JS 优于 Forward KL。
- **[GRPO-CARE](https://arxiv.org/abs/2506.16141)** (Jun 2026): 在多模态推理中加 consistency bonus，提升 24.5% reasoning consistency。
- **[PutnamGAP](https://arxiv.org/abs/2508.08833)**: 覆盖代数/分析/数论/组合/几何 803 道证明题 + 248 计算题；perturbation 包括 surface-renaming 和 parametric variants。O3 在 parametric variants 上下降 12.9pp。

- **调研总结**: 这个领域在 2026 年已经出现了多个将对比学习与 GRPO 结合的工作（CLIPO、MCPO），且 JS-divergence 作为 GRPO 正则化器已被 DyJR 验证。审稿人会期望：(1) 与 CLIPO 的详细对比和差异分析；(2) 在多个标准 robustness benchmark 上的完整评测；(3) compute-normalized 公平对比；(4) 充分的 ablation 隔离各组件贡献。

---

【缺陷 1】
- 类别: baseline 不足或过时
- 问题: **Proposal 完全遗漏了 CLIPO (arXiv 2603.10101, Mar 2026)**——这是与本 proposal 最直接相关的 concurrent work。CLIPO 同样将对比学习（InfoNCE over successful rollouts）集成到 GRPO 中用于 math reasoning，且已有开源实现和多 benchmark 评测。Proposal 的 contrastive discrimination loss（L_contrastive）与 CLIPO 的核心机制高度重叠。不将 CLIPO 作为 baseline，审稿人第一反应就会质疑"这和 CLIPO 有什么区别"，几乎可以确定会被要求 revision 或直接 reject。
- 严重度: 可补救
- 补救方案: 
  1. **必须将 CLIPO 加入 baseline 表（第 8 个 baseline）**，并在实验中做 head-to-head 对比。
  2. **在 related work 中明确区分**：CLIPO 的对比学习是在同一问题的多个正确 rollouts 之间做（cross-trajectory within same prompt），目的是捕获推理不变结构；ConsistGRPO 的对比学习是在**语义等价但表面形式不同的问题对**之间做（cross-perturbation），目的是 perturbation invariance。这是本质差异——CLIPO 不涉及 perturbation generation pipeline，也不 enforce cross-perturbation invariance。
  3. 同时考虑加入 **MCPO (arXiv 2605.25443)** 作为参考，因其也是 contrastive + GRPO，进一步说明 ConsistGRPO 的定位差异。
- 调研依据: CLIPO (arXiv 2603.10101) 和 MCPO (arXiv 2605.25443)

【缺陷 2】
- 类别: 实验设计不足
- 问题: **AbstRaL baseline 的可执行性存疑**。Proposal 将 AbstRaL 列为 baseline，但 AbstRaL 的核心设计是 GSM 级别（grade-school math），其抽象策略和训练数据主要针对 GSM8K 及其变体。Proposal 的主要评测是在 MATH/AMC/AIME 竞赛数学级别。直接在竞赛数学上运行 AbstRaL 可能需要重新训练或适配，且原论文未提供竞赛级别的实验。如果 AbstRaL 在竞赛数学上表现很差，这个 baseline 的对比价值有限（strawman comparison），反而会被审稿人质疑公平性。
- 严重度: 可补救
- 补救方案:
  1. 在 GSM-Symbolic 上保留 AbstRaL 对比（这是其强项），但在 MATH/AIME 级别实验中将其标注为"best-effort reproduction"。
  2. 明确说明 AbstRaL 的局限性（仅 GSM 级别验证），避免 cherry-picking 的印象。
  3. 如果 AbstRaL 没有开源代码或竞赛级别的 checkpoint，考虑将其降级为 related work 讨论，不作为实验 baseline。
- 调研依据: AbstRaL (ICLR 2026) 原论文实验限于 GSM perturbation benchmarks

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: **缺少 Pass@k 指标**。TA-GRPO 的核心实验指标是 Pass@k（k=1,4,8,16,32,64），且 proposal 自己也引用了 TA-GRPO 的 Pass@k 结果。如果 ConsistGRPO 只报告 greedy accuracy（Pass@1）而不报告 Pass@k，无法直接与 TA-GRPO 做 apples-to-apples 对比。此外，Pass@k 指标可以揭示 consistency regularization 对 solution diversity 的影响——这是审稿人会关心的关键问题（consistency 是否以牺牲 diversity 为代价？）。
- 严重度: 可补救
- 补救方案:
  1. 在主表中增加 Pass@k（至少 k=1,8,64）作为评测指标。
  2. 在 ablation 中分析 λ₁ (JS consistency weight) 对 Pass@k 曲线的影响：较强的一致性约束是否导致 diversity collapse？这直接关联 DyJR 提出的 diversity preservation 问题。
  3. 报告 entropy trajectory（proposal 已规划）可以部分回答这个问题，但 Pass@k 是更直接的度量。
- 调研依据: TA-GRPO (arXiv 2601.22478) 以 Pass@k 为核心指标；DyJR (arXiv 2603.16157) 关注 diversity collapse

【缺陷 4】
- 类别: ablation 不完整
- 问题: **缺少 JS-divergence vs. KL-divergence vs. 其他 divergence 的 ablation**。Proposal 选择 JS-divergence 作为 consistency loss 而非 KL-divergence，但未在 ablation 中设计对照实验。DyJR 已专门做过 JS vs. Forward KL 的对比（JS 显著优于 Forward KL），AIR 则使用了 asymmetric KL with stop-gradient。审稿人几乎一定会问"为什么选 JS 而不是 KL？"——如果没有实验支撑，仅靠"JS 是对称的"这一理论论点可能不够说服力。
- 严重度: 可补救
- 补救方案:
  1. 在 ablation 中增加第 5 个维度：**divergence metric comparison**——至少对比 JS-divergence、Forward KL、Reverse KL、Symmetric KL。
  2. 可以引用 DyJR 的发现作为先验支持，但仍需在自己的 setting（cross-perturbation consistency 而非 replay buffer diversity）中验证。
  3. 同时考虑对比 AIR 的 asymmetric stop-gradient 方案——既然 proposal 已在 related work 中论证了"math perturbation pairs 是对称的，不适合 AIR 的非对称设计"，ablation 中应有实验验证这一 claim。
- 调研依据: DyJR (arXiv 2603.16157) 对比 JS vs. Forward KL；AIR (arXiv 2605.20994) 使用非对称 KL；Beyond KL Divergence (arXiv 2602.04380) 探索灵活 Bregman divergence

【缺陷 5】
- 类别: 可行性问题
- 问题: **Perturbation generation pipeline 在竞赛数学级别的可靠性和覆盖率未充分论证**。Proposal 提到对 MATH/AMC/AIME 适配 GSM-Symbolic/VAR-MATH 的 perturbation generator，对几何/数论等困难类型使用 "LLM-generated perturbations with symbolic verification"。但：(a) GSM-Symbolic 的 template-based 方法主要针对 word problem 结构，AIME 级别问题的结构远更复杂和多样；(b) SymPy-based validity filter 对竞赛级问题（涉及复杂代数/组合/数论）的覆盖率可能很低；(c) LLM-generated perturbation 的质量控制（数学等价性保证）是一个独立的工程挑战，proposal 未给出估算的 perturbation success rate 或 pilot study 数据。
- 严重度: 可补救
- 补救方案:
  1. **先做 pilot study**：对 MATH-500 中随机抽取 100 题，运行 perturbation pipeline，报告各子类别（algebra/number theory/geometry 等）的 perturbation success rate。这个数据应在正文中报告。
  2. 如果某些子类别 success rate 过低（如 <30%），考虑在主实验中限定 training data 为 perturbation 可行的子集（algebra/arithmetic），并将其他子类别作为 OOD generalization 评测。
  3. 设定 LLM-generated perturbation 的质量评估流程：random sample + human verification 的 precision/recall。
  4. 考虑直接引用 VAR-MATH 或 MathForge 已有的 perturbation 数据集作为补充，减少 pipeline 自建风险。
- 调研依据: PutnamGAP 需要 5 human-crafted variants per problem（说明自动化对高难度问题不易）；GSM-Symbolic 的 template 方法限于 word problem 结构

【缺陷 6】
- 类别: compute 公平性问题
- 问题: **ConsistGRPO 的 compute overhead 可能被低估**。ConsistGRPO 对每个问题 x 需要：(a) 生成 perturbation x'；(b) 对 x 和 x' 各采样 G 个 rollout（总共 2G 个 rollout vs. 原始 GRPO 的 G 个）；(c) 计算 JS-divergence；(d) 计算 contrastive loss（需要 forward pass 提取 hidden states + MLP projection）。Proposal 设计了 "FLOPs-matched GRPO (2× training steps)" 作为 compute-normalized baseline，但 2× 可能不够——perturbation generation（尤其 LLM-based）、contrastive loss 的额外 forward pass、JS-divergence 计算都有额外开销。如果实际开销是 2.5-3×，那 2× 的 FLOPs-matched baseline 就不公平。
- 严重度: 可补救
- 补救方案:
  1. **在实验前先 profiling**：跑一个 mini experiment 精确测量 ConsistGRPO 相对于 vanilla GRPO 的实际 FLOPs/wall-clock 倍数。
  2. 根据实际测量值调整 FLOPs-matched baseline 的 training steps，而非预设 2×。
  3. 报告 breakdown：rollout generation、JS-divergence computation、contrastive loss computation 各占多少额外开销。
  4. 如果总开销超过 2.5×，考虑增加一个 "sample-efficiency" 分析：ConsistGRPO 在达到某个 robustness threshold 时需要多少 training steps，vs. vanilla GRPO 用同等 compute 能达到什么水平。
- 调研依据: 基于领域实验规范判断；TA-GRPO 的 2G rollouts 设计类似但不含 contrastive loss overhead

【缺陷 7】
- 类别: 评估方案缺陷
- 问题: **缺少 GSM-Plus 作为评测 benchmark**。Proposal 列出了 GSM-Symbolic、VAR-MATH、MATH-Perturb、PutnamGAP、GSM-SEM 五个 robustness benchmark，但遗漏了 **GSM-Plus**——这是较早但仍被广泛引用的 robustness benchmark，包含更多样化的 perturbation 类型（数值变化、增加步骤、语义转换等），且已有 25+ LLM 的评测基线。此外，**GSM-Plus 的 perturbation 类型分类体系**（8 类 perturbation）与 ConsistGRPO 的 ablation（仅 numerical substitution / variable renaming / combined）形成有益补充。
- 严重度: 可补救
- 补救方案:
  1. 将 GSM-Plus 加入评测 benchmark 列表。
  2. 利用 GSM-Plus 的 8 类 perturbation 做 fine-grained robustness 分析，展示 ConsistGRPO 对不同 perturbation 类型的效果差异。
  3. 这是一个低成本高回报的补充——GSM-Plus 是公开数据集，无需额外构建。
- 调研依据: GSM-Plus (arXiv 2402.19255) 被广泛引用，包含 8 类 perturbation 的系统化分类

【缺陷 8】
- 类别: 实验设计不足
- 问题: **缺少对 "consistency-diversity tradeoff" 的系统性分析**。JS-divergence consistency loss 和 contrastive loss 的本质是约束 policy 在不同 perturbation 上产生相似的 rollout 分布——这可能会降低 solution diversity，导致 mode collapse。DyJR 整篇论文就是在解决 GRPO 中的 diversity collapse 问题，CLIPO/MCPO 也讨论了 diversity 保持。Proposal 虽然提到了 entropy trajectory 分析，但缺少更系统的 diversity 指标。
- 严重度: 可补救
- 补救方案:
  1. 增加 **solution diversity 指标**：unique correct solution count per problem（不同推理路径数）、average pairwise edit distance between rollouts、或 DyJR 使用的 diversity metrics。
  2. 在 ablation 中展示 λ₁/λ₂ 从 0 增大到较大值时，accuracy 和 diversity 的 Pareto frontier。
  3. 讨论可能的缓解策略：例如仅对 top-level distribution 做 consistency 而允许 trajectory-level 多样性，或设定 JS-divergence 的 target threshold（不追求 JS→0，而是 JS < ε）。
- 调研依据: DyJR (arXiv 2603.16157) 专注 diversity preservation；CLIPO (arXiv 2603.10101) 讨论 cross-trajectory 一致性与多样性的平衡

---

**总结**：这份 proposal 的实验设计框架已经相当完整（7 个 baseline、4 维 ablation、compute-normalized comparison、dual-scale validation），说明作者对实验规范有清晰认知。上述 8 个缺陷中没有方向性致命问题，全部可补救。其中**缺陷 1（遗漏 CLIPO baseline）是最紧急的**——这是审稿人几乎 100% 会提出的问题，必须在实验设计阶段就解决。缺陷 4（JS vs. KL ablation）和缺陷 8（diversity tradeoff 分析）是审稿人高概率追问的点。其余缺陷的修补成本相对较低，但能显著提升实验的完备性和说服力。

Sources:
- [CLIPO: Contrastive Learning in Policy Optimization Generalizes RLVR](https://arxiv.org/abs/2603.10101)
- [Harmony in Diversity: MCPO](https://arxiv.org/abs/2605.25443)
- [TA-GRPO: Transform-Augmented GRPO Improves Pass@k](https://arxiv.org/abs/2601.22478)
- [AIR: Towards Context-Invariant Safety Alignment](https://arxiv.org/abs/2605.20994)
- [AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking](https://arxiv.org/abs/2506.07751)
- [DyJR: Preserving Diversity in RL with Verifiable Rewards](https://arxiv.org/abs/2603.16157)
- [GRPO-CARE: Consistency-Aware Reinforcement Learning](https://arxiv.org/abs/2506.16141)
- [GSM-Symbolic: Understanding Limitations of Mathematical Reasoning](https://arxiv.org/abs/2410.05229)
- [GSM-Plus: Comprehensive Benchmark for Robustness](https://arxiv.org/abs/2402.19255)
- [PutnamGAP: Robustness via Mathematically-Equivalent Transformation](https://arxiv.org/abs/2508.08833)
- [Beyond KL Divergence: Policy Optimization with Flexible Bregman Divergences](https://arxiv.org/abs/2602.04380)
- [GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations](https://arxiv.org/abs/2605.07053)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d407255-c906-4a33-ab4a-965ce9ba0c4a",
  "isSidechain": false,
  "requestId": "req_011CbWN5PAQump7u9zkfzpeQ",
  "type": "assistant",
  "uuid": "481d04fa-f107-4a7b-b0b3-bf328466c75f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HLbauRECpXby8z3H85iqLC",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 29906,
      "output_tokens": 5691,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5691,
          "cache_read_input_tokens": 29906,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Distribution-Level Consistency Regularization for Perturbation-Invariant Math RL: Beyond Reward Pooling  ## Core Problem  RL-trained mathematical reasoning models achieve SOTA on clean benchmarks bu…",
  "leafUuid": "481d04fa-f107-4a7b-b0b3-bf328466c75f",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Distribution-level consistency regularization for math RL",
  "sessionId": "29ae946e-9ea6-4d7b-8932-f18ef42e5983"
}
```

---
