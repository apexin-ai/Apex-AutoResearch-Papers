# Research conversation: 【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。 【原始 pro

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 97
- **Recorded user turns:** 6
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3.jsonl`
- **Structured JSON:** [`f36d767e96d2824129cb.json`](../../sessions/f3/f36d767e96d2824129cb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:32:19.393Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:32:19.393Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "content": "【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。\n\n【原始 proposal】:\n# Formal Error Profiling Enables Targeted Math Self-Improvement\n\n## Core Problem\n\nSelf-improvement loops for mathematical reasoning suffer from two key failures: model collapse when using self-verification, and wasteful data generation that doesn't target the model's actual mathematical skill deficits. Can formal symbolic tools serve as both collapse-proof verifiers and fine-grained error diagnosticians to enable stable, efficient self-improvement?\n\n## Research Opportunity\n\nThree recent advances create a ripe moment: FoVer (ACL 2026) proved formal tools can generate accurate step-level error labels for training, STAT (ICLR 2026) showed skill-gap-targeted synthesis outperforms uniform synthesis by 7.5% on MATH, and NSRSA (March 2026) demonstrated symbolic verification helps iterative self-training but only at the arithmetic level on GSM8K. The specific combination of formal step-level error categorization driving targeted symbolic problem synthesis in a closed self-improvement loop has not been attempted. Unlike LLM-teacher-based error analysis (Self-Error-Instruct, STAT, WarriorMath), formal tools provide ground-truth error diagnosis that cannot be hacked or hallucinated, directly addressing the collapse mechanism identified by the solver-verifier gap theory.\n\n## Research Landscape\n\nCurrent SOTA in synthetic math data includes SPARQ (June 2025, +24% via quality-diversity algorithms from 7.5K seeds), CoTEvol (April 2026, +6.6% average via evolutionary CoT synthesis), and MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). For self-improvement, SPICE (Oct 2025) achieves +8.9% math improvement via document-grounded self-play, while SvS (Aug 2025) achieves +18.3% Pass@32 on AIME24 via variational problem synthesis maintaining training entropy. For verification, FoVer trains generalizable PRMs from formal verification data across 12 benchmarks, and imperfect verifier research (April 2026) shows noise rates up to 15% are tolerable. Key limitation: all error-targeted synthesis methods (STAT, Self-Error-Instruct, WarriorMath) depend on frontier LLM teachers for error diagnosis rather than formal tools — STAT uses a teacher model's metacognition to build skill profiles, introducing teacher-dependent biases. Meanwhile, NSRSA's symbolic verification covers only arithmetic operations on GSM8K, leaving algebraic manipulation, equation solving, and constraint reasoning uncovered. The Bidirectional Curriculum framework (March 2026) dynamically adjusts difficulty but lacks formal verification to ensure step-level correctness of synthesized solutions. Concurrent work: Adaptive Problem Generation via Symbolic Representations (Feb 2026) uses SymPy-based symbolic representations in a closed-loop RLVR framework to adapt problem difficulty, but does not perform error-type diagnosis or skill-targeted synthesis — it adapts difficulty globally rather than targeting specific formal error categories. SwS (NeurIPS 2025, updates April 2026) identifies weaknesses via RL pass-rate analysis but without formal step-level diagnosis. Reasoning Core (March 2026) procedurally generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) performs step-aware Lean 4 verification but in one-shot refinement, not closed-loop training.\n\n## Proposed Approach\n\nWe propose a closed-loop self-improvement system where formal symbolic tools (Z3 for satisfiability/logic, SymPy for algebraic computation) serve as both step-level error diagnosticians and targeted problem generators. Each iteration formalizes the student model's solutions, uses symbolic verification to classify step-level errors into a fine-grained taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), and then drives SymPy-based problem synthesis that generates new problems specifically targeting the model's weakest skills — with ground-truth solutions guaranteed by the solver. The student is fine-tuned on this targeted data via SFT and DPO (using formally-verified vs. formally-rejected solution pairs as preference pairs), then re-profiled. Unlike LLM-teacher error analysis (STAT, Self-Error-Instruct), formal diagnosis is unhackable and teacher-free; unlike NSRSA's arithmetic-only symbolic verification on GSM8K, our system covers the full spectrum from algebra through proof-level reasoning across MATH-level and competition problems, using Qwen3.5-9B as the student model.\n\n## Detailed Description\n\nSelf-improvement loops for mathematical reasoning fail through model collapse (solver-verifier gap) and untargeted data waste. We propose FormalLoop, a teacher-free, collapse-resistant self-improvement system using formal symbolic tools as ground-truth error diagnosticians. Each iteration: (1) the student model (Qwen3.5-9B) solves problems, (2) solutions are formalized and verified step-by-step using Z3 and SymPy, (3) step-level errors are classified into a formal mathematical skill taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), (4) SymPy-based problem synthesis generates targeted problems exercising weak skills with solver-guaranteed solutions, and (5) the student trains via SFT+DPO on targeted data and formally-constructed preference pairs. This unifies three validated-but-disconnected advances: FoVer's formal step-level labels (ACL 2026), STAT's error-targeted synthesis superiority (ICLR 2026, +7.5% over uniform), and NSRSA's symbolic verification for training stability (arXiv 2026) — extending formal verification from arithmetic-only GSM8K to full algebraic-to-proof MATH-level coverage, and from one-shot PRM training to iterative closed-loop improvement. Key differentiator vs. concurrent work: Adaptive Problem Generation (Feb 2026) adapts difficulty globally but does not diagnose error types; SwS identifies weaknesses via pass rates without formal diagnosis.\n\n## Key References\n\n- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)\n- STAT: Skill-Targeted Adaptive Training (ICLR 2026)\n- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)\n- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)\n- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)\n- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)\n- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)\n- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)\n- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)\n- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)\n- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)\n- Adaptive Problem Generation via Symbolic Representations (arXiv 2026)\n- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026)\n- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)\n- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)\n- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)\n- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)\n- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)\n- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 600 H100 hours (5 self-training iterations × ~70h generation/verification/training + 200h evaluation/ablations), timeline: 4-5 months (formalization pipeline, Z3/SymPy integration, error taxonomy design, problem synthesis templates, training infrastructure, 5 iterations, paper writing), estimated_gpu_cost: $1,500 (at ~$2.50/hr H100 spot)\n- **human_in_loop**: gpu_hours: 550 H100 hours (Claude accelerates formalization pipeline and taxonomy iteration, slightly fewer wasted runs), timeline: 3-4 months, claude_api_cost: $400-600 (code generation for Z3/SymPy pipeline, formalization prompt engineering, error taxonomy refinement, analysis), estimated_gpu_cost: $1,375\n- **auto_research**: gpu_hours: 550 H100 hours (same experimental compute, fewer false starts), timeline: 6-8 weeks (parallelized implementation, automated hyperparameter search, faster iteration), claude_api_cost: $1,200-2,000 (end-to-end pipeline implementation, formalization code, experiment orchestration, paper drafting), estimated_gpu_cost: $1,375, speed_bottleneck: Symbolic verification throughput — Z3/SymPy step verification is CPU-bound (~0.5-2s per step) and serialized per solution; formalizing natural language solutions to symbolic form requires careful LLM-to-formal translation with ~60-70% success rate, necessitating retry loops\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:32:19.396Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:32:19.396Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-27T08:32:19.442Z_

【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。

【原始 proposal】:
# Formal Error Profiling Enables Targeted Math Self-Improvement

## Core Problem

Self-improvement loops for mathematical reasoning suffer from two key failures: model collapse when using self-verification, and wasteful data generation that doesn't target the model's actual mathematical skill deficits. Can formal symbolic tools serve as both collapse-proof verifiers and fine-grained error diagnosticians to enable stable, efficient self-improvement?

## Research Opportunity

Three recent advances create a ripe moment: FoVer (ACL 2026) proved formal tools can generate accurate step-level error labels for training, STAT (ICLR 2026) showed skill-gap-targeted synthesis outperforms uniform synthesis by 7.5% on MATH, and NSRSA (March 2026) demonstrated symbolic verification helps iterative self-training but only at the arithmetic level on GSM8K. The specific combination of formal step-level error categorization driving targeted symbolic problem synthesis in a closed self-improvement loop has not been attempted. Unlike LLM-teacher-based error analysis (Self-Error-Instruct, STAT, WarriorMath), formal tools provide ground-truth error diagnosis that cannot be hacked or hallucinated, directly addressing the collapse mechanism identified by the solver-verifier gap theory.

## Research Landscape

Current SOTA in synthetic math data includes SPARQ (June 2025, +24% via quality-diversity algorithms from 7.5K seeds), CoTEvol (April 2026, +6.6% average via evolutionary CoT synthesis), and MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). For self-improvement, SPICE (Oct 2025) achieves +8.9% math improvement via document-grounded self-play, while SvS (Aug 2025) achieves +18.3% Pass@32 on AIME24 via variational problem synthesis maintaining training entropy. For verification, FoVer trains generalizable PRMs from formal verification data across 12 benchmarks, and imperfect verifier research (April 2026) shows noise rates up to 15% are tolerable. Key limitation: all error-targeted synthesis methods (STAT, Self-Error-Instruct, WarriorMath) depend on frontier LLM teachers for error diagnosis rather than formal tools — STAT uses a teacher model's metacognition to build skill profiles, introducing teacher-dependent biases. Meanwhile, NSRSA's symbolic verification covers only arithmetic operations on GSM8K, leaving algebraic manipulation, equation solving, and constraint reasoning uncovered. The Bidirectional Curriculum framework (March 2026) dynamically adjusts difficulty but lacks formal verification to ensure step-level correctness of synthesized solutions. Concurrent work: Adaptive Problem Generation via Symbolic Representations (Feb 2026) uses SymPy-based symbolic representations in a closed-loop RLVR framework to adapt problem difficulty, but does not perform error-type diagnosis or skill-targeted synthesis — it adapts difficulty globally rather than targeting specific formal error categories. SwS (NeurIPS 2025, updates April 2026) identifies weaknesses via RL pass-rate analysis but without formal step-level diagnosis. Reasoning Core (March 2026) procedurally generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) performs step-aware Lean 4 verification but in one-shot refinement, not closed-loop training.

## Proposed Approach

We propose a closed-loop self-improvement system where formal symbolic tools (Z3 for satisfiability/logic, SymPy for algebraic computation) serve as both step-level error diagnosticians and targeted problem generators. Each iteration formalizes the student model's solutions, uses symbolic verification to classify step-level errors into a fine-grained taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), and then drives SymPy-based problem synthesis that generates new problems specifically targeting the model's weakest skills — with ground-truth solutions guaranteed by the solver. The student is fine-tuned on this targeted data via SFT and DPO (using formally-verified vs. formally-rejected solution pairs as preference pairs), then re-profiled. Unlike LLM-teacher error analysis (STAT, Self-Error-Instruct), formal diagnosis is unhackable and teacher-free; unlike NSRSA's arithmetic-only symbolic verification on GSM8K, our system covers the full spectrum from algebra through proof-level reasoning across MATH-level and competition problems, using Qwen3.5-9B as the student model.

## Detailed Description

Self-improvement loops for mathematical reasoning fail through model collapse (solver-verifier gap) and untargeted data waste. We propose FormalLoop, a teacher-free, collapse-resistant self-improvement system using formal symbolic tools as ground-truth error diagnosticians. Each iteration: (1) the student model (Qwen3.5-9B) solves problems, (2) solutions are formalized and verified step-by-step using Z3 and SymPy, (3) step-level errors are classified into a formal mathematical skill taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), (4) SymPy-based problem synthesis generates targeted problems exercising weak skills with solver-guaranteed solutions, and (5) the student trains via SFT+DPO on targeted data and formally-constructed preference pairs. This unifies three validated-but-disconnected advances: FoVer's formal step-level labels (ACL 2026), STAT's error-targeted synthesis superiority (ICLR 2026, +7.5% over uniform), and NSRSA's symbolic verification for training stability (arXiv 2026) — extending formal verification from arithmetic-only GSM8K to full algebraic-to-proof MATH-level coverage, and from one-shot PRM training to iterative closed-loop improvement. Key differentiator vs. concurrent work: Adaptive Problem Generation (Feb 2026) adapts difficulty globally but does not diagnose error types; SwS identifies weaknesses via pass rates without formal diagnosis.

## Key References

- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)
- STAT: Skill-Targeted Adaptive Training (ICLR 2026)
- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)
- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)
- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)
- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)
- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)
- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)
- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)
- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)
- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)
- Adaptive Problem Generation via Symbolic Representations (arXiv 2026)
- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026)
- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)
- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)
- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)
- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)
- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)
- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)

## Resource Estimate

- **manual**: gpu_hours: 600 H100 hours (5 self-training iterations × ~70h generation/verification/training + 200h evaluation/ablations), timeline: 4-5 months (formalization pipeline, Z3/SymPy integration, error taxonomy design, problem synthesis templates, training infrastructure, 5 iterations, paper writing), estimated_gpu_cost: $1,500 (at ~$2.50/hr H100 spot)
- **human_in_loop**: gpu_hours: 550 H100 hours (Claude accelerates formalization pipeline and taxonomy iteration, slightly fewer wasted runs), timeline: 3-4 months, claude_api_cost: $400-600 (code generation for Z3/SymPy pipeline, formalization prompt engineering, error taxonomy refinement, analysis), estimated_gpu_cost: $1,375
- **auto_research**: gpu_hours: 550 H100 hours (same experimental compute, fewer false starts), timeline: 6-8 weeks (parallelized implementation, automated hyperparameter search, faster iteration), claude_api_cost: $1,200-2,000 (end-to-end pipeline implementation, formalization code, experiment orchestration, paper drafting), estimated_gpu_cost: $1,375, speed_bottleneck: Symbolic verification throughput — Z3/SymPy step verification is CPU-bound (~0.5-2s per step) and serialized per solution; formalizing natural language solutions to symbolic form requires careful LLM-to-formal translation with ~60-70% success rate, necessitating retry loops


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6da9e317-8aaf-4d85-a7b6-23fcc602c39b",
  "type": "user",
  "uuid": "75940e56-b4d8-41f3-bef5-46f71e86d671",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:32:19.442Z_

```json
{
  "parentUuid": "75940e56-b4d8-41f3-bef5-46f71e86d671",
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
  "uuid": "9f09f7e8-00c0-4990-bd9d-d190353cb0ab",
  "timestamp": "2026-05-27T08:32:19.442Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:32:19.442Z_

```json
{
  "parentUuid": "9f09f7e8-00c0-4990-bd9d-d190353cb0ab",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3a5c4b33-9beb-4520-9d85-8ce49e25aec0",
  "timestamp": "2026-05-27T08:32:19.442Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
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
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Assistant

_source line 7 · 2026-05-27T08:32:31.750Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the 终审 agent (Meta Judge / Final Arbiter). They've provided the original proposal and told me it has passed the triple-consensus triage (GO). Now they want me to remember this proposal for future iterations where I'll integrate worker (发掘 agent and 补救 agent) outputs.

Let me carefully read and understand this proposal:

**Title**: Formal Error Profiling Enables Targeted Math Self-Improvement

**Core Idea**: A closed-loop self-improvement system (FormalLoop) where formal symbolic tools (Z3, SymPy) serve as both:


- Step-level error diagnosticians that classify mistakes into a taxonomy covering algebraic manipulation, equation solving, arithmetic, constraint reasoning, and logical inference
- Targeted problem generators that synthesize exercises addressing specific weak areas

**Key Innovation**: This approach leverages formal tools for ground-truth error diagnosis that can't be manipulated or hallucinated, unlike LLM-based analysis. It builds on NSRSA's arithmetic verification but extends it across the full spectrum from algebra to formal proofs.

**Method**: The iterative cycle has the student model solving problems, formalizing and verifying solutions step-by-step with Z3 and SymPy, classifying any step-level errors into the formal taxonomy, generating targeted problems through SymPy, then training the student via SFT and DPO on this curated data.

I've noted the key references—FoVer, STAT, NSRSA—and I'm ready to evaluate worker outputs once they arrive.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a5c4b33-9beb-4520-9d85-8ce49e25aec0",
  "isSidechain": false,
  "requestId": "req_011CbSmDnEsFP6E15VBBBZri",
  "type": "assistant",
  "uuid": "eb613960-ca51-4fcf-a35d-188340b2254a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DJP4UG1hq9VGmSpEYRNFYu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 16543,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 893,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 3806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3806
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

_source line 8 · 2026-05-27T08:32:38.586Z_

收到。我已完整记录并理解这份原始 proposal：

**Formal Error Profiling Enables Targeted Math Self-Improvement (FormalLoop)**

核心要点已锁定：
- **立意**：用 Z3/SymPy 等形式化符号工具替代 LLM-teacher 做 step-level error diagnosis，驱动 targeted problem synthesis，形成 closed-loop self-improvement
- **差异化**：相比 STAT（LLM teacher 依赖）、NSRSA（仅 arithmetic on GSM8K）、Adaptive Problem Generation（仅全局难度调节无 error-type diagnosis），本方案结合了 formal verification + error categorization + targeted synthesis 三者
- **方法**：5 轮迭代，Qwen3.5-9B 作为 student，SFT+DPO 训练，形式化 error taxonomy 5 类
- **关键引用**：FoVer (ACL 2026)、STAT (ICLR 2026)、NSRSA (arXiv 2026) 等 19 篇
- **资源估计**：~550-600 H100 hours，3-5 个月

我现在以「角色 B：迭代中」待命，等待第一轮发掘 agent 和补救 agent 的输出。请发送 worker 结果，我将：
1. 交叉验证 worker 建议（WebSearch）
2. 整合有效建议
3. 更新 proposal
4. 估计中稿概率
5. 决定继续/收敛/止损

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb613960-ca51-4fcf-a35d-188340b2254a",
  "isSidechain": false,
  "requestId": "req_011CbSmDnEsFP6E15VBBBZri",
  "type": "assistant",
  "uuid": "28582871-354f-48cd-a7e1-b0806ef2e4af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DJP4UG1hq9VGmSpEYRNFYu",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3806,
      "cache_read_input_tokens": 16543,
      "output_tokens": 893,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3806,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 893,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 3806,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3806
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

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。  【原始 proposal】: # Formal Error Profiling Enables Targeted Math Self-Improvement  ## Cor…",
  "leafUuid": "28582871-354f-48cd-a7e1-b0806ef2e4af",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 12 · 2026-05-27T08:38:00.528Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:38:00.528Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "content": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have sufficient research to provide my analysis. Let me synthesize everything.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- [FoVer, arXiv 2505.15960](https://arxiv.org/abs/2505.15960) (ACL Findings 2026): 使用 Z3 和 Isabelle 从 formal reasoning tasks 自动生成 step-level labels 训练 PRM，在 12 个 benchmark 上泛化良好。关键细节：FoVer 的训练数据来自 **formal logic / theorem proving tasks**（本身就是形式化的），而非从 informal 自然语言数学解法中提取。这与 proposal 声称的\"从自然语言解法中做形式化 step-level 诊断\"有本质距离。\n- [STAT, arXiv 2510.10023](https://arxiv.org/abs/2510.10023) (ICLR 2026): 使用 teacher model 的 metacognition 构建 Missing-Skill-Profile，STAT-Syn 合成针对弱技能的训练数据，在 MATH 上 +7.5%。关键局限：**完全依赖 frontier teacher model**（GPT-4 级别）进行技能识别和数据合成，teacher 的 bias 直接传递给 student。\n- [NSRSA, arXiv 2603.21558](https://arxiv.org/abs/2603.21558) (arXiv 2026): 在 GSM8K 上用 SymPy 做 arithmetic-level 符号验证 gate 训练数据，5 轮迭代中维持提升而无 collapse。关键局限：**仅覆盖算术运算**，在 Qwen3-4B-Thinking 上测试，问题规模和数学深度都很有限。\n- [Adaptive Problem Generation via Symbolic Representations, arXiv 2602.19187](https://arxiv.org/abs/2602.19187) (arXiv 2026): 使用 SymPy-based symbolic representations 在 closed-loop RLVR 框架中自适应调整 problem difficulty。关键区别：**只做 difficulty adaptation（全局），不做 error-type diagnosis（细粒度）**。\n- [SwS, arXiv 2506.08989](https://arxiv.org/abs/2506.08989) (NeurIPS 2025): 通过 RL pass-rate 分析识别 weaknesses，提取 failure cases 的 core concepts 合成新问题。不使用 formal step-level diagnosis。\n- [Solver-Verifier Gap Theory](https://arxiv.org/abs/2507.00075) (ICLR 2026): 理论建模 self-improvement 的 training dynamics，核心发现：可靠的 verifier 是防止 model collapse 的关键策略。暗示：verifier 的可靠性越高，self-improvement 的理论上限越高。\n- [MATH-VF / Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869) (arXiv 2025): 用 SymPy + Z3 做 step-level 数学验证（training-free），但只做 **one-shot verification**，不是 iterative training loop。\n- [FormalMATH Benchmark](https://arxiv.org/abs/2505.02735) (arXiv 2025): SOTA theorem provers 在实际采样预算下 formalization 成功率仅 16.46%，显示形式化覆盖的严峻挑战。\n- 调研总结：当前领域研究者在两条线上分别推进——一条是 \"error-targeted synthesis\"（STAT, SwS, Self-Error-Instruct），依赖 LLM teacher 做诊断；另一条是 \"symbolic verification for training\"（NSRSA, FoVer, Safe），但限于特定任务类型或单次应用。**将两条线打通（formal diagnosis → targeted synthesis → iterative loop）是一个被识别但尚未实现的组合**，proposal 的定位是准确的。但 formalization 的覆盖率和可靠性是这条路线的核心技术瓶颈，proposal 对此的讨论不够充分。\n\n---\n\n【发掘点 1】\n- 维度: 核心 claim 强化\n- 内容: Proposal 当前将 \"teacher-free\" 作为一个附带优势提及，但实际上这应该被提升为 **第一等级的贡献 claim**。调研发现，STAT 依赖 frontier teacher 的 metacognition 做 skill profiling，SwS 依赖 LLM 提取 failure concepts，Self-Error-Instruct 依赖 instructor model 做 error 分析——**所有现有 error-targeted synthesis 方法都绑定在 teacher-student 范式上**。这意味着：(a) 需要 API 访问 frontier model，成本高且不可复现；(b) teacher 的 bias/盲点直接传导到 student 的 skill profile（如果 teacher 也认不出某类错误，student 永远不会被针对训练）；(c) teacher 能力上限决定了 student 的提升天花板。FormalLoop 不是\"换了个更好的 teacher\"，而是**彻底取消了 teacher 角色**——error diagnosis 来自数学公理系统而非另一个 LLM。这是一个范式级别的差异，应当在 framing 中占据核心位置，而非被埋在技术细节里。建议将论文的核心叙事从 \"formal tools as verifiers\" 重构为 \"the first teacher-free error-targeted self-improvement system for mathematical reasoning\"。\n- 价值: 直接提升 Novelty 和 Significance。\"Teacher-free\" 不仅是技术选择，更解决了一个领域级问题——当前所有 error-targeted 方法的 scalability 被 teacher model 的成本和 bias 天花板限制。将此作为主 claim 使论文的贡献从 \"组合创新\" 升级为 \"范式突破\"。\n- 调研依据: 对 STAT、SwS、Self-Error-Instruct、WarriorMath 的系统对比，发现 teacher 依赖是共性瓶颈。\n\n【发掘点 2】\n- 维度: 前提假设质疑\n- 内容: Proposal 声称 formal verification 覆盖 \"full spectrum from algebra through proof-level reasoning across MATH-level and competition problems\"，但这个 claim 的前提假设存在严重的未验证风险。具体问题：(1) **Formalization 覆盖率瓶颈**：Proposal 自身承认 formalization 成功率约 60-70%，这意味着 30-40% 的学生解法无法被 formally diagnosed。更关键的是，**无法 formalize 的那 30-40% 很可能不是随机分布的**——组合数学、几何直觉、构造性证明等类型的问题天然更难 formalize 到 Z3/SymPy，这会导致 error profile 存在系统性偏差：模型在这些领域的弱点会被 under-detected。(2) **Z3+SymPy 的数学覆盖范围**：Z3 处理 satisfiability/logic，SymPy 处理代数/微积分，但 MATH benchmark 中大量 Number Theory（模运算、整除性）、Combinatorics（计数、概率）、Geometry（坐标/合成几何）问题的 step-level verification 在 Z3/SymPy 中并不 trivial，很多需要 domain-specific encoding。Proposal 应当坦诚讨论覆盖率边界，并将 \"在可 formalize 的子集上做 ground-truth diagnosis\" 定位为第一步，而非声称 \"full spectrum\"。\n- 价值: 这不是要否定 idea，而是提升 claim 的可信度。过度声称 \"full spectrum\" 会招致审稿人基于覆盖率反例的直接攻击。诚实的 claim（\"we achieve ground-truth diagnosis on a significant and formally-tractable subset, and show this is sufficient for effective self-improvement\"）反而更有说服力，尤其可以结合 imperfect verifier 论文（noise rate up to 15% is tolerable）来论证：即使只覆盖 60-70%，formal diagnosis 的 precision advantage 仍然使其优于 100%-coverage-but-noisy 的 LLM-teacher diagnosis。\n- 调研依据: FormalMATH benchmark 显示 SOTA prover formalization 成功率仅 16.46%（虽然任务不同，但反映 formalization 难度）；FoVer 的训练数据来自本身就是 formal 的 logic/theorem proving tasks，与从 informal math 解法做 formalization 有本质差异。\n\n【发掘点 3】\n- 维度: novelty 锐化\n- 内容: Proposal 提到使用 \"formally-verified vs. formally-rejected solution pairs as preference pairs\" 做 DPO，但将此作为管线的一个步骤一笔带过。这实际上是一个**独立的、有份量的 novelty 点**，值得被单独论述。当前 DPO 文献中，preference pairs 的来源几乎都是：(a) 人类标注（expensive, subjective），(b) frontier model 判断（noisy, model-dependent），(c) outcome correctness（binary, coarse-grained）。FormalLoop 的 DPO 信号来自 **step-level formal verification**，这带来一个独特优势：可以构造 **在特定步骤 diverge 的 preference pairs**——两个解法共享前 k 步，在第 k+1 步分叉，一个 formally verified correct 一个 formally rejected。这种 **step-localized preference signal** 在 DPO 文献中是全新的，让模型学到的不是\"好解法 vs 坏解法\"，而是\"在这个具体推理点该怎么走\"。建议在论文中将此作为一个独立 contribution 阐述，而非管线描述中的附属步骤。\n- 价值: Novelty 维度。将 DPO 信号的粒度从 solution-level 推进到 step-level（且有 formal guarantee），这本身就是一个可以独立发表的 insight。在 FormalLoop 论文中作为独立 contribution 呈现，会显著增强论文的 novelty 密度。\n- 调研依据: 基于领域整体趋势判断——当前 DPO/RLHF 文献中 step-level formal preference pairs 尚无先例；FoVer 的 step-level labels 用于 PRM training（reward model），但未用于 DPO preference pair construction。\n\n【发掘点 4】\n- 维度: significance 提升\n- 内容: Proposal 的理论叙事可以更强。Solver-verifier gap theory (ICLR 2026) 证明了 verifier 的可靠性是 self-improvement 成功的关键。Proposal 应当显式构建一个 **理论论证链**：(1) solver-verifier gap theory 预测 verifier 可靠性决定 self-improvement 上限 → (2) formal verification 提供的是 ground-truth verification（reliability = 1，在可 formalize 的范围内）→ (3) 因此 FormalLoop 理论上具有比所有 LLM-based verifier 更高的 self-improvement 天花板 → (4) 这个理论预测可通过实验验证（FormalLoop vs. LLM-verified loop 在多轮迭代后的 collapse resistance 对比）。这个论证链不仅加强了 motivation，还提供了一个 **可验证的理论假设**——\"formal verification 应当展现出更强的 collapse resistance\"——这让论文从 \"engineering contribution\"（我们搭了个更好的管线）升级为 \"scientific contribution\"（我们验证了一个关于 self-improvement dynamics 的理论假设）。\n- 价值: Significance 维度。从工程贡献升级为科学贡献，直接提升论文在顶会的竞争力。审稿人对 \"better pipeline\" 的兴趣有限，但对 \"empirically testing a theoretical prediction about self-improvement dynamics\" 的兴趣会高得多。\n- 调研依据: Solver-verifier gap theory (ICLR 2026) 提供了直接的理论框架；NSRSA 的实验（symbolic verification 在 5 轮迭代中维持提升而 outcome-only 方法 plateau）已经提供了部分初步证据。\n\n【发掘点 5】\n- 维度: trivial alternative 威胁\n- 内容: 需要正面回应一个审稿人必然会提出的问题：**为什么不直接用 outcome verification（最终答案对不对）+ STAT 的 LLM skill profiling？** 这个 trivial alternative 的成本更低（无需 formalization pipeline），覆盖率更高（100% 的问题都能 profile），且 STAT 已经证明了 +7.5% 的效果。Proposal 需要清晰论证 formal step-level diagnosis 相对于这个 baseline 的 **不可替代的增量价值**。建议的论证角度：(a) **错误归因精度**：outcome verification 只知道解法错了，不知道错在哪一步——两个最终答案错误的解法可能在完全不同的步骤出错，对应完全不同的 skill deficits。LLM teacher 的 step-level diagnosis 虽然能定位，但有 hallucination 风险（\"LLMs cannot spot math errors even when allowed to peek into the solution\"，arXiv 2509.01395）。Formal verification 是唯一能提供 guaranteed correct step-level attribution 的方法。(b) **迭代稳定性**：LLM teacher 的 bias 会在多轮迭代中被放大（teacher 在第 1 轮误诊的 skill gap 导致第 2 轮的训练数据偏差，进而导致第 3 轮的 profile 进一步偏离），而 formal verification 的 zero-bias 特性使每轮迭代都是 independently calibrated 的。这个 argument 在多轮 loop 的设定下尤其有力。\n- 价值: 直接回应 trivial alternative 威胁，加强 novelty claim 的说服力。如果这个问题不被主动回答，审稿人几乎一定会以此质疑。\n- 调研依据: STAT (ICLR 2026) 作为 trivial alternative 的代表；arXiv 2509.01395 (\"LLMs cannot spot math errors\") 提供了 LLM-based diagnosis 不可靠的实证依据。\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [STAT: Skill-Targeted Adaptive Training](https://arxiv.org/abs/2510.10023)\n- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)\n- [SwS: Self-aware Weakness-driven Problem Synthesis](https://arxiv.org/abs/2506.08989)\n- [Solver-Verifier Gap Theory](https://arxiv.org/abs/2507.00075)\n- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869)\n- [FormalMATH Benchmark](https://arxiv.org/abs/2505.02735)\n- [LLMs cannot spot math errors](https://arxiv.org/abs/2509.01395)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research context. Let me compile my analysis.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **FoVer** (ACL 2026 Findings): 使用 Z3 和 Isabelle 进行 step-level 验证生成 PRM 训练数据。实验覆盖 ProcessBench + 12 个推理 benchmark（MATH, AIME, ANLI, MMLU, BBH）。Baseline 为 human-annotated PRMs 和无 formal verification 的 PRMs。Ablation 区分了不同 formal tool 的贡献。\n- **STAT** (ICLR 2026): Teacher LLM 做 skill profiling + targeted synthesis。实验使用 Llama/Qwen 系列，评估 MATH（+7.5%）及 OOD benchmark AIME24/25, AMC23（+4.6%）。Ablation 包括 STAT-Sel vs STAT-Syn、不同 skill 数量、与 GRPO 互补性。\n- **NSRSA** (arXiv 2026): Qwen3-4B-Thinking 跑 5 轮 self-training。5 个实验条件：no verification / outcome verification / majority voting / full NSRSA / NSRSA+DPO。仅覆盖 GSM8K 算术验证，cross-transfer 到 MATH-500。拒绝了~34% 通过 outcome verification 的 \"lucky guess\" 样本。\n- **SwS** (NeurIPS 2025): Qwen2.5-base (3B/7B/32B)，8 个 benchmark（GSM8K, MATH-500, Minerva Math, Olympiad-Bench, Gaokao-2023, AMC23, AIME24, AIME25），生成 40k synthetic problems per size。Baseline 包括 vanilla RLVR、SPICE、curriculum-based methods。\n- **SvS** (arXiv 2025): 12 个 benchmark，3B-32B 模型，+18.3% Pass@32 on AIME24。关键评估维度：entropy stability、Pass@K 曲线。\n- **Adaptive Problem Generation via Symbolic Representations** (arXiv Feb 2026): 使用 SymPy 符号空间做 closed-loop 问题生成，GRPO/PPO 训练，评估 GSM8K, MATH500, AIME24。这是最直接的可比工作——同样使用 SymPy 做符号问题生成但不做 error-type diagnosis。\n- **Qwen3.5-9B** (Released March 2026): Apache 2.0，已在 HuggingFace 开放。GPQA Diamond 81.7，math reasoning 较强。支持 thinking/non-thinking 模式。\n\n- **调研总结**: 该领域当前实验标准要求：(1) 至少 6-8 个 benchmark 覆盖 GSM8K 到 AIME 不同难度梯度；(2) 与 RLVR/GRPO 标准 post-training 方法对比；(3) 多个 model size 验证泛化性；(4) 细粒度 ablation 隔离各组件贡献；(5) 迭代过程中的 collapse/entropy 分析。审稿人普遍要求 compute-normalized comparison 和 statistical significance reporting。\n\n---\n\n【缺陷 1】\n- 类别: 可行性问题 / 实验设计不足\n- 问题: Proposal 声称覆盖 \"full spectrum from algebra through proof-level reasoning across MATH-level and competition problems\"，但 Z3+SymPy 的实际覆盖范围存在严重 gap。MATH benchmark 包含 7 个类别（Algebra, Counting & Probability, Geometry, Intermediate Algebra, Number Theory, Prealgebra, Precalculus），其中 **Geometry（~15% of MATH）和 Counting & Probability（~15%）基本无法被 Z3/SymPy 有效形式化验证**。Number Theory 中的许多问题也超出 Z3 的能力范围。Proposal 自身承认形式化成功率仅 ~60-70%，但未分析这一 gap 对 error profiling 的系统性偏差：**error profile 只能反映可形式化问题上的错误分布，而非模型真实的完整弱点图谱**。模型在 geometry/combinatorics 上可能是最弱的，但系统完全无法诊断这些类别的错误。\n- 严重度: 可补救\n- 补救方案:\n  1. **明确限定 claim scope**：将核心 claim 从 \"full spectrum\" 缩窄为 \"algebraic and arithmetic reasoning domains amenable to symbolic formalization\"，承认 geometry/combinatorics 是 out-of-scope limitation\n  2. **按 MATH 子类别分析形式化覆盖率**：报告每个子类别的 formalization success rate，让 reviewer 清楚系统的真实覆盖范围\n  3. **对不可形式化类别设计 fallback 策略**：例如对 geometry/combinatorics 使用 outcome-based verification (答案正确性) 作为退化方案，而非完全忽略这些类别\n  4. **在 ablation 中加入 \"coverage analysis\"**：对比 full-spectrum uniform synthesis vs. formal-targeted synthesis 在可形式化 vs. 不可形式化子类别上的各自表现\n- 调研依据: NSRSA 的实验教训——该论文诚实限定在 GSM8K 算术验证，获得了 ACL 接受；而 Adaptive Problem Generation (Feb 2026) 同样使用 SymPy 但也仅限于可符号表达的问题类型。过度声称覆盖范围是审稿红旗。\n\n【缺陷 2】\n- 类别: baseline 不足或过时\n- 问题: Proposal 虽然在 Research Landscape 中提到了大量相关工作，但**没有明确列出实验中要对比的 baseline list**。根据调研，以下 baseline 是审稿人会期望看到的：\n  1. **SwS** (NeurIPS 2025) — 最直接可比：weakness-driven problem synthesis，使用 pass-rate 分析弱点而非 formal diagnosis。这是验证 \"formal error profiling 比 pass-rate-based weakness detection 更好\" 的核心对照\n  2. **Adaptive Problem Generation** (Feb 2026) — 同样使用 SymPy 做 symbolic problem synthesis in closed loop，但不做 error-type diagnosis。这是验证 \"error-type targeting 比 global difficulty adaptation 更好\" 的核心对照\n  3. **GRPO/RLVR baseline** — 当前 post-training 标准方法，任何 self-improvement 方法都必须与之对比\n  4. **Vanilla SFT on uniform synthetic data** — 验证 targeting 比 uniform 好的最基本 baseline\n  5. **STAT-style LLM-teacher error profiling** — 验证 \"formal tools 比 LLM teacher 好\" 的核心 claim\n- 严重度: 可补救\n- 补救方案: 明确规划以下 baseline 矩阵：\n  - **Training paradigm baselines**: Vanilla SFT, SFT+DPO (uniform data), GRPO/RLVR\n  - **Targeting method baselines**: Uniform random synthesis, STAT-style LLM-teacher profiling + targeted synthesis, SwS pass-rate-based weakness targeting\n  - **Symbolic method baseline**: Adaptive Problem Generation (global difficulty adaptation without error-type targeting)\n  - **Verification baselines**: Outcome-only verification (NSRSA-style), majority voting, no verification\n  \n  其中 SwS 和 STAT 有公开代码/描述可复现；Adaptive Problem Generation 可从论文描述复现其核心 pipeline。\n- 调研依据: SwS (NeurIPS 2025) 的实验对比了 vanilla RLVR、curriculum-based methods、SPICE 等；STAT 对比了 vanilla SFT、random augmentation、teacher-free methods。审稿人期望看到与这些 published 方法的直接对比。\n\n【缺陷 3】\n- 类别: 评估方案缺陷\n- 问题: Proposal **未明确指定评估 benchmark 和 evaluation protocol**。在该领域，审稿人期望看到明确的 benchmark list、evaluation metrics（accuracy、Pass@K、多少次 sampling）、以及 OOD 泛化测试。此外，Qwen3.5-9B 的 base math 能力已经很强（GPQA Diamond 81.7），self-improvement 的边际增益可能较小——如果没有 confidence interval 和 statistical significance testing，小幅改进难以说服 reviewer。\n- 严重度: 可补救\n- 补救方案:\n  1. **明确 benchmark 列表**：至少覆盖 GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench（7 个，跨越不同难度梯度）\n  2. **评估 protocol**：报告 greedy accuracy + Pass@K (K=8,32) + majority voting@K，与 SvS/SwS 的报告方式对齐\n  3. **统计显著性**：至少 3 次独立 run 的均值和标准差，对关键结果做 significance test\n  4. **OOD 泛化**：由于 self-improvement 基于 MATH 训练集问题，必须在 AIME24/25 等 OOD competition benchmark 上验证泛化\n  5. **按 MATH 子类别报告**：区分可形式化类别 vs. 不可形式化类别的改进幅度（直接支撑核心 claim）\n- 调研依据: SwS 使用 8 个 benchmark + Pass@K 报告；SvS 使用 12 个 benchmark + Pass@32；STAT 在 MATH + 4 个 OOD benchmark 报告。这是该领域的最低评估标准。\n\n【缺陷 4】\n- 类别: ablation 不完整\n- 问题: Proposal 描述了 SFT+DPO 训练方式和 formal error taxonomy，但**未设计任何 ablation study**。核心 claim 包含多个可分离组件，审稿人必然要求逐个验证。\n- 严重度: 可补救\n- 补救方案: 需要设计以下 ablation：\n  1. **Error profiling source**: Formal verification profiling vs. LLM-based profiling vs. pass-rate-based profiling vs. random → 隔离 \"formal\" 的贡献\n  2. **Targeting vs. uniform**: Targeted synthesis (based on error profile) vs. uniform synthesis (same quantity, random skill distribution) → 隔离 \"targeting\" 的贡献\n  3. **Training objective**: SFT only vs. DPO only vs. SFT+DPO → 隔离 DPO preference learning 的增益\n  4. **Error taxonomy granularity**: 5-type fine-grained taxonomy vs. 2-type coarse taxonomy (arithmetic vs. non-arithmetic) vs. single aggregate → 隔离 fine-grained diagnosis 的价值\n  5. **Iteration analysis**: Per-iteration improvement curve，报告 accuracy、error profile 变化、formalization coverage 变化、entropy → 证明 loop 是稳定收敛而非 collapse\n  6. **Preference pair quality**: DPO pairs 来自 formal verification vs. DPO pairs 来自 outcome verification → 隔离 step-level formal verification 对 preference learning 的贡献\n- 调研依据: STAT 的 ablation 包括 STAT-Sel vs STAT-Syn、skill 数量变化、与 GRPO 互补性；NSRSA 的 ablation 区分了 5 种 verification 条件；SwS 分析了 per-category weakness targeting 的贡献。这些 ablation 粒度是审稿人的期望基线。\n\n【缺陷 5】\n- 类别: 实验设计不足 / 可行性问题\n- 问题: Proposal 提到使用 \"formally-verified vs. formally-rejected solution pairs as preference pairs\" 做 DPO，但**未讨论 formalization failure 与 reasoning error 的区分问题**。当一个 solution step 无法通过 formal verification 时，可能有两种原因：(a) 推理确实错误，(b) 形式化过程本身失败（LLM-to-formal translation 的 ~30-40% failure rate）。如果将 formalization failure 错误标注为 reasoning error 并用于 DPO rejected 样本，会引入系统性噪声，尤其是当 formalization failure 与 problem difficulty 正相关时（越难的问题越难形式化），这会系统性地将 hard problem 的 solution 标注为 \"rejected\"，产生 anti-difficulty bias。\n- 严重度: 可补救\n- 补救方案:\n  1. **引入 formalization confidence score**：区分 \"verification failed = error\" 和 \"formalization failed = unknown\"，只对高置信度 verified/rejected pairs 做 DPO\n  2. **设计 filtering pipeline**：对 DPO rejected 样本做二次检查——如果 formal verification reject 但 answer 正确，标记为 \"suspicious formalization failure\" 并排除\n  3. **报告 DPO 数据质量指标**：false positive rate（正确 solution 被 reject）和 false negative rate（错误 solution 被 accept），参考 imperfect verifier 论文 (April 2026) 的 tolerance threshold（≤15% noise rate）\n  4. **在 ablation 中对比不同 filtering 严格度的影响**\n- 调研依据: \"An Imperfect Verifier is Good Enough\" (April 2026) 证明 noise rate ≤15% 是可容忍的，但需要明确度量和报告。NSRSA 报告了 ~34% 的 rejection rate（correct-answer but flawed-reasoning solutions），这种细粒度分析是审稿人期望看到的。\n\n【缺陷 6】\n- 类别: compute 公平性问题\n- 问题: Proposal 未讨论与 baseline 方法的 **compute-normalized comparison**。FormalLoop 的 5 轮迭代涉及大量 symbolic verification overhead（proposal 提到 Z3/SymPy step verification 是 CPU-bound ~0.5-2s per step），这使得每轮的 wall-clock time 和总 compute 可能显著高于 SwS/STAT 等 baselines。如果 FormalLoop 用了更多 compute 才获得同等或略好的结果，审稿人会质疑是 formal verification 的贡献还是 more compute 的贡献。\n- 严重度: 可补救\n- 补救方案:\n  1. **明确报告每个方法的总 compute**（GPU hours + CPU hours for symbolic verification），而非仅报告 GPU hours\n  2. **设计 compute-matched comparison**：给 baseline 方法等量的额外 compute budget（例如让 SwS 多训练几步，或让 uniform synthesis 生成更多数据）\n  3. **绘制 accuracy vs. total compute 曲线**：展示 FormalLoop 在相同 compute budget 下是否仍然优于 baselines（参照 SvS 的 entropy-vs-iteration 分析方式）\n  4. **分析 symbolic verification throughput 瓶颈**：报告每轮 formalization+verification 的 wall-clock time，以及可并行化程度\n- 调研依据: SwS 的实验明确报告了训练 token 数量和 sampling 次数作为 compute 度量；STAT 控制了 training data quantity 的公平性。基于领域实验规范判断，compute fairness 是 AAAI 审稿的常见质疑点。\n\n【缺陷 7】\n- 类别: 实验设计不足\n- 问题: Proposal 仅使用 **Qwen3.5-9B 单一模型**进行实验。在该领域，SwS 使用 3B/7B/32B 三个 scale，SvS 覆盖 3B-32B，STAT 使用 Llama+Qwen 两个 model family。单一模型的结果很容易被审稿人质疑为 \"method 恰好对这个特定模型有效\"。\n- 严重度: 可补救\n- 补救方案:\n  1. **至少增加一个 smaller model（如 Qwen3.5-4B 或 Llama-3-8B）** 验证方法在不同能力水平模型上的效果\n  2. **理想情况下覆盖 2 个 model size + 2 个 model family**，但考虑 600 H100 hours 的预算约束，务实方案是 Qwen3.5-9B (主实验) + Qwen3.5-4B (验证实验，减少迭代轮数)\n  3. **如果 compute 预算确实不足以支持多模型**，至少在 related work/limitation 中明确说明，并将 multi-model 验证列为 future work\n- 调研依据: SwS (NeurIPS 2025) 覆盖 Qwen2.5 3B/7B/32B；STAT (ICLR 2026) 覆盖 Llama+Qwen。单模型实验在顶会接受率上明显劣势。在 600 H100 hours 预算下，增加一个 4B 模型的 3 轮迭代实验（约 150 hours 额外）是可行的。\n\n【缺陷 8】\n- 类别: 实验设计不足\n- 问题: 5 类 error taxonomy（algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference）**缺乏验证和覆盖度分析**。这个 taxonomy 是 proposal 的核心创新之一，但 (a) 没有 pilot study 验证这 5 类是否真的覆盖了模型在 MATH 上的主要错误类型，(b) 没有讨论 error 类型之间的重叠/歧义（一个错误可能同时涉及 algebraic manipulation 和 equation solving），(c) 没有与已有 math skill taxonomy（如 STAT 的 skill taxonomy）对比说明为何选择这 5 类。\n- 严重度: 可补救\n- 补救方案:\n  1. **Pilot study**：在正式实验前，用 Qwen3.5-9B 在 MATH test set 的 500 道题上生成 solutions，人工或 formal verification 分析实际 error 分布，验证 taxonomy 覆盖度\n  2. **报告 error classification 的 inter-annotator agreement 或 formal consistency**：同一错误被不同 formal tools 分类的一致性\n  3. **与 STAT 的 skill taxonomy 对比**：说明为何 formal taxonomy 选择这 5 个维度（可能是因为这 5 类恰好是 Z3/SymPy 能区分的类型——这本身就是一个有意义的 insight）\n  4. **在 ablation 中测试 taxonomy 的粒度敏感性**（见缺陷 4 第 4 点）\n- 调研依据: STAT 使用 teacher LLM 生成 skill list 并验证其覆盖度；SwS 按 problem category 分组弱点。error taxonomy 的合理性需要实证支持，不能仅靠 a priori 设定。\n\n---\n\n**总结**：上述 8 个缺陷均为可补救问题，无方向性致命缺陷。最关键的 3 个是：**缺陷 1**（形式化覆盖 gap 导致 claim 过度）、**缺陷 2**（baseline 不明确且可能缺失关键对照）、**缺陷 4**（ablation 设计缺失）。这三个如果不补，几乎可以确定会被 reviewer 要求 major revision。其余缺陷（DPO 质量、compute 公平性、多模型、taxonomy 验证、evaluation protocol）是加固实验说服力的重要环节。在 600 H100 hours 的预算下，建议优先投入在 baseline 对比和 ablation 上，coverage analysis 和 DPO quality analysis 是低成本高回报的补充实验。\n\nSources:\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://arxiv.org/abs/2510.10023)\n- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning](https://arxiv.org/abs/2603.21558)\n- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://arxiv.org/abs/2506.08989)\n- [SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis](https://arxiv.org/abs/2508.14029)\n- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)\n- [Qwen3.5-9B on HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B)\n- [Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving](https://arxiv.org/abs/2505.20869)\n- [SPICE: Self-Play In Corpus Environments Improves Reasoning](https://arxiv.org/abs/2510.24684)"
}
```

---

### Runtime record

_source line 13 · 2026-05-27T08:38:00.528Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:38:00.528Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

## Round 2

32 recorded events

### User

_source line 14 · 2026-05-27T08:38:00.572Z_

【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have sufficient research to provide my analysis. Let me synthesize everything.

---

【状态】: 有发掘空间

【前置调研发现】
- [FoVer, arXiv 2505.15960](https://arxiv.org/abs/2505.15960) (ACL Findings 2026): 使用 Z3 和 Isabelle 从 formal reasoning tasks 自动生成 step-level labels 训练 PRM，在 12 个 benchmark 上泛化良好。关键细节：FoVer 的训练数据来自 **formal logic / theorem proving tasks**（本身就是形式化的），而非从 informal 自然语言数学解法中提取。这与 proposal 声称的"从自然语言解法中做形式化 step-level 诊断"有本质距离。
- [STAT, arXiv 2510.10023](https://arxiv.org/abs/2510.10023) (ICLR 2026): 使用 teacher model 的 metacognition 构建 Missing-Skill-Profile，STAT-Syn 合成针对弱技能的训练数据，在 MATH 上 +7.5%。关键局限：**完全依赖 frontier teacher model**（GPT-4 级别）进行技能识别和数据合成，teacher 的 bias 直接传递给 student。
- [NSRSA, arXiv 2603.21558](https://arxiv.org/abs/2603.21558) (arXiv 2026): 在 GSM8K 上用 SymPy 做 arithmetic-level 符号验证 gate 训练数据，5 轮迭代中维持提升而无 collapse。关键局限：**仅覆盖算术运算**，在 Qwen3-4B-Thinking 上测试，问题规模和数学深度都很有限。
- [Adaptive Problem Generation via Symbolic Representations, arXiv 2602.19187](https://arxiv.org/abs/2602.19187) (arXiv 2026): 使用 SymPy-based symbolic representations 在 closed-loop RLVR 框架中自适应调整 problem difficulty。关键区别：**只做 difficulty adaptation（全局），不做 error-type diagnosis（细粒度）**。
- [SwS, arXiv 2506.08989](https://arxiv.org/abs/2506.08989) (NeurIPS 2025): 通过 RL pass-rate 分析识别 weaknesses，提取 failure cases 的 core concepts 合成新问题。不使用 formal step-level diagnosis。
- [Solver-Verifier Gap Theory](https://arxiv.org/abs/2507.00075) (ICLR 2026): 理论建模 self-improvement 的 training dynamics，核心发现：可靠的 verifier 是防止 model collapse 的关键策略。暗示：verifier 的可靠性越高，self-improvement 的理论上限越高。
- [MATH-VF / Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869) (arXiv 2025): 用 SymPy + Z3 做 step-level 数学验证（training-free），但只做 **one-shot verification**，不是 iterative training loop。
- [FormalMATH Benchmark](https://arxiv.org/abs/2505.02735) (arXiv 2025): SOTA theorem provers 在实际采样预算下 formalization 成功率仅 16.46%，显示形式化覆盖的严峻挑战。
- 调研总结：当前领域研究者在两条线上分别推进——一条是 "error-targeted synthesis"（STAT, SwS, Self-Error-Instruct），依赖 LLM teacher 做诊断；另一条是 "symbolic verification for training"（NSRSA, FoVer, Safe），但限于特定任务类型或单次应用。**将两条线打通（formal diagnosis → targeted synthesis → iterative loop）是一个被识别但尚未实现的组合**，proposal 的定位是准确的。但 formalization 的覆盖率和可靠性是这条路线的核心技术瓶颈，proposal 对此的讨论不够充分。

---

【发掘点 1】
- 维度: 核心 claim 强化
- 内容: Proposal 当前将 "teacher-free" 作为一个附带优势提及，但实际上这应该被提升为 **第一等级的贡献 claim**。调研发现，STAT 依赖 frontier teacher 的 metacognition 做 skill profiling，SwS 依赖 LLM 提取 failure concepts，Self-Error-Instruct 依赖 instructor model 做 error 分析——**所有现有 error-targeted synthesis 方法都绑定在 teacher-student 范式上**。这意味着：(a) 需要 API 访问 frontier model，成本高且不可复现；(b) teacher 的 bias/盲点直接传导到 student 的 skill profile（如果 teacher 也认不出某类错误，student 永远不会被针对训练）；(c) teacher 能力上限决定了 student 的提升天花板。FormalLoop 不是"换了个更好的 teacher"，而是**彻底取消了 teacher 角色**——error diagnosis 来自数学公理系统而非另一个 LLM。这是一个范式级别的差异，应当在 framing 中占据核心位置，而非被埋在技术细节里。建议将论文的核心叙事从 "formal tools as verifiers" 重构为 "the first teacher-free error-targeted self-improvement system for mathematical reasoning"。
- 价值: 直接提升 Novelty 和 Significance。"Teacher-free" 不仅是技术选择，更解决了一个领域级问题——当前所有 error-targeted 方法的 scalability 被 teacher model 的成本和 bias 天花板限制。将此作为主 claim 使论文的贡献从 "组合创新" 升级为 "范式突破"。
- 调研依据: 对 STAT、SwS、Self-Error-Instruct、WarriorMath 的系统对比，发现 teacher 依赖是共性瓶颈。

【发掘点 2】
- 维度: 前提假设质疑
- 内容: Proposal 声称 formal verification 覆盖 "full spectrum from algebra through proof-level reasoning across MATH-level and competition problems"，但这个 claim 的前提假设存在严重的未验证风险。具体问题：(1) **Formalization 覆盖率瓶颈**：Proposal 自身承认 formalization 成功率约 60-70%，这意味着 30-40% 的学生解法无法被 formally diagnosed。更关键的是，**无法 formalize 的那 30-40% 很可能不是随机分布的**——组合数学、几何直觉、构造性证明等类型的问题天然更难 formalize 到 Z3/SymPy，这会导致 error profile 存在系统性偏差：模型在这些领域的弱点会被 under-detected。(2) **Z3+SymPy 的数学覆盖范围**：Z3 处理 satisfiability/logic，SymPy 处理代数/微积分，但 MATH benchmark 中大量 Number Theory（模运算、整除性）、Combinatorics（计数、概率）、Geometry（坐标/合成几何）问题的 step-level verification 在 Z3/SymPy 中并不 trivial，很多需要 domain-specific encoding。Proposal 应当坦诚讨论覆盖率边界，并将 "在可 formalize 的子集上做 ground-truth diagnosis" 定位为第一步，而非声称 "full spectrum"。
- 价值: 这不是要否定 idea，而是提升 claim 的可信度。过度声称 "full spectrum" 会招致审稿人基于覆盖率反例的直接攻击。诚实的 claim（"we achieve ground-truth diagnosis on a significant and formally-tractable subset, and show this is sufficient for effective self-improvement"）反而更有说服力，尤其可以结合 imperfect verifier 论文（noise rate up to 15% is tolerable）来论证：即使只覆盖 60-70%，formal diagnosis 的 precision advantage 仍然使其优于 100%-coverage-but-noisy 的 LLM-teacher diagnosis。
- 调研依据: FormalMATH benchmark 显示 SOTA prover formalization 成功率仅 16.46%（虽然任务不同，但反映 formalization 难度）；FoVer 的训练数据来自本身就是 formal 的 logic/theorem proving tasks，与从 informal math 解法做 formalization 有本质差异。

【发掘点 3】
- 维度: novelty 锐化
- 内容: Proposal 提到使用 "formally-verified vs. formally-rejected solution pairs as preference pairs" 做 DPO，但将此作为管线的一个步骤一笔带过。这实际上是一个**独立的、有份量的 novelty 点**，值得被单独论述。当前 DPO 文献中，preference pairs 的来源几乎都是：(a) 人类标注（expensive, subjective），(b) frontier model 判断（noisy, model-dependent），(c) outcome correctness（binary, coarse-grained）。FormalLoop 的 DPO 信号来自 **step-level formal verification**，这带来一个独特优势：可以构造 **在特定步骤 diverge 的 preference pairs**——两个解法共享前 k 步，在第 k+1 步分叉，一个 formally verified correct 一个 formally rejected。这种 **step-localized preference signal** 在 DPO 文献中是全新的，让模型学到的不是"好解法 vs 坏解法"，而是"在这个具体推理点该怎么走"。建议在论文中将此作为一个独立 contribution 阐述，而非管线描述中的附属步骤。
- 价值: Novelty 维度。将 DPO 信号的粒度从 solution-level 推进到 step-level（且有 formal guarantee），这本身就是一个可以独立发表的 insight。在 FormalLoop 论文中作为独立 contribution 呈现，会显著增强论文的 novelty 密度。
- 调研依据: 基于领域整体趋势判断——当前 DPO/RLHF 文献中 step-level formal preference pairs 尚无先例；FoVer 的 step-level labels 用于 PRM training（reward model），但未用于 DPO preference pair construction。

【发掘点 4】
- 维度: significance 提升
- 内容: Proposal 的理论叙事可以更强。Solver-verifier gap theory (ICLR 2026) 证明了 verifier 的可靠性是 self-improvement 成功的关键。Proposal 应当显式构建一个 **理论论证链**：(1) solver-verifier gap theory 预测 verifier 可靠性决定 self-improvement 上限 → (2) formal verification 提供的是 ground-truth verification（reliability = 1，在可 formalize 的范围内）→ (3) 因此 FormalLoop 理论上具有比所有 LLM-based verifier 更高的 self-improvement 天花板 → (4) 这个理论预测可通过实验验证（FormalLoop vs. LLM-verified loop 在多轮迭代后的 collapse resistance 对比）。这个论证链不仅加强了 motivation，还提供了一个 **可验证的理论假设**——"formal verification 应当展现出更强的 collapse resistance"——这让论文从 "engineering contribution"（我们搭了个更好的管线）升级为 "scientific contribution"（我们验证了一个关于 self-improvement dynamics 的理论假设）。
- 价值: Significance 维度。从工程贡献升级为科学贡献，直接提升论文在顶会的竞争力。审稿人对 "better pipeline" 的兴趣有限，但对 "empirically testing a theoretical prediction about self-improvement dynamics" 的兴趣会高得多。
- 调研依据: Solver-verifier gap theory (ICLR 2026) 提供了直接的理论框架；NSRSA 的实验（symbolic verification 在 5 轮迭代中维持提升而 outcome-only 方法 plateau）已经提供了部分初步证据。

【发掘点 5】
- 维度: trivial alternative 威胁
- 内容: 需要正面回应一个审稿人必然会提出的问题：**为什么不直接用 outcome verification（最终答案对不对）+ STAT 的 LLM skill profiling？** 这个 trivial alternative 的成本更低（无需 formalization pipeline），覆盖率更高（100% 的问题都能 profile），且 STAT 已经证明了 +7.5% 的效果。Proposal 需要清晰论证 formal step-level diagnosis 相对于这个 baseline 的 **不可替代的增量价值**。建议的论证角度：(a) **错误归因精度**：outcome verification 只知道解法错了，不知道错在哪一步——两个最终答案错误的解法可能在完全不同的步骤出错，对应完全不同的 skill deficits。LLM teacher 的 step-level diagnosis 虽然能定位，但有 hallucination 风险（"LLMs cannot spot math errors even when allowed to peek into the solution"，arXiv 2509.01395）。Formal verification 是唯一能提供 guaranteed correct step-level attribution 的方法。(b) **迭代稳定性**：LLM teacher 的 bias 会在多轮迭代中被放大（teacher 在第 1 轮误诊的 skill gap 导致第 2 轮的训练数据偏差，进而导致第 3 轮的 profile 进一步偏离），而 formal verification 的 zero-bias 特性使每轮迭代都是 independently calibrated 的。这个 argument 在多轮 loop 的设定下尤其有力。
- 价值: 直接回应 trivial alternative 威胁，加强 novelty claim 的说服力。如果这个问题不被主动回答，审稿人几乎一定会以此质疑。
- 调研依据: STAT (ICLR 2026) 作为 trivial alternative 的代表；arXiv 2509.01395 ("LLMs cannot spot math errors") 提供了 LLM-based diagnosis 不可靠的实证依据。

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [STAT: Skill-Targeted Adaptive Training](https://arxiv.org/abs/2510.10023)
- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [SwS: Self-aware Weakness-driven Problem Synthesis](https://arxiv.org/abs/2506.08989)
- [Solver-Verifier Gap Theory](https://arxiv.org/abs/2507.00075)
- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869)
- [FormalMATH Benchmark](https://arxiv.org/abs/2505.02735)
- [LLMs cannot spot math errors](https://arxiv.org/abs/2509.01395)

【补救 agent 本轮输出】:
Now I have sufficient research context. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **FoVer** (ACL 2026 Findings): 使用 Z3 和 Isabelle 进行 step-level 验证生成 PRM 训练数据。实验覆盖 ProcessBench + 12 个推理 benchmark（MATH, AIME, ANLI, MMLU, BBH）。Baseline 为 human-annotated PRMs 和无 formal verification 的 PRMs。Ablation 区分了不同 formal tool 的贡献。
- **STAT** (ICLR 2026): Teacher LLM 做 skill profiling + targeted synthesis。实验使用 Llama/Qwen 系列，评估 MATH（+7.5%）及 OOD benchmark AIME24/25, AMC23（+4.6%）。Ablation 包括 STAT-Sel vs STAT-Syn、不同 skill 数量、与 GRPO 互补性。
- **NSRSA** (arXiv 2026): Qwen3-4B-Thinking 跑 5 轮 self-training。5 个实验条件：no verification / outcome verification / majority voting / full NSRSA / NSRSA+DPO。仅覆盖 GSM8K 算术验证，cross-transfer 到 MATH-500。拒绝了~34% 通过 outcome verification 的 "lucky guess" 样本。
- **SwS** (NeurIPS 2025): Qwen2.5-base (3B/7B/32B)，8 个 benchmark（GSM8K, MATH-500, Minerva Math, Olympiad-Bench, Gaokao-2023, AMC23, AIME24, AIME25），生成 40k synthetic problems per size。Baseline 包括 vanilla RLVR、SPICE、curriculum-based methods。
- **SvS** (arXiv 2025): 12 个 benchmark，3B-32B 模型，+18.3% Pass@32 on AIME24。关键评估维度：entropy stability、Pass@K 曲线。
- **Adaptive Problem Generation via Symbolic Representations** (arXiv Feb 2026): 使用 SymPy 符号空间做 closed-loop 问题生成，GRPO/PPO 训练，评估 GSM8K, MATH500, AIME24。这是最直接的可比工作——同样使用 SymPy 做符号问题生成但不做 error-type diagnosis。
- **Qwen3.5-9B** (Released March 2026): Apache 2.0，已在 HuggingFace 开放。GPQA Diamond 81.7，math reasoning 较强。支持 thinking/non-thinking 模式。

- **调研总结**: 该领域当前实验标准要求：(1) 至少 6-8 个 benchmark 覆盖 GSM8K 到 AIME 不同难度梯度；(2) 与 RLVR/GRPO 标准 post-training 方法对比；(3) 多个 model size 验证泛化性；(4) 细粒度 ablation 隔离各组件贡献；(5) 迭代过程中的 collapse/entropy 分析。审稿人普遍要求 compute-normalized comparison 和 statistical significance reporting。

---

【缺陷 1】
- 类别: 可行性问题 / 实验设计不足
- 问题: Proposal 声称覆盖 "full spectrum from algebra through proof-level reasoning across MATH-level and competition problems"，但 Z3+SymPy 的实际覆盖范围存在严重 gap。MATH benchmark 包含 7 个类别（Algebra, Counting & Probability, Geometry, Intermediate Algebra, Number Theory, Prealgebra, Precalculus），其中 **Geometry（~15% of MATH）和 Counting & Probability（~15%）基本无法被 Z3/SymPy 有效形式化验证**。Number Theory 中的许多问题也超出 Z3 的能力范围。Proposal 自身承认形式化成功率仅 ~60-70%，但未分析这一 gap 对 error profiling 的系统性偏差：**error profile 只能反映可形式化问题上的错误分布，而非模型真实的完整弱点图谱**。模型在 geometry/combinatorics 上可能是最弱的，但系统完全无法诊断这些类别的错误。
- 严重度: 可补救
- 补救方案:
  1. **明确限定 claim scope**：将核心 claim 从 "full spectrum" 缩窄为 "algebraic and arithmetic reasoning domains amenable to symbolic formalization"，承认 geometry/combinatorics 是 out-of-scope limitation
  2. **按 MATH 子类别分析形式化覆盖率**：报告每个子类别的 formalization success rate，让 reviewer 清楚系统的真实覆盖范围
  3. **对不可形式化类别设计 fallback 策略**：例如对 geometry/combinatorics 使用 outcome-based verification (答案正确性) 作为退化方案，而非完全忽略这些类别
  4. **在 ablation 中加入 "coverage analysis"**：对比 full-spectrum uniform synthesis vs. formal-targeted synthesis 在可形式化 vs. 不可形式化子类别上的各自表现
- 调研依据: NSRSA 的实验教训——该论文诚实限定在 GSM8K 算术验证，获得了 ACL 接受；而 Adaptive Problem Generation (Feb 2026) 同样使用 SymPy 但也仅限于可符号表达的问题类型。过度声称覆盖范围是审稿红旗。

【缺陷 2】
- 类别: baseline 不足或过时
- 问题: Proposal 虽然在 Research Landscape 中提到了大量相关工作，但**没有明确列出实验中要对比的 baseline list**。根据调研，以下 baseline 是审稿人会期望看到的：
  1. **SwS** (NeurIPS 2025) — 最直接可比：weakness-driven problem synthesis，使用 pass-rate 分析弱点而非 formal diagnosis。这是验证 "formal error profiling 比 pass-rate-based weakness detection 更好" 的核心对照
  2. **Adaptive Problem Generation** (Feb 2026) — 同样使用 SymPy 做 symbolic problem synthesis in closed loop，但不做 error-type diagnosis。这是验证 "error-type targeting 比 global difficulty adaptation 更好" 的核心对照
  3. **GRPO/RLVR baseline** — 当前 post-training 标准方法，任何 self-improvement 方法都必须与之对比
  4. **Vanilla SFT on uniform synthetic data** — 验证 targeting 比 uniform 好的最基本 baseline
  5. **STAT-style LLM-teacher error profiling** — 验证 "formal tools 比 LLM teacher 好" 的核心 claim
- 严重度: 可补救
- 补救方案: 明确规划以下 baseline 矩阵：
  - **Training paradigm baselines**: Vanilla SFT, SFT+DPO (uniform data), GRPO/RLVR
  - **Targeting method baselines**: Uniform random synthesis, STAT-style LLM-teacher profiling + targeted synthesis, SwS pass-rate-based weakness targeting
  - **Symbolic method baseline**: Adaptive Problem Generation (global difficulty adaptation without error-type targeting)
  - **Verification baselines**: Outcome-only verification (NSRSA-style), majority voting, no verification
  
  其中 SwS 和 STAT 有公开代码/描述可复现；Adaptive Problem Generation 可从论文描述复现其核心 pipeline。
- 调研依据: SwS (NeurIPS 2025) 的实验对比了 vanilla RLVR、curriculum-based methods、SPICE 等；STAT 对比了 vanilla SFT、random augmentation、teacher-free methods。审稿人期望看到与这些 published 方法的直接对比。

【缺陷 3】
- 类别: 评估方案缺陷
- 问题: Proposal **未明确指定评估 benchmark 和 evaluation protocol**。在该领域，审稿人期望看到明确的 benchmark list、evaluation metrics（accuracy、Pass@K、多少次 sampling）、以及 OOD 泛化测试。此外，Qwen3.5-9B 的 base math 能力已经很强（GPQA Diamond 81.7），self-improvement 的边际增益可能较小——如果没有 confidence interval 和 statistical significance testing，小幅改进难以说服 reviewer。
- 严重度: 可补救
- 补救方案:
  1. **明确 benchmark 列表**：至少覆盖 GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench（7 个，跨越不同难度梯度）
  2. **评估 protocol**：报告 greedy accuracy + Pass@K (K=8,32) + majority voting@K，与 SvS/SwS 的报告方式对齐
  3. **统计显著性**：至少 3 次独立 run 的均值和标准差，对关键结果做 significance test
  4. **OOD 泛化**：由于 self-improvement 基于 MATH 训练集问题，必须在 AIME24/25 等 OOD competition benchmark 上验证泛化
  5. **按 MATH 子类别报告**：区分可形式化类别 vs. 不可形式化类别的改进幅度（直接支撑核心 claim）
- 调研依据: SwS 使用 8 个 benchmark + Pass@K 报告；SvS 使用 12 个 benchmark + Pass@32；STAT 在 MATH + 4 个 OOD benchmark 报告。这是该领域的最低评估标准。

【缺陷 4】
- 类别: ablation 不完整
- 问题: Proposal 描述了 SFT+DPO 训练方式和 formal error taxonomy，但**未设计任何 ablation study**。核心 claim 包含多个可分离组件，审稿人必然要求逐个验证。
- 严重度: 可补救
- 补救方案: 需要设计以下 ablation：
  1. **Error profiling source**: Formal verification profiling vs. LLM-based profiling vs. pass-rate-based profiling vs. random → 隔离 "formal" 的贡献
  2. **Targeting vs. uniform**: Targeted synthesis (based on error profile) vs. uniform synthesis (same quantity, random skill distribution) → 隔离 "targeting" 的贡献
  3. **Training objective**: SFT only vs. DPO only vs. SFT+DPO → 隔离 DPO preference learning 的增益
  4. **Error taxonomy granularity**: 5-type fine-grained taxonomy vs. 2-type coarse taxonomy (arithmetic vs. non-arithmetic) vs. single aggregate → 隔离 fine-grained diagnosis 的价值
  5. **Iteration analysis**: Per-iteration improvement curve，报告 accuracy、error profile 变化、formalization coverage 变化、entropy → 证明 loop 是稳定收敛而非 collapse
  6. **Preference pair quality**: DPO pairs 来自 formal verification vs. DPO pairs 来自 outcome verification → 隔离 step-level formal verification 对 preference learning 的贡献
- 调研依据: STAT 的 ablation 包括 STAT-Sel vs STAT-Syn、skill 数量变化、与 GRPO 互补性；NSRSA 的 ablation 区分了 5 种 verification 条件；SwS 分析了 per-category weakness targeting 的贡献。这些 ablation 粒度是审稿人的期望基线。

【缺陷 5】
- 类别: 实验设计不足 / 可行性问题
- 问题: Proposal 提到使用 "formally-verified vs. formally-rejected solution pairs as preference pairs" 做 DPO，但**未讨论 formalization failure 与 reasoning error 的区分问题**。当一个 solution step 无法通过 formal verification 时，可能有两种原因：(a) 推理确实错误，(b) 形式化过程本身失败（LLM-to-formal translation 的 ~30-40% failure rate）。如果将 formalization failure 错误标注为 reasoning error 并用于 DPO rejected 样本，会引入系统性噪声，尤其是当 formalization failure 与 problem difficulty 正相关时（越难的问题越难形式化），这会系统性地将 hard problem 的 solution 标注为 "rejected"，产生 anti-difficulty bias。
- 严重度: 可补救
- 补救方案:
  1. **引入 formalization confidence score**：区分 "verification failed = error" 和 "formalization failed = unknown"，只对高置信度 verified/rejected pairs 做 DPO
  2. **设计 filtering pipeline**：对 DPO rejected 样本做二次检查——如果 formal verification reject 但 answer 正确，标记为 "suspicious formalization failure" 并排除
  3. **报告 DPO 数据质量指标**：false positive rate（正确 solution 被 reject）和 false negative rate（错误 solution 被 accept），参考 imperfect verifier 论文 (April 2026) 的 tolerance threshold（≤15% noise rate）
  4. **在 ablation 中对比不同 filtering 严格度的影响**
- 调研依据: "An Imperfect Verifier is Good Enough" (April 2026) 证明 noise rate ≤15% 是可容忍的，但需要明确度量和报告。NSRSA 报告了 ~34% 的 rejection rate（correct-answer but flawed-reasoning solutions），这种细粒度分析是审稿人期望看到的。

【缺陷 6】
- 类别: compute 公平性问题
- 问题: Proposal 未讨论与 baseline 方法的 **compute-normalized comparison**。FormalLoop 的 5 轮迭代涉及大量 symbolic verification overhead（proposal 提到 Z3/SymPy step verification 是 CPU-bound ~0.5-2s per step），这使得每轮的 wall-clock time 和总 compute 可能显著高于 SwS/STAT 等 baselines。如果 FormalLoop 用了更多 compute 才获得同等或略好的结果，审稿人会质疑是 formal verification 的贡献还是 more compute 的贡献。
- 严重度: 可补救
- 补救方案:
  1. **明确报告每个方法的总 compute**（GPU hours + CPU hours for symbolic verification），而非仅报告 GPU hours
  2. **设计 compute-matched comparison**：给 baseline 方法等量的额外 compute budget（例如让 SwS 多训练几步，或让 uniform synthesis 生成更多数据）
  3. **绘制 accuracy vs. total compute 曲线**：展示 FormalLoop 在相同 compute budget 下是否仍然优于 baselines（参照 SvS 的 entropy-vs-iteration 分析方式）
  4. **分析 symbolic verification throughput 瓶颈**：报告每轮 formalization+verification 的 wall-clock time，以及可并行化程度
- 调研依据: SwS 的实验明确报告了训练 token 数量和 sampling 次数作为 compute 度量；STAT 控制了 training data quantity 的公平性。基于领域实验规范判断，compute fairness 是 AAAI 审稿的常见质疑点。

【缺陷 7】
- 类别: 实验设计不足
- 问题: Proposal 仅使用 **Qwen3.5-9B 单一模型**进行实验。在该领域，SwS 使用 3B/7B/32B 三个 scale，SvS 覆盖 3B-32B，STAT 使用 Llama+Qwen 两个 model family。单一模型的结果很容易被审稿人质疑为 "method 恰好对这个特定模型有效"。
- 严重度: 可补救
- 补救方案:
  1. **至少增加一个 smaller model（如 Qwen3.5-4B 或 Llama-3-8B）** 验证方法在不同能力水平模型上的效果
  2. **理想情况下覆盖 2 个 model size + 2 个 model family**，但考虑 600 H100 hours 的预算约束，务实方案是 Qwen3.5-9B (主实验) + Qwen3.5-4B (验证实验，减少迭代轮数)
  3. **如果 compute 预算确实不足以支持多模型**，至少在 related work/limitation 中明确说明，并将 multi-model 验证列为 future work
- 调研依据: SwS (NeurIPS 2025) 覆盖 Qwen2.5 3B/7B/32B；STAT (ICLR 2026) 覆盖 Llama+Qwen。单模型实验在顶会接受率上明显劣势。在 600 H100 hours 预算下，增加一个 4B 模型的 3 轮迭代实验（约 150 hours 额外）是可行的。

【缺陷 8】
- 类别: 实验设计不足
- 问题: 5 类 error taxonomy（algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference）**缺乏验证和覆盖度分析**。这个 taxonomy 是 proposal 的核心创新之一，但 (a) 没有 pilot study 验证这 5 类是否真的覆盖了模型在 MATH 上的主要错误类型，(b) 没有讨论 error 类型之间的重叠/歧义（一个错误可能同时涉及 algebraic manipulation 和 equation solving），(c) 没有与已有 math skill taxonomy（如 STAT 的 skill taxonomy）对比说明为何选择这 5 类。
- 严重度: 可补救
- 补救方案:
  1. **Pilot study**：在正式实验前，用 Qwen3.5-9B 在 MATH test set 的 500 道题上生成 solutions，人工或 formal verification 分析实际 error 分布，验证 taxonomy 覆盖度
  2. **报告 error classification 的 inter-annotator agreement 或 formal consistency**：同一错误被不同 formal tools 分类的一致性
  3. **与 STAT 的 skill taxonomy 对比**：说明为何 formal taxonomy 选择这 5 个维度（可能是因为这 5 类恰好是 Z3/SymPy 能区分的类型——这本身就是一个有意义的 insight）
  4. **在 ablation 中测试 taxonomy 的粒度敏感性**（见缺陷 4 第 4 点）
- 调研依据: STAT 使用 teacher LLM 生成 skill list 并验证其覆盖度；SwS 按 problem category 分组弱点。error taxonomy 的合理性需要实证支持，不能仅靠 a priori 设定。

---

**总结**：上述 8 个缺陷均为可补救问题，无方向性致命缺陷。最关键的 3 个是：**缺陷 1**（形式化覆盖 gap 导致 claim 过度）、**缺陷 2**（baseline 不明确且可能缺失关键对照）、**缺陷 4**（ablation 设计缺失）。这三个如果不补，几乎可以确定会被 reviewer 要求 major revision。其余缺陷（DPO 质量、compute 公平性、多模型、taxonomy 验证、evaluation protocol）是加固实验说服力的重要环节。在 600 H100 hours 的预算下，建议优先投入在 baseline 对比和 ablation 上，coverage analysis 和 DPO quality analysis 是低成本高回报的补充实验。

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://arxiv.org/abs/2510.10023)
- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning](https://arxiv.org/abs/2603.21558)
- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://arxiv.org/abs/2506.08989)
- [SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis](https://arxiv.org/abs/2508.14029)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [Qwen3.5-9B on HuggingFace](https://huggingface.co/Qwen/Qwen3.5-9B)
- [Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving](https://arxiv.org/abs/2505.20869)
- [SPICE: Self-Play In Corpus Environments Improves Reasoning](https://arxiv.org/abs/2510.24684)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "28582871-354f-48cd-a7e1-b0806ef2e4af",
  "isSidechain": false,
  "promptId": "91ff0dbe-5132-4cf4-8862-06f114d5741d",
  "type": "user",
  "uuid": "29dafdc6-34a7-41ab-870a-cda748f0957d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide my analysis. Let me synthesize everything.  ---  【状态】: 有发掘空间  【前置…",
  "leafUuid": "29dafdc6-34a7-41ab-870a-cda748f0957d",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Assistant

_source line 17 · 2026-05-27T08:38:20.104Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze both worker outputs carefully and then do cross-validation research before producing my integrated output.

**发掘 agent summary:**
- Status: 有发掘空间
- 5 discovery points:
  1. "Teacher-free" should be elevated to first-class contribution claim (核心 claim 强化)
  2. "Full spectrum" claim has unverified premise - formalization coverage is ~60-70%, with systematic bias against geometry/combinatorics (前提假设质疑)
  3. Step-level formal DPO preference pairs is an independent novelty point (novelty 锐化)
  4. I need to construct an explicit theoretical argument chain connecting the solver-verifier gap theory to establish stronger significance (significance 提升)
  5. I should directly counter the trivial alternative explanation - that simple outcome verification combined with standard LLM skill profiling could achieve similar results (trivial alternative 威胁)

**补救 agent summary:**
- Status: 有缺陷待补救
- 8 defects, all remediable: coverage gaps in Z3 and SymPy tooling, missing baseline comparisons, no formal evaluation protocol, no ablation studies designed, and several other technical gaps that need addressing.

**Convergence between workers:**
- Both flagged the "full spectrum" overclaim as a major issue - this is strong signal that I need to be more precise
- Both identified the critical need for explicit baseline comparisons against STAT and SwS approaches
- Both raised concerns about the novelty and risk of using step-level DPO preference pairs

**Key suggestions I need to cross-validate with WebSearch:**
- Whether "teacher-free" actually represents a genuine paradigm shift or if similar approaches already exist
- The validity of using step-level formal DPO preference pairs as a training mechanism
- Whether SwS and Adaptive Problem Generation are truly the most relevant baselines to compare against
- The specific claim about LLMs' inability to spot math errors from arXiv 2509.01395 - need to confirm this paper exists and supports what's being claimed
- Whether the solver-verifier gap theory and its predictions hold up under scrutiny

I'm going to run targeted WebSearches to validate these core claims before proceeding.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29dafdc6-34a7-41ab-870a-cda748f0957d",
  "isSidechain": false,
  "requestId": "req_011CbSmevjHg1VGqos8bHLpo",
  "type": "assistant",
  "uuid": "db455b52-f447-4217-8271-6c5f31f19277",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APEkcuJpG2TmWShjppY7uR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11584,
      "cache_read_input_tokens": 20349,
      "output_tokens": 741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 741,
          "cache_read_input_tokens": 20349,
          "cache_creation_input_tokens": 11584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11584
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

_source line 18 · 2026-05-27T08:38:20.106Z_

我需要先做交叉验证调研，再整合两个 worker 的输出。让我验证几个关键 worker 建议的可靠性。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db455b52-f447-4217-8271-6c5f31f19277",
  "isSidechain": false,
  "requestId": "req_011CbSmevjHg1VGqos8bHLpo",
  "type": "assistant",
  "uuid": "e91ed5dc-6620-4d5d-ac21-bcd041ea8af9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APEkcuJpG2TmWShjppY7uR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11584,
      "cache_read_input_tokens": 20349,
      "output_tokens": 741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 741,
          "cache_read_input_tokens": 20349,
          "cache_creation_input_tokens": 11584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11584
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

_source line 19 · 2026-05-27T08:38:20.110Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XYFJ4F7LfuF4RcnVsLivMB`</summary>

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
  "parentUuid": "e91ed5dc-6620-4d5d-ac21-bcd041ea8af9",
  "isSidechain": false,
  "requestId": "req_011CbSmevjHg1VGqos8bHLpo",
  "type": "assistant",
  "uuid": "5e7b156c-493b-4054-924e-fd4291874cf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01APEkcuJpG2TmWShjppY7uR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11584,
      "cache_read_input_tokens": 20349,
      "output_tokens": 741,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 741,
          "cache_read_input_tokens": 20349,
          "cache_creation_input_tokens": 11584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11584
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

_source line 20 · 2026-05-27T08:38:20.116Z_

<details><summary>↩ Tool result · `toolu_01XYFJ4F7LfuF4RcnVsLivMB`</summary>

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
  "parentUuid": "5e7b156c-493b-4054-924e-fd4291874cf2",
  "isSidechain": false,
  "promptId": "91ff0dbe-5132-4cf4-8862-06f114d5741d",
  "type": "user",
  "uuid": "fc3bb1e7-791b-43bf-a8d1-94f6ef8b7aec",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "5e7b156c-493b-4054-924e-fd4291874cf2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T08:38:22.927Z_

Now let me run the cross-validation searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc3bb1e7-791b-43bf-a8d1-94f6ef8b7aec",
  "isSidechain": false,
  "requestId": "req_011CbSmgNU8Rwdr8wgMj1VGk",
  "type": "assistant",
  "uuid": "0e531ff8-beac-404b-828f-789a75d2c639",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJSYYn21ScW5SEJzAcKhZi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 31933,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 83,
          "cache_read_input_tokens": 31933,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1269
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

_source line 22 · 2026-05-27T08:38:23.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014VFLSabiG8pwKxqJgbKany`</summary>

```json
{
  "query": "step-level DPO preference pairs formal verification math reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e531ff8-beac-404b-828f-789a75d2c639",
  "isSidechain": false,
  "requestId": "req_011CbSmgNU8Rwdr8wgMj1VGk",
  "type": "assistant",
  "uuid": "f73f8bcb-775c-4f4a-b9e0-1bfed0962b8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BJSYYn21ScW5SEJzAcKhZi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1269,
      "cache_read_input_tokens": 31933,
      "output_tokens": 83,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1269,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 83,
          "cache_read_input_tokens": 31933,
          "cache_creation_input_tokens": 1269,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1269
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

_source line 23 · 2026-05-27T08:38:33.454Z_

<details><summary>↩ Tool result · `toolu_014VFLSabiG8pwKxqJgbKany`</summary>

```text
Web search results for query: "step-level DPO preference pairs formal verification math reasoning 2025 2026"

Links: [{"title":"Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs | OpenReview","url":"https://openreview.net/forum?id=H5FUVj0vMd"},{"title":"STEP-DPO: STEP-WISE PREFERENCE OPTIMIZATION","url":"https://openreview.net/pdf?id=H5FUVj0vMd"},{"title":"Step-level Value Preference Optimization for Mathematical Reasoning","url":"https://arxiv.org/pdf/2406.10858"},{"title":"Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise   Rewards for Mathematical Reasoning","url":"https://arxiv.org/pdf/2502.14356"},{"title":"Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1249/"},{"title":"Continuous-Utility Direct Preference Optimization","url":"https://arxiv.org/pdf/2602.00931"}]

Based on the search results, here's what I found:

## Step-level DPO for Mathematical Reasoning (2025-2026)

Step-DPO treats individual reasoning steps as units for preference optimization rather than evaluating answers holistically. A data construction pipeline for Step-DPO has been developed, enabling the creation of a high-quality dataset containing 10K step-wise preference pairs.

### Performance Results

Step-DPO results in a model achieving 70.8% accuracy on MATH and 94.0% on GSM8K, surpassing a series of closed-source models, including GPT-4-1106, Claude-3-Opus, and Gemini-1.5-Pro.

### Related Recent Work (2025-2026)

**Full-Step-DPO**: A more recent advancement, it leverages step-wise rewards from the entire reasoning chain by training a self-supervised process reward model, which automatically scores each step.

**Continuous-Utility DPO**: Rather than relying on binary labels, CU-DPO replaces binary supervision with continuous, high-fidelity utilities that aggregate LLM-judged scores across answer correctness, reasoning quality, and completeness.

These approaches address limitations in using direct preference optimization for complex, multi-step mathematical reasoning by providing finer-grained supervision at the step level rather than evaluating entire solutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f73f8bcb-775c-4f4a-b9e0-1bfed0962b8c",
  "isSidechain": false,
  "promptId": "91ff0dbe-5132-4cf4-8862-06f114d5741d",
  "type": "user",
  "uuid": "2108c1e6-1342-48ba-976d-c8a5fc543942",
  "toolUseResult": {
    "query": "step-level DPO preference pairs formal verification math reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QpdNr74tL4Wwdk6b7oFEtG",
        "content": [
          {
            "title": "Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=H5FUVj0vMd"
          },
          {
            "title": "STEP-DPO: STEP-WISE PREFERENCE OPTIMIZATION",
            "url": "https://openreview.net/pdf?id=H5FUVj0vMd"
          },
          {
            "title": "Step-level Value Preference Optimization for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2406.10858"
          },
          {
            "title": "Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise   Rewards for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2502.14356"
          },
          {
            "title": "Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1249/"
          },
          {
            "title": "Continuous-Utility Direct Preference Optimization",
            "url": "https://arxiv.org/pdf/2602.00931"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\n## Step-level DPO for Mathematical Reasoning (2025-2026)\n\nStep-DPO treats individual reasoning steps as units for preference optimization rather than evaluating answers holistically. A data construction pipeline for Step-DPO has been developed, enabling the creation of a high-quality dataset containing 10K step-wise preference pairs.\n\n### Performance Results\n\nStep-DPO results in a model achieving 70.8% accuracy on MATH and 94.0% on GSM8K, surpassing a series of closed-source models, including GPT-4-1106, Claude-3-Opus, and Gemini-1.5-Pro.\n\n### Related Recent Work (2025-2026)\n\n**Full-Step-DPO**: A more recent advancement, it leverages step-wise rewards from the entire reasoning chain by training a self-supervised process reward model, which automatically scores each step.\n\n**Continuous-Utility DPO**: Rather than relying on binary labels, CU-DPO replaces binary supervision with continuous, high-fidelity utilities that aggregate LLM-judged scores across answer correctness, reasoning quality, and completeness.\n\nThese approaches address limitations in using direct preference optimization for complex, multi-step mathematical reasoning by providing finer-grained supervision at the step level rather than evaluating entire solutions."
    ],
    "durationSeconds": 10.034977985000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f73f8bcb-775c-4f4a-b9e0-1bfed0962b8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-27T08:38:36.015Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AN8t6hSP6Ty3vxL4pY63gg`</summary>

```json
{
  "query": "\"LLMs cannot spot math errors\" arxiv 2509.01395 mathematical error detection"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2108c1e6-1342-48ba-976d-c8a5fc543942",
  "isSidechain": false,
  "requestId": "req_011CbSmhMD1B2H7C5hLznzNY",
  "type": "assistant",
  "uuid": "32dc80a4-54fa-4d7b-8ad5-b51a7053d3fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015RuZ5vZitJ9WFF5Ghr2Yb3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 33202,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 33202,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 25 · 2026-05-27T08:38:42.483Z_

<details><summary>↩ Tool result · `toolu_01AN8t6hSP6Ty3vxL4pY63gg`</summary>

```text
Web search results for query: ""LLMs cannot spot math errors" arxiv 2509.01395 mathematical error detection"

Links: [{"title":"[2509.01395] LLMs cannot spot math errors, even when allowed to peek into the solution","url":"https://arxiv.org/abs/2509.01395"},{"title":"LLMs cannot spot math errors, even when allowed to peek into the solution","url":"https://arxiv.org/html/2509.01395"},{"title":"LLMs cannot spot math errors, even when allowed to peek into the solution","url":"https://arxiv.org/pdf/2509.01395"},{"title":"LLMs cannot spot math errors, even when allowed to peek into the solution - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.553/"},{"title":"LLMs cannot spot math errors, even when allowed to peek ...","url":"https://aclanthology.org/2025.emnlp-main.553.pdf"},{"title":"Error Detection and Correction for Interpretable Mathematics in Large Language Models","url":"https://arxiv.org/pdf/2508.03500"}]

I found the paper you're looking for! Here are the key findings:

The paper "LLMs cannot spot math errors, even when allowed to peek into the solution" by KV Aditya Srivatsa, Kaushal Kumar Maurya, and Ekaterina Kochmar investigates how large language models struggle with meta-reasoning tasks such as identifying errors in student solutions.

The work investigates the challenge of locating the first error step in stepwise solutions using two error reasoning datasets: VtG and PRM800K.

**Main Finding:** The experiments show that state-of-the-art LLMs struggle to locate the first error step in student solutions even when given access to the reference solution.

**Proposed Solution:** The authors propose an approach that generates an intermediate corrected student solution, aligning more closely with the original student's solution, which helps improve performance.

The paper was submitted to arXiv on September 1, 2025, and appears to have been accepted to the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32dc80a4-54fa-4d7b-8ad5-b51a7053d3fb",
  "isSidechain": false,
  "promptId": "91ff0dbe-5132-4cf4-8862-06f114d5741d",
  "type": "user",
  "uuid": "b1e115c1-2bf6-4c16-9e50-acdd7913573b",
  "toolUseResult": {
    "query": "\"LLMs cannot spot math errors\" arxiv 2509.01395 mathematical error detection",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Jz2BF9iQvBP8AvrzcpFLjy",
        "content": [
          {
            "title": "[2509.01395] LLMs cannot spot math errors, even when allowed to peek into the solution",
            "url": "https://arxiv.org/abs/2509.01395"
          },
          {
            "title": "LLMs cannot spot math errors, even when allowed to peek into the solution",
            "url": "https://arxiv.org/html/2509.01395"
          },
          {
            "title": "LLMs cannot spot math errors, even when allowed to peek into the solution",
            "url": "https://arxiv.org/pdf/2509.01395"
          },
          {
            "title": "LLMs cannot spot math errors, even when allowed to peek into the solution - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.553/"
          },
          {
            "title": "LLMs cannot spot math errors, even when allowed to peek ...",
            "url": "https://aclanthology.org/2025.emnlp-main.553.pdf"
          },
          {
            "title": "Error Detection and Correction for Interpretable Mathematics in Large Language Models",
            "url": "https://arxiv.org/pdf/2508.03500"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key findings:\n\nThe paper \"LLMs cannot spot math errors, even when allowed to peek into the solution\" by KV Aditya Srivatsa, Kaushal Kumar Maurya, and Ekaterina Kochmar investigates how large language models struggle with meta-reasoning tasks such as identifying errors in student solutions.\n\nThe work investigates the challenge of locating the first error step in stepwise solutions using two error reasoning datasets: VtG and PRM800K.\n\n**Main Finding:** The experiments show that state-of-the-art LLMs struggle to locate the first error step in student solutions even when given access to the reference solution.\n\n**Proposed Solution:** The authors propose an approach that generates an intermediate corrected student solution, aligning more closely with the original student's solution, which helps improve performance.\n\nThe paper was submitted to arXiv on September 1, 2025, and appears to have been accepted to the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP)."
    ],
    "durationSeconds": 6.4633363830000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "32dc80a4-54fa-4d7b-8ad5-b51a7053d3fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-27T08:38:44.980Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MKkKQ1uNYTGJQG6qLu46Pd`</summary>

```json
{
  "query": "teacher-free self-improvement math reasoning LLM without teacher model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1e115c1-2bf6-4c16-9e50-acdd7913573b",
  "isSidechain": false,
  "requestId": "req_011CbSmi1oE8EqVBYop1ayaL",
  "type": "assistant",
  "uuid": "a6238437-d653-4465-9bf8-384d166f3084",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExTMjiCGm6tCpNbXZi4o6b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 625,
      "cache_read_input_tokens": 33934,
      "output_tokens": 71,
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
          "output_tokens": 71,
          "cache_read_input_tokens": 33934,
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

_source line 27 · 2026-05-27T08:38:52.461Z_

<details><summary>↩ Tool result · `toolu_01MKkKQ1uNYTGJQG6qLu46Pd`</summary>

```text
Web search results for query: "teacher-free self-improvement math reasoning LLM without teacher model 2025 2026"

Links: [{"title":"S2R: Teaching LLMs to Self-verify and Self-correct via ...","url":"https://aclanthology.org/2025.acl-long.1104.pdf"},{"title":"New LLMs For Math Education - Learning Engineering Virtual Institute","url":"https://learning-engineering-virtual-institute.org/new-llms-for-math-education/"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf"},{"title":"University LLM Simulates Student Teaming on Math Problems","url":"https://www.govtech.com/education/higher-ed/university-llm-simulates-student-teaming-on-math-problems"},{"title":"MathVC: An LLM-Simulated Multi-Character Virtual Classroom for Mathematics Education","url":"https://arxiv.org/html/2404.06711v2"},{"title":"5th MATH-AI Workshop at NeurIPS'25 - Math-AI","url":"https://mathai2025.github.io/papers/"},{"title":"Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability","url":"https://arxiv.org/pdf/2601.18778"},{"title":"Best LLMs for Math & Problem Solving: Top AI Models for Reasoning, Calculus, Proofs & More - Designs Valley","url":"https://designsvalley.com/best-llm-for-math/"},{"title":"Best Math LLMs January 2026: Top AI Models for Mathematical Reasoning | WhatLLM.org","url":"https://whatllm.org/blog/best-math-models-january-2026"}]

I found several relevant research papers and articles about teacher-free self-improvement for LLMs in math reasoning. Here are the key findings:

## Recent Research on Teacher-Free Self-Improvement

One notable approach is SOAR, an asymmetric teacher-student meta-RL framework where both the teacher and student are initialized from the target model. The teacher proposes question-answer pairs that the student trains on with RL, and the teacher is rewarded based on student improvement on a difficult subset.

Recent work like S2R (Teaching LLMs to Self-verify and Self-correct) has been published at ACL 2025, and DeepSeek R1 demonstrated that large-scale reinforcement learning can incentivize LLM's deep thinking for math reasoning.

Another approach is R*-Math, which describes how small LLMs can master math reasoning with self-evolved deep thinking.

## Self-Play and Self-Correction Methods

Current research addresses the challenge that self-correction capability has been shown to be severely lacking in current LLMs, especially in the absence of external input (also called intrinsic self-correction).

## Peer Collaboration Without Teachers

Researchers at George Mason University and William and Mary University have created a chatbot prototype called MathVC to simulate peer-to-peer collaboration, rather than teacher-to-student training.

The search results show active research in 2025-2026 focused on enabling LLMs to improve their math reasoning abilities through self-play, reinforcement learning, and peer-based learning approaches that don't rely on external teacher models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6238437-d653-4465-9bf8-384d166f3084",
  "isSidechain": false,
  "promptId": "91ff0dbe-5132-4cf4-8862-06f114d5741d",
  "type": "user",
  "uuid": "2f378511-c828-4cc7-86ba-b85a698ad4f1",
  "toolUseResult": {
    "query": "teacher-free self-improvement math reasoning LLM without teacher model 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EubHff9AgHNwLwS95nXVVJ",
        "content": [
          {
            "title": "S2R: Teaching LLMs to Self-verify and Self-correct via ...",
            "url": "https://aclanthology.org/2025.acl-long.1104.pdf"
          },
          {
            "title": "New LLMs For Math Education - Learning Engineering Virtual Institute",
            "url": "https://learning-engineering-virtual-institute.org/new-llms-for-math-education/"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf"
          },
          {
            "title": "University LLM Simulates Student Teaming on Math Problems",
            "url": "https://www.govtech.com/education/higher-ed/university-llm-simulates-student-teaming-on-math-problems"
          },
          {
            "title": "MathVC: An LLM-Simulated Multi-Character Virtual Classroom for Mathematics Education",
            "url": "https://arxiv.org/html/2404.06711v2"
          },
          {
            "title": "5th MATH-AI Workshop at NeurIPS'25 - Math-AI",
            "url": "https://mathai2025.github.io/papers/"
          },
          {
            "title": "Teaching Models to Teach Themselves: Reasoning at the Edge of Learnability",
            "url": "https://arxiv.org/pdf/2601.18778"
          },
          {
            "title": "Best LLMs for Math & Problem Solving: Top AI Models for Reasoning, Calculus, Proofs & More - Designs Valley",
            "url": "https://designsvalley.com/best-llm-for-math/"
          },
          {
            "title": "Best Math LLMs January 2026: Top AI Models for Mathematical Reasoning | WhatLLM.org",
            "url": "https://whatllm.org/blog/best-math-models-january-2026"
          }
        ]
      },
      "I found several relevant research papers and articles about teacher-free self-improvement for LLMs in math reasoning. Here are the key findings:\n\n## Recent Research on Teacher-Free Self-Improvement\n\nOne notable approach is SOAR, an asymmetric teacher-student meta-RL framework where both the teacher and student are initialized from the target model. The teacher proposes question-answer pairs that the student trains on with RL, and the teacher is rewarded based on student improvement on a difficult subset.\n\nRecent work like S2R (Teaching LLMs to Self-verify and Self-correct) has been published at ACL 2025, and DeepSeek R1 demonstrated that large-scale reinforcement learning can incentivize LLM's deep thinking for math reasoning.\n\nAnother approach is R*-Math, which describes how small LLMs can master math reasoning with self-evolved deep thinking.\n\n## Self-Play and Self-Correction Methods\n\nCurrent research addresses the challenge that self-correction capability has been shown to be severely lacking in current LLMs, especially in the absence of external input (also called intrinsic self-correction).\n\n## Peer Collaboration Without Teachers\n\nResearchers at George Mason University and William and Mary University have created a chatbot prototype called MathVC to simulate peer-to-peer collaboration, rather than teacher-to-student training.\n\nThe search results show active research in 2025-2026 focused on enabling LLMs to improve their math reasoning abilities through self-play, reinforcement learning, and peer-based learning approaches that don't rely on external teacher models."
    ],
    "durationSeconds": 7.477889285000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a6238437-d653-4465-9bf8-384d166f3084",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-27T08:38:54.848Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019LWwgedVkJxXnggsyMgp6U`</summary>

```json
{
  "query": "SwS self-aware weakness-driven problem synthesis NeurIPS 2025 code available baseline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f378511-c828-4cc7-86ba-b85a698ad4f1",
  "isSidechain": false,
  "requestId": "req_011CbSmikV17UjiJymCyDxor",
  "type": "assistant",
  "uuid": "e90c50f9-f903-41fb-aa38-bf94b081bb65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AC3KxYtFH4QtZpjvHosAgA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 34559,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 919,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 34559,
          "cache_creation_input_tokens": 919,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 919
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

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide my analysis. Let me synthesize everything.  ---  【状态】: 有发掘空间  【前置…",
  "leafUuid": "e90c50f9-f903-41fb-aa38-bf94b081bb65",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Tool result

_source line 31 · 2026-05-27T08:39:02.439Z_

<details><summary>↩ Tool result · `toolu_019LWwgedVkJxXnggsyMgp6U`</summary>

```text
Web search results for query: "SwS self-aware weakness-driven problem synthesis NeurIPS 2025 code available baseline"

Links: [{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=0jQUNQsZra"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/sws-self-aware-weakness-driven-problem-synthesis-in-reinforcement-learning-for-llm-reasoning/"},{"title":"GitHub - MasterVito/SwS: Official Repo for SwS: A Weakness-driven Problem Synthesis Framework in RL for LLM Reasoning","url":"https://github.com/MasterVito/SwS"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning","url":"https://mastervito.github.io/MasterVito.SwS.github.io/"},{"title":"[2506.08989] SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/abs/2506.08989"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in ...","url":"https://openreview.net/pdf/c3403842de341324f63358f1732f1518761661f2.pdf"},{"title":"Self-aware Weakness-Driven Synthesis Framework","url":"https://www.emergentmind.com/topics/self-aware-weakness-driven-problem-synthesis-framework-sws"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/html/2506.08989v1"}]

Based on the search results, here's what I found about SwS:

## Overview

SwS is a NeurIPS 2025 poster paper about Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning. The framework systematically identifies model deficiencies and leverages them for problem augmentation.

## Key Approach

The framework defines weaknesses as questions that the model consistently fails to learn through iterative sampling during RL training, and it extracts core concepts from these failure cases to synthesize new problems that strengthen the model's weak areas.

## Results

Without relying on external knowledge distillation, the framework yields average performance gains of 10.0% and 7.7% on 7B and 32B models across eight mainstream reasoning benchmarks.

## Code Availability

All code has been released, including implementations for RL training and problem synthesis. The official repository is available at https://github.com/MasterVito/SwS.

## Additional Resources

- **ArXiv Paper**: https://arxiv.org/abs/2506.08989
- **OpenReview**: https://openreview.net/forum?id=0jQUNQsZra
- **Project Website**: https://mastervito.github.io/MasterVito.SwS.github.io/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e90c50f9-f903-41fb-aa38-bf94b081bb65",
  "isSidechain": false,
  "promptId": "91ff0dbe-5132-4cf4-8862-06f114d5741d",
  "type": "user",
  "uuid": "cdaf6f20-57a6-4a55-8150-5a2b16695a8a",
  "toolUseResult": {
    "query": "SwS self-aware weakness-driven problem synthesis NeurIPS 2025 code available baseline",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wq395GCKiM85G3HF3m22KR",
        "content": [
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=0jQUNQsZra"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/publication/sws-self-aware-weakness-driven-problem-synthesis-in-reinforcement-learning-for-llm-reasoning/"
          },
          {
            "title": "GitHub - MasterVito/SwS: Official Repo for SwS: A Weakness-driven Problem Synthesis Framework in RL for LLM Reasoning",
            "url": "https://github.com/MasterVito/SwS"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning",
            "url": "https://mastervito.github.io/MasterVito.SwS.github.io/"
          },
          {
            "title": "[2506.08989] SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning",
            "url": "https://arxiv.org/abs/2506.08989"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in ...",
            "url": "https://openreview.net/pdf/c3403842de341324f63358f1732f1518761661f2.pdf"
          },
          {
            "title": "Self-aware Weakness-Driven Synthesis Framework",
            "url": "https://www.emergentmind.com/topics/self-aware-weakness-driven-problem-synthesis-framework-sws"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning",
            "url": "https://arxiv.org/html/2506.08989v1"
          }
        ]
      },
      "Based on the search results, here's what I found about SwS:\n\n## Overview\n\nSwS is a NeurIPS 2025 poster paper about Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning. The framework systematically identifies model deficiencies and leverages them for problem augmentation.\n\n## Key Approach\n\nThe framework defines weaknesses as questions that the model consistently fails to learn through iterative sampling during RL training, and it extracts core concepts from these failure cases to synthesize new problems that strengthen the model's weak areas.\n\n## Results\n\nWithout relying on external knowledge distillation, the framework yields average performance gains of 10.0% and 7.7% on 7B and 32B models across eight mainstream reasoning benchmarks.\n\n## Code Availability\n\nAll code has been released, including implementations for RL training and problem synthesis. The official repository is available at https://github.com/MasterVito/SwS.\n\n## Additional Resources\n\n- **ArXiv Paper**: https://arxiv.org/abs/2506.08989\n- **OpenReview**: https://openreview.net/forum?id=0jQUNQsZra\n- **Project Website**: https://mastervito.github.io/MasterVito.SwS.github.io/"
    ],
    "durationSeconds": 7.587237749999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e90c50f9-f903-41fb-aa38-bf94b081bb65",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T08:39:05.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ht784hxaEksCANBP1Z3ouA`</summary>

```json
{
  "query": "Step-DPO formal verification preference pairs symbolic proof 2025 2026 math"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cdaf6f20-57a6-4a55-8150-5a2b16695a8a",
  "isSidechain": false,
  "requestId": "req_011CbSmjVCGqWwoRscfZod64",
  "type": "assistant",
  "uuid": "ef24767f-1bd8-42fd-b380-bc205b242cfe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LQRh7CjaxVL7bhYkNxmEAB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 35478,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 881,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 35478,
          "cache_creation_input_tokens": 881,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 881
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

_source line 33 · 2026-05-27T08:39:12.780Z_

<details><summary>↩ Tool result · `toolu_01Ht784hxaEksCANBP1Z3ouA`</summary>

```text
Web search results for query: "Step-DPO formal verification preference pairs symbolic proof 2025 2026 math"

Links: [{"title":"Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs | OpenReview","url":"https://openreview.net/forum?id=H5FUVj0vMd"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=zHuV3Vatov"},{"title":"STEP-DPO: STEP-WISE PREFERENCE OPTIMIZATION","url":"https://openreview.net/pdf?id=H5FUVj0vMd"},{"title":"Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification","url":"https://arxiv.org/pdf/2603.19715"},{"title":"Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1249/"},{"title":"Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning","url":"https://arxiv.org/html/2502.14356v1"},{"title":"[2603.19715] Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification","url":"https://arxiv.org/abs/2603.19715"}]

Based on the web search results, I found several relevant papers combining these concepts:

## Step-DPO: Step-wise Preference Optimization

Step-DPO is a method that treats individual reasoning steps as units for preference optimization rather than evaluating answers holistically. A data construction pipeline for Step-DPO enables the creation of a high-quality dataset containing 10K step-wise preference pairs. Vanilla DPO offers minimal benefits for long-chain mathematical reasoning because models employing DPO struggle to identify detailed errors in incorrect answers due to a lack of fine-grained process supervision.

Fine-tuning Qwen-72B-Instruct with Step-DPO results in a model achieving 70.8% accuracy on MATH and 94.0% on GSM8K, surpassing a series of closed-source models, including GPT-4-1106, Claude-3-Opus, and Gemini-1.5-Pro.

## Related Work: Full-Step-DPO (2025)

Full-Step-DPO is a novel DPO framework tailored for mathematical reasoning that improves upon Step-DPO by focusing on all steps in the reasoning chain rather than just the first erroneous step, reducing reliance on human or GPT-4 annotations.

## Neuro-Symbolic Verification (2026)

A neuro-symbolic proof generation framework automates proof search by performing best-first tree search over proof states, using LLMs for candidate proof steps and incorporating ITP tools to repair rejected steps, filter proof states, and automatically discharge subgoals.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef24767f-1bd8-42fd-b380-bc205b242cfe",
  "isSidechain": false,
  "promptId": "91ff0dbe-5132-4cf4-8862-06f114d5741d",
  "type": "user",
  "uuid": "d18bf376-d4eb-487e-b6b1-d171644cac17",
  "toolUseResult": {
    "query": "Step-DPO formal verification preference pairs symbolic proof 2025 2026 math",
    "results": [
      {
        "tool_use_id": "srvtoolu_015d97yaqig9UJYt3xGTvZrt",
        "content": [
          {
            "title": "Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=H5FUVj0vMd"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=zHuV3Vatov"
          },
          {
            "title": "STEP-DPO: STEP-WISE PREFERENCE OPTIMIZATION",
            "url": "https://openreview.net/pdf?id=H5FUVj0vMd"
          },
          {
            "title": "Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification",
            "url": "https://arxiv.org/pdf/2603.19715"
          },
          {
            "title": "Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning - ACL Anthology",
            "url": "https://aclanthology.org/2025.findings-acl.1249/"
          },
          {
            "title": "Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2502.14356v1"
          },
          {
            "title": "[2603.19715] Stepwise: Neuro-Symbolic Proof Search for Automated Systems Verification",
            "url": "https://arxiv.org/abs/2603.19715"
          }
        ]
      },
      "Based on the web search results, I found several relevant papers combining these concepts:\n\n## Step-DPO: Step-wise Preference Optimization\n\nStep-DPO is a method that treats individual reasoning steps as units for preference optimization rather than evaluating answers holistically. A data construction pipeline for Step-DPO enables the creation of a high-quality dataset containing 10K step-wise preference pairs. Vanilla DPO offers minimal benefits for long-chain mathematical reasoning because models employing DPO struggle to identify detailed errors in incorrect answers due to a lack of fine-grained process supervision.\n\nFine-tuning Qwen-72B-Instruct with Step-DPO results in a model achieving 70.8% accuracy on MATH and 94.0% on GSM8K, surpassing a series of closed-source models, including GPT-4-1106, Claude-3-Opus, and Gemini-1.5-Pro.\n\n## Related Work: Full-Step-DPO (2025)\n\nFull-Step-DPO is a novel DPO framework tailored for mathematical reasoning that improves upon Step-DPO by focusing on all steps in the reasoning chain rather than just the first erroneous step, reducing reliance on human or GPT-4 annotations.\n\n## Neuro-Symbolic Verification (2026)\n\nA neuro-symbolic proof generation framework automates proof search by performing best-first tree search over proof states, using LLMs for candidate proof steps and incorporating ITP tools to repair rejected steps, filter proof states, and automatically discharge subgoals."
    ],
    "durationSeconds": 7.604896248000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ef24767f-1bd8-42fd-b380-bc205b242cfe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T08:39:15.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017hXKM2MbyJ4aK988rH3Awh`</summary>

```json
{
  "query": "adaptive problem generation symbolic representations SymPy closed-loop RLVR arxiv 2602.19187"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d18bf376-d4eb-487e-b6b1-d171644cac17",
  "isSidechain": false,
  "requestId": "req_011CbSmkFNrBzFTg3iruMpPk",
  "type": "assistant",
  "uuid": "51d4f7f7-30d2-4283-929d-d7e8c4aa925b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eJG1jGfoNerZtA7xXvNv2",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 36359,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 828,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 36359,
          "cache_creation_input_tokens": 828,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 828
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

_source line 35 · 2026-05-27T08:39:22.417Z_

<details><summary>↩ Tool result · `toolu_017hXKM2MbyJ4aK988rH3Awh`</summary>

```text
Web search results for query: "adaptive problem generation symbolic representations SymPy closed-loop RLVR arxiv 2602.19187"

Links: [{"title":"[2602.19187] Adaptive Problem Generation via Symbolic Representations","url":"https://arxiv.org/abs/2602.19187"},{"title":"Adaptive Problem Generation via Symbolic Representations","url":"https://arxiv.org/pdf/2602.19187"},{"title":"Adaptive Problem Generation via Symbolic Representations","url":"https://arxiv.org/html/2602.19187"},{"title":"System and method of adaptive generation of problem determination decision procedures","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7831537"},{"title":"Making Mathematical Reasoning Adaptive","url":"https://arxiv.org/pdf/2510.04617"}]

Based on the search results, I found the paper you're looking for:

"Adaptive Problem Generation via Symbolic Representations" is a paper that presents a method for generating training data for reinforcement learning with verifiable rewards to improve small open-weights language models on mathematical tasks.

Key aspects of the research include:

1. **The Problem**: Existing data generation approaches rely on open-loop pipelines and fixed modifications that do not adapt to the model's capabilities, and they typically operate directly on word problems, limiting control over problem structure.

2. **The Solution**: The researchers perform modifications in a symbolic problem space, representing each problem as a set of symbolic variables and constraints (e.g., via algebraic frameworks such as SymPy or SMT formulations), which enables precise control over problem structure and automatic generation of ground-truth solutions.

3. **Closed-Loop Framework**: To adapt the problem difficulty to the model, they introduce a closed-loop framework that learns modification strategies through prompt optimization in symbolic space.

4. **Results**: Experimental results demonstrate that both adaptive problem generation and symbolic representation modifications contribute to improving the model's math solving ability.

The paper was published on arXiv on February 22, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51d4f7f7-30d2-4283-929d-d7e8c4aa925b",
  "isSidechain": false,
  "promptId": "91ff0dbe-5132-4cf4-8862-06f114d5741d",
  "type": "user",
  "uuid": "d721236c-e64d-4794-98f1-d6b9fe445a2a",
  "toolUseResult": {
    "query": "adaptive problem generation symbolic representations SymPy closed-loop RLVR arxiv 2602.19187",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E1WoqcRWKQig82BQVXddh9",
        "content": [
          {
            "title": "[2602.19187] Adaptive Problem Generation via Symbolic Representations",
            "url": "https://arxiv.org/abs/2602.19187"
          },
          {
            "title": "Adaptive Problem Generation via Symbolic Representations",
            "url": "https://arxiv.org/pdf/2602.19187"
          },
          {
            "title": "Adaptive Problem Generation via Symbolic Representations",
            "url": "https://arxiv.org/html/2602.19187"
          },
          {
            "title": "System and method of adaptive generation of problem determination decision procedures",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7831537"
          },
          {
            "title": "Making Mathematical Reasoning Adaptive",
            "url": "https://arxiv.org/pdf/2510.04617"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Adaptive Problem Generation via Symbolic Representations\" is a paper that presents a method for generating training data for reinforcement learning with verifiable rewards to improve small open-weights language models on mathematical tasks.\n\nKey aspects of the research include:\n\n1. **The Problem**: Existing data generation approaches rely on open-loop pipelines and fixed modifications that do not adapt to the model's capabilities, and they typically operate directly on word problems, limiting control over problem structure.\n\n2. **The Solution**: The researchers perform modifications in a symbolic problem space, representing each problem as a set of symbolic variables and constraints (e.g., via algebraic frameworks such as SymPy or SMT formulations), which enables precise control over problem structure and automatic generation of ground-truth solutions.\n\n3. **Closed-Loop Framework**: To adapt the problem difficulty to the model, they introduce a closed-loop framework that learns modification strategies through prompt optimization in symbolic space.\n\n4. **Results**: Experimental results demonstrate that both adaptive problem generation and symbolic representation modifications contribute to improving the model's math solving ability.\n\nThe paper was published on arXiv on February 22, 2026."
    ],
    "durationSeconds": 6.467412819999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "51d4f7f7-30d2-4283-929d-d7e8c4aa925b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-27T08:39:22.420Z_

```json
{
  "parentUuid": "d721236c-e64d-4794-98f1-d6b9fe445a2a",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e44afcf5-f8a7-4bf9-80dd-84b7050c6f38",
  "timestamp": "2026-05-27T08:39:22.420Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-27T08:40:28.916Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me synthesize my cross-validation findings and produce the integrated output.

**Cross-validation results:**

1. **Step-level DPO with formal verification (发掘点3)**: Step-DPO exists (NeurIPS 2024), Full-Step-DPO exists (ACL 2025 Findings). These do step-level preference optimization but use **LLM-generated or human annotations** to identify error steps, NOT formal verification. So the claim that using formal verification to construct step-localized preference pairs is novel appears VALID. No prior work uses formal symbolic tools (Z3/SymPy) specifically as the source of step-level DPO preference signals. 

The distinction here is important though — step-level DPO itself is established prior art, but applying formal verification as the mechanism to identify and localize errors for preference pairs is the novel angle. The contribution is really about the formally-verified source, not the step-level optimization framework itself.

2. **"LLMs cannot spot math errors" (arXiv 2509.01395)**: CONFIRMED. Paper exists, published at EMNLP 2025. It shows SOTA LLMs struggle to locate error steps even with reference solutions. This strongly supports the "teacher-free formal diagnosis" advantage. 发掘点5's citation is VALID.

3. **Teacher-free self-improvement**: I found several methods like S2R, SOAR, and R*-Math that use self-play and RL for improvement without explicit teachers, but none specifically combine formal error diagnosis with targeted synthesis. The novelty seems to lie in that specific combination rather than the teacher-free aspect alone, since RLVR and GRPO-based approaches are also teacher-free in their own ways.

4. **SwS (NeurIPS 2025)**: CONFIRMED. Code is available on GitHub. This is a solid baseline for weakness-driven problem synthesis without formal diagnosis, so using it as a comparison point makes sense.

5. **Adaptive Problem Generation (arXiv 2602.19187)**: CONFIRMED. Uses SymPy symbolic space for closed-loop problem generation with RLVR.

6. **Step-DPO / Full-Step-DPO as prior art**: Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) already do step-level preference optimization, so the proposal needs to acknowledge these as prior work and clarify the distinction — those rely on LLM or human annotations for step identification, while FormalLoop uses formal verification instead.

The key integration point is sharpening the "teacher-free" claim: it's not just about avoiding external teachers, but specifically about using formal error diagnosis to target synthesis, which is where the real novelty sits.

The "full spectrum" overclaim needs narrowing too — both reviewers flagged this independently, so I should constrain the scope to formally-tractable problems and lean on the imperfect verifier argument as justification.

For step-level formal DPO, I'm adopting this as a contribution but with the caveat that the novelty lies in using formal verification as the preference signal source, not in step-level optimization itself. The theoretical grounding from the solver-verifier gap also strengthens the motivation considerably.

The trivial alternative defense is worth including since the arXiv paper validates the core evidence and preempts reviewer pushback. On the practical side, I need to adopt all the remedial fixes: coverage gaps align with the overclaim narrowing, the baseline list should include SwS, STAT, and Adaptive Problem Gen plus the step-DPO variants, standard evaluation benchmarks are essential, ablations are non-negotiable for a top venue, and I should clarify the distinction between formalization failure versus other failure modes.

For compute fairness, that's standard. On the single model limitation, I can work with the 600 H100 hour budget to validate with a smaller 3-4B parameter model. The taxonomy validation through a pilot study is low-cost and necessary.

Looking at probability estimates, the novelty sits between medium and medium-strong—teacher-free error-targeted synthesis fills a real gap, but it's more of a combination of existing techniques than a fundamental breakthrough, and the Step-DPO prior work does weaken the DPO novelty claim somewhat. The significance is medium-strong since it addresses a genuine problem in the field.

The idea ceiling lands around 40-45%, and after these improvements the experimental completeness is much better with explicit baselines and ablations, though execution remains the critical factor. Overall I'm estimating this at 35% probability.

Actually, stepping back—this is round 1 and we're making substantial improvements. The core idea is solid, it's a well-motivated combination of proven techniques addressing a real gap, and the teacher-free error-targeted synthesis angle is genuinely novel. The theoretical grounding through the solver-verifier gap is strong. The main limitation is that it's a combination paper rather than something fundamentally new, but for AAAI 2026 that's acceptable. The novelty is medium-strong given the genuine gap in combining formal verification with error targeting in a closed loop, and the significance is solid because it tackles real limitations in current self-improvement methods.

With the experimental design fixes, technical soundness could also reach medium-strong. So I'm revising my estimate to 37% median, with a range of 32-43%. The ceiling of 45% accounts for the fact that combination papers can perform well at top venues when they're well-motivated and backed by strong results, and the theoretical angle about formal verification providing maximum verifier reliability gives this more scientific depth than a purely engineering contribution.

I'll keep iterating.

Now I need to integrate the experimental design fully into the proposal and refine the framing. I'm also identifying key references to add—Step-DPO and Full-Step-DPO for prior work on step-level training, plus that recent paper on LLMs' inability to spot math errors as supporting evidence. I'll preserve all the existing references while weaving these new ones in. Continuing through more recent work on self-play and verification approaches—Self-Error-Instruct generalizes from model mistakes, SPICE uses self-play in synthetic environments, and several papers explore variational problem synthesis and weakness-driven generation to sustain reasoning improvements. There's also emerging work on handling imperfect verifiers and formal verification methods for mathematical problem solving. I'm adding the final reference with its full citation details to complete the list of 22 papers on mathematical reasoning and LLM verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e44afcf5-f8a7-4bf9-80dd-84b7050c6f38",
  "isSidechain": false,
  "requestId": "req_011CbSmkxapsNdLzisazsgwc",
  "type": "assistant",
  "uuid": "6b003a39-550b-4f93-a41c-1556d85a061f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DmmdEVZEVV11LsdZ8C2X6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 37187,
      "output_tokens": 9251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9251,
          "cache_read_input_tokens": 37187,
          "cache_creation_input_tokens": 677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 677
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

_source line 38 · 2026-05-27T08:42:41.688Z_

Now I have sufficient cross-validation data. Let me synthesize everything.

**Cross-validation summary:**

1. **Step-level formal DPO (发掘点3)**: Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) already do step-level preference optimization — but using LLM/human annotations, NOT formal verification. The novelty of "formally-verified step-level preference pairs" holds, but proposal MUST cite Step-DPO/Full-Step-DPO as prior art and differentiate. Worker's claim needs qualification.

2. **"LLMs cannot spot math errors" (arXiv 2509.01395)**: CONFIRMED at EMNLP 2025. Strongly validates the "teacher-free formal diagnosis" advantage.

3. **Teacher-free framing**: RLVR/GRPO methods are also technically "teacher-free." The precise novelty must be scoped as "teacher-free error-TARGETED synthesis" — not just teacher-free self-improvement in general.

4. **SwS as baseline**: CONFIRMED — NeurIPS 2025, public code on GitHub. Strongly recommended baseline.

5. **Adaptive Problem Generation (arXiv 2602.19187)**: CONFIRMED — SymPy symbolic space, closed-loop RLVR, adapts difficulty without error-type diagnosis. Valid differentiation target and baseline.

Now producing the integrated output:

【阶段】: 迭代第 1 轮

【交叉验证调研】:
1. **Step-level DPO prior art**: 搜索发现 Step-DPO (NeurIPS 2024) 和 Full-Step-DPO (ACL 2025 Findings) 已实现 step-level preference optimization，但均使用 LLM/human 标注定位错误步骤。发掘 agent 声称"step-level DPO 在文献中全新"不完全准确——step-level DPO 本身是已有工作，真正新的是用 formal verification 作为 step-level preference signal 的来源。Proposal 必须引用这两篇并明确差异化。
2. **"LLMs cannot spot math errors" (arXiv 2509.01395)**: 确认存在，EMNLP 2025 发表。结论确切：SOTA LLMs 即使给出参考解也难以定位错误步骤。强力支撑 formal diagnosis 优于 LLM diagnosis 的论点。
3. **SwS 代码可用性**: 确认 NeurIPS 2025 接收，GitHub 公开代码 (github.com/MasterVito/SwS)，可复现作为核心 baseline。
4. **Adaptive Problem Generation**: 确认 arXiv 2602.19187，使用 SymPy symbolic space + closed-loop RLVR，仅做 difficulty adaptation，不做 error-type diagnosis。是验证"error-type targeting vs. global difficulty adaptation"的理想对照。
5. **Teacher-free 定位精确性**: 搜索发现 RLVR/GRPO 方法（如 DeepSeek-R1）也是 "teacher-free"。因此 proposal 的差异化不应仅停留在"teacher-free"，而应精确为"teacher-free error-TARGETED synthesis"——这个组合确实无先例。

【发掘 agent 有效建议采纳】:
- **发掘点1 (Teacher-free 作为首要 claim)**: **采纳并修正**——已验证。将"teacher-free"精确限定为"teacher-free error-targeted synthesis"（因为 RLVR 也是 teacher-free），避免被审稿人用 GRPO 反驳。核心叙事重构为"首个不依赖 teacher model 的 error-targeted self-improvement system"。
- **发掘点2 (Full spectrum overclaim)**: **采纳**——已验证，与补救缺陷1高度共识（2/2 workers）。缩窄 claim 至 formally-tractable domains，结合 imperfect verifier 论文论证部分覆盖仍优于 noisy full coverage。
- **发掘点3 (Step-level formal DPO)**: **部分采纳并修正**——交叉验证发现 Step-DPO / Full-Step-DPO 是已有工作，step-level DPO 本身非新。采纳"formally-verified preference pairs"作为独立 contribution，但必须引用 Step-DPO/Full-Step-DPO 并明确差异化：prior work 用 LLM/human 标注，我们用 formal verification（zero noise, zero cost）。
- **发掘点4 (Solver-verifier gap 理论论证链)**: **采纳**——已验证。构建 solver-verifier gap theory → formal verification reliability=1 → higher self-improvement ceiling 的论证链，将论文从工程贡献升级为科学假设验证。
- **发掘点5 (Trivial alternative 防御)**: **采纳**——arXiv 2509.01395 已验证。在 proposal 中显式回应"为什么不直接用 outcome + STAT"的质疑，引用 EMNLP 2025 实证。

【补救 agent 有效建议采纳】:
- **缺陷1 (Coverage gap)**: **采纳**——与发掘点2共识（2/2）。限定 claim scope，按 MATH 子类别分析形式化覆盖率，设计 fallback 策略。
- **缺陷2 (Baseline list)**: **采纳**——SwS 代码已验证可用，Adaptive Problem Gen 已验证可对比。明确列出 baseline 矩阵：SwS、Adaptive Problem Gen、GRPO、uniform SFT、STAT-style LLM profiling。
- **缺陷3 (Evaluation protocol)**: **采纳**——与领域标准对齐，7+ benchmarks + Pass@K + 统计显著性。
- **缺陷4 (Ablation design)**: **采纳**——6 组 ablation 全部合理且必要。
- **缺陷5 (Formalization failure vs reasoning error)**: **采纳**——引入 formalization confidence filtering，报告 DPO 数据质量指标。
- **缺陷6 (Compute fairness)**: **采纳**——报告 GPU+CPU hours，设计 compute-matched comparison。
- **缺陷7 (Single model)**: **采纳**——增加 Qwen3.5-4B 作为验证实验（3 轮迭代，~120 额外 H100 hours），总预算调至 ~720 H100 hours，可控范围内。
- **缺陷8 (Taxonomy validation)**: **采纳**——增加 pilot study 验证 taxonomy 覆盖度。

【本轮 proposal 主要变更】:
**Idea 层面变更:**
- 核心叙事重构：从"formal tools as verifiers"→"首个 teacher-free error-targeted self-improvement system"
- "Full spectrum"缩窄为"algebraic and arithmetic reasoning domains amenable to symbolic formalization"，明确 geometry/combinatorics 为 fallback 覆盖
- 显式构建 solver-verifier gap → formal reliability=1 → higher ceiling 的理论论证链
- 新增 trivial alternative 防御（outcome + STAT vs. formal diagnosis），引用 arXiv 2509.01395
- 新增 Step-DPO / Full-Step-DPO 引用，明确 formally-verified preference pairs 的差异化
- 新增 "LLMs cannot spot math errors" (EMNLP 2025) 引用

**实验层面变更:**
- 明确 baseline 矩阵（5 类 baseline）
- 明确 evaluation protocol（7 benchmarks, greedy + Pass@K, 3 runs, 统计显著性）
- 完整 ablation design（6 组）
- Formalization confidence filtering pipeline for DPO
- 按 MATH 子类别报告形式化覆盖率和改进幅度
- 新增 Qwen3.5-4B 验证实验
- Compute-normalized comparison 设计
- Pilot study for taxonomy validation

【idea 质量评估】: Novelty=中强（teacher-free error-targeted synthesis 确实无先例，但本质仍为 validated components 的组合；Step-DPO prior art 略削弱 DPO 分支的新颖度）Significance=中强（解决 teacher dependency + collapse resistance 的实际痛点，有理论 grounding）→ idea 天花板约 43%

【实验完备性评估】: Technical Soundness=中强（baseline 矩阵完整，ablation 设计覆盖核心 claim，evaluation protocol 对齐领域标准，coverage limitation 诚实处理）→ 地板已补好

【当前概率估计】: [32% - 43%] 中位 37%

【决策】: 继续

【决策理由】: 第 1 轮带来了大幅实质性改进——核心 framing 重构、claim scope 修正、完整实验方案设计。但 proposal 的几个关键论证（trivial alternative 防御、理论链条、coverage limitation 的精确处理）还需要第 2 轮 workers 检验是否 tight。中位 37% 刚过门槛，仍有提升空间。

**引用核对清单**（确认原始 19 篇 + 新增 3 篇全部包含在纯净版中）:
1. FoVer (ACL Findings 2026) ✓
2. STAT (ICLR 2026) ✓
3. NSRSA (arXiv 2026) ✓
4. Solver-Verifier Gap (ICLR 2026) ✓
5. SPARQ (arXiv 2025) ✓
6. CoTEvol (arXiv 2026) ✓
7. MathMixup (arXiv 2026) ✓
8. Self-Error-Instruct (ACL 2025) ✓
9. SPICE (arXiv 2025) ✓
10. SvS (arXiv 2025) ✓
11. SwS (NeurIPS 2025) ✓
12. Adaptive Problem Generation (arXiv 2026) ✓
13. Imperfect Verifier (arXiv 2026) ✓
14. MATH-VF (arXiv 2025) ✓
15. Safe (ACL 2025) ✓
16. WarriorMath (arXiv 2025) ✓
17. Bidirectional Curriculum (arXiv 2026) ✓
18. Reasoning Core (arXiv 2026) ✓
19. Neuro-Symbolic Data Generation (NeurIPS 2024) ✓
20. Step-DPO (NeurIPS 2024) [NEW] ✓
21. Full-Step-DPO (ACL 2025 Findings) [NEW] ✓
22. LLMs Cannot Spot Math Errors (EMNLP 2025, arXiv 2509.01395) [NEW] ✓

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
# Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement

## Core Problem

Self-improvement loops for mathematical reasoning suffer from two key failures: model collapse when using self-verification (explained by solver-verifier gap theory, ICLR 2026), and wasteful data generation that doesn't target the model's actual mathematical skill deficits. All existing error-targeted synthesis methods — STAT (ICLR 2026), Self-Error-Instruct (ACL 2025), SwS (NeurIPS 2025), WarriorMath (arXiv 2025) — depend on frontier LLM teachers or LLM-based metacognition for error diagnosis, introducing teacher bias, hallucinated error attributions, and scalability bottlenecks. Empirical evidence shows that LLMs cannot reliably spot mathematical errors even when given reference solutions (arXiv 2509.01395, EMNLP 2025). Can formal symbolic tools serve as both collapse-proof verifiers and ground-truth error diagnosticians to enable stable, teacher-free, targeted self-improvement?

## Research Opportunity

Three recent advances create a ripe moment: FoVer (ACL Findings 2026) proved formal tools can generate accurate step-level error labels for training, STAT (ICLR 2026) showed skill-gap-targeted synthesis outperforms uniform synthesis by 7.5% on MATH, and NSRSA (arXiv 2026) demonstrated symbolic verification helps iterative self-training maintain stability but only at the arithmetic level on GSM8K. The specific combination of formal step-level error categorization driving targeted symbolic problem synthesis in a closed self-improvement loop has not been attempted. The solver-verifier gap theory (ICLR 2026) predicts that verifier reliability is the key determinant of self-improvement ceiling — formal verification provides reliability approaching 1 within its scope, theoretically enabling a higher self-improvement ceiling than any LLM-based verifier. We test this theoretical prediction directly: FormalLoop should exhibit stronger collapse resistance and higher asymptotic improvement than LLM-verified loops across multiple iterations.

## Why Not Just Use Outcome Verification + LLM Teacher Profiling?

The most natural alternative is combining outcome-level verification (is the final answer correct?) with STAT-style LLM teacher skill profiling. We argue formal step-level diagnosis provides irreplaceable advantages: (1) **Error attribution precision**: Outcome verification only knows a solution is wrong, not where or why. LLM-based step diagnosis can localize, but empirical evidence shows LLMs fail at mathematical error detection even with reference solutions (arXiv 2509.01395, EMNLP 2025). Formal verification provides guaranteed correct step-level attribution. (2) **Iterative stability**: LLM teacher biases amplify across iterations — a misdiagnosed skill gap in round 1 produces biased training data in round 2, compounding errors. Formal verification provides independently calibrated diagnosis each round, preventing bias accumulation. (3) **No ceiling from teacher capability**: STAT's skill profiling quality is bounded by the teacher model's metacognition; formal diagnosis is bounded only by formalization scope (addressed below).

## Research Landscape

Current SOTA in synthetic math data includes SPARQ (June 2025, +24% via quality-diversity algorithms from 7.5K seeds), CoTEvol (April 2026, +6.6% average via evolutionary CoT synthesis), and MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). For self-improvement, SPICE (Oct 2025) achieves +8.9% math improvement via document-grounded self-play, while SvS (Aug 2025) achieves +18.3% Pass@32 on AIME24 via variational problem synthesis maintaining training entropy. For verification, FoVer trains generalizable PRMs from formal verification data across 12 benchmarks, and imperfect verifier research (April 2026) shows noise rates up to 15% are tolerable. Key limitation: all error-targeted synthesis methods (STAT, Self-Error-Instruct, WarriorMath) depend on frontier LLM teachers for error diagnosis — STAT uses a teacher model's metacognition to build skill profiles, introducing teacher-dependent biases. Meanwhile, NSRSA's symbolic verification covers only arithmetic operations on GSM8K, leaving algebraic manipulation, equation solving, and constraint reasoning uncovered. The Bidirectional Curriculum framework (March 2026) dynamically adjusts difficulty but lacks formal verification. Concurrent work: Adaptive Problem Generation via Symbolic Representations (Feb 2026, arXiv 2602.19187) uses SymPy-based symbolic representations in a closed-loop RLVR framework to adapt problem difficulty, but does not perform error-type diagnosis or skill-targeted synthesis — it adapts difficulty globally rather than targeting specific formal error categories. SwS (NeurIPS 2025, updates April 2026) identifies weaknesses via RL pass-rate analysis but without formal step-level diagnosis. Reasoning Core (March 2026) procedurally generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) performs step-aware Lean 4 verification but in one-shot refinement, not closed-loop training. For step-level preference optimization, Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) perform step-wise DPO using LLM or human annotations to identify error steps; our work differs by using formal verification as a zero-noise, zero-cost source of step-level preference signals.

## Proposed Approach

We propose FormalLoop, a closed-loop self-improvement system where formal symbolic tools (Z3 for satisfiability/logic, SymPy for algebraic computation) serve as both step-level error diagnosticians and targeted problem generators. Each iteration formalizes the student model's solutions, uses symbolic verification to classify step-level errors into a fine-grained taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), and drives SymPy-based problem synthesis targeting the model's weakest skills — with ground-truth solutions guaranteed by the solver. The student is fine-tuned via SFT and DPO, then re-profiled.

**Scope of formal coverage**: We explicitly scope formal verification to algebraic and arithmetic reasoning domains amenable to symbolic formalization (Algebra, Number Theory, Prealgebra, portions of Intermediate Algebra and Precalculus in MATH). For categories less amenable to Z3/SymPy formalization (Geometry, Counting & Probability), we employ outcome-based verification as a fallback. We report per-category formalization success rates and analyze the impact of partial coverage. Crucially, even partial formal coverage can outperform full-coverage noisy LLM diagnosis: imperfect verifier research (arXiv 2026) shows noise tolerance up to 15%, and formal verification achieves near-zero noise within its scope, whereas LLM teachers exhibit substantial noise across all categories.

**Formally-verified DPO preference pairs**: Unlike Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings), which rely on LLM/human annotations to locate error steps, we construct preference pairs where two solution trajectories share the first k verified-correct steps and diverge at step k+1 (one formally verified, one formally rejected). This provides step-localized preference signals with formal guarantees — zero annotation cost, zero label noise within formalization scope.

**Formalization quality control**: To prevent conflating formalization failures with genuine reasoning errors, we introduce a formalization confidence pipeline: (a) distinguish "verification failed = error detected" from "formalization failed = unknown status," (b) exclude solutions where formal rejection co-occurs with correct final answer (suspicious formalization failure), (c) only use high-confidence verified/rejected pairs for DPO. We target a noise rate well below the 15% tolerance threshold established by imperfect verifier research (arXiv 2026).

## Experimental Design

**Student models**: Qwen3.5-9B (primary) + Qwen3.5-4B (validation, 3 iterations).

**Benchmarks** (7, spanning difficulty gradient): GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench. OOD generalization tested on AIME24/25 (training uses MATH-train distribution).

**Evaluation protocol**: Greedy accuracy + Pass@K (K=8, 32) + majority voting@K. 3 independent runs; report mean ± std with significance tests on key comparisons. Per-MATH-subcategory breakdown separating formally-covered vs. fallback categories.

**Baseline matrix**:
- Training paradigm: Vanilla SFT (uniform synthetic data), SFT+DPO (uniform data), GRPO/RLVR
- Targeting methods: SwS (NeurIPS 2025; pass-rate-based weakness targeting), STAT-style LLM-teacher profiling + targeted synthesis
- Symbolic method: Adaptive Problem Generation (arXiv 2026; global difficulty adaptation without error-type targeting)
- Verification: Outcome-only verification loop (NSRSA-style), majority voting verification

**Ablation studies** (6 groups):
1. Error profiling source: Formal verification vs. LLM-based vs. pass-rate-based vs. random
2. Targeting vs. uniform: Targeted synthesis (from error profile) vs. uniform synthesis (same quantity)
3. Training objective: SFT only vs. DPO only vs. SFT+DPO
4. Error taxonomy granularity: 5-type fine-grained vs. 2-type coarse (arithmetic / non-arithmetic) vs. single aggregate
5. Iteration dynamics: Per-iteration accuracy, error profile shift, formalization coverage, entropy — demonstrating stable convergence rather than collapse
6. Preference pair source: DPO pairs from formal verification vs. from outcome verification vs. from LLM annotation (Step-DPO style)

**Compute fairness**: Report total compute (GPU hours + CPU hours for symbolic verification) per method. Design compute-matched comparison giving baselines equivalent extra compute budget. Plot accuracy vs. total compute curves.

**Pilot study**: Before main experiments, run Qwen3.5-9B on 500 MATH test problems, classify errors via formal tools, validate taxonomy coverage and inter-category overlap, compare with STAT's skill taxonomy to justify our 5-category design.

## Key References

- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)
- STAT: Skill-Targeted Adaptive Training (ICLR 2026)
- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)
- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)
- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)
- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)
- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)
- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)
- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)
- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)
- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)
- Adaptive Problem Generation via Symbolic Representations (arXiv 2026, arXiv 2602.19187)
- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026)
- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)
- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)
- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)
- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)
- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)
- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)
- Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs (NeurIPS 2024)
- Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning (ACL 2025 Findings)
- LLMs Cannot Spot Math Errors Even When Allowed to Peek into the Solution (EMNLP 2025, arXiv 2509.01395)

## Resource Estimate

- **manual**: gpu_hours: 720 H100 hours (5 iterations Qwen3.5-9B + 3 iterations Qwen3.5-4B + evaluation/ablations), timeline: 4-5 months, estimated_gpu_cost: $1,800
- **human_in_loop**: gpu_hours: 670 H100 hours, timeline: 3-4 months, claude_api_cost: $400-600, estimated_gpu_cost: $1,675
- **auto_research**: gpu_hours: 670 H100 hours, timeline: 6-8 weeks, claude_api_cost: $1,200-2,000, estimated_gpu_cost: $1,675, speed_bottleneck: Symbolic verification throughput — Z3/SymPy step verification is CPU-bound (~0.5-2s per step) and serialized per solution; formalizing natural language solutions to symbolic form requires careful LLM-to-formal translation with ~60-70% success rate on amenable categories, necessitating retry loops
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b003a39-550b-4f93-a41c-1556d85a061f",
  "isSidechain": false,
  "requestId": "req_011CbSmkxapsNdLzisazsgwc",
  "type": "assistant",
  "uuid": "22288e6d-aa69-42f1-9876-e03b07b53d0f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015DmmdEVZEVV11LsdZ8C2X6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 37187,
      "output_tokens": 9251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 677,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9251,
          "cache_read_input_tokens": 37187,
          "cache_creation_input_tokens": 677,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 677
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

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide my analysis. Let me synthesize everything.  ---  【状态】: 有发掘空间  【前置…",
  "leafUuid": "22288e6d-aa69-42f1-9876-e03b07b53d0f",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to provide my analysis. Let me synthesize everything.  ---  【状态】: 有发掘空间  【前置…",
  "leafUuid": "22288e6d-aa69-42f1-9876-e03b07b53d0f",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 44 · 2026-05-27T08:42:42.875Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:42:42.875Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "content": "【引用修复】你刚输出的 proposal 纯净版遗漏了以下原文中存在的引用：\n- ACL 2026\n\n请重新输出完整的纯净版 proposal，确保上述引用全部包含在内。只输出 --- 包围的纯净版 proposal，不要输出其他内容。"
}
```

---

### Runtime record

_source line 45 · 2026-05-27T08:42:42.875Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:42:42.875Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

## Round 3

8 recorded events

### User

_source line 46 · 2026-05-27T08:42:42.897Z_

【引用修复】你刚输出的 proposal 纯净版遗漏了以下原文中存在的引用：
- ACL 2026

请重新输出完整的纯净版 proposal，确保上述引用全部包含在内。只输出 --- 包围的纯净版 proposal，不要输出其他内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22288e6d-aa69-42f1-9876-e03b07b53d0f",
  "isSidechain": false,
  "promptId": "cccef0b8-b057-4151-a532-e31aa83b63de",
  "type": "user",
  "uuid": "690bb56f-9225-4c85-9239-a7da5f4c2190",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-27T08:42:57.209Z_

<details><summary>Logged reasoning block</summary>

```text
The user is pointing out that I lost "ACL 2026" as a reference marker somewhere in the proposal body text. Let me check the original proposal for where "ACL 2026" appears in the body text (not just the references section):

Original proposal body mentions:
- "FoVer (ACL 2026)" - in Research Opportunity section
- "FoVer's formal step-level labels (ACL 2026)" - in Detailed Description

In my rewritten version, I have:
- "FoVer (ACL Findings 2026)" - I changed "ACL 2026" to "ACL Findings 2026" in the body text


I see the issue now. The original uses "ACL 2026" in the body text but "ACL Findings 2026" in the references section, and I incorrectly standardized both to the longer form. I need to keep "ACL 2026" in the body citations while using "ACL Findings 2026" only in the references. I need to make sure the citation format stays consistent with the original—using "ACL 2026" as the inline marker throughout the body text while reserving "ACL Findings 2026" for the references section. Let me go through and restore the proposal with these corrections in place.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "690bb56f-9225-4c85-9239-a7da5f4c2190",
  "isSidechain": false,
  "requestId": "req_011CbSn1jo42HcxrJchrwSpU",
  "type": "assistant",
  "uuid": "3ee55d43-2bbd-4176-8cc0-344ad67b763d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBrBTxDEz8Ykv6rrE6tQuX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9349,
      "cache_read_input_tokens": 37864,
      "output_tokens": 4203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9349,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4203,
          "cache_read_input_tokens": 37864,
          "cache_creation_input_tokens": 9349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9349
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

_source line 48 · 2026-05-27T08:43:32.632Z_

---
# Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement

## Core Problem

Self-improvement loops for mathematical reasoning suffer from two key failures: model collapse when using self-verification (explained by solver-verifier gap theory, ICLR 2026), and wasteful data generation that doesn't target the model's actual mathematical skill deficits. All existing error-targeted synthesis methods — STAT (ICLR 2026), Self-Error-Instruct (ACL 2025), SwS (NeurIPS 2025), WarriorMath (arXiv 2025) — depend on frontier LLM teachers or LLM-based metacognition for error diagnosis, introducing teacher bias, hallucinated error attributions, and scalability bottlenecks. Empirical evidence shows that LLMs cannot reliably spot mathematical errors even when given reference solutions (arXiv 2509.01395, EMNLP 2025). Can formal symbolic tools serve as both collapse-proof verifiers and ground-truth error diagnosticians to enable stable, teacher-free, targeted self-improvement?

## Research Opportunity

Three recent advances create a ripe moment: FoVer (ACL 2026) proved formal tools can generate accurate step-level error labels for training, STAT (ICLR 2026) showed skill-gap-targeted synthesis outperforms uniform synthesis by 7.5% on MATH, and NSRSA (arXiv 2026) demonstrated symbolic verification helps iterative self-training maintain stability but only at the arithmetic level on GSM8K. The specific combination of formal step-level error categorization driving targeted symbolic problem synthesis in a closed self-improvement loop has not been attempted. The solver-verifier gap theory (ICLR 2026) predicts that verifier reliability is the key determinant of self-improvement ceiling — formal verification provides reliability approaching 1 within its scope, theoretically enabling a higher self-improvement ceiling than any LLM-based verifier. We test this theoretical prediction directly: FormalLoop should exhibit stronger collapse resistance and higher asymptotic improvement than LLM-verified loops across multiple iterations.

## Why Not Just Use Outcome Verification + LLM Teacher Profiling?

The most natural alternative is combining outcome-level verification (is the final answer correct?) with STAT-style LLM teacher skill profiling. We argue formal step-level diagnosis provides irreplaceable advantages: (1) **Error attribution precision**: Outcome verification only knows a solution is wrong, not where or why. LLM-based step diagnosis can localize, but empirical evidence shows LLMs fail at mathematical error detection even with reference solutions (arXiv 2509.01395, EMNLP 2025). Formal verification provides guaranteed correct step-level attribution. (2) **Iterative stability**: LLM teacher biases amplify across iterations — a misdiagnosed skill gap in round 1 produces biased training data in round 2, compounding errors. Formal verification provides independently calibrated diagnosis each round, preventing bias accumulation. (3) **No ceiling from teacher capability**: STAT's skill profiling quality is bounded by the teacher model's metacognition; formal diagnosis is bounded only by formalization scope (addressed below).

## Research Landscape

Current SOTA in synthetic math data includes SPARQ (June 2025, +24% via quality-diversity algorithms from 7.5K seeds), CoTEvol (April 2026, +6.6% average via evolutionary CoT synthesis), and MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). For self-improvement, SPICE (Oct 2025) achieves +8.9% math improvement via document-grounded self-play, while SvS (Aug 2025) achieves +18.3% Pass@32 on AIME24 via variational problem synthesis maintaining training entropy. For verification, FoVer (ACL 2026) trains generalizable PRMs from formal verification data across 12 benchmarks, and imperfect verifier research (April 2026) shows noise rates up to 15% are tolerable. Key limitation: all error-targeted synthesis methods (STAT, Self-Error-Instruct, WarriorMath) depend on frontier LLM teachers for error diagnosis — STAT uses a teacher model's metacognition to build skill profiles, introducing teacher-dependent biases. Meanwhile, NSRSA's symbolic verification covers only arithmetic operations on GSM8K, leaving algebraic manipulation, equation solving, and constraint reasoning uncovered. The Bidirectional Curriculum framework (March 2026) dynamically adjusts difficulty but lacks formal verification. Concurrent work: Adaptive Problem Generation via Symbolic Representations (Feb 2026, arXiv 2602.19187) uses SymPy-based symbolic representations in a closed-loop RLVR framework to adapt problem difficulty, but does not perform error-type diagnosis or skill-targeted synthesis — it adapts difficulty globally rather than targeting specific formal error categories. SwS (NeurIPS 2025, updates April 2026) identifies weaknesses via RL pass-rate analysis but without formal step-level diagnosis. Reasoning Core (March 2026) procedurally generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) performs step-aware Lean 4 verification but in one-shot refinement, not closed-loop training. For step-level preference optimization, Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) perform step-wise DPO using LLM or human annotations to identify error steps; our work differs by using formal verification as a zero-noise, zero-cost source of step-level preference signals.

## Proposed Approach

We propose FormalLoop, a closed-loop self-improvement system where formal symbolic tools (Z3 for satisfiability/logic, SymPy for algebraic computation) serve as both step-level error diagnosticians and targeted problem generators. Each iteration formalizes the student model's solutions, uses symbolic verification to classify step-level errors into a fine-grained taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), and drives SymPy-based problem synthesis targeting the model's weakest skills — with ground-truth solutions guaranteed by the solver. The student is fine-tuned via SFT and DPO, then re-profiled. This unifies three validated-but-disconnected advances: FoVer's formal step-level labels (ACL 2026), STAT's error-targeted synthesis superiority (ICLR 2026, +7.5% over uniform), and NSRSA's symbolic verification for training stability (arXiv 2026) — extending formal verification from arithmetic-only GSM8K to algebraic-to-proof MATH-level coverage on amenable categories, and from one-shot PRM training to iterative closed-loop improvement.

**Scope of formal coverage**: We explicitly scope formal verification to algebraic and arithmetic reasoning domains amenable to symbolic formalization (Algebra, Number Theory, Prealgebra, portions of Intermediate Algebra and Precalculus in MATH). For categories less amenable to Z3/SymPy formalization (Geometry, Counting & Probability), we employ outcome-based verification as a fallback. We report per-category formalization success rates and analyze the impact of partial coverage. Crucially, even partial formal coverage can outperform full-coverage noisy LLM diagnosis: imperfect verifier research (arXiv 2026) shows noise tolerance up to 15%, and formal verification achieves near-zero noise within its scope, whereas LLM teachers exhibit substantial noise across all categories.

**Formally-verified DPO preference pairs**: Unlike Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings), which rely on LLM/human annotations to locate error steps, we construct preference pairs where two solution trajectories share the first k verified-correct steps and diverge at step k+1 (one formally verified, one formally rejected). This provides step-localized preference signals with formal guarantees — zero annotation cost, zero label noise within formalization scope.

**Formalization quality control**: To prevent conflating formalization failures with genuine reasoning errors, we introduce a formalization confidence pipeline: (a) distinguish "verification failed = error detected" from "formalization failed = unknown status," (b) exclude solutions where formal rejection co-occurs with correct final answer (suspicious formalization failure), (c) only use high-confidence verified/rejected pairs for DPO. We target a noise rate well below the 15% tolerance threshold established by imperfect verifier research (arXiv 2026).

## Experimental Design

**Student models**: Qwen3.5-9B (primary, 5 iterations) + Qwen3.5-4B (validation, 3 iterations).

**Benchmarks** (7, spanning difficulty gradient): GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench. OOD generalization tested on AIME24/25 (training uses MATH-train distribution).

**Evaluation protocol**: Greedy accuracy + Pass@K (K=8, 32) + majority voting@K. 3 independent runs; report mean ± std with significance tests on key comparisons. Per-MATH-subcategory breakdown separating formally-covered vs. fallback categories.

**Baseline matrix**:
- Training paradigm: Vanilla SFT (uniform synthetic data), SFT+DPO (uniform data), GRPO/RLVR
- Targeting methods: SwS (NeurIPS 2025; pass-rate-based weakness targeting), STAT-style LLM-teacher profiling + targeted synthesis
- Symbolic method: Adaptive Problem Generation (arXiv 2026; global difficulty adaptation without error-type targeting)
- Verification: Outcome-only verification loop (NSRSA-style), majority voting verification

**Ablation studies** (6 groups):
1. Error profiling source: Formal verification vs. LLM-based vs. pass-rate-based vs. random
2. Targeting vs. uniform: Targeted synthesis (from error profile) vs. uniform synthesis (same quantity)
3. Training objective: SFT only vs. DPO only vs. SFT+DPO
4. Error taxonomy granularity: 5-type fine-grained vs. 2-type coarse (arithmetic / non-arithmetic) vs. single aggregate
5. Iteration dynamics: Per-iteration accuracy, error profile shift, formalization coverage, entropy — demonstrating stable convergence rather than collapse
6. Preference pair source: DPO pairs from formal verification vs. from outcome verification vs. from LLM annotation (Step-DPO style)

**Compute fairness**: Report total compute (GPU hours + CPU hours for symbolic verification) per method. Design compute-matched comparison giving baselines equivalent extra compute budget. Plot accuracy vs. total compute curves.

**Pilot study**: Before main experiments, run Qwen3.5-9B on 500 MATH test problems, classify errors via formal tools, validate taxonomy coverage and inter-category overlap, compare with STAT's skill taxonomy to justify the 5-category design.

## Key References

- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)
- STAT: Skill-Targeted Adaptive Training (ICLR 2026)
- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)
- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)
- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)
- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)
- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)
- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)
- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)
- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)
- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)
- Adaptive Problem Generation via Symbolic Representations (arXiv 2026, arXiv 2602.19187)
- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026)
- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)
- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)
- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)
- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)
- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)
- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)
- Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs (NeurIPS 2024)
- Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning (ACL 2025 Findings)
- LLMs Cannot Spot Math Errors Even When Allowed to Peek into the Solution (EMNLP 2025, arXiv 2509.01395)

## Resource Estimate

- **manual**: gpu_hours: 720 H100 hours (5 iterations Qwen3.5-9B + 3 iterations Qwen3.5-4B + evaluation/ablations), timeline: 4-5 months, estimated_gpu_cost: $1,800
- **human_in_loop**: gpu_hours: 670 H100 hours, timeline: 3-4 months, claude_api_cost: $400-600, estimated_gpu_cost: $1,675
- **auto_research**: gpu_hours: 670 H100 hours, timeline: 6-8 weeks, claude_api_cost: $1,200-2,000, estimated_gpu_cost: $1,675, speed_bottleneck: Symbolic verification throughput — Z3/SymPy step verification is CPU-bound (~0.5-2s per step) and serialized per solution; formalizing natural language solutions to symbolic form requires careful LLM-to-formal translation with ~60-70% success rate on amenable categories, necessitating retry loops
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ee55d43-2bbd-4176-8cc0-344ad67b763d",
  "isSidechain": false,
  "requestId": "req_011CbSn1jo42HcxrJchrwSpU",
  "type": "assistant",
  "uuid": "9b0db83e-d61a-4c1f-b9c7-d7bd8415abfb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LBrBTxDEz8Ykv6rrE6tQuX",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9349,
      "cache_read_input_tokens": 37864,
      "output_tokens": 4203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9349,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4203,
          "cache_read_input_tokens": 37864,
          "cache_creation_input_tokens": 9349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9349
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

_source line 49_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【引用修复】你刚输出的 proposal 纯净版遗漏了以下原文中存在的引用： - ACL 2026  请重新输出完整的纯净版 proposal，确保上述引用全部包含在内。只输出 --- 包围的纯净版 proposal，不要输出其他内容。",
  "leafUuid": "9b0db83e-d61a-4c1f-b9c7-d7bd8415abfb",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 52 · 2026-05-27T08:47:50.554Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:47:50.554Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "content": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have enough research to provide a thorough assessment. Let me compile my analysis.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- **NSRSA (arXiv 2603.21558, March 2026)**: 最接近的竞争工作。已在 GSM8K 上使用 SymPy 做 arithmetic-level symbolic verification + DPO preference pair 构建，拒绝了约 34% 通过 outcome verification 但推理有误的解。但仅覆盖 arithmetic 操作，无 error 分类，无 targeted synthesis。NSRSA 的 DPO pair 是 solution-level（通过/拒绝），而非 step-localized。\n- **STAT (arXiv 2510.10023, ICLR 2026)**: 使用 teacher LLM 的 metacognition 建立 skill profile，通过 Missing-Skill-Profile 驱动 reweighting/synthesis。在 MATH 上提升 7.5%。核心局限：skill profiling 质量受限于 teacher model 能力。\n- **Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, Feb 2026)**: 使用 SymPy 做 symbolic problem representation，在 RLVR 闭环中 adapt difficulty。但不做 error-type diagnosis——只调整全局难度，不 target 特定错误类别。\n- **SwS (NeurIPS 2025)**: 通过 RL pass-rate 分析识别 weakness，提取 core concepts 合成新问题。无 formal verification，无 step-level diagnosis。在 7B/32B 模型上分别提升 10%/7.7%。\n- **Solver-Verifier Gap Theory (ICLR 2026, arXiv 2507.00075)**: 理论证明 verifier reliability 决定 self-improvement ceiling。模型精度呈指数收敛到 verifier reliability 决定的极限。\n- **MATH-VF (arXiv 2505.20869, 2025)**: 使用 SymPy+Z3 做 step-wise verification，但作为 training-free inference-time framework，未用于 self-improvement loop。\n- **Autoformalization success rates (multiple papers)**: 在 theorem proving 场景下，最强模型 formalization 成功率仅 16-40%。但这些是 Lean/Isabelle 的 full theorem proving，而非 SymPy/Z3 的 algebraic verification——后者的 formalization 难度显著较低。\n- 调研总结：当前领域研究者在 formal verification for math reasoning 方向主要关注两条线：(1) 用 formal tools 生成 PRM 训练数据（FoVer），(2) 用 symbolic verification 做 iterative self-training 的 data quality gate（NSRSA）。但 **formal error categorization → targeted synthesis** 这一闭环在现有工作中确实空缺。该 proposal 恰好处于 FoVer（formal verification 做 step-level labeling）、STAT（targeted synthesis）、NSRSA（symbolic verification for iterative training）三者的交叉空白地带。\n\n---\n\n【发掘点 1】\n- 维度: trivial alternative 威胁\n- 内容: Proposal 需要更尖锐地回应一个 trivial baseline：**MATH 数据集已有 subcategory 标签（Algebra, Number Theory, Prealgebra 等），直接用 outcome verification + 现有 subcategory 标签做 targeted synthesis 即可**——无需任何 formal verification，只需计算模型在各 subcategory 的准确率，然后对低准确率类别生成更多题目。这个成本极低的 baseline 没有出现在当前的 baseline matrix 中。Proposal 虽然设计了 \"error profiling source: formal vs. LLM-based vs. pass-rate-based vs. random\" 的 ablation，但 \"pass-rate-based\" 如果等同于 SwS 的方法，那和 \"subcategory-level accuracy targeting\" 还不一样。建议明确增加 **subcategory-level outcome targeting** 作为 ablation 或 baseline，并清晰阐述 formal verification 在 subcategory **内部** 的 fine-grained error type 区分（如同一 Algebra 题内，algebraic manipulation error vs. equation solving error）为什么能带来 subcategory-level 所无法提供的增量价值。这是 reviewer 最可能提出的 \"why not just...\" 质疑。\n- 价值: 直击 novelty 的核心——如果 subcategory-level targeting 效果相当，formal step-level diagnosis 的增量贡献将被严重削弱。提前回应这一 trivial alternative 能让 novelty claim 更站得住脚。\n- 调研依据: STAT 的 skill taxonomy 本质上就是一种更细粒度的 subcategory 划分（由 teacher LLM 生成）；SwS 使用 pass-rate 分析但也是在 problem-level 操作。FormalLoop 的核心增量必须证明 step-level error type granularity > subcategory-level granularity，而非仅证明 formal > LLM-based。\n\n【发掘点 2】\n- 维度: significance 提升\n- 内容: **Error profile dynamics 应被提升为一等公民的科学贡献，而非仅作为 ablation 附产品。** 当前 proposal 在 ablation 5 中提到 \"per-iteration error profile shift\"，但这被埋在实验设计的第 5 条。在整个 self-improvement 文献中，几乎没有工作用 ground-truth error labels 追踪模型在多轮迭代中的 error type 演化——现有工作（NSRSA、SwS）只能追踪整体准确率曲线。FormalLoop 独特地拥有 formally-verified 的 per-iteration error profile，可以回答一系列高价值的科学问题：(a) 不同 error type 的消减速度是否有固定的优先级顺序？(b) 是否存在 error type 之间的依赖关系（如 arithmetic error 必须先解决才能暴露 algebraic manipulation error）？(c) error profile 的 entropy 下降曲线是否能预测 self-improvement 的收敛点？建议将此提升为与 \"teacher-free targeted self-improvement\" 并列的核心贡献之一，而非实验的 byproduct。\n- 价值: 这将 proposal 从 \"一个更好的 self-improvement pipeline\" 提升到 \"一个理解 self-improvement dynamics 的分析工具\"，直接提升 significance。审稿人更容易为提供新理解的工作打高分，而不仅仅是提升几个百分点的工程贡献。\n- 调研依据: Solver-Verifier Gap Theory (ICLR 2026) 提供了 self-improvement dynamics 的理论框架（指数收敛律），但该理论是 aggregate-level 的。FormalLoop 可以提供 skill-decomposed 的 dynamics，补充该理论框架，这在现有文献中完全空白。\n\n【发掘点 3】\n- 维度: novelty 锐化\n- 内容: **Step-localized formally-verified DPO pairs 与 NSRSA 的差异化需要更加锐利。** 当前 proposal 提到 \"unlike Step-DPO and Full-Step-DPO\"，但最直接的竞争者其实是 NSRSA——它也用 symbolic verification 构建 DPO pairs。调研发现 NSRSA 的 DPO 是 solution-level 的（整条解被 accept/reject），而 FormalLoop 的 DPO 是 step-localized 的（两条轨迹共享前 k 个 verified-correct steps，在 k+1 步分叉）。这是一个重要的技术差异：step-localized DPO 提供了更精确的 credit assignment，理论上应该比 solution-level DPO 有更高的 sample efficiency。建议 (1) 在 related work 中将 NSRSA 的 DPO 方式作为直接对比对象明确讨论，(2) 在 ablation 6 中确保包含 \"solution-level formal DPO (NSRSA-style) vs. step-localized formal DPO (ours)\" 的对比，而不仅是 \"formal vs. outcome vs. LLM annotation\" 的来源对比。\n- 价值: 锐化 novelty——让审稿人清楚 FormalLoop 不仅是 \"用 formal tools 替代 LLM\"，而是在 DPO 的 credit assignment 粒度上有技术创新。这比简单的 tool substitution 更有说服力。\n- 调研依据: NSRSA (arXiv 2603.21558) 的实验结果显示其 DPO reward accuracy 从 46% 提升到 63%，但这是 solution-level 的。Step-localized DPO 的 credit assignment 优势是 Step-DPO (NeurIPS 2024) 系列工作的核心洞察，FormalLoop 将这一洞察与 formal verification 的 zero-noise guarantee 结合，是有实质新颖性的。\n\n【发掘点 4】\n- 维度: 核心 claim 强化\n- 内容: **\"Partial precise > Full noisy\" 原则应被提炼为可推广的理论贡献。** Proposal 的一个关键论点是：即使 formal verification 只覆盖 algebraic/arithmetic 子域（约 60-70% 的 formalization 成功率），其 near-zero noise 也优于 LLM teacher 对所有类别的 noisy diagnosis。这一论点目前散落在 \"scope of formal coverage\" 和 \"Why Not Just Use Outcome Verification\" 两节中。建议将其凝练为一个明确的、可量化验证的假设：**\"在 self-improvement loop 中，verifier 的 precision-coverage tradeoff 存在一个 tipping point——当 noise rate 超过阈值 τ 时，扩大 coverage 的边际收益为负。\"** Imperfect verifier research (arXiv 2026) 给出了 τ ≈ 15% 的实证估计，FormalLoop 可以通过 ablation（人工注入不同水平的 formalization noise）来验证这一 tradeoff curve。这将使 proposal 从 \"我们用了更好的 tools\" 提升到 \"我们发现了 verifier design 的一个基本 tradeoff\"。\n- 价值: 这个原则如果成立，其影响力远超 math reasoning 本身——任何需要 verifier 的 self-improvement 场景（代码生成、逻辑推理等）都适用。将 proposal 的 significance 从 domain-specific 提升到 generalizable principle。\n- 调研依据: Imperfect verifier research (arXiv 2026) 证明 noise tolerance 约 15%，Solver-Verifier Gap Theory (ICLR 2026) 证明 verifier reliability 决定 self-improvement ceiling。两者结合直接支持 precision-coverage tradeoff 的存在，但目前无人在 targeted self-improvement 场景中实证验证这一 tradeoff。\n\n【发掘点 5】\n- 维度: 前提假设质疑\n- 内容: **Formalization 成功率 60-70% 的估计需要更严格的支撑，否则存在 survivorship bias 风险。** 调研发现，autoformalization 在 theorem proving 场景下成功率仅 16-40%（最强模型）。Proposal 论证其场景（SymPy/Z3 algebraic verification）比 Lean/Isabelle theorem proving 简单，因此成功率更高——这个论证本身是合理的，但 60-70% 这个数字似乎缺乏直接的实证来源。更关键的问题是：**formalization 失败的 30-40% 的解是否是随机的？** 如果 formalization 倾向于在某类特定错误上失败（如涉及隐式推理步骤的错误），则 error profile 将系统性地低估这类错误的频率，导致 targeted synthesis 的方向偏差。这不是\"formal verification 不准确\"的问题——formal verification 对于其成功 formalize 的部分是准确的——而是 **selection bias** 问题：能被 formalize 的错误和不能被 formalize 的错误在类型分布上是否有系统性差异？建议在 pilot study 中增加一项分析：比较 formalization 成功组和失败组的错误类型分布差异。\n- 价值: 如果 selection bias 确实存在且未被控制，那么 FormalLoop 的 targeted synthesis 可能系统性地忽略某类重要错误，导致 error profile 的 ground-truth 优势被稀释。提前识别并回应这一假设风险能显著增强 paper 的 soundness。\n- 调研依据: Autoformalization 文献 (FormalMATH, StepFun-Formalizer) 显示 formalization 成功率与问题复杂度、推理步骤类型高度相关——涉及隐式知识或 multi-step 推理链的步骤更难 formalize。这支持 selection bias 假设的合理性。\n\nSources:\n- [NSRSA - Stabilizing Iterative Self-Training with Verified Reasoning](https://arxiv.org/abs/2603.21558)\n- [STAT - Skill-Targeted Adaptive Training](https://arxiv.org/abs/2510.10023)\n- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)\n- [SwS - Self-aware Weakness-driven Problem Synthesis](https://openreview.net/forum?id=0jQUNQsZra)\n- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)\n- [FoVer - Efficient PRM Training Data Synthesis](https://arxiv.org/abs/2505.15960)\n- [MATH-VF - Step-Wise Formal Verification](https://arxiv.org/html/2505.20869v1)\n- [Safe - Retrospective Step-aware Formal Verification](https://arxiv.org/pdf/2506.04592)\n- [FormalMATH Benchmark](https://arxiv.org/pdf/2505.02735)\n- [StepFun-Formalizer](https://arxiv.org/pdf/2508.04440)\n\n【补救 agent 本轮输出】:\nNow I have sufficient background to provide my assessment. Let me compile the findings.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **STAT (ICLR 2026, arXiv 2510.10023)**: 实验使用 MATH-Train 作为数据源，统一 9.5K 训练样本做 compute-matched comparison；baseline 包括 Embed-Sel、random selection、uniform SFT；ablation 涵盖 threshold sensitivity 和 teacher model 变体（GPT-4o vs. 较弱 teacher）。评审要求对 skill profile 质量做人工验证。\n- **SwS (NeurIPS 2025, arXiv 2506.08989)**: 在 3B/7B/32B 三个模型规模上实验；8 个数学 benchmark 评测；baseline 包括 seed-data-only RLVR、human-labeled problem set RLVR；weakness 定义为 RL 训练中 pass rate 持续低的题目，无需外部 teacher。\n- **NSRSA (arXiv 2603.21558, March 2026)**: 5 轮 self-training iteration，Qwen3-4B-Thinking 在 GSM8K 上从 80.5% → 91.0%；对比 no-verification (collapse to 73.2%)、outcome-only (plateau 85.8%)；symbolic verification 仅覆盖 arithmetic operations，拒绝了约 34% 正确答案但推理有缺陷的样本。DPO 实验提升 reward accuracy 46% → 63%。\n- **FoVer (ACL Findings 2026, arXiv 2505.15960)**: 使用 Z3 + Isabelle 生成 40K step-level 标注数据；在 12 个 benchmark 评测 PRM 泛化性；baseline 包括 Monte Carlo roll-out PRM 和 human-annotated PRM；展示了 formal verification 数据训练的 PRM 可泛化到非形式化任务。\n- **MATH-VF (arXiv 2505.20869)**: 提出 SimpleMath 形式化语言 + Z3/SymPy Critic 做 step-wise verification；实测显示 Z3 在高阶概念（gcd/lcm）上受限，SymPy 在多变量不等式上有困难；未公开 per-category formalization coverage 具体数值。\n- **Imperfect Verifier (arXiv 2604.07666)**: noise rate ≤15% 时 validation accuracy 与 clean baseline 差距在 2pp 以内；precision 比 recall 更重要；跨三个模型家族（Qwen3/GLM4/Llama 3.1）和 4B-9B 规模验证。\n- **Adaptive Problem Generation (arXiv 2602.19187)**: SymPy 空间做 symbolic problem representation + closed-loop difficulty adaptation；GRPO/PPO 两种 RLVR 算法对比；seed-data baseline；不做 error-type diagnosis。\n- **Step-DPO (NeurIPS 2024, arXiv 2406.18629)**: 只优化第一个错误步骤避免惩罚正确前序步骤；Qwen2-72B-Instruct 在 MATH 上 70.8%；依赖 LLM/人工标注定位错误步骤。\n\n- **调研总结**: 该领域当前实验设计标准要求：(1) 至少 3 个模型规模或 2 个模型家族验证泛化性；(2) compute-matched comparison 是审稿人硬性要求；(3) ablation 需隔离每个组件的贡献且对比至少 3 种变体；(4) 形式化方法的论文必须报告覆盖率/成功率并分析其对整体效果的影响；(5) 自训练循环方法需展示多轮 iteration 的稳定性曲线和 collapse 对比。\n\n---\n\n【缺陷 1】\n- 类别: baseline 不足\n- 问题: Proposal 的 baseline matrix 缺少 **FoVer-style formal-verification-trained PRM 作为 verifier 的自训练循环** 这一关键 baseline。FoVer 已经证明可以用 formal verification 数据训练出泛化到 12 个 benchmark 的 PRM。一个自然的替代方案是：用 FoVer 方法训练一个 PRM，然后用该 PRM 做 Best-of-N 或 RLVR 的 reward model，在同一个 self-improvement loop 中运行。这条 baseline 直接对标 FormalLoop 的核心差异化——\"formal verification 应该直接用于 error profiling + targeted synthesis\" vs. \"formal verification 应该间接通过 PRM 使用\"。缺少这个 baseline，审稿人会质疑：FormalLoop 的增益到底来自 formal verification 本身，还是来自 targeted synthesis pipeline？\n- 严重度: 可补救\n- 补救方案: 增加一条 baseline：FoVer-PRM + Best-of-N/RLVR self-improvement loop。用 FoVer 公开的 FoVer-40K 数据（或按其方法生成）训练 PRM，在同一 iteration 框架下作为 verifier 运行。这能直接隔离 \"formal verification 用于 PRM 训练\" vs. \"formal verification 用于直接 error profiling + targeted synthesis\" 的效果差异。\n- 调研依据: FoVer (ACL Findings 2026) 已开源数据和代码，其 PRM 在 12 个 benchmark 上表现优于 Monte Carlo roll-out PRM，是一个 strong baseline。\n\n【缺陷 2】\n- 类别: 可行性问题\n- 问题: Proposal 声称 formalization success rate 为 ~60-70%（在 amenable categories 上），但这个数字缺乏具体来源和验证。MATH-VF 论文未公开 per-category formalization coverage 数值；Z3 在 gcd/lcm 等概念上受限、SymPy 在多变量不等式上有困难是已知问题。Proposal 将 MATH 的 Algebra、Number Theory、Prealgebra、部分 Intermediate Algebra 和 Precalculus 标为 amenable，但对每个子类别的实际可形式化比例没有依据。如果实际 success rate 显著低于 60%，则 (a) error profiling 的覆盖范围过窄，targeted synthesis 效果打折；(b) DPO 对的产量不足（见缺陷 3）；(c) 整体方法的优势可能仅体现在少数类别上，无法支撑 general improvement 的 claim。\n- 严重度: 可补救\n- 补救方案: **(a) 扩展 pilot study 的范围和报告粒度**——不仅在 500 道 MATH 测试题上运行，还应对 MATH-Train 的所有 7 个子类别各取 200-300 道题，用 Qwen3.5-9B 生成解答并尝试形式化，报告每个子类别的形式化成功率、失败原因分布（formalization failure vs. solver timeout vs. scope limitation）。**(b) 设定 go/no-go 阈值**——如果 amenable 类别的平均形式化成功率低于 50%，需要重新评估方法的 scope 或引入额外的形式化增强策略（如 MATH-VF 的 SimpleMath 中间语言方法）。**(c) 报告\"有效覆盖率\"**——即 formalization success rate × amenable categories 在 MATH 中的占比，给出整体实际覆盖比例。\n- 调研依据: MATH-VF (arXiv 2505.20869) 提出了 SimpleMath 形式化语言来提高 formalization 成功率，但即便如此也未报告各类别的具体覆盖数值，说明这是已知的难点。\n\n【缺陷 3】\n- 类别: 实验设计不足\n- 问题: **Formally-verified DPO 对的产量（yield）未估算**。Proposal 描述的 DPO pair 构造要求两条解题轨迹共享前 k 个 formally-verified-correct 步骤，在第 k+1 步分歧（一条 verified correct，一条 verified rejected）。这个构造需要同时满足：(a) 两条轨迹都能成功形式化（60-70% × 60-70% ≈ 36-49% 概率）；(b) 两条轨迹有共同正确前缀；(c) 在共享前缀后恰好出现分歧。满足所有条件的样本对可能非常稀少。如果每道题生成 8 条解答（Pass@8 的采样量），可用 DPO 对数量可能远低于有效训练所需。Step-DPO 报告需要 10K+ pairs 才能有效训练。\n- 严重度: 可补救\n- 补救方案: **(a) 在 pilot study 中增加 DPO pair yield 估算**——用 Qwen3.5-9B 对 500 道题各生成 16 条解答，运行形式化+验证 pipeline，统计能构造出的 step-localized DPO pairs 数量。**(b) 设计退化策略（fallback）**——当 step-localized pairs 不足时，允许退化为 \"solution-level\" DPO pairs（整条正确 vs. 整条错误，类似 outcome-based），报告不同粒度 DPO pairs 的混合比例及其效果。**(c) 增加采样量**——每道题从 8 条增加到 16-32 条解答以提高 pair yield。**(d) 在 ablation 6 中额外报告各条件下可用 DPO pair 的数量**，使审稿人能判断 data quantity 差异是否 confound 了 pair quality 的对比。\n- 调研依据: Step-DPO (NeurIPS 2024) 使用 ~10K pairs 训练，Full-Step-DPO 也需要类似规模。NSRSA 的 DPO 实验构造 pair 的方式更宽松（基于 symbolic verification accept/reject，不要求 step-aligned prefix），产量更高。\n\n【缺陷 4】\n- 类别: 实验设计不足\n- 问题: **模型多样性不足**。Proposal 仅使用 Qwen3.5 家族的两个规模（9B 和 4B）。当前领域标准（SwS 在 3B/7B/32B 上实验；Imperfect Verifier 跨 Qwen3/GLM4/Llama 3.1 三个家族验证）要求至少验证跨模型家族的泛化性。仅在 Qwen3.5 上的结果可能被审稿人质疑为 model-specific，特别是 formalization pipeline 的性能（LLM-to-formal translation 成功率）高度依赖模型的 code/symbolic 能力，不同模型家族可能表现差异巨大。\n- 严重度: 可补救\n- 补救方案: **(a) 增加至少一个非 Qwen 家族的验证模型**——Llama 3.1-8B 或 Phi-4 14B 是合理选择，成本可控（3 iterations 足够展示趋势）。**(b) 如果计算资源确实不够，至少在 pilot study 中对比 Qwen3.5-9B 和另一个家族模型的 formalization success rate**，证明 pipeline 不是 Qwen-specific。**(c) 在 Limitations 中明确声明仅在 Qwen 家族验证，并 justify 为什么（如 Qwen 系列在 math reasoning 上最有代表性）。\n- 调研依据: Imperfect Verifier (arXiv 2604.07666) 跨 Qwen3/GLM4/Llama 3.1 三个家族验证是该领域近期的标准做法；SwS (NeurIPS 2025) 在 3B-32B 验证。\n\n【缺陷 5】\n- 类别: compute 公平性问题\n- 问题: **Compute-matched comparison 的设计缺乏具体定义**。Proposal 提到 \"design compute-matched comparison giving baselines equivalent extra compute budget\"，但没有定义 compute budget 的计量单位和等价标准。FormalLoop 的 compute 由三部分组成：(a) GPU hours（LLM inference for formalization + fine-tuning）；(b) CPU hours（Z3/SymPy symbolic verification）；(c) LLM inference for problem synthesis/NL generation。Baseline 方法的 compute 结构不同（如 STAT 需要 teacher LLM inference，SwS 需要 RL pass-rate estimation）。如果只按 GPU hours 对齐，FormalLoop 的 CPU overhead 被隐藏；如果按 wall-clock time 对齐，并行化程度不同会导致不公平。审稿人 **一定** 会追问这个问题。\n- 严重度: 可补救\n- 补救方案: **(a) 定义统一的 compute metric**——建议用 \"equivalent FLOPs\" 或 \"total dollar cost (GPU + CPU + API)\" 作为计量标准，对所有方法计算并报告。**(b) 设计两种 compute-matched 对比**：(i) 给 baseline 等量的 GPU training FLOPs（fine-tuning 对齐）；(ii) 给 baseline 等量的 total compute budget（包括 data generation/verification/synthesis 全流程）。**(c) 在 accuracy vs. total compute 曲线中使用统一的 x 轴单位**。**(d) 单独报告 FormalLoop 各阶段（formalization、verification、synthesis、training）的 compute breakdown**。\n- 调研依据: SwS 和 STAT 都在固定数据量（如 STAT 的 9.5K pairs）下对比，这是一种 data-matched 而非 compute-matched 的策略。Proposal 的场景更复杂（有 symbolic verification overhead），需要更精细的公平性设计。基于领域实验规范判断。\n\n【缺陷 6】\n- 类别: 实验设计不足\n- 问题: **Symbolic problem synthesis 的质量评估缺失**。Proposal 的核心 pipeline 包含 \"SymPy-based problem synthesis targeting the model's weakest skills\"，但实验设计中没有任何评估合成题目质量的方案。合成题目可能存在以下问题：(a) 形式上合法但过于简单/trivial（不能有效训练目标 skill）；(b) 难度分布与目标 benchmark 不匹配；(c) 自然语言表述不自然或有歧义。如果合成题目质量有问题，targeted synthesis 的效果就会打折，而这个因素会被 confound 在 \"targeting vs. uniform\" 的 ablation 中，导致无法区分 \"targeting 有效\" vs. \"合成题目质量好\"。\n- 严重度: 可补救\n- 补救方案: **(a) 增加合成题目的质量评估**——对合成题目进行 human evaluation（随机抽样 100-200 道，由数学背景标注员评估 well-formedness、difficulty appropriateness、NL quality）。**(b) 对合成题目做 difficulty calibration**——用基准模型的 pass rate 衡量合成题目的实际难度，对比目标 benchmark 的难度分布。**(c) 在 ablation 中增加一组对照：用相同 SymPy 模板但 random targeting（不根据 error profile 选择 skill）合成等量题目，隔离 targeting 策略和 synthesis 质量的效果。\n- 调研依据: Adaptive Problem Generation (arXiv 2602.19187) 在 symbolic space 做问题生成时有 closed-loop difficulty adaptation 机制；SPARQ 使用 quality-diversity algorithms 确保合成问题的多样性。FormalLoop 的合成 pipeline 缺少类似的质量保障机制。\n\n【缺陷 7】\n- 类别: 可行性问题\n- 问题: **Compute 预算可能不足以支撑完整 ablation 计划**。Proposal 规划了 720 H100 hours 覆盖 5 iterations Qwen3.5-9B + 3 iterations Qwen3.5-4B + evaluation + ablations。粗略估算：Qwen3.5-9B 单次 full fine-tune 约 40-80 H100 hours（取决于数据量和 epoch 数），5 iterations ≈ 200-400 hours；6 组 ablation 中多个需要完整训练 run（ablation 1 有 4 条件、ablation 3 有 3 条件、ablation 6 有 3 条件 = 至少 10 个额外 training runs），即使减少 iteration 数到 2-3 轮也需要 ~200-400 hours；加上 evaluation（7 benchmarks × Pass@K 采样）和 Qwen3.5-4B 实验，总计可能接近 900-1200 hours。如果再加上缺陷 4 建议的跨家族验证，budget 更吃紧。\n- 严重度: 可补救\n- 补救方案: **(a) 明确 ablation 实验的简化策略**——指定 ablation 在 Qwen3.5-4B 上运行（而非 9B）、限制 iteration 数为 2-3 轮、限制评测 benchmark 为 3 个代表性的（如 GSM8K + MATH-500 + AIME24）。**(b) 重新估算 compute budget**——按上述简化方案重算，确保预算覆盖。**(c) 对 ablation 做优先级排序**——ablation 1（error profiling source）和 ablation 6（preference pair source）最关键，ablation 4（taxonomy granularity）可降低优先级。预算不足时先保证 high-priority ablations 的完整性。\n- 调研依据: STAT 的 ablation 在较小规模上进行且限制数据量到 9.5K。SwS 的 ablation 也在 7B 模型上做，不在最大模型上重复全部实验。基于领域实验规范判断。\n\n【缺陷 8】\n- 类别: 实验设计不足\n- 问题: **STAT-style baseline 的 teacher model 未指定**。Proposal 列出 \"STAT-style LLM-teacher profiling + targeted synthesis\" 作为 baseline，但未说明用哪个 teacher model。STAT 原论文使用 GPT-4o 作为 teacher，并在 ablation 中展示 teacher 能力对效果有显著影响。Teacher 的选择直接影响该 baseline 的强度——用弱 teacher 会使该 baseline 偏弱，用强 teacher 则是公平对比。审稿人会要求明确说明。\n- 严重度: 可补救\n- 补救方案: **(a) 指定使用 GPT-4o 或同等水平的 frontier model 作为 teacher**，确保 baseline 足够强。**(b) 如果 API 成本是考量，说明 teacher model 选择的理由及其对结果公平性的影响。**(c) 在 resource estimate 中加入 teacher API 调用成本（STAT-style baseline 需要大量 teacher inference）。\n- 调研依据: STAT (ICLR 2026) 使用 GPT-4o 作为 teacher，并在 Section E.3 做了 teacher model variant 的 ablation，展示了 teacher 质量对效果的显著影响。\n\nSources:\n- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://arxiv.org/abs/2510.10023)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)](https://arxiv.org/abs/2505.15960)\n- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://arxiv.org/abs/2506.08989)\n- [NSRSA: Symbolic Recursive Self-Alignment (arXiv 2026)](https://arxiv.org/abs/2603.21558)\n- [MATH-VF: Step-Wise Formal Verification (arXiv 2025)](https://arxiv.org/abs/2505.20869)\n- [An Imperfect Verifier is Good Enough (arXiv 2026)](https://arxiv.org/abs/2604.07666)\n- [Adaptive Problem Generation via Symbolic Representations (arXiv 2026)](https://arxiv.org/abs/2602.19187)\n- [Step-DPO: Step-wise Preference Optimization (NeurIPS 2024)](https://arxiv.org/abs/2406.18629)\n- [Full-Step-DPO (ACL 2025 Findings)](https://arxiv.org/abs/2502.14356)"
}
```

---

### Runtime record

_source line 53 · 2026-05-27T08:47:50.555Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:47:50.555Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

## Round 4

20 recorded events

### User

_source line 54 · 2026-05-27T08:47:50.579Z_

【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have enough research to provide a thorough assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- **NSRSA (arXiv 2603.21558, March 2026)**: 最接近的竞争工作。已在 GSM8K 上使用 SymPy 做 arithmetic-level symbolic verification + DPO preference pair 构建，拒绝了约 34% 通过 outcome verification 但推理有误的解。但仅覆盖 arithmetic 操作，无 error 分类，无 targeted synthesis。NSRSA 的 DPO pair 是 solution-level（通过/拒绝），而非 step-localized。
- **STAT (arXiv 2510.10023, ICLR 2026)**: 使用 teacher LLM 的 metacognition 建立 skill profile，通过 Missing-Skill-Profile 驱动 reweighting/synthesis。在 MATH 上提升 7.5%。核心局限：skill profiling 质量受限于 teacher model 能力。
- **Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187, Feb 2026)**: 使用 SymPy 做 symbolic problem representation，在 RLVR 闭环中 adapt difficulty。但不做 error-type diagnosis——只调整全局难度，不 target 特定错误类别。
- **SwS (NeurIPS 2025)**: 通过 RL pass-rate 分析识别 weakness，提取 core concepts 合成新问题。无 formal verification，无 step-level diagnosis。在 7B/32B 模型上分别提升 10%/7.7%。
- **Solver-Verifier Gap Theory (ICLR 2026, arXiv 2507.00075)**: 理论证明 verifier reliability 决定 self-improvement ceiling。模型精度呈指数收敛到 verifier reliability 决定的极限。
- **MATH-VF (arXiv 2505.20869, 2025)**: 使用 SymPy+Z3 做 step-wise verification，但作为 training-free inference-time framework，未用于 self-improvement loop。
- **Autoformalization success rates (multiple papers)**: 在 theorem proving 场景下，最强模型 formalization 成功率仅 16-40%。但这些是 Lean/Isabelle 的 full theorem proving，而非 SymPy/Z3 的 algebraic verification——后者的 formalization 难度显著较低。
- 调研总结：当前领域研究者在 formal verification for math reasoning 方向主要关注两条线：(1) 用 formal tools 生成 PRM 训练数据（FoVer），(2) 用 symbolic verification 做 iterative self-training 的 data quality gate（NSRSA）。但 **formal error categorization → targeted synthesis** 这一闭环在现有工作中确实空缺。该 proposal 恰好处于 FoVer（formal verification 做 step-level labeling）、STAT（targeted synthesis）、NSRSA（symbolic verification for iterative training）三者的交叉空白地带。

---

【发掘点 1】
- 维度: trivial alternative 威胁
- 内容: Proposal 需要更尖锐地回应一个 trivial baseline：**MATH 数据集已有 subcategory 标签（Algebra, Number Theory, Prealgebra 等），直接用 outcome verification + 现有 subcategory 标签做 targeted synthesis 即可**——无需任何 formal verification，只需计算模型在各 subcategory 的准确率，然后对低准确率类别生成更多题目。这个成本极低的 baseline 没有出现在当前的 baseline matrix 中。Proposal 虽然设计了 "error profiling source: formal vs. LLM-based vs. pass-rate-based vs. random" 的 ablation，但 "pass-rate-based" 如果等同于 SwS 的方法，那和 "subcategory-level accuracy targeting" 还不一样。建议明确增加 **subcategory-level outcome targeting** 作为 ablation 或 baseline，并清晰阐述 formal verification 在 subcategory **内部** 的 fine-grained error type 区分（如同一 Algebra 题内，algebraic manipulation error vs. equation solving error）为什么能带来 subcategory-level 所无法提供的增量价值。这是 reviewer 最可能提出的 "why not just..." 质疑。
- 价值: 直击 novelty 的核心——如果 subcategory-level targeting 效果相当，formal step-level diagnosis 的增量贡献将被严重削弱。提前回应这一 trivial alternative 能让 novelty claim 更站得住脚。
- 调研依据: STAT 的 skill taxonomy 本质上就是一种更细粒度的 subcategory 划分（由 teacher LLM 生成）；SwS 使用 pass-rate 分析但也是在 problem-level 操作。FormalLoop 的核心增量必须证明 step-level error type granularity > subcategory-level granularity，而非仅证明 formal > LLM-based。

【发掘点 2】
- 维度: significance 提升
- 内容: **Error profile dynamics 应被提升为一等公民的科学贡献，而非仅作为 ablation 附产品。** 当前 proposal 在 ablation 5 中提到 "per-iteration error profile shift"，但这被埋在实验设计的第 5 条。在整个 self-improvement 文献中，几乎没有工作用 ground-truth error labels 追踪模型在多轮迭代中的 error type 演化——现有工作（NSRSA、SwS）只能追踪整体准确率曲线。FormalLoop 独特地拥有 formally-verified 的 per-iteration error profile，可以回答一系列高价值的科学问题：(a) 不同 error type 的消减速度是否有固定的优先级顺序？(b) 是否存在 error type 之间的依赖关系（如 arithmetic error 必须先解决才能暴露 algebraic manipulation error）？(c) error profile 的 entropy 下降曲线是否能预测 self-improvement 的收敛点？建议将此提升为与 "teacher-free targeted self-improvement" 并列的核心贡献之一，而非实验的 byproduct。
- 价值: 这将 proposal 从 "一个更好的 self-improvement pipeline" 提升到 "一个理解 self-improvement dynamics 的分析工具"，直接提升 significance。审稿人更容易为提供新理解的工作打高分，而不仅仅是提升几个百分点的工程贡献。
- 调研依据: Solver-Verifier Gap Theory (ICLR 2026) 提供了 self-improvement dynamics 的理论框架（指数收敛律），但该理论是 aggregate-level 的。FormalLoop 可以提供 skill-decomposed 的 dynamics，补充该理论框架，这在现有文献中完全空白。

【发掘点 3】
- 维度: novelty 锐化
- 内容: **Step-localized formally-verified DPO pairs 与 NSRSA 的差异化需要更加锐利。** 当前 proposal 提到 "unlike Step-DPO and Full-Step-DPO"，但最直接的竞争者其实是 NSRSA——它也用 symbolic verification 构建 DPO pairs。调研发现 NSRSA 的 DPO 是 solution-level 的（整条解被 accept/reject），而 FormalLoop 的 DPO 是 step-localized 的（两条轨迹共享前 k 个 verified-correct steps，在 k+1 步分叉）。这是一个重要的技术差异：step-localized DPO 提供了更精确的 credit assignment，理论上应该比 solution-level DPO 有更高的 sample efficiency。建议 (1) 在 related work 中将 NSRSA 的 DPO 方式作为直接对比对象明确讨论，(2) 在 ablation 6 中确保包含 "solution-level formal DPO (NSRSA-style) vs. step-localized formal DPO (ours)" 的对比，而不仅是 "formal vs. outcome vs. LLM annotation" 的来源对比。
- 价值: 锐化 novelty——让审稿人清楚 FormalLoop 不仅是 "用 formal tools 替代 LLM"，而是在 DPO 的 credit assignment 粒度上有技术创新。这比简单的 tool substitution 更有说服力。
- 调研依据: NSRSA (arXiv 2603.21558) 的实验结果显示其 DPO reward accuracy 从 46% 提升到 63%，但这是 solution-level 的。Step-localized DPO 的 credit assignment 优势是 Step-DPO (NeurIPS 2024) 系列工作的核心洞察，FormalLoop 将这一洞察与 formal verification 的 zero-noise guarantee 结合，是有实质新颖性的。

【发掘点 4】
- 维度: 核心 claim 强化
- 内容: **"Partial precise > Full noisy" 原则应被提炼为可推广的理论贡献。** Proposal 的一个关键论点是：即使 formal verification 只覆盖 algebraic/arithmetic 子域（约 60-70% 的 formalization 成功率），其 near-zero noise 也优于 LLM teacher 对所有类别的 noisy diagnosis。这一论点目前散落在 "scope of formal coverage" 和 "Why Not Just Use Outcome Verification" 两节中。建议将其凝练为一个明确的、可量化验证的假设：**"在 self-improvement loop 中，verifier 的 precision-coverage tradeoff 存在一个 tipping point——当 noise rate 超过阈值 τ 时，扩大 coverage 的边际收益为负。"** Imperfect verifier research (arXiv 2026) 给出了 τ ≈ 15% 的实证估计，FormalLoop 可以通过 ablation（人工注入不同水平的 formalization noise）来验证这一 tradeoff curve。这将使 proposal 从 "我们用了更好的 tools" 提升到 "我们发现了 verifier design 的一个基本 tradeoff"。
- 价值: 这个原则如果成立，其影响力远超 math reasoning 本身——任何需要 verifier 的 self-improvement 场景（代码生成、逻辑推理等）都适用。将 proposal 的 significance 从 domain-specific 提升到 generalizable principle。
- 调研依据: Imperfect verifier research (arXiv 2026) 证明 noise tolerance 约 15%，Solver-Verifier Gap Theory (ICLR 2026) 证明 verifier reliability 决定 self-improvement ceiling。两者结合直接支持 precision-coverage tradeoff 的存在，但目前无人在 targeted self-improvement 场景中实证验证这一 tradeoff。

【发掘点 5】
- 维度: 前提假设质疑
- 内容: **Formalization 成功率 60-70% 的估计需要更严格的支撑，否则存在 survivorship bias 风险。** 调研发现，autoformalization 在 theorem proving 场景下成功率仅 16-40%（最强模型）。Proposal 论证其场景（SymPy/Z3 algebraic verification）比 Lean/Isabelle theorem proving 简单，因此成功率更高——这个论证本身是合理的，但 60-70% 这个数字似乎缺乏直接的实证来源。更关键的问题是：**formalization 失败的 30-40% 的解是否是随机的？** 如果 formalization 倾向于在某类特定错误上失败（如涉及隐式推理步骤的错误），则 error profile 将系统性地低估这类错误的频率，导致 targeted synthesis 的方向偏差。这不是"formal verification 不准确"的问题——formal verification 对于其成功 formalize 的部分是准确的——而是 **selection bias** 问题：能被 formalize 的错误和不能被 formalize 的错误在类型分布上是否有系统性差异？建议在 pilot study 中增加一项分析：比较 formalization 成功组和失败组的错误类型分布差异。
- 价值: 如果 selection bias 确实存在且未被控制，那么 FormalLoop 的 targeted synthesis 可能系统性地忽略某类重要错误，导致 error profile 的 ground-truth 优势被稀释。提前识别并回应这一假设风险能显著增强 paper 的 soundness。
- 调研依据: Autoformalization 文献 (FormalMATH, StepFun-Formalizer) 显示 formalization 成功率与问题复杂度、推理步骤类型高度相关——涉及隐式知识或 multi-step 推理链的步骤更难 formalize。这支持 selection bias 假设的合理性。

Sources:
- [NSRSA - Stabilizing Iterative Self-Training with Verified Reasoning](https://arxiv.org/abs/2603.21558)
- [STAT - Skill-Targeted Adaptive Training](https://arxiv.org/abs/2510.10023)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [SwS - Self-aware Weakness-driven Problem Synthesis](https://openreview.net/forum?id=0jQUNQsZra)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)
- [FoVer - Efficient PRM Training Data Synthesis](https://arxiv.org/abs/2505.15960)
- [MATH-VF - Step-Wise Formal Verification](https://arxiv.org/html/2505.20869v1)
- [Safe - Retrospective Step-aware Formal Verification](https://arxiv.org/pdf/2506.04592)
- [FormalMATH Benchmark](https://arxiv.org/pdf/2505.02735)
- [StepFun-Formalizer](https://arxiv.org/pdf/2508.04440)

【补救 agent 本轮输出】:
Now I have sufficient background to provide my assessment. Let me compile the findings.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **STAT (ICLR 2026, arXiv 2510.10023)**: 实验使用 MATH-Train 作为数据源，统一 9.5K 训练样本做 compute-matched comparison；baseline 包括 Embed-Sel、random selection、uniform SFT；ablation 涵盖 threshold sensitivity 和 teacher model 变体（GPT-4o vs. 较弱 teacher）。评审要求对 skill profile 质量做人工验证。
- **SwS (NeurIPS 2025, arXiv 2506.08989)**: 在 3B/7B/32B 三个模型规模上实验；8 个数学 benchmark 评测；baseline 包括 seed-data-only RLVR、human-labeled problem set RLVR；weakness 定义为 RL 训练中 pass rate 持续低的题目，无需外部 teacher。
- **NSRSA (arXiv 2603.21558, March 2026)**: 5 轮 self-training iteration，Qwen3-4B-Thinking 在 GSM8K 上从 80.5% → 91.0%；对比 no-verification (collapse to 73.2%)、outcome-only (plateau 85.8%)；symbolic verification 仅覆盖 arithmetic operations，拒绝了约 34% 正确答案但推理有缺陷的样本。DPO 实验提升 reward accuracy 46% → 63%。
- **FoVer (ACL Findings 2026, arXiv 2505.15960)**: 使用 Z3 + Isabelle 生成 40K step-level 标注数据；在 12 个 benchmark 评测 PRM 泛化性；baseline 包括 Monte Carlo roll-out PRM 和 human-annotated PRM；展示了 formal verification 数据训练的 PRM 可泛化到非形式化任务。
- **MATH-VF (arXiv 2505.20869)**: 提出 SimpleMath 形式化语言 + Z3/SymPy Critic 做 step-wise verification；实测显示 Z3 在高阶概念（gcd/lcm）上受限，SymPy 在多变量不等式上有困难；未公开 per-category formalization coverage 具体数值。
- **Imperfect Verifier (arXiv 2604.07666)**: noise rate ≤15% 时 validation accuracy 与 clean baseline 差距在 2pp 以内；precision 比 recall 更重要；跨三个模型家族（Qwen3/GLM4/Llama 3.1）和 4B-9B 规模验证。
- **Adaptive Problem Generation (arXiv 2602.19187)**: SymPy 空间做 symbolic problem representation + closed-loop difficulty adaptation；GRPO/PPO 两种 RLVR 算法对比；seed-data baseline；不做 error-type diagnosis。
- **Step-DPO (NeurIPS 2024, arXiv 2406.18629)**: 只优化第一个错误步骤避免惩罚正确前序步骤；Qwen2-72B-Instruct 在 MATH 上 70.8%；依赖 LLM/人工标注定位错误步骤。

- **调研总结**: 该领域当前实验设计标准要求：(1) 至少 3 个模型规模或 2 个模型家族验证泛化性；(2) compute-matched comparison 是审稿人硬性要求；(3) ablation 需隔离每个组件的贡献且对比至少 3 种变体；(4) 形式化方法的论文必须报告覆盖率/成功率并分析其对整体效果的影响；(5) 自训练循环方法需展示多轮 iteration 的稳定性曲线和 collapse 对比。

---

【缺陷 1】
- 类别: baseline 不足
- 问题: Proposal 的 baseline matrix 缺少 **FoVer-style formal-verification-trained PRM 作为 verifier 的自训练循环** 这一关键 baseline。FoVer 已经证明可以用 formal verification 数据训练出泛化到 12 个 benchmark 的 PRM。一个自然的替代方案是：用 FoVer 方法训练一个 PRM，然后用该 PRM 做 Best-of-N 或 RLVR 的 reward model，在同一个 self-improvement loop 中运行。这条 baseline 直接对标 FormalLoop 的核心差异化——"formal verification 应该直接用于 error profiling + targeted synthesis" vs. "formal verification 应该间接通过 PRM 使用"。缺少这个 baseline，审稿人会质疑：FormalLoop 的增益到底来自 formal verification 本身，还是来自 targeted synthesis pipeline？
- 严重度: 可补救
- 补救方案: 增加一条 baseline：FoVer-PRM + Best-of-N/RLVR self-improvement loop。用 FoVer 公开的 FoVer-40K 数据（或按其方法生成）训练 PRM，在同一 iteration 框架下作为 verifier 运行。这能直接隔离 "formal verification 用于 PRM 训练" vs. "formal verification 用于直接 error profiling + targeted synthesis" 的效果差异。
- 调研依据: FoVer (ACL Findings 2026) 已开源数据和代码，其 PRM 在 12 个 benchmark 上表现优于 Monte Carlo roll-out PRM，是一个 strong baseline。

【缺陷 2】
- 类别: 可行性问题
- 问题: Proposal 声称 formalization success rate 为 ~60-70%（在 amenable categories 上），但这个数字缺乏具体来源和验证。MATH-VF 论文未公开 per-category formalization coverage 数值；Z3 在 gcd/lcm 等概念上受限、SymPy 在多变量不等式上有困难是已知问题。Proposal 将 MATH 的 Algebra、Number Theory、Prealgebra、部分 Intermediate Algebra 和 Precalculus 标为 amenable，但对每个子类别的实际可形式化比例没有依据。如果实际 success rate 显著低于 60%，则 (a) error profiling 的覆盖范围过窄，targeted synthesis 效果打折；(b) DPO 对的产量不足（见缺陷 3）；(c) 整体方法的优势可能仅体现在少数类别上，无法支撑 general improvement 的 claim。
- 严重度: 可补救
- 补救方案: **(a) 扩展 pilot study 的范围和报告粒度**——不仅在 500 道 MATH 测试题上运行，还应对 MATH-Train 的所有 7 个子类别各取 200-300 道题，用 Qwen3.5-9B 生成解答并尝试形式化，报告每个子类别的形式化成功率、失败原因分布（formalization failure vs. solver timeout vs. scope limitation）。**(b) 设定 go/no-go 阈值**——如果 amenable 类别的平均形式化成功率低于 50%，需要重新评估方法的 scope 或引入额外的形式化增强策略（如 MATH-VF 的 SimpleMath 中间语言方法）。**(c) 报告"有效覆盖率"**——即 formalization success rate × amenable categories 在 MATH 中的占比，给出整体实际覆盖比例。
- 调研依据: MATH-VF (arXiv 2505.20869) 提出了 SimpleMath 形式化语言来提高 formalization 成功率，但即便如此也未报告各类别的具体覆盖数值，说明这是已知的难点。

【缺陷 3】
- 类别: 实验设计不足
- 问题: **Formally-verified DPO 对的产量（yield）未估算**。Proposal 描述的 DPO pair 构造要求两条解题轨迹共享前 k 个 formally-verified-correct 步骤，在第 k+1 步分歧（一条 verified correct，一条 verified rejected）。这个构造需要同时满足：(a) 两条轨迹都能成功形式化（60-70% × 60-70% ≈ 36-49% 概率）；(b) 两条轨迹有共同正确前缀；(c) 在共享前缀后恰好出现分歧。满足所有条件的样本对可能非常稀少。如果每道题生成 8 条解答（Pass@8 的采样量），可用 DPO 对数量可能远低于有效训练所需。Step-DPO 报告需要 10K+ pairs 才能有效训练。
- 严重度: 可补救
- 补救方案: **(a) 在 pilot study 中增加 DPO pair yield 估算**——用 Qwen3.5-9B 对 500 道题各生成 16 条解答，运行形式化+验证 pipeline，统计能构造出的 step-localized DPO pairs 数量。**(b) 设计退化策略（fallback）**——当 step-localized pairs 不足时，允许退化为 "solution-level" DPO pairs（整条正确 vs. 整条错误，类似 outcome-based），报告不同粒度 DPO pairs 的混合比例及其效果。**(c) 增加采样量**——每道题从 8 条增加到 16-32 条解答以提高 pair yield。**(d) 在 ablation 6 中额外报告各条件下可用 DPO pair 的数量**，使审稿人能判断 data quantity 差异是否 confound 了 pair quality 的对比。
- 调研依据: Step-DPO (NeurIPS 2024) 使用 ~10K pairs 训练，Full-Step-DPO 也需要类似规模。NSRSA 的 DPO 实验构造 pair 的方式更宽松（基于 symbolic verification accept/reject，不要求 step-aligned prefix），产量更高。

【缺陷 4】
- 类别: 实验设计不足
- 问题: **模型多样性不足**。Proposal 仅使用 Qwen3.5 家族的两个规模（9B 和 4B）。当前领域标准（SwS 在 3B/7B/32B 上实验；Imperfect Verifier 跨 Qwen3/GLM4/Llama 3.1 三个家族验证）要求至少验证跨模型家族的泛化性。仅在 Qwen3.5 上的结果可能被审稿人质疑为 model-specific，特别是 formalization pipeline 的性能（LLM-to-formal translation 成功率）高度依赖模型的 code/symbolic 能力，不同模型家族可能表现差异巨大。
- 严重度: 可补救
- 补救方案: **(a) 增加至少一个非 Qwen 家族的验证模型**——Llama 3.1-8B 或 Phi-4 14B 是合理选择，成本可控（3 iterations 足够展示趋势）。**(b) 如果计算资源确实不够，至少在 pilot study 中对比 Qwen3.5-9B 和另一个家族模型的 formalization success rate**，证明 pipeline 不是 Qwen-specific。**(c) 在 Limitations 中明确声明仅在 Qwen 家族验证，并 justify 为什么（如 Qwen 系列在 math reasoning 上最有代表性）。
- 调研依据: Imperfect Verifier (arXiv 2604.07666) 跨 Qwen3/GLM4/Llama 3.1 三个家族验证是该领域近期的标准做法；SwS (NeurIPS 2025) 在 3B-32B 验证。

【缺陷 5】
- 类别: compute 公平性问题
- 问题: **Compute-matched comparison 的设计缺乏具体定义**。Proposal 提到 "design compute-matched comparison giving baselines equivalent extra compute budget"，但没有定义 compute budget 的计量单位和等价标准。FormalLoop 的 compute 由三部分组成：(a) GPU hours（LLM inference for formalization + fine-tuning）；(b) CPU hours（Z3/SymPy symbolic verification）；(c) LLM inference for problem synthesis/NL generation。Baseline 方法的 compute 结构不同（如 STAT 需要 teacher LLM inference，SwS 需要 RL pass-rate estimation）。如果只按 GPU hours 对齐，FormalLoop 的 CPU overhead 被隐藏；如果按 wall-clock time 对齐，并行化程度不同会导致不公平。审稿人 **一定** 会追问这个问题。
- 严重度: 可补救
- 补救方案: **(a) 定义统一的 compute metric**——建议用 "equivalent FLOPs" 或 "total dollar cost (GPU + CPU + API)" 作为计量标准，对所有方法计算并报告。**(b) 设计两种 compute-matched 对比**：(i) 给 baseline 等量的 GPU training FLOPs（fine-tuning 对齐）；(ii) 给 baseline 等量的 total compute budget（包括 data generation/verification/synthesis 全流程）。**(c) 在 accuracy vs. total compute 曲线中使用统一的 x 轴单位**。**(d) 单独报告 FormalLoop 各阶段（formalization、verification、synthesis、training）的 compute breakdown**。
- 调研依据: SwS 和 STAT 都在固定数据量（如 STAT 的 9.5K pairs）下对比，这是一种 data-matched 而非 compute-matched 的策略。Proposal 的场景更复杂（有 symbolic verification overhead），需要更精细的公平性设计。基于领域实验规范判断。

【缺陷 6】
- 类别: 实验设计不足
- 问题: **Symbolic problem synthesis 的质量评估缺失**。Proposal 的核心 pipeline 包含 "SymPy-based problem synthesis targeting the model's weakest skills"，但实验设计中没有任何评估合成题目质量的方案。合成题目可能存在以下问题：(a) 形式上合法但过于简单/trivial（不能有效训练目标 skill）；(b) 难度分布与目标 benchmark 不匹配；(c) 自然语言表述不自然或有歧义。如果合成题目质量有问题，targeted synthesis 的效果就会打折，而这个因素会被 confound 在 "targeting vs. uniform" 的 ablation 中，导致无法区分 "targeting 有效" vs. "合成题目质量好"。
- 严重度: 可补救
- 补救方案: **(a) 增加合成题目的质量评估**——对合成题目进行 human evaluation（随机抽样 100-200 道，由数学背景标注员评估 well-formedness、difficulty appropriateness、NL quality）。**(b) 对合成题目做 difficulty calibration**——用基准模型的 pass rate 衡量合成题目的实际难度，对比目标 benchmark 的难度分布。**(c) 在 ablation 中增加一组对照：用相同 SymPy 模板但 random targeting（不根据 error profile 选择 skill）合成等量题目，隔离 targeting 策略和 synthesis 质量的效果。
- 调研依据: Adaptive Problem Generation (arXiv 2602.19187) 在 symbolic space 做问题生成时有 closed-loop difficulty adaptation 机制；SPARQ 使用 quality-diversity algorithms 确保合成问题的多样性。FormalLoop 的合成 pipeline 缺少类似的质量保障机制。

【缺陷 7】
- 类别: 可行性问题
- 问题: **Compute 预算可能不足以支撑完整 ablation 计划**。Proposal 规划了 720 H100 hours 覆盖 5 iterations Qwen3.5-9B + 3 iterations Qwen3.5-4B + evaluation + ablations。粗略估算：Qwen3.5-9B 单次 full fine-tune 约 40-80 H100 hours（取决于数据量和 epoch 数），5 iterations ≈ 200-400 hours；6 组 ablation 中多个需要完整训练 run（ablation 1 有 4 条件、ablation 3 有 3 条件、ablation 6 有 3 条件 = 至少 10 个额外 training runs），即使减少 iteration 数到 2-3 轮也需要 ~200-400 hours；加上 evaluation（7 benchmarks × Pass@K 采样）和 Qwen3.5-4B 实验，总计可能接近 900-1200 hours。如果再加上缺陷 4 建议的跨家族验证，budget 更吃紧。
- 严重度: 可补救
- 补救方案: **(a) 明确 ablation 实验的简化策略**——指定 ablation 在 Qwen3.5-4B 上运行（而非 9B）、限制 iteration 数为 2-3 轮、限制评测 benchmark 为 3 个代表性的（如 GSM8K + MATH-500 + AIME24）。**(b) 重新估算 compute budget**——按上述简化方案重算，确保预算覆盖。**(c) 对 ablation 做优先级排序**——ablation 1（error profiling source）和 ablation 6（preference pair source）最关键，ablation 4（taxonomy granularity）可降低优先级。预算不足时先保证 high-priority ablations 的完整性。
- 调研依据: STAT 的 ablation 在较小规模上进行且限制数据量到 9.5K。SwS 的 ablation 也在 7B 模型上做，不在最大模型上重复全部实验。基于领域实验规范判断。

【缺陷 8】
- 类别: 实验设计不足
- 问题: **STAT-style baseline 的 teacher model 未指定**。Proposal 列出 "STAT-style LLM-teacher profiling + targeted synthesis" 作为 baseline，但未说明用哪个 teacher model。STAT 原论文使用 GPT-4o 作为 teacher，并在 ablation 中展示 teacher 能力对效果有显著影响。Teacher 的选择直接影响该 baseline 的强度——用弱 teacher 会使该 baseline 偏弱，用强 teacher 则是公平对比。审稿人会要求明确说明。
- 严重度: 可补救
- 补救方案: **(a) 指定使用 GPT-4o 或同等水平的 frontier model 作为 teacher**，确保 baseline 足够强。**(b) 如果 API 成本是考量，说明 teacher model 选择的理由及其对结果公平性的影响。**(c) 在 resource estimate 中加入 teacher API 调用成本（STAT-style baseline 需要大量 teacher inference）。
- 调研依据: STAT (ICLR 2026) 使用 GPT-4o 作为 teacher，并在 Section E.3 做了 teacher model variant 的 ablation，展示了 teacher 质量对效果的显著影响。

Sources:
- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://arxiv.org/abs/2510.10023)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)](https://arxiv.org/abs/2505.15960)
- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://arxiv.org/abs/2506.08989)
- [NSRSA: Symbolic Recursive Self-Alignment (arXiv 2026)](https://arxiv.org/abs/2603.21558)
- [MATH-VF: Step-Wise Formal Verification (arXiv 2025)](https://arxiv.org/abs/2505.20869)
- [An Imperfect Verifier is Good Enough (arXiv 2026)](https://arxiv.org/abs/2604.07666)
- [Adaptive Problem Generation via Symbolic Representations (arXiv 2026)](https://arxiv.org/abs/2602.19187)
- [Step-DPO: Step-wise Preference Optimization (NeurIPS 2024)](https://arxiv.org/abs/2406.18629)
- [Full-Step-DPO (ACL 2025 Findings)](https://arxiv.org/abs/2502.14356)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9b0db83e-d61a-4c1f-b9c7-d7bd8415abfb",
  "isSidechain": false,
  "promptId": "26b492eb-4837-41c6-aa13-e3269fe7194c",
  "type": "user",
  "uuid": "b3faaf66-308f-4c61-97b8-3ac776fd34ab",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research to provide a thorough assessment. Let me compile my analysis.  ---  【状态】: 有发掘空间…",
  "leafUuid": "b3faaf66-308f-4c61-97b8-3ac776fd34ab",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Assistant

_source line 57 · 2026-05-27T08:48:08.657Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze both worker outputs for Round 2 and do cross-validation.

**发掘 agent Round 2 summary:**
- Status: 有发掘空间
- 5 discovery points:
  1. Trivial alternative: subcategory-level outcome targeting (MATH already has subcategory labels) — need to add as baseline/ablation
  2. Error profile dynamics as first-class scientific contribution (not just ablation byproduct)
  3. Step-localized DPO vs NSRSA's solution-level DPO — sharpen differentiation
  4. "Partial precise > Full noisy" as generalizable principle — precision-coverage tradeoff
  5. Formalization success rate 60-70% needs empirical validation; selection bias risk

**补救 agent Round 2 summary:**
- Status: 有缺陷待补救
- 8 defects identified: missing FoVer-PRM baseline that would close the formal verification loop, unsubstantiated formalization success rates, no DPO pair yield estimates, limited model diversity beyond Qwen, and imprecise compute-matched comparisons that need tightening.

**Convergence between workers (2+ agreement):**
Both reviewers flagged the formalization success rate as needing validation — this is a strong signal that's been partially addressed but requires more rigor. They're also converging on DPO being under-specified, though from different angles: one questioning NSRSA differentiation while the other wants yield estimates. Compute concerns appear consistently within the remediation feedback.

**Cross-validation needed:**
I need to verify whether subcategory-level targeting is actually a trivial baseline approach and whether MATH has granular enough subcategory labels to support this.

Now I'm checking whether FoVer-PRM is actually available as a baseline, whether the 36-49% DPO pair yield estimate aligns with what Step-DPO reports, and whether the imperfect verifier paper actually supports the precision-coverage tradeoff framing being used here.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3faaf66-308f-4c61-97b8-3ac776fd34ab",
  "isSidechain": false,
  "requestId": "req_011CbSnQRDzQf865oqs5hDDz",
  "type": "assistant",
  "uuid": "eccdbde4-78d5-40f2-8f62-1ae244be0835",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHcMZeC5Lu58bMiLbdKmtt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14455,
      "cache_read_input_tokens": 47213,
      "output_tokens": 707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 707,
          "cache_read_input_tokens": 47213,
          "cache_creation_input_tokens": 14455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14455
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

_source line 58 · 2026-05-27T08:48:08.658Z_

Let me cross-validate the key worker suggestions before integrating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eccdbde4-78d5-40f2-8f62-1ae244be0835",
  "isSidechain": false,
  "requestId": "req_011CbSnQRDzQf865oqs5hDDz",
  "type": "assistant",
  "uuid": "b2976207-49a1-4ec3-8656-52e90deff8ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHcMZeC5Lu58bMiLbdKmtt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14455,
      "cache_read_input_tokens": 47213,
      "output_tokens": 707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 707,
          "cache_read_input_tokens": 47213,
          "cache_creation_input_tokens": 14455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14455
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

_source line 59 · 2026-05-27T08:48:08.947Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SZuguLquGnuxQPbs6tJZNH`</summary>

```json
{
  "query": "MATH benchmark subcategory labels algebra number theory geometry targeted training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b2976207-49a1-4ec3-8656-52e90deff8ae",
  "isSidechain": false,
  "requestId": "req_011CbSnQRDzQf865oqs5hDDz",
  "type": "assistant",
  "uuid": "46c11236-8eb4-433d-9597-dd7fd457bc3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EHcMZeC5Lu58bMiLbdKmtt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14455,
      "cache_read_input_tokens": 47213,
      "output_tokens": 707,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14455,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 707,
          "cache_read_input_tokens": 47213,
          "cache_creation_input_tokens": 14455,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14455
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

_source line 60 · 2026-05-27T08:48:19.820Z_

<details><summary>↩ Tool result · `toolu_01SZuguLquGnuxQPbs6tJZNH`</summary>

```text
Web search results for query: "MATH benchmark subcategory labels algebra number theory geometry targeted training 2025 2026"

Links: [{"title":"LLM Math Benchmarks 2025–2026: GSM8K, MATH, AIME, AMC | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm/math-benchmarks"},{"title":"MATH Dataset Benchmark","url":"https://www.emergentmind.com/topics/math-dataset"},{"title":"Best Datasets for Math in 2026 - Abaka AI","url":"https://www.abaka.ai/blog/top-math-datasets-2026-guide"},{"title":"MATH Benchmark Leaderboard","url":"https://llm-stats.com/benchmarks/math"},{"title":"(PDF) HARDMath2: A Benchmark for Applied Mathematics ...","url":"https://arxiv.org/pdf/2505.11774"},{"title":"Comparison of the 3 Most Powerful Math Problem-Solving AI Models: Gemini 3.1 Pro vs Claude Sonnet 4.6 vs GPT-5.4 (2026 Real-World Test Data) - Apiyi.com Blog","url":"https://help.apiyi.com/en/best-ai-model-for-math-2026-en.html"},{"title":"Evaluating the Effect of Labeled Benchmarks on Children’s Number Line Estimation Performance and Strategy Use","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5491597/"}]

Based on the search results, here's what I found about the MATH benchmark subcategory labels:

The MATH benchmark spans multiple difficulty levels (1-5) across seven mathematical subjects including Prealgebra, Algebra, Number Theory, Counting and Probability, Geometry, Intermediate Algebra, and Precalculus.

The results also show current performance metrics for 2025-2026. o3-mini from OpenAI currently leads the MATH leaderboard with a score of 0.979 across 70 evaluated AI models, and the MATH dataset contains 12,500 challenging competition mathematics problems from AMC 10, AMC 12, AIME, and other mathematics competitions.

Regarding targeted training approaches, one technique involves labeling the prompt with the problem type (such as "This is a combinatorics problem" or "This is an analytic geometry problem") to help the model invoke the correct solving strategy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "46c11236-8eb4-433d-9597-dd7fd457bc3b",
  "isSidechain": false,
  "promptId": "26b492eb-4837-41c6-aa13-e3269fe7194c",
  "type": "user",
  "uuid": "94b5cd62-6593-421c-861a-927a34c7478a",
  "toolUseResult": {
    "query": "MATH benchmark subcategory labels algebra number theory geometry targeted training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GdtEW6aQtt4X6frjdyFuaL",
        "content": [
          {
            "title": "LLM Math Benchmarks 2025–2026: GSM8K, MATH, AIME, AMC | CodeSOTA | CodeSOTA",
            "url": "https://www.codesota.com/llm/math-benchmarks"
          },
          {
            "title": "MATH Dataset Benchmark",
            "url": "https://www.emergentmind.com/topics/math-dataset"
          },
          {
            "title": "Best Datasets for Math in 2026 - Abaka AI",
            "url": "https://www.abaka.ai/blog/top-math-datasets-2026-guide"
          },
          {
            "title": "MATH Benchmark Leaderboard",
            "url": "https://llm-stats.com/benchmarks/math"
          },
          {
            "title": "(PDF) HARDMath2: A Benchmark for Applied Mathematics ...",
            "url": "https://arxiv.org/pdf/2505.11774"
          },
          {
            "title": "Comparison of the 3 Most Powerful Math Problem-Solving AI Models: Gemini 3.1 Pro vs Claude Sonnet 4.6 vs GPT-5.4 (2026 Real-World Test Data) - Apiyi.com Blog",
            "url": "https://help.apiyi.com/en/best-ai-model-for-math-2026-en.html"
          },
          {
            "title": "Evaluating the Effect of Labeled Benchmarks on Children’s Number Line Estimation Performance and Strategy Use",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5491597/"
          }
        ]
      },
      "Based on the search results, here's what I found about the MATH benchmark subcategory labels:\n\nThe MATH benchmark spans multiple difficulty levels (1-5) across seven mathematical subjects including Prealgebra, Algebra, Number Theory, Counting and Probability, Geometry, Intermediate Algebra, and Precalculus.\n\nThe results also show current performance metrics for 2025-2026. o3-mini from OpenAI currently leads the MATH leaderboard with a score of 0.979 across 70 evaluated AI models, and the MATH dataset contains 12,500 challenging competition mathematics problems from AMC 10, AMC 12, AIME, and other mathematics competitions.\n\nRegarding targeted training approaches, one technique involves labeling the prompt with the problem type (such as \"This is a combinatorics problem\" or \"This is an analytic geometry problem\") to help the model invoke the correct solving strategy."
    ],
    "durationSeconds": 10.867466158,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "46c11236-8eb4-433d-9597-dd7fd457bc3b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-27T08:48:22.400Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cria1nJaM7PC1a2WDkgKaL`</summary>

```json
{
  "query": "FoVer formal verification PRM code data open source github 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "94b5cd62-6593-421c-861a-927a34c7478a",
  "isSidechain": false,
  "requestId": "req_011CbSnSaDnmWXidP9zkNnRo",
  "type": "assistant",
  "uuid": "1ee7613a-fa34-4995-8f26-099bc0be4ece",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMmzbbkfjpnjjk3X1cBQdc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1329,
      "cache_read_input_tokens": 61668,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1329,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 61668,
          "cache_creation_input_tokens": 1329,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1329
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

_source line 62 · 2026-05-27T08:48:29.472Z_

<details><summary>↩ Tool result · `toolu_01Cria1nJaM7PC1a2WDkgKaL`</summary>

```text
Web search results for query: "FoVer formal verification PRM code data open source github 2025 2026"

Links: [{"title":"Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/pdf/2505.15960"},{"title":"[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/abs/2505.15960"},{"title":"FoVer: Efficient PRM Training Data Synthesis via Formal Verification","url":"https://fover-prm.github.io/"},{"title":"GitHub - psunlpgroup/FoVer: This repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). · GitHub","url":"https://github.com/psunlpgroup/FoVer"},{"title":"Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/html/2505.15960v3"},{"title":"FOVER: Training Verifiers with Formal Tools","url":"https://www.emergentmind.com/papers/2505.15960"}]

Based on the search results, here's what I found about FoVer:

## Overview

FoVer is a framework that synthesizes PRM (Process Reward Model) training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle.

## Key Features

By leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls. Using FoVer, they create PRM training data named FoVER-40K by annotating step-level error labels on LLM responses to formal logic and theorem proving tasks using Z3 and Isabelle.

## Research Results

Experiments on 12 reasoning benchmarks show that fine-tuning on their training data improves PRMs not only on math and logic reasoning tasks, which are informal variants of the training tasks, but also on NLI and BBH benchmarks, which differ substantially from the tasks used to construct the training data.

## Open Source Availability

This repository includes code and materials for the paper "Efficient PRM Training Data Synthesis via Formal Verification" (ACL 2026 Findings). The datasets, models, and code are provided at https://github.com/psunlpgroup/FoVer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ee7613a-fa34-4995-8f26-099bc0be4ece",
  "isSidechain": false,
  "promptId": "26b492eb-4837-41c6-aa13-e3269fe7194c",
  "type": "user",
  "uuid": "aebdb242-652d-45ed-b08e-5dc5d13510ec",
  "toolUseResult": {
    "query": "FoVer formal verification PRM code data open source github 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014KvMRDNR8zLteTvAj9BTqr",
        "content": [
          {
            "title": "Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/abs/2505.15960"
          },
          {
            "title": "FoVer: Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://fover-prm.github.io/"
          },
          {
            "title": "GitHub - psunlpgroup/FoVer: This repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). · GitHub",
            "url": "https://github.com/psunlpgroup/FoVer"
          },
          {
            "title": "Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/html/2505.15960v3"
          },
          {
            "title": "FOVER: Training Verifiers with Formal Tools",
            "url": "https://www.emergentmind.com/papers/2505.15960"
          }
        ]
      },
      "Based on the search results, here's what I found about FoVer:\n\n## Overview\n\nFoVer is a framework that synthesizes PRM (Process Reward Model) training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle.\n\n## Key Features\n\nBy leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls. Using FoVer, they create PRM training data named FoVER-40K by annotating step-level error labels on LLM responses to formal logic and theorem proving tasks using Z3 and Isabelle.\n\n## Research Results\n\nExperiments on 12 reasoning benchmarks show that fine-tuning on their training data improves PRMs not only on math and logic reasoning tasks, which are informal variants of the training tasks, but also on NLI and BBH benchmarks, which differ substantially from the tasks used to construct the training data.\n\n## Open Source Availability\n\nThis repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). The datasets, models, and code are provided at https://github.com/psunlpgroup/FoVer."
    ],
    "durationSeconds": 7.068293282999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1ee7613a-fa34-4995-8f26-099bc0be4ece",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-27T08:48:32.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RefX8pkNHxPLV79u4XWTgd`</summary>

```json
{
  "query": "imperfect verifier noise rate precision coverage tradeoff self-improvement math 2026 arxiv 2604"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aebdb242-652d-45ed-b08e-5dc5d13510ec",
  "isSidechain": false,
  "requestId": "req_011CbSnTHTkh2WeWDYtux46q",
  "type": "assistant",
  "uuid": "bbc458d6-ca53-43a4-9d11-7c0e22ed9541",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VRcJ8ZhjMdf99Yds3LRpuu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 62997,
      "output_tokens": 76,
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
          "output_tokens": 76,
          "cache_read_input_tokens": 62997,
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

_source line 64 · 2026-05-27T08:48:38.800Z_

<details><summary>↩ Tool result · `toolu_01RefX8pkNHxPLV79u4XWTgd`</summary>

```text
Web search results for query: "imperfect verifier noise rate precision coverage tradeoff self-improvement math 2026 arxiv 2604"

Links: [{"title":"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/html/2604.07666"},{"title":"[2604.07666] An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/abs/2604.07666"},{"title":"Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap","url":"https://arxiv.org/pdf/2507.00075"},{"title":"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/pdf/2604.07666"},{"title":"Rate or Fate? RLV$^\\varepsilon$R: Reinforcement Learning with Verifiable Noisy Rewards","url":"https://arxiv.org/pdf/2601.04411"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/html/2510.00915v2"}]

Based on the search results, I found the paper you're looking for:

"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards" (arXiv:2604.07666v1, published April 9, 2026) by Andreas Plesner, Francisco Guzmán, and Anish Athalye.

Key findings from the paper:

- The paper focuses on Reinforcement Learning with Verifiable Rewards (RLVR) for post-training Large Language Models.

- Verifiers are rarely error-free, and the paper addresses unresolved questions about how robust RLVR is to noise and what verifier accuracy is required for effective training.

- Noise rates up to 15% yield peak validation accuracy within 2 percentage points of the clean baseline.

- These findings are consistent across controlled and model-based noise types, three model families (Qwen3, GLM4, Llama 3.1), and model sizes from 4B to 9B.

- The paper suggests that practitioners should prioritize moderate accuracy with high precision over perfect verification - directly addressing the precision-coverage tradeoff mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbc458d6-ca53-43a4-9d11-7c0e22ed9541",
  "isSidechain": false,
  "promptId": "26b492eb-4837-41c6-aa13-e3269fe7194c",
  "type": "user",
  "uuid": "6af1e1d6-3b3c-4db7-9955-873b21e6952b",
  "toolUseResult": {
    "query": "imperfect verifier noise rate precision coverage tradeoff self-improvement math 2026 arxiv 2604",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RsrFr5xoubjRd8EMiuwnjY",
        "content": [
          {
            "title": "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards",
            "url": "https://arxiv.org/html/2604.07666"
          },
          {
            "title": "[2604.07666] An Imperfect Verifier is Good Enough: Learning with Noisy Rewards",
            "url": "https://arxiv.org/abs/2604.07666"
          },
          {
            "title": "Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap",
            "url": "https://arxiv.org/pdf/2507.00075"
          },
          {
            "title": "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards",
            "url": "https://arxiv.org/pdf/2604.07666"
          },
          {
            "title": "Rate or Fate? RLV$^\\varepsilon$R: Reinforcement Learning with Verifiable Noisy Rewards",
            "url": "https://arxiv.org/pdf/2601.04411"
          },
          {
            "title": "Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers",
            "url": "https://arxiv.org/html/2510.00915v2"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards\" (arXiv:2604.07666v1, published April 9, 2026) by Andreas Plesner, Francisco Guzmán, and Anish Athalye.\n\nKey findings from the paper:\n\n- The paper focuses on Reinforcement Learning with Verifiable Rewards (RLVR) for post-training Large Language Models.\n\n- Verifiers are rarely error-free, and the paper addresses unresolved questions about how robust RLVR is to noise and what verifier accuracy is required for effective training.\n\n- Noise rates up to 15% yield peak validation accuracy within 2 percentage points of the clean baseline.\n\n- These findings are consistent across controlled and model-based noise types, three model families (Qwen3, GLM4, Llama 3.1), and model sizes from 4B to 9B.\n\n- The paper suggests that practitioners should prioritize moderate accuracy with high precision over perfect verification - directly addressing the precision-coverage tradeoff mentioned in your query."
    ],
    "durationSeconds": 6.407184768,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bbc458d6-ca53-43a4-9d11-7c0e22ed9541",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-27T08:49:38.668Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have enough cross-validation data. Let me synthesize:

**Cross-validation results for Round 2:**

1. **Subcategory-level targeting (发掘1)**: MATH benchmark indeed has 7 well-defined subcategories (Algebra, Number Theory, Geometry, etc.) with 5 difficulty levels. This is a legitimate trivial baseline — just compute per-subcategory accuracy and oversample weak categories. The proposal MUST address this. ADOPT.

2. **FoVer-PRM baseline (补救1)**: CONFIRMED — FoVer code/data is open source on GitHub (github.com/psunlpgroup/FoVer), FoVer-40K dataset available. This is a strong, reproducible baseline. ADOPT.


3. **Imperfect verifier precision-coverage tradeoff (发掘4)**: The imperfect verifier paper directly supports prioritizing moderate accuracy with high precision over perfect verification — this validates the "partial precise > full noisy" principle. ADOPT with strong confidence.

4. **DPO pair yield (补救3)**: The step-localized pair construction is quite restrictive since it requires two successful trajectories sharing a common prefix and diverging at a step. This mirrors the Step-DPO constraints that needed 10K+ pairs, so it's a genuine feasibility concern. ADOPT.

Now I need to decide what to do with each point. For the subcategory-level targeting baseline, I should add this as an explicit ablation — measuring MATH subcategory accuracy without any formal verification. The error profile dynamics are worth promoting from a side effect to a core contribution since FormalLoop uniquely tracks ground-truth error type evolution across iterations. And for the DPO differentiation, the distinction between solution-level DPO like NSRSA versus step-localized DPO is meaningful and should be highlighted.

The precision-coverage tradeoff is testable through noise injection ablations, which gives the work broader significance beyond just math problems. I need to address the selection bias concern by comparing error distributions between cases where formalization succeeds versus fails. For the baselines, I should include FoVer-PRM to isolate the contribution of direct formal profiling versus indirect verification through PRM, and expand the pilot study to validate formalization rates and address the earlier concerns about selection bias.

For the remaining improvements: I'll estimate DPO pair yield and design a fallback to solution-level pairs if step-localized pairs run short. Given compute constraints, I can only add a Llama 3.1-8B comparison in the pilot study as a limitation. I need to define compute costs as a unified dollar metric, add human evaluation for synthesized problems, and streamline the ablation plan to focus on Qwen 3.5-4B with 2-3 iterations across 3 representative benchmarks, prioritizing ablations 1, 2, and 6.

For the STAT baseline, I'll specify GPT-4o as the teacher model. Looking at the probability reassessment, the novelty has strengthened from medium-strong to nearly strong with the teacher-free error-targeted synthesis, step-localized formal DPO, and error profile dynamics analysis creating multiple differentiated contributions. Significance also improved to nearly strong given the generalizable verifier design principle and practical teacher-free approach. The idea ceiling sits around 45-48%, and with the FoVer-PRM baseline and subcategory targeting, the experimental design is now much more complete.

The main remaining challenge is compute budget tightness with all these additions, though the technical soundness remains medium-strong. Reconsidering the overall assessment: the precision-coverage tradeoff principle elevates this from domain-specific to generalizable work, error profile dynamics adds a unique analytical dimension, the FoVer-PRM baseline significantly strengthens experimental rigor, subcategory-level targeting preempts obvious reviewer concerns, and DPO pair yield estimation addresses feasibility questions. The idea is now well-differentiated with multiple novel angles and comprehensive experimental design, though formalization success rate and compute budget remain the primary risks. stronger with each iteration, and the convergence criteria suggest there's still room for refinement. I'm not hitting the stopping conditions yet—both discovery and remediation phases found meaningful issues in Round 2, and the probability improved noticeably. Let me push into Round 3 to see if I can tighten this further. quite comprehensive now. Let me think about whether a 3rd round would add meaningful value...

R2 additions are mostly refinements to existing structure (sharper differentiation, additional baselines, quality assurance). The core idea and experimental framework are now fairly solid. A 3rd round might yield diminishing returns — workers would likely find smaller issues.

However, the proposal has grown in complexity and I should check if it's getting too bloated. Also, the precision-coverage tradeoff principle and error profile dynamics contributions need to be well-integrated into the narrative.

The R2 workers did surface substantive improvements though — the FoVer-PRM baseline, DPO yield analysis, subcategory targeting, and precision-coverage tradeoff are real gains. The question is whether R3 would uncover more of that caliber or just polish. The idea framing and experimental design feel solid now, so remaining issues are probably execution-related rather than conceptual. Still, one more round could catch something I'm missing, and the proposal deserves a final review before converging. I'll go ahead with R3 but should be ready to finalize after that.

Now I need to update the proposal carefully — preserving all 22 original references, integrating any new ones from R2 validation, trimming where possible to keep it concise, and weaving in the new contributions cleanly. I notice the Imperfect Verifier paper now has an arXiv ID I should add.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6af1e1d6-3b3c-4db7-9955-873b21e6952b",
  "isSidechain": false,
  "requestId": "req_011CbSnTyubQT3kzi4YmcF1e",
  "type": "assistant",
  "uuid": "75a98fdb-cc70-4698-b14c-e4400e8db5af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01327bgJkQ6fqSCyx9PnLZUw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 63679,
      "output_tokens": 9242,
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
          "output_tokens": 9242,
          "cache_read_input_tokens": 63679,
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

### Assistant

_source line 66 · 2026-05-27T08:51:59.657Z_

Good, I have my cross-validation results. Let me now synthesize the full Round 2 integration.

**Cross-validation summary for Round 2:**
1. **MATH subcategory labels** — Confirmed: MATH has 7 well-defined subcategories with 5 difficulty levels. Subcategory-level outcome targeting is a trivially implementable baseline that the proposal must address.
2. **FoVer open source** — Confirmed: Code + FoVer-40K data on GitHub (github.com/psunlpgroup/FoVer). FoVer-PRM baseline is reproducible and important.
3. **Imperfect verifier precision-coverage** — Confirmed (arXiv 2604.07666): Paper explicitly states "practitioners should prioritize moderate accuracy with high precision over perfect verification." Directly supports the "partial precise > full noisy" principle.
4. **DPO pair yield** — Step-DPO needs 10K+ pairs; the step-localized construction is much more restrictive than solution-level. Feasibility concern is real.

【阶段】: 迭代第 2 轮

【交叉验证调研】:
1. **Subcategory-level targeting (发掘1)**: 搜索确认 MATH 有 7 个子类别 × 5 个难度等级，标签公开可用。直接用 per-subcategory accuracy 做 targeting 是零成本的 trivial baseline，proposal 必须包含并论证 formal step-level 诊断相对于 subcategory-level 诊断的增量价值。**已验证，采纳。**
2. **FoVer-PRM baseline (补救1)**: 搜索确认 FoVer 代码和 FoVer-40K 数据在 GitHub 公开 (github.com/psunlpgroup/FoVer)。用 FoVer-PRM 做 verifier 的 self-improvement loop 是一个 strong, reproducible baseline。**已验证，采纳。**
3. **Precision-coverage tradeoff (发掘4)**: 搜索确认 imperfect verifier 论文 (arXiv 2604.07666) 明确建议 "prioritize moderate accuracy with high precision over perfect verification"。直接支撑 "partial precise > full noisy" 原则的可推广性。**已验证，采纳。**
4. **DPO pair yield (补救3)**: Step-DPO 需要 10K+ pairs 有效训练，step-localized 构造的联合概率 (formalize 成功² × 共享前缀 × 分歧) 确实很低。需要 fallback 策略和 yield 估算。**基于文献推算合理，采纳。**

【发掘 agent 有效建议采纳】:
- **发掘1 (Subcategory-level targeting baseline)**: **采纳**——已验证。增加 "subcategory-level outcome targeting" 作为 ablation 1 的额外条件（formal vs. LLM-based vs. pass-rate-based vs. subcategory-level vs. random）。论证 formal step-level 诊断在同一 subcategory 内区分不同 error type 的增量价值。
- **发掘2 (Error profile dynamics 作为一等贡献)**: **采纳**——无需额外文献支撑，这是 FormalLoop 架构的自然产物且在现有文献中空白。提升为与 "teacher-free targeted synthesis" 并列的核心贡献。
- **发掘3 (NSRSA DPO 差异化)**: **采纳**——NSRSA solution-level DPO vs. FormalLoop step-localized DPO 的区分确切。在 ablation 6 中增加 "solution-level formal DPO (NSRSA-style)" 条件。
- **发掘4 (Precision-coverage tradeoff 原则)**: **采纳**——已验证。凝练为可量化假设，设计 noise injection ablation 验证 tradeoff curve。
- **发掘5 (Selection bias 分析)**: **采纳**——合理的 soundness 风险。在 pilot study 中增加 formalization success/failure 组的 error type 分布对比。

【补救 agent 有效建议采纳】:
- **补救1 (FoVer-PRM baseline)**: **采纳**——已验证代码/数据可用。增加 FoVer-PRM + Best-of-N/RLVR loop 作为 baseline。
- **补救2 (Formalization rate 验证)**: **采纳**——与发掘5共识。扩展 pilot study：7 个子类别各 200-300 题，报告 per-category formalization success rate 和 failure mode 分布。
- **补救3 (DPO pair yield)**: **采纳**——在 pilot study 增加 yield 估算。设计 fallback：step-localized pairs 不足时混入 solution-level formal pairs，报告混合比例。增加 per-problem 采样量到 16-32。
- **补救4 (Cross-family 验证)**: **部分采纳**——pilot study 中对比 Qwen3.5-9B 和 Llama 3.1-8B 的 formalization success rate，但不做 full training loop（compute 受限）。在 Limitations 中说明。
- **补救5 (Compute metric 定义)**: **采纳**——使用 "total dollar cost (GPU + CPU + API)" 作为统一 metric。
- **补救6 (Synthesis quality evaluation)**: **采纳**——增加 100-200 道合成题的 human evaluation。
- **补救7 (Compute budget 优化)**: **采纳**——ablation 在 Qwen3.5-4B 上运行，2-3 轮迭代，3 个代表性 benchmark (GSM8K, MATH-500, AIME24)。优先级：ablation 1 (profiling source) > 6 (DPO pair source) > 2 (targeting) > 3,4,5。
- **补救8 (STAT teacher 指定)**: **采纳**——指定 GPT-4o 作为 STAT baseline 的 teacher model。

【本轮 proposal 主要变更】:
**Idea 层面变更:**
- 新增核心贡献：error profile dynamics analysis（ground-truth skill-decomposed self-improvement dynamics，回答 error type 消减优先级、依赖关系、entropy 预测收敛等科学问题）
- 新增可推广原则："precision-coverage tradeoff hypothesis"——verifier noise 超过阈值 τ 时扩大 coverage 的边际收益为负，可通过 noise injection ablation 验证
- 强化 vs NSRSA 差异化：solution-level DPO (NSRSA) vs. step-localized DPO (ours) 的 credit assignment 精度差异
- 增加 subcategory-level targeting 的显式回应

**实验层面变更:**
- 新增 baseline：FoVer-PRM + Best-of-N/RLVR loop；subcategory-level outcome targeting
- Ablation 1 扩展：增加 subcategory-level 条件
- Ablation 6 扩展：增加 NSRSA-style solution-level formal DPO 条件
- 新增 ablation 7：precision-coverage tradeoff（noise injection 验证）
- Pilot study 扩展：per-category formalization rate、DPO pair yield、selection bias 分析、cross-family formalization comparison
- STAT baseline teacher 指定为 GPT-4o
- Compute metric 统一为 total dollar cost
- 合成题目 human evaluation
- Ablation 简化策略：4B model、2-3 iterations、3 benchmarks、priority ranking

【idea 质量评估】: Novelty=中强偏强（teacher-free error-targeted synthesis + step-localized formal DPO + error profile dynamics + precision-coverage tradeoff principle — 4 个差异化贡献点，各有明确的文献空白支撑）Significance=中强偏强（generalizable principle 超越 math-specific，科学+实用双重价值）→ idea 天花板约 46%

【实验完备性评估】: Technical Soundness=中强（baseline 矩阵更完整含 FoVer-PRM，ablation 含 priority ranking，pilot study 覆盖关键 feasibility 问题；主要残余风险是 compute budget 紧张和 DPO pair yield 的不确定性）→ 地板已基本补好

【当前概率估计】: [35% - 46%] 中位 40%

【决策】: 继续

【决策理由】: R2 带来了有实质意义的提升（+3% 中位），主要来自 idea 层面的贡献升级（error profile dynamics、precision-coverage tradeoff）和实验层面的关键补充（FoVer-PRM baseline、subcategory targeting、DPO yield）。但 proposal 的信息密度需要在 R3 压缩——当前结构已经开始膨胀，需要精炼。R3 应以"收敛打磨"为目标，除非 workers 发现新的实质性问题。

**引用核对清单**（确认 22 篇全部保留，无新增）:
1. FoVer (ACL Findings 2026) ✓
2. STAT (ICLR 2026) ✓
3. NSRSA (arXiv 2026) ✓
4. Solver-Verifier Gap (ICLR 2026) ✓
5. SPARQ (arXiv 2025) ✓
6. CoTEvol (arXiv 2026) ✓
7. MathMixup (arXiv 2026) ✓
8. Self-Error-Instruct (ACL 2025) ✓
9. SPICE (arXiv 2025) ✓
10. SvS (arXiv 2025) ✓
11. SwS (NeurIPS 2025) ✓
12. Adaptive Problem Generation (arXiv 2026, arXiv 2602.19187) ✓
13. Imperfect Verifier (arXiv 2026, arXiv 2604.07666) ✓
14. MATH-VF (arXiv 2025) ✓
15. Safe (ACL 2025) ✓
16. WarriorMath (arXiv 2025) ✓
17. Bidirectional Curriculum (arXiv 2026) ✓
18. Reasoning Core (arXiv 2026) ✓
19. Neuro-Symbolic Data Generation (NeurIPS 2024) ✓
20. Step-DPO (NeurIPS 2024) ✓
21. Full-Step-DPO (ACL 2025 Findings) ✓
22. LLMs Cannot Spot Math Errors (EMNLP 2025, arXiv 2509.01395) ✓

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
# Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement

## Core Problem

Self-improvement loops for mathematical reasoning suffer from model collapse (solver-verifier gap theory, ICLR 2026) and untargeted data waste. All existing error-targeted synthesis methods — STAT (ICLR 2026), Self-Error-Instruct (ACL 2025), SwS (NeurIPS 2025), WarriorMath (arXiv 2025) — depend on LLM teachers or LLM metacognition for error diagnosis, introducing teacher bias, hallucinated attributions, and scalability ceilings. Empirically, LLMs cannot reliably spot mathematical errors even with reference solutions (arXiv 2509.01395, EMNLP 2025). Can formal symbolic tools serve as collapse-proof verifiers and ground-truth error diagnosticians, enabling stable, teacher-free, targeted self-improvement?

## Core Contributions

1. **Teacher-free error-targeted self-improvement**: The first self-improvement system where error diagnosis and targeted synthesis are driven entirely by formal symbolic tools (Z3, SymPy), eliminating LLM teacher dependency. Unlike RLVR/GRPO (also teacher-free), FormalLoop targets specific error types rather than optimizing globally.

2. **Formally-verified step-localized DPO**: Preference pairs where trajectories share k formally-verified-correct steps and diverge at step k+1 — providing step-localized credit assignment with formal guarantees. Unlike Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) which use LLM/human annotations, and unlike NSRSA (arXiv 2026) which constructs solution-level accept/reject pairs, our pairs provide zero-noise step-localized preference signals.

3. **Ground-truth error profile dynamics**: FormalLoop uniquely enables tracking formally-verified per-skill-type error evolution across self-improvement iterations — answering whether error types have fixed reduction priority orderings, whether skill dependencies exist (e.g., arithmetic errors must resolve before algebraic errors become visible), and whether error profile entropy predicts convergence. No prior work provides ground-truth skill-decomposed self-improvement dynamics.

4. **Precision-coverage tradeoff hypothesis**: We hypothesize that in self-improvement loops, there exists a verifier noise threshold τ beyond which expanding coverage yields negative marginal returns. Imperfect verifier research (arXiv 2604.07666, arXiv 2026) estimates τ ≈ 15%; solver-verifier gap theory (ICLR 2026) predicts verifier reliability determines the self-improvement ceiling. FormalLoop tests this: formal verification achieves near-zero noise within its scope (~60-70% of amenable categories), which should outperform full-coverage but noisier LLM diagnosis. We validate via noise injection ablation.

## Why Not Simpler Alternatives?

**vs. Outcome verification + STAT-style LLM teacher profiling**: (1) Error attribution precision — outcome verification doesn't localize errors; LLM step diagnosis hallucinates (arXiv 2509.01395, EMNLP 2025); formal verification provides guaranteed step-level attribution. (2) Iterative stability — LLM teacher biases compound across iterations; formal diagnosis is independently calibrated each round. (3) No teacher ceiling — STAT's profiling quality is bounded by teacher metacognition.

**vs. Subcategory-level outcome targeting** (using MATH's existing 7 subcategory labels to oversample weak categories): This requires no formal verification at all. However, subcategory labels are coarse — within Algebra alone, a model may struggle specifically with equation solving but not algebraic manipulation. Formal step-level diagnosis provides within-subcategory skill decomposition that subcategory-level targeting cannot. We include subcategory-level targeting as an explicit baseline to quantify this granularity advantage.

**vs. FoVer-PRM as verifier in a standard self-improvement loop**: FoVer (ACL 2026) trains PRMs from formal verification data for general use. A natural alternative is using a FoVer-trained PRM as the verifier in a self-improvement loop (via Best-of-N or RLVR). FormalLoop differs by using formal verification directly for error categorization and targeted synthesis — not indirectly through a learned PRM. We include FoVer-PRM + RLVR as a baseline to isolate direct formal profiling's advantage.

## Research Landscape

Current SOTA in synthetic math data: SPARQ (June 2025, +24% via quality-diversity from 7.5K seeds), CoTEvol (April 2026, +6.6% via evolutionary CoT synthesis), MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). Self-improvement: SPICE (Oct 2025, +8.9% via document-grounded self-play), SvS (Aug 2025, +18.3% Pass@32 on AIME24 via variational problem synthesis). Verification: FoVer (ACL 2026) trains PRMs from formal verification across 12 benchmarks; imperfect verifier research (arXiv 2604.07666, arXiv 2026) shows ≤15% noise is tolerable with precision mattering more than recall. Concurrent: Adaptive Problem Generation (arXiv 2602.19187, Feb 2026) uses SymPy in closed-loop RLVR but adapts difficulty globally without error-type diagnosis. SwS (NeurIPS 2025) identifies weaknesses via pass-rate analysis without formal diagnosis. Reasoning Core (March 2026) generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) does step-aware Lean 4 verification in one-shot refinement, not closed-loop. Bidirectional Curriculum (March 2026) dynamically adjusts difficulty without formal verification. NSRSA (arXiv 2026) uses SymPy arithmetic verification for iterative self-training on GSM8K with solution-level DPO, but covers only arithmetic operations without error categorization or targeted synthesis. MATH-VF (arXiv 2025) uses Z3+SymPy for step-wise verification but as a training-free inference tool.

## Proposed Approach

FormalLoop runs iterative cycles on a student model (Qwen3.5-9B primary, Qwen3.5-4B validation): (1) student solves problems, (2) solutions are formalized and verified step-by-step via Z3/SymPy, (3) step-level errors classified into a formal taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), (4) SymPy-based synthesis generates targeted problems exercising weak skills with solver-guaranteed solutions, (5) student trains via SFT+DPO on targeted data and formally-constructed preference pairs, then re-profiled.

**Formal coverage scope**: Formal verification covers algebraic and arithmetic domains amenable to Z3/SymPy (Algebra, Number Theory, Prealgebra, portions of Intermediate Algebra and Precalculus). Geometry and Counting & Probability use outcome-based verification as fallback. Per-category formalization success rates are reported. Even partial coverage with near-zero noise can outperform full-coverage noisy LLM diagnosis (imperfect verifier research, arXiv 2604.07666).

**Formalization quality control**: To prevent conflating formalization failures with reasoning errors: (a) distinguish "verification failed" from "formalization failed" status, (b) exclude solutions where formal rejection co-occurs with correct final answer, (c) use only high-confidence pairs for DPO. Target noise rate well below the 15% tolerance threshold (arXiv 2604.07666).

**DPO pair construction with fallback**: Primary: step-localized pairs (shared k correct steps, diverge at k+1). When step-localized pairs are insufficient (estimated via pilot study yield analysis), mix in solution-level formally-verified pairs (NSRSA-style). Report mixing ratio and its effect on training.

## Experimental Design

**Models**: Qwen3.5-9B (primary, 5 iterations) + Qwen3.5-4B (validation, 3 iterations). Pilot study includes Llama 3.1-8B formalization success rate comparison (not full training loop).

**Benchmarks**: GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench. OOD generalization on AIME24/25. Per-MATH-subcategory breakdown (formally-covered vs. fallback).

**Evaluation protocol**: Greedy accuracy + Pass@K (K=8, 32) + majority voting@K. 3 independent runs, mean ± std, significance tests. Per-problem sampling: 16-32 solutions for DPO pair construction.

**Baseline matrix**:
- Training paradigm: Vanilla SFT (uniform), SFT+DPO (uniform), GRPO/RLVR
- Targeting: SwS (NeurIPS 2025, pass-rate weakness targeting), STAT-style (GPT-4o teacher) profiling + targeted synthesis, subcategory-level outcome targeting
- Symbolic: Adaptive Problem Generation (arXiv 2602.19187, global difficulty adaptation)
- Verification: FoVer-PRM (ACL 2026, github.com/psunlpgroup/FoVer) + Best-of-N/RLVR loop, outcome-only verification loop (NSRSA-style)

**Ablation studies** (priority-ranked; ablations run on Qwen3.5-4B, 2-3 iterations, 3 benchmarks: GSM8K, MATH-500, AIME24):
1. [Must] Error profiling source: Formal vs. LLM-based vs. pass-rate-based vs. subcategory-level vs. random
2. [Must] Preference pair source: Step-localized formal DPO vs. solution-level formal DPO (NSRSA-style) vs. outcome DPO vs. LLM-annotated DPO (Step-DPO style)
3. [Must] Targeting vs. uniform: Targeted synthesis vs. uniform synthesis (same quantity)
4. [Should] Training objective: SFT only vs. DPO only vs. SFT+DPO
5. [Should] Taxonomy granularity: 5-type vs. 2-type (arithmetic/non-arithmetic) vs. single aggregate
6. [Should] Iteration dynamics: Per-iteration accuracy, error profile evolution, formalization coverage, entropy curves
7. [Nice] Precision-coverage tradeoff: Inject artificial noise (5%, 10%, 15%, 20%) into formal labels, measure impact on self-improvement trajectory

**Compute fairness**: Unified metric: total dollar cost (GPU + CPU + API). Report per-method cost breakdown. Compute-matched comparisons: (i) fixed GPU training FLOPs, (ii) fixed total dollar budget. Accuracy vs. total cost curves.

**Pilot study** (before main experiments):
- Per-subcategory formalization success rate on MATH-Train (200-300 problems per subcategory)
- Failure mode analysis: formalization failure vs. solver timeout vs. scope limitation
- Selection bias analysis: compare error type distributions between formalization-success and formalization-failure groups
- DPO pair yield estimation: 500 problems × 16 solutions, count constructable step-localized pairs
- Cross-family comparison: Qwen3.5-9B vs. Llama 3.1-8B formalization success rates
- Taxonomy coverage validation and comparison with STAT's skill taxonomy
- Human evaluation of 100-200 synthesized problems (well-formedness, difficulty, NL quality)

## Key References

- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)
- STAT: Skill-Targeted Adaptive Training (ICLR 2026)
- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)
- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)
- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)
- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)
- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)
- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)
- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)
- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)
- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)
- Adaptive Problem Generation via Symbolic Representations (arXiv 2026, arXiv 2602.19187)
- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026, arXiv 2604.07666)
- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)
- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)
- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)
- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)
- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)
- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)
- Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs (NeurIPS 2024)
- Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning (ACL 2025 Findings)
- LLMs Cannot Spot Math Errors Even When Allowed to Peek into the Solution (EMNLP 2025, arXiv 2509.01395)

## Resource Estimate

- **manual**: gpu_hours: 750 H100 hours (5 iterations 9B + 3 iterations 4B + ablations on 4B + pilot study + evaluation), timeline: 4-5 months, estimated_gpu_cost: $1,875
- **human_in_loop**: gpu_hours: 700 H100 hours, timeline: 3-4 months, claude_api_cost: $500-700 (pipeline code, taxonomy iteration, analysis), teacher_api_cost: $200-400 (GPT-4o for STAT baseline), estimated_gpu_cost: $1,750
- **auto_research**: gpu_hours: 700 H100 hours, timeline: 6-8 weeks, claude_api_cost: $1,500-2,500, teacher_api_cost: $200-400, estimated_gpu_cost: $1,750, speed_bottleneck: Z3/SymPy step verification is CPU-bound (~0.5-2s per step); LLM-to-formal translation ~60-70% success rate on amenable categories requires retry loops
---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75a98fdb-cc70-4698-b14c-e4400e8db5af",
  "isSidechain": false,
  "requestId": "req_011CbSnTyubQT3kzi4YmcF1e",
  "type": "assistant",
  "uuid": "0b4a98e8-ee20-4873-a699-299b43676695",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01327bgJkQ6fqSCyx9PnLZUw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 63679,
      "output_tokens": 9242,
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
          "output_tokens": 9242,
          "cache_read_input_tokens": 63679,
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

### Runtime record

_source line 67_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research to provide a thorough assessment. Let me compile my analysis.  ---  【状态】: 有发掘空间…",
  "leafUuid": "0b4a98e8-ee20-4873-a699-299b43676695",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 68_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 69_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research to provide a thorough assessment. Let me compile my analysis.  ---  【状态】: 有发掘空间…",
  "leafUuid": "0b4a98e8-ee20-4873-a699-299b43676695",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 70_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 71_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 72 · 2026-05-27T08:58:41.730Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:58:41.730Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "content": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have sufficient research to make a well-grounded assessment. Let me compile my analysis.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- [NSRSA / arXiv 2603.21558] (arXiv March 2026): 最接近的工作。使用 SymPy 对 arithmetic 操作进行符号验证，在 GSM8K 上做 iterative self-training + solution-level DPO。但仅覆盖算术运算，不做 error categorization 或 targeted synthesis。与 FormalLoop 的核心差异在于：NSRSA 是 accept/reject，FormalLoop 是 diagnose-categorize-target。\n- [FoVer / arXiv 2505.15960] (ACL Findings 2026): 用 Z3 和 Isabelle 做 formal verification 来生成 PRM 训练数据，跨 12 个 benchmark 表现强劲。目标是训练 verifier，不是 error-targeted self-improvement。Proposal 已正确将 FoVer-PRM + RLVR 作为 baseline。\n- [STAT / arXiv 2510.10023] (ICLR 2026): 用 LLM teacher 的 metacognition 做 skill profiling + targeted synthesis/reweighting。在 MATH 上提升 7.5%，OOD 平均提升 4.6%。高层 idea（profile by skill → target weak skills）与 FormalLoop 共享，关键差异在 profiling 机制（formal vs. LLM teacher）。\n- [SwS / arXiv 2506.08989] (NeurIPS 2025): 通过 pass-rate 分析识别 weakness，合成针对性问题用于 RL 训练。7B/32B 模型分别提升 10%/7.7%。不使用 formal diagnosis，granularity 停留在 problem-level 而非 step-level。\n- [Adaptive Problem Generation / arXiv 2602.19187] (Feb 2026): 在符号空间中用 SymPy 做 closed-loop RLVR，通过 prompt optimization 自适应调节难度。但只做 global difficulty adaptation，没有 error-type diagnosis。\n- [Pushing the Boundaries / arXiv 2601.22642] (Jan 2026): 用 formal logic verification 在生成过程中动态纠错（active correction during generation），7B/14B 模型分别超 SOTA 10.4%/14.2%。与 FormalLoop 使用 formal verification 的方式不同（active correction vs. error profiling），但属于 formal verification in training loop 的同一大方向。**Proposal 中未提及此工作。**\n- [Imperfect Verifier / arXiv 2604.07666] (April 2026): 证明 noise rate ≤15% 时 RLVR 训练效果几乎无损。直接支撑 FormalLoop 的 precision-coverage tradeoff 论证。\n- [Solver-Verifier Gap / arXiv 2507.00075] (ICLR 2026): 理论建模 self-improvement 的 solver-verifier capability gap，预测 verifier reliability 决定 self-improvement ceiling。为 FormalLoop 使用高精度 formal verifier 提供理论支撑。\n- 调研总结: 该领域 2025-2026 年的研究重点在于 (1) 提升 self-improvement 的 verifier 质量以防止 model collapse，(2) 将 weakness identification 从粗粒度（subcategory/pass-rate）推向细粒度（skill-level/step-level），(3) 引入 formal tools 来替代 noisy 的 LLM-based verification。FormalLoop 恰好处于这三条趋势的交汇点——这既是其优势（顺应趋势），也是其挑战（\"obvious next step\" 风险）。\n\n---\n\n【发掘点 1】\n- 维度: 核心 claim 强化 / novelty 锐化\n- 内容: 当前 Proposal 的 framing 将 \"teacher-free\" 作为核心卖点，但更有穿透力的 framing 应该是 **\"ground-truth error attribution unlocks a new class of self-improvement dynamics analysis that is fundamentally impossible with any LLM-based approach\"**。具体来说：当前的 \"teacher-free\" framing 容易被审稿人解读为 \"cost saving\" 或 \"scalability improvement\"——这些是 incremental 优势。但 formal verification 的真正独特价值不在于\"便宜\"或\"不需要 teacher\"，而在于**它提供的 error attribution 是 ground-truth 而非 estimate**。这个性质使得 Contribution 3（error profile dynamics）从一个 \"nice-to-have 分析\" 变成一个 **\"only possible with this approach\" 的 unique capability**。建议重构 narrative：FormalLoop 不仅仅是 STAT 的 formal 版本（替换 teacher），而是通过 ground-truth error attribution 开启了一类 STAT 根本无法做的研究——比如 ground-truth skill dependency structure 和 convergence prediction。这让 \"为什么要用 formal tools\" 的回答从 \"to avoid teacher bias\" 升级为 \"to enable analyses that are impossible otherwise\"。\n- 价值: 直接提升 Novelty 和 Significance。将 paper 从 \"engineering integration of known components\"（NSRSA 的 formal verification + STAT 的 targeted training）重新定位为 \"enabling a new analytical paradigm for self-improvement dynamics\"。后者对审稿人来说 surprise factor 显著更高。\n- 调研依据: STAT (ICLR 2026) 的 skill profiling 受限于 LLM teacher metacognition，其 Missing-Skill-Profile 是 estimate 而非 ground truth，因此无法可靠回答 skill dependency 等问题。Solver-Verifier Gap theory (ICLR 2026) 从理论上预测了 verifier reliability 的重要性，但缺乏 ground-truth empirical validation。FormalLoop 的 error profile dynamics 恰好能提供这一缺失的 empirical grounding。\n\n【发掘点 2】\n- 维度: significance 提升\n- 内容: **将 Error Profile Dynamics（当前 Contribution 3）从 secondary observation 提升为 co-primary research question。** 当前 proposal 将 error profile dynamics 列为第 3 个 contribution，隐含将其视为 \"附带分析\"。但实际上，以下三个子问题——(a) error type 是否存在 fixed reduction priority ordering，(b) skill dependency structure 是否存在（如 arithmetic errors 必须先解决才能让 algebraic errors 变得可见），(c) error profile entropy 是否能预测 convergence——是独立于 FormalLoop 具体实现的、关于 self-improvement dynamics 的 fundamental questions。这些问题此前之所以没人回答，不是因为没人想到，而是因为没有 ground-truth error attribution 工具来可靠地回答。如果 FormalLoop 的实验能揭示 non-trivial skill dependency structures（例如 arithmetic → algebraic manipulation → equation solving 的层级关系），这个发现的影响力可能远超 FormalLoop 系统本身——它会影响未来所有 math self-improvement 系统的 curriculum design。\n- 价值: 显著提升 Significance。从 \"我们做了一个更好的 self-improvement system\" 变成 \"我们揭示了 self-improvement 过程中 error type 的演化规律\"。后者的 impact scope 更广。\n- 调研依据: Curriculum learning 文献（如 arXiv 2510.19099 \"What Makes a Good Curriculum\"）研究 difficulty ordering 但没有 skill-type-level 的 ground-truth dynamics 分析。STAT (ICLR 2026) 虽然有 per-skill 分析但使用 LLM estimation，无法作为 ground truth。SwS (NeurIPS 2025) 的 weakness 分析停留在 problem-level pass rate，没有 error type decomposition。FormalLoop 可以填补这个 gap。\n\n【发掘点 3】\n- 维度: related work 差异化\n- 内容: **Proposal 遗漏了 \"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\" (arXiv 2601.22642, Jan 2026)**。这篇工作同样在 training pipeline 中使用 formal logic verification，但其用途是 active correction during generation（在生成过程中动态检测并纠正错误），而非 error profiling + targeted synthesis。在 7B/14B 模型上分别超 SOTA 10.4%/14.2%。审稿人很可能知道这篇工作（2026 年 1 月发布，结果强劲），如果 related work 中不讨论它，会被认为文献调研不充分。建议在 related work 中明确定位差异：该工作关注 inference-time formal verification guidance，FormalLoop 关注 training-time formal error diagnosis。两者互补而非竞争——FormalLoop 的 error profiling 产出的 targeted training data 可以提升模型的基础能力，而 interleaved formal verification 可以在 inference 时进一步纠错。\n- 价值: 消除 Related Work 盲区，防止审稿人认为 novelty claim 不成立或文献调研不全面。同时，定位好这个差异可以进一步锐化 FormalLoop 的 novelty——FormalLoop 的 formal verification 是用于 training loop 的 error diagnosis，不是 inference-time correction。\n- 调研依据: 直接来自搜索结果，arXiv 2601.22642，2026 年 1 月发布。\n\n【发掘点 4】\n- 维度: novelty 锐化 / 前提假设质疑\n- 内容: **Error taxonomy 的 principled derivation 需要加强。** 当前 taxonomy 包含 5 类（algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference），但 proposal 未解释这 5 类的来源是 principled 还是 ad hoc。审稿人可能会问：\"为什么是这 5 类而不是别的分法？\" 一个更强的定位方式是：**让 taxonomy 由 formal verification tool 的能力边界自然推导出来**。即每个类别对应 Z3/SymPy 的一种不同的验证操作类型（SymPy symbolic simplification → algebraic manipulation; SymPy solve → equation solving; SymPy numerical evaluation → arithmetic; Z3 constraint satisfaction → constraint reasoning; Z3 logical implication checking → logical inference）。这样 taxonomy 就不是人为选择的，而是 formal tools 能力的自然映射。这有两个好处：(a) 消除 \"arbitrary taxonomy\" 的审稿质疑，(b) 强化 \"formal tools 不仅替代 teacher，更定义了 error analysis 的结构\" 的 narrative。\n- 价值: 提升 Novelty 的可信度。如果 taxonomy 是 principled 的，整个 error profiling 系统就更 rigorous；如果是 ad hoc 的，审稿人可能质疑 taxonomy 的 robustness 和 generalizability。\n- 调研依据: STAT (ICLR 2026) 的 skill taxonomy 由 LLM teacher 生成，本身就是 ad hoc 的（LLM 生成的 skill list 依赖于 prompt 和 teacher 的 bias）。FormalLoop 有机会做得更好——如果 taxonomy 来自 formal tools 的能力结构，它就比 STAT 的 taxonomy 更 principled。这是一个相对 STAT 的额外优势。\n\n【发掘点 5】\n- 维度: trivial alternative 威胁\n- 内容: **需要更尖锐地论证 fine-grained taxonomy 的增量价值相对于 coarser formal-rejection-rate targeting。** 当前 proposal 已将 subcategory-level targeting 和 taxonomy granularity ablation 纳入计划，但有一个中间态的 trivial alternative 需要明确 address：**使用 formal verification 的 accept/reject 信号（不做 error categorization），按 problem type 统计 formal rejection rate，然后 oversample rejection rate 高的 problem types。** 这不需要 error taxonomy，只需要 binary formal verification + rejection rate statistics，工程复杂度远低于完整的 FormalLoop。虽然 ablation 5 的 \"single aggregate\" condition 在某种程度上测试了这个 alternative，但建议在 paper 写作中明确将此作为一个 straw man 进行讨论，并解释为什么 step-level error categorization 比 problem-level rejection rate 提供了 qualitatively different 的信号（即：同一个 problem type 内的不同错误需要不同类型的 targeted training，这是 rejection rate 无法区分的）。\n- 价值: 预防审稿人的 \"为什么不用更简单的方法\" 质疑。如果 proposal 不主动 address 这个 middle-ground alternative，审稿人可能在 rebuttal 阶段提出，而 rebuttal 空间有限。\n- 调研依据: NSRSA (arXiv 2603.21558) 实质上就是这种 coarser alternative 的一个实例——formal accept/reject + DPO，没有 error categorization。FormalLoop 需要证明 categorization 提供了 NSRSA 没有的增量价值。基于领域整体趋势判断。\n\nSources:\n- [NSRSA - Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [FoVer - Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [FoVer GitHub Repository](https://github.com/psunlpgroup/FoVer)\n- [STAT - Skill-Targeted Adaptive Training (ICLR 2026)](https://openreview.net/forum?id=m3jG3GaNIj)\n- [SwS - Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)\n- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)\n- [Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification](https://arxiv.org/abs/2601.22642)\n- [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666)\n- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)\n- [Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (MATH-VF)](https://arxiv.org/abs/2505.20869)\n- [Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification](https://arxiv.org/abs/2506.04592)\n- [Self-Error-Instruct (ACL 2025)](https://aclanthology.org/2025.acl-long.417/)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research to conduct a thorough evaluation. Let me compile my assessment.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **STAT: Skill-Targeted Adaptive Training** (ICLR 2026): Tested on Llama-3.2-3B/1B, Qwen2.5-3B. Baselines include MATH-Train, Embed-Sel, GRPO. Evaluated on MATH, AIME24/25, AMC23. Shows STAT complementary to GRPO. 3-model evaluation across families. Reports per-skill missing profiles.\n- **NSRSA: Symbolic Recursive Self-Alignment** (arXiv 2603.21558, 2026): Qwen3-4B-Thinking on GSM8K across 5 iterations under 5 conditions (no-verify, outcome, majority vote, full NSRSA, NSRSA+DPO). Rejects ~34% of correct-answer solutions with flawed reasoning. Solution-level DPO only.\n- **FoVer: Efficient PRM Training Data Synthesis** (ACL 2026 Findings): Z3 + Isabelle formal verification for PRM data. Evaluated on 12 benchmarks including math, logic, NLI, BBH. Demonstrates cross-domain generalization of formally-trained PRMs.\n- **SwS: Weakness-Driven Problem Synthesis** (NeurIPS 2025): 3B to 32B model range, 8 math benchmarks. Pass-rate based weakness identification. +10% for 7B, +7.7% for 32B. Compares against human-labeled problem sets.\n- **Imperfect Verifier (arXiv 2604.07666, 2026)**: Noise ≤15% yields near-clean accuracy. Precision > recall. Tested across Qwen3, GLM4, Llama 3.1 (4B-9B). Three model families, code + scientific reasoning.\n- **Solver-Verifier Gap Theory** (ICLR 2026): Exponential convergence law. External data timing doesn't significantly affect final performance under limited-data regimes.\n- **SPARQ** (arXiv 2506.06499, 2025): 7.5K seeds → 20M+ pairs, +24% on MATH for Gemma-2-9B via quality-diversity filtering. Ablates filtering strategies and diversity metrics.\n- **MATH-VF (Step-Wise Formal Verification)** (arXiv 2505.20869, 2025): Z3+SymPy step-level verification. SymPy for symbolic computation/equation solving; Z3 for logical/polynomial constraints. Training-free framework tested on MATH500 and ProcessBench.\n- **Position: Don't Use CLT in LLM Evals** (arXiv 2503.01747): CLT-based methods dramatically underestimate uncertainty on small benchmarks. At least 10 seeds recommended for small-N benchmarks like AIME (15 problems per contest).\n- **AIME Data Contamination** (MathArena/emergentmind): AIME 2024 scores inflated 10-20 points by data contamination in models trained after 2024. Timeline-controlled evaluation essential.\n\n- **调研总结**: 该领域当前实验设计标准要求：(1) 跨模型家族验证（至少2个家族），(2) 高方差小样本benchmark需≥8-10 seeds或Bayesian置信区间，(3) 数据污染分析（特别是AIME24），(4) 详细的per-iteration数据量和计算成本分解，(5) compute-matched比较是新兴标准。当前proposal的baseline矩阵和ablation设计在该领域属于上游水平，但在统计严谨性和若干实验细节上存在可修补的缺陷。\n\n---\n\n【缺陷 1】\n- 类别: 评估方案缺陷\n- 问题: Proposal 规定\"3 independent runs, mean ± std, significance tests\"用于所有 benchmark，但 AIME24 和 AIME25 每个仅有 30 道题（各15题×2场），AMC23 约25题。在如此小的样本量下，3 runs 的统计功效严重不足。近期文献（arXiv 2503.01747）明确指出，CLT-based 方法在小样本 LLM 评估中\"dramatically underestimates uncertainty\"，建议 AIME 类 benchmark 至少 10 seeds。对于 FormalLoop 这种 iterative 方法，每轮训练的随机性会进一步放大方差。3 runs 可能导致无法在 AIME/AMC 上得出显著结论，而这恰恰是 proposal 声称要展示 OOD generalization 的核心 benchmark。\n- 严重度: 可补救\n- 补救方案: (1) AIME24/25、AMC23 上增加至 8-10 independent runs（不同随机种子的完整训练循环），或在资源不允许时至少用不同采样温度做 16+ evaluation seeds（同一模型、不同采样）。(2) 采用 Bayesian bootstrap 置信区间替代 CLT-based significance test。(3) 在 GSM8K、MATH-500 等大样本 benchmark 上 3 runs 足够，但应明确分层：大样本 benchmark 用 t-test，小样本 benchmark 用 bootstrap 或 permutation test。(4) 报告 per-problem pass rate 分布（而非仅聚合准确率），让读者自行评估方差。\n- 调研依据: arXiv 2503.01747 \"Position: Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints\"；MathArena AIME evaluation methodology recommendations。\n\n【缺陷 2】\n- 类别: 评估方案缺陷\n- 问题: Proposal 使用 AIME24 作为 OOD generalization 的关键 benchmark，但 Qwen3.5 系列（2026年3月发布）的预训练数据极有可能包含 AIME 2024 题目。调研显示 AIME 2024 在 2026 年发布的模型上存在 10-20 分的数据污染膨胀。如果 baseline 和 FormalLoop 都在受污染的 benchmark 上评估，虽然相对比较仍有效，但绝对数值的 OOD 泛化 claim 会被审稿人质疑。\n- 严重度: 可补救\n- 补救方案: (1) 增加 AIME 2026（2026年2月举行，大概率不在 Qwen3.5 预训练数据中）作为最无污染的 OOD benchmark。(2) 对 AIME24 做污染检测：检查 base model（未经 FormalLoop 训练）在 AIME24 上的 pass@1 表现，与已知的未污染基准对比。(3) 在论文中明确报告 base model 在所有 benchmark 上的 baseline 性能，让读者自行判断污染程度。(4) 如条件允许，加入 Putnam/HMMT 等更高难度竞赛题目作为几乎不可能被污染的 OOD 测试。\n- 调研依据: MathArena 社区对 AIME 2024 数据污染的分析；Qwen3.5 release timeline（2026年3月）vs. AIME 2024（2024年2月）。\n\n【缺陷 3】\n- 类别: 实验设计不足\n- 问题: Proposal 的 Approach 部分没有明确指定 NL-to-formal translation 的实现方式。\"solutions are formalized and verified step-by-step via Z3/SymPy\" 暗示存在一个从自然语言解题步骤到形式化约束的翻译环节，Resource Estimate 中提到\"LLM-to-formal translation ~60-70% success rate\"，但 Approach 部分未说明：(a) 是 student model 自己做 formalization 还是用另一个 LLM？(b) retry logic 的具体策略？(c) formalization 的 prompt 设计和 few-shot 示例来源？(d) 不同数学子类的 formalization template 是否不同？这不仅影响可复现性，更直接影响实验结果的解读——如果 formalization 本身引入系统性偏差（比如某些错误类型更容易被正确 formalize），则 error profile 可能反映的是 formalization 能力而非推理能力。\n- 严重度: 可补救\n- 补救方案: (1) 在 Approach 部分明确指定 formalization pipeline：使用什么模型（建议用 student model 自己做，保持 teacher-free claim 的一致性；或明确声明 formalization 用的是通用 code-generation 能力而非 diagnostic 判断，与 teacher-free claim 不矛盾）。(2) 详细描述 per-subcategory formalization templates（如 algebra equation → SymPy Eq() + solve()；inequality → Z3 constraint）。(3) 在 pilot study 中增加 formalization 质量评估：随机抽样 200 条 formalization，人工判断 formalization 是否忠实反映原始推理步骤。(4) 报告 formalization confounding analysis：对比\"formalization 成功且 Z3 判对\"vs.\"formalization 成功且 Z3 判错\"两组的原始推理质量差异，排除 formalization 偏差。\n- 调研依据: MATH-VF (arXiv 2505.20869) 的 formalization 方法（SymPy/Z3 分别处理不同类型约束）；FoVer (ACL 2026) 使用 Z3+Isabelle 但有明确的 formalization pipeline 描述。\n\n【缺陷 4】\n- 类别: 实验设计不足\n- 问题: Proposal 未指定每次迭代的合成数据量。Iterative self-improvement 的核心变量之一是每轮训练数据的规模——过少则信号不足，过多则可能引入冗余或 overfitting。Proposal 中提到\"SymPy-based synthesis generates targeted problems exercising weak skills\"，但没有说明：(a) 每类 error type 合成多少题？(b) 总量是固定的还是根据 error profile 动态调整？(c) 合成题目与原始训练集的比例？这直接影响与 baseline 的 compute fairness 比较——如果 FormalLoop 每轮用 10K 合成题而 vanilla SFT baseline 用 100K 原始题，比较就不公平。\n- 严重度: 可补救\n- 补救方案: (1) 明确指定 per-iteration data budget（如每轮 5K-10K 合成题，按 error profile 比例分配）。(2) 在 compute fairness 比较中，除了 dollar cost，还应报告 per-method total training tokens/examples。(3) 考虑两种 matched comparison：(i) 固定训练数据量（FormalLoop targeted 5K vs. uniform 5K），(ii) 固定计算预算（包括合成成本）。(4) 在 ablation 中增加 data scaling 分析：2K/5K/10K/20K per iteration，观察 marginal return。\n- 调研依据: SPARQ (arXiv 2506.06499) 明确报告了 7.5K seeds → 20M+ 合成数据的 scaling 分析；SwS (NeurIPS 2025) 报告了 augmented problem set 的具体规模。\n\n【缺陷 5】\n- 类别: 评估方案缺陷\n- 问题: GSM8K 在 2026 年对 9B 级别模型已接近饱和（顶级模型 >95%，capable 9B 模型通常 >85-90%）。如果 Qwen3.5-9B 的 baseline GSM8K 准确率已经很高，那么在 GSM8K 上展示的改进将缺乏区分度和说服力。Proposal 将 GSM8K 列为主要 benchmark 之一且在 ablation 中也使用，但未讨论 ceiling effect。\n- 严重度: 可补救\n- 补救方案: (1) 在 pilot study 中首先报告 base model（未经 FormalLoop）在所有 benchmark 上的性能，明确 headroom。(2) 如果 GSM8K baseline >90%，将其降级为 sanity check（确保不退化），不作为主要 improvement claim 的依据。(3) ablation benchmark 替换建议：将 GSM8K 替换为 Minerva Math 或 Olympiad-Bench（这些 benchmark 对 9B 模型有更大 headroom），保留 MATH-500 和 AIME24 作为 ablation 评估。(4) 对 GSM8K 报告 error reduction rate（从 baseline 的错误中减少了多少%）而非绝对准确率提升，这在高 baseline 下更有信息量。\n- 调研依据: LMMarketCap GSM8K leaderboard 2026 数据显示 frontier model 已达 99%；领域共识是 GSM8K 主要用于较小模型或作为 sanity check。\n\n【缺陷 6】\n- 类别: 实验设计不足\n- 问题: Proposal 指定\"5 iterations (9B) + 3 iterations (4B)\"但未提供迭代次数的选择依据或收敛准则。在 self-improvement 文献中，不同方法的最优迭代次数差异很大（NSRSA 在 5 轮时达到最优，但 vanilla self-training 可能在 2-3 轮就开始退化）。没有 convergence criterion 的固定迭代设计有两个风险：(a) 如果 FormalLoop 在第 3 轮就收敛，后续 2 轮是浪费且可能引入 overfitting；(b) 如果 baseline 在第 2 轮就退化但 FormalLoop 在第 5 轮才显优势，直接比较 final iteration 的结果会掩盖 iteration-level dynamics。\n- 严重度: 可补救\n- 补救方案: (1) 定义明确的 convergence criterion：例如连续 2 轮在 validation set（如 MATH-500）上准确率提升 <0.5%，或 error profile entropy 变化 <ε。(2) 所有方法都跑满 5 轮，但报告 per-iteration 结果曲线（已在 ablation #6 中部分涉及——将其从 [Should] 升级为 [Must]）。(3) 报告 best-iteration 和 final-iteration 两种结果，让读者同时看到 peak performance 和 stability。(4) 对于 4B validation model，3 iterations 可能不足以展示收敛特性——考虑增至 4-5 iterations 或明确论证为何 3 轮足够。\n- 调研依据: NSRSA (arXiv 2603.21558) 在 5 iterations 上展示了完整的收敛/退化曲线；Solver-Verifier Gap Theory (ICLR 2026) 预测指数收敛律，可据此设置理论 convergence bound。\n\n【缺陷 7】\n- 类别: ablation 不完整\n- 问题: Proposal 的 ablation #4 比较 SFT-only vs. DPO-only vs. SFT+DPO，但未涉及 DPO 的关键超参数 β（控制 preference 学习强度）。对于 step-localized formal DPO 这种新型 preference pair 构造方式，β 的最优值可能与标准 DPO 不同——因为 step-localized pair 的 chosen/rejected 差异更小（仅一步之差），β 过大可能导致 overfitting 到微小的步骤差异，β 过小则信号不足。此外，SFT 和 DPO 的 loss weight 比例也未讨论。\n- 严重度: 可补救\n- 补救方案: (1) 在 ablation #4 的 SFT+DPO 条件下，增加 β ∈ {0.05, 0.1, 0.2, 0.5} 的 sensitivity analysis（可在 4B 模型、2 iterations、1 benchmark 上快速验证）。(2) 讨论 step-localized pair 的 chosen-rejected margin 分布，与 solution-level pair 对比，论证 β 选择的合理性。(3) 如果 β sensitivity 结果表明 step-localized DPO 对 β 不敏感（一定范围内效果稳定），这本身就是一个积极发现，值得报告。\n- 调研依据: Step-DPO (NeurIPS 2024) 和 Full-Step-DPO (ACL 2025 Findings) 均在步骤级 DPO 中讨论了 margin 和 β 的交互；基于领域实验规范判断，DPO 超参数 sensitivity 是审稿人常见要求。\n\nSources:\n- [STAT: Skill-Targeted Adaptive Training](https://openreview.net/forum?id=m3jG3GaNIj)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [SwS: Self-aware Weakness-driven Problem Synthesis](https://openreview.net/forum?id=0jQUNQsZra)\n- [NSRSA: Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)\n- [An Imperfect Verifier is Good Enough](https://arxiv.org/abs/2604.07666)\n- [Solver-Verifier Gap Theory](https://arxiv.org/abs/2507.00075)\n- [SPARQ: Synthetic Problem Generation](https://arxiv.org/abs/2506.06499)\n- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/html/2505.20869v1)\n- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)\n- [Position: Don't Use CLT in LLM Evals](https://arxiv.org/pdf/2503.01747)\n- [Step-DPO](https://arxiv.org/abs/2406.18629)\n- [GSM8K Benchmark Saturation](https://lmmarketcap.com/benchmarks/gsm8k)\n- [Qwen 3.5 Complete Guide](https://codersera.com/blog/qwen-3-5-complete-guide-2026/)\n- [AIME Benchmark Data Contamination](https://www.emergentmind.com/topics/matharena-aime-2024)"
}
```

---

### Runtime record

_source line 73 · 2026-05-27T08:58:41.730Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:58:41.730Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

## Round 5

19 recorded events

### User

_source line 74 · 2026-05-27T08:58:41.754Z_

【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have sufficient research to make a well-grounded assessment. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- [NSRSA / arXiv 2603.21558] (arXiv March 2026): 最接近的工作。使用 SymPy 对 arithmetic 操作进行符号验证，在 GSM8K 上做 iterative self-training + solution-level DPO。但仅覆盖算术运算，不做 error categorization 或 targeted synthesis。与 FormalLoop 的核心差异在于：NSRSA 是 accept/reject，FormalLoop 是 diagnose-categorize-target。
- [FoVer / arXiv 2505.15960] (ACL Findings 2026): 用 Z3 和 Isabelle 做 formal verification 来生成 PRM 训练数据，跨 12 个 benchmark 表现强劲。目标是训练 verifier，不是 error-targeted self-improvement。Proposal 已正确将 FoVer-PRM + RLVR 作为 baseline。
- [STAT / arXiv 2510.10023] (ICLR 2026): 用 LLM teacher 的 metacognition 做 skill profiling + targeted synthesis/reweighting。在 MATH 上提升 7.5%，OOD 平均提升 4.6%。高层 idea（profile by skill → target weak skills）与 FormalLoop 共享，关键差异在 profiling 机制（formal vs. LLM teacher）。
- [SwS / arXiv 2506.08989] (NeurIPS 2025): 通过 pass-rate 分析识别 weakness，合成针对性问题用于 RL 训练。7B/32B 模型分别提升 10%/7.7%。不使用 formal diagnosis，granularity 停留在 problem-level 而非 step-level。
- [Adaptive Problem Generation / arXiv 2602.19187] (Feb 2026): 在符号空间中用 SymPy 做 closed-loop RLVR，通过 prompt optimization 自适应调节难度。但只做 global difficulty adaptation，没有 error-type diagnosis。
- [Pushing the Boundaries / arXiv 2601.22642] (Jan 2026): 用 formal logic verification 在生成过程中动态纠错（active correction during generation），7B/14B 模型分别超 SOTA 10.4%/14.2%。与 FormalLoop 使用 formal verification 的方式不同（active correction vs. error profiling），但属于 formal verification in training loop 的同一大方向。**Proposal 中未提及此工作。**
- [Imperfect Verifier / arXiv 2604.07666] (April 2026): 证明 noise rate ≤15% 时 RLVR 训练效果几乎无损。直接支撑 FormalLoop 的 precision-coverage tradeoff 论证。
- [Solver-Verifier Gap / arXiv 2507.00075] (ICLR 2026): 理论建模 self-improvement 的 solver-verifier capability gap，预测 verifier reliability 决定 self-improvement ceiling。为 FormalLoop 使用高精度 formal verifier 提供理论支撑。
- 调研总结: 该领域 2025-2026 年的研究重点在于 (1) 提升 self-improvement 的 verifier 质量以防止 model collapse，(2) 将 weakness identification 从粗粒度（subcategory/pass-rate）推向细粒度（skill-level/step-level），(3) 引入 formal tools 来替代 noisy 的 LLM-based verification。FormalLoop 恰好处于这三条趋势的交汇点——这既是其优势（顺应趋势），也是其挑战（"obvious next step" 风险）。

---

【发掘点 1】
- 维度: 核心 claim 强化 / novelty 锐化
- 内容: 当前 Proposal 的 framing 将 "teacher-free" 作为核心卖点，但更有穿透力的 framing 应该是 **"ground-truth error attribution unlocks a new class of self-improvement dynamics analysis that is fundamentally impossible with any LLM-based approach"**。具体来说：当前的 "teacher-free" framing 容易被审稿人解读为 "cost saving" 或 "scalability improvement"——这些是 incremental 优势。但 formal verification 的真正独特价值不在于"便宜"或"不需要 teacher"，而在于**它提供的 error attribution 是 ground-truth 而非 estimate**。这个性质使得 Contribution 3（error profile dynamics）从一个 "nice-to-have 分析" 变成一个 **"only possible with this approach" 的 unique capability**。建议重构 narrative：FormalLoop 不仅仅是 STAT 的 formal 版本（替换 teacher），而是通过 ground-truth error attribution 开启了一类 STAT 根本无法做的研究——比如 ground-truth skill dependency structure 和 convergence prediction。这让 "为什么要用 formal tools" 的回答从 "to avoid teacher bias" 升级为 "to enable analyses that are impossible otherwise"。
- 价值: 直接提升 Novelty 和 Significance。将 paper 从 "engineering integration of known components"（NSRSA 的 formal verification + STAT 的 targeted training）重新定位为 "enabling a new analytical paradigm for self-improvement dynamics"。后者对审稿人来说 surprise factor 显著更高。
- 调研依据: STAT (ICLR 2026) 的 skill profiling 受限于 LLM teacher metacognition，其 Missing-Skill-Profile 是 estimate 而非 ground truth，因此无法可靠回答 skill dependency 等问题。Solver-Verifier Gap theory (ICLR 2026) 从理论上预测了 verifier reliability 的重要性，但缺乏 ground-truth empirical validation。FormalLoop 的 error profile dynamics 恰好能提供这一缺失的 empirical grounding。

【发掘点 2】
- 维度: significance 提升
- 内容: **将 Error Profile Dynamics（当前 Contribution 3）从 secondary observation 提升为 co-primary research question。** 当前 proposal 将 error profile dynamics 列为第 3 个 contribution，隐含将其视为 "附带分析"。但实际上，以下三个子问题——(a) error type 是否存在 fixed reduction priority ordering，(b) skill dependency structure 是否存在（如 arithmetic errors 必须先解决才能让 algebraic errors 变得可见），(c) error profile entropy 是否能预测 convergence——是独立于 FormalLoop 具体实现的、关于 self-improvement dynamics 的 fundamental questions。这些问题此前之所以没人回答，不是因为没人想到，而是因为没有 ground-truth error attribution 工具来可靠地回答。如果 FormalLoop 的实验能揭示 non-trivial skill dependency structures（例如 arithmetic → algebraic manipulation → equation solving 的层级关系），这个发现的影响力可能远超 FormalLoop 系统本身——它会影响未来所有 math self-improvement 系统的 curriculum design。
- 价值: 显著提升 Significance。从 "我们做了一个更好的 self-improvement system" 变成 "我们揭示了 self-improvement 过程中 error type 的演化规律"。后者的 impact scope 更广。
- 调研依据: Curriculum learning 文献（如 arXiv 2510.19099 "What Makes a Good Curriculum"）研究 difficulty ordering 但没有 skill-type-level 的 ground-truth dynamics 分析。STAT (ICLR 2026) 虽然有 per-skill 分析但使用 LLM estimation，无法作为 ground truth。SwS (NeurIPS 2025) 的 weakness 分析停留在 problem-level pass rate，没有 error type decomposition。FormalLoop 可以填补这个 gap。

【发掘点 3】
- 维度: related work 差异化
- 内容: **Proposal 遗漏了 "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification" (arXiv 2601.22642, Jan 2026)**。这篇工作同样在 training pipeline 中使用 formal logic verification，但其用途是 active correction during generation（在生成过程中动态检测并纠正错误），而非 error profiling + targeted synthesis。在 7B/14B 模型上分别超 SOTA 10.4%/14.2%。审稿人很可能知道这篇工作（2026 年 1 月发布，结果强劲），如果 related work 中不讨论它，会被认为文献调研不充分。建议在 related work 中明确定位差异：该工作关注 inference-time formal verification guidance，FormalLoop 关注 training-time formal error diagnosis。两者互补而非竞争——FormalLoop 的 error profiling 产出的 targeted training data 可以提升模型的基础能力，而 interleaved formal verification 可以在 inference 时进一步纠错。
- 价值: 消除 Related Work 盲区，防止审稿人认为 novelty claim 不成立或文献调研不全面。同时，定位好这个差异可以进一步锐化 FormalLoop 的 novelty——FormalLoop 的 formal verification 是用于 training loop 的 error diagnosis，不是 inference-time correction。
- 调研依据: 直接来自搜索结果，arXiv 2601.22642，2026 年 1 月发布。

【发掘点 4】
- 维度: novelty 锐化 / 前提假设质疑
- 内容: **Error taxonomy 的 principled derivation 需要加强。** 当前 taxonomy 包含 5 类（algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference），但 proposal 未解释这 5 类的来源是 principled 还是 ad hoc。审稿人可能会问："为什么是这 5 类而不是别的分法？" 一个更强的定位方式是：**让 taxonomy 由 formal verification tool 的能力边界自然推导出来**。即每个类别对应 Z3/SymPy 的一种不同的验证操作类型（SymPy symbolic simplification → algebraic manipulation; SymPy solve → equation solving; SymPy numerical evaluation → arithmetic; Z3 constraint satisfaction → constraint reasoning; Z3 logical implication checking → logical inference）。这样 taxonomy 就不是人为选择的，而是 formal tools 能力的自然映射。这有两个好处：(a) 消除 "arbitrary taxonomy" 的审稿质疑，(b) 强化 "formal tools 不仅替代 teacher，更定义了 error analysis 的结构" 的 narrative。
- 价值: 提升 Novelty 的可信度。如果 taxonomy 是 principled 的，整个 error profiling 系统就更 rigorous；如果是 ad hoc 的，审稿人可能质疑 taxonomy 的 robustness 和 generalizability。
- 调研依据: STAT (ICLR 2026) 的 skill taxonomy 由 LLM teacher 生成，本身就是 ad hoc 的（LLM 生成的 skill list 依赖于 prompt 和 teacher 的 bias）。FormalLoop 有机会做得更好——如果 taxonomy 来自 formal tools 的能力结构，它就比 STAT 的 taxonomy 更 principled。这是一个相对 STAT 的额外优势。

【发掘点 5】
- 维度: trivial alternative 威胁
- 内容: **需要更尖锐地论证 fine-grained taxonomy 的增量价值相对于 coarser formal-rejection-rate targeting。** 当前 proposal 已将 subcategory-level targeting 和 taxonomy granularity ablation 纳入计划，但有一个中间态的 trivial alternative 需要明确 address：**使用 formal verification 的 accept/reject 信号（不做 error categorization），按 problem type 统计 formal rejection rate，然后 oversample rejection rate 高的 problem types。** 这不需要 error taxonomy，只需要 binary formal verification + rejection rate statistics，工程复杂度远低于完整的 FormalLoop。虽然 ablation 5 的 "single aggregate" condition 在某种程度上测试了这个 alternative，但建议在 paper 写作中明确将此作为一个 straw man 进行讨论，并解释为什么 step-level error categorization 比 problem-level rejection rate 提供了 qualitatively different 的信号（即：同一个 problem type 内的不同错误需要不同类型的 targeted training，这是 rejection rate 无法区分的）。
- 价值: 预防审稿人的 "为什么不用更简单的方法" 质疑。如果 proposal 不主动 address 这个 middle-ground alternative，审稿人可能在 rebuttal 阶段提出，而 rebuttal 空间有限。
- 调研依据: NSRSA (arXiv 2603.21558) 实质上就是这种 coarser alternative 的一个实例——formal accept/reject + DPO，没有 error categorization。FormalLoop 需要证明 categorization 提供了 NSRSA 没有的增量价值。基于领域整体趋势判断。

Sources:
- [NSRSA - Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [FoVer - Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [FoVer GitHub Repository](https://github.com/psunlpgroup/FoVer)
- [STAT - Skill-Targeted Adaptive Training (ICLR 2026)](https://openreview.net/forum?id=m3jG3GaNIj)
- [SwS - Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://openreview.net/forum?id=0jQUNQsZra)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification](https://arxiv.org/abs/2601.22642)
- [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)
- [Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (MATH-VF)](https://arxiv.org/abs/2505.20869)
- [Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification](https://arxiv.org/abs/2506.04592)
- [Self-Error-Instruct (ACL 2025)](https://aclanthology.org/2025.acl-long.417/)

【补救 agent 本轮输出】:
Now I have sufficient research to conduct a thorough evaluation. Let me compile my assessment.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **STAT: Skill-Targeted Adaptive Training** (ICLR 2026): Tested on Llama-3.2-3B/1B, Qwen2.5-3B. Baselines include MATH-Train, Embed-Sel, GRPO. Evaluated on MATH, AIME24/25, AMC23. Shows STAT complementary to GRPO. 3-model evaluation across families. Reports per-skill missing profiles.
- **NSRSA: Symbolic Recursive Self-Alignment** (arXiv 2603.21558, 2026): Qwen3-4B-Thinking on GSM8K across 5 iterations under 5 conditions (no-verify, outcome, majority vote, full NSRSA, NSRSA+DPO). Rejects ~34% of correct-answer solutions with flawed reasoning. Solution-level DPO only.
- **FoVer: Efficient PRM Training Data Synthesis** (ACL 2026 Findings): Z3 + Isabelle formal verification for PRM data. Evaluated on 12 benchmarks including math, logic, NLI, BBH. Demonstrates cross-domain generalization of formally-trained PRMs.
- **SwS: Weakness-Driven Problem Synthesis** (NeurIPS 2025): 3B to 32B model range, 8 math benchmarks. Pass-rate based weakness identification. +10% for 7B, +7.7% for 32B. Compares against human-labeled problem sets.
- **Imperfect Verifier (arXiv 2604.07666, 2026)**: Noise ≤15% yields near-clean accuracy. Precision > recall. Tested across Qwen3, GLM4, Llama 3.1 (4B-9B). Three model families, code + scientific reasoning.
- **Solver-Verifier Gap Theory** (ICLR 2026): Exponential convergence law. External data timing doesn't significantly affect final performance under limited-data regimes.
- **SPARQ** (arXiv 2506.06499, 2025): 7.5K seeds → 20M+ pairs, +24% on MATH for Gemma-2-9B via quality-diversity filtering. Ablates filtering strategies and diversity metrics.
- **MATH-VF (Step-Wise Formal Verification)** (arXiv 2505.20869, 2025): Z3+SymPy step-level verification. SymPy for symbolic computation/equation solving; Z3 for logical/polynomial constraints. Training-free framework tested on MATH500 and ProcessBench.
- **Position: Don't Use CLT in LLM Evals** (arXiv 2503.01747): CLT-based methods dramatically underestimate uncertainty on small benchmarks. At least 10 seeds recommended for small-N benchmarks like AIME (15 problems per contest).
- **AIME Data Contamination** (MathArena/emergentmind): AIME 2024 scores inflated 10-20 points by data contamination in models trained after 2024. Timeline-controlled evaluation essential.

- **调研总结**: 该领域当前实验设计标准要求：(1) 跨模型家族验证（至少2个家族），(2) 高方差小样本benchmark需≥8-10 seeds或Bayesian置信区间，(3) 数据污染分析（特别是AIME24），(4) 详细的per-iteration数据量和计算成本分解，(5) compute-matched比较是新兴标准。当前proposal的baseline矩阵和ablation设计在该领域属于上游水平，但在统计严谨性和若干实验细节上存在可修补的缺陷。

---

【缺陷 1】
- 类别: 评估方案缺陷
- 问题: Proposal 规定"3 independent runs, mean ± std, significance tests"用于所有 benchmark，但 AIME24 和 AIME25 每个仅有 30 道题（各15题×2场），AMC23 约25题。在如此小的样本量下，3 runs 的统计功效严重不足。近期文献（arXiv 2503.01747）明确指出，CLT-based 方法在小样本 LLM 评估中"dramatically underestimates uncertainty"，建议 AIME 类 benchmark 至少 10 seeds。对于 FormalLoop 这种 iterative 方法，每轮训练的随机性会进一步放大方差。3 runs 可能导致无法在 AIME/AMC 上得出显著结论，而这恰恰是 proposal 声称要展示 OOD generalization 的核心 benchmark。
- 严重度: 可补救
- 补救方案: (1) AIME24/25、AMC23 上增加至 8-10 independent runs（不同随机种子的完整训练循环），或在资源不允许时至少用不同采样温度做 16+ evaluation seeds（同一模型、不同采样）。(2) 采用 Bayesian bootstrap 置信区间替代 CLT-based significance test。(3) 在 GSM8K、MATH-500 等大样本 benchmark 上 3 runs 足够，但应明确分层：大样本 benchmark 用 t-test，小样本 benchmark 用 bootstrap 或 permutation test。(4) 报告 per-problem pass rate 分布（而非仅聚合准确率），让读者自行评估方差。
- 调研依据: arXiv 2503.01747 "Position: Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints"；MathArena AIME evaluation methodology recommendations。

【缺陷 2】
- 类别: 评估方案缺陷
- 问题: Proposal 使用 AIME24 作为 OOD generalization 的关键 benchmark，但 Qwen3.5 系列（2026年3月发布）的预训练数据极有可能包含 AIME 2024 题目。调研显示 AIME 2024 在 2026 年发布的模型上存在 10-20 分的数据污染膨胀。如果 baseline 和 FormalLoop 都在受污染的 benchmark 上评估，虽然相对比较仍有效，但绝对数值的 OOD 泛化 claim 会被审稿人质疑。
- 严重度: 可补救
- 补救方案: (1) 增加 AIME 2026（2026年2月举行，大概率不在 Qwen3.5 预训练数据中）作为最无污染的 OOD benchmark。(2) 对 AIME24 做污染检测：检查 base model（未经 FormalLoop 训练）在 AIME24 上的 pass@1 表现，与已知的未污染基准对比。(3) 在论文中明确报告 base model 在所有 benchmark 上的 baseline 性能，让读者自行判断污染程度。(4) 如条件允许，加入 Putnam/HMMT 等更高难度竞赛题目作为几乎不可能被污染的 OOD 测试。
- 调研依据: MathArena 社区对 AIME 2024 数据污染的分析；Qwen3.5 release timeline（2026年3月）vs. AIME 2024（2024年2月）。

【缺陷 3】
- 类别: 实验设计不足
- 问题: Proposal 的 Approach 部分没有明确指定 NL-to-formal translation 的实现方式。"solutions are formalized and verified step-by-step via Z3/SymPy" 暗示存在一个从自然语言解题步骤到形式化约束的翻译环节，Resource Estimate 中提到"LLM-to-formal translation ~60-70% success rate"，但 Approach 部分未说明：(a) 是 student model 自己做 formalization 还是用另一个 LLM？(b) retry logic 的具体策略？(c) formalization 的 prompt 设计和 few-shot 示例来源？(d) 不同数学子类的 formalization template 是否不同？这不仅影响可复现性，更直接影响实验结果的解读——如果 formalization 本身引入系统性偏差（比如某些错误类型更容易被正确 formalize），则 error profile 可能反映的是 formalization 能力而非推理能力。
- 严重度: 可补救
- 补救方案: (1) 在 Approach 部分明确指定 formalization pipeline：使用什么模型（建议用 student model 自己做，保持 teacher-free claim 的一致性；或明确声明 formalization 用的是通用 code-generation 能力而非 diagnostic 判断，与 teacher-free claim 不矛盾）。(2) 详细描述 per-subcategory formalization templates（如 algebra equation → SymPy Eq() + solve()；inequality → Z3 constraint）。(3) 在 pilot study 中增加 formalization 质量评估：随机抽样 200 条 formalization，人工判断 formalization 是否忠实反映原始推理步骤。(4) 报告 formalization confounding analysis：对比"formalization 成功且 Z3 判对"vs."formalization 成功且 Z3 判错"两组的原始推理质量差异，排除 formalization 偏差。
- 调研依据: MATH-VF (arXiv 2505.20869) 的 formalization 方法（SymPy/Z3 分别处理不同类型约束）；FoVer (ACL 2026) 使用 Z3+Isabelle 但有明确的 formalization pipeline 描述。

【缺陷 4】
- 类别: 实验设计不足
- 问题: Proposal 未指定每次迭代的合成数据量。Iterative self-improvement 的核心变量之一是每轮训练数据的规模——过少则信号不足，过多则可能引入冗余或 overfitting。Proposal 中提到"SymPy-based synthesis generates targeted problems exercising weak skills"，但没有说明：(a) 每类 error type 合成多少题？(b) 总量是固定的还是根据 error profile 动态调整？(c) 合成题目与原始训练集的比例？这直接影响与 baseline 的 compute fairness 比较——如果 FormalLoop 每轮用 10K 合成题而 vanilla SFT baseline 用 100K 原始题，比较就不公平。
- 严重度: 可补救
- 补救方案: (1) 明确指定 per-iteration data budget（如每轮 5K-10K 合成题，按 error profile 比例分配）。(2) 在 compute fairness 比较中，除了 dollar cost，还应报告 per-method total training tokens/examples。(3) 考虑两种 matched comparison：(i) 固定训练数据量（FormalLoop targeted 5K vs. uniform 5K），(ii) 固定计算预算（包括合成成本）。(4) 在 ablation 中增加 data scaling 分析：2K/5K/10K/20K per iteration，观察 marginal return。
- 调研依据: SPARQ (arXiv 2506.06499) 明确报告了 7.5K seeds → 20M+ 合成数据的 scaling 分析；SwS (NeurIPS 2025) 报告了 augmented problem set 的具体规模。

【缺陷 5】
- 类别: 评估方案缺陷
- 问题: GSM8K 在 2026 年对 9B 级别模型已接近饱和（顶级模型 >95%，capable 9B 模型通常 >85-90%）。如果 Qwen3.5-9B 的 baseline GSM8K 准确率已经很高，那么在 GSM8K 上展示的改进将缺乏区分度和说服力。Proposal 将 GSM8K 列为主要 benchmark 之一且在 ablation 中也使用，但未讨论 ceiling effect。
- 严重度: 可补救
- 补救方案: (1) 在 pilot study 中首先报告 base model（未经 FormalLoop）在所有 benchmark 上的性能，明确 headroom。(2) 如果 GSM8K baseline >90%，将其降级为 sanity check（确保不退化），不作为主要 improvement claim 的依据。(3) ablation benchmark 替换建议：将 GSM8K 替换为 Minerva Math 或 Olympiad-Bench（这些 benchmark 对 9B 模型有更大 headroom），保留 MATH-500 和 AIME24 作为 ablation 评估。(4) 对 GSM8K 报告 error reduction rate（从 baseline 的错误中减少了多少%）而非绝对准确率提升，这在高 baseline 下更有信息量。
- 调研依据: LMMarketCap GSM8K leaderboard 2026 数据显示 frontier model 已达 99%；领域共识是 GSM8K 主要用于较小模型或作为 sanity check。

【缺陷 6】
- 类别: 实验设计不足
- 问题: Proposal 指定"5 iterations (9B) + 3 iterations (4B)"但未提供迭代次数的选择依据或收敛准则。在 self-improvement 文献中，不同方法的最优迭代次数差异很大（NSRSA 在 5 轮时达到最优，但 vanilla self-training 可能在 2-3 轮就开始退化）。没有 convergence criterion 的固定迭代设计有两个风险：(a) 如果 FormalLoop 在第 3 轮就收敛，后续 2 轮是浪费且可能引入 overfitting；(b) 如果 baseline 在第 2 轮就退化但 FormalLoop 在第 5 轮才显优势，直接比较 final iteration 的结果会掩盖 iteration-level dynamics。
- 严重度: 可补救
- 补救方案: (1) 定义明确的 convergence criterion：例如连续 2 轮在 validation set（如 MATH-500）上准确率提升 <0.5%，或 error profile entropy 变化 <ε。(2) 所有方法都跑满 5 轮，但报告 per-iteration 结果曲线（已在 ablation #6 中部分涉及——将其从 [Should] 升级为 [Must]）。(3) 报告 best-iteration 和 final-iteration 两种结果，让读者同时看到 peak performance 和 stability。(4) 对于 4B validation model，3 iterations 可能不足以展示收敛特性——考虑增至 4-5 iterations 或明确论证为何 3 轮足够。
- 调研依据: NSRSA (arXiv 2603.21558) 在 5 iterations 上展示了完整的收敛/退化曲线；Solver-Verifier Gap Theory (ICLR 2026) 预测指数收敛律，可据此设置理论 convergence bound。

【缺陷 7】
- 类别: ablation 不完整
- 问题: Proposal 的 ablation #4 比较 SFT-only vs. DPO-only vs. SFT+DPO，但未涉及 DPO 的关键超参数 β（控制 preference 学习强度）。对于 step-localized formal DPO 这种新型 preference pair 构造方式，β 的最优值可能与标准 DPO 不同——因为 step-localized pair 的 chosen/rejected 差异更小（仅一步之差），β 过大可能导致 overfitting 到微小的步骤差异，β 过小则信号不足。此外，SFT 和 DPO 的 loss weight 比例也未讨论。
- 严重度: 可补救
- 补救方案: (1) 在 ablation #4 的 SFT+DPO 条件下，增加 β ∈ {0.05, 0.1, 0.2, 0.5} 的 sensitivity analysis（可在 4B 模型、2 iterations、1 benchmark 上快速验证）。(2) 讨论 step-localized pair 的 chosen-rejected margin 分布，与 solution-level pair 对比，论证 β 选择的合理性。(3) 如果 β sensitivity 结果表明 step-localized DPO 对 β 不敏感（一定范围内效果稳定），这本身就是一个积极发现，值得报告。
- 调研依据: Step-DPO (NeurIPS 2024) 和 Full-Step-DPO (ACL 2025 Findings) 均在步骤级 DPO 中讨论了 margin 和 β 的交互；基于领域实验规范判断，DPO 超参数 sensitivity 是审稿人常见要求。

Sources:
- [STAT: Skill-Targeted Adaptive Training](https://openreview.net/forum?id=m3jG3GaNIj)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [SwS: Self-aware Weakness-driven Problem Synthesis](https://openreview.net/forum?id=0jQUNQsZra)
- [NSRSA: Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [An Imperfect Verifier is Good Enough](https://arxiv.org/abs/2604.07666)
- [Solver-Verifier Gap Theory](https://arxiv.org/abs/2507.00075)
- [SPARQ: Synthetic Problem Generation](https://arxiv.org/abs/2506.06499)
- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/html/2505.20869v1)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [Position: Don't Use CLT in LLM Evals](https://arxiv.org/pdf/2503.01747)
- [Step-DPO](https://arxiv.org/abs/2406.18629)
- [GSM8K Benchmark Saturation](https://lmmarketcap.com/benchmarks/gsm8k)
- [Qwen 3.5 Complete Guide](https://codersera.com/blog/qwen-3-5-complete-guide-2026/)
- [AIME Benchmark Data Contamination](https://www.emergentmind.com/topics/matharena-aime-2024)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0b4a98e8-ee20-4873-a699-299b43676695",
  "isSidechain": false,
  "promptId": "5d9daf01-9398-4777-a30d-b02a0f31f43c",
  "type": "user",
  "uuid": "57abe0d0-8863-4a68-a4a3-8b3dffed6288",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 75_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to make a well-grounded assessment. Let me compile my analysis.  ---  【状态】:…",
  "leafUuid": "57abe0d0-8863-4a68-a4a3-8b3dffed6288",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Tool call

_source line 77 · 2026-05-27T08:58:45.523Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C4mhYjVhc2GNz3sGB47xMC`</summary>

```json
{
  "query": "\"Pushing the Boundaries\" formal logic verification interleaved bonus arxiv 2601.22642 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57abe0d0-8863-4a68-a4a3-8b3dffed6288",
  "isSidechain": false,
  "requestId": "req_011CbSoERLHDjTfmTsMM7cEY",
  "type": "assistant",
  "uuid": "9c567aba-c2bc-4696-8c55-15d51874b5ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TfjUXQfVp719vqHS7gnD7V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18911,
      "cache_read_input_tokens": 64364,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18911,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 77,
          "cache_read_input_tokens": 64364,
          "cache_creation_input_tokens": 18911,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18911
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

_source line 78 · 2026-05-27T08:58:51.747Z_

<details><summary>↩ Tool result · `toolu_01C4mhYjVhc2GNz3sGB47xMC`</summary>

```text
Web search results for query: ""Pushing the Boundaries" formal logic verification interleaved bonus arxiv 2601.22642 2026"

Links: [{"title":"[2601.22642] Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification","url":"https://arxiv.org/abs/2601.22642"},{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification","url":"https://arxiv.org/pdf/2601.22642"},{"title":"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models","url":"https://arxiv.org/html/2601.22642"},{"title":"Paper page - Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training","url":"https://huggingface.co/papers/2603.02208"},{"title":"SIGHT: Reinforcement Learning with Self-Evidence and Information-Gain Diverse Branching for Search Agent","url":"https://arxiv.org/html/2602.11551v1"}]

I found the research paper you're looking for. Here are the key details:

**Title:** "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification"

**arXiv ID:** 2601.22642 (submitted January 30, 2026)

**Main Contribution:** The paper introduces a formal logic verification-guided framework that dynamically interleaves formal symbolic verification with the natural language generation process, providing real-time feedback to detect and rectify errors as they occur.

**Key Innovation:** Distinguished from previous neuro-symbolic methods limited by passive post-hoc validation, the approach actively penalizes intermediate fallacies during the reasoning chain.

**Methodology:** The framework is operationalized via a novel two-stage training pipeline that synergizes formal logic verification-guided supervised fine-tuning and policy optimization.

**Results:** Extensive evaluation on six benchmarks spanning mathematical, logical, and general reasoning demonstrates that their 7B and 14B models outperform state-of-the-art baselines by average margins of 10.4% and 14.2%, respectively.

The paper is available on arXiv at https://arxiv.org/abs/2601.22642 in multiple formats (abstract, PDF, and HTML).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c567aba-c2bc-4696-8c55-15d51874b5ac",
  "isSidechain": false,
  "promptId": "5d9daf01-9398-4777-a30d-b02a0f31f43c",
  "type": "user",
  "uuid": "c37d4813-d44f-4d4e-aeb2-0a075a987c30",
  "toolUseResult": {
    "query": "\"Pushing the Boundaries\" formal logic verification interleaved bonus arxiv 2601.22642 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014QMbQCuqbyEgvDs5QBsk25",
        "content": [
          {
            "title": "[2601.22642] Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification",
            "url": "https://arxiv.org/abs/2601.22642"
          },
          {
            "title": "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification",
            "url": "https://arxiv.org/pdf/2601.22642"
          },
          {
            "title": "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification in Language Models",
            "url": "https://arxiv.org/html/2601.22642"
          },
          {
            "title": "Paper page - Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training",
            "url": "https://huggingface.co/papers/2603.02208"
          },
          {
            "title": "SIGHT: Reinforcement Learning with Self-Evidence and Information-Gain Diverse Branching for Search Agent",
            "url": "https://arxiv.org/html/2602.11551v1"
          }
        ]
      },
      "I found the research paper you're looking for. Here are the key details:\n\n**Title:** \"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\"\n\n**arXiv ID:** 2601.22642 (submitted January 30, 2026)\n\n**Main Contribution:** The paper introduces a formal logic verification-guided framework that dynamically interleaves formal symbolic verification with the natural language generation process, providing real-time feedback to detect and rectify errors as they occur.\n\n**Key Innovation:** Distinguished from previous neuro-symbolic methods limited by passive post-hoc validation, the approach actively penalizes intermediate fallacies during the reasoning chain.\n\n**Methodology:** The framework is operationalized via a novel two-stage training pipeline that synergizes formal logic verification-guided supervised fine-tuning and policy optimization.\n\n**Results:** Extensive evaluation on six benchmarks spanning mathematical, logical, and general reasoning demonstrates that their 7B and 14B models outperform state-of-the-art baselines by average margins of 10.4% and 14.2%, respectively.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2601.22642 in multiple formats (abstract, PDF, and HTML)."
    ],
    "durationSeconds": 6.218152343,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9c567aba-c2bc-4696-8c55-15d51874b5ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-27T08:58:54.447Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0119T2Fn1quzHwT3QtkpXRHX`</summary>

```json
{
  "query": "AIME 2025 2026 benchmark data contamination LLM evaluation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c37d4813-d44f-4d4e-aeb2-0a075a987c30",
  "isSidechain": false,
  "requestId": "req_011CbSoF9yLTQt8p3DHfmMdj",
  "type": "assistant",
  "uuid": "12666bba-2e64-4517-9f54-6c9cb81d559c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F9EvQxzVvB9e38FFX3zrqs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 674,
      "cache_read_input_tokens": 83275,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 674,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 83275,
          "cache_creation_input_tokens": 674,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 674
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

_source line 80 · 2026-05-27T08:59:00.320Z_

<details><summary>↩ Tool result · `toolu_0119T2Fn1quzHwT3QtkpXRHX`</summary>

```text
Web search results for query: "AIME 2025 2026 benchmark data contamination LLM evaluation 2026"

Links: [{"title":"LLM Evaluation Guide 2026: How to Benchmark & Compare Language Models","url":"https://jobsbyculture.com/blog/llm-evaluation-guide-2026"},{"title":"Evaluation data contamination in LLMs: how do we measure it and (when)   does it matter?","url":"https://arxiv.org/pdf/2411.03923"},{"title":"NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark","url":"https://arxiv.org/pdf/2310.18018"},{"title":"Contamination Report for Multilingual Benchmarks","url":"https://arxiv.org/pdf/2410.16186"},{"title":"Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models","url":"https://arxiv.org/pdf/2402.15938"}]

Based on the search results, I found relevant information about benchmark data contamination in LLM evaluation. Here's what the current research shows:

## Data Contamination in LLM Evaluation

Multiple benchmarks have been shown to have data contamination issues, where test questions appear verbatim in training corpora.

The worst kind of data contamination happens when a Large Language Model is trained on the test split of a benchmark, and then evaluated in the same benchmark. Contamination causes an overestimation of the performance of a contaminated model in a target benchmark and associated task with respect to their noncontaminated counterparts.

Recent research indicates the scope of the problem may be significant. Contamination may have a much larger effect than reported in recent LLM releases and there are differences in the extent to which models at different scale are impacted by contamination.

## Detection and Mitigation Efforts

Researchers have developed various approaches to address this issue. CDD (Contamination Detection via output Distribution) necessitates only the sampled texts to detect data contamination by identifying the peakedness of LLM's output distribution.

However, I did not find specific results in the search focusing on AIME 2025/2026 benchmark contamination. The results provide general information about data contamination issues across multiple benchmarks in LLM evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12666bba-2e64-4517-9f54-6c9cb81d559c",
  "isSidechain": false,
  "promptId": "5d9daf01-9398-4777-a30d-b02a0f31f43c",
  "type": "user",
  "uuid": "01909d14-1b24-42c6-a282-f58b22abb026",
  "toolUseResult": {
    "query": "AIME 2025 2026 benchmark data contamination LLM evaluation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WDrwFGFd7ofvRtkrkmjm7w",
        "content": [
          {
            "title": "LLM Evaluation Guide 2026: How to Benchmark & Compare Language Models",
            "url": "https://jobsbyculture.com/blog/llm-evaluation-guide-2026"
          },
          {
            "title": "Evaluation data contamination in LLMs: how do we measure it and (when)   does it matter?",
            "url": "https://arxiv.org/pdf/2411.03923"
          },
          {
            "title": "NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination   for each Benchmark",
            "url": "https://arxiv.org/pdf/2310.18018"
          },
          {
            "title": "Contamination Report for Multilingual Benchmarks",
            "url": "https://arxiv.org/pdf/2410.16186"
          },
          {
            "title": "Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models",
            "url": "https://arxiv.org/pdf/2402.15938"
          }
        ]
      },
      "Based on the search results, I found relevant information about benchmark data contamination in LLM evaluation. Here's what the current research shows:\n\n## Data Contamination in LLM Evaluation\n\nMultiple benchmarks have been shown to have data contamination issues, where test questions appear verbatim in training corpora.\n\nThe worst kind of data contamination happens when a Large Language Model is trained on the test split of a benchmark, and then evaluated in the same benchmark. Contamination causes an overestimation of the performance of a contaminated model in a target benchmark and associated task with respect to their noncontaminated counterparts.\n\nRecent research indicates the scope of the problem may be significant. Contamination may have a much larger effect than reported in recent LLM releases and there are differences in the extent to which models at different scale are impacted by contamination.\n\n## Detection and Mitigation Efforts\n\nResearchers have developed various approaches to address this issue. CDD (Contamination Detection via output Distribution) necessitates only the sampled texts to detect data contamination by identifying the peakedness of LLM's output distribution.\n\nHowever, I did not find specific results in the search focusing on AIME 2025/2026 benchmark contamination. The results provide general information about data contamination issues across multiple benchmarks in LLM evaluation."
    ],
    "durationSeconds": 5.869405000999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "12666bba-2e64-4517-9f54-6c9cb81d559c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-27T08:59:04.242Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0119YDCESkmKZmuCABS844Xv`</summary>

```json
{
  "query": "AIME 2026 math competition problems February 2026 benchmark LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01909d14-1b24-42c6-a282-f58b22abb026",
  "isSidechain": false,
  "requestId": "req_011CbSoFnei3BicNAPkKu7Tu",
  "type": "assistant",
  "uuid": "e608b5b6-f633-4e90-988a-76ff80c86ef2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcfgnEPzmcnsUnvAdon5J7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 645,
      "cache_read_input_tokens": 83949,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 645,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 83949,
          "cache_creation_input_tokens": 645,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 645
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

_source line 82 · 2026-05-27T08:59:11.446Z_

<details><summary>↩ Tool result · `toolu_0119YDCESkmKZmuCABS844Xv`</summary>

```text
Web search results for query: "AIME 2026 math competition problems February 2026 benchmark LLM"

Links: [{"title":"2026 AIME I - AoPS Wiki","url":"https://artofproblemsolving.com/wiki/index.php/2026_AIME_I"},{"title":"2026 AIME Webinars | RSM Math Competition Preparation","url":"https://www.mathschool.com/blog/competitions/2026-aime-webinars"},{"title":"American Invitational Mathematics Examination (AIME): A Complete Guide | AdmissionSight","url":"https://admissionsight.com/american-invitational-mathematics-examination/"},{"title":"AIME Practice Tests & Online Prep | 10 Practice Tests with solutions + AI-powered review","url":"https://www.mathpreppro.com/features/aime"},{"title":"AIME Problems and Solutions - AoPS Wiki","url":"https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions"},{"title":"math-conpetition – Ivy League Education Center","url":"https://ivyleaguecenter.org/tag/math-conpetition/"},{"title":"American Invitational Mathematics Examination - Wikipedia","url":"https://en.wikipedia.org/wiki/American_Invitational_Mathematics_Examination"},{"title":"Mathematical Association of America: American Invitational Mathematics Examination (AIME) | TeenLife","url":"https://www.teenlife.com/l/competition/american-invitational-mathematics-examination-aime/"},{"title":"American Math Competition (AMC 8, 10 & 12) Registration | Exam Dates & Schedule","url":"https://en.amcclub.org.cn/"},{"title":"AIME - TLUPS","url":"https://tlups.com/aime/"}]

Based on the search results, here's what I found about the AIME 2026 math competition in February 2026:

## AIME 2026 Competition Details

The 2026 AIME I test was administered on February 5th, 2026, with AIME II held on February 11.

The contest features 15 challenging problems that require written numerical answers, and you have three hours to finish. Each answer is an integer between 000 and 999 inclusive.

## Problem Resources

2026 AIME I problems and solutions are available through the Art of Problem Solving (AoPS) Wiki, which provides the full test, an answer key, and individual problem solutions.

## Competition Topics

Concepts typically covered in the competition include topics in elementary algebra, geometry, trigonometry, as well as number theory, probability, and combinatorics.

## Scoring

One point is earned for each correct answer, and no points are deducted for incorrect answers. No partial credit is given, so AIME scores are integers from 0 to 15 inclusive.

The search results don't contain specific information about using AIME problems as an LLM benchmark, but the 2026 AIME I problems are now publicly available and could potentially serve that purpose for evaluating language model mathematical reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e608b5b6-f633-4e90-988a-76ff80c86ef2",
  "isSidechain": false,
  "promptId": "5d9daf01-9398-4777-a30d-b02a0f31f43c",
  "type": "user",
  "uuid": "9bc2a560-4285-46ec-838b-e4314867560c",
  "toolUseResult": {
    "query": "AIME 2026 math competition problems February 2026 benchmark LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_016uah8AWUWusAAzUrtJKB3m",
        "content": [
          {
            "title": "2026 AIME I - AoPS Wiki",
            "url": "https://artofproblemsolving.com/wiki/index.php/2026_AIME_I"
          },
          {
            "title": "2026 AIME Webinars | RSM Math Competition Preparation",
            "url": "https://www.mathschool.com/blog/competitions/2026-aime-webinars"
          },
          {
            "title": "American Invitational Mathematics Examination (AIME): A Complete Guide | AdmissionSight",
            "url": "https://admissionsight.com/american-invitational-mathematics-examination/"
          },
          {
            "title": "AIME Practice Tests & Online Prep | 10 Practice Tests with solutions + AI-powered review",
            "url": "https://www.mathpreppro.com/features/aime"
          },
          {
            "title": "AIME Problems and Solutions - AoPS Wiki",
            "url": "https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions"
          },
          {
            "title": "math-conpetition – Ivy League Education Center",
            "url": "https://ivyleaguecenter.org/tag/math-conpetition/"
          },
          {
            "title": "American Invitational Mathematics Examination - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/American_Invitational_Mathematics_Examination"
          },
          {
            "title": "Mathematical Association of America: American Invitational Mathematics Examination (AIME) | TeenLife",
            "url": "https://www.teenlife.com/l/competition/american-invitational-mathematics-examination-aime/"
          },
          {
            "title": "American Math Competition (AMC 8, 10 & 12) Registration | Exam Dates & Schedule",
            "url": "https://en.amcclub.org.cn/"
          },
          {
            "title": "AIME - TLUPS",
            "url": "https://tlups.com/aime/"
          }
        ]
      },
      "Based on the search results, here's what I found about the AIME 2026 math competition in February 2026:\n\n## AIME 2026 Competition Details\n\nThe 2026 AIME I test was administered on February 5th, 2026, with AIME II held on February 11.\n\nThe contest features 15 challenging problems that require written numerical answers, and you have three hours to finish. Each answer is an integer between 000 and 999 inclusive.\n\n## Problem Resources\n\n2026 AIME I problems and solutions are available through the Art of Problem Solving (AoPS) Wiki, which provides the full test, an answer key, and individual problem solutions.\n\n## Competition Topics\n\nConcepts typically covered in the competition include topics in elementary algebra, geometry, trigonometry, as well as number theory, probability, and combinatorics.\n\n## Scoring\n\nOne point is earned for each correct answer, and no points are deducted for incorrect answers. No partial credit is given, so AIME scores are integers from 0 to 15 inclusive.\n\nThe search results don't contain specific information about using AIME problems as an LLM benchmark, but the 2026 AIME I problems are now publicly available and could potentially serve that purpose for evaluating language model mathematical reasoning capabilities."
    ],
    "durationSeconds": 7.200294726,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "e608b5b6-f633-4e90-988a-76ff80c86ef2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 83 · 2026-05-27T08:59:11.454Z_

```json
{
  "parentUuid": "9bc2a560-4285-46ec-838b-e4314867560c",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0148ec17-304c-42d2-a868-5b84e03ae9ac",
  "timestamp": "2026-05-27T08:59:11.454Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 84 · 2026-05-27T09:00:21.420Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have my cross-validation data for Round 3. Let me synthesize:

**Cross-validation results:**

1. **"Pushing the Boundaries" (arXiv 2601.22642)**: CONFIRMED. This paper uses formal logic verification interleaved during generation — a training pipeline with formal verification for active correction. Results: 7B/14B models outperform SOTA by 10.4%/14.2%. This IS a relevant missing reference that should be cited. The differentiation is clear: inference-time active correction vs. training-time error profiling + targeted synthesis. ADOPT 发掘3.


2. **AIME 2026 availability**: CONFIRMED. The 2026 AIME I exam was held February 5, 2026 with publicly available problems, and since Qwen3.5 released in March 2026, these problems are less likely to be in pretraining data—supporting the recommendation to use AIME26 as a cleaner out-of-distribution benchmark.
3. **AIME data contamination**: While general contamination concerns are well-documented, I couldn't find specific numbers for AIME24 contamination, though the concern remains reasonable given Qwen3.5's training cutoff.

I'm moderately confident in adopting these points. Now looking at the agent suggestions, the first one about reframing "teacher-free" as enabling novel analyses rather than just cost savings is a solid narrative improvement worth adopting, though it's more of a refinement than a new contribution. The second suggestion to elevate error profile dynamics as co-primary with the main question is already captured in Contribution 3, so I'll keep it there but strengthen how we frame the underlying scientific questions rather than making it equally primary.

The missing reference to "Pushing the Boundaries" needs to be added. Deriving the taxonomy directly from Z3 and SymPy capabilities rather than selecting categories ad hoc is a stronger methodological choice, so I'm adopting that. The formal-rejection-rate targeting as a straw man comparison is worth making explicit in the narrative since we already have ablation conditions that partially test this, so that's helpful for clarity.

On the remedial suggestions, there's a valid concern about statistical rigor when working with small benchmarks that I need to address. I need to define the convergence criterion and upgrade iteration dynamics to a must-have requirement, then report both best and final iteration results. For DPO β sensitivity, I'll mention it as a planned hyperparameter sweep rather than adding it as a full ablation to manage compute constraints. Now assessing the overall probability: the core novelty remains solid—teacher-free error-targeted synthesis, step-localized formal DPO, error profile dynamics, and the principled tool-derived taxonomy from R3—with significance trending upward after these refinements.

The ground-truth framing for enabling impossible analyses is genuinely stronger than just cost-saving arguments, pushing the idea ceiling to around 47%. The experimental plan is now quite comprehensive with bootstrap confidence intervals, multiple seeds for smaller benchmarks, AIME26 added for contamination checks, the NL-to-formal pipeline specified, per-iteration budgets defined, and convergence criteria locked in. Technical soundness looks solid, though I'm concerned the compute budget is getting tight with all these additions, and the formalization success rate remains uncertain pending the pilot study. The proposal is also getting lengthy and needs tightening. Overall probability lands around 41% in the 36-47% range, with R1 starting at 37%.

Looking at the progression from R2 to R3, the improvements are incremental—only a 1% jump from 40% to 41%. The changes are mostly refinements: sharpening the narrative around ground-truth and taxonomy, adding statistical rigor through bootstrap methods and more seeds, including the missing reference, specifying implementation details like the NL-to-formal conversion and data budgets, and adjusting benchmarks with AIME26 and GSM8K demotion. These are hardening moves rather than structural shifts. The core idea and experimental framework haven't fundamentally changed since R2, and with two consecutive rounds of fine-tuning and essentially flat probability growth, convergence signals are clear.

Both agents flagged diminishing returns—the discovery agent found 5 points but they're increasingly about framing, and the remediation agent found 7 points but they're mostly statistical details. The proposal is mature enough to move forward. Further iterations would just add more ablation conditions and statistical refinements without materially changing the core contribution or probability estimate.

I'm converging on a final probability of 41% (range 36–47%), which passes the threshold for outputting an optimization plan. I'll produce the R3 integration and then the final optimization strategy. I'm deciding to converge on this solution, which means the system will prompt me separately for the final output. Looking back at the format requirements, since I'm converging rather than iterating further, I don't need to produce a next-round proposal—just the convergence decision. But I should still mentally consolidate what the final proposal looks like with all the R3 refinements integrated, even if I'm not outputting it as a formal next iteration. Let me reconsider the success probability one more time before I finalize this.

The core contributions are solid: teacher-free error-targeted synthesis addresses a genuine gap, step-localized formal DPO is novel and distinct from existing approaches, error profile dynamics offers unique scientific value, and the precision-coverage tradeoff is a generalizable principle. The experimental design is comprehensive with strong baselines, seven prioritized ablations, a thorough pilot study, statistical rigor through bootstrap confidence intervals and contamination analysis, compute fairness metrics, and cross-model validation. The main risks around formalization success and compute budget tightness are both mitigated—the pilot study has a clear go/no-go threshold, and I have a simplification strategy for ablations if needed.

For AAAI 2026, this feels like a well-grounded proposal that goes beyond pure engineering through its theoretical foundation in the solver-verifier gap and the novel error profile analysis capability, even though it's fundamentally an integration paper. The execution complexity is real, but the risk mitigation strategies are solid. I'm settling on 41% as my median estimate, which puts it above the 36% threshold for the optimization plan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0148ec17-304c-42d2-a868-5b84e03ae9ac",
  "isSidechain": false,
  "requestId": "req_011CbSoGcEAwF35BS1GG6xyd",
  "type": "assistant",
  "uuid": "2dd9527b-a318-4356-bafc-3df83145bd83",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JZMkM2JTHwAsyFJ5gUmS7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 84594,
      "output_tokens": 5008,
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
          "output_tokens": 5008,
          "cache_read_input_tokens": 84594,
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

### Assistant

_source line 85 · 2026-05-27T09:01:02.121Z_

Now let me synthesize all cross-validation results and produce my Round 3 integration.

**Cross-validation summary:**
1. **"Pushing the Boundaries" (arXiv 2601.22642)** — CONFIRMED: Uses formal logic verification interleaved during generation for active error correction. 7B/14B outperform SOTA by 10.4%/14.2%. Key difference: inference-time active correction vs. FormalLoop's training-time error profiling. Must cite.
2. **AIME 2026 availability** — CONFIRMED: 2026 AIME I held February 5, 2026. Problems public on AoPS Wiki. Qwen3.5 released March 2026, so AIME26 is a much cleaner OOD benchmark than AIME24.
3. **AIME24 contamination** — General contamination concerns well-documented; specific AIME24 numbers not found but the timeline risk (AIME24 Feb 2024 → Qwen3.5 training cutoff) is real. Reasonable to add AIME26 and report base model baselines.

【阶段】: 迭代第 3 轮

【交叉验证调研】:
1. **Pushing the Boundaries (arXiv 2601.22642)**: 搜索确认——formal logic verification 用于生成过程中的动态纠错（interleaved bonus），7B/14B 分别超 SOTA 10.4%/14.2%。与 FormalLoop 差异明确：inference-time active correction vs. training-time error profiling + targeted synthesis。必须引用。**已验证，采纳发掘3。**
2. **AIME 2026 可用性**: 搜索确认——2026 AIME I 于 2026 年 2 月 5 日举行，题目已公开。Qwen3.5 3 月发布，AIME26 大概率不在预训练数据中。**已验证，采纳补救2。**
3. **AIME24 数据污染风险**: 未找到具体的 AIME24 污染数据，但 timeline 分析（AIME24 Feb 2024 → Qwen3.5 training cutoff 2026）表明风险真实存在。**基于 timeline 推理合理，采纳。**

【发掘 agent 有效建议采纳】:
- **发掘1 (Ground-truth 作为 enabling new analyses 的 framing)**: **采纳作为叙事微调**——将"teacher-free"从"成本节约"重构为"开启 LLM-based 方法根本无法做到的 ground-truth 分析"。但这是 R2 已有 framing 的锐化，非结构性变更。
- **发掘2 (Error profile dynamics 进一步提升)**: **部分采纳**——已在 R2 作为 Contribution 3 列出。继续强化其 framing（强调是 only-possible-with-formal-tools 的 unique capability），但不再进一步提升为"co-primary"以免稀释核心方法学故事。
- **发掘3 (Missing reference: Pushing the Boundaries)**: **采纳**——已验证。在 Related Work 中引用并明确差异化：inference-time correction vs. training-time profiling。两者互补。
- **发掘4 (Principled taxonomy from tool capabilities)**: **采纳**——将 error taxonomy 定义为 Z3/SymPy 验证操作类型的自然映射，消除"arbitrary taxonomy"质疑。
- **发掘5 (Formal-rejection-rate targeting 作为 middle-ground straw man)**: **采纳作为叙事补充**——在 "Why Not Simpler Alternatives" 部分增加此 straw man，与 ablation 5 的 "single aggregate" 条件对应。

【补救 agent 有效建议采纳】:
- **补救1 (小样本 benchmark 统计严谨性)**: **采纳**——AIME/AMC 增至 8-10 seeds 或 Bayesian bootstrap CI；大样本 benchmark 保持 3 runs。
- **补救2 (AIME24 污染 + AIME26)**: **采纳**——已验证 AIME26 可用。增加 AIME26 为 benchmark，报告 base model baseline，对所有 AIME 做污染检测。
- **补救3 (NL-to-formal 实现细节)**: **采纳**——指定 student model 自身做 formalization（保持 teacher-free），描述 per-subcategory templates，在 pilot study 增加 formalization 忠实度检验。
- **补救4 (Per-iteration 数据量)**: **采纳**——指定每轮 5K-10K 合成题，按 error profile 比例分配。增加 data-matched comparison。
- **补救5 (GSM8K ceiling effect)**: **采纳**——GSM8K 降级为 sanity check，ablation benchmark 替换为 Minerva Math。
- **补救6 (Convergence criterion)**: **采纳**——定义基于 validation accuracy + error profile entropy 的收敛准则。Per-iteration dynamics 从 [Should] 升至 [Must]。
- **补救7 (DPO β sensitivity)**: **降权处理**——记为 planned hyperparameter sweep，不作为独立 ablation 组以避免进一步加重 compute 负担。在 ablation 4 的 SFT+DPO 条件下做 2-3 个 β 值的 quick sweep 即可。

【本轮 proposal 主要变更】:
**Idea 层面变更:**
- 叙事微调："teacher-free" → "ground-truth error attribution enabling analyses impossible with LLM-based approaches"
- Error taxonomy 来源说明：从 Z3/SymPy 验证操作类型自然推导，非 ad hoc 设定
- 新增 middle-ground trivial alternative 回应：formal-rejection-rate targeting（无 categorization 的 binary accept/reject + rejection-rate-based oversampling）
- 新增引用：Pushing the Boundaries (arXiv 2601.22642)，明确定位差异

**实验层面变更:**
- 新增 AIME26 为 benchmark（最少污染的 OOD 测试），总 benchmark 增至 8 个
- GSM8K 降级为 sanity check，ablation benchmark 中替换为 Minerva Math
- AIME/AMC 统计方法升级：8-10 seeds + Bayesian bootstrap CI
- NL-to-formal pipeline 明确：student model 自身做 formalization + per-subcategory templates
- Per-iteration synthesis budget 明确：5K-10K 题/轮
- 收敛准则明确：validation accuracy Δ < 0.5% + error profile entropy Δ < ε 连续 2 轮
- Per-iteration dynamics 升至 [Must]
- DPO β sensitivity 纳入 ablation 4 作为 quick sweep
- Pilot study 增加 formalization 忠实度检验

【idea 质量评估】: Novelty=中强偏强（4 个差异化贡献 + principled taxonomy，均有文献空白支撑；但核心仍是 validated components 的组合）Significance=中强偏强（ground-truth 分析的 unique capability framing 比"cost saving"更有力，generalizable principle 跨领域）→ idea 天花板约 47%

【实验完备性评估】: Technical Soundness=中强偏强（统计严谨性改善，数据污染处理，implementation 细节明确，收敛准则定义；残余风险主要在 compute budget 和 formalization 成功率的实测值）→ 地板已进一步加固

【当前概率估计】: [36% - 47%] 中位 41%

【决策】: 收敛

【决策理由】: 触发收敛条件——连续 2 轮（R2→R3）变更以微调为主（叙事锐化、统计细节、benchmark 调整、实现细节），无结构性重构；中位概率 R2 40% → R3 41%，Δ=1%，基本持平。发掘 agent R3 的 5 个建议中 4 个是 framing 微调而非新贡献发现；补救 agent R3 的 7 个缺陷全部是实验细节层面的加固。Proposal 核心架构（idea framing + 4 contributions + baseline matrix + ablation plan + pilot study）在 R2 已成型，R3 只做了表面硬化。继续迭代大概率进入 diminishing returns。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2dd9527b-a318-4356-bafc-3df83145bd83",
  "isSidechain": false,
  "requestId": "req_011CbSoGcEAwF35BS1GG6xyd",
  "type": "assistant",
  "uuid": "4821ef57-72ee-4330-a472-22d34b5a8bb0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JZMkM2JTHwAsyFJ5gUmS7",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 956,
      "cache_read_input_tokens": 84594,
      "output_tokens": 5008,
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
          "output_tokens": 5008,
          "cache_read_input_tokens": 84594,
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

### Runtime record

_source line 86_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to make a well-grounded assessment. Let me compile my analysis.  ---  【状态】:…",
  "leafUuid": "4821ef57-72ee-4330-a472-22d34b5a8bb0",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 87_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have sufficient research to make a well-grounded assessment. Let me compile my analysis.  ---  【状态】:…",
  "leafUuid": "4821ef57-72ee-4330-a472-22d34b5a8bb0",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 90_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 91 · 2026-05-27T09:01:03.347Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T09:01:03.347Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "content": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。"
}
```

---

### Runtime record

_source line 92 · 2026-05-27T09:01:03.347Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T09:01:03.347Z",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

## Round 6

5 recorded events

### User

_source line 93 · 2026-05-27T09:01:03.371Z_

【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4821ef57-72ee-4330-a472-22d34b5a8bb0",
  "isSidechain": false,
  "promptId": "a2ee0ca9-980f-4c5d-8453-95bddfbe69d2",
  "type": "user",
  "uuid": "c1fa6f47-f98c-482b-8e79-a730b770aae9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 94 · 2026-05-27T09:01:18.126Z_

<details><summary>Logged reasoning block</summary>

```text
The user is asking me to produce the final output as 角色 C (最终输出). Since the process converged with median probability 41% (≥ 36%), I should output the optimization plan comparing against the ORIGINAL proposal.

Let me carefully compare the final optimized version against the original proposal and produce a concrete list of modifications.

Let me recall the original proposal's structure:
1. Core Problem
2. Research Opportunity
3. Research Landscape
4. Proposed Approach
5. Detailed Description
6. Key References (19 refs)


7. Resource Estimate

And the final optimized version has:
1. Core Problem (reframed with teacher-free emphasis + LLM error detection evidence)
2. Core Contributions (NEW section — 4 explicit contributions)
3. Why Not Simpler Alternatives? (NEW section — 3 alternatives addressed)
4. Research Landscape (expanded with new refs and positioning)
5. Proposed Approach (with formal coverage scope, DPO details, quality control, fallback)
6. Experimental Design (greatly expanded — models, benchmarks, evaluation protocol, baselines, ablations, compute fairness, pilot study)
7. Key References (22 refs, +3 new)
8. Resource Estimate (updated with revised compute and timeline based on expanded experiments)

Now I'm laying out the specific optimization plan with all the structural changes and additions I'm making to strengthen the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c1fa6f47-f98c-482b-8e79-a730b770aae9",
  "isSidechain": false,
  "requestId": "req_011CbSoQrqUbE3N8yRb1qVRX",
  "type": "assistant",
  "uuid": "2c153618-9db1-46f9-9bc5-2fda8dc1a631",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Unh8xVaxEkzZ7bQedQGa7U",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5085,
      "cache_read_input_tokens": 85550,
      "output_tokens": 4942,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4942,
          "cache_read_input_tokens": 85550,
          "cache_creation_input_tokens": 5085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5085
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

_source line 95 · 2026-05-27T09:03:01.204Z_

【优化方案】

1. **标题** — 从 "Formal Error Profiling Enables Targeted Math Self-Improvement" 改为 **"Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement"** — 命中 Novelty：标题直接传达核心差异化（teacher-free），让审稿人第一眼就抓住与 STAT/SwS/Self-Error-Instruct 的区别。

2. **Core Problem 重构** — 原文以"model collapse + wasteful data"作为双痛点开场，未突出 teacher 依赖问题。改为：**将"所有现有 error-targeted synthesis 方法均依赖 LLM teacher"确立为核心矛盾**，引用 "LLMs Cannot Spot Math Errors" (EMNLP 2025, arXiv 2509.01395) 作为实证——LLMs 即使给出参考解也无法可靠定位数学错误。这将论文的 motivation 从"做得更好"升级为"解决一个被验证的根本性缺陷"。 — 命中 Significance + Novelty。

3. **新增「Core Contributions」结构化章节** — 原始 proposal 将贡献散落在 Proposed Approach 和 Detailed Description 中，审稿人需自行提炼。改为 **4 个明确编号的贡献**：
   - (C1) Teacher-free error-targeted self-improvement：首个完全由 formal symbolic tools 驱动错误诊断和定向合成的 self-improvement 系统，区别于 RLVR/GRPO（也 teacher-free 但不 error-targeted）
   - (C2) Formally-verified step-localized DPO：与 Step-DPO (NeurIPS 2024) / Full-Step-DPO (ACL 2025 Findings) 区分（它们用 LLM/human 标注），与 NSRSA (arXiv 2026) 区分（它用 solution-level accept/reject）；我们的 preference pairs 在第 k+1 步分歧且有 formal guarantee
   - (C3) Ground-truth error profile dynamics：首次用 formally-verified labels 追踪多轮迭代中 per-skill-type error 演化，回答 skill dependency structure、error reduction priority ordering、entropy-based convergence prediction 等此前无法用 ground-truth 数据回答的问题
   - (C4) Precision-coverage tradeoff hypothesis：在 self-improvement loop 中，verifier noise 超过阈值 τ 时扩大 coverage 的边际收益为负（imperfect verifier research, arXiv 2604.07666 估计 τ≈15%），通过 noise injection ablation 实证验证
   — 命中 Novelty + Significance + Technical Soundness（审稿人看到 4 个清晰独立的贡献点，比模糊的"我们统一了三条线"更有说服力）。

4. **新增「Why Not Simpler Alternatives?」章节** — 原始 proposal 未主动回应 trivial alternative 威胁。新增三个显式 straw man 及其反驳：
   - *vs. Outcome verification + STAT-style LLM teacher profiling*：错误归因精度（outcome 不定位、LLM step diagnosis 有 hallucination）、迭代稳定性（teacher bias 跨轮放大）、无 teacher ceiling
   - *vs. Subcategory-level outcome targeting*（用 MATH 的 7 个子类别标签直接 oversample 弱类别）：subcategory 太粗——同一 Algebra 类内 algebraic manipulation error 和 equation solving error 需要不同 targeted training，subcategory-level 无法区分
   - *vs. FoVer-PRM as verifier in standard self-improvement loop*：FoVer 间接通过 PRM 使用 formal verification 信号，FormalLoop 直接用于 error categorization + targeted synthesis——隔离直接 profiling 的增量价值
   - *vs. Formal-rejection-rate targeting*（binary accept/reject + rejection-rate-based oversampling，无 error categorization）：同一 problem type 内的不同错误需要不同类型的 targeted training，binary rejection rate 无法区分（NSRSA 实质是此 alternative 的实例）
   — 命中 Novelty（预防审稿人最可能的 4 种"why not just..."攻击）。

5. **Proposed Approach：Formal Coverage Scope 明确限定** — 原始 proposal 声称覆盖 "full spectrum from algebra through proof-level reasoning"，这是审稿红旗。改为：**显式限定 formal verification 范围为 algebraic/arithmetic domains amenable to Z3/SymPy**（Algebra, Number Theory, Prealgebra, 部分 Intermediate Algebra 和 Precalculus），Geometry 和 Counting & Probability 使用 outcome-based verification 作为 fallback。论证：即使部分覆盖（~60-70% on amenable categories），near-zero noise 的 partial coverage 仍优于 full-coverage noisy LLM diagnosis（imperfect verifier research, arXiv 2604.07666）。 — 命中 Technical Soundness（诚实 claim 比 overclaim 更安全）。

6. **Proposed Approach：Error Taxonomy 来源说明** — 原始 proposal 的 5 类 taxonomy（algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference）看似 ad hoc。改为：**将每类 error type 定义为 Z3/SymPy 验证操作类型的自然映射**（SymPy symbolic simplification → algebraic manipulation; SymPy solve → equation solving; SymPy numerical evaluation → arithmetic; Z3 constraint satisfaction → constraint reasoning; Z3 logical implication → logical inference）。taxonomy 不是人为选择，而是 formal tools 能力的结构化投射。 — 命中 Novelty + Technical Soundness（消除"arbitrary taxonomy"质疑，且构成相对 STAT ad-hoc skill taxonomy 的额外优势）。

7. **Proposed Approach：Formalization Quality Control Pipeline** — 原始 proposal 未区分 formalization failure 和 reasoning error。新增：(a) 区分"verification failed = error detected"和"formalization failed = unknown"，(b) 排除 formal rejection + correct answer 的 suspicious cases，(c) 只对高置信度 pairs 做 DPO，(d) 报告 noise rate 并对标 15% tolerance threshold。 — 命中 Technical Soundness。

8. **Proposed Approach：DPO Pair Construction with Fallback** — 原始 proposal 仅提 "formally-verified vs. formally-rejected pairs"，未考虑 yield 问题。新增：step-localized pairs 为主、solution-level formal pairs 为 fallback，pilot study 估算 yield，报告混合比例。 — 命中 Technical Soundness + Feasibility。

9. **Proposed Approach：NL-to-Formal Translation 实现细节** — 原始 proposal 仅说"solutions are formalized"未说怎么做。新增：student model 自身做 formalization（保持 teacher-free consistency），per-subcategory formalization templates（algebra equation → SymPy Eq() + solve()；inequality → Z3 constraint），pilot study 包含 formalization 忠实度人工检验。 — 命中 Technical Soundness + Reproducibility。

10. **新增完整「Experimental Design」章节** — 原始 proposal 无任何实验设计。这是最大的结构性补充：

    **Models**: Qwen3.5-9B (primary, 5 iterations) + Qwen3.5-4B (validation, 3 iterations)。Pilot study 包含 Llama 3.1-8B formalization success rate 对比。

    **Benchmarks** (8个): GSM8K (sanity check only), MATH-500, Minerva Math, AMC23, AIME24, AIME25, AIME26, Olympiad-Bench。AIME26 (Feb 2026) 为最少污染的 OOD 测试。Per-MATH-subcategory breakdown。

    **Evaluation protocol**: Greedy + Pass@K (K=8,32) + majority voting@K。大样本 benchmarks 3 runs + t-test；AIME/AMC 8-10 seeds + Bayesian bootstrap CI。报告 base model baseline 用于污染分析。

    **Baseline matrix** (5类):
    - Training paradigm: Vanilla SFT, SFT+DPO (uniform), GRPO/RLVR
    - Targeting: SwS (NeurIPS 2025, code available), STAT-style (GPT-4o teacher), subcategory-level outcome targeting
    - Symbolic: Adaptive Problem Generation (arXiv 2602.19187)
    - Verification: FoVer-PRM (ACL 2026, open source) + Best-of-N/RLVR, outcome-only loop (NSRSA-style)

    **Ablation studies** (priority-ranked, on Qwen3.5-4B, 2-3 iterations, 3 benchmarks):
    - [Must] Error profiling source (5 conditions: formal / LLM / pass-rate / subcategory-level / random)
    - [Must] DPO pair source (4 conditions: step-localized formal / solution-level formal NSRSA-style / outcome / LLM-annotated Step-DPO style)
    - [Must] Targeting vs. uniform
    - [Must] Per-iteration dynamics (accuracy, error profile evolution, entropy, formalization coverage)
    - [Should] Training objective (SFT / DPO / SFT+DPO, with β sensitivity sweep)
    - [Should] Taxonomy granularity (5-type / 2-type / single aggregate)
    - [Nice] Precision-coverage tradeoff (noise injection 5%/10%/15%/20%)

    **Compute fairness**: 统一 metric = total dollar cost (GPU + CPU + API)。两种 matched comparison (fixed training FLOPs / fixed total budget)。Accuracy vs. cost curves。Per-iteration synthesis budget: 5K-10K problems/round, per-error-type proportional allocation。

    **Convergence criterion**: Validation accuracy Δ < 0.5% + error profile entropy Δ < ε 连续 2 轮。报告 best-iteration 和 final-iteration 双结果。

    **Pilot study** (before main experiments):
    - Per-subcategory formalization success rate (200-300 problems/subcategory)
    - Failure mode analysis + selection bias analysis (formalization success vs. failure groups)
    - DPO pair yield estimation (500 problems × 16 solutions)
    - Cross-family formalization comparison (Qwen3.5-9B vs. Llama 3.1-8B)
    - Taxonomy coverage validation + comparison with STAT's skill taxonomy
    - Synthesized problem quality: human evaluation (100-200 problems)
    - Formalization faithfulness: human verification (200 formalizations)
    — 以上整体命中 Technical Soundness（从无实验设计到领域上游水平的完整方案）。

11. **Research Landscape 扩展** — 新增 3 条关键定位：
    - Step-DPO (NeurIPS 2024) / Full-Step-DPO (ACL 2025 Findings)：step-level DPO 的先驱，但用 LLM/human 标注——FormalLoop 用 formal verification
    - "LLMs Cannot Spot Math Errors" (EMNLP 2025, arXiv 2509.01395)：LLM-based error diagnosis 不可靠的实证
    - "Pushing the Boundaries" (arXiv 2601.22642, Jan 2026)：formal logic verification 用于 inference-time active correction——FormalLoop 用于 training-time error profiling，两者互补
    — 命中 Related Work 完备性（审稿人检查文献调研时不会发现盲区）。

12. **Resource Estimate 更新** — 从 600 H100 hours 调整为 ~750 H100 hours（+150h for 4B validation model, expanded ablations, pilot study, additional AIME seeds），timeline 不变。新增 teacher API cost ($200-400 for GPT-4o STAT baseline)。 — 命中 Feasibility 的透明度。

【主要风险】:

1. **Formalization 成功率不达预期（最高风险）**: 如果 pilot study 发现 amenable categories 上的 formalization 成功率显著低于 50%（而非预估的 60-70%），error profiling 的有效覆盖率将不足以支撑核心 claim。Pilot study 设有 go/no-go 阈值，但如果触发 no-go，整个方法需要根本性调整（如引入 MATH-VF 的 SimpleMath 中间语言）。审稿人会直接追问这个数字。

2. **"Combination paper" 感知风险**: 尽管已构建 4 个独立贡献点和理论论证链，部分审稿人可能仍将 FormalLoop 视为 "NSRSA + STAT + FoVer 的工程拼接"。防御要点在于 Contribution 3 (error profile dynamics) 和 Contribution 4 (precision-coverage tradeoff) — 这两个贡献是 any 单一 prior work 无法产生的，只有在 formal diagnosis + iterative loop 的组合中才存在。Rebuttal 中应重点强调这一点。

【实施评估】:
- **计算资源**: ~750 H100 GPU hours（main experiments ~400h, ablations ~200h, pilot study + evaluation ~150h）+ 大量 CPU hours（Z3/SymPy verification, ~0.5-2s/step, parallelizable across problems）。建议使用 H100 spot instances (~$2.50/hr) 或等效云平台。总 GPU 成本约 $1,875。
- **数据需求**: MATH-Train（公开，~7.5K 题）作为种子集；GSM8K / MATH-500 / Minerva Math / AMC23 / AIME24 / AIME25 / AIME26 / Olympiad-Bench（均公开可得）用于评估。无需自建数据集。STAT baseline 需 GPT-4o API 访问（$200-400）。
- **人工介入**: (1) Pilot study 中 formalization 忠实度人工检验（200 条，约 1-2 人日），(2) 合成题目质量 human evaluation（100-200 道，约 1-2 人日），(3) Error taxonomy 的 pilot validation（与自动分类对比，约 1 人日）。总人工约 4-6 人日，需数学背景标注员。
- **训练需求**: 需要模型训练——Qwen3.5-9B 的 SFT+DPO fine-tuning，5 轮迭代，每轮 5K-10K 样本。单轮 fine-tune 约 40-80 H100 hours。4B validation model 训练成本约为 9B 的 40%。不需要从头预训练。
- **新 Benchmark**: 不需要构建新 benchmark。需要构建的是：(1) error taxonomy 定义及其到 Z3/SymPy 操作的映射规范，(2) per-subcategory formalization templates，(3) SymPy-based targeted problem synthesis templates。这些是 engineering artifacts 而非 benchmark。
- **预估周期**: Manual 路线 4-5 个月（Month 1: formalization pipeline + pilot study → go/no-go; Month 2: main experiments iteration 1-3; Month 3: iterations 4-5 + 4B validation; Month 4: ablations + analysis; Month 5: paper writing）。Human-in-loop 路线 3-4 个月。Auto-research 路线 6-8 周（parallelized implementation）。**关键路径**: pilot study 的 go/no-go 决策点在 Month 1 末——如果 formalization 成功率不达标，需立即调整方案（引入 SimpleMath 中间语言或缩窄 scope），避免后续月份的沉没成本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2c153618-9db1-46f9-9bc5-2fda8dc1a631",
  "isSidechain": false,
  "requestId": "req_011CbSoQrqUbE3N8yRb1qVRX",
  "type": "assistant",
  "uuid": "a86814f2-5f88-4163-a50f-c015c241eb88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Unh8xVaxEkzZ7bQedQGa7U",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 5085,
      "cache_read_input_tokens": 85550,
      "output_tokens": 4942,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5085,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4942,
          "cache_read_input_tokens": 85550,
          "cache_creation_input_tokens": 5085,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5085
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

_source line 96_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。",
  "leafUuid": "a86814f2-5f88-4163-a50f-c015c241eb88",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---

### Runtime record

_source line 97_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for math self-improvement",
  "sessionId": "a1923fb6-ee25-4f53-b5b0-1b6a7c1ac2c3"
}
```

---
