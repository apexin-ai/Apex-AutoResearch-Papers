# Research conversation: 【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。 【原始 pro

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 86
- **Recorded user turns:** 5
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-3/c4b58ce6-1e05-49ce-9f5b-5ac182d708a4.jsonl`
- **Structured JSON:** [`47bc243f2c01b017084b.json`](../../sessions/47/47bc243f2c01b017084b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T12:37:40.669Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:37:40.669Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "content": "【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。\n\n【原始 proposal】:\n# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition\n\n## Core Problem\n\nHow can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain proof blocks to formal verification?\n\n## Research Opportunity\n\nPseudo-Formalization (Barkallah et al., May 2026) introduced modular proof blocks with explicit premises, conclusions, and dependencies — but verifies them only via LLM, missing ~50% of research-level errors. Safe (Liu et al., ACL 2025) achieves step-level formal verification at 80% proof success but imposes 4-8x cost overhead by verifying ALL steps uniformly. No prior work has exploited PF's self-contained modular structure as a bridge to targeted autoformalization: each PF block's explicit claim statement and premises are far closer to a formal theorem statement than raw NL text, potentially making block-level autoformalization significantly more reliable than whole-proof autoformalization. By using Block Verification confidence as a triage signal, we can route only the 10-20% most uncertain blocks to formal verification, catching errors that LLM verification misses while avoiding the prohibitive cost of universal formalization.\n\n## Research Landscape\n\nCurrent proof verification spans a cost-reliability spectrum with no effective middle ground: LLM-as-judge is cheap but unreliable (best PRM drops from 78.3% to 37.3% on Hard2Verify; Barkallah et al., 2026; Pandit et al., 2025); PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026); Safe verifies each step in Lean 4 with ~80% success but costs 4-8x more compute per step than process reward models (Liu et al., ACL 2025); end-to-end autoformalization pipelines achieve only ~35% success because autoformalization accuracy (66% human-judged, not the 97% reported under LLM-judging) and theorem proving success (~70%) compound poorly across the full pipeline (miniF2F-Lean Revisited, NeurIPS 2025). Adjacent work on uncertainty-guided selective verification has shown 14-100% error reduction with minimal abstention in SMT-based formalization (Ganguly et al., NeurIPS 2025) and adaptive verification allocation achieves 44% fewer verifier calls with higher accuracy on MATH (Qu, arXiv 2026), but neither has been applied to the NL proof verification domain with pseudo-formal structure as the intermediary. Concurrent work update (May 2026): VERGE (Singh et al., arXiv 2026) implements semantic routing between SMT solvers and LLM-ensemble soft verification for general reasoning claims but targets first-order logic rather than mathematical proof blocks and does not exploit modular proof structure; HERMES (Ospanov et al., ICML 2026) is the first agent to interleave informal reasoning with formally verified Lean 4 proof steps, achieving 67% accuracy improvement with 80% fewer FLOPs, but applies uniform formalization without uncertainty-guided selectivity; UCCI (arXiv 2026) provides calibrated uncertainty for cost-optimal LLM cascade routing but operates on model cascades rather than formal/informal verification tiers; ProofSketcher (arXiv 2026) produces typed proof sketches with trusted kernel expansion but without uncertainty-guided routing. None of these concurrent systems exploit PF's modular block structure as autoformalization targets nor combine uncertainty-guided routing with pseudo-formal decomposition for mathematical proof verification.\n\n## Proposed Approach\n\nWe build a two-tier verification pipeline atop Pseudo-Formalization (Barkallah et al., 2026): given a mathematical proof, we decompose it into PF blocks with explicit premises, conclusions, and dependency graphs, then run LLM-based Block Verification using QwQ-32B augmented with calibrated uncertainty scoring via ensemble disagreement (N=5 stochastic forward passes with temperature sampling) and token-level CoT entropy, calibrated via isotonic regression on held-out ArxivMathGradingBench annotations. Blocks below a cost-optimized confidence threshold (targeting the bottom 10-20% by uncertainty) are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging each PF block's explicit premises and conclusion as structured autoformalization targets for substantially higher translation fidelity than raw NL text — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction. We evaluate on ArxivMathGradingBench (error detection recall vs. verification cost), miniF2F (end-to-end correctness), and compare against PF+BV-only, Safe (universal formalization), PRM baselines, and HERMES, with ablations on threshold selection, uncertainty calibration method, and the autoformalization advantage of PF blocks over raw NL.\n\n## Detailed Description\n\nWe propose Uncertainty-Guided Selective Formal Verification, a two-tier proof verification pipeline that bridges the cost-reliability gap between cheap LLM-based verification and expensive universal formal verification of mathematical proofs. Building on Pseudo-Formalization's modular proof blocks — each with explicit premises, conclusions, and inter-block dependencies — we add calibrated uncertainty scoring to Block Verification using ensemble disagreement and CoT entropy. Blocks exceeding a learned confidence threshold are accepted via LLM verification alone; the remaining 10-20% most uncertain blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B and formally verified via Goedel-Prover-V2-32B proof search. A key insight is that PF blocks' self-contained structure makes them far more amenable to reliable autoformalization than raw natural language text, enabling block-level formal verification success rates substantially higher than whole-proof autoformalization (which achieves only ~35% end-to-end on miniF2F). Concurrent work VERGE and HERMES explore formal-informal integration but neither exploits PF's modular structure nor uses uncertainty-guided selectivity for mathematical proof verification. We target near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization.\n\n## Key References\n\n- Pseudo-Formalization for Automatic Proof Verification (arXiv 2026)\n- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025)\n- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2025)\n- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)\n- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)\n- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2026)\n- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2026)\n- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)\n- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)\n- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 300-400 (uncertainty calibration ~50h, StepFun-Formalizer inference/adaptation ~80h, Goedel-Prover-V2 proof search ~100h, baselines and ablations ~70-100h; all on A100-80GB), timeline: 12-16 weeks (2-3 researchers), estimated_gpu_cost: $900-1200\n- **human_in_loop**: gpu_hours: 250-350 (better experiment planning reduces wasted runs), timeline: 8-11 weeks, claude_api_cost: $200-400, estimated_gpu_cost: $750-1050\n- **auto_research**: gpu_hours: 300-400 (compute-bound tasks unchanged), timeline: 5-7 weeks, claude_api_cost: $500-900, estimated_gpu_cost: $900-1200, speed_bottleneck: Lean 4 proof search is inherently sequential (~2-5 min per block via Goedel-Prover-V2); formal verification throughput cannot be parallelized across dependent proof blocks, and Lean kernel type-checking is CPU-bound\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T12:37:40.673Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:37:40.673Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-27T12:37:40.729Z_

【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。

【原始 proposal】:
# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition

## Core Problem

How can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain proof blocks to formal verification?

## Research Opportunity

Pseudo-Formalization (Barkallah et al., May 2026) introduced modular proof blocks with explicit premises, conclusions, and dependencies — but verifies them only via LLM, missing ~50% of research-level errors. Safe (Liu et al., ACL 2025) achieves step-level formal verification at 80% proof success but imposes 4-8x cost overhead by verifying ALL steps uniformly. No prior work has exploited PF's self-contained modular structure as a bridge to targeted autoformalization: each PF block's explicit claim statement and premises are far closer to a formal theorem statement than raw NL text, potentially making block-level autoformalization significantly more reliable than whole-proof autoformalization. By using Block Verification confidence as a triage signal, we can route only the 10-20% most uncertain blocks to formal verification, catching errors that LLM verification misses while avoiding the prohibitive cost of universal formalization.

## Research Landscape

Current proof verification spans a cost-reliability spectrum with no effective middle ground: LLM-as-judge is cheap but unreliable (best PRM drops from 78.3% to 37.3% on Hard2Verify; Barkallah et al., 2026; Pandit et al., 2025); PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026); Safe verifies each step in Lean 4 with ~80% success but costs 4-8x more compute per step than process reward models (Liu et al., ACL 2025); end-to-end autoformalization pipelines achieve only ~35% success because autoformalization accuracy (66% human-judged, not the 97% reported under LLM-judging) and theorem proving success (~70%) compound poorly across the full pipeline (miniF2F-Lean Revisited, NeurIPS 2025). Adjacent work on uncertainty-guided selective verification has shown 14-100% error reduction with minimal abstention in SMT-based formalization (Ganguly et al., NeurIPS 2025) and adaptive verification allocation achieves 44% fewer verifier calls with higher accuracy on MATH (Qu, arXiv 2026), but neither has been applied to the NL proof verification domain with pseudo-formal structure as the intermediary. Concurrent work update (May 2026): VERGE (Singh et al., arXiv 2026) implements semantic routing between SMT solvers and LLM-ensemble soft verification for general reasoning claims but targets first-order logic rather than mathematical proof blocks and does not exploit modular proof structure; HERMES (Ospanov et al., ICML 2026) is the first agent to interleave informal reasoning with formally verified Lean 4 proof steps, achieving 67% accuracy improvement with 80% fewer FLOPs, but applies uniform formalization without uncertainty-guided selectivity; UCCI (arXiv 2026) provides calibrated uncertainty for cost-optimal LLM cascade routing but operates on model cascades rather than formal/informal verification tiers; ProofSketcher (arXiv 2026) produces typed proof sketches with trusted kernel expansion but without uncertainty-guided routing. None of these concurrent systems exploit PF's modular block structure as autoformalization targets nor combine uncertainty-guided routing with pseudo-formal decomposition for mathematical proof verification.

## Proposed Approach

We build a two-tier verification pipeline atop Pseudo-Formalization (Barkallah et al., 2026): given a mathematical proof, we decompose it into PF blocks with explicit premises, conclusions, and dependency graphs, then run LLM-based Block Verification using QwQ-32B augmented with calibrated uncertainty scoring via ensemble disagreement (N=5 stochastic forward passes with temperature sampling) and token-level CoT entropy, calibrated via isotonic regression on held-out ArxivMathGradingBench annotations. Blocks below a cost-optimized confidence threshold (targeting the bottom 10-20% by uncertainty) are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging each PF block's explicit premises and conclusion as structured autoformalization targets for substantially higher translation fidelity than raw NL text — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction. We evaluate on ArxivMathGradingBench (error detection recall vs. verification cost), miniF2F (end-to-end correctness), and compare against PF+BV-only, Safe (universal formalization), PRM baselines, and HERMES, with ablations on threshold selection, uncertainty calibration method, and the autoformalization advantage of PF blocks over raw NL.

## Detailed Description

We propose Uncertainty-Guided Selective Formal Verification, a two-tier proof verification pipeline that bridges the cost-reliability gap between cheap LLM-based verification and expensive universal formal verification of mathematical proofs. Building on Pseudo-Formalization's modular proof blocks — each with explicit premises, conclusions, and inter-block dependencies — we add calibrated uncertainty scoring to Block Verification using ensemble disagreement and CoT entropy. Blocks exceeding a learned confidence threshold are accepted via LLM verification alone; the remaining 10-20% most uncertain blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B and formally verified via Goedel-Prover-V2-32B proof search. A key insight is that PF blocks' self-contained structure makes them far more amenable to reliable autoformalization than raw natural language text, enabling block-level formal verification success rates substantially higher than whole-proof autoformalization (which achieves only ~35% end-to-end on miniF2F). Concurrent work VERGE and HERMES explore formal-informal integration but neither exploits PF's modular structure nor uses uncertainty-guided selectivity for mathematical proof verification. We target near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization.

## Key References

- Pseudo-Formalization for Automatic Proof Verification (arXiv 2026)
- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025)
- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2025)
- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)
- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)
- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2026)
- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2026)
- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)
- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)
- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)

## Resource Estimate

- **manual**: gpu_hours: 300-400 (uncertainty calibration ~50h, StepFun-Formalizer inference/adaptation ~80h, Goedel-Prover-V2 proof search ~100h, baselines and ablations ~70-100h; all on A100-80GB), timeline: 12-16 weeks (2-3 researchers), estimated_gpu_cost: $900-1200
- **human_in_loop**: gpu_hours: 250-350 (better experiment planning reduces wasted runs), timeline: 8-11 weeks, claude_api_cost: $200-400, estimated_gpu_cost: $750-1050
- **auto_research**: gpu_hours: 300-400 (compute-bound tasks unchanged), timeline: 5-7 weeks, claude_api_cost: $500-900, estimated_gpu_cost: $900-1200, speed_bottleneck: Lean 4 proof search is inherently sequential (~2-5 min per block via Goedel-Prover-V2); formal verification throughput cannot be parallelized across dependent proof blocks, and Lean kernel type-checking is CPU-bound


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "cf4ec307-ad39-4057-9e4d-052dfdb78bd1",
  "type": "user",
  "uuid": "644035de-08a8-4da1-996b-7812c4dd7770",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T12:37:40.728Z_

```json
{
  "parentUuid": "644035de-08a8-4da1-996b-7812c4dd7770",
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
  "uuid": "a6c1a3a1-2eff-4563-9679-ddb6a46dac99",
  "timestamp": "2026-05-27T12:37:40.728Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T12:37:40.728Z_

```json
{
  "parentUuid": "a6c1a3a1-2eff-4563-9679-ddb6a46dac99",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "a9c206c6-48be-45fd-be3d-54bc5056ced0",
  "timestamp": "2026-05-27T12:37:40.728Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
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
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Assistant

_source line 7 · 2026-05-27T12:37:55.959Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the 终审 agent (Meta Judge) in the first phase. They've provided the original proposal that has passed the triple-consensus triage. Now they're asking me to remember this proposal and prepare for the iterative phase (角色 B).

Wait, let me re-read. They say "以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。"


So this is just the setup - they're telling me the proposal passed triage, and I should remember it for when the worker outputs come in. I'm reading through the proposal now to understand its core structure: it's about building a two-tier verification pipeline for mathematical proofs that decomposes them into pseudo-formalization blocks, uses LLM-based verification with calibrated uncertainty metrics like ensemble disagreement and chain-of-thought entropy, and then selectively routes only the most uncertain 10-20% of blocks to formal verification.

The key technical components involve pseudo-formalization decomposition, uncertainty scoring through ensemble methods and entropy analysis, isotonic regression for calibration, and then autoformalization and formal verification using specific models like StepFun-Formalizer-32B and Goedel-Prover-V2-32B, all evaluated on benchmarks like ArxivMathGradingBench and miniF2F. I'm noting the key references they cite - papers on pseudo-formalization, safe verification approaches, and step-level verification benchmarks - so I can track them as the worker outputs come in.

Now I'm compiling the remaining references on formal uncertainty, test-time compute allocation, verification engines, and efficient mathematical reasoning in LLMs, along with the latest work on Goedel-Prover-V2 and confidence-based verification methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c206c6-48be-45fd-be3d-54bc5056ced0",
  "isSidechain": false,
  "requestId": "req_011CbT5vxAekBziBQzBnJGfs",
  "type": "assistant",
  "uuid": "ced79b68-7285-4d80-9540-e9a1c2cbf97b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E11nY3LbdySYbUE2AQsJtB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 16543,
      "output_tokens": 1363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1363,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 3541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3541
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

_source line 8 · 2026-05-27T12:38:02.850Z_

已完整阅读并记录原始 proposal。以下是我作为终审 agent 的状态确认：

**Proposal 标题**: Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition

**核心 idea 摘要**: 利用 Pseudo-Formalization 的模块化证明块结构，结合校准的不确定性评分（ensemble disagreement + CoT entropy），仅将最不确定的 10-20% 证明块路由到 Lean 4 形式化验证，在成本和可靠性之间取得中间地带。

**已锁定的引用清单**（10 篇，后续重写时必须逐条保留）:
1. Pseudo-Formalization (arXiv 2026) — Barkallah et al.
2. Safe (ACL 2025) — Liu et al.
3. Hard2Verify (arXiv 2025) — Pandit et al.
4. miniF2F-Lean Revisited (NeurIPS 2025)
5. Grammars of Formal Uncertainty (NeurIPS 2025) — Ganguly et al.
6. Adaptive Test-Time Compute Allocation (arXiv 2026) — Qu
7. VERGE (arXiv 2026) — Singh et al.
8. HERMES (ICML 2026) — Ospanov et al.
9. Goedel-Prover-V2 (ICLR 2026)
10. Reasoning with Confidence / Uncertainty Heads (arXiv 2025)

**资源估计已记录**: 300-400 GPU hours (A100-80GB), 12-16 weeks, $900-1200 GPU cost。

已准备就绪，等待第一轮「发掘 agent」和「补救 agent」的输出，届时我将以**角色 B（迭代中）**进行整合、交叉验证、更新 proposal 并估计中稿概率。请发送 worker 输出。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ced79b68-7285-4d80-9540-e9a1c2cbf97b",
  "isSidechain": false,
  "requestId": "req_011CbT5vxAekBziBQzBnJGfs",
  "type": "assistant",
  "uuid": "53d9df8e-2615-4f5d-b5c7-fe0bc19c2d8a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E11nY3LbdySYbUE2AQsJtB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 3541,
      "cache_read_input_tokens": 16543,
      "output_tokens": 1363,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3541,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1363,
          "cache_read_input_tokens": 16543,
          "cache_creation_input_tokens": 3541,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3541
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
  "lastPrompt": "【背景】: 以下 proposal 已通过外部入口筛选（triple-consensus triage），确认 GO。请记住这份 proposal 的完整内容，后续你将以「角色 B：迭代中」整合 worker 输出并更新它。  【原始 proposal】: # Uncertainty-Guided Selective Formal Verification via Pseudo-Formal De…",
  "leafUuid": "53d9df8e-2615-4f5d-b5c7-fe0bc19c2d8a",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 12 · 2026-05-27T12:44:15.129Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:44:15.129Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "content": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have enough research context. Let me synthesize my assessment.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- [Pseudo-Formalization for Automatic Proof Verification (arXiv:2605.20531)](https://arxiv.org/abs/2605.20531) (arXiv, May 2026): 核心前序工作。引入模块化 PF 块（显式前提/结论/依赖图），Block Verification Pareto-dominates LLM-as-judge，但在 ArxivMathGradingBench 上仍漏检约 50% 错误。关键：PF 块的自包含结构是本 proposal 的核心杠杆。\n- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/): 首次用 Lean 4 逐步形式化验证 LLM 输出，但对所有步骤均匀验证，4-8x 成本开销。本 proposal 试图选择性替代之。\n- [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760): 首个交替非形式推理与形式化 Lean 4 验证步骤的 agent，67% 准确率提升 + 80% FLOP 减少。**但它面向 proof generation 而非 proof verification，且无 uncertainty-guided 选择性——对所有步骤均做形式化。** 这是最关键的差异化对手。\n- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047): 提出 PCFG 框架对 LLM 输出做不确定性分类，选择性验证在 SMT-based formalization 中实现 14-100% 错误减少。**直接验证了 selective verification 范式的可行性**，但仅在 first-order logic 领域，未应用于数学证明块。\n- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613): miniF2F pass@32 达 88.1%（自修正模式 90.4%），verifier-guided self-correction 是本 proposal formal verification 层的核心引擎。\n- [StepFun-Formalizer-32B (AAAI 2026)](https://arxiv.org/abs/2508.04440): BEq@1 40.5% on FormalMATH-Lite——SOTA 但仍然有限。proposal 依赖此作为 autoformalization 层。\n- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108): 端到端 autoformalization pipeline 成功率仅 ~36%（非文献中常报的 97%），人工评估表明 autoformalization 准确率被 LLM judging 严重高估。\n- [A Unified Approach to Routing and Cascading for LLMs (2024)](https://arxiv.org/abs/2410.10347): 提供 routing + cascading 的理论最优框架，cascade routing 在所有设置上提升 4%。\n- [LLMs are Overconfident (2025-2026)](https://arxiv.org/pdf/2510.26995): RL-trained LLMs 系统性过度自信，平均高估正确概率 20-60%。**直接威胁本 proposal 的 uncertainty calibration 假设。**\n- [VERGE (arXiv 2026)](https://arxiv.org/abs/2601.20055): 语义路由 SMT/LLM-ensemble，但针对 FOL claims 而非数学证明块。\n- 调研总结：当前领域正在从\"全量形式化 vs. 纯 LLM 验证\"的二元格局转向**选择性、成本感知的混合验证**。核心突破点在于 (a) 如何构建可靠的 triage 信号，(b) 如何设计中间表示使 autoformalization 更 tractable。Ganguly 等人验证了 selective verification 的可行性但局限于 FOL；HERMES 验证了 informal-formal interleaving 但不做选择性路由。本 proposal 恰好占据了\"选择性 + 模块化中间表示\"的空白位。\n\n---\n\n【发掘点 1】\n- 维度: 前提假设质疑 / trivial alternative 威胁\n- 内容: **\"Confident-but-Wrong\" 盲区是本 proposal 最大的未显式化风险。** 整个 pipeline 的有效性建立在一个关键假设上：BV 漏检的错误主要集中在 BV 不确定（高 uncertainty）的块上。但文献（2025-2026 多篇 calibration 研究）已充分证明 LLM 系统性过度自信——RL-trained 模型平均高估正确概率 20-60%。如果 BV 漏检的 50% 错误中有相当比例是 BV *高置信度判错*（即 confident-but-wrong），那么 uncertainty-guided routing 根本无法触达这些错误，整个 selective verification 的收益上界会急剧缩小。**Proposal 必须在 framing 中显式讨论这一风险**，并给出缓解策略——例如：(a) 分析 PF+BV 在 ArxivMathGradingBench 上的错误分布，区分\"不确定且错误\"vs\"自信且错误\"的比例；(b) 论证 PF 的模块化分解天然将\"难以验证\"的推理步骤隔离到独立块中，使这些块即使 BV 过度自信也会在 ensemble disagreement 中产生更高方差；(c) 引入 \"structural difficulty\" 信号（如块内推理步数、依赖的定理数量）作为 uncertainty 之外的补充路由信号。**不直面这个问题，审稿人大概率会在 rebuttal 阶段提出，且它可能是 fatal 的。**\n- 价值: 直击 Novelty 和 Soundness 的核心：如果 triage 信号不可靠，selective verification 退化为随机采样 formal verification，novelty claim 崩塌。显式讨论并缓解此风险将极大增强 claim 的可信度。\n- 调研依据: 基于 [LLMs are Overconfident (2025)](https://arxiv.org/pdf/2510.26995)、[Decoupling Reasoning and Confidence (2026)](https://arxiv.org/pdf/2603.09117) 关于 RL-trained LLM 过度自信的发现，以及 [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047) 中 token entropy 作为 uncertainty 信号在不同 domain 效果差异巨大（逻辑任务 +34.8% vs 事实任务 -44.5%）的发现。\n\n【发掘点 2】\n- 维度: novelty 锐化\n- 内容: **PF 块作为 autoformalization 目标的结构性优势——这是本 proposal 最独特的 insight，但目前论述过于轻描淡写。** Proposal 中仅用 \"far more amenable\" \"substantially higher\" 等模糊措辞来声称 PF 块比 raw NL 更适合 autoformalization，但没有给出任何结构性分析来支撑这个 claim。应当显式拆解 PF 块与 Lean 4 theorem statement 之间的结构对齐：(a) PF 块有显式 typed premises → 直接对应 Lean 4 的 `hypothesis` 列表；(b) PF 块有单一 conclusion → 直接对应 Lean 4 的 `goal`；(c) PF 块无环境上下文依赖 → 消除了 whole-proof autoformalization 中最棘手的上下文补全问题。这种\"PF 块 ≈ 半结构化定理声明\"的论证如果做扎实，可以将 novelty 从\"工程组合\"提升为\"modular proof decomposition 是 informal-formal verification 的天然桥梁\"这一更具普适性的 insight。这也是与 HERMES 最本质的差异：HERMES 在生成时交替 informal/formal，而本 proposal 通过 PF 的模块化分解在验证时创建了结构化的 formalization 入口点。\n- 价值: 将核心 novelty 从 \"combination of existing techniques\" 提升为 \"architectural insight about modular decomposition as a bridge\"，直接命中 Novelty 维度。如果审稿人认为这只是 engineering，中稿概率大幅下降；如果审稿人认为这揭示了一个 reusable insight，则显著提升。\n- 调研依据: 基于 [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108) 揭示端到端 autoformalization 仅 36% 成功率的原因分析（上下文补全和 statement 歧义是主要瓶颈），以及 [StepFun-Formalizer (AAAI 2026)](https://arxiv.org/abs/2508.04440) 在 FormalMATH-Lite 上 40.5% BEq@1 的性能——PF 块的结构化输入有望显著缩小这两个瓶颈。\n\n【发掘点 3】\n- 维度: significance 提升 / 核心 claim 强化\n- 内容: **PF 的 inter-block dependency graph 是一个被严重低估的信号源，应纳入路由策略以强化 significance。** 当前 proposal 仅用 uncertainty 作为路由信号，但 PF 提供了一个免费的附加结构：块间依赖图。一个 high-fan-out 块（被多个下游块依赖）如果验证错误，错误会级联传播到所有依赖块——这种块即使 BV 置信度较高，也值得投入 formal verification。将路由策略从纯 uncertainty-based 升级为 \"uncertainty × dependency criticality\" 的双信号策略，有三个好处：(a) 缓解发掘点 1 的 confident-but-wrong 问题（critical 块即使 BV 不 uncertain 也会被路由）；(b) 让 PF 的独特结构更深度地参与 pipeline 而不仅仅是 autoformalization 的输入格式，增强 \"PF is the bridge\" 的 narrative；(c) 与 cascade routing 文献（Unified Routing + Cascading, 2024）的理论框架对齐——将 dependency criticality 类比为 \"cost of being wrong\" 系数。\n- 价值: 从 \"single-signal routing\" 升级为 \"graph-aware multi-signal routing\"，同时命中 Novelty（新的路由策略）和 Significance（利用了 PF 的独特结构属性，非其他方法可获得的信号）。\n- 调研依据: 基于 [A Unified Approach to Routing and Cascading (2024)](https://arxiv.org/abs/2410.10347) 的 cascade routing 理论框架（routing 决策应考虑 cost of deferral），以及 PF 原文中 inter-block dependency graph 的定义。\n\n【发掘点 4】\n- 维度: related work 差异化\n- 内容: **与 HERMES 的差异化必须从\"功能对比\"提升到\"范式差异\"。** 当前 proposal 对 HERMES 的区分停留在表层：HERMES 做 uniform formalization，本 proposal 做 selective formalization。但这掩盖了一个更根本的差异：HERMES 是一个 **proof generation** agent（生成新证明时交替 informal/formal），而本 proposal 是一个 **proof verification** pipeline（检查已有证明的正确性）。这两个任务的约束完全不同——generation 时你可以控制输出格式，verification 时你必须处理任意格式的输入证明。PF 的存在恰恰解决了 verification 场景下的核心困难：将任意格式的 NL 证明转化为可模块化处理的结构。此外，HERMES 的 80% FLOP 减少是相对于 reward-based 方法（如 Best-of-N），而本 proposal 的成本比较对象是 universal formal verification（Safe）——两者的 cost baseline 不同，不应直接比较。建议在 related work 中明确建立 \"generation vs. verification\" 的 taxonomy，将本 proposal 定位为 \"the first uncertainty-guided selective formal verification system for NL proof checking\"。\n- 价值: 清晰的 taxonomy 防止审稿人将本工作与 HERMES 混为一谈（这是最可能的 novelty 质疑来源），直接命中 Related Work 差异化维度。\n- 调研依据: 基于 [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760) 的实际定位（agent for proof generation with formal checking）与本 proposal 定位（pipeline for proof verification with selective formalization）的根本差异。\n\n【发掘点 5】\n- 维度: significance 提升\n- 内容: **Framing 可以从 \"cost-reliability optimization\" 提升为更具普适意义的 insight：\"modular proof decomposition as a natural bridge between informal and formal verification.\"** 当前 proposal 的叙事是\"我们找到了一个更好的 cost-reliability tradeoff\"——这是一个 system-level 的贡献叙事，容易被审稿人归为 engineering paper。但如果核心叙事转变为\"我们发现模块化证明分解（如 PF）天然地创建了从非形式到形式验证的桥梁，并通过实验验证了这一桥梁的有效性\"，则贡献从 system optimization 升级为 architectural insight：不仅对本 pipeline 有效，对未来任何需要混合 informal/formal 验证的系统都有指导意义。这个 reframing 不需要改变任何技术方案，只需要调整叙事重心。\n- 价值: 将论文从\"又一个 pipeline 优化\"提升为\"提出了一个 reusable architectural principle\"，显著命中 Significance 维度。AAAI 审稿人更看重 insight 的普适性。\n- 调研依据: 基于领域整体趋势判断——当前 verification 文献（Safe, HERMES, VERGE, ProofSketcher）都在探索 informal-formal 的混合策略，但没有任何一篇工作明确提出\"modular decomposition is the bridge\"这一 architectural claim。\n\nSources:\n- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)\n- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)\n- [HERMES: Efficient and Verifiable Mathematical Reasoning (ICML 2026)](https://arxiv.org/abs/2511.18760)\n- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)\n- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)\n- [StepFun-Formalizer-32B (AAAI 2026)](https://arxiv.org/abs/2508.04440)\n- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)\n- [VERGE: Formal Refinement and Guidance Engine (arXiv 2026)](https://arxiv.org/abs/2601.20055)\n- [A Unified Approach to Routing and Cascading for LLMs](https://arxiv.org/abs/2410.10347)\n- [ProofSketcher (arXiv 2026)](https://arxiv.org/abs/2604.06401)\n- [LLMs are Overconfident (2025)](https://arxiv.org/pdf/2510.26995)\n- [Decoupling Reasoning and Confidence (2026)](https://arxiv.org/pdf/2603.09117)\n\n【补救 agent 本轮输出】:\nNow I have comprehensive research context. Let me compile my thorough analysis of the experimental design.\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- [Pseudo-Formalization for Automatic Proof Verification, arXiv 2605.20531](https://arxiv.org/abs/2605.20531) (arXiv 2026): 评估于 Hard2Verify 和 ArxivMathGradingBench（仅 35 篇论文、40 个已知错误）。用 error-finding precision 和 recall 作为核心指标。PF+BV Pareto 优于 LLM-as-judge baseline。\n- [Safe: Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/) (ACL 2025): 提出 FormalStep 基准（30,809 条 formal statements），在多个数学推理数据集上评估。验证成功率约 80%。开源代码和数据。\n- [HERMES](https://arxiv.org/abs/2511.18760) (ICML 2026): 在 4 个数学推理基准上评测，对比 base model。展示了 token usage 大幅减少。报告了 accuracy 提升和 FLOPs 减少。\n- [Grammars of Formal Uncertainty, Ganguly et al.](https://arxiv.org/abs/2505.20047) (NeurIPS 2025): PCFG 框架建模 LLM 输出的不确定性。Grammar entropy 在逻辑任务上 AUROC>0.93。SMT autoformalization 对准确率影响是 domain-specific 的（逻辑任务 +34.8%，事实任务 -44.5%）。评估了 5 个 frontier LLM。\n- [miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108) (NeurIPS 2025): 端到端 autoformalization pipeline 成功率约 36%（原 miniF2F）。LLM 判定的 autoformalization 准确率 97% 被人工审核修正为 66%。提出 miniF2F-v2 后最佳准确率提升至 70%。\n- [Goedel-Prover-V2](https://arxiv.org/pdf/2508.03613) (ICLR 2026): Lean 4 proof search SOTA。HILBERT 在 miniF2F 上达到 99.2%。支持 self-correction。\n- [StepFun-Formalizer-32B](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B) (2025): NL-to-Lean4 autoformalization。type-check rate 在不同 benchmark 上从 4%–57.2% 不等。BEq+ 准确率约 30%。\n- [ThinkPRM / Process Reward Models](https://arxiv.org/pdf/2504.16828) (2025-2026): ThinkPRM 是当前 data-efficient PRM SOTA。Qwen2.5-Math-PRM 系列是主流 baseline。在 ProcessBench 上评测。\n- [DiscoUQ](https://arxiv.org/pdf/2603.20975) (2026): LLM ensemble 不确定性量化框架，利用 inter-agent disagreement 结构信息，AUROC 0.802，优于 baseline。\n- 调研总结: 该领域当前实验标准要求 (1) 在 error detection 任务上报告 precision/recall 及其 tradeoff，(2) 对 cost 进行严格归一化对比（per-step 或 per-proof），(3) ablation 需隔离各不确定性信号的贡献，(4) autoformalization 准确率需人工或 formal verification 验证（不可仅依赖 LLM judge），(5) 统计显著性分析在小数据集上尤为重要。审稿人通常会要求 Pareto 曲线展示 cost-accuracy tradeoff 以及 failure case 分析。\n\n---\n\n【缺陷 1】\n- 类别: 评估方案缺陷\n- 问题: ArxivMathGradingBench 仅含 35 篇论文、40 个已知错误，作为核心评估基准统计功效严重不足。在如此小的样本上报告 error detection recall 的差异（例如从 50% 提升到 70%）对应的仅是 20→28 个 error 的变化，置信区间极宽。更严重的是，proposal 要求从这 40 个标注中还要分出 held-out set 做 isotonic regression 校准——校准集可能仅有 10-15 个正例，isotonic regression 在这种规模上极易过拟合，校准结果不可靠。审稿人几乎必然会质疑这些结果的统计显著性。\n- 严重度: 可补救\n- 补救方案: \n  (a) 报告 bootstrap confidence intervals（至少 1000 次 resample）和 McNemar's test 或 paired permutation test 来量化与 baseline 差异的统计显著性。\n  (b) 补充一个合成评估集：对 Hard2Verify 中的 competition-level 问题，利用已知正确解（ground truth）和已知错误解（LLM 生成的错误 proof）构建更大规模的 error detection 评估集（目标 200+ 错误实例）。这在 PF 原文中已有 Hard2Verify 的实验数据可参考。\n  (c) 对 isotonic regression 校准采用 leave-one-out cross-validation 而非简单 train/test split，或者改用 Platt scaling（参数更少，更适合小数据）。\n  (d) 考虑在 FormalProofBench（graduate-level proofs, 2026）上做额外评估，以增加 research-level 评估的覆盖度。\n- 调研依据: ArxivMathGradingBench 的规模来自 [Barkallah et al., 2026] 原文；Ganguly et al. (NeurIPS 2025) 在其 selective verification 实验中评估了 5 个 LLM 在多个 domain 上的表现以获得足够统计功效。\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: miniF2F 被列为评估基准之一（\"end-to-end correctness\"），但 miniF2F 是一个 theorem proving benchmark，不是 proof verification benchmark。本 proposal 的核心任务是验证给定 proof 的正确性，而非生成新 proof。Proposal 未说明如何将 miniF2F 适配为 verification 评测：(a) 验证对象是什么？是 LLM 生成的解？是已知正确解？还是 mix？(b) 如何构造 negative examples（错误 proof）？(c) 评测指标是什么——verification accuracy 还是 error detection recall/precision？如果不厘清这一点，审稿人会认为 miniF2F 实验缺乏说服力。\n- 严重度: 可补救\n- 补救方案:\n  (a) 明确 miniF2F 的评测协议：推荐方案是用 SOTA reasoning LLM（如 QwQ-32B）为 miniF2F 的 488 个问题生成 N 个 candidate proofs（混合正确和错误），然后用本系统进行 verification，以 verification precision/recall 作为指标。\n  (b) 或者改为使用 miniF2F-v2（NeurIPS 2025 的修正版）验证 autoformalization pipeline 本身的质量——即 PF block autoformalization 在 miniF2F-v2 的 formal statements 上的 type-check rate 和语义正确率，作为组件级评估。\n  (c) 无论哪种方案，都需要与 Safe 在同一 miniF2F 实验设定下比较，保证对照公平。\n- 调研依据: [miniF2F-Lean Revisited, NeurIPS 2025] 明确指出 miniF2F 是 theorem proving 基准；Safe (ACL 2025) 的 miniF2F 实验是验证 LLM 生成的解的正确性，本 proposal 需与其对齐。\n\n【缺陷 3】\n- 类别: baseline 不足或过时\n- 问题: PRM baseline 未指定具体模型。2025-2026 年 PRM 领域发展迅速，当前 SOTA 包括 ThinkPRM（verbalized process reward，NeurIPS 2025 area）、Qwen2.5-Math-PRM-72B、以及 formally-verified PRM（Generalizable PRMs via Formally Verified Training Data, 2025）。仅说\"PRM baselines\"过于模糊，审稿人会要求指定具体模型并解释选择理由。此外，proposal 未将 ThinkPRM 作为 baseline 纳入，而 ThinkPRM 作为 verbalized step-level verifier 与本 proposal 的 LLM-based Block Verification 直接可比。\n- 严重度: 可补救\n- 补救方案:\n  (a) 明确纳入至少两个 PRM baseline：Qwen2.5-Math-PRM-72B（当前最强开源 PRM）和 ThinkPRM（data-efficient verbalized PRM，与 BV 的 CoT verification 最直接可比）。\n  (b) 在 error detection 任务上用相同 evaluation protocol 对比这些 PRM：给定 proof step/block，PRM 的 step-level score 作为 error detection signal，report precision/recall。\n  (c) 如果 compute 不允许 72B PRM，至少用 Qwen2.5-Math-PRM-7B + ThinkPRM-7B 作为可行替代，并注明参数量差异。\n- 调研依据: [ThinkPRM, 2025]、[Qwen2.5-Math-PRM, 2025]、[Generalizable PRMs via Formally Verified Training Data, 2025] 是当前 PRM 领域的核心 baseline。\n\n【缺陷 4】\n- 类别: ablation 不完整\n- 问题: Proposal 提到 ablation \"on threshold selection, uncertainty calibration method, and the autoformalization advantage of PF blocks over raw NL\"，但缺少两个关键 ablation：\n  (1) 两个不确定性信号（ensemble disagreement vs. CoT entropy）的独立贡献。当前设计将二者融合后做 isotonic regression 校准，但未计划分别评估它们的 error detection AUROC。如果其中一个信号贡献极小，融合反而可能引入噪声。Ganguly et al. (NeurIPS 2025) 明确证明不确定性信号是 task-dependent 的，本 proposal 需要验证在 math proof verification 这一特定任务上哪些信号最有效。\n  (2) Autoformalization failure 的处理策略 ablation。当 StepFun-Formalizer 无法成功 autoformalize 或 Goedel-Prover-V2 proof search 超时（proposal 估计 2-5 min/block），系统的 fallback 策略是什么？Accept the block？Reject it？Report \"uncertain\"？不同 fallback 策略对 end-to-end recall/precision 影响很大，必须做 ablation。\n- 严重度: 可补救\n- 补救方案:\n  (a) 新增 ablation 表格：ensemble disagreement only / CoT entropy only / combined 三种配置的 AUROC、ECE（Expected Calibration Error）、和 error detection recall@fixed-cost 对比。\n  (b) 新增 autoformalization failure handling ablation：fallback-accept（乐观） / fallback-reject（保守） / fallback-to-majority-vote（再做一轮 ensemble BV）三种策略的 precision/recall tradeoff。\n  (c) 报告 Goedel-Prover-V2 proof search 在 PF block 粒度上的 success rate 和 timeout rate，以量化 formal verification tier 的 coverage。\n- 调研依据: Ganguly et al. (NeurIPS 2025) 展示了不同 uncertainty signal 在不同 task 上效果差异巨大（AUROC 变化范围超过 0.3）；DiscoUQ (2026) 证明 ensemble disagreement 结构信息比简单投票更有效。\n\n【缺陷 5】\n- 类别: compute 公平性问题\n- 问题: Cost comparison 存在两个不透明之处：\n  (1) LLM verification tier 的 ensemble 成本未计入总成本：N=5 stochastic forward passes 意味着 Block Verification 阶段本身已是 single-pass BV 的 5 倍成本。Proposal 声称总成本为 Safe 的 1.5-2x，但这个估算是否已包含 5x 的 ensemble 开销？如果 PF+BV single-pass 是 1x，ensemble BV 已是 5x，再加上 10-20% blocks 的 autoformalization + proof search，总成本可能远超 2x。\n  (2) 与 Safe 的成本对比缺少统一度量单位：Safe 的\"4-8x cost overhead\"是相对于什么 baseline？是相对于 no verification（直接接受 LLM 解答）？还是相对于 single-pass BV？Proposal 需要定义统一的 cost unit（如 GPU-seconds per proof, FLOPs per proof, 或 API cost per proof），并在这个统一单位下对比所有方法。\n- 严重度: 可补救\n- 补救方案:\n  (a) 定义统一的 cost metric：推荐用 GPU-seconds per proof（或 per 1000 tokens of proof text）作为 cost unit，涵盖所有计算环节。\n  (b) 构建详细 cost breakdown table：PF decomposition cost + ensemble BV cost (5 × single BV) + routing overhead + autoformalization cost (per routed block) + proof search cost (per routed block, including timeout cases) = total cost。\n  (c) 绘制 cost-accuracy Pareto 曲线：横轴为 normalized cost（relative to single-pass BV），纵轴为 error detection recall（或 F1）。在这条曲线上标注所有对比方法（PF+BV single-pass, PF+BV ensemble, proposed selective, Safe universal, PRM baselines）。这种 Pareto 分析是该领域审稿人的标准期望。\n  (d) 考虑 ensemble size 的 ablation：N=3 vs. N=5 vs. N=7，验证 N=5 是否是 cost-quality sweet spot。\n- 调研依据: Safe (ACL 2025) 报告的 4-8x 是 per-step overhead vs. no formal verification；Qu (arXiv 2026) 的 adaptive verification 工作明确以 verifier call 次数作为 cost metric 并提供 Pareto 分析。\n\n【缺陷 6】\n- 类别: 实验设计不足\n- 问题: \"PF blocks 比 raw NL 更易 autoformalize\"是本 proposal 的核心假设之一（\"a key insight is that PF blocks' self-contained structure makes them far more amenable to reliable autoformalization than raw natural language text\"），但 ablation 设计缺乏具体对照实验方案。这个 claim 需要一个严格的 controlled comparison 来量化 PF block format 带来的 autoformalization quality gain。目前只说\"ablation on the autoformalization advantage of PF blocks over raw NL\"，但未回答关键设计问题：(a) 什么是\"raw NL\"对照组？是整段 proof text 还是按句切分的 proof step？(b) 用什么指标衡量 autoformalization 质量？type-check rate？BEq 语义匹配？人工评估？(c) 如何控制变量——同一 proof 的 PF block 与对应的 NL fragment 必须 align 才能比较。\n- 严重度: 可补救\n- 补救方案:\n  (a) 设计 paired comparison 实验：对同一组 proof，一组输入为 PF block（包含 explicit premises/conclusion），另一组输入为对应的 raw NL proof fragment（从原始 proof 中提取相同推理步骤但不含 PF 结构标注）。两组都用 StepFun-Formalizer-32B autoformalize to Lean 4。\n  (b) 评估指标至少三个：(i) Lean 4 type-check rate（语法正确性），(ii) Lean 4 proof search success rate via Goedel-Prover-V2（语义正确性），(iii) 如果 sample size 足够，做人工评估 sample check（参考 miniF2F-Lean Revisited 的教训：LLM-judged autoformalization 准确率从 97% 降到 66%）。\n  (c) 报告 paired t-test 或 Wilcoxon signed-rank test 的 p-value。\n- 调研依据: [miniF2F-Lean Revisited, NeurIPS 2025] 明确警告 autoformalization 质量不能仅用 LLM judge 评估；[StepFun-Formalizer, 2025] 报告 type-check rate 在不同 benchmark 上变化极大（4%–57%），说明 input format 对 autoformalization 质量影响很大，支持做 controlled comparison。\n\n【缺陷 7】\n- 类别: 可行性问题\n- 问题: Proposal 的 resource estimate 看似合理（300-400 GPU hours on A100-80GB），但有一个潜在瓶颈未被充分讨论：Lean 4 proof search 是 CPU-bound 且 sequential（proposal 自己承认\"2-5 min per block\"）。如果 10-20% 的 blocks 被路由到 formal verification，一个中等长度的 research paper proof 可能有 20-50 个 PF blocks，其中 2-10 个需要 formal verification，每个 2-5 min，单个 proof 的 formal verification 就需要 4-50 min。在 ArxivMathGradingBench 的 35 篇论文（每篇可能有多个 proof）上，加上 ablation 和多种配置的重复实验，Lean 4 proof search 时间可能成为真正的瓶颈。此外，Goedel-Prover-V2-32B 需要 GPU 推理来生成 proof candidate，再用 Lean kernel CPU-check，这是 GPU+CPU 混合负载，需要合理调度。\n- 严重度: 可补救\n- 补救方案:\n  (a) 明确 Lean 4 proof search 的 timeout 策略（建议 per-block timeout 5 min，total per-proof timeout 30 min）。\n  (b) 估算 formal verification tier 的总 wall-clock time：假设 35 篇 × 平均 30 blocks/paper × 15% routing rate × 3.5 min/block = ~550 min ≈ 9h for one pass。加上 ablation 配置（~5 种 × 9h = 45h wall-clock），这在 timeline 内是可行的但 tight。\n  (c) 在 resource estimate 中分开列出 GPU hours（Goedel-Prover-V2 推理）和 CPU hours（Lean kernel type-checking），避免混淆。\n  (d) 对于 miniF2F 的更大规模评估，可以利用 independent blocks 之间的并行性来加速（非 dependent blocks 可并行 proof search）。\n- 调研依据: HERMES (ICML 2026) 报告了 80% fewer FLOPs，但其 Lean 4 interaction overhead 仍显著；Goedel-Prover-V2 (ICLR 2026) 的 self-correction loop 意味着每个 block 可能需要多轮 proof search。\n\nSources:\n- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)\n- [Safe: Enhancing Mathematical Reasoning via Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/)\n- [HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs](https://arxiv.org/abs/2511.18760)\n- [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047)\n- [miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108)\n- [Goedel-Prover-V2](https://arxiv.org/pdf/2508.03613)\n- [StepFun-Formalizer-32B](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/pdf/2504.16828)\n- [DiscoUQ: Structured Disagreement Analysis](https://arxiv.org/pdf/2603.20975)\n- [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/html/2605.18796)"
}
```

---

### Runtime record

_source line 13 · 2026-05-27T12:44:15.129Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:44:15.129Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

## Round 2

25 recorded events

### User

_source line 14 · 2026-05-27T12:44:15.158Z_

【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have enough research context. Let me synthesize my assessment.

---

【状态】: 有发掘空间

【前置调研发现】
- [Pseudo-Formalization for Automatic Proof Verification (arXiv:2605.20531)](https://arxiv.org/abs/2605.20531) (arXiv, May 2026): 核心前序工作。引入模块化 PF 块（显式前提/结论/依赖图），Block Verification Pareto-dominates LLM-as-judge，但在 ArxivMathGradingBench 上仍漏检约 50% 错误。关键：PF 块的自包含结构是本 proposal 的核心杠杆。
- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/): 首次用 Lean 4 逐步形式化验证 LLM 输出，但对所有步骤均匀验证，4-8x 成本开销。本 proposal 试图选择性替代之。
- [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760): 首个交替非形式推理与形式化 Lean 4 验证步骤的 agent，67% 准确率提升 + 80% FLOP 减少。**但它面向 proof generation 而非 proof verification，且无 uncertainty-guided 选择性——对所有步骤均做形式化。** 这是最关键的差异化对手。
- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047): 提出 PCFG 框架对 LLM 输出做不确定性分类，选择性验证在 SMT-based formalization 中实现 14-100% 错误减少。**直接验证了 selective verification 范式的可行性**，但仅在 first-order logic 领域，未应用于数学证明块。
- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613): miniF2F pass@32 达 88.1%（自修正模式 90.4%），verifier-guided self-correction 是本 proposal formal verification 层的核心引擎。
- [StepFun-Formalizer-32B (AAAI 2026)](https://arxiv.org/abs/2508.04440): BEq@1 40.5% on FormalMATH-Lite——SOTA 但仍然有限。proposal 依赖此作为 autoformalization 层。
- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108): 端到端 autoformalization pipeline 成功率仅 ~36%（非文献中常报的 97%），人工评估表明 autoformalization 准确率被 LLM judging 严重高估。
- [A Unified Approach to Routing and Cascading for LLMs (2024)](https://arxiv.org/abs/2410.10347): 提供 routing + cascading 的理论最优框架，cascade routing 在所有设置上提升 4%。
- [LLMs are Overconfident (2025-2026)](https://arxiv.org/pdf/2510.26995): RL-trained LLMs 系统性过度自信，平均高估正确概率 20-60%。**直接威胁本 proposal 的 uncertainty calibration 假设。**
- [VERGE (arXiv 2026)](https://arxiv.org/abs/2601.20055): 语义路由 SMT/LLM-ensemble，但针对 FOL claims 而非数学证明块。
- 调研总结：当前领域正在从"全量形式化 vs. 纯 LLM 验证"的二元格局转向**选择性、成本感知的混合验证**。核心突破点在于 (a) 如何构建可靠的 triage 信号，(b) 如何设计中间表示使 autoformalization 更 tractable。Ganguly 等人验证了 selective verification 的可行性但局限于 FOL；HERMES 验证了 informal-formal interleaving 但不做选择性路由。本 proposal 恰好占据了"选择性 + 模块化中间表示"的空白位。

---

【发掘点 1】
- 维度: 前提假设质疑 / trivial alternative 威胁
- 内容: **"Confident-but-Wrong" 盲区是本 proposal 最大的未显式化风险。** 整个 pipeline 的有效性建立在一个关键假设上：BV 漏检的错误主要集中在 BV 不确定（高 uncertainty）的块上。但文献（2025-2026 多篇 calibration 研究）已充分证明 LLM 系统性过度自信——RL-trained 模型平均高估正确概率 20-60%。如果 BV 漏检的 50% 错误中有相当比例是 BV *高置信度判错*（即 confident-but-wrong），那么 uncertainty-guided routing 根本无法触达这些错误，整个 selective verification 的收益上界会急剧缩小。**Proposal 必须在 framing 中显式讨论这一风险**，并给出缓解策略——例如：(a) 分析 PF+BV 在 ArxivMathGradingBench 上的错误分布，区分"不确定且错误"vs"自信且错误"的比例；(b) 论证 PF 的模块化分解天然将"难以验证"的推理步骤隔离到独立块中，使这些块即使 BV 过度自信也会在 ensemble disagreement 中产生更高方差；(c) 引入 "structural difficulty" 信号（如块内推理步数、依赖的定理数量）作为 uncertainty 之外的补充路由信号。**不直面这个问题，审稿人大概率会在 rebuttal 阶段提出，且它可能是 fatal 的。**
- 价值: 直击 Novelty 和 Soundness 的核心：如果 triage 信号不可靠，selective verification 退化为随机采样 formal verification，novelty claim 崩塌。显式讨论并缓解此风险将极大增强 claim 的可信度。
- 调研依据: 基于 [LLMs are Overconfident (2025)](https://arxiv.org/pdf/2510.26995)、[Decoupling Reasoning and Confidence (2026)](https://arxiv.org/pdf/2603.09117) 关于 RL-trained LLM 过度自信的发现，以及 [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047) 中 token entropy 作为 uncertainty 信号在不同 domain 效果差异巨大（逻辑任务 +34.8% vs 事实任务 -44.5%）的发现。

【发掘点 2】
- 维度: novelty 锐化
- 内容: **PF 块作为 autoformalization 目标的结构性优势——这是本 proposal 最独特的 insight，但目前论述过于轻描淡写。** Proposal 中仅用 "far more amenable" "substantially higher" 等模糊措辞来声称 PF 块比 raw NL 更适合 autoformalization，但没有给出任何结构性分析来支撑这个 claim。应当显式拆解 PF 块与 Lean 4 theorem statement 之间的结构对齐：(a) PF 块有显式 typed premises → 直接对应 Lean 4 的 `hypothesis` 列表；(b) PF 块有单一 conclusion → 直接对应 Lean 4 的 `goal`；(c) PF 块无环境上下文依赖 → 消除了 whole-proof autoformalization 中最棘手的上下文补全问题。这种"PF 块 ≈ 半结构化定理声明"的论证如果做扎实，可以将 novelty 从"工程组合"提升为"modular proof decomposition 是 informal-formal verification 的天然桥梁"这一更具普适性的 insight。这也是与 HERMES 最本质的差异：HERMES 在生成时交替 informal/formal，而本 proposal 通过 PF 的模块化分解在验证时创建了结构化的 formalization 入口点。
- 价值: 将核心 novelty 从 "combination of existing techniques" 提升为 "architectural insight about modular decomposition as a bridge"，直接命中 Novelty 维度。如果审稿人认为这只是 engineering，中稿概率大幅下降；如果审稿人认为这揭示了一个 reusable insight，则显著提升。
- 调研依据: 基于 [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108) 揭示端到端 autoformalization 仅 36% 成功率的原因分析（上下文补全和 statement 歧义是主要瓶颈），以及 [StepFun-Formalizer (AAAI 2026)](https://arxiv.org/abs/2508.04440) 在 FormalMATH-Lite 上 40.5% BEq@1 的性能——PF 块的结构化输入有望显著缩小这两个瓶颈。

【发掘点 3】
- 维度: significance 提升 / 核心 claim 强化
- 内容: **PF 的 inter-block dependency graph 是一个被严重低估的信号源，应纳入路由策略以强化 significance。** 当前 proposal 仅用 uncertainty 作为路由信号，但 PF 提供了一个免费的附加结构：块间依赖图。一个 high-fan-out 块（被多个下游块依赖）如果验证错误，错误会级联传播到所有依赖块——这种块即使 BV 置信度较高，也值得投入 formal verification。将路由策略从纯 uncertainty-based 升级为 "uncertainty × dependency criticality" 的双信号策略，有三个好处：(a) 缓解发掘点 1 的 confident-but-wrong 问题（critical 块即使 BV 不 uncertain 也会被路由）；(b) 让 PF 的独特结构更深度地参与 pipeline 而不仅仅是 autoformalization 的输入格式，增强 "PF is the bridge" 的 narrative；(c) 与 cascade routing 文献（Unified Routing + Cascading, 2024）的理论框架对齐——将 dependency criticality 类比为 "cost of being wrong" 系数。
- 价值: 从 "single-signal routing" 升级为 "graph-aware multi-signal routing"，同时命中 Novelty（新的路由策略）和 Significance（利用了 PF 的独特结构属性，非其他方法可获得的信号）。
- 调研依据: 基于 [A Unified Approach to Routing and Cascading (2024)](https://arxiv.org/abs/2410.10347) 的 cascade routing 理论框架（routing 决策应考虑 cost of deferral），以及 PF 原文中 inter-block dependency graph 的定义。

【发掘点 4】
- 维度: related work 差异化
- 内容: **与 HERMES 的差异化必须从"功能对比"提升到"范式差异"。** 当前 proposal 对 HERMES 的区分停留在表层：HERMES 做 uniform formalization，本 proposal 做 selective formalization。但这掩盖了一个更根本的差异：HERMES 是一个 **proof generation** agent（生成新证明时交替 informal/formal），而本 proposal 是一个 **proof verification** pipeline（检查已有证明的正确性）。这两个任务的约束完全不同——generation 时你可以控制输出格式，verification 时你必须处理任意格式的输入证明。PF 的存在恰恰解决了 verification 场景下的核心困难：将任意格式的 NL 证明转化为可模块化处理的结构。此外，HERMES 的 80% FLOP 减少是相对于 reward-based 方法（如 Best-of-N），而本 proposal 的成本比较对象是 universal formal verification（Safe）——两者的 cost baseline 不同，不应直接比较。建议在 related work 中明确建立 "generation vs. verification" 的 taxonomy，将本 proposal 定位为 "the first uncertainty-guided selective formal verification system for NL proof checking"。
- 价值: 清晰的 taxonomy 防止审稿人将本工作与 HERMES 混为一谈（这是最可能的 novelty 质疑来源），直接命中 Related Work 差异化维度。
- 调研依据: 基于 [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760) 的实际定位（agent for proof generation with formal checking）与本 proposal 定位（pipeline for proof verification with selective formalization）的根本差异。

【发掘点 5】
- 维度: significance 提升
- 内容: **Framing 可以从 "cost-reliability optimization" 提升为更具普适意义的 insight："modular proof decomposition as a natural bridge between informal and formal verification."** 当前 proposal 的叙事是"我们找到了一个更好的 cost-reliability tradeoff"——这是一个 system-level 的贡献叙事，容易被审稿人归为 engineering paper。但如果核心叙事转变为"我们发现模块化证明分解（如 PF）天然地创建了从非形式到形式验证的桥梁，并通过实验验证了这一桥梁的有效性"，则贡献从 system optimization 升级为 architectural insight：不仅对本 pipeline 有效，对未来任何需要混合 informal/formal 验证的系统都有指导意义。这个 reframing 不需要改变任何技术方案，只需要调整叙事重心。
- 价值: 将论文从"又一个 pipeline 优化"提升为"提出了一个 reusable architectural principle"，显著命中 Significance 维度。AAAI 审稿人更看重 insight 的普适性。
- 调研依据: 基于领域整体趋势判断——当前 verification 文献（Safe, HERMES, VERGE, ProofSketcher）都在探索 informal-formal 的混合策略，但没有任何一篇工作明确提出"modular decomposition is the bridge"这一 architectural claim。

Sources:
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)
- [Safe: Step-aware Formal Verification (ACL 2025)](https://aclanthology.org/2025.acl-long.594/)
- [HERMES: Efficient and Verifiable Mathematical Reasoning (ICML 2026)](https://arxiv.org/abs/2511.18760)
- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)
- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)
- [StepFun-Formalizer-32B (AAAI 2026)](https://arxiv.org/abs/2508.04440)
- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)
- [VERGE: Formal Refinement and Guidance Engine (arXiv 2026)](https://arxiv.org/abs/2601.20055)
- [A Unified Approach to Routing and Cascading for LLMs](https://arxiv.org/abs/2410.10347)
- [ProofSketcher (arXiv 2026)](https://arxiv.org/abs/2604.06401)
- [LLMs are Overconfident (2025)](https://arxiv.org/pdf/2510.26995)
- [Decoupling Reasoning and Confidence (2026)](https://arxiv.org/pdf/2603.09117)

【补救 agent 本轮输出】:
Now I have comprehensive research context. Let me compile my thorough analysis of the experimental design.

【状态】: 有缺陷待补救

【前置调研发现】
- [Pseudo-Formalization for Automatic Proof Verification, arXiv 2605.20531](https://arxiv.org/abs/2605.20531) (arXiv 2026): 评估于 Hard2Verify 和 ArxivMathGradingBench（仅 35 篇论文、40 个已知错误）。用 error-finding precision 和 recall 作为核心指标。PF+BV Pareto 优于 LLM-as-judge baseline。
- [Safe: Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/) (ACL 2025): 提出 FormalStep 基准（30,809 条 formal statements），在多个数学推理数据集上评估。验证成功率约 80%。开源代码和数据。
- [HERMES](https://arxiv.org/abs/2511.18760) (ICML 2026): 在 4 个数学推理基准上评测，对比 base model。展示了 token usage 大幅减少。报告了 accuracy 提升和 FLOPs 减少。
- [Grammars of Formal Uncertainty, Ganguly et al.](https://arxiv.org/abs/2505.20047) (NeurIPS 2025): PCFG 框架建模 LLM 输出的不确定性。Grammar entropy 在逻辑任务上 AUROC>0.93。SMT autoformalization 对准确率影响是 domain-specific 的（逻辑任务 +34.8%，事实任务 -44.5%）。评估了 5 个 frontier LLM。
- [miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108) (NeurIPS 2025): 端到端 autoformalization pipeline 成功率约 36%（原 miniF2F）。LLM 判定的 autoformalization 准确率 97% 被人工审核修正为 66%。提出 miniF2F-v2 后最佳准确率提升至 70%。
- [Goedel-Prover-V2](https://arxiv.org/pdf/2508.03613) (ICLR 2026): Lean 4 proof search SOTA。HILBERT 在 miniF2F 上达到 99.2%。支持 self-correction。
- [StepFun-Formalizer-32B](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B) (2025): NL-to-Lean4 autoformalization。type-check rate 在不同 benchmark 上从 4%–57.2% 不等。BEq+ 准确率约 30%。
- [ThinkPRM / Process Reward Models](https://arxiv.org/pdf/2504.16828) (2025-2026): ThinkPRM 是当前 data-efficient PRM SOTA。Qwen2.5-Math-PRM 系列是主流 baseline。在 ProcessBench 上评测。
- [DiscoUQ](https://arxiv.org/pdf/2603.20975) (2026): LLM ensemble 不确定性量化框架，利用 inter-agent disagreement 结构信息，AUROC 0.802，优于 baseline。
- 调研总结: 该领域当前实验标准要求 (1) 在 error detection 任务上报告 precision/recall 及其 tradeoff，(2) 对 cost 进行严格归一化对比（per-step 或 per-proof），(3) ablation 需隔离各不确定性信号的贡献，(4) autoformalization 准确率需人工或 formal verification 验证（不可仅依赖 LLM judge），(5) 统计显著性分析在小数据集上尤为重要。审稿人通常会要求 Pareto 曲线展示 cost-accuracy tradeoff 以及 failure case 分析。

---

【缺陷 1】
- 类别: 评估方案缺陷
- 问题: ArxivMathGradingBench 仅含 35 篇论文、40 个已知错误，作为核心评估基准统计功效严重不足。在如此小的样本上报告 error detection recall 的差异（例如从 50% 提升到 70%）对应的仅是 20→28 个 error 的变化，置信区间极宽。更严重的是，proposal 要求从这 40 个标注中还要分出 held-out set 做 isotonic regression 校准——校准集可能仅有 10-15 个正例，isotonic regression 在这种规模上极易过拟合，校准结果不可靠。审稿人几乎必然会质疑这些结果的统计显著性。
- 严重度: 可补救
- 补救方案: 
  (a) 报告 bootstrap confidence intervals（至少 1000 次 resample）和 McNemar's test 或 paired permutation test 来量化与 baseline 差异的统计显著性。
  (b) 补充一个合成评估集：对 Hard2Verify 中的 competition-level 问题，利用已知正确解（ground truth）和已知错误解（LLM 生成的错误 proof）构建更大规模的 error detection 评估集（目标 200+ 错误实例）。这在 PF 原文中已有 Hard2Verify 的实验数据可参考。
  (c) 对 isotonic regression 校准采用 leave-one-out cross-validation 而非简单 train/test split，或者改用 Platt scaling（参数更少，更适合小数据）。
  (d) 考虑在 FormalProofBench（graduate-level proofs, 2026）上做额外评估，以增加 research-level 评估的覆盖度。
- 调研依据: ArxivMathGradingBench 的规模来自 [Barkallah et al., 2026] 原文；Ganguly et al. (NeurIPS 2025) 在其 selective verification 实验中评估了 5 个 LLM 在多个 domain 上的表现以获得足够统计功效。

【缺陷 2】
- 类别: 实验设计不足
- 问题: miniF2F 被列为评估基准之一（"end-to-end correctness"），但 miniF2F 是一个 theorem proving benchmark，不是 proof verification benchmark。本 proposal 的核心任务是验证给定 proof 的正确性，而非生成新 proof。Proposal 未说明如何将 miniF2F 适配为 verification 评测：(a) 验证对象是什么？是 LLM 生成的解？是已知正确解？还是 mix？(b) 如何构造 negative examples（错误 proof）？(c) 评测指标是什么——verification accuracy 还是 error detection recall/precision？如果不厘清这一点，审稿人会认为 miniF2F 实验缺乏说服力。
- 严重度: 可补救
- 补救方案:
  (a) 明确 miniF2F 的评测协议：推荐方案是用 SOTA reasoning LLM（如 QwQ-32B）为 miniF2F 的 488 个问题生成 N 个 candidate proofs（混合正确和错误），然后用本系统进行 verification，以 verification precision/recall 作为指标。
  (b) 或者改为使用 miniF2F-v2（NeurIPS 2025 的修正版）验证 autoformalization pipeline 本身的质量——即 PF block autoformalization 在 miniF2F-v2 的 formal statements 上的 type-check rate 和语义正确率，作为组件级评估。
  (c) 无论哪种方案，都需要与 Safe 在同一 miniF2F 实验设定下比较，保证对照公平。
- 调研依据: [miniF2F-Lean Revisited, NeurIPS 2025] 明确指出 miniF2F 是 theorem proving 基准；Safe (ACL 2025) 的 miniF2F 实验是验证 LLM 生成的解的正确性，本 proposal 需与其对齐。

【缺陷 3】
- 类别: baseline 不足或过时
- 问题: PRM baseline 未指定具体模型。2025-2026 年 PRM 领域发展迅速，当前 SOTA 包括 ThinkPRM（verbalized process reward，NeurIPS 2025 area）、Qwen2.5-Math-PRM-72B、以及 formally-verified PRM（Generalizable PRMs via Formally Verified Training Data, 2025）。仅说"PRM baselines"过于模糊，审稿人会要求指定具体模型并解释选择理由。此外，proposal 未将 ThinkPRM 作为 baseline 纳入，而 ThinkPRM 作为 verbalized step-level verifier 与本 proposal 的 LLM-based Block Verification 直接可比。
- 严重度: 可补救
- 补救方案:
  (a) 明确纳入至少两个 PRM baseline：Qwen2.5-Math-PRM-72B（当前最强开源 PRM）和 ThinkPRM（data-efficient verbalized PRM，与 BV 的 CoT verification 最直接可比）。
  (b) 在 error detection 任务上用相同 evaluation protocol 对比这些 PRM：给定 proof step/block，PRM 的 step-level score 作为 error detection signal，report precision/recall。
  (c) 如果 compute 不允许 72B PRM，至少用 Qwen2.5-Math-PRM-7B + ThinkPRM-7B 作为可行替代，并注明参数量差异。
- 调研依据: [ThinkPRM, 2025]、[Qwen2.5-Math-PRM, 2025]、[Generalizable PRMs via Formally Verified Training Data, 2025] 是当前 PRM 领域的核心 baseline。

【缺陷 4】
- 类别: ablation 不完整
- 问题: Proposal 提到 ablation "on threshold selection, uncertainty calibration method, and the autoformalization advantage of PF blocks over raw NL"，但缺少两个关键 ablation：
  (1) 两个不确定性信号（ensemble disagreement vs. CoT entropy）的独立贡献。当前设计将二者融合后做 isotonic regression 校准，但未计划分别评估它们的 error detection AUROC。如果其中一个信号贡献极小，融合反而可能引入噪声。Ganguly et al. (NeurIPS 2025) 明确证明不确定性信号是 task-dependent 的，本 proposal 需要验证在 math proof verification 这一特定任务上哪些信号最有效。
  (2) Autoformalization failure 的处理策略 ablation。当 StepFun-Formalizer 无法成功 autoformalize 或 Goedel-Prover-V2 proof search 超时（proposal 估计 2-5 min/block），系统的 fallback 策略是什么？Accept the block？Reject it？Report "uncertain"？不同 fallback 策略对 end-to-end recall/precision 影响很大，必须做 ablation。
- 严重度: 可补救
- 补救方案:
  (a) 新增 ablation 表格：ensemble disagreement only / CoT entropy only / combined 三种配置的 AUROC、ECE（Expected Calibration Error）、和 error detection recall@fixed-cost 对比。
  (b) 新增 autoformalization failure handling ablation：fallback-accept（乐观） / fallback-reject（保守） / fallback-to-majority-vote（再做一轮 ensemble BV）三种策略的 precision/recall tradeoff。
  (c) 报告 Goedel-Prover-V2 proof search 在 PF block 粒度上的 success rate 和 timeout rate，以量化 formal verification tier 的 coverage。
- 调研依据: Ganguly et al. (NeurIPS 2025) 展示了不同 uncertainty signal 在不同 task 上效果差异巨大（AUROC 变化范围超过 0.3）；DiscoUQ (2026) 证明 ensemble disagreement 结构信息比简单投票更有效。

【缺陷 5】
- 类别: compute 公平性问题
- 问题: Cost comparison 存在两个不透明之处：
  (1) LLM verification tier 的 ensemble 成本未计入总成本：N=5 stochastic forward passes 意味着 Block Verification 阶段本身已是 single-pass BV 的 5 倍成本。Proposal 声称总成本为 Safe 的 1.5-2x，但这个估算是否已包含 5x 的 ensemble 开销？如果 PF+BV single-pass 是 1x，ensemble BV 已是 5x，再加上 10-20% blocks 的 autoformalization + proof search，总成本可能远超 2x。
  (2) 与 Safe 的成本对比缺少统一度量单位：Safe 的"4-8x cost overhead"是相对于什么 baseline？是相对于 no verification（直接接受 LLM 解答）？还是相对于 single-pass BV？Proposal 需要定义统一的 cost unit（如 GPU-seconds per proof, FLOPs per proof, 或 API cost per proof），并在这个统一单位下对比所有方法。
- 严重度: 可补救
- 补救方案:
  (a) 定义统一的 cost metric：推荐用 GPU-seconds per proof（或 per 1000 tokens of proof text）作为 cost unit，涵盖所有计算环节。
  (b) 构建详细 cost breakdown table：PF decomposition cost + ensemble BV cost (5 × single BV) + routing overhead + autoformalization cost (per routed block) + proof search cost (per routed block, including timeout cases) = total cost。
  (c) 绘制 cost-accuracy Pareto 曲线：横轴为 normalized cost（relative to single-pass BV），纵轴为 error detection recall（或 F1）。在这条曲线上标注所有对比方法（PF+BV single-pass, PF+BV ensemble, proposed selective, Safe universal, PRM baselines）。这种 Pareto 分析是该领域审稿人的标准期望。
  (d) 考虑 ensemble size 的 ablation：N=3 vs. N=5 vs. N=7，验证 N=5 是否是 cost-quality sweet spot。
- 调研依据: Safe (ACL 2025) 报告的 4-8x 是 per-step overhead vs. no formal verification；Qu (arXiv 2026) 的 adaptive verification 工作明确以 verifier call 次数作为 cost metric 并提供 Pareto 分析。

【缺陷 6】
- 类别: 实验设计不足
- 问题: "PF blocks 比 raw NL 更易 autoformalize"是本 proposal 的核心假设之一（"a key insight is that PF blocks' self-contained structure makes them far more amenable to reliable autoformalization than raw natural language text"），但 ablation 设计缺乏具体对照实验方案。这个 claim 需要一个严格的 controlled comparison 来量化 PF block format 带来的 autoformalization quality gain。目前只说"ablation on the autoformalization advantage of PF blocks over raw NL"，但未回答关键设计问题：(a) 什么是"raw NL"对照组？是整段 proof text 还是按句切分的 proof step？(b) 用什么指标衡量 autoformalization 质量？type-check rate？BEq 语义匹配？人工评估？(c) 如何控制变量——同一 proof 的 PF block 与对应的 NL fragment 必须 align 才能比较。
- 严重度: 可补救
- 补救方案:
  (a) 设计 paired comparison 实验：对同一组 proof，一组输入为 PF block（包含 explicit premises/conclusion），另一组输入为对应的 raw NL proof fragment（从原始 proof 中提取相同推理步骤但不含 PF 结构标注）。两组都用 StepFun-Formalizer-32B autoformalize to Lean 4。
  (b) 评估指标至少三个：(i) Lean 4 type-check rate（语法正确性），(ii) Lean 4 proof search success rate via Goedel-Prover-V2（语义正确性），(iii) 如果 sample size 足够，做人工评估 sample check（参考 miniF2F-Lean Revisited 的教训：LLM-judged autoformalization 准确率从 97% 降到 66%）。
  (c) 报告 paired t-test 或 Wilcoxon signed-rank test 的 p-value。
- 调研依据: [miniF2F-Lean Revisited, NeurIPS 2025] 明确警告 autoformalization 质量不能仅用 LLM judge 评估；[StepFun-Formalizer, 2025] 报告 type-check rate 在不同 benchmark 上变化极大（4%–57%），说明 input format 对 autoformalization 质量影响很大，支持做 controlled comparison。

【缺陷 7】
- 类别: 可行性问题
- 问题: Proposal 的 resource estimate 看似合理（300-400 GPU hours on A100-80GB），但有一个潜在瓶颈未被充分讨论：Lean 4 proof search 是 CPU-bound 且 sequential（proposal 自己承认"2-5 min per block"）。如果 10-20% 的 blocks 被路由到 formal verification，一个中等长度的 research paper proof 可能有 20-50 个 PF blocks，其中 2-10 个需要 formal verification，每个 2-5 min，单个 proof 的 formal verification 就需要 4-50 min。在 ArxivMathGradingBench 的 35 篇论文（每篇可能有多个 proof）上，加上 ablation 和多种配置的重复实验，Lean 4 proof search 时间可能成为真正的瓶颈。此外，Goedel-Prover-V2-32B 需要 GPU 推理来生成 proof candidate，再用 Lean kernel CPU-check，这是 GPU+CPU 混合负载，需要合理调度。
- 严重度: 可补救
- 补救方案:
  (a) 明确 Lean 4 proof search 的 timeout 策略（建议 per-block timeout 5 min，total per-proof timeout 30 min）。
  (b) 估算 formal verification tier 的总 wall-clock time：假设 35 篇 × 平均 30 blocks/paper × 15% routing rate × 3.5 min/block = ~550 min ≈ 9h for one pass。加上 ablation 配置（~5 种 × 9h = 45h wall-clock），这在 timeline 内是可行的但 tight。
  (c) 在 resource estimate 中分开列出 GPU hours（Goedel-Prover-V2 推理）和 CPU hours（Lean kernel type-checking），避免混淆。
  (d) 对于 miniF2F 的更大规模评估，可以利用 independent blocks 之间的并行性来加速（非 dependent blocks 可并行 proof search）。
- 调研依据: HERMES (ICML 2026) 报告了 80% fewer FLOPs，但其 Lean 4 interaction overhead 仍显著；Goedel-Prover-V2 (ICLR 2026) 的 self-correction loop 意味着每个 block 可能需要多轮 proof search。

Sources:
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)
- [Safe: Enhancing Mathematical Reasoning via Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/)
- [HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs](https://arxiv.org/abs/2511.18760)
- [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047)
- [miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108)
- [Goedel-Prover-V2](https://arxiv.org/pdf/2508.03613)
- [StepFun-Formalizer-32B](https://huggingface.co/stepfun-ai/StepFun-Formalizer-32B)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/pdf/2504.16828)
- [DiscoUQ: Structured Disagreement Analysis](https://arxiv.org/pdf/2603.20975)
- [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/html/2605.18796)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53d9df8e-2615-4f5d-b5c7-fe0bc19c2d8a",
  "isSidechain": false,
  "promptId": "fd745b34-b853-4af8-8c77-3ea58bb1436a",
  "type": "user",
  "uuid": "6f1d17e4-c1be-48a4-bd41-f05bb7bdf688",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
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
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research context. Let me synthesize my assessment.  ---  【状态】: 有发掘空间  【前置调研发现】 - [Pseudo-…",
  "leafUuid": "6f1d17e4-c1be-48a4-bd41-f05bb7bdf688",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Assistant

_source line 17 · 2026-05-27T12:44:33.075Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze both worker outputs and plan my cross-validation searches before producing the integrated output.

**Summary of worker outputs:**

**发掘 agent (5 points):**
1. "Confident-but-Wrong" blind spot - LLMs are systematically overconfident, so uncertainty-guided routing may miss high-confidence errors
2. PF blocks as autoformalization targets need stronger structural analysis (PF block ≈ semi-structured theorem statement)
3. Dependency graph as additional routing signal (uncertainty × dependency criticality)
4. HERMES differentiation should be "generation vs. verification" paradigm difference


5. The core framing should shift from optimizing cost-reliability tradeoffs to viewing modular decomposition as the actual bridge connecting informal and formal verification

**补救 agent (7 defects):**
1. ArxivMathGradingBench too small (35 papers, 40 errors) - statistical power insufficient
2. miniF2F is theorem proving benchmark, not verification benchmark - need adaptation protocol
3. PRM baselines unspecified - need ThinkPRM, Qwen2.5-Math-PRM
4. Ablation incomplete - need individual uncertainty signal contributions + autoformalization failure handling
5. Cost comparison unfair - ensemble 5x cost not accounted, no unified cost metric
6. PF vs raw NL autoformalization claim needs controlled experiment design
7. Lean 4 proof search bottleneck - CPU-bound sequential, need timeout strategy

Now I need to verify several key claims through cross-validation searches. First, I should check whether ensemble disagreement combined with CoT entropy is actually more robust against LLM overconfidence than single-model confidence alone. Then I'll search for existing work on graph-aware verification routing to see if the dependency graph approach is truly novel. I also need to confirm that ThinkPRM is currently considered a standard baseline for step-level verification, and finally verify Safe's cost multiplier claims and what exactly they're comparing against.

I'll run three targeted searches to validate these critical points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f1d17e4-c1be-48a4-bd41-f05bb7bdf688",
  "isSidechain": false,
  "requestId": "req_011CbT6S2PxS7bdh3FdnuVtA",
  "type": "assistant",
  "uuid": "993a6f2a-9efa-4d4a-a149-4544be86ea38",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YtvvY771x9C22t2E3oXVN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12165,
      "cache_read_input_tokens": 20084,
      "output_tokens": 687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 687,
          "cache_read_input_tokens": 20084,
          "cache_creation_input_tokens": 12165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12165
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

_source line 18 · 2026-05-27T12:44:33.079Z_

我需要先对两位 worker 的关键建议做交叉验证调研，然后再整合。让我启动 3 个针对性搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "993a6f2a-9efa-4d4a-a149-4544be86ea38",
  "isSidechain": false,
  "requestId": "req_011CbT6S2PxS7bdh3FdnuVtA",
  "type": "assistant",
  "uuid": "e6e5632b-391a-4095-a700-a2cee1db8a88",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YtvvY771x9C22t2E3oXVN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12165,
      "cache_read_input_tokens": 20084,
      "output_tokens": 687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 687,
          "cache_read_input_tokens": 20084,
          "cache_creation_input_tokens": 12165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12165
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

_source line 19 · 2026-05-27T12:44:33.190Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nbs3xU1PrDpAnsRFjxQQLX`</summary>

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
  "parentUuid": "e6e5632b-391a-4095-a700-a2cee1db8a88",
  "isSidechain": false,
  "requestId": "req_011CbT6S2PxS7bdh3FdnuVtA",
  "type": "assistant",
  "uuid": "defc88ae-a492-45ee-bd27-e02a0b7406e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013YtvvY771x9C22t2E3oXVN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12165,
      "cache_read_input_tokens": 20084,
      "output_tokens": 687,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 687,
          "cache_read_input_tokens": 20084,
          "cache_creation_input_tokens": 12165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12165
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

_source line 20 · 2026-05-27T12:44:33.197Z_

<details><summary>↩ Tool result · `toolu_01Nbs3xU1PrDpAnsRFjxQQLX`</summary>

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
  "parentUuid": "defc88ae-a492-45ee-bd27-e02a0b7406e3",
  "isSidechain": false,
  "promptId": "fd745b34-b853-4af8-8c77-3ea58bb1436a",
  "type": "user",
  "uuid": "719827da-0ffd-4d8c-9031-c0e5164cdcef",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "defc88ae-a492-45ee-bd27-e02a0b7406e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T12:44:37.159Z_

现在启动 3 个并行的交叉验证搜索：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "719827da-0ffd-4d8c-9031-c0e5164cdcef",
  "isSidechain": false,
  "requestId": "req_011CbT6TMXvCZZRpF4n2bxg8",
  "type": "assistant",
  "uuid": "c5012dfb-cc76-41d3-bca4-bb5696ffc994",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6C62fgq7fGBAx4tEpQkGp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1215,
      "cache_read_input_tokens": 32249,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1215,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 32249,
          "cache_creation_input_tokens": 1215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1215
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

_source line 22 · 2026-05-27T12:44:38.099Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01353997DV9PShaRUhFjoGzL`</summary>

```json
{
  "query": "ensemble disagreement uncertainty LLM overconfidence calibration 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c5012dfb-cc76-41d3-bca4-bb5696ffc994",
  "isSidechain": false,
  "requestId": "req_011CbT6TMXvCZZRpF4n2bxg8",
  "type": "assistant",
  "uuid": "4c80298a-2a88-4da4-9c4d-cd34d95771fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6C62fgq7fGBAx4tEpQkGp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1215,
      "cache_read_input_tokens": 32249,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1215,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 32249,
          "cache_creation_input_tokens": 1215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1215
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

_source line 23 · 2026-05-27T12:44:38.570Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RXa4ofbtkVuZYgkVxkeq61`</summary>

```json
{
  "query": "ThinkPRM process reward model step-level verification baseline 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4c80298a-2a88-4da4-9c4d-cd34d95771fa",
  "isSidechain": false,
  "requestId": "req_011CbT6TMXvCZZRpF4n2bxg8",
  "type": "assistant",
  "uuid": "ba9d3b30-a0ca-4781-8534-02d405d2f143",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6C62fgq7fGBAx4tEpQkGp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1215,
      "cache_read_input_tokens": 32249,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1215,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 32249,
          "cache_creation_input_tokens": 1215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1215
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

_source line 24 · 2026-05-27T12:44:38.832Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CMUuJxNXRUY2DoPHgrsst5`</summary>

```json
{
  "query": "graph-aware verification routing dependency-critical formal verification mathematical proof 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ba9d3b30-a0ca-4781-8534-02d405d2f143",
  "isSidechain": false,
  "requestId": "req_011CbT6TMXvCZZRpF4n2bxg8",
  "type": "assistant",
  "uuid": "24459e42-6f2d-40ec-9064-07fd9b050542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6C62fgq7fGBAx4tEpQkGp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1215,
      "cache_read_input_tokens": 32249,
      "output_tokens": 195,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1215,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 195,
          "cache_read_input_tokens": 32249,
          "cache_creation_input_tokens": 1215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1215
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

_source line 25 · 2026-05-27T12:44:45.866Z_

<details><summary>↩ Tool result · `toolu_01RXa4ofbtkVuZYgkVxkeq61`</summary>

```text
Web search results for query: "ThinkPRM process reward model step-level verification baseline 2025 2026"

Links: [{"title":"Process Reward Models That Think | OpenReview","url":"https://openreview.net/forum?id=V727xqBYIW"},{"title":"[2504.16828] Process Reward Models That Think","url":"https://arxiv.org/abs/2504.16828"},{"title":"Process Reward Models That Think | alphaXiv","url":"https://www.alphaxiv.org/overview/2504.16828v5"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Paper page - Process Reward Models That Think","url":"https://huggingface.co/papers/2504.16828"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost","url":"https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"},{"title":"GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub","url":"https://github.com/RyanLiu112/Awesome-Process-Reward-Models"}]

I found comprehensive information about ThinkPRM. Here's what the search results show:

## Overview

ThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. It aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT).

## Step-Level Verification Approach

The work builds data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). This generative approach differs from traditional discriminative PRMs.

## Performance vs. Baselines

ThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. In an out-of-domain evaluation on a subset of GPQA-Diamond and LiveCodeBench, the PRM surpasses discriminative verifiers trained on the full PRM800K by 8% and 4.5%, respectively. Under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench.

## Key Advantage

The approach outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba9d3b30-a0ca-4781-8534-02d405d2f143",
  "isSidechain": false,
  "promptId": "fd745b34-b853-4af8-8c77-3ea58bb1436a",
  "type": "user",
  "uuid": "a58918c2-b63a-45bc-bd34-34cb49d82e9e",
  "toolUseResult": {
    "query": "ThinkPRM process reward model step-level verification baseline 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Hw5PL1fgtxTjwFTyZvuPL",
        "content": [
          {
            "title": "Process Reward Models That Think | OpenReview",
            "url": "https://openreview.net/forum?id=V727xqBYIW"
          },
          {
            "title": "[2504.16828] Process Reward Models That Think",
            "url": "https://arxiv.org/abs/2504.16828"
          },
          {
            "title": "Process Reward Models That Think | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2504.16828v5"
          },
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          },
          {
            "title": "Paper page - Process Reward Models That Think",
            "url": "https://huggingface.co/papers/2504.16828"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "ThinkPRM: A Generative Process Reward Models for Scalable Reasoning Verification - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/04/29/thinkprm-a-generative-process-reward-models-for-scalable-reasoning-verification/"
          },
          {
            "title": "GitHub - RyanLiu112/Awesome-Process-Reward-Models: A comprehensive collection of process reward models. · GitHub",
            "url": "https://github.com/RyanLiu112/Awesome-Process-Reward-Models"
          }
        ]
      },
      "I found comprehensive information about ThinkPRM. Here's what the search results show:\n\n## Overview\n\nThinkPRM is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than those required by discriminative PRMs. It aims to build data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT).\n\n## Step-Level Verification Approach\n\nThe work builds data-efficient PRMs as verbalized step-wise reward models that verify every step in the solution by generating a verification chain-of-thought (CoT). This generative approach differs from traditional discriminative PRMs.\n\n## Performance vs. Baselines\n\nThinkPRM beats the baselines on ProcessBench, MATH-500, and AIME '24 under best-of-N selection and reward-guided search. In an out-of-domain evaluation on a subset of GPQA-Diamond and LiveCodeBench, the PRM surpasses discriminative verifiers trained on the full PRM800K by 8% and 4.5%, respectively. Under the same token budget, ThinkPRM scales up verification compute more effectively compared to LLM-as-a-Judge, outperforming it by 7.2% on a subset of ProcessBench.\n\n## Key Advantage\n\nThe approach outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of the process labels in PRM800K across several challenging benchmarks."
    ],
    "durationSeconds": 7.291744079,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ba9d3b30-a0ca-4781-8534-02d405d2f143",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T12:44:45.958Z_

<details><summary>↩ Tool result · `toolu_01353997DV9PShaRUhFjoGzL`</summary>

```text
Web search results for query: "ensemble disagreement uncertainty LLM overconfidence calibration 2025 2026"

Links: [{"title":"LLM Calibration and Uncertainty Quantification in Production AI Agents | Zylos Research","url":"https://zylos.ai/research/2026-04-18-llm-calibration-uncertainty-production-agents"},{"title":"LLMs are Overconfident: Evaluating Confidence Interval Calibration with FermiEval","url":"https://arxiv.org/pdf/2510.26995"},{"title":"When Two LLMs Debate, Both Think They'll Win","url":"https://arxiv.org/pdf/2505.19184"},{"title":"Mitigating Automation Bias in Physician-LLM Diagnostic Reasoning Using Behavioral Nudges","url":"https://cdn.clinicaltrials.gov/large-docs/15/NCT07328815/Prot_SAP_000.pdf"},{"title":"Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11648734/"},{"title":"Aligning LLM Uncertainty with Human Disagreement in Subjectivity Analysis","url":"https://arxiv.org/html/2605.10415"},{"title":"A better method for identifying overconfident large language models - MIT Schwarzman College of Computing","url":"https://computing.mit.edu/news/a-better-method-for-identifying-overconfident-large-language-models/"},{"title":"Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers","url":"https://arxiv.org/pdf/2602.07842"}]

Based on the web search results, here's what recent research reveals about ensemble disagreement, uncertainty quantification, and LLM calibration in 2025-2026:

## LLM Overconfidence and Calibration Challenges

Large language models excel at numerical estimation but struggle to correctly quantify uncertainty, with research showing they are systematically overconfident. Across several modern models, nominal 99% confidence intervals cover the true answer only 65% of the time on average.

## Training-Based Calibration Solutions

Recent research examines the state of the art in LLM calibration through early 2026, covering mechanisms behind overconfidence and uncertainty quantification methods. The ICML 2025 paper introduces CFT (Calibration-Aware Fine-Tuning) as a modification of the fine-tuning objective that preserves calibration properties while optimizing for helpfulness, dramatically reducing Expected Calibration Error while maintaining or improving accuracy.

## Ensemble Disagreement as Uncertainty Signal

Researchers developed a method involving measuring divergence between a target model and a small ensemble of models, finding that measuring cross-model disagreement more accurately captures uncertainty than traditional approaches. Rather than relying on single-model self-assessment, some approaches estimate confidence via an ensemble of three distinct LLMs, shifting confidence estimation away from unreliable internal self-reports toward practical uncertainty quantification by aggregating judgments from multiple models.

## Alignment and Confidence Dynamics

Recent findings suggest LLMs lack the ability to accurately self-assess or update their beliefs in dynamic, multi-turn tasks, highlighting challenges for deployment in assistant and agentic settings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c80298a-2a88-4da4-9c4d-cd34d95771fa",
  "isSidechain": false,
  "promptId": "fd745b34-b853-4af8-8c77-3ea58bb1436a",
  "type": "user",
  "uuid": "df841590-0b3d-45a2-91bb-3e93a57693b7",
  "toolUseResult": {
    "query": "ensemble disagreement uncertainty LLM overconfidence calibration 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015nFgXekXVcuMSNS7A7aZGy",
        "content": [
          {
            "title": "LLM Calibration and Uncertainty Quantification in Production AI Agents | Zylos Research",
            "url": "https://zylos.ai/research/2026-04-18-llm-calibration-uncertainty-production-agents"
          },
          {
            "title": "LLMs are Overconfident: Evaluating Confidence Interval Calibration with FermiEval",
            "url": "https://arxiv.org/pdf/2510.26995"
          },
          {
            "title": "When Two LLMs Debate, Both Think They'll Win",
            "url": "https://arxiv.org/pdf/2505.19184"
          },
          {
            "title": "Mitigating Automation Bias in Physician-LLM Diagnostic Reasoning Using Behavioral Nudges",
            "url": "https://cdn.clinicaltrials.gov/large-docs/15/NCT07328815/Prot_SAP_000.pdf"
          },
          {
            "title": "Large language model uncertainty proxies: discrimination and calibration for medical diagnosis and treatment - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11648734/"
          },
          {
            "title": "Aligning LLM Uncertainty with Human Disagreement in Subjectivity Analysis",
            "url": "https://arxiv.org/html/2605.10415"
          },
          {
            "title": "A better method for identifying overconfident large language models - MIT Schwarzman College of Computing",
            "url": "https://computing.mit.edu/news/a-better-method-for-identifying-overconfident-large-language-models/"
          },
          {
            "title": "Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers",
            "url": "https://arxiv.org/pdf/2602.07842"
          }
        ]
      },
      "Based on the web search results, here's what recent research reveals about ensemble disagreement, uncertainty quantification, and LLM calibration in 2025-2026:\n\n## LLM Overconfidence and Calibration Challenges\n\nLarge language models excel at numerical estimation but struggle to correctly quantify uncertainty, with research showing they are systematically overconfident. Across several modern models, nominal 99% confidence intervals cover the true answer only 65% of the time on average.\n\n## Training-Based Calibration Solutions\n\nRecent research examines the state of the art in LLM calibration through early 2026, covering mechanisms behind overconfidence and uncertainty quantification methods. The ICML 2025 paper introduces CFT (Calibration-Aware Fine-Tuning) as a modification of the fine-tuning objective that preserves calibration properties while optimizing for helpfulness, dramatically reducing Expected Calibration Error while maintaining or improving accuracy.\n\n## Ensemble Disagreement as Uncertainty Signal\n\nResearchers developed a method involving measuring divergence between a target model and a small ensemble of models, finding that measuring cross-model disagreement more accurately captures uncertainty than traditional approaches. Rather than relying on single-model self-assessment, some approaches estimate confidence via an ensemble of three distinct LLMs, shifting confidence estimation away from unreliable internal self-reports toward practical uncertainty quantification by aggregating judgments from multiple models.\n\n## Alignment and Confidence Dynamics\n\nRecent findings suggest LLMs lack the ability to accurately self-assess or update their beliefs in dynamic, multi-turn tasks, highlighting challenges for deployment in assistant and agentic settings."
    ],
    "durationSeconds": 7.8549509429999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4c80298a-2a88-4da4-9c4d-cd34d95771fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T12:44:46.737Z_

<details><summary>↩ Tool result · `toolu_01CMUuJxNXRUY2DoPHgrsst5`</summary>

```text
Web search results for query: "graph-aware verification routing dependency-critical formal verification mathematical proof 2025 2026"

Links: [{"title":"Parallel Verification of Natural Deduction Proof Graphs","url":"https://arxiv.org/pdf/2311.10440"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"},{"title":"Formal Verification of Routing Protocols for Wireless Ad Hoc Networks","url":"https://www.eurecom.fr/en/publication/2657/download/cm-publi-2657.pdf"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/pdf/2506.12509"},{"title":"Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM","url":"https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"},{"title":"Automatic verification of dependency","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8555226"},{"title":"ConnChecker: Automated Root-Cause Analysis for Formal Connectivity Check via Graph","url":"https://arxiv.org/pdf/2603.07943"}]

I've performed the web search for your query. Here are the relevant results found:

## Key Results:

1. **Parallel Verification of Natural Deduction Proof Graphs** - Graph-based interactive theorem provers offer a visual representation of proofs, explicitly representing the dependencies and inferences between proof steps in a graph or hypergraph format. The work presents parallel algorithms for formal verification of graph-based natural deduction style proofs.

2. **ProofFlow: A Dependency Graph Approach** (2025) - This work presents a benchmark of 184 undergraduate-level problems manually annotated with step-by-step solutions and logical dependency graphs. The approach focuses on faithful proof autoformalization with structured dependency handling.

3. **Graph of Verification (GoV)** - This mechanism allows GoV to adaptively adjust its verification granularity—from atomic steps for formal tasks to entire paragraphs for natural language—to match the native structure of the reasoning process.

4. **ConnChecker** - A graph-based framework designed to accelerate root-cause analysis in formal connectivity verification that processes counterexample reports along with functional and structural dependency graphs.

5. **Broader Context (2025-2026)** - Developments in formal reasoning have immediate applications in formal verification of safety-critical systems, with AI potentially automating formalization and proof efforts to make complex systems more robust.

The search results show active research in graph-aware verification approaches with dependency tracking and formal verification methods in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24459e42-6f2d-40ec-9064-07fd9b050542",
  "isSidechain": false,
  "promptId": "fd745b34-b853-4af8-8c77-3ea58bb1436a",
  "type": "user",
  "uuid": "1ae67e5f-3872-4eb0-b4dd-d2fbb1695441",
  "toolUseResult": {
    "query": "graph-aware verification routing dependency-critical formal verification mathematical proof 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013LbXxJLgtUGofLapiWhEXr",
        "content": [
          {
            "title": "Parallel Verification of Natural Deduction Proof Graphs",
            "url": "https://arxiv.org/pdf/2311.10440"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/pdf/2510.15981"
          },
          {
            "title": "Formal Verification of Routing Protocols for Wireless Ad Hoc Networks",
            "url": "https://www.eurecom.fr/en/publication/2657/download/cm-publi-2657.pdf"
          },
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://arxiv.org/pdf/2506.12509"
          },
          {
            "title": "Formal Reasoning Meets LLMs: Toward AI for Mathematics and Verification – Communications of the ACM",
            "url": "https://cacm.acm.org/research/formal-reasoning-meets-llms-toward-ai-for-mathematics-and-verification/"
          },
          {
            "title": "Automatic verification of dependency",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8555226"
          },
          {
            "title": "ConnChecker: Automated Root-Cause Analysis for Formal Connectivity Check via Graph",
            "url": "https://arxiv.org/pdf/2603.07943"
          }
        ]
      },
      "I've performed the web search for your query. Here are the relevant results found:\n\n## Key Results:\n\n1. **Parallel Verification of Natural Deduction Proof Graphs** - Graph-based interactive theorem provers offer a visual representation of proofs, explicitly representing the dependencies and inferences between proof steps in a graph or hypergraph format. The work presents parallel algorithms for formal verification of graph-based natural deduction style proofs.\n\n2. **ProofFlow: A Dependency Graph Approach** (2025) - This work presents a benchmark of 184 undergraduate-level problems manually annotated with step-by-step solutions and logical dependency graphs. The approach focuses on faithful proof autoformalization with structured dependency handling.\n\n3. **Graph of Verification (GoV)** - This mechanism allows GoV to adaptively adjust its verification granularity—from atomic steps for formal tasks to entire paragraphs for natural language—to match the native structure of the reasoning process.\n\n4. **ConnChecker** - A graph-based framework designed to accelerate root-cause analysis in formal connectivity verification that processes counterexample reports along with functional and structural dependency graphs.\n\n5. **Broader Context (2025-2026)** - Developments in formal reasoning have immediate applications in formal verification of safety-critical systems, with AI potentially automating formalization and proof efforts to make complex systems more robust.\n\nThe search results show active research in graph-aware verification approaches with dependency tracking and formal verification methods in 2025-2026."
    ],
    "durationSeconds": 7.902298986999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "24459e42-6f2d-40ec-9064-07fd9b050542",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research context. Let me synthesize my assessment.  ---  【状态】: 有发掘空间  【前置调研发现】 - [Pseudo-…",
  "leafUuid": "1ae67e5f-3872-4eb0-b4dd-d2fbb1695441",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Assistant

_source line 30 · 2026-05-27T12:46:28.763Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the search results for cross-validation:

**Search 1: Ensemble disagreement + overconfidence**
- Confirms LLMs are overconfident (99% CI covers only 65% of true answers on average)
- BUT cross-model disagreement (ensemble) is found to more accurately capture uncertainty than single-model self-assessment
- This is important: the 发掘 agent's point about "confident-but-wrong" is valid for single-model confidence, but ensemble disagreement may partially mitigate this. However, the concern is still valid — if all ensemble members are wrong in the same way, disagreement won't detect it.


- The risk is real but ensemble approaches may offer some mitigation, so this deserves attention in the proposal.

**Search 2: ThinkPRM**
- Confirmed: ThinkPRM is a significant baseline — beats discriminative PRMs on ProcessBench, MATH-500, AIME'24
- Outperforms LLM-as-Judge by 7.2% on ProcessBench subset
- Uses verbalized step-wise verification (CoT), directly comparable to BV
- ThinkPRM should definitely be included as a baseline.

**Search 3:**
Looking at graph-aware verification routing, I found several related approaches like ProofFlow which uses dependency graphs for autoformalization, and Graph of Verification which handles adaptive granularity in DAG-based verification. However, none of them leverage dependency graph criticality as a routing signal for selective formal verification — so this appears to be a novel contribution.

Now I'm ready to synthesize my overall assessment of these key points.

The first point about confident-but-wrong LLM outputs is validated by research showing overconfidence is real, though ensemble disagreement provides better signal than single-model confidence — I should adopt this with explicit discussion and structural difficulty signals as safeguards. The second point about analyzing proof block structure is logically sound and doesn't require external verification since it's fundamentally about writing quality and argumentation depth. The third point about using dependency graphs as a routing signal is validated as novel, though I'll position it as a secondary signal rather than overcomplicating the main contribution. The fourth point about HERMES being a proof generation agent is logically consistent and worth adopting.

For the remedial agent's feedback, the concern about ArxivMathGradingBench being too small is pragmatic since it's the only research-level benchmark available — I'll adopt the suggestions for bootstrap confidence intervals and synthetic evaluation. The miniF2F protocol needs clarification, which I'll address. ThinkPRM is indeed a strong current baseline that I should acknowledge. The ablation study needs to be more complete by examining individual uncertainty signal contributions and failure modes. The cost fairness concern about ensemble methods is valid and needs addressing.

Now I'm assessing the overall proposal: the novelty is medium-strong with the combination of proof formalization's modular structure and uncertainty-guided routing, strengthened further by reframing it as an architectural principle. The significance is also medium-strong since it bridges a real gap in the cost-reliability tradeoff. However, the experimental completeness is currently weak-to-medium with several identified gaps that need filling.

After addressing these defects, the experimental work could reach medium-strong quality. My probability estimate puts the idea ceiling around 45-50% for AAAI, with the current state at 25-32% and potential to reach 35-45% after fixes. The proposal has genuine novelty in combining proof formalization structure with uncertainty routing for verification, demonstrates practical significance with meaningful cost reduction, and shows reasonable feasibility with solid related work analysis.

I should continue iterating since both agents identified substantive, actionable points in this first round. I'm going to incorporate the key suggestions: adding explicit discussion of the "confident-but-wrong" failure mode and structural difficulty signals, deepening the proof formalization block analysis to show how premises map to hypotheses and conclusions to goals without context dependency, introducing dependency criticality as a secondary routing signal, establishing a clear generation versus verification taxonomy to differentiate HERMES, and reframing the core narrative around modular decomposition as a bridge between these concerns.

For the remedial fixes, I need to add bootstrap confidence intervals and synthetic evaluation for ArxivMathGradingBench, clarify the miniF2F evaluation protocol, specify which PRM baselines I'm comparing against, design ablations for the uncertainty signal and failure handling, introduce a unified cost metric with Pareto curves and ensemble size analysis, set up a controlled comparison between proof formalization and natural language autoformalization, and detail the Lean 4 timeout strategy with resource breakdowns.

Now I'm drafting the updated proposal while being careful to preserve all original references and keep the density high without unnecessary expansion. I'm noting additional tools and benchmarks that came up—arxivMathGradingBench, QwQ-32B, StepFun-Formalizer-32B, ProofSketcher, UCCI, and Lean 4—but I need to be selective about which new references actually strengthen the core proposal rather than just padding the list. ThinkPRM seems like the most essential addition as a baseline comparison.

Now I'm reassessing the probability ceiling across the rubric dimensions. The novelty is medium-strong since the proof-flow block as a structured autoformalization target is genuinely new, and applying uncertainty-guided routing to this specific domain adds real innovation, though it's fundamentally still a pipeline combining existing ideas. Significance lands at medium—there's practical value in cost reduction and the architectural insight about modular decomposition, but the niche audience of mathematical proof verification limits the broader impact. Technical soundness is currently weak-to-medium with several experimental gaps, though those are fixable and could push it to medium-strong once addressed.

The related work section is comprehensive with clear differentiation from concurrent approaches. Taking the minimum of the novelty and significance ceilings puts me around 40-45%, and with experimental improvements that could shift to 38-43%, whereas the current state sits at 28-35% with a midpoint around 31%.

Thinking about this for AAAI 2026, the paper does occupy a clear gap—using proof-flow blocks as a bridge for selective formal verification is well-motivated and novel. The experimental challenges are real but all fixable, though the main risks are whether the approach could be undermined by overconfident-but-wrong predictions, whether autoformalization actually succeeds on proof-flow blocks in practice, and whether reviewers dismiss it as pure engineering rather than a conceptual contribution.

After reframing and strengthening the proposal, I'm estimating an idea ceiling around 42-48%, which drops to 35-42% after experimental fixes, and currently sits at 30-37% with a midpoint of 33% after incorporating this round's improvements. Actually, I need to recalibrate—the question is really about the current proposal as written, before experiments are run. The probability should reflect whether this plan, if executed well, would be accepted. Given that the idea is genuinely novel with clear differentiation, the experimental plan is now much more solid after these revisions, the framing is stronger, and key risks are acknowledged and mitigated, I'd estimate 32-42% with a midpoint around 36%.

Now I'm going through the feedback systematically to decide what to adopt. From the first set of suggestions, I'm taking the confident-but-wrong risk framing since ensemble disagreement alone doesn't fully solve it but the structural difficulty signal is a novel addition, the PF block structural analysis since it's logically sound, the dependency graph routing with some caution to avoid overcomplicating things and positioning it as a secondary signal with ablation studies, the HERMES generation versus verification distinction, and the architectural insight reframing. From the second batch, I'm adopting the statistical power improvements with bootstrap confidence intervals and synthetic evaluation, the miniF2F protocol, and the PRM baselines including ThinkPRM and Qwen2.5-Math-PRM.

I'm also taking the ablation completeness, cost fairness analysis, controlled comparison between PF and natural language approaches, and a lighter touch on the Lean 4 bottleneck since it's already acknowledged. Now I need to write this up carefully, keeping the proposal dense and focused without bloating it.

I'm drafting the core proposal structure starting with the problem statement and research opportunity, then moving into the thesis that modular proof decomposition from Pseudo-Formalization acts as a natural bridge between informal and formal verification approaches.

The key insight is that each PF block's explicit premises, conclusions, and dependency structure create tractable autoformalization targets, enable uncertainty scoring at the block level, and expose dependency graphs that inform which blocks need verification priority. This modular decomposition approach generalizes beyond just our pipeline to any system needing selective formal verification of informal reasoning.

I'm now working through the research landscape section with stronger framing around generation versus verification taxonomy and literature on confident-but-wrong failures, then restructuring the evaluation plan with specific baselines, protocols, and ablations. I need to preserve all the original references while keeping everything tight and well-organized. I'm continuing through the key references, adding several more recent papers on formal verification and mathematical reasoning in LLMs, then noting some specific empirical findings like the significant performance drop on the Hard2Verify benchmark and citation details from recent work. Now I'm considering whether to incorporate the dependency graph idea as a secondary routing signal—it's novel and validated, but I need to be careful not to bloat the proposal scope. I'll frame it as an enhancement to robustness rather than a core contribution. Let me structure the updated proposal carefully, keeping each section focused and precise. Now I'm drafting the full proposal document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ae67e5f-3872-4eb0-b4dd-d2fbb1695441",
  "isSidechain": false,
  "requestId": "req_011CbT6UMUUghjuifuCavLZK",
  "type": "assistant",
  "uuid": "679769c8-9aa8-4076-9378-6344a8b7754e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYrN6mcpw2dj8eCdnnR6dK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2510,
      "cache_read_input_tokens": 33464,
      "output_tokens": 10940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10940,
          "cache_read_input_tokens": 33464,
          "cache_creation_input_tokens": 2510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2510
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

_source line 31 · 2026-05-27T12:48:34.617Z_

Now I have all the cross-validation results. Let me synthesize and produce the integrated output.

**Cross-validation findings summary:**
1. **Ensemble disagreement vs overconfidence**: Research confirms LLMs are systematically overconfident, BUT ensemble disagreement is shown to capture uncertainty more accurately than single-model self-assessment. The "confident-but-wrong" risk is real but partially mitigated by ensemble approach — still worth explicit discussion.
2. **ThinkPRM as baseline**: Confirmed — ThinkPRM outperforms LLM-as-Judge by 7.2% on ProcessBench, outperforms discriminative PRMs on multiple benchmarks with only 1% of labels. It's the current SOTA data-efficient PRM and directly comparable to BV. 补救 agent's suggestion validated.
3. **Graph-aware verification routing**: Found ProofFlow (2025, dependency graph for autoformalization) and Graph of Verification (GoV, DAG-based verification granularity), but **neither uses dependency criticality as a routing signal for selective formal verification**. 发掘 agent's suggestion is genuinely novel.

【阶段】: 迭代第 1 轮

【交叉验证调研】:
1. "Ensemble disagreement vs LLM overconfidence" — 搜索发现：ensemble/cross-model disagreement 比单模型自评更准确地捕获不确定性（MIT 研究, Zylos 2026综述），但 LLM 系统性过度自信问题（99% CI 实际覆盖仅 65%）在单模型层面确实严重。结论：发掘点1的风险真实存在但 ensemble 设计已部分缓解，仍需显式讨论并补充 structural difficulty signal。
2. "ThinkPRM step-level verification baseline" — 搜索确认：ThinkPRM 在 ProcessBench 上比 LLM-as-Judge 高 7.2%，比 PRM800K 训练的判别式 PRM 分别高 8%/4.5%（out-of-domain），是当前 SOTA data-efficient PRM，与 BV 的 CoT verification 直接可比。补救点3 已验证。
3. "Graph-aware verification routing for math proof" — 搜索发现 ProofFlow（2025, dependency graph for autoformalization）和 Graph of Verification（DAG-based verification granularity），但无任何工作将 dependency criticality 用作选择性形式化验证的 routing signal。发掘点3 的新颖性已验证。

【发掘 agent 有效建议采纳】:
- 发掘点1（Confident-but-wrong 风险）: **已验证，采纳**。ensemble disagreement 部分缓解但不消除此风险。在 proposal 中显式讨论风险并引入 structural difficulty signal（块内推理步数、依赖定理数量）作为补充路由信号。
- 发掘点2（PF 块结构性分析强化）: **逻辑验证，采纳**。加入 PF 块→Lean 4 的显式结构对齐分析（premises→hypothesis, conclusion→goal, self-contained→no context completion）。
- 发掘点3（Dependency graph 作为路由信号）: **已验证为新颖，采纳**。搜索未发现任何工作将 dependency criticality 用于 verification routing。作为 secondary signal 纳入，与 uncertainty 组合为 "uncertainty × dependency criticality" 双信号策略。
- 发掘点4（HERMES generation vs verification taxonomy）: **逻辑验证，采纳**。建立清晰的 taxonomy 防止审稿人混淆。
- 发掘点5（Architectural insight reframing）: **采纳，但控制力度**。将核心叙事从 "cost-reliability optimization" 提升为 "modular decomposition as bridge"，但避免过度声称普适性以免审稿人质疑 evidence 不足。

【补救 agent 有效建议采纳】:
- 缺陷1（ArxivMathGradingBench 统计功效）: **采纳**。加入 bootstrap CI + 合成评估集（Hard2Verify 构建 200+ error instances）+ Platt scaling 替代 isotonic regression。
- 缺陷2（miniF2F 评测协议）: **采纳**。明确协议：用 LLM 生成 candidate proofs，混合正确/错误，评 verification precision/recall；同时将 PF block autoformalization 的 type-check rate 作为组件评估。
- 缺陷3（PRM baselines）: **已验证，采纳**。明确纳入 ThinkPRM 和 Qwen2.5-Math-PRM-7B。
- 缺陷4（Ablation 不完整）: **采纳**。新增：(a) ensemble disagreement / CoT entropy / combined 的 AUROC 对比；(b) autoformalization failure fallback 策略 ablation。
- 缺陷5（Cost 公平性）: **采纳**。定义 GPU-seconds per proof 统一度量 + cost breakdown table + Pareto 曲线 + ensemble size ablation (N=3/5/7)。
- 缺陷6（PF vs NL autoformalization controlled comparison）: **采纳**。设计 paired comparison 实验，type-check rate + proof search success rate + paired statistical test。
- 缺陷7（Lean 4 瓶颈）: **采纳，轻量化**。加入 timeout 策略（per-block 5min, per-proof 30min）和 GPU/CPU 时间分列。

【本轮 proposal 主要变更】:
**Idea 层面变更:**
- 核心叙事从 "cost-reliability tradeoff" 重构为 "modular proof decomposition as a natural bridge between informal and formal verification"
- 新增 PF 块→Lean 4 的显式结构对齐分析（premises→hypothesis, conclusion→goal, self-contained context）
- 路由策略从纯 uncertainty 升级为 "uncertainty × dependency criticality" 双信号
- 新增 "confident-but-wrong" 风险的显式讨论与缓解策略
- 建立 "proof generation vs. proof verification" taxonomy 明确与 HERMES 的范式差异

**实验层面变更:**
- 新增合成评估集（Hard2Verify 构建 200+ error instances）补充 ArxivMathGradingBench
- 明确 miniF2F 评测协议（LLM-generated candidate proofs, verification precision/recall）
- 指定 PRM baselines：ThinkPRM + Qwen2.5-Math-PRM-7B
- 新增 3 个 ablation：uncertainty signal decomposition, failure fallback strategy, ensemble size (N=3/5/7)
- 引入统一 cost metric (GPU-seconds/proof) + Pareto 曲线 + cost breakdown table
- 设计 PF vs raw NL autoformalization paired comparison experiment
- 加入 Lean 4 timeout 策略和 GPU/CPU 资源分列

【idea 质量评估】: Novelty=中强 Significance=中强 → idea 天花板约 45%
- Novelty 中强：PF 块作为 autoformalization bridge 是该领域独特 insight，dependency criticality routing 经验证无先例，但整体仍是 pipeline 组合
- Significance 中强：reframing 为 architectural principle 提升了普适意义，但应用域仍较窄（数学证明验证）

【实验完备性评估】: Technical Soundness=中（修复后可达中强） → 实验层面目前是 proposal 阶段的设计，补救建议均已采纳
- 统计功效问题已有补救方案但仍依赖合成数据集的构建质量
- Cost 公平性分析框架已建立，但实际数字需实验验证
- 所有 ablation 已规划，覆盖了审稿人最可能质疑的维度

【当前概率估计】: [32% - 42%] 中位 36%
- 上限 42% 受限于 pipeline/combination paper 的天然 novelty 上界，即使 reframing 为 architectural insight
- 下限 32% 反映核心实验依赖的不确定性（autoformalization success rate on PF blocks 未经验证、ArxivMathGradingBench 小样本风险）
- 中位 36% 基于：idea 质量天花板约 45%，实验设计扣减约 8-10% 的不确定性惩罚

【决策】: 继续

【决策理由】: 第 1 轮改动幅度大（idea 重构 + 实验全面补强），需要至少一轮 worker 验证改动后的 proposal 是否 internally consistent、是否有新引入的问题、以及 novelty reframing 是否站得住脚。发掘 agent 和补救 agent 都未报告致命缺陷，概率处于上升轨道。

**引用保留核对清单**（逐条确认出现在下方纯净版中）:
1. ✅ Pseudo-Formalization (Barkallah et al., arXiv 2026)
2. ✅ Safe (Liu et al., ACL 2025)
3. ✅ Hard2Verify (Pandit et al., arXiv 2025)
4. ✅ miniF2F-Lean Revisited (NeurIPS 2025)
5. ✅ Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025)
6. ✅ Adaptive Test-Time Compute Allocation (Qu, arXiv 2026)
7. ✅ VERGE (Singh et al., arXiv 2026)
8. ✅ HERMES (Ospanov et al., ICML 2026)
9. ✅ Goedel-Prover-V2 (ICLR 2026)
10. ✅ Reasoning with Confidence / Uncertainty Heads (arXiv 2025)
11. ✅ ProofSketcher (arXiv 2026)
12. ✅ UCCI (arXiv 2026)
13. ✅ 78.3% → 37.3% on Hard2Verify
14. ✅ ArxivMathGradingBench
15. ✅ QwQ-32B, StepFun-Formalizer-32B, Goedel-Prover-V2-32B
16. ✅ 新增: ThinkPRM (2025), Qwen2.5-Math-PRM, ProofFlow (2025)

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition

## Core Problem

How can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain and structurally critical proof blocks to formal verification?

## Architectural Insight (Thesis)

Modular proof decomposition — as instantiated by Pseudo-Formalization (Barkallah et al., 2026) — serves as a natural bridge between informal and formal verification of mathematical proofs. Each PF block's structure creates a tractable autoformalization target because: (a) explicit typed premises map directly to Lean 4 hypothesis lists, (b) a single explicit conclusion maps to a Lean 4 goal statement, and (c) self-contained blocks eliminate the context-completion problem that plagues whole-proof autoformalization (which achieves only ~35% end-to-end success; miniF2F-Lean Revisited, NeurIPS 2025). This structural alignment, combined with calibrated uncertainty scoring and inter-block dependency awareness, enables selective formal verification: routing only the most uncertain and dependency-critical blocks to formal verification while accepting the rest via cheaper LLM verification.

## Research Opportunity

Pseudo-Formalization (Barkallah et al., May 2026) introduced modular proof blocks with explicit premises, conclusions, and dependencies — but verifies them only via LLM, missing ~50% of research-level errors on ArxivMathGradingBench. Safe (Liu et al., ACL 2025) achieves step-level formal verification at 80% proof success but imposes 4-8x cost overhead by verifying ALL steps uniformly. No prior work has exploited PF's self-contained modular structure as a bridge to targeted autoformalization. By combining Block Verification confidence with dependency-graph criticality as a dual triage signal, we can route only the 10-20% most uncertain or structurally critical blocks to formal verification, catching errors that LLM verification misses while avoiding the prohibitive cost of universal formalization.

## Research Landscape

Current proof verification spans a cost-reliability spectrum with no effective middle ground:

**LLM-based verification (cheap, unreliable):** Best PRM drops from 78.3% to 37.3% on Hard2Verify (Pandit et al., 2025). PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026). ThinkPRM (2025) advances data-efficient verbalized PRMs that outperform discriminative PRMs with 1% of process labels, representing the current strongest step-level LLM verifier.

**Universal formal verification (reliable, expensive):** Safe verifies each step in Lean 4 with ~80% success but costs 4-8x more compute per step (Liu et al., ACL 2025). End-to-end autoformalization pipelines achieve only ~35% success because autoformalization accuracy (66% human-judged, not the 97% reported under LLM-judging) and theorem proving success (~70%) compound poorly (miniF2F-Lean Revisited, NeurIPS 2025).

**Selective/adaptive verification (emerging):** Uncertainty-guided selective verification achieves 14-100% error reduction with minimal abstention in SMT-based formalization (Ganguly et al., NeurIPS 2025); adaptive verification allocation achieves 44% fewer verifier calls with higher accuracy on MATH (Qu, arXiv 2026). Neither has been applied to NL proof verification with pseudo-formal structure as intermediary.

**Concurrent work — generation vs. verification taxonomy:** A critical distinction separates proof generation systems from proof verification pipelines. HERMES (Ospanov et al., ICML 2026) is a proof generation agent that interleaves informal reasoning with formally verified Lean 4 steps during proof construction, achieving 67% accuracy improvement with 80% fewer FLOPs — but it applies uniform formalization during generation, where output format is controllable. Our work addresses the fundamentally different proof verification setting, where input proofs have arbitrary format and PF decomposition is necessary to create structured formalization targets. VERGE (Singh et al., arXiv 2026) implements semantic routing between SMT solvers and LLM-ensemble verification but targets first-order logic claims rather than mathematical proof blocks. UCCI (arXiv 2026) provides calibrated uncertainty for cost-optimal LLM cascade routing but operates on model cascades rather than formal/informal verification tiers. ProofSketcher (arXiv 2026) produces typed proof sketches with trusted kernel expansion but without uncertainty-guided routing. ProofFlow (2025) uses dependency graphs for autoformalization fidelity but not for verification routing. None of these systems combine PF's modular block structure with uncertainty-guided routing for mathematical proof verification.

## Proposed Approach

We build a two-tier verification pipeline atop Pseudo-Formalization (Barkallah et al., 2026):

**Tier 1 — LLM Block Verification with calibrated uncertainty.** Given a mathematical proof, we decompose it into PF blocks with explicit premises, conclusions, and dependency graphs, then run LLM-based Block Verification using QwQ-32B augmented with dual uncertainty scoring: (i) ensemble disagreement via N=5 stochastic forward passes with temperature sampling, and (ii) token-level CoT entropy. Scores are calibrated via Platt scaling on held-out annotations (preferred over isotonic regression for small-sample robustness).

**Dual-signal routing.** Blocks are routed to Tier 2 based on a combined score: uncertainty (calibrated BV confidence) × dependency criticality (fan-out degree in the inter-block dependency graph — high-fan-out blocks propagate errors to many downstream blocks). This dual-signal design mitigates the "confident-but-wrong" risk: even if BV assigns high confidence to a structurally critical block, its high dependency fan-out ensures it receives formal verification. We target routing the bottom 10-20% of blocks by combined score.

**Confident-but-wrong risk mitigation.** LLMs exhibit systematic overconfidence (e.g., nominal 99% CIs covering only ~65% of true answers). Our mitigation is threefold: (a) ensemble disagreement captures inter-model uncertainty more reliably than single-model confidence; (b) dependency criticality provides an uncertainty-independent routing signal; (c) we include a structural difficulty heuristic (block-internal reasoning step count, number of cited theorems) as an additional routing feature. We explicitly measure the proportion of confident-but-wrong errors in ablation to quantify this risk.

**Tier 2 — Selective formal verification.** Routed blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging each PF block's explicit premises and conclusion as structured autoformalization targets (premises→Lean 4 hypotheses, conclusion→Lean 4 goal, no context completion needed) — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction. Per-block timeout: 5 minutes; per-proof timeout: 30 minutes. Fallback strategy for autoformalization failure or proof search timeout is treated as an ablation variable (accept / reject / re-verify via majority-vote ensemble BV).

## Evaluation Plan

**Benchmarks:**
- ArxivMathGradingBench (Barkallah et al., 2026): 35 papers, 40 known errors. Primary research-level evaluation. Report error detection precision, recall, F1 with bootstrap confidence intervals (1000 resamples) and McNemar's test for pairwise comparisons.
- Synthetic Error Detection Set: Constructed from Hard2Verify competition-level problems using LLM-generated incorrect proofs alongside ground-truth correct proofs, targeting 200+ error instances. Provides statistical power unavailable from ArxivMathGradingBench alone.
- miniF2F Verification Protocol: Generate N candidate proofs per problem using QwQ-32B (mix of correct and incorrect), then evaluate our pipeline's verification precision/recall. Align with Safe's miniF2F evaluation setting for fair comparison.

**Baselines:**
- PF + BV single-pass (Barkallah et al., 2026): upper bound on cost efficiency, lower bound on reliability
- PF + BV ensemble (N=5, no formal verification): isolates uncertainty scoring contribution
- ThinkPRM (2025): SOTA data-efficient verbalized PRM, most directly comparable to BV's CoT verification
- Qwen2.5-Math-PRM-7B: strongest open-source discriminative PRM at comparable scale
- Safe universal formalization (Liu et al., ACL 2025): upper bound on reliability, lower bound on cost efficiency
- HERMES (Ospanov et al., ICML 2026): if applicable to verification setting; otherwise note the generation-vs-verification gap

**Cost framework:** Unified metric: GPU-seconds per proof (covering all computation: PF decomposition, ensemble BV, routing, autoformalization, proof search including timeouts). Cost breakdown table decomposing each component. Pareto curve (cost vs. error detection recall) plotting all methods on a single figure.

**Ablations:**
1. Uncertainty signal decomposition: ensemble disagreement only / CoT entropy only / combined — report AUROC, ECE, error detection recall at fixed cost
2. Routing signal: uncertainty only / dependency criticality only / dual signal — error detection recall and cost
3. Ensemble size: N=3 / N=5 / N=7 — cost-quality tradeoff
4. Autoformalization failure fallback: accept / reject / majority-vote re-verification — precision/recall impact
5. Threshold selection: sweep routing percentage from 5% to 50% — Pareto curve
6. PF blocks vs. raw NL autoformalization (core hypothesis validation): paired comparison on same proofs — PF block input vs. corresponding raw NL fragment input to StepFun-Formalizer-32B. Metrics: Lean 4 type-check rate, Goedel-Prover-V2 proof search success rate, paired Wilcoxon signed-rank test. This directly validates the architectural insight that PF structure enables more reliable autoformalization.
7. Confident-but-wrong analysis: measure proportion of BV errors that are high-confidence (>0.8) on ArxivMathGradingBench, quantify what fraction dual-signal routing captures vs. uncertainty-only routing.

## Key References

- Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2026)
- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)
- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (Pandit et al., arXiv 2025)
- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)
- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (Ganguly et al., NeurIPS 2025)
- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (Qu, arXiv 2026)
- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., arXiv 2026)
- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)
- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)
- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)
- ThinkPRM: Process Reward Models That Think (2025)
- Qwen2.5-Math-PRM (2025)
- ProofSketcher (arXiv 2026)
- UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing (arXiv 2026)
- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (2025)

## Resource Estimate

- **GPU hours**: 350-500 (uncertainty calibration + ensemble BV ~80h; StepFun-Formalizer inference ~80h; Goedel-Prover-V2 proof search ~120h including timeouts; synthetic dataset construction ~30h; baselines + ablations ~100-150h; all on A100-80GB). Lean 4 kernel type-checking is CPU-bound (~50 CPU-hours additional).
- **Timeline**: 12-16 weeks (2-3 researchers). Critical path: synthetic evaluation set construction (weeks 1-3) → uncertainty calibration (weeks 3-6) → full pipeline + ablations (weeks 6-14) → analysis + writing (weeks 14-16).
- **Estimated GPU cost**: $1050-1500
- **Lean 4 proof search bottleneck**: Per-block timeout 5 min, per-proof timeout 30 min. Estimated formal verification wall-clock for ArxivMathGradingBench: ~9h per configuration pass (35 papers × ~30 blocks × 15% routing × 3.5 min/block). Independent blocks parallelizable.
---

Sources:
- [LLMs are Overconfident](https://arxiv.org/pdf/2510.26995)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [ProofFlow: A Dependency Graph Approach](https://arxiv.org/pdf/2510.15981)
- [MIT: Better method for identifying overconfident LLMs](https://computing.mit.edu/news/a-better-method-for-identifying-overconfident-large-language-models/)
- [Graph of Verification](https://arxiv.org/pdf/2506.12509)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "679769c8-9aa8-4076-9378-6344a8b7754e",
  "isSidechain": false,
  "requestId": "req_011CbT6UMUUghjuifuCavLZK",
  "type": "assistant",
  "uuid": "873cc2d7-ef34-4481-8042-9b55721ce7d2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AYrN6mcpw2dj8eCdnnR6dK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2510,
      "cache_read_input_tokens": 33464,
      "output_tokens": 10940,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2510,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10940,
          "cache_read_input_tokens": 33464,
          "cache_creation_input_tokens": 2510,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2510
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
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research context. Let me synthesize my assessment.  ---  【状态】: 有发掘空间  【前置调研发现】 - [Pseudo-…",
  "leafUuid": "873cc2d7-ef34-4481-8042-9b55721ce7d2",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 1 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research context. Let me synthesize my assessment.  ---  【状态】: 有发掘空间  【前置调研发现】 - [Pseudo-…",
  "leafUuid": "873cc2d7-ef34-4481-8042-9b55721ce7d2",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 37 · 2026-05-27T12:53:53.875Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T12:53:53.875Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "content": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have a comprehensive picture of the research landscape. Let me compile my assessment.\n\n---\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n\n- **[Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)** (arXiv, May 2026): The foundational paper. Decomposes proofs into self-contained modules with explicit premises, conclusions, and dependencies; verifies via LLM only. Achieves Pareto-dominance over LLM-as-judge but leaves ~50% of research-level errors undetected. Critically, the paper itself does *not* explore its modular structure as a formalization target — this is genuinely an untapped direction.\n\n- **[Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047)** (NeurIPS 2025): The closest conceptual precedent for \"uncertainty → selective formal verification.\" Models LLM-generated SMT-LIB program distributions with PCFGs, achieves 14-100% error reduction with minimal abstention. **Key difference from this proposal**: operates on structured formal artifacts (SMT-LIB programs), not natural language math proofs; no modular decomposition layer; no dependency-based routing signal. The proposal's novelty relative to this work hinges on (a) the PF intermediary layer and (b) the dual-signal routing design.\n\n- **[ProofFlow](https://arxiv.org/abs/2510.15981)** (arXiv 2025): Constructs DAGs to map logical dependencies between proof steps for faithful autoformalization. Achieves ProofScore of 0.545 vs. baselines at 0.072-0.123. **Uses dependency graphs for autoformalization fidelity but not for verification routing decisions.** This is the paper that comes closest to combining dependency awareness with formalization, but the routing dimension is completely absent.\n\n- **[miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108)** (NeurIPS 2025): Reveals that end-to-end autoformalization + theorem proving achieves only ~36% success rate; autoformalization accuracy is ~66% (human-judged) vs. inflated 97% (LLM-judged). The paper attributes much of the failure to context-completion difficulties and benchmark quality. **This directly supports the proposal's thesis that self-contained PF blocks should be better autoformalization targets by eliminating context-completion.**\n\n- **[Solve-Detect-Verify / FlexiVe](https://arxiv.org/abs/2505.11966)** (arXiv 2025): Adaptive verification budget between fast/slow thinking for generative verifiers. Conceptually parallel (selective allocation of verification compute) but operates within LLM-tier verification (generative reward models), not across the LLM-to-formal verification boundary. No structural decomposition.\n\n- **[UCCI](https://arxiv.org/abs/2605.18796)** (arXiv 2026): Calibrated uncertainty (isotonic regression) for cost-optimal LLM cascade routing. Cuts inference cost by 31% at maintained quality. **Operates on model cascades (small→large LLM) rather than formal/informal verification tiers.** The calibration methodology is relevant, but the routing target is fundamentally different.\n\n- **[Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)** (2024/2025): Step-level formalization with Lean 4 compiler feedback loops and process-supervised verifier. **Relevant as evidence that step-level (rather than whole-proof) autoformalization is more tractable**, which supports the proposal's block-level approach. However, their \"steps\" come from the formalization process itself, not from a pre-existing modular decomposition like PF.\n\n- **调研总结**: The field is converging on two key insights: (1) whole-proof autoformalization is fundamentally limited (~36% end-to-end), driving interest in modular/step-level approaches; (2) selective allocation of expensive verification is an emerging paradigm (Ganguly for SMT, FlexiVe for GenRM, UCCI for model cascades), but **no one has yet combined a structured modular decomposition with uncertainty-guided routing to a formal verification tier for NL math proofs**. The proposal sits at a genuine gap in the literature.\n\n---\n\n【发掘点 1】\n- 维度: significance 提升 / 核心 claim 强化\n- 内容: 当前 proposal 的 significance framing 是 \"cost-efficient verification\"（在 cost-reliability spectrum 找到中间地带）。这虽然正确，但天花板不够高。调研发现 miniF2F-Lean Revisited 的核心结论是：whole-proof autoformalization 受 context-completion problem 制约，end-to-end 成功率仅 ~36%，这是一个 **fundamental architectural limitation**，不是简单的工程问题——随着模型变强，whole-proof autoformalization 的瓶颈（context dependency compounding）不会自动消失。Proposal 应当将 significance 提升到这一层：**PF-based selective formalization 不仅仅是\"省钱\"，而是可能是唯一能让 formal verification 扩展到 research-level proofs 的可行架构**。因为 research-level proofs 太长、太复杂，whole-proof autoformalization 在可预见的未来无法处理；而 PF 的 self-contained block structure 通过消除 context-completion 问题，从根本上改变了 autoformalization 的可行性边界。这把 contribution 从\"一个 cost-saving 工程优化\"提升到\"解决 formal verification scalability 的 architectural insight\"。\n- 价值: 直接提升 Significance 维度。审稿人看到\"cost-efficient\"会想\"incremental engineering\"；看到\"the only viable path to formal verification of complex proofs\"会想\"architectural contribution\"。\n- 调研依据: miniF2F-Lean Revisited (NeurIPS 2025) 揭示的 whole-proof autoformalization ~36% 成功率上限，以及 Process-Driven Autoformalization 证明 step-level formalization 更 tractable 的实证。\n\n【发掘点 2】\n- 维度: novelty 锐化 / related work 差异化\n- 内容: Proposal 当前与 Ganguly et al. (NeurIPS 2025) 的差异化描述不够锐利。表面差异是\"SMT vs NL proofs\"和\"有无 PF intermediary\"，但这容易被审稿人解读为\"same idea, different domain\"。真正的核心差异需要更 sharp 地表达：Ganguly 的 uncertainty signal 来自 **生成端** (LLM 生成 SMT-LIB program 的 distribution)，routing target 是 **同质的** (都是 SMT solver verification，只是选择是否 verify)。而本 proposal 的 uncertainty signal 来自 **验证端** (BV 对 block 正确性的判断 uncertainty)，routing target 是 **异质的** (从 LLM verification 路由到 formal verification，是两种根本不同的验证 paradigm)。更重要的是，Ganguly 没有 **structural routing signal**——他们的 selective verification 完全基于 output uncertainty，而本 proposal 的 dual-signal design 引入了 dependency criticality 这个与 uncertainty 正交的 routing dimension。这是一个 genuinely novel contribution，不只是 domain transfer。建议在 related work 差异化中明确强调这三个层次的区别：(1) uncertainty source (生成端 vs 验证端), (2) routing target heterogeneity (同质 vs 异质 verification paradigm), (3) structural criticality dimension (absent in Ganguly)。\n- 价值: Novelty + Related Work 差异化。防止审稿人把本工作简单归类为\"Ganguly et al. applied to NL proofs\"。\n- 调研依据: 直接对比 Ganguly et al. (NeurIPS 2025) 的方法设计——其 PCFG-based uncertainty modeling 完全在生成端操作，无 inter-step dependency 概念。\n\n【发掘点 3】\n- 维度: trivial alternative 威胁\n- 内容: Proposal 需要明确防御一个 trivial alternative：**简单启发式 routing 是否已经足够好？** 具体而言，如果用 block-internal reasoning step count、cited theorems 数量、或 block 文本长度等 simple features 作为 routing signal，是否能达到与 calibrated uncertainty 相近的效果？Proposal 已经在 Tier 2 描述中提到了 \"structural difficulty heuristic\"作为额外 routing feature，但这反而暴露了问题：如果 simple heuristic 本身就有效，那 ensemble disagreement + CoT entropy 的增量价值是什么？建议：(a) 在 ablation 中显式加入 \"simple heuristic only\" 作为 routing baseline（block length, step count, cited theorem count），(b) 在 claim 层面明确论证 why calibrated uncertainty should capture errors that structural heuristics miss（例如：结构简单但 reasoning subtle 的 block，heuristic 会 miss 但 BV ensemble disagreement 会 flag）。这不是要加实验（那是补救 agent 的事），而是要在 idea 层面把 claim 说圆：calibrated uncertainty 的增量价值到底在哪里。\n- 价值: 加固 Novelty claim。如果 simple heuristic 足够好，这个 idea 的核心技术贡献（calibrated uncertainty + dual signal）就被 undermine 了。\n- 调研依据: 基于领域整体趋势判断——UCCI (2026) 和 Ganguly (2025) 都在强调 calibrated uncertainty 相对于 naive confidence 的优势，但两者都没有与 simple structural heuristics 做过 head-to-head 比较。\n\n【发掘点 4】\n- 维度: 核心 claim 强化 / 前提假设质疑\n- 内容: \"Dependency criticality\" 目前仅用 fan-out degree 来度量。这个定义虽然直觉合理（高 fan-out block 的错误传播到更多下游 block），但存在两个盲区：(1) **\"bottleneck\" block**——fan-out 不高但处于依赖链的唯一路径上，其错误会导致所有下游 block 的前提失效。图论中的 \"dominator node\" 概念更准确地捕捉了这种 criticality。(2) **距离 final conclusion 的 proximity**——直接支撑 main theorem 的 block，即使 fan-out 为 1，其错误也是致命的。建议将 dependency criticality 从单一的 fan-out degree 扩展为更丰富的 graph-theoretic measure：dominator analysis (dominator tree 中的 immediate dominator 节点) + topological centrality (PageRank 或 betweenness centrality on the dependency DAG)。这不改变方法论的核心架构，但锐化了 \"structural criticality\" 这个 contribution 的技术深度，让审稿人看到这不是一个 ad-hoc heuristic 而是有图论 grounding 的 principled design。\n- 价值: 直接提升 Novelty 维度。把 dependency criticality 从一个 simple heuristic (fan-out) 提升为一个 principled graph-theoretic framework，增加了技术贡献的 depth。\n- 调研依据: ProofFlow (2025) 使用 DAG 做 autoformalization fidelity 但未探索 graph-theoretic criticality measures for routing; Ganguly et al. 完全没有 structural routing signal。这个方向在当前文献中是空白的。\n\n【发掘点 5】\n- 维度: significance 提升\n- 内容: Proposal 当前的 evaluation 以 error detection (precision/recall/F1) 为核心 metric。但如果把 significance 提升到\"making formal verification scalable for real mathematical research\"这个层面（见发掘点 1），那么一个更有影响力的 metric 是 **autoformalization tractability gain**：即 PF block-level autoformalization 相比 whole-proof / raw-NL-fragment autoformalization，在 Lean 4 type-check rate 和 proof search success rate 上的提升倍数。Proposal 的 ablation 6 已经包含了这个比较，但目前只是作为 ablation 之一。建议将其提升为 **core result** 而非 ablation：如果 PF blocks 能将 autoformalization success rate 从 ~35% (whole-proof baseline, miniF2F-Lean Revisited) 显著提升到例如 60%+，这本身就是一个 standalone contribution-level finding，直接回答了\"why modular decomposition matters for formal verification\"这个 open question。把它埋在 ablation 里是低估了它的价值。\n- 价值: 提升 Significance。把一个 ablation-level 的验证提升为 contribution-level 的 finding，让论文同时在 verification pipeline design 和 autoformalization methodology 两个维度有贡献。\n- 调研依据: miniF2F-Lean Revisited (NeurIPS 2025) 确立了 whole-proof autoformalization ~36% 的 baseline；Process-Driven Autoformalization 证明 step-level approaches 更 tractable。如果 PF block-level 能显著超越这些 baselines，这是一个对领域有重要价值的 empirical finding。\n\nSources:\n- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)\n- [Safe: Enhancing Mathematical Reasoning via Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/)\n- [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047)\n- [ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization](https://arxiv.org/abs/2510.15981)\n- [miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108)\n- [Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier](https://arxiv.org/abs/2505.11966)\n- [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/abs/2605.18796)\n- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)\n- [HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs](https://arxiv.org/abs/2511.18760)\n- [Adaptive Test-Time Compute Allocation](https://arxiv.org/pdf/2602.03975)\n\n【补救 agent 本轮输出】:\nNow I have comprehensive context. Let me synthesize my findings and produce the formal evaluation.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **Safe (Liu et al., ACL 2025)**: 提出 FormalStep benchmark（30,809 formal statements），逐步 Lean 4 形式化验证，将 retrospective formal scores 与 PRM 分数集成。实验覆盖多个 LLM 和数学数据集。Baselines 包括多种 PRM 和 LLM-as-judge 方法。\n- **Pseudo-Formalization (Barkallah et al., arXiv 2605.20531, May 2026)**: Block Verification 在 ArxivMathGradingBench（35 papers, 40 known errors）和奥赛数学上 Pareto-dominate LLM-as-judge baselines。数据集极小。\n- **ThinkPRM (arXiv 2504.16828, 2025; submitted ICLR 2026)**: 在 ProcessBench, MATH-500, AIME'24, GPQA-Diamond, LiveCodeBench 上评估。使用 R1-Distill-Qwen{1.5B,7B,14B} 和 QwQ-32B-Preview 四个变体。Ablation 包括训练数据量、模型规模。\n- **Ganguly et al. \"Grammars of Formal Uncertainty\" (NeurIPS 2025)**: SMT-based selective verification，使用 N=5 for baselines, N=100 for UQ analysis。AUROC>0.93 on grammar entropy。Selective verification 实现 14-100% error reduction。\n- **Goedel-Prover-V2 (ICLR 2026)**: SOTA open-source ATP, pass@32 在 MiniF2F 达 88.1%（self-correction 模式 90.4%），PutnamBench 解决 86 题。\n- **StepFun-Formalizer-32B (AAAI 2026)**: Statement autoformalization 的 BEq@1 为 40.5% (FormalMATH-Lite) / 26.7% (ProverBench)。注意：这是 statement-level 性能，不是 block-level proof step formalization。\n- **miniF2F-Lean Revisited (NeurIPS 2025)**: 揭示 autoformalization accuracy 在人类评估下仅 ~66%（LLM 评估报告 97%），端到端 ~35%。\n- **\"Do We Need Frontier Models to Verify Mathematical Proofs?\" (arXiv 2604.02450, 2026)**: 通过 LLM-guided prompt search + specialized prompt ensemble，使小模型 (Qwen3.5-35B) 在 proof verification accuracy 上接近 frontier models（提升 9.1% accuracy, 15.9% self-consistency）。直接相关但 proposal 未涉及。\n- **DiscoUQ (2026)**: 结构化 ensemble disagreement 分析，AUROC 0.802, ECE 0.036，显著优于 baseline。提示 ensemble disagreement 的具体实现方式对校准质量影响很大。\n- 调研总结：该领域当前实验标准要求 (a) 在多个难度层级的 benchmark 上评估（competition-level + research-level）, (b) 与最新 PRM/verbalized verifier 作对比, (c) 明确的 compute-normalized Pareto 分析, (d) 至少包括 autoformalization success rate 的独立报告。审稿人普遍关注统计显著性（尤其在小数据集上）、autoformalization 各环节的成功率分解报告、以及 LLM-only 强基线是否被充分探索。\n\n---\n\n【缺陷 1】\n- 类别: 评估方案缺陷 — 统计功效不足\n- 问题: ArxivMathGradingBench 仅含 35 papers / 40 known errors，作为 primary research-level evaluation，bootstrap CI（1000 resamples）在 n=40 上置信区间会非常宽，McNemar's test 在样本量如此小时 power 极低。Proposal 声称的方法改进（例如从 ~50% recall 提升到 ~70%）在 40 个 error 上意味着仅多检测到 ~8 个错误，随机波动就可能解释这一差异。这是审稿人最可能质疑的点之一——\"你在 40 个 error 上的改进有统计意义吗？\"\n- 严重度: 可补救\n- 补救方案: \n  (1) **明确将 Synthetic Error Detection Set 提升为 co-primary benchmark**（而非辅助），并将其目标从 \"200+ instances\" 提高到 **400-500 instances**，跨越多个错误类型（logical gap, computational error, incorrect theorem citation, unjustified step 等）。在 400+ 样本上，McNemar's test 和 bootstrap CI 才有足够 power 检测 5-10% 的绝对改进。\n  (2) 在 ArxivMathGradingBench 上，**补充 per-paper accuracy（proof-level correctness detection）** 作为辅助指标，增加统计单元数量（从 40 errors 扩展到 35 papers × {correct/incorrect} classification）。\n  (3) 明确报告 effect size（Cohen's h 或 odds ratio）而不仅仅是 p-value，让审稿人评估实际影响大小。\n  (4) 在 miniF2F Verification Protocol 上确保足够的候选 proof 数量（建议每题生成 ≥8 候选，覆盖 ≥100 题），使该 benchmark 也具备独立的统计可信度。\n- 调研依据: Ganguly et al. (NeurIPS 2025) 在 selective verification 中使用 N=100 samples per question 以确保统计意义；Hard2Verify 投入 500+ 小时人工标注确保 benchmark 规模。ArxivMathGradingBench 的 40 errors 远低于该领域评估标准。\n\n【缺陷 2】\n- 类别: 可行性问题 — Block-level autoformalization 成功率未知\n- 问题: Proposal 的核心架构假设是 PF block 的结构（explicit premises → Lean hypotheses, conclusion → Lean goal）能显著提升 autoformalization 成功率，从而使 Tier 2 selective formal verification 可行。但 StepFun-Formalizer-32B 在 statement-level autoformalization 上的 BEq@1 仅为 40.5% (FormalMATH-Lite) / 26.7% (ProverBench)。PF blocks 不仅需要 statement formalization（premises 和 conclusion），还需要 Goedel-Prover-V2 证明 conclusion follows from premises——这是 theorem proving，不是单纯 statement translation。如果 block-level autoformalization + proof search 的端到端成功率低于 40-50%，则 Tier 2 在超过一半被路由的 blocks 上会失败，极大削弱系统可靠性。Ablation 6 虽然测试了这一点，但如果结果太差，整个 pipeline 的核心 claim 就无法成立。\n- 严重度: 可补救（但需要前置验证）\n- 补救方案:\n  (1) **在全面实验前做 pilot study**：随机抽取 50-100 PF blocks（涵盖不同数学领域和难度），分别测试 StepFun-Formalizer 的 formalization 成功率和 Goedel-Prover-V2 的 proof search 成功率，建立 block-level 端到端成功率的 baseline 估计。如果端到端成功率 < 30%，需要重新评估 Tier 2 的可行性或引入更强的 autoformalization 策略（如 multi-shot formalization with self-correction）。\n  (2) 在实验中**分解报告 Tier 2 各环节成功率**：formalization type-check rate → proof search success rate → end-to-end verification success rate，让审稿人理解瓶颈在哪里。\n  (3) 讨论 **fallback 策略对 headline 数字的影响**：当 Tier 2 失败时，accept/reject/majority-vote 的选择会直接影响 precision 和 recall。Proposal 将其列为 ablation variable 是对的，但应该在 expected results 中明确讨论\"如果 Tier 2 成功率仅为 X%，各 fallback 策略下的系统性能预期\"。\n- 调研依据: miniF2F-Lean Revisited (NeurIPS 2025) 明确显示 autoformalization 端到端成功率在人类评估下仅 ~35%（66% formalization × ~53% proving），且这是在 competition-level 标准化问题上。Research-level PF blocks 的难度更高，成功率可能更低。StepFun-Formalizer (AAAI 2026) 的 BEq@1 40.5% 也仅是 statement-level。\n\n【缺陷 3】\n- 类别: baseline 不足或过时 — 缺少\"强 LLM verification\"基线\n- 问题: Proposal 的 baselines 在 LLM-only 一端包括 PF+BV single-pass、PF+BV ensemble、ThinkPRM、Qwen2.5-Math-PRM-7B，但遗漏了一个关键的最新 baseline：**specialized prompt ensemble for proof verification**。\"Do We Need Frontier Models to Verify Mathematical Proofs?\" (arXiv 2604.02450, April 2026) 通过 LLM-guided prompt search + specialized prompt ensemble，使 Qwen3.5-35B 在 proof verification 上接近 frontier model 性能（提升 9.1% accuracy, 15.9% self-consistency）。这意味着仅通过更好的 prompting 就能显著缩小 LLM verification 和 formal verification 之间的差距。如果审稿人知道这个工作，会问：\"你的 Tier 1 BV 是否已经用了最优 prompt？如果用了 specialized prompt ensemble，是否还需要 Tier 2 formal verification？\"\n- 严重度: 可补救\n- 补救方案:\n  (1) 新增 baseline：**PF + BV with specialized prompt ensemble**，使用该论文的方法对 BV 进行 prompt optimization，作为 \"best-effort LLM verification\" 的 upper bound。\n  (2) 如果该 baseline 显著缩小了与 Tier 2 方案的差距，应在论文中诚实讨论：在哪些 error 类型上 specialized prompt 已经足够好，在哪些上仍需 formal verification。这反而会增强论文的说服力（\"即使用了最好的 LLM prompting，仍有 X% 的 errors 需要 formal verification 才能捕捉\"）。\n  (3) 同时检查 PF + BV ensemble 是否可以升级为使用更强的 reasoning model（如 QwQ-32B 已有，但是否考虑 R1 系列或其他更新模型作为 sensitivity check）。\n- 调研依据: \"Do We Need Frontier Models to Verify Mathematical Proofs?\" (2026) 直接在 proof verification 任务上展示了 prompt optimization 的显著提升。如果 proposal 不纳入此 baseline，审稿人很可能在 rebuttal 时要求补实验。\n\n【缺陷 4】\n- 类别: 评估方案缺陷 — Synthetic Error Detection Set 构造有效性\n- 问题: Proposal 提出从 Hard2Verify competition-level problems 构造 Synthetic Error Detection Set（\"LLM-generated incorrect proofs alongside ground-truth correct proofs, targeting 200+ error instances\"）。两个关键问题：(a) LLM-generated errors 的分布与 research-level 真实 proof errors（ArxivMathGradingBench 中的类型：subtle logical gaps, wrong theorem applications, boundary case omissions 等）可能存在系统性偏差——LLM 错误倾向于 hallucinated steps 和 computational mistakes，而非 subtle mathematical reasoning gaps；(b) \"ground-truth correct proofs\" 的正确性如何验证——如果靠 LLM 判断正确性，则引入循环依赖。\n- 严重度: 可补救\n- 补救方案:\n  (1) **多源错误生成策略**：除了 LLM-generated incorrect proofs，还应包括：(i) 对已知正确 proof 进行 controlled perturbation（删除关键步骤、替换定理引用、修改计算结果），(ii) 从 Hard2Verify 的人类标注中提取已知错误步骤。这能增加错误类型的多样性。\n  (2) **对 synthetic set 进行小规模人工验证**：随机抽样 50-80 个 instances（含 positive 和 negative），由数学研究生验证标签质量，报告 inter-annotator agreement（Cohen's κ）。\n  (3) **正确 proof 的验证**：对于 competition-level problems，使用答案匹配（correct final answer）+ 形式化验证（Lean 4 proof）双重确认，避免将有正确答案但推理过程错误的 proof 标记为 correct。\n  (4) 在论文中明确报告 synthetic set 的 **error type distribution** 并与 ArxivMathGradingBench 的 error types 做比较分析。\n- 调研依据: Hard2Verify (Pandit et al., 2025) 投入 500+ 小时 PhD-level 人工标注确保 benchmark 质量；Safe (ACL 2025) 提出 FormalStep 包含 30,809 formal statements 以确保评测规模。基于领域实验规范判断，审稿人会质疑未经验证的 synthetic benchmark 的可靠性。\n\n【缺陷 5】\n- 类别: 实验设计不足 — Platt scaling 校准数据不足\n- 问题: Proposal 使用 Platt scaling 在 \"held-out annotations\" 上校准 BV confidence scores，并注明 \"preferred over isotonic regression for small-sample robustness\"。但 ArxivMathGradingBench 仅有 ~1050 blocks（35 papers × ~30 blocks），其中 40 个 error blocks 和 ~1010 个 correct blocks，且需要留出 held-out set 用于校准。Platt scaling 虽然只有 2 个参数，但在 class imbalance 极端（~4% error rate）且样本量有限的情况下，sigmoid fit 可能 degenerate，ECE 在如此小的样本上也不可靠。此外，如果校准在 ArxivMathGradingBench 上进行，那么在同一 benchmark 上评估 calibration-dependent 的 routing 决策，存在 data leakage 或 overfitting 风险。\n- 严重度: 可补救\n- 补救方案:\n  (1) **使用 Synthetic Error Detection Set 和 miniF2F protocol 作为校准数据源**（大样本 + 已知 ground truth），ArxivMathGradingBench 仅用于最终评估（held-out test set），避免 data leakage。\n  (2) 报告 **calibration 的 cross-validation 稳定性**：在不同 random splits 的 calibration set 上拟合 Platt scaling parameters，报告参数的变异系数。\n  (3) 补充 **temperature scaling** 作为 calibration 方法的 ablation（1 个参数 vs. Platt 的 2 个参数），在小样本上可能更稳定。\n  (4) 明确区分 \"calibration split\" 和 \"evaluation split\"，写清 data flow diagram 避免审稿人质疑 data leakage。\n- 调研依据: 基于领域实验规范判断。Ganguly et al. (NeurIPS 2025) 使用 N=100 per question 来确保 UQ 信号的统计可靠性。DiscoUQ (2026) 报告 ECE 时确保了足够的评估样本。Platt scaling 在极端 class imbalance 和小样本下的 degeneracy 是已知问题（需要至少 ~50-100 positive examples for stable fit）。\n\n【缺陷 6】\n- 类别: 可行性问题 — PF 代码/数据可获得性\n- 问题: Barkallah et al. 于 2026 年 5 月 19 日发表（距今约 1 周），是整个 pipeline 的基础依赖（PF decomposition + Block Verification + ArxivMathGradingBench benchmark）。如果其代码和数据尚未开源或开源不完整，则 (a) PF decomposition 需要从论文描述重新实现——涉及 prompt engineering 和多步 LLM pipeline 的精确复现，可能耗时 2-4 周；(b) ArxivMathGradingBench 的 35 papers 和 40 errors 的具体标注需要获取；(c) Block Verification 的 prompt 和评估流程需要复现。\n- 严重度: 可补救\n- 补救方案:\n  (1) **立即确认代码/数据可获得性**：检查 arXiv 论文是否附带 GitHub 链接或 supplementary materials。如果有代码仓库，验证其完整性（是否包含 PF decomposition pipeline、BV evaluation、ArxivMathGradingBench annotations）。\n  (2) **如果代码未开源**：联系作者请求代码共享（在 academic community 中通常可行，但存在 timeline 风险）；或在 timeline 中预留 2-3 周用于从论文复现 PF decomposition 和 BV。\n  (3) **在 Resource Estimate 中增加 contingency**：如果需要复现 PF，timeline 可能从 12-16 周延长到 14-18 周。\n- 调研依据: 基于领域实验规范判断。论文发表仅 1 周，开源状态不确定是合理的 feasibility concern。\n\n【缺陷 7】\n- 类别: 实验设计不足 — Tier 2 失败率对系统 claim 的影响未量化\n- 问题: Proposal 的 core claim 是通过 selective formal verification 在 cost 和 reliability 之间取得最优 tradeoff（Pareto curve）。但这一 claim 的成立依赖于 Tier 2 的实际成功率。Proposal 将 fallback 策略列为 ablation variable（accept / reject / majority-vote），但未讨论一个关键场景：**如果 Tier 2 端到端成功率仅为 30-40%（基于 miniF2F-Lean Revisited 的 ~35% 和 StepFun-Formalizer 的 40.5% BEq@1），则大部分被路由到 Tier 2 的 blocks 将以 fallback 方式处理**。此时：(a) \"reject\" fallback 会大幅降低 recall（因为 Tier 2 失败的 blocks 中有真正错误的 blocks）；(b) \"accept\" fallback 等于放弃了 formal verification 的收益；(c) \"majority-vote re-verify\" 增加 cost 且回到 LLM-only 水平。Proposal 需要在实验设计中**显式建模 Tier 2 failure rate 对系统 Pareto 曲线的影响**。\n- 严重度: 可补救\n- 补救方案:\n  (1) 在 Ablation 中增加一个 **sensitivity analysis**：假设 Tier 2 端到端成功率分别为 30% / 50% / 70% / 90%，在每个假设下画出系统 Pareto 曲线，展示 Tier 2 成功率如何影响整体 cost-reliability tradeoff。这让审稿人在看到 Ablation 6 的实际数字前，就能理解系统在不同 Tier 2 成功率下的 robustness。\n  (2) 考虑增加 **iterative autoformalization with self-correction** 作为提升 Tier 2 成功率的策略：利用 Goedel-Prover-V2 的 self-correction 模式（从 88.1% 提升到 90.4% on MiniF2F），对 autoformalization failure 进行 Lean compiler feedback-driven retry（最多 k 次）。\n  (3) 在 cost framework 中，明确将 Tier 2 failure cases 的 fallback cost 纳入 GPU-seconds 计算（目前似乎只计了成功路径的 cost）。\n- 调研依据: Goedel-Prover-V2 (ICLR 2026) 的 self-correction 模式显示 iterative refinement 可以提升 proof search 成功率（88.1% → 90.4%）。miniF2F-Lean Revisited (NeurIPS 2025) 的 ~35% 端到端成功率为 Tier 2 可能面临的困难提供了参考下限。\n\n---\n\n**总结评估**: Proposal 的实验设计整体框架是扎实的——7 个 ablation 覆盖了核心设计选择，3 个 benchmark 覆盖了不同难度，baseline 覆盖了 cost-reliability 谱系两端，cost framework 和 statistical testing 计划也到位。以上 7 个缺陷中，没有致命的方向性问题，均可通过补充实验、增加 baseline、明确数据流和做 pilot study 来修复。**最关键的两个缺陷是 #1（统计功效）和 #2（block-level autoformalization 可行性）**——前者决定了实验结果能否令审稿人信服，后者决定了整个 Tier 2 是否 work。建议优先做缺陷 #2 的 pilot study 和缺陷 #6 的代码可获得性确认，这两项是项目 go/no-go 的关键前置信息。\n\nSources:\n- [Safe: Enhancing Mathematical Reasoning via Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)\n- [Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., 2026)](https://arxiv.org/abs/2605.20531)\n- [ThinkPRM: Process Reward Models That Think (2025)](https://arxiv.org/abs/2504.16828)\n- [Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025)](https://arxiv.org/abs/2505.20047)\n- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)\n- [StepFun-Formalizer (AAAI 2026)](https://arxiv.org/pdf/2508.04440)\n- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)\n- [HERMES (Ospanov et al., ICML 2026)](https://arxiv.org/abs/2511.18760)\n- [Do We Need Frontier Models to Verify Mathematical Proofs? (2026)](https://arxiv.org/abs/2604.02450)\n- [Hard2Verify (Pandit et al., 2025)](https://arxiv.org/abs/2510.13744)\n- [DiscoUQ: Structured Disagreement Analysis (2026)](https://arxiv.org/pdf/2603.20975)"
}
```

---

### Runtime record

_source line 38 · 2026-05-27T12:53:53.876Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T12:53:53.876Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

## Round 3

21 recorded events

### User

_source line 39 · 2026-05-27T12:53:53.906Z_

【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have a comprehensive picture of the research landscape. Let me compile my assessment.

---

【状态】: 有发掘空间

【前置调研发现】

- **[Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)** (arXiv, May 2026): The foundational paper. Decomposes proofs into self-contained modules with explicit premises, conclusions, and dependencies; verifies via LLM only. Achieves Pareto-dominance over LLM-as-judge but leaves ~50% of research-level errors undetected. Critically, the paper itself does *not* explore its modular structure as a formalization target — this is genuinely an untapped direction.

- **[Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047)** (NeurIPS 2025): The closest conceptual precedent for "uncertainty → selective formal verification." Models LLM-generated SMT-LIB program distributions with PCFGs, achieves 14-100% error reduction with minimal abstention. **Key difference from this proposal**: operates on structured formal artifacts (SMT-LIB programs), not natural language math proofs; no modular decomposition layer; no dependency-based routing signal. The proposal's novelty relative to this work hinges on (a) the PF intermediary layer and (b) the dual-signal routing design.

- **[ProofFlow](https://arxiv.org/abs/2510.15981)** (arXiv 2025): Constructs DAGs to map logical dependencies between proof steps for faithful autoformalization. Achieves ProofScore of 0.545 vs. baselines at 0.072-0.123. **Uses dependency graphs for autoformalization fidelity but not for verification routing decisions.** This is the paper that comes closest to combining dependency awareness with formalization, but the routing dimension is completely absent.

- **[miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108)** (NeurIPS 2025): Reveals that end-to-end autoformalization + theorem proving achieves only ~36% success rate; autoformalization accuracy is ~66% (human-judged) vs. inflated 97% (LLM-judged). The paper attributes much of the failure to context-completion difficulties and benchmark quality. **This directly supports the proposal's thesis that self-contained PF blocks should be better autoformalization targets by eliminating context-completion.**

- **[Solve-Detect-Verify / FlexiVe](https://arxiv.org/abs/2505.11966)** (arXiv 2025): Adaptive verification budget between fast/slow thinking for generative verifiers. Conceptually parallel (selective allocation of verification compute) but operates within LLM-tier verification (generative reward models), not across the LLM-to-formal verification boundary. No structural decomposition.

- **[UCCI](https://arxiv.org/abs/2605.18796)** (arXiv 2026): Calibrated uncertainty (isotonic regression) for cost-optimal LLM cascade routing. Cuts inference cost by 31% at maintained quality. **Operates on model cascades (small→large LLM) rather than formal/informal verification tiers.** The calibration methodology is relevant, but the routing target is fundamentally different.

- **[Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)** (2024/2025): Step-level formalization with Lean 4 compiler feedback loops and process-supervised verifier. **Relevant as evidence that step-level (rather than whole-proof) autoformalization is more tractable**, which supports the proposal's block-level approach. However, their "steps" come from the formalization process itself, not from a pre-existing modular decomposition like PF.

- **调研总结**: The field is converging on two key insights: (1) whole-proof autoformalization is fundamentally limited (~36% end-to-end), driving interest in modular/step-level approaches; (2) selective allocation of expensive verification is an emerging paradigm (Ganguly for SMT, FlexiVe for GenRM, UCCI for model cascades), but **no one has yet combined a structured modular decomposition with uncertainty-guided routing to a formal verification tier for NL math proofs**. The proposal sits at a genuine gap in the literature.

---

【发掘点 1】
- 维度: significance 提升 / 核心 claim 强化
- 内容: 当前 proposal 的 significance framing 是 "cost-efficient verification"（在 cost-reliability spectrum 找到中间地带）。这虽然正确，但天花板不够高。调研发现 miniF2F-Lean Revisited 的核心结论是：whole-proof autoformalization 受 context-completion problem 制约，end-to-end 成功率仅 ~36%，这是一个 **fundamental architectural limitation**，不是简单的工程问题——随着模型变强，whole-proof autoformalization 的瓶颈（context dependency compounding）不会自动消失。Proposal 应当将 significance 提升到这一层：**PF-based selective formalization 不仅仅是"省钱"，而是可能是唯一能让 formal verification 扩展到 research-level proofs 的可行架构**。因为 research-level proofs 太长、太复杂，whole-proof autoformalization 在可预见的未来无法处理；而 PF 的 self-contained block structure 通过消除 context-completion 问题，从根本上改变了 autoformalization 的可行性边界。这把 contribution 从"一个 cost-saving 工程优化"提升到"解决 formal verification scalability 的 architectural insight"。
- 价值: 直接提升 Significance 维度。审稿人看到"cost-efficient"会想"incremental engineering"；看到"the only viable path to formal verification of complex proofs"会想"architectural contribution"。
- 调研依据: miniF2F-Lean Revisited (NeurIPS 2025) 揭示的 whole-proof autoformalization ~36% 成功率上限，以及 Process-Driven Autoformalization 证明 step-level formalization 更 tractable 的实证。

【发掘点 2】
- 维度: novelty 锐化 / related work 差异化
- 内容: Proposal 当前与 Ganguly et al. (NeurIPS 2025) 的差异化描述不够锐利。表面差异是"SMT vs NL proofs"和"有无 PF intermediary"，但这容易被审稿人解读为"same idea, different domain"。真正的核心差异需要更 sharp 地表达：Ganguly 的 uncertainty signal 来自 **生成端** (LLM 生成 SMT-LIB program 的 distribution)，routing target 是 **同质的** (都是 SMT solver verification，只是选择是否 verify)。而本 proposal 的 uncertainty signal 来自 **验证端** (BV 对 block 正确性的判断 uncertainty)，routing target 是 **异质的** (从 LLM verification 路由到 formal verification，是两种根本不同的验证 paradigm)。更重要的是，Ganguly 没有 **structural routing signal**——他们的 selective verification 完全基于 output uncertainty，而本 proposal 的 dual-signal design 引入了 dependency criticality 这个与 uncertainty 正交的 routing dimension。这是一个 genuinely novel contribution，不只是 domain transfer。建议在 related work 差异化中明确强调这三个层次的区别：(1) uncertainty source (生成端 vs 验证端), (2) routing target heterogeneity (同质 vs 异质 verification paradigm), (3) structural criticality dimension (absent in Ganguly)。
- 价值: Novelty + Related Work 差异化。防止审稿人把本工作简单归类为"Ganguly et al. applied to NL proofs"。
- 调研依据: 直接对比 Ganguly et al. (NeurIPS 2025) 的方法设计——其 PCFG-based uncertainty modeling 完全在生成端操作，无 inter-step dependency 概念。

【发掘点 3】
- 维度: trivial alternative 威胁
- 内容: Proposal 需要明确防御一个 trivial alternative：**简单启发式 routing 是否已经足够好？** 具体而言，如果用 block-internal reasoning step count、cited theorems 数量、或 block 文本长度等 simple features 作为 routing signal，是否能达到与 calibrated uncertainty 相近的效果？Proposal 已经在 Tier 2 描述中提到了 "structural difficulty heuristic"作为额外 routing feature，但这反而暴露了问题：如果 simple heuristic 本身就有效，那 ensemble disagreement + CoT entropy 的增量价值是什么？建议：(a) 在 ablation 中显式加入 "simple heuristic only" 作为 routing baseline（block length, step count, cited theorem count），(b) 在 claim 层面明确论证 why calibrated uncertainty should capture errors that structural heuristics miss（例如：结构简单但 reasoning subtle 的 block，heuristic 会 miss 但 BV ensemble disagreement 会 flag）。这不是要加实验（那是补救 agent 的事），而是要在 idea 层面把 claim 说圆：calibrated uncertainty 的增量价值到底在哪里。
- 价值: 加固 Novelty claim。如果 simple heuristic 足够好，这个 idea 的核心技术贡献（calibrated uncertainty + dual signal）就被 undermine 了。
- 调研依据: 基于领域整体趋势判断——UCCI (2026) 和 Ganguly (2025) 都在强调 calibrated uncertainty 相对于 naive confidence 的优势，但两者都没有与 simple structural heuristics 做过 head-to-head 比较。

【发掘点 4】
- 维度: 核心 claim 强化 / 前提假设质疑
- 内容: "Dependency criticality" 目前仅用 fan-out degree 来度量。这个定义虽然直觉合理（高 fan-out block 的错误传播到更多下游 block），但存在两个盲区：(1) **"bottleneck" block**——fan-out 不高但处于依赖链的唯一路径上，其错误会导致所有下游 block 的前提失效。图论中的 "dominator node" 概念更准确地捕捉了这种 criticality。(2) **距离 final conclusion 的 proximity**——直接支撑 main theorem 的 block，即使 fan-out 为 1，其错误也是致命的。建议将 dependency criticality 从单一的 fan-out degree 扩展为更丰富的 graph-theoretic measure：dominator analysis (dominator tree 中的 immediate dominator 节点) + topological centrality (PageRank 或 betweenness centrality on the dependency DAG)。这不改变方法论的核心架构，但锐化了 "structural criticality" 这个 contribution 的技术深度，让审稿人看到这不是一个 ad-hoc heuristic 而是有图论 grounding 的 principled design。
- 价值: 直接提升 Novelty 维度。把 dependency criticality 从一个 simple heuristic (fan-out) 提升为一个 principled graph-theoretic framework，增加了技术贡献的 depth。
- 调研依据: ProofFlow (2025) 使用 DAG 做 autoformalization fidelity 但未探索 graph-theoretic criticality measures for routing; Ganguly et al. 完全没有 structural routing signal。这个方向在当前文献中是空白的。

【发掘点 5】
- 维度: significance 提升
- 内容: Proposal 当前的 evaluation 以 error detection (precision/recall/F1) 为核心 metric。但如果把 significance 提升到"making formal verification scalable for real mathematical research"这个层面（见发掘点 1），那么一个更有影响力的 metric 是 **autoformalization tractability gain**：即 PF block-level autoformalization 相比 whole-proof / raw-NL-fragment autoformalization，在 Lean 4 type-check rate 和 proof search success rate 上的提升倍数。Proposal 的 ablation 6 已经包含了这个比较，但目前只是作为 ablation 之一。建议将其提升为 **core result** 而非 ablation：如果 PF blocks 能将 autoformalization success rate 从 ~35% (whole-proof baseline, miniF2F-Lean Revisited) 显著提升到例如 60%+，这本身就是一个 standalone contribution-level finding，直接回答了"why modular decomposition matters for formal verification"这个 open question。把它埋在 ablation 里是低估了它的价值。
- 价值: 提升 Significance。把一个 ablation-level 的验证提升为 contribution-level 的 finding，让论文同时在 verification pipeline design 和 autoformalization methodology 两个维度有贡献。
- 调研依据: miniF2F-Lean Revisited (NeurIPS 2025) 确立了 whole-proof autoformalization ~36% 的 baseline；Process-Driven Autoformalization 证明 step-level approaches 更 tractable。如果 PF block-level 能显著超越这些 baselines，这是一个对领域有重要价值的 empirical finding。

Sources:
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)
- [Safe: Enhancing Mathematical Reasoning via Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/)
- [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047)
- [ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization](https://arxiv.org/abs/2510.15981)
- [miniF2F-Lean Revisited](https://arxiv.org/abs/2511.03108)
- [Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier](https://arxiv.org/abs/2505.11966)
- [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/abs/2605.18796)
- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)
- [HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs](https://arxiv.org/abs/2511.18760)
- [Adaptive Test-Time Compute Allocation](https://arxiv.org/pdf/2602.03975)

【补救 agent 本轮输出】:
Now I have comprehensive context. Let me synthesize my findings and produce the formal evaluation.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **Safe (Liu et al., ACL 2025)**: 提出 FormalStep benchmark（30,809 formal statements），逐步 Lean 4 形式化验证，将 retrospective formal scores 与 PRM 分数集成。实验覆盖多个 LLM 和数学数据集。Baselines 包括多种 PRM 和 LLM-as-judge 方法。
- **Pseudo-Formalization (Barkallah et al., arXiv 2605.20531, May 2026)**: Block Verification 在 ArxivMathGradingBench（35 papers, 40 known errors）和奥赛数学上 Pareto-dominate LLM-as-judge baselines。数据集极小。
- **ThinkPRM (arXiv 2504.16828, 2025; submitted ICLR 2026)**: 在 ProcessBench, MATH-500, AIME'24, GPQA-Diamond, LiveCodeBench 上评估。使用 R1-Distill-Qwen{1.5B,7B,14B} 和 QwQ-32B-Preview 四个变体。Ablation 包括训练数据量、模型规模。
- **Ganguly et al. "Grammars of Formal Uncertainty" (NeurIPS 2025)**: SMT-based selective verification，使用 N=5 for baselines, N=100 for UQ analysis。AUROC>0.93 on grammar entropy。Selective verification 实现 14-100% error reduction。
- **Goedel-Prover-V2 (ICLR 2026)**: SOTA open-source ATP, pass@32 在 MiniF2F 达 88.1%（self-correction 模式 90.4%），PutnamBench 解决 86 题。
- **StepFun-Formalizer-32B (AAAI 2026)**: Statement autoformalization 的 BEq@1 为 40.5% (FormalMATH-Lite) / 26.7% (ProverBench)。注意：这是 statement-level 性能，不是 block-level proof step formalization。
- **miniF2F-Lean Revisited (NeurIPS 2025)**: 揭示 autoformalization accuracy 在人类评估下仅 ~66%（LLM 评估报告 97%），端到端 ~35%。
- **"Do We Need Frontier Models to Verify Mathematical Proofs?" (arXiv 2604.02450, 2026)**: 通过 LLM-guided prompt search + specialized prompt ensemble，使小模型 (Qwen3.5-35B) 在 proof verification accuracy 上接近 frontier models（提升 9.1% accuracy, 15.9% self-consistency）。直接相关但 proposal 未涉及。
- **DiscoUQ (2026)**: 结构化 ensemble disagreement 分析，AUROC 0.802, ECE 0.036，显著优于 baseline。提示 ensemble disagreement 的具体实现方式对校准质量影响很大。
- 调研总结：该领域当前实验标准要求 (a) 在多个难度层级的 benchmark 上评估（competition-level + research-level）, (b) 与最新 PRM/verbalized verifier 作对比, (c) 明确的 compute-normalized Pareto 分析, (d) 至少包括 autoformalization success rate 的独立报告。审稿人普遍关注统计显著性（尤其在小数据集上）、autoformalization 各环节的成功率分解报告、以及 LLM-only 强基线是否被充分探索。

---

【缺陷 1】
- 类别: 评估方案缺陷 — 统计功效不足
- 问题: ArxivMathGradingBench 仅含 35 papers / 40 known errors，作为 primary research-level evaluation，bootstrap CI（1000 resamples）在 n=40 上置信区间会非常宽，McNemar's test 在样本量如此小时 power 极低。Proposal 声称的方法改进（例如从 ~50% recall 提升到 ~70%）在 40 个 error 上意味着仅多检测到 ~8 个错误，随机波动就可能解释这一差异。这是审稿人最可能质疑的点之一——"你在 40 个 error 上的改进有统计意义吗？"
- 严重度: 可补救
- 补救方案: 
  (1) **明确将 Synthetic Error Detection Set 提升为 co-primary benchmark**（而非辅助），并将其目标从 "200+ instances" 提高到 **400-500 instances**，跨越多个错误类型（logical gap, computational error, incorrect theorem citation, unjustified step 等）。在 400+ 样本上，McNemar's test 和 bootstrap CI 才有足够 power 检测 5-10% 的绝对改进。
  (2) 在 ArxivMathGradingBench 上，**补充 per-paper accuracy（proof-level correctness detection）** 作为辅助指标，增加统计单元数量（从 40 errors 扩展到 35 papers × {correct/incorrect} classification）。
  (3) 明确报告 effect size（Cohen's h 或 odds ratio）而不仅仅是 p-value，让审稿人评估实际影响大小。
  (4) 在 miniF2F Verification Protocol 上确保足够的候选 proof 数量（建议每题生成 ≥8 候选，覆盖 ≥100 题），使该 benchmark 也具备独立的统计可信度。
- 调研依据: Ganguly et al. (NeurIPS 2025) 在 selective verification 中使用 N=100 samples per question 以确保统计意义；Hard2Verify 投入 500+ 小时人工标注确保 benchmark 规模。ArxivMathGradingBench 的 40 errors 远低于该领域评估标准。

【缺陷 2】
- 类别: 可行性问题 — Block-level autoformalization 成功率未知
- 问题: Proposal 的核心架构假设是 PF block 的结构（explicit premises → Lean hypotheses, conclusion → Lean goal）能显著提升 autoformalization 成功率，从而使 Tier 2 selective formal verification 可行。但 StepFun-Formalizer-32B 在 statement-level autoformalization 上的 BEq@1 仅为 40.5% (FormalMATH-Lite) / 26.7% (ProverBench)。PF blocks 不仅需要 statement formalization（premises 和 conclusion），还需要 Goedel-Prover-V2 证明 conclusion follows from premises——这是 theorem proving，不是单纯 statement translation。如果 block-level autoformalization + proof search 的端到端成功率低于 40-50%，则 Tier 2 在超过一半被路由的 blocks 上会失败，极大削弱系统可靠性。Ablation 6 虽然测试了这一点，但如果结果太差，整个 pipeline 的核心 claim 就无法成立。
- 严重度: 可补救（但需要前置验证）
- 补救方案:
  (1) **在全面实验前做 pilot study**：随机抽取 50-100 PF blocks（涵盖不同数学领域和难度），分别测试 StepFun-Formalizer 的 formalization 成功率和 Goedel-Prover-V2 的 proof search 成功率，建立 block-level 端到端成功率的 baseline 估计。如果端到端成功率 < 30%，需要重新评估 Tier 2 的可行性或引入更强的 autoformalization 策略（如 multi-shot formalization with self-correction）。
  (2) 在实验中**分解报告 Tier 2 各环节成功率**：formalization type-check rate → proof search success rate → end-to-end verification success rate，让审稿人理解瓶颈在哪里。
  (3) 讨论 **fallback 策略对 headline 数字的影响**：当 Tier 2 失败时，accept/reject/majority-vote 的选择会直接影响 precision 和 recall。Proposal 将其列为 ablation variable 是对的，但应该在 expected results 中明确讨论"如果 Tier 2 成功率仅为 X%，各 fallback 策略下的系统性能预期"。
- 调研依据: miniF2F-Lean Revisited (NeurIPS 2025) 明确显示 autoformalization 端到端成功率在人类评估下仅 ~35%（66% formalization × ~53% proving），且这是在 competition-level 标准化问题上。Research-level PF blocks 的难度更高，成功率可能更低。StepFun-Formalizer (AAAI 2026) 的 BEq@1 40.5% 也仅是 statement-level。

【缺陷 3】
- 类别: baseline 不足或过时 — 缺少"强 LLM verification"基线
- 问题: Proposal 的 baselines 在 LLM-only 一端包括 PF+BV single-pass、PF+BV ensemble、ThinkPRM、Qwen2.5-Math-PRM-7B，但遗漏了一个关键的最新 baseline：**specialized prompt ensemble for proof verification**。"Do We Need Frontier Models to Verify Mathematical Proofs?" (arXiv 2604.02450, April 2026) 通过 LLM-guided prompt search + specialized prompt ensemble，使 Qwen3.5-35B 在 proof verification 上接近 frontier model 性能（提升 9.1% accuracy, 15.9% self-consistency）。这意味着仅通过更好的 prompting 就能显著缩小 LLM verification 和 formal verification 之间的差距。如果审稿人知道这个工作，会问："你的 Tier 1 BV 是否已经用了最优 prompt？如果用了 specialized prompt ensemble，是否还需要 Tier 2 formal verification？"
- 严重度: 可补救
- 补救方案:
  (1) 新增 baseline：**PF + BV with specialized prompt ensemble**，使用该论文的方法对 BV 进行 prompt optimization，作为 "best-effort LLM verification" 的 upper bound。
  (2) 如果该 baseline 显著缩小了与 Tier 2 方案的差距，应在论文中诚实讨论：在哪些 error 类型上 specialized prompt 已经足够好，在哪些上仍需 formal verification。这反而会增强论文的说服力（"即使用了最好的 LLM prompting，仍有 X% 的 errors 需要 formal verification 才能捕捉"）。
  (3) 同时检查 PF + BV ensemble 是否可以升级为使用更强的 reasoning model（如 QwQ-32B 已有，但是否考虑 R1 系列或其他更新模型作为 sensitivity check）。
- 调研依据: "Do We Need Frontier Models to Verify Mathematical Proofs?" (2026) 直接在 proof verification 任务上展示了 prompt optimization 的显著提升。如果 proposal 不纳入此 baseline，审稿人很可能在 rebuttal 时要求补实验。

【缺陷 4】
- 类别: 评估方案缺陷 — Synthetic Error Detection Set 构造有效性
- 问题: Proposal 提出从 Hard2Verify competition-level problems 构造 Synthetic Error Detection Set（"LLM-generated incorrect proofs alongside ground-truth correct proofs, targeting 200+ error instances"）。两个关键问题：(a) LLM-generated errors 的分布与 research-level 真实 proof errors（ArxivMathGradingBench 中的类型：subtle logical gaps, wrong theorem applications, boundary case omissions 等）可能存在系统性偏差——LLM 错误倾向于 hallucinated steps 和 computational mistakes，而非 subtle mathematical reasoning gaps；(b) "ground-truth correct proofs" 的正确性如何验证——如果靠 LLM 判断正确性，则引入循环依赖。
- 严重度: 可补救
- 补救方案:
  (1) **多源错误生成策略**：除了 LLM-generated incorrect proofs，还应包括：(i) 对已知正确 proof 进行 controlled perturbation（删除关键步骤、替换定理引用、修改计算结果），(ii) 从 Hard2Verify 的人类标注中提取已知错误步骤。这能增加错误类型的多样性。
  (2) **对 synthetic set 进行小规模人工验证**：随机抽样 50-80 个 instances（含 positive 和 negative），由数学研究生验证标签质量，报告 inter-annotator agreement（Cohen's κ）。
  (3) **正确 proof 的验证**：对于 competition-level problems，使用答案匹配（correct final answer）+ 形式化验证（Lean 4 proof）双重确认，避免将有正确答案但推理过程错误的 proof 标记为 correct。
  (4) 在论文中明确报告 synthetic set 的 **error type distribution** 并与 ArxivMathGradingBench 的 error types 做比较分析。
- 调研依据: Hard2Verify (Pandit et al., 2025) 投入 500+ 小时 PhD-level 人工标注确保 benchmark 质量；Safe (ACL 2025) 提出 FormalStep 包含 30,809 formal statements 以确保评测规模。基于领域实验规范判断，审稿人会质疑未经验证的 synthetic benchmark 的可靠性。

【缺陷 5】
- 类别: 实验设计不足 — Platt scaling 校准数据不足
- 问题: Proposal 使用 Platt scaling 在 "held-out annotations" 上校准 BV confidence scores，并注明 "preferred over isotonic regression for small-sample robustness"。但 ArxivMathGradingBench 仅有 ~1050 blocks（35 papers × ~30 blocks），其中 40 个 error blocks 和 ~1010 个 correct blocks，且需要留出 held-out set 用于校准。Platt scaling 虽然只有 2 个参数，但在 class imbalance 极端（~4% error rate）且样本量有限的情况下，sigmoid fit 可能 degenerate，ECE 在如此小的样本上也不可靠。此外，如果校准在 ArxivMathGradingBench 上进行，那么在同一 benchmark 上评估 calibration-dependent 的 routing 决策，存在 data leakage 或 overfitting 风险。
- 严重度: 可补救
- 补救方案:
  (1) **使用 Synthetic Error Detection Set 和 miniF2F protocol 作为校准数据源**（大样本 + 已知 ground truth），ArxivMathGradingBench 仅用于最终评估（held-out test set），避免 data leakage。
  (2) 报告 **calibration 的 cross-validation 稳定性**：在不同 random splits 的 calibration set 上拟合 Platt scaling parameters，报告参数的变异系数。
  (3) 补充 **temperature scaling** 作为 calibration 方法的 ablation（1 个参数 vs. Platt 的 2 个参数），在小样本上可能更稳定。
  (4) 明确区分 "calibration split" 和 "evaluation split"，写清 data flow diagram 避免审稿人质疑 data leakage。
- 调研依据: 基于领域实验规范判断。Ganguly et al. (NeurIPS 2025) 使用 N=100 per question 来确保 UQ 信号的统计可靠性。DiscoUQ (2026) 报告 ECE 时确保了足够的评估样本。Platt scaling 在极端 class imbalance 和小样本下的 degeneracy 是已知问题（需要至少 ~50-100 positive examples for stable fit）。

【缺陷 6】
- 类别: 可行性问题 — PF 代码/数据可获得性
- 问题: Barkallah et al. 于 2026 年 5 月 19 日发表（距今约 1 周），是整个 pipeline 的基础依赖（PF decomposition + Block Verification + ArxivMathGradingBench benchmark）。如果其代码和数据尚未开源或开源不完整，则 (a) PF decomposition 需要从论文描述重新实现——涉及 prompt engineering 和多步 LLM pipeline 的精确复现，可能耗时 2-4 周；(b) ArxivMathGradingBench 的 35 papers 和 40 errors 的具体标注需要获取；(c) Block Verification 的 prompt 和评估流程需要复现。
- 严重度: 可补救
- 补救方案:
  (1) **立即确认代码/数据可获得性**：检查 arXiv 论文是否附带 GitHub 链接或 supplementary materials。如果有代码仓库，验证其完整性（是否包含 PF decomposition pipeline、BV evaluation、ArxivMathGradingBench annotations）。
  (2) **如果代码未开源**：联系作者请求代码共享（在 academic community 中通常可行，但存在 timeline 风险）；或在 timeline 中预留 2-3 周用于从论文复现 PF decomposition 和 BV。
  (3) **在 Resource Estimate 中增加 contingency**：如果需要复现 PF，timeline 可能从 12-16 周延长到 14-18 周。
- 调研依据: 基于领域实验规范判断。论文发表仅 1 周，开源状态不确定是合理的 feasibility concern。

【缺陷 7】
- 类别: 实验设计不足 — Tier 2 失败率对系统 claim 的影响未量化
- 问题: Proposal 的 core claim 是通过 selective formal verification 在 cost 和 reliability 之间取得最优 tradeoff（Pareto curve）。但这一 claim 的成立依赖于 Tier 2 的实际成功率。Proposal 将 fallback 策略列为 ablation variable（accept / reject / majority-vote），但未讨论一个关键场景：**如果 Tier 2 端到端成功率仅为 30-40%（基于 miniF2F-Lean Revisited 的 ~35% 和 StepFun-Formalizer 的 40.5% BEq@1），则大部分被路由到 Tier 2 的 blocks 将以 fallback 方式处理**。此时：(a) "reject" fallback 会大幅降低 recall（因为 Tier 2 失败的 blocks 中有真正错误的 blocks）；(b) "accept" fallback 等于放弃了 formal verification 的收益；(c) "majority-vote re-verify" 增加 cost 且回到 LLM-only 水平。Proposal 需要在实验设计中**显式建模 Tier 2 failure rate 对系统 Pareto 曲线的影响**。
- 严重度: 可补救
- 补救方案:
  (1) 在 Ablation 中增加一个 **sensitivity analysis**：假设 Tier 2 端到端成功率分别为 30% / 50% / 70% / 90%，在每个假设下画出系统 Pareto 曲线，展示 Tier 2 成功率如何影响整体 cost-reliability tradeoff。这让审稿人在看到 Ablation 6 的实际数字前，就能理解系统在不同 Tier 2 成功率下的 robustness。
  (2) 考虑增加 **iterative autoformalization with self-correction** 作为提升 Tier 2 成功率的策略：利用 Goedel-Prover-V2 的 self-correction 模式（从 88.1% 提升到 90.4% on MiniF2F），对 autoformalization failure 进行 Lean compiler feedback-driven retry（最多 k 次）。
  (3) 在 cost framework 中，明确将 Tier 2 failure cases 的 fallback cost 纳入 GPU-seconds 计算（目前似乎只计了成功路径的 cost）。
- 调研依据: Goedel-Prover-V2 (ICLR 2026) 的 self-correction 模式显示 iterative refinement 可以提升 proof search 成功率（88.1% → 90.4%）。miniF2F-Lean Revisited (NeurIPS 2025) 的 ~35% 端到端成功率为 Tier 2 可能面临的困难提供了参考下限。

---

**总结评估**: Proposal 的实验设计整体框架是扎实的——7 个 ablation 覆盖了核心设计选择，3 个 benchmark 覆盖了不同难度，baseline 覆盖了 cost-reliability 谱系两端，cost framework 和 statistical testing 计划也到位。以上 7 个缺陷中，没有致命的方向性问题，均可通过补充实验、增加 baseline、明确数据流和做 pilot study 来修复。**最关键的两个缺陷是 #1（统计功效）和 #2（block-level autoformalization 可行性）**——前者决定了实验结果能否令审稿人信服，后者决定了整个 Tier 2 是否 work。建议优先做缺陷 #2 的 pilot study 和缺陷 #6 的代码可获得性确认，这两项是项目 go/no-go 的关键前置信息。

Sources:
- [Safe: Enhancing Mathematical Reasoning via Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)
- [Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., 2026)](https://arxiv.org/abs/2605.20531)
- [ThinkPRM: Process Reward Models That Think (2025)](https://arxiv.org/abs/2504.16828)
- [Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025)](https://arxiv.org/abs/2505.20047)
- [Goedel-Prover-V2 (ICLR 2026)](https://arxiv.org/abs/2508.03613)
- [StepFun-Formalizer (AAAI 2026)](https://arxiv.org/pdf/2508.04440)
- [miniF2F-Lean Revisited (NeurIPS 2025)](https://arxiv.org/abs/2511.03108)
- [HERMES (Ospanov et al., ICML 2026)](https://arxiv.org/abs/2511.18760)
- [Do We Need Frontier Models to Verify Mathematical Proofs? (2026)](https://arxiv.org/abs/2604.02450)
- [Hard2Verify (Pandit et al., 2025)](https://arxiv.org/abs/2510.13744)
- [DiscoUQ: Structured Disagreement Analysis (2026)](https://arxiv.org/pdf/2603.20975)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "873cc2d7-ef34-4481-8042-9b55721ce7d2",
  "isSidechain": false,
  "promptId": "dd8c3ab0-46d7-4386-bd02-fb2287bbce2a",
  "type": "user",
  "uuid": "06443321-862f-4577-9d4d-c0d8412769c4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 40_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have a comprehensive picture of the research landscape. Let me compile my assessment.  ---  【状态】: 有发掘…",
  "leafUuid": "06443321-862f-4577-9d4d-c0d8412769c4",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Assistant

_source line 42 · 2026-05-27T12:54:19.847Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze both worker outputs for Round 2 and plan my cross-validation searches.

**发掘 agent Round 2 (5 points):**

1. **Significance升级**: 从"cost-efficient verification"提升到"PF-based selective formalization可能是唯一能让formal verification扩展到research-level proofs的可行架构"——因为whole-proof autoformalization的~36%上限是fundamental architectural limitation。
2. **Ganguly差异化锐化**: 三层差异——(1) uncertainty source (生成端 vs 验证端), (2) routing target heterogeneity (同质 vs 异质), (3) structural criticality dimension。


3. **Trivial alternative威胁**: 简单启发式routing是否已够好？需要在claim层面论证calibrated uncertainty的增量价值。
4. **Dependency criticality深化**: 从fan-out degree扩展到graph-theoretic measures (dominator analysis + betweenness centrality)。
5. **Ablation 6提升为core result**: PF block vs whole-proof autoformalization success rate应该是contribution-level finding，不只是ablation。

**补救 agent Round 2 (7 defects):**

Now I'm looking at the statistical power issues with the synthetic set and what needs to be addressed there.

I need to validate block-level autoformalization end-to-end, which is a core risk that requires pilot testing. There's also a gap in not comparing against stronger LLM verification baselines with specialized prompt ensembles. The synthetic set construction needs multiple error sources and human validation, and I should use it for Platt scaling calibration rather than relying on limited calibration data. The PF paper's recent publication makes its code and data availability uncertain, and I haven't done sensitivity analysis on Tier 2 failure rates yet.

Now I'm thinking through which searches would be most valuable to validate my approach. The "Do We Need Frontier Models to Verify Mathematical Proofs?" paper is a concrete baseline claim I should verify exists and assess for relevance. I'm also considering whether there's prior work on dominator analysis or betweenness centrality applied to proof dependency graphs, and whether there's evidence for step-level formalization in Lean 4. I'll proceed with those searches to validate the key claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06443321-862f-4577-9d4d-c0d8412769c4",
  "isSidechain": false,
  "requestId": "req_011CbT7AgqfpEiNucxAY1x2x",
  "type": "assistant",
  "uuid": "f5138998-e41c-4427-8f52-4f5e4b369bf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SeCwfUxJCSeKtar89rDE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21768,
      "cache_read_input_tokens": 35974,
      "output_tokens": 1219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1219,
          "cache_read_input_tokens": 35974,
          "cache_creation_input_tokens": 21768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21768
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

_source line 43 · 2026-05-27T12:54:19.849Z_

我需要对第 2 轮 worker 的关键建议做交叉验证。启动 3 个并行搜索：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5138998-e41c-4427-8f52-4f5e4b369bf1",
  "isSidechain": false,
  "requestId": "req_011CbT7AgqfpEiNucxAY1x2x",
  "type": "assistant",
  "uuid": "c09b6b94-8ab0-47f9-9b22-82bd1c7633f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SeCwfUxJCSeKtar89rDE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21768,
      "cache_read_input_tokens": 35974,
      "output_tokens": 1219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1219,
          "cache_read_input_tokens": 35974,
          "cache_creation_input_tokens": 21768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21768
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

_source line 44 · 2026-05-27T12:54:20.632Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DkDrpu4kn3NhLFPMCaHBst`</summary>

```json
{
  "query": "\"Do We Need Frontier Models to Verify Mathematical Proofs\" arXiv 2604.02450 2026 prompt ensemble verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c09b6b94-8ab0-47f9-9b22-82bd1c7633f5",
  "isSidechain": false,
  "requestId": "req_011CbT7AgqfpEiNucxAY1x2x",
  "type": "assistant",
  "uuid": "afee5c21-dbd9-4ab6-86c0-5b09867e0858",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SeCwfUxJCSeKtar89rDE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21768,
      "cache_read_input_tokens": 35974,
      "output_tokens": 1219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1219,
          "cache_read_input_tokens": 35974,
          "cache_creation_input_tokens": 21768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21768
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

_source line 45 · 2026-05-27T12:54:21.171Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013cmUv1sLocsZo1xCszZSS1`</summary>

```json
{
  "query": "Pseudo-Formalization automatic proof verification code github Barkallah 2026 open source"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afee5c21-dbd9-4ab6-86c0-5b09867e0858",
  "isSidechain": false,
  "requestId": "req_011CbT7AgqfpEiNucxAY1x2x",
  "type": "assistant",
  "uuid": "b6592d66-5c5f-46cf-8288-66a679b56d29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SeCwfUxJCSeKtar89rDE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21768,
      "cache_read_input_tokens": 35974,
      "output_tokens": 1219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1219,
          "cache_read_input_tokens": 35974,
          "cache_creation_input_tokens": 21768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21768
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

_source line 46 · 2026-05-27T12:54:21.567Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VdHCMBttVJfFvie3qoVzEP`</summary>

```json
{
  "query": "dominator analysis dependency graph proof verification criticality routing formal methods 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6592d66-5c5f-46cf-8288-66a679b56d29",
  "isSidechain": false,
  "requestId": "req_011CbT7AgqfpEiNucxAY1x2x",
  "type": "assistant",
  "uuid": "3be5b200-921b-4743-bd39-3c6e6b39eaee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018SeCwfUxJCSeKtar89rDE8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21768,
      "cache_read_input_tokens": 35974,
      "output_tokens": 1219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1219,
          "cache_read_input_tokens": 35974,
          "cache_creation_input_tokens": 21768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21768
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

_source line 47 · 2026-05-27T12:54:26.223Z_

<details><summary>↩ Tool result · `toolu_01DkDrpu4kn3NhLFPMCaHBst`</summary>

```text
Web search results for query: ""Do We Need Frontier Models to Verify Mathematical Proofs" arXiv 2604.02450 2026 prompt ensemble verification"

Links: [{"title":"[2604.02450] Do We Need Frontier Models to Verify Mathematical Proofs?","url":"https://arxiv.org/abs/2604.02450"},{"title":"[2604.02450v1] Do We Need Frontier Models to Verify Mathematical Proofs?","url":"https://arxiv.org/abs/2604.02450v1"},{"title":"Do We Need Frontier Models to Verify Mathematical Proofs?","url":"https://arxiv.org/html/2604.02450v1"},{"title":"Do We Need Frontier Models to Verify Mathematical Proofs?","url":"https://arxiv.org/pdf/2604.02450"},{"title":"Automated Conjecture Resolution with Formal Verification","url":"https://arxiv.org/html/2604.03789v1"}]

I found the paper! Here are the key findings from arXiv paper 2604.02450 "Do We Need Frontier Models to Verify Mathematical Proofs?" by Aaditya Naik, Guruprerana Shabadi, Rajeev Alur, and Mayur Naik:

**Main Research Question and Approach:**
The paper investigates what model capability does reliable verification actually require by systematically evaluating four open-source and two frontier LLMs on datasets of human-graded natural language proofs of competition-level problems.

**Key Metrics and Findings:**
The study considers two key metrics: verifier accuracy and self-consistency (the rate of agreement across repeated judgments on the same proof). The results show that smaller open-source models are only up to ~10% behind frontier models in accuracy but they are up to ~25% more inconsistent.

**Prompt Ensemble Strategy:**
The researchers found that smaller models do possess the mathematical capabilities to verify proofs at the level of frontier models, but they struggle to reliably elicit these capabilities with general judging prompts. Through an LLM-guided prompt search, they synthesized an ensemble of specialized prompts that overcome the specific failure modes of smaller models, boosting their performance by up to 9.1% in accuracy and 15.9% in self-consistency. These gains allow models like Qwen3.5-35B to perform on par with frontier models such as Gemini 3.1 Pro for proof verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "afee5c21-dbd9-4ab6-86c0-5b09867e0858",
  "isSidechain": false,
  "promptId": "dd8c3ab0-46d7-4386-bd02-fb2287bbce2a",
  "type": "user",
  "uuid": "866b0b23-78ec-4a7a-9d62-46e0f738cdc1",
  "toolUseResult": {
    "query": "\"Do We Need Frontier Models to Verify Mathematical Proofs\" arXiv 2604.02450 2026 prompt ensemble verification",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VhYnNKzunE2YPKsmHy7Dmm",
        "content": [
          {
            "title": "[2604.02450] Do We Need Frontier Models to Verify Mathematical Proofs?",
            "url": "https://arxiv.org/abs/2604.02450"
          },
          {
            "title": "[2604.02450v1] Do We Need Frontier Models to Verify Mathematical Proofs?",
            "url": "https://arxiv.org/abs/2604.02450v1"
          },
          {
            "title": "Do We Need Frontier Models to Verify Mathematical Proofs?",
            "url": "https://arxiv.org/html/2604.02450v1"
          },
          {
            "title": "Do We Need Frontier Models to Verify Mathematical Proofs?",
            "url": "https://arxiv.org/pdf/2604.02450"
          },
          {
            "title": "Automated Conjecture Resolution with Formal Verification",
            "url": "https://arxiv.org/html/2604.03789v1"
          }
        ]
      },
      "I found the paper! Here are the key findings from arXiv paper 2604.02450 \"Do We Need Frontier Models to Verify Mathematical Proofs?\" by Aaditya Naik, Guruprerana Shabadi, Rajeev Alur, and Mayur Naik:\n\n**Main Research Question and Approach:**\nThe paper investigates what model capability does reliable verification actually require by systematically evaluating four open-source and two frontier LLMs on datasets of human-graded natural language proofs of competition-level problems.\n\n**Key Metrics and Findings:**\nThe study considers two key metrics: verifier accuracy and self-consistency (the rate of agreement across repeated judgments on the same proof). The results show that smaller open-source models are only up to ~10% behind frontier models in accuracy but they are up to ~25% more inconsistent.\n\n**Prompt Ensemble Strategy:**\nThe researchers found that smaller models do possess the mathematical capabilities to verify proofs at the level of frontier models, but they struggle to reliably elicit these capabilities with general judging prompts. Through an LLM-guided prompt search, they synthesized an ensemble of specialized prompts that overcome the specific failure modes of smaller models, boosting their performance by up to 9.1% in accuracy and 15.9% in self-consistency. These gains allow models like Qwen3.5-35B to perform on par with frontier models such as Gemini 3.1 Pro for proof verification."
    ],
    "durationSeconds": 5.583956708000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "afee5c21-dbd9-4ab6-86c0-5b09867e0858",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T12:54:27.255Z_

<details><summary>↩ Tool result · `toolu_013cmUv1sLocsZo1xCszZSS1`</summary>

```text
Web search results for query: "Pseudo-Formalization automatic proof verification code github Barkallah 2026 open source"

Links: [{"title":"Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/html/2605.20531"},{"title":"[2605.20531] Pseudo-Formalization for Automatic Proof Verification","url":"https://arxiv.org/abs/2605.20531"},{"title":"Automated Proof Generation for Rust Code via Self-Evolution","url":"https://arxiv.org/pdf/2410.15756"},{"title":"Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal   Proofs","url":"https://arxiv.org/pdf/2210.12283"},{"title":"Passport: Improving Automated Formal Verification Using Identifiers","url":"https://arxiv.org/pdf/2204.10370"},{"title":"Laurel: Unblocking Automated Verification with Large Language Models","url":"https://arxiv.org/pdf/2405.16792"}]

Based on the search results, I found information about the Pseudo-Formalization research:

Pseudo-Formalization (PF) is a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.

The research was authored by Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, and Tengyu Ma, with the paper published on arXiv on May 19, 2026.

To verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, in an algorithm called Block Verification.

The paper is available on arXiv (arXiv:2605.20531). However, the search results do not contain information about an open-source GitHub repository with code. You may want to check the paper directly on arXiv or the authors' institutional pages for links to any released code.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6592d66-5c5f-46cf-8288-66a679b56d29",
  "isSidechain": false,
  "promptId": "dd8c3ab0-46d7-4386-bd02-fb2287bbce2a",
  "type": "user",
  "uuid": "aa3ab5bc-e6df-4366-9458-1d1589a33bdc",
  "toolUseResult": {
    "query": "Pseudo-Formalization automatic proof verification code github Barkallah 2026 open source",
    "results": [
      {
        "tool_use_id": "srvtoolu_015Q1d74B3UEYgJH1bvBaEGi",
        "content": [
          {
            "title": "Pseudo-Formalization for Automatic Proof Verification",
            "url": "https://arxiv.org/html/2605.20531"
          },
          {
            "title": "[2605.20531] Pseudo-Formalization for Automatic Proof Verification",
            "url": "https://arxiv.org/abs/2605.20531"
          },
          {
            "title": "Automated Proof Generation for Rust Code via Self-Evolution",
            "url": "https://arxiv.org/pdf/2410.15756"
          },
          {
            "title": "Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal   Proofs",
            "url": "https://arxiv.org/pdf/2210.12283"
          },
          {
            "title": "Passport: Improving Automated Formal Verification Using Identifiers",
            "url": "https://arxiv.org/pdf/2204.10370"
          },
          {
            "title": "Laurel: Unblocking Automated Verification with Large Language Models",
            "url": "https://arxiv.org/pdf/2405.16792"
          }
        ]
      },
      "Based on the search results, I found information about the Pseudo-Formalization research:\n\nPseudo-Formalization (PF) is a proof format that captures the modularity and precision of formal proofs while retaining the flexibility of natural language. A Pseudo-Formal proof is decomposed into self-contained modules, each stating its premises, conclusion, and proof in natural language.\n\nThe research was authored by Slim Barkallah, Luke Bailey, Kaiyue Wen, Mohammed Abouzaid, and Tengyu Ma, with the paper published on arXiv on May 19, 2026.\n\nTo verify the correctness of a regular natural language proof, an LLM translates it to Pseudo-Formal and then verifies each module independently, in an algorithm called Block Verification.\n\nThe paper is available on arXiv (arXiv:2605.20531). However, the search results do not contain information about an open-source GitHub repository with code. You may want to check the paper directly on arXiv or the authors' institutional pages for links to any released code."
    ],
    "durationSeconds": 6.081079214999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b6592d66-5c5f-46cf-8288-66a679b56d29",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-27T12:54:31.633Z_

<details><summary>↩ Tool result · `toolu_01VdHCMBttVJfFvie3qoVzEP`</summary>

```text
Web search results for query: "dominator analysis dependency graph proof verification criticality routing formal methods 2025 2026"

Links: [{"title":"Parallel Verification of Natural Deduction Proof Graphs","url":"https://arxiv.org/pdf/2311.10440"},{"title":"Dominator (graph theory) - Wikipedia","url":"https://en.wikipedia.org/wiki/Dominator_(graph_theory)"},{"title":"Dominator Tree Certification and Independent Spanning Trees","url":"https://arxiv.org/pdf/1210.8303"},{"title":"Hiding irrelevant facts in verification conditions","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7926037"},{"title":"The Program Dependence Graph and Its Use in Optimization JEANNE FERRANTE","url":"https://web.eecs.umich.edu/~mahlke/courses/583f23/reading/ferrante_toplas_87.pdf"},{"title":"Enhancing redundancy removal with early merging","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8484591"},{"title":"Method and apparatus for critical and false path verification","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6714902"}]

I've completed the web search for your query. Here are the relevant results:

The search returned several academic and technical sources covering related topics:

1. **Parallel Verification of Natural Deduction Proof Graphs** - This work presents parallel algorithms for formal verification of graph-based natural deduction proofs, introducing layering that captures dependencies between proof steps, allowing nodes in each layer to be verified in parallel as long as prior layers have been verified.

2. **Dominator Tree Certification** - This research addresses how to verify that the dominator tree of a flow graph is correct, defining a correctness certificate for a dominator tree and showing how to augment fast dominator-finding algorithms so that they produce a correctness certificate.

3. **Dominator Applications in Graph Theory** - In hardware systems, dominators are used for computing signal probabilities for test generation, estimating switching activities for power and noise analysis, and selecting cut points in equivalence checking; in software systems, they are used for reducing the size of the test set in structural testing techniques.

4. **Program Verification with Dominators** - Verification conditions can be structured according to a dominator relationship between the program blocks of the control-flow graph.

5. **Critical Path Verification** - The search also found research on formal methods for critical and false path verification in circuit design, combining simulation and formal verification approaches.

These sources cover formal methods, proof verification, dependency graphs, and dominator analysis, though they don't appear to be specifically focused on the year 2025-2026 timeframe you requested.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3be5b200-921b-4743-bd39-3c6e6b39eaee",
  "isSidechain": false,
  "promptId": "dd8c3ab0-46d7-4386-bd02-fb2287bbce2a",
  "type": "user",
  "uuid": "b6f3838f-5379-4a96-a26c-8807cd5bd8b8",
  "toolUseResult": {
    "query": "dominator analysis dependency graph proof verification criticality routing formal methods 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KoRW1tAKtaeUz63uBLb3cN",
        "content": [
          {
            "title": "Parallel Verification of Natural Deduction Proof Graphs",
            "url": "https://arxiv.org/pdf/2311.10440"
          },
          {
            "title": "Dominator (graph theory) - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Dominator_(graph_theory)"
          },
          {
            "title": "Dominator Tree Certification and Independent Spanning Trees",
            "url": "https://arxiv.org/pdf/1210.8303"
          },
          {
            "title": "Hiding irrelevant facts in verification conditions",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7926037"
          },
          {
            "title": "The Program Dependence Graph and Its Use in Optimization JEANNE FERRANTE",
            "url": "https://web.eecs.umich.edu/~mahlke/courses/583f23/reading/ferrante_toplas_87.pdf"
          },
          {
            "title": "Enhancing redundancy removal with early merging",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8484591"
          },
          {
            "title": "Method and apparatus for critical and false path verification",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/6714902"
          }
        ]
      },
      "I've completed the web search for your query. Here are the relevant results:\n\nThe search returned several academic and technical sources covering related topics:\n\n1. **Parallel Verification of Natural Deduction Proof Graphs** - This work presents parallel algorithms for formal verification of graph-based natural deduction proofs, introducing layering that captures dependencies between proof steps, allowing nodes in each layer to be verified in parallel as long as prior layers have been verified.\n\n2. **Dominator Tree Certification** - This research addresses how to verify that the dominator tree of a flow graph is correct, defining a correctness certificate for a dominator tree and showing how to augment fast dominator-finding algorithms so that they produce a correctness certificate.\n\n3. **Dominator Applications in Graph Theory** - In hardware systems, dominators are used for computing signal probabilities for test generation, estimating switching activities for power and noise analysis, and selecting cut points in equivalence checking; in software systems, they are used for reducing the size of the test set in structural testing techniques.\n\n4. **Program Verification with Dominators** - Verification conditions can be structured according to a dominator relationship between the program blocks of the control-flow graph.\n\n5. **Critical Path Verification** - The search also found research on formal methods for critical and false path verification in circuit design, combining simulation and formal verification approaches.\n\nThese sources cover formal methods, proof verification, dependency graphs, and dominator analysis, though they don't appear to be specifically focused on the year 2025-2026 timeframe you requested."
    ],
    "durationSeconds": 10.060902895000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3be5b200-921b-4743-bd39-3c6e6b39eaee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 50 · 2026-05-27T12:54:31.639Z_

```json
{
  "parentUuid": "b6f3838f-5379-4a96-a26c-8807cd5bd8b8",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "277c22b2-ac4c-469a-8f56-ec529025c384",
  "timestamp": "2026-05-27T12:54:31.639Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 51 · 2026-05-27T12:56:00.809Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me analyze the cross-validation results:

1. **"Do We Need Frontier Models"**: CONFIRMED. Real paper (arXiv 2604.02450, April 2026). Specialized prompt ensemble boosts smaller models by up to 9.1% accuracy, 15.9% self-consistency, making Qwen3.5-35B comparable to frontier models for proof verification. This is a legitimate baseline concern from the 补救 agent.

2. **PF code availability**: NO CODE FOUND. The search didn't find any GitHub repository or open-source code. 

The paper's recent publication date—just over a week ago—represents a genuine feasibility risk that validates the 补救 agent's concern about implementation gaps.

3. **Dominator analysis for verification routing**: No existing work applies dominator analysis specifically for verification routing decisions in proof verification. While the concept appears in compiler optimization and hardware verification, applying it here is novel but untested, introducing both innovation potential and scope risk.

Now I'm synthesizing my assessment for Round 2, starting with the 发掘 agent's contributions.

**发掘 agent assessment:**

The reframing from cost-saving to architectural necessity for scalable formal verification is well-grounded in miniF2F-Lean Revisited's ~36% end-to-end limit, which strengthens the significance claim. The three-layer differentiation between uncertainty source, routing target heterogeneity, and structural criticality is clear and defensible. For the trivial alternative defense, adding a simple heuristic baseline to the ablation study would effectively demonstrate why calibrated uncertainty outperforms basic routing strategies. The dependency criticality idea shows promise, though I need to evaluate how it deepens the contribution.

Adding dominator analysis and betweenness centrality would increase technical rigor, but proof dependency DAGs from PF are typically small (20-50 nodes), making such computations trivial. Since no prior work combines these approaches, it's novel, but I'm concerned about scope creep given the proposal's complexity. I'll mention these graph-theoretic extensions as sensitivity analysis rather than a core contribution, keeping fan-out as the primary metric. Elevating Ablation 6 to a core result is compelling—if PF blocks significantly outperform raw NL for autoformalization, that's a standalone contribution worth highlighting beyond the ablation section.

For the remedial concerns: increasing the synthetic set to 400-500 examples is reasonable and reporting effect sizes will strengthen the statistical foundation. The block-level autoformalization pilot is critical since the entire Tier 2 premise depends on achieving at least 30% end-to-end success; I'll frame this as a go/no-go milestone. The prompt ensemble baseline is verified and directly relevant, so I'll incorporate it as a comparison point.

For the remaining issues: multi-source error generation with human validation for the synthetic set is solid, using that set for Platt scaling calibration while reserving ArxivMathGradingBench for evaluation keeps things clean, and I need to account for the lack of available code from the prior work in my timeline. Running sensitivity analysis across different Tier 2 success rates will also help stress-test the approach.

The major shifts this round are reframing significance from cost-saving to architectural necessity, strengthening the differentiation from Ganguly's work, defending against trivial alternatives, and ablation studies.

Now assessing probability: the novelty is genuinely strong with the three-layer differentiation, generation-versus-verification taxonomy, dependency-graph routing, and the insight about PF blocks as a bridge to autoformalization. Significance also upgrades to strong with the reframing around architectural viability for complex proof verification. The critical vulnerability is that the claim about PF blocks improving autoformalization remains unproven—if the pilot study doesn't validate this, the entire contribution collapses. With this significance upgrade, the idea ceiling moves to around 48%, though experimental completeness still needs tighter baselines and clearer data flows.

The probability sits at 38% now, up modestly from 36%. The significance gain is offset by newly surfaced risks around PF code availability and unknown autoformalization success rates. I'm checking whether another iteration makes sense: both reviewers still identified substantive issues rather than minor refinements, changes are becoming more incremental than structural, and there's no oscillation in the assessment. One more pass could verify internal consistency and whether the elevated autoformalization tractability claim actually holds under scrutiny.

But looking at what the second round actually produced—mostly refinements to significance framing and operational details like statistical power and code availability—I'm noticing the granularity is increasing. A third round would likely surface even finer-grained issues, and I'm skeptical those would meaningfully shift the probability estimate. The proposal is already quite solid at this point, so I'm leaning toward wrapping up after this round rather than continuing further. The changes from Round 2 are substantive enough to warrant another iteration—reframing the significance, promoting the ablation study to a core result, adding the prompt ensemble baseline, and establishing the pilot study as a go/no-go gate all represent meaningful shifts. Now I need to carefully preserve all the references while incorporating these updates into a concise revised proposal. Now I'm looking at the performance metrics across these approaches—showing improvements like 78.3% to 37.3% reduction, human and LLM judgment rates, end-to-end success rates, and efficiency gains in verifier calls and computation. I should add the verified baseline paper on frontier models for proof verification, and mention the other references if they come up naturally in the discussion.

Actually, I need to reconsider how to frame the core contribution here. Rather than presenting the selective verification pipeline as the main result with a side note about PF blocks, I should elevate the modular decomposition finding itself as a primary contribution—showing that PF's block-level structure significantly improves autoformalization tractability and serves as a bridge between informal and formal verification. Then the two-tier pipeline becomes the second contribution built on top of that insight. This gives the paper a stronger structure with two distinct contributions instead of one system with an incidental ablation finding.

For defending against trivial alternatives, I should add a simple heuristic baseline to the ablations—just routing based on basic rules—to show that the selective approach outperforms naive strategies.

I also need to sharpen the related work section to make the three-layer distinction from Ganguly's work explicit, add a prompt ensemble baseline for comparison, mention dominator and centrality analysis as possible extensions for dependency criticality while keeping fan-out as the primary approach, frame the pilot study as a Phase 0 go/no-go decision point, and include the PF code contingency in the resource estimates.

Before drafting the full proposal, let me do a reference check to make sure everything is properly cited. continuing with more recent papers on formal verification and process reward models, including VERGE, HERMES, Goedel-Prover-V2, and work on uncertainty-based verification approaches, plus the emerging process reward model literature starting with ThinkPRM and Qwen variants.

Now I'm adding papers on proof autoformalization like ProofSketcher and ProofFlow, along with work on cascade routing and whether frontier models are actually needed for mathematical verification. I'm also noting some key empirical results—the significant drop in performance on harder verification benchmarks, the gap in error detection on arxiv grading, and the success rates around 80% for safe proofs.

For the body text, I'm tracking specific numbers like the 66% human-judged accuracy for autoformalization (much lower than the 97% sometimes claimed), the roughly 70% theorem proving success, and the end-to-end pipeline success sitting around 35%. I'm also pulling in efficiency gains from papers like HERMES showing 67% accuracy improvement with 80% fewer FLOPs, and noting the specific models being used like QwQ-32B and StepFun-Formalizer-32B. The ArxivMathGradingBench with 35 papers and 40 known errors is a useful benchmark to reference, and the 40.5% BEq@1 score on FormalMATH-Lite gives a concrete performance baseline.

Now I'm realizing the proposal is getting unwieldy, so I need to tighten things up—cutting redundancy, using bullet points strategically for the evaluation plan, and keeping the approach section lean and focused. I should aim for roughly the same length as the first round proposal but with denser, higher-quality content rather than padding it out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "277c22b2-ac4c-469a-8f56-ec529025c384",
  "isSidechain": false,
  "requestId": "req_011CbT7DU63MZbfkPg4LRRsm",
  "type": "assistant",
  "uuid": "af7ef127-3687-466d-9594-8d72e7f8f51e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtXrrLG9xhXYLHFaWjnyn8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 57742,
      "output_tokens": 11210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11210,
          "cache_read_input_tokens": 57742,
          "cache_creation_input_tokens": 3204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3204
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

_source line 52 · 2026-05-27T12:58:31.023Z_

交叉验证结果已获得。现在整合第 2 轮输出。

【阶段】: 迭代第 2 轮

【交叉验证调研】:
1. **"Do We Need Frontier Models to Verify Mathematical Proofs?"** (arXiv 2604.02450, April 2026) — **已验证存在且高度相关**。通过 LLM-guided prompt search + specialized prompt ensemble，Qwen3.5-35B 在 proof verification 上提升 9.1% accuracy、15.9% self-consistency，接近 frontier model (Gemini 3.1 Pro) 水平。补救 agent 的 baseline 建议完全成立——这是审稿人必定知道的工作，不纳入会被要求补实验。
2. **PF 代码/数据可获得性** — **未找到 GitHub 仓库**。arXiv 2605.20531 于 2026-05-19 发表（约 1 周前），搜索未发现任何开源代码或数据链接。补救 agent 的 feasibility concern (缺陷6) 已验证——需要在 timeline 中加入 contingency。
3. **Dominator analysis for verification routing** — **未找到先例**。搜索发现 dominator trees 在编译器优化（程序依赖图）和硬件验证（关键路径分析）中广泛使用，但**无任何工作将 dominator analysis 应用于数学证明验证的 routing 决策**。发掘点4 的新颖性确认，但也意味着没有现成方法可借鉴——增加了实现不确定性。

【发掘 agent 有效建议采纳】:
- 发掘点1（Significance 从"cost-saving"升级为"scalable formal verification 的唯一可行架构"）: **已验证，采纳**。miniF2F-Lean Revisited 的 ~36% 端到端上限是硬数据支撑。这个 reframing 不改变技术方案但显著提升审稿人感知的贡献层级。
- 发掘点2（Ganguly 三层差异化：uncertainty source / routing target heterogeneity / structural criticality）: **逻辑验证，采纳**。三层区分清晰且 defensible，防止被归类为"same idea, different domain"。
- 发掘点3（Trivial alternative defense：simple heuristic baseline）: **采纳**。在 ablation 中新增 "simple structural heuristic only" routing baseline（block length, step count, cited theorem count），并在 claim 中论证 calibrated uncertainty 的增量价值（捕捉结构简单但推理 subtle 的错误块）。
- 发掘点4（Dependency criticality 从 fan-out 扩展到 dominator/centrality）: **部分采纳**。dominator analysis 在证明依赖图上无先例（已验证新颖），但 PF dependency DAG 通常较小（20-50 nodes），完整 graph-theoretic framework 有 over-engineering 风险。采纳为：以 fan-out 为主，supplementary 提及 dominator nodes 和 betweenness centrality 作为 sensitivity analysis，不作为核心贡献。
- 发掘点5（Ablation 6 提升为 core result）: **采纳**。如果 PF blocks 显著提升 autoformalization success rate，这本身是 contribution-level finding。重构论文为双贡献结构：(1) empirical finding about PF-block autoformalization advantage, (2) selective verification pipeline built upon it。

【补救 agent 有效建议采纳】:
- 缺陷1（Synthetic set 提升到 400-500 instances + effect size）: **采纳**。400-500 instances 在 McNemar's test 下可检测 5-10% 绝对改进。
- 缺陷2（Block-level autoformalization pilot study as go/no-go）: **采纳，列为最关键前置验证**。如果端到端 <30%，整个 Tier 2 需要重新设计。
- 缺陷3（Prompt ensemble baseline）: **已验证，采纳**。新增 "PF + BV with specialized prompt ensemble" 作为 best-effort LLM verification upper bound。
- 缺陷4（Synthetic set 构造：多源错误 + 人工验证）: **采纳**。controlled perturbation + LLM-generated errors + 小规模人工验证 (50-80 instances, Cohen's κ)。
- 缺陷5（Calibration data flow：synthetic set 校准 / ArxivMathGradingBench 评估）: **采纳**。清晰分离 calibration 和 evaluation 数据源，消除 data leakage。
- 缺陷6（PF 代码可获得性）: **已验证，采纳**。搜索未发现开源代码。timeline 加入 2-3 周 contingency for reproduction。
- 缺陷7（Tier 2 sensitivity analysis）: **采纳**。在不同 Tier 2 成功率假设（30%/50%/70%/90%）下画 Pareto 曲线。

【本轮 proposal 主要变更】:
**Idea 层面变更:**
- Significance reframing：从 "cost-reliability optimization" 升级为 "modular decomposition as the only viable path to scalable formal verification of complex proofs"
- PF-block autoformalization advantage 从 ablation 提升为 core contribution (双贡献结构)
- Ganguly et al. 差异化锐化为三层结构（uncertainty source / routing heterogeneity / structural criticality）
- Trivial alternative defense：论证 calibrated uncertainty 捕捉 heuristic-invisible 错误的机制
- Dependency criticality 补充 dominator/centrality 作为 sensitivity analysis extension

**实验层面变更:**
- 新增 pilot study (Phase 0, go/no-go milestone): 50-100 PF blocks 的 autoformalization + proof search 端到端成功率
- 新增 baseline: PF + BV with specialized prompt ensemble (arXiv 2604.02450)
- 新增 ablation: simple structural heuristic-only routing baseline
- Synthetic set 提升至 400-500 instances，多源错误生成 + 人工验证子集
- Calibration/evaluation 数据源分离（synthetic+miniF2F 校准，ArxivMathGradingBench 评估）
- Tier 2 sensitivity analysis（不同成功率假设下的 Pareto 曲线）
- PF 代码可获得性 contingency (timeline +2-3 weeks)

【idea 质量评估】: Novelty=中强 Significance=强 → idea 天花板约 48%
- Novelty 中强（趋强）：三层 Ganguly 差异化 + dependency criticality + 双贡献结构 已构成清晰的独立贡献；但 pipeline 组合的底色仍在
- Significance 强：从 "cheaper verification" 到 "the only viable architecture for scaling formal verification to complex proofs" 是质的提升，有 miniF2F-Lean Revisited 的硬数据支撑

【实验完备性评估】: Technical Soundness=中（设计层面中强，但 Tier 2 可行性未经实验验证） → pilot study 是关键
- 实验框架全面（8 个 ablation + 3 benchmark + 7 baselines + Pareto 分析 + sensitivity analysis）
- 最大风险：block-level autoformalization 端到端成功率未知，pilot study 结果决定 Tier 2 是否 viable
- 次要风险：PF 代码可获得性不确定

【当前概率估计】: [33% - 44%] 中位 38%
- 上限 44% 反映 significance 提升和双贡献结构的增量
- 下限 33% 反映 Tier 2 可行性未验证和 PF 代码风险
- 中位 38% = idea 天花板 48% - 实验不确定性惩罚 ~10%

【决策】: 继续（预期下轮收敛）

【决策理由】: 第 2 轮引入了 significance reframing、双贡献结构、新 baseline、pilot study 等实质性变更，需要 1 轮 worker 验证：(1) significance claim "only viable architecture" 是否 over-claim；(2) 双贡献结构是否 internally consistent；(3) 实验计划在增加 pilot study 和新 baseline 后是否仍在 resource budget 内。两位 worker 均未报告致命缺陷，概率从 36% 微升至 38%——变化在合理范围内但仍有微调空间。预期第 3 轮 worker 输出以 fine-tuning 为主，触发收敛条件。

**引用保留核对清单**（逐条确认出现在下方纯净版中）:
1. ✅ Pseudo-Formalization (Barkallah et al., arXiv 2026 / May 2026)
2. ✅ Safe (Liu et al., ACL 2025)
3. ✅ Hard2Verify (Pandit et al., arXiv 2025)
4. ✅ miniF2F-Lean Revisited (NeurIPS 2025)
5. ✅ Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025)
6. ✅ Adaptive Test-Time Compute Allocation (Qu, arXiv 2026)
7. ✅ VERGE (Singh et al., arXiv 2026)
8. ✅ HERMES (Ospanov et al., ICML 2026)
9. ✅ Goedel-Prover-V2 (ICLR 2026)
10. ✅ Reasoning with Confidence / Uncertainty Heads (arXiv 2025)
11. ✅ ThinkPRM (2025)
12. ✅ Qwen2.5-Math-PRM (2025)
13. ✅ ProofSketcher (arXiv 2026)
14. ✅ UCCI (arXiv 2026)
15. ✅ ProofFlow (2025)
16. ✅ 新增: "Do We Need Frontier Models to Verify Mathematical Proofs?" (arXiv 2604.02450, 2026)
17. ✅ 新增: Process-Driven Autoformalization in Lean 4 (2024)
18. ✅ 78.3%→37.3%, ArxivMathGradingBench, ~50%, 80%, 4-8x, 66%/97%, ~35%, 14-100%, 44%, 67%/80%
19. ✅ QwQ-32B, StepFun-Formalizer-32B, Goedel-Prover-V2-32B, BEq@1 40.5%

【下一轮 proposal（纯净版，将原样传给 worker）】:
---
# Uncertainty-Guided Selective Formal Verification via Pseudo-Formal Decomposition

## Core Problem

How can we achieve near-formal-verification reliability for natural language mathematical proof checking while keeping cost tractable, by selectively routing only the most uncertain and structurally critical proof blocks to formal verification?

## Thesis and Contributions

We advance two claims, each supported by a corresponding contribution:

**Claim 1 (Architectural Insight):** Modular proof decomposition — as instantiated by Pseudo-Formalization (Barkallah et al., 2026) — serves as a natural bridge between informal and formal verification of mathematical proofs. Each PF block's explicit typed premises map directly to Lean 4 hypothesis lists, its single explicit conclusion maps to a Lean 4 goal statement, and its self-contained nature eliminates the context-completion problem that fundamentally limits whole-proof autoformalization to ~35% end-to-end success (miniF2F-Lean Revisited, NeurIPS 2025). We empirically validate this by demonstrating that PF-block-level autoformalization achieves substantially higher success rates than raw-NL-fragment autoformalization in a controlled paired comparison.

**Claim 2 (System Design):** Building on this bridge, we design a two-tier selective verification pipeline that combines calibrated uncertainty scoring with dependency-graph criticality to route only the 10-20% most uncertain or structurally critical blocks to Lean 4 formal verification. This achieves near-formal reliability at ~1.5-2x cost overhead versus Safe's 4-8x for universal formalization, and represents a viable path toward scaling formal verification to research-level proofs — where whole-proof autoformalization is fundamentally intractable.

## Research Opportunity

Whole-proof autoformalization faces a fundamental scalability barrier: context-completion difficulties and compounding error across steps limit end-to-end success to ~35% even with SOTA tools (66% autoformalization accuracy × ~70% theorem proving success; miniF2F-Lean Revisited, NeurIPS 2025). This barrier does not diminish with stronger models — it is architectural, arising from the unbounded context dependencies in monolithic proofs. Consequently, universal formal verification (Safe, Liu et al., ACL 2025) imposes 4-8x cost overhead per step while still being limited by autoformalization failures. Meanwhile, LLM-only verification (PF+Block Verification; Barkallah et al., May 2026) is cheap but leaves ~50% of research-level errors undetected on ArxivMathGradingBench. PF's modular block structure offers a way through this impasse: self-contained blocks with explicit premises and conclusions are structurally aligned with formal theorem statements, making block-level autoformalization fundamentally more tractable than whole-proof autoformalization. Step-level formalization has independently been shown more tractable than whole-proof approaches (Process-Driven Autoformalization in Lean 4, 2024). By adding calibrated uncertainty and dependency-graph criticality as a dual triage signal, we can route only the most critical blocks to formal verification, catching errors that LLM verification misses while operating within the tractability boundary of block-level autoformalization.

## Research Landscape

**LLM-based verification (cheap, unreliable):** Best PRM drops from 78.3% to 37.3% on Hard2Verify (Pandit et al., 2025). PF+Block Verification Pareto-dominates LLM-as-judge on olympiad and research-level benchmarks but still leaves ~50% of errors undetected on ArxivMathGradingBench (Barkallah et al., 2026). ThinkPRM (2025) advances data-efficient verbalized PRMs outperforming discriminative PRMs with 1% of process labels, representing the current strongest step-level LLM verifier. Specialized prompt ensembles can close much of the gap between small and frontier models for proof verification (Do We Need Frontier Models to Verify Mathematical Proofs?, arXiv 2604.02450, 2026), raising the LLM-only performance ceiling.

**Universal formal verification (reliable, expensive):** Safe verifies each step in Lean 4 with ~80% success at 4-8x cost (Liu et al., ACL 2025). End-to-end autoformalization achieves only ~35% success (miniF2F-Lean Revisited, NeurIPS 2025). StepFun-Formalizer-32B achieves BEq@1 of 40.5% on FormalMATH-Lite for statement-level autoformalization.

**Selective/adaptive verification (emerging):** Ganguly et al. (NeurIPS 2025) achieve 14-100% error reduction via selective SMT-based formalization using PCFG-based uncertainty. Our work differs on three levels: (1) uncertainty source — Ganguly models generation-side distribution (LLM→SMT-LIB), we model verification-side judgment uncertainty (BV ensemble disagreement on existing proofs); (2) routing target heterogeneity — Ganguly routes within a single verification paradigm (verify vs. abstain on SMT), we route across fundamentally different paradigms (LLM verification → formal verification); (3) structural criticality — Ganguly uses no structural signal, we introduce dependency-graph criticality as an orthogonal routing dimension. Qu (arXiv 2026) achieves 44% fewer verifier calls via adaptive allocation on MATH but operates within LLM-tier verification only.

**Proof generation vs. verification taxonomy:** HERMES (Ospanov et al., ICML 2026) interleaves informal reasoning with Lean 4 verification during proof generation, achieving 67% accuracy improvement with 80% fewer FLOPs — but addresses proof generation (where output format is controllable) with uniform formalization, not proof verification of arbitrary NL input. Our work addresses the fundamentally different verification setting where PF decomposition is necessary to create structured formalization targets from arbitrary input. VERGE (Singh et al., arXiv 2026) routes between SMT solvers and LLM-ensemble verification for first-order logic claims, not mathematical proof blocks. UCCI (arXiv 2026) provides calibrated uncertainty for LLM cascade routing (small→large model), not across formal/informal verification tiers. ProofSketcher (arXiv 2026) produces typed proof sketches without uncertainty-guided routing. ProofFlow (2025) uses dependency graphs for autoformalization fidelity but not for verification routing decisions.

## Proposed Approach

**Phase 0 — Pilot study (go/no-go).** Before full pipeline development, we validate the core architectural assumption: randomly sample 50-100 PF blocks across mathematical domains and difficulty levels, test StepFun-Formalizer-32B autoformalization success rate and Goedel-Prover-V2-32B proof search success rate, establish block-level end-to-end success rate baseline. Threshold: if end-to-end success rate < 30%, Tier 2 requires redesign (e.g., multi-shot formalization with compiler-feedback self-correction). Report decomposed success rates: formalization type-check rate → proof search success rate → end-to-end rate.

**Tier 1 — LLM Block Verification with calibrated uncertainty.** Decompose proof into PF blocks (Barkallah et al., 2026) with explicit premises, conclusions, and dependency graphs. Run Block Verification using QwQ-32B with dual uncertainty scoring: (i) ensemble disagreement via N=5 stochastic forward passes with temperature sampling, (ii) token-level CoT entropy. Calibrate via Platt scaling on synthetic evaluation set and miniF2F verification data (NOT on ArxivMathGradingBench, which is reserved for evaluation only), with temperature scaling as calibration method ablation.

**Dual-signal routing.** Route blocks based on: uncertainty score × dependency criticality (primary: fan-out degree in inter-block dependency DAG; supplementary sensitivity analysis: dominator nodes, betweenness centrality). This dual signal mitigates the "confident-but-wrong" risk inherent in LLM overconfidence: (a) ensemble disagreement captures inter-model uncertainty more reliably than single-model confidence; (b) dependency criticality provides an uncertainty-independent signal — high-fan-out blocks receive formal verification even if BV is confident; (c) structural difficulty heuristics (block-internal step count, cited theorem count) serve as additional features.

**Why calibrated uncertainty, not just structural heuristics?** Simple heuristics (block length, step count) capture surface complexity but miss blocks that are structurally simple yet reasoning-subtle — e.g., a one-step block applying a theorem in a non-obvious way. Ensemble disagreement flags exactly these cases: when model copies disagree on a seemingly-simple block, this signals hidden reasoning difficulty invisible to structural features. We validate this claim via head-to-head ablation against heuristic-only routing.

**Tier 2 — Selective formal verification.** Routed blocks are autoformalized to Lean 4 using StepFun-Formalizer-32B — leveraging PF block structure (premises→Lean 4 hypotheses, conclusion→Lean 4 goal, no context completion needed) — then formally verified via Goedel-Prover-V2-32B proof search with verifier-guided self-correction (up to k=3 retry rounds using Lean compiler feedback). Per-block timeout: 5 min; per-proof timeout: 30 min. Fallback strategy for autoformalization failure or proof search timeout is an ablation variable.

## Evaluation Plan

**Benchmarks:**
- ArxivMathGradingBench (Barkallah et al., 2026): 35 papers, 40 known errors. Held-out evaluation only (not used for calibration). Error detection precision/recall/F1, bootstrap CI (1000 resamples), McNemar's test, effect size (Cohen's h). Supplementary: per-paper accuracy.
- Synthetic Error Detection Set: 400-500 instances from Hard2Verify competition-level problems. Multi-source error construction: (i) LLM-generated incorrect proofs, (ii) controlled perturbation of correct proofs (deleted steps, swapped theorems, computation errors), (iii) extracted known-error steps from Hard2Verify annotations. Ground-truth verification via answer matching + Lean 4 proof for correct proofs. Human validation on 50-80 instance subsample (Cohen's κ). Used for calibration and as co-primary evaluation benchmark.
- miniF2F Verification Protocol: Generate ≥8 candidate proofs per problem (≥100 problems) using QwQ-32B, evaluate verification precision/recall. Aligned with Safe's miniF2F setting.

**Baselines (7 methods):**
- PF + BV single-pass (Barkallah et al., 2026)
- PF + BV ensemble (N=5, no routing to formal verification)
- PF + BV with specialized prompt ensemble (per arXiv 2604.02450, 2026): best-effort LLM verification upper bound
- ThinkPRM (2025): SOTA data-efficient verbalized PRM
- Qwen2.5-Math-PRM-7B: strongest open-source discriminative PRM at comparable scale
- Safe universal formalization (Liu et al., ACL 2025)
- HERMES (Ospanov et al., ICML 2026): if applicable to verification setting

**Cost framework:** Unified metric: GPU-seconds per proof. Detailed breakdown: PF decomposition + ensemble BV (5× single BV) + routing overhead + autoformalization (per routed block) + proof search including retries and timeouts + fallback cost for Tier 2 failures. Pareto curve (cost vs. error detection recall) plotting all methods.

**Ablations (8 experiments):**
1. Uncertainty signal decomposition: ensemble disagreement only / CoT entropy only / combined — AUROC, ECE, recall@fixed-cost
2. Routing signal: uncertainty only / dependency criticality only / simple structural heuristic only / dual signal — recall and cost
3. Ensemble size: N=3 / N=5 / N=7
4. Autoformalization failure fallback: accept / reject / majority-vote re-verification
5. Threshold sweep: routing percentage 5%-50% — Pareto curve
6. **PF blocks vs. raw NL autoformalization (Contribution 1 validation):** Paired comparison on same proofs. PF block input vs. raw NL fragment input to StepFun-Formalizer-32B. Metrics: Lean 4 type-check rate, proof search success rate. Paired Wilcoxon signed-rank test. This is a core result, not merely an ablation.
7. Confident-but-wrong analysis: proportion of BV errors at >0.8 confidence, fraction captured by dual-signal vs. uncertainty-only routing
8. Tier 2 sensitivity analysis: system Pareto curves under assumed Tier 2 success rates of 30%/50%/70%/90%, demonstrating robustness

**Calibration method ablation:** Platt scaling vs. temperature scaling, cross-validated on calibration set, evaluated by ECE and routing decision quality.

## Key References

- Pseudo-Formalization for Automatic Proof Verification (Barkallah et al., arXiv 2026)
- Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (Liu et al., ACL 2025)
- Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (Pandit et al., arXiv 2025)
- miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward (NeurIPS 2025)
- Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (Ganguly et al., NeurIPS 2025)
- Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (Qu, arXiv 2026)
- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (Singh et al., arXiv 2026)
- HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (Ospanov et al., ICML 2026)
- Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction (ICLR 2026)
- Reasoning with Confidence: Efficient Verification of LLM Reasoning Steps via Uncertainty Heads (arXiv 2025)
- ThinkPRM: Process Reward Models That Think (2025)
- Qwen2.5-Math-PRM (2025)
- ProofSketcher (arXiv 2026)
- UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing (arXiv 2026)
- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (2025)
- Do We Need Frontier Models to Verify Mathematical Proofs? (arXiv 2604.02450, 2026)
- Process-Driven Autoformalization in Lean 4 (2024)

## Resource Estimate

- **Phase 0 pilot:** ~30-50 GPU-hours (A100-80GB), 1-2 weeks. Go/no-go decision point.
- **Full pipeline (Phase 1-3):** GPU hours: 400-550 (ensemble BV ~80h; StepFun-Formalizer ~80h; Goedel-Prover-V2 proof search ~130h including retries/timeouts; synthetic set construction ~40h; baselines + ablations ~120-170h). CPU hours: ~60h (Lean 4 kernel type-checking). Timeline: 14-18 weeks (2-3 researchers), including 2-3 week contingency for PF pipeline reproduction if code unavailable.
- **Estimated GPU cost:** $1200-1650
- **Lean 4 proof search:** Per-block timeout 5 min, per-proof timeout 30 min. ArxivMathGradingBench single pass: ~9h wall-clock (35 papers × ~30 blocks × 15% routing × 3.5 min/block). Independent blocks parallelizable.
- **Critical path:** Phase 0 pilot (weeks 1-2) → PF pipeline setup + synthetic set (weeks 2-5) → uncertainty calibration (weeks 5-8) → full pipeline + ablations (weeks 8-15) → analysis + writing (weeks 15-18).
---

Sources:
- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450)
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)
- [Dominator (graph theory) - Wikipedia](https://en.wikipedia.org/wiki/Dominator_(graph_theory))

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af7ef127-3687-466d-9594-8d72e7f8f51e",
  "isSidechain": false,
  "requestId": "req_011CbT7DU63MZbfkPg4LRRsm",
  "type": "assistant",
  "uuid": "db99ca56-79c5-400c-bdb4-c4de252836dd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TtXrrLG9xhXYLHFaWjnyn8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3204,
      "cache_read_input_tokens": 57742,
      "output_tokens": 11210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11210,
          "cache_read_input_tokens": 57742,
          "cache_creation_input_tokens": 3204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3204
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
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have a comprehensive picture of the research landscape. Let me compile my assessment.  ---  【状态】: 有发掘…",
  "leafUuid": "db99ca56-79c5-400c-bdb4-c4de252836dd",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 2 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have a comprehensive picture of the research landscape. Let me compile my assessment.  ---  【状态】: 有发掘…",
  "leafUuid": "db99ca56-79c5-400c-bdb4-c4de252836dd",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 57_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 58 · 2026-05-27T13:06:31.599Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T13:06:31.599Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "content": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。\n\n【发掘 agent 本轮输出】:\nNow I have enough research to provide a thorough analysis. Let me compile my findings.\n\n【状态】: 有发掘空间\n\n【前置调研发现】\n- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531) (arXiv, May 2026): 本 proposal 的直接基础。PF 将证明分解为自包含模块，每个模块显式声明前提、结论和证明。Block Verification 在 ArxivMathGradingBench 上 Pareto-dominates LLM-as-judge 但仍遗漏 ~50% 的错误。该论文发表仅 8 天（相对于今天 2026-05-27），说明 proposal 紧跟前沿。\n- [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047) (NeurIPS 2025): 最接近的竞争者。用 PCFG 建模 LLM→SMT-LIB 的生成端不确定性，实现选择性验证，误差降低 14-100%。proposal 声称的三维差异化（不确定性来源、跨范式路由、结构关键性）经调研确认为真实差异，非表面区分。\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 在 first-order logic claims 上跨验证范式路由（SMT solver vs LLM ensemble），使用 claim 类型（logical vs commonsense）而非不确定性作为路由信号。这是架构层面最接近的系统——都是跨范式路由。\n- [ProofFlow](https://arxiv.org/abs/2510.15981) (ICLR 2026): 用依赖 DAG 保持 autoformalization 的结构忠实度，ProofScore 0.545 远超 whole-proof (0.123) 和 step-proof (0.072)。验证了依赖图结构在证明形式化中的价值，但用途不同：ProofFlow 用于 autoformalization 忠实度，proposal 用于验证路由。\n- [UCCI](https://arxiv.org/abs/2605.18796) (arXiv, May 2026): 用 isotonic regression 校准 token-level margin uncertainty 做 LLM cascade routing。方法论高度相关但路由目标不同（小模型→大模型 vs LLM verification→formal verification）。\n- [Process-Driven Autoformalization in Lean 4](https://openreview.net/forum?id=k8KsI84Ds7) (2024): 展示 step-level formalization + compiler feedback 优于 whole-proof。部分支持 proposal 的核心假设，但 PDA 的 step-level 仍需维护 running context，与 PF block 的完全自包含不同。\n- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450) (arXiv 2026): 通过 specialized prompt ensemble，小模型可达到 frontier 模型的验证水平（准确率提升 9.1%，一致性提升 15.9%）。这提升了 LLM-only verification 的天花板，但 proposal 已将此纳入 baseline。\n- [ThinkPRM](https://arxiv.org/abs/2504.16828) (2025): 用 1% 的 process labels 训练的 verbalized PRM 超过 discriminative PRM。代表当前最强的 step-level LLM verifier。\n- [StepFun-Formalizer-32B](https://arxiv.org/abs/2508.04440) / [Goedel-Prover-V2](https://github.com/Goedel-LM/Goedel-Prover-V2) (ICLR 2026): Proposal 选用的具体工具链。StepFun-Formalizer BEq@1 40.5% on FormalMATH-Lite；Goedel-Prover-V2 MiniF2F pass@32 达 88.1%。工具选型合理。\n- 调研总结: 该领域当前的突破方向有两条：(1) 降低 autoformalization 粒度（whole-proof → step-level → block-level）以提高成功率；(2) 用不确定性信号做选择性验证以降低成本。本 proposal 的核心 insight 在于将这两条线索交叉：用 PF block 作为最佳粒度单位，用不确定性+结构关键性做选择性路由。这个交叉点目前尚无人占据。\n\n---\n\n【发掘点 1】\n- 维度: 核心 claim 强化 / novelty 锐化\n- 内容: **将 dual-signal routing 重新表述为决策论风险最小化框架。** 当前 proposal 将 uncertainty × dependency criticality 呈现为工程组合（\"dual signal mitigates confident-but-wrong risk\"）。但这其实是一个决策论问题的自然解：每个 block b 的验证路由决策应最小化 Expected Verification Loss = P(BV_error | b) × C(error | b)，其中 P 由校准后的 ensemble uncertainty 估计，C 由依赖图关键性（b 的传递可达 block 数量 × 各下游 block 的 uncertainty 权重）估计。当 E[Loss] 超过 formal verification 的边际成本时路由到 Tier 2。这个重新表述的价值在于：(1) 将两个看似 ad hoc 的信号统一为一个有原则的目标函数；(2) 路由阈值不再是超参数，而是成本-风险均衡的自然结果；(3) 与 Ganguly 等人的差异变得更本质——他们优化的是 abstention policy（是否验证），你优化的是 cross-tier routing policy（如何验证），目标函数的结构完全不同。\n- 价值: 这一重新表述将 Novelty 从 \"组合了两个信号\" 提升为 \"提出了一个有原则的跨范式验证路由框架\"。审稿人面对 \"我们把 A 和 B 乘在一起\" 容易说 \"trivial combination\"；面对 \"我们定义了一个风险最小化目标，A 和 B 分别估计目标的两个因子\" 则很难说 trivial。\n- 调研依据: UCCI (arXiv 2605.18796) 将校准后的 uncertainty 直接连接到 cost-optimal escalation threshold，用约束优化选择路由阈值——这验证了 \"校准 uncertainty → 成本最优路由\" 这一范式在 LLM routing 中的有效性。本建议将同样的原则扩展到 cross-paradigm verification routing，并引入 cost-of-error 维度。\n\n【发掘点 2】\n- 维度: 核心 claim 强化 / significance 提升\n- 内容: **精确定义 \"context-completion problem\" 并将其作为 Claim 1 的理论核心，明确 PF block 与现有 step-level 方法的结构差异。** 当前 proposal 说 PF block 的 \"self-contained nature eliminates the context-completion problem\"，但没有精确定义这个 problem 是什么以及为什么 PF block 是比现有 step-level 方法更好的解法。具体建议：(1) 精确定义 context-completion problem——在 whole-proof 和普通 step-level formalization 中，每步的形式化依赖于前序所有步骤的正确形式化，构成一条 sequential error accumulation chain；任何一步形式化失败会导致后续所有步的 context 不完整，从而连锁失败。(2) 对比 PF block 与 Process-Driven Autoformalization (PDA, 2024) 的关键结构差异：PDA 是 step-level 但每步仍依赖 running Lean context（前序 `have`/`let` 声明），编译反馈只能修复当前步但无法消除跨步依赖；PF block 是 *closed-world* 形式化目标——所有 premise 显式声明，autoformalization 不需要推断或维护跨 block 的形式化上下文。(3) 这意味着 PF block 的形式化成功率在理论上独立于其他 block 的形式化结果，允许各 block *并行*独立形式化且互不影响——这是 step-level 方法做不到的。\n- 价值: 当前 Claim 1 的 framing 是 \"PF block 是 informal 和 formal 之间的自然桥梁\"。精确定义后变为 \"PF block 是已知唯一提供 closed-world 形式化属性的自然语言证明分解粒度，从根本上消除了限制 whole-proof 和普通 step-level autoformalization 的 sequential error accumulation\"。这将 Claim 1 从描述性观察提升为结构性定理级别的论断，大幅强化 Significance 和 Novelty。\n- 调研依据: Process-Driven Autoformalization (2024) 展示 step-level 优于 whole-proof，但其框架仍需 Lean compiler 的 running context feedback；ProofFlow (ICLR 2026) 展示 step-proof 的 ProofScore 仅 0.072 vs dependency-aware 的 0.545——这恰恰说明 step-level 本身不够，*结构化* 的分解（保留 dependency 信息、提供自包含 context）才是关键。PF block 正好提供了这种结构。\n\n【发掘点 3】\n- 维度: significance 提升 / novelty 锐化\n- 内容: **将 \"confident-but-wrong\" 分析从 ablation 提升为独立贡献，定位为对 LLM 数学验证可靠性的系统性诊断。** 当前 proposal 将 confident-but-wrong 分析放在 ablation 7 中（\"proportion of BV errors at >0.8 confidence\"）。但如果这一分析揭示了系统性模式——例如，某些数学领域（代数 vs 分析）、某些证明手法（构造性 vs 反证法）、某些 block 结构特征（引用定理数量、隐含假设密度）系统性地导致 BV 高置信度误判——这将成为一个独立有价值的发现。建议：(1) 对 confident-but-wrong cases 做结构化归因分析（数学领域、证明策略、block 复杂度特征），超越简单的比例统计；(2) 如果发现系统性模式，这就成为对 LLM 数学验证的 *failure mode taxonomy*——告诉领域研究者 \"在哪些场景下你不能信任 LLM 验证器的高置信度判断\"。这一发现的价值独立于本 proposal 的具体系统设计。\n- 价值: 将一个常规 ablation 变为一个独立 contribution，同时为 dual-signal routing 的必要性提供实证支撑（如果 confident-but-wrong 有系统性模式，单纯的 ensemble uncertainty 可能仍然不够，dependency criticality 作为 uncertainty-independent 信号的价值就被凸显）。这同时提升 Significance（对整个 LLM verification 领域的诊断价值）和 Novelty（现有工作未系统性地刻画 BV confident-but-wrong 的 failure modes）。\n- 调研依据: Hard2Verify (Pandit et al., 2025) 展示了 PRM 在难问题上的大幅性能下降（78.3%→37.3%），但只报告了 aggregate 数字而未分析 failure mode 的结构性模式。ThinkPRM (2025) 同样关注 overall performance 而非 failure mode 归因。将 confident-but-wrong 分析结构化将填补这一诊断空白。\n\nSources:\n- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)\n- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)\n- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)\n- [ProofFlow (ICLR 2026)](https://arxiv.org/abs/2510.15981)\n- [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/abs/2605.18796)\n- [Process-Driven Autoformalization in Lean 4](https://openreview.net/forum?id=k8KsI84Ds7)\n- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [Safe: Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)\n- [StepFun-Formalizer-32B](https://arxiv.org/abs/2508.04440)\n- [Goedel-Prover-V2 (ICLR 2026)](https://github.com/Goedel-LM/Goedel-Prover-V2)\n- [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760)\n- [Hard2Verify (2025)](https://arxiv.org/abs/2505.20047)\n\n【补救 agent 本轮输出】:\nNow I have sufficient research to evaluate the experimental design. Let me compile my analysis.\n\n---\n\n【状态】: 有缺陷待补救\n\n【前置调研发现】\n- **Safe (Liu et al., ACL 2025)**: 使用 FormalStep benchmark (30,809 formal statements) 评估单步形式化验证，在 miniF2F 上测试。Baseline 包含 self-consistency、PRM、LLM-as-Judge。评估指标为 per-step verification accuracy 和 end-to-end solution-level accuracy。\n- **Pseudo-Formalization (Barkallah et al., arXiv 2605.20531, 2026)**: 在 ArxivMathGradingBench (35 papers, 40 errors) 和 olympiad benchmark 上评估。Pareto-dominates LLM-as-judge baselines on error detection precision/recall。\n- **ThinkPRM (arXiv 2504.16828, 2025)**: 在 ProcessBench, MATH-500, AIME '24, GPQA-Diamond, LiveCodeBench 上评估。使用 best-of-N selection 和 reward-guided search 指标。Baseline 包含 discriminative PRM (PRM800K full data) 和 LLM-as-Judge。\n- **Ganguly et al. (NeurIPS 2025)**: 使用 PCFG-based localized entropy 实现 AUROC>0.93 的错误预测。实验设计核心是 selective verification 的 error reduction 与 abstention rate 的 trade-off curve。\n- **miniF2F-Lean Revisited (NeurIPS 2025)**: 人工验证发现 autoformalization accuracy 被 LLM 评估高估（97% LLM-judged → 66% human-reviewed）。End-to-end pipeline 在原版 miniF2F 上 ~35%，在修正版 miniF2F-v2 上 ~70%。\n- **StepFun-Formalizer-32B (AAAI 2026)**: Statement-level BEq@1 = 40.5% on FormalMATH-Lite, 26.7% on ProverBench。\n- **Goedel-Prover-V2-32B (ICLR 2026)**: miniF2F pass@32 = 88.1%（standard）, 90.4%（self-correction）。在 PutnamBench 上 86 problems at pass@184。\n- **Hard2Verify (Pandit et al., 2025)**: 评估 29 个 verifier，使用 PhD-expert step-level annotation。最强 PRM 从 78.3% 降到 37.3%。\n- **FormalProofBench (arXiv 2603.26996, 2026)**: Graduate-level formal proof，最佳模型 33.5% accuracy。评估 failure modes、cost、latency。\n- **BrokenMath (2025)**: 竞赛数学 benchmark，使用 LLM perturbation + expert review 构建 false statements。\n- **\"Do We Need Frontier Models\" (arXiv 2604.02450, 2026)**: Prompt ensemble 使 Qwen3.5-35B 与 Gemini 3.1 Pro 持平；accuracy boost up to 9.1%，self-consistency boost up to 15.9%。\n\n- **调研总结**: 该领域当前实验设计标准要求：(1) 至少覆盖 LLM-only verification (PRM/generative)、formal verification 两类 baseline；(2) 在竞赛级和研究级两个难度层上分别评估；(3) cost-performance Pareto 分析已成为惯例；(4) 审稿人普遍关注 benchmark 规模的统计显著性、calibration-evaluation 数据隔离、以及 autoformalization pipeline 各环节的 decomposed success rates。\n\n---\n\n【缺陷 1】\n- 类别: 评估方案缺陷\n- 问题: Proposal 中明确写道 Synthetic Error Detection Set \"Used for calibration and as co-primary evaluation benchmark\"——同一个数据集同时用于 Platt scaling 校准和作为主要评估 benchmark，存在 calibration-evaluation 数据泄漏风险。Platt scaling 的参数会在该分布上优化，导致 calibration quality 在该 benchmark 上的表现被系统性高估。这是审稿人几乎一定会指出的实验设计硬伤。\n- 严重度: 可补救\n- 补救方案: 将 Synthetic Error Detection Set 严格分为三个互不重叠的子集：(1) **calibration set**（~60%，用于 Platt scaling 参数拟合）；(2) **validation set**（~15%，用于超参选择和 early stopping）；(3) **evaluation set**（~25%，仅用于最终报告指标）。或者采用 5-fold cross-calibration：每轮用 4/5 做校准、1/5 做评估，报告 5 轮平均。后者利用数据更充分但需报告 fold 间方差。在论文中明确说明校准和评估数据零重叠。考虑到 synthetic set 总量仅 400-500，建议将总量提升到 600-800 以支持三路划分后各子集的统计可靠性。\n- 调研依据: Ganguly et al. (NeurIPS 2025) 在 selective verification 中使用独立的 held-out set 评估 uncertainty threshold 的效果；calibration 文献（Platt scaling, temperature scaling）标准做法均要求 calibration set 与 test set 严格分离。\n\n【缺陷 2】\n- 类别: 实验设计不足\n- 问题: ArxivMathGradingBench 仅含 35 papers、40 known errors，作为主要评估 benchmark 统计功效（statistical power）严重不足。假设方法 A 检出 30/40 错误、方法 B 检出 25/40 错误，McNemar's test 的 discordant pairs 可能仅 5-10 个，难以达到 p<0.05。Bootstrap CI (1000 resamples) 在 n=40 的离散二值数据上会产生很宽的置信区间。Proposal 声称的多方法对比（7 baselines + ablations）在此样本量下很难得出统计显著结论。\n- 严重度: 可补救\n- 补救方案: (1) **预注册 power analysis**: 基于 pilot study 估计的 effect size，计算 ArxivMathGradingBench 的 statistical power，明确报告并承认局限性。(2) **引入额外研究级 benchmark 或扩展评测集**: 考虑从 FormalProofBench (graduate-level proofs)、arXiv 勘误表中额外抽取论文构建补充评测集，或使用 BrokenMath 竞赛级 benchmark 作为补充。(3) **per-block 粒度分析**: 除 per-error detection 外，报告 per-block 粒度的 Tier 2 routing precision（routed blocks 中实际含错的比例），利用更大的 block 数量（~1050 blocks）提升统计功效。(4) **效应量报告优先于 p 值**: 在 n=40 的小样本场景下，强调 Cohen's h / odds ratio 等效应量指标和 bootstrap CI，弱化 p 值判断。\n- 调研依据: Hard2Verify (Pandit et al., 2025) 使用 500+ 小时人工标注获得更大规模的 step-level annotations；FormalProofBench (2026) 提供 graduate-level proofs 作为补充数据来源。领域内审稿人普遍关注 benchmark 规模是否支持声称的统计显著性。\n\n【缺陷 3】\n- 类别: 实验设计不足\n- 问题: Proposal 未讨论 **false positive 分析**——即系统将正确的 proof block 误判为含错时的后果和度量。对于验证系统，false positive 会直接损害用户信任。Proposal 仅报告 error detection precision/recall/F1，但未明确分析：(1) Tier 1 uncertainty routing 将多少正确 block 发送到 Tier 2；(2) Tier 2 formal verification 中有多少 autoformalization 失败或 proof search timeout 被误报为\"发现错误\"。尤其是 fallback strategy 中 \"reject\"（autoformalization 失败即判定有错）会产生大量 false positive。\n- 严重度: 可补救\n- 补救方案: (1) 增加 **per-tier false positive rate** 报告：Tier 1 routing 中被路由到 Tier 2 的 block 里实际无错的比例（routing false positive rate）；Tier 2 中 autoformalization 失败但原 block 实际正确的比例（formalization-failure false positive rate）。(2) 在 Pareto curve 中增加一条 **false positive rate vs. recall** 的权衡曲线，与 cost vs. recall 并列展示。(3) 在 ablation 4（fallback strategy）中，明确对比三种 fallback 的 false positive rate，而非仅对比 recall。\n- 调研依据: Safe (ACL 2025) 报告了 per-step verification accuracy（含 false positive 和 false negative 两个方向）；Hard2Verify (2025) 的评估协议区分了 missed errors 和 false alarms。基于领域实验规范判断，verification 系统必须同时报告两个方向的错误。\n\n【缺陷 4】\n- 类别: 实验设计不足\n- 问题: Proposal 提到 dependency graph criticality（fan-out degree, dominator nodes, betweenness centrality）作为 routing 的关键信号之一，但**未说明 dependency DAG 如何从 PF 分解中构建**。具体而言：(1) PF block 之间的依赖关系是由 LLM 在 PF 分解时自动标注的，还是需要额外的后处理步骤？(2) 依赖图的准确性如何验证——如果 LLM 生成的依赖关系有错（遗漏依赖或幻觉依赖），centrality 指标会失真。(3) Proposal 的 Claim 2 核心依赖 dual-signal routing，但如果 dependency graph 本身不可靠，criticality signal 的价值会大打折扣。\n- 严重度: 可补救\n- 补救方案: (1) 明确说明 dependency graph 构建流程（是 PF 分解的直接输出还是需要独立推断步骤）。(2) 增加 **dependency graph quality 的 human evaluation**: 在 pilot study 中对 50-100 个 PF blocks 的依赖图进行人工审核，报告 dependency precision/recall（是否遗漏真实依赖、是否包含虚假依赖）。(3) 在 ablation 2（routing signal）中，如果 dependency-only routing 表现差于 uncertainty-only，需讨论原因是否来自 dependency graph noise，而非 criticality signal 本身无效。\n- 调研依据: ProofFlow (2025) 使用 dependency graphs for autoformalization fidelity 但专门讨论了 graph construction accuracy 问题。基于领域实验规范判断，任何基于图结构的 routing 都需要验证图本身的质量。\n\n【缺陷 5】\n- 类别: 可行性问题\n- 问题: Pilot study 设定 go/no-go threshold 为 end-to-end success rate < 30%，但 proposal 未讨论 **30%-50% 的灰色地带**——这恰恰是最可能出现的区间。根据调研：StepFun-Formalizer-32B 在 FormalMATH-Lite 上 BEq@1 = 40.5%（statement-level），Goedel-Prover-V2 在 miniF2F 上 pass@32 = 88.1%，但 FormalProofBench 上最佳模型仅 33.5%。PF block 的 formalization 难度介于 statement-level（较简单，有标准化格式）和 full proof（很难）之间。如果 end-to-end 成功率落在 30%-50%，系统技术上可行但 routing 10-20% 的 blocks 中只有 30-50% 能完成形式验证，**Tier 2 的实际覆盖率可能仅有 3-10%**，对整体 error detection recall 的提升有限。\n- 严重度: 可补救\n- 补救方案: (1) 在 pilot study 中增加分级 decision matrix：<30% → 需要重新设计 Tier 2（如 multi-shot with compiler feedback）；30-50% → 可继续但需 adjust routing percentage upward（route 30-40% 而非 10-20%）以保证足够的 formalized blocks；50-70% → 按计划执行；>70% → 可降低 routing percentage。(2) 在 ablation 8（Tier 2 sensitivity analysis）中已有 30%/50%/70%/90% 的 parametric study，但应将其与 routing percentage sweep（ablation 5）做联合分析——生成 (routing %, Tier 2 success rate) → recall 的二维 Pareto surface。(3) 明确报告 **effective Tier 2 coverage**：实际完成形式验证的 block 占所有 block 的比例，而非仅报告 routing percentage。\n- 调研依据: StepFun-Formalizer-32B (AAAI 2026) 的 40.5% BEq@1 和 FormalProofBench (2026) 的 33.5% 表明 block-level autoformalization 成功率很可能落在灰色地带。miniF2F-Lean Revisited (NeurIPS 2025) 的核心发现就是 pipeline 各环节成功率的乘积效应导致 end-to-end 大幅下降。\n\n【缺陷 6】\n- 类别: baseline 不足或过时\n- 问题: Proposal 列出 7 个 baseline，覆盖面已经较好，但存在两个缺口：(1) **缺少 frontier LLM single-pass verification baseline**（如 Claude Sonnet 4.5 thinking 或 Gemini 2.5 Pro 直接做 proof verification）。\"Do We Need Frontier Models\" (2026) 的核心发现是 prompt ensemble 可以让小模型逼近 frontier model，但 proposal 应该包含 frontier model 作为 **upper bound reference** 以量化 LLM-only verification 的天花板。(2) **HERMES baseline 的适用性存疑**: Proposal 标注 \"if applicable to verification setting\"，但 HERMES 是 proof generation tool（在生成过程中做 formal checking），不是 post-hoc verification tool，两者的 setting 根本不同。将一个 generation tool 作为 verification baseline 在实验设计上不太严谨，审稿人可能质疑。\n- 严重度: 可补救\n- 补救方案: (1) 增加 **frontier LLM direct verification** baseline（如 GPT-5 或 Claude Sonnet 4.5 single-pass proof verification），作为 LLM-only ceiling reference。成本可控——仅需在评估集上 single-pass inference。(2) 对 HERMES 做二选一决策：如果确实能改造为 verification 模式（给定 proof，逐步 formalize 并检查），保留并详细说明改造方法；否则移除，避免审稿人质疑 baseline 对比的公平性。可替换为 **stepproof (2025)** 或 **\"Pessimistic Verification\" (2025)** 等更直接的 verification-setting 方法。\n- 调研依据: \"Do We Need Frontier Models\" (arXiv 2604.02450, 2026) 明确展示 frontier model vs. smaller model 在 proof verification 上的差距和 prompt ensemble 的补偿效果；Hard2Verify (2025) 评估了 29 个 verifier 包括 frontier models，这是领域标准做法。\n\n【缺陷 7】\n- 类别: 评估方案缺陷\n- 问题: Proposal 的三个 benchmark（ArxivMathGradingBench、Synthetic Error Detection Set、miniF2F Verification Protocol）在数学难度分布上存在覆盖偏差：ArxivMathGradingBench 是研究级，miniF2F 是竞赛级（高中/本科竞赛），Synthetic Set 从 Hard2Verify 竞赛级问题构建。**缺少 graduate/undergraduate textbook-level 的中等难度评估**。这意味着系统在\"中等难度、非竞赛、非前沿研究\"这一最常见使用场景下的表现未被评估。同时，miniF2F Verification Protocol 的 focus 是 verification precision/recall（验证 LLM 生成的候选证明），与 ArxivMathGradingBench 的 focus（检测人类证明中的错误）是不同的 task，二者的 metric 不完全可比。\n- 严重度: 可补救\n- 补救方案: (1) 考虑增加一个 **中等难度 benchmark** 如 MATH dataset (competition math, well-studied) 或 FormalProofBench subset (graduate-level textbook proofs)。(2) 如果资源有限，至少在 paper discussion section 中明确承认难度分布的覆盖偏差，并说明 generalization 限制。(3) 更清晰地区分两个评测 setting 的定义：**error detection setting**（输入：可能含错的证明 → 输出：哪里有错）vs. **solution selection setting**（输入：多个候选证明 → 输出：哪个正确）。miniF2F protocol 属于后者，而 ArxivMathGradingBench 属于前者，两者应分开报告而非混合比较。\n- 调研依据: ThinkPRM (2025) 在 ProcessBench, MATH-500, AIME '24, GPQA-Diamond, LiveCodeBench 五个不同难度的 benchmark 上评估；Hard2Verify (2025) 专门设计覆盖 frontier difficulty。领域标准是至少覆盖两个以上难度层级。\n\n【缺陷 8】\n- 类别: ablation 不完整\n- 问题: Proposal 使用 QwQ-32B 作为 Tier 1 BV 的 backbone model，但未设计 **BV backbone model ablation**。\"Do We Need Frontier Models\" (2026) 的核心发现是不同模型在 proof verification 上表现差异巨大（up to ~25% in self-consistency），且 prompt ensemble 可以补偿小模型的不足。Proposal 的 uncertainty calibration 质量（ensemble disagreement）高度依赖 BV backbone 的能力——如果 backbone 太弱，5 个 copy 可能一致地错误（confident-but-wrong），如果太强，ensemble disagreement 信号可能太弱以至于无法有效 routing。\n- 严重度: 可补救\n- 补救方案: (1) 至少增加一个 **alternative BV backbone** 的对比实验（如 Qwen3.5-35B 或其他同规模 reasoning model），评估 backbone 选择对 calibration quality（ECE）和 routing effectiveness（recall@fixed-cost）的影响。(2) 如果计算资源有限，可在 synthetic set 上用较低 ensemble size (N=3) 做此对比，作为 supplementary experiment。(3) 报告 ensemble disagreement rate 的分布——如果 QwQ-32B 的 5 copies 在 >90% 的 blocks 上完全一致，说明 ensemble 信号过弱，需要 mixed-model ensemble 或更大 temperature。\n- 调研依据: \"Do We Need Frontier Models\" (arXiv 2604.02450, 2026) 系统性地评估了不同规模模型在 proof verification 上的差异和 prompt ensemble 的补偿效果。\n\nSources:\n- [Safe: Enhancing Mathematical Reasoning in LLMs via Retrospective Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/)\n- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)\n- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks](https://arxiv.org/abs/2505.20047)\n- [miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward](https://arxiv.org/abs/2511.03108)\n- [StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs](https://arxiv.org/abs/2508.04440)\n- [Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction](https://arxiv.org/abs/2508.03613)\n- [Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math](https://arxiv.org/abs/2510.13744)\n- [FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?](https://arxiv.org/abs/2603.26996)\n- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450)\n- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)"
}
```

---

### Runtime record

_source line 59 · 2026-05-27T13:06:31.600Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T13:06:31.600Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

## Round 4

22 recorded events

### User

_source line 60 · 2026-05-27T13:06:31.628Z_

【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。

【发掘 agent 本轮输出】:
Now I have enough research to provide a thorough analysis. Let me compile my findings.

【状态】: 有发掘空间

【前置调研发现】
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531) (arXiv, May 2026): 本 proposal 的直接基础。PF 将证明分解为自包含模块，每个模块显式声明前提、结论和证明。Block Verification 在 ArxivMathGradingBench 上 Pareto-dominates LLM-as-judge 但仍遗漏 ~50% 的错误。该论文发表仅 8 天（相对于今天 2026-05-27），说明 proposal 紧跟前沿。
- [Grammars of Formal Uncertainty](https://arxiv.org/abs/2505.20047) (NeurIPS 2025): 最接近的竞争者。用 PCFG 建模 LLM→SMT-LIB 的生成端不确定性，实现选择性验证，误差降低 14-100%。proposal 声称的三维差异化（不确定性来源、跨范式路由、结构关键性）经调研确认为真实差异，非表面区分。
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055) (arXiv 2026): 在 first-order logic claims 上跨验证范式路由（SMT solver vs LLM ensemble），使用 claim 类型（logical vs commonsense）而非不确定性作为路由信号。这是架构层面最接近的系统——都是跨范式路由。
- [ProofFlow](https://arxiv.org/abs/2510.15981) (ICLR 2026): 用依赖 DAG 保持 autoformalization 的结构忠实度，ProofScore 0.545 远超 whole-proof (0.123) 和 step-proof (0.072)。验证了依赖图结构在证明形式化中的价值，但用途不同：ProofFlow 用于 autoformalization 忠实度，proposal 用于验证路由。
- [UCCI](https://arxiv.org/abs/2605.18796) (arXiv, May 2026): 用 isotonic regression 校准 token-level margin uncertainty 做 LLM cascade routing。方法论高度相关但路由目标不同（小模型→大模型 vs LLM verification→formal verification）。
- [Process-Driven Autoformalization in Lean 4](https://openreview.net/forum?id=k8KsI84Ds7) (2024): 展示 step-level formalization + compiler feedback 优于 whole-proof。部分支持 proposal 的核心假设，但 PDA 的 step-level 仍需维护 running context，与 PF block 的完全自包含不同。
- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450) (arXiv 2026): 通过 specialized prompt ensemble，小模型可达到 frontier 模型的验证水平（准确率提升 9.1%，一致性提升 15.9%）。这提升了 LLM-only verification 的天花板，但 proposal 已将此纳入 baseline。
- [ThinkPRM](https://arxiv.org/abs/2504.16828) (2025): 用 1% 的 process labels 训练的 verbalized PRM 超过 discriminative PRM。代表当前最强的 step-level LLM verifier。
- [StepFun-Formalizer-32B](https://arxiv.org/abs/2508.04440) / [Goedel-Prover-V2](https://github.com/Goedel-LM/Goedel-Prover-V2) (ICLR 2026): Proposal 选用的具体工具链。StepFun-Formalizer BEq@1 40.5% on FormalMATH-Lite；Goedel-Prover-V2 MiniF2F pass@32 达 88.1%。工具选型合理。
- 调研总结: 该领域当前的突破方向有两条：(1) 降低 autoformalization 粒度（whole-proof → step-level → block-level）以提高成功率；(2) 用不确定性信号做选择性验证以降低成本。本 proposal 的核心 insight 在于将这两条线索交叉：用 PF block 作为最佳粒度单位，用不确定性+结构关键性做选择性路由。这个交叉点目前尚无人占据。

---

【发掘点 1】
- 维度: 核心 claim 强化 / novelty 锐化
- 内容: **将 dual-signal routing 重新表述为决策论风险最小化框架。** 当前 proposal 将 uncertainty × dependency criticality 呈现为工程组合（"dual signal mitigates confident-but-wrong risk"）。但这其实是一个决策论问题的自然解：每个 block b 的验证路由决策应最小化 Expected Verification Loss = P(BV_error | b) × C(error | b)，其中 P 由校准后的 ensemble uncertainty 估计，C 由依赖图关键性（b 的传递可达 block 数量 × 各下游 block 的 uncertainty 权重）估计。当 E[Loss] 超过 formal verification 的边际成本时路由到 Tier 2。这个重新表述的价值在于：(1) 将两个看似 ad hoc 的信号统一为一个有原则的目标函数；(2) 路由阈值不再是超参数，而是成本-风险均衡的自然结果；(3) 与 Ganguly 等人的差异变得更本质——他们优化的是 abstention policy（是否验证），你优化的是 cross-tier routing policy（如何验证），目标函数的结构完全不同。
- 价值: 这一重新表述将 Novelty 从 "组合了两个信号" 提升为 "提出了一个有原则的跨范式验证路由框架"。审稿人面对 "我们把 A 和 B 乘在一起" 容易说 "trivial combination"；面对 "我们定义了一个风险最小化目标，A 和 B 分别估计目标的两个因子" 则很难说 trivial。
- 调研依据: UCCI (arXiv 2605.18796) 将校准后的 uncertainty 直接连接到 cost-optimal escalation threshold，用约束优化选择路由阈值——这验证了 "校准 uncertainty → 成本最优路由" 这一范式在 LLM routing 中的有效性。本建议将同样的原则扩展到 cross-paradigm verification routing，并引入 cost-of-error 维度。

【发掘点 2】
- 维度: 核心 claim 强化 / significance 提升
- 内容: **精确定义 "context-completion problem" 并将其作为 Claim 1 的理论核心，明确 PF block 与现有 step-level 方法的结构差异。** 当前 proposal 说 PF block 的 "self-contained nature eliminates the context-completion problem"，但没有精确定义这个 problem 是什么以及为什么 PF block 是比现有 step-level 方法更好的解法。具体建议：(1) 精确定义 context-completion problem——在 whole-proof 和普通 step-level formalization 中，每步的形式化依赖于前序所有步骤的正确形式化，构成一条 sequential error accumulation chain；任何一步形式化失败会导致后续所有步的 context 不完整，从而连锁失败。(2) 对比 PF block 与 Process-Driven Autoformalization (PDA, 2024) 的关键结构差异：PDA 是 step-level 但每步仍依赖 running Lean context（前序 `have`/`let` 声明），编译反馈只能修复当前步但无法消除跨步依赖；PF block 是 *closed-world* 形式化目标——所有 premise 显式声明，autoformalization 不需要推断或维护跨 block 的形式化上下文。(3) 这意味着 PF block 的形式化成功率在理论上独立于其他 block 的形式化结果，允许各 block *并行*独立形式化且互不影响——这是 step-level 方法做不到的。
- 价值: 当前 Claim 1 的 framing 是 "PF block 是 informal 和 formal 之间的自然桥梁"。精确定义后变为 "PF block 是已知唯一提供 closed-world 形式化属性的自然语言证明分解粒度，从根本上消除了限制 whole-proof 和普通 step-level autoformalization 的 sequential error accumulation"。这将 Claim 1 从描述性观察提升为结构性定理级别的论断，大幅强化 Significance 和 Novelty。
- 调研依据: Process-Driven Autoformalization (2024) 展示 step-level 优于 whole-proof，但其框架仍需 Lean compiler 的 running context feedback；ProofFlow (ICLR 2026) 展示 step-proof 的 ProofScore 仅 0.072 vs dependency-aware 的 0.545——这恰恰说明 step-level 本身不够，*结构化* 的分解（保留 dependency 信息、提供自包含 context）才是关键。PF block 正好提供了这种结构。

【发掘点 3】
- 维度: significance 提升 / novelty 锐化
- 内容: **将 "confident-but-wrong" 分析从 ablation 提升为独立贡献，定位为对 LLM 数学验证可靠性的系统性诊断。** 当前 proposal 将 confident-but-wrong 分析放在 ablation 7 中（"proportion of BV errors at >0.8 confidence"）。但如果这一分析揭示了系统性模式——例如，某些数学领域（代数 vs 分析）、某些证明手法（构造性 vs 反证法）、某些 block 结构特征（引用定理数量、隐含假设密度）系统性地导致 BV 高置信度误判——这将成为一个独立有价值的发现。建议：(1) 对 confident-but-wrong cases 做结构化归因分析（数学领域、证明策略、block 复杂度特征），超越简单的比例统计；(2) 如果发现系统性模式，这就成为对 LLM 数学验证的 *failure mode taxonomy*——告诉领域研究者 "在哪些场景下你不能信任 LLM 验证器的高置信度判断"。这一发现的价值独立于本 proposal 的具体系统设计。
- 价值: 将一个常规 ablation 变为一个独立 contribution，同时为 dual-signal routing 的必要性提供实证支撑（如果 confident-but-wrong 有系统性模式，单纯的 ensemble uncertainty 可能仍然不够，dependency criticality 作为 uncertainty-independent 信号的价值就被凸显）。这同时提升 Significance（对整个 LLM verification 领域的诊断价值）和 Novelty（现有工作未系统性地刻画 BV confident-but-wrong 的 failure modes）。
- 调研依据: Hard2Verify (Pandit et al., 2025) 展示了 PRM 在难问题上的大幅性能下降（78.3%→37.3%），但只报告了 aggregate 数字而未分析 failure mode 的结构性模式。ThinkPRM (2025) 同样关注 overall performance 而非 failure mode 归因。将 confident-but-wrong 分析结构化将填补这一诊断空白。

Sources:
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)
- [Grammars of Formal Uncertainty (NeurIPS 2025)](https://arxiv.org/abs/2505.20047)
- [VERGE: Formal Refinement and Guidance Engine](https://arxiv.org/abs/2601.20055)
- [ProofFlow (ICLR 2026)](https://arxiv.org/abs/2510.15981)
- [UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing](https://arxiv.org/abs/2605.18796)
- [Process-Driven Autoformalization in Lean 4](https://openreview.net/forum?id=k8KsI84Ds7)
- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [Safe: Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)
- [StepFun-Formalizer-32B](https://arxiv.org/abs/2508.04440)
- [Goedel-Prover-V2 (ICLR 2026)](https://github.com/Goedel-LM/Goedel-Prover-V2)
- [HERMES (ICML 2026)](https://arxiv.org/abs/2511.18760)
- [Hard2Verify (2025)](https://arxiv.org/abs/2505.20047)

【补救 agent 本轮输出】:
Now I have sufficient research to evaluate the experimental design. Let me compile my analysis.

---

【状态】: 有缺陷待补救

【前置调研发现】
- **Safe (Liu et al., ACL 2025)**: 使用 FormalStep benchmark (30,809 formal statements) 评估单步形式化验证，在 miniF2F 上测试。Baseline 包含 self-consistency、PRM、LLM-as-Judge。评估指标为 per-step verification accuracy 和 end-to-end solution-level accuracy。
- **Pseudo-Formalization (Barkallah et al., arXiv 2605.20531, 2026)**: 在 ArxivMathGradingBench (35 papers, 40 errors) 和 olympiad benchmark 上评估。Pareto-dominates LLM-as-judge baselines on error detection precision/recall。
- **ThinkPRM (arXiv 2504.16828, 2025)**: 在 ProcessBench, MATH-500, AIME '24, GPQA-Diamond, LiveCodeBench 上评估。使用 best-of-N selection 和 reward-guided search 指标。Baseline 包含 discriminative PRM (PRM800K full data) 和 LLM-as-Judge。
- **Ganguly et al. (NeurIPS 2025)**: 使用 PCFG-based localized entropy 实现 AUROC>0.93 的错误预测。实验设计核心是 selective verification 的 error reduction 与 abstention rate 的 trade-off curve。
- **miniF2F-Lean Revisited (NeurIPS 2025)**: 人工验证发现 autoformalization accuracy 被 LLM 评估高估（97% LLM-judged → 66% human-reviewed）。End-to-end pipeline 在原版 miniF2F 上 ~35%，在修正版 miniF2F-v2 上 ~70%。
- **StepFun-Formalizer-32B (AAAI 2026)**: Statement-level BEq@1 = 40.5% on FormalMATH-Lite, 26.7% on ProverBench。
- **Goedel-Prover-V2-32B (ICLR 2026)**: miniF2F pass@32 = 88.1%（standard）, 90.4%（self-correction）。在 PutnamBench 上 86 problems at pass@184。
- **Hard2Verify (Pandit et al., 2025)**: 评估 29 个 verifier，使用 PhD-expert step-level annotation。最强 PRM 从 78.3% 降到 37.3%。
- **FormalProofBench (arXiv 2603.26996, 2026)**: Graduate-level formal proof，最佳模型 33.5% accuracy。评估 failure modes、cost、latency。
- **BrokenMath (2025)**: 竞赛数学 benchmark，使用 LLM perturbation + expert review 构建 false statements。
- **"Do We Need Frontier Models" (arXiv 2604.02450, 2026)**: Prompt ensemble 使 Qwen3.5-35B 与 Gemini 3.1 Pro 持平；accuracy boost up to 9.1%，self-consistency boost up to 15.9%。

- **调研总结**: 该领域当前实验设计标准要求：(1) 至少覆盖 LLM-only verification (PRM/generative)、formal verification 两类 baseline；(2) 在竞赛级和研究级两个难度层上分别评估；(3) cost-performance Pareto 分析已成为惯例；(4) 审稿人普遍关注 benchmark 规模的统计显著性、calibration-evaluation 数据隔离、以及 autoformalization pipeline 各环节的 decomposed success rates。

---

【缺陷 1】
- 类别: 评估方案缺陷
- 问题: Proposal 中明确写道 Synthetic Error Detection Set "Used for calibration and as co-primary evaluation benchmark"——同一个数据集同时用于 Platt scaling 校准和作为主要评估 benchmark，存在 calibration-evaluation 数据泄漏风险。Platt scaling 的参数会在该分布上优化，导致 calibration quality 在该 benchmark 上的表现被系统性高估。这是审稿人几乎一定会指出的实验设计硬伤。
- 严重度: 可补救
- 补救方案: 将 Synthetic Error Detection Set 严格分为三个互不重叠的子集：(1) **calibration set**（~60%，用于 Platt scaling 参数拟合）；(2) **validation set**（~15%，用于超参选择和 early stopping）；(3) **evaluation set**（~25%，仅用于最终报告指标）。或者采用 5-fold cross-calibration：每轮用 4/5 做校准、1/5 做评估，报告 5 轮平均。后者利用数据更充分但需报告 fold 间方差。在论文中明确说明校准和评估数据零重叠。考虑到 synthetic set 总量仅 400-500，建议将总量提升到 600-800 以支持三路划分后各子集的统计可靠性。
- 调研依据: Ganguly et al. (NeurIPS 2025) 在 selective verification 中使用独立的 held-out set 评估 uncertainty threshold 的效果；calibration 文献（Platt scaling, temperature scaling）标准做法均要求 calibration set 与 test set 严格分离。

【缺陷 2】
- 类别: 实验设计不足
- 问题: ArxivMathGradingBench 仅含 35 papers、40 known errors，作为主要评估 benchmark 统计功效（statistical power）严重不足。假设方法 A 检出 30/40 错误、方法 B 检出 25/40 错误，McNemar's test 的 discordant pairs 可能仅 5-10 个，难以达到 p<0.05。Bootstrap CI (1000 resamples) 在 n=40 的离散二值数据上会产生很宽的置信区间。Proposal 声称的多方法对比（7 baselines + ablations）在此样本量下很难得出统计显著结论。
- 严重度: 可补救
- 补救方案: (1) **预注册 power analysis**: 基于 pilot study 估计的 effect size，计算 ArxivMathGradingBench 的 statistical power，明确报告并承认局限性。(2) **引入额外研究级 benchmark 或扩展评测集**: 考虑从 FormalProofBench (graduate-level proofs)、arXiv 勘误表中额外抽取论文构建补充评测集，或使用 BrokenMath 竞赛级 benchmark 作为补充。(3) **per-block 粒度分析**: 除 per-error detection 外，报告 per-block 粒度的 Tier 2 routing precision（routed blocks 中实际含错的比例），利用更大的 block 数量（~1050 blocks）提升统计功效。(4) **效应量报告优先于 p 值**: 在 n=40 的小样本场景下，强调 Cohen's h / odds ratio 等效应量指标和 bootstrap CI，弱化 p 值判断。
- 调研依据: Hard2Verify (Pandit et al., 2025) 使用 500+ 小时人工标注获得更大规模的 step-level annotations；FormalProofBench (2026) 提供 graduate-level proofs 作为补充数据来源。领域内审稿人普遍关注 benchmark 规模是否支持声称的统计显著性。

【缺陷 3】
- 类别: 实验设计不足
- 问题: Proposal 未讨论 **false positive 分析**——即系统将正确的 proof block 误判为含错时的后果和度量。对于验证系统，false positive 会直接损害用户信任。Proposal 仅报告 error detection precision/recall/F1，但未明确分析：(1) Tier 1 uncertainty routing 将多少正确 block 发送到 Tier 2；(2) Tier 2 formal verification 中有多少 autoformalization 失败或 proof search timeout 被误报为"发现错误"。尤其是 fallback strategy 中 "reject"（autoformalization 失败即判定有错）会产生大量 false positive。
- 严重度: 可补救
- 补救方案: (1) 增加 **per-tier false positive rate** 报告：Tier 1 routing 中被路由到 Tier 2 的 block 里实际无错的比例（routing false positive rate）；Tier 2 中 autoformalization 失败但原 block 实际正确的比例（formalization-failure false positive rate）。(2) 在 Pareto curve 中增加一条 **false positive rate vs. recall** 的权衡曲线，与 cost vs. recall 并列展示。(3) 在 ablation 4（fallback strategy）中，明确对比三种 fallback 的 false positive rate，而非仅对比 recall。
- 调研依据: Safe (ACL 2025) 报告了 per-step verification accuracy（含 false positive 和 false negative 两个方向）；Hard2Verify (2025) 的评估协议区分了 missed errors 和 false alarms。基于领域实验规范判断，verification 系统必须同时报告两个方向的错误。

【缺陷 4】
- 类别: 实验设计不足
- 问题: Proposal 提到 dependency graph criticality（fan-out degree, dominator nodes, betweenness centrality）作为 routing 的关键信号之一，但**未说明 dependency DAG 如何从 PF 分解中构建**。具体而言：(1) PF block 之间的依赖关系是由 LLM 在 PF 分解时自动标注的，还是需要额外的后处理步骤？(2) 依赖图的准确性如何验证——如果 LLM 生成的依赖关系有错（遗漏依赖或幻觉依赖），centrality 指标会失真。(3) Proposal 的 Claim 2 核心依赖 dual-signal routing，但如果 dependency graph 本身不可靠，criticality signal 的价值会大打折扣。
- 严重度: 可补救
- 补救方案: (1) 明确说明 dependency graph 构建流程（是 PF 分解的直接输出还是需要独立推断步骤）。(2) 增加 **dependency graph quality 的 human evaluation**: 在 pilot study 中对 50-100 个 PF blocks 的依赖图进行人工审核，报告 dependency precision/recall（是否遗漏真实依赖、是否包含虚假依赖）。(3) 在 ablation 2（routing signal）中，如果 dependency-only routing 表现差于 uncertainty-only，需讨论原因是否来自 dependency graph noise，而非 criticality signal 本身无效。
- 调研依据: ProofFlow (2025) 使用 dependency graphs for autoformalization fidelity 但专门讨论了 graph construction accuracy 问题。基于领域实验规范判断，任何基于图结构的 routing 都需要验证图本身的质量。

【缺陷 5】
- 类别: 可行性问题
- 问题: Pilot study 设定 go/no-go threshold 为 end-to-end success rate < 30%，但 proposal 未讨论 **30%-50% 的灰色地带**——这恰恰是最可能出现的区间。根据调研：StepFun-Formalizer-32B 在 FormalMATH-Lite 上 BEq@1 = 40.5%（statement-level），Goedel-Prover-V2 在 miniF2F 上 pass@32 = 88.1%，但 FormalProofBench 上最佳模型仅 33.5%。PF block 的 formalization 难度介于 statement-level（较简单，有标准化格式）和 full proof（很难）之间。如果 end-to-end 成功率落在 30%-50%，系统技术上可行但 routing 10-20% 的 blocks 中只有 30-50% 能完成形式验证，**Tier 2 的实际覆盖率可能仅有 3-10%**，对整体 error detection recall 的提升有限。
- 严重度: 可补救
- 补救方案: (1) 在 pilot study 中增加分级 decision matrix：<30% → 需要重新设计 Tier 2（如 multi-shot with compiler feedback）；30-50% → 可继续但需 adjust routing percentage upward（route 30-40% 而非 10-20%）以保证足够的 formalized blocks；50-70% → 按计划执行；>70% → 可降低 routing percentage。(2) 在 ablation 8（Tier 2 sensitivity analysis）中已有 30%/50%/70%/90% 的 parametric study，但应将其与 routing percentage sweep（ablation 5）做联合分析——生成 (routing %, Tier 2 success rate) → recall 的二维 Pareto surface。(3) 明确报告 **effective Tier 2 coverage**：实际完成形式验证的 block 占所有 block 的比例，而非仅报告 routing percentage。
- 调研依据: StepFun-Formalizer-32B (AAAI 2026) 的 40.5% BEq@1 和 FormalProofBench (2026) 的 33.5% 表明 block-level autoformalization 成功率很可能落在灰色地带。miniF2F-Lean Revisited (NeurIPS 2025) 的核心发现就是 pipeline 各环节成功率的乘积效应导致 end-to-end 大幅下降。

【缺陷 6】
- 类别: baseline 不足或过时
- 问题: Proposal 列出 7 个 baseline，覆盖面已经较好，但存在两个缺口：(1) **缺少 frontier LLM single-pass verification baseline**（如 Claude Sonnet 4.5 thinking 或 Gemini 2.5 Pro 直接做 proof verification）。"Do We Need Frontier Models" (2026) 的核心发现是 prompt ensemble 可以让小模型逼近 frontier model，但 proposal 应该包含 frontier model 作为 **upper bound reference** 以量化 LLM-only verification 的天花板。(2) **HERMES baseline 的适用性存疑**: Proposal 标注 "if applicable to verification setting"，但 HERMES 是 proof generation tool（在生成过程中做 formal checking），不是 post-hoc verification tool，两者的 setting 根本不同。将一个 generation tool 作为 verification baseline 在实验设计上不太严谨，审稿人可能质疑。
- 严重度: 可补救
- 补救方案: (1) 增加 **frontier LLM direct verification** baseline（如 GPT-5 或 Claude Sonnet 4.5 single-pass proof verification），作为 LLM-only ceiling reference。成本可控——仅需在评估集上 single-pass inference。(2) 对 HERMES 做二选一决策：如果确实能改造为 verification 模式（给定 proof，逐步 formalize 并检查），保留并详细说明改造方法；否则移除，避免审稿人质疑 baseline 对比的公平性。可替换为 **stepproof (2025)** 或 **"Pessimistic Verification" (2025)** 等更直接的 verification-setting 方法。
- 调研依据: "Do We Need Frontier Models" (arXiv 2604.02450, 2026) 明确展示 frontier model vs. smaller model 在 proof verification 上的差距和 prompt ensemble 的补偿效果；Hard2Verify (2025) 评估了 29 个 verifier 包括 frontier models，这是领域标准做法。

【缺陷 7】
- 类别: 评估方案缺陷
- 问题: Proposal 的三个 benchmark（ArxivMathGradingBench、Synthetic Error Detection Set、miniF2F Verification Protocol）在数学难度分布上存在覆盖偏差：ArxivMathGradingBench 是研究级，miniF2F 是竞赛级（高中/本科竞赛），Synthetic Set 从 Hard2Verify 竞赛级问题构建。**缺少 graduate/undergraduate textbook-level 的中等难度评估**。这意味着系统在"中等难度、非竞赛、非前沿研究"这一最常见使用场景下的表现未被评估。同时，miniF2F Verification Protocol 的 focus 是 verification precision/recall（验证 LLM 生成的候选证明），与 ArxivMathGradingBench 的 focus（检测人类证明中的错误）是不同的 task，二者的 metric 不完全可比。
- 严重度: 可补救
- 补救方案: (1) 考虑增加一个 **中等难度 benchmark** 如 MATH dataset (competition math, well-studied) 或 FormalProofBench subset (graduate-level textbook proofs)。(2) 如果资源有限，至少在 paper discussion section 中明确承认难度分布的覆盖偏差，并说明 generalization 限制。(3) 更清晰地区分两个评测 setting 的定义：**error detection setting**（输入：可能含错的证明 → 输出：哪里有错）vs. **solution selection setting**（输入：多个候选证明 → 输出：哪个正确）。miniF2F protocol 属于后者，而 ArxivMathGradingBench 属于前者，两者应分开报告而非混合比较。
- 调研依据: ThinkPRM (2025) 在 ProcessBench, MATH-500, AIME '24, GPQA-Diamond, LiveCodeBench 五个不同难度的 benchmark 上评估；Hard2Verify (2025) 专门设计覆盖 frontier difficulty。领域标准是至少覆盖两个以上难度层级。

【缺陷 8】
- 类别: ablation 不完整
- 问题: Proposal 使用 QwQ-32B 作为 Tier 1 BV 的 backbone model，但未设计 **BV backbone model ablation**。"Do We Need Frontier Models" (2026) 的核心发现是不同模型在 proof verification 上表现差异巨大（up to ~25% in self-consistency），且 prompt ensemble 可以补偿小模型的不足。Proposal 的 uncertainty calibration 质量（ensemble disagreement）高度依赖 BV backbone 的能力——如果 backbone 太弱，5 个 copy 可能一致地错误（confident-but-wrong），如果太强，ensemble disagreement 信号可能太弱以至于无法有效 routing。
- 严重度: 可补救
- 补救方案: (1) 至少增加一个 **alternative BV backbone** 的对比实验（如 Qwen3.5-35B 或其他同规模 reasoning model），评估 backbone 选择对 calibration quality（ECE）和 routing effectiveness（recall@fixed-cost）的影响。(2) 如果计算资源有限，可在 synthetic set 上用较低 ensemble size (N=3) 做此对比，作为 supplementary experiment。(3) 报告 ensemble disagreement rate 的分布——如果 QwQ-32B 的 5 copies 在 >90% 的 blocks 上完全一致，说明 ensemble 信号过弱，需要 mixed-model ensemble 或更大 temperature。
- 调研依据: "Do We Need Frontier Models" (arXiv 2604.02450, 2026) 系统性地评估了不同规模模型在 proof verification 上的差异和 prompt ensemble 的补偿效果。

Sources:
- [Safe: Enhancing Mathematical Reasoning in LLMs via Retrospective Step-aware Formal Verification](https://aclanthology.org/2025.acl-long.594/)
- [Pseudo-Formalization for Automatic Proof Verification](https://arxiv.org/abs/2605.20531)
- [ThinkPRM: Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks](https://arxiv.org/abs/2505.20047)
- [miniF2F-Lean Revisited: Reviewing Limitations and Charting a Path Forward](https://arxiv.org/abs/2511.03108)
- [StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs](https://arxiv.org/abs/2508.04440)
- [Goedel-Prover-V2: Scaling Formal Theorem Proving with Scaffolded Data Synthesis and Self-Correction](https://arxiv.org/abs/2508.03613)
- [Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math](https://arxiv.org/abs/2510.13744)
- [FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?](https://arxiv.org/abs/2603.26996)
- [Do We Need Frontier Models to Verify Mathematical Proofs?](https://arxiv.org/abs/2604.02450)
- [Process-Driven Autoformalization in Lean 4](https://arxiv.org/abs/2406.01940)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db99ca56-79c5-400c-bdb4-c4de252836dd",
  "isSidechain": false,
  "promptId": "7f8dad30-780f-45d2-b4c1-07d90064adf1",
  "type": "user",
  "uuid": "640a6280-b2a9-4616-a5f9-3dd653043ab1",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research to provide a thorough analysis. Let me compile my findings.  【状态】: 有发掘空间  【前置调研发…",
  "leafUuid": "640a6280-b2a9-4616-a5f9-3dd653043ab1",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Assistant

_source line 63 · 2026-05-27T13:07:20.494Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze Round 3 worker outputs carefully.

**发掘 agent Round 3 (3 points):**

1. **Decision-theoretic reframing of dual-signal routing**: Recast uncertainty × dependency criticality as Expected Verification Loss = P(BV_error|b) × C(error|b), where P is calibrated uncertainty and C is dependency criticality. This unifies the two signals into a principled objective function rather than an ad-hoc combination.

2. **Precise definition of "context-completion problem" and PF block's "closed-world" property**: PF blocks provide closed-world formalization targets (all premises explicit, no running context needed), which is structurally distinct from PDA's step-level approach (still needs running Lean context). This means PF blocks can be formalized independently and in parallel.
   
3. **Confident-but-wrong analysis as a failure mode taxonomy**: I should structure the patterns where the verifier is confident but incorrect as a systematic taxonomy across mathematical domains, proof strategies, and block complexity features, treating it as an independent contribution to understanding LLM verification limitations.

**补救 agent Round 3 (8 defects):**

1. **Calibration-evaluation data leakage**: Synthetic set used for both calibration and evaluation — need strict separation.
2. **ArxivMathGradingBench statistical power** (repeated from previous rounds, more specific suggestions).
3. **False positive analysis missing**: Need per-tier false positive rates.
4. **Dependency DAG construction not specified**: How is it built? How accurate is it?
5. **30

-50% gray zone for pilot study**: Need graded decision matrix, not just binary go/no-go.
6. **Baseline gaps**: Missing frontier LLM baseline; HERMES applicability questionable.
7. **Difficulty distribution coverage bias**: Missing medium-difficulty (textbook-level) evaluation.
8. **BV backbone model ablation missing**: Need to test with alternative backbone model.

Now I'm evaluating these defects. The decision-theoretic framework suggestion is compelling—it reframes the routing problem from a simple signal multiplication into minimizing expected verification loss, which is more principled and defensible, though I need to check if UCCI's cost-optimal framework actually maps to this. The closed-world formalization is also strong, clarifying the structural distinction between PF blocks operating in a closed world versus PDA steps with running context.

For the confident-but-wrong taxonomy, it's an interesting observation but risky scope-wise—adding a third contribution to an already complex paper risks diluting focus, so I'll keep it as structured analysis within the work rather than claiming it as an independent contribution. The data leakage issue is critical and valid; the proposal text explicitly mentions using the benchmark for both calibration and co-primary evaluation, which is a genuine problem requiring strict separation. Statistical power keeps coming up across multiple review rounds, but the core constraint—ArxivMathGradingBench's limited size—is inherent to the field itself.

The per-block analysis idea is worth adopting as an incremental improvement. I need to address the false positive analysis requirement, clarify how dependency graphs are actually constructed and validated rather than assuming they exist, and move away from the binary go/no-go decision toward a graded matrix. On the frontier LLM baseline and HERMES suggestions, the frontier model approach is reasonable but potentially expensive with API costs, while the HERMES point warrants consideration.

For the remaining defects, I'm balancing validity against scope creep. The difficulty coverage gap is real but adding another benchmark would strain the experiment, so I'll acknowledge it without expanding the scope. Similarly, the BV backbone ablation is valid but would require significant additional compute, so I'll frame it as a sensitivity check rather than a full ablation.

Now I need to verify some key assumptions: whether UCCI's decision-theoretic routing framework is actually the right reference for cost-optimal routing, and whether ProofFlow's reported numbers are accurate.

Looking at the convergence pattern across rounds, the suggestions are becoming increasingly granular and focused on framing rather than substantive gaps. The probability trajectory has plateaued, and the defects being raised are mostly refinements of earlier issues or operational details. This feels like we're approaching a natural stopping point.

The high-impact changes this round—the decision-theoretic framework, closed-world formalization, data leakage fix, and dependency DAG spec—are worth adopting, but the remaining suggestions won't meaningfully strengthen the proposal. The core idea is sound, the experimental design is solid, and the lingering risks around autoformalization success and code availability can only be resolved through actual execution, not further iteration.

I think we should declare convergence after this round and move forward.

Now I need to validate a few key claims through targeted searches: whether the decision-theoretic framing for verification routing is genuinely novel, and whether FormalProofBench actually exists as described.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "640a6280-b2a9-4616-a5f9-3dd653043ab1",
  "isSidechain": false,
  "requestId": "req_011CbT88YQEHRPcZu1AF8ACc",
  "type": "assistant",
  "uuid": "9eb934ba-2261-4db0-91b5-e3098add2e55",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1Mq33D8SCUNwniBwyH9p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21372,
      "cache_read_input_tokens": 60946,
      "output_tokens": 2111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2111,
          "cache_read_input_tokens": 60946,
          "cache_creation_input_tokens": 21372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21372
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

_source line 64 · 2026-05-27T13:07:20.737Z_

我需要对第 3 轮关键建议做交叉验证。启动并行搜索：

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9eb934ba-2261-4db0-91b5-e3098add2e55",
  "isSidechain": false,
  "requestId": "req_011CbT88YQEHRPcZu1AF8ACc",
  "type": "assistant",
  "uuid": "5bbb5152-54c4-44bd-8308-b17dc23e5c9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1Mq33D8SCUNwniBwyH9p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21372,
      "cache_read_input_tokens": 60946,
      "output_tokens": 2111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2111,
          "cache_read_input_tokens": 60946,
          "cache_creation_input_tokens": 21372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21372
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

_source line 65 · 2026-05-27T13:07:21.218Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q1yR28Bmecg5BFVdcLfyQE`</summary>

```json
{
  "query": "expected verification loss risk minimization routing formal verification LLM uncertainty cost-optimal 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bbb5152-54c4-44bd-8308-b17dc23e5c9d",
  "isSidechain": false,
  "requestId": "req_011CbT88YQEHRPcZu1AF8ACc",
  "type": "assistant",
  "uuid": "4f2d4934-dcca-4173-ad91-168775800d63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1Mq33D8SCUNwniBwyH9p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21372,
      "cache_read_input_tokens": 60946,
      "output_tokens": 2111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2111,
          "cache_read_input_tokens": 60946,
          "cache_creation_input_tokens": 21372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21372
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

_source line 66 · 2026-05-27T13:07:22.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HLLVCofZZ7PktxEvM8hRAf`</summary>

```json
{
  "query": "FormalProofBench graduate level formal proof benchmark arXiv 2603.26996 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f2d4934-dcca-4173-ad91-168775800d63",
  "isSidechain": false,
  "requestId": "req_011CbT88YQEHRPcZu1AF8ACc",
  "type": "assistant",
  "uuid": "50e33bfa-4cd9-4430-b7b0-782410ae8e64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1Mq33D8SCUNwniBwyH9p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21372,
      "cache_read_input_tokens": 60946,
      "output_tokens": 2111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2111,
          "cache_read_input_tokens": 60946,
          "cache_creation_input_tokens": 21372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21372
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

_source line 67 · 2026-05-27T13:07:22.447Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011aVZuNXSpsd6DrGEqyxpSY`</summary>

```json
{
  "query": "ProofFlow dependency graph autoformalization ProofScore step-proof comparison ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "50e33bfa-4cd9-4430-b7b0-782410ae8e64",
  "isSidechain": false,
  "requestId": "req_011CbT88YQEHRPcZu1AF8ACc",
  "type": "assistant",
  "uuid": "1c9d8ac8-d594-4502-97c7-399281e3735e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U1Mq33D8SCUNwniBwyH9p5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21372,
      "cache_read_input_tokens": 60946,
      "output_tokens": 2111,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21372,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2111,
          "cache_read_input_tokens": 60946,
          "cache_creation_input_tokens": 21372,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21372
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

_source line 68 · 2026-05-27T13:07:27.773Z_

<details><summary>↩ Tool result · `toolu_01HLLVCofZZ7PktxEvM8hRAf`</summary>

```text
Web search results for query: "FormalProofBench graduate level formal proof benchmark arXiv 2603.26996 2026"

Links: [{"title":"[2603.26996] FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://arxiv.org/abs/2603.26996"},{"title":"FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://arxiv.org/html/2603.26996"},{"title":"FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://arxiv.org/pdf/2603.26996"},{"title":"(PDF) FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?","url":"https://www.researchgate.net/publication/403308231_FormalProofBench_Can_Models_Write_Graduate_Level_Math_Proofs_That_Are_Formally_Verified"},{"title":"[2507.04719] Advocate for Complete Benchmarks for Formal Reasoning with Formal/Informal Statements and Formal/Informal Proofs","url":"https://arxiv.org/abs/2507.04719"}]

Based on the search results, here's what I found about FormalProofBench:

FormalProofBench is a private benchmark designed to evaluate whether AI models can produce formally verified mathematical proofs at the graduate level. Each task pairs a natural-language problem with a Lean 4 formal statement, and a model must output a Lean proof accepted by the Lean 4 checker.

FormalProofBench targets advanced undergraduate and graduate mathematics, with problems drawn from qualifying exams and standard textbooks across topics including analysis, algebra, probability, and logic.

In terms of results, the best-performing foundation model achieves 33.5% accuracy, with performance dropping rapidly after that. The evaluation includes empirical analysis of tool-use, failure modes, cost and latency, providing a thorough evaluation of the formal-theorem proving abilities of frontier models.

The paper was submitted on March 27, 2026, and was written by Nikil Ravi, Kexing Ying, Vasilii Nesterov, and others from institutions including Vals AI, EPFL, and Moscow Institute of Physics and Technology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "50e33bfa-4cd9-4430-b7b0-782410ae8e64",
  "isSidechain": false,
  "promptId": "7f8dad30-780f-45d2-b4c1-07d90064adf1",
  "type": "user",
  "uuid": "e864f908-3fd8-44f8-86fc-b48f30851447",
  "toolUseResult": {
    "query": "FormalProofBench graduate level formal proof benchmark arXiv 2603.26996 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018CWsLAxYGo9kKzorv85wFx",
        "content": [
          {
            "title": "[2603.26996] FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://arxiv.org/abs/2603.26996"
          },
          {
            "title": "FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://arxiv.org/html/2603.26996"
          },
          {
            "title": "FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://arxiv.org/pdf/2603.26996"
          },
          {
            "title": "(PDF) FormalProofBench: Can Models Write Graduate Level Math Proofs That Are Formally Verified?",
            "url": "https://www.researchgate.net/publication/403308231_FormalProofBench_Can_Models_Write_Graduate_Level_Math_Proofs_That_Are_Formally_Verified"
          },
          {
            "title": "[2507.04719] Advocate for Complete Benchmarks for Formal Reasoning with Formal/Informal Statements and Formal/Informal Proofs",
            "url": "https://arxiv.org/abs/2507.04719"
          }
        ]
      },
      "Based on the search results, here's what I found about FormalProofBench:\n\nFormalProofBench is a private benchmark designed to evaluate whether AI models can produce formally verified mathematical proofs at the graduate level. Each task pairs a natural-language problem with a Lean 4 formal statement, and a model must output a Lean proof accepted by the Lean 4 checker.\n\nFormalProofBench targets advanced undergraduate and graduate mathematics, with problems drawn from qualifying exams and standard textbooks across topics including analysis, algebra, probability, and logic.\n\nIn terms of results, the best-performing foundation model achieves 33.5% accuracy, with performance dropping rapidly after that. The evaluation includes empirical analysis of tool-use, failure modes, cost and latency, providing a thorough evaluation of the formal-theorem proving abilities of frontier models.\n\nThe paper was submitted on March 27, 2026, and was written by Nikil Ravi, Kexing Ying, Vasilii Nesterov, and others from institutions including Vals AI, EPFL, and Moscow Institute of Physics and Technology."
    ],
    "durationSeconds": 5.546409336999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "50e33bfa-4cd9-4430-b7b0-782410ae8e64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-27T13:07:29.535Z_

<details><summary>↩ Tool result · `toolu_01Q1yR28Bmecg5BFVdcLfyQE`</summary>

```text
Web search results for query: "expected verification loss risk minimization routing formal verification LLM uncertainty cost-optimal 2025 2026"

Links: [{"title":"UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing","url":"https://arxiv.org/html/2605.18796"},{"title":"RACER: Risk-Aware Calibrated Efficient Routing for Large Language Models","url":"https://arxiv.org/pdf/2603.06616"},{"title":"Leveraging Uncertainty Estimation for Efficient LLM Routing","url":"https://arxiv.org/html/2502.11021"},{"title":"(PDF) Leveraging Uncertainty Estimation for Efficient LLM Routing","url":"https://www.researchgate.net/publication/389091409_Leveraging_Uncertainty_Estimation_for_Efficient_LLM_Routing"},{"title":"Leveraging Uncertainty Estimation for Efficient LLM Routing | OpenReview","url":"https://openreview.net/forum?id=DJpEIwKJt7"}]

Based on the search results, here are the key findings related to expected verification loss, risk minimization, routing, formal verification, LLM uncertainty, and cost-optimal approaches:

## Key Research Areas (2025-2026)

**Cost-Optimal LLM Routing with Uncertainty:**

UCCI calibrates token-level uncertainty into error probabilities and selects an escalation threshold by constrained cost minimization. The research poses cascade design as expected cost minimization subject to an accuracy constraint, and proves that threshold policies on calibrated error probabilities are cost-optimal under three explicit assumptions.

**Risk-Aware Routing Frameworks:**

RACER proposes a risk-aware calibrated efficient routing paradigm with guaranteed risk control, defining routing risk as the probability of excluding all optimal LLMs and formulating LLM routing as the α-Valid Optimal Routing problem to minimize the expected model set size while bounding the risk.

**Uncertainty-Driven Routing:**

Recent work proposes leveraging Semantic Entropy as an uncertainty measure to guide routing decisions, using it to measure model confidence and enable routers to offload queries to cloud-based LLMs when higher certainty is needed while keeping confident responses on-device to minimize cost.

These approaches collectively address the challenge of balancing accuracy, cost efficiency, and risk management in LLM deployment systems through uncertainty estimation and calibrated decision-making frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4f2d4934-dcca-4173-ad91-168775800d63",
  "isSidechain": false,
  "promptId": "7f8dad30-780f-45d2-b4c1-07d90064adf1",
  "type": "user",
  "uuid": "40b3bbbb-6a8a-43b2-b7ed-8d0fa7f372ab",
  "toolUseResult": {
    "query": "expected verification loss risk minimization routing formal verification LLM uncertainty cost-optimal 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0141Ffs9MBkFmftMZaskmdcu",
        "content": [
          {
            "title": "UCCI: Calibrated Uncertainty for Cost-Optimal LLM Cascade Routing",
            "url": "https://arxiv.org/html/2605.18796"
          },
          {
            "title": "RACER: Risk-Aware Calibrated Efficient Routing for Large Language Models",
            "url": "https://arxiv.org/pdf/2603.06616"
          },
          {
            "title": "Leveraging Uncertainty Estimation for Efficient LLM Routing",
            "url": "https://arxiv.org/html/2502.11021"
          },
          {
            "title": "(PDF) Leveraging Uncertainty Estimation for Efficient LLM Routing",
            "url": "https://www.researchgate.net/publication/389091409_Leveraging_Uncertainty_Estimation_for_Efficient_LLM_Routing"
          },
          {
            "title": "Leveraging Uncertainty Estimation for Efficient LLM Routing | OpenReview",
            "url": "https://openreview.net/forum?id=DJpEIwKJt7"
          }
        ]
      },
      "Based on the search results, here are the key findings related to expected verification loss, risk minimization, routing, formal verification, LLM uncertainty, and cost-optimal approaches:\n\n## Key Research Areas (2025-2026)\n\n**Cost-Optimal LLM Routing with Uncertainty:**\n\nUCCI calibrates token-level uncertainty into error probabilities and selects an escalation threshold by constrained cost minimization. The research poses cascade design as expected cost minimization subject to an accuracy constraint, and proves that threshold policies on calibrated error probabilities are cost-optimal under three explicit assumptions.\n\n**Risk-Aware Routing Frameworks:**\n\nRACER proposes a risk-aware calibrated efficient routing paradigm with guaranteed risk control, defining routing risk as the probability of excluding all optimal LLMs and formulating LLM routing as the α-Valid Optimal Routing problem to minimize the expected model set size while bounding the risk.\n\n**Uncertainty-Driven Routing:**\n\nRecent work proposes leveraging Semantic Entropy as an uncertainty measure to guide routing decisions, using it to measure model confidence and enable routers to offload queries to cloud-based LLMs when higher certainty is needed while keeping confident responses on-device to minimize cost.\n\nThese approaches collectively address the challenge of balancing accuracy, cost efficiency, and risk management in LLM deployment systems through uncertainty estimation and calibrated decision-making frameworks."
    ],
    "durationSeconds": 8.311340975000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4f2d4934-dcca-4173-ad91-168775800d63",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-27T13:07:31.536Z_

<details><summary>↩ Tool result · `toolu_011aVZuNXSpsd6DrGEqyxpSY`</summary>

```text
Web search results for query: "ProofFlow dependency graph autoformalization ProofScore step-proof comparison ICLR 2026"

Links: [{"title":"ProofFlow - ICLR 2026 video presentation - YouTube","url":"https://www.youtube.com/watch?v=EVJIO2XmOz8"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization | OpenReview","url":"https://openreview.net/forum?id=s9t2FJVsBH"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/pdf/2510.15981"},{"title":"ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/html/2510.15981v1"},{"title":"[2510.15981] ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://arxiv.org/abs/2510.15981"},{"title":"(PDF) ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization","url":"https://www.researchgate.net/publication/396716261_ProofFlow_A_Dependency_Graph_Approach_to_Faithful_Proof_Autoformalization"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=s9t2FJVsBH"}]

Based on the search results, I found comprehensive information about ProofFlow and the related concepts you're asking about:

## ProofFlow: A Dependency Graph Approach to Proof Autoformalization

ProofFlow is a dependency-aware proof autoformalization system presented at ICLR 2026. It treats structural fidelity as a primary objective and constructs a directed acyclic graph (DAG) to map the logical dependencies between proof steps. It employs a novel lemma-based approach to systematically formalize each step as an intermediate lemma, preserving the logical structure of the original argument.

## ProofScore Metric

ProofScore is a new composite metric introduced to evaluate syntactic correctness, semantic faithfulness, and structural fidelity.

## Performance Comparison

ProofFlow achieves a ProofScore of 0.545, substantially exceeding baselines like full-proof formalization (0.123), which processes the entire proof at once, and step-proof formalization (0.072), which handles each step independently.

## Benchmark and Contributions

The work presents a new benchmark of 184 undergraduate-level problems, manually annotated with step-by-step solutions and logical dependency graphs. The pipeline, benchmark, and score metric are open-sourced at https://github.com/Huawei-AI4Math/ProofFlow.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c9d8ac8-d594-4502-97c7-399281e3735e",
  "isSidechain": false,
  "promptId": "7f8dad30-780f-45d2-b4c1-07d90064adf1",
  "type": "user",
  "uuid": "55ce9062-6120-4d2d-a443-f6630d899a55",
  "toolUseResult": {
    "query": "ProofFlow dependency graph autoformalization ProofScore step-proof comparison ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011VfMGc6y92KWZT6JnudBq7",
        "content": [
          {
            "title": "ProofFlow - ICLR 2026 video presentation - YouTube",
            "url": "https://www.youtube.com/watch?v=EVJIO2XmOz8"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization | OpenReview",
            "url": "https://openreview.net/forum?id=s9t2FJVsBH"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/pdf/2510.15981"
          },
          {
            "title": "ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/html/2510.15981v1"
          },
          {
            "title": "[2510.15981] ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://arxiv.org/abs/2510.15981"
          },
          {
            "title": "(PDF) ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization",
            "url": "https://www.researchgate.net/publication/396716261_ProofFlow_A_Dependency_Graph_Approach_to_Faithful_Proof_Autoformalization"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf?id=s9t2FJVsBH"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about ProofFlow and the related concepts you're asking about:\n\n## ProofFlow: A Dependency Graph Approach to Proof Autoformalization\n\nProofFlow is a dependency-aware proof autoformalization system presented at ICLR 2026. It treats structural fidelity as a primary objective and constructs a directed acyclic graph (DAG) to map the logical dependencies between proof steps. It employs a novel lemma-based approach to systematically formalize each step as an intermediate lemma, preserving the logical structure of the original argument.\n\n## ProofScore Metric\n\nProofScore is a new composite metric introduced to evaluate syntactic correctness, semantic faithfulness, and structural fidelity.\n\n## Performance Comparison\n\nProofFlow achieves a ProofScore of 0.545, substantially exceeding baselines like full-proof formalization (0.123), which processes the entire proof at once, and step-proof formalization (0.072), which handles each step independently.\n\n## Benchmark and Contributions\n\nThe work presents a new benchmark of 184 undergraduate-level problems, manually annotated with step-by-step solutions and logical dependency graphs. The pipeline, benchmark, and score metric are open-sourced at https://github.com/Huawei-AI4Math/ProofFlow."
    ],
    "durationSeconds": 9.085977296999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1c9d8ac8-d594-4502-97c7-399281e3735e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 71_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research to provide a thorough analysis. Let me compile my findings.  【状态】: 有发掘空间  【前置调研发…",
  "leafUuid": "55ce9062-6120-4d2d-a443-f6630d899a55",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 72_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Assistant

_source line 73 · 2026-05-27T13:09:05.787Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Cross-validation results:

1. **Decision-theoretic routing framework**: VALIDATED. UCCI and RACER both frame routing as cost minimization under constraints. UCCI proves threshold policies on calibrated error probabilities are cost-optimal. RACER defines routing risk and minimizes expected model set size. This confirms the 发掘 agent's suggestion that the decision-theoretic framing is well-grounded in existing routing literature and would strengthen the proposal. The novelty is in applying it to cross-paradigm (LLM→formal) verification routing rather than LLM cascading.


2. **FormalProofBench**: CONFIRMED as a real benchmark from March 2026 with graduate-level math problems in Lean 4 where the best model achieves 33.5%. It's a proof generation benchmark rather than verification, so it's useful for calibrating difficulty expectations but not as a direct evaluation benchmark.
3. **ProofFlow**: CONFIRMED at ICLR 2026 with ProofScore metrics showing 0.545 for dependency-aware evaluation versus 0.123 for full-proof and 0.072 for step-proof—this is a strong data point supporting the core thesis that dependency-aware formalization dramatically outperforms other approaches.

Now I'm weighing the agent suggestions from this round. The framing improvements are solid, though some risk scope creep. The operational fixes are more mixed—data leakage and false positive analysis are genuinely new concerns worth adopting, while statistical power keeps resurfacing. The dependency DAG construction and graded pilot matrix are also valid additions to strengthen the methodology.

Looking at convergence signals: the suggestions are getting more granular, focusing on refinements rather than structural problems. The probability trajectory has stabilized around 38-40%, and the remaining gaps—like autoformalization success rates and proof-finding code—need experimental validation, not more proposal iteration. I've addressed the fundamental issues across three rounds, so I'm going to converge here, integrate the strongest suggestions, and finalize the proposal. The improvements from Round 3 are substantive in places—the decision-theoretic framework and data leakage fix address real weaknesses—but the overall pattern shows diminishing returns and convergence. The probability has stabilized around 39%, changes are becoming more granular, and there's no oscillation, so I should wrap up here. Since the final estimate exceeds 36%, the decision is to move forward with the optimized proposal.

Now I need to clarify the output format: should I produce the convergence declaration in iteration format, or go straight to the final output? The instructions suggest different roles at different stages—Role B for iteration summaries, Role C for the final output after convergence. Since I'm declaring convergence now, I'll produce the full final output including the optimized proposal. 我在进行第三轮的交叉验证，检查各个角色的建议是否存在矛盾或遗漏之处。看起来关于用户体验优化和技术实现路径的建议已经趋于一致，我需要判断是否已经收敛到可以输出最终方案的程度。

现在我在整理采纳的修改项、评估这些变更对整体方案的影响，以及给出概率估计——考虑到方案的新颖性、科学意义和实验设计的完整性，我对其可行性有相当的信心。最后我会生成修改建议列表，对比原始提案指出具体的优化点，同时标注主要风险和实施评估。

重新审视概率时，我注意到这个方案在三轮迭代后已经相当成熟：PF-block作为自动形式化桥接加上决策论的双信号路由是全新的组合，针对形式验证的可扩展性瓶颈有明确的针对性，实验计划涵盖8个以上的消融实验、3个基准测试和7个以上的基线对比。不过仍有几个关键风险需要考虑——PF代码的可用性、块级自动形式化的成功率（试点研究至关重要）、ArxivMathGradingBench数据集规模较小（虽然可以用合成数据集补充），以及"1.5-2倍成本"的声称需要验证。对于AAAI而言，这篇论文既有算法创新又有实际应用价值，问题定义清晰且动机充分，技术方案在试点结果的前提下是可靠的。综合考虑，我认为39%左右的概率是合理的，主要限制因素是这类管道组合论文在顶会上的接受度。

既然39%超过了36%的阈值，这就是一个"通过"的案例，我需要输出优化方案。

现在我来完成最终输出，这会比较长但需要全面覆盖最后一轮的修改。对于角色C的输出，我需要列出相比原始提案的改动。回顾原始提案的核心问题、研究机会和研究景观的框架，我要指出具体的改进之处。

主要改动包括：在核心问题中加入了"结构关键性"的维度，新增了一个论文贡献部分来区分两个核心发现——PF块自动形式化的优势作为实证结果，以及选择性验证管道的设计。研究机会从单纯的成本-可靠性权衡重新定位为可扩展形式验证架构的问题，认识到全证明自动形式化的35%上限是架构性的而非工程性的。研究景观部分则增加了生成与验证的分类法，以及与Ganguly工作的三层区分来说明不确定性的来源。

在提议方法中，我加入了初期试点研究阶段、基于决策论的预期验证损失路由机制、对置信但错误风险的缓解策略、使用Platt缩放的校准方法、结构难度启发式方法、Tier 2的迭代自我修正机制以及依赖DAG质量验证。

现在我需要规划评估方案，包括三个基准测试、七个以上的基线模型、八个以上的消融实验，以及统一的成本框架来分析GPU秒数与证明的关系，同时重点关注ProofFlow与原始自然语言自动形式化的对比、置信但错误的结构化分析，以及Tier 2的敏感性分析。

参考文献也从10篇扩展到17篇以上。资源估计更新为400-550个GPU小时，耗时14-18周，包括试点阶段和ProofFlow代码的应急方案。

现在我需要思考如何在角色C格式的框架下清晰地呈现这些主要修改，并确保每项改动都能对应到评审维度的加分点。我还需要验证39%这个中点是否合理，从评审者的角度来考虑这个数字。

AAAI的评审者会看到这个工作的几个核心优势：新颖的问题框架（对自然语言证明的选择性形式化验证）、文献中的明确空白（没有人结合ProofFlow结构和不确定性路由）、有硬数据支撑的动机（35%的自动形式化上限、50%的Blueshift验证错误漏检率）、原则性的决策论证路由框架、全面的实验计划，以及实际意义（成本从4-8倍降低到约2倍）。但同时也会注意到这是一篇管道论文（组合现有工具），核心假设未经验证，主要基准很小，依赖非常新近的工作，成本声称需要验证，而且系统复杂度高可能被视为过度设计。

考虑到管道性质和未证实的假设，39%的评分是合理的，甚至可能略显慷慨。但将其重新框架化为架构洞察和双重贡献结构能显著帮助。我会把评分定在34%-44%的范围内，中位数39%。还需要在交叉验证中加入RACER参考，因为它与决策论证框架直接相关。现在开始写输出，保持全面但不过度冗长。

我要组织两部分内容：角色B第三轮的迭代输出，包括交叉验证研究、agent采纳的发掘和补救、本轮变更以及想法和实验评估；然后是角色C的最终输出，涵盖优化方案、主要风险和实施评估。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55ce9062-6120-4d2d-a443-f6630d899a55",
  "isSidechain": false,
  "requestId": "req_011CbT8CxUgQLEHdEVVhzVhx",
  "type": "assistant",
  "uuid": "d3412201-6988-4dff-be08-77410c0a46fb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018s5PcFKV54JujVYBwEawbq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4063,
      "cache_read_input_tokens": 82318,
      "output_tokens": 9796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4063,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9796,
          "cache_read_input_tokens": 82318,
          "cache_creation_input_tokens": 4063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4063
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

_source line 74 · 2026-05-27T13:11:13.637Z_

交叉验证完成。现在整合第 3 轮并做收敛判断。

【阶段】: 迭代第 3 轮

【交叉验证调研】:
1. **Decision-theoretic routing framework** — **已验证有理论基础**。UCCI (arXiv 2026) 证明在三个显式假设下，基于校准错误概率的阈值策略是成本最优的；RACER (arXiv 2603.06616, 2026) 将 LLM routing 形式化为 α-Valid Optimal Routing 问题（最小化 expected model set size，约束 routing risk）。两者都将 routing 表述为 cost minimization under constraints，但都是 within-tier routing (小模型→大模型)。发掘 agent 的建议——将其扩展到 cross-paradigm routing (LLM→formal verification) 并引入 cost-of-error 维度——在现有文献中无先例，是 genuine extension。
2. **FormalProofBench** — **已验证存在**。arXiv 2603.26996 (March 2026), graduate-level math, Lean 4, best model 33.5%。但注意：这是 proof GENERATION benchmark (models write proofs)，不是 verification benchmark。可作为 Tier 2 difficulty calibration 参考（graduate-level formalization 确实很难），但不能直接用作 evaluation benchmark。
3. **ProofFlow ICLR 2026** — **已验证关键数据**。ProofScore: dependency-aware 0.545 vs full-proof 0.123 vs step-proof 0.072。这是极强的支撑数据：dependency-aware 分解将 autoformalization fidelity 提升了 4.4x vs full-proof, 7.6x vs step-proof。直接支持 Claim 1（PF block 的结构化分解显著优于其他粒度）。ProofFlow 开源于 https://github.com/Huawei-AI4Math/ProofFlow。

【发掘 agent 有效建议采纳】:
- 发掘点1（Decision-theoretic Expected Verification Loss 框架）: **已验证，采纳**。UCCI 和 RACER 验证了 cost-optimal routing = constrained optimization on calibrated probabilities 在 LLM 领域的有效性。将 dual-signal 重述为 E[Loss] = P(BV_error|b) × C(error|b) 是对现有框架的 principled cross-paradigm extension。将 routing 阈值从超参数变为成本-风险均衡的自然结果，显著提升 Novelty defensibility。
- 发掘点2（Closed-world formalization 精确定义 + PDA 对比）: **已验证，采纳**。ProofFlow 的数据（0.545 vs 0.072 step-proof）提供了独立实证：结构化分解（保留 dependency）远优于简单 step-level 切分。PF block 的 closed-world 属性（所有 premises 显式声明，无需 running context）与 PDA 的 step-level（仍需 running Lean context）构成清晰结构差异。此定义使 Claim 1 从描述性提升为结构性论断。
- 发掘点3（Confident-but-wrong failure taxonomy 提升为独立贡献）: **部分采纳，降权**。构想有价值但存在 scope creep 风险——论文已有两个 claim（autoformalization bridge + selective verification pipeline），再加第三个（failure mode taxonomy）会稀释焦点。采纳为：在 confident-but-wrong 分析中做结构化归因（数学领域、证明策略），但定位为 "analytical finding" 而非 "third contribution"。

【补救 agent 有效建议采纳】:
- 缺陷1（Calibration-evaluation data leakage）: **采纳，关键修复**。原文确有 "Used for calibration and as co-primary evaluation benchmark" 的矛盾表述。修复：Synthetic set 严格三路划分（calibration 60% / validation 15% / evaluation 25%），总量提升到 600-800 以保证各子集统计可靠性。ArxivMathGradingBench 仅用于 evaluation。
- 缺陷2（ArxivMathGradingBench 统计功效）: **部分采纳**。第 3 次提及此问题，核心已在前轮处理（bootstrap CI, synthetic set, effect size）。本轮新增：per-block routing precision 分析（~1050 blocks 提供更大统计功效）+ 预注册 power analysis。不再增加新 benchmark 以避免 scope 膨胀。
- 缺陷3（False positive 分析）: **采纳**。Verification 系统必须同时报告两个方向的错误。新增 per-tier false positive rate + FP rate vs recall tradeoff 曲线。
- 缺陷4（Dependency DAG 构建流程 + 质量验证）: **采纳**。明确 DAG 是 PF decomposition 的直接输出（Barkallah et al. 2026 的 PF 格式包含 inter-block dependencies），在 pilot study 中加入 dependency graph quality human evaluation。
- 缺陷5（30-50% 灰色地带 graded decision matrix）: **采纳**。将 binary go/no-go 升级为 4 级 decision matrix，并新增 effective Tier 2 coverage 指标。
- 缺陷6（Frontier LLM baseline + HERMES 适用性）: **部分采纳**。增加 frontier LLM single-pass 作为 reference point（成本可控，仅 evaluation 集上 single-pass）。HERMES 标注为 "reference comparison (proof generation setting)" 而非直接 baseline，在 discussion 中明确 setting 差异。不替换为 stepproof 等——未验证其相关性。
- 缺陷7（Difficulty coverage bias）: **部分采纳**。在 discussion/limitations 中明确承认，但不新增 benchmark 以控制 scope。
- 缺陷8（BV backbone ablation）: **部分采纳**。作为 supplementary experiment（在 synthetic set 上 N=3 对比 Qwen3.5-35B），不作为 main ablation。

【本轮 proposal 主要变更】:
**Idea 层面变更:**
- Routing 框架从 "uncertainty × criticality" 重述为 decision-theoretic Expected Verification Loss: E[Loss] = P(BV_error|b) × C(error|b)，routing 阈值由 cost-risk 均衡决定
- 精确定义 context-completion problem 和 PF block 的 closed-world formalization property，对比 PDA step-level 的 running-context 依赖
- 引入 ProofFlow (ICLR 2026) 的 ProofScore 数据（0.545 vs 0.072）作为 Claim 1 的独立实证支撑
- Confident-but-wrong 分析增加结构化归因维度（数学领域、证明策略）

**实验层面变更:**
- Synthetic set 严格三路划分 (calibration/validation/evaluation)，总量提升到 600-800
- 新增 per-tier false positive rate 分析和 FP rate vs recall tradeoff 曲线
- Pilot study 升级为 graded decision matrix（<30% / 30-50% / 50-70% / >70%）
- 新增 effective Tier 2 coverage 指标
- Dependency DAG 质量 human evaluation 纳入 pilot study
- 增加 frontier LLM single-pass reference baseline
- HERMES 重新定位为 reference comparison (不同 setting)
- BV backbone sensitivity check 作为 supplementary experiment

【idea 质量评估】: Novelty=中强(趋强) Significance=强 → idea 天花板约 48%
- Novelty: decision-theoretic E[Loss] 框架将 routing 从 ad-hoc 组合提升为 principled optimization；closed-world formalization 定义锐化了 Claim 1；三层 Ganguly 差异化保持清晰。但 pipeline 组合底色仍在。
- Significance: "formal verification scalability" framing + ProofFlow 实证 (0.545 vs 0.072) 强化了"模块化分解是 informal-formal 桥梁"的论断。

【实验完备性评估】: Technical Soundness=中强 → 设计全面，data leakage 已修复，false positive 已补充
- 数据流清晰（calibration/validation/evaluation 严格分离）
- 覆盖面完整（8+ ablation, 3 benchmark, 7+ baseline, 2 Pareto curves, sensitivity analysis）
- 主要残余风险：autoformalization 成功率未验证（pilot study 负责）、PF 代码可获得性（contingency 已规划）

【当前概率估计】: [34% - 44%] 中位 39%
- 上限 44%：idea 天花板 48% 减去 pipeline 组合的固有 discount ~4%
- 下限 34%：如果 pilot study 结果在灰色地带 (30-50%) 且 ArxivMathGradingBench 统计不显著
- 中位 39%：相比 R2 的 38% 微升 1%，反映 decision-theoretic framing + data leakage 修复 + false positive 补充的增量价值

【决策】: 收敛

【决策理由】:
1. **变更粒度递减**: R1 = 结构性重构 (idea reframing + 实验全面补强)；R2 = 模块级强化 (significance 升级 + 双贡献结构 + pilot study)；R3 = 局部精炼 (decision-theoretic notation + 数据流修复 + false positive)。符合收敛特征。
2. **概率稳定**: 36% → 38% → 39%，连续 2 轮微升 ≤2%，变化在噪声范围内。
3. **残余风险不可通过 proposal 迭代解决**: autoformalization 成功率需实验、PF 代码需联系作者、ArxivMathGradingBench 规模是领域固有约束。
4. **两位 worker 均未发现新的结构性问题**: R3 发掘 agent 仅 3 点（R1 为 5 点，R2 为 5 点），且全部为 framing 层面优化；补救 agent 的缺陷多为前轮问题的细化或边际扩展。
5. **无跷跷板效应**: 所有轮次的修改互相兼容，未出现"补 A 崩 B"的情况。

---

以下为最终输出（角色 C：收敛，中位 39% ≥ 36%，通过）。

【优化方案】

**对比原始 proposal 的修改建议列表：**

1. **[Core Problem / 标题]** — 在 "most uncertain proof blocks" 后添加 "and structurally critical"，反映 dual-signal routing — **命中 Novelty：从 single-signal 升级为 principled dual-signal design**

2. **[新增 Thesis and Contributions 章节]** — 建立双贡献结构：Claim 1 = PF block 是已知唯一提供 closed-world formalization 属性的证明分解粒度，消除限制 whole-proof 和 step-level autoformalization 的 sequential error accumulation（ProofFlow ICLR 2026 的 ProofScore 0.545 vs step-proof 0.072 提供独立实证）；Claim 2 = 基于此构建 decision-theoretic selective verification pipeline — **命中 Significance + Novelty：从 "pipeline 优化" 提升为 "architectural insight + system design" 双层贡献**

3. **[Research Opportunity]** — 将核心叙事从 "finding a better cost-reliability tradeoff" 重构为 "modular decomposition as the only viable path to scalable formal verification of complex proofs"，论证 whole-proof autoformalization 的 ~35% 上限是 architectural limitation（context-completion + error accumulation），非工程问题 — **命中 Significance：从 incremental optimization 提升为 addressing fundamental scalability barrier**

4. **[Research Landscape]** — 四项关键增强：(a) 建立 "proof generation vs. proof verification" taxonomy，HERMES 定位为 generation agent 而非直接竞争者；(b) 对 Ganguly et al. (NeurIPS 2025) 建立三层差异化：uncertainty source（生成端 vs 验证端）、routing target heterogeneity（同质 vs 异质验证范式）、structural criticality dimension（无 vs 有）；(c) 新增 ThinkPRM (2025)、prompt ensemble (arXiv 2604.02450, 2026)、ProofFlow (ICLR 2026)、Process-Driven Autoformalization (2024) 引用；(d) 精确定义 PF block 的 closed-world property 与 PDA step-level 的 running-context 依赖的结构差异 — **命中 Related Work + Novelty：防止被归类为 "same idea different domain" 或 "combination of existing tools"**

5. **[Proposed Approach — Phase 0 Pilot Study]** — 新增 go/no-go 前置验证：50-100 PF blocks 端到端 autoformalization + proof search 成功率测试，graded decision matrix（<30% 需重新设计 Tier 2 / 30-50% 需调高 routing % / 50-70% 按计划 / >70% 可降低 routing %）。同时验证 dependency DAG 质量（human evaluation, dependency precision/recall） — **命中 Technical Soundness：展示 research maturity，预防 "core assumption unproven" 攻击**

6. **[Proposed Approach — Routing 框架]** — 将 "uncertainty × dependency criticality" 重述为 decision-theoretic Expected Verification Loss：E[Loss] = P(BV_error|b) × C(error|b)，P 由校准 ensemble uncertainty 估计，C 由 dependency graph 传递可达 block 数量加权估计。routing 阈值由 E[Loss] > marginal_cost(formal_verification) 决定，非人工超参数。引用 UCCI (arXiv 2026) 和 RACER (arXiv 2026) 的 cost-optimal routing 理论基础 — **命中 Novelty：从 "two signals multiplied together" 提升为 "principled risk minimization framework with cost-optimal threshold"**

7. **[Proposed Approach — Confident-but-wrong 缓解]** — 新增显式风险讨论：LLM 系统性过度自信（99% CI 实际覆盖 ~65%）+ 三重缓解策略（ensemble disagreement > single-model confidence, dependency criticality 作为 uncertainty-independent signal, structural difficulty heuristic）+ ablation 中专项分析 confident-but-wrong 的结构化归因（数学领域、证明策略、block 特征） — **命中 Technical Soundness：主动应对审稿人最可能的攻击向量**

8. **[Proposed Approach — Calibration]** — 从 isotonic regression 改为 Platt scaling（小样本更稳定），calibration 数据来源从 ArxivMathGradingBench 改为 Synthetic set + miniF2F data，ArxivMathGradingBench 仅用于最终 evaluation，消除 data leakage — **命中 Technical Soundness：消除实验设计硬伤**

9. **[Proposed Approach — Tier 2 增强]** — 增加 iterative self-correction（k=3 retries with Lean compiler feedback），per-block timeout 5min / per-proof timeout 30min；fallback 策略作为 ablation variable — **命中 Technical Soundness：提升 Tier 2 实际成功率**

10. **[Evaluation Plan — 完全新增章节]** — 原始 proposal 仅一句话概述评测，现扩展为完整评测计划：
    - 3 benchmarks：ArxivMathGradingBench (evaluation only) + Synthetic Error Detection Set (600-800 instances, 三路划分, 多源错误, 人工验证子集) + miniF2F Verification Protocol (≥8 candidates/problem, ≥100 problems)
    - 7+ baselines：PF+BV single-pass, ensemble, prompt ensemble, ThinkPRM, Qwen2.5-Math-PRM-7B, Safe, frontier LLM reference; HERMES 作为 reference comparison (不同 setting)
    - 8+ ablations：uncertainty decomposition, routing signal (含 simple heuristic-only), ensemble size, fallback strategy, threshold sweep, PF vs raw NL (core result), confident-but-wrong structured analysis, Tier 2 sensitivity analysis
    - Cost framework：统一 GPU-seconds/proof + cost breakdown table + Pareto curve
    - 统计：bootstrap CI, McNemar's, effect size (Cohen's h), per-block routing precision, pre-registered power analysis
    - False positive 分析：per-tier FP rate + FP rate vs recall tradeoff curve
    — **命中 Technical Soundness：从 sketch 级实验设计提升为 publication-ready evaluation plan**

11. **[Key References]** — 从 10 篇扩展到 17+ 篇，新增：ThinkPRM (2025), Qwen2.5-Math-PRM (2025), ProofSketcher (arXiv 2026), UCCI (arXiv 2026), ProofFlow (ICLR 2026), "Do We Need Frontier Models" (arXiv 2026), Process-Driven Autoformalization (2024) — **命中 Related Work：覆盖所有审稿人可能知道的相关工作**

12. **[Resource Estimate]** — 更新为 400-550 GPU hours (A100-80GB) + ~60 CPU hours, timeline 14-18 weeks (含 PF 代码 contingency + pilot study phase), $1200-1650 GPU cost。新增 critical path 分解和 Lean 4 proof search wall-clock 估算 — **命中 Feasibility：展示对实施风险的充分考量**

【主要风险】:
1. **Block-level autoformalization 端到端成功率未知**（最大风险）: 如果 PF block autoformalization + Goedel-Prover-V2 proof search 的端到端成功率落在 30-50% 灰色地带，Tier 2 的实际 error detection 增量有限——系统可能退化为"用 5x ensemble BV cost 获得的大部分收益 + 少量 formal verification 的边际改善"。pilot study (Phase 0) 是关键 go/no-go 节点。
2. **Confident-but-wrong 比例可能高于预期**: 如果 BV 漏检的 50% 错误中大部分是 confident-but-wrong（而非 uncertain-and-wrong），即使 dual-signal routing 也无法完全覆盖，系统的 error detection recall 上限将显著低于预期。structured analysis 的归因结果决定了此风险的实际严重程度。

【实施评估】:
  - 计算资源: A100-80GB GPU, 400-550 GPU hours + ~60 CPU hours。预估 GPU 成本 $1200-1650。Lean 4 proof search 是 GPU+CPU 混合负载（Goedel-Prover-V2 推理 GPU, Lean kernel type-checking CPU）。
  - 数据需求: ArxivMathGradingBench (35 papers, 40 errors, 需从 Barkallah et al. 2026 获取)；Hard2Verify (公开可得)；miniF2F/miniF2F-v2 (公开可得)。Synthetic Error Detection Set 需自行构建（600-800 instances）。
  - 人工介入: (a) Synthetic set 人工验证子集 (50-80 instances, ~20-30 person-hours, 数学研究生)；(b) Pilot study 中 dependency DAG 质量 human evaluation (50-100 blocks, ~10-15 person-hours)；(c) Confident-but-wrong case 归因分析可能需要领域专家参与。总人工约 40-60 person-hours。
  - 训练需求: **无模型训练**。所有组件使用现成预训练模型（QwQ-32B, StepFun-Formalizer-32B, Goedel-Prover-V2-32B, ThinkPRM）。仅需 Platt scaling 校准（2 参数 logistic fit，不构成训练负载）。
  - 新 Benchmark: 需构建 Synthetic Error Detection Set (600-800 instances)。构建方式：LLM 生成错误证明 + controlled perturbation of correct proofs + Hard2Verify 已知错误提取。预估构建时间 2-3 weeks（含人工验证）。
  - 预估周期: 14-18 weeks（2-3 researchers）。Critical path: Phase 0 pilot (weeks 1-2) → PF pipeline setup + synthetic set construction (weeks 2-5) → uncertainty calibration (weeks 5-8) → full pipeline + ablations (weeks 8-15) → analysis + writing (weeks 15-18)。PF 代码不可得时 +2-3 weeks contingency。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3412201-6988-4dff-be08-77410c0a46fb",
  "isSidechain": false,
  "requestId": "req_011CbT8CxUgQLEHdEVVhzVhx",
  "type": "assistant",
  "uuid": "139e083b-d0a6-40f3-9e6d-4e635a14d427",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018s5PcFKV54JujVYBwEawbq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4063,
      "cache_read_input_tokens": 82318,
      "output_tokens": 9796,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4063,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9796,
          "cache_read_input_tokens": 82318,
          "cache_creation_input_tokens": 4063,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4063
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

_source line 75_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research to provide a thorough analysis. Let me compile my findings.  【状态】: 有发掘空间  【前置调研发…",
  "leafUuid": "139e083b-d0a6-40f3-9e6d-4e635a14d427",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 76_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 77_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 以「角色 B：迭代中」整合第 3 轮 worker 输出，按指定格式输出决策、概率估计、以及（若继续）下一轮 proposal 纯净版。  【发掘 agent 本轮输出】: Now I have enough research to provide a thorough analysis. Let me compile my findings.  【状态】: 有发掘空间  【前置调研发…",
  "leafUuid": "139e083b-d0a6-40f3-9e6d-4e635a14d427",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 78_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 79_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 80 · 2026-05-27T13:11:15.012Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T13:11:15.012Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "content": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。"
}
```

---

### Runtime record

_source line 81 · 2026-05-27T13:11:15.012Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T13:11:15.012Z",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

## Round 5

5 recorded events

### User

_source line 82 · 2026-05-27T13:11:15.040Z_

【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "139e083b-d0a6-40f3-9e6d-4e635a14d427",
  "isSidechain": false,
  "promptId": "319a6871-33a0-4820-9a21-ca0782cddf47",
  "type": "user",
  "uuid": "467ba372-4ac1-459e-b45f-0005d894339d",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 83 · 2026-05-27T13:11:35.119Z_

<details><summary>Logged reasoning block</summary>

````text
The user is asking me to produce the final output in 角色 C format. I already produced most of this in my previous response, but let me re-examine and produce a clean, polished version.

Looking back at my previous output, I already included the 角色 C content (优化方案, 主要风险, 实施评估). But the user is asking me to produce it again in the proper format. Let me produce a clean, definitive version.

Let me review the 角色 C format requirements:

```
【优化方案】

1. [位置 / 章节] — [具体改动] — [命中哪个评审维度的加分]


```

Now I need to structure the optimization proposals with specific locations, concrete changes, and which review dimensions they address. I'll also need to identify the main risks that reviewers might attack and provide an implementation assessment covering computational resources, data requirements, and any manual intervention needed.

```

我现在需要整理思路，确保修改方案清晰、可执行。当前的思路是围绕具体的审查维度来组织修改建议，同时评估实施风险和可行性，最后给出概率估计。我应该避免重复已经写过的内容，专注于如何让这个方案更加精准和有针对性。

```

我在思考如何更精准地组织修改方案，确保每项修改都对应具体的审查维度，同时要评估实施的风险和时间成本。关键是要让这些建议既可操作又能有效提升通过概率。
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "467ba372-4ac1-459e-b45f-0005d894339d",
  "isSidechain": false,
  "requestId": "req_011CbT8VS92RdRj3oRb67zPG",
  "type": "assistant",
  "uuid": "124fcfd9-aa50-4ee6-b301-e9a8cb298b31",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UX2rkaYEb38rtJFQxA4b1B",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9873,
      "cache_read_input_tokens": 86381,
      "output_tokens": 6063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6063,
          "cache_read_input_tokens": 86381,
          "cache_creation_input_tokens": 9873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9873
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

_source line 84 · 2026-05-27T13:13:20.977Z_

【优化方案】

**最终概率估计**: [34% - 44%] 中位 39%（经 3 轮迭代，idea 天花板 ~48%，实验不确定性惩罚 ~9%）

**迭代历程**: R0 原始 → R1 36%（结构性重构）→ R2 38%（significance 升级 + 双贡献）→ R3 39%（decision-theoretic framing + 数据流修复）→ 收敛

---

1. **[全局 / 论文定位]** — 将核心叙事从 "cost-reliability tradeoff optimization" 重构为 "modular proof decomposition as the only viable architecture for scaling formal verification to complex proofs"。论证依据：whole-proof autoformalization 端到端成功率仅 ~35%（miniF2F-Lean Revisited, NeurIPS 2025），此上限是 architectural limitation（context-completion compounding），非工程问题，不随模型增强消失。PF block 的 self-contained 结构从根本上绕过此瓶颈。 — **命中 Significance：从 "incremental pipeline optimization"（审稿人易判 borderline reject）提升为 "addressing fundamental scalability barrier"（审稿人更易给 accept）**

2. **[新增 Thesis and Contributions 章节，置于 Core Problem 之后]** — 建立显式双贡献结构：
   - **Claim 1（Empirical Finding）**: PF block 是已知唯一提供 closed-world formalization 属性的自然语言证明分解粒度——所有 premises 显式声明（→ Lean 4 hypotheses），单一 conclusion 显式声明（→ Lean 4 goal），无跨 block context 依赖（→ 消除 sequential error accumulation）。这使 PF block-level autoformalization 成功率显著高于 whole-proof（~35%）和普通 step-level（ProofFlow ICLR 2026: ProofScore 0.072）。此 finding 独立于本系统的其他设计选择，对任何需要 NL→formal 桥接的系统都有价值。
   - **Claim 2（System Design）**: 基于 Claim 1，设计 decision-theoretic selective verification pipeline，通过 Expected Verification Loss 最小化实现 cost-optimal cross-paradigm routing。
   — **命中 Novelty + Significance：双贡献结构让审稿人看到"不只是一个 pipeline"，Claim 1 是 reusable insight，Claim 2 是 principled system**

3. **[Core Problem]** — 在 "most uncertain proof blocks" 后添加 "and structurally critical"，匹配 dual-signal routing 设计 — **命中 Novelty（贯穿一致性）**

4. **[Research Landscape — 新增 generation vs. verification taxonomy]** — 建立显式分类：HERMES (Ospanov et al., ICML 2026) 是 proof generation agent（生成时交替 informal/formal，输出格式可控），本工作是 proof verification pipeline（输入为任意格式 NL 证明，PF 分解是必要的结构化步骤）。两者约束根本不同，不应直接比较。 — **命中 Related Work：防止审稿人将本工作与 HERMES 混淆（最可能的 novelty 质疑来源）**

5. **[Research Landscape — Ganguly et al. 三层差异化]** — 对 Grammars of Formal Uncertainty (Ganguly et al., NeurIPS 2025) 建立三层结构性区分，而非仅说 "different domain"：(1) uncertainty source：Ganguly 建模生成端分布（LLM→SMT-LIB program），本工作建模验证端判断 uncertainty（BV ensemble 对已有证明的判断分歧）；(2) routing target heterogeneity：Ganguly 在单一验证范式内路由（verify vs. abstain on SMT），本工作跨两种根本不同的验证范式路由（LLM verification → formal verification）；(3) structural criticality：Ganguly 无结构信号，本工作引入 dependency-graph criticality 作为正交路由维度。 — **命中 Novelty：从 "Ganguly applied to NL proofs" 变为 "fundamentally different routing framework"**

6. **[Research Landscape — 新增文献覆盖]** — 纳入以下审稿人可能知道的工作（原始 proposal 缺失）：
   - ThinkPRM (2025)：当前 SOTA data-efficient verbalized PRM，与 BV 的 CoT verification 直接可比
   - "Do We Need Frontier Models to Verify Mathematical Proofs?" (arXiv 2604.02450, 2026)：prompt ensemble 使小模型逼近 frontier，提升 LLM-only verification ceiling
   - ProofFlow (ICLR 2026)：dependency graph for autoformalization fidelity，ProofScore 0.545 vs step-proof 0.072——独立支撑 Claim 1
   - Process-Driven Autoformalization in Lean 4 (2024)：step-level formalization 比 whole-proof 更 tractable 的早期证据，但仍需 running Lean context（与 PF block 的 closed-world 不同）
   - UCCI (arXiv 2026)、RACER (arXiv 2026)：cost-optimal routing 的理论基础，支撑 Claim 2 的 decision-theoretic framing
   — **命中 Related Work：消除遗漏引用风险，审稿人看到全面覆盖会更放心**

7. **[Proposed Approach — 新增 Phase 0 Pilot Study]** — 在全面实验前设置 go/no-go 前置验证：随机抽取 50-100 PF blocks，测试 StepFun-Formalizer-32B autoformalization + Goedel-Prover-V2-32B proof search 的端到端成功率。Graded decision matrix：<30% → 需重新设计 Tier 2（引入 multi-shot formalization with compiler feedback self-correction）；30-50% → 调高 routing percentage 至 30-40%；50-70% → 按计划执行；>70% → 可降低 routing percentage。同时在 pilot 中验证 dependency DAG 质量（human evaluation, dependency precision/recall）。报告 effective Tier 2 coverage（实际完成 formal verification 的 block 占全部 block 的比例）。 — **命中 Technical Soundness：展示对核心假设的审慎态度，预防 "core assumption unproven" 攻击**

8. **[Proposed Approach — Routing 框架重述]** — 将原始的 "uncertainty × dependency criticality" ad-hoc 组合重述为 decision-theoretic Expected Verification Loss 框架：
   - E[Loss(b)] = P(BV_error | b) × C(error | b)
   - P 由 Platt-scaling 校准后的 ensemble uncertainty 估计
   - C 由 dependency graph 传递可达 block 数量（加权各下游 block 的 uncertainty）估计；主指标 fan-out degree，supplementary sensitivity analysis 含 dominator nodes 和 betweenness centrality
   - Routing 条件：E[Loss(b)] > marginal_cost(formal_verification_of_b)，阈值是 cost-risk 均衡的自然结果，非人工超参
   - 理论基础引用 UCCI (arXiv 2026) 对 threshold policies on calibrated probabilities are cost-optimal 的证明
   — **命中 Novelty：从 "we multiply two signals"（trivial combination 攻击面）提升为 "principled risk minimization with cost-optimal threshold"（有理论 grounding）**

9. **[Proposed Approach — Confident-but-wrong 显式讨论]** — 新增专节：(a) 引述 LLM 系统性过度自信的文献证据（nominal 99% CI 实际覆盖仅 ~65%）；(b) 三重缓解策略——ensemble disagreement 比 single-model confidence 更可靠、dependency criticality 作为 uncertainty-independent 路由信号、structural difficulty heuristic 作为补充特征；(c) 在 ablation 中做结构化归因分析（按数学领域、证明策略、block 特征分析 confident-but-wrong 模式）。 — **命中 Technical Soundness：主动应对审稿人最可能的 "what if your uncertainty signal is unreliable" 攻击**

10. **[Proposed Approach — Why calibrated uncertainty, not just heuristics]** — 新增论证：simple structural heuristics（block length, step count）捕捉表面复杂度，但 miss 结构简单却推理 subtle 的 block（如一步定理应用但应用方式 non-obvious）。Ensemble disagreement 恰好 flag 此类 case：当模型 copies 在 seemingly-simple block 上 disagree，信号是 hidden reasoning difficulty。通过 ablation head-to-head 对比 heuristic-only routing vs. calibrated uncertainty routing 来验证。 — **命中 Novelty：防御 "trivial alternative" 攻击（为什么不直接用简单规则路由）**

11. **[Proposed Approach — Calibration 方法修正]** — 从 isotonic regression on ArxivMathGradingBench 改为 Platt scaling on Synthetic set + miniF2F data。ArxivMathGradingBench 严格保留为 evaluation-only，消除 calibration-evaluation data leakage。Temperature scaling 作为 calibration method ablation。 — **命中 Technical Soundness：消除数据泄漏的实验设计硬伤**

12. **[Proposed Approach — Tier 2 增强]** — 增加 iterative self-correction for autoformalization failure（k=3 retries with Lean compiler feedback，参照 Goedel-Prover-V2 self-correction 模式 88.1%→90.4%）。明确 per-block timeout 5min / per-proof timeout 30min。Fallback strategy (accept / reject / majority-vote re-verification) 作为 ablation variable。 — **命中 Technical Soundness + Feasibility**

13. **[新增 Evaluation Plan 章节 — 原始 proposal 仅一句话，现扩展为完整设计]** — 结构化为以下模块：

    **Benchmarks (3)**:
    - ArxivMathGradingBench (Barkallah et al., 2026): 35 papers, 40 errors。仅用于最终 evaluation（不参与 calibration）。Bootstrap CI (1000 resamples), McNemar's test, Cohen's h effect size。补充 per-paper accuracy 和 per-block routing precision（~1050 blocks 提供更大统计功效）。预注册 power analysis。
    - Synthetic Error Detection Set: 600-800 instances。Multi-source construction: LLM-generated incorrect proofs + controlled perturbation of correct proofs + Hard2Verify extracted errors。严格三路划分: calibration 60% / validation 15% / evaluation 25%。Human validation on 50-80 instance subsample (Cohen's κ)。
    - miniF2F Verification Protocol: ≥8 candidate proofs per problem (≥100 problems) via QwQ-32B，evaluation: verification precision/recall。Aligned with Safe's miniF2F setting。

    **Baselines (7+)**:
    - PF+BV single-pass, PF+BV ensemble (N=5), PF+BV with specialized prompt ensemble (arXiv 2604.02450)
    - ThinkPRM (2025), Qwen2.5-Math-PRM-7B
    - Safe universal formalization (Liu et al., ACL 2025)
    - Frontier LLM single-pass reference (ceiling benchmark)
    - HERMES (Ospanov et al., ICML 2026) 作为 reference comparison（注明 generation vs. verification setting 差异）

    **Cost framework**: 统一 GPU-seconds per proof，详细 cost breakdown table（PF decomposition + ensemble BV + routing + autoformalization + proof search including retries/timeouts + fallback cost），Pareto curve (cost vs. recall) 绘制所有方法。

    **Ablations (8+)**:
    1. Uncertainty signal decomposition: ensemble disagreement / CoT entropy / combined → AUROC, ECE, recall@fixed-cost
    2. Routing signal: uncertainty only / dependency criticality only / simple structural heuristic only / dual signal → recall + cost
    3. Ensemble size: N=3 / N=5 / N=7
    4. Fallback strategy: accept / reject / majority-vote
    5. Threshold sweep: routing 5%-50% → Pareto curve
    6. **PF blocks vs. raw NL autoformalization (Claim 1 core validation)**: paired comparison, type-check rate + proof search success rate, Wilcoxon signed-rank test — **此实验是 core result，不仅是 ablation**
    7. Confident-but-wrong structured analysis: 按数学领域、证明策略、block 特征归因，quantify dual-signal vs uncertainty-only 的捕获率差异
    8. Tier 2 sensitivity analysis: 在假设成功率 30%/50%/70%/90% 下画系统 Pareto 曲线，展示 robustness

    **新增**: Per-tier false positive rate 分析 + FP rate vs. recall tradeoff 曲线。BV backbone sensitivity check (Qwen3.5-35B, N=3, on synthetic set) 作为 supplementary experiment。Calibration method ablation (Platt vs. temperature scaling)。

    — **命中 Technical Soundness：从 sketch 级设计提升为 publication-ready evaluation plan，覆盖审稿人可能提出的全部质疑维度**

14. **[Key References]** — 从 10 篇扩展到 17+ 篇。新增：ThinkPRM (2025), Qwen2.5-Math-PRM (2025), ProofSketcher (arXiv 2026), UCCI (arXiv 2026), ProofFlow (ICLR 2026), "Do We Need Frontier Models" (arXiv 2604.02450, 2026), Process-Driven Autoformalization (2024)。所有原始 10 篇引用完整保留。 — **命中 Related Work：全覆盖**

15. **[Resource Estimate]** — 更新：GPU 400-550h (A100-80GB) + CPU ~60h, timeline 14-18 weeks (2-3 researchers)，含 Phase 0 pilot (weeks 1-2) 和 PF 代码不可得时 +2-3 weeks contingency。$1200-1650 GPU cost。明确 Lean 4 proof search 的 wall-clock 估算（ArxivMathGradingBench 单次 pass ~9h）和 critical path 分解。 — **命中 Feasibility：展示实施风险的充分考量**

---

【主要风险】:

1. **Block-level autoformalization 端到端成功率可能落在 30-50% 灰色地带**（审稿人最可能攻击点）: StepFun-Formalizer-32B 在 statement-level 仅 40.5% BEq@1，Goedel-Prover-V2 proof search 虽在 miniF2F 达 88.1% 但那是 competition-level 标准化问题。Research-level PF blocks 的 formalization + proving 端到端成功率很可能低于预期。如果仅 30-50%，Tier 2 的实际 error detection 增量有限，系统可能退化为 "expensive ensemble BV + marginal formal verification bonus"。**缓解**: Phase 0 pilot study 是 go/no-go 关卡；graded decision matrix 确保灰色地带仍有可行路径；Tier 2 sensitivity analysis 预展示系统在不同成功率下的 robustness。

2. **Confident-but-wrong 比例可能高于预期**: 如果 BV 漏检的 ~50% 错误中，大部分是 BV 高置信度误判（而非 BV 不确定的遗漏），那么 uncertainty-guided routing 的 recall 上限将远低于 theoretical maximum。即使 dual-signal design 部分缓解（dependency criticality 是 uncertainty-independent），如果高置信度误判跨所有 block 类型均匀分布而非集中在 high-fan-out blocks，则 dependency criticality 也无法有效补偿。**缓解**: Ablation 7 的结构化归因分析将 quantify 此风险的实际严重程度，为后续工作指明方向。

---

【实施评估】:
  - **计算资源**: A100-80GB GPU，总计 400-550 GPU hours + ~60 CPU hours（Lean 4 kernel type-checking）。可在单节点 4×A100 上完成全部实验，无需分布式训练。预估 GPU 成本 $1200-1650（按 $3/GPU-hour 计）。Lean 4 proof search 单次 ArxivMathGradingBench pass 约 9h wall-clock。
  - **数据需求**: ArxivMathGradingBench（需从 Barkallah et al. 2026 获取，当前无公开代码/数据，需联系作者或自行复现——**最大 timeline 风险**）；Hard2Verify（公开可得）；miniF2F / miniF2F-v2（公开可得）；Synthetic Error Detection Set 需自行构建（600-800 instances）。
  - **人工介入**: (a) Synthetic set 人工验证子集：50-80 instances，数学研究生，~20-30 person-hours；(b) Pilot study dependency DAG quality evaluation：50-100 blocks，~10-15 person-hours；(c) Confident-but-wrong case 归因分析：领域专家参与，~10-15 person-hours。总人工约 40-60 person-hours。
  - **训练需求**: **无模型训练**。全部组件使用现成预训练模型推理（QwQ-32B, StepFun-Formalizer-32B, Goedel-Prover-V2-32B, ThinkPRM）。仅需 Platt scaling 校准（2 参数 logistic fit，几秒完成）。
  - **新 Benchmark**: 需构建 Synthetic Error Detection Set（600-800 instances）。三源构建：LLM 生成错误证明 + 对正确证明做 controlled perturbation（删除步骤 / 替换定理 / 修改计算）+ Hard2Verify 已知错误提取。含人工验证子集。预估构建时间 2-3 weeks。
  - **预估周期**: **14-18 weeks**（2-3 researchers）。Critical path: Phase 0 pilot (weeks 1-2) → PF pipeline setup + synthetic set construction (weeks 2-5) → uncertainty calibration (weeks 5-8) → full pipeline + ablations (weeks 8-15) → analysis + writing (weeks 15-18)。若 PF 代码不可得需额外 2-3 weeks 复现。距 AAAI 2026 投稿截止（预计 2026 年 8 月中旬）约 11 weeks，**timeline 紧张，建议立即启动 Phase 0 pilot 和联系 PF 作者获取代码/数据**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "124fcfd9-aa50-4ee6-b301-e9a8cb298b31",
  "isSidechain": false,
  "requestId": "req_011CbT8VS92RdRj3oRb67zPG",
  "type": "assistant",
  "uuid": "afeb6fa1-b53b-45b3-b627-165a184efac9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UX2rkaYEb38rtJFQxA4b1B",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9873,
      "cache_read_input_tokens": 86381,
      "output_tokens": 6063,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9873,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 6063,
          "cache_read_input_tokens": 86381,
          "cache_creation_input_tokens": 9873,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9873
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

_source line 85_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 流程已收敛且中位概率达交付门槛，请按「角色 C：最终输出」的通过格式，输出优化方案文本（对比原始 proposal 的修改建议列表 + 主要风险）。",
  "leafUuid": "afeb6fa1-b53b-45b3-b627-165a184efac9",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---

### Runtime record

_source line 86_

```json
{
  "type": "ai-title",
  "aiTitle": "Uncertainty-guided selective formal verification for proofs",
  "sessionId": "c4b58ce6-1e05-49ce-9f5b-5ac182d708a4"
}
```

---
