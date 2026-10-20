# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Premise-Graph Contrastive Trainin

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 52
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-2/68d7646a-bf03-45a6-a7a2-f1d82af85608.jsonl`
- **Structured JSON:** [`76839cea18dd9988a2a9.json`](../../sessions/76/76839cea18dd9988a2a9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:13:18.425Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:13:18.425Z",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models\n\n## Core Problem\n\nCurrent process reward models confuse surface fluency with logical validity — 43% of PRM reward gains are attributable to stylistic shortcuts rather than reasoning correctness — leading to catastrophic reward hacking during RL training where policies achieve >0.9 PRM scores but <4% actual accuracy. Can we train PRMs that are invariant to surface form but sensitive to logical structure?\n\n## Research Opportunity\n\nPERL (ICML 2025) demonstrated that LLMs can extract premise dependency links between reasoning steps at 90% recall, and that premise-aware verification improves error detection by 6-16%. However, this structural information has only been used at evaluation time, not for PRM training. Simultaneously, DAG-Math (2025) and ProofFlow (2025) have made dependency graph extraction from mathematical reasoning chains feasible. No prior work combines these premise dependency structures with contrastive PRM training to explicitly disentangle logical validity from surface fluency — addressing the documented root cause of PRM fragility at training time rather than through post-hoc corrections.\n\n## Research Landscape\n\nThe field has documented severe PRM robustness failures: 'Reward Under Attack' (arXiv:2603.06621, Feb 2026) showed PRMs function as fluency detectors with wide exploitable reward peaks, and 'Reward Models Identify Consistency, Not Causality' (arXiv:2502.14619, Feb 2025) confirmed this is fundamental. Existing defenses include CRA (Aug 2025, post-hoc sparse autoencoder correction), APRM (Nov 2025, adversarial training with harder negatives gaining +5.3pp OOD), CRM (ICLR 2026, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. On the infrastructure side, PARC/PERL (ICML 2025) showed premise links form DAGs with 90% extractable recall; GenPRM (AAAI 2026) provides code-verified step analysis; and AgentEval (arXiv:2604.23581, 2026) showed DAG-based dependency modeling yields +22pp failure detection recall over flat evaluation. The best PRMs on PRMBench score 67.7 (PathFinder-PRM-7B) vs. 83.8 human ceiling, leaving a 16-point gap where structural approaches could contribute. Concurrent work: CPMI (arXiv:2604.10660, April 2026) uses contrastive mutual information for PRM auto-labeling but does not employ premise dependency graphs; RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs in agentic tasks but uses no contrastive training and targets a different graph type; Graph of Verification (GoV) decomposes reasoning into DAGs for verification but is training-free. The specific combination of premise dependency DAGs with contrastive PRM training remains untried.\n\n## Proposed Approach\n\nExtract premise dependency DAGs from mathematical reasoning chains using PARC's proven extraction method (90% recall on Llama-3.1-8B-Instruct), then construct structure-aware contrastive training pairs: graph-preserving surface perturbations (rephrased steps maintaining identical DAG topology) as positives, and graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps preserving surface fluency) as hard negatives. Train a Qwen2.5-Math-7B-Instruct-based PRM with a dual objective combining standard step-correctness classification and a graph-contrastive InfoNCE loss over DAG-anchored step embeddings, forcing the model to learn representations invariant to surface form but sensitive to logical dependency structure. Augment PRM800K and Math-Shepherd seed chains (~300K solutions) with DAG annotations and ~600K contrastive pairs generated via LLM paraphrasing and targeted premise-link corruption. Evaluate on PRMBench (targeting >70 vs. 67.7 SOTA), ProcessBench, and the adversarial robustness suite from 'Reward Under Attack,' measuring both step-level accuracy and reduction in stylistic shortcut exploitability.\n\n## Detailed Description\n\nWe propose Premise-Graph Contrastive Training (PGCT), a method that leverages explicit logical dependency structure to train process reward models resistant to surface-form reward hacking. Current PRMs conflate fluency with validity — 43% of reward gains stem from stylistic shortcuts, and PRMs detect consistency rather than causality. Our key insight is that premise dependency DAGs, extractable at 90% recall via PARC (ICML 2025), provide a structural scaffold for contrastive training that disentangles these confounds. We construct graph-preserving surface perturbations (varied phrasing, identical logic) and graph-breaking fluent perturbations (severed premise links, maintained fluency) as contrastive pairs, training with a dual objective combining step-correctness prediction and InfoNCE loss over DAG-anchored representations. Built on Qwen2.5-Math-7B-Instruct with PRM800K and Math-Shepherd data augmented by ~600K structure-aware contrastive pairs, PGCT targets >70 on PRMBench (vs. 67.7 SOTA, 83.8 human ceiling) and substantially reduced adversarial exploitability. No prior work combines premise dependency graphs with contrastive PRM training — concurrent approaches (CPMI, CRM, RewardFlow) address complementary aspects but omit explicit logical structure from the training signal.\n\n## Key References\n\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv 2026, arXiv:2603.06621)\n- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)\n- Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs — PARC/PERL (ICML 2025, arXiv:2502.02362)\n- DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs (arXiv 2025, arXiv:2510.19842)\n- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv 2025, arXiv:2510.15981)\n- Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction — CRA (arXiv 2025, arXiv:2508.04216)\n- Adversarial Training for Process Reward Models — APRM (arXiv 2025, arXiv:2511.22888)\n- Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning — CRM (ICLR 2026, arXiv:2509.26578)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025, arXiv:2504.15275)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026, arXiv:2504.00891)\n- AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking (arXiv 2026, arXiv:2604.23581)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025, arXiv:2501.03124)\n- Efficient Process Reward Modeling via Contrastive Mutual Information — CPMI (arXiv 2026, arXiv:2604.10660)\n- RewardFlow: Topology-Aware Reward Propagation on State Graphs (arXiv 2026, arXiv:2603.18859)\n- PathFinder-PRM: Exploring Path Diversity in Step-Level Reward Models (arXiv 2025)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 700-1000 A100-hours (DAG extraction: ~80h, contrastive pair generation: ~120h, PRM training with ablations: ~400h, evaluation and baselines: ~100h), timeline: 14-18 weeks for 2-3 researchers, estimated_gpu_cost: $2,100-$3,000 at $3/hr A100 spot pricing\n- **human_in_loop**: gpu_hours: 500-700 A100-hours (Claude accelerates data pipeline debugging, contrastive pair quality filtering, and ablation design, reducing failed experiments ~30%), timeline: 10-14 weeks for 2 researchers, claude_api_cost: $400-$700 (data quality analysis, code generation, experiment triage), estimated_gpu_cost: $1,500-$2,100 at $3/hr A100 spot pricing\n- **auto_research**: gpu_hours: 800-1200 A100-hours (more parallel sweeps offset by automated experiment selection), timeline: 6-8 weeks with automated pipeline, claude_api_cost: $1,000-$1,500 (automated DAG quality validation, contrastive pair generation, hyperparameter sweep orchestration, paper drafting), estimated_gpu_cost: $2,400-$3,600 at $3/hr A100 spot pricing, speed_bottleneck: DAG extraction quality validation — premise link accuracy must be audited per-domain (algebra vs. geometry vs. combinatorics) before contrastive pairs are trustworthy; serial human spot-checks required\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:13:18.432Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:13:18.432Z",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

## Round 1

50 recorded events

### User

_source line 3 · 2026-05-27T08:13:18.448Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models

## Core Problem

Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains are attributable to stylistic shortcuts rather than reasoning correctness — leading to catastrophic reward hacking during RL training where policies achieve >0.9 PRM scores but <4% actual accuracy. Can we train PRMs that are invariant to surface form but sensitive to logical structure?

## Research Opportunity

PERL (ICML 2025) demonstrated that LLMs can extract premise dependency links between reasoning steps at 90% recall, and that premise-aware verification improves error detection by 6-16%. However, this structural information has only been used at evaluation time, not for PRM training. Simultaneously, DAG-Math (2025) and ProofFlow (2025) have made dependency graph extraction from mathematical reasoning chains feasible. No prior work combines these premise dependency structures with contrastive PRM training to explicitly disentangle logical validity from surface fluency — addressing the documented root cause of PRM fragility at training time rather than through post-hoc corrections.

## Research Landscape

The field has documented severe PRM robustness failures: 'Reward Under Attack' (arXiv:2603.06621, Feb 2026) showed PRMs function as fluency detectors with wide exploitable reward peaks, and 'Reward Models Identify Consistency, Not Causality' (arXiv:2502.14619, Feb 2025) confirmed this is fundamental. Existing defenses include CRA (Aug 2025, post-hoc sparse autoencoder correction), APRM (Nov 2025, adversarial training with harder negatives gaining +5.3pp OOD), CRM (ICLR 2026, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. On the infrastructure side, PARC/PERL (ICML 2025) showed premise links form DAGs with 90% extractable recall; GenPRM (AAAI 2026) provides code-verified step analysis; and AgentEval (arXiv:2604.23581, 2026) showed DAG-based dependency modeling yields +22pp failure detection recall over flat evaluation. The best PRMs on PRMBench score 67.7 (PathFinder-PRM-7B) vs. 83.8 human ceiling, leaving a 16-point gap where structural approaches could contribute. Concurrent work: CPMI (arXiv:2604.10660, April 2026) uses contrastive mutual information for PRM auto-labeling but does not employ premise dependency graphs; RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs in agentic tasks but uses no contrastive training and targets a different graph type; Graph of Verification (GoV) decomposes reasoning into DAGs for verification but is training-free. The specific combination of premise dependency DAGs with contrastive PRM training remains untried.

## Proposed Approach

Extract premise dependency DAGs from mathematical reasoning chains using PARC's proven extraction method (90% recall on Llama-3.1-8B-Instruct), then construct structure-aware contrastive training pairs: graph-preserving surface perturbations (rephrased steps maintaining identical DAG topology) as positives, and graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps preserving surface fluency) as hard negatives. Train a Qwen2.5-Math-7B-Instruct-based PRM with a dual objective combining standard step-correctness classification and a graph-contrastive InfoNCE loss over DAG-anchored step embeddings, forcing the model to learn representations invariant to surface form but sensitive to logical dependency structure. Augment PRM800K and Math-Shepherd seed chains (~300K solutions) with DAG annotations and ~600K contrastive pairs generated via LLM paraphrasing and targeted premise-link corruption. Evaluate on PRMBench (targeting >70 vs. 67.7 SOTA), ProcessBench, and the adversarial robustness suite from 'Reward Under Attack,' measuring both step-level accuracy and reduction in stylistic shortcut exploitability.

## Detailed Description

We propose Premise-Graph Contrastive Training (PGCT), a method that leverages explicit logical dependency structure to train process reward models resistant to surface-form reward hacking. Current PRMs conflate fluency with validity — 43% of reward gains stem from stylistic shortcuts, and PRMs detect consistency rather than causality. Our key insight is that premise dependency DAGs, extractable at 90% recall via PARC (ICML 2025), provide a structural scaffold for contrastive training that disentangles these confounds. We construct graph-preserving surface perturbations (varied phrasing, identical logic) and graph-breaking fluent perturbations (severed premise links, maintained fluency) as contrastive pairs, training with a dual objective combining step-correctness prediction and InfoNCE loss over DAG-anchored representations. Built on Qwen2.5-Math-7B-Instruct with PRM800K and Math-Shepherd data augmented by ~600K structure-aware contrastive pairs, PGCT targets >70 on PRMBench (vs. 67.7 SOTA, 83.8 human ceiling) and substantially reduced adversarial exploitability. No prior work combines premise dependency graphs with contrastive PRM training — concurrent approaches (CPMI, CRM, RewardFlow) address complementary aspects but omit explicit logical structure from the training signal.

## Key References

- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv 2026, arXiv:2603.06621)
- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)
- Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs — PARC/PERL (ICML 2025, arXiv:2502.02362)
- DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs (arXiv 2025, arXiv:2510.19842)
- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv 2025, arXiv:2510.15981)
- Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction — CRA (arXiv 2025, arXiv:2508.04216)
- Adversarial Training for Process Reward Models — APRM (arXiv 2025, arXiv:2511.22888)
- Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning — CRM (ICLR 2026, arXiv:2509.26578)
- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025, arXiv:2504.15275)
- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026, arXiv:2504.00891)
- AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking (arXiv 2026, arXiv:2604.23581)
- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025, arXiv:2501.03124)
- Efficient Process Reward Modeling via Contrastive Mutual Information — CPMI (arXiv 2026, arXiv:2604.10660)
- RewardFlow: Topology-Aware Reward Propagation on State Graphs (arXiv 2026, arXiv:2603.18859)
- PathFinder-PRM: Exploring Path Diversity in Step-Level Reward Models (arXiv 2025)

## Resource Estimate

- **manual**: gpu_hours: 700-1000 A100-hours (DAG extraction: ~80h, contrastive pair generation: ~120h, PRM training with ablations: ~400h, evaluation and baselines: ~100h), timeline: 14-18 weeks for 2-3 researchers, estimated_gpu_cost: $2,100-$3,000 at $3/hr A100 spot pricing
- **human_in_loop**: gpu_hours: 500-700 A100-hours (Claude accelerates data pipeline debugging, contrastive pair quality filtering, and ablation design, reducing failed experiments ~30%), timeline: 10-14 weeks for 2 researchers, claude_api_cost: $400-$700 (data quality analysis, code generation, experiment triage), estimated_gpu_cost: $1,500-$2,100 at $3/hr A100 spot pricing
- **auto_research**: gpu_hours: 800-1200 A100-hours (more parallel sweeps offset by automated experiment selection), timeline: 6-8 weeks with automated pipeline, claude_api_cost: $1,000-$1,500 (automated DAG quality validation, contrastive pair generation, hyperparameter sweep orchestration, paper drafting), estimated_gpu_cost: $2,400-$3,600 at $3/hr A100 spot pricing, speed_bottleneck: DAG extraction quality validation — premise link accuracy must be audited per-domain (algebra vs. geometry vs. combinatorics) before contrastive pairs are trustworthy; serial human spot-checks required


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "6175ded9-9769-4454-a9af-1a5b6e59250e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:13:18.445Z_

```json
{
  "parentUuid": "6175ded9-9769-4454-a9af-1a5b6e59250e",
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
  "uuid": "5e5d30ee-a41d-442d-8ad5-0c6cdff31b26",
  "timestamp": "2026-05-27T08:13:18.445Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:13:18.445Z_

```json
{
  "parentUuid": "5e5d30ee-a41d-442d-8ad5-0c6cdff31b26",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d28d837b-b7ba-4899-a9a7-07f5590768d0",
  "timestamp": "2026-05-27T08:13:18.445Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
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
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Assistant

_source line 7 · 2026-05-27T08:13:23.032Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal about "Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models" for AAAI 2026. I need to:

1. First, do web searches to understand the current landscape
2. Then evaluate the proposal according to the rubric

Let me start by searching for the key topics and papers mentioned in the proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d28d837b-b7ba-4899-a9a7-07f5590768d0",
  "isSidechain": false,
  "requestId": "req_011CbSjmgF7YQY88RpLHzmFv",
  "type": "assistant",
  "uuid": "db895401-8b43-4aa7-943c-ce152bcb1f7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RveBYsowkqG8MBc39VP9QY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6696,
      "cache_read_input_tokens": 11014,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6696,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 209,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6696
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

_source line 8 · 2026-05-27T08:13:23.588Z_

I'll start by conducting thorough web searches to understand the current research landscape before evaluating this proposal. Let me search for several key topics in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db895401-8b43-4aa7-943c-ce152bcb1f7d",
  "isSidechain": false,
  "requestId": "req_011CbSjmgF7YQY88RpLHzmFv",
  "type": "assistant",
  "uuid": "b48edda2-014e-4904-8e4c-ed05f5083dc1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RveBYsowkqG8MBc39VP9QY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6696,
      "cache_read_input_tokens": 11014,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6696,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 209,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6696
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

_source line 9 · 2026-05-27T08:13:24.142Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QshBemWCBKwKLb35CgrZRe`</summary>

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
  "parentUuid": "b48edda2-014e-4904-8e4c-ed05f5083dc1",
  "isSidechain": false,
  "requestId": "req_011CbSjmgF7YQY88RpLHzmFv",
  "type": "assistant",
  "uuid": "cf4beccc-808b-49af-875f-b07b484c5832",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RveBYsowkqG8MBc39VP9QY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6696,
      "cache_read_input_tokens": 11014,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6696,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 209,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6696,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6696
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

_source line 10 · 2026-05-27T08:13:24.150Z_

<details><summary>↩ Tool result · `toolu_01QshBemWCBKwKLb35CgrZRe`</summary>

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
  "parentUuid": "cf4beccc-808b-49af-875f-b07b484c5832",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "db55f133-07d4-4c33-b712-139687ff2dbe",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "cf4beccc-808b-49af-875f-b07b484c5832",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-27T08:13:26.490Z_

Now let me conduct multiple targeted searches in parallel to understand the research landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db55f133-07d4-4c33-b712-139687ff2dbe",
  "isSidechain": false,
  "requestId": "req_011CbSjn6aLb5Q2mHDkZfwdc",
  "type": "assistant",
  "uuid": "a6d81871-3487-4a45-9d9d-cb56c70421f8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jpwRnLK431SsZEVeszroV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 17710,
      "output_tokens": 309,
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
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 17710,
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

### Tool call

_source line 12 · 2026-05-27T08:13:27.726Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L583M73mbM6qhdJbGYkfA4`</summary>

```json
{
  "query": "process reward model robustness reward hacking contrastive training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6d81871-3487-4a45-9d9d-cb56c70421f8",
  "isSidechain": false,
  "requestId": "req_011CbSjn6aLb5Q2mHDkZfwdc",
  "type": "assistant",
  "uuid": "ff0471e9-29f8-487c-8c9e-fbe1f8b4f14d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jpwRnLK431SsZEVeszroV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 17710,
      "output_tokens": 309,
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
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 17710,
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

### Tool call

_source line 13 · 2026-05-27T08:13:28.498Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QkrYePesjo4bPsKiQpnFbj`</summary>

```json
{
  "query": "PERL PARC premise dependency DAG reasoning chains ICML 2025 arXiv:2502.02362"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff0471e9-29f8-487c-8c9e-fbe1f8b4f14d",
  "isSidechain": false,
  "requestId": "req_011CbSjn6aLb5Q2mHDkZfwdc",
  "type": "assistant",
  "uuid": "a4bbaba1-765c-4774-8e5c-e1c1455e5302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jpwRnLK431SsZEVeszroV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 17710,
      "output_tokens": 309,
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
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 17710,
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

### Tool call

_source line 14 · 2026-05-27T08:13:29.435Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R6a1ZTRfo12MXtVH3jhD5d`</summary>

```json
{
  "query": "PRMBench process reward model benchmark PathFinder-PRM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4bbaba1-765c-4774-8e5c-e1c1455e5302",
  "isSidechain": false,
  "requestId": "req_011CbSjn6aLb5Q2mHDkZfwdc",
  "type": "assistant",
  "uuid": "dbae6b0a-9969-4707-8835-8954df59eff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jpwRnLK431SsZEVeszroV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 17710,
      "output_tokens": 309,
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
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 17710,
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

### Tool call

_source line 15 · 2026-05-27T08:13:30.375Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F7Xcd2GsVgQmNpUVB3hgby`</summary>

```json
{
  "query": "\"reward under attack\" process reward model hackability arXiv:2603.06621 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dbae6b0a-9969-4707-8835-8954df59eff1",
  "isSidechain": false,
  "requestId": "req_011CbSjn6aLb5Q2mHDkZfwdc",
  "type": "assistant",
  "uuid": "d43399c4-88ff-4df6-b35a-5ad1fdb7cc70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jpwRnLK431SsZEVeszroV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 17710,
      "output_tokens": 309,
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
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 17710,
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

### Tool call

_source line 16 · 2026-05-27T08:13:31.025Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y7o63yGCJanzUcFDdsTr7n`</summary>

```json
{
  "query": "contrastive training process reward model premise graph logical structure 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d43399c4-88ff-4df6-b35a-5ad1fdb7cc70",
  "isSidechain": false,
  "requestId": "req_011CbSjn6aLb5Q2mHDkZfwdc",
  "type": "assistant",
  "uuid": "99f2deb2-4494-4f03-a27f-38ed8f29aabd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013jpwRnLK431SsZEVeszroV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 736,
      "cache_read_input_tokens": 17710,
      "output_tokens": 309,
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
          "input_tokens": 3,
          "output_tokens": 309,
          "cache_read_input_tokens": 17710,
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

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process re…",
  "leafUuid": "99f2deb2-4494-4f03-a27f-38ed8f29aabd",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Tool result

_source line 19 · 2026-05-27T08:13:35.630Z_

<details><summary>↩ Tool result · `toolu_01QkrYePesjo4bPsKiQpnFbj`</summary>

```text
Web search results for query: "PERL PARC premise dependency DAG reasoning chains ICML 2025 arXiv:2502.02362"

Links: [{"title":"[2502.02362] Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs","url":"https://arxiv.org/abs/2502.02362"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs | alphaXiv","url":"https://www.alphaxiv.org/abs/2502.02362"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification","url":"https://arxiv.org/pdf/2502.02362"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs","url":"https://arxiv.org/html/2502.02362"},{"title":"What Makes a Good Reasoning Chain? Uncovering Structural Patterns in Long Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2505.22148v1"}]

Based on the search results, here's what I found about the paper:

## Overview

The paper introduces PERL (Premises and ERrors identification in LLMs), a PARC-based dataset, demonstrating that LLMs can reliably identify premises within complex reasoning chains.

## Key Contribution

The framework restructures conventional linear reasoning chains into Premise Augmented Reasoning Chains (PARC) by introducing premise links, resulting in a directed acyclic graph where the nodes are the steps and the edges are the premise links.

## Motivation

Because LLM reasoning chains can be long and hard to verify, the work leverages the fact that mathematical reasoning allows each step to be derived from a small set of premises, which are a subset of the preceding steps in the reasoning chain.

## Results

Even open-source LLMs achieve 90% recall in premise identification. Additionally, the accuracy of error identification improves by 6% to 16% absolute when step-by-step verification is carried out in PARC under the premises.

The paper appears to be accepted at ICML 2025 and is available on arXiv as 2502.02362.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4bbaba1-765c-4774-8e5c-e1c1455e5302",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "4842bfde-099f-4a6b-89ad-462e4c4d642b",
  "toolUseResult": {
    "query": "PERL PARC premise dependency DAG reasoning chains ICML 2025 arXiv:2502.02362",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XW53AeJsTN3X6XHjtfYc9q",
        "content": [
          {
            "title": "[2502.02362] Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs",
            "url": "https://arxiv.org/abs/2502.02362"
          },
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2502.02362"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2601.17593"
          },
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification",
            "url": "https://arxiv.org/pdf/2502.02362"
          },
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs",
            "url": "https://arxiv.org/html/2502.02362"
          },
          {
            "title": "What Makes a Good Reasoning Chain? Uncovering Structural Patterns in Long Chain-of-Thought Reasoning",
            "url": "https://arxiv.org/html/2505.22148v1"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\n## Overview\n\nThe paper introduces PERL (Premises and ERrors identification in LLMs), a PARC-based dataset, demonstrating that LLMs can reliably identify premises within complex reasoning chains.\n\n## Key Contribution\n\nThe framework restructures conventional linear reasoning chains into Premise Augmented Reasoning Chains (PARC) by introducing premise links, resulting in a directed acyclic graph where the nodes are the steps and the edges are the premise links.\n\n## Motivation\n\nBecause LLM reasoning chains can be long and hard to verify, the work leverages the fact that mathematical reasoning allows each step to be derived from a small set of premises, which are a subset of the preceding steps in the reasoning chain.\n\n## Results\n\nEven open-source LLMs achieve 90% recall in premise identification. Additionally, the accuracy of error identification improves by 6% to 16% absolute when step-by-step verification is carried out in PARC under the premises.\n\nThe paper appears to be accepted at ICML 2025 and is available on arXiv as 2502.02362."
    ],
    "durationSeconds": 7.127674481,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a4bbaba1-765c-4774-8e5c-e1c1455e5302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T08:13:36.202Z_

<details><summary>↩ Tool result · `toolu_01L583M73mbM6qhdJbGYkfA4`</summary>

```text
Web search results for query: "process reward model robustness reward hacking contrastive training 2025 2026"

Links: [{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/pdf/2502.18770"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"},{"title":"[2409.13156] RRM: Robust Reward Model Training Mitigates Reward Hacking","url":"https://arxiv.org/abs/2409.13156"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"},{"title":"Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF","url":"https://arxiv.org/pdf/2509.24713"},{"title":"RRM: Robust Reward Model Training Mitigates Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=88AS5MQnmC"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/pdf/2604.02986"}]

I found several recent research papers on reward model robustness, reward hacking, and related techniques. Here are the key findings:

## Recent Work on Reward Hacking Mitigation

Reward hacking is the tendency for policy models to exploit weaknesses in the reward model to maximize reward signals without achieving genuine alignment or improvement, and this can manifest as degenerate behaviors, such as generating repetitive or overly verbose outputs, merely to satisfy the proxy reward.

## Methods to Address Robustness

Several approaches are being explored:

1. **Causal Frameworks**: Recent work on causally robust reward modeling addresses the challenge of reward hacking in the context of aligning Large Language Models via Reinforcement Learning from Human Feedback.

2. **Contrastive Methods**: Reward hacking occurs where the policy learns to exploit spurious cues that increase RM scores without genuinely improving underlying quality. In practice, models may internalize superficial heuristics that correlate with high reward—e.g., associating verbosity with factuality, agreement with helpfulness, or making tests pass without task completion.

3. **Adversarial Training**: Research uses adversarial samples to augment RM training, finding that such adversarial training results in reward models that are more robust to hacking and have better downstream performance in RLHF.

4. **Circuit-Based Approaches**: Circuit-Aware Reward Training uses circuit analysis to guide data augmentation, regularization, and ensemble strategies, providing both theoretical insights into reward model failures and practical interventions for improving longtail robustness.

These papers, published in 2025-2026, represent cutting-edge work on improving reward model robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff0471e9-29f8-487c-8c9e-fbe1f8b4f14d",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "8370cfc9-c311-472b-b482-094f219fd474",
  "toolUseResult": {
    "query": "process reward model robustness reward hacking contrastive training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011LBdbQwJ7U3jSAeredc7Km",
        "content": [
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/pdf/2502.18770"
          },
          {
            "title": "Robust Reward Modeling via Causal Rubrics",
            "url": "https://arxiv.org/pdf/2506.16507"
          },
          {
            "title": "[2409.13156] RRM: Robust Reward Model Training Mitigates Reward Hacking",
            "url": "https://arxiv.org/abs/2409.13156"
          },
          {
            "title": "IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/pdf/2602.19416"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.10623"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/pdf/2504.06141"
          },
          {
            "title": "Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF",
            "url": "https://arxiv.org/pdf/2509.24713"
          },
          {
            "title": "RRM: Robust Reward Model Training Mitigates Reward Hacking | OpenReview",
            "url": "https://openreview.net/forum?id=88AS5MQnmC"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/pdf/2604.02986"
          }
        ]
      },
      "I found several recent research papers on reward model robustness, reward hacking, and related techniques. Here are the key findings:\n\n## Recent Work on Reward Hacking Mitigation\n\nReward hacking is the tendency for policy models to exploit weaknesses in the reward model to maximize reward signals without achieving genuine alignment or improvement, and this can manifest as degenerate behaviors, such as generating repetitive or overly verbose outputs, merely to satisfy the proxy reward.\n\n## Methods to Address Robustness\n\nSeveral approaches are being explored:\n\n1. **Causal Frameworks**: Recent work on causally robust reward modeling addresses the challenge of reward hacking in the context of aligning Large Language Models via Reinforcement Learning from Human Feedback.\n\n2. **Contrastive Methods**: Reward hacking occurs where the policy learns to exploit spurious cues that increase RM scores without genuinely improving underlying quality. In practice, models may internalize superficial heuristics that correlate with high reward—e.g., associating verbosity with factuality, agreement with helpfulness, or making tests pass without task completion.\n\n3. **Adversarial Training**: Research uses adversarial samples to augment RM training, finding that such adversarial training results in reward models that are more robust to hacking and have better downstream performance in RLHF.\n\n4. **Circuit-Based Approaches**: Circuit-Aware Reward Training uses circuit analysis to guide data augmentation, regularization, and ensemble strategies, providing both theoretical insights into reward model failures and practical interventions for improving longtail robustness.\n\nThese papers, published in 2025-2026, represent cutting-edge work on improving reward model robustness."
    ],
    "durationSeconds": 8.471433367,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ff0471e9-29f8-487c-8c9e-fbe1f8b4f14d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T08:13:36.802Z_

<details><summary>↩ Tool result · `toolu_01F7Xcd2GsVgQmNpUVB3hgby`</summary>

```text
Web search results for query: ""reward under attack" process reward model hackability arXiv:2603.06621 2026"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Beyond Semantic Manipulation: Token-Space Attacks on Reward Models","url":"https://arxiv.org/pdf/2604.02686"},{"title":"Adversarial Reward-Hacking","url":"https://www.emergentmind.com/topics/adversarial-reward-hacking"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/pdf/2510.01367"},{"title":"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.01750"}]

Based on the search results, I found the paper you're looking for:

**"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models"** (arXiv:2603.06621) demonstrates that state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.

The paper introduces a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify vulnerabilities. The three tiers are: static perturbations (model-agnostic), adversarial tokens (white-box with gradients), and RL-induced reward hacking (black-box), with the first and third tiers producing natural text while the second establishes worst-case bounds.

The static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes with reward changes less than 0.1, yet inconsistent detection of logically-corrupted reasoning.

The paper was submitted on February 20, 2026. The authors include Rishabh Tiwari, Aditya Tomar, Udbhav Bamba, and others from institutions including UC Berkeley.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d43399c4-88ff-4df6-b35a-5ad1fdb7cc70",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "044e620c-38f4-4178-bc48-82c9502146d8",
  "toolUseResult": {
    "query": "\"reward under attack\" process reward model hackability arXiv:2603.06621 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J63Ei6GhGbLzW991PqhXGj",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Beyond Semantic Manipulation: Token-Space Attacks on Reward Models",
            "url": "https://arxiv.org/pdf/2604.02686"
          },
          {
            "title": "Adversarial Reward-Hacking",
            "url": "https://www.emergentmind.com/topics/adversarial-reward-hacking"
          },
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/pdf/2604.01476"
          },
          {
            "title": "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort",
            "url": "https://arxiv.org/pdf/2510.01367"
          },
          {
            "title": "Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/pdf/2602.01750"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**\"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\"** (arXiv:2603.06621) demonstrates that state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.\n\nThe paper introduces a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify vulnerabilities. The three tiers are: static perturbations (model-agnostic), adversarial tokens (white-box with gradients), and RL-induced reward hacking (black-box), with the first and third tiers producing natural text while the second establishes worst-case bounds.\n\nThe static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes with reward changes less than 0.1, yet inconsistent detection of logically-corrupted reasoning.\n\nThe paper was submitted on February 20, 2026. The authors include Rishabh Tiwari, Aditya Tomar, Udbhav Bamba, and others from institutions including UC Berkeley."
    ],
    "durationSeconds": 6.424703273000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d43399c4-88ff-4df6-b35a-5ad1fdb7cc70",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T08:13:38.619Z_

<details><summary>↩ Tool result · `toolu_01R6a1ZTRfo12MXtVH3jhD5d`</summary>

```text
Web search results for query: "PRMBench process reward model benchmark PathFinder-PRM 2025 2026"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"},{"title":"PRMBench: Benchmark for Process-level Math Reasoning","url":"https://www.emergentmind.com/topics/prmbench"},{"title":"GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.","url":"https://github.com/declare-lab/PathFinder-PRM"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"},{"title":"Process-Supervised Reward Model","url":"https://www.emergentmind.com/topics/process-supervised-reward-model-prm"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124"},{"title":"Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://huggingface.co/papers/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"}]

Based on the search results, here's what I found about PRMBench and PathFinder-PRM:

## PRMBench Overview

PRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of PRMs, comprising 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.

## PathFinder-PRM Performance

On PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3× less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.

## Key Innovation

PathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness. These results demonstrate that decoupled error detection and reward estimation not only boost fine-grained error detection but also substantially improve end-to-end, reward-guided mathematical reasoning with greater data efficiency.

The research represents recent advances (from 2025-2026) in evaluating and improving Process Reward Models for mathematical reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbae6b0a-9969-4707-8835-8954df59eff1",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "ee750441-50a1-4f7d-86c8-b40e4a412690",
  "toolUseResult": {
    "query": "PRMBench process reward model benchmark PathFinder-PRM 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NpwcMsMV2WRurGpdnUi2XB",
        "content": [
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF",
            "url": "https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"
          },
          {
            "title": "PRMBench: Benchmark for Process-level Math Reasoning",
            "url": "https://www.emergentmind.com/topics/prmbench"
          },
          {
            "title": "GitHub - declare-lab/PathFinder-PRM: This repository contains the official implementation of Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision.",
            "url": "https://github.com/declare-lab/PathFinder-PRM"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"
          },
          {
            "title": "Process-Supervised Reward Model",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-model-prm"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/pdf/2501.03124"
          },
          {
            "title": "[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/abs/2501.03124"
          },
          {
            "title": "Paper page - PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://huggingface.co/papers/2501.03124"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://prmbench.github.io/"
          }
        ]
      },
      "Based on the search results, here's what I found about PRMBench and PathFinder-PRM:\n\n## PRMBench Overview\n\nPRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of PRMs, comprising 6,216 carefully designed problems and 83,456 step-level labels, evaluating models across multiple dimensions, including simplicity, soundness, and sensitivity.\n\n## PathFinder-PRM Performance\n\nOn PRMBench, PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7, outperforming the prior best (65.5) while using 3× less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.\n\n## Key Innovation\n\nPathFinder-PRM is a novel hierarchical, error-aware discriminative PRM that first classifies math and consistency errors at each step, then combines these fine-grained signals to estimate step correctness. These results demonstrate that decoupled error detection and reward estimation not only boost fine-grained error detection but also substantially improve end-to-end, reward-guided mathematical reasoning with greater data efficiency.\n\nThe research represents recent advances (from 2025-2026) in evaluating and improving Process Reward Models for mathematical reasoning tasks."
    ],
    "durationSeconds": 9.180777364999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dbae6b0a-9969-4707-8835-8954df59eff1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T08:13:43.178Z_

<details><summary>↩ Tool result · `toolu_01Y7o63yGCJanzUcFDdsTr7n`</summary>

```text
Web search results for query: "contrastive training process reward model premise graph logical structure 2025 2026"

Links: [{"title":"Subgraph-Aware Training of Language Models for Knowledge Graph Completion Using Structure-Aware Contrastive Learning | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714946"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM ...","url":"https://openreview.net/pdf?id=TDfrN1TbGH"},{"title":"MERIt: Meta-Path Guided Contrastive Learning for Logical Reasoning","url":"https://arxiv.org/pdf/2203.00357"},{"title":"GitHub - JLZhong23/awesome-reward-models","url":"https://github.com/jlzhong23/awesome-reward-models"},{"title":"Information-aware graph contrastive learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12518162"},{"title":"Information-aware graph contrastive learning","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12511540"}]

Based on the web search results, here's what I found related to your query:

## Contrastive Training and Process Reward Models (2025-2026)

**Process Reward Models with Adversarial Training:**
Process Reward Models (PRMs) can identify subtle errors in reasoning, but current PRM training techniques predominantly rely on static datasets that cannot adapt to more nuanced errors. Some paradigms lack mechanisms to actively mine harder negatives.

**Contrastive Learning in Knowledge Graphs:**
Recent frameworks propose subgraph-aware training with contrastive learning focused on harder in-batch negative triples and harder positive triples in terms of structural properties of knowledge graphs.

**Logical Reasoning and Contrastive Learning:**
Contrastive learning approaches for logical reasoning find positive instance pairs according to logical structure, while negative ones are generated by modifying relations that break logical consistency.

**Reward Model Research (2025):**
Recent work includes research on process-supervised reward models for mathematical reasoning, multi-domain process reward models via synthetic reasoning data, and step-level reward models as navigators for reasoning.

The search results show active research combining contrastive training methods, process reward models, and logical/graph-based structures in 2025-2026, though the specific combination of all elements in your query appears across different research directions rather than in a single unified framework.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "99f2deb2-4494-4f03-a27f-38ed8f29aabd",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "3022ff56-ae2d-4ee8-a8fc-75da6b28ccb1",
  "toolUseResult": {
    "query": "contrastive training process reward model premise graph logical structure 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AtAh3qH63fofNJesbmPjTv",
        "content": [
          {
            "title": "Subgraph-Aware Training of Language Models for Knowledge Graph Completion Using Structure-Aware Contrastive Learning | Proceedings of the ACM on Web Conference 2025",
            "url": "https://dl.acm.org/doi/10.1145/3696410.3714946"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM ...",
            "url": "https://openreview.net/pdf?id=TDfrN1TbGH"
          },
          {
            "title": "MERIt: Meta-Path Guided Contrastive Learning for Logical Reasoning",
            "url": "https://arxiv.org/pdf/2203.00357"
          },
          {
            "title": "GitHub - JLZhong23/awesome-reward-models",
            "url": "https://github.com/jlzhong23/awesome-reward-models"
          },
          {
            "title": "Information-aware graph contrastive learning",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12518162"
          },
          {
            "title": "Information-aware graph contrastive learning",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12511540"
          }
        ]
      },
      "Based on the web search results, here's what I found related to your query:\n\n## Contrastive Training and Process Reward Models (2025-2026)\n\n**Process Reward Models with Adversarial Training:**\nProcess Reward Models (PRMs) can identify subtle errors in reasoning, but current PRM training techniques predominantly rely on static datasets that cannot adapt to more nuanced errors. Some paradigms lack mechanisms to actively mine harder negatives.\n\n**Contrastive Learning in Knowledge Graphs:**\nRecent frameworks propose subgraph-aware training with contrastive learning focused on harder in-batch negative triples and harder positive triples in terms of structural properties of knowledge graphs.\n\n**Logical Reasoning and Contrastive Learning:**\nContrastive learning approaches for logical reasoning find positive instance pairs according to logical structure, while negative ones are generated by modifying relations that break logical consistency.\n\n**Reward Model Research (2025):**\nRecent work includes research on process-supervised reward models for mathematical reasoning, multi-domain process reward models via synthetic reasoning data, and step-level reward models as navigators for reasoning.\n\nThe search results show active research combining contrastive training methods, process reward models, and logical/graph-based structures in 2025-2026, though the specific combination of all elements in your query appears across different research directions rather than in a single unified framework."
    ],
    "durationSeconds": 12.150172359,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "99f2deb2-4494-4f03-a27f-38ed8f29aabd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-27T08:13:47.533Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I've got the initial search results. Let me do a few more targeted searches to understand the specific related works better, especially CPMI, CRM, and RewardFlow, and to check for any work that directly combines premise graphs with contrastive PRM training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3022ff56-ae2d-4ee8-a8fc-75da6b28ccb1",
  "isSidechain": false,
  "requestId": "req_011CbSjoVgvTVTmfZy56iU3j",
  "type": "assistant",
  "uuid": "2f24210c-e4ba-4306-9687-0b93d32c0de9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cdm4asoiCawXS1JWDbrD28",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 18446,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 18446,
          "cache_creation_input_tokens": 3948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3948
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

_source line 25 · 2026-05-27T08:13:48.054Z_

Let me do a few more targeted searches to verify specific claims and check for closer related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f24210c-e4ba-4306-9687-0b93d32c0de9",
  "isSidechain": false,
  "requestId": "req_011CbSjoVgvTVTmfZy56iU3j",
  "type": "assistant",
  "uuid": "64b98d4f-0586-451b-8052-44755f252254",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cdm4asoiCawXS1JWDbrD28",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 18446,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 18446,
          "cache_creation_input_tokens": 3948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3948
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

_source line 26 · 2026-05-27T08:13:49.021Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X15zrVgQ4xYdSLm3ubECYr`</summary>

```json
{
  "query": "CPMI contrastive mutual information process reward model auto-labeling arXiv:2604.10660 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64b98d4f-0586-451b-8052-44755f252254",
  "isSidechain": false,
  "requestId": "req_011CbSjoVgvTVTmfZy56iU3j",
  "type": "assistant",
  "uuid": "fadbe3de-98c1-4161-b387-8c44f7f91ae5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cdm4asoiCawXS1JWDbrD28",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 18446,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 18446,
          "cache_creation_input_tokens": 3948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3948
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

_source line 27 · 2026-05-27T08:13:49.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Aa6MWFbrXGVTtZbiEzMtMT`</summary>

```json
{
  "query": "CRM conditional reward model ICLR 2026 arXiv:2509.26578 linking process outcome"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fadbe3de-98c1-4161-b387-8c44f7f91ae5",
  "isSidechain": false,
  "requestId": "req_011CbSjoVgvTVTmfZy56iU3j",
  "type": "assistant",
  "uuid": "755be95b-f42c-4e98-a0b0-5418fdfe145e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cdm4asoiCawXS1JWDbrD28",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 18446,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 18446,
          "cache_creation_input_tokens": 3948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3948
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

_source line 28 · 2026-05-27T08:13:50.972Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AESiKXrhi6MNj9x37riVKA`</summary>

```json
{
  "query": "\"reward models identify consistency not causality\" arXiv:2502.14619 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "755be95b-f42c-4e98-a0b0-5418fdfe145e",
  "isSidechain": false,
  "requestId": "req_011CbSjoVgvTVTmfZy56iU3j",
  "type": "assistant",
  "uuid": "87ff3f6d-fdcb-4e77-91b5-7b7ee6572a0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cdm4asoiCawXS1JWDbrD28",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 18446,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 18446,
          "cache_creation_input_tokens": 3948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3948
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

_source line 29 · 2026-05-27T08:13:51.776Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0147Jj1Kf5WoAfas96ER8pPo`</summary>

```json
{
  "query": "process reward model graph structure DAG contrastive pairs logical validity surface fluency 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87ff3f6d-fdcb-4e77-91b5-7b7ee6572a0b",
  "isSidechain": false,
  "requestId": "req_011CbSjoVgvTVTmfZy56iU3j",
  "type": "assistant",
  "uuid": "1ef2472e-149b-478c-9deb-4440cfda12c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cdm4asoiCawXS1JWDbrD28",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 18446,
      "output_tokens": 339,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3948,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 339,
          "cache_read_input_tokens": 18446,
          "cache_creation_input_tokens": 3948,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3948
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process re…",
  "leafUuid": "1ef2472e-149b-478c-9deb-4440cfda12c2",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Tool result

_source line 32 · 2026-05-27T08:13:55.555Z_

<details><summary>↩ Tool result · `toolu_01X15zrVgQ4xYdSLm3ubECYr`</summary>

```text
Web search results for query: "CPMI contrastive mutual information process reward model auto-labeling arXiv:2604.10660 2026"

Links: [{"title":"[2604.10660] Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/abs/2604.10660"},{"title":"Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/html/2604.10660"},{"title":"Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/pdf/2601.12748"},{"title":"Self-Supervised Contrastive Learning of Protein Representations By Mutual Information Maximization","url":"https://www.biorxiv.org/content/10.1101/2020.09.04.283929.full.pdf"},{"title":"Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations","url":"https://arxiv.org/html/2509.21511"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** Efficient Process Reward Modeling via Contrastive Mutual Information

**arXiv ID:** 2604.10660

**Publication Date:** April 12, 2026

**Key Contribution:**

The paper proposes contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing the computational burden of annotating dataset.

**How CPMI Works:**

CPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.

**Problem Addressed:**

Training a process reward model (PRM) typically requires human annotators to assign reward scores to each reasoning step, which is both costly and time-consuming. Existing automated approaches, such as Monte Carlo (MC) estimation, also demand substantial computational resources due to repeated LLM rollouts.

**Results:**

The experimental results show that CPMI-based labeling reduces dataset construction time by 84% and token generation by 98% compared to MC estimation, while achieving higher accuracy on process-level evaluations and mathematical reasoning benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fadbe3de-98c1-4161-b387-8c44f7f91ae5",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "120a57ee-26bd-4f99-a2df-9d8a68440dd7",
  "toolUseResult": {
    "query": "CPMI contrastive mutual information process reward model auto-labeling arXiv:2604.10660 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ShTAmvgnph8m38wZUszEAM",
        "content": [
          {
            "title": "[2604.10660] Efficient Process Reward Modeling via Contrastive Mutual Information",
            "url": "https://arxiv.org/abs/2604.10660"
          },
          {
            "title": "Efficient Process Reward Modeling via Contrastive Mutual Information",
            "url": "https://arxiv.org/html/2604.10660"
          },
          {
            "title": "Towards Robust Process Reward Modeling via Noise-aware Learning",
            "url": "https://arxiv.org/pdf/2601.12748"
          },
          {
            "title": "Self-Supervised Contrastive Learning of Protein Representations By Mutual Information Maximization",
            "url": "https://www.biorxiv.org/content/10.1101/2020.09.04.283929.full.pdf"
          },
          {
            "title": "Contrastive Mutual Information Learning: Toward Robust Representations without Positive-Pair Augmentations",
            "url": "https://arxiv.org/html/2509.21511"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Paper Title:** Efficient Process Reward Modeling via Contrastive Mutual Information\n\n**arXiv ID:** 2604.10660\n\n**Publication Date:** April 12, 2026\n\n**Key Contribution:**\n\nThe paper proposes contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing the computational burden of annotating dataset.\n\n**How CPMI Works:**\n\nCPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.\n\n**Problem Addressed:**\n\nTraining a process reward model (PRM) typically requires human annotators to assign reward scores to each reasoning step, which is both costly and time-consuming. Existing automated approaches, such as Monte Carlo (MC) estimation, also demand substantial computational resources due to repeated LLM rollouts.\n\n**Results:**\n\nThe experimental results show that CPMI-based labeling reduces dataset construction time by 84% and token generation by 98% compared to MC estimation, while achieving higher accuracy on process-level evaluations and mathematical reasoning benchmarks."
    ],
    "durationSeconds": 6.529320536999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fadbe3de-98c1-4161-b387-8c44f7f91ae5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T08:13:55.850Z_

<details><summary>↩ Tool result · `toolu_01Aa6MWFbrXGVTtZbiEzMtMT`</summary>

```text
Web search results for query: "CRM conditional reward model ICLR 2026 arXiv:2509.26578 linking process outcome"

Links: [{"title":"[2509.26578] Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/abs/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"[2509.26578v1] Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/abs/2509.26578v1"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/html/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=4DJoBOQNd0"}]

I found the paper you're searching for! Here's what I found:

The paper proposes Conditional Reward Modeling (CRM) that frames LLM reasoning as a temporal process leading to a correct answer, where the reward of each reasoning step is not only conditioned on the preceding steps but also explicitly linked to the final outcome of the reasoning trajectory.

**Key aspects of the research:**

- **Problem addressed**: Existing Process Reward Models (PRMs) either treat each reasoning step in isolation, failing to capture inter-step dependencies, or struggle to align process rewards with the final outcome, causing the reward signal to fail respecting temporal causality in sequential reasoning and facing ambiguous credit assignment.

- **Core innovation**: By enforcing conditional probability rules, the design captures the causal relationships among reasoning steps, with the link to the outcome allowing precise attribution of each intermediate step, thereby resolving credit assignment ambiguity.

- **Performance benefits**: Experiments across Best-of-N sampling, beam search and reinforcement learning demonstrate that CRM consistently outperforms existing reward models, and is more robust to reward hacking and delivers stable downstream improvements without relying on verifiable rewards derived from ground truth.

**Authors**: Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, and Kan Ren from ShanghaiTech University and BIGAI.

The paper is available on arXiv and appears to be under review at ICLR 2026 based on the OpenReview listing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "755be95b-f42c-4e98-a0b0-5418fdfe145e",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "6c63550d-afea-4a48-a9e2-4de6fff08638",
  "toolUseResult": {
    "query": "CRM conditional reward model ICLR 2026 arXiv:2509.26578 linking process outcome",
    "results": [
      {
        "tool_use_id": "srvtoolu_016yvKb1w3zkf74wAjgUNvmB",
        "content": [
          {
            "title": "[2509.26578] Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/abs/2509.26578"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          },
          {
            "title": "[2509.26578v1] Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/abs/2509.26578v1"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/html/2509.26578"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=4DJoBOQNd0"
          }
        ]
      },
      "I found the paper you're searching for! Here's what I found:\n\nThe paper proposes Conditional Reward Modeling (CRM) that frames LLM reasoning as a temporal process leading to a correct answer, where the reward of each reasoning step is not only conditioned on the preceding steps but also explicitly linked to the final outcome of the reasoning trajectory.\n\n**Key aspects of the research:**\n\n- **Problem addressed**: Existing Process Reward Models (PRMs) either treat each reasoning step in isolation, failing to capture inter-step dependencies, or struggle to align process rewards with the final outcome, causing the reward signal to fail respecting temporal causality in sequential reasoning and facing ambiguous credit assignment.\n\n- **Core innovation**: By enforcing conditional probability rules, the design captures the causal relationships among reasoning steps, with the link to the outcome allowing precise attribution of each intermediate step, thereby resolving credit assignment ambiguity.\n\n- **Performance benefits**: Experiments across Best-of-N sampling, beam search and reinforcement learning demonstrate that CRM consistently outperforms existing reward models, and is more robust to reward hacking and delivers stable downstream improvements without relying on verifiable rewards derived from ground truth.\n\n**Authors**: Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, and Kan Ren from ShanghaiTech University and BIGAI.\n\nThe paper is available on arXiv and appears to be under review at ICLR 2026 based on the OpenReview listing."
    ],
    "durationSeconds": 5.8772410430000015,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "755be95b-f42c-4e98-a0b0-5418fdfe145e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-27T08:13:59.385Z_

<details><summary>↩ Tool result · `toolu_0147Jj1Kf5WoAfas96ER8pPo`</summary>

```text
Web search results for query: "process reward model graph structure DAG contrastive pairs logical validity surface fluency 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2505.02387"},{"title":"DPRM: A Dual Implicit Process Reward Model in Multi-Hop Question Answering","url":"https://arxiv.org/pdf/2511.08364"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"Process Reward Model with Q-Value Rankings","url":"https://arxiv.org/pdf/2410.11287"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"}]

Based on the search results, I found several relevant papers on process reward models and related topics from 2026:

**Key Findings:**

1. **DAG Structure in Reasoning**: Research analyzes the emergence of DAG structure across layers in language models, finding that DAG structure is meaningfully encoded in LLM representations with recoverability peaking in intermediate layers. This suggests that LLM reasoning exhibits measurable internal graph structure rather than being purely sequential.

2. **Dual Implicit Process Reward Models**: A proposed DPRM addresses the limitation that existing implicit PRMs cannot handle graph structure constraints in knowledge graphs by training two implicit PRMs for CoT and KG reasoning in multi-hop question answering tasks.

3. **Process Reward Modeling Approaches**: Process reward models provide finer-grained rewards at the level of individual reasoning steps or even tokens. One approach optimizes Q-value rankings using a novel comparative loss function, providing a more granular and theoretically grounded methodology for process rewards.

4. **Conditional Reward Modeling**: Conditional Reward Modeling frames reasoning as a temporal process where the reward signal is modeled as the probabilistic evolution of deriving the correct outcome conditioned on existing reasoning steps.

5. **Application to Data Analysis**: Process Reward Models have shown success in mathematical reasoning and code generation by providing step-level supervision and fine-grained verification.

These results show active research in 2026 on connecting process reward models with graph-based reasoning structures and logical validity in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ef2472e-149b-478c-9deb-4440cfda12c2",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "6d37c2f4-7266-4c70-9bc8-72d4f1381899",
  "toolUseResult": {
    "query": "process reward model graph structure DAG contrastive pairs logical validity surface fluency 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PntxxiXGQfLtWJE5xAsjfQ",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2505.02387"
          },
          {
            "title": "DPRM: A Dual Implicit Process Reward Model in Multi-Hop Question Answering",
            "url": "https://arxiv.org/pdf/2511.08364"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2601.17593"
          },
          {
            "title": "Process Reward Model with Q-Value Rankings",
            "url": "https://arxiv.org/pdf/2410.11287"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.26578"
          },
          {
            "title": "Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis",
            "url": "https://arxiv.org/html/2604.24198v1"
          }
        ]
      },
      "Based on the search results, I found several relevant papers on process reward models and related topics from 2026:\n\n**Key Findings:**\n\n1. **DAG Structure in Reasoning**: Research analyzes the emergence of DAG structure across layers in language models, finding that DAG structure is meaningfully encoded in LLM representations with recoverability peaking in intermediate layers. This suggests that LLM reasoning exhibits measurable internal graph structure rather than being purely sequential.\n\n2. **Dual Implicit Process Reward Models**: A proposed DPRM addresses the limitation that existing implicit PRMs cannot handle graph structure constraints in knowledge graphs by training two implicit PRMs for CoT and KG reasoning in multi-hop question answering tasks.\n\n3. **Process Reward Modeling Approaches**: Process reward models provide finer-grained rewards at the level of individual reasoning steps or even tokens. One approach optimizes Q-value rankings using a novel comparative loss function, providing a more granular and theoretically grounded methodology for process rewards.\n\n4. **Conditional Reward Modeling**: Conditional Reward Modeling frames reasoning as a temporal process where the reward signal is modeled as the probabilistic evolution of deriving the correct outcome conditioned on existing reasoning steps.\n\n5. **Application to Data Analysis**: Process Reward Models have shown success in mathematical reasoning and code generation by providing step-level supervision and fine-grained verification.\n\nThese results show active research in 2026 on connecting process reward models with graph-based reasoning structures and logical validity in language models."
    ],
    "durationSeconds": 7.605868061999994,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1ef2472e-149b-478c-9deb-4440cfda12c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-27T08:14:00.788Z_

<details><summary>↩ Tool result · `toolu_01AESiKXrhi6MNj9x37riVKA`</summary>

```text
Web search results for query: ""reward models identify consistency not causality" arXiv:2502.14619 2025"

Links: [{"title":"[2502.14619] Reward Models Identify Consistency, Not Causality","url":"https://arxiv.org/abs/2502.14619"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=7400"},{"title":"Artificial Intelligence Feb 2025","url":"https://arxiv.org/list/cs.AI/2025-02?skip=2575&show=50"},{"title":"Reward Models Identify Consistency, Not Causality Yuhui Xu∗ Hanze Dong Lei Wang","url":"https://arxiv.org/pdf/2502.14619"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=17825&show=25"},{"title":"Computation and Language Feb 2025","url":"https://www.arxiv.org/list/cs.CL/2025-02?skip=2050&show=500"},{"title":"Machine Learning Feb 2025","url":"https://www.arxiv.org/list/cs.LG/2025-02?skip=1750&show=50"},{"title":"EQA-RM: A Generative Embodied Reward Model with Test-time Scaling","url":"https://arxiv.org/html/2506.10389v1"}]

I found the paper you were searching for. Here's what the search revealed:

## "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619)

This paper presents findings about reward models (RMs) and their role in aligning large language models with human preferences. The research challenges common assumptions about how RMs behave.

### Key Findings

The analysis reveals that state-of-the-art reward models prioritize structural consistency over causal correctness. More specifically, removing the problem statement has minimal impact on reward scores, whereas altering numerical values or disrupting the reasoning flow significantly affects RM outputs.

RMs exhibit a strong dependence on complete reasoning trajectories—truncated or incomplete steps lead to significant variations in reward assignments, indicating that RMs primarily rely on learned reasoning patterns rather than explicit problem comprehension.

### Main Insights

The key insights are: (1) RMs primarily assess coherence rather than true reasoning quality; (2) The role of explicit problem comprehension in reward assignment is overstated; and (3) Current RMs may be more effective at ranking responses through pattern recognition than causal understanding.

The paper was submitted on February 20, 2025, and is 16 pages long. It's authored by Yuhui Xu, Hanze Dong, Lei Wang, Caiming Xiong, and Junnan Li, and has been cross-listed across Machine Learning (cs.LG), Artificial Intelligence (cs.AI), and Computation and Language (cs.CL) categories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87ff3f6d-fdcb-4e77-91b5-7b7ee6572a0b",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "50e0b925-5169-4d57-9189-966ebe7e0cee",
  "toolUseResult": {
    "query": "\"reward models identify consistency not causality\" arXiv:2502.14619 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N7Bbegjz28hgyTWgve6qh9",
        "content": [
          {
            "title": "[2502.14619] Reward Models Identify Consistency, Not Causality",
            "url": "https://arxiv.org/abs/2502.14619"
          },
          {
            "title": "Computer Science Feb 2025",
            "url": "https://arxiv.org/list/cs/2025-02?skip=7400"
          },
          {
            "title": "Artificial Intelligence Feb 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-02?skip=2575&show=50"
          },
          {
            "title": "Reward Models Identify Consistency, Not Causality Yuhui Xu∗ Hanze Dong Lei Wang",
            "url": "https://arxiv.org/pdf/2502.14619"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=17825&show=25"
          },
          {
            "title": "Computation and Language Feb 2025",
            "url": "https://www.arxiv.org/list/cs.CL/2025-02?skip=2050&show=500"
          },
          {
            "title": "Machine Learning Feb 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-02?skip=1750&show=50"
          },
          {
            "title": "EQA-RM: A Generative Embodied Reward Model with Test-time Scaling",
            "url": "https://arxiv.org/html/2506.10389v1"
          }
        ]
      },
      "I found the paper you were searching for. Here's what the search revealed:\n\n## \"Reward Models Identify Consistency, Not Causality\" (arXiv:2502.14619)\n\nThis paper presents findings about reward models (RMs) and their role in aligning large language models with human preferences. The research challenges common assumptions about how RMs behave.\n\n### Key Findings\n\nThe analysis reveals that state-of-the-art reward models prioritize structural consistency over causal correctness. More specifically, removing the problem statement has minimal impact on reward scores, whereas altering numerical values or disrupting the reasoning flow significantly affects RM outputs.\n\nRMs exhibit a strong dependence on complete reasoning trajectories—truncated or incomplete steps lead to significant variations in reward assignments, indicating that RMs primarily rely on learned reasoning patterns rather than explicit problem comprehension.\n\n### Main Insights\n\nThe key insights are: (1) RMs primarily assess coherence rather than true reasoning quality; (2) The role of explicit problem comprehension in reward assignment is overstated; and (3) Current RMs may be more effective at ranking responses through pattern recognition than causal understanding.\n\nThe paper was submitted on February 20, 2025, and is 16 pages long. It's authored by Yuhui Xu, Hanze Dong, Lei Wang, Caiming Xiong, and Junnan Li, and has been cross-listed across Machine Learning (cs.LG), Artificial Intelligence (cs.AI), and Computation and Language (cs.CL) categories."
    ],
    "durationSeconds": 9.813440143,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "87ff3f6d-fdcb-4e77-91b5-7b7ee6572a0b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-27T08:14:00.796Z_

```json
{
  "parentUuid": "50e0b925-5169-4d57-9189-966ebe7e0cee",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "7573284d-57fe-41ba-b140-53212ff6aa63",
  "timestamp": "2026-05-27T08:14:00.796Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-27T08:14:03.580Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more round of searches to check a few more specific claims and potential competing work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7573284d-57fe-41ba-b140-53212ff6aa63",
  "isSidechain": false,
  "requestId": "req_011CbSjpo1Va9PjBYzmJSuHf",
  "type": "assistant",
  "uuid": "3337dc40-983f-4a46-bcb4-4c013a3cc1cc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBtRqvbd2d9xYb65DWwyGn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 648,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 22394,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 648,
          "output_tokens": 262,
          "cache_read_input_tokens": 22394,
          "cache_creation_input_tokens": 2424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2424
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

_source line 38 · 2026-05-27T08:14:04.536Z_

Let me do one more round of searches to check the "43% stylistic shortcuts" claim and look for any very recent work that might directly compete.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3337dc40-983f-4a46-bcb4-4c013a3cc1cc",
  "isSidechain": false,
  "requestId": "req_011CbSjpo1Va9PjBYzmJSuHf",
  "type": "assistant",
  "uuid": "d954570d-760f-43b3-96ce-f436b930b14a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBtRqvbd2d9xYb65DWwyGn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 648,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 22394,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 648,
          "output_tokens": 262,
          "cache_read_input_tokens": 22394,
          "cache_creation_input_tokens": 2424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2424
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

_source line 39 · 2026-05-27T08:14:05.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DNtmH3GhakKCtPXXSERzQE`</summary>

```json
{
  "query": "PRM reward hacking \"43%\" stylistic shortcuts surface fluency process reward model 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d954570d-760f-43b3-96ce-f436b930b14a",
  "isSidechain": false,
  "requestId": "req_011CbSjpo1Va9PjBYzmJSuHf",
  "type": "assistant",
  "uuid": "45da4baf-66dd-4f95-a4fc-4c0798dbdfc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBtRqvbd2d9xYb65DWwyGn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 648,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 22394,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 648,
          "output_tokens": 262,
          "cache_read_input_tokens": 22394,
          "cache_creation_input_tokens": 2424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2424
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

_source line 40 · 2026-05-27T08:14:06.555Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016wzMRatid31zb8QYceiWb5`</summary>

```json
{
  "query": "adversarial process reward model APRM arXiv:2511.22888 harder negatives OOD 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45da4baf-66dd-4f95-a4fc-4c0798dbdfc5",
  "isSidechain": false,
  "requestId": "req_011CbSjpo1Va9PjBYzmJSuHf",
  "type": "assistant",
  "uuid": "82ed88da-6cb6-4ee4-8984-a34a94ef363b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBtRqvbd2d9xYb65DWwyGn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 648,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 22394,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 648,
          "output_tokens": 262,
          "cache_read_input_tokens": 22394,
          "cache_creation_input_tokens": 2424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2424
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

_source line 41 · 2026-05-27T08:14:07.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016dxpVZi85dXW4i5cWA6Tnv`</summary>

```json
{
  "query": "GenPRM code-verified step analysis AAAI 2026 arXiv:2504.00891"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82ed88da-6cb6-4ee4-8984-a34a94ef363b",
  "isSidechain": false,
  "requestId": "req_011CbSjpo1Va9PjBYzmJSuHf",
  "type": "assistant",
  "uuid": "244ab647-b030-4615-b5b6-cb1fe71d6306",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PBtRqvbd2d9xYb65DWwyGn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 648,
      "cache_creation_input_tokens": 2424,
      "cache_read_input_tokens": 22394,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2424,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 648,
          "output_tokens": 262,
          "cache_read_input_tokens": 22394,
          "cache_creation_input_tokens": 2424,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2424
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

_source line 42 · 2026-05-27T08:14:12.611Z_

<details><summary>↩ Tool result · `toolu_01DNtmH3GhakKCtPXXSERzQE`</summary>

```text
Web search results for query: "PRM reward hacking "43%" stylistic shortcuts surface fluency process reward model 2025 2026"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Rectifying Shortcut Behaviors in Preference-based Reward Learning","url":"https://arxiv.org/pdf/2510.19050"},{"title":"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning","url":"https://arxiv.org/pdf/2504.15275"},{"title":"Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort","url":"https://arxiv.org/pdf/2510.01367"}]

I found relevant research on this topic. Here are the key findings from the search results:

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure. A three-tiered diagnostic framework has been introduced that applies increasing adversarial pressure to quantify these vulnerabilities.

The "43%" finding you mentioned appears in recent research: Approximately 43% of the reward gain in RL-trained policies is attributable to stylistic shortcuts rather than genuine reasoning improvements. More specifically, RL-trained policies on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

Static perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes (reward changes <0.1), yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.

These findings reveal that current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

This research was published in February 2026 and appears to be the paper you were searching for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45da4baf-66dd-4f95-a4fc-4c0798dbdfc5",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "e980e435-0353-4323-925f-5c49141df928",
  "toolUseResult": {
    "query": "PRM reward hacking \"43%\" stylistic shortcuts surface fluency process reward model 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016wwknbggnguw3pu8mDvgQV",
        "content": [
          {
            "title": "[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
            "url": "https://arxiv.org/abs/2603.06621"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2603.06621"
          },
          {
            "title": "Reward Under Attack: Analyzing the Robustness and Hackability of",
            "url": "https://arxiv.org/pdf/2603.06621"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Rectifying Shortcut Behaviors in Preference-based Reward Learning",
            "url": "https://arxiv.org/pdf/2510.19050"
          },
          {
            "title": "Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning",
            "url": "https://arxiv.org/pdf/2504.15275"
          },
          {
            "title": "Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort",
            "url": "https://arxiv.org/pdf/2510.01367"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key findings from the search results:\n\nProcess Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure. A three-tiered diagnostic framework has been introduced that applies increasing adversarial pressure to quantify these vulnerabilities.\n\nThe \"43%\" finding you mentioned appears in recent research: Approximately 43% of the reward gain in RL-trained policies is attributable to stylistic shortcuts rather than genuine reasoning improvements. More specifically, RL-trained policies on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\nStatic perturbation analysis uncovers a fluency-logic dissociation: high invariance to surface-level style changes (reward changes <0.1), yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.\n\nThese findings reveal that current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\nThis research was published in February 2026 and appears to be the paper you were searching for."
    ],
    "durationSeconds": 7.053464245999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "45da4baf-66dd-4f95-a4fc-4c0798dbdfc5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 43_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process re…",
  "leafUuid": "e980e435-0353-4323-925f-5c49141df928",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Tool result

_source line 45 · 2026-05-27T08:14:13.202Z_

<details><summary>↩ Tool result · `toolu_016wzMRatid31zb8QYceiWb5`</summary>

```text
Web search results for query: "adversarial process reward model APRM arXiv:2511.22888 harder negatives OOD 2025"

Links: [{"title":"[2511.22888] Adversarial Training for Process Reward Models","url":"https://arxiv.org/abs/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/html/2511.22888"},{"title":"Adversarial Training for Process Reward Models","url":"https://arxiv.org/pdf/2511.22888"},{"title":"Adversarially Trained Reward Models","url":"https://www.emergentmind.com/topics/adversarially-trained-reward-models"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/html/2504.06141v2"},{"title":"[2504.06141] Adversarial Training of Reward Models","url":"https://arxiv.org/abs/2504.06141"}]

Based on the search results, here's what I found about the paper arXiv:2511.22888:

## Adversarial Training for Process Reward Models (APRM)

Process Reward Models (PRMs) enhance reasoning ability of LLMs by providing step-level supervision, but their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors.

The paper introduces Adversarially Trained PRMs (APRM), where a Generator learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them. This interaction yields progressively harder negatives for the PRM, improving its robustness and generalization to novel errors without requiring manual step-level labels.

### Results

Averaged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline. More notably, APRM achieves gains of +5.3 pp on out-of-distribution tasks.

The paper was submitted on November 28, 2025, and formalizes PRM training as a two-player, general-sum, non-cooperative game where the competitive interaction between the generator and PRM creates an adaptive curriculum, directly addressing the limitations of static or passively generated training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "82ed88da-6cb6-4ee4-8984-a34a94ef363b",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "feaebea8-18b5-4c42-94b9-7b643f9f99c3",
  "toolUseResult": {
    "query": "adversarial process reward model APRM arXiv:2511.22888 harder negatives OOD 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VHzobitY6eeB5Seb96hvKC",
        "content": [
          {
            "title": "[2511.22888] Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/abs/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/html/2511.22888"
          },
          {
            "title": "Adversarial Training for Process Reward Models",
            "url": "https://arxiv.org/pdf/2511.22888"
          },
          {
            "title": "Adversarially Trained Reward Models",
            "url": "https://www.emergentmind.com/topics/adversarially-trained-reward-models"
          },
          {
            "title": "Adversarial Training of Reward Models",
            "url": "https://arxiv.org/html/2504.06141v2"
          },
          {
            "title": "[2504.06141] Adversarial Training of Reward Models",
            "url": "https://arxiv.org/abs/2504.06141"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper arXiv:2511.22888:\n\n## Adversarial Training for Process Reward Models (APRM)\n\nProcess Reward Models (PRMs) enhance reasoning ability of LLMs by providing step-level supervision, but their widespread adoption is limited due to expensive manual step-level annotation and poor generalization of static training data to novel errors.\n\nThe paper introduces Adversarially Trained PRMs (APRM), where a Generator learns to produce reasoning errors to deceive a PRM, while the PRM concurrently learns to detect them. This interaction yields progressively harder negatives for the PRM, improving its robustness and generalization to novel errors without requiring manual step-level labels.\n\n### Results\n\nAveraged across diverse mathematical reasoning benchmarks, APRM improves solver accuracy by +3.4 percentage points over the strongest PRM baseline. More notably, APRM achieves gains of +5.3 pp on out-of-distribution tasks.\n\nThe paper was submitted on November 28, 2025, and formalizes PRM training as a two-player, general-sum, non-cooperative game where the competitive interaction between the generator and PRM creates an adaptive curriculum, directly addressing the limitations of static or passively generated training data."
    ],
    "durationSeconds": 6.643043452999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "82ed88da-6cb6-4ee4-8984-a34a94ef363b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-27T08:14:13.680Z_

<details><summary>↩ Tool result · `toolu_016dxpVZi85dXW4i5cWA6Tnv`</summary>

```text
Web search results for query: "GenPRM code-verified step analysis AAAI 2026 arXiv:2504.00891"

Links: [{"title":"GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".","url":"https://github.com/RyanLiu112/GenPRM"},{"title":"[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://arxiv.org/abs/2504.00891"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Arxiv - DeepPaper","url":"https://arxiv.deeppaper.ai/papers/2504.00891v2"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward ...","url":"https://arxiv.org/pdf/2504.00891"},{"title":"Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis","url":"https://arxiv.org/html/2604.24198v1"},{"title":"GenPRM/GenPRM-1.5B · Hugging Face","url":"https://huggingface.co/GenPRM/GenPRM-1.5B"},{"title":"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning","url":"https://ryanliu112.github.io/GenPRM/"}]

I found relevant information about GenPRM. Here's what I found:

## GenPRM Overview

GenPRM has been accepted by AAAI 2026. The paper is titled "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning" and is available as arXiv preprint arXiv:2504.00891.

## What is GenPRM?

GenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. 

GenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought reasoning and code verification processes before providing final judgment.

## Key Methodology

To obtain high-quality process supervision labels and rationale data, the authors propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification.

## Performance

Experimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only 23K training data from MATH.

The official codebase is available on GitHub, and various model versions are available on Hugging Face.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "244ab647-b030-4615-b5b6-cb1fe71d6306",
  "isSidechain": false,
  "promptId": "b1c7793f-5e10-4491-9c54-1f0d15f42bdc",
  "type": "user",
  "uuid": "10d6b843-aa3b-43db-b866-a2e3da970505",
  "toolUseResult": {
    "query": "GenPRM code-verified step analysis AAAI 2026 arXiv:2504.00891",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J88G3ZffKLv1EHj4e5RniU",
        "content": [
          {
            "title": "GitHub - RyanLiu112/GenPRM: [AAAI 2026] Official codebase for \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\".",
            "url": "https://github.com/RyanLiu112/GenPRM"
          },
          {
            "title": "[2504.00891] GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
            "url": "https://arxiv.org/abs/2504.00891"
          },
          {
            "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning | Arxiv - DeepPaper",
            "url": "https://arxiv.deeppaper.ai/papers/2504.00891v2"
          },
          {
            "title": "GenPRM: Scaling Test-Time Compute of Process Reward ...",
            "url": "https://arxiv.org/pdf/2504.00891"
          },
          {
            "title": "Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis",
            "url": "https://arxiv.org/html/2604.24198v1"
          },
          {
            "title": "GenPRM/GenPRM-1.5B · Hugging Face",
            "url": "https://huggingface.co/GenPRM/GenPRM-1.5B"
          },
          {
            "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
            "url": "https://ryanliu112.github.io/GenPRM/"
          }
        ]
      },
      "I found relevant information about GenPRM. Here's what I found:\n\n## GenPRM Overview\n\nGenPRM has been accepted by AAAI 2026. The paper is titled \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\" and is available as arXiv preprint arXiv:2504.00891.\n\n## What is GenPRM?\n\nGenPRM is a generative process reward model that performs explicit Chain-of-Thought (CoT) reasoning with code verification before providing judgment for each reasoning step. \n\nGenPRM redefines process supervision as a generative task rather than a discriminative scoring task by integrating Chain-of-Thought reasoning and code verification processes before providing final judgment.\n\n## Key Methodology\n\nTo obtain high-quality process supervision labels and rationale data, the authors propose Relative Progress Estimation (RPE) and a rationale synthesis framework that incorporates code verification.\n\n## Performance\n\nExperimental results on ProcessBench and several mathematical reasoning tasks show that GenPRM significantly outperforms prior PRMs with only 23K training data from MATH.\n\nThe official codebase is available on GitHub, and various model versions are available on Hugging Face."
    ],
    "durationSeconds": 6.194261271999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "244ab647-b030-4615-b5b6-cb1fe71d6306",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-27T08:15:12.052Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture of the landscape. Let me synthesize my findings and evaluate this proposal.

Let me assess the key aspects:

## Summary of the Research Landscape

The proposal is about training Process Reward Models (PRMs) that are invariant to surface form but sensitive to logical structure, using premise dependency DAGs extracted via PARC/PERL as the scaffold for contrastive training.

### What's Known:
1. **PRMs are fragile**: "Reward Under Attack" (2026) and "Reward Models Identify Consistency, Not Causality" (2025) have clearly documented that PRMs function as fluency/consistency detectors rather than reasoning verifiers. 

43% of their failures come from stylistic shortcuts.

2. **Premise dependency DAGs are extractable**: PARC/PERL (ICML 2025) showed that LLMs can extract premise links at 90% recall, and that premise-aware verification improves error detection by 6-16%.

3. **Multiple PRM improvement approaches exist**: APRM uses adversarial training for +5.3pp OOD gains, CRM applies conditional reward modeling, CPMI leverages contrastive mutual information for auto-labeling, and PURE minimizes form variance.

4. **Other recent approaches**: GenPRM generates reasoning paths, PathFinder-PRM achieves SOTA 67.7 on PRMBench through error-aware hierarchical supervision, and CRA adjusts rewards causally.

5. **Contrastive and adversarial methods have limitations**: CPMI uses contrastive learning but ignores premise structure, while APRM generates harder negatives without considering the graph relationships.

The novelty here seems to hinge on combining premise DAGs with contrastive training in a structure-aware way—specifically constructing pairs that either preserve or break the graph structure. I haven't found another paper doing exactly this combination.

But stepping back, the logic feels more like a natural progression than a surprising discovery. PRMs get fooled by surface fluency, premise dependencies capture logical structure, contrastive training disentangles confounded signals—so using DAGs to build contrastive pairs that separate form from logic is the obvious next move. A researcher familiar with both the reward robustness literature and PARC/PERL would likely think this is the straightforward thing to try. The novelty is really in the execution rather than an unexpected insight.

Now I'm wondering whether the explicit DAG structure actually provides meaningful gains over simpler alternatives. APRM already gets +5.3pp OOD with adversarial training and harder negatives—would PGCT do significantly better? I could also just augment the training data with paraphrased correct solutions as additional positives, or use standard contrastive learning with step-level embeddings without the DAG machinery. The key question is whether the DAG complexity is justified by the results.

I'm also concerned about the 90% premise extraction recall—that's measured on Llama-3.1-8B-Instruct, but I need to verify it holds across the diverse reasoning chains in PRM800K and Math-Shepherd, especially across different math domains like algebra, geometry, and combinatorics.

There's a deeper issue too: the assumption that graph-breaking perturbations are learnable signals assumes the model can distinguish a "broken DAG" from an alternative valid reasoning path, but in math there are often multiple valid derivations, so a severed link might actually represent a legitimate alternative approach. And even if InfoNCE loss over DAG-anchored representations works in theory, standard transformers may not naturally encode DAG topology, so the model might not actually "see" the structure it's supposed to learn from.

The problem itself is clearly important and well-documented, so if this approach works it would be meaningful. But the improvement target is modest—aiming for >70 on PRMBench versus the current 67.7 SOTA is only a +2.3 point gain, which feels incremental. The real value would come from adversarial robustness, though that's harder to measure concretely.

The related work section is thorough and the positioning against concurrent approaches like CPMI, CRM, RewardFlow, and GoV is fair and well-articulated. But here's the thing: the core insight feels like a natural next step rather than something surprising—anyone familiar with the literature would likely think of using explicit premise dependency structure during PRM training.

There are also simpler alternatives worth considering, like adversarial training in the APRM style or basic paraphrase augmentation, that might capture most of the benefits without the added complexity. And there's a critical assumption underlying everything: the quality of DAG extraction, which doesn't get enough scrutiny in the proposal.

Weighing it all together, I'd say this is competently constructed with solid motivation and excellent literature coverage, but the novelty feels more like a predictable combination than a surprising insight. The significance is there—the problem matters—but the approach is incremental. I'm thinking this lands in the 25-35% acceptance range. It's well-executed engineering, but it doesn't quite demand attention on its own merits. Though if the experiments turn out to be exceptionally strong, that could shift things.

Actually, wait—let me reconsider the specific insight about using premise dependency DAGs as the structural foundation here.

The graph-preserving versus graph-breaking perturbations are actually quite thoughtful. They create a training signal that directly targets the documented failure mode of fluency-logic dissociation, which is more principled than just generating harder negatives the way APRM does. But I should still question whether the full DAG structure is truly necessary, or if simpler structural signals like step dependency counts would achieve similar results. The graph-contrastive training might be overengineered if a more minimal approach works just as well.

So I'm settling on: novelty is medium, leaning toward the higher end because the design is principled and the combination is novel, even if not surprising. Significance is also medium—the problem is clearly important, but the solution is incremental.

For AAAI specifically, this kind of well-executed combination paper might fare better than at ICML or NeurIPS, though I'm supposed to evaluate the idea itself rather than venue fit. My final assessment is around 25-35% acceptance probability, with the main concerns being that reviewers could see this as a natural combination lacking sufficient novelty, and that simpler baselines might achieve comparable results without the added complexity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10d6b843-aa3b-43db-b866-a2e3da970505",
  "isSidechain": false,
  "requestId": "req_011CbSjqk7Ps2Y7EJjuNURLF",
  "type": "assistant",
  "uuid": "4be7e959-debb-4bf9-9e11-0e0c4bc63844",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DENWZHmgCo1umn1MFptQND",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2909,
      "cache_read_input_tokens": 24818,
      "output_tokens": 6030,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6030,
          "cache_read_input_tokens": 24818,
          "cache_creation_input_tokens": 2909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2909
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

_source line 48 · 2026-05-27T08:16:35.873Z_

Now I have sufficient information to provide a thorough evaluation. Let me compile my findings.

---

```
【阶段】: Triage

【领域调研】:

1. "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models" (arXiv:2603.06621, Feb 2026):
   - 本 proposal 的核心动机来源。证实 PRMs 在对抗压力下系统性可被利用，43% 的 RL reward gain 归因于 stylistic shortcuts，策略在 AIME 上达到 >0.9 PRM reward 但 <4% 真实准确率。提出了 fluency-logic dissociation 现象。
   - 论文确实存在，描述准确。

2. "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025):
   - Xu et al. 证明 reward model 优先评估 structural consistency 而非 causal correctness——移除问题陈述对 reward 影响甚微，但改变数值或打断推理流程显著影响 RM 输出。
   - 论文确实存在，描述准确。

3. PARC/PERL (arXiv:2502.02362, ICML 2025):
   - 将线性推理链重构为 premise-augmented reasoning chains (DAG)，证明开源 LLM 在 premise identification 上达到 90% recall，基于 premise 的验证将错误识别准确率提升 6-16%。
   - 论文确实存在，描述准确。

4. APRM — Adversarial Training for Process Reward Models (arXiv:2511.22888, Nov 2025):
   - Generator-PRM 对抗博弈框架，通过渐进式更难 negatives 训练，平均 +3.4pp（OOD +5.3pp）。
   - **与本 proposal 直接竞争**：同样目标是提升 PRM 对 novel errors 的泛化，但不使用显式逻辑结构。

5. CRM — Conditional Reward Modeling (arXiv:2509.26578, ICLR 2026):
   - 将推理建模为 temporal process，reward 条件化于前序 steps 和最终结果，捕获 inter-step causal relationships。
   - 与本 proposal 关注 inter-step dependencies 有重叠，但不使用 premise DAG 也不使用 contrastive training。

6. CPMI — Contrastive Mutual Information for PRM (arXiv:2604.10660, April 2026):
   - 用 contrastive pointwise mutual information 进行自动 step-level reward labeling，相比 MC 估计减少 84% 标注时间。
   - 使用 contrastive 思想但用途不同（labeling vs. training），不涉及 premise graphs。

7. GenPRM (arXiv:2504.00891, AAAI 2026):
   - 将 process supervision 重新定义为生成式任务，结合 CoT reasoning 和 code verification。已被 AAAI 2026 接收。
   - 不同范式（generative vs. discriminative），与本 proposal 正交。

8. PathFinder-PRM (2025):
   - PRMBench 当前 SOTA 67.7（human ceiling 83.8），通过分层 error-aware supervision 实现。
   - 本 proposal 的 benchmark target 基准。

9. "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs" (arXiv:2601.17593, 2026):
   - 分析 LLM 内部表示中 DAG 结构的可恢复性，发现中间层达到峰值。
   - 为 DAG-based 方法提供了额外理论支撑，但 proposal 未引用此工作。

- **调研总结**: PRM 鲁棒性是 2025-2026 年的热点方向，已有多种攻击角度的改进方案（adversarial training、conditional modeling、contrastive labeling、generative verification），但尚无工作将 premise dependency DAGs 显式融入 PRM contrastive training。该领域竞争激烈，新方法需要在多个 benchmark 上展现显著优势才能脱颖而出。

【Trivial Alternative 检验】:

存在多个更简单的替代方案可能部分实现类似效果：

1. **APRM 式 adversarial training**：已证明通过对抗博弈生成 harder negatives 可以 OOD +5.3pp，无需 premise DAG extraction pipeline。PGCT 需要证明显式 DAG 结构比 APRM 的自动 hard negative mining 效果更好——但 APRM 的 negatives 是自适应生成的，而 PGCT 的 negatives 是基于规则构造的（premise-link corruption），后者可能不够 hard。

2. **Simple paraphrase augmentation**：仅使用 LLM paraphrase 生成同语义不同表述的 step 作为 additional training data（不需要 DAG），可能已经能提升部分 surface invariance，因为 PRM 会看到 "不同表述→同样 correct" 的信号。

3. **Random step shuffling/dropping**：不使用 premise DAG，而是简单地随机打乱步骤引用或 drop 某些步骤作为 negative pairs，可能捕获部分 logical dependency signal。

**增量价值论点**：PGCT 的增量价值在于——premise DAG 提供了精确的"该保留什么、该破坏什么"的信息，使得 graph-preserving perturbations 确保语义不变性，graph-breaking perturbations 精准打击逻辑依赖。但这个增量价值是否足以justify整个 DAG extraction + graph contrastive training pipeline 的复杂性，需要实验验证。这是一个 engineering bet，不是一个 conceptual breakthrough。

【前提假设检验】:

核心逻辑链中有几个未经验证的假设：

1. **DAG extraction 在 PRM800K/Math-Shepherd 上的可靠性（关键假设）**：PARC 的 90% recall 是在 PERL 的特定评估集上报告的（使用 Llama-3.1-8B-Instruct）。PRM800K 和 Math-Shepherd 包含来自不同模型的 ~300K solutions，步骤格式和推理风格高度多样。DAG extraction 在这些异质数据上的 recall 和 precision 未知。如果 extraction 质量下降（比如降到 70%），则 contrastive pairs 中将包含大量噪声，可能反而损害训练。

2. **Graph-breaking perturbations 的 validity（重要假设）**："severed premise link" 可能不一定是 invalid reasoning——在数学中，同一结论可以从不同 premise 推出。一个看似 "dangling reference" 的步骤可能实际上是隐式使用了另一组前提。因此，graph-breaking negatives 可能包含 false negatives（标为错误但实际正确的样本），这会严重污染 contrastive signal。

3. **InfoNCE 可以通过 DAG-anchored embeddings 学到 structure sensitivity（技术假设）**：标准 transformer 的 representation 已经编码了 positional/contextual 信息。额外的 InfoNCE loss 是否能教会 model 区分 "DAG 完整" vs "DAG 破损" 取决于 DAG-anchored embedding 的具体设计——但 proposal 对此缺乏技术细节（如何将 DAG topology 注入 embedding space？pooling over DAG subgraph？GNN layer？）。

4. **43% stylistic shortcuts 的可纠正性假设**：proposal 默认这 43% 可以通过 structure-aware contrastive training 纠正。但 "Reward Under Attack" 的分析是在 RL-trained policies 上做的；PGCT 改进的是 PRM training，不直接改变 RL policy 的行为。即使 PRM 变得更 robust，policy 可能找到新的 attack surface。

【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是将 premise dependency DAGs（PARC/PERL, ICML 2025）与 contrastive PRM training 结合。确认搜索后，确实没有已发表工作做了完全相同的组合。然而，这个组合是**高度 predictable 的"自然下一步"**：任何同时读了 "Reward Under Attack"（fluency-logic dissociation）和 PARC/PERL（premise DAGs extractable at 90% recall）的研究者都会想到"用 DAG 信息指导 training"。与 APRM（arXiv:2511.22888）相比，PGCT 用显式结构替换了自适应对抗训练，这是一个 design choice 而非 paradigm shift。与 CRM（ICLR 2026）的 inter-step dependency modeling 在动机上高度重叠，只是实现路径不同。Novelty 在于 engineering combination，不在于 conceptual surprise。

2. **Significance: 中** — 
   所瞄准的问题（PRM reward hacking）确实重要且被充分文档化——"Reward Under Attack" 和 "Reward Models Identify Consistency Not Causality" 都是高影响力工作。但 proposal 的目标改进幅度偏modest（PRMBench 67.7 → >70，仅 +2.3 points，vs. human ceiling 83.8）。更重要的是，领域内已有多个竞争方案（APRM +5.3pp OOD, CRM at ICLR 2026, GenPRM at AAAI 2026, PURE at NeurIPS 2025），PGCT 如果只是 "another approach with marginal gains"，影响力有限。如果核心发现是 positive（DAG-contrastive training 确实提升 robustness），审稿人更可能的反应是 "makes sense, good to see it confirmed" 而非 "surprising, changes how I think about the problem."

3. **Related Work: 强** — 
   proposal 展现了对领域的深入了解。14 篇引用中，经我验证的关键论文（Reward Under Attack, PARC/PERL, CRM, APRM, CPMI, GenPRM, PRMBench, PathFinder-PRM）均真实存在，描述准确。对 concurrent work 的区分定位（CPMI 不用 DAG, CRM 不用 contrastive, RewardFlow 是 agentic tasks, GoV 是 training-free）清晰且公允。coverage 几乎涵盖了领域内所有主要方向。唯一遗漏的是 "From Chains to DAGs"（arXiv:2601.17593）和一些 2026 年初的新工作（如 "Robust Reward Modeling via Causal Rubrics"），但这些不影响核心定位。

【概率估计】: [25% - 35%] 中位 30%

【估计理由】: 
Novelty 是中——组合虽新但 predictable，这限制了概率上界（审稿人容易写出"straightforward combination"的评价）。Significance 同样是中——问题重要但改进幅度 modest 且竞争激烈。Related Work 的强表现为 proposal 提供了 solid 的定位基础，但 related work 好只能保下限不能拉上限。整体这是一个 "well-motivated, well-positioned engineering contribution"，在 AAAI 级别的 idea 评估中落在 25-35% 区间。如果实验执行出色（DAG extraction 质量高、在 adversarial robustness 上大幅超越 APRM），有可能突破 35%。但 idea 本身不具备让审稿人说 "surprising" 的力度。Novelty 是主要瓶颈维度。

【主要风险】: 
1. **"Natural combination" 风险**：审稿人可能认为将 PARC/PERL 的 premise DAGs 用于 PRM contrastive training 是一个 obvious next step，novelty contribution 不足以支撑 top venue。APRM 和 CRM 已经以不同方式处理了 inter-step dependency 和 harder negatives 问题。
2. **Trivial alternative 威胁**：如果 simple paraphrase augmentation（不使用 DAG 的 surface perturbation）或 APRM 式 adversarial training 能达到 comparable 效果，则 PGCT 复杂的 DAG pipeline 的增量价值不明确——这是审稿人最可能的 "why not just..." 质疑。
```

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/abs/2502.14619)
- [PARC/PERL: Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs](https://arxiv.org/abs/2502.02362)
- [Adversarial Training for Process Reward Models (APRM)](https://arxiv.org/abs/2511.22888)
- [Linking Process to Outcome: Conditional Reward Modeling (CRM)](https://arxiv.org/abs/2509.26578)
- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891)
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [PathFinder-PRM on GitHub](https://github.com/declare-lab/PathFinder-PRM)
- [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs](https://arxiv.org/pdf/2601.17593)
- [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://arxiv.org/abs/2409.13156)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4be7e959-debb-4bf9-9e11-0e0c4bc63844",
  "isSidechain": false,
  "requestId": "req_011CbSjqk7Ps2Y7EJjuNURLF",
  "type": "assistant",
  "uuid": "353b7d55-aabe-442a-bcc0-7013695f2f59",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DENWZHmgCo1umn1MFptQND",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2909,
      "cache_read_input_tokens": 24818,
      "output_tokens": 6030,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2909,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6030,
          "cache_read_input_tokens": 24818,
          "cache_creation_input_tokens": 2909,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2909
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process re…",
  "leafUuid": "353b7d55-aabe-442a-bcc0-7013695f2f59",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process re…",
  "leafUuid": "353b7d55-aabe-442a-bcc0-7013695f2f59",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "68d7646a-bf03-45a6-a7a2-f1d82af85608"
}
```

---
