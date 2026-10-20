# Research conversation: You are a senior ML researcher conducting a comprehensive literature survey. **Today's date: 2026-05-29 (UTC).** ## Task

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/705442d6-a941-47cc-bbd3-b77f62e0535c.jsonl`
- **Structured JSON:** [`b96c60678c62347c51a2.json`](../../sessions/b9/b96c60678c62347c51a2.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T05:23:25.069Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T05:23:25.069Z",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "content": "You are a senior ML researcher conducting a comprehensive literature survey.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Task\nFind the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:\n\n**Target: AAAI 2026\nTrack: Machine Learning (ML) — Reinforcement Learning / Mathematical Reasoning\n\nDirection: RL-trained mathematical reasoning models exhibit 47-73% accuracy drops under trivial perturbations (numerical substitution, variable renaming) despite achieving SOTA on clean benchmarks. We propose Math-Aware Consistency Regularization (MACR): adding a JS-divergence consistency term between model outputs on original and mathematically-equivalent perturbed problems during GRPO training, with a complementary discrimination loss against surface-similar but semantically different problems. This adapts proven NLP consistency techniques (F²C, PPCL) to mathematical reasoning with math-equivalence-aware perturbation generation and RL integration — a combination no existing work provides.\n\nSeed Papers:\n- Mirzadeh et al., GSM-Symbolic (Apple, ICLR 2025) — documents up to 65% accuracy drops from single irrelevant clause; establishes that models pattern-match rather than reason\n- VAR-MATH (arXiv 2025) — most damning evidence: 47.9-72.9% drops for RL models on numerically re-parameterized competition math; directly motivates why RL training is the problem\n- Gao et al., AbstRaL (ICLR 2026) — only existing training-time intervention; uses abstraction not invariance; limited to GSM-level; our primary comparison baseline\n- Flip-Flop Consistency / F²C (arXiv 2024) — JS-divergence consistency for prompt perturbation robustness in NLP; proves the technique works but has never been adapted to math reasoning or RL\n- PPCL (EACL 2024) — KL-based consistency regularization recovering 59-69% of perturbation-induced drops in NLU; complementary theoretical grounding\n- CSR: Causal Consistency Regularization (arXiv 2025) — enforces causal faithfulness via operator-level interventions during SFT; closest methodological cousin but SFT-only and targets faithfulness not perturbation invariance\n- APRM (arXiv 2025) — adversarial PRM training on reasoning errors; shows PRM quality matters for downstream RL; motivates our perturbation-robust PRM extension\n\nKnown Gaps:\n- No work applies consistency regularization (JS/KL divergence across equivalent problem variants) during RL training for mathematical reasoning — F²C and PPCL remain NLP-only and SFT-only\n- No PRM has been trained to be robust to surface-form variations of equivalent problems — APRM addresses reasoning errors, not perturbation invariance\n- No training-time robustness intervention has been demonstrated on competition-level math (AIME/Putnam); AbstRaL is GSM-only\n\nTheoretical Anchor: Mathematical equivalence defines a natural invariance class — problems that differ only in surface form (variable names, specific numbers, phrasing) but share identical mathematical structure should produce identical solution distributions. RL training violates this invariance because the reward signal (correct/incorrect final answer) provides no gradient against surface-form-dependent reasoning. A consistency regularization term explicitly penalizes policy divergence across equivalent variants, forcing the model to learn representations that are invariant to mathematically irrelevant features. This is a direct instantiation of Invariant Risk Minimization principles in the RL-for-reasoning setting.\n\nConstraints:\n- Compute: ≤200 H100-hours (budget: 40h baseline GRPO + 90h method variants + 30h evaluation + 20h analysis + 20h buffer)\n- Models: Primary experiments on 7B (Qwen2.5-Math-7B); scaling verification on 14B\n- Evaluation: GSM-Symbolic, GSM-Plus, VAR-MATH (AMC23/AIME24/AIME25), MATH-Perturb; train-time perturbations (numerical substitution, variable renaming) held out from eval perturbations (distractor insertion, structural changes)\n\nQuality Self-Checks:\n- [x] Core insight: RL training optimizes for reward on fixed problem forms, creating surface-form dependencies that consistency regularization can break by enforcing invariance across equivalent variants.\n- [x] Why not obvious: Consistency regularization is well-known in NLP but requires math-aware equivalence-preserving perturbation generation (not just paraphrase) and RL integration (not just SFT) — two non-trivial adaptations that straddle communities.\n- [ ] Baseline fear test: A pure data-augmentation baseline (adding perturbed problems to RL training without consistency loss) could achieve substantial gains. The paper MUST include this baseline and show the consistency term provides additional benefit beyond augmentation. If the gap is <5%, the contribution is weak.\n- [x] Information exploited: Mathematical equivalence structure — the method uses symbolic verification that perturbations preserve the problem's mathematical structure, which pure augmentation or paraphrase-based consistency ignores.\n\nAvoid:\n- Framing this as 'just data augmentation with extra steps' — the consistency objective is the contribution, not the perturbation generation. Must clearly show augmentation-only baseline is insufficient.\n- Over-claiming generality without testing on held-out perturbation types — the key differentiator from augmentation is transfer to unseen perturbation types, so this MUST be demonstrated.\n- Testing only on GSM-level math — this repeats AbstRaL's limitation and loses the competition-math differentiator.\n- Ignoring clean accuracy — if MACR degrades unperturbed accuracy by >2 points, reviewers will question practicality.**\n\n## What counts as 'important'\n\nPrioritize (in order):\n1. **Best paper awards** at top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, etc.)\n2. **Oral / spotlight presentations** at these venues\n3. **Highly cited papers** (>50 citations in 1-2 years)\n4. **Papers that introduced widely-adopted methods** (e.g., new training paradigm, new benchmark)\n5. **Recent survey papers** that provide comprehensive field overviews\n6. **Strong recent work** from top labs (Google, Meta, DeepMind, OpenAI, CMU, Stanford, etc.)\n\n## Search strategy\n\nExecute AT LEAST 15 targeted searches:\n\n1. `best paper award ACL EMNLP NeurIPS ICML ICLR 2026 Target: AAAI 2026\nTrack: Machine Learning (ML) — Reinforcement Learning / Mathematical Reasoning\n\nDirection: RL-trained mathematical reasoning models exhibit 47-73% accuracy drops under trivial perturbations (numerical substitution, variable renaming) despite achieving SOTA on clean benchmarks. We propose Math-Aware Consistency Regularization (MACR): adding a JS-divergence consistency term between model outputs on original and mathematically-equivalent perturbed problems during GRPO training, with a complementary discrimination loss against surface-similar but semantically different problems. This adapts proven NLP consistency techniques (F²C, PPCL) to mathematical reasoning with math-equivalence-aware perturbation generation and RL integration — a combination no existing work provides.\n\nSeed Papers:\n- Mirzadeh et al., GSM-Symbolic (Apple, ICLR 2025) — documents up to 65% accuracy drops from single irrelevant clause; establishes that models pattern-match rather than reason\n- VAR-MATH (arXiv 2025) — most damning evidence: 47.9-72.9% drops for RL models on numerically re-parameterized competition math; directly motivates why RL training is the problem\n- Gao et al., AbstRaL (ICLR 2026) — only existing training-time intervention; uses abstraction not invariance; limited to GSM-level; our primary comparison baseline\n- Flip-Flop Consistency / F²C (arXiv 2024) — JS-divergence consistency for prompt perturbation robustness in NLP; proves the technique works but has never been adapted to math reasoning or RL\n- PPCL (EACL 2024) — KL-based consistency regularization recovering 59-69% of perturbation-induced drops in NLU; complementary theoretical grounding\n- CSR: Causal Consistency Regularization (arXiv 2025) — enforces causal faithfulness via operator-level interventions during SFT; closest methodological cousin but SFT-only and targets faithfulness not perturbation invariance\n- APRM (arXiv 2025) — adversarial PRM training on reasoning errors; shows PRM quality matters for downstream RL; motivates our perturbation-robust PRM extension\n\nKnown Gaps:\n- No work applies consistency regularization (JS/KL divergence across equivalent problem variants) during RL training for mathematical reasoning — F²C and PPCL remain NLP-only and SFT-only\n- No PRM has been trained to be robust to surface-form variations of equivalent problems — APRM addresses reasoning errors, not perturbation invariance\n- No training-time robustness intervention has been demonstrated on competition-level math (AIME/Putnam); AbstRaL is GSM-only\n\nTheoretical Anchor: Mathematical equivalence defines a natural invariance class — problems that differ only in surface form (variable names, specific numbers, phrasing) but share identical mathematical structure should produce identical solution distributions. RL training violates this invariance because the reward signal (correct/incorrect final answer) provides no gradient against surface-form-dependent reasoning. A consistency regularization term explicitly penalizes policy divergence across equivalent variants, forcing the model to learn representations that are invariant to mathematically irrelevant features. This is a direct instantiation of Invariant Risk Minimization principles in the RL-for-reasoning setting.\n\nConstraints:\n- Compute: ≤200 H100-hours (budget: 40h baseline GRPO + 90h method variants + 30h evaluation + 20h analysis + 20h buffer)\n- Models: Primary experiments on 7B (Qwen2.5-Math-7B); scaling verification on 14B\n- Evaluation: GSM-Symbolic, GSM-Plus, VAR-MATH (AMC23/AIME24/AIME25), MATH-Perturb; train-time perturbations (numerical substitution, variable renaming) held out from eval perturbations (distractor insertion, structural changes)\n\nQuality Self-Checks:\n- [x] Core insight: RL training optimizes for reward on fixed problem forms, creating surface-form dependencies that consistency regularization can break by enforcing invariance across equivalent variants.\n- [x] Why not obvious: Consistency regularization is well-known in NLP but requires math-aware equivalence-preserving perturbation generation (not just paraphrase) and RL integration (not just SFT) — two non-trivial adaptations that straddle communities.\n- [ ] Baseline fear test: A pure data-augmentation baseline (adding perturbed problems to RL training without consistency loss) could achieve substantial gains. The paper MUST include this baseline and show the consistency term provides additional benefit beyond augmentation. If the gap is <5%, the contribution is weak.\n- [x] Information exploited: Mathematical equivalence structure — the method uses symbolic verification that perturbations preserve the problem's mathematical structure, which pure augmentation or paraphrase-based consistency ignores.\n\nAvoid:\n- Framing this as 'just data augmentation with extra steps' — the consistency objective is the contribution, not the perturbation generation. Must clearly show augmentation-only baseline is insufficient.\n- Over-claiming generality without testing on held-out perturbation types — the key differentiator from augmentation is transfer to unseen perturbation types, so this MUST be demonstrated.\n- Testing only on GSM-level math — this repeats AbstRaL's limitation and loses the competition-math differentiator.\n- Ignoring clean accuracy — if MACR degrades unperturbed accuracy by >2 points, reviewers will question practicality.`\n2. `oral spotlight {venue} 2026 {topic}` — for each major venue\n3. `site:openreview.net {topic} 2026 outstanding` — OpenReview 高分论文\n4. `{topic} survey 2026` 或 `{topic} survey 2025` — 综述论文\n5. `site:arxiv.org {topic} 2026` — arXiv 最新高引\n6. `most cited {topic} 2025 2026` — Google Scholar\n7. `site:paperswithcode.com {task} SOTA` — SOTA 排行榜上的论文\n8. `{topic} benchmark {year}` — 定义领域的 benchmark 论文\n9. 对每个找到的重要论文，搜索其 cited-by 发现后续工作\n\nFor EVERY paper you find, use WebFetch to read its abstract and introduction on arXiv or OpenReview. Do NOT rely on search snippets alone — you need to understand what each paper actually does.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Full paper title\",\n  \"authors\": \"First author et al.\",\n  \"venue\": \"EMNLP 2025 / NeurIPS 2024 / arXiv 2025 / ...\",\n  \"url\": \"https://arxiv.org/abs/... or openreview URL\",\n  \"why_important\": \"Best paper / Oral / High-cited / Introduced X / ...\",\n  \"one_line_summary\": \"What this paper does in one sentence\"\n}\n\nFind at least 15 papers. More is better if they are genuinely relevant.\nIMPORTANT: You MUST end your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T05:23:25.077Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T05:23:25.077Z",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-29T05:23:25.096Z_

You are a senior ML researcher conducting a comprehensive literature survey.

**Today's date: 2026-05-29 (UTC).**

## Task
Find the **15 most important recent papers** (published 2024–2026) in or closely related to the following research area:

**Target: AAAI 2026
Track: Machine Learning (ML) — Reinforcement Learning / Mathematical Reasoning

Direction: RL-trained mathematical reasoning models exhibit 47-73% accuracy drops under trivial perturbations (numerical substitution, variable renaming) despite achieving SOTA on clean benchmarks. We propose Math-Aware Consistency Regularization (MACR): adding a JS-divergence consistency term between model outputs on original and mathematically-equivalent perturbed problems during GRPO training, with a complementary discrimination loss against surface-similar but semantically different problems. This adapts proven NLP consistency techniques (F²C, PPCL) to mathematical reasoning with math-equivalence-aware perturbation generation and RL integration — a combination no existing work provides.

Seed Papers:
- Mirzadeh et al., GSM-Symbolic (Apple, ICLR 2025) — documents up to 65% accuracy drops from single irrelevant clause; establishes that models pattern-match rather than reason
- VAR-MATH (arXiv 2025) — most damning evidence: 47.9-72.9% drops for RL models on numerically re-parameterized competition math; directly motivates why RL training is the problem
- Gao et al., AbstRaL (ICLR 2026) — only existing training-time intervention; uses abstraction not invariance; limited to GSM-level; our primary comparison baseline
- Flip-Flop Consistency / F²C (arXiv 2024) — JS-divergence consistency for prompt perturbation robustness in NLP; proves the technique works but has never been adapted to math reasoning or RL
- PPCL (EACL 2024) — KL-based consistency regularization recovering 59-69% of perturbation-induced drops in NLU; complementary theoretical grounding
- CSR: Causal Consistency Regularization (arXiv 2025) — enforces causal faithfulness via operator-level interventions during SFT; closest methodological cousin but SFT-only and targets faithfulness not perturbation invariance
- APRM (arXiv 2025) — adversarial PRM training on reasoning errors; shows PRM quality matters for downstream RL; motivates our perturbation-robust PRM extension

Known Gaps:
- No work applies consistency regularization (JS/KL divergence across equivalent problem variants) during RL training for mathematical reasoning — F²C and PPCL remain NLP-only and SFT-only
- No PRM has been trained to be robust to surface-form variations of equivalent problems — APRM addresses reasoning errors, not perturbation invariance
- No training-time robustness intervention has been demonstrated on competition-level math (AIME/Putnam); AbstRaL is GSM-only

Theoretical Anchor: Mathematical equivalence defines a natural invariance class — problems that differ only in surface form (variable names, specific numbers, phrasing) but share identical mathematical structure should produce identical solution distributions. RL training violates this invariance because the reward signal (correct/incorrect final answer) provides no gradient against surface-form-dependent reasoning. A consistency regularization term explicitly penalizes policy divergence across equivalent variants, forcing the model to learn representations that are invariant to mathematically irrelevant features. This is a direct instantiation of Invariant Risk Minimization principles in the RL-for-reasoning setting.

Constraints:
- Compute: ≤200 H100-hours (budget: 40h baseline GRPO + 90h method variants + 30h evaluation + 20h analysis + 20h buffer)
- Models: Primary experiments on 7B (Qwen2.5-Math-7B); scaling verification on 14B
- Evaluation: GSM-Symbolic, GSM-Plus, VAR-MATH (AMC23/AIME24/AIME25), MATH-Perturb; train-time perturbations (numerical substitution, variable renaming) held out from eval perturbations (distractor insertion, structural changes)

Quality Self-Checks:
- [x] Core insight: RL training optimizes for reward on fixed problem forms, creating surface-form dependencies that consistency regularization can break by enforcing invariance across equivalent variants.
- [x] Why not obvious: Consistency regularization is well-known in NLP but requires math-aware equivalence-preserving perturbation generation (not just paraphrase) and RL integration (not just SFT) — two non-trivial adaptations that straddle communities.
- [ ] Baseline fear test: A pure data-augmentation baseline (adding perturbed problems to RL training without consistency loss) could achieve substantial gains. The paper MUST include this baseline and show the consistency term provides additional benefit beyond augmentation. If the gap is <5%, the contribution is weak.
- [x] Information exploited: Mathematical equivalence structure — the method uses symbolic verification that perturbations preserve the problem's mathematical structure, which pure augmentation or paraphrase-based consistency ignores.

Avoid:
- Framing this as 'just data augmentation with extra steps' — the consistency objective is the contribution, not the perturbation generation. Must clearly show augmentation-only baseline is insufficient.
- Over-claiming generality without testing on held-out perturbation types — the key differentiator from augmentation is transfer to unseen perturbation types, so this MUST be demonstrated.
- Testing only on GSM-level math — this repeats AbstRaL's limitation and loses the competition-math differentiator.
- Ignoring clean accuracy — if MACR degrades unperturbed accuracy by >2 points, reviewers will question practicality.**

## What counts as 'important'

Prioritize (in order):
1. **Best paper awards** at top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, AAAI, etc.)
2. **Oral / spotlight presentations** at these venues
3. **Highly cited papers** (>50 citations in 1-2 years)
4. **Papers that introduced widely-adopted methods** (e.g., new training paradigm, new benchmark)
5. **Recent survey papers** that provide comprehensive field overviews
6. **Strong recent work** from top labs (Google, Meta, DeepMind, OpenAI, CMU, Stanford, etc.)

## Search strategy

Execute AT LEAST 15 targeted searches:

1. `best paper award ACL EMNLP NeurIPS ICML ICLR 2026 Target: AAAI 2026
Track: Machine Learning (ML) — Reinforcement Learning / Mathematical Reasoning

Direction: RL-trained mathematical reasoning models exhibit 47-73% accuracy drops under trivial perturbations (numerical substitution, variable renaming) despite achieving SOTA on clean benchmarks. We propose Math-Aware Consistency Regularization (MACR): adding a JS-divergence consistency term between model outputs on original and mathematically-equivalent perturbed problems during GRPO training, with a complementary discrimination loss against surface-similar but semantically different problems. This adapts proven NLP consistency techniques (F²C, PPCL) to mathematical reasoning with math-equivalence-aware perturbation generation and RL integration — a combination no existing work provides.

Seed Papers:
- Mirzadeh et al., GSM-Symbolic (Apple, ICLR 2025) — documents up to 65% accuracy drops from single irrelevant clause; establishes that models pattern-match rather than reason
- VAR-MATH (arXiv 2025) — most damning evidence: 47.9-72.9% drops for RL models on numerically re-parameterized competition math; directly motivates why RL training is the problem
- Gao et al., AbstRaL (ICLR 2026) — only existing training-time intervention; uses abstraction not invariance; limited to GSM-level; our primary comparison baseline
- Flip-Flop Consistency / F²C (arXiv 2024) — JS-divergence consistency for prompt perturbation robustness in NLP; proves the technique works but has never been adapted to math reasoning or RL
- PPCL (EACL 2024) — KL-based consistency regularization recovering 59-69% of perturbation-induced drops in NLU; complementary theoretical grounding
- CSR: Causal Consistency Regularization (arXiv 2025) — enforces causal faithfulness via operator-level interventions during SFT; closest methodological cousin but SFT-only and targets faithfulness not perturbation invariance
- APRM (arXiv 2025) — adversarial PRM training on reasoning errors; shows PRM quality matters for downstream RL; motivates our perturbation-robust PRM extension

Known Gaps:
- No work applies consistency regularization (JS/KL divergence across equivalent problem variants) during RL training for mathematical reasoning — F²C and PPCL remain NLP-only and SFT-only
- No PRM has been trained to be robust to surface-form variations of equivalent problems — APRM addresses reasoning errors, not perturbation invariance
- No training-time robustness intervention has been demonstrated on competition-level math (AIME/Putnam); AbstRaL is GSM-only

Theoretical Anchor: Mathematical equivalence defines a natural invariance class — problems that differ only in surface form (variable names, specific numbers, phrasing) but share identical mathematical structure should produce identical solution distributions. RL training violates this invariance because the reward signal (correct/incorrect final answer) provides no gradient against surface-form-dependent reasoning. A consistency regularization term explicitly penalizes policy divergence across equivalent variants, forcing the model to learn representations that are invariant to mathematically irrelevant features. This is a direct instantiation of Invariant Risk Minimization principles in the RL-for-reasoning setting.

Constraints:
- Compute: ≤200 H100-hours (budget: 40h baseline GRPO + 90h method variants + 30h evaluation + 20h analysis + 20h buffer)
- Models: Primary experiments on 7B (Qwen2.5-Math-7B); scaling verification on 14B
- Evaluation: GSM-Symbolic, GSM-Plus, VAR-MATH (AMC23/AIME24/AIME25), MATH-Perturb; train-time perturbations (numerical substitution, variable renaming) held out from eval perturbations (distractor insertion, structural changes)

Quality Self-Checks:
- [x] Core insight: RL training optimizes for reward on fixed problem forms, creating surface-form dependencies that consistency regularization can break by enforcing invariance across equivalent variants.
- [x] Why not obvious: Consistency regularization is well-known in NLP but requires math-aware equivalence-preserving perturbation generation (not just paraphrase) and RL integration (not just SFT) — two non-trivial adaptations that straddle communities.
- [ ] Baseline fear test: A pure data-augmentation baseline (adding perturbed problems to RL training without consistency loss) could achieve substantial gains. The paper MUST include this baseline and show the consistency term provides additional benefit beyond augmentation. If the gap is <5%, the contribution is weak.
- [x] Information exploited: Mathematical equivalence structure — the method uses symbolic verification that perturbations preserve the problem's mathematical structure, which pure augmentation or paraphrase-based consistency ignores.

Avoid:
- Framing this as 'just data augmentation with extra steps' — the consistency objective is the contribution, not the perturbation generation. Must clearly show augmentation-only baseline is insufficient.
- Over-claiming generality without testing on held-out perturbation types — the key differentiator from augmentation is transfer to unseen perturbation types, so this MUST be demonstrated.
- Testing only on GSM-level math — this repeats AbstRaL's limitation and loses the competition-math differentiator.
- Ignoring clean accuracy — if MACR degrades unperturbed accuracy by >2 points, reviewers will question practicality.`
2. `oral spotlight {venue} 2026 {topic}` — for each major venue
3. `site:openreview.net {topic} 2026 outstanding` — OpenReview 高分论文
4. `{topic} survey 2026` 或 `{topic} survey 2025` — 综述论文
5. `site:arxiv.org {topic} 2026` — arXiv 最新高引
6. `most cited {topic} 2025 2026` — Google Scholar
7. `site:paperswithcode.com {task} SOTA` — SOTA 排行榜上的论文
8. `{topic} benchmark {year}` — 定义领域的 benchmark 论文
9. 对每个找到的重要论文，搜索其 cited-by 发现后续工作

For EVERY paper you find, use WebFetch to read its abstract and introduction on arXiv or OpenReview. Do NOT rely on search snippets alone — you need to understand what each paper actually does.

## Output format

Output a JSON array. Each element:
{
  "title": "Full paper title",
  "authors": "First author et al.",
  "venue": "EMNLP 2025 / NeurIPS 2024 / arXiv 2025 / ...",
  "url": "https://arxiv.org/abs/... or openreview URL",
  "why_important": "Best paper / Oral / High-cited / Introduced X / ...",
  "one_line_summary": "What this paper does in one sentence"
}

Find at least 15 papers. More is better if they are genuinely relevant.
IMPORTANT: You MUST end your response with the JSON array.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "1e710e2b-1087-47bf-b32b-3c7b19e507c4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T05:23:25.095Z_

```json
{
  "parentUuid": "1e710e2b-1087-47bf-b32b-3c7b19e507c4",
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
  "uuid": "af5cc014-a0f4-47c4-8612-fb4e034061e7",
  "timestamp": "2026-05-29T05:23:25.095Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T05:23:25.095Z_

```json
{
  "parentUuid": "af5cc014-a0f4-47c4-8612-fb4e034061e7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3059f36e-e061-4131-87a0-2d2b4152cecd",
  "timestamp": "2026-05-29T05:23:25.095Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
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
  "aiTitle": "Conduct literature survey on RL math reasoning robustness",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Assistant

_source line 7 · 2026-05-29T05:23:30.996Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to conduct a comprehensive literature survey finding the 15 most important recent papers (2024-2026) related to their research direction on RL-trained mathematical reasoning models and consistency regularization. Let me break this down into parallel search tasks.

I need to search for papers across several dimensions:
1. Mathematical reasoning robustness/perturbation
2. RL for mathematical reasoning (GRPO, PPO, etc.)
3. Consistency regularization in NLP/ML
4. Process reward models
5. LLM reasoning benchmarks
6. Invariant risk minimization for LLMs


I'll initiate parallel searches across these different research areas to efficiently gather the most relevant papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3059f36e-e061-4131-87a0-2d2b4152cecd",
  "isSidechain": false,
  "requestId": "req_011CbWJS7tmNp8DHJFHZLY5P",
  "type": "assistant",
  "uuid": "877c703d-2cfe-4363-8d77-fe7e64ba5c94",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wTVNVWvJTKZ3XjMwid743",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15730,
      "cache_read_input_tokens": 0,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15730,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15730
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

_source line 8 · 2026-05-29T05:23:30.999Z_

I'll conduct this comprehensive literature survey by launching multiple parallel search agents covering different aspects of your research direction. Let me first load the WebSearch and WebFetch tools, then dispatch targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "877c703d-2cfe-4363-8d77-fe7e64ba5c94",
  "isSidechain": false,
  "requestId": "req_011CbWJS7tmNp8DHJFHZLY5P",
  "type": "assistant",
  "uuid": "69505c8d-2960-4d92-b0e4-b2a3f0bacc90",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wTVNVWvJTKZ3XjMwid743",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15730,
      "cache_read_input_tokens": 0,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15730,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15730
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

_source line 9 · 2026-05-29T05:23:31.234Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WEEU8TfGV5tmS3JkJMLQe6`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "69505c8d-2960-4d92-b0e4-b2a3f0bacc90",
  "isSidechain": false,
  "requestId": "req_011CbWJS7tmNp8DHJFHZLY5P",
  "type": "assistant",
  "uuid": "5a9f776b-fc6c-4e3e-bb1c-8af61fde2490",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019wTVNVWvJTKZ3XjMwid743",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15730,
      "cache_read_input_tokens": 0,
      "output_tokens": 288,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15730,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 288,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15730,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15730
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

_source line 10 · 2026-05-29T05:23:31.242Z_

<details><summary>↩ Tool result · `toolu_01WEEU8TfGV5tmS3JkJMLQe6`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a9f776b-fc6c-4e3e-bb1c-8af61fde2490",
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "4c1aa3c6-b01c-4c85-a044-b29f535acf66",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "5a9f776b-fc6c-4e3e-bb1c-8af61fde2490",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
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
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "4c1aa3c6-b01c-4c85-a044-b29f535acf66",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct literature survey on RL math reasoning robustness",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Assistant

_source line 13 · 2026-05-29T05:23:37.142Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have WebSearch and WebFetch available. Let me launch multiple parallel search agents to cover the different dimensions of this literature survey. I'll organize them by topic area to ensure comprehensive coverage.

Let me dispatch several agents in parallel to search for papers across different dimensions:

1. Mathematical reasoning robustness & perturbation benchmarks
2. RL for mathematical reasoning (GRPO, PPO, DeepSeek-R1, etc.)
3. Consistency regularization in NLP/ML
4. Process reward models (PRM)
5. Best paper awards at top venues 2024-2026
6. Invariant learning / data augmentation for reasoning


Launching the parallel searches now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c1aa3c6-b01c-4c85-a044-b29f535acf66",
  "isSidechain": false,
  "requestId": "req_011CbWJSZvgVeUUmhDyfUE53",
  "type": "assistant",
  "uuid": "629fc3ef-e3cf-44ee-a26a-da5809605005",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASMuHW4AHBNNu1Y18gNXXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 15730,
      "output_tokens": 2471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2471,
          "cache_read_input_tokens": 15730,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 14 · 2026-05-29T05:23:37.145Z_

Now let me launch parallel search agents to cover all dimensions of this survey comprehensively.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "629fc3ef-e3cf-44ee-a26a-da5809605005",
  "isSidechain": false,
  "requestId": "req_011CbWJSZvgVeUUmhDyfUE53",
  "type": "assistant",
  "uuid": "78548e30-0883-4b69-bb6b-c52bf7b4290a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASMuHW4AHBNNu1Y18gNXXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 15730,
      "output_tokens": 2471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2471,
          "cache_read_input_tokens": 15730,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 15 · 2026-05-29T05:23:43.338Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TxEWRrPKqdU1xhLHMJQ5Y2`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search: Math reasoning robustness",
  "prompt": "You are helping with a literature survey on RL-trained mathematical reasoning robustness. Search for the most important papers (2024-2026) on:\n\n1. Mathematical reasoning robustness under perturbation (numerical substitution, variable renaming, distractor insertion)\n2. Benchmarks measuring LLM math reasoning fragility (GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, etc.)\n3. Training-time interventions for math reasoning robustness\n\nExecute these searches and for EVERY promising paper, fetch its arXiv abstract:\n\nSearch 1: \"mathematical reasoning robustness perturbation LLM 2025 2026\"\nSearch 2: \"GSM-Symbolic GSM-Plus VAR-MATH benchmark math reasoning fragility\"\nSearch 3: \"math reasoning LLM accuracy drop perturbation numerical substitution\"\nSearch 4: \"MATH-Perturb benchmark mathematical reasoning evaluation robustness\"\nSearch 5: \"training robustness mathematical reasoning language model 2025\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Focus on papers that are highly cited or from top venues."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78548e30-0883-4b69-bb6b-c52bf7b4290a",
  "isSidechain": false,
  "requestId": "req_011CbWJSZvgVeUUmhDyfUE53",
  "type": "assistant",
  "uuid": "8f8f0406-7775-4bae-a236-9bf2e6c75194",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASMuHW4AHBNNu1Y18gNXXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 15730,
      "output_tokens": 2471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2471,
          "cache_read_input_tokens": 15730,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 16 · 2026-05-29T05:23:49.051Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01B7A1Wfkvop5qwRwy91H3Bw`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search: RL for math reasoning",
  "prompt": "You are helping with a literature survey on reinforcement learning for mathematical reasoning. Search for the most important papers (2024-2026) on:\n\n1. GRPO (Group Relative Policy Optimization) for math reasoning\n2. RL training for mathematical reasoning (DeepSeek-R1, OpenAI o1/o3 related work)\n3. PPO/RLHF applied to mathematical problem solving\n4. Reward modeling for math (process reward models, outcome reward models)\n\nExecute these searches and for EVERY promising paper, fetch its arXiv abstract:\n\nSearch 1: \"GRPO group relative policy optimization mathematical reasoning 2025 2026\"\nSearch 2: \"DeepSeek-R1 reinforcement learning reasoning 2025\"\nSearch 3: \"reinforcement learning mathematical reasoning training 2025 2026\"\nSearch 4: \"process reward model mathematical reasoning 2024 2025\"\nSearch 5: \"RLHF math reasoning chain of thought 2025\"\nSearch 6: \"adversarial process reward model APRM reasoning errors 2025\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Focus on papers that are highly cited, have best paper awards, or introduced widely-adopted methods (like GRPO, DeepSeek-R1, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f8f0406-7775-4bae-a236-9bf2e6c75194",
  "isSidechain": false,
  "requestId": "req_011CbWJSZvgVeUUmhDyfUE53",
  "type": "assistant",
  "uuid": "385b02db-cb56-4b0f-b0ff-1fff169ff965",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASMuHW4AHBNNu1Y18gNXXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 15730,
      "output_tokens": 2471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2471,
          "cache_read_input_tokens": 15730,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 17 · 2026-05-29T05:23:54.829Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012vc1PRdNP4dLW875E7Fs6y`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search: Consistency regularization NLP",
  "prompt": "You are helping with a literature survey on consistency regularization techniques in NLP and their potential application to mathematical reasoning. Search for the most important papers (2024-2026) on:\n\n1. Consistency regularization for LLM robustness (JS divergence, KL divergence)\n2. F²C / Flip-Flop Consistency for prompt perturbation robustness\n3. PPCL - perturbation consistency learning\n4. Causal consistency regularization for reasoning\n5. Invariant risk minimization for language models\n6. Data augmentation vs consistency training for NLP robustness\n\nExecute these searches and for EVERY promising paper, fetch its arXiv abstract:\n\nSearch 1: \"consistency regularization language model robustness perturbation 2024 2025\"\nSearch 2: \"Flip-Flop Consistency F2C prompt perturbation JS divergence\"\nSearch 3: \"PPCL perturbation consistency regularization NLU 2024\"\nSearch 4: \"causal consistency regularization reasoning faithfulness 2025\"\nSearch 5: \"invariant risk minimization language model reasoning 2025 2026\"\nSearch 6: \"consistency training data augmentation robustness LLM 2025\"\nSearch 7: \"AbstRaL abstract reasoning reinforcement learning math 2025 2026\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Focus on papers from top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, EACL)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "385b02db-cb56-4b0f-b0ff-1fff169ff965",
  "isSidechain": false,
  "requestId": "req_011CbWJSZvgVeUUmhDyfUE53",
  "type": "assistant",
  "uuid": "e61872b9-2d54-40d1-b34d-458f63602f49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASMuHW4AHBNNu1Y18gNXXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 15730,
      "output_tokens": 2471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2471,
          "cache_read_input_tokens": 15730,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 18 · 2026-05-29T05:24:01.610Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HmFFtHqEr9GPki79YHAwSF`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search: Best papers & awards 2024-2026",
  "prompt": "You are helping with a literature survey on mathematical reasoning and RL for LLMs. Search for best paper awards and outstanding papers at top venues (2024-2026) that are related to:\n- Mathematical reasoning in LLMs\n- Reinforcement learning for reasoning\n- Robustness of LLM reasoning\n- Consistency/invariance in neural networks\n\nExecute these searches:\n\nSearch 1: \"best paper award NeurIPS 2025 mathematical reasoning\"\nSearch 2: \"best paper award ICML 2025 reinforcement learning reasoning\"\nSearch 3: \"best paper award ICLR 2025 2026 mathematical reasoning LLM\"\nSearch 4: \"outstanding paper NeurIPS ICML 2025 reasoning robustness\"\nSearch 5: \"oral spotlight ICLR 2026 mathematical reasoning\"\nSearch 6: \"best paper ACL EMNLP 2025 reasoning consistency\"\nSearch 7: site:openreview.net \"ICLR 2026\" \"mathematical reasoning\" \"reinforcement learning\"\nSearch 8: \"Qwen2.5-Math training mathematical reasoning 2025\"\nSearch 9: \"most cited mathematical reasoning LLM paper 2025\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Prioritize best paper winners and oral/spotlight presentations."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e61872b9-2d54-40d1-b34d-458f63602f49",
  "isSidechain": false,
  "requestId": "req_011CbWJSZvgVeUUmhDyfUE53",
  "type": "assistant",
  "uuid": "9c4c6224-dad8-42ee-8516-8db6756c6dcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASMuHW4AHBNNu1Y18gNXXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 15730,
      "output_tokens": 2471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2471,
          "cache_read_input_tokens": 15730,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 19 · 2026-05-29T05:24:06.544Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UTPHSY2psshZr3F12GSjVv`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search: Data augmentation & invariance math",
  "prompt": "You are helping with a literature survey. Search for the most important papers (2024-2026) on:\n\n1. Data augmentation for mathematical reasoning training\n2. Invariance learning for reasoning models\n3. Perturbation-based training for LLM reasoning robustness\n4. Contrastive learning for mathematical reasoning\n5. Self-consistency and verification in math reasoning\n\nExecute these searches:\n\nSearch 1: \"data augmentation mathematical reasoning LLM training 2025 2026\"\nSearch 2: \"self-consistency mathematical reasoning verification 2024 2025\"\nSearch 3: \"contrastive learning mathematical reasoning robustness 2025\"\nSearch 4: \"symbolic perturbation math problem generation training 2025\"\nSearch 5: \"math word problem augmentation robustness training 2025\"\nSearch 6: \"reasoning invariance surface form LLM 2025\"\nSearch 7: \"test-time compute scaling mathematical reasoning 2025\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Focus on highly cited papers and those from top venues."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c4c6224-dad8-42ee-8516-8db6756c6dcb",
  "isSidechain": false,
  "requestId": "req_011CbWJSZvgVeUUmhDyfUE53",
  "type": "assistant",
  "uuid": "4bbdc5bf-35da-4fb9-bc0c-5f68bdd39e1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASMuHW4AHBNNu1Y18gNXXn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1308,
      "cache_read_input_tokens": 15730,
      "output_tokens": 2471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1308,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2471,
          "cache_read_input_tokens": 15730,
          "cache_creation_input_tokens": 1308,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1308
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

_source line 20 · 2026-05-29T05:26:09.236Z_

<details><summary>↩ Tool result · `toolu_01TxEWRrPKqdU1xhLHMJQ5Y2`</summary>

```text
I now have a comprehensive collection. Let me compile the final report with all the papers organized by category.

---

Here is the literature survey with 13 distinct papers covering RL-trained mathematical reasoning robustness (2024--2026).

---

## CATEGORY 1: Benchmarks Measuring LLM Math Reasoning Fragility

### 1. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

- **Authors:** Iman Mirzadeh et al. (Apple)
- **Venue/Year:** ICLR 2025
- **URL:** https://arxiv.org/abs/2410.05229
- **What it does:** Introduces GSM-Symbolic, a benchmark using symbolic templates to generate diverse instantiations of grade-school math problems. Shows that all models' performance declines when only numerical values change, and adding a single irrelevant-but-plausible clause causes accuracy drops up to 65%, suggesting LLMs replicate memorized reasoning patterns rather than performing genuine logical reasoning.
- **Why it's important:** Published at ICLR 2025 (top venue). One of the most widely cited papers on math reasoning fragility. Originated from Apple ML Research. Established the template-based perturbation methodology that many subsequent papers build upon.

### 2. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers

- **Authors:** Qintong Li et al.
- **Venue/Year:** ACL 2024
- **URL:** https://arxiv.org/abs/2402.19255
- **What it does:** Creates an augmented version of GSM8K with systematic mathematical perturbations (numerical variation, question target alteration, added statements). Tests 25 LLMs with 4 prompting techniques and finds up to 20% accuracy gaps between original and perturbed problems, while human performance is unaffected.
- **Why it's important:** Published at ACL 2024 (top NLP venue). One of the earliest systematic robustness benchmarks for math reasoning. Widely referenced as a baseline in subsequent work.

### 3. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations

- **Authors:** Kaixuan Huang et al. (Princeton, Google DeepMind)
- **Venue/Year:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.06453
- **What it does:** Constructs perturbations of level-5 (hardest) MATH problems in two categories: "simple" perturbations that preserve solution structure and "hard" perturbations that fundamentally change problem nature. Finds o1-mini drops 16.49% and gemini-2.0-flash-thinking drops 12.9% on hard perturbations. Identifies a novel memorization pattern where models blindly apply learned solution strategies without checking applicability.
- **Why it's important:** First benchmark to distinguish simple vs. hard perturbations at competition-math difficulty. The "blind skill application" finding is a key insight for understanding RL-trained reasoners. Strong author team spanning Princeton and Google DeepMind.

### 4. VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks

- **Authors:** Jian Yao et al.
- **Venue/Year:** arXiv preprint, July 2025 (revised January 2026)
- **URL:** https://arxiv.org/abs/2507.12885
- **What it does:** Converts AMC23, AIME24, and AIME25 problems into parameterized templates and evaluates models on multiple numeric variants. RL-finetuned models show substantial performance declines averaging 47.9%, 58.8%, and 72.9% across those three suites, exposing that RL methods often rely on superficial heuristics rather than generalizable reasoning.
- **Why it's important:** Directly targets the question of whether RL training produces genuine reasoning or benchmark-specific pattern matching. The dramatic drops for RL-trained models (up to 72.9%) are among the largest reported in the literature.

### 5. PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning

- **Authors:** Yuren Hao et al.
- **Venue/Year:** arXiv preprint, August 2025
- **URL:** https://arxiv.org/abs/2508.08833
- **What it does:** Introduces the Generalization-and-Perturbation (GAP) framework and the 6,306-item PutnamGAP benchmark derived from all 1,051 Putnam Competition problems. OpenAI's O3 drops from 51.5% to 46.8% on surface-renamed variants and to 38.6% on parametric variants, revealing clear robustness gaps even in frontier models at competition-level difficulty.
- **Why it's important:** Largest-scale perturbation benchmark for competition mathematics. Tests at a much higher difficulty level than GSM-based benchmarks. Demonstrates that even the strongest reasoning models (O3) are not robust to meaning-preserving rewording.

### 6. Robust Reasoning Benchmark (RRB)

- **Authors:** Pavel Golikov et al.
- **Venue/Year:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2604.08571
- **What it does:** Applies a pipeline of 13 deterministic textual perturbations to AIME 2024 and 2025 problems. Finds frontier models are largely resilient, but open-weights reasoning models show accuracy drops up to 54%. Identifies "Intra-Query Attention Dilution" where solving multiple math problems sequentially degrades performance on later problems.
- **Why it's important:** Most recent benchmark (2026). Introduces the attention dilution concept, arguing future architectures need explicit contextual resets within chain-of-thought. Provides the most comprehensive perturbation taxonomy (13 types).

---

## CATEGORY 2: Analysis of Math Reasoning Fragility Mechanisms

### 7. Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models

- **Authors:** Zhishen Sun et al.
- **Venue/Year:** arXiv preprint, November 2025
- **URL:** https://arxiv.org/abs/2511.08022
- **What it does:** Proposes a perturbation framework with progressively intensifying "semantically irrelevant perturbation sentences." Models remain stable against non-numerical disruptions but collapse under numerical perturbations -- smaller models drop up to 51.55%, commercial models drop 3--10%. Finds models maintain 20--40% accuracy even without core instructions, confirming pattern-matching behavior.
- **Why it's important:** Key mechanistic finding: models are specifically fragile to irrelevant numerical information, not irrelevant textual information. The 20--40% accuracy-without-instructions result is a striking demonstration that models partially "know the answer pattern" before reading the problem.

### 8. Benchmarking Reasoning Robustness in Large Language Models (Math-RoB)

- **Authors:** Tong Yu et al.
- **Venue/Year:** arXiv preprint, March 2025
- **URL:** https://arxiv.org/abs/2503.04550
- **What it does:** Identifies four core vulnerabilities: positional bias, instruction sensitivity (5--7.5% drops), numerical fragility (GPT-4o drops from 97.5% to 82.5% on value substitution), and memory dependence (guessing when data is absent). Introduces Math-RoB, a benchmark exploiting hallucinations triggered by missing information.
- **Why it's important:** Provides the most systematic taxonomy of reasoning failure modes. The 15-point GPT-4o drop on simple value substitution is a striking result.

### 9. RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning

- **Authors:** Xinyuan Li et al.
- **Venue/Year:** arXiv preprint, November 2025 (revised January 2026)
- **URL:** https://arxiv.org/abs/2511.04120
- **What it does:** Uses Item Response Theory (IRT) with 35 LLMs as "test subjects" to build difficulty rankings, then uses RL to reformulate math problems at controlled difficulty levels. Testing on competition-level benchmarks shows an average 21.73% performance decrease across 26 models.
- **Why it's important:** Novel use of psychometric theory (IRT) to systematically calibrate perturbation difficulty. Bridges educational measurement theory with LLM evaluation.

### 10. MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning

- **Authors:** Neeraja Kirtane et al.
- **Venue/Year:** arXiv preprint, October 2025
- **URL:** https://arxiv.org/abs/2510.06430
- **What it does:** Evaluates 34 models on meaning-preserving linguistic rewording of high-school math problems (changing names, variables, context while keeping numerical structure identical). Smaller models show 9--11% drops; frontier models are more stable.
- **Why it's important:** Focuses specifically on linguistic (not numerical) perturbations, complementing numerical-perturbation studies. The large-scale evaluation (34 models) provides broad coverage.

---

## CATEGORY 3: Training-Time Interventions for Math Reasoning Robustness

### 11. AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking

- **Authors:** Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe
- **Venue/Year:** ICLR 2026
- **URL:** https://arxiv.org/abs/2506.07751
- **What it does:** Proposes reinforcement learning with granular abstraction data to promote abstract reasoning in smaller LLMs. Significantly mitigates performance degradation on GSM perturbation benchmarks and provides wider generalization benefits across mathematical and general reasoning tasks, demonstrating that "abstract thinking broadly enables better generalizability."
- **Why it's important:** Published at ICLR 2026 (top venue). One of the first papers showing a concrete training-time fix that improves robustness on perturbation benchmarks. Co-authored by Samy Bengio (also on GSM-Symbolic). Directly addresses the RL-for-robustness question.

### 12. LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning

- **Authors:** Zhen Hao Wong et al.
- **Venue/Year:** arXiv preprint, June 2025
- **URL:** https://arxiv.org/abs/2506.04821
- **What it does:** Trains models via RL on seven custom logic puzzles (constraint propagation, symbolic deduction) with binary correctness feedback. Significantly improves out-of-distribution performance on mathematical benchmarks, especially for mid-difficulty multi-step reasoning problems, while strengthening algebraic manipulation, geometric inference, and combinatorial logic.
- **Why it's important:** Demonstrates that RL training on non-math logic puzzles transfers to improved math robustness -- an important finding for training-time interventions.

### 13. Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (SPARKLE)

- **Authors:** Jiayu Wang et al.
- **Venue/Year:** NeurIPS 2025
- **URL:** https://arxiv.org/abs/2506.04723
- **What it does:** Introduces SPARKLE, a framework analyzing how RL improves LLM math reasoning along three dimensions: plan execution, knowledge integration, and problem-solving chains. Finds that explicit human-crafted step-by-step plans can surprisingly degrade performance on hard benchmarks, while RL-trained models show greater robustness. Introduces SparkleRL-PSS, a training pipeline reusing difficult problems via partial step scaffolding.
- **Why it's important:** Accepted at NeurIPS 2025 (top venue). Provides the deepest mechanistic understanding of why RL training improves reasoning robustness. The counterintuitive finding about explicit plans hurting performance has important implications for training methodology.

---

## Summary Table

| # | Paper | Venue | Category | Key Finding |
|---|-------|-------|----------|-------------|
| 1 | GSM-Symbolic | ICLR 2025 | Benchmark | Up to 65% drop from irrelevant clauses |
| 2 | GSM-Plus | ACL 2024 | Benchmark | Up to 20% gap on perturbations |
| 3 | MATH-Perturb | arXiv 2025 | Benchmark | 16.5% drop on hard perturbations (o1-mini) |
| 4 | VAR-MATH | arXiv 2025 | Benchmark | Up to 72.9% drop for RL-trained models |
| 5 | PutnamGAP | arXiv 2025 | Benchmark | O3 drops 12.9pp on parametric variants |
| 6 | RRB | arXiv 2026 | Benchmark | 13 perturbation types; 54% max drop |
| 7 | Numerical Sensitivity | arXiv 2025 | Analysis | Up to 51.55% drop from numerical distractors |
| 8 | Math-RoB | arXiv 2025 | Analysis | 4 vulnerability types; GPT-4o drops 15pp |
| 9 | RIDE | arXiv 2025 | Analysis | IRT-calibrated perturbations; 21.73% avg drop |
| 10 | MathRobust-LV | arXiv 2025 | Analysis | 9--11% drop from linguistic rewording |
| 11 | AbstRaL | ICLR 2026 | Training fix | RL + abstraction mitigates GSM fragility |
| 12 | LogicPuzzleRL | arXiv 2025 | Training fix | Logic puzzle RL transfers to math robustness |
| 13 | SPARKLE | NeurIPS 2025 | Training fix | Partial-step scaffolding RL improves robustness |

Three papers are from top venues (ICLR 2025, ACL 2024, NeurIPS 2025, ICLR 2026), providing strong publication-quality anchors for the survey. The remaining are recent arXiv preprints that collectively cover the full landscape from benchmarking fragility to training-time interventions.

agentId: a74cf45dec59802ec (use SendMessage with to: 'a74cf45dec59802ec' to continue this agent)
&lt;usage>total_tokens: 26707
tool_uses: 23
duration_ms: 145890&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f8f0406-7775-4bae-a236-9bf2e6c75194",
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "cca99958-f4a5-475d-8370-7f98e9b6c6aa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on RL-trained mathematical reasoning robustness. Search for the most important papers (2024-2026) on:\n\n1. Mathematical reasoning robustness under perturbation (numerical substitution, variable renaming, distractor insertion)\n2. Benchmarks measuring LLM math reasoning fragility (GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, etc.)\n3. Training-time interventions for math reasoning robustness\n\nExecute these searches and for EVERY promising paper, fetch its arXiv abstract:\n\nSearch 1: \"mathematical reasoning robustness perturbation LLM 2025 2026\"\nSearch 2: \"GSM-Symbolic GSM-Plus VAR-MATH benchmark math reasoning fragility\"\nSearch 3: \"math reasoning LLM accuracy drop perturbation numerical substitution\"\nSearch 4: \"MATH-Perturb benchmark mathematical reasoning evaluation robustness\"\nSearch 5: \"training robustness mathematical reasoning language model 2025\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Focus on papers that are highly cited or from top venues.",
    "agentId": "a74cf45dec59802ec",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive collection. Let me compile the final report with all the papers organized by category.\n\n---\n\nHere is the literature survey with 13 distinct papers covering RL-trained mathematical reasoning robustness (2024--2026).\n\n---\n\n## CATEGORY 1: Benchmarks Measuring LLM Math Reasoning Fragility\n\n### 1. GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\n\n- **Authors:** Iman Mirzadeh et al. (Apple)\n- **Venue/Year:** ICLR 2025\n- **URL:** https://arxiv.org/abs/2410.05229\n- **What it does:** Introduces GSM-Symbolic, a benchmark using symbolic templates to generate diverse instantiations of grade-school math problems. Shows that all models' performance declines when only numerical values change, and adding a single irrelevant-but-plausible clause causes accuracy drops up to 65%, suggesting LLMs replicate memorized reasoning patterns rather than performing genuine logical reasoning.\n- **Why it's important:** Published at ICLR 2025 (top venue). One of the most widely cited papers on math reasoning fragility. Originated from Apple ML Research. Established the template-based perturbation methodology that many subsequent papers build upon.\n\n### 2. GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers\n\n- **Authors:** Qintong Li et al.\n- **Venue/Year:** ACL 2024\n- **URL:** https://arxiv.org/abs/2402.19255\n- **What it does:** Creates an augmented version of GSM8K with systematic mathematical perturbations (numerical variation, question target alteration, added statements). Tests 25 LLMs with 4 prompting techniques and finds up to 20% accuracy gaps between original and perturbed problems, while human performance is unaffected.\n- **Why it's important:** Published at ACL 2024 (top NLP venue). One of the earliest systematic robustness benchmarks for math reasoning. Widely referenced as a baseline in subsequent work.\n\n### 3. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\n\n- **Authors:** Kaixuan Huang et al. (Princeton, Google DeepMind)\n- **Venue/Year:** arXiv preprint, February 2025\n- **URL:** https://arxiv.org/abs/2502.06453\n- **What it does:** Constructs perturbations of level-5 (hardest) MATH problems in two categories: \"simple\" perturbations that preserve solution structure and \"hard\" perturbations that fundamentally change problem nature. Finds o1-mini drops 16.49% and gemini-2.0-flash-thinking drops 12.9% on hard perturbations. Identifies a novel memorization pattern where models blindly apply learned solution strategies without checking applicability.\n- **Why it's important:** First benchmark to distinguish simple vs. hard perturbations at competition-math difficulty. The \"blind skill application\" finding is a key insight for understanding RL-trained reasoners. Strong author team spanning Princeton and Google DeepMind.\n\n### 4. VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks\n\n- **Authors:** Jian Yao et al.\n- **Venue/Year:** arXiv preprint, July 2025 (revised January 2026)\n- **URL:** https://arxiv.org/abs/2507.12885\n- **What it does:** Converts AMC23, AIME24, and AIME25 problems into parameterized templates and evaluates models on multiple numeric variants. RL-finetuned models show substantial performance declines averaging 47.9%, 58.8%, and 72.9% across those three suites, exposing that RL methods often rely on superficial heuristics rather than generalizable reasoning.\n- **Why it's important:** Directly targets the question of whether RL training produces genuine reasoning or benchmark-specific pattern matching. The dramatic drops for RL-trained models (up to 72.9%) are among the largest reported in the literature.\n\n### 5. PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning\n\n- **Authors:** Yuren Hao et al.\n- **Venue/Year:** arXiv preprint, August 2025\n- **URL:** https://arxiv.org/abs/2508.08833\n- **What it does:** Introduces the Generalization-and-Perturbation (GAP) framework and the 6,306-item PutnamGAP benchmark derived from all 1,051 Putnam Competition problems. OpenAI's O3 drops from 51.5% to 46.8% on surface-renamed variants and to 38.6% on parametric variants, revealing clear robustness gaps even in frontier models at competition-level difficulty.\n- **Why it's important:** Largest-scale perturbation benchmark for competition mathematics. Tests at a much higher difficulty level than GSM-based benchmarks. Demonstrates that even the strongest reasoning models (O3) are not robust to meaning-preserving rewording.\n\n### 6. Robust Reasoning Benchmark (RRB)\n\n- **Authors:** Pavel Golikov et al.\n- **Venue/Year:** arXiv preprint, March 2026\n- **URL:** https://arxiv.org/abs/2604.08571\n- **What it does:** Applies a pipeline of 13 deterministic textual perturbations to AIME 2024 and 2025 problems. Finds frontier models are largely resilient, but open-weights reasoning models show accuracy drops up to 54%. Identifies \"Intra-Query Attention Dilution\" where solving multiple math problems sequentially degrades performance on later problems.\n- **Why it's important:** Most recent benchmark (2026). Introduces the attention dilution concept, arguing future architectures need explicit contextual resets within chain-of-thought. Provides the most comprehensive perturbation taxonomy (13 types).\n\n---\n\n## CATEGORY 2: Analysis of Math Reasoning Fragility Mechanisms\n\n### 7. Numerical Sensitivity and Robustness: Exploring the Flaws of Mathematical Reasoning in Large Language Models\n\n- **Authors:** Zhishen Sun et al.\n- **Venue/Year:** arXiv preprint, November 2025\n- **URL:** https://arxiv.org/abs/2511.08022\n- **What it does:** Proposes a perturbation framework with progressively intensifying \"semantically irrelevant perturbation sentences.\" Models remain stable against non-numerical disruptions but collapse under numerical perturbations -- smaller models drop up to 51.55%, commercial models drop 3--10%. Finds models maintain 20--40% accuracy even without core instructions, confirming pattern-matching behavior.\n- **Why it's important:** Key mechanistic finding: models are specifically fragile to irrelevant numerical information, not irrelevant textual information. The 20--40% accuracy-without-instructions result is a striking demonstration that models partially \"know the answer pattern\" before reading the problem.\n\n### 8. Benchmarking Reasoning Robustness in Large Language Models (Math-RoB)\n\n- **Authors:** Tong Yu et al.\n- **Venue/Year:** arXiv preprint, March 2025\n- **URL:** https://arxiv.org/abs/2503.04550\n- **What it does:** Identifies four core vulnerabilities: positional bias, instruction sensitivity (5--7.5% drops), numerical fragility (GPT-4o drops from 97.5% to 82.5% on value substitution), and memory dependence (guessing when data is absent). Introduces Math-RoB, a benchmark exploiting hallucinations triggered by missing information.\n- **Why it's important:** Provides the most systematic taxonomy of reasoning failure modes. The 15-point GPT-4o drop on simple value substitution is a striking result.\n\n### 9. RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning\n\n- **Authors:** Xinyuan Li et al.\n- **Venue/Year:** arXiv preprint, November 2025 (revised January 2026)\n- **URL:** https://arxiv.org/abs/2511.04120\n- **What it does:** Uses Item Response Theory (IRT) with 35 LLMs as \"test subjects\" to build difficulty rankings, then uses RL to reformulate math problems at controlled difficulty levels. Testing on competition-level benchmarks shows an average 21.73% performance decrease across 26 models.\n- **Why it's important:** Novel use of psychometric theory (IRT) to systematically calibrate perturbation difficulty. Bridges educational measurement theory with LLM evaluation.\n\n### 10. MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning\n\n- **Authors:** Neeraja Kirtane et al.\n- **Venue/Year:** arXiv preprint, October 2025\n- **URL:** https://arxiv.org/abs/2510.06430\n- **What it does:** Evaluates 34 models on meaning-preserving linguistic rewording of high-school math problems (changing names, variables, context while keeping numerical structure identical). Smaller models show 9--11% drops; frontier models are more stable.\n- **Why it's important:** Focuses specifically on linguistic (not numerical) perturbations, complementing numerical-perturbation studies. The large-scale evaluation (34 models) provides broad coverage.\n\n---\n\n## CATEGORY 3: Training-Time Interventions for Math Reasoning Robustness\n\n### 11. AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking\n\n- **Authors:** Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe\n- **Venue/Year:** ICLR 2026\n- **URL:** https://arxiv.org/abs/2506.07751\n- **What it does:** Proposes reinforcement learning with granular abstraction data to promote abstract reasoning in smaller LLMs. Significantly mitigates performance degradation on GSM perturbation benchmarks and provides wider generalization benefits across mathematical and general reasoning tasks, demonstrating that \"abstract thinking broadly enables better generalizability.\"\n- **Why it's important:** Published at ICLR 2026 (top venue). One of the first papers showing a concrete training-time fix that improves robustness on perturbation benchmarks. Co-authored by Samy Bengio (also on GSM-Symbolic). Directly addresses the RL-for-robustness question.\n\n### 12. LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning\n\n- **Authors:** Zhen Hao Wong et al.\n- **Venue/Year:** arXiv preprint, June 2025\n- **URL:** https://arxiv.org/abs/2506.04821\n- **What it does:** Trains models via RL on seven custom logic puzzles (constraint propagation, symbolic deduction) with binary correctness feedback. Significantly improves out-of-distribution performance on mathematical benchmarks, especially for mid-difficulty multi-step reasoning problems, while strengthening algebraic manipulation, geometric inference, and combinatorial logic.\n- **Why it's important:** Demonstrates that RL training on non-math logic puzzles transfers to improved math robustness -- an important finding for training-time interventions.\n\n### 13. Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning (SPARKLE)\n\n- **Authors:** Jiayu Wang et al.\n- **Venue/Year:** NeurIPS 2025\n- **URL:** https://arxiv.org/abs/2506.04723\n- **What it does:** Introduces SPARKLE, a framework analyzing how RL improves LLM math reasoning along three dimensions: plan execution, knowledge integration, and problem-solving chains. Finds that explicit human-crafted step-by-step plans can surprisingly degrade performance on hard benchmarks, while RL-trained models show greater robustness. Introduces SparkleRL-PSS, a training pipeline reusing difficult problems via partial step scaffolding.\n- **Why it's important:** Accepted at NeurIPS 2025 (top venue). Provides the deepest mechanistic understanding of why RL training improves reasoning robustness. The counterintuitive finding about explicit plans hurting performance has important implications for training methodology.\n\n---\n\n## Summary Table\n\n| # | Paper | Venue | Category | Key Finding |\n|---|-------|-------|----------|-------------|\n| 1 | GSM-Symbolic | ICLR 2025 | Benchmark | Up to 65% drop from irrelevant clauses |\n| 2 | GSM-Plus | ACL 2024 | Benchmark | Up to 20% gap on perturbations |\n| 3 | MATH-Perturb | arXiv 2025 | Benchmark | 16.5% drop on hard perturbations (o1-mini) |\n| 4 | VAR-MATH | arXiv 2025 | Benchmark | Up to 72.9% drop for RL-trained models |\n| 5 | PutnamGAP | arXiv 2025 | Benchmark | O3 drops 12.9pp on parametric variants |\n| 6 | RRB | arXiv 2026 | Benchmark | 13 perturbation types; 54% max drop |\n| 7 | Numerical Sensitivity | arXiv 2025 | Analysis | Up to 51.55% drop from numerical distractors |\n| 8 | Math-RoB | arXiv 2025 | Analysis | 4 vulnerability types; GPT-4o drops 15pp |\n| 9 | RIDE | arXiv 2025 | Analysis | IRT-calibrated perturbations; 21.73% avg drop |\n| 10 | MathRobust-LV | arXiv 2025 | Analysis | 9--11% drop from linguistic rewording |\n| 11 | AbstRaL | ICLR 2026 | Training fix | RL + abstraction mitigates GSM fragility |\n| 12 | LogicPuzzleRL | arXiv 2025 | Training fix | Logic puzzle RL transfers to math robustness |\n| 13 | SPARKLE | NeurIPS 2025 | Training fix | Partial-step scaffolding RL improves robustness |\n\nThree papers are from top venues (ICLR 2025, ACL 2024, NeurIPS 2025, ICLR 2026), providing strong publication-quality anchors for the survey. The remaining are recent arXiv preprints that collectively cover the full landscape from benchmarking fragility to training-time interventions."
      }
    ],
    "totalDurationMs": 145890,
    "totalTokens": 26707,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 368,
      "cache_read_input_tokens": 22776,
      "output_tokens": 3562,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 368
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3562,
          "cache_read_input_tokens": 22776,
          "cache_creation_input_tokens": 368,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 368,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 23
    }
  },
  "sourceToolAssistantUUID": "8f8f0406-7775-4bae-a236-9bf2e6c75194",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "cca99958-f4a5-475d-8370-7f98e9b6c6aa",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct literature survey on RL math reasoning robustness",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Tool result

_source line 23 · 2026-05-29T05:26:22.940Z_

<details><summary>↩ Tool result · `toolu_01UTPHSY2psshZr3F12GSjVv`</summary>

```text
Now I have enough material for a comprehensive report. Here is the literature survey:

---

## Literature Survey: Data Augmentation, Invariance, and Robustness for LLM Mathematical Reasoning (2024-2026)

### Paper 1: GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models

- **Authors:** Mirzadeh et al. (Apple)
- **Venue/Year:** ICLR 2025 (published as conference paper)
- **URL:** https://arxiv.org/abs/2410.05229
- **What it does:** Introduces GSM-Symbolic, a benchmark built from symbolic templates that generate diverse instantiations of the same math problem (varying names, numbers, structure). Reveals that LLMs show noticeable variance across instantiations, with performance drops up to 65% when irrelevant "No-Op" clauses are added, suggesting pattern matching rather than genuine reasoning.
- **Why it's important:** Published at ICLR 2025 (top venue), from Apple ML Research. This paper became a landmark reference for the "reasoning robustness" debate. It has generated significant follow-up work and controversy -- subsequent 2026 re-evaluations with frontier models suggest the effect diminishes on cleaner data, but the benchmark methodology (symbolic templates for controlled evaluation) has been widely adopted.

---

### Paper 2: MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations

- **Authors:** Huang, Guo, Li, Ji, Ge, Li, Guo, Cai, Yuan, Wang, Wu, Yin, Tang, Huang, Jin, Chen, Zhang, and Wang
- **Venue/Year:** arXiv preprint, February 2025
- **URL:** https://arxiv.org/abs/2502.06453
- **What it does:** Constructs MATH-P-Simple and MATH-P-Hard, 279 perturbed versions of the hardest MATH dataset problems. Perturbations include adding conditions, changing problem structure, and altering constraints. Demonstrates significant drops even on frontier models: o1-mini (-16.49%), gemini-2.0-flash-thinking (-12.9%). Identifies a memorization pattern where models apply problem-solving techniques without evaluating relevance to modifications.
- **Why it's important:** Extends the GSM-Symbolic line of work to competition-level math (MATH level 5). The large author list includes researchers from Princeton and Google DeepMind. Provides concrete evidence that even advanced reasoning models are brittle to structural perturbations, not just superficial changes.

---

### Paper 3: Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning in Large Language Models

- **Authors:** Zhou, Zhu, Antognini, Kim, and Zhang
- **Venue/Year:** NAACL 2024 (main conference)
- **URL:** https://arxiv.org/abs/2404.11500
- **What it does:** Investigates how surface-level rephrasing of math problems (without changing semantics) impacts LLM solve rates -- finding swings from 5% to 100% on the same problem. Proposes Self-Consistency-over-Paraphrases (SCoP), which generates multiple paraphrased versions of a problem and aggregates answers, outperforming standard self-consistency (majority voting).
- **Why it's important:** Published at NAACL 2024, a top NLP venue. Directly demonstrates that reasoning is not invariant to surface form and provides a practical method (SCoP) to exploit this for improved accuracy. This is a foundational reference for the "surface form sensitivity" problem in math reasoning.

---

### Paper 4: DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning

- **Authors:** Shao, Luo, Lu, Ren, Hu, Ye, Gou, Ma, and Zhang (DeepSeek)
- **Venue/Year:** arXiv, November 2025
- **URL:** https://arxiv.org/abs/2511.22570
- **What it does:** Trains an LLM-based verifier for theorem proving and uses it as a reward model for a proof generator. The generator is incentivized to identify and fix issues in its own proofs. Introduces scaled verification compute to automatically label hard-to-verify proofs as new training data. Achieves gold-level scores on IMO 2025 and CMO 2024, and 118/120 on Putnam 2024 (surpassing the highest human score of 90).
- **Why it's important:** State-of-the-art results on premiere mathematical competitions. The self-verification loop (generator + verifier co-training) represents a major advance in self-consistency for mathematical reasoning. From DeepSeek, one of the most influential labs in reasoning model development. The Putnam result (exceeding all human participants) is a milestone.

---

### Paper 5: s1: Simple Test-Time Scaling

- **Authors:** Muennighoff, Yang, Shi, Li, Fei-Fei, Hajishirzi, Zettlemoyer, Liang, Candes, and Hashimoto
- **Venue/Year:** EMNLP 2025
- **URL:** https://arxiv.org/abs/2501.19393
- **What it does:** Demonstrates that test-time scaling can be achieved simply: (1) curate 1,000 high-quality questions emphasizing difficulty, diversity, and quality; (2) fine-tune Qwen2.5-32B-Instruct on this data; (3) use "budget forcing" to control reasoning length (forcibly terminating or extending thinking via appending "Wait" tokens). The resulting model exceeds o1-preview on competition math by up to 27% (MATH, AIME24). Scaling from 50% to 57% on AIME24 through budget forcing alone.
- **Why it's important:** Published at EMNLP 2025, with an author list spanning Stanford, UW, and other top institutions. The paper is notable for its simplicity and reproducibility -- model, data, and code are fully open-source. It demonstrated that test-time compute scaling does not require massive proprietary infrastructure. Highly cited and widely reproduced.

---

### Paper 6: Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning

- **Authors:** Liu, Ye, Ma, Chou, and Yuille (Johns Hopkins University)
- **Venue/Year:** arXiv, December 2025 (camera-ready, likely accepted to a top venue)
- **URL:** https://arxiv.org/abs/2512.16917
- **What it does:** Proposes an on-policy joint training framework where an LLM reasoner and an LLM-based discriminator co-evolve. The discriminator evaluates the logical soundness of reasoning chain segments, creating an adversarial training dynamic. Improves DeepSeek-R1-Distill-Qwen-7B from 54.0 to 61.3 on AIME24.
- **Why it's important:** Introduces adversarial/contrastive training specifically for reasoning chains (not just final answers). The segment-level discriminator approach is novel -- it moves beyond outcome-based reward to process-level evaluation, which is key for robustness.

---

### Paper 7: Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning

- **Authors:** Chen, Raventos, Cheng, Ganguli, and Druckmann
- **Venue/Year:** NeurIPS 2025 (poster)
- **URL:** https://arxiv.org/abs/2502.07154
- **What it does:** Shows that standard cross-entropy fine-tuning is misaligned with test-time compute scaling (pass@N strategies). Training longer with cross-entropy actually decreases pass@N accuracy due to model overconfidence -- the model collapses its output distribution. Proposes confidence-limiting training that preserves output diversity, improving performance on MATH and MiniF2F when combined with test-time search.
- **Why it's important:** Accepted at NeurIPS 2025, a top venue. Provides a crucial insight for anyone combining fine-tuning with test-time scaling: standard training hurts diversity. This directly impacts how data augmentation and training should be designed when the deployment strategy involves sampling multiple solutions (self-consistency, best-of-N, etc.).

---

### Paper 8: MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning

- **Authors:** Li, Chen, Li, Liang, Zhou, Wang, and Zhang
- **Venue/Year:** arXiv preprint (under review), January 2026
- **URL:** https://arxiv.org/abs/2601.17006
- **What it does:** Proposes difficulty-controllable math data synthesis using hybrid and decomposed strategies, combined with curriculum learning. Creates graded difficulty datasets with automated checking and manual review. Fine-tuned Qwen2.5-7B achieves 52.6% across seven benchmarks, surpassing prior state-of-the-art augmentation methods.
- **Why it's important:** Directly addresses the data augmentation question with a practical system. The key insight is that difficulty control and curriculum ordering both help independently, and their combination yields the largest gains. Represents the current frontier of synthetic math data generation.

---

### Paper 9: Adaptive Problem Generation via Symbolic Representations

- **Authors:** Yeo, Jeon, Weerakoon, Qiao, Prakash, Solar-Lezama, and Misra
- **Venue/Year:** arXiv preprint, February 2026
- **URL:** https://arxiv.org/abs/2602.19187
- **What it does:** Generates RL training data by working in symbolic problem space (SymPy/SMT formulations) rather than directly on word problems. Symbolic representations enable precise structural control over problems and automatic ground-truth solution generation. Uses a closed-loop framework with prompt optimization to adapt problem difficulty to the learner.
- **Why it's important:** Bridges symbolic AI and LLM training. The decoupling of mathematical structure from linguistic realization is directly relevant to invariance learning -- by generating problems from symbolic templates, models are forced to learn the underlying math rather than surface patterns. Includes Armando Solar-Lezama (MIT), a leading figure in program synthesis.

---

### Paper 10: Robust Reasoning Benchmark

- **Authors:** Golikov, Opryshko, Pekhimenko, and Jeffrey
- **Venue/Year:** arXiv preprint, March 2026
- **URL:** https://arxiv.org/abs/2604.08571
- **What it does:** Applies 13 deterministic text perturbations (character substitutions, formatting changes, encoding variations) to AIME 2024/2025 problems and evaluates 8 advanced models. Identifies failure modes including "cognitive thrashing," "tokenization breakdown," and "reasoning collapse" in open-source models, with accuracy drops up to 100% on specific perturbations. Also discovers "Intra-Query Attention Dilution" -- performance degrades when solving multiple problems sequentially in one context window.
- **Why it's important:** Most recent and comprehensive robustness evaluation (2026). Goes beyond semantic perturbations to test tokenization-level and formatting-level robustness. The identification of novel failure modes (cognitive thrashing, attention dilution) provides actionable targets for perturbation-based training approaches.

---

### Summary of Themes

1. **Robustness benchmarking** (GSM-Symbolic, MATH-Perturb, Robust Reasoning Benchmark): All demonstrate that current LLMs are brittle to perturbations of math problems, whether semantic, structural, or even cosmetic. This motivates perturbation-based training.

2. **Surface form sensitivity** (Paraphrase and Solve, Beyond Language): Mathematical reasoning is not invariant to how problems are stated. SCoP exploits this via paraphrase-based self-consistency.

3. **Data augmentation for training** (MathMixup, Adaptive Problem Generation, Rewriting Pre-Training Data): The field is moving toward difficulty-controlled, symbolically-grounded data synthesis with curriculum learning.

4. **Self-verification and consistency** (DeepSeekMath-V2, Not All Votes Count / PROVE): Co-training generators with verifiers and using program-based verification to filter self-consistency votes both substantially improve reasoning reliability.

5. **Test-time compute scaling** (s1, Rethinking Fine-Tuning, Thinking-Optimal Scaling): Simple approaches to test-time scaling are highly effective, but training must be designed to preserve output diversity (confidence limiting) rather than collapsing to single solutions.

6. **Adversarial/contrastive training** (Generative Adversarial Reasoner): Segment-level adversarial discrimination of reasoning chains is an emerging approach to process-level robustness.

agentId: a375724644f3d443a (use SendMessage with to: 'a375724644f3d443a' to continue this agent)
&lt;usage>total_tokens: 26524
tool_uses: 25
duration_ms: 136391&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4bbdc5bf-35da-4fb9-bc0c-5f68bdd39e1a",
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "a43b66ff-319d-47ed-aed7-f44a007f5982",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey. Search for the most important papers (2024-2026) on:\n\n1. Data augmentation for mathematical reasoning training\n2. Invariance learning for reasoning models\n3. Perturbation-based training for LLM reasoning robustness\n4. Contrastive learning for mathematical reasoning\n5. Self-consistency and verification in math reasoning\n\nExecute these searches:\n\nSearch 1: \"data augmentation mathematical reasoning LLM training 2025 2026\"\nSearch 2: \"self-consistency mathematical reasoning verification 2024 2025\"\nSearch 3: \"contrastive learning mathematical reasoning robustness 2025\"\nSearch 4: \"symbolic perturbation math problem generation training 2025\"\nSearch 5: \"math word problem augmentation robustness training 2025\"\nSearch 6: \"reasoning invariance surface form LLM 2025\"\nSearch 7: \"test-time compute scaling mathematical reasoning 2025\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Focus on highly cited papers and those from top venues.",
    "agentId": "a375724644f3d443a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough material for a comprehensive report. Here is the literature survey:\n\n---\n\n## Literature Survey: Data Augmentation, Invariance, and Robustness for LLM Mathematical Reasoning (2024-2026)\n\n### Paper 1: GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\n\n- **Authors:** Mirzadeh et al. (Apple)\n- **Venue/Year:** ICLR 2025 (published as conference paper)\n- **URL:** https://arxiv.org/abs/2410.05229\n- **What it does:** Introduces GSM-Symbolic, a benchmark built from symbolic templates that generate diverse instantiations of the same math problem (varying names, numbers, structure). Reveals that LLMs show noticeable variance across instantiations, with performance drops up to 65% when irrelevant \"No-Op\" clauses are added, suggesting pattern matching rather than genuine reasoning.\n- **Why it's important:** Published at ICLR 2025 (top venue), from Apple ML Research. This paper became a landmark reference for the \"reasoning robustness\" debate. It has generated significant follow-up work and controversy -- subsequent 2026 re-evaluations with frontier models suggest the effect diminishes on cleaner data, but the benchmark methodology (symbolic templates for controlled evaluation) has been widely adopted.\n\n---\n\n### Paper 2: MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\n\n- **Authors:** Huang, Guo, Li, Ji, Ge, Li, Guo, Cai, Yuan, Wang, Wu, Yin, Tang, Huang, Jin, Chen, Zhang, and Wang\n- **Venue/Year:** arXiv preprint, February 2025\n- **URL:** https://arxiv.org/abs/2502.06453\n- **What it does:** Constructs MATH-P-Simple and MATH-P-Hard, 279 perturbed versions of the hardest MATH dataset problems. Perturbations include adding conditions, changing problem structure, and altering constraints. Demonstrates significant drops even on frontier models: o1-mini (-16.49%), gemini-2.0-flash-thinking (-12.9%). Identifies a memorization pattern where models apply problem-solving techniques without evaluating relevance to modifications.\n- **Why it's important:** Extends the GSM-Symbolic line of work to competition-level math (MATH level 5). The large author list includes researchers from Princeton and Google DeepMind. Provides concrete evidence that even advanced reasoning models are brittle to structural perturbations, not just superficial changes.\n\n---\n\n### Paper 3: Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning in Large Language Models\n\n- **Authors:** Zhou, Zhu, Antognini, Kim, and Zhang\n- **Venue/Year:** NAACL 2024 (main conference)\n- **URL:** https://arxiv.org/abs/2404.11500\n- **What it does:** Investigates how surface-level rephrasing of math problems (without changing semantics) impacts LLM solve rates -- finding swings from 5% to 100% on the same problem. Proposes Self-Consistency-over-Paraphrases (SCoP), which generates multiple paraphrased versions of a problem and aggregates answers, outperforming standard self-consistency (majority voting).\n- **Why it's important:** Published at NAACL 2024, a top NLP venue. Directly demonstrates that reasoning is not invariant to surface form and provides a practical method (SCoP) to exploit this for improved accuracy. This is a foundational reference for the \"surface form sensitivity\" problem in math reasoning.\n\n---\n\n### Paper 4: DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning\n\n- **Authors:** Shao, Luo, Lu, Ren, Hu, Ye, Gou, Ma, and Zhang (DeepSeek)\n- **Venue/Year:** arXiv, November 2025\n- **URL:** https://arxiv.org/abs/2511.22570\n- **What it does:** Trains an LLM-based verifier for theorem proving and uses it as a reward model for a proof generator. The generator is incentivized to identify and fix issues in its own proofs. Introduces scaled verification compute to automatically label hard-to-verify proofs as new training data. Achieves gold-level scores on IMO 2025 and CMO 2024, and 118/120 on Putnam 2024 (surpassing the highest human score of 90).\n- **Why it's important:** State-of-the-art results on premiere mathematical competitions. The self-verification loop (generator + verifier co-training) represents a major advance in self-consistency for mathematical reasoning. From DeepSeek, one of the most influential labs in reasoning model development. The Putnam result (exceeding all human participants) is a milestone.\n\n---\n\n### Paper 5: s1: Simple Test-Time Scaling\n\n- **Authors:** Muennighoff, Yang, Shi, Li, Fei-Fei, Hajishirzi, Zettlemoyer, Liang, Candes, and Hashimoto\n- **Venue/Year:** EMNLP 2025\n- **URL:** https://arxiv.org/abs/2501.19393\n- **What it does:** Demonstrates that test-time scaling can be achieved simply: (1) curate 1,000 high-quality questions emphasizing difficulty, diversity, and quality; (2) fine-tune Qwen2.5-32B-Instruct on this data; (3) use \"budget forcing\" to control reasoning length (forcibly terminating or extending thinking via appending \"Wait\" tokens). The resulting model exceeds o1-preview on competition math by up to 27% (MATH, AIME24). Scaling from 50% to 57% on AIME24 through budget forcing alone.\n- **Why it's important:** Published at EMNLP 2025, with an author list spanning Stanford, UW, and other top institutions. The paper is notable for its simplicity and reproducibility -- model, data, and code are fully open-source. It demonstrated that test-time compute scaling does not require massive proprietary infrastructure. Highly cited and widely reproduced.\n\n---\n\n### Paper 6: Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning\n\n- **Authors:** Liu, Ye, Ma, Chou, and Yuille (Johns Hopkins University)\n- **Venue/Year:** arXiv, December 2025 (camera-ready, likely accepted to a top venue)\n- **URL:** https://arxiv.org/abs/2512.16917\n- **What it does:** Proposes an on-policy joint training framework where an LLM reasoner and an LLM-based discriminator co-evolve. The discriminator evaluates the logical soundness of reasoning chain segments, creating an adversarial training dynamic. Improves DeepSeek-R1-Distill-Qwen-7B from 54.0 to 61.3 on AIME24.\n- **Why it's important:** Introduces adversarial/contrastive training specifically for reasoning chains (not just final answers). The segment-level discriminator approach is novel -- it moves beyond outcome-based reward to process-level evaluation, which is key for robustness.\n\n---\n\n### Paper 7: Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning\n\n- **Authors:** Chen, Raventos, Cheng, Ganguli, and Druckmann\n- **Venue/Year:** NeurIPS 2025 (poster)\n- **URL:** https://arxiv.org/abs/2502.07154\n- **What it does:** Shows that standard cross-entropy fine-tuning is misaligned with test-time compute scaling (pass@N strategies). Training longer with cross-entropy actually decreases pass@N accuracy due to model overconfidence -- the model collapses its output distribution. Proposes confidence-limiting training that preserves output diversity, improving performance on MATH and MiniF2F when combined with test-time search.\n- **Why it's important:** Accepted at NeurIPS 2025, a top venue. Provides a crucial insight for anyone combining fine-tuning with test-time scaling: standard training hurts diversity. This directly impacts how data augmentation and training should be designed when the deployment strategy involves sampling multiple solutions (self-consistency, best-of-N, etc.).\n\n---\n\n### Paper 8: MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning\n\n- **Authors:** Li, Chen, Li, Liang, Zhou, Wang, and Zhang\n- **Venue/Year:** arXiv preprint (under review), January 2026\n- **URL:** https://arxiv.org/abs/2601.17006\n- **What it does:** Proposes difficulty-controllable math data synthesis using hybrid and decomposed strategies, combined with curriculum learning. Creates graded difficulty datasets with automated checking and manual review. Fine-tuned Qwen2.5-7B achieves 52.6% across seven benchmarks, surpassing prior state-of-the-art augmentation methods.\n- **Why it's important:** Directly addresses the data augmentation question with a practical system. The key insight is that difficulty control and curriculum ordering both help independently, and their combination yields the largest gains. Represents the current frontier of synthetic math data generation.\n\n---\n\n### Paper 9: Adaptive Problem Generation via Symbolic Representations\n\n- **Authors:** Yeo, Jeon, Weerakoon, Qiao, Prakash, Solar-Lezama, and Misra\n- **Venue/Year:** arXiv preprint, February 2026\n- **URL:** https://arxiv.org/abs/2602.19187\n- **What it does:** Generates RL training data by working in symbolic problem space (SymPy/SMT formulations) rather than directly on word problems. Symbolic representations enable precise structural control over problems and automatic ground-truth solution generation. Uses a closed-loop framework with prompt optimization to adapt problem difficulty to the learner.\n- **Why it's important:** Bridges symbolic AI and LLM training. The decoupling of mathematical structure from linguistic realization is directly relevant to invariance learning -- by generating problems from symbolic templates, models are forced to learn the underlying math rather than surface patterns. Includes Armando Solar-Lezama (MIT), a leading figure in program synthesis.\n\n---\n\n### Paper 10: Robust Reasoning Benchmark\n\n- **Authors:** Golikov, Opryshko, Pekhimenko, and Jeffrey\n- **Venue/Year:** arXiv preprint, March 2026\n- **URL:** https://arxiv.org/abs/2604.08571\n- **What it does:** Applies 13 deterministic text perturbations (character substitutions, formatting changes, encoding variations) to AIME 2024/2025 problems and evaluates 8 advanced models. Identifies failure modes including \"cognitive thrashing,\" \"tokenization breakdown,\" and \"reasoning collapse\" in open-source models, with accuracy drops up to 100% on specific perturbations. Also discovers \"Intra-Query Attention Dilution\" -- performance degrades when solving multiple problems sequentially in one context window.\n- **Why it's important:** Most recent and comprehensive robustness evaluation (2026). Goes beyond semantic perturbations to test tokenization-level and formatting-level robustness. The identification of novel failure modes (cognitive thrashing, attention dilution) provides actionable targets for perturbation-based training approaches.\n\n---\n\n### Summary of Themes\n\n1. **Robustness benchmarking** (GSM-Symbolic, MATH-Perturb, Robust Reasoning Benchmark): All demonstrate that current LLMs are brittle to perturbations of math problems, whether semantic, structural, or even cosmetic. This motivates perturbation-based training.\n\n2. **Surface form sensitivity** (Paraphrase and Solve, Beyond Language): Mathematical reasoning is not invariant to how problems are stated. SCoP exploits this via paraphrase-based self-consistency.\n\n3. **Data augmentation for training** (MathMixup, Adaptive Problem Generation, Rewriting Pre-Training Data): The field is moving toward difficulty-controlled, symbolically-grounded data synthesis with curriculum learning.\n\n4. **Self-verification and consistency** (DeepSeekMath-V2, Not All Votes Count / PROVE): Co-training generators with verifiers and using program-based verification to filter self-consistency votes both substantially improve reasoning reliability.\n\n5. **Test-time compute scaling** (s1, Rethinking Fine-Tuning, Thinking-Optimal Scaling): Simple approaches to test-time scaling are highly effective, but training must be designed to preserve output diversity (confidence limiting) rather than collapsing to single solutions.\n\n6. **Adversarial/contrastive training** (Generative Adversarial Reasoner): Segment-level adversarial discrimination of reasoning chains is an emerging approach to process-level robustness."
      }
    ],
    "totalDurationMs": 136391,
    "totalTokens": 26524,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 22509,
      "output_tokens": 3128,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 886
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3128,
          "cache_read_input_tokens": 22509,
          "cache_creation_input_tokens": 886,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 886,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "4bbdc5bf-35da-4fb9-bc0c-5f68bdd39e1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-29T05:26:29.355Z_

<details><summary>↩ Tool result · `toolu_01HmFFtHqEr9GPki79YHAwSF`</summary>

```text
I now have comprehensive information on all the key papers. Let me compile the final report.

---

Here are the results of the literature survey. I found 10 distinct papers across NeurIPS 2025, ICML 2025, ICLR 2025, and ICLR 2026, prioritized by award status and presentation type.

---

## 1. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?

- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang
- **Venue/Year:** NeurIPS 2025 (Best Paper Runner-Up); ICML 2025 AI4MATH Workshop (Best Paper Award)
- **URL:** https://arxiv.org/abs/2504.13837
- **What it does:** Uses the unbiased pass@k metric to evaluate whether RLVR (Reinforcement Learning with Verifiable Rewards) creates genuinely new reasoning abilities in LLMs. Finds that while RLVR improves sampling efficiency (correct answers appear more frequently at small k), the base model achieves higher pass@k at large k, meaning RLVR does not expand the fundamental reasoning capability boundary.
- **Why it's important:** NeurIPS 2025 Best Paper Runner-Up and ICML 2025 Workshop Best Paper. Directly challenges the prevailing narrative that RL enables "superhuman" reasoning, making it a landmark paper for understanding the limits of RLVR.

---

## 2. Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free

- **Authors:** Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang et al. (Alibaba Qwen team)
- **Venue/Year:** NeurIPS 2025 (Best Paper Award)
- **URL:** https://arxiv.org/abs/2505.06708
- **What it does:** Systematically investigates gating-augmented softmax attention across models from 1.7B to 15B parameters. Demonstrates that appending a head-specific sigmoid gate after Scaled Dot-Product Attention introduces non-linearity and query-dependent sparsity, eliminating the "attention sink" phenomenon and improving training stability, long-context extrapolation, and overall performance. Already incorporated into Qwen3-Next.
- **Why it's important:** NeurIPS 2025 Best Paper Award. The first systematic exploration of attention gating at scale, with direct practical impact on production LLM architectures.

---

## 3. Superposition Yields Robust Neural Scaling

- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore
- **Venue/Year:** NeurIPS 2025 (Best Paper Runner-Up)
- **URL:** https://arxiv.org/abs/2505.10465
- **What it does:** Proposes a mechanistic explanation for neural scaling laws by linking them to representation superposition (encoding more features than available dimensions). Using sparse autoencoders and validation on open-source LLMs (OPT, Pythia, Qwen), shows that in "strong superposition" regimes, loss scales inversely with model width (L proportional to 1/m), providing a first-principles derivation robust to data distribution.
- **Why it's important:** NeurIPS 2025 Best Paper Runner-Up. Provides foundational theoretical understanding of why larger models generalize better, relevant to understanding scaling of reasoning capabilities.

---

## 4. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- **Authors:** DeepSeek-AI (Daya Guo, Dejian Yang, Haowei Zhang et al., 200+ contributors)
- **Venue/Year:** Nature 2025 (vol. 645, pp. 633-638); arXiv January 2025
- **URL:** https://arxiv.org/abs/2501.12948
- **What it does:** Demonstrates that reasoning abilities can be incentivized through pure RL without human-labeled reasoning trajectories. DeepSeek-R1-Zero, trained via large-scale RL without SFT, naturally develops self-reflection, verification, and dynamic strategy adaptation. Achieves superior performance on mathematics, coding, and STEM tasks.
- **Why it's important:** Published in Nature, one of the most influential and highly cited LLM papers of 2025. The first open research validating that reasoning can emerge purely from RL, catalyzing the entire RLVR research direction.

---

## 5. Reasoning with Sampling: Your Base Model is Smarter Than You Think

- **Authors:** Aayush Karan, Yilun Du
- **Venue/Year:** ICLR 2026 (Oral Presentation)
- **URL:** https://arxiv.org/abs/2510.14901
- **What it does:** Proposes an iterative sampling algorithm inspired by MCMC techniques that leverages base models' own likelihoods at inference time. Achieves reasoning performance that nearly matches or exceeds RL posttraining on MATH500, HumanEval, and GPQA, while avoiding the diversity collapse characteristic of RL-trained models. Requires no training, datasets, or verifiers.
- **Why it's important:** ICLR 2026 Oral. Complements Paper #1 by showing base models already contain strong reasoning capabilities that can be unlocked through better sampling, further questioning the necessity of RL posttraining.

---

## 6. LLMs Get Lost In Multi-Turn Conversation

- **Authors:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- **Venue/Year:** ICLR 2026 (Outstanding Paper Award)
- **URL:** https://arxiv.org/abs/2505.06120
- **What it does:** Through 200,000+ simulated multi-turn conversations, demonstrates that all top LLMs show an average 39% performance drop in multi-turn vs. single-turn settings. Identifies that models anchor on early assumptions and fail to integrate later corrections, revealing a fundamental reliability collapse (not just aptitude loss).
- **Why it's important:** ICLR 2026 Outstanding Paper Award. Directly relevant to robustness and consistency of LLM reasoning -- shows that reasoning degrades substantially when information is distributed across conversational turns.

---

## 7. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement

- **Authors:** An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu et al. (Alibaba Qwen team)
- **Venue/Year:** arXiv 2024 (September); widely cited in 2025
- **URL:** https://arxiv.org/abs/2409.12122
- **What it does:** Presents a self-improvement pipeline for mathematical reasoning spanning pre-training, SFT, and RL. Uses prior model iterations to synthesize training data (>1 trillion tokens), develops iterative reward models, and supports both chain-of-thought and tool-integrated reasoning in Chinese and English. Evaluated across 10 datasets from GSM8K to AIME24.
- **Why it's important:** Defines the state-of-the-art pipeline for mathematical reasoning LLMs. Highly cited and widely used as a base model in subsequent RL research (many ICLR 2026 papers build on Qwen2.5-Math).

---

## 8. Learning to Reason without External Rewards (Intuitor)

- **Authors:** Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song
- **Venue/Year:** ICLR 2026 (Conference Paper)
- **URL:** https://openreview.net/forum?id=OU9nFEYR2M
- **What it does:** Introduces Reinforcement Learning from Internal Feedback (RLIF) via "Intuitor," which uses a model's own confidence (self-certainty) as its sole reward signal. Achieves competitive mathematical reasoning performance and improved adaptability to unfamiliar domains like code generation, without any annotated solutions or external reward signals.
- **Why it's important:** ICLR 2026 Conference Paper. Proposes a fundamentally different paradigm for RL-based reasoning that eliminates the need for external verifiers, addressing a key bottleneck in scaling RLVR to domains without ground-truth answers.

---

## 9. Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning

- **Authors:** Qihao Liu, Luoxin Ye, Wufei Ma, Yu-Cheng Chou, Alan Yuille
- **Venue/Year:** ICLR 2026 (Conference Paper)
- **URL:** https://openreview.net/forum?id=ihucMuRXcY
- **What it does:** Introduces an adversarial RL framework that co-evolves an LLM reasoner and an LLM-based discriminator. The discriminator evaluates reasoning steps for logical soundness while generating dense step-level rewards. Improves DeepSeek-R1-Distill-Qwen-7B from 54.0 to 61.3 (+7.3) and DeepSeek-R1-Distill-Llama-8B from 43.7 to 53.7 (+10.0) on AIME24.
- **Why it's important:** ICLR 2026 Conference Paper. Addresses a core challenge in RL for reasoning -- sparse reward signals -- by introducing adversarial step-level feedback, achieving strong gains on competition-level math benchmarks.

---

## 10. Transformers are Inherently Succinct

- **Authors:** Pascal Bergstraesser, Ryan Cotterell, Anthony Widjaja Lin
- **Venue/Year:** ICLR 2026 (Outstanding Paper Award)
- **URL:** https://openreview.net/forum?id=VKGTGGcwl6 (ICLR 2026 proceedings)
- **What it does:** Provides a theoretical analysis of transformer expressiveness, showing that transformers can encode concepts more efficiently than RNNs. Establishes fundamental results about the computational power of transformer architectures.
- **Why it's important:** ICLR 2026 Outstanding Paper Award. Provides theoretical grounding for why transformer architectures are particularly well-suited for complex reasoning tasks.

---

## Summary of Awards

| Paper | Venue | Award |
|-------|-------|-------|
| Does RL Really Incentivize Reasoning... | NeurIPS 2025 | Best Paper Runner-Up |
| Does RL Really Incentivize Reasoning... | ICML 2025 Workshop | Best Paper |
| Gated Attention for LLMs | NeurIPS 2025 | Best Paper |
| Superposition Yields Robust Neural Scaling | NeurIPS 2025 | Best Paper Runner-Up |
| DeepSeek-R1 | Nature 2025 | Published in Nature |
| Reasoning with Sampling | ICLR 2026 | Oral |
| LLMs Get Lost In Multi-Turn Conversation | ICLR 2026 | Outstanding Paper |
| Transformers are Inherently Succinct | ICLR 2026 | Outstanding Paper |

The most directly relevant cluster for a survey on "mathematical reasoning + RL for LLMs" is Papers 1, 4, 5, 7, 8, and 9, which form a coherent narrative: DeepSeek-R1 (#4) proved RL can incentivize reasoning; Yue et al. (#1) showed RLVR does not expand capabilities beyond the base model; Karan & Du (#5) showed sampling alone can match RL; and papers #8 and #9 explore alternative RL paradigms (intrinsic rewards and adversarial training) to push beyond these limits.

agentId: aafb33869bd78b422 (use SendMessage with to: 'aafb33869bd78b422' to continue this agent)
&lt;usage>total_tokens: 33690
tool_uses: 32
duration_ms: 147740&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c4c6224-dad8-42ee-8516-8db6756c6dcb",
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "c3c6407d-64c5-4e9c-887f-2ac22963462c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on mathematical reasoning and RL for LLMs. Search for best paper awards and outstanding papers at top venues (2024-2026) that are related to:\n- Mathematical reasoning in LLMs\n- Reinforcement learning for reasoning\n- Robustness of LLM reasoning\n- Consistency/invariance in neural networks\n\nExecute these searches:\n\nSearch 1: \"best paper award NeurIPS 2025 mathematical reasoning\"\nSearch 2: \"best paper award ICML 2025 reinforcement learning reasoning\"\nSearch 3: \"best paper award ICLR 2025 2026 mathematical reasoning LLM\"\nSearch 4: \"outstanding paper NeurIPS ICML 2025 reasoning robustness\"\nSearch 5: \"oral spotlight ICLR 2026 mathematical reasoning\"\nSearch 6: \"best paper ACL EMNLP 2025 reasoning consistency\"\nSearch 7: site:openreview.net \"ICLR 2026\" \"mathematical reasoning\" \"reinforcement learning\"\nSearch 8: \"Qwen2.5-Math training mathematical reasoning 2025\"\nSearch 9: \"most cited mathematical reasoning LLM paper 2025\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Prioritize best paper winners and oral/spotlight presentations.",
    "agentId": "aafb33869bd78b422",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information on all the key papers. Let me compile the final report.\n\n---\n\nHere are the results of the literature survey. I found 10 distinct papers across NeurIPS 2025, ICML 2025, ICLR 2025, and ICLR 2026, prioritized by award status and presentation type.\n\n---\n\n## 1. Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\n\n- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang\n- **Venue/Year:** NeurIPS 2025 (Best Paper Runner-Up); ICML 2025 AI4MATH Workshop (Best Paper Award)\n- **URL:** https://arxiv.org/abs/2504.13837\n- **What it does:** Uses the unbiased pass@k metric to evaluate whether RLVR (Reinforcement Learning with Verifiable Rewards) creates genuinely new reasoning abilities in LLMs. Finds that while RLVR improves sampling efficiency (correct answers appear more frequently at small k), the base model achieves higher pass@k at large k, meaning RLVR does not expand the fundamental reasoning capability boundary.\n- **Why it's important:** NeurIPS 2025 Best Paper Runner-Up and ICML 2025 Workshop Best Paper. Directly challenges the prevailing narrative that RL enables \"superhuman\" reasoning, making it a landmark paper for understanding the limits of RLVR.\n\n---\n\n## 2. Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\n\n- **Authors:** Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang et al. (Alibaba Qwen team)\n- **Venue/Year:** NeurIPS 2025 (Best Paper Award)\n- **URL:** https://arxiv.org/abs/2505.06708\n- **What it does:** Systematically investigates gating-augmented softmax attention across models from 1.7B to 15B parameters. Demonstrates that appending a head-specific sigmoid gate after Scaled Dot-Product Attention introduces non-linearity and query-dependent sparsity, eliminating the \"attention sink\" phenomenon and improving training stability, long-context extrapolation, and overall performance. Already incorporated into Qwen3-Next.\n- **Why it's important:** NeurIPS 2025 Best Paper Award. The first systematic exploration of attention gating at scale, with direct practical impact on production LLM architectures.\n\n---\n\n## 3. Superposition Yields Robust Neural Scaling\n\n- **Authors:** Yizhou Liu, Ziming Liu, Jeff Gore\n- **Venue/Year:** NeurIPS 2025 (Best Paper Runner-Up)\n- **URL:** https://arxiv.org/abs/2505.10465\n- **What it does:** Proposes a mechanistic explanation for neural scaling laws by linking them to representation superposition (encoding more features than available dimensions). Using sparse autoencoders and validation on open-source LLMs (OPT, Pythia, Qwen), shows that in \"strong superposition\" regimes, loss scales inversely with model width (L proportional to 1/m), providing a first-principles derivation robust to data distribution.\n- **Why it's important:** NeurIPS 2025 Best Paper Runner-Up. Provides foundational theoretical understanding of why larger models generalize better, relevant to understanding scaling of reasoning capabilities.\n\n---\n\n## 4. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\n\n- **Authors:** DeepSeek-AI (Daya Guo, Dejian Yang, Haowei Zhang et al., 200+ contributors)\n- **Venue/Year:** Nature 2025 (vol. 645, pp. 633-638); arXiv January 2025\n- **URL:** https://arxiv.org/abs/2501.12948\n- **What it does:** Demonstrates that reasoning abilities can be incentivized through pure RL without human-labeled reasoning trajectories. DeepSeek-R1-Zero, trained via large-scale RL without SFT, naturally develops self-reflection, verification, and dynamic strategy adaptation. Achieves superior performance on mathematics, coding, and STEM tasks.\n- **Why it's important:** Published in Nature, one of the most influential and highly cited LLM papers of 2025. The first open research validating that reasoning can emerge purely from RL, catalyzing the entire RLVR research direction.\n\n---\n\n## 5. Reasoning with Sampling: Your Base Model is Smarter Than You Think\n\n- **Authors:** Aayush Karan, Yilun Du\n- **Venue/Year:** ICLR 2026 (Oral Presentation)\n- **URL:** https://arxiv.org/abs/2510.14901\n- **What it does:** Proposes an iterative sampling algorithm inspired by MCMC techniques that leverages base models' own likelihoods at inference time. Achieves reasoning performance that nearly matches or exceeds RL posttraining on MATH500, HumanEval, and GPQA, while avoiding the diversity collapse characteristic of RL-trained models. Requires no training, datasets, or verifiers.\n- **Why it's important:** ICLR 2026 Oral. Complements Paper #1 by showing base models already contain strong reasoning capabilities that can be unlocked through better sampling, further questioning the necessity of RL posttraining.\n\n---\n\n## 6. LLMs Get Lost In Multi-Turn Conversation\n\n- **Authors:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville\n- **Venue/Year:** ICLR 2026 (Outstanding Paper Award)\n- **URL:** https://arxiv.org/abs/2505.06120\n- **What it does:** Through 200,000+ simulated multi-turn conversations, demonstrates that all top LLMs show an average 39% performance drop in multi-turn vs. single-turn settings. Identifies that models anchor on early assumptions and fail to integrate later corrections, revealing a fundamental reliability collapse (not just aptitude loss).\n- **Why it's important:** ICLR 2026 Outstanding Paper Award. Directly relevant to robustness and consistency of LLM reasoning -- shows that reasoning degrades substantially when information is distributed across conversational turns.\n\n---\n\n## 7. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement\n\n- **Authors:** An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu et al. (Alibaba Qwen team)\n- **Venue/Year:** arXiv 2024 (September); widely cited in 2025\n- **URL:** https://arxiv.org/abs/2409.12122\n- **What it does:** Presents a self-improvement pipeline for mathematical reasoning spanning pre-training, SFT, and RL. Uses prior model iterations to synthesize training data (>1 trillion tokens), develops iterative reward models, and supports both chain-of-thought and tool-integrated reasoning in Chinese and English. Evaluated across 10 datasets from GSM8K to AIME24.\n- **Why it's important:** Defines the state-of-the-art pipeline for mathematical reasoning LLMs. Highly cited and widely used as a base model in subsequent RL research (many ICLR 2026 papers build on Qwen2.5-Math).\n\n---\n\n## 8. Learning to Reason without External Rewards (Intuitor)\n\n- **Authors:** Xuandong Zhao, Zhewei Kang, Aosong Feng, Sergey Levine, Dawn Song\n- **Venue/Year:** ICLR 2026 (Conference Paper)\n- **URL:** https://openreview.net/forum?id=OU9nFEYR2M\n- **What it does:** Introduces Reinforcement Learning from Internal Feedback (RLIF) via \"Intuitor,\" which uses a model's own confidence (self-certainty) as its sole reward signal. Achieves competitive mathematical reasoning performance and improved adaptability to unfamiliar domains like code generation, without any annotated solutions or external reward signals.\n- **Why it's important:** ICLR 2026 Conference Paper. Proposes a fundamentally different paradigm for RL-based reasoning that eliminates the need for external verifiers, addressing a key bottleneck in scaling RLVR to domains without ground-truth answers.\n\n---\n\n## 9. Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning\n\n- **Authors:** Qihao Liu, Luoxin Ye, Wufei Ma, Yu-Cheng Chou, Alan Yuille\n- **Venue/Year:** ICLR 2026 (Conference Paper)\n- **URL:** https://openreview.net/forum?id=ihucMuRXcY\n- **What it does:** Introduces an adversarial RL framework that co-evolves an LLM reasoner and an LLM-based discriminator. The discriminator evaluates reasoning steps for logical soundness while generating dense step-level rewards. Improves DeepSeek-R1-Distill-Qwen-7B from 54.0 to 61.3 (+7.3) and DeepSeek-R1-Distill-Llama-8B from 43.7 to 53.7 (+10.0) on AIME24.\n- **Why it's important:** ICLR 2026 Conference Paper. Addresses a core challenge in RL for reasoning -- sparse reward signals -- by introducing adversarial step-level feedback, achieving strong gains on competition-level math benchmarks.\n\n---\n\n## 10. Transformers are Inherently Succinct\n\n- **Authors:** Pascal Bergstraesser, Ryan Cotterell, Anthony Widjaja Lin\n- **Venue/Year:** ICLR 2026 (Outstanding Paper Award)\n- **URL:** https://openreview.net/forum?id=VKGTGGcwl6 (ICLR 2026 proceedings)\n- **What it does:** Provides a theoretical analysis of transformer expressiveness, showing that transformers can encode concepts more efficiently than RNNs. Establishes fundamental results about the computational power of transformer architectures.\n- **Why it's important:** ICLR 2026 Outstanding Paper Award. Provides theoretical grounding for why transformer architectures are particularly well-suited for complex reasoning tasks.\n\n---\n\n## Summary of Awards\n\n| Paper | Venue | Award |\n|-------|-------|-------|\n| Does RL Really Incentivize Reasoning... | NeurIPS 2025 | Best Paper Runner-Up |\n| Does RL Really Incentivize Reasoning... | ICML 2025 Workshop | Best Paper |\n| Gated Attention for LLMs | NeurIPS 2025 | Best Paper |\n| Superposition Yields Robust Neural Scaling | NeurIPS 2025 | Best Paper Runner-Up |\n| DeepSeek-R1 | Nature 2025 | Published in Nature |\n| Reasoning with Sampling | ICLR 2026 | Oral |\n| LLMs Get Lost In Multi-Turn Conversation | ICLR 2026 | Outstanding Paper |\n| Transformers are Inherently Succinct | ICLR 2026 | Outstanding Paper |\n\nThe most directly relevant cluster for a survey on \"mathematical reasoning + RL for LLMs\" is Papers 1, 4, 5, 7, 8, and 9, which form a coherent narrative: DeepSeek-R1 (#4) proved RL can incentivize reasoning; Yue et al. (#1) showed RLVR does not expand capabilities beyond the base model; Karan & Du (#5) showed sampling alone can match RL; and papers #8 and #9 explore alternative RL paradigms (intrinsic rewards and adversarial training) to push beyond these limits."
      }
    ],
    "totalDurationMs": 147740,
    "totalTokens": 33690,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2272,
      "cache_read_input_tokens": 28482,
      "output_tokens": 2935,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2272
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2935,
          "cache_read_input_tokens": 28482,
          "cache_creation_input_tokens": 2272,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2272,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 32
    }
  },
  "sourceToolAssistantUUID": "9c4c6224-dad8-42ee-8516-8db6756c6dcb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "c3c6407d-64c5-4e9c-887f-2ac22963462c",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct literature survey on RL math reasoning robustness",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Tool result

_source line 27 · 2026-05-29T05:26:41.330Z_

<details><summary>↩ Tool result · `toolu_012vc1PRdNP4dLW875E7Fs6y`</summary>

```text
I now have a comprehensive set of papers. Here is the full literature survey report.

---

## Literature Survey: Consistency Regularization Techniques in NLP and Mathematical Reasoning (2024-2026)

Below are 10 distinct papers organized by topic, with full details extracted from their arXiv/venue pages.

---

### Paper 1: PPCL -- Prompt Perturbation Consistency Learning

- **Full Title:** Prompt Perturbation Consistency Learning for Robust Language Models
- **Authors:** Yao Qiang, Subhrangshu Nandi, Ninareh Mehrabi, Greg Ver Steeg, Anoop Kumar, Anna Rumshisky, Aram Galstyan
- **Venue/Year:** Findings of EACL 2024
- **URL:** https://aclanthology.org/2024.findings-eacl.91/ (also https://arxiv.org/abs/2402.15833)
- **What it does:** Proposes PPCL, which regularizes the JS divergence between output distributions from clean and perturbed prompts (oronyms, synonyms, paraphrases) during fine-tuning. Recovers ~59% and ~69% of performance drops for intent classification and slot filling respectively, while using 10x fewer augmented samples than data augmentation baselines.
- **Why it's important:** Published at a top CL venue (EACL Findings). This is one of the foundational papers directly applying consistency regularization via JS divergence to LLM prompt robustness. Demonstrates that consistency training dramatically outperforms brute-force data augmentation for NLU robustness.

---

### Paper 2: F2C -- Flip-Flop Consistency

- **Full Title:** Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs
- **Authors:** Parsa Hejabi, Elnaz Rahmati, Alireza S. Ziabari, Morteza Dehghani (University of Southern California)
- **Venue/Year:** arXiv preprint, October 2025 (submitted to ICLR 2026)
- **URL:** https://arxiv.org/abs/2510.14242
- **What it does:** Introduces an unsupervised two-component method: (1) Consensus Cross-Entropy (CCE) that uses majority voting across prompt variations as pseudo-labels, and (2) a representation alignment loss pulling low-confidence predictions toward the consensus. Achieves +11.62% agreement, +8.94% mean F1, and -3.29% variance across 11 datasets with 4-15 prompt variations each. Generalizes to held-out prompt formats.
- **Why it's important:** Directly extends PPCL to a fully unsupervised setting (no labeled perturbation data needed). Represents the state of the art in prompt perturbation robustness as of late 2025. Under review at a top venue (ICLR 2026).

---

### Paper 3: CSR -- Causal Consistency Regularization for Faithful Reasoning

- **Full Title:** Causal Consistency Regularization: Training Verifiably Sensitive Reasoning in Large Language Models
- **Authors:** Sanjeda Akter, Ibne Farabi Shihab, Anuj Sharma
- **Venue/Year:** arXiv preprint, September 2025 (v3: January 2026)
- **URL:** https://arxiv.org/abs/2509.01544
- **What it does:** Proposes Counterfactual Sensitivity Regularization (CSR), which applies operator-level interventions to reasoning traces (e.g., swapping "+" with "-") and penalizes the model via KL divergence when logically invalid traces still produce original answers. Improves reasoning faithfulness by up to 70 percentage points over standard fine-tuning, with only ~9% training overhead. Transfers across model families with 94-97% success in structured domains.
- **Why it's important:** Directly relevant to mathematical reasoning -- enforces that reasoning steps are causally connected to answers, not just post-hoc rationalizations. Bridges consistency regularization and causal reasoning faithfulness. Uses the same KL/divergence-based regularization paradigm as PPCL but applied to reasoning traces rather than input perturbations.

---

### Paper 4: Consistency Training Against Sycophancy and Jailbreaks

- **Full Title:** Consistency Training Helps Stop Sycophancy and Jailbreaks
- **Authors:** Alex Irpan, Alexander Matt Turner, Mark Kurzeja, David K. Elson, Rohin Shah (Google DeepMind)
- **Venue/Year:** arXiv preprint, October 2025 (submitted to ICLR 2026)
- **URL:** https://arxiv.org/abs/2510.27062
- **What it does:** Investigates consistency training as a self-supervised paradigm teaching models to be invariant to irrelevant prompt cues. Compares Bias-augmented Consistency Training (BCT) and the new Activation Consistency Training (ACT). Both reduce Gemini 2.5 Flash's susceptibility to sycophancy and jailbreaks. BCT trains on output-level consistency; ACT enforces consistency over internal activations. BCT proves more effective against jailbreaks.
- **Why it's important:** From Google DeepMind, applied to a production-scale model (Gemini 2.5 Flash). Reframes alignment challenges as consistency problems. Shows consistency training is not just for task robustness but also for safety alignment. Under review at ICLR 2026.

---

### Paper 5: AbstRaL -- Reinforced Abstract Reasoning for Math

- **Full Title:** AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking
- **Authors:** Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe
- **Venue/Year:** ICLR 2026 (accepted, poster)
- **URL:** https://arxiv.org/abs/2506.07751
- **What it does:** Teaches LLMs to generate mathematical abstractions of grade-school math problems, then connects abstractions with symbolic tools. Uses reinforcement learning (shown to be superior to SFT for learning faithful abstractions) on GranulAR data distilled from oracle LLMs. Significantly mitigates performance degradation on GSM perturbation benchmarks and also improves out-of-distribution mathematical and general reasoning.
- **Why it's important:** Accepted at ICLR 2026 -- a top venue. Directly addresses robustness in mathematical reasoning. Shows that abstraction via RL implicitly provides consistency benefits: the model reasons over problem structure rather than surface features, making it invariant to numerical/nominal perturbations.

---

### Paper 6: Robustness and CoT Consistency of RL-Finetuned VLMs

- **Full Title:** On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs
- **Authors:** Rosie Zhao, Anshul Shah, Xiaoyu Zhu, Xinke Deng, Zhongyu Jiang, Yang Yang, Joerg Liebelt, Arnab Mondal (Apple)
- **Venue/Year:** ICML 2026 (accepted)
- **URL:** https://arxiv.org/abs/2602.12506
- **What it does:** Investigates how RL-finetuned vision-language models respond to textual perturbations (misleading captions, incorrect CoT traces). Identifies an accuracy-faithfulness trade-off: RL fine-tuning raises benchmark accuracy but erodes CoT reliability and robustness to contextual shifts. Evaluates adversarial augmentation and faithfulness-aware rewards as mitigations.
- **Why it's important:** Accepted at ICML 2026 (top venue). From Apple. Demonstrates that RL-based training can hurt consistency even while improving accuracy -- a critical finding for anyone applying RL to mathematical reasoning. Advocates for training methods emphasizing correctness, robustness, and faithfulness jointly.

---

### Paper 7: Invariant Language Modeling

- **Full Title:** Invariant Language Modeling
- **Authors:** Maxime Peyrard, Sarvjeet Singh Ghotra, Martin Josifoski, Vidhan Agarwal, Barun Patra, Dean Carignan, Emre Kiciman, Robert West
- **Venue/Year:** EMNLP 2022
- **URL:** https://arxiv.org/abs/2110.08413
- **What it does:** Adapts Invariant Risk Minimization (IRM) to language models via a game-theoretic formulation where environments compete to optimize environment-specific losses by updating model subsets in round-robin fashion. Demonstrates removal of structured noise, elimination of spurious correlations, and improved OOD generalization with negligible computational overhead.
- **Why it's important:** Published at EMNLP (top NLP venue). The foundational work applying IRM principles to language modeling. Provides the theoretical bridge between causal/invariant learning and NLP robustness that later consistency regularization methods build upon.

---

### Paper 8: CCR -- Fighting Spurious Correlations via Causal Learning

- **Full Title:** Fighting Spurious Correlations in Text Classification via a Causal Learning Perspective
- **Authors:** Yuqing Zhou, Ziwei Zhu
- **Venue/Year:** NAACL 2025 (accepted)
- **URL:** https://arxiv.org/abs/2411.01045
- **What it does:** Proposes CCR (Causally Calibrated Robust Classifier), which reduces reliance on spurious correlations through counterfactual feature selection and an unbiased inverse propensity weighting loss. Achieves competitive performance on CivilComments and MultiNLI without requiring group labels, sometimes matching methods that do use them.
- **Why it's important:** Accepted at NAACL 2025 (top venue). Connects causal learning to NLP robustness in text classification. Shows that causal feature selection can replace group-label-dependent debiasing methods -- relevant for applying invariance principles to reasoning tasks where spurious correlations are common.

---

### Paper 9: LLM Robustness Survey

- **Full Title:** Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics
- **Authors:** Pankaj Kumar, Subhankar Mishra
- **Venue/Year:** Accepted at TMLR (Transactions on Machine Learning Research), 2025
- **URL:** https://arxiv.org/abs/2505.18658
- **What it does:** Provides a comprehensive survey categorizing LLM non-robustness sources into intrinsic limitations, data vulnerabilities, and adversarial threats. Reviews mitigation approaches including consistency training, data augmentation, adversarial training, and regularization. Discusses assessment benchmarks and metrics.
- **Why it's important:** Accepted at TMLR. Provides the broadest recent overview of where consistency regularization fits among other robustness strategies for LLMs. Useful as a reference for positioning any new work in this space.

---

### Paper 10: Enterprise LLM Perturbation Consistency Benchmark

- **Full Title:** Evaluating Robustness of Large Language Models in Enterprise Applications: Benchmarks for Perturbation Consistency Across Formats and Languages
- **Authors:** Tara Bogavelli, Oluwanifemi Bamgbose, Gabrielle Gauthier Melancon, Fanny Riols, Roshnee Sharma
- **Venue/Year:** arXiv preprint, January 2026
- **URL:** https://arxiv.org/abs/2601.06341
- **What it does:** Benchmarks 11 LLMs (4B to 120B+ parameters) across perturbation types including text edits, formatting changes (JSON, YAML), multilingual inputs, and instruction positioning shifts. Finds minor perturbations can degrade performance by up to 40 percentage points. Notably, model size does not guarantee robustness (an 8B model outperformed most larger models).
- **Why it's important:** Provides empirical evidence for the scale of the consistency problem in production settings. The finding that model size does not solve perturbation sensitivity motivates training-time solutions like consistency regularization.

---

## Summary of Key Themes

1. **JS/KL divergence regularization** is the dominant technical approach: PPCL uses JS divergence between clean/perturbed outputs; CSR uses KL divergence between original/counterfactual reasoning traces; F2C uses representation alignment losses.

2. **Consistency training outperforms data augmentation**: PPCL shows 10x sample efficiency over augmentation; F2C works fully unsupervised; BCT/ACT work as self-supervised methods.

3. **The accuracy-faithfulness trade-off** is a critical finding: RL fine-tuning can improve accuracy while degrading reasoning consistency (Zhao et al., ICML 2026), motivating joint optimization of correctness and consistency (CSR).

4. **Abstraction as implicit consistency**: AbstRaL (ICLR 2026) shows that teaching models to reason abstractly provides robustness to surface-level perturbations in math problems, connecting abstraction learning to consistency.

5. **Causal/invariant learning foundations**: Invariant Language Modeling (EMNLP 2022) and CCR (NAACL 2025) provide the causal learning foundations that consistency regularization builds upon, applying IRM and counterfactual reasoning to NLP.

agentId: a8041b8866eacd2f8 (use SendMessage with to: 'a8041b8866eacd2f8' to continue this agent)
&lt;usage>total_tokens: 31654
tool_uses: 30
duration_ms: 166494&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e61872b9-2d54-40d1-b34d-458f63602f49",
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "b2b12442-382f-4667-8e49-c808016290bb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on consistency regularization techniques in NLP and their potential application to mathematical reasoning. Search for the most important papers (2024-2026) on:\n\n1. Consistency regularization for LLM robustness (JS divergence, KL divergence)\n2. F²C / Flip-Flop Consistency for prompt perturbation robustness\n3. PPCL - perturbation consistency learning\n4. Causal consistency regularization for reasoning\n5. Invariant risk minimization for language models\n6. Data augmentation vs consistency training for NLP robustness\n\nExecute these searches and for EVERY promising paper, fetch its arXiv abstract:\n\nSearch 1: \"consistency regularization language model robustness perturbation 2024 2025\"\nSearch 2: \"Flip-Flop Consistency F2C prompt perturbation JS divergence\"\nSearch 3: \"PPCL perturbation consistency regularization NLU 2024\"\nSearch 4: \"causal consistency regularization reasoning faithfulness 2025\"\nSearch 5: \"invariant risk minimization language model reasoning 2025 2026\"\nSearch 6: \"consistency training data augmentation robustness LLM 2025\"\nSearch 7: \"AbstRaL abstract reasoning reinforcement learning math 2025 2026\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Focus on papers from top venues (ACL, EMNLP, NAACL, NeurIPS, ICML, ICLR, EACL).",
    "agentId": "a8041b8866eacd2f8",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive set of papers. Here is the full literature survey report.\n\n---\n\n## Literature Survey: Consistency Regularization Techniques in NLP and Mathematical Reasoning (2024-2026)\n\nBelow are 10 distinct papers organized by topic, with full details extracted from their arXiv/venue pages.\n\n---\n\n### Paper 1: PPCL -- Prompt Perturbation Consistency Learning\n\n- **Full Title:** Prompt Perturbation Consistency Learning for Robust Language Models\n- **Authors:** Yao Qiang, Subhrangshu Nandi, Ninareh Mehrabi, Greg Ver Steeg, Anoop Kumar, Anna Rumshisky, Aram Galstyan\n- **Venue/Year:** Findings of EACL 2024\n- **URL:** https://aclanthology.org/2024.findings-eacl.91/ (also https://arxiv.org/abs/2402.15833)\n- **What it does:** Proposes PPCL, which regularizes the JS divergence between output distributions from clean and perturbed prompts (oronyms, synonyms, paraphrases) during fine-tuning. Recovers ~59% and ~69% of performance drops for intent classification and slot filling respectively, while using 10x fewer augmented samples than data augmentation baselines.\n- **Why it's important:** Published at a top CL venue (EACL Findings). This is one of the foundational papers directly applying consistency regularization via JS divergence to LLM prompt robustness. Demonstrates that consistency training dramatically outperforms brute-force data augmentation for NLU robustness.\n\n---\n\n### Paper 2: F2C -- Flip-Flop Consistency\n\n- **Full Title:** Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs\n- **Authors:** Parsa Hejabi, Elnaz Rahmati, Alireza S. Ziabari, Morteza Dehghani (University of Southern California)\n- **Venue/Year:** arXiv preprint, October 2025 (submitted to ICLR 2026)\n- **URL:** https://arxiv.org/abs/2510.14242\n- **What it does:** Introduces an unsupervised two-component method: (1) Consensus Cross-Entropy (CCE) that uses majority voting across prompt variations as pseudo-labels, and (2) a representation alignment loss pulling low-confidence predictions toward the consensus. Achieves +11.62% agreement, +8.94% mean F1, and -3.29% variance across 11 datasets with 4-15 prompt variations each. Generalizes to held-out prompt formats.\n- **Why it's important:** Directly extends PPCL to a fully unsupervised setting (no labeled perturbation data needed). Represents the state of the art in prompt perturbation robustness as of late 2025. Under review at a top venue (ICLR 2026).\n\n---\n\n### Paper 3: CSR -- Causal Consistency Regularization for Faithful Reasoning\n\n- **Full Title:** Causal Consistency Regularization: Training Verifiably Sensitive Reasoning in Large Language Models\n- **Authors:** Sanjeda Akter, Ibne Farabi Shihab, Anuj Sharma\n- **Venue/Year:** arXiv preprint, September 2025 (v3: January 2026)\n- **URL:** https://arxiv.org/abs/2509.01544\n- **What it does:** Proposes Counterfactual Sensitivity Regularization (CSR), which applies operator-level interventions to reasoning traces (e.g., swapping \"+\" with \"-\") and penalizes the model via KL divergence when logically invalid traces still produce original answers. Improves reasoning faithfulness by up to 70 percentage points over standard fine-tuning, with only ~9% training overhead. Transfers across model families with 94-97% success in structured domains.\n- **Why it's important:** Directly relevant to mathematical reasoning -- enforces that reasoning steps are causally connected to answers, not just post-hoc rationalizations. Bridges consistency regularization and causal reasoning faithfulness. Uses the same KL/divergence-based regularization paradigm as PPCL but applied to reasoning traces rather than input perturbations.\n\n---\n\n### Paper 4: Consistency Training Against Sycophancy and Jailbreaks\n\n- **Full Title:** Consistency Training Helps Stop Sycophancy and Jailbreaks\n- **Authors:** Alex Irpan, Alexander Matt Turner, Mark Kurzeja, David K. Elson, Rohin Shah (Google DeepMind)\n- **Venue/Year:** arXiv preprint, October 2025 (submitted to ICLR 2026)\n- **URL:** https://arxiv.org/abs/2510.27062\n- **What it does:** Investigates consistency training as a self-supervised paradigm teaching models to be invariant to irrelevant prompt cues. Compares Bias-augmented Consistency Training (BCT) and the new Activation Consistency Training (ACT). Both reduce Gemini 2.5 Flash's susceptibility to sycophancy and jailbreaks. BCT trains on output-level consistency; ACT enforces consistency over internal activations. BCT proves more effective against jailbreaks.\n- **Why it's important:** From Google DeepMind, applied to a production-scale model (Gemini 2.5 Flash). Reframes alignment challenges as consistency problems. Shows consistency training is not just for task robustness but also for safety alignment. Under review at ICLR 2026.\n\n---\n\n### Paper 5: AbstRaL -- Reinforced Abstract Reasoning for Math\n\n- **Full Title:** AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking\n- **Authors:** Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe\n- **Venue/Year:** ICLR 2026 (accepted, poster)\n- **URL:** https://arxiv.org/abs/2506.07751\n- **What it does:** Teaches LLMs to generate mathematical abstractions of grade-school math problems, then connects abstractions with symbolic tools. Uses reinforcement learning (shown to be superior to SFT for learning faithful abstractions) on GranulAR data distilled from oracle LLMs. Significantly mitigates performance degradation on GSM perturbation benchmarks and also improves out-of-distribution mathematical and general reasoning.\n- **Why it's important:** Accepted at ICLR 2026 -- a top venue. Directly addresses robustness in mathematical reasoning. Shows that abstraction via RL implicitly provides consistency benefits: the model reasons over problem structure rather than surface features, making it invariant to numerical/nominal perturbations.\n\n---\n\n### Paper 6: Robustness and CoT Consistency of RL-Finetuned VLMs\n\n- **Full Title:** On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\n- **Authors:** Rosie Zhao, Anshul Shah, Xiaoyu Zhu, Xinke Deng, Zhongyu Jiang, Yang Yang, Joerg Liebelt, Arnab Mondal (Apple)\n- **Venue/Year:** ICML 2026 (accepted)\n- **URL:** https://arxiv.org/abs/2602.12506\n- **What it does:** Investigates how RL-finetuned vision-language models respond to textual perturbations (misleading captions, incorrect CoT traces). Identifies an accuracy-faithfulness trade-off: RL fine-tuning raises benchmark accuracy but erodes CoT reliability and robustness to contextual shifts. Evaluates adversarial augmentation and faithfulness-aware rewards as mitigations.\n- **Why it's important:** Accepted at ICML 2026 (top venue). From Apple. Demonstrates that RL-based training can hurt consistency even while improving accuracy -- a critical finding for anyone applying RL to mathematical reasoning. Advocates for training methods emphasizing correctness, robustness, and faithfulness jointly.\n\n---\n\n### Paper 7: Invariant Language Modeling\n\n- **Full Title:** Invariant Language Modeling\n- **Authors:** Maxime Peyrard, Sarvjeet Singh Ghotra, Martin Josifoski, Vidhan Agarwal, Barun Patra, Dean Carignan, Emre Kiciman, Robert West\n- **Venue/Year:** EMNLP 2022\n- **URL:** https://arxiv.org/abs/2110.08413\n- **What it does:** Adapts Invariant Risk Minimization (IRM) to language models via a game-theoretic formulation where environments compete to optimize environment-specific losses by updating model subsets in round-robin fashion. Demonstrates removal of structured noise, elimination of spurious correlations, and improved OOD generalization with negligible computational overhead.\n- **Why it's important:** Published at EMNLP (top NLP venue). The foundational work applying IRM principles to language modeling. Provides the theoretical bridge between causal/invariant learning and NLP robustness that later consistency regularization methods build upon.\n\n---\n\n### Paper 8: CCR -- Fighting Spurious Correlations via Causal Learning\n\n- **Full Title:** Fighting Spurious Correlations in Text Classification via a Causal Learning Perspective\n- **Authors:** Yuqing Zhou, Ziwei Zhu\n- **Venue/Year:** NAACL 2025 (accepted)\n- **URL:** https://arxiv.org/abs/2411.01045\n- **What it does:** Proposes CCR (Causally Calibrated Robust Classifier), which reduces reliance on spurious correlations through counterfactual feature selection and an unbiased inverse propensity weighting loss. Achieves competitive performance on CivilComments and MultiNLI without requiring group labels, sometimes matching methods that do use them.\n- **Why it's important:** Accepted at NAACL 2025 (top venue). Connects causal learning to NLP robustness in text classification. Shows that causal feature selection can replace group-label-dependent debiasing methods -- relevant for applying invariance principles to reasoning tasks where spurious correlations are common.\n\n---\n\n### Paper 9: LLM Robustness Survey\n\n- **Full Title:** Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics\n- **Authors:** Pankaj Kumar, Subhankar Mishra\n- **Venue/Year:** Accepted at TMLR (Transactions on Machine Learning Research), 2025\n- **URL:** https://arxiv.org/abs/2505.18658\n- **What it does:** Provides a comprehensive survey categorizing LLM non-robustness sources into intrinsic limitations, data vulnerabilities, and adversarial threats. Reviews mitigation approaches including consistency training, data augmentation, adversarial training, and regularization. Discusses assessment benchmarks and metrics.\n- **Why it's important:** Accepted at TMLR. Provides the broadest recent overview of where consistency regularization fits among other robustness strategies for LLMs. Useful as a reference for positioning any new work in this space.\n\n---\n\n### Paper 10: Enterprise LLM Perturbation Consistency Benchmark\n\n- **Full Title:** Evaluating Robustness of Large Language Models in Enterprise Applications: Benchmarks for Perturbation Consistency Across Formats and Languages\n- **Authors:** Tara Bogavelli, Oluwanifemi Bamgbose, Gabrielle Gauthier Melancon, Fanny Riols, Roshnee Sharma\n- **Venue/Year:** arXiv preprint, January 2026\n- **URL:** https://arxiv.org/abs/2601.06341\n- **What it does:** Benchmarks 11 LLMs (4B to 120B+ parameters) across perturbation types including text edits, formatting changes (JSON, YAML), multilingual inputs, and instruction positioning shifts. Finds minor perturbations can degrade performance by up to 40 percentage points. Notably, model size does not guarantee robustness (an 8B model outperformed most larger models).\n- **Why it's important:** Provides empirical evidence for the scale of the consistency problem in production settings. The finding that model size does not solve perturbation sensitivity motivates training-time solutions like consistency regularization.\n\n---\n\n## Summary of Key Themes\n\n1. **JS/KL divergence regularization** is the dominant technical approach: PPCL uses JS divergence between clean/perturbed outputs; CSR uses KL divergence between original/counterfactual reasoning traces; F2C uses representation alignment losses.\n\n2. **Consistency training outperforms data augmentation**: PPCL shows 10x sample efficiency over augmentation; F2C works fully unsupervised; BCT/ACT work as self-supervised methods.\n\n3. **The accuracy-faithfulness trade-off** is a critical finding: RL fine-tuning can improve accuracy while degrading reasoning consistency (Zhao et al., ICML 2026), motivating joint optimization of correctness and consistency (CSR).\n\n4. **Abstraction as implicit consistency**: AbstRaL (ICLR 2026) shows that teaching models to reason abstractly provides robustness to surface-level perturbations in math problems, connecting abstraction learning to consistency.\n\n5. **Causal/invariant learning foundations**: Invariant Language Modeling (EMNLP 2022) and CCR (NAACL 2025) provide the causal learning foundations that consistency regularization builds upon, applying IRM and counterfactual reasoning to NLP."
      }
    ],
    "totalDurationMs": 166494,
    "totalTokens": 31654,
    "totalToolUseCount": 30,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1360,
      "cache_read_input_tokens": 26989,
      "output_tokens": 3304,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1360
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3304,
          "cache_read_input_tokens": 26989,
          "cache_creation_input_tokens": 1360,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1360,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 30
    }
  },
  "sourceToolAssistantUUID": "e61872b9-2d54-40d1-b34d-458f63602f49",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-29T05:27:09.857Z_

<details><summary>↩ Tool result · `toolu_01B7A1Wfkvop5qwRwy91H3Bw`</summary>

```text
I now have all the information needed. Here is the comprehensive survey.

---

## Literature Survey: Reinforcement Learning for Mathematical Reasoning (2024--2026)

Below are the most important papers, organized by theme. Each entry includes the full abstract details retrieved from arXiv or the publisher.

---

### 1. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

- **Authors:** Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo et al.
- **Venue/Year:** arXiv preprint, February 2024 (arXiv:2402.03300)
- **URL:** https://arxiv.org/abs/2402.03300
- **Abstract summary:** Introduces DeepSeekMath 7B, built by continued pre-training of DeepSeek-Coder-Base-v1.5 7B on 120B math-related tokens from Common Crawl plus natural language and code data. Achieves 51.7% on the competition-level MATH benchmark without external toolkits or voting. The two key contributions are (1) a carefully engineered data selection pipeline for web math data, and (2) **Group Relative Policy Optimization (GRPO)**, a variant of PPO that enhances mathematical reasoning while optimizing memory usage by eliminating the critic model and instead using within-group reward normalization.
- **Why it matters:** This is the **foundational GRPO paper**. GRPO has since become the dominant RL algorithm for math reasoning (adopted by DeepSeek-R1, Qwen2.5-Math, and many others). The insight that you can replace the expensive critic network with group-level baselines transformed the field.

---

### 2. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- **Authors:** DeepSeek-AI (Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, et al.; 199+ contributors)
- **Venue/Year:** arXiv January 2025 (arXiv:2501.12948); published in **Nature** vol. 645, pp. 633--638, 2025
- **URL:** https://arxiv.org/abs/2501.12948
- **Abstract summary:** Demonstrates that reasoning abilities in LLMs can be incentivized through **pure reinforcement learning** without human-labeled reasoning trajectories. Using GRPO on the DeepSeek-V3 671B base model, the resulting R1-Zero model develops sophisticated reasoning behaviors -- self-reflection, verification, and dynamic strategy adaptation -- purely from RL. R1-Zero went from 15.6% to 71.0% on AIME 2024 (comparable to OpenAI o1-0912), and with further refinements (majority voting), reached 86.7%. Distillation of reasoning patterns to smaller models is also demonstrated.
- **Why it matters:** One of the most influential AI papers of 2025. Published in Nature. First open demonstration that **pure RL (no SFT) can elicit advanced reasoning** including self-verification and chain-of-thought. Sparked an enormous wave of follow-up work and open-source replication efforts. Widely considered the open-source counterpart to OpenAI's o1/o3 line of reasoning models.

---

### 3. Let's Verify Step by Step

- **Authors:** Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe (OpenAI)
- **Venue/Year:** arXiv May 2023 (arXiv:2305.20050); published at ICLR 2024
- **URL:** https://arxiv.org/abs/2305.20050
- **Abstract summary:** Compares outcome supervision (feedback on final answers only) vs. process supervision (feedback on each intermediate reasoning step) for training reliable math reasoning. On the MATH dataset, process supervision significantly outperforms outcome supervision: the process-supervised reward model (PRM) solves 78% of problems. Active learning further enhances process supervision. The authors release **PRM800K**, a dataset of 800,000 step-level human correctness labels for model-generated solutions.
- **Why it matters:** The **seminal paper on process reward models (PRMs)** for mathematical reasoning. PRM800K became the standard benchmark dataset for PRM research. Established the process vs. outcome supervision dichotomy that underpins nearly all subsequent reward modeling work in math. From OpenAI, this is widely seen as foundational to the o1/o3 reasoning approach.

---

### 4. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations

- **Authors:** Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, Damai Dai, Yifei Li, Deli Chen, Y. Wu, Zhifang Sui
- **Venue/Year:** arXiv December 2023 (arXiv:2312.08935); published at **ACL 2024**
- **URL:** https://arxiv.org/abs/2312.08935
- **Abstract summary:** Introduces Math-Shepherd, a process reward model that assigns scores to each step of math solutions. Unlike "Let's Verify Step by Step," the training data is **automatically constructed** (no human annotations), breaking the annotation bottleneck. The model is applied in two ways: (1) verification/reranking of multiple LLM outputs, and (2) step-by-step PPO reinforcement learning. With PPO, Mistral-7B improves from 77.9% to 84.1% on GSM8K and 28.6% to 33.0% on MATH; with additional verification, accuracy reaches 89.1% and 43.5% respectively.
- **Why it matters:** Demonstrated that **automated process supervision data** can be nearly as effective as expensive human annotations (from PRM800K), making PRM training scalable. Published at ACL 2024. Highly cited and directly influenced the Qwen and DeepSeek PRM pipelines.

---

### 5. AlphaProof: Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning

- **Authors:** Thomas Hubert, Rishi Mehta, Laurent Sartran, Miklos Z. Horvath, Goran Zuzic, Eric Wieser, Aja Huang, Julian Schrittwieser, ..., Demis Hassabis, Pushmeet Kohli, David Silver (Google DeepMind)
- **Venue/Year:** Published in **Nature**, vol. 651, pp. 607--613 (published online November 12, 2025)
- **URL:** https://www.nature.com/articles/s41586-025-09833-y
- **Abstract summary:** Presents AlphaProof, an AlphaZero-inspired system that combines reinforcement learning with formal verification in the Lean theorem prover. Trained on approximately 80 million auto-formalized problems, it uses tree search and **test-time reinforcement learning** (generating and learning from millions of problem variants at inference) to solve olympiad-level problems. At the 2024 International Mathematical Olympiad, AlphaProof solved 3 of 5 non-geometry problems, and combined with AlphaGeometry 2, achieved a **silver-medal equivalent score** -- the first AI medal-level performance in IMO history.
- **Why it matters:** Historic milestone -- first AI to achieve medal-level performance at the IMO. Published in Nature. Demonstrates a fundamentally different RL paradigm (formal verification + tree search + test-time RL) compared to the GRPO/PPO approaches used for informal reasoning. Shows that RL can scale to the hardest mathematical reasoning tasks when grounded in formal proof environments.

---

### 6. PRIME: Process Reinforcement through Implicit Rewards

- **Authors:** Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Jiacheng Chen, Wendi Li, Bingxiang He, ..., Zhiyuan Liu, Maosong Sun, Bowen Zhou, Ning Ding
- **Venue/Year:** arXiv February 2025 (arXiv:2502.01456)
- **URL:** https://arxiv.org/abs/2502.01456
- **Abstract summary:** Proposes PRIME (Process Reinforcement through IMplicit rEwards), which enables online PRM updates using only policy rollouts and outcome labels -- no explicit process-level annotations or dedicated reward model training required. Implicit process rewards are derived directly from the policy. Starting from Qwen2.5-Math-7B-Base, PRIME achieves a 15.1% average improvement across key reasoning benchmarks. The resulting Eurus-2-7B-PRIME surpasses Qwen2.5-Math-7B-Instruct on seven reasoning benchmarks using only 10% of its training data.
- **Why it matters:** Bridges the gap between process and outcome reward models by showing you can get dense process-level credit assignment **implicitly** from outcome signals alone. Eliminates the expensive PRM training pipeline. Highly practical -- enables process-level RL without any step-level annotations.

---

### 7. The Lessons of Developing Process Reward Models in Mathematical Reasoning

- **Authors:** Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin (Qwen/Alibaba team)
- **Venue/Year:** arXiv January 2025 (arXiv:2501.07301); published at ACL 2025 Findings
- **URL:** https://arxiv.org/abs/2501.07301
- **Abstract summary:** Systematically investigates challenges in PRM development. Demonstrates that Monte Carlo estimation-based data synthesis yields inferior performance compared to LLM-as-a-judge and human annotation methods. Reveals biases in Best-of-N evaluation strategies and proposes a consensus filtering mechanism integrating MC estimation with LLM-as-a-judge. Provides a comprehensive evaluation framework combining response-level and step-level metrics, resulting in a new state-of-the-art PRM with practical guidelines.
- **Why it matters:** The most comprehensive empirical study of PRM development pitfalls. From the Qwen team (who build one of the most widely used math reasoning model families). Provides actionable lessons that have influenced how the community trains and evaluates PRMs.

---

### 8. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement

- **Authors:** An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, Zhenru Zhang (Alibaba/Qwen team)
- **Venue/Year:** arXiv September 2024 (arXiv:2409.12122)
- **URL:** https://arxiv.org/abs/2409.12122
- **Abstract summary:** Presents Qwen2.5-Math and Qwen2.5-Math-Instruct (1.5B/7B/72B), integrating self-improvement throughout the entire pipeline. Pre-training uses prior models to generate large-scale math data; post-training develops reward models via massive sampling for iterative SFT data evolution and RL; inference uses reward models to optimize sampling. Supports bilingual (English/Chinese) with Chain-of-Thought and Tool-Integrated Reasoning. Evaluated on 10 math benchmarks from elementary to competition level (GSM8K, MATH, GaoKao, AMC23, AIME24).
- **Why it matters:** One of the strongest open-source math reasoning model families. Demonstrates the full **self-improvement loop** (pre-train -> reward model -> iterative SFT + RL -> inference-time reward guidance). The 72B model is competitive with frontier closed-source models on competition math. Widely used as a base model for subsequent RL research (including PRIME, GRPO variants, etc.).

---

### 9. Adversarial Training for Process Reward Models (APRM)

- **Authors:** Gurusha Juneja, Deepak Nathani, William Yang Wang
- **Venue/Year:** arXiv November 2025 (arXiv:2511.22888)
- **URL:** https://arxiv.org/abs/2511.22888
- **Abstract summary:** Introduces Adversarially Trained PRMs (APRM), where a Generator learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them. This adversarial interaction yields progressively harder negative examples, improving PRM robustness and generalization to novel errors without manual step-level labels. APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline across mathematical reasoning benchmarks, with +5.3 pp gains on out-of-distribution tasks.
- **Why it matters:** Novel approach to PRM training that addresses a fundamental weakness -- static training data leads to poor generalization. The adversarial framework generates increasingly difficult error patterns, making the PRM robust to unseen error types. Directly relevant to making reward-guided mathematical reasoning more reliable.

---

### 10. Reinforcement Learning for Reasoning in Large Language Models with One Training Example

- **Authors:** Yiping Wang, Qing Yang, Zhiyuan Zeng, Liliang Ren, Liyuan Liu, Baolin Peng, Hao Cheng, Xuehai He, Kuan Wang, Jianfeng Gao, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, Yelong Shen
- **Venue/Year:** arXiv April 2025 (arXiv:2504.20571)
- **URL:** https://arxiv.org/abs/2504.20571
- **Abstract summary:** Demonstrates that RL with verifiable rewards using a **single training example** effectively enhances mathematical reasoning. Applied to Qwen2.5-Math-1.5B, performance on MATH500 jumps from 36.0% to 73.6%, and across six benchmarks from 17.6% to 35.7% -- matching results from training sets with 1.2k examples. Identifies "cross-category generalization" and "post-saturation generalization" phenomena. Gains come from policy gradient mechanisms rather than grokking, with exploration being critical.
- **Why it matters:** A surprising and provocative result showing that **a single example suffices** for RL to unlock mathematical reasoning. Challenges assumptions about data requirements for RL post-training and suggests that RL's benefit comes primarily from enabling exploration and policy optimization, not from the training data distribution itself.

---

### 11. Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning

- **Authors:** Zelin Tan, Hejia Geng, Xiaohang Yu, Mulei Zhang, Guancheng Wan, Yifan Zhou, Qiang He, et al.
- **Venue/Year:** arXiv September 2025 (arXiv:2509.25300); accepted to **ACL 2026**
- **URL:** https://arxiv.org/abs/2509.25300
- **Abstract summary:** Systematically studies scaling dynamics of RL post-training for math reasoning using the full Qwen2.5 family (0.5B to 72B). Establishes a predictive power-law relationship between model capacity, training data, and compute. Key findings: larger models have superior learning efficiency; there is a latent saturation trend as model size increases; repeated reuse of high-quality data is highly effective in data-limited regimes.
- **Why it matters:** First comprehensive scaling laws study for RL post-training in math. Accepted at ACL 2026. Provides practical guidance on how to allocate compute, data, and model capacity for RL training -- essential for anyone training reasoning models.

---

### Summary Table

| # | Paper | Key Contribution | Year | Venue |
|---|-------|-----------------|------|-------|
| 1 | DeepSeekMath | Introduced GRPO algorithm | 2024 | arXiv |
| 2 | DeepSeek-R1 | Pure RL for reasoning (no SFT) | 2025 | Nature |
| 3 | Let's Verify Step by Step | Process vs. outcome reward models + PRM800K | 2023/2024 | ICLR 2024 |
| 4 | Math-Shepherd | Automated process supervision + step-level PPO | 2023/2024 | ACL 2024 |
| 5 | AlphaProof | IMO silver medal via formal RL | 2025 | Nature |
| 6 | PRIME | Implicit process rewards from outcome signals | 2025 | arXiv |
| 7 | Lessons of Developing PRMs | Comprehensive PRM development study | 2025 | ACL 2025 |
| 8 | Qwen2.5-Math | Self-improvement loop for math models | 2024 | arXiv |
| 9 | APRM | Adversarial training for robust PRMs | 2025 | arXiv |
| 10 | RL with One Example | Single-example RL matches full-dataset RL | 2025 | arXiv |
| 11 | Scaling Behaviors of RL Post-Training | Scaling laws for RL math training | 2025/2026 | ACL 2026 |

These 11 papers cover the core themes: the GRPO algorithm and its origin (papers 1, 2), process vs. outcome reward modeling (papers 3, 4, 6, 7, 9), RL training paradigms for math reasoning (papers 2, 5, 8, 10), and scaling/efficiency of RL post-training (papers 10, 11). Together they represent the most influential work in RL for mathematical reasoning from 2024--2026.

agentId: aaa15cbe6d5012e05 (use SendMessage with to: 'aaa15cbe6d5012e05' to continue this agent)
&lt;usage>total_tokens: 30932
tool_uses: 26
duration_ms: 200799&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "385b02db-cb56-4b0f-b0ff-1fff169ff965",
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "98ddf509-5965-481c-b8b6-b7f7e929cada",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey on reinforcement learning for mathematical reasoning. Search for the most important papers (2024-2026) on:\n\n1. GRPO (Group Relative Policy Optimization) for math reasoning\n2. RL training for mathematical reasoning (DeepSeek-R1, OpenAI o1/o3 related work)\n3. PPO/RLHF applied to mathematical problem solving\n4. Reward modeling for math (process reward models, outcome reward models)\n\nExecute these searches and for EVERY promising paper, fetch its arXiv abstract:\n\nSearch 1: \"GRPO group relative policy optimization mathematical reasoning 2025 2026\"\nSearch 2: \"DeepSeek-R1 reinforcement learning reasoning 2025\"\nSearch 3: \"reinforcement learning mathematical reasoning training 2025 2026\"\nSearch 4: \"process reward model mathematical reasoning 2024 2025\"\nSearch 5: \"RLHF math reasoning chain of thought 2025\"\nSearch 6: \"adversarial process reward model APRM reasoning errors 2025\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract and key details. Report back with:\n- Full title\n- Authors (first author et al.)\n- Venue/year\n- URL\n- What the paper does (1-2 sentences)\n- Why it's important (awards, citations, influence)\n\nFind at least 5-8 distinct papers. Focus on papers that are highly cited, have best paper awards, or introduced widely-adopted methods (like GRPO, DeepSeek-R1, etc.).",
    "agentId": "aaa15cbe6d5012e05",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the information needed. Here is the comprehensive survey.\n\n---\n\n## Literature Survey: Reinforcement Learning for Mathematical Reasoning (2024--2026)\n\nBelow are the most important papers, organized by theme. Each entry includes the full abstract details retrieved from arXiv or the publisher.\n\n---\n\n### 1. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\n\n- **Authors:** Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y.K. Li, Y. Wu, Daya Guo et al.\n- **Venue/Year:** arXiv preprint, February 2024 (arXiv:2402.03300)\n- **URL:** https://arxiv.org/abs/2402.03300\n- **Abstract summary:** Introduces DeepSeekMath 7B, built by continued pre-training of DeepSeek-Coder-Base-v1.5 7B on 120B math-related tokens from Common Crawl plus natural language and code data. Achieves 51.7% on the competition-level MATH benchmark without external toolkits or voting. The two key contributions are (1) a carefully engineered data selection pipeline for web math data, and (2) **Group Relative Policy Optimization (GRPO)**, a variant of PPO that enhances mathematical reasoning while optimizing memory usage by eliminating the critic model and instead using within-group reward normalization.\n- **Why it matters:** This is the **foundational GRPO paper**. GRPO has since become the dominant RL algorithm for math reasoning (adopted by DeepSeek-R1, Qwen2.5-Math, and many others). The insight that you can replace the expensive critic network with group-level baselines transformed the field.\n\n---\n\n### 2. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\n\n- **Authors:** DeepSeek-AI (Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, et al.; 199+ contributors)\n- **Venue/Year:** arXiv January 2025 (arXiv:2501.12948); published in **Nature** vol. 645, pp. 633--638, 2025\n- **URL:** https://arxiv.org/abs/2501.12948\n- **Abstract summary:** Demonstrates that reasoning abilities in LLMs can be incentivized through **pure reinforcement learning** without human-labeled reasoning trajectories. Using GRPO on the DeepSeek-V3 671B base model, the resulting R1-Zero model develops sophisticated reasoning behaviors -- self-reflection, verification, and dynamic strategy adaptation -- purely from RL. R1-Zero went from 15.6% to 71.0% on AIME 2024 (comparable to OpenAI o1-0912), and with further refinements (majority voting), reached 86.7%. Distillation of reasoning patterns to smaller models is also demonstrated.\n- **Why it matters:** One of the most influential AI papers of 2025. Published in Nature. First open demonstration that **pure RL (no SFT) can elicit advanced reasoning** including self-verification and chain-of-thought. Sparked an enormous wave of follow-up work and open-source replication efforts. Widely considered the open-source counterpart to OpenAI's o1/o3 line of reasoning models.\n\n---\n\n### 3. Let's Verify Step by Step\n\n- **Authors:** Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe (OpenAI)\n- **Venue/Year:** arXiv May 2023 (arXiv:2305.20050); published at ICLR 2024\n- **URL:** https://arxiv.org/abs/2305.20050\n- **Abstract summary:** Compares outcome supervision (feedback on final answers only) vs. process supervision (feedback on each intermediate reasoning step) for training reliable math reasoning. On the MATH dataset, process supervision significantly outperforms outcome supervision: the process-supervised reward model (PRM) solves 78% of problems. Active learning further enhances process supervision. The authors release **PRM800K**, a dataset of 800,000 step-level human correctness labels for model-generated solutions.\n- **Why it matters:** The **seminal paper on process reward models (PRMs)** for mathematical reasoning. PRM800K became the standard benchmark dataset for PRM research. Established the process vs. outcome supervision dichotomy that underpins nearly all subsequent reward modeling work in math. From OpenAI, this is widely seen as foundational to the o1/o3 reasoning approach.\n\n---\n\n### 4. Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\n\n- **Authors:** Peiyi Wang, Lei Li, Zhihong Shao, R.X. Xu, Damai Dai, Yifei Li, Deli Chen, Y. Wu, Zhifang Sui\n- **Venue/Year:** arXiv December 2023 (arXiv:2312.08935); published at **ACL 2024**\n- **URL:** https://arxiv.org/abs/2312.08935\n- **Abstract summary:** Introduces Math-Shepherd, a process reward model that assigns scores to each step of math solutions. Unlike \"Let's Verify Step by Step,\" the training data is **automatically constructed** (no human annotations), breaking the annotation bottleneck. The model is applied in two ways: (1) verification/reranking of multiple LLM outputs, and (2) step-by-step PPO reinforcement learning. With PPO, Mistral-7B improves from 77.9% to 84.1% on GSM8K and 28.6% to 33.0% on MATH; with additional verification, accuracy reaches 89.1% and 43.5% respectively.\n- **Why it matters:** Demonstrated that **automated process supervision data** can be nearly as effective as expensive human annotations (from PRM800K), making PRM training scalable. Published at ACL 2024. Highly cited and directly influenced the Qwen and DeepSeek PRM pipelines.\n\n---\n\n### 5. AlphaProof: Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning\n\n- **Authors:** Thomas Hubert, Rishi Mehta, Laurent Sartran, Miklos Z. Horvath, Goran Zuzic, Eric Wieser, Aja Huang, Julian Schrittwieser, ..., Demis Hassabis, Pushmeet Kohli, David Silver (Google DeepMind)\n- **Venue/Year:** Published in **Nature**, vol. 651, pp. 607--613 (published online November 12, 2025)\n- **URL:** https://www.nature.com/articles/s41586-025-09833-y\n- **Abstract summary:** Presents AlphaProof, an AlphaZero-inspired system that combines reinforcement learning with formal verification in the Lean theorem prover. Trained on approximately 80 million auto-formalized problems, it uses tree search and **test-time reinforcement learning** (generating and learning from millions of problem variants at inference) to solve olympiad-level problems. At the 2024 International Mathematical Olympiad, AlphaProof solved 3 of 5 non-geometry problems, and combined with AlphaGeometry 2, achieved a **silver-medal equivalent score** -- the first AI medal-level performance in IMO history.\n- **Why it matters:** Historic milestone -- first AI to achieve medal-level performance at the IMO. Published in Nature. Demonstrates a fundamentally different RL paradigm (formal verification + tree search + test-time RL) compared to the GRPO/PPO approaches used for informal reasoning. Shows that RL can scale to the hardest mathematical reasoning tasks when grounded in formal proof environments.\n\n---\n\n### 6. PRIME: Process Reinforcement through Implicit Rewards\n\n- **Authors:** Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, Yuchen Zhang, Jiacheng Chen, Wendi Li, Bingxiang He, ..., Zhiyuan Liu, Maosong Sun, Bowen Zhou, Ning Ding\n- **Venue/Year:** arXiv February 2025 (arXiv:2502.01456)\n- **URL:** https://arxiv.org/abs/2502.01456\n- **Abstract summary:** Proposes PRIME (Process Reinforcement through IMplicit rEwards), which enables online PRM updates using only policy rollouts and outcome labels -- no explicit process-level annotations or dedicated reward model training required. Implicit process rewards are derived directly from the policy. Starting from Qwen2.5-Math-7B-Base, PRIME achieves a 15.1% average improvement across key reasoning benchmarks. The resulting Eurus-2-7B-PRIME surpasses Qwen2.5-Math-7B-Instruct on seven reasoning benchmarks using only 10% of its training data.\n- **Why it matters:** Bridges the gap between process and outcome reward models by showing you can get dense process-level credit assignment **implicitly** from outcome signals alone. Eliminates the expensive PRM training pipeline. Highly practical -- enables process-level RL without any step-level annotations.\n\n---\n\n### 7. The Lessons of Developing Process Reward Models in Mathematical Reasoning\n\n- **Authors:** Zhenru Zhang, Chujie Zheng, Yangzhen Wu, Beichen Zhang, Runji Lin, Bowen Yu, Dayiheng Liu, Jingren Zhou, Junyang Lin (Qwen/Alibaba team)\n- **Venue/Year:** arXiv January 2025 (arXiv:2501.07301); published at ACL 2025 Findings\n- **URL:** https://arxiv.org/abs/2501.07301\n- **Abstract summary:** Systematically investigates challenges in PRM development. Demonstrates that Monte Carlo estimation-based data synthesis yields inferior performance compared to LLM-as-a-judge and human annotation methods. Reveals biases in Best-of-N evaluation strategies and proposes a consensus filtering mechanism integrating MC estimation with LLM-as-a-judge. Provides a comprehensive evaluation framework combining response-level and step-level metrics, resulting in a new state-of-the-art PRM with practical guidelines.\n- **Why it matters:** The most comprehensive empirical study of PRM development pitfalls. From the Qwen team (who build one of the most widely used math reasoning model families). Provides actionable lessons that have influenced how the community trains and evaluates PRMs.\n\n---\n\n### 8. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement\n\n- **Authors:** An Yang, Beichen Zhang, Binyuan Hui, Bofei Gao, Bowen Yu, Chengpeng Li, Dayiheng Liu, Jianhong Tu, Jingren Zhou, Junyang Lin, Keming Lu, Mingfeng Xue, Runji Lin, Tianyu Liu, Xingzhang Ren, Zhenru Zhang (Alibaba/Qwen team)\n- **Venue/Year:** arXiv September 2024 (arXiv:2409.12122)\n- **URL:** https://arxiv.org/abs/2409.12122\n- **Abstract summary:** Presents Qwen2.5-Math and Qwen2.5-Math-Instruct (1.5B/7B/72B), integrating self-improvement throughout the entire pipeline. Pre-training uses prior models to generate large-scale math data; post-training develops reward models via massive sampling for iterative SFT data evolution and RL; inference uses reward models to optimize sampling. Supports bilingual (English/Chinese) with Chain-of-Thought and Tool-Integrated Reasoning. Evaluated on 10 math benchmarks from elementary to competition level (GSM8K, MATH, GaoKao, AMC23, AIME24).\n- **Why it matters:** One of the strongest open-source math reasoning model families. Demonstrates the full **self-improvement loop** (pre-train -> reward model -> iterative SFT + RL -> inference-time reward guidance). The 72B model is competitive with frontier closed-source models on competition math. Widely used as a base model for subsequent RL research (including PRIME, GRPO variants, etc.).\n\n---\n\n### 9. Adversarial Training for Process Reward Models (APRM)\n\n- **Authors:** Gurusha Juneja, Deepak Nathani, William Yang Wang\n- **Venue/Year:** arXiv November 2025 (arXiv:2511.22888)\n- **URL:** https://arxiv.org/abs/2511.22888\n- **Abstract summary:** Introduces Adversarially Trained PRMs (APRM), where a Generator learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them. This adversarial interaction yields progressively harder negative examples, improving PRM robustness and generalization to novel errors without manual step-level labels. APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline across mathematical reasoning benchmarks, with +5.3 pp gains on out-of-distribution tasks.\n- **Why it matters:** Novel approach to PRM training that addresses a fundamental weakness -- static training data leads to poor generalization. The adversarial framework generates increasingly difficult error patterns, making the PRM robust to unseen error types. Directly relevant to making reward-guided mathematical reasoning more reliable.\n\n---\n\n### 10. Reinforcement Learning for Reasoning in Large Language Models with One Training Example\n\n- **Authors:** Yiping Wang, Qing Yang, Zhiyuan Zeng, Liliang Ren, Liyuan Liu, Baolin Peng, Hao Cheng, Xuehai He, Kuan Wang, Jianfeng Gao, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, Yelong Shen\n- **Venue/Year:** arXiv April 2025 (arXiv:2504.20571)\n- **URL:** https://arxiv.org/abs/2504.20571\n- **Abstract summary:** Demonstrates that RL with verifiable rewards using a **single training example** effectively enhances mathematical reasoning. Applied to Qwen2.5-Math-1.5B, performance on MATH500 jumps from 36.0% to 73.6%, and across six benchmarks from 17.6% to 35.7% -- matching results from training sets with 1.2k examples. Identifies \"cross-category generalization\" and \"post-saturation generalization\" phenomena. Gains come from policy gradient mechanisms rather than grokking, with exploration being critical.\n- **Why it matters:** A surprising and provocative result showing that **a single example suffices** for RL to unlock mathematical reasoning. Challenges assumptions about data requirements for RL post-training and suggests that RL's benefit comes primarily from enabling exploration and policy optimization, not from the training data distribution itself.\n\n---\n\n### 11. Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning\n\n- **Authors:** Zelin Tan, Hejia Geng, Xiaohang Yu, Mulei Zhang, Guancheng Wan, Yifan Zhou, Qiang He, et al.\n- **Venue/Year:** arXiv September 2025 (arXiv:2509.25300); accepted to **ACL 2026**\n- **URL:** https://arxiv.org/abs/2509.25300\n- **Abstract summary:** Systematically studies scaling dynamics of RL post-training for math reasoning using the full Qwen2.5 family (0.5B to 72B). Establishes a predictive power-law relationship between model capacity, training data, and compute. Key findings: larger models have superior learning efficiency; there is a latent saturation trend as model size increases; repeated reuse of high-quality data is highly effective in data-limited regimes.\n- **Why it matters:** First comprehensive scaling laws study for RL post-training in math. Accepted at ACL 2026. Provides practical guidance on how to allocate compute, data, and model capacity for RL training -- essential for anyone training reasoning models.\n\n---\n\n### Summary Table\n\n| # | Paper | Key Contribution | Year | Venue |\n|---|-------|-----------------|------|-------|\n| 1 | DeepSeekMath | Introduced GRPO algorithm | 2024 | arXiv |\n| 2 | DeepSeek-R1 | Pure RL for reasoning (no SFT) | 2025 | Nature |\n| 3 | Let's Verify Step by Step | Process vs. outcome reward models + PRM800K | 2023/2024 | ICLR 2024 |\n| 4 | Math-Shepherd | Automated process supervision + step-level PPO | 2023/2024 | ACL 2024 |\n| 5 | AlphaProof | IMO silver medal via formal RL | 2025 | Nature |\n| 6 | PRIME | Implicit process rewards from outcome signals | 2025 | arXiv |\n| 7 | Lessons of Developing PRMs | Comprehensive PRM development study | 2025 | ACL 2025 |\n| 8 | Qwen2.5-Math | Self-improvement loop for math models | 2024 | arXiv |\n| 9 | APRM | Adversarial training for robust PRMs | 2025 | arXiv |\n| 10 | RL with One Example | Single-example RL matches full-dataset RL | 2025 | arXiv |\n| 11 | Scaling Behaviors of RL Post-Training | Scaling laws for RL math training | 2025/2026 | ACL 2026 |\n\nThese 11 papers cover the core themes: the GRPO algorithm and its origin (papers 1, 2), process vs. outcome reward modeling (papers 3, 4, 6, 7, 9), RL training paradigms for math reasoning (papers 2, 5, 8, 10), and scaling/efficiency of RL post-training (papers 10, 11). Together they represent the most influential work in RL for mathematical reasoning from 2024--2026."
      }
    ],
    "totalDurationMs": 200799,
    "totalTokens": 30932,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 455,
      "cache_read_input_tokens": 25986,
      "output_tokens": 4490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 455
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4490,
          "cache_read_input_tokens": 25986,
          "cache_creation_input_tokens": 455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 455,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 26
    }
  },
  "sourceToolAssistantUUID": "385b02db-cb56-4b0f-b0ff-1fff169ff965",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "98ddf509-5965-481c-b8b6-b7f7e929cada",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct literature survey on RL math reasoning robustness",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Assistant

_source line 31 · 2026-05-29T05:28:29.202Z_

<details><summary>Logged reasoning block</summary>

```text
I now have a comprehensive set of papers from all five search agents. Let me consolidate and synthesize the findings, then do some additional targeted searches to fill any gaps. Let me identify the key papers that are most relevant to the MACR proposal:

From Agent 1 (Math reasoning robustness):
1. GSM-Symbolic (ICLR 2025) - already a seed paper
2. GSM-Plus (ACL 2024) - benchmark
3. MATH-Perturb (arXiv 2025) - benchmark


4. VAR-MATH (arXiv 2025) - already a seed paper
5. PutnamGAP (arXiv 2025) - new, interesting
6. RRB (arXiv 2026) - new
7. Numerical Sensitivity (arXiv 2025)
8. Math-RoB (arXiv 2025)
9. RIDE (arXiv 2025)
10. MathRobust-LV (arXiv 2025)
11. AbstRaL (ICLR 2026) - already a seed paper
12. LogicPuzzleRL (appears to be cut off)
13. SPARKLE (NeurIPS 2025)

Now looking at the RL approaches for math reasoning, starting with foundational work like DeepSeekMath and the highly impactful DeepSeek-R1, then moving through process reward models like the ICLR paper and Math-Shepherd, up to recent developments including AlphaProof's IMO breakthrough and various 2025 papers exploring implicit rewards and best practices.

For consistency regularization, I'm seeing several seed papers already identified, along with newer work on robustness in vision-language models and invariant language modeling approaches, with some overlap to filter out.

From the best papers and awards category, there's a strong emphasis on reasoning—particularly that NeurIPS runner-up questioning whether RL actually incentivizes reasoning, which seems crucial. The other award winners are less directly relevant to my focus, though the ICLR oral on reasoning with sampling could be useful.

Now looking at the data augmentation and invariance papers, I'm seeing some duplicates I've already noted, but DeepSeekMath-V2 stands out as genuinely new and interesting. The focus on test-time scaling through s1 and paraphrasing approaches aligns well with what I'm tracking.

I need to step back and think about what actually matters for the MACR proposal—the 15 most impactful papers should balance foundational work with recent breakthroughs, focusing on quality and relevance rather than just novelty. The seed papers are already known, so I should prioritize the strongest new discoveries alongside the most essential established work. Continuing through the key papers on robustness and consistency—there's work on surface form sensitivity, consistency training approaches from DeepMind, and research showing that test-time scaling and RL fine-tuning have interesting tradeoffs with model consistency. I'm realizing I should narrow my focus here rather than listing everything.

Let me zero in on what's most directly relevant to the MACR proposal: papers demonstrating robustness problems, RL approaches for math reasoning, consistency regularization techniques, process reward models, and how data augmentation compares to consistency-based methods. I should also check for recent work on Invariant Risk Minimization applied to reasoning, GRPO improvements from 2025-2026, and competition math benchmarks. Actually, I think I have enough to work with now. I'll compile the final list carefully, making sure to include recent papers from 2024-2026 while excluding the seed papers the user already knows about.

Wait—re-reading the task, it asks for the 15 most important recent papers in this research area, but the user has already given me seed papers. They're probably looking for 15 additional papers beyond those seeds, not a replacement list. So I should focus on new discoveries rather than including foundational work like DeepSeek-R1 unless it's truly essential. Let me build my top 15 excluding those 7 seed papers and prioritize papers with strong venue placement, citations, or awards.

Now I'm compiling my final list: DeepSeek-R1 from Nature 2025 for its pure RL approach to reasoning, the GRPO algorithm paper introducing a key training method, the NeurIPS 2025 runner-up that critically examines whether RL actually improves reasoning, followed by several process reward model papers like the ICLR 2024 verification work and ACL 2024's Math-Shepherd, then newer approaches like implicit process rewards and robustness benchmarks ranging from GSM-Plus to competition-level perturbations and the Putnam difficulty benchmark, plus the NAACL 2024 paraphrase work.

I'm also adding consistency training from DeepMind, the ICLR 2026 oral on reasoning with sampling, Qwen2.5-Math as a base model reference, Apple's ICML 2026 work showing RL can hurt consistency, and ACL 2026's scaling laws for RL math post-training. I should definitely include s1's test-time scaling work from EMNLP 2025 since it's directly relevant to compute allocation, and AlphaProof from Nature 2025 for its formal verification approach.

Now I'm narrowing down to the 15 most critical papers specifically for the MACR proposal. Since the core contribution is about surface-form robustness through consistency regularization during RL training, I need papers that directly address robustness failures, RL training dynamics, and math-specific perturbations. GSM-Plus is essential for establishing the perturbation vulnerability problem, and I should prioritize papers on adversarial RL for reasoning, confidence limiting during fine-tuning, and surprising findings about minimal-example RL training. - Robustness of RL-Finetuned VLMs (ICML 2026) - RL can actually hurt consistency

Now I'm looking at related methods like process reward models and adversarial approaches, plus scaling laws for RL. I need to narrow this down to fifteen papers with the strongest coverage, so I'm keeping the foundational DeepSeek work and cutting the less directly relevant ones.

My core selections are DeepSeek-R1, DeepSeekMath with GRPO, the NeurIPS best paper runner-up on whether RL really incentivizes reasoning, and the PRM foundation from Let's Verify Step by Step. I'm also including robustness benchmarks like GSM-Plus and MATH-Perturb, plus PutnamGAP for the highest difficulty cases. For surface form sensitivity I have Paraphrase and Solve, and I'm keeping PRIME for implicit reward modeling and a consistency training paper from DeepMind. Reasoning with Sampling challenges the necessity of RL, and I'm still deciding on the final few slots.

I'm reconsidering whether to include the Generative Adversarial Reasoner and the "RL with One Example" paper since they're quite relevant, but my current list of 15 feels solid. Let me finalize this and move forward with compiling the full analysis.

Actually, I need to be careful here—the user's seed papers already include GSM-Symbolic, VAR-MATH, AbstRaL, F²C, PPCL, CSR, and APRM, so I should exclude those and find 15 papers beyond these. Let me lock in my final selection starting with DeepSeek-R1, DeepSeekMath with GRPO, and continuing from there. Adding a few more key papers on RL approaches and robustness, then I'll verify the details on that DeepMind consistency training paper before compiling everything into JSON format. I'm reconsidering whether to keep "Paraphrase and Solve" since it does establish the problem of surface form sensitivity, even though it's inference-time rather than training-time. I'll stick with the final 15-paper list: the three core RL papers (DeepSeek-R1, DeepSeekMath, and the RL incentives analysis), four robustness benchmarks, four papers on reasoning verification and sampling, plus the consistency training work, Qwen2.5-Math, the VLM robustness study, and scaling behaviors—covering the full landscape from RL approaches to robustness evaluation to training-time consistency.

Let me do one more targeted search to verify I haven't missed anything critical on consistency regularization.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ddf509-5965-481c-b8b6-b7f7e929cada",
  "isSidechain": false,
  "requestId": "req_011CbWJigCuNUTe1VA3cuiGp",
  "type": "assistant",
  "uuid": "0b545353-3c85-4cb4-bee0-411225c7ee31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8DcDvPM4SQB277hZfA8V2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9655,
      "cache_creation_input_tokens": 10716,
      "cache_read_input_tokens": 17038,
      "output_tokens": 5979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9655,
          "output_tokens": 5979,
          "cache_read_input_tokens": 17038,
          "cache_creation_input_tokens": 10716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10716
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

_source line 32 · 2026-05-29T05:28:29.353Z_

Now let me run a few more targeted searches to fill potential gaps, especially around consistency regularization applied to RL and any very recent 2026 papers I might have missed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b545353-3c85-4cb4-bee0-411225c7ee31",
  "isSidechain": false,
  "requestId": "req_011CbWJigCuNUTe1VA3cuiGp",
  "type": "assistant",
  "uuid": "4c155f11-2d07-4895-8852-e301d7e694a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8DcDvPM4SQB277hZfA8V2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9655,
      "cache_creation_input_tokens": 10716,
      "cache_read_input_tokens": 17038,
      "output_tokens": 5979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9655,
          "output_tokens": 5979,
          "cache_read_input_tokens": 17038,
          "cache_creation_input_tokens": 10716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10716
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

_source line 33 · 2026-05-29T05:28:36.845Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01EeXaMV16XZnq5Mn3BkNWRn`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search: Consistency reg + RL gap",
  "prompt": "You are helping with a literature survey. I need to verify that NO paper has applied consistency regularization (JS/KL divergence between equivalent inputs) during RL training for mathematical reasoning. Also search for any papers that combine data augmentation with RL for math reasoning robustness.\n\nExecute these searches and fetch arXiv abstracts for any promising papers:\n\nSearch 1: \"consistency regularization reinforcement learning mathematical reasoning\"\nSearch 2: \"JS divergence KL divergence RL training math reasoning robustness\"\nSearch 3: \"invariance regularization GRPO PPO mathematical reasoning\"\nSearch 4: \"perturbation invariance training mathematical reasoning LLM 2025 2026\"\nSearch 5: \"data augmentation reinforcement learning math reasoning robustness 2025\"\nSearch 6: \"equivalent problem variants training mathematical reasoning\"\nSearch 7: \"surface form invariance mathematical reasoning training\"\nSearch 8: \"consistency loss RL fine-tuning reasoning 2025 2026\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract. Report:\n- Full title, authors, venue, URL\n- What it does (1-2 sentences)\n- Whether it applies consistency regularization during RL training specifically\n\nThis is critical: I need to know if the gap \"no one has applied consistency regularization during RL training for math reasoning\" still holds as of May 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c155f11-2d07-4895-8852-e301d7e694a1",
  "isSidechain": false,
  "requestId": "req_011CbWJigCuNUTe1VA3cuiGp",
  "type": "assistant",
  "uuid": "868e9c9a-4fac-4fa4-8a94-53ab2bd84b2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8DcDvPM4SQB277hZfA8V2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9655,
      "cache_creation_input_tokens": 10716,
      "cache_read_input_tokens": 17038,
      "output_tokens": 5979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9655,
          "output_tokens": 5979,
          "cache_read_input_tokens": 17038,
          "cache_creation_input_tokens": 10716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10716
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

_source line 34 · 2026-05-29T05:28:44.041Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JoC7e3BDkFgMyqyrAEXars`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search: Key paper verification",
  "prompt": "I need to verify details and fetch abstracts for several specific papers that came up in a literature survey. For EACH of the following, search for and fetch the arXiv abstract page to confirm details:\n\n1. \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\" - should be NeurIPS 2025\n   URL: https://arxiv.org/abs/2504.13837\n\n2. \"Consistency Training Helps Stop Sycophancy and Jailbreaks\" by Irpan et al. (Google DeepMind)\n   URL: https://arxiv.org/abs/2510.27062\n\n3. \"PRIME: Process Reinforcement through Implicit Rewards\"\n   URL: https://arxiv.org/abs/2502.01456\n\n4. \"PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning\"\n   URL: https://arxiv.org/abs/2508.08833\n\n5. \"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\" (Apple, ICML 2026)\n   URL: https://arxiv.org/abs/2602.12506\n\n6. \"Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning\" (NAACL 2024)\n   URL: https://arxiv.org/abs/2404.11500\n\nFor each, use WebFetch to get the abstract and confirm: title, authors, venue, year, and a one-sentence summary. Report any discrepancies or papers that don't exist."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "868e9c9a-4fac-4fa4-8a94-53ab2bd84b2a",
  "isSidechain": false,
  "requestId": "req_011CbWJigCuNUTe1VA3cuiGp",
  "type": "assistant",
  "uuid": "3b18dae9-e67f-445b-a088-8c24301872ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F8DcDvPM4SQB277hZfA8V2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 9655,
      "cache_creation_input_tokens": 10716,
      "cache_read_input_tokens": 17038,
      "output_tokens": 5979,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10716,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 9655,
          "output_tokens": 5979,
          "cache_read_input_tokens": 17038,
          "cache_creation_input_tokens": 10716,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10716
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "3b18dae9-e67f-445b-a088-8c24301872ee",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct literature survey on RL math reasoning robustness",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Tool result

_source line 37 · 2026-05-29T05:29:33.213Z_

<details><summary>↩ Tool result · `toolu_01JoC7e3BDkFgMyqyrAEXars`</summary>

```text
Here is the verification report for all six papers:

---

**Paper 1: "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?"**
- **URL:** https://arxiv.org/abs/2504.13837
- **Title:** Confirmed exactly as stated.
- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang
- **Venue/Year:** NeurIPS 2025 Oral (also received Best Paper Award at ICML 2025 AI4MATH Workshop). Confirmed as NeurIPS 2025.
- **Summary:** Shows that current RLVR training does not elicit fundamentally new reasoning patterns in LLMs beyond what base models already possess; distillation is more effective at introducing novel reasoning abilities.
- **Discrepancies:** None. All details match.

---

**Paper 2: "Consistency Training Helps Stop Sycophancy and Jailbreaks"**
- **URL:** https://arxiv.org/abs/2510.27062
- **Title:** Confirmed exactly as stated.
- **Authors:** Alex Irpan, Alexander Matt Turner, Mark Kurzeja, David K. Elson, Rohin Shah. Irpan is first author, consistent with "Irpan et al."
- **Venue/Year:** No specific venue listed on arXiv; submitted October 31, 2025. The claim of "Google DeepMind" affiliation is consistent with the known affiliations of these authors (Rohin Shah and Alex Irpan are at DeepMind).
- **Summary:** Proposes consistency training (Bias-augmented and Activation Consistency Training) to reduce sycophancy and jailbreak susceptibility in LLMs, evaluated on Gemini 2.5 Flash.
- **Discrepancies:** No venue/conference is listed on arXiv. If the survey states a specific conference, that cannot be confirmed from the arXiv page. Otherwise details match.

---

**Paper 3: "PRIME: Process Reinforcement through Implicit Rewards"**
- **URL:** https://arxiv.org/abs/2502.01456
- **Title:** Confirmed. Full title is "Process Reinforcement through Implicit Rewards" (PRIME is the acronym).
- **Authors:** Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, and many others (25 authors total), including Ning Ding, Zhiyuan Liu, Maosong Sun, Bowen Zhou.
- **Venue/Year:** No specific venue listed; submitted February 3, 2025, revised September 2025.
- **Summary:** Proposes PRIME, a method enabling online process reward model updates using only policy rollouts and outcome labels via implicit process rewards, achieving strong results on math and coding benchmarks with the Eurus-2-7B-PRIME model.
- **Discrepancies:** None regarding the title or content. No venue is listed on arXiv.

---

**Paper 4: "PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning"**
- **URL:** https://arxiv.org/abs/2508.08833
- **Title:** DISCREPANCY. The actual full title is **"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems"**. The short title used in the survey ("PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning") is not the official arXiv title -- "PutnamGAP" is the name of the benchmark dataset introduced in the paper, not part of the title.
- **Authors:** Yuren Hao, Xiang Wan, ChengXiang Zhai
- **Venue/Year:** No specific venue listed; preprint submitted August 12, 2025.
- **Summary:** Introduces PutnamGAP, a benchmark of mathematically-equivalent variations of competition-level math problems, showing that even top models like O3 suffer significant performance degradation on surface-renaming and parametric variants.
- **Discrepancies:** The title as cited in the survey is not the official title. The benchmark name "PutnamGAP" has been prepended. Should be corrected to the actual title.

---

**Paper 5: "On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs"**
- **URL:** https://arxiv.org/abs/2602.12506
- **Title:** Confirmed exactly as stated.
- **Authors:** Rosie Zhao, Anshul Shah, Xiaoyu Zhu, Xinke Deng, Zhongyu Jiang, Yang Yang, Joerg Liebelt, Arnab Mondal
- **Venue/Year:** ICML 2026. Confirmed. Submitted February 13, 2026, revised May 21, 2026.
- **Affiliation:** The claim of "Apple" cannot be directly confirmed from the arXiv abstract page alone, but the venue and year are confirmed as ICML 2026.
- **Summary:** Shows that RL-finetuned VLMs suffer from an accuracy-faithfulness trade-off where benchmark accuracy improves but chain-of-thought reliability and robustness to perturbations degrade; adversarial augmentation alone does not prevent faithfulness drift.
- **Discrepancies:** None on title, venue, or year.

---

**Paper 6: "Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning"**
- **URL:** https://arxiv.org/abs/2404.11500
- **Title:** MINOR DISCREPANCY. The full official title is **"Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning in Large Language Models"** -- the survey version drops the trailing "in Large Language Models."
- **Authors:** Yue Zhou, Yada Zhu, Diego Antognini, Yoon Kim, Yang Zhang
- **Venue/Year:** NAACL 2024. Confirmed.
- **Summary:** Shows that minor wording changes significantly impact LLM math-solving performance and proposes Self-Consistency-over-Paraphrases (SCoP) to leverage diverse paraphrased reasoning paths for improved accuracy.
- **Discrepancies:** Title is slightly truncated in the survey citation (missing "in Large Language Models").

---

**Summary of discrepancies found:**

1. **Paper 2** (Irpan et al.) -- No venue is listed on arXiv. If the survey attributes it to a specific conference, that is unverifiable from arXiv.
2. **Paper 4** (PutnamGAP) -- The title as cited is incorrect. "PutnamGAP" is the benchmark name, not part of the official paper title. The real title is "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems."
3. **Paper 6** (Paraphrase and Solve) -- The title is slightly truncated; the full title ends with "in Large Language Models."

All six URLs resolve to real, existing papers. No paper was missing or non-existent.

agentId: a4022849cd365b3cf (use SendMessage with to: 'a4022849cd365b3cf' to continue this agent)
&lt;usage>total_tokens: 14869
tool_uses: 7
duration_ms: 49169&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b18dae9-e67f-445b-a088-8c24301872ee",
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "36eb01fd-7ab5-4dba-9c80-57a9c11d686f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify details and fetch abstracts for several specific papers that came up in a literature survey. For EACH of the following, search for and fetch the arXiv abstract page to confirm details:\n\n1. \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\" - should be NeurIPS 2025\n   URL: https://arxiv.org/abs/2504.13837\n\n2. \"Consistency Training Helps Stop Sycophancy and Jailbreaks\" by Irpan et al. (Google DeepMind)\n   URL: https://arxiv.org/abs/2510.27062\n\n3. \"PRIME: Process Reinforcement through Implicit Rewards\"\n   URL: https://arxiv.org/abs/2502.01456\n\n4. \"PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning\"\n   URL: https://arxiv.org/abs/2508.08833\n\n5. \"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\" (Apple, ICML 2026)\n   URL: https://arxiv.org/abs/2602.12506\n\n6. \"Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning\" (NAACL 2024)\n   URL: https://arxiv.org/abs/2404.11500\n\nFor each, use WebFetch to get the abstract and confirm: title, authors, venue, year, and a one-sentence summary. Report any discrepancies or papers that don't exist.",
    "agentId": "a4022849cd365b3cf",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the verification report for all six papers:\n\n---\n\n**Paper 1: \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\"**\n- **URL:** https://arxiv.org/abs/2504.13837\n- **Title:** Confirmed exactly as stated.\n- **Authors:** Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, Gao Huang\n- **Venue/Year:** NeurIPS 2025 Oral (also received Best Paper Award at ICML 2025 AI4MATH Workshop). Confirmed as NeurIPS 2025.\n- **Summary:** Shows that current RLVR training does not elicit fundamentally new reasoning patterns in LLMs beyond what base models already possess; distillation is more effective at introducing novel reasoning abilities.\n- **Discrepancies:** None. All details match.\n\n---\n\n**Paper 2: \"Consistency Training Helps Stop Sycophancy and Jailbreaks\"**\n- **URL:** https://arxiv.org/abs/2510.27062\n- **Title:** Confirmed exactly as stated.\n- **Authors:** Alex Irpan, Alexander Matt Turner, Mark Kurzeja, David K. Elson, Rohin Shah. Irpan is first author, consistent with \"Irpan et al.\"\n- **Venue/Year:** No specific venue listed on arXiv; submitted October 31, 2025. The claim of \"Google DeepMind\" affiliation is consistent with the known affiliations of these authors (Rohin Shah and Alex Irpan are at DeepMind).\n- **Summary:** Proposes consistency training (Bias-augmented and Activation Consistency Training) to reduce sycophancy and jailbreak susceptibility in LLMs, evaluated on Gemini 2.5 Flash.\n- **Discrepancies:** No venue/conference is listed on arXiv. If the survey states a specific conference, that cannot be confirmed from the arXiv page. Otherwise details match.\n\n---\n\n**Paper 3: \"PRIME: Process Reinforcement through Implicit Rewards\"**\n- **URL:** https://arxiv.org/abs/2502.01456\n- **Title:** Confirmed. Full title is \"Process Reinforcement through Implicit Rewards\" (PRIME is the acronym).\n- **Authors:** Ganqu Cui, Lifan Yuan, Zefan Wang, Hanbin Wang, and many others (25 authors total), including Ning Ding, Zhiyuan Liu, Maosong Sun, Bowen Zhou.\n- **Venue/Year:** No specific venue listed; submitted February 3, 2025, revised September 2025.\n- **Summary:** Proposes PRIME, a method enabling online process reward model updates using only policy rollouts and outcome labels via implicit process rewards, achieving strong results on math and coding benchmarks with the Eurus-2-7B-PRIME model.\n- **Discrepancies:** None regarding the title or content. No venue is listed on arXiv.\n\n---\n\n**Paper 4: \"PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning\"**\n- **URL:** https://arxiv.org/abs/2508.08833\n- **Title:** DISCREPANCY. The actual full title is **\"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems\"**. The short title used in the survey (\"PutnamGAP: An Investigation of Robustness of LLMs in Mathematical Reasoning\") is not the official arXiv title -- \"PutnamGAP\" is the name of the benchmark dataset introduced in the paper, not part of the title.\n- **Authors:** Yuren Hao, Xiang Wan, ChengXiang Zhai\n- **Venue/Year:** No specific venue listed; preprint submitted August 12, 2025.\n- **Summary:** Introduces PutnamGAP, a benchmark of mathematically-equivalent variations of competition-level math problems, showing that even top models like O3 suffer significant performance degradation on surface-renaming and parametric variants.\n- **Discrepancies:** The title as cited in the survey is not the official title. The benchmark name \"PutnamGAP\" has been prepended. Should be corrected to the actual title.\n\n---\n\n**Paper 5: \"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\"**\n- **URL:** https://arxiv.org/abs/2602.12506\n- **Title:** Confirmed exactly as stated.\n- **Authors:** Rosie Zhao, Anshul Shah, Xiaoyu Zhu, Xinke Deng, Zhongyu Jiang, Yang Yang, Joerg Liebelt, Arnab Mondal\n- **Venue/Year:** ICML 2026. Confirmed. Submitted February 13, 2026, revised May 21, 2026.\n- **Affiliation:** The claim of \"Apple\" cannot be directly confirmed from the arXiv abstract page alone, but the venue and year are confirmed as ICML 2026.\n- **Summary:** Shows that RL-finetuned VLMs suffer from an accuracy-faithfulness trade-off where benchmark accuracy improves but chain-of-thought reliability and robustness to perturbations degrade; adversarial augmentation alone does not prevent faithfulness drift.\n- **Discrepancies:** None on title, venue, or year.\n\n---\n\n**Paper 6: \"Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning\"**\n- **URL:** https://arxiv.org/abs/2404.11500\n- **Title:** MINOR DISCREPANCY. The full official title is **\"Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning in Large Language Models\"** -- the survey version drops the trailing \"in Large Language Models.\"\n- **Authors:** Yue Zhou, Yada Zhu, Diego Antognini, Yoon Kim, Yang Zhang\n- **Venue/Year:** NAACL 2024. Confirmed.\n- **Summary:** Shows that minor wording changes significantly impact LLM math-solving performance and proposes Self-Consistency-over-Paraphrases (SCoP) to leverage diverse paraphrased reasoning paths for improved accuracy.\n- **Discrepancies:** Title is slightly truncated in the survey citation (missing \"in Large Language Models\").\n\n---\n\n**Summary of discrepancies found:**\n\n1. **Paper 2** (Irpan et al.) -- No venue is listed on arXiv. If the survey attributes it to a specific conference, that is unverifiable from arXiv.\n2. **Paper 4** (PutnamGAP) -- The title as cited is incorrect. \"PutnamGAP\" is the benchmark name, not part of the official paper title. The real title is \"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems.\"\n3. **Paper 6** (Paraphrase and Solve) -- The title is slightly truncated; the full title ends with \"in Large Language Models.\"\n\nAll six URLs resolve to real, existing papers. No paper was missing or non-existent."
      }
    ],
    "totalDurationMs": 49169,
    "totalTokens": 14869,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 290,
      "cache_creation_input_tokens": 3048,
      "cache_read_input_tokens": 9757,
      "output_tokens": 1774,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 290,
          "output_tokens": 1774,
          "cache_read_input_tokens": 9757,
          "cache_creation_input_tokens": 3048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3048,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "3b18dae9-e67f-445b-a088-8c24301872ee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-29T05:32:24.916Z_

<details><summary>↩ Tool result · `toolu_01EeXaMV16XZnq5Mn3BkNWRn`</summary>

```text
Now I have a comprehensive picture. Let me compile the final report.

---

## Literature Survey Results: Consistency Regularization During RL Training for Mathematical Reasoning

### Executive Summary

After executing 8 primary searches and multiple follow-up searches, plus fetching 15+ arXiv abstracts, **the gap holds: no paper has applied consistency regularization (JS/KL divergence between equivalent/paraphrased inputs) during RL training specifically for mathematical reasoning** as of May 2026. Several papers come close by addressing adjacent problems, but none combine all three elements: (1) consistency regularization via divergence between equivalent inputs, (2) RL training (GRPO/PPO/REINFORCE), and (3) mathematical reasoning.

---

### Papers Found, Organized by Relevance

#### TIER 1: Closest to the Gap (But Still Don't Fill It)

**1. PrAg-PO: Prompt Augmented Policy Optimization for Robust and Diverse Mathematical Reasoning**
- Authors: Wenquan Lu, Hai Huang, Enqi Liu, Randall Balestriero
- Date: Feb 3, 2026 (revised May 8, 2026) | Venue: arXiv preprint
- URL: https://arxiv.org/abs/2602.03190
- What it does: Mixes prompt templates with template-specific format rewards during GRPO training. Different templates are sampled per training batch to diversify rollouts.
- **Does NOT apply consistency regularization.** It is pure data augmentation at the prompt level -- rollouts within a group use the same template, and there is no divergence loss between outputs on equivalent inputs. The robustness comes from exposure to varied templates, not from a consistency constraint.

**2. MathForge / "Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation"**
- Authors: Yanqi Dai, Yuxiang Ji, Xiao Zhang, Yong Wang, Xiangxiang Chu, Zhiwu Lu
- Date: Jan 28, 2026 | Venue: ICLR 2026
- URL: https://arxiv.org/abs/2601.20614
- What it does: Reformulates questions across multiple aspects (adding story backgrounds, abstract terminology, nesting sub-problems) to increase difficulty, combined with difficulty-aware GRPO (DGPO).
- **Does NOT apply consistency regularization.** The augmented questions are harder variants used as additional training data. There is no divergence loss between outputs on equivalent/original vs. reformulated inputs.

**3. CC-LEARN: Cohort-based Consistency Learning**
- Authors: Xiao Ye, Shaswat Shrivastava, Zhaonan Li, et al.
- Date: Jun 18, 2025 | Venue: arXiv preprint
- URL: https://arxiv.org/abs/2506.15662
- What it does: Groups similar questions into "cohorts" derived from shared programmatic abstractions, then trains with RL using a composite reward (cohort accuracy + retrieval bonus + rejection penalty).
- **Does NOT apply consistency regularization via divergence.** Consistency is achieved through a reward signal that incentivizes uniform accuracy across cohort members, NOT through a JS/KL loss between model output distributions on equivalent inputs. Also targets general reasoning (ARC-Challenge, StrategyQA), not specifically math.

**4. AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking**
- Authors: Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe
- Date: Jun 9, 2025 | Venue: ICLR 2026
- URL: https://arxiv.org/abs/2506.07751
- What it does: Uses RL on granular abstraction data to promote abstract reasoning, mitigating performance degradation on GSM perturbation benchmarks.
- **Does NOT apply consistency regularization.** The approach teaches abstraction through RL rewards on abstraction tasks, not through a divergence-based consistency loss between equivalent inputs.

**5. ACRE: Answer-Consistent Chain-of-thought Reinforcement Learning for Multi-modal LLMs**
- Authors: Minbin Huang, Runhui Huang, Chuanyang Zheng, et al.
- Date: Oct 11, 2025 | Venue: arXiv preprint
- URL: https://arxiv.org/abs/2510.10104
- What it does: Modifies GRPO with a consistency-verification reward: after generating CoT + answer, shuffles answer options and checks if the model gives the same answer. High reward only if both agree and are correct.
- **Partially related but different.** This enforces answer consistency across option orderings (a form of invariance), but (a) it's a reward mechanism, not a divergence-based regularization loss, (b) it targets multimodal reasoning (video), not math specifically, and (c) the "equivalent inputs" are just option-order permutations, not paraphrased/equivalent math problems.

#### TIER 2: Related Work on Divergence in RL (But Not Input Consistency)

**6. DPH-RL / "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in RLVR"**
- Authors: Long Li, Zhijian Zhou, Jiaran Hao, et al.
- Date: Sep 9, 2025 (revised Mar 3, 2026) | Venue: arXiv preprint
- URL: https://arxiv.org/abs/2509.07430
- What it does: Replaces reverse-KL with mass-covering f-divergences (forward-KL, JS divergence) as the policy regularizer in RLVR to prevent solution diversity collapse.
- **Uses JS/KL divergence but NOT for input consistency.** The divergence is between the trained policy and the reference policy (standard RL regularization), not between outputs on equivalent inputs. Applied to math and SQL tasks.

**7. GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning**
- Authors: Yi Chen, Yuying Ge, Rui Wang, et al.
- Date: Jun 19, 2025 | Venue: arXiv preprint
- URL: https://arxiv.org/abs/2506.16141
- What it does: Replaces KL penalty with an adaptive consistency bonus comparing reasoning likelihood against a slowly-evolving reference model, optimizing both correctness and CoT coherence.
- **Does NOT apply input consistency regularization.** "Consistency" here means logical coherence between reasoning steps and answers, measured via reference model comparison. Targets multimodal video reasoning, not math.

**8. R-C2: Cycle-Consistent Reinforcement Learning Improves Multimodal Reasoning**
- Authors: Zirui Zhang, Haoyu Dong, Kexin Pei, Chengzhi Mao
- Date: Mar 26, 2026 | Venue: arXiv preprint
- URL: https://arxiv.org/abs/2603.25720
- What it does: Enforces cross-modal cycle consistency in RL -- requiring backward inference, modality switching, and forward reconstruction as a dense label-free reward.
- **Different form of consistency.** This is cross-modal (visual<->text) cycle consistency, not input-invariance consistency on paraphrased problems. Not applied to math reasoning.

**9. CoVo / "Consistent Paths Lead to Truth: Self-Rewarding RL for LLM Reasoning"**
- Authors: Kongcheng Zhang, Qi Yao, Shunyu Liu, et al.
- Date: Jun 10, 2025 | Venue: arXiv preprint
- URL: https://arxiv.org/abs/2506.08745
- What it does: Uses consistency of intermediate reasoning states across different trajectories as an intrinsic reward for self-rewarding RL.
- **Not input consistency.** Measures whether different reasoning paths converge to the same answer as a reward signal. No divergence between outputs on equivalent inputs.

#### TIER 3: Benchmarking Only (Identify the Problem, Don't Train)

**10. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations**
- Authors: Kaixuan Huang, Jiacheng Guo, et al.
- Date: Feb 10, 2025 | URL: https://arxiv.org/abs/2502.06453
- Benchmarking only. Shows significant performance drops under perturbations but proposes no training method.

**11. VAR-MATH: Probing True Mathematical Reasoning via Symbolic Multi-Instance Benchmarks**
- Authors: Jian Yao, Ran Cheng, Kay Chen Tan
- Date: Jul 17, 2025 | URL: https://arxiv.org/abs/2507.12885
- Benchmarking only. Shows RL-trained models have 47-73% performance drops on variabilized benchmarks.

**12. PutnamGAP / "An Investigation of Robustness of LLMs in Mathematical Reasoning"**
- Authors: Yuren Hao, Xiang Wan, ChengXiang Zhai
- Date: Aug 12, 2025 | URL: https://arxiv.org/abs/2508.08833
- Benchmarking only. Proposes mathematically-equivalent transformations for evaluation.

**13. Robust Reasoning Benchmark**
- Authors: Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey
- Date: Mar 26, 2026 | URL: https://arxiv.org/abs/2604.08571
- Benchmarking only. 13 deterministic textual perturbations on AIME problems.

**14. LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking**
- Authors: Lukas Helff, Quentin Delfosse, et al.
- Date: Apr 16, 2026 | URL: https://arxiv.org/abs/2604.15149
- Introduces Isomorphic Perturbation Testing for evaluation but does not use it during training.

#### TIER 4: Tangentially Related

**15. CREAM: Consistency Regularized Self-Rewarding Language Models**
- Authors: Zhaoyang Wang et al. | Date: Oct 2024 | Venue: ICLR 2025
- URL: https://arxiv.org/abs/2410.12735
- Consistency regularization between reward iterations (not between equivalent inputs). General alignment, not math.

**16. Paraphrase and Solve (SCoP)**
- Authors: Yue Zhou et al. | Date: Apr 2024 | Venue: NAACL 2024
- URL: https://arxiv.org/abs/2404.11500
- Inference-time method (self-consistency over paraphrases). No training-time regularization.

**17. Multidimensional Consistency Improves Reasoning**
- Authors: Huiyuan Lai, Xiao Zhang, Malvina Nissim | Date: Mar 2025
- URL: https://arxiv.org/abs/2503.02670
- Post-hoc evaluation/aggregation across input variations. No training-time divergence loss.

**18. LogicPuzzleRL**
- Authors: Zhen Hao Wong et al. | Date: Jun 5, 2025
- URL: https://arxiv.org/abs/2506.04821
- RL training on logic puzzles for robust math reasoning. No consistency regularization.

**19. On Robustness and CoT Consistency of RL-Finetuned VLMs**
- Authors: Rosie Zhao et al. | Date: Feb 13, 2026 | Venue: ICML 2026
- URL: https://arxiv.org/abs/2602.12506
- Studies how RL fine-tuning hurts CoT consistency in VLMs. Finds augmentation + faithfulness rewards partially help but risk shortcut learning. Does not apply input-consistency regularization.

---

### Gap Analysis

The specific idea -- **adding a JS/KL divergence loss between the model's output distributions on equivalent/paraphrased math problems as a regularization term during RL training (GRPO/PPO)** -- has NOT been done. Here is why the closest papers don't fill this gap:

| Paper | Data Aug in RL? | Divergence Loss Between Equiv. Inputs? | Math Domain? |
|-------|----------------|----------------------------------------|--------------|
| PrAg-PO | Yes (prompt templates) | No | Yes |
| MathForge | Yes (reformulation) | No | Yes |
| CC-LEARN | Yes (cohorts) | No (reward-based) | No |
| AbstRaL | Yes (abstraction) | No | Yes |
| ACRE | No (option shuffle) | No (reward-based) | Multimodal |
| DPH-RL | No | Yes, but policy-vs-reference | Yes |
| GRPO-CARE | No | No (reference model bonus) | No |
| R-C2 | No | No (cycle reward) | No |

The community has (a) extensively benchmarked the fragility problem (MATH-Perturb, VAR-MATH, PutnamGAP, RRB), (b) used data augmentation within RL but without a consistency loss (PrAg-PO, MathForge), (c) used divergence measures within RL but only as policy regularizers, not input-consistency constraints (DPH-RL), and (d) explored consistency as reward signals or inference-time aggregation (ACRE, CC-LEARN, SCoP, CoVo). But nobody has combined a divergence-based consistency loss between equivalent math problem formulations as a training objective alongside RL for math reasoning.

Sources:
- [PrAg-PO](https://arxiv.org/abs/2602.03190)
- [MathForge / Harder Is Better](https://arxiv.org/abs/2601.20614)
- [CC-LEARN](https://arxiv.org/abs/2506.15662)
- [AbstRaL](https://arxiv.org/abs/2506.07751)
- [ACRE](https://arxiv.org/abs/2510.10104)
- [DPH-RL / Choice of Divergence](https://arxiv.org/abs/2509.07430)
- [GRPO-CARE](https://arxiv.org/abs/2506.16141)
- [R-C2](https://arxiv.org/abs/2603.25720)
- [CoVo / Self-Rewarding RL](https://arxiv.org/abs/2506.08745)
- [MATH-Perturb](https://arxiv.org/abs/2502.06453)
- [VAR-MATH](https://arxiv.org/abs/2507.12885)
- [PutnamGAP](https://arxiv.org/abs/2508.08833)
- [Robust Reasoning Benchmark](https://arxiv.org/abs/2604.08571)
- [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149)
- [CREAM](https://arxiv.org/abs/2410.12735)
- [Paraphrase and Solve](https://arxiv.org/abs/2404.11500)
- [Multidimensional Consistency](https://arxiv.org/abs/2503.02670)
- [LogicPuzzleRL](https://arxiv.org/abs/2506.04821)
- [On Robustness of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)

agentId: abf473f8c342a84d0 (use SendMessage with to: 'abf473f8c342a84d0' to continue this agent)
&lt;usage>total_tokens: 41642
tool_uses: 45
duration_ms: 228064&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "868e9c9a-4fac-4fa4-8a94-53ab2bd84b2a",
  "isSidechain": false,
  "promptId": "8654e8f3-9008-4b4f-8d58-630bb06ffe4a",
  "type": "user",
  "uuid": "b1fea44b-f47a-4d5d-b549-13d1ebf467a7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping with a literature survey. I need to verify that NO paper has applied consistency regularization (JS/KL divergence between equivalent inputs) during RL training for mathematical reasoning. Also search for any papers that combine data augmentation with RL for math reasoning robustness.\n\nExecute these searches and fetch arXiv abstracts for any promising papers:\n\nSearch 1: \"consistency regularization reinforcement learning mathematical reasoning\"\nSearch 2: \"JS divergence KL divergence RL training math reasoning robustness\"\nSearch 3: \"invariance regularization GRPO PPO mathematical reasoning\"\nSearch 4: \"perturbation invariance training mathematical reasoning LLM 2025 2026\"\nSearch 5: \"data augmentation reinforcement learning math reasoning robustness 2025\"\nSearch 6: \"equivalent problem variants training mathematical reasoning\"\nSearch 7: \"surface form invariance mathematical reasoning training\"\nSearch 8: \"consistency loss RL fine-tuning reasoning 2025 2026\"\n\nFor each paper found, use WebFetch on its arXiv page to get the full abstract. Report:\n- Full title, authors, venue, URL\n- What it does (1-2 sentences)\n- Whether it applies consistency regularization during RL training specifically\n\nThis is critical: I need to know if the gap \"no one has applied consistency regularization during RL training for math reasoning\" still holds as of May 2026.",
    "agentId": "abf473f8c342a84d0",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Let me compile the final report.\n\n---\n\n## Literature Survey Results: Consistency Regularization During RL Training for Mathematical Reasoning\n\n### Executive Summary\n\nAfter executing 8 primary searches and multiple follow-up searches, plus fetching 15+ arXiv abstracts, **the gap holds: no paper has applied consistency regularization (JS/KL divergence between equivalent/paraphrased inputs) during RL training specifically for mathematical reasoning** as of May 2026. Several papers come close by addressing adjacent problems, but none combine all three elements: (1) consistency regularization via divergence between equivalent inputs, (2) RL training (GRPO/PPO/REINFORCE), and (3) mathematical reasoning.\n\n---\n\n### Papers Found, Organized by Relevance\n\n#### TIER 1: Closest to the Gap (But Still Don't Fill It)\n\n**1. PrAg-PO: Prompt Augmented Policy Optimization for Robust and Diverse Mathematical Reasoning**\n- Authors: Wenquan Lu, Hai Huang, Enqi Liu, Randall Balestriero\n- Date: Feb 3, 2026 (revised May 8, 2026) | Venue: arXiv preprint\n- URL: https://arxiv.org/abs/2602.03190\n- What it does: Mixes prompt templates with template-specific format rewards during GRPO training. Different templates are sampled per training batch to diversify rollouts.\n- **Does NOT apply consistency regularization.** It is pure data augmentation at the prompt level -- rollouts within a group use the same template, and there is no divergence loss between outputs on equivalent inputs. The robustness comes from exposure to varied templates, not from a consistency constraint.\n\n**2. MathForge / \"Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation\"**\n- Authors: Yanqi Dai, Yuxiang Ji, Xiao Zhang, Yong Wang, Xiangxiang Chu, Zhiwu Lu\n- Date: Jan 28, 2026 | Venue: ICLR 2026\n- URL: https://arxiv.org/abs/2601.20614\n- What it does: Reformulates questions across multiple aspects (adding story backgrounds, abstract terminology, nesting sub-problems) to increase difficulty, combined with difficulty-aware GRPO (DGPO).\n- **Does NOT apply consistency regularization.** The augmented questions are harder variants used as additional training data. There is no divergence loss between outputs on equivalent/original vs. reformulated inputs.\n\n**3. CC-LEARN: Cohort-based Consistency Learning**\n- Authors: Xiao Ye, Shaswat Shrivastava, Zhaonan Li, et al.\n- Date: Jun 18, 2025 | Venue: arXiv preprint\n- URL: https://arxiv.org/abs/2506.15662\n- What it does: Groups similar questions into \"cohorts\" derived from shared programmatic abstractions, then trains with RL using a composite reward (cohort accuracy + retrieval bonus + rejection penalty).\n- **Does NOT apply consistency regularization via divergence.** Consistency is achieved through a reward signal that incentivizes uniform accuracy across cohort members, NOT through a JS/KL loss between model output distributions on equivalent inputs. Also targets general reasoning (ARC-Challenge, StrategyQA), not specifically math.\n\n**4. AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking**\n- Authors: Silin Gao, Antoine Bosselut, Samy Bengio, Emmanuel Abbe\n- Date: Jun 9, 2025 | Venue: ICLR 2026\n- URL: https://arxiv.org/abs/2506.07751\n- What it does: Uses RL on granular abstraction data to promote abstract reasoning, mitigating performance degradation on GSM perturbation benchmarks.\n- **Does NOT apply consistency regularization.** The approach teaches abstraction through RL rewards on abstraction tasks, not through a divergence-based consistency loss between equivalent inputs.\n\n**5. ACRE: Answer-Consistent Chain-of-thought Reinforcement Learning for Multi-modal LLMs**\n- Authors: Minbin Huang, Runhui Huang, Chuanyang Zheng, et al.\n- Date: Oct 11, 2025 | Venue: arXiv preprint\n- URL: https://arxiv.org/abs/2510.10104\n- What it does: Modifies GRPO with a consistency-verification reward: after generating CoT + answer, shuffles answer options and checks if the model gives the same answer. High reward only if both agree and are correct.\n- **Partially related but different.** This enforces answer consistency across option orderings (a form of invariance), but (a) it's a reward mechanism, not a divergence-based regularization loss, (b) it targets multimodal reasoning (video), not math specifically, and (c) the \"equivalent inputs\" are just option-order permutations, not paraphrased/equivalent math problems.\n\n#### TIER 2: Related Work on Divergence in RL (But Not Input Consistency)\n\n**6. DPH-RL / \"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in RLVR\"**\n- Authors: Long Li, Zhijian Zhou, Jiaran Hao, et al.\n- Date: Sep 9, 2025 (revised Mar 3, 2026) | Venue: arXiv preprint\n- URL: https://arxiv.org/abs/2509.07430\n- What it does: Replaces reverse-KL with mass-covering f-divergences (forward-KL, JS divergence) as the policy regularizer in RLVR to prevent solution diversity collapse.\n- **Uses JS/KL divergence but NOT for input consistency.** The divergence is between the trained policy and the reference policy (standard RL regularization), not between outputs on equivalent inputs. Applied to math and SQL tasks.\n\n**7. GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning**\n- Authors: Yi Chen, Yuying Ge, Rui Wang, et al.\n- Date: Jun 19, 2025 | Venue: arXiv preprint\n- URL: https://arxiv.org/abs/2506.16141\n- What it does: Replaces KL penalty with an adaptive consistency bonus comparing reasoning likelihood against a slowly-evolving reference model, optimizing both correctness and CoT coherence.\n- **Does NOT apply input consistency regularization.** \"Consistency\" here means logical coherence between reasoning steps and answers, measured via reference model comparison. Targets multimodal video reasoning, not math.\n\n**8. R-C2: Cycle-Consistent Reinforcement Learning Improves Multimodal Reasoning**\n- Authors: Zirui Zhang, Haoyu Dong, Kexin Pei, Chengzhi Mao\n- Date: Mar 26, 2026 | Venue: arXiv preprint\n- URL: https://arxiv.org/abs/2603.25720\n- What it does: Enforces cross-modal cycle consistency in RL -- requiring backward inference, modality switching, and forward reconstruction as a dense label-free reward.\n- **Different form of consistency.** This is cross-modal (visual<->text) cycle consistency, not input-invariance consistency on paraphrased problems. Not applied to math reasoning.\n\n**9. CoVo / \"Consistent Paths Lead to Truth: Self-Rewarding RL for LLM Reasoning\"**\n- Authors: Kongcheng Zhang, Qi Yao, Shunyu Liu, et al.\n- Date: Jun 10, 2025 | Venue: arXiv preprint\n- URL: https://arxiv.org/abs/2506.08745\n- What it does: Uses consistency of intermediate reasoning states across different trajectories as an intrinsic reward for self-rewarding RL.\n- **Not input consistency.** Measures whether different reasoning paths converge to the same answer as a reward signal. No divergence between outputs on equivalent inputs.\n\n#### TIER 3: Benchmarking Only (Identify the Problem, Don't Train)\n\n**10. MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations**\n- Authors: Kaixuan Huang, Jiacheng Guo, et al.\n- Date: Feb 10, 2025 | URL: https://arxiv.org/abs/2502.06453\n- Benchmarking only. Shows significant performance drops under perturbations but proposes no training method.\n\n**11. VAR-MATH: Probing True Mathematical Reasoning via Symbolic Multi-Instance Benchmarks**\n- Authors: Jian Yao, Ran Cheng, Kay Chen Tan\n- Date: Jul 17, 2025 | URL: https://arxiv.org/abs/2507.12885\n- Benchmarking only. Shows RL-trained models have 47-73% performance drops on variabilized benchmarks.\n\n**12. PutnamGAP / \"An Investigation of Robustness of LLMs in Mathematical Reasoning\"**\n- Authors: Yuren Hao, Xiang Wan, ChengXiang Zhai\n- Date: Aug 12, 2025 | URL: https://arxiv.org/abs/2508.08833\n- Benchmarking only. Proposes mathematically-equivalent transformations for evaluation.\n\n**13. Robust Reasoning Benchmark**\n- Authors: Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey\n- Date: Mar 26, 2026 | URL: https://arxiv.org/abs/2604.08571\n- Benchmarking only. 13 deterministic textual perturbations on AIME problems.\n\n**14. LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking**\n- Authors: Lukas Helff, Quentin Delfosse, et al.\n- Date: Apr 16, 2026 | URL: https://arxiv.org/abs/2604.15149\n- Introduces Isomorphic Perturbation Testing for evaluation but does not use it during training.\n\n#### TIER 4: Tangentially Related\n\n**15. CREAM: Consistency Regularized Self-Rewarding Language Models**\n- Authors: Zhaoyang Wang et al. | Date: Oct 2024 | Venue: ICLR 2025\n- URL: https://arxiv.org/abs/2410.12735\n- Consistency regularization between reward iterations (not between equivalent inputs). General alignment, not math.\n\n**16. Paraphrase and Solve (SCoP)**\n- Authors: Yue Zhou et al. | Date: Apr 2024 | Venue: NAACL 2024\n- URL: https://arxiv.org/abs/2404.11500\n- Inference-time method (self-consistency over paraphrases). No training-time regularization.\n\n**17. Multidimensional Consistency Improves Reasoning**\n- Authors: Huiyuan Lai, Xiao Zhang, Malvina Nissim | Date: Mar 2025\n- URL: https://arxiv.org/abs/2503.02670\n- Post-hoc evaluation/aggregation across input variations. No training-time divergence loss.\n\n**18. LogicPuzzleRL**\n- Authors: Zhen Hao Wong et al. | Date: Jun 5, 2025\n- URL: https://arxiv.org/abs/2506.04821\n- RL training on logic puzzles for robust math reasoning. No consistency regularization.\n\n**19. On Robustness and CoT Consistency of RL-Finetuned VLMs**\n- Authors: Rosie Zhao et al. | Date: Feb 13, 2026 | Venue: ICML 2026\n- URL: https://arxiv.org/abs/2602.12506\n- Studies how RL fine-tuning hurts CoT consistency in VLMs. Finds augmentation + faithfulness rewards partially help but risk shortcut learning. Does not apply input-consistency regularization.\n\n---\n\n### Gap Analysis\n\nThe specific idea -- **adding a JS/KL divergence loss between the model's output distributions on equivalent/paraphrased math problems as a regularization term during RL training (GRPO/PPO)** -- has NOT been done. Here is why the closest papers don't fill this gap:\n\n| Paper | Data Aug in RL? | Divergence Loss Between Equiv. Inputs? | Math Domain? |\n|-------|----------------|----------------------------------------|--------------|\n| PrAg-PO | Yes (prompt templates) | No | Yes |\n| MathForge | Yes (reformulation) | No | Yes |\n| CC-LEARN | Yes (cohorts) | No (reward-based) | No |\n| AbstRaL | Yes (abstraction) | No | Yes |\n| ACRE | No (option shuffle) | No (reward-based) | Multimodal |\n| DPH-RL | No | Yes, but policy-vs-reference | Yes |\n| GRPO-CARE | No | No (reference model bonus) | No |\n| R-C2 | No | No (cycle reward) | No |\n\nThe community has (a) extensively benchmarked the fragility problem (MATH-Perturb, VAR-MATH, PutnamGAP, RRB), (b) used data augmentation within RL but without a consistency loss (PrAg-PO, MathForge), (c) used divergence measures within RL but only as policy regularizers, not input-consistency constraints (DPH-RL), and (d) explored consistency as reward signals or inference-time aggregation (ACRE, CC-LEARN, SCoP, CoVo). But nobody has combined a divergence-based consistency loss between equivalent math problem formulations as a training objective alongside RL for math reasoning.\n\nSources:\n- [PrAg-PO](https://arxiv.org/abs/2602.03190)\n- [MathForge / Harder Is Better](https://arxiv.org/abs/2601.20614)\n- [CC-LEARN](https://arxiv.org/abs/2506.15662)\n- [AbstRaL](https://arxiv.org/abs/2506.07751)\n- [ACRE](https://arxiv.org/abs/2510.10104)\n- [DPH-RL / Choice of Divergence](https://arxiv.org/abs/2509.07430)\n- [GRPO-CARE](https://arxiv.org/abs/2506.16141)\n- [R-C2](https://arxiv.org/abs/2603.25720)\n- [CoVo / Self-Rewarding RL](https://arxiv.org/abs/2506.08745)\n- [MATH-Perturb](https://arxiv.org/abs/2502.06453)\n- [VAR-MATH](https://arxiv.org/abs/2507.12885)\n- [PutnamGAP](https://arxiv.org/abs/2508.08833)\n- [Robust Reasoning Benchmark](https://arxiv.org/abs/2604.08571)\n- [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149)\n- [CREAM](https://arxiv.org/abs/2410.12735)\n- [Paraphrase and Solve](https://arxiv.org/abs/2404.11500)\n- [Multidimensional Consistency](https://arxiv.org/abs/2503.02670)\n- [LogicPuzzleRL](https://arxiv.org/abs/2506.04821)\n- [On Robustness of RL-Finetuned VLMs](https://arxiv.org/abs/2602.12506)"
      }
    ],
    "totalDurationMs": 228064,
    "totalTokens": 41642,
    "totalToolUseCount": 45,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1641,
      "cache_read_input_tokens": 36111,
      "output_tokens": 3889,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1641
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3889,
          "cache_read_input_tokens": 36111,
          "cache_creation_input_tokens": 1641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1641,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 45
    }
  },
  "sourceToolAssistantUUID": "868e9c9a-4fac-4fa4-8a94-53ab2bd84b2a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39 · 2026-05-29T05:32:24.929Z_

```json
{
  "parentUuid": "b1fea44b-f47a-4d5d-b549-13d1ebf467a7",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c4c08608-29ad-4d83-bd21-e25998f83115",
  "timestamp": "2026-05-29T05:32:24.929Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "c4c08608-29ad-4d83-bd21-e25998f83115",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct literature survey on RL math reasoning robustness",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Assistant

_source line 42 · 2026-05-29T05:33:04.812Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have comprehensive results from all search agents. Let me compile the final list of 15 most important papers. The gap analysis agent confirmed that the core gap (consistency regularization during RL training for math reasoning) still holds, which is great news for the MACR proposal.

Let me also note that the gap analysis agent found two very important NEW papers:
1. **PrAg-PO** (arXiv 2026) - prompt augmentation in GRPO, closest to MACR but no consistency loss
2. **MathForge / "Harder Is Better"** (ICLR 2026) - question reformulation + difficulty-aware GRPO


These are critical comparison papers for MACR—PrAg-PO is essentially the data augmentation baseline that MACR needs to outperform. Now I'm prioritizing papers by venue prestige, citation impact, and methodological influence, while focusing on those most relevant to MACR's core contributions: addressing robustness failures in RL-trained math reasoners through consistency regularization within the GRPO training paradigm. Continuing with the robustness and consistency benchmarks—MATH-Perturb and PutnamGAP represent the extremes of perturbation difficulty, while papers like Paraphrase and Solve and the DeepMind consistency work directly address surface form sensitivity and alignment degradation from RL. Then I'm adding the base model (Qwen2.5-Math), the closest augmentation-only baseline (PrAg-PO), and wrapping up with MathForge.

Now I'm reconsidering which papers are truly essential. The core ones I need are DeepSeek-R1 for establishing the RL reasoning paradigm, DeepSeekMath and GRPO as the foundational algorithm, the NeurIPS paper questioning whether RL actually incentivizes reasoning, and GSM-Plus as the first systematic evaluation.

Then there's a second tier of important work: robustness benchmarks like MATH-Perturb and PutnamGAP, consistency training from DeepMind, PrAg-PO as the closest baseline for augmentation during RL, process reward models from the ICLR paper, implicit rewards from PRIME, and papers examining how RL affects model consistency and surface form sensitivity.

I'm weighing whether to swap in Math-Shepherd for automated PRMs or Scaling Behaviors for compute planning, but I think my current fifteen papers strike the right balance. There's also "Rethinking Fine-Tuning" which touches on how training can reduce output diversity—relevant to why consistency regularization helps—and SPARKLE about dissecting RL for math reasoning, but I'm satisfied with what I have.

I found a couple more papers to consider: CREAM about consistency regularization in self-rewarding models, which is related but focused on alignment rather than math robustness, so I'm leaving it out. And DPH-RL using JS divergence as a policy regularizer in RLVR—it's interesting for the divergence angle in RL, though not specifically for input consistency, so I'm still deciding whether it's worth including.

Let me lock in my final 15 papers, starting with DeepSeek-R1, DeepSeekMath with GRPO, the reasoning incentives paper, Let's Verify Step by Step, PRIME, GSM-Plus, MATH-Perturb, PutnamGAP, and Paraphrase and Solve.

Then I'm adding Consistency Training from DeepMind, the robustness study on RL-finetuned vision-language models, Qwen2.5-Math, PrAg-PO, MathForge/Harder Is Better, and Reasoning with Sampling as an oral presentation at ICLR.

This covers the key areas well: the RL-for-reasoning paradigm, reward modeling approaches, robustness benchmarks and perturbations, surface form sensitivity, consistency techniques, and strong base models.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4c08608-29ad-4d83-bd21-e25998f83115",
  "isSidechain": false,
  "requestId": "req_011CbWK7uC96ut8WNCKqnz51",
  "type": "assistant",
  "uuid": "4dc41ff1-29e4-4e46-92ae-39efda5a626a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxJCmRGX4YUz7kUhFD3ySW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21597,
      "cache_read_input_tokens": 27754,
      "output_tokens": 5880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5880,
          "cache_read_input_tokens": 27754,
          "cache_creation_input_tokens": 21597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21597
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

_source line 43 · 2026-05-29T05:34:17.208Z_

Now I have comprehensive results from all search agents. Let me compile the final curated list of 15 papers. The gap analysis agent confirmed a critical finding: **no existing paper applies consistency regularization (JS/KL divergence between equivalent inputs) during RL training for mathematical reasoning** — the MACR gap is confirmed as of May 2026.

Here is the consolidated survey with the 15 most important recent papers, excluding your 7 seed papers (GSM-Symbolic, VAR-MATH, AbstRaL, F²C, PPCL, CSR, APRM):

---

## Survey Summary

The papers cluster into five themes directly relevant to MACR:

1. **The RL training paradigm** — DeepSeek-R1 and GRPO define how modern math reasoning models are trained; "Does RL Really Incentivize Reasoning?" challenges whether RL creates new capabilities or merely concentrates existing ones.

2. **Robustness benchmarks** — GSM-Plus, MATH-Perturb, and PutnamGAP collectively demonstrate the fragility problem from elementary to competition-level math, providing evaluation infrastructure for MACR.

3. **Consistency techniques** — DeepMind's consistency training paper proves the technique scales to production LLMs; the Apple ICML 2026 paper shows RL fine-tuning actively *hurts* consistency, motivating a joint optimization.

4. **Closest comparison baselines** — PrAg-PO and MathForge both augment RL training with varied problem formulations but without a consistency loss — they are MACR's primary augmentation-only baselines.

5. **Reward modeling** — "Let's Verify Step by Step" and PRIME provide the process-reward foundations that MACR's perturbation-robust PRM extension builds upon.

---

```json
[
  {
    "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
    "authors": "Guo et al. (DeepSeek-AI)",
    "venue": "Nature 2025 (vol. 645, pp. 633–638); arXiv January 2025",
    "url": "https://arxiv.org/abs/2501.12948",
    "why_important": "Published in Nature. Most influential RL-for-reasoning paper of 2025. First open demonstration that pure RL (no SFT) elicits advanced reasoning including self-verification. Defines the training paradigm MACR builds upon.",
    "one_line_summary": "Demonstrates that large-scale GRPO training on a base model produces emergent reasoning behaviors (self-reflection, verification, strategy adaptation) achieving performance competitive with OpenAI o1 on AIME 2024."
  },
  {
    "title": "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models",
    "authors": "Shao et al. (DeepSeek)",
    "venue": "arXiv 2024 (2402.03300)",
    "url": "https://arxiv.org/abs/2402.03300",
    "why_important": "Introduced GRPO (Group Relative Policy Optimization), the RL algorithm used by DeepSeek-R1, Qwen2.5-Math, and the proposed MACR method. Foundational paper for the entire RL-for-math-reasoning line of work.",
    "one_line_summary": "Introduces GRPO — a PPO variant that eliminates the critic model via within-group reward normalization — achieving 51.7% on MATH with a 7B model trained on 120B math tokens from Common Crawl."
  },
  {
    "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?",
    "authors": "Yue et al.",
    "venue": "NeurIPS 2025 (Oral; Best Paper Runner-Up); ICML 2025 AI4MATH Workshop (Best Paper Award)",
    "url": "https://arxiv.org/abs/2504.13837",
    "why_important": "NeurIPS 2025 Best Paper Runner-Up. Directly challenges the prevailing narrative that RL creates new reasoning — shows RLVR improves sampling efficiency but does not expand the fundamental capability boundary. Critical context for understanding what MACR's consistency term actually does (reshaping distribution, not adding capability).",
    "one_line_summary": "Using unbiased pass@k evaluation, shows that RLVR concentrates probability on correct solutions already reachable by the base model rather than enabling genuinely new reasoning patterns."
  },
  {
    "title": "Let's Verify Step by Step",
    "authors": "Lightman et al. (OpenAI)",
    "venue": "ICLR 2024",
    "url": "https://arxiv.org/abs/2305.20050",
    "why_important": "Seminal paper on process reward models (PRMs). Established the process vs. outcome supervision dichotomy. Released PRM800K (800K step-level human labels). Foundational for MACR's perturbation-robust PRM extension.",
    "one_line_summary": "Demonstrates that process supervision (feedback on each reasoning step) significantly outperforms outcome supervision for mathematical reasoning, with the resulting PRM solving 78% of MATH problems."
  },
  {
    "title": "PRIME: Process Reinforcement through Implicit Rewards",
    "authors": "Cui et al.",
    "venue": "arXiv 2025 (2502.01456)",
    "url": "https://arxiv.org/abs/2502.01456",
    "why_important": "Eliminates the expensive PRM training pipeline by deriving dense process-level credit assignment implicitly from outcome signals alone. Eurus-2-7B-PRIME surpasses Qwen2.5-Math-7B-Instruct using only 10% of training data. Directly relevant to MACR's reward modeling choices.",
    "one_line_summary": "Enables online process reward model updates using only policy rollouts and outcome labels — no explicit step-level annotations needed — by extracting implicit process rewards directly from the policy."
  },
  {
    "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers",
    "authors": "Li et al.",
    "venue": "ACL 2024",
    "url": "https://arxiv.org/abs/2402.19255",
    "why_important": "Published at ACL 2024. One of the earliest systematic robustness benchmarks for math reasoning. Tests 25 LLMs with 4 prompting techniques. Widely referenced as a baseline evaluation suite. One of MACR's evaluation benchmarks.",
    "one_line_summary": "Creates systematic mathematical perturbations of GSM8K (numerical variation, question target alteration, added statements), revealing up to 20% accuracy gaps between original and perturbed problems while human performance is unaffected."
  },
  {
    "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
    "authors": "Huang et al. (Princeton, Google DeepMind)",
    "venue": "arXiv 2025 (2502.06453)",
    "url": "https://arxiv.org/abs/2502.06453",
    "why_important": "First benchmark targeting competition-level math (MATH level 5) with both structure-preserving and structure-changing perturbations. Identifies 'blind skill application' — models apply memorized solution strategies without checking applicability. One of MACR's evaluation benchmarks.",
    "one_line_summary": "Constructs simple and hard perturbations of the hardest MATH problems, showing o1-mini drops 16.5% and discovering that models blindly apply learned solution templates even when perturbations invalidate them."
  },
  {
    "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
    "authors": "Hao et al.",
    "venue": "arXiv 2025 (2508.08833)",
    "url": "https://arxiv.org/abs/2508.08833",
    "why_important": "Largest-scale perturbation benchmark for competition mathematics (6,306 items from all 1,051 Putnam problems). Tests at the highest difficulty level in the literature. Shows even O3 drops from 51.5% to 38.6% on parametric variants — critical evidence that frontier models are not robust.",
    "one_line_summary": "Introduces PutnamGAP, a benchmark of mathematically-equivalent transformations (surface renaming, parametric variation) of Putnam Competition problems, revealing significant robustness gaps even in state-of-the-art reasoning models."
  },
  {
    "title": "Paraphrase and Solve: Exploring and Exploiting the Impact of Surface Form on Mathematical Reasoning in Large Language Models",
    "authors": "Zhou et al.",
    "venue": "NAACL 2024",
    "url": "https://arxiv.org/abs/2404.11500",
    "why_important": "Published at NAACL 2024. Foundational reference for surface-form sensitivity in math reasoning — shows solve rates swing from 5% to 100% on the same problem with different wording. Proposes SCoP (Self-Consistency-over-Paraphrases), an inference-time consistency method MACR can be compared against.",
    "one_line_summary": "Demonstrates that surface-level rephrasing of math problems causes dramatic accuracy swings (5% to 100%), and proposes aggregating answers across multiple paraphrased versions to exploit this variability for improved accuracy."
  },
  {
    "title": "Consistency Training Helps Stop Sycophancy and Jailbreaks",
    "authors": "Irpan et al. (Google DeepMind)",
    "venue": "arXiv 2025 (2510.27062)",
    "url": "https://arxiv.org/abs/2510.27062",
    "why_important": "From Google DeepMind, applied to production-scale Gemini 2.5 Flash. Proves consistency training (BCT/ACT) scales to frontier LLMs and generalizes beyond task robustness to alignment (sycophancy, jailbreaks). Strongest evidence that the consistency paradigm MACR adapts is viable at scale.",
    "one_line_summary": "Proposes Bias-augmented Consistency Training (BCT) and Activation Consistency Training (ACT) to teach models invariance to irrelevant prompt cues, reducing sycophancy and jailbreak susceptibility in Gemini 2.5 Flash."
  },
  {
    "title": "On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs",
    "authors": "Zhao et al. (Apple)",
    "venue": "ICML 2026",
    "url": "https://arxiv.org/abs/2602.12506",
    "why_important": "Accepted at ICML 2026. Identifies the accuracy-faithfulness trade-off: RL fine-tuning raises benchmark accuracy but erodes CoT reliability and robustness. Directly motivates MACR's approach of jointly optimizing for accuracy and consistency during RL training rather than treating them as separate objectives.",
    "one_line_summary": "Shows that RL-finetuned vision-language models suffer degraded chain-of-thought consistency and robustness to perturbations despite higher benchmark accuracy, and that adversarial augmentation alone does not prevent this faithfulness drift."
  },
  {
    "title": "Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement",
    "authors": "Yang et al. (Alibaba/Qwen)",
    "venue": "arXiv 2024 (2409.12122)",
    "url": "https://arxiv.org/abs/2409.12122",
    "why_important": "Defines the state-of-the-art open-source math reasoning model family. Qwen2.5-Math-7B is MACR's primary experimental base model. Demonstrates the full self-improvement loop (pre-train → reward model → iterative SFT + RL → inference-time reward guidance) that MACR augments with consistency regularization.",
    "one_line_summary": "Presents Qwen2.5-Math (1.5B/7B/72B) with an integrated self-improvement pipeline spanning pre-training data synthesis, iterative SFT and RL with reward models, and inference-time reward-guided sampling across 10 math benchmarks."
  },
  {
    "title": "PrAg-PO: Prompt Augmented Policy Optimization for Robust and Diverse Mathematical Reasoning",
    "authors": "Lu et al.",
    "venue": "arXiv 2026 (2602.03190)",
    "url": "https://arxiv.org/abs/2602.03190",
    "why_important": "The closest existing work to MACR's augmentation-only baseline: mixes prompt templates with template-specific format rewards during GRPO training. Critically, it uses NO consistency loss between equivalent inputs — purely data augmentation within RL. This is the paper MACR must decisively beat to demonstrate the consistency term's value.",
    "one_line_summary": "Diversifies GRPO training by sampling different prompt templates per batch with template-specific format rewards, improving mathematical reasoning robustness through prompt-level data augmentation without any consistency regularization objective."
  },
  {
    "title": "Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (MathForge)",
    "authors": "Dai et al.",
    "venue": "ICLR 2026",
    "url": "https://arxiv.org/abs/2601.20614",
    "why_important": "Accepted at ICLR 2026. Reformulates math questions across multiple aspects (story backgrounds, abstract terminology, nested sub-problems) with difficulty-aware GRPO. Another augmentation-during-RL approach without consistency loss — a key comparison point for MACR's claim that the consistency objective provides benefit beyond augmentation.",
    "one_line_summary": "Proposes multi-aspect question reformulation (adding story contexts, abstracting terminology, nesting sub-problems) combined with difficulty-aware GRPO to improve mathematical reasoning through harder training variants."
  },
  {
    "title": "Reasoning with Sampling: Your Base Model is Smarter Than You Think",
    "authors": "Karan and Du",
    "venue": "ICLR 2026 (Oral Presentation)",
    "url": "https://arxiv.org/abs/2510.14901",
    "why_important": "ICLR 2026 Oral. Shows base models already contain strong reasoning accessible via MCMC-inspired sampling, nearly matching RL post-training on MATH500 and GPQA without any training. Complements the Yue et al. NeurIPS finding. Implies MACR's value lies in making RL-trained models as consistent as base models' latent capability, not in adding new capability.",
    "one_line_summary": "Proposes an iterative MCMC-inspired sampling algorithm that achieves reasoning performance matching or exceeding RL post-training on multiple benchmarks using only the base model's own likelihoods, with no training required."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4dc41ff1-29e4-4e46-92ae-39efda5a626a",
  "isSidechain": false,
  "requestId": "req_011CbWK7uC96ut8WNCKqnz51",
  "type": "assistant",
  "uuid": "9d4392ef-28de-40d8-af67-b4a28802cab6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QxJCmRGX4YUz7kUhFD3ySW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21597,
      "cache_read_input_tokens": 27754,
      "output_tokens": 5880,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21597,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 5880,
          "cache_read_input_tokens": 27754,
          "cache_creation_input_tokens": 21597,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21597
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher conducting a comprehensive literature survey.  **Today's date: 2026-05-29 (UTC).**  ## Task Find the **15 most important recent papers** (published 2024–2026) in or clos…",
  "leafUuid": "9d4392ef-28de-40d8-af67-b4a28802cab6",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Conduct literature survey on RL math reasoning robustness",
  "sessionId": "705442d6-a941-47cc-bbd3-b77f62e0535c"
}
```

---
