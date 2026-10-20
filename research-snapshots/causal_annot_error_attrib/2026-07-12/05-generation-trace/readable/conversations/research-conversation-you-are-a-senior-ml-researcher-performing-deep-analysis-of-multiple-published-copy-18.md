# Research conversation: You are a senior ML researcher performing deep analysis of multiple published papers. **Today's date: 2026-05-29 (UTC).*

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/323cdf93-5570-4239-99e8-4d2f25f379e5.jsonl`
- **Structured JSON:** [`75972ed67e56c417e8cb.json`](../../sessions/75/75972ed67e56c417e8cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T07:27:13.691Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T07:27:13.691Z",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "content": "You are a senior ML researcher performing deep analysis of multiple published papers.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Research context\n\nWe are generating ideas in the area of: **Target: AAAI 2026\nTrack: Machine Learning (ML) — Reinforcement Learning / Mathematical Reasoning\n\nDirection: RL-trained mathematical reasoning models exhibit 47-73% accuracy drops under trivial perturbations (numerical substitution, variable renaming) despite achieving SOTA on clean benchmarks. We propose Math-Aware Consistency Regularization (MACR): adding a JS-divergence consistency term between model outputs on original and mathematically-equivalent perturbed problems during GRPO training, with a complementary discrimination loss against surface-similar but semantically different problems. This adapts proven NLP consistency techniques (F²C, PPCL) to mathematical reasoning with math-equivalence-aware perturbation generation and RL integration — a combination no existing work provides.\n\nSeed Papers:\n- Mirzadeh et al., GSM-Symbolic (Apple, ICLR 2025) — documents up to 65% accuracy drops from single irrelevant clause; establishes that models pattern-match rather than reason\n- VAR-MATH (arXiv 2025) — most damning evidence: 47.9-72.9% drops for RL models on numerically re-parameterized competition math; directly motivates why RL training is the problem\n- Gao et al., AbstRaL (ICLR 2026) — only existing training-time intervention; uses abstraction not invariance; limited to GSM-level; our primary comparison baseline\n- Flip-Flop Consistency / F²C (arXiv 2024) — JS-divergence consistency for prompt perturbation robustness in NLP; proves the technique works but has never been adapted to math reasoning or RL\n- PPCL (EACL 2024) — KL-based consistency regularization recovering 59-69% of perturbation-induced drops in NLU; complementary theoretical grounding\n- CSR: Causal Consistency Regularization (arXiv 2025) — enforces causal faithfulness via operator-level interventions during SFT; closest methodological cousin but SFT-only and targets faithfulness not perturbation invariance\n- APRM (arXiv 2025) — adversarial PRM training on reasoning errors; shows PRM quality matters for downstream RL; motivates our perturbation-robust PRM extension\n\nKnown Gaps:\n- No work applies consistency regularization (JS/KL divergence across equivalent problem variants) during RL training for mathematical reasoning — F²C and PPCL remain NLP-only and SFT-only\n- No PRM has been trained to be robust to surface-form variations of equivalent problems — APRM addresses reasoning errors, not perturbation invariance\n- No training-time robustness intervention has been demonstrated on competition-level math (AIME/Putnam); AbstRaL is GSM-only\n\nTheoretical Anchor: Mathematical equivalence defines a natural invariance class — problems that differ only in surface form (variable names, specific numbers, phrasing) but share identical mathematical structure should produce identical solution distributions. RL training violates this invariance because the reward signal (correct/incorrect final answer) provides no gradient against surface-form-dependent reasoning. A consistency regularization term explicitly penalizes policy divergence across equivalent variants, forcing the model to learn representations that are invariant to mathematically irrelevant features. This is a direct instantiation of Invariant Risk Minimization principles in the RL-for-reasoning setting.\n\nConstraints:\n- Compute: ≤200 H100-hours (budget: 40h baseline GRPO + 90h method variants + 30h evaluation + 20h analysis + 20h buffer)\n- Models: Primary experiments on 7B (Qwen2.5-Math-7B); scaling verification on 14B\n- Evaluation: GSM-Symbolic, GSM-Plus, VAR-MATH (AMC23/AIME24/AIME25), MATH-Perturb; train-time perturbations (numerical substitution, variable renaming) held out from eval perturbations (distractor insertion, structural changes)\n\nQuality Self-Checks:\n- [x] Core insight: RL training optimizes for reward on fixed problem forms, creating surface-form dependencies that consistency regularization can break by enforcing invariance across equivalent variants.\n- [x] Why not obvious: Consistency regularization is well-known in NLP but requires math-aware equivalence-preserving perturbation generation (not just paraphrase) and RL integration (not just SFT) — two non-trivial adaptations that straddle communities.\n- [ ] Baseline fear test: A pure data-augmentation baseline (adding perturbed problems to RL training without consistency loss) could achieve substantial gains. The paper MUST include this baseline and show the consistency term provides additional benefit beyond augmentation. If the gap is <5%, the contribution is weak.\n- [x] Information exploited: Mathematical equivalence structure — the method uses symbolic verification that perturbations preserve the problem's mathematical structure, which pure augmentation or paraphrase-based consistency ignores.\n\nAvoid:\n- Framing this as 'just data augmentation with extra steps' — the consistency objective is the contribution, not the perturbation generation. Must clearly show augmentation-only baseline is insufficient.\n- Over-claiming generality without testing on held-out perturbation types — the key differentiator from augmentation is transfer to unseen perturbation types, so this MUST be demonstrated.\n- Testing only on GSM-level math — this repeats AbstRaL's limitation and loses the competition-math differentiator.\n- Ignoring clean accuracy — if MACR degrades unperturbed accuracy by >2 points, reviewers will question practicality.**\n\n## Your task (Batch 1)\n\nAnalyze the following 5 papers. For EACH paper:\n1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.\n2. If on OpenReview, also read reviewer comments.\n3. Write a concise analysis focusing on HOW the paper innovates.\n\n## Papers to analyze\n\n[\n  {\n    \"title\": \"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\",\n    \"authors\": \"Mirzadeh et al.\",\n    \"venue\": \"ICLR 2025\",\n    \"url\": \"https://arxiv.org/abs/2410.05229\",\n    \"why_important\": \"Foundational robustness benchmark from Apple; ICLR 2025 publication; established that LLMs suffer up to 65% accuracy drops from a single irrelevant clause, proving models pattern-match rather than reason — the core problem MACR addresses\",\n    \"one_line_summary\": \"Introduces symbolic templates for GSM8K showing LLMs exhibit high variance and catastrophic accuracy drops under trivial perturbations like numerical substitution and distractor insertion.\"\n  },\n  {\n    \"title\": \"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers\",\n    \"authors\": \"Li et al.\",\n    \"venue\": \"ACL 2024\",\n    \"url\": \"https://arxiv.org/abs/2402.19255\",\n    \"why_important\": \"Established the systematic perturbation taxonomy for math reasoning robustness at ACL 2024; widely adopted benchmark (one of MACR's evaluation sets); tested 25 LLMs across 8 perturbation types\",\n    \"one_line_summary\": \"Creates an adversarial extension of GSM8K with numerical, structural, and contextual perturbations, showing that even solved problems become unsolvable under minor modifications.\"\n  },\n  {\n    \"title\": \"CREAM: Consistency Regularized Self-Rewarding Language Models\",\n    \"authors\": \"Wang et al.\",\n    \"venue\": \"ICLR 2025\",\n    \"url\": \"https://arxiv.org/abs/2410.12735\",\n    \"why_important\": \"ICLR 2025 publication demonstrating consistency regularization within RL-adjacent training; shows cross-iteration reward consistency prevents bias accumulation in self-rewarding — validates consistency principles in iterative LLM training\",\n    \"one_line_summary\": \"Regularizes self-rewarding language models by enforcing reward consistency across training iterations, mitigating overconfident labeling and accumulated bias in preference data.\"\n  },\n  {\n    \"title\": \"rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking\",\n    \"authors\": \"Guan et al.\",\n    \"venue\": \"ICML 2025 (Oral)\",\n    \"url\": \"https://arxiv.org/abs/2501.04519\",\n    \"why_important\": \"ICML 2025 Oral from Microsoft; achieves 90% on MATH with 7B model via MCTS + PRM self-evolution; demonstrates that process reward models are critical for RL reasoning — motivates MACR's perturbation-robust PRM extension\",\n    \"one_line_summary\": \"Enables small LLMs to achieve OpenAI o1-level math reasoning through Monte Carlo Tree Search guided by a self-evolved process reward model, with iterative code-augmented CoT synthesis.\"\n  },\n  {\n    \"title\": \"Robust Reasoning Benchmark\",\n    \"authors\": \"Golikov et al.\",\n    \"venue\": \"arXiv 2026\",\n    \"url\": \"https://arxiv.org/abs/2604.08571\",\n    \"why_important\": \"Most recent robustness benchmark (2026) applying 13 deterministic perturbations to AIME 2024/2025; reveals up to 54% accuracy drops in open-weights models and identifies failure modes (cognitive thrashing, tokenization breakdown) — validates MACR's focus on competition-level math\",\n    \"one_line_summary\": \"Applies 13 textual perturbations to AIME problems, finding frontier models are largely resilient but open-weights reasoning models suffer up to 54% accuracy drops with multiple failure modes.\"\n  }\n]\n\n## Analysis requirements\n\nFor each paper, analyze:\n- What gap did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- If reviewer comments are available: what was praised, what was criticized?\n\n## CRITICAL: Length constraint\n\n**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.\n\n## Output format\n\nOutput a JSON array. Each element:\n{\n  \"title\": \"Paper title\",\n  \"venue\": \"Where published\",\n  \"problem_identification\": \"What gap/problem? How found? (1-2 sentences)\",\n  \"key_insight\": \"Core intellectual contribution (1 sentence)\",\n  \"innovation_type\": \"new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis\",\n  \"method_summary\": \"Technical approach (2-3 sentences)\",\n  \"limitations_and_open_questions\": \"Gaps + follow-up questions (1-2 sentences)\",\n  \"building_blocks\": [\"Reusable methods/tools/datasets\"],\n  \"relevance_to_seed\": \"Relation to our research area (1 sentence)\"\n}\n\nYou MUST output exactly 5 analyses in the JSON array. IMPORTANT: End your response with the JSON array."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T07:27:13.699Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T07:27:13.699Z",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-29T07:27:13.894Z_

You are a senior ML researcher performing deep analysis of multiple published papers.

**Today's date: 2026-05-29 (UTC).**

## Research context

We are generating ideas in the area of: **Target: AAAI 2026
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

## Your task (Batch 1)

Analyze the following 5 papers. For EACH paper:
1. Use WebSearch and WebFetch to find and read its abstract, introduction, and method section.
2. If on OpenReview, also read reviewer comments.
3. Write a concise analysis focusing on HOW the paper innovates.

## Papers to analyze

[
  {
    "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
    "authors": "Mirzadeh et al.",
    "venue": "ICLR 2025",
    "url": "https://arxiv.org/abs/2410.05229",
    "why_important": "Foundational robustness benchmark from Apple; ICLR 2025 publication; established that LLMs suffer up to 65% accuracy drops from a single irrelevant clause, proving models pattern-match rather than reason — the core problem MACR addresses",
    "one_line_summary": "Introduces symbolic templates for GSM8K showing LLMs exhibit high variance and catastrophic accuracy drops under trivial perturbations like numerical substitution and distractor insertion."
  },
  {
    "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers",
    "authors": "Li et al.",
    "venue": "ACL 2024",
    "url": "https://arxiv.org/abs/2402.19255",
    "why_important": "Established the systematic perturbation taxonomy for math reasoning robustness at ACL 2024; widely adopted benchmark (one of MACR's evaluation sets); tested 25 LLMs across 8 perturbation types",
    "one_line_summary": "Creates an adversarial extension of GSM8K with numerical, structural, and contextual perturbations, showing that even solved problems become unsolvable under minor modifications."
  },
  {
    "title": "CREAM: Consistency Regularized Self-Rewarding Language Models",
    "authors": "Wang et al.",
    "venue": "ICLR 2025",
    "url": "https://arxiv.org/abs/2410.12735",
    "why_important": "ICLR 2025 publication demonstrating consistency regularization within RL-adjacent training; shows cross-iteration reward consistency prevents bias accumulation in self-rewarding — validates consistency principles in iterative LLM training",
    "one_line_summary": "Regularizes self-rewarding language models by enforcing reward consistency across training iterations, mitigating overconfident labeling and accumulated bias in preference data."
  },
  {
    "title": "rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking",
    "authors": "Guan et al.",
    "venue": "ICML 2025 (Oral)",
    "url": "https://arxiv.org/abs/2501.04519",
    "why_important": "ICML 2025 Oral from Microsoft; achieves 90% on MATH with 7B model via MCTS + PRM self-evolution; demonstrates that process reward models are critical for RL reasoning — motivates MACR's perturbation-robust PRM extension",
    "one_line_summary": "Enables small LLMs to achieve OpenAI o1-level math reasoning through Monte Carlo Tree Search guided by a self-evolved process reward model, with iterative code-augmented CoT synthesis."
  },
  {
    "title": "Robust Reasoning Benchmark",
    "authors": "Golikov et al.",
    "venue": "arXiv 2026",
    "url": "https://arxiv.org/abs/2604.08571",
    "why_important": "Most recent robustness benchmark (2026) applying 13 deterministic perturbations to AIME 2024/2025; reveals up to 54% accuracy drops in open-weights models and identifies failure modes (cognitive thrashing, tokenization breakdown) — validates MACR's focus on competition-level math",
    "one_line_summary": "Applies 13 textual perturbations to AIME problems, finding frontier models are largely resilient but open-weights reasoning models suffer up to 54% accuracy drops with multiple failure modes."
  }
]

## Analysis requirements

For each paper, analyze:
- What gap did they identify and HOW?
- What was the key insight others missed?
- How did they formulate the problem differently?
- What existing technique did they adapt/combine/simplify?
- If reviewer comments are available: what was praised, what was criticized?

## CRITICAL: Length constraint

**Each paper's analysis MUST be under 2000 characters.** Be concise and analytical — no filler, no generic praise, no redundant descriptions. Every sentence must carry information.

## Output format

Output a JSON array. Each element:
{
  "title": "Paper title",
  "venue": "Where published",
  "problem_identification": "What gap/problem? How found? (1-2 sentences)",
  "key_insight": "Core intellectual contribution (1 sentence)",
  "innovation_type": "new_formulation | new_technique | new_benchmark | simplification | cross_domain | combination | scaling | analysis",
  "method_summary": "Technical approach (2-3 sentences)",
  "limitations_and_open_questions": "Gaps + follow-up questions (1-2 sentences)",
  "building_blocks": ["Reusable methods/tools/datasets"],
  "relevance_to_seed": "Relation to our research area (1 sentence)"
}

You MUST output exactly 5 analyses in the JSON array. IMPORTANT: End your response with the JSON array.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "type": "user",
  "uuid": "5b4bc3d1-3d4e-4e54-a068-4b7d544d4623",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T07:27:13.890Z_

```json
{
  "parentUuid": "5b4bc3d1-3d4e-4e54-a068-4b7d544d4623",
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
  "uuid": "fbc79712-6ba4-4817-92a5-295591d0c804",
  "timestamp": "2026-05-29T07:27:13.890Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T07:27:13.890Z_

```json
{
  "parentUuid": "fbc79712-6ba4-4817-92a5-295591d0c804",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e957527e-e4f2-4497-91d0-62002c5bf998",
  "timestamp": "2026-05-29T07:27:13.890Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
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
  "aiTitle": "Analyze ML papers on math reasoning robustness",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Assistant

_source line 7 · 2026-05-29T07:27:18.902Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to analyze 5 papers in detail. Let me search for and read each paper, then provide structured analyses. I'll launch multiple agents to research these papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e957527e-e4f2-4497-91d0-62002c5bf998",
  "isSidechain": false,
  "requestId": "req_011CbWTsieYMMcPj96CwYxFJ",
  "type": "assistant",
  "uuid": "fbcae1b7-410c-4b69-8184-67ff8360d6d1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fPsJdiBo2qhwDByCqppJM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4115,
      "cache_read_input_tokens": 11014,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4115,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4115
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

_source line 8 · 2026-05-29T07:27:19.960Z_

I'll research all 5 papers in parallel to gather their abstracts, methods, and any reviewer comments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fbcae1b7-410c-4b69-8184-67ff8360d6d1",
  "isSidechain": false,
  "requestId": "req_011CbWTsieYMMcPj96CwYxFJ",
  "type": "assistant",
  "uuid": "c6e6b6b8-9479-47f9-9218-85a030c79883",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fPsJdiBo2qhwDByCqppJM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4115,
      "cache_read_input_tokens": 11014,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4115,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4115
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

_source line 9 · 2026-05-29T07:27:20.708Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KzPUL93g85u5Qd5W3pbLyX`</summary>

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
  "parentUuid": "c6e6b6b8-9479-47f9-9218-85a030c79883",
  "isSidechain": false,
  "requestId": "req_011CbWTsieYMMcPj96CwYxFJ",
  "type": "assistant",
  "uuid": "5b5c00e6-0414-4a2f-91bc-fb88c21b15a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011fPsJdiBo2qhwDByCqppJM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4115,
      "cache_read_input_tokens": 11014,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4115,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 158,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 4115,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4115
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

_source line 10 · 2026-05-29T07:27:20.717Z_

<details><summary>↩ Tool result · `toolu_01KzPUL93g85u5Qd5W3pbLyX`</summary>

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
  "parentUuid": "5b5c00e6-0414-4a2f-91bc-fb88c21b15a1",
  "isSidechain": false,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "type": "user",
  "uuid": "5a5c2d2a-b674-4b59-b76f-3def803d0f99",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "5b5c00e6-0414-4a2f-91bc-fb88c21b15a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-29T07:27:24.258Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the WebSearch and WebFetch tools available. Let me research all 5 papers in parallel using agents.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a5c2d2a-b674-4b59-b76f-3def803d0f99",
  "isSidechain": false,
  "requestId": "req_011CbWTtEAZdtspPNrrvXeeS",
  "type": "assistant",
  "uuid": "81f31e49-8d49-4f57-b092-99f5e685b459",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD3PLGQf8UKBbwYvYa6DYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 15129,
      "output_tokens": 1864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1864,
          "cache_read_input_tokens": 15129,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 12 · 2026-05-29T07:27:24.262Z_

Now let me research all 5 papers in parallel using agents.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "81f31e49-8d49-4f57-b092-99f5e685b459",
  "isSidechain": false,
  "requestId": "req_011CbWTtEAZdtspPNrrvXeeS",
  "type": "assistant",
  "uuid": "45e56b00-3514-465e-8128-70d1fd1ae600",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD3PLGQf8UKBbwYvYa6DYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 15129,
      "output_tokens": 1864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1864,
          "cache_read_input_tokens": 15129,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 13 · 2026-05-29T07:27:33.141Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01WybWba9isbRmofTUGoW4sX`</summary>

```json
{
  "description": "Analyze GSM-Symbolic paper",
  "prompt": "You are researching the paper \"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\" by Mirzadeh et al. (ICLR 2025), available at https://arxiv.org/abs/2410.05229.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for and read OpenReview reviews if available (search \"GSM-Symbolic openreview ICLR 2025\").\n3. Search for any detailed method descriptions or blog posts about the paper.\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- If reviewer comments found: what was praised, what was criticized?\n- Key quantitative results (accuracy drops, variance numbers, etc.)\n\nBe thorough and specific — include numbers, method details, and concrete findings. This will be used for a research analysis.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45e56b00-3514-465e-8128-70d1fd1ae600",
  "isSidechain": false,
  "requestId": "req_011CbWTtEAZdtspPNrrvXeeS",
  "type": "assistant",
  "uuid": "89e2d521-68b8-418b-a89f-276a3644904d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD3PLGQf8UKBbwYvYa6DYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 15129,
      "output_tokens": 1864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1864,
          "cache_read_input_tokens": 15129,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 14 · 2026-05-29T07:27:36.637Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PDP25UBSLkATujUnyvr6HG`</summary>

```json
{
  "description": "Analyze GSM-Plus paper",
  "prompt": "You are researching the paper \"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers\" by Li et al. (ACL 2024), available at https://arxiv.org/abs/2402.19255.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for any OpenReview or ACL Anthology reviews.\n3. Search for any detailed method descriptions.\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently (the perturbation taxonomy)?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- If reviewer comments found: what was praised, what was criticized?\n- Key quantitative results (how many perturbation types, accuracy drops, number of LLMs tested)\n\nBe thorough and specific — include numbers, method details, and concrete findings.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89e2d521-68b8-418b-a89f-276a3644904d",
  "isSidechain": false,
  "requestId": "req_011CbWTtEAZdtspPNrrvXeeS",
  "type": "assistant",
  "uuid": "36dc2167-aa87-4707-b31e-1a8650ed55cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD3PLGQf8UKBbwYvYa6DYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 15129,
      "output_tokens": 1864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1864,
          "cache_read_input_tokens": 15129,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 15 · 2026-05-29T07:27:41.007Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MyE62JygWjixeWoCnPqxpy`</summary>

```json
{
  "description": "Analyze CREAM paper",
  "prompt": "You are researching the paper \"CREAM: Consistency Regularized Self-Rewarding Language Models\" by Wang et al. (ICLR 2025), available at https://arxiv.org/abs/2410.12735.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for OpenReview reviews for CREAM ICLR 2025.\n3. Search for any detailed method/technique descriptions.\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What specific consistency regularization technique did they use (KL divergence, JS divergence, etc.)?\n- How does the consistency term integrate with the training loop?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- If reviewer comments found: what was praised, what was criticized?\n- Key quantitative results\n\nBe thorough and specific — include numbers, method details, and concrete findings. This is particularly important as CREAM validates consistency regularization principles in iterative LLM training.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36dc2167-aa87-4707-b31e-1a8650ed55cb",
  "isSidechain": false,
  "requestId": "req_011CbWTtEAZdtspPNrrvXeeS",
  "type": "assistant",
  "uuid": "dd59c538-a91e-4599-ae22-b0e0d2c21572",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD3PLGQf8UKBbwYvYa6DYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 15129,
      "output_tokens": 1864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1864,
          "cache_read_input_tokens": 15129,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 16 · 2026-05-29T07:27:47.804Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01S4PqtPDiU3auALy2NJY8vV`</summary>

```json
{
  "description": "Analyze rStar-Math paper",
  "prompt": "You are researching the paper \"rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking\" by Guan et al. (ICML 2025 Oral), available at https://arxiv.org/abs/2501.04519.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for OpenReview reviews or ICML 2025 reviews for rStar-Math.\n3. Search for any blog posts or detailed method descriptions (Microsoft Research).\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- How does the MCTS + PRM self-evolution work technically?\n- What role does the Process Reward Model play and how is it trained?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- If reviewer comments found: what was praised, what was criticized?\n- Key quantitative results (especially the 90% MATH claim, model sizes, comparison to o1)\n\nBe thorough and specific — include numbers, method details, and concrete findings. Focus especially on how the PRM is trained and evolved, as this is relevant to our research on perturbation-robust PRMs.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd59c538-a91e-4599-ae22-b0e0d2c21572",
  "isSidechain": false,
  "requestId": "req_011CbWTtEAZdtspPNrrvXeeS",
  "type": "assistant",
  "uuid": "53949194-84d1-47aa-bf72-21a0b46c8387",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD3PLGQf8UKBbwYvYa6DYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 15129,
      "output_tokens": 1864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1864,
          "cache_read_input_tokens": 15129,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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

_source line 17 · 2026-05-29T07:27:53.264Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TTJbp2Hf3WPfBs3sfyyCzi`</summary>

```json
{
  "description": "Analyze Robust Reasoning Benchmark",
  "prompt": "You are researching the paper \"Robust Reasoning Benchmark\" by Golikov et al. (arXiv 2026), available at https://arxiv.org/abs/2604.08571.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for any additional information, blog posts, or discussions about this paper.\n3. Try to find details about the 13 deterministic perturbation types they apply to AIME problems.\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently from GSM-Symbolic and GSM-Plus?\n- What are the 13 perturbation types (or as many as you can find)?\n- What failure modes did they identify (cognitive thrashing, tokenization breakdown)?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- Key quantitative results (up to 54% accuracy drops, which models are resilient vs vulnerable)\n- How do they differentiate between frontier models and open-weights models?\n\nBe thorough and specific — include numbers, method details, and concrete findings. This is a very recent 2026 paper so search carefully.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53949194-84d1-47aa-bf72-21a0b46c8387",
  "isSidechain": false,
  "requestId": "req_011CbWTtEAZdtspPNrrvXeeS",
  "type": "assistant",
  "uuid": "5a4a5eb3-6bd9-4792-9073-1a4d462bb219",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RD3PLGQf8UKBbwYvYa6DYr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1178,
      "cache_read_input_tokens": 15129,
      "output_tokens": 1864,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1864,
          "cache_read_input_tokens": 15129,
          "cache_creation_input_tokens": 1178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1178
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
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-29 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "5a4a5eb3-6bd9-4792-9073-1a4d462bb219",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on math reasoning robustness",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Tool result

_source line 20 · 2026-05-29T07:30:55.361Z_

<details><summary>↩ Tool result · `toolu_01TTJbp2Hf3WPfBs3sfyyCzi`</summary>

```text
I now have comprehensive information about this paper. Here is my detailed summary.

---

## Detailed Summary: "Robust Reasoning Benchmark" (Golikov et al., arXiv:2604.08571, 2026)

**Authors:** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey (University of Toronto / Vector Institute)

---

### The Gap They Identified and HOW

The authors observed that LLMs achieve impressive scores on standard math benchmarks like AIME, but their problem-solving abilities are deeply dependent on context and textual formatting. The critical gap: it was unknown whether high benchmark performance reflects genuine robust reasoning or merely fragile pattern matching overfit to standard textual presentations. Prior adversarial approaches (like GSM-Symbolic) that altered numeric values made it impossible to disentangle reasoning failures from arithmetic failures. When a model fails after a numerical perturbation, it is unclear whether the failure lies in the reasoning logic or the arithmetic calculation. RRB was designed to isolate pure structural fragility by never touching the math itself.

---

### The Key Insight Others Missed

The fundamental insight is that you can test reasoning robustness without changing the mathematical content at all. By applying deterministic, reversible, textual transformations that preserve the exact mathematical values, logic, and final answer, you can isolate whether a model genuinely "understands" a problem or merely pattern-matches on familiar formatting. The transformations are trivial for humans with pen and paper to decode, yet they are structurally hostile to LLM tokenization and attention mechanisms. This exposes that LLM "reasoning" is often overfit to standard textual presentation rather than reflecting true mathematical understanding.

---

### How They Formulate the Problem Differently from GSM-Symbolic and GSM-Plus

| Aspect | GSM-Symbolic | GSM-Plus | RRB |
|--------|-------------|----------|-----|
| **What changes** | Numeric values via symbolic templates | Eight reasoning-skill perturbations (arithmetic variation, distractor insertion, etc.) | Textual/structural presentation only |
| **Math preserved?** | No (new numbers) | Partially (varies by perturbation) | Yes, completely -- "the exact pristine mathematical state" |
| **Failure attribution** | Ambiguous (reasoning vs. arithmetic?) | Cleaner but still mixes content changes | Clean: failures are purely structural/tokenization-related |
| **Determinism** | Template-based but stochastic instantiation | Various | Strictly deterministic, algorithmically invertible |
| **Domain** | Grade-school math (GSM8K) | Grade-school math (GSM8K) | Competition math (AIME 2024/2025) |
| **Approach** | LLM-generated perturbations | Skill-based augmentations | Domain-agnostic algorithmic transformations, no LLM in the loop |

RRB forces a two-stage reasoning trajectory: first decode the structural transformation, then solve the math. This separates decoding ability from mathematical reasoning cleanly.

---

### The 13 Deterministic Perturbation Types

Organized into four categories:

**Category 1 -- Semantic and Lexical Substitutions:**
1. **Not Not** -- Double negations inserted before numerical values and adjectives (e.g., "not not least"). Logically equivalent to the original.
2. **Opposites** -- Semantic terms remapped to antonyms within queries (e.g., "short" means "long"), with a substitution key provided in the prompt.
3. **Wrappers** -- Terms encapsulated in arbitrary syntactic wrappers acting as identity functions (e.g., "3(p)" replaces "p"), with mappings provided explicitly.

**Category 2 -- Contextual Overload (Interleaved Contexts):**
4. **Line-level Interleaving** -- Two distinct math problems split into ~60-character segments, alternated with problem tags. The model must extract only the designated problem.
5. **Word-level Interleaving** -- Words from two problems strictly alternated one-by-one, with the shorter problem repeated to match length.
6. **Symbol-level Interleaving** -- Individual characters from two problems interwoven character-by-character.

**Category 3 -- Syntactic Distortions:**
7. **Sentence Reversal** -- Order of sentences (delimited by periods) reversed in the entire query.
8. **Word Reversal** -- Order of words (space-delimited) reversed throughout the input.
9. **Symbol Reversal** -- Each word's characters reversed individually while maintaining word positions.

**Category 4 -- Visual and Spatial Encoding:**
10. **Rail Fence Cipher** -- Symbols placed in zigzag patterns across multiple rows with dots filling gaps; requires diagonal reading to reconstruct.
11. **Rectangle Perimeter** -- Query mapped onto a rectangle's perimeter flowing clockwise from top-left, with dots filling the center.
12. **Snake Vertical** -- Text written into grids using vertical zigzag patterns (down column 1, up column 2, down column 3, etc.).
13. **Snake Horizontal** -- Horizontal boustrophedon pattern (right across row 1, left across row 2, right across row 3, alternating).

**Design principles enforced across all perturbations:**
- Information-theoretic invariance (no added constraints or ambiguities)
- Algorithmic reversibility (verified via Python scripts)
- Cognitive tractability (humans can decode with pen and paper)
- Explicit decoding protocol provided in plain English in the prompt
- Grid preservation using dots or perfect padding

**Critical preprocessing steps:** LaTeX comment removal, newline flattening (replacing newlines with semicolons), and escape sequence neutralization (inserting spaces before \n, \t, etc. to prevent control character formation during reversals).

---

### Failure Modes Identified

**1. Cognitive Thrashing:** Open-weights reasoning models (particularly Nemotron-7B) enter unproductive token-generation loops rather than failing cleanly. Nemotron-7B generated approximately 27,000 tokens on Rectangle Perimeter tasks while achieving 0% accuracy. The authors observe that "stopping criteria and logical progression heuristics are highly brittle" -- the models lack the metacognitive ability to recognize they are confused.

**2. Tokenization Breakdown:** Perturbations that break words into isolated characters (Symbol Reversal, Rail Fence Cipher, character-level interleaving) shatter Byte-Pair Encoding (BPE) boundaries. Models cannot map isolated character tokens back into coherent internal causal graphs, resulting in near-zero accuracy. The authors state: "Their general reasoning is bottlenecked by subword semantic priors."

**3. Reasoning Collapse:** Complete accuracy degradation on specific transformation types. Qwen3-30B drops from strong baseline performance to approximately 1% on Snake (Vertical) tasks. The authors attribute this to "left-to-right, 1D pre-training biases" that fundamentally constrain spatial reasoning capabilities.

**4. Intra-Query Attention Dilution (IQAD):** A distinct phenomenon studied in isolation. When models solve multiple independent AIME problems sequentially within a single context window, accuracy on subsequent problems degrades. Attention analysis showed that middle and late transformer layers consistently allocate 10%-16.5% of attention probability mass to irrelevant distractor regions (prior solved problems), and approximately 32.9% of attention in deeper layers attaches to initial system prompts ("attention sink" behavior). This is scale-invariant, affecting models from 7B to 120B parameters, suggesting a fundamental architectural limitation.

---

### Existing Techniques Adapted/Combined/Simplified

The paper does not invent new encoding methods. Instead, it systematizes classical cipher and encoding schemes -- Rail Fence Cipher, boustrophedon (snake) patterns, rectangle perimeter mapping -- and combines them with linguistic transformations (reversals, double negation, antonym substitution, interleaving) into a unified, rigorous evaluation framework with strict design principles. The novelty is in the application to LLM robustness evaluation with formal guarantees of information preservation, not in the individual transformations themselves.

---

### Main Limitations

1. **Domain specificity:** Evaluation focuses exclusively on competitive mathematics (AIME). Generalization to legal, medical, or coding reasoning tasks is unexplored.
2. **Optimal task granularity is an open question:** The paper discusses the theoretical "atomic unit of reasoning" -- the maximum computation a model can perform in a single context state before structural noise degrades algorithmic logic -- but cannot formally quantify it.
3. **Proprietary model testing was less comprehensive:** Due to computational costs, closed-source models were evaluated on baseline and only 4 sequential problems, whereas open-weights models were tested more exhaustively.
4. **Generalization of IQAD findings:** Whether the attention dilution phenomenon extends to non-numeric reasoning and how maximum safe "cognitive load" scales with parameter count remain open.

---

### Key Quantitative Results

**Frontier (closed-source) models:**
- **GPT-5.4:** ~3% average accuracy drop across all perturbations -- the most resilient model tested.
- **Gemini 3.1 Pro:** ~8% average accuracy drop. Scored 99% on Snake (Horizontal) but dropped to 65% on Snake (Vertical), showing sensitivity to spatial orientation.
- **Claude 4.6 Opus:** ~52% average accuracy drop, but this is primarily driven by categorical refusals, not reasoning failure. Claude's safety filters misclassify symbol manipulation perturbations as prompt injection or jailbreak attempts. It refuses "the vast majority of prompts involving symbol manipulation."

**Open-weights models:**
- **Nemotron-7B:** ~53% average accuracy drop; 0% accuracy on Rectangle Perimeter with ~27K tokens generated (cognitive thrashing).
- **Qwen3-30B-A3B-Thinking:** ~47% average accuracy drop; drops to ~1% on Snake (Vertical) vs. 16% on Snake (Horizontal).
- **DeepSeek-R1-Distill-70B:** Substantial degradation on visual/syntactic tasks (exact average not stated).
- **OpenAI GPT-OSS-120B:** Tested for IQAD; showed degradation despite being the largest open-weights model.
- Individual perturbations can cause up to 100% accuracy drops on specific tasks (e.g., symbol-level interleaving).

**IQAD results:** All open-weights models (7B to 120B) and Claude 4.6 Opus showed accuracy decay on later problems in sequential contexts.

---

### Frontier vs. Open-Weights Model Differentiation

The paper draws a sharp divide:
- **Frontier models** (GPT-5.4, Gemini 3.1 Pro) show "remarkable robustness to structural noise" with minimal performance loss (3-8%), suggesting they may employ undisclosed architectural advantages or post-training techniques for handling structural variation.
- **Open-weights models** exhibit systematic failure modes (thrashing, tokenization breakdown, collapse) suggesting their reasoning is "bottlenecked by subword semantic priors" and overfit to standard token distributions.
- **Claude** occupies an unusual position: its failures are not reasoning failures but safety-system failures (refusals), making it a different category of vulnerability entirely.
- The paper notes that proprietary agentic frameworks (including Google's AntiGravity, which leaked screenshots show uses a `&lt;task_boundary_tool>` syntax) already implement explicit contextual resets and task boundaries -- suggesting industry awareness of these phenomena and that frontier providers may already be mitigating attention dilution through scaffolding rather than pure architectural solutions.

---

Sources:
- [Robust Reasoning Benchmark - arXiv Abstract](https://arxiv.org/abs/2604.08571)
- [Robust Reasoning Benchmark - Full HTML](https://arxiv.org/html/2604.08571v2)
- [SwiftScholar Paper Detail](https://www.swiftscholar.net/paper/69dd894984947a5132b62b34)
- [GSM-Plus Paper](https://arxiv.org/abs/2402.19255)
- [Gennady Pekhimenko - CIFAR Profile](https://cifar.ca/bios/gennady-pekhimenko/)

agentId: a56d5b8ff9d0d9bc6 (use SendMessage with to: 'a56d5b8ff9d0d9bc6' to continue this agent)
&lt;usage>total_tokens: 24352
tool_uses: 13
duration_ms: 182068&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5a4a5eb3-6bd9-4792-9073-1a4d462bb219",
  "isSidechain": false,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "type": "user",
  "uuid": "efa8c255-8ce4-4e01-a9fc-2056c3657774",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"Robust Reasoning Benchmark\" by Golikov et al. (arXiv 2026), available at https://arxiv.org/abs/2604.08571.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for any additional information, blog posts, or discussions about this paper.\n3. Try to find details about the 13 deterministic perturbation types they apply to AIME problems.\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently from GSM-Symbolic and GSM-Plus?\n- What are the 13 perturbation types (or as many as you can find)?\n- What failure modes did they identify (cognitive thrashing, tokenization breakdown)?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- Key quantitative results (up to 54% accuracy drops, which models are resilient vs vulnerable)\n- How do they differentiate between frontier models and open-weights models?\n\nBe thorough and specific — include numbers, method details, and concrete findings. This is a very recent 2026 paper so search carefully.",
    "agentId": "a56d5b8ff9d0d9bc6",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information about this paper. Here is my detailed summary.\n\n---\n\n## Detailed Summary: \"Robust Reasoning Benchmark\" (Golikov et al., arXiv:2604.08571, 2026)\n\n**Authors:** Pavel Golikov, Evgenii Opryshko, Gennady Pekhimenko, Mark C. Jeffrey (University of Toronto / Vector Institute)\n\n---\n\n### The Gap They Identified and HOW\n\nThe authors observed that LLMs achieve impressive scores on standard math benchmarks like AIME, but their problem-solving abilities are deeply dependent on context and textual formatting. The critical gap: it was unknown whether high benchmark performance reflects genuine robust reasoning or merely fragile pattern matching overfit to standard textual presentations. Prior adversarial approaches (like GSM-Symbolic) that altered numeric values made it impossible to disentangle reasoning failures from arithmetic failures. When a model fails after a numerical perturbation, it is unclear whether the failure lies in the reasoning logic or the arithmetic calculation. RRB was designed to isolate pure structural fragility by never touching the math itself.\n\n---\n\n### The Key Insight Others Missed\n\nThe fundamental insight is that you can test reasoning robustness without changing the mathematical content at all. By applying deterministic, reversible, textual transformations that preserve the exact mathematical values, logic, and final answer, you can isolate whether a model genuinely \"understands\" a problem or merely pattern-matches on familiar formatting. The transformations are trivial for humans with pen and paper to decode, yet they are structurally hostile to LLM tokenization and attention mechanisms. This exposes that LLM \"reasoning\" is often overfit to standard textual presentation rather than reflecting true mathematical understanding.\n\n---\n\n### How They Formulate the Problem Differently from GSM-Symbolic and GSM-Plus\n\n| Aspect | GSM-Symbolic | GSM-Plus | RRB |\n|--------|-------------|----------|-----|\n| **What changes** | Numeric values via symbolic templates | Eight reasoning-skill perturbations (arithmetic variation, distractor insertion, etc.) | Textual/structural presentation only |\n| **Math preserved?** | No (new numbers) | Partially (varies by perturbation) | Yes, completely -- \"the exact pristine mathematical state\" |\n| **Failure attribution** | Ambiguous (reasoning vs. arithmetic?) | Cleaner but still mixes content changes | Clean: failures are purely structural/tokenization-related |\n| **Determinism** | Template-based but stochastic instantiation | Various | Strictly deterministic, algorithmically invertible |\n| **Domain** | Grade-school math (GSM8K) | Grade-school math (GSM8K) | Competition math (AIME 2024/2025) |\n| **Approach** | LLM-generated perturbations | Skill-based augmentations | Domain-agnostic algorithmic transformations, no LLM in the loop |\n\nRRB forces a two-stage reasoning trajectory: first decode the structural transformation, then solve the math. This separates decoding ability from mathematical reasoning cleanly.\n\n---\n\n### The 13 Deterministic Perturbation Types\n\nOrganized into four categories:\n\n**Category 1 -- Semantic and Lexical Substitutions:**\n1. **Not Not** -- Double negations inserted before numerical values and adjectives (e.g., \"not not least\"). Logically equivalent to the original.\n2. **Opposites** -- Semantic terms remapped to antonyms within queries (e.g., \"short\" means \"long\"), with a substitution key provided in the prompt.\n3. **Wrappers** -- Terms encapsulated in arbitrary syntactic wrappers acting as identity functions (e.g., \"3(p)\" replaces \"p\"), with mappings provided explicitly.\n\n**Category 2 -- Contextual Overload (Interleaved Contexts):**\n4. **Line-level Interleaving** -- Two distinct math problems split into ~60-character segments, alternated with problem tags. The model must extract only the designated problem.\n5. **Word-level Interleaving** -- Words from two problems strictly alternated one-by-one, with the shorter problem repeated to match length.\n6. **Symbol-level Interleaving** -- Individual characters from two problems interwoven character-by-character.\n\n**Category 3 -- Syntactic Distortions:**\n7. **Sentence Reversal** -- Order of sentences (delimited by periods) reversed in the entire query.\n8. **Word Reversal** -- Order of words (space-delimited) reversed throughout the input.\n9. **Symbol Reversal** -- Each word's characters reversed individually while maintaining word positions.\n\n**Category 4 -- Visual and Spatial Encoding:**\n10. **Rail Fence Cipher** -- Symbols placed in zigzag patterns across multiple rows with dots filling gaps; requires diagonal reading to reconstruct.\n11. **Rectangle Perimeter** -- Query mapped onto a rectangle's perimeter flowing clockwise from top-left, with dots filling the center.\n12. **Snake Vertical** -- Text written into grids using vertical zigzag patterns (down column 1, up column 2, down column 3, etc.).\n13. **Snake Horizontal** -- Horizontal boustrophedon pattern (right across row 1, left across row 2, right across row 3, alternating).\n\n**Design principles enforced across all perturbations:**\n- Information-theoretic invariance (no added constraints or ambiguities)\n- Algorithmic reversibility (verified via Python scripts)\n- Cognitive tractability (humans can decode with pen and paper)\n- Explicit decoding protocol provided in plain English in the prompt\n- Grid preservation using dots or perfect padding\n\n**Critical preprocessing steps:** LaTeX comment removal, newline flattening (replacing newlines with semicolons), and escape sequence neutralization (inserting spaces before \\n, \\t, etc. to prevent control character formation during reversals).\n\n---\n\n### Failure Modes Identified\n\n**1. Cognitive Thrashing:** Open-weights reasoning models (particularly Nemotron-7B) enter unproductive token-generation loops rather than failing cleanly. Nemotron-7B generated approximately 27,000 tokens on Rectangle Perimeter tasks while achieving 0% accuracy. The authors observe that \"stopping criteria and logical progression heuristics are highly brittle\" -- the models lack the metacognitive ability to recognize they are confused.\n\n**2. Tokenization Breakdown:** Perturbations that break words into isolated characters (Symbol Reversal, Rail Fence Cipher, character-level interleaving) shatter Byte-Pair Encoding (BPE) boundaries. Models cannot map isolated character tokens back into coherent internal causal graphs, resulting in near-zero accuracy. The authors state: \"Their general reasoning is bottlenecked by subword semantic priors.\"\n\n**3. Reasoning Collapse:** Complete accuracy degradation on specific transformation types. Qwen3-30B drops from strong baseline performance to approximately 1% on Snake (Vertical) tasks. The authors attribute this to \"left-to-right, 1D pre-training biases\" that fundamentally constrain spatial reasoning capabilities.\n\n**4. Intra-Query Attention Dilution (IQAD):** A distinct phenomenon studied in isolation. When models solve multiple independent AIME problems sequentially within a single context window, accuracy on subsequent problems degrades. Attention analysis showed that middle and late transformer layers consistently allocate 10%-16.5% of attention probability mass to irrelevant distractor regions (prior solved problems), and approximately 32.9% of attention in deeper layers attaches to initial system prompts (\"attention sink\" behavior). This is scale-invariant, affecting models from 7B to 120B parameters, suggesting a fundamental architectural limitation.\n\n---\n\n### Existing Techniques Adapted/Combined/Simplified\n\nThe paper does not invent new encoding methods. Instead, it systematizes classical cipher and encoding schemes -- Rail Fence Cipher, boustrophedon (snake) patterns, rectangle perimeter mapping -- and combines them with linguistic transformations (reversals, double negation, antonym substitution, interleaving) into a unified, rigorous evaluation framework with strict design principles. The novelty is in the application to LLM robustness evaluation with formal guarantees of information preservation, not in the individual transformations themselves.\n\n---\n\n### Main Limitations\n\n1. **Domain specificity:** Evaluation focuses exclusively on competitive mathematics (AIME). Generalization to legal, medical, or coding reasoning tasks is unexplored.\n2. **Optimal task granularity is an open question:** The paper discusses the theoretical \"atomic unit of reasoning\" -- the maximum computation a model can perform in a single context state before structural noise degrades algorithmic logic -- but cannot formally quantify it.\n3. **Proprietary model testing was less comprehensive:** Due to computational costs, closed-source models were evaluated on baseline and only 4 sequential problems, whereas open-weights models were tested more exhaustively.\n4. **Generalization of IQAD findings:** Whether the attention dilution phenomenon extends to non-numeric reasoning and how maximum safe \"cognitive load\" scales with parameter count remain open.\n\n---\n\n### Key Quantitative Results\n\n**Frontier (closed-source) models:**\n- **GPT-5.4:** ~3% average accuracy drop across all perturbations -- the most resilient model tested.\n- **Gemini 3.1 Pro:** ~8% average accuracy drop. Scored 99% on Snake (Horizontal) but dropped to 65% on Snake (Vertical), showing sensitivity to spatial orientation.\n- **Claude 4.6 Opus:** ~52% average accuracy drop, but this is primarily driven by categorical refusals, not reasoning failure. Claude's safety filters misclassify symbol manipulation perturbations as prompt injection or jailbreak attempts. It refuses \"the vast majority of prompts involving symbol manipulation.\"\n\n**Open-weights models:**\n- **Nemotron-7B:** ~53% average accuracy drop; 0% accuracy on Rectangle Perimeter with ~27K tokens generated (cognitive thrashing).\n- **Qwen3-30B-A3B-Thinking:** ~47% average accuracy drop; drops to ~1% on Snake (Vertical) vs. 16% on Snake (Horizontal).\n- **DeepSeek-R1-Distill-70B:** Substantial degradation on visual/syntactic tasks (exact average not stated).\n- **OpenAI GPT-OSS-120B:** Tested for IQAD; showed degradation despite being the largest open-weights model.\n- Individual perturbations can cause up to 100% accuracy drops on specific tasks (e.g., symbol-level interleaving).\n\n**IQAD results:** All open-weights models (7B to 120B) and Claude 4.6 Opus showed accuracy decay on later problems in sequential contexts.\n\n---\n\n### Frontier vs. Open-Weights Model Differentiation\n\nThe paper draws a sharp divide:\n- **Frontier models** (GPT-5.4, Gemini 3.1 Pro) show \"remarkable robustness to structural noise\" with minimal performance loss (3-8%), suggesting they may employ undisclosed architectural advantages or post-training techniques for handling structural variation.\n- **Open-weights models** exhibit systematic failure modes (thrashing, tokenization breakdown, collapse) suggesting their reasoning is \"bottlenecked by subword semantic priors\" and overfit to standard token distributions.\n- **Claude** occupies an unusual position: its failures are not reasoning failures but safety-system failures (refusals), making it a different category of vulnerability entirely.\n- The paper notes that proprietary agentic frameworks (including Google's AntiGravity, which leaked screenshots show uses a `&lt;task_boundary_tool>` syntax) already implement explicit contextual resets and task boundaries -- suggesting industry awareness of these phenomena and that frontier providers may already be mitigating attention dilution through scaffolding rather than pure architectural solutions.\n\n---\n\nSources:\n- [Robust Reasoning Benchmark - arXiv Abstract](https://arxiv.org/abs/2604.08571)\n- [Robust Reasoning Benchmark - Full HTML](https://arxiv.org/html/2604.08571v2)\n- [SwiftScholar Paper Detail](https://www.swiftscholar.net/paper/69dd894984947a5132b62b34)\n- [GSM-Plus Paper](https://arxiv.org/abs/2402.19255)\n- [Gennady Pekhimenko - CIFAR Profile](https://cifar.ca/bios/gennady-pekhimenko/)"
      }
    ],
    "totalDurationMs": 182068,
    "totalTokens": 24352,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 609,
      "cache_creation_input_tokens": 2037,
      "cache_read_input_tokens": 18796,
      "output_tokens": 2910,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2037
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 609,
          "output_tokens": 2910,
          "cache_read_input_tokens": 18796,
          "cache_creation_input_tokens": 2037,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2037,
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
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "5a4a5eb3-6bd9-4792-9073-1a4d462bb219",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-29T07:31:35.086Z_

<details><summary>↩ Tool result · `toolu_01WybWba9isbRmofTUGoW4sX`</summary>

```text
I now have a thorough collection of information. Here is the detailed research summary:

---

## GSM-Symbolic: Detailed Research Analysis

### Paper Metadata
- **Authors**: Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)
- **Published**: ICLR 2025 (Poster), originally posted October 7, 2024 on arXiv
- **OpenReview ID**: AjXkRZIvjB

---

### 1. What Gap/Problem Did They Identify, and HOW?

The authors identified that GSM8K -- the most widely used benchmark for evaluating grade-school mathematical reasoning in LLMs -- provides unreliable metrics. Specifically:

- **Data contamination concern**: GSM8K has a fixed set of questions, so models may have been trained on (or seen close variants of) the test set. The authors found that GSM8K performance was more than one standard deviation above the GSM-Symbolic mean for 21 out of 25 models tested, suggesting inflated scores.
- **No variance measurement**: A single accuracy number on a fixed test set provides no information about the *robustness* or *variability* of model reasoning.
- **No controlled difficulty manipulation**: GSM8K has no mechanism to systematically vary question complexity or introduce distractors.

They identified these problems by creating symbolic templates from 100 GSM8K questions and generating 50 different instantiations per template (5,000 total questions), then measuring the distribution of model performance across these semantically equivalent but numerically different questions.

---

### 2. What Was the Key Insight Others Missed?

The central insight is that **what appears to be reasoning is actually sophisticated pattern matching against training distributions**. Specifically:

- Prior work focused on whether LLMs get the right answer; this paper focused on whether performance is *invariant* to irrelevant changes. Genuine reasoning should be robust to (a) changing numerical values, (b) changing proper names, and (c) adding irrelevant information.
- The GSM-NoOp experiment was the most novel contribution: adding a single irrelevant but superficially plausible clause (e.g., "five of them were a bit smaller than average" added to a counting problem) caused catastrophic failures. Models would blindly incorporate this information (e.g., subtracting 5), revealing they match surface patterns rather than understanding problem structure.
- The finding that even providing 8 in-context shots of the same question with its correct solution (NoOp-Symb setting) did not recover performance demonstrates the limitation is not about insufficient context but about fundamental processing.

---

### 3. How Did They Formulate the Problem Differently?

Rather than evaluating LLMs on a single fixed test set, they reformulated math benchmark evaluation as a **distributional measurement**:

- **Symbolic templates**: Each GSM8K question is converted to a template with identified variables, their domains, and constraint conditions (e.g., divisibility requirements to ensure integer answers). Templates use symbolic placeholders for names, numbers, and objects.
- **Multiple instantiations**: 50 random samples per template, creating a distribution of performance rather than a single point estimate.
- **Controlled difficulty variants**:
  - **GSM-M1**: Remove one reasoning clause (easier)
  - **GSM-Symbolic** (base): Same difficulty as GSM8K
  - **GSM-P1**: Add one clause (harder)
  - **GSM-P2**: Add two clauses (hardest)
  - **GSM-NoOp**: Add irrelevant-but-plausible clauses (tests distractor robustness)

This framework separates multiple dimensions: numerical sensitivity, name sensitivity, complexity scaling, and distractor robustness.

---

### 4. What Existing Technique Did They Adapt/Combine/Simplify?

The paper adapts several existing ideas:

- **Template-based benchmark generation**: Similar in spirit to functional benchmarks (Srivastava+ 2024) and TemplateGSM (a concurrent work that generated training data from templates). However, GSM-Symbolic focuses specifically on evaluation with controlled variants.
- **Perturbation-based robustness testing**: The idea of changing numbers/names in math problems has precedent, but the systematic framework with 50 instantiations per template and distributional analysis was new at this scale.
- **Irrelevant information insertion**: Adding distractors to test problems is a well-known technique in education research. The authors adapted it specifically for LLM evaluation with the GSM-NoOp variant.
- **Chain-of-thought evaluation**: Standard 8-shot CoT prompting with greedy decoding, following established protocols.

The novelty was primarily in the *combination* and *systematic application* rather than any single technique.

---

### 5. Key Quantitative Results

**GSM8K vs. GSM-Symbolic (performance drop + variance)**:
| Model | GSM8K | GSM-Symbolic | Variance |
|-------|-------|-------------|----------|
| Gemma2-9B | 87.0% | 79.1% +/- 2.99 | Gap: ~12% worst-to-best |
| Phi-3-mini | 85.0% | 80.7% +/- 2.94 | Gap: ~15% worst-to-best |
| GPT-4o | 95.0% | 94.9% +/- 1.87 | Negligible drop |
| GPT-4o-mini | -- | 91.7% +/- 2.02 | -- |
| o1-mini | -- | 94.5% +/- 1.58 | -- |
| o1-preview | -- | 92.7% +/- 1.82 | -- |

**Difficulty scaling (GSM-M1 through GSM-P2)**:
| Model | GSM-M1 | GSM-Symbolic | GSM-P1 | GSM-P2 |
|-------|--------|-------------|--------|--------|
| Phi-3-mini | 85.9% +/- 2.44 | 80.7% +/- 2.94 | 63.4% +/- 5.63 | 37.5% +/- 5.76 |
| Gemma2-9B | 84.4% +/- 2.36 | 79.1% +/- 2.99 | 68.1% +/- 4.77 | 41.8% +/- 6.00 |
| GPT-4o | 94.4% +/- 1.62 | 94.9% +/- 1.87 | 93.9% +/- 2.59 | 88.0% +/- 3.43 |
| o1-preview | 93.6% +/- 1.68 | 92.7% +/- 1.82 | 95.4% +/- 1.72 | 94.0% +/- 2.38 |

Note: Variance increases monotonically with difficulty for all models. Phi-3-mini drops from 85.9% to 37.5% (48.4 percentage points) going from M1 to P2, while o1-preview is nearly flat.

**GSM-NoOp (catastrophic drops)**:
| Model | GSM-Symbolic | GSM-NoOp | Drop |
|-------|-------------|----------|------|
| Phi-3-mini | 80.7% | 18.0% +/- 3.83 | **62.7 pp** |
| Gemma2-9B | 79.1% | 22.3% +/- 5.11 | **56.8 pp** |
| Llama3-8B | 74.6% | 18.6% +/- 3.86 | **56.0 pp** |
| GPT-4o | 94.9% | 63.1% +/- 4.53 | **31.8 pp** |
| o1-preview | 92.7% | 77.4% +/- 3.84 | **15.3 pp** |

**Fine-tuning ablation**: Fine-tuning Phi-3.5 on 10,000 GSM-P1 examples improved P1 performance slightly but did NOT improve P2 performance, suggesting scaling training data alone does not fix reasoning limitations.

**Arithmetic accuracy**: Added in revision -- computational accuracy remains 97-99% across digit ranges, confirming drops are from reasoning failures, not arithmetic errors.

---

### 6. Reviewer Comments (ICLR 2025)

**Scores**: 8, 8, 6, 6 (accepted as Poster)

**What was praised**:
- Comprehensive empirical analysis across 25+ models (both open and closed)
- Valuable benchmark resource (GSM-Symbolic, GSM-NoOp) for future research
- Highly relevant topic with extensive evidence
- The GSM-NoOp design was singled out as an innovative contribution revealing previously undiscussed LLM vulnerabilities
- Experimental design applicable to other datasets beyond math

**What was criticized**:

1. **Statistical rigor** (most prominent criticism): Multiple reviewers and public commenters (especially Desi Ivanova) noted the paper's statistical analysis was insufficient. Ivanova demonstrated that using proper Wilson score confidence intervals at 5% significance, only 4 of 25 models showed statistically significant differences between GSM8K and GSM-Symbolic. The authors' one-sample t-test was called "methodologically invalid" for comparing two datasets.

2. **Overclaiming**: The area chair explicitly warned against overclaiming that "LLMs cannot reason" since frontier models (GPT-4o, o1) showed minimal drops. The paper's strongest claims are supported mainly by weaker/smaller models.

3. **Novelty concerns**: Reviewer FK55 noted that numerical alteration and irrelevant information insertion are established techniques. TemplateGSM (concurrent work) had similar template-based generation methodology.

4. **Ambiguous reasoning definition**: Multiple reviewers pressed for a rigorous definition of "true logical reasoning" vs. "genuine mathematical reasoning." The authors proposed a definition based on "novelty" (solving problems via logical steps applied to new instances) but this remained contested.

5. **Confounding factors**: Reviewer 7pZc noted that changing numerical ranges (5-100 vs. original values) could cause arithmetic errors unrelated to reasoning. Distribution mismatch between GSM8K and GSM-Symbolic (e.g., original value 62 vs. sampling from [100, 500]) could explain drops without invoking reasoning failures.

6. **Out-of-distribution concern**: Performance degradation with added clauses might reflect distributional shift from training data rather than fundamental reasoning limitations.

**Author responses**:
- Added Appendix A.3 with t-test results (though the statistical criticism was not fully resolved)
- Added Appendix A.6 showing 97-99% arithmetic accuracy, addressing the computation-vs-reasoning confound
- Added fine-tuning experiments in Appendix A.4
- Acknowledged that frontier models (o1 series) show much greater robustness

---

### 7. Main Limitations

1. **Statistical methodology**: The paper's core claims about "non-negligible variance" lack proper hypothesis testing. Ivanova's external analysis showed observed variance is expected under binomial sampling for most models. The increased variance with difficulty is mathematically inevitable (Var = N*p*(1-p)) and not evidence of pattern matching.

2. **Template scope**: Only 100 templates from GSM8K, limiting diversity and generalizability.

3. **Distribution mismatch**: GSM-Symbolic templates sample from different numerical ranges than original GSM8K values, introducing a confound. Tokenization differences for different number magnitudes could affect performance independently of reasoning.

4. **Frontier model robustness**: GPT-4o drops only 0.1% on GSM-Symbolic and o1-preview drops only 15.3% even on NoOp, substantially undermining the paper's strongest claims. The narrative that "LLMs cannot reason" is primarily supported by smaller/weaker models.

5. **No causal mechanism**: The paper demonstrates performance drops but does not provide a mechanistic explanation of *why* models fail (e.g., attention patterns, internal representations).

6. **Fine-tuning was limited**: Only one model (Phi-3.5) was fine-tuned, and on a relatively small dataset. The conclusion that "scaling training data will not help" is not well-supported by a single experiment.

7. **NoOp subjectivity**: The criteria for what constitutes a "no-op" clause and the specific phrasing chosen could be subjective, potentially biasing toward patterns that trigger known model failure modes.

---

### Sources

- [arXiv paper](https://arxiv.org/abs/2410.05229)
- [Full HTML version](https://arxiv.org/html/2410.05229v1)
- [OpenReview forum with reviews](https://openreview.net/forum?id=AjXkRZIvjB)
- [Apple ML Research page](https://machinelearning.apple.com/research/gsm-symbolic)
- [Desi Ivanova's statistical critique](https://desirivanova.com/post/gsm-symbolic/)
- [Gretel.ai / TDS analysis by Alexander Watson](https://medium.com/data-science/gsm-symbolic-analyzing-llm-limitations-in-mathematical-reasoning-and-potential-solutions-363b82370a26)
- [AI Scientist Substack analysis](https://aiscientist.substack.com/p/musing-88-gsm-symbolic-understanding)
- [ICLR 2025 poster page](https://iclr.cc/virtual/2025/poster/30620)

agentId: a9c4346e03b1169e1 (use SendMessage with to: 'a9c4346e03b1169e1' to continue this agent)
&lt;usage>total_tokens: 28928
tool_uses: 20
duration_ms: 241939&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89e2d521-68b8-418b-a89f-276a3644904d",
  "isSidechain": false,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "type": "user",
  "uuid": "d9e65dc7-c969-4750-9f55-48beb679642c",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\" by Mirzadeh et al. (ICLR 2025), available at https://arxiv.org/abs/2410.05229.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for and read OpenReview reviews if available (search \"GSM-Symbolic openreview ICLR 2025\").\n3. Search for any detailed method descriptions or blog posts about the paper.\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- If reviewer comments found: what was praised, what was criticized?\n- Key quantitative results (accuracy drops, variance numbers, etc.)\n\nBe thorough and specific — include numbers, method details, and concrete findings. This will be used for a research analysis.",
    "agentId": "a9c4346e03b1169e1",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a thorough collection of information. Here is the detailed research summary:\n\n---\n\n## GSM-Symbolic: Detailed Research Analysis\n\n### Paper Metadata\n- **Authors**: Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar (Apple)\n- **Published**: ICLR 2025 (Poster), originally posted October 7, 2024 on arXiv\n- **OpenReview ID**: AjXkRZIvjB\n\n---\n\n### 1. What Gap/Problem Did They Identify, and HOW?\n\nThe authors identified that GSM8K -- the most widely used benchmark for evaluating grade-school mathematical reasoning in LLMs -- provides unreliable metrics. Specifically:\n\n- **Data contamination concern**: GSM8K has a fixed set of questions, so models may have been trained on (or seen close variants of) the test set. The authors found that GSM8K performance was more than one standard deviation above the GSM-Symbolic mean for 21 out of 25 models tested, suggesting inflated scores.\n- **No variance measurement**: A single accuracy number on a fixed test set provides no information about the *robustness* or *variability* of model reasoning.\n- **No controlled difficulty manipulation**: GSM8K has no mechanism to systematically vary question complexity or introduce distractors.\n\nThey identified these problems by creating symbolic templates from 100 GSM8K questions and generating 50 different instantiations per template (5,000 total questions), then measuring the distribution of model performance across these semantically equivalent but numerically different questions.\n\n---\n\n### 2. What Was the Key Insight Others Missed?\n\nThe central insight is that **what appears to be reasoning is actually sophisticated pattern matching against training distributions**. Specifically:\n\n- Prior work focused on whether LLMs get the right answer; this paper focused on whether performance is *invariant* to irrelevant changes. Genuine reasoning should be robust to (a) changing numerical values, (b) changing proper names, and (c) adding irrelevant information.\n- The GSM-NoOp experiment was the most novel contribution: adding a single irrelevant but superficially plausible clause (e.g., \"five of them were a bit smaller than average\" added to a counting problem) caused catastrophic failures. Models would blindly incorporate this information (e.g., subtracting 5), revealing they match surface patterns rather than understanding problem structure.\n- The finding that even providing 8 in-context shots of the same question with its correct solution (NoOp-Symb setting) did not recover performance demonstrates the limitation is not about insufficient context but about fundamental processing.\n\n---\n\n### 3. How Did They Formulate the Problem Differently?\n\nRather than evaluating LLMs on a single fixed test set, they reformulated math benchmark evaluation as a **distributional measurement**:\n\n- **Symbolic templates**: Each GSM8K question is converted to a template with identified variables, their domains, and constraint conditions (e.g., divisibility requirements to ensure integer answers). Templates use symbolic placeholders for names, numbers, and objects.\n- **Multiple instantiations**: 50 random samples per template, creating a distribution of performance rather than a single point estimate.\n- **Controlled difficulty variants**:\n  - **GSM-M1**: Remove one reasoning clause (easier)\n  - **GSM-Symbolic** (base): Same difficulty as GSM8K\n  - **GSM-P1**: Add one clause (harder)\n  - **GSM-P2**: Add two clauses (hardest)\n  - **GSM-NoOp**: Add irrelevant-but-plausible clauses (tests distractor robustness)\n\nThis framework separates multiple dimensions: numerical sensitivity, name sensitivity, complexity scaling, and distractor robustness.\n\n---\n\n### 4. What Existing Technique Did They Adapt/Combine/Simplify?\n\nThe paper adapts several existing ideas:\n\n- **Template-based benchmark generation**: Similar in spirit to functional benchmarks (Srivastava+ 2024) and TemplateGSM (a concurrent work that generated training data from templates). However, GSM-Symbolic focuses specifically on evaluation with controlled variants.\n- **Perturbation-based robustness testing**: The idea of changing numbers/names in math problems has precedent, but the systematic framework with 50 instantiations per template and distributional analysis was new at this scale.\n- **Irrelevant information insertion**: Adding distractors to test problems is a well-known technique in education research. The authors adapted it specifically for LLM evaluation with the GSM-NoOp variant.\n- **Chain-of-thought evaluation**: Standard 8-shot CoT prompting with greedy decoding, following established protocols.\n\nThe novelty was primarily in the *combination* and *systematic application* rather than any single technique.\n\n---\n\n### 5. Key Quantitative Results\n\n**GSM8K vs. GSM-Symbolic (performance drop + variance)**:\n| Model | GSM8K | GSM-Symbolic | Variance |\n|-------|-------|-------------|----------|\n| Gemma2-9B | 87.0% | 79.1% +/- 2.99 | Gap: ~12% worst-to-best |\n| Phi-3-mini | 85.0% | 80.7% +/- 2.94 | Gap: ~15% worst-to-best |\n| GPT-4o | 95.0% | 94.9% +/- 1.87 | Negligible drop |\n| GPT-4o-mini | -- | 91.7% +/- 2.02 | -- |\n| o1-mini | -- | 94.5% +/- 1.58 | -- |\n| o1-preview | -- | 92.7% +/- 1.82 | -- |\n\n**Difficulty scaling (GSM-M1 through GSM-P2)**:\n| Model | GSM-M1 | GSM-Symbolic | GSM-P1 | GSM-P2 |\n|-------|--------|-------------|--------|--------|\n| Phi-3-mini | 85.9% +/- 2.44 | 80.7% +/- 2.94 | 63.4% +/- 5.63 | 37.5% +/- 5.76 |\n| Gemma2-9B | 84.4% +/- 2.36 | 79.1% +/- 2.99 | 68.1% +/- 4.77 | 41.8% +/- 6.00 |\n| GPT-4o | 94.4% +/- 1.62 | 94.9% +/- 1.87 | 93.9% +/- 2.59 | 88.0% +/- 3.43 |\n| o1-preview | 93.6% +/- 1.68 | 92.7% +/- 1.82 | 95.4% +/- 1.72 | 94.0% +/- 2.38 |\n\nNote: Variance increases monotonically with difficulty for all models. Phi-3-mini drops from 85.9% to 37.5% (48.4 percentage points) going from M1 to P2, while o1-preview is nearly flat.\n\n**GSM-NoOp (catastrophic drops)**:\n| Model | GSM-Symbolic | GSM-NoOp | Drop |\n|-------|-------------|----------|------|\n| Phi-3-mini | 80.7% | 18.0% +/- 3.83 | **62.7 pp** |\n| Gemma2-9B | 79.1% | 22.3% +/- 5.11 | **56.8 pp** |\n| Llama3-8B | 74.6% | 18.6% +/- 3.86 | **56.0 pp** |\n| GPT-4o | 94.9% | 63.1% +/- 4.53 | **31.8 pp** |\n| o1-preview | 92.7% | 77.4% +/- 3.84 | **15.3 pp** |\n\n**Fine-tuning ablation**: Fine-tuning Phi-3.5 on 10,000 GSM-P1 examples improved P1 performance slightly but did NOT improve P2 performance, suggesting scaling training data alone does not fix reasoning limitations.\n\n**Arithmetic accuracy**: Added in revision -- computational accuracy remains 97-99% across digit ranges, confirming drops are from reasoning failures, not arithmetic errors.\n\n---\n\n### 6. Reviewer Comments (ICLR 2025)\n\n**Scores**: 8, 8, 6, 6 (accepted as Poster)\n\n**What was praised**:\n- Comprehensive empirical analysis across 25+ models (both open and closed)\n- Valuable benchmark resource (GSM-Symbolic, GSM-NoOp) for future research\n- Highly relevant topic with extensive evidence\n- The GSM-NoOp design was singled out as an innovative contribution revealing previously undiscussed LLM vulnerabilities\n- Experimental design applicable to other datasets beyond math\n\n**What was criticized**:\n\n1. **Statistical rigor** (most prominent criticism): Multiple reviewers and public commenters (especially Desi Ivanova) noted the paper's statistical analysis was insufficient. Ivanova demonstrated that using proper Wilson score confidence intervals at 5% significance, only 4 of 25 models showed statistically significant differences between GSM8K and GSM-Symbolic. The authors' one-sample t-test was called \"methodologically invalid\" for comparing two datasets.\n\n2. **Overclaiming**: The area chair explicitly warned against overclaiming that \"LLMs cannot reason\" since frontier models (GPT-4o, o1) showed minimal drops. The paper's strongest claims are supported mainly by weaker/smaller models.\n\n3. **Novelty concerns**: Reviewer FK55 noted that numerical alteration and irrelevant information insertion are established techniques. TemplateGSM (concurrent work) had similar template-based generation methodology.\n\n4. **Ambiguous reasoning definition**: Multiple reviewers pressed for a rigorous definition of \"true logical reasoning\" vs. \"genuine mathematical reasoning.\" The authors proposed a definition based on \"novelty\" (solving problems via logical steps applied to new instances) but this remained contested.\n\n5. **Confounding factors**: Reviewer 7pZc noted that changing numerical ranges (5-100 vs. original values) could cause arithmetic errors unrelated to reasoning. Distribution mismatch between GSM8K and GSM-Symbolic (e.g., original value 62 vs. sampling from [100, 500]) could explain drops without invoking reasoning failures.\n\n6. **Out-of-distribution concern**: Performance degradation with added clauses might reflect distributional shift from training data rather than fundamental reasoning limitations.\n\n**Author responses**:\n- Added Appendix A.3 with t-test results (though the statistical criticism was not fully resolved)\n- Added Appendix A.6 showing 97-99% arithmetic accuracy, addressing the computation-vs-reasoning confound\n- Added fine-tuning experiments in Appendix A.4\n- Acknowledged that frontier models (o1 series) show much greater robustness\n\n---\n\n### 7. Main Limitations\n\n1. **Statistical methodology**: The paper's core claims about \"non-negligible variance\" lack proper hypothesis testing. Ivanova's external analysis showed observed variance is expected under binomial sampling for most models. The increased variance with difficulty is mathematically inevitable (Var = N*p*(1-p)) and not evidence of pattern matching.\n\n2. **Template scope**: Only 100 templates from GSM8K, limiting diversity and generalizability.\n\n3. **Distribution mismatch**: GSM-Symbolic templates sample from different numerical ranges than original GSM8K values, introducing a confound. Tokenization differences for different number magnitudes could affect performance independently of reasoning.\n\n4. **Frontier model robustness**: GPT-4o drops only 0.1% on GSM-Symbolic and o1-preview drops only 15.3% even on NoOp, substantially undermining the paper's strongest claims. The narrative that \"LLMs cannot reason\" is primarily supported by smaller/weaker models.\n\n5. **No causal mechanism**: The paper demonstrates performance drops but does not provide a mechanistic explanation of *why* models fail (e.g., attention patterns, internal representations).\n\n6. **Fine-tuning was limited**: Only one model (Phi-3.5) was fine-tuned, and on a relatively small dataset. The conclusion that \"scaling training data will not help\" is not well-supported by a single experiment.\n\n7. **NoOp subjectivity**: The criteria for what constitutes a \"no-op\" clause and the specific phrasing chosen could be subjective, potentially biasing toward patterns that trigger known model failure modes.\n\n---\n\n### Sources\n\n- [arXiv paper](https://arxiv.org/abs/2410.05229)\n- [Full HTML version](https://arxiv.org/html/2410.05229v1)\n- [OpenReview forum with reviews](https://openreview.net/forum?id=AjXkRZIvjB)\n- [Apple ML Research page](https://machinelearning.apple.com/research/gsm-symbolic)\n- [Desi Ivanova's statistical critique](https://desirivanova.com/post/gsm-symbolic/)\n- [Gretel.ai / TDS analysis by Alexander Watson](https://medium.com/data-science/gsm-symbolic-analyzing-llm-limitations-in-mathematical-reasoning-and-potential-solutions-363b82370a26)\n- [AI Scientist Substack analysis](https://aiscientist.substack.com/p/musing-88-gsm-symbolic-understanding)\n- [ICLR 2025 poster page](https://iclr.cc/virtual/2025/poster/30620)"
      }
    ],
    "totalDurationMs": 241939,
    "totalTokens": 28928,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 499,
      "cache_read_input_tokens": 25070,
      "output_tokens": 3358,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 499
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3358,
          "cache_read_input_tokens": 25070,
          "cache_creation_input_tokens": 499,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 499,
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
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "89e2d521-68b8-418b-a89f-276a3644904d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-29 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "d9e65dc7-c969-4750-9f55-48beb679642c",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on math reasoning robustness",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Tool result

_source line 24 · 2026-05-29T07:31:38.952Z_

<details><summary>↩ Tool result · `toolu_01MyE62JygWjixeWoCnPqxpy`</summary>

````text
Now I have comprehensive data. Let me compile the final detailed summary.

---

## Detailed Research Summary: CREAM (Consistency Regularized Self-Rewarding Language Models)

**Wang et al., ICLR 2025 (Poster) -- Microsoft Research**
Paper: [arXiv:2410.12735](https://arxiv.org/abs/2410.12735) | OpenReview: [Vf6RDObyEF](https://openreview.net/forum?id=Vf6RDObyEF) | Code: [github.com/Raibows/CREAM](https://github.com/Raibows/CREAM)

---

### 1. Problem Identified and How They Found It

Self-Rewarding Language Models (SRLM) use a single LLM as both the policy model (generating responses) and the reward model (scoring/ranking those responses via LLM-as-a-Judge). Ranked responses become preference pairs for DPO training. The fundamental problem: **there is no guarantee of accuracy in the self-assigned rewards and rankings**. This matters because inaccurate preference labels directly corrupt the training signal.

They identified this empirically by observing that 7B-parameter models show **diminishing or even degrading performance after 2-3 iterations** of self-rewarding. On Llama-2 7B, SRLM performance on ARC-Easy catastrophically drops from 60.44% (M1) to 46.55% (M3). They hypothesized this is due to **accumulated bias in the reward system** -- each iteration's errors compound into the next, creating a snowball of unreliable preference data.

### 2. Key Insight Others Missed

The critical insight is that **cross-iteration reward consistency serves as a reliable signal for preference data quality**. If the current model and the previous iteration's model agree on the ranking of responses, that preference pair is likely reliable. If they disagree, the preference label is suspect. Rather than naively trusting all self-generated rewards equally, CREAM uses this consistency signal to modulate confidence in preference labels.

Others had approached related problems through reward model ensembles or pessimistic aggregation of reward values, but these require maintaining multiple models and operate on reward values. CREAM's insight is simpler: **regularize at the preference-label level, not the reward-value level**, using only the two most recent checkpoints (current and previous iteration).

### 3. Novel Problem Formulation

CREAM first formulates a **generalized iterative preference fine-tuning framework** where the optimization alternates between two steps:
- **Step 1 (Preference-labeling):** Determine optimal preference label z using the intrinsic reward r_theta(x,y) proportional to [log pi_theta(y|x) - log pi_ref(y|x)]
- **Step 2 (Learning):** Minimize the combined SFT + DPO loss with z fixed

**Theorem 3.1** proves this two-step procedure converges. The key reformulation is then adding a regularization term to this framework to address overconfident preference labeling.

### 4. Specific Consistency Regularization Technique

The regularization uses **KL divergence to a uniform distribution**. The regularization loss is:

```
L_Reg = -log(sigma(Delta_1)) - log(sigma(Delta_2))
```

**Lemma 3.2** proves that in expectation, this equals:

```
E[L_Reg] = 2 * KL(u(.) || P_theta(.))
```

where u(.) is the uniform distribution over binary preference labels (u(z=0) = u(z=1) = 0.5). The Bayesian intuition (clarified during rebuttal): when a language model self-judges responses, the Bayesian prior should assign equal probability to either preference direction. The regularization pushes the model toward this uniform prior for ambiguous pairs.

**Theorem 3.3** then proves this is equivalent to **soft-labeled DPO**:

```
Loss = C_lambda * L_DPO(theta; y, y', x, z) + (1 - C_lambda) * L_DPO(theta; y, y', x, 1-z)
```

where `C_lambda = (1 + lambda) / (1 + 2*lambda)` is a confidence coefficient and `L_DPO(theta; y, y', x, 1-z)` is the "reversed DPO" loss (swapping chosen and rejected). This is effectively label smoothing for binary preference classification.

### 5. Integration with the Training Loop

The consistency rate C is computed empirically via **Kendall's Tau correlation coefficient**:

```
tau_j = (2 / [N(N-1)]) * sum_{i&lt;i'} [1[(J_ij - J_i'j)(K_ij - K_i'j) > 0] - 1[(J_ij - J_i'j)(K_ij - K_i'j) < 0]]
```

where J_ij = ranking by current model theta_t, K_ij = ranking by previous model theta_{t-1}. The global consistency rate is:

```
C = |D_U|^{-1} * sum_j (tau_j + 1) / 2
```

**Lemma 3.4** connects this to theory: E[tau_j] = 1 - 2*lambda, linking the empirical Kendall's Tau directly to the theoretical regularization parameter.

The final training objective per iteration is:

```
L(theta) = C * L_DPO(pi_theta_t, D_DPO) + (1-C) * L_DPO(pi_theta_t, D_RDPO)
```

where D_RDPO is the reversed DPO dataset (preference labels flipped). The algorithm runs for T iterations (typically T=2-3), with each iteration: (1) sample N responses per prompt, (2) rank with both current and previous models, (3) compute C via Kendall's Tau, (4) train with the soft-labeled DPO objective.

### 6. Existing Techniques Adapted/Combined

CREAM synthesizes several existing ideas:
- **DPO** (Rafailov et al., 2023) as the base alignment method
- **Self-Rewarding LM** (Yuan et al., 2024) as the iterative framework -- but replaces prompt-based LLM-as-a-Judge with implicit DPO-based rewarding (log-probability ratios) because 7B models are too weak for reliable prompt-based judging
- **Label smoothing** -- the final formulation is mathematically equivalent to label smoothing in preference classification
- **Consistency regularization** from semi-supervised learning adapted to the iterative self-improvement setting, where "consistency across iterations" replaces "consistency across augmentations"
- **Kendall's Tau rank correlation** from statistics, repurposed as a dynamic regularization strength estimator

### 7. Key Quantitative Results

**Llama-3 7B (M3 iteration, 5 tasks average):**

| Method | ARC-E | ARC-C | OBQA | SIQA | GSM8K |
|--------|-------|-------|------|------|-------|
| SRLM | 87.17 | 81.23 | 87.30 (degraded) | 70.37 (degraded) | 77.48 (degraded) |
| CREAM | **89.52** | **83.36** | **90.20** | 72.06 | **81.73** |
| Oracle | 89.31 | 81.31 | 90.20 | **73.75** | 76.04 (degraded) |

CREAM outperforms even the Oracle (external InternLM2 reward model) on several tasks.

**Ranking Consistency (Kendall's Tau):**

| Method | M2 vs M1 | M3 vs M2 |
|--------|----------|----------|
| SRLM | -0.22 (poor) | -- |
| CREAM | 0.46 (strong) | 0.84 (excellent) |

Consistency rate distribution: starts at C ~0.39 at M2, stabilizes near 0.9 by M3.

**Llama-2 7B catastrophic failure prevention:** SRLM drops from 60.44% to 46.55% on ARC-Easy across iterations; CREAM recovers to 62.08%.

**Extended iterations (4-6):** CREAM converges at M4 and maintains performance through M6; SRLM degrades by M2.

### 8. Reviewer Feedback (OpenReview)

**Scores:** 1A7Q: 7->8, Nh1y: 6->6, AuNi: 3->6, LeV2: 5->6. Accepted as poster.

**What was praised:**
- Genuine problem with theoretical grounding and mathematical rigor (Theorems 3.1, 3.3, Lemmas 3.2, 3.4)
- Comprehensive experiments with ablations and extended iterations
- Practical efficiency: only two checkpoints needed (vs. ensemble methods needing many)
- Method extends the improvement window beyond the typical 2-3 iterations
- Well-organized presentation of challenges and analysis

**What was criticized:**
- Reviewer AuNi (initially 3/10): Insufficient engagement with reward hacking literature and ensemble-based methods (Fisch et al., 2024). Formalism obscured intuition. Authors provided extensive comparisons showing CREAM is fundamentally different (preference-level vs. reward-value regularization) and more efficient.
- Reviewer LeV2: Questioned motivation for 7B-scale work (why not just use external RMs?). Challenged treating consistency as a model property rather than a data property. Authors showed threshold-based and per-sample dynamic variants perform worse than global average C.
- Reviewer Nh1y: Concerns about reversed DPO reasoning, C=0 edge cases, and stochastic ranking noise. Authors clarified via label-smoothing interpretation and showed C rarely drops to 0.
- Multiple reviewers wanted more iterations (beyond M3) -- authors added M4-M6 results during rebuttal.

### 9. Limitations

1. **Model scale**: Experiments limited to 7B-13B parameter models due to computational constraints. Validation on larger scales is future work.
2. **Prompt-based rewarding failure**: 7B models cannot reliably do LLM-as-a-Judge via prompting, necessitating the DPO-based implicit reward approach. This may limit generality.
3. **Absolute ranking accuracy remains low**: Overall ranking accuracy is at most ~70%, acknowledged as "not satisfying" -- but the consistency regularization compensates by downweighting unreliable pairs.
4. **Requires initial alignment capability**: Tested on pre-trained Llama-3-8B (no chat tuning), the method needs at least SFT to work. It cannot bootstrap from a completely unaligned model.
5. **Baseline model dependency**: First iteration must use the reference model (M0) for consistency since there is no previous iteration checkpoint.

### 10. Why This Matters for Consistency Regularization in Iterative LLM Training

CREAM validates a core principle: **iterative self-improvement in LLMs suffers from compounding errors in self-generated training signals, and cross-iteration consistency provides a principled, lightweight mechanism to detect and mitigate these errors**. The mathematical equivalence to label smoothing (Theorem 3.3) and the connection between Kendall's Tau and the regularization parameter (Lemma 3.4) provide a clean theoretical bridge between empirically measurable consistency and theoretically grounded regularization. The method's efficiency -- requiring only two checkpoints rather than model ensembles -- makes it practical for the iterative training paradigm.

agentId: adc4fac82ef92d176 (use SendMessage with to: 'adc4fac82ef92d176' to continue this agent)
&lt;usage>total_tokens: 28691
tool_uses: 17
duration_ms: 237940&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "dd59c538-a91e-4599-ae22-b0e0d2c21572",
  "isSidechain": false,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "type": "user",
  "uuid": "e7c65140-ab8f-47af-9ea2-7e5e66e63c30",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"CREAM: Consistency Regularized Self-Rewarding Language Models\" by Wang et al. (ICLR 2025), available at https://arxiv.org/abs/2410.12735.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for OpenReview reviews for CREAM ICLR 2025.\n3. Search for any detailed method/technique descriptions.\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- What specific consistency regularization technique did they use (KL divergence, JS divergence, etc.)?\n- How does the consistency term integrate with the training loop?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- If reviewer comments found: what was praised, what was criticized?\n- Key quantitative results\n\nBe thorough and specific — include numbers, method details, and concrete findings. This is particularly important as CREAM validates consistency regularization principles in iterative LLM training.",
    "agentId": "adc4fac82ef92d176",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Let me compile the final detailed summary.\n\n---\n\n## Detailed Research Summary: CREAM (Consistency Regularized Self-Rewarding Language Models)\n\n**Wang et al., ICLR 2025 (Poster) -- Microsoft Research**\nPaper: [arXiv:2410.12735](https://arxiv.org/abs/2410.12735) | OpenReview: [Vf6RDObyEF](https://openreview.net/forum?id=Vf6RDObyEF) | Code: [github.com/Raibows/CREAM](https://github.com/Raibows/CREAM)\n\n---\n\n### 1. Problem Identified and How They Found It\n\nSelf-Rewarding Language Models (SRLM) use a single LLM as both the policy model (generating responses) and the reward model (scoring/ranking those responses via LLM-as-a-Judge). Ranked responses become preference pairs for DPO training. The fundamental problem: **there is no guarantee of accuracy in the self-assigned rewards and rankings**. This matters because inaccurate preference labels directly corrupt the training signal.\n\nThey identified this empirically by observing that 7B-parameter models show **diminishing or even degrading performance after 2-3 iterations** of self-rewarding. On Llama-2 7B, SRLM performance on ARC-Easy catastrophically drops from 60.44% (M1) to 46.55% (M3). They hypothesized this is due to **accumulated bias in the reward system** -- each iteration's errors compound into the next, creating a snowball of unreliable preference data.\n\n### 2. Key Insight Others Missed\n\nThe critical insight is that **cross-iteration reward consistency serves as a reliable signal for preference data quality**. If the current model and the previous iteration's model agree on the ranking of responses, that preference pair is likely reliable. If they disagree, the preference label is suspect. Rather than naively trusting all self-generated rewards equally, CREAM uses this consistency signal to modulate confidence in preference labels.\n\nOthers had approached related problems through reward model ensembles or pessimistic aggregation of reward values, but these require maintaining multiple models and operate on reward values. CREAM's insight is simpler: **regularize at the preference-label level, not the reward-value level**, using only the two most recent checkpoints (current and previous iteration).\n\n### 3. Novel Problem Formulation\n\nCREAM first formulates a **generalized iterative preference fine-tuning framework** where the optimization alternates between two steps:\n- **Step 1 (Preference-labeling):** Determine optimal preference label z using the intrinsic reward r_theta(x,y) proportional to [log pi_theta(y|x) - log pi_ref(y|x)]\n- **Step 2 (Learning):** Minimize the combined SFT + DPO loss with z fixed\n\n**Theorem 3.1** proves this two-step procedure converges. The key reformulation is then adding a regularization term to this framework to address overconfident preference labeling.\n\n### 4. Specific Consistency Regularization Technique\n\nThe regularization uses **KL divergence to a uniform distribution**. The regularization loss is:\n\n```\nL_Reg = -log(sigma(Delta_1)) - log(sigma(Delta_2))\n```\n\n**Lemma 3.2** proves that in expectation, this equals:\n\n```\nE[L_Reg] = 2 * KL(u(.) || P_theta(.))\n```\n\nwhere u(.) is the uniform distribution over binary preference labels (u(z=0) = u(z=1) = 0.5). The Bayesian intuition (clarified during rebuttal): when a language model self-judges responses, the Bayesian prior should assign equal probability to either preference direction. The regularization pushes the model toward this uniform prior for ambiguous pairs.\n\n**Theorem 3.3** then proves this is equivalent to **soft-labeled DPO**:\n\n```\nLoss = C_lambda * L_DPO(theta; y, y', x, z) + (1 - C_lambda) * L_DPO(theta; y, y', x, 1-z)\n```\n\nwhere `C_lambda = (1 + lambda) / (1 + 2*lambda)` is a confidence coefficient and `L_DPO(theta; y, y', x, 1-z)` is the \"reversed DPO\" loss (swapping chosen and rejected). This is effectively label smoothing for binary preference classification.\n\n### 5. Integration with the Training Loop\n\nThe consistency rate C is computed empirically via **Kendall's Tau correlation coefficient**:\n\n```\ntau_j = (2 / [N(N-1)]) * sum_{i&lt;i'} [1[(J_ij - J_i'j)(K_ij - K_i'j) > 0] - 1[(J_ij - J_i'j)(K_ij - K_i'j) < 0]]\n```\n\nwhere J_ij = ranking by current model theta_t, K_ij = ranking by previous model theta_{t-1}. The global consistency rate is:\n\n```\nC = |D_U|^{-1} * sum_j (tau_j + 1) / 2\n```\n\n**Lemma 3.4** connects this to theory: E[tau_j] = 1 - 2*lambda, linking the empirical Kendall's Tau directly to the theoretical regularization parameter.\n\nThe final training objective per iteration is:\n\n```\nL(theta) = C * L_DPO(pi_theta_t, D_DPO) + (1-C) * L_DPO(pi_theta_t, D_RDPO)\n```\n\nwhere D_RDPO is the reversed DPO dataset (preference labels flipped). The algorithm runs for T iterations (typically T=2-3), with each iteration: (1) sample N responses per prompt, (2) rank with both current and previous models, (3) compute C via Kendall's Tau, (4) train with the soft-labeled DPO objective.\n\n### 6. Existing Techniques Adapted/Combined\n\nCREAM synthesizes several existing ideas:\n- **DPO** (Rafailov et al., 2023) as the base alignment method\n- **Self-Rewarding LM** (Yuan et al., 2024) as the iterative framework -- but replaces prompt-based LLM-as-a-Judge with implicit DPO-based rewarding (log-probability ratios) because 7B models are too weak for reliable prompt-based judging\n- **Label smoothing** -- the final formulation is mathematically equivalent to label smoothing in preference classification\n- **Consistency regularization** from semi-supervised learning adapted to the iterative self-improvement setting, where \"consistency across iterations\" replaces \"consistency across augmentations\"\n- **Kendall's Tau rank correlation** from statistics, repurposed as a dynamic regularization strength estimator\n\n### 7. Key Quantitative Results\n\n**Llama-3 7B (M3 iteration, 5 tasks average):**\n\n| Method | ARC-E | ARC-C | OBQA | SIQA | GSM8K |\n|--------|-------|-------|------|------|-------|\n| SRLM | 87.17 | 81.23 | 87.30 (degraded) | 70.37 (degraded) | 77.48 (degraded) |\n| CREAM | **89.52** | **83.36** | **90.20** | 72.06 | **81.73** |\n| Oracle | 89.31 | 81.31 | 90.20 | **73.75** | 76.04 (degraded) |\n\nCREAM outperforms even the Oracle (external InternLM2 reward model) on several tasks.\n\n**Ranking Consistency (Kendall's Tau):**\n\n| Method | M2 vs M1 | M3 vs M2 |\n|--------|----------|----------|\n| SRLM | -0.22 (poor) | -- |\n| CREAM | 0.46 (strong) | 0.84 (excellent) |\n\nConsistency rate distribution: starts at C ~0.39 at M2, stabilizes near 0.9 by M3.\n\n**Llama-2 7B catastrophic failure prevention:** SRLM drops from 60.44% to 46.55% on ARC-Easy across iterations; CREAM recovers to 62.08%.\n\n**Extended iterations (4-6):** CREAM converges at M4 and maintains performance through M6; SRLM degrades by M2.\n\n### 8. Reviewer Feedback (OpenReview)\n\n**Scores:** 1A7Q: 7->8, Nh1y: 6->6, AuNi: 3->6, LeV2: 5->6. Accepted as poster.\n\n**What was praised:**\n- Genuine problem with theoretical grounding and mathematical rigor (Theorems 3.1, 3.3, Lemmas 3.2, 3.4)\n- Comprehensive experiments with ablations and extended iterations\n- Practical efficiency: only two checkpoints needed (vs. ensemble methods needing many)\n- Method extends the improvement window beyond the typical 2-3 iterations\n- Well-organized presentation of challenges and analysis\n\n**What was criticized:**\n- Reviewer AuNi (initially 3/10): Insufficient engagement with reward hacking literature and ensemble-based methods (Fisch et al., 2024). Formalism obscured intuition. Authors provided extensive comparisons showing CREAM is fundamentally different (preference-level vs. reward-value regularization) and more efficient.\n- Reviewer LeV2: Questioned motivation for 7B-scale work (why not just use external RMs?). Challenged treating consistency as a model property rather than a data property. Authors showed threshold-based and per-sample dynamic variants perform worse than global average C.\n- Reviewer Nh1y: Concerns about reversed DPO reasoning, C=0 edge cases, and stochastic ranking noise. Authors clarified via label-smoothing interpretation and showed C rarely drops to 0.\n- Multiple reviewers wanted more iterations (beyond M3) -- authors added M4-M6 results during rebuttal.\n\n### 9. Limitations\n\n1. **Model scale**: Experiments limited to 7B-13B parameter models due to computational constraints. Validation on larger scales is future work.\n2. **Prompt-based rewarding failure**: 7B models cannot reliably do LLM-as-a-Judge via prompting, necessitating the DPO-based implicit reward approach. This may limit generality.\n3. **Absolute ranking accuracy remains low**: Overall ranking accuracy is at most ~70%, acknowledged as \"not satisfying\" -- but the consistency regularization compensates by downweighting unreliable pairs.\n4. **Requires initial alignment capability**: Tested on pre-trained Llama-3-8B (no chat tuning), the method needs at least SFT to work. It cannot bootstrap from a completely unaligned model.\n5. **Baseline model dependency**: First iteration must use the reference model (M0) for consistency since there is no previous iteration checkpoint.\n\n### 10. Why This Matters for Consistency Regularization in Iterative LLM Training\n\nCREAM validates a core principle: **iterative self-improvement in LLMs suffers from compounding errors in self-generated training signals, and cross-iteration consistency provides a principled, lightweight mechanism to detect and mitigate these errors**. The mathematical equivalence to label smoothing (Theorem 3.3) and the connection between Kendall's Tau and the regularization parameter (Lemma 3.4) provide a clean theoretical bridge between empirically measurable consistency and theoretically grounded regularization. The method's efficiency -- requiring only two checkpoints rather than model ensembles -- makes it practical for the iterative training paradigm."
      }
    ],
    "totalDurationMs": 237940,
    "totalTokens": 28691,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2333,
      "cache_read_input_tokens": 23496,
      "output_tokens": 2861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2333
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2861,
          "cache_read_input_tokens": 23496,
          "cache_creation_input_tokens": 2333,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2333,
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
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "dd59c538-a91e-4599-ae22-b0e0d2c21572",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 25 · 2026-05-29T07:31:54.373Z_

<details><summary>↩ Tool result · `toolu_01PDP25UBSLkATujUnyvr6HG`</summary>

```text


I now have comprehensive information from the full paper. I can see the limitations section, the complete methodology, all results, and the Polya's principles mapping. Let me compile my detailed summary.

---

## Detailed Summary: GSM-Plus (Li et al., ACL 2024)

**Paper:** "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers"
**Authors:** Qintong Li, Leyang Cui, Xueliang Zhao, Lingpeng Kong, Wei Bi (University of Hong Kong & Tencent AI Lab)
**Venue:** ACL 2024 (62nd Annual Meeting, Long Papers), Bangkok, Thailand, pages 2961-2984

---

### 1. What Gap/Problem Did They Identify, and HOW?

The authors identified that **high LLM accuracy on GSM8K (the most popular grade-school math benchmark) does not reflect genuine mathematical understanding**. At the time of writing, GPT-4 exceeded 90% and open-source models exceeded 80% on GSM8K. However, the community debated whether this performance reflected true mathematical reasoning or superficial pattern matching / training data leakage.

They identified this gap through **concrete empirical observation**: Figure 1 of the paper shows GPT-3.5-Turbo correctly solving a GSM8K question about James walking away from home, but failing on a trivially modified version where the direction word changes from "leave" to "return." The model misuses the operator (adding instead of subtracting), making "simple errors that humans would not." This motivated them to systematically test robustness.

They also surveyed existing robustness benchmarks (Table 1 in the paper) and found that prior datasets each covered only **limited perturbation types**: SVAMP covered paraphrasing + rule-based perturbations; GSM-IC covered only distractors; GSM8K_robust covered only numerical variations. No single benchmark comprehensively tested all the mathematical reasoning skills needed.

Their benchmark revealed **a gap of up to 20% between reported accuracy and adversarial accuracy**, while human performance remained unaffected (actually slightly improved from 96.77% to 98.75%).

---

### 2. What Was the Key Insight Others Missed?

The central insight was that **robustness requires testing across multiple, qualitatively different reasoning capabilities simultaneously, not just one perturbation type at a time.** Prior work tested individual aspects (e.g., just numerical substitution, just distractors) and thus gave an incomplete picture. GSM-Plus is the first benchmark to apply all 8 perturbation types to every single question, enabling a holistic per-question robustness profile.

A second critical insight was that **arithmetic variation (especially reversing operations) and critical thinking were severely underexplored** because they are hard to annotate automatically. Previous findings suggested LLMs were "typically robust to numerical variation and problem understanding" (from Bubeck et al., 2023; Zhou et al., 2023b), which created a false sense of security. GSM-Plus revealed that these previously untested dimensions are precisely where LLMs fail most catastrophically -- with nearly 100% performance drop rates for critical thinking across most open-source models.

A third insight: **math-specific SFT (supervised fine-tuning) improves benchmark accuracy but does NOT meaningfully improve robustness.** The PDR of SFT models is not significantly smaller than their foundation models. For example, LLaMA-2-13B has a PDR of 34.76% while its SFT derivative Abel-13B has a PDR of 31.97% -- marginal improvement despite large accuracy gains on the standard benchmark.

---

### 3. How Did They Formulate the Problem Differently? (The Perturbation Taxonomy)

Motivated by **Polya's principles** (from "How to Solve It," 1945/2004), which describe four stages of human mathematical problem-solving: (1) identifying variables and relevant context, (2) representing the problem's structure and discovering a potential pattern, (3) calculating an answer, and (4) verifying correctness -- the authors designed **8 perturbation types from 5 perspectives**:

**Perspective 1 -- Numerical Variation** (tests overfitting to specific numbers; maps to Polya's stage 1):
- **Numerical Substitution**: Replaces numbers with same-digit-count alternatives (e.g., "16" to "20"). GPT-4 pass rate: 91.51%.
- **Digit Expansion**: Increases digit count (e.g., "16" to "1600"). GPT-4 pass rate: 92.60%.
- **Integer-Decimal-Fraction Conversion (IDF)**: Changes number representation type (e.g., "2" to "2.5", or "1/4" to "0.25"). GPT-4 pass rate: 84.24%.

**Perspective 2 -- Arithmetic Variation** (tests flexible application of operations; maps to Polya's stages 2-3):
- **Adding Operation**: Inserts additional statements requiring extra arithmetic steps. GPT-4 pass rate: 75.75%.
- **Reversing Operation**: Transforms the original answer into a known condition and asks for a previously-known value (backward reasoning). GPT-4 pass rate: 29.76% (the hardest for GPT-4 to generate correctly).

**Perspective 3 -- Problem Understanding** (tests comprehension robustness; maps to Polya's stage 1):
- **Problem Understanding**: Rephrases text while preserving meaning and answer. GPT-4 pass rate: 97.49%.

**Perspective 4 -- Distractor Insertion** (tests statement evaluation ability; maps to Polya's stage 4):
- **Distractor Insertion**: Adds topic-related but irrelevant sentences containing numbers. GPT-4 pass rate: 88.25%.

**Perspective 5 -- Critical Thinking** (tests ability to recognize unsolvable problems; maps to Polya's stage 4):
- **Critical Thinking**: Removes an essential statement, making the problem unsolvable. The correct response is to recognize the missing information. GPT-4 pass rate: 87.77%.

---

### 4. What Existing Technique Did They Adapt/Combine/Simplify?

**For dataset construction**, they adapted a **GPT-4 generation + human refinement pipeline**. GPT-4 initially generated all question variations and answers, but the authors discovered GPT-4 was unreliable -- it could: (i) fail to incorporate perturbations, (ii) make additional unspecified changes, (iii) generate invalid questions, (iv) make questions too difficult, or (v) produce wrong answers. Human annotators revised 18.85% of GPT-4's outputs. This hybrid approach was more scalable than pure human annotation but more reliable than pure LLM generation.

**For the proposed robustness improvement method (Compositional Prompting, COMP)**, they combined and adapted ideas from two existing techniques:
1. **Decomposed prompting** (Khot et al., 2022) -- iteratively breaking complex problems into subproblems, borrowed from multi-hop QA.
2. **Self-refinement / iterative feedback** (Madaan et al., 2023; Yu et al., 2023b) -- having LLMs verify and correct each generation step.

COMP works in four steps using four separate prompts:
1. **Premise Extraction (Prompt 1)**: Extract essential numerical premises from the question.
2. **Subgoal Generation (Prompt 2)**: Generate the reasoning goal for the current thought step.
3. **Calculation (Prompt 3)**: Perform the calculation for that subgoal, with explicit verification instructions (e.g., "If you have a strong belief that errors exist in the above reasoning step, explain why and regenerate this step. Otherwise, output 'Pass'").
4. **Completion Verification (Prompt 4)**: Check whether the final answer has been reached. If not, iterate.

This is essentially a **compositional chain-of-thought with built-in per-step verification**, adapted from multi-hop QA and self-refinement to the math domain.

---

### 5. Key Quantitative Results

**Scale:** 1,319 GSM8K seed questions x 8 perturbations = **10,552 total question variations**. Tested on **25 LLMs** with **4 prompting techniques** (CoT, PoT, LtM, Complexity-based CoT).

**Overall Performance (Table 4/8 from paper):**

| Model | GSM8K | GSM-Plus | PDR | ASP |
|---|---|---|---|---|
| Human | 96.77% | 98.75% | -2.05% | 92.11% |
| GPT-4 | 93.25% | 85.58% | 8.23% | 81.54% |
| GPT-3.5-Turbo | 73.62% | 61.19% | 16.88% | 51.36% |
| LLaMA-2-70B | 56.71% | 40.04% | 29.40% | 32.31% |
| MetaMath-Mistral-7B | 77.79% | 56.25% | 27.69% | 50.56% |
| CodeLlama-34B | 45.64% | 30.00% | 34.27% | 22.42% |
| Abel-70B | 83.85% | 59.94% | 28.52% | 55.31% |

**Performance by Perturbation Type (vulnerability ranking, worst to best):**
- **Critical Thinking**: Nearly 100% PDR for most open-source models. Models hallucinate solutions instead of recognizing missing information. Only GPT-4 and GPT-3.5-Turbo show partial resilience.
- **Arithmetic Variation (Adding/Reversing)**: Exceeding 40% PDR for most models. All models exhibit notable PDR when reversing statements (backward reasoning).
- **Distractor Insertion**: 16.1%-40.6% PDR. Program-based models are especially sensitive (MAmmoTH-13B: 40.6%, SEGO-13B: 43.9%).
- **IDF Conversion**: Significant drops, especially for program-based models that confuse decimal representations (e.g., treating "0.25" as the literal number rather than "1/4").
- **Numerical Substitution & Digit Expansion**: Minimal fluctuations. LLaMA-2-13B even shows slight 2.1% improvement on numerical substitution.
- **Problem Understanding**: Most LLMs show robust performance.

**Prompting Results (GPT-3.5-Turbo, Table 5):**

| Method | GSM8K | GSM-Plus | Crit. Thinking |
|---|---|---|---|
| CoT | 74.17 | 62.92 | 40.83 |
| LtM | 74.17 | 62.60 | 39.17 |
| COMP | 76.67 | 65.52 | 54.17 |
| CoT + SC | 76.67 | 65.88 | 40.00 |
| COMP + SC | 80.00 | 69.47 | 55.83 |

COMP improves +3.4% on GSM8K and +4.7% on GSM-Plus over LtM. Critical thinking improved from 40.83% to 54.17%.

**Key model-level findings:**
- Larger models generally display lower PDR than smaller models (Abel-7B: 37.67%, Abel-13B: 31.97%, Abel-70B: 28.52%).
- Good foundation models help both accuracy and robustness: MetaMath-Mistral-7B (PDR 27.69%) outperforms MetaMath-7B on LLaMA-2 (PDR 33.53%).
- SFT dataset choice matters significantly: LLaMA-2-7B fine-tuned on different datasets yields PDRs of 33.53% (MetaMathQA), 37.67% (Abel-data), 35.39% (TORA-CORPUS), and 39.17% (MathInstruct).
- CodeLlama shows the largest PDR among foundation models (40.56%-39.71%), suggesting program-only LLMs need natural language guidance for robust math reasoning.

---

### 6. Limitations (Explicitly Stated by Authors)

The paper includes three explicit limitations:

1. **Scope limited to elementary school math.** The work focuses on grade-school level (GSM8K). Evaluating robustness at other educational levels (high school, college) is left as future work.

2. **No analysis of solution chain correctness.** They compare only final answer accuracy on GSM8K vs. GSM-Plus using PDR and ASP metrics. They do not investigate the accuracy of intermediate reasoning steps "due to the challenges in designing a reliable metric for this purpose."

3. **No investigation of root causes of failure.** GSM-Plus evaluates robustness under various perturbations but "does not investigate the underlying reasons behind the failures of solving problems."

**Additional implicit limitations:**
- The dataset is **static** and could become a memorization target over time.
- GPT-4 involvement in question generation could introduce **preference bias**, though Table 3 suggests minimal impact (GPT-4 scores 87.36% on its own variations vs. 85.58% on human-corrected ones).
- The **Reversing Operation** perturbation had the lowest GPT-4 generation pass rate (29.76%), suggesting these are the hardest to create correctly and may have quality issues.
- COMP does not fully bridge the robustness gap: "Although compositional prompting improves performance on seed questions and their variations, it does not bridge the performance gap of LLMs between the standard benchmark and the adversarial benchmark."

---

### 7. Reviewer Comments

The ACL ARR reviews for this paper are **not publicly available**. The OpenReview page (https://openreview.net/forum?id=4V8OgFU8gTR) shows "0 Replies" -- the reviews were conducted through the ACL Rolling Review process but were not made public on the platform. The paper was accepted as an ACL 2024 Long Paper, indicating it received favorable reviews overall. The acknowledgements thank "the anonymous reviewers for reviewing the paper and providing helpful feedback," confirming the review process occurred but the content is not accessible.

---

### Summary of Contribution

GSM-Plus fills a critical gap by being the first benchmark to apply a comprehensive, theoretically-grounded (Polya's principles) set of 8 perturbation types across all 1,319 GSM8K test questions, producing 10,552 adversarial variants. Its main finding -- that LLMs achieving 90%+ on GSM8K drop by up to 20% on perturbed versions while humans remain unaffected -- provides strong evidence that high benchmark scores mask shallow reasoning. The most damaging finding is that critical thinking (recognizing unsolvable problems) causes near-complete failure in open-source models, and that math-specific fine-tuning improves accuracy without meaningfully improving robustness.

agentId: a5381cb0eaf656a29 (use SendMessage with to: 'a5381cb0eaf656a29' to continue this agent)
&lt;usage>total_tokens: 58295
tool_uses: 23
duration_ms: 257732&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "36dc2167-aa87-4707-b31e-1a8650ed55cb",
  "isSidechain": false,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "type": "user",
  "uuid": "77f20e96-d74b-4cca-8f27-848dbda86663",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers\" by Li et al. (ACL 2024), available at https://arxiv.org/abs/2402.19255.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for any OpenReview or ACL Anthology reviews.\n3. Search for any detailed method descriptions.\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently (the perturbation taxonomy)?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- If reviewer comments found: what was praised, what was criticized?\n- Key quantitative results (how many perturbation types, accuracy drops, number of LLMs tested)\n\nBe thorough and specific — include numbers, method details, and concrete findings.",
    "agentId": "a5381cb0eaf656a29",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "\n\nI now have comprehensive information from the full paper. I can see the limitations section, the complete methodology, all results, and the Polya's principles mapping. Let me compile my detailed summary.\n\n---\n\n## Detailed Summary: GSM-Plus (Li et al., ACL 2024)\n\n**Paper:** \"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers\"\n**Authors:** Qintong Li, Leyang Cui, Xueliang Zhao, Lingpeng Kong, Wei Bi (University of Hong Kong & Tencent AI Lab)\n**Venue:** ACL 2024 (62nd Annual Meeting, Long Papers), Bangkok, Thailand, pages 2961-2984\n\n---\n\n### 1. What Gap/Problem Did They Identify, and HOW?\n\nThe authors identified that **high LLM accuracy on GSM8K (the most popular grade-school math benchmark) does not reflect genuine mathematical understanding**. At the time of writing, GPT-4 exceeded 90% and open-source models exceeded 80% on GSM8K. However, the community debated whether this performance reflected true mathematical reasoning or superficial pattern matching / training data leakage.\n\nThey identified this gap through **concrete empirical observation**: Figure 1 of the paper shows GPT-3.5-Turbo correctly solving a GSM8K question about James walking away from home, but failing on a trivially modified version where the direction word changes from \"leave\" to \"return.\" The model misuses the operator (adding instead of subtracting), making \"simple errors that humans would not.\" This motivated them to systematically test robustness.\n\nThey also surveyed existing robustness benchmarks (Table 1 in the paper) and found that prior datasets each covered only **limited perturbation types**: SVAMP covered paraphrasing + rule-based perturbations; GSM-IC covered only distractors; GSM8K_robust covered only numerical variations. No single benchmark comprehensively tested all the mathematical reasoning skills needed.\n\nTheir benchmark revealed **a gap of up to 20% between reported accuracy and adversarial accuracy**, while human performance remained unaffected (actually slightly improved from 96.77% to 98.75%).\n\n---\n\n### 2. What Was the Key Insight Others Missed?\n\nThe central insight was that **robustness requires testing across multiple, qualitatively different reasoning capabilities simultaneously, not just one perturbation type at a time.** Prior work tested individual aspects (e.g., just numerical substitution, just distractors) and thus gave an incomplete picture. GSM-Plus is the first benchmark to apply all 8 perturbation types to every single question, enabling a holistic per-question robustness profile.\n\nA second critical insight was that **arithmetic variation (especially reversing operations) and critical thinking were severely underexplored** because they are hard to annotate automatically. Previous findings suggested LLMs were \"typically robust to numerical variation and problem understanding\" (from Bubeck et al., 2023; Zhou et al., 2023b), which created a false sense of security. GSM-Plus revealed that these previously untested dimensions are precisely where LLMs fail most catastrophically -- with nearly 100% performance drop rates for critical thinking across most open-source models.\n\nA third insight: **math-specific SFT (supervised fine-tuning) improves benchmark accuracy but does NOT meaningfully improve robustness.** The PDR of SFT models is not significantly smaller than their foundation models. For example, LLaMA-2-13B has a PDR of 34.76% while its SFT derivative Abel-13B has a PDR of 31.97% -- marginal improvement despite large accuracy gains on the standard benchmark.\n\n---\n\n### 3. How Did They Formulate the Problem Differently? (The Perturbation Taxonomy)\n\nMotivated by **Polya's principles** (from \"How to Solve It,\" 1945/2004), which describe four stages of human mathematical problem-solving: (1) identifying variables and relevant context, (2) representing the problem's structure and discovering a potential pattern, (3) calculating an answer, and (4) verifying correctness -- the authors designed **8 perturbation types from 5 perspectives**:\n\n**Perspective 1 -- Numerical Variation** (tests overfitting to specific numbers; maps to Polya's stage 1):\n- **Numerical Substitution**: Replaces numbers with same-digit-count alternatives (e.g., \"16\" to \"20\"). GPT-4 pass rate: 91.51%.\n- **Digit Expansion**: Increases digit count (e.g., \"16\" to \"1600\"). GPT-4 pass rate: 92.60%.\n- **Integer-Decimal-Fraction Conversion (IDF)**: Changes number representation type (e.g., \"2\" to \"2.5\", or \"1/4\" to \"0.25\"). GPT-4 pass rate: 84.24%.\n\n**Perspective 2 -- Arithmetic Variation** (tests flexible application of operations; maps to Polya's stages 2-3):\n- **Adding Operation**: Inserts additional statements requiring extra arithmetic steps. GPT-4 pass rate: 75.75%.\n- **Reversing Operation**: Transforms the original answer into a known condition and asks for a previously-known value (backward reasoning). GPT-4 pass rate: 29.76% (the hardest for GPT-4 to generate correctly).\n\n**Perspective 3 -- Problem Understanding** (tests comprehension robustness; maps to Polya's stage 1):\n- **Problem Understanding**: Rephrases text while preserving meaning and answer. GPT-4 pass rate: 97.49%.\n\n**Perspective 4 -- Distractor Insertion** (tests statement evaluation ability; maps to Polya's stage 4):\n- **Distractor Insertion**: Adds topic-related but irrelevant sentences containing numbers. GPT-4 pass rate: 88.25%.\n\n**Perspective 5 -- Critical Thinking** (tests ability to recognize unsolvable problems; maps to Polya's stage 4):\n- **Critical Thinking**: Removes an essential statement, making the problem unsolvable. The correct response is to recognize the missing information. GPT-4 pass rate: 87.77%.\n\n---\n\n### 4. What Existing Technique Did They Adapt/Combine/Simplify?\n\n**For dataset construction**, they adapted a **GPT-4 generation + human refinement pipeline**. GPT-4 initially generated all question variations and answers, but the authors discovered GPT-4 was unreliable -- it could: (i) fail to incorporate perturbations, (ii) make additional unspecified changes, (iii) generate invalid questions, (iv) make questions too difficult, or (v) produce wrong answers. Human annotators revised 18.85% of GPT-4's outputs. This hybrid approach was more scalable than pure human annotation but more reliable than pure LLM generation.\n\n**For the proposed robustness improvement method (Compositional Prompting, COMP)**, they combined and adapted ideas from two existing techniques:\n1. **Decomposed prompting** (Khot et al., 2022) -- iteratively breaking complex problems into subproblems, borrowed from multi-hop QA.\n2. **Self-refinement / iterative feedback** (Madaan et al., 2023; Yu et al., 2023b) -- having LLMs verify and correct each generation step.\n\nCOMP works in four steps using four separate prompts:\n1. **Premise Extraction (Prompt 1)**: Extract essential numerical premises from the question.\n2. **Subgoal Generation (Prompt 2)**: Generate the reasoning goal for the current thought step.\n3. **Calculation (Prompt 3)**: Perform the calculation for that subgoal, with explicit verification instructions (e.g., \"If you have a strong belief that errors exist in the above reasoning step, explain why and regenerate this step. Otherwise, output 'Pass'\").\n4. **Completion Verification (Prompt 4)**: Check whether the final answer has been reached. If not, iterate.\n\nThis is essentially a **compositional chain-of-thought with built-in per-step verification**, adapted from multi-hop QA and self-refinement to the math domain.\n\n---\n\n### 5. Key Quantitative Results\n\n**Scale:** 1,319 GSM8K seed questions x 8 perturbations = **10,552 total question variations**. Tested on **25 LLMs** with **4 prompting techniques** (CoT, PoT, LtM, Complexity-based CoT).\n\n**Overall Performance (Table 4/8 from paper):**\n\n| Model | GSM8K | GSM-Plus | PDR | ASP |\n|---|---|---|---|---|\n| Human | 96.77% | 98.75% | -2.05% | 92.11% |\n| GPT-4 | 93.25% | 85.58% | 8.23% | 81.54% |\n| GPT-3.5-Turbo | 73.62% | 61.19% | 16.88% | 51.36% |\n| LLaMA-2-70B | 56.71% | 40.04% | 29.40% | 32.31% |\n| MetaMath-Mistral-7B | 77.79% | 56.25% | 27.69% | 50.56% |\n| CodeLlama-34B | 45.64% | 30.00% | 34.27% | 22.42% |\n| Abel-70B | 83.85% | 59.94% | 28.52% | 55.31% |\n\n**Performance by Perturbation Type (vulnerability ranking, worst to best):**\n- **Critical Thinking**: Nearly 100% PDR for most open-source models. Models hallucinate solutions instead of recognizing missing information. Only GPT-4 and GPT-3.5-Turbo show partial resilience.\n- **Arithmetic Variation (Adding/Reversing)**: Exceeding 40% PDR for most models. All models exhibit notable PDR when reversing statements (backward reasoning).\n- **Distractor Insertion**: 16.1%-40.6% PDR. Program-based models are especially sensitive (MAmmoTH-13B: 40.6%, SEGO-13B: 43.9%).\n- **IDF Conversion**: Significant drops, especially for program-based models that confuse decimal representations (e.g., treating \"0.25\" as the literal number rather than \"1/4\").\n- **Numerical Substitution & Digit Expansion**: Minimal fluctuations. LLaMA-2-13B even shows slight 2.1% improvement on numerical substitution.\n- **Problem Understanding**: Most LLMs show robust performance.\n\n**Prompting Results (GPT-3.5-Turbo, Table 5):**\n\n| Method | GSM8K | GSM-Plus | Crit. Thinking |\n|---|---|---|---|\n| CoT | 74.17 | 62.92 | 40.83 |\n| LtM | 74.17 | 62.60 | 39.17 |\n| COMP | 76.67 | 65.52 | 54.17 |\n| CoT + SC | 76.67 | 65.88 | 40.00 |\n| COMP + SC | 80.00 | 69.47 | 55.83 |\n\nCOMP improves +3.4% on GSM8K and +4.7% on GSM-Plus over LtM. Critical thinking improved from 40.83% to 54.17%.\n\n**Key model-level findings:**\n- Larger models generally display lower PDR than smaller models (Abel-7B: 37.67%, Abel-13B: 31.97%, Abel-70B: 28.52%).\n- Good foundation models help both accuracy and robustness: MetaMath-Mistral-7B (PDR 27.69%) outperforms MetaMath-7B on LLaMA-2 (PDR 33.53%).\n- SFT dataset choice matters significantly: LLaMA-2-7B fine-tuned on different datasets yields PDRs of 33.53% (MetaMathQA), 37.67% (Abel-data), 35.39% (TORA-CORPUS), and 39.17% (MathInstruct).\n- CodeLlama shows the largest PDR among foundation models (40.56%-39.71%), suggesting program-only LLMs need natural language guidance for robust math reasoning.\n\n---\n\n### 6. Limitations (Explicitly Stated by Authors)\n\nThe paper includes three explicit limitations:\n\n1. **Scope limited to elementary school math.** The work focuses on grade-school level (GSM8K). Evaluating robustness at other educational levels (high school, college) is left as future work.\n\n2. **No analysis of solution chain correctness.** They compare only final answer accuracy on GSM8K vs. GSM-Plus using PDR and ASP metrics. They do not investigate the accuracy of intermediate reasoning steps \"due to the challenges in designing a reliable metric for this purpose.\"\n\n3. **No investigation of root causes of failure.** GSM-Plus evaluates robustness under various perturbations but \"does not investigate the underlying reasons behind the failures of solving problems.\"\n\n**Additional implicit limitations:**\n- The dataset is **static** and could become a memorization target over time.\n- GPT-4 involvement in question generation could introduce **preference bias**, though Table 3 suggests minimal impact (GPT-4 scores 87.36% on its own variations vs. 85.58% on human-corrected ones).\n- The **Reversing Operation** perturbation had the lowest GPT-4 generation pass rate (29.76%), suggesting these are the hardest to create correctly and may have quality issues.\n- COMP does not fully bridge the robustness gap: \"Although compositional prompting improves performance on seed questions and their variations, it does not bridge the performance gap of LLMs between the standard benchmark and the adversarial benchmark.\"\n\n---\n\n### 7. Reviewer Comments\n\nThe ACL ARR reviews for this paper are **not publicly available**. The OpenReview page (https://openreview.net/forum?id=4V8OgFU8gTR) shows \"0 Replies\" -- the reviews were conducted through the ACL Rolling Review process but were not made public on the platform. The paper was accepted as an ACL 2024 Long Paper, indicating it received favorable reviews overall. The acknowledgements thank \"the anonymous reviewers for reviewing the paper and providing helpful feedback,\" confirming the review process occurred but the content is not accessible.\n\n---\n\n### Summary of Contribution\n\nGSM-Plus fills a critical gap by being the first benchmark to apply a comprehensive, theoretically-grounded (Polya's principles) set of 8 perturbation types across all 1,319 GSM8K test questions, producing 10,552 adversarial variants. Its main finding -- that LLMs achieving 90%+ on GSM8K drop by up to 20% on perturbed versions while humans remain unaffected -- provides strong evidence that high benchmark scores mask shallow reasoning. The most damaging finding is that critical thinking (recognizing unsolvable problems) causes near-complete failure in open-source models, and that math-specific fine-tuning improves accuracy without meaningfully improving robustness."
      }
    ],
    "totalDurationMs": 257732,
    "totalTokens": 58295,
    "totalToolUseCount": 23,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16951,
      "cache_read_input_tokens": 37668,
      "output_tokens": 3673,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16951
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 3673,
          "cache_read_input_tokens": 37668,
          "cache_creation_input_tokens": 16951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16951,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "36dc2167-aa87-4707-b31e-1a8650ed55cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-29 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "77f20e96-d74b-4cca-8f27-848dbda86663",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on math reasoning robustness",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Tool result

_source line 28 · 2026-05-29T07:32:18.385Z_

<details><summary>↩ Tool result · `toolu_01S4PqtPDiU3auALy2NJY8vV`</summary>

````text
This is very relevant to the research. Now I have all the information needed for a comprehensive summary. Let me compile everything.

---

## Detailed Research Summary: rStar-Math (Guan et al., ICML 2025 Oral)

### 1. Problem Identified and How They Identified It

The authors identified three interrelated gaps:

**Gap A: Diminishing returns from data scaling.** Prior work on math reasoning for SLMs focused on scaling CoT training data, often distilled from frontier models (GPT-4, etc.). The authors observed that this approach was hitting a ceiling -- OpenMathInstruct-2 showed only a 3.9% improvement on MATH despite an 8x increase in dataset size. Simply generating more CoT data was insufficient.

**Gap B: Weak open-source test-time compute scaling.** While OpenAI's o1 demonstrated that test-time search (System 2 reasoning) dramatically improves performance, open-source methods for scaling test-time computation had shown "limited gains in math reasoning." The bottleneck was the lack of effective reward models to guide search.

**Gap C: The PRM training dilemma.** Process Reward Models (PRMs) offer dense step-level supervision, but training them requires precise step-level reward annotations. Human labeling is prohibitively expensive at scale. Automated approaches using MCTS Q-values as direct regression targets (what they call PQM -- Q-value-based Process Reward Models) suffer from inherent noise in Q-value estimates, degrading PRM quality. The authors articulated this precisely: "among a set of correct steps, it is difficult to rank them as best, second-best, or average and then assign precise scores. Similarly, among incorrect steps, differentiating the worst from moderately poor steps poses analogous challenges."

### 2. Key Insight Others Missed

The central insight was a **reframing from regression to ranking** for process reward model training. While prior work tried to estimate precise numerical reward scores for each reasoning step (and failed due to noise), the rStar-Math authors recognized that **Q-values from MCTS, while too noisy for precise scoring, are reliable enough to distinguish positive (correct) steps from negative (incorrect/irrelevant) steps.** This is a much weaker requirement that Q-values can actually satisfy.

This led them to train a **Process Preference Model (PPM)** using pairwise ranking loss (Bradley-Terry model) instead of MSE regression against Q-value targets. The PPM doesn't try to assign absolute scores -- it only learns which steps are better than others.

A second key insight was that the **policy model and reward model can co-evolve from scratch** without needing distillation from a superior model. By iterating between generating better data (via MCTS with improving reward models) and training better models on that data, both components bootstrap each other upward.

### 3. Problem Reformulation

Traditional approaches treated PRM training as a **regression problem**: given a reasoning step, predict its reward score (a precise scalar). rStar-Math reformulated this as a **preference learning problem**: given two reasoning steps in the same context, determine which one is better. This is fundamentally the same shift that RLHF made from absolute reward prediction to preference-based reward modeling, but applied specifically to process-level (step-level) supervision in math reasoning.

They also reformulated the data synthesis problem. Instead of treating CoT generation as a one-shot sampling problem (generate N solutions, keep the correct ones), they treated it as a **tree search problem** where MCTS systematically explores the space of reasoning trajectories, with code execution providing ground-truth verification at each step.

### 4. How MCTS + PRM Self-Evolution Works Technically

**MCTS Structure:**
- Root node = the math problem
- Each child node = one reasoning step (natural language CoT + Python code)
- At each step, the policy SLM generates n candidate next-steps (n=8 in early rounds, 16 in later rounds)
- Code execution filters invalid candidates -- only steps where Python executes successfully become valid nodes
- Node selection uses UCT (Upper Confidence Bound for Trees): `UCT(s) = Q(s) + c * sqrt(ln(N_parent) / N(s))` with c=2

**Value Estimation (two phases):**

*Terminal-guided (Rounds 1-2):* Q-values propagate backward from terminal nodes. Correct final answers score +1, incorrect score -1. Intermediate steps accumulate scores: `q(s_i)^k = q(s_i)^(k-1) + q(s_d)^k`. Steps that frequently contribute to correct solutions get high Q-values.

*PPM-augmented (Rounds 3-4):* The trained PPM provides initial Q-value estimates for non-terminal nodes: `q(s_i)^0 = PPM(x || s_1 || ... || s_i)`. These are then refined through terminal backpropagation. This dramatically improves search efficiency.

**The 4-Round Self-Evolution:**

- **Round 1 (Bootstrap):** Uses DeepSeek-Coder-V2-236B as the initial policy. 8 rollouts, 5 candidates/step. Terminal-guided Q-values only. Generates initial training data covering 60.17% of 747k problems. Trains first policy SLM (SLM-r1). PPM is not yet reliable.

- **Round 2:** Uses SLM-r1 as policy. 16 rollouts, 8 candidates/step. Still terminal-guided. Covers 66.60% of problems. Trains first reliable PPM (PPM-r2). This round is critical -- SLM-r2 already surpasses GPT-4o (76.6%) on MATH, reaching 86.6%.

- **Round 3:** Uses SLM-r2 + PPM-r2. PPM now integrated into MCTS for node evaluation. Significantly higher-quality trajectories covering more olympiad-level problems. Covers 77.86%. Produces SLM-r3 and PPM-r3.

- **Round 4:** Uses SLM-r3 + PPM-r3. Extended search for unsolved problems: 64 then 128 rollouts. 16 candidates/step. Multiple random seeds. Reaches 90.25% problem coverage (80.58% olympiad coverage).

**Training data selection:** For each problem, the top-2 trajectories ranked by average Q-value are selected for policy SLM fine-tuning via SFT.

### 5. Process Reward Model (PPM): Training Details

**This is the most relevant section for perturbation-robust PRM research.**

**How PPM Differs from Traditional PRMs:**
- **ORM** (Outcome Reward Model): scores entire solutions, not steps. Achieved 82.6% on MATH in ablation.
- **PRM** (Process Reward Model): scores each step, but requires expensive human annotations.
- **PQM** (Q-value PRM): uses MCTS Q-values as regression targets with MSE loss. Achieved 88.2% on MATH. Suffers from Q-value noise.
- **PPM** (Process Preference Model): uses MCTS Q-values only to construct preference pairs, trained with pairwise ranking loss. Achieved 89.4% on MATH.

**Preference Pair Construction:**
For each intermediate step in the MCTS tree:
1. Select the 2 candidates with highest Q-values as **positive** steps (must lead to correct final answers)
2. Select the 2 candidates with lowest Q-values as **negative** steps (must lead to incorrect final answers)
3. Critical constraint for intermediate steps: positive and negative pairs share identical preceding context (same parent path in the tree), isolating the quality of that single step
4. For final-answer steps: this constraint relaxes since identical reasoning rarely produces different final outputs; instead, 2 correct-answer trajectories vs. 2 wrong-answer trajectories are used

**Loss Function:**
Bradley-Terry pairwise ranking loss:
```
L_ppm(theta) = -1/4 * E[sum over pairs of log(sigma(r_theta(x, y_pos) - r_theta(x, y_neg)))]
```
Where `r_theta` is the PPM's scalar output, constrained to [-1, 1] via tanh activation.

**Why This Matters:** The preference-based formulation is inherently more robust to noisy Q-values because it only requires the Q-values to get the **ordering** right (positive > negative), not the precise magnitudes. This is directly relevant to perturbation-robust PRMs -- the PPM is already somewhat robust to noise in its training signal by design.

### 6. Existing Techniques Adapted/Combined/Simplified

rStar-Math is a synthesis of several existing ideas:
- **MCTS for LLM reasoning** (from AlphaGo-style search adapted to language): The tree search structure builds on prior work applying MCTS to math reasoning
- **Code-augmented verification**: Requiring executable Python at each step is adapted from code-generation verification methods, but applied here to filter CoT reasoning steps
- **Bradley-Terry preference learning**: Well-established in RLHF (e.g., InstructGPT, DPO), but applied here to process-level rewards rather than outcome-level
- **Self-play / self-improvement**: The iterative co-evolution of policy and reward model echoes ideas from AlphaZero's self-play and Expert Iteration
- **Process reward models**: Building on MathShepherd, PRM800K, and others, but with the novel PPM training formulation

The simplification is primarily in how PRM training data is obtained: instead of requiring human annotations or precise automated scores, they need only binary correctness labels at the trajectory level (does the solution reach the right answer?), which is cheap to obtain via code execution.

### 7. Main Limitations

**Acknowledged by Authors:**
- **No visual reasoning**: 8 of the unsolved AIME problems required geometric/visual understanding, which rStar-Math cannot handle
- **Data quality**: Of 747k problems, ~10% remain unsolved; manual review of 20 unsolved problems found 19 had incorrectly labeled answers
- **Massive compute**: Bootstrap round required 10 nodes of 8x80GB H100 GPUs for ~2 weeks; subsequent rounds used 15 nodes of 4x40GB A100 GPUs for 3-7 days each
- **Inference cost**: Average tokens per trajectory range from 3,299 (GSM8K) to 15,693 (AIME), with multiple trajectories needed for best-of-N selection (8-64 trajectories at test time)
- **Domain-specific**: Only demonstrated on math; generalization to code, science, or other reasoning tasks remains speculative
- **Bootstrap dependency**: Round 1 requires a strong initial model (DeepSeek-Coder-V2-236B), and the relationship between bootstrap model quality and final performance is not thoroughly analyzed

**Identified by External Analysis:**
- **Potential data contamination**: Training uses NuminaMath, which may overlap with OlympiadBench and Omni-Math evaluation sets. The paper uses MATH training split and AMC-AIME training split as GPT-4 synthesis seeds, creating potential overlap
- **Incomplete mechanistic understanding**: Whether observed "self-reflection" capabilities are genuine emergent behavior or methodology artifacts is unclear
- **Limited ablation of MCTS hyperparameters**: Sensitivity to rollout count, candidate count, UCB exploration constant, etc. is not fully explored
- **PPM convergence dynamics unclear**: Whether PPM improvements drive policy gains or vice versa is confounded -- the causal direction of improvement is not disentangled

### 8. Reviewer Comments

**ICML 2025 peer reviews are not publicly accessible** on OpenReview as of the time of this research (the API returns empty results, and the forum page only shows metadata). The paper received an **oral presentation** designation, indicating it was in the top tier of accepted papers.

**AI-generated review analysis (from HF Daily Paper Reviews) identified:**

*Praised:*
- Novel PPM training formulation avoiding expensive step-level annotations
- Code-augmented CoT providing rigorous verification at each reasoning step
- Impressive quantitative results, especially the 90% MATH score from a 7B model
- Scalable self-evolution recipe demonstrating consistent improvements across rounds
- Demonstration that SLMs can compete with frontier models without distillation

*Criticized:*
- Narrow evaluation domain (math only)
- Heavy computational requirements limiting reproducibility
- Bootstrap dependency on a 236B parameter model in Round 1
- No comparison against simpler sampling strategies during training
- Limited error attribution analysis for remaining failures

### 9. Key Quantitative Results

| Benchmark | rStar-Math (Qwen-7B) | o1-preview | o1-mini | GPT-4o |
|---|---|---|---|---|
| MATH-500 | **90.0%** (from 58.8% base) | 85.5% | 90.0% | 76.6% |
| AIME 2024 | **53.3%** (8/15 problems) | 44.6% | 56.7% | 9.3% |
| AMC 2023 | 87.5% | - | 95.0% | - |
| Olympiad Bench | **65.6%** | - | 65.3% | - |
| College Math | **60.5%** | - | 57.8% | - |
| GaoKao En 2023 | **81.3%** | - | 78.4% | - |
| GSM8K | **95.2%** | - | 94.8% | - |

**Cross-model results (64 trajectories):**
- Qwen2.5-Math-7B: 90.0% MATH, 53.3% AIME
- Qwen2.5-Math-1.5B: 88.6% MATH, 46.7% AIME
- Phi3-mini-3.8B: 86.4% MATH, 43.3% AIME
- Qwen2-Math-7B: 88.6% MATH, 46.7% AIME

**Ablation highlights:**
- PPM (89.4% MATH) > PQM (88.2%) > ORM (82.6%), validating the preference-based approach
- Step-verified trajectories (78.4% SFT) >> rejection sampling (73.4%) >> random sampling (72.4%)
- "Once the policy model attains a reasonably strong capability level, the PPM becomes the key determinant of the upper performance limit" -- this is a critical finding, showing PRM quality is the bottleneck

### Relevance to Perturbation-Robust PRM Research

Several aspects of rStar-Math are directly relevant:

1. **The PPM's inherent robustness to label noise**: By using ranking loss instead of regression, the PPM only needs Q-values to correctly order positive vs. negative steps, not to provide precise scores. This provides built-in robustness to perturbations in training signal quality.

2. **The preference pair construction is a vulnerability**: The method selects top-2 and bottom-2 Q-value candidates as positive/negative pairs. If adversarial perturbations could make incorrect steps have high Q-values (or correct steps have low Q-values), this could corrupt PPM training data. The recent "Adversarial Training for Process Reward Models" paper (arxiv 2511.22888) addresses exactly this vulnerability.

3. **Code execution as verification provides a strong but brittle signal**: Code that executes successfully is not necessarily semantically correct -- it could produce the right numerical answer through flawed reasoning. This is a potential attack surface for perturbation-based adversarial analysis.

4. **The finding that PPM is the performance bottleneck** means that improving PRM robustness (e.g., through adversarial training or perturbation-robustness techniques) could directly translate to improved end-to-end math reasoning performance.

Sources:
- [rStar-Math on arXiv](https://arxiv.org/abs/2501.04519)
- [rStar-Math full paper (HTML)](https://arxiv.org/html/2501.04519)
- [OpenReview forum](https://openreview.net/forum?id=5zwF1GizFa)
- [Microsoft Research blog](https://www.microsoft.com/en-us/research/blog/new-methods-boost-reasoning-in-small-and-large-language-models/)
- [AI Paper Reviewer analysis](https://deep-diver.github.io/ai-paper-reviewer/paper-reviews/2501.04519/)
- [AI Papers Academy analysis](https://aipapersacademy.com/rstar-math/)
- [Lambda Class summary](https://blog.lambdaclass.com/summary-on-rstar-math-showing-how-smaller-llms-can-outperform-bigger-ones-with-deep-thinking/)
- [Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)
- [GitHub repository](https://github.com/microsoft/rStar)

agentId: aa0673e080b1e58bc (use SendMessage with to: 'aa0673e080b1e58bc' to continue this agent)
&lt;usage>total_tokens: 30984
tool_uses: 20
duration_ms: 270570&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "53949194-84d1-47aa-bf72-21a0b46c8387",
  "isSidechain": false,
  "promptId": "e2027b0c-9c37-4d02-abda-83dbebeded5e",
  "type": "user",
  "uuid": "92bfb809-c9ff-498e-9e6f-6d62ba706ebb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are researching the paper \"rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking\" by Guan et al. (ICML 2025 Oral), available at https://arxiv.org/abs/2501.04519.\n\nYour task:\n1. Use WebFetch to read the paper's abstract and introduction from the arxiv page.\n2. Search for OpenReview reviews or ICML 2025 reviews for rStar-Math.\n3. Search for any blog posts or detailed method descriptions (Microsoft Research).\n\nFor your final response, provide a detailed summary covering:\n- What gap/problem did they identify and HOW?\n- What was the key insight others missed?\n- How did they formulate the problem differently?\n- How does the MCTS + PRM self-evolution work technically?\n- What role does the Process Reward Model play and how is it trained?\n- What existing technique did they adapt/combine/simplify?\n- What are the main limitations?\n- If reviewer comments found: what was praised, what was criticized?\n- Key quantitative results (especially the 90% MATH claim, model sizes, comparison to o1)\n\nBe thorough and specific — include numbers, method details, and concrete findings. Focus especially on how the PRM is trained and evolved, as this is relevant to our research on perturbation-robust PRMs.",
    "agentId": "aa0673e080b1e58bc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "This is very relevant to the research. Now I have all the information needed for a comprehensive summary. Let me compile everything.\n\n---\n\n## Detailed Research Summary: rStar-Math (Guan et al., ICML 2025 Oral)\n\n### 1. Problem Identified and How They Identified It\n\nThe authors identified three interrelated gaps:\n\n**Gap A: Diminishing returns from data scaling.** Prior work on math reasoning for SLMs focused on scaling CoT training data, often distilled from frontier models (GPT-4, etc.). The authors observed that this approach was hitting a ceiling -- OpenMathInstruct-2 showed only a 3.9% improvement on MATH despite an 8x increase in dataset size. Simply generating more CoT data was insufficient.\n\n**Gap B: Weak open-source test-time compute scaling.** While OpenAI's o1 demonstrated that test-time search (System 2 reasoning) dramatically improves performance, open-source methods for scaling test-time computation had shown \"limited gains in math reasoning.\" The bottleneck was the lack of effective reward models to guide search.\n\n**Gap C: The PRM training dilemma.** Process Reward Models (PRMs) offer dense step-level supervision, but training them requires precise step-level reward annotations. Human labeling is prohibitively expensive at scale. Automated approaches using MCTS Q-values as direct regression targets (what they call PQM -- Q-value-based Process Reward Models) suffer from inherent noise in Q-value estimates, degrading PRM quality. The authors articulated this precisely: \"among a set of correct steps, it is difficult to rank them as best, second-best, or average and then assign precise scores. Similarly, among incorrect steps, differentiating the worst from moderately poor steps poses analogous challenges.\"\n\n### 2. Key Insight Others Missed\n\nThe central insight was a **reframing from regression to ranking** for process reward model training. While prior work tried to estimate precise numerical reward scores for each reasoning step (and failed due to noise), the rStar-Math authors recognized that **Q-values from MCTS, while too noisy for precise scoring, are reliable enough to distinguish positive (correct) steps from negative (incorrect/irrelevant) steps.** This is a much weaker requirement that Q-values can actually satisfy.\n\nThis led them to train a **Process Preference Model (PPM)** using pairwise ranking loss (Bradley-Terry model) instead of MSE regression against Q-value targets. The PPM doesn't try to assign absolute scores -- it only learns which steps are better than others.\n\nA second key insight was that the **policy model and reward model can co-evolve from scratch** without needing distillation from a superior model. By iterating between generating better data (via MCTS with improving reward models) and training better models on that data, both components bootstrap each other upward.\n\n### 3. Problem Reformulation\n\nTraditional approaches treated PRM training as a **regression problem**: given a reasoning step, predict its reward score (a precise scalar). rStar-Math reformulated this as a **preference learning problem**: given two reasoning steps in the same context, determine which one is better. This is fundamentally the same shift that RLHF made from absolute reward prediction to preference-based reward modeling, but applied specifically to process-level (step-level) supervision in math reasoning.\n\nThey also reformulated the data synthesis problem. Instead of treating CoT generation as a one-shot sampling problem (generate N solutions, keep the correct ones), they treated it as a **tree search problem** where MCTS systematically explores the space of reasoning trajectories, with code execution providing ground-truth verification at each step.\n\n### 4. How MCTS + PRM Self-Evolution Works Technically\n\n**MCTS Structure:**\n- Root node = the math problem\n- Each child node = one reasoning step (natural language CoT + Python code)\n- At each step, the policy SLM generates n candidate next-steps (n=8 in early rounds, 16 in later rounds)\n- Code execution filters invalid candidates -- only steps where Python executes successfully become valid nodes\n- Node selection uses UCT (Upper Confidence Bound for Trees): `UCT(s) = Q(s) + c * sqrt(ln(N_parent) / N(s))` with c=2\n\n**Value Estimation (two phases):**\n\n*Terminal-guided (Rounds 1-2):* Q-values propagate backward from terminal nodes. Correct final answers score +1, incorrect score -1. Intermediate steps accumulate scores: `q(s_i)^k = q(s_i)^(k-1) + q(s_d)^k`. Steps that frequently contribute to correct solutions get high Q-values.\n\n*PPM-augmented (Rounds 3-4):* The trained PPM provides initial Q-value estimates for non-terminal nodes: `q(s_i)^0 = PPM(x || s_1 || ... || s_i)`. These are then refined through terminal backpropagation. This dramatically improves search efficiency.\n\n**The 4-Round Self-Evolution:**\n\n- **Round 1 (Bootstrap):** Uses DeepSeek-Coder-V2-236B as the initial policy. 8 rollouts, 5 candidates/step. Terminal-guided Q-values only. Generates initial training data covering 60.17% of 747k problems. Trains first policy SLM (SLM-r1). PPM is not yet reliable.\n\n- **Round 2:** Uses SLM-r1 as policy. 16 rollouts, 8 candidates/step. Still terminal-guided. Covers 66.60% of problems. Trains first reliable PPM (PPM-r2). This round is critical -- SLM-r2 already surpasses GPT-4o (76.6%) on MATH, reaching 86.6%.\n\n- **Round 3:** Uses SLM-r2 + PPM-r2. PPM now integrated into MCTS for node evaluation. Significantly higher-quality trajectories covering more olympiad-level problems. Covers 77.86%. Produces SLM-r3 and PPM-r3.\n\n- **Round 4:** Uses SLM-r3 + PPM-r3. Extended search for unsolved problems: 64 then 128 rollouts. 16 candidates/step. Multiple random seeds. Reaches 90.25% problem coverage (80.58% olympiad coverage).\n\n**Training data selection:** For each problem, the top-2 trajectories ranked by average Q-value are selected for policy SLM fine-tuning via SFT.\n\n### 5. Process Reward Model (PPM): Training Details\n\n**This is the most relevant section for perturbation-robust PRM research.**\n\n**How PPM Differs from Traditional PRMs:**\n- **ORM** (Outcome Reward Model): scores entire solutions, not steps. Achieved 82.6% on MATH in ablation.\n- **PRM** (Process Reward Model): scores each step, but requires expensive human annotations.\n- **PQM** (Q-value PRM): uses MCTS Q-values as regression targets with MSE loss. Achieved 88.2% on MATH. Suffers from Q-value noise.\n- **PPM** (Process Preference Model): uses MCTS Q-values only to construct preference pairs, trained with pairwise ranking loss. Achieved 89.4% on MATH.\n\n**Preference Pair Construction:**\nFor each intermediate step in the MCTS tree:\n1. Select the 2 candidates with highest Q-values as **positive** steps (must lead to correct final answers)\n2. Select the 2 candidates with lowest Q-values as **negative** steps (must lead to incorrect final answers)\n3. Critical constraint for intermediate steps: positive and negative pairs share identical preceding context (same parent path in the tree), isolating the quality of that single step\n4. For final-answer steps: this constraint relaxes since identical reasoning rarely produces different final outputs; instead, 2 correct-answer trajectories vs. 2 wrong-answer trajectories are used\n\n**Loss Function:**\nBradley-Terry pairwise ranking loss:\n```\nL_ppm(theta) = -1/4 * E[sum over pairs of log(sigma(r_theta(x, y_pos) - r_theta(x, y_neg)))]\n```\nWhere `r_theta` is the PPM's scalar output, constrained to [-1, 1] via tanh activation.\n\n**Why This Matters:** The preference-based formulation is inherently more robust to noisy Q-values because it only requires the Q-values to get the **ordering** right (positive > negative), not the precise magnitudes. This is directly relevant to perturbation-robust PRMs -- the PPM is already somewhat robust to noise in its training signal by design.\n\n### 6. Existing Techniques Adapted/Combined/Simplified\n\nrStar-Math is a synthesis of several existing ideas:\n- **MCTS for LLM reasoning** (from AlphaGo-style search adapted to language): The tree search structure builds on prior work applying MCTS to math reasoning\n- **Code-augmented verification**: Requiring executable Python at each step is adapted from code-generation verification methods, but applied here to filter CoT reasoning steps\n- **Bradley-Terry preference learning**: Well-established in RLHF (e.g., InstructGPT, DPO), but applied here to process-level rewards rather than outcome-level\n- **Self-play / self-improvement**: The iterative co-evolution of policy and reward model echoes ideas from AlphaZero's self-play and Expert Iteration\n- **Process reward models**: Building on MathShepherd, PRM800K, and others, but with the novel PPM training formulation\n\nThe simplification is primarily in how PRM training data is obtained: instead of requiring human annotations or precise automated scores, they need only binary correctness labels at the trajectory level (does the solution reach the right answer?), which is cheap to obtain via code execution.\n\n### 7. Main Limitations\n\n**Acknowledged by Authors:**\n- **No visual reasoning**: 8 of the unsolved AIME problems required geometric/visual understanding, which rStar-Math cannot handle\n- **Data quality**: Of 747k problems, ~10% remain unsolved; manual review of 20 unsolved problems found 19 had incorrectly labeled answers\n- **Massive compute**: Bootstrap round required 10 nodes of 8x80GB H100 GPUs for ~2 weeks; subsequent rounds used 15 nodes of 4x40GB A100 GPUs for 3-7 days each\n- **Inference cost**: Average tokens per trajectory range from 3,299 (GSM8K) to 15,693 (AIME), with multiple trajectories needed for best-of-N selection (8-64 trajectories at test time)\n- **Domain-specific**: Only demonstrated on math; generalization to code, science, or other reasoning tasks remains speculative\n- **Bootstrap dependency**: Round 1 requires a strong initial model (DeepSeek-Coder-V2-236B), and the relationship between bootstrap model quality and final performance is not thoroughly analyzed\n\n**Identified by External Analysis:**\n- **Potential data contamination**: Training uses NuminaMath, which may overlap with OlympiadBench and Omni-Math evaluation sets. The paper uses MATH training split and AMC-AIME training split as GPT-4 synthesis seeds, creating potential overlap\n- **Incomplete mechanistic understanding**: Whether observed \"self-reflection\" capabilities are genuine emergent behavior or methodology artifacts is unclear\n- **Limited ablation of MCTS hyperparameters**: Sensitivity to rollout count, candidate count, UCB exploration constant, etc. is not fully explored\n- **PPM convergence dynamics unclear**: Whether PPM improvements drive policy gains or vice versa is confounded -- the causal direction of improvement is not disentangled\n\n### 8. Reviewer Comments\n\n**ICML 2025 peer reviews are not publicly accessible** on OpenReview as of the time of this research (the API returns empty results, and the forum page only shows metadata). The paper received an **oral presentation** designation, indicating it was in the top tier of accepted papers.\n\n**AI-generated review analysis (from HF Daily Paper Reviews) identified:**\n\n*Praised:*\n- Novel PPM training formulation avoiding expensive step-level annotations\n- Code-augmented CoT providing rigorous verification at each reasoning step\n- Impressive quantitative results, especially the 90% MATH score from a 7B model\n- Scalable self-evolution recipe demonstrating consistent improvements across rounds\n- Demonstration that SLMs can compete with frontier models without distillation\n\n*Criticized:*\n- Narrow evaluation domain (math only)\n- Heavy computational requirements limiting reproducibility\n- Bootstrap dependency on a 236B parameter model in Round 1\n- No comparison against simpler sampling strategies during training\n- Limited error attribution analysis for remaining failures\n\n### 9. Key Quantitative Results\n\n| Benchmark | rStar-Math (Qwen-7B) | o1-preview | o1-mini | GPT-4o |\n|---|---|---|---|---|\n| MATH-500 | **90.0%** (from 58.8% base) | 85.5% | 90.0% | 76.6% |\n| AIME 2024 | **53.3%** (8/15 problems) | 44.6% | 56.7% | 9.3% |\n| AMC 2023 | 87.5% | - | 95.0% | - |\n| Olympiad Bench | **65.6%** | - | 65.3% | - |\n| College Math | **60.5%** | - | 57.8% | - |\n| GaoKao En 2023 | **81.3%** | - | 78.4% | - |\n| GSM8K | **95.2%** | - | 94.8% | - |\n\n**Cross-model results (64 trajectories):**\n- Qwen2.5-Math-7B: 90.0% MATH, 53.3% AIME\n- Qwen2.5-Math-1.5B: 88.6% MATH, 46.7% AIME\n- Phi3-mini-3.8B: 86.4% MATH, 43.3% AIME\n- Qwen2-Math-7B: 88.6% MATH, 46.7% AIME\n\n**Ablation highlights:**\n- PPM (89.4% MATH) > PQM (88.2%) > ORM (82.6%), validating the preference-based approach\n- Step-verified trajectories (78.4% SFT) >> rejection sampling (73.4%) >> random sampling (72.4%)\n- \"Once the policy model attains a reasonably strong capability level, the PPM becomes the key determinant of the upper performance limit\" -- this is a critical finding, showing PRM quality is the bottleneck\n\n### Relevance to Perturbation-Robust PRM Research\n\nSeveral aspects of rStar-Math are directly relevant:\n\n1. **The PPM's inherent robustness to label noise**: By using ranking loss instead of regression, the PPM only needs Q-values to correctly order positive vs. negative steps, not to provide precise scores. This provides built-in robustness to perturbations in training signal quality.\n\n2. **The preference pair construction is a vulnerability**: The method selects top-2 and bottom-2 Q-value candidates as positive/negative pairs. If adversarial perturbations could make incorrect steps have high Q-values (or correct steps have low Q-values), this could corrupt PPM training data. The recent \"Adversarial Training for Process Reward Models\" paper (arxiv 2511.22888) addresses exactly this vulnerability.\n\n3. **Code execution as verification provides a strong but brittle signal**: Code that executes successfully is not necessarily semantically correct -- it could produce the right numerical answer through flawed reasoning. This is a potential attack surface for perturbation-based adversarial analysis.\n\n4. **The finding that PPM is the performance bottleneck** means that improving PRM robustness (e.g., through adversarial training or perturbation-robustness techniques) could directly translate to improved end-to-end math reasoning performance.\n\nSources:\n- [rStar-Math on arXiv](https://arxiv.org/abs/2501.04519)\n- [rStar-Math full paper (HTML)](https://arxiv.org/html/2501.04519)\n- [OpenReview forum](https://openreview.net/forum?id=5zwF1GizFa)\n- [Microsoft Research blog](https://www.microsoft.com/en-us/research/blog/new-methods-boost-reasoning-in-small-and-large-language-models/)\n- [AI Paper Reviewer analysis](https://deep-diver.github.io/ai-paper-reviewer/paper-reviews/2501.04519/)\n- [AI Papers Academy analysis](https://aipapersacademy.com/rstar-math/)\n- [Lambda Class summary](https://blog.lambdaclass.com/summary-on-rstar-math-showing-how-smaller-llms-can-outperform-bigger-ones-with-deep-thinking/)\n- [Adversarial Training for PRMs](https://arxiv.org/abs/2511.22888)\n- [GitHub repository](https://github.com/microsoft/rStar)"
      }
    ],
    "totalDurationMs": 270570,
    "totalTokens": 30984,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 469,
      "cache_read_input_tokens": 26393,
      "output_tokens": 4121,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 469
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4121,
          "cache_read_input_tokens": 26393,
          "cache_creation_input_tokens": 469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 469,
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
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "53949194-84d1-47aa-bf72-21a0b46c8387",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-29 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "92bfb809-c9ff-498e-9e6f-6d62ba706ebb",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on math reasoning robustness",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Assistant

_source line 31 · 2026-05-29T07:32:22.620Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive research on all 5 papers. Let me synthesize this into the required JSON format, keeping each analysis under 2000 characters. Let me compose the final output carefully.

Let me count characters for each entry to ensure compliance with the 2000-character limit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92bfb809-c9ff-498e-9e6f-6d62ba706ebb",
  "isSidechain": false,
  "requestId": "req_011CbWUGAPiHdUyGQijrNqWD",
  "type": "assistant",
  "uuid": "5981aaa8-8bbe-4dc9-8a94-5246f6993e3e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wv9Zy1LSeAysodBxuLUBNN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3020,
      "cache_creation_input_tokens": 16263,
      "cache_read_input_tokens": 16307,
      "output_tokens": 2748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16263,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3020,
          "output_tokens": 2748,
          "cache_read_input_tokens": 16307,
          "cache_creation_input_tokens": 16263,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16263
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

_source line 32 · 2026-05-29T07:33:31.705Z_

Now I have comprehensive research on all 5 papers. Let me compose the final JSON analysis, ensuring each entry stays under 2000 characters.

```json
[
  {
    "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
    "venue": "ICLR 2025",
    "problem_identification": "Identified that GSM8K's fixed test set provides no variance signal and is contamination-prone, by converting 100 questions into symbolic templates with 50 instantiations each and measuring distributional performance — revealing that 21/25 models score >1σ above their GSM-Symbolic mean on original GSM8K.",
    "key_insight": "Genuine reasoning must be invariant to mathematically irrelevant surface changes; the GSM-NoOp experiment (adding a single irrelevant clause) exposed catastrophic pattern-matching failures (up to 65% drops) that in-context examples cannot recover, proving models integrate surface cues rather than parsing problem structure.",
    "innovation_type": "new_benchmark",
    "method_summary": "Creates symbolic templates from GSM8K with parameterized names, numbers, and objects, generating 50 instantiations per template. Introduces controlled difficulty variants (GSM-M1 through GSM-P2, adding/removing reasoning clauses) and GSM-NoOp (irrelevant-but-plausible distractors). Evaluates 25+ models using 8-shot CoT with greedy decoding, reporting distributional statistics rather than point estimates.",
    "limitations_and_open_questions": "Statistical critique (Ivanova) showed only 4/25 models exhibit statistically significant drops under proper Wilson intervals; frontier models (o1-preview: 15.3% NoOp drop vs. Phi-3-mini: 62.7%) are far more resilient, undermining universal claims. How do distribution shifts in numerical ranges confound the reasoning-failure narrative?",
    "building_blocks": ["GSM-Symbolic templates", "GSM-NoOp distractor design", "Distributional evaluation methodology", "Controlled difficulty scaling (M1/P1/P2)"],
    "relevance_to_seed": "Foundational motivation for MACR — establishes the surface-form fragility problem that consistency regularization targets, and provides one of our evaluation benchmarks."
  },
  {
    "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers",
    "venue": "ACL 2024",
    "problem_identification": "Found that prior robustness benchmarks each tested only one perturbation type (SVAMP: paraphrasing; GSM-IC: distractors), giving an incomplete robustness picture. Surveyed existing datasets (Table 1) and demonstrated that solving a GSM8K question does not imply solving its trivially modified variant — GPT-3.5-Turbo fails when 'leave' becomes 'return.'",
    "key_insight": "Robustness requires simultaneous testing across qualitatively different reasoning capabilities grounded in Polya's problem-solving stages; critically, math-specific SFT improves accuracy but NOT robustness (SFT PDR ≈ foundation PDR), meaning the training paradigm itself is insufficient.",
    "innovation_type": "new_benchmark",
    "method_summary": "Designs 8 perturbation types from 5 perspectives mapped to Polya's principles: numerical (substitution, digit expansion, IDF conversion), arithmetic (adding/reversing operations), problem understanding (rephrasing), distractor insertion, and critical thinking (removing essential info). GPT-4 generates 10,552 variants from 1,319 GSM8K questions with 18.85% human correction. Tests 25 LLMs across 4 prompting methods.",
    "limitations_and_open_questions": "Limited to grade-school math — no competition-level evaluation. No analysis of intermediate reasoning step correctness or root-cause failure mechanisms. Does the proposed Compositional Prompting (COMP) method scale beyond GPT-3.5-Turbo, and can it close the human-LLM robustness gap?",
    "building_blocks": ["8-type perturbation taxonomy", "PDR/ASP robustness metrics", "Polya-grounded evaluation framework", "Compositional Prompting (COMP)"],
    "relevance_to_seed": "Provides our perturbation taxonomy and one evaluation benchmark (GSM-Plus); the finding that SFT doesn't fix robustness directly motivates training-time interventions like MACR."
  },
  {
    "title": "CREAM: Consistency Regularized Self-Rewarding Language Models",
    "venue": "ICLR 2025",
    "problem_identification": "Observed that 7B self-rewarding LMs degrade after 2-3 iterations (Llama-2 7B: ARC-Easy drops 60.44%→46.55%) due to compounding errors in self-generated preference labels — each iteration's reward inaccuracies snowball into corrupted training data.",
    "key_insight": "Cross-iteration reward consistency (measured via Kendall's Tau between current and previous model rankings) provides a lightweight, principled signal for preference data reliability — disagreement between iterations indicates unreliable labels that should be downweighted.",
    "innovation_type": "new_technique",
    "method_summary": "Computes global consistency rate C via Kendall's Tau between rankings from consecutive model checkpoints. Proves (Theorem 3.3) this is equivalent to soft-labeled DPO: L = C·L_DPO(chosen,rejected) + (1-C)·L_DPO(rejected,chosen), effectively label-smoothing for preferences. Lemma 3.4 links empirical Tau to the regularization parameter. Only requires two checkpoints — no ensembles.",
    "limitations_and_open_questions": "Limited to 7B-13B scale; ranking accuracy tops ~70% (acknowledged as unsatisfying). Requires at least SFT-level alignment to bootstrap. Does the consistency principle transfer to RL training objectives beyond DPO, and to domain-specific (e.g., math) rather than general preference alignment?",
    "building_blocks": ["Cross-iteration consistency as regularization signal", "Soft-labeled DPO formulation", "Kendall's Tau as dynamic regularization strength", "Reversed-DPO loss component"],
    "relevance_to_seed": "Validates consistency regularization within iterative LLM training (RL-adjacent); the cross-iteration consistency principle parallels MACR's cross-perturbation consistency — both use agreement signals to stabilize training."
  },
  {
    "title": "rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking",
    "venue": "ICML 2025 (Oral)",
    "problem_identification": "Identified three bottlenecks: diminishing returns from CoT data scaling (OpenMathInstruct-2: 8× data → only 3.9% gain), weak open-source test-time compute scaling due to poor reward models, and the PRM training dilemma — MCTS Q-values are too noisy for regression-based PRM training but human step-level annotations are prohibitively expensive.",
    "key_insight": "Reframing process reward model training from regression (predict precise Q-values) to preference ranking (which step is better?) dramatically improves PRM quality because Q-values, while too noisy for absolute scoring, reliably distinguish positive from negative steps — a much weaker requirement.",
    "innovation_type": "combination",
    "method_summary": "Introduces Process Preference Model (PPM) trained with Bradley-Terry pairwise loss on MCTS-derived preference pairs (top-2 vs. bottom-2 Q-value candidates sharing identical context). Runs 4-round self-evolution: MCTS generates code-augmented CoT trajectories, PPM trains on resulting preferences, improved PPM guides next-round MCTS. Code execution provides step-level verification. Achieves 90% MATH with Qwen-7B.",
    "limitations_and_open_questions": "Massive compute (10 nodes × 8 H100s for weeks); Round 1 bootstraps from 236B-parameter model. PPM robustness to adversarial perturbations is untested — if surface-form changes corrupt Q-value orderings, the preference pair construction breaks. Does PPM quality degrade under distribution shift?",
    "building_blocks": ["Process Preference Model (PPM) with Bradley-Terry loss", "MCTS-guided CoT trajectory generation", "Code-augmented step verification", "4-round policy-PRM co-evolution"],
    "relevance_to_seed": "Demonstrates PRM is the performance bottleneck in RL-for-math, directly motivating MACR's perturbation-robust PRM extension; PPM's preference-based formulation suggests a natural integration point for consistency-based robustness."
  },
  {
    "title": "Robust Reasoning Benchmark",
    "venue": "arXiv 2026",
    "problem_identification": "Observed that prior adversarial benchmarks (GSM-Symbolic, GSM-Plus) conflate reasoning failures with arithmetic failures by changing numerical values. Identified that it was unknown whether competition-math (AIME) performance reflects robust reasoning or fragile pattern-matching on standard formatting.",
    "key_insight": "You can isolate pure structural fragility without touching mathematical content — 13 deterministic, reversible textual transformations preserve exact mathematical state while exposing that LLM reasoning is overfit to standard presentation, with failures attributable to tokenization breakdown and attention dilution rather than mathematical incompetence.",
    "innovation_type": "new_benchmark",
    "method_summary": "Applies 13 perturbations across 4 categories to AIME 2024/2025: semantic substitutions (double negation, antonyms, wrappers), contextual overload (line/word/symbol interleaving), syntactic distortions (sentence/word/symbol reversal), and visual encodings (Rail Fence cipher, rectangle perimeter, snake patterns). All transformations are algorithmically invertible with explicit decoding protocols provided in prompts. Separately studies Intra-Query Attention Dilution via sequential problem contexts.",
    "limitations_and_open_questions": "AIME-only domain; proprietary models tested less comprehensively. Claude's failures stem from safety-filter refusals, not reasoning — raising questions about confounding. The concept of 'atomic reasoning unit' (maximum computation before structural noise degrades logic) is proposed but not formally quantified.",
    "building_blocks": ["13 deterministic reversible perturbation types", "Failure mode taxonomy (cognitive thrashing, tokenization breakdown)", "IQAD attention dilution analysis", "Competition-math robustness evaluation"],
    "relevance_to_seed": "Validates MACR's focus on competition-level math robustness; finding that open-weights models drop ~47-54% on AIME under surface-only changes confirms the problem persists at competition level and is not limited to GSM-level math."
  }
]
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5981aaa8-8bbe-4dc9-8a94-5246f6993e3e",
  "isSidechain": false,
  "requestId": "req_011CbWUGAPiHdUyGQijrNqWD",
  "type": "assistant",
  "uuid": "5632451a-83da-4027-bdeb-f7a746d3abe3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wv9Zy1LSeAysodBxuLUBNN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3020,
      "cache_creation_input_tokens": 16263,
      "cache_read_input_tokens": 16307,
      "output_tokens": 2748,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16263,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3020,
          "output_tokens": 2748,
          "cache_read_input_tokens": 16307,
          "cache_creation_input_tokens": 16263,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16263
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML researcher performing deep analysis of multiple published papers.  **Today's date: 2026-05-29 (UTC).**  ## Research context  We are generating ideas in the area of: **Target: AAAI…",
  "leafUuid": "5632451a-83da-4027-bdeb-f7a746d3abe3",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Analyze ML papers on math reasoning robustness",
  "sessionId": "323cdf93-5570-4239-99e8-4d2f25f379e5"
}
```

---
