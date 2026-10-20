# Research conversation: Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models ## Core Problem Current process reward model

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/chats/exported-trajectories/account-2/21b9d1bb-97a5-4ae9-8693-da25a18e1ec9.jsonl`
- **Structured JSON:** [`2be4b23b05067f41f7f1.json`](../../sessions/2b/2be4b23b05067f41f7f1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T08:22:34.696Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T08:22:34.696Z",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "content": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models\n\n## Core Problem\n\nCurrent process reward models confuse surface fluency with logical validity — 43% of PRM reward gains are attributable to stylistic shortcuts rather than reasoning correctness — leading to catastrophic reward hacking during RL training where policies achieve >0.9 PRM scores but <4% actual accuracy. Can we train PRMs that are invariant to surface form but sensitive to logical structure?\n\n## Research Opportunity\n\nPERL (ICML 2025) demonstrated that LLMs can extract premise dependency links between reasoning steps at 90% recall, and that premise-aware verification improves error detection by 6-16%. However, this structural information has only been used at evaluation time, not for PRM training. Simultaneously, DAG-Math (2025) and ProofFlow (2025) have made dependency graph extraction from mathematical reasoning chains feasible. No prior work combines these premise dependency structures with contrastive PRM training to explicitly disentangle logical validity from surface fluency — addressing the documented root cause of PRM fragility at training time rather than through post-hoc corrections.\n\n## Research Landscape\n\nThe field has documented severe PRM robustness failures: 'Reward Under Attack' (arXiv:2603.06621, Feb 2026) showed PRMs function as fluency detectors with wide exploitable reward peaks, and 'Reward Models Identify Consistency, Not Causality' (arXiv:2502.14619, Feb 2025) confirmed this is fundamental. Existing defenses include CRA (Aug 2025, post-hoc sparse autoencoder correction), APRM (Nov 2025, adversarial training with harder negatives gaining +5.3pp OOD), CRM (ICLR 2026, sequential conditioning on preceding steps), and PURE (NeurIPS 2025, min-form credit aggregation). None uses explicit logical dependency structure during PRM training. On the infrastructure side, PARC/PERL (ICML 2025) showed premise links form DAGs with 90% extractable recall; GenPRM (AAAI 2026) provides code-verified step analysis; and AgentEval (arXiv:2604.23581, 2026) showed DAG-based dependency modeling yields +22pp failure detection recall over flat evaluation. The best PRMs on PRMBench score 67.7 (PathFinder-PRM-7B) vs. 83.8 human ceiling, leaving a 16-point gap where structural approaches could contribute. Concurrent work: CPMI (arXiv:2604.10660, April 2026) uses contrastive mutual information for PRM auto-labeling but does not employ premise dependency graphs; RewardFlow (arXiv:2603.18859, March 2026) propagates rewards over state-transition graphs in agentic tasks but uses no contrastive training and targets a different graph type; Graph of Verification (GoV) decomposes reasoning into DAGs for verification but is training-free. The specific combination of premise dependency DAGs with contrastive PRM training remains untried.\n\n## Proposed Approach\n\nExtract premise dependency DAGs from mathematical reasoning chains using PARC's proven extraction method (90% recall on Llama-3.1-8B-Instruct), then construct structure-aware contrastive training pairs: graph-preserving surface perturbations (rephrased steps maintaining identical DAG topology) as positives, and graph-breaking fluent perturbations (severed premise links, dangling references, logically invalid steps preserving surface fluency) as hard negatives. Train a Qwen2.5-Math-7B-Instruct-based PRM with a dual objective combining standard step-correctness classification and a graph-contrastive InfoNCE loss over DAG-anchored step embeddings, forcing the model to learn representations invariant to surface form but sensitive to logical dependency structure. Augment PRM800K and Math-Shepherd seed chains (~300K solutions) with DAG annotations and ~600K contrastive pairs generated via LLM paraphrasing and targeted premise-link corruption. Evaluate on PRMBench (targeting >70 vs. 67.7 SOTA), ProcessBench, and the adversarial robustness suite from 'Reward Under Attack,' measuring both step-level accuracy and reduction in stylistic shortcut exploitability.\n\n## Detailed Description\n\nWe propose Premise-Graph Contrastive Training (PGCT), a method that leverages explicit logical dependency structure to train process reward models resistant to surface-form reward hacking. Current PRMs conflate fluency with validity — 43% of reward gains stem from stylistic shortcuts, and PRMs detect consistency rather than causality. Our key insight is that premise dependency DAGs, extractable at 90% recall via PARC (ICML 2025), provide a structural scaffold for contrastive training that disentangles these confounds. We construct graph-preserving surface perturbations (varied phrasing, identical logic) and graph-breaking fluent perturbations (severed premise links, maintained fluency) as contrastive pairs, training with a dual objective combining step-correctness prediction and InfoNCE loss over DAG-anchored representations. Built on Qwen2.5-Math-7B-Instruct with PRM800K and Math-Shepherd data augmented by ~600K structure-aware contrastive pairs, PGCT targets >70 on PRMBench (vs. 67.7 SOTA, 83.8 human ceiling) and substantially reduced adversarial exploitability. No prior work combines premise dependency graphs with contrastive PRM training — concurrent approaches (CPMI, CRM, RewardFlow) address complementary aspects but omit explicit logical structure from the training signal.\n\n## Key References\n\n- Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models (arXiv 2026, arXiv:2603.06621)\n- Reward Models Identify Consistency, Not Causality (arXiv 2025, arXiv:2502.14619)\n- Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs — PARC/PERL (ICML 2025, arXiv:2502.02362)\n- DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs (arXiv 2025, arXiv:2510.19842)\n- ProofFlow: A Dependency Graph Approach to Faithful Proof Autoformalization (arXiv 2025, arXiv:2510.15981)\n- Causal Reward Adjustment: Mitigating Reward Hacking via Backdoor Correction — CRA (arXiv 2025, arXiv:2508.04216)\n- Adversarial Training for Process Reward Models — APRM (arXiv 2025, arXiv:2511.22888)\n- Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning — CRM (ICLR 2026, arXiv:2509.26578)\n- Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning — PURE (NeurIPS 2025, arXiv:2504.15275)\n- GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026, arXiv:2504.00891)\n- AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking (arXiv 2026, arXiv:2604.23581)\n- PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (ACL 2025, arXiv:2501.03124)\n- Efficient Process Reward Modeling via Contrastive Mutual Information — CPMI (arXiv 2026, arXiv:2604.10660)\n- RewardFlow: Topology-Aware Reward Propagation on State Graphs (arXiv 2026, arXiv:2603.18859)\n- PathFinder-PRM: Exploring Path Diversity in Step-Level Reward Models (arXiv 2025)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 700-1000 A100-hours (DAG extraction: ~80h, contrastive pair generation: ~120h, PRM training with ablations: ~400h, evaluation and baselines: ~100h), timeline: 14-18 weeks for 2-3 researchers, estimated_gpu_cost: $2,100-$3,000 at $3/hr A100 spot pricing\n- **human_in_loop**: gpu_hours: 500-700 A100-hours (Claude accelerates data pipeline debugging, contrastive pair quality filtering, and ablation design, reducing failed experiments ~30%), timeline: 10-14 weeks for 2 researchers, claude_api_cost: $400-$700 (data quality analysis, code generation, experiment triage), estimated_gpu_cost: $1,500-$2,100 at $3/hr A100 spot pricing\n- **auto_research**: gpu_hours: 800-1200 A100-hours (more parallel sweeps offset by automated experiment selection), timeline: 6-8 weeks with automated pipeline, claude_api_cost: $1,000-$1,500 (automated DAG quality validation, contrastive pair generation, hyperparameter sweep orchestration, paper drafting), estimated_gpu_cost: $2,400-$3,600 at $3/hr A100 spot pricing, speed_bottleneck: DAG extraction quality validation — premise link accuracy must be audited per-domain (algebra vs. geometry vs. combinatorics) before contrastive pairs are trustworthy; serial human spot-checks required\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T08:22:34.700Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T08:22:34.700Z",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

## Round 1

51 recorded events

### User

_source line 3 · 2026-05-27T08:22:34.721Z_

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
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "1e82f01f-99f7-4c49-a3ae-d685fc727cac",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T08:22:34.720Z_

```json
{
  "parentUuid": "1e82f01f-99f7-4c49-a3ae-d685fc727cac",
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
  "uuid": "e7ab1172-17dd-4d5f-b374-542f59229bf8",
  "timestamp": "2026-05-27T08:22:34.720Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T08:22:34.720Z_

```json
{
  "parentUuid": "e7ab1172-17dd-4d5f-b374-542f59229bf8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "13093743-8f7b-4ff1-933a-82c6e34dbdd4",
  "timestamp": "2026-05-27T08:22:34.720Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
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
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Assistant

_source line 7 · 2026-05-27T08:22:43.766Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "发掘 agent" (Discovery Agent) to analyze a research proposal about "Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models" (PGCT). 

Let me first read and understand the proposal thoroughly, then conduct web searches to do my due diligence on the related work landscape before giving any suggestions.

The proposal's core idea:
1. Current PRMs confuse surface fluency with logical validity (43% of reward gains from stylistic shortcuts)
2. PARC/PERL showed premise dependency links can be extracted at 90% recall


3. The key innovation is applying these extracted premise dependency graphs to contrastive training—creating positive examples through surface-level changes that preserve the logical structure, and negative examples through fluent perturbations that break the graph—then training the PRM with a combined objective that evaluates both step correctness and graph-anchored embedding similarity.

Now I'm searching the literature to map out what's already been explored in this space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13093743-8f7b-4ff1-933a-82c6e34dbdd4",
  "isSidechain": false,
  "requestId": "req_011CbSkUgRRGDxwWvVLZy4zC",
  "type": "assistant",
  "uuid": "c21ff37b-a806-4279-b1f8-e70bf4b263d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dLRQWo5u1UANxnDzrKCwk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6847,
      "cache_read_input_tokens": 11014,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 354,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6847
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

_source line 8 · 2026-05-27T08:22:44.015Z_

I'll start by conducting thorough literature research before making any judgments. Let me search for the most relevant recent work across several dimensions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c21ff37b-a806-4279-b1f8-e70bf4b263d4",
  "isSidechain": false,
  "requestId": "req_011CbSkUgRRGDxwWvVLZy4zC",
  "type": "assistant",
  "uuid": "142e3877-39d9-4b48-8512-fc5ad675916a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dLRQWo5u1UANxnDzrKCwk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6847,
      "cache_read_input_tokens": 11014,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 354,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6847
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

_source line 9 · 2026-05-27T08:22:44.047Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01V2KzisWS3gP4JmMWKTnVeC`</summary>

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
  "parentUuid": "142e3877-39d9-4b48-8512-fc5ad675916a",
  "isSidechain": false,
  "requestId": "req_011CbSkUgRRGDxwWvVLZy4zC",
  "type": "assistant",
  "uuid": "17389a18-f3f7-4631-a23d-290c6502f894",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019dLRQWo5u1UANxnDzrKCwk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 6847,
      "cache_read_input_tokens": 11014,
      "output_tokens": 354,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6847,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 354,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 6847,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6847
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

_source line 10 · 2026-05-27T08:22:44.056Z_

<details><summary>↩ Tool result · `toolu_01V2KzisWS3gP4JmMWKTnVeC`</summary>

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
  "parentUuid": "17389a18-f3f7-4631-a23d-290c6502f894",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "be8b628a-ee10-4f4f-8030-9d064732a554",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "17389a18-f3f7-4631-a23d-290c6502f894",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-27T08:22:47.373Z_

Now let me conduct my pre-research searches. I'll run multiple searches in parallel to cover different angles of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be8b628a-ee10-4f4f-8030-9d064732a554",
  "isSidechain": false,
  "requestId": "req_011CbSkVNYR6Urz3yx4DZCKC",
  "type": "assistant",
  "uuid": "6c6c4efa-a316-4acb-a79d-68b7231de705",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3Q8VwgRpmr3UixpdofZEi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 17861,
      "output_tokens": 97,
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
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 17861,
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

### Tool call

_source line 12 · 2026-05-27T08:22:47.549Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JihKJbC3eQUyMNBv4rPk5X`</summary>

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
  "parentUuid": "6c6c4efa-a316-4acb-a79d-68b7231de705",
  "isSidechain": false,
  "requestId": "req_011CbSkVNYR6Urz3yx4DZCKC",
  "type": "assistant",
  "uuid": "a1552ef7-91ca-4fca-851d-b270ecaee807",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3Q8VwgRpmr3UixpdofZEi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 17861,
      "output_tokens": 97,
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
          "input_tokens": 3,
          "output_tokens": 97,
          "cache_read_input_tokens": 17861,
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

_source line 13 · 2026-05-27T08:22:58.441Z_

<details><summary>↩ Tool result · `toolu_01JihKJbC3eQUyMNBv4rPk5X`</summary>

```text
Web search results for query: "process reward model robustness reward hacking contrastive training 2025 2026"

Links: [{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/pdf/2502.18770"},{"title":"Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis","url":"https://arxiv.org/html/2601.20103v1"},{"title":"Robust Reward Modeling via Causal Rubrics","url":"https://arxiv.org/pdf/2506.16507"},{"title":"[2409.13156] RRM: Robust Reward Model Training Mitigates Reward Hacking","url":"https://arxiv.org/abs/2409.13156"},{"title":"IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.19416"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/pdf/2602.10623"},{"title":"Adversarial Training of Reward Models","url":"https://arxiv.org/pdf/2504.06141"},{"title":"Circuit-Aware Reward Training: A Mechanistic Framework for Longtail Robustness in RLHF","url":"https://arxiv.org/pdf/2509.24713"},{"title":"RRM: Robust Reward Model Training Mitigates Reward Hacking | OpenReview","url":"https://openreview.net/forum?id=88AS5MQnmC"}]

Based on the web search results, here's what I found on process reward models, robustness, reward hacking, and contrastive training in 2025-2026:

## Key Research Areas

### Reward Hacking Challenges
Reward hacking is the tendency for policy models to exploit weaknesses in the reward model to maximize reward signals without achieving genuine alignment or improvement. Reward models often learn to assign high scores based on superficial or spurious attributes—such as response length, specific formatting patterns, or stylistic quirks.

### Contrastive and Detection-Based Approaches
TRACE proposes a contrastive evaluation setup for reward hack detection, drawing inspiration from popular RL techniques such as GRPO, which can be extended to a training framework for robust detectors. Additionally, most prior work treats reward hacking as a blackbox constraint optimization phenomenon, with common strategies including adding regularization or constraints during optimization, or improving the reward model via scaling, calibration, or auxiliary supervision.

### Robust Reward Modeling Approaches
Recent 2025-2026 papers address robustness through multiple angles:
- Work on causally robust reward modeling (Crome) addresses the challenge of reward hacking in the context of aligning Large Language Models via Reinforcement Learning from Human Feedback
- Bayesian Non-negative Reward Modeling substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions
- Adversarial training results in reward models that are more robust to hacking and have better downstream performance in RLHF
- Circuit-Aware Reward Training (CART) uses circuit analysis to guide data augmentation, regularization, and ensemble strategies, providing practical interventions for improving longtail robustness


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1552ef7-91ca-4fca-851d-b270ecaee807",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "f33e8d58-548d-41a7-a1dd-e81e8cafc49a",
  "toolUseResult": {
    "query": "process reward model robustness reward hacking contrastive training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_018X5Q6LHZrJoWZkveB6AHgg",
        "content": [
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/pdf/2502.18770"
          },
          {
            "title": "Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis",
            "url": "https://arxiv.org/html/2601.20103v1"
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
          }
        ]
      },
      "Based on the web search results, here's what I found on process reward models, robustness, reward hacking, and contrastive training in 2025-2026:\n\n## Key Research Areas\n\n### Reward Hacking Challenges\nReward hacking is the tendency for policy models to exploit weaknesses in the reward model to maximize reward signals without achieving genuine alignment or improvement. Reward models often learn to assign high scores based on superficial or spurious attributes—such as response length, specific formatting patterns, or stylistic quirks.\n\n### Contrastive and Detection-Based Approaches\nTRACE proposes a contrastive evaluation setup for reward hack detection, drawing inspiration from popular RL techniques such as GRPO, which can be extended to a training framework for robust detectors. Additionally, most prior work treats reward hacking as a blackbox constraint optimization phenomenon, with common strategies including adding regularization or constraints during optimization, or improving the reward model via scaling, calibration, or auxiliary supervision.\n\n### Robust Reward Modeling Approaches\nRecent 2025-2026 papers address robustness through multiple angles:\n- Work on causally robust reward modeling (Crome) addresses the challenge of reward hacking in the context of aligning Large Language Models via Reinforcement Learning from Human Feedback\n- Bayesian Non-negative Reward Modeling substantially mitigates reward over-optimization, improves robustness under distribution shifts, and yields more interpretable reward decompositions\n- Adversarial training results in reward models that are more robust to hacking and have better downstream performance in RLHF\n- Circuit-Aware Reward Training (CART) uses circuit analysis to guide data augmentation, regularization, and ensemble strategies, providing practical interventions for improving longtail robustness"
    ],
    "durationSeconds": 10.884683949,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a1552ef7-91ca-4fca-851d-b270ecaee807",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains ar…",
  "leafUuid": "f33e8d58-548d-41a7-a1dd-e81e8cafc49a",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Tool call

_source line 16 · 2026-05-27T08:23:00.835Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WNBaNUSmG9SoBCDLnG2bDp`</summary>

```json
{
  "query": "PARC PERL premise dependency DAG reasoning chains verification ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f33e8d58-548d-41a7-a1dd-e81e8cafc49a",
  "isSidechain": false,
  "requestId": "req_011CbSkWRczThoqNmZ7qEnaW",
  "type": "assistant",
  "uuid": "f1aea258-a8bc-4290-a782-91263092186e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaNA2FbTx3XmqvwzmbpYPN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 944,
      "cache_read_input_tokens": 18742,
      "output_tokens": 69,
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
          "output_tokens": 69,
          "cache_read_input_tokens": 18742,
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

### Tool result

_source line 17 · 2026-05-27T08:23:07.291Z_

<details><summary>↩ Tool result · `toolu_01WNBaNUSmG9SoBCDLnG2bDp`</summary>

```text
Web search results for query: "PARC PERL premise dependency DAG reasoning chains verification ICML 2025"

Links: [{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs","url":"https://arxiv.org/pdf/2502.02362"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs","url":"https://abhinavchinta.com/parc/"},{"title":"ICML Poster Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs","url":"https://icml.cc/virtual/2025/poster/46462"},{"title":"Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs","url":"https://arxiv.org/html/2502.02362"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"}]

Based on the search results, here's what I found:

PARC (Premise-Augmented Reasoning Chains) restructures conventional linear reasoning chains by introducing premise links, resulting in a directed acyclic graph where the nodes are the steps and the edges are the premise links.

PERL (Premises and ERrors identification in LLMs) is a PARC-based dataset through which researchers demonstrated that LLMs can reliably identify premises within complex reasoning chains. Even open-source LLMs achieve 90% recall in premise identification.

**Key findings on verification:**

PARC helps identify errors in reasoning chains more reliably, with error identification accuracy improving by 6% to 16% absolute when step-by-step verification is carried out in PARC under the premises.

Steps that are locally correct but depend on erroneous prior steps (premises) are flagged as accumulation errors, using Depth-First Search (DFS) on the PARC structure to systematically identify these dependencies.

This research appears to have been presented at ICML 2025, focusing on improving error identification in mathematical reasoning by making explicit the dependency relationships between reasoning steps.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1aea258-a8bc-4290-a782-91263092186e",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "a6b1d9af-8016-4233-b4d2-f0999267323e",
  "toolUseResult": {
    "query": "PARC PERL premise dependency DAG reasoning chains verification ICML 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M2WLNufNnxucZ8GZ2oygZh",
        "content": [
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs",
            "url": "https://arxiv.org/pdf/2502.02362"
          },
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs",
            "url": "https://abhinavchinta.com/parc/"
          },
          {
            "title": "ICML Poster Premise-Augmented Reasoning Chains Improve Error Identification in Math reasoning with LLMs",
            "url": "https://icml.cc/virtual/2025/poster/46462"
          },
          {
            "title": "Premise-Augmented Reasoning Chains Improve Error Identification in Math Reasoning with LLMs",
            "url": "https://arxiv.org/html/2502.02362"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2601.17593"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nPARC (Premise-Augmented Reasoning Chains) restructures conventional linear reasoning chains by introducing premise links, resulting in a directed acyclic graph where the nodes are the steps and the edges are the premise links.\n\nPERL (Premises and ERrors identification in LLMs) is a PARC-based dataset through which researchers demonstrated that LLMs can reliably identify premises within complex reasoning chains. Even open-source LLMs achieve 90% recall in premise identification.\n\n**Key findings on verification:**\n\nPARC helps identify errors in reasoning chains more reliably, with error identification accuracy improving by 6% to 16% absolute when step-by-step verification is carried out in PARC under the premises.\n\nSteps that are locally correct but depend on erroneous prior steps (premises) are flagged as accumulation errors, using Depth-First Search (DFS) on the PARC structure to systematically identify these dependencies.\n\nThis research appears to have been presented at ICML 2025, focusing on improving error identification in mathematical reasoning by making explicit the dependency relationships between reasoning steps."
    ],
    "durationSeconds": 6.451862451000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f1aea258-a8bc-4290-a782-91263092186e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T08:23:09.788Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LPccuXTtR1XdnWNoBhpZWz`</summary>

```json
{
  "query": "\"reward under attack\" process reward model fluency detector exploitability arXiv 2603.06621"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a6b1d9af-8016-4233-b4d2-f0999267323e",
  "isSidechain": false,
  "requestId": "req_011CbSkX5Rq97XJr7j2EPzRS",
  "type": "assistant",
  "uuid": "85141113-f08a-4f56-8f56-6fd3c1734567",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9y7oNL4kkMRm7NTEhVuhh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 607,
      "cache_read_input_tokens": 19686,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 19686,
          "cache_creation_input_tokens": 607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 607
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

_source line 19 · 2026-05-27T08:23:17.601Z_

<details><summary>↩ Tool result · `toolu_01LPccuXTtR1XdnWNoBhpZWz`</summary>

```text
Web search results for query: ""reward under attack" process reward model fluency detector exploitability arXiv 2603.06621"

Links: [{"title":"[2603.06621] Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models","url":"https://arxiv.org/abs/2603.06621"},{"title":"Reward Under Attack: Analyzing the Robustness and Hackability of","url":"https://arxiv.org/pdf/2603.06621"},{"title":"1 Introduction","url":"https://arxiv.org/html/2603.06621"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=reward+hacking"},{"title":"Beyond Semantic Manipulation: Token-Space Attacks on Reward Models","url":"https://arxiv.org/pdf/2604.02686"},{"title":"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals","url":"https://arxiv.org/pdf/2604.01476"},{"title":"Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study","url":"https://arxiv.org/html/2507.05619v1"},{"title":"Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking","url":"https://arxiv.org/pdf/2602.01750"}]

I found the paper for you! Here's what the research is about:

**Paper Title:** Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models

**Key Findings:**

Process Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.

The research introduces a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify these vulnerabilities. The framework includes:

1. **Static Perturbation Analysis:** High invariance to surface-level style changes reward changes <0.1, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.

2. **Adversarial Optimization:** Gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks.

3. **RL-Induced Reward Hacking:** Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.

**Main Conclusion:** Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.

The paper was published on February 20, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "85141113-f08a-4f56-8f56-6fd3c1734567",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "a4b1aaed-d352-4946-bcfb-c988e8572e01",
  "toolUseResult": {
    "query": "\"reward under attack\" process reward model fluency detector exploitability arXiv 2603.06621",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X3v13R6mix5bYBrrRHU5Sq",
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
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=reward+hacking"
          },
          {
            "title": "Beyond Semantic Manipulation: Token-Space Attacks on Reward Models",
            "url": "https://arxiv.org/pdf/2604.02686"
          },
          {
            "title": "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals",
            "url": "https://arxiv.org/pdf/2604.01476"
          },
          {
            "title": "Detecting and Mitigating Reward Hacking in Reinforcement Learning Systems: A Comprehensive Empirical Study",
            "url": "https://arxiv.org/html/2507.05619v1"
          },
          {
            "title": "Adversarial Reward Auditing for Active Detection and Mitigation of Reward Hacking",
            "url": "https://arxiv.org/pdf/2602.01750"
          }
        ]
      },
      "I found the paper for you! Here's what the research is about:\n\n**Paper Title:** Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\n\n**Key Findings:**\n\nProcess Reward Models (PRMs) are rapidly becoming the backbone of LLM reasoning pipelines, yet state-of-the-art PRMs are systematically exploitable under adversarial optimization pressure.\n\nThe research introduces a three-tiered diagnostic framework that applies increasing adversarial pressure to quantify these vulnerabilities. The framework includes:\n\n1. **Static Perturbation Analysis:** High invariance to surface-level style changes reward changes <0.1, yet inconsistent detection of logically-corrupted reasoning, with different models failing on different attack types.\n\n2. **Adversarial Optimization:** Gradient-based attacks inflate rewards on invalid trajectories, with reward landscapes exhibiting wide, exploitable peaks.\n\n3. **RL-Induced Reward Hacking:** Policies trained on AIME problems achieve near-perfect PRM rewards (>0.9), while ground-truth accuracy remains low (below 4%), with 43% of reward gains attributable to stylistic shortcuts.\n\n**Main Conclusion:** Current PRMs function as fluency detectors rather than reasoning verifiers, creating systematic blind spots that undermine their use as training signals.\n\nThe paper was published on February 20, 2026."
    ],
    "durationSeconds": 7.8090620920000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "85141113-f08a-4f56-8f56-6fd3c1734567",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-27T08:23:20.233Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HvNevZ2HPyZbcFECieGkcw`</summary>

```json
{
  "query": "CPMI contrastive mutual information process reward model auto-labeling arXiv 2604.10660 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4b1aaed-d352-4946-bcfb-c988e8572e01",
  "isSidechain": false,
  "requestId": "req_011CbSkXqaB7n4MSLCJbvDej",
  "type": "assistant",
  "uuid": "c33ca947-4cb0-4791-a2a4-494e8450c86a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L8bUW7oRfUvyndrQp9Ymqj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 20293,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 20293,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 21 · 2026-05-27T08:23:27.075Z_

<details><summary>↩ Tool result · `toolu_01HvNevZ2HPyZbcFECieGkcw`</summary>

```text
Web search results for query: "CPMI contrastive mutual information process reward model auto-labeling arXiv 2604.10660 2026"

Links: [{"title":"[2604.10660] Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/abs/2604.10660"},{"title":"Efficient Process Reward Modeling via Contrastive Mutual Information","url":"https://arxiv.org/html/2604.10660"},{"title":"Towards Robust Process Reward Modeling via Noise-aware Learning","url":"https://arxiv.org/pdf/2601.12748"},{"title":"Self-Supervised Contrastive Learning of Protein Representations By Mutual Information Maximization","url":"https://www.biorxiv.org/content/10.1101/2020.09.04.283929.full.pdf"},{"title":"On Mutual Information in Contrastive Learning for Visual Representations","url":"https://arxiv.org/pdf/2005.13149"},{"title":"Free Process Rewards without Process Labels","url":"https://arxiv.org/pdf/2412.01981"}]

Based on the search results, I found the paper you're looking for:

The paper addresses verifying intermediate reasoning steps of chain-of-thought (CoT) trajectories using process reward models (PRMs). 

The authors propose contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing the computational burden of annotating dataset. CPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.

The experimental results show that CPMI-based labeling reduces dataset construction time by 84% and token generation by 98% compared to MC estimation, while achieving higher accuracy on process-level evaluations and mathematical reasoning benchmarks.

The paper is titled "Efficient Process Reward Modeling via Contrastive Mutual Information" and was submitted on April 12, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c33ca947-4cb0-4791-a2a4-494e8450c86a",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "888d0685-2387-451e-86d0-3d9875c2a21d",
  "toolUseResult": {
    "query": "CPMI contrastive mutual information process reward model auto-labeling arXiv 2604.10660 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012wkFjWTbjw2UYWHw9ivJJR",
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
            "title": "On Mutual Information in Contrastive Learning for Visual Representations",
            "url": "https://arxiv.org/pdf/2005.13149"
          },
          {
            "title": "Free Process Rewards without Process Labels",
            "url": "https://arxiv.org/pdf/2412.01981"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper addresses verifying intermediate reasoning steps of chain-of-thought (CoT) trajectories using process reward models (PRMs). \n\nThe authors propose contrastive pointwise mutual information (CPMI), a novel automatic reward labeling method that leverages the model's internal probability to infer step-level supervision while significantly reducing the computational burden of annotating dataset. CPMI quantifies how much a reasoning step increases the mutual information between the step and the correct target answer relative to hard-negative alternatives.\n\nThe experimental results show that CPMI-based labeling reduces dataset construction time by 84% and token generation by 98% compared to MC estimation, while achieving higher accuracy on process-level evaluations and mathematical reasoning benchmarks.\n\nThe paper is titled \"Efficient Process Reward Modeling via Contrastive Mutual Information\" and was submitted on April 12, 2026."
    ],
    "durationSeconds": 6.834997114999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c33ca947-4cb0-4791-a2a4-494e8450c86a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T08:23:29.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LuzQ84YnTbaRrNRtBqUWmK`</summary>

```json
{
  "query": "graph structure reasoning verification DAG-based reward model training logical dependency 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "888d0685-2387-451e-86d0-3d9875c2a21d",
  "isSidechain": false,
  "requestId": "req_011CbSkYY4zSzdbuapyQtXjd",
  "type": "assistant",
  "uuid": "40958b05-76a2-43eb-bb9e-49a13f28bf02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011SHbZY9NNFFEXL7tzBKXEX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 595,
      "cache_read_input_tokens": 21062,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 595,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 21062,
          "cache_creation_input_tokens": 595,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 595
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

_source line 23 · 2026-05-27T08:23:40.519Z_

<details><summary>↩ Tool result · `toolu_01LuzQ84YnTbaRrNRtBqUWmK`</summary>

```text
Web search results for query: "graph structure reasoning verification DAG-based reward model training logical dependency 2025 2026"

Links: [{"title":"Graph of Verification: Structured Verification of LLM Reasoning","url":"https://arxiv.org/pdf/2506.12509"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries","url":"https://arxiv.org/pdf/2603.29500"},{"title":"Graph Reasoning Paradigm: Structured and Symbolic Reasoning with Topology-Aware Reinforcement Learning for Large Language Models","url":"https://arxiv.org/pdf/2601.12995"},{"title":"GraphReason: Enhancing Reasoning Capabilities of Large Language Models   through A Graph-Based Verification Approach","url":"https://arxiv.org/pdf/2308.09267"},{"title":"Verifying Chain-of-Thought Reasoning via Its Computational Graph","url":"https://arxiv.org/pdf/2510.09312"},{"title":"DAG-Math: Graph-Guided Mathematical Reasoning in LLMs","url":"https://arxiv.org/html/2510.19842v1"}]

Here are the search results for your query about graph structure reasoning verification, DAG-based reward model training, and logical dependencies from 2025-2026:

## Key Recent Research

**Graph-Based Verification Approaches:**

Graph structures can be formally modeled as DAGs (Directed Acyclic Graphs) that serve as the backbone for systematic verification. A topological sort enforces causal consistency, ensuring premises are verified before conclusions, followed by sequential verification that assesses each unit based on previously validated antecedents, terminating at the first detected error for precise fault localization.

**DAG Structure in LLM Reasoning:**

DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers and enabling nontrivial recovery of dependency graphs. LLM reasoning exhibits measurable internal graph structure rather than being purely sequential.

**Reward Model Training with Formal Verification:**

Only fully validated reasoning chains receive high rewards, and the integration of formal verification guides models towards generating step-by-step machine-checkable proofs.

**Graph Reasoning with Topology-Aware RL:**

Recent work designs process-aware verification through graph-structured outcome rewards and mitigates reward hacking via stratified clipping advantage estimation.

**DAG-Math Framework:**

Recent research formalizes Chain-of-Thought as a rule-based stochastic process on directed acyclic graphs.

These papers represent cutting-edge work in integrating graph structures, logical dependencies, and reward-based training for LLM reasoning verification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "40958b05-76a2-43eb-bb9e-49a13f28bf02",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "cd63d511-e100-4155-9fc6-3e0518529b81",
  "toolUseResult": {
    "query": "graph structure reasoning verification DAG-based reward model training logical dependency 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LBcEmCR6sfkpYvzoYPZ6Pj",
        "content": [
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning",
            "url": "https://arxiv.org/pdf/2506.12509"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2601.17593"
          },
          {
            "title": "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries",
            "url": "https://arxiv.org/pdf/2603.29500"
          },
          {
            "title": "Graph Reasoning Paradigm: Structured and Symbolic Reasoning with Topology-Aware Reinforcement Learning for Large Language Models",
            "url": "https://arxiv.org/pdf/2601.12995"
          },
          {
            "title": "GraphReason: Enhancing Reasoning Capabilities of Large Language Models   through A Graph-Based Verification Approach",
            "url": "https://arxiv.org/pdf/2308.09267"
          },
          {
            "title": "Verifying Chain-of-Thought Reasoning via Its Computational Graph",
            "url": "https://arxiv.org/pdf/2510.09312"
          },
          {
            "title": "DAG-Math: Graph-Guided Mathematical Reasoning in LLMs",
            "url": "https://arxiv.org/html/2510.19842v1"
          }
        ]
      },
      "Here are the search results for your query about graph structure reasoning verification, DAG-based reward model training, and logical dependencies from 2025-2026:\n\n## Key Recent Research\n\n**Graph-Based Verification Approaches:**\n\nGraph structures can be formally modeled as DAGs (Directed Acyclic Graphs) that serve as the backbone for systematic verification. A topological sort enforces causal consistency, ensuring premises are verified before conclusions, followed by sequential verification that assesses each unit based on previously validated antecedents, terminating at the first detected error for precise fault localization.\n\n**DAG Structure in LLM Reasoning:**\n\nDAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers and enabling nontrivial recovery of dependency graphs. LLM reasoning exhibits measurable internal graph structure rather than being purely sequential.\n\n**Reward Model Training with Formal Verification:**\n\nOnly fully validated reasoning chains receive high rewards, and the integration of formal verification guides models towards generating step-by-step machine-checkable proofs.\n\n**Graph Reasoning with Topology-Aware RL:**\n\nRecent work designs process-aware verification through graph-structured outcome rewards and mitigates reward hacking via stratified clipping advantage estimation.\n\n**DAG-Math Framework:**\n\nRecent research formalizes Chain-of-Thought as a rule-based stochastic process on directed acyclic graphs.\n\nThese papers represent cutting-edge work in integrating graph structures, logical dependencies, and reward-based training for LLM reasoning verification."
    ],
    "durationSeconds": 10.603424467999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "40958b05-76a2-43eb-bb9e-49a13f28bf02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-27T08:23:43.899Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RSCPpw1JXUGeUibJ4mvNBA`</summary>

```json
{
  "query": "contrastive learning disentangle surface form logical structure NLP reasoning invariance 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd63d511-e100-4155-9fc6-3e0518529b81",
  "isSidechain": false,
  "requestId": "req_011CbSkZXZ1p3oScNmstDmac",
  "type": "assistant",
  "uuid": "9e55c981-e7be-47a4-ac48-b8415e0fd4e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G6sRNDYnbZY1LVZv7u4W3k",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 21657,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 21657,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 25 · 2026-05-27T08:23:51.897Z_

<details><summary>↩ Tool result · `toolu_01RSCPpw1JXUGeUibJ4mvNBA`</summary>

```text
Web search results for query: "contrastive learning disentangle surface form logical structure NLP reasoning invariance 2025 2026"

Links: [{"title":"Disentangled Contrastive Learning for Learning Robust Textual   Representations","url":"https://arxiv.org/pdf/2104.04907"},{"title":"Neuro-Symbolic Contrastive Learning for Cross-domain Inference","url":"https://arxiv.org/pdf/2502.09213"},{"title":"MERIt: Meta-Path Guided Contrastive Learning for Logical Reasoning","url":"https://arxiv.org/pdf/2203.00357"},{"title":"Towards a Unified Framework of Contrastive Learning for Disentangled Representations | OpenReview","url":"https://openreview.net/forum?id=QrB38MAAEP"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/c4a581f8219f62e3e5c83d4d80be5c9d-Paper-Conference.pdf"},{"title":"GitHub - ryanzhumich/Contrastive-Learning-NLP-Papers: Paper List for Contrastive Learning for Natural Language Processing · GitHub","url":"https://github.com/ryanzhumich/Contrastive-Learning-NLP-Papers"},{"title":"Contrastive Self-Supervised Learning for Commonsense Reasoning","url":"https://arxiv.org/pdf/2005.00669"}]

I've performed the web search for your query on contrastive learning, disentanglement, surface form, logical structure, NLP reasoning, and invariance for 2025-2026. Here are the relevant findings:

## Key Results

The search returned several relevant papers on this topic:

1. **Neuro-Symbolic Contrastive Learning (2025)**: A recent approach shows that the embedding space can capture highly varied textual information with similar semantic logical relations, while also separating similar textual relations that have dissimilar logical relations. This work uses contrastive pairs to carve the sharp underlying logical structure into neural networks, enabling logical generalisation and logical reasoning.

2. **Disentangled Contrastive Learning**: Research proposes a disentangled contrastive learning method that separately optimizes the uniformity and alignment of representations without negative sampling. Experimental results for NLP benchmarks demonstrate that such approaches can achieve promising improvements with invariance tests and adversarial attacks.

3. **Meta-Path Guided Contrastive Learning**: Logical reasoning requires correctly inferring semantic relations among sentences and extracting logical structures residing in options and context to justify reasonableness.

4. **General Contrastive Learning Principles**: Contrastive learning is a technique to learn an embedding space such that similar data sample pairs have close representations while dissimilar samples stay far apart from each other.

The search results show active research in combining contrastive learning with logical reasoning and disentangled representations in NLP, with emphasis on invariance and the separation of surface form from underlying logical structure.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e55c981-e7be-47a4-ac48-b8415e0fd4e1",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "8534de2d-7643-4102-a755-732acfcf3edd",
  "toolUseResult": {
    "query": "contrastive learning disentangle surface form logical structure NLP reasoning invariance 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XBoefxzkeSCNu2zXBxDsF3",
        "content": [
          {
            "title": "Disentangled Contrastive Learning for Learning Robust Textual   Representations",
            "url": "https://arxiv.org/pdf/2104.04907"
          },
          {
            "title": "Neuro-Symbolic Contrastive Learning for Cross-domain Inference",
            "url": "https://arxiv.org/pdf/2502.09213"
          },
          {
            "title": "MERIt: Meta-Path Guided Contrastive Learning for Logical Reasoning",
            "url": "https://arxiv.org/pdf/2203.00357"
          },
          {
            "title": "Towards a Unified Framework of Contrastive Learning for Disentangled Representations | OpenReview",
            "url": "https://openreview.net/forum?id=QrB38MAAEP"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/c4a581f8219f62e3e5c83d4d80be5c9d-Paper-Conference.pdf"
          },
          {
            "title": "GitHub - ryanzhumich/Contrastive-Learning-NLP-Papers: Paper List for Contrastive Learning for Natural Language Processing · GitHub",
            "url": "https://github.com/ryanzhumich/Contrastive-Learning-NLP-Papers"
          },
          {
            "title": "Contrastive Self-Supervised Learning for Commonsense Reasoning",
            "url": "https://arxiv.org/pdf/2005.00669"
          }
        ]
      },
      "I've performed the web search for your query on contrastive learning, disentanglement, surface form, logical structure, NLP reasoning, and invariance for 2025-2026. Here are the relevant findings:\n\n## Key Results\n\nThe search returned several relevant papers on this topic:\n\n1. **Neuro-Symbolic Contrastive Learning (2025)**: A recent approach shows that the embedding space can capture highly varied textual information with similar semantic logical relations, while also separating similar textual relations that have dissimilar logical relations. This work uses contrastive pairs to carve the sharp underlying logical structure into neural networks, enabling logical generalisation and logical reasoning.\n\n2. **Disentangled Contrastive Learning**: Research proposes a disentangled contrastive learning method that separately optimizes the uniformity and alignment of representations without negative sampling. Experimental results for NLP benchmarks demonstrate that such approaches can achieve promising improvements with invariance tests and adversarial attacks.\n\n3. **Meta-Path Guided Contrastive Learning**: Logical reasoning requires correctly inferring semantic relations among sentences and extracting logical structures residing in options and context to justify reasonableness.\n\n4. **General Contrastive Learning Principles**: Contrastive learning is a technique to learn an embedding space such that similar data sample pairs have close representations while dissimilar samples stay far apart from each other.\n\nThe search results show active research in combining contrastive learning with logical reasoning and disentangled representations in NLP, with emphasis on invariance and the separation of surface form from underlying logical structure."
    ],
    "durationSeconds": 7.993101819999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9e55c981-e7be-47a4-ac48-b8415e0fd4e1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
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
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains ar…",
  "leafUuid": "8534de2d-7643-4102-a755-732acfcf3edd",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Tool call

_source line 28 · 2026-05-27T08:23:54.717Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KRb3kXpv9tnRzapUwETMvv`</summary>

```json
{
  "query": "PRMBench process reward model benchmark SOTA 2026 PathFinder-PRM score leaderboard"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8534de2d-7643-4102-a755-732acfcf3edd",
  "isSidechain": false,
  "requestId": "req_011CbSkaN8G32uv86c5RjC4f",
  "type": "assistant",
  "uuid": "887556a2-8fd0-4ac0-9bd4-668411ddd78e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YXKoTJTY7CiZLrQ8ymj3XS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 828,
      "cache_read_input_tokens": 22426,
      "output_tokens": 75,
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
          "output_tokens": 75,
          "cache_read_input_tokens": 22426,
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

_source line 29 · 2026-05-27T08:24:01.770Z_

<details><summary>↩ Tool result · `toolu_01KRb3kXpv9tnRzapUwETMvv`</summary>

```text
Web search results for query: "PRMBench process reward model benchmark SOTA 2026 PathFinder-PRM score leaderboard"

Links: [{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF","url":"https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"},{"title":"Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision","url":"https://arxiv.org/pdf/2505.19706"},{"title":"PRMBench: Benchmark for Process-level Math Reasoning","url":"https://www.emergentmind.com/topics/prmbench"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://prmbench.github.io/"},{"title":"[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/abs/2501.03124"},{"title":"GitHub - ssmisya/PRMBench: [ACL' 25] The official code repository for PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models.","url":"https://github.com/ssmisya/PRMBench"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models","url":"https://arxiv.org/pdf/2501.03124"},{"title":"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1230/"}]

Based on the search results, here's what I found about PRMBench, PathFinder-PRM, and the SOTA scores:

## PRMBench Overview

PRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of PRMs, comprising 6,216 carefully designed problems and 83,456 step-level labels.

## PathFinder-PRM SOTA Score

PathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7 on PRMBench, outperforming the prior best (65.5) while using 3× less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.

## Model Performance Context

PathFinder-PRM is an error-aware hierarchical PRM that classifies each step to detect the presence of math or consistency errors, and combines these fine-grained error labels to produce a final reward score. PathFinder-PRM establishes the new state of the art among PRMs trained on PRM800K-only data and continues to scale gracefully when incorporating additional automated annotations.

The official PRMBench leaderboard is available at prmbench.github.io, where you can find the most current results and detailed performance breakdowns across different evaluation categories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "887556a2-8fd0-4ac0-9bd4-668411ddd78e",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "3e2817c6-7cda-42d2-a54c-b263827cd974",
  "toolUseResult": {
    "query": "PRMBench process reward model benchmark SOTA 2026 PathFinder-PRM score leaderboard",
    "results": [
      {
        "tool_use_id": "srvtoolu_018qvmecVbQxT7Gtt6HUDPL6",
        "content": [
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models | Request PDF",
            "url": "https://www.researchgate.net/publication/394270805_PRMBench_A_Fine-grained_and_Challenging_Benchmark_for_Process-Level_Reward_Models"
          },
          {
            "title": "Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision",
            "url": "https://arxiv.org/pdf/2505.19706"
          },
          {
            "title": "PRMBench: Benchmark for Process-level Math Reasoning",
            "url": "https://www.emergentmind.com/topics/prmbench"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://prmbench.github.io/"
          },
          {
            "title": "[2501.03124] PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/abs/2501.03124"
          },
          {
            "title": "GitHub - ssmisya/PRMBench: [ACL' 25] The official code repository for PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models.",
            "url": "https://github.com/ssmisya/PRMBench"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
            "url": "https://arxiv.org/pdf/2501.03124"
          },
          {
            "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.1230/"
          }
        ]
      },
      "Based on the search results, here's what I found about PRMBench, PathFinder-PRM, and the SOTA scores:\n\n## PRMBench Overview\n\nPRMBench is a process-level benchmark specifically designed to assess the fine-grained error detection capabilities of PRMs, comprising 6,216 carefully designed problems and 83,456 step-level labels.\n\n## PathFinder-PRM SOTA Score\n\nPathFinder-PRM achieves a new state-of-the-art PRMScore of 67.7 on PRMBench, outperforming the prior best (65.5) while using 3× less data. When applied to reward guided greedy search, the model yields prm@8 48.3, a +1.5 point gain over the strongest baseline.\n\n## Model Performance Context\n\nPathFinder-PRM is an error-aware hierarchical PRM that classifies each step to detect the presence of math or consistency errors, and combines these fine-grained error labels to produce a final reward score. PathFinder-PRM establishes the new state of the art among PRMs trained on PRM800K-only data and continues to scale gracefully when incorporating additional automated annotations.\n\nThe official PRMBench leaderboard is available at prmbench.github.io, where you can find the most current results and detailed performance breakdowns across different evaluation categories."
    ],
    "durationSeconds": 7.046771716999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "887556a2-8fd0-4ac0-9bd4-668411ddd78e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-27T08:24:01.783Z_

```json
{
  "parentUuid": "3e2817c6-7cda-42d2-a54c-b263827cd974",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "26057893-d49e-4bbc-a879-f79b4c76f7db",
  "timestamp": "2026-05-27T08:24:01.783Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-27T08:24:04.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K6WYap5Mzm4o9HFgCKfvJd`</summary>

```json
{
  "query": "\"from chains to DAGs\" probing graph structure reasoning LLM 2026 premise dependency extractable"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26057893-d49e-4bbc-a879-f79b4c76f7db",
  "isSidechain": false,
  "requestId": "req_011CbSkb6TTbU5NTK8YeJZ2n",
  "type": "assistant",
  "uuid": "80077dd4-60db-4285-a264-0ec0f85167c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U3ZyPXjkAc3CBmYwTNnB98",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 973,
      "cache_read_input_tokens": 23254,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 973,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 23254,
          "cache_creation_input_tokens": 973,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 973
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

_source line 32 · 2026-05-27T08:24:10.379Z_

<details><summary>↩ Tool result · `toolu_01K6WYap5Mzm4o9HFgCKfvJd`</summary>

```text
Web search results for query: ""from chains to DAGs" probing graph structure reasoning LLM 2026 premise dependency extractable"

Links: [{"title":"[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/abs/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/html/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs","url":"https://arxiv.org/pdf/2601.17593"},{"title":"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"},{"title":"From Chains to Graphs: Self-Structured Reasoning for General-Domain LLMs","url":"https://arxiv.org/pdf/2601.03597"}]

I found the paper you're searching for! Here are the key details:

**"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs"** is a paper by Tianjun Zhong and colleagues that introduces Reasoning DAG Probing, a framework for testing whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers.

**Key findings:**

- Many reasoning problems are more naturally modeled as directed acyclic graphs (DAGs), where intermediate conclusions branch, merge, and are reused, rather than as linear chains.

- The researchers associate each reasoning node with a textual realization and train lightweight probes to predict node depth, pairwise distance, and adjacency from hidden states.

- Across reasoning benchmarks, DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale, and enabling nontrivial recovery of dependency graphs.

- These findings suggest that LLM reasoning is not purely sequential, but exhibits measurable internal graph structure.

The paper was submitted on January 24, 2026, and is available on arXiv as paper 2601.17593.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "80077dd4-60db-4285-a264-0ec0f85167c2",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "31bfb2b5-b2bb-49ef-93c2-f7698ce495ec",
  "toolUseResult": {
    "query": "\"from chains to DAGs\" probing graph structure reasoning LLM 2026 premise dependency extractable",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y69DBkBRNveXPq7GJ7iyKC",
        "content": [
          {
            "title": "[2601.17593] From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/abs/2601.17593"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/html/2601.17593"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs",
            "url": "https://arxiv.org/pdf/2601.17593"
          },
          {
            "title": "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260117593Z/abstract"
          },
          {
            "title": "From Chains to Graphs: Self-Structured Reasoning for General-Domain LLMs",
            "url": "https://arxiv.org/pdf/2601.03597"
          }
        ]
      },
      "I found the paper you're searching for! Here are the key details:\n\n**\"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs\"** is a paper by Tianjun Zhong and colleagues that introduces Reasoning DAG Probing, a framework for testing whether LLM hidden states linearly encode properties of an underlying reasoning DAG and where this structure emerges across layers.\n\n**Key findings:**\n\n- Many reasoning problems are more naturally modeled as directed acyclic graphs (DAGs), where intermediate conclusions branch, merge, and are reused, rather than as linear chains.\n\n- The researchers associate each reasoning node with a textual realization and train lightweight probes to predict node depth, pairwise distance, and adjacency from hidden states.\n\n- Across reasoning benchmarks, DAG structure is meaningfully encoded in LLM representations, with recoverability peaking in intermediate layers, varying systematically by node depth, edge span, and model scale, and enabling nontrivial recovery of dependency graphs.\n\n- These findings suggest that LLM reasoning is not purely sequential, but exhibits measurable internal graph structure.\n\nThe paper was submitted on January 24, 2026, and is available on arXiv as paper 2601.17593."
    ],
    "durationSeconds": 5.756420054999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "80077dd4-60db-4285-a264-0ec0f85167c2",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-27T08:24:13.418Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CwqS5W35Y9mRiP74jEadnq`</summary>

```json
{
  "query": "CRM conditional reward model ICLR 2026 sequential conditioning preceding steps arXiv 2509.26578"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "31bfb2b5-b2bb-49ef-93c2-f7698ce495ec",
  "isSidechain": false,
  "requestId": "req_011CbSkbjDYhEkBTGrDSyA6c",
  "type": "assistant",
  "uuid": "fd4f9f69-9cdf-440c-9594-5307032a0f47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PvxJeupj3e4CKJZ7tPKfTX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 24227,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 24227,
          "cache_creation_input_tokens": 649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 649
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

_source line 34 · 2026-05-27T08:24:26.712Z_

<details><summary>↩ Tool result · `toolu_01CwqS5W35Y9mRiP74jEadnq`</summary>

```text
Web search results for query: "CRM conditional reward model ICLR 2026 sequential conditioning preceding steps arXiv 2509.26578"

Links: [{"title":"[2509.26578] Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/abs/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/pdf/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning","url":"https://arxiv.org/html/2509.26578"},{"title":"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=4DJoBOQNd0"},{"title":"Is Conditional Generative Modeling all you need for Decision-Making?","url":"https://arxiv.org/pdf/2211.15657"}]

I found the paper you were searching for! Here are the details:

**Conditional Reward Modeling (CRM)** is proposed as an approach that frames LLM reasoning as a temporal process leading to a correct answer. The reward of each reasoning step is not only conditioned on the preceding steps but also explicitly linked to the final outcome of the reasoning trajectory.

**Key Features:**

- By enforcing conditional probability rules, the design captures the causal relationships among reasoning steps, with the link to the outcome allowing precise attribution of each intermediate step, thereby resolving credit assignment ambiguity.

- Through consistent probabilistic modeling, the rewards produced by CRM enable more reliable cross-sample comparison.

**Performance:**

- Experiments across Best-of-N sampling, beam search and reinforcement learning demonstrate that CRM consistently outperforms existing reward models, offering a principled framework for enhancing LLM reasoning.

- CRM is more robust to reward hacking and delivers stable downstream improvements without relying on verifiable rewards derived from ground truth.

The paper (arXiv:2509.26578) was authored by Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, and Kan Ren from ShanghaiTech University and BIGAI, and was uploaded to arXiv on September 30, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fd4f9f69-9cdf-440c-9594-5307032a0f47",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "bb87ef3a-6c2d-49db-8b41-b305520fe24d",
  "toolUseResult": {
    "query": "CRM conditional reward model ICLR 2026 sequential conditioning preceding steps arXiv 2509.26578",
    "results": [
      {
        "tool_use_id": "srvtoolu_018Pu4EsmsvUuDW6DAjUudoD",
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
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning",
            "url": "https://arxiv.org/html/2509.26578"
          },
          {
            "title": "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=4DJoBOQNd0"
          },
          {
            "title": "Is Conditional Generative Modeling all you need for Decision-Making?",
            "url": "https://arxiv.org/pdf/2211.15657"
          }
        ]
      },
      "I found the paper you were searching for! Here are the details:\n\n**Conditional Reward Modeling (CRM)** is proposed as an approach that frames LLM reasoning as a temporal process leading to a correct answer. The reward of each reasoning step is not only conditioned on the preceding steps but also explicitly linked to the final outcome of the reasoning trajectory.\n\n**Key Features:**\n\n- By enforcing conditional probability rules, the design captures the causal relationships among reasoning steps, with the link to the outcome allowing precise attribution of each intermediate step, thereby resolving credit assignment ambiguity.\n\n- Through consistent probabilistic modeling, the rewards produced by CRM enable more reliable cross-sample comparison.\n\n**Performance:**\n\n- Experiments across Best-of-N sampling, beam search and reinforcement learning demonstrate that CRM consistently outperforms existing reward models, offering a principled framework for enhancing LLM reasoning.\n\n- CRM is more robust to reward hacking and delivers stable downstream improvements without relying on verifiable rewards derived from ground truth.\n\nThe paper (arXiv:2509.26578) was authored by Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, and Kan Ren from ShanghaiTech University and BIGAI, and was uploaded to arXiv on September 30, 2025."
    ],
    "durationSeconds": 13.287245509999993,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fd4f9f69-9cdf-440c-9594-5307032a0f47",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-27T08:24:29.870Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CeH3T9cc44mv6gk5H3H5gv`</summary>

```json
{
  "query": "premise graph structure contrastive training reward model logical validity surface fluency disentangle 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb87ef3a-6c2d-49db-8b41-b305520fe24d",
  "isSidechain": false,
  "requestId": "req_011CbSkcw2yVhTBifNxpbuQX",
  "type": "assistant",
  "uuid": "ef435bdd-2c24-47f7-8c2c-ead07abb4c99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018G3cdzz8Fb1ATJTmz2M4fa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 24876,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 662,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 24876,
          "cache_creation_input_tokens": 662,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 662
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

_source line 36 · 2026-05-27T08:24:37.470Z_

<details><summary>↩ Tool result · `toolu_01CeH3T9cc44mv6gk5H3H5gv`</summary>

```text
Web search results for query: "premise graph structure contrastive training reward model logical validity surface fluency disentangle 2026"

Links: [{"title":"Reward Models Identify Consistency, Not Causality","url":"https://arxiv.org/pdf/2502.14619"},{"title":"Boosting Graph Contrastive Learning via Graph Contrastive Saliency","url":"https://proceedings.mlr.press/v202/wei23c/wei23c.pdf"},{"title":"MERIt: Meta-Path Guided Contrastive Learning for Logical Reasoning","url":"https://arxiv.org/pdf/2203.00357"},{"title":"Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation   for Logical Reading Comprehension","url":"https://arxiv.org/pdf/2409.14495"},{"title":"LSRIF: Logic-Structured Reinforcement Learning for Instruction Following","url":"https://arxiv.org/pdf/2601.06431"}]

The search results contain several relevant papers from 2025-2026 that address related topics. Here's what I found:

**Key Results:**

1. **"Reward Models Identify Consistency, Not Causality"** - This paper discusses how reward models play a crucial role in enhancing reasoning capabilities and serve as mechanisms to evaluate logical correctness, but they evaluate logical structure rather than verifying causal correctness.

2. **"Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation for Logical Reading Comprehension"** - This method improves baselines substantially across two challenging logical reasoning benchmarks (ReClor and LogiQA 2.0).

3. **"LSRIF: Logic-Structured Reinforcement Learning for Instruction Following"** - This paper proposes a logic-structured training framework that explicitly models instruction logic with a dataset containing constraint structures such as parallel, sequential, and conditional types, and a structure-aware rewarding method.

4. **"Boosting Graph Contrastive Learning via Graph Contrastive Saliency"** - This work uses gradient-based saliency measurements to disentangle semantic and environmental background structures of graphs.

5. **"MERIt: Meta-Path Guided Contrastive Learning for Logical Reasoning"** - This method consists of meta-path guided data construction and counterfactual data augmentation to perform automatic instance composition from unlabeled corpus for contrastive learning.

These papers collectively address themes of contrastive learning, logical reasoning, reward models, and graph/structural analysis relevant to your search query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ef435bdd-2c24-47f7-8c2c-ead07abb4c99",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "fd028236-9b71-4d0b-b5d9-59c74622603c",
  "toolUseResult": {
    "query": "premise graph structure contrastive training reward model logical validity surface fluency disentangle 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P3RwMusfey5stmLSChSYvb",
        "content": [
          {
            "title": "Reward Models Identify Consistency, Not Causality",
            "url": "https://arxiv.org/pdf/2502.14619"
          },
          {
            "title": "Boosting Graph Contrastive Learning via Graph Contrastive Saliency",
            "url": "https://proceedings.mlr.press/v202/wei23c/wei23c.pdf"
          },
          {
            "title": "MERIt: Meta-Path Guided Contrastive Learning for Logical Reasoning",
            "url": "https://arxiv.org/pdf/2203.00357"
          },
          {
            "title": "Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation   for Logical Reading Comprehension",
            "url": "https://arxiv.org/pdf/2409.14495"
          },
          {
            "title": "LSRIF: Logic-Structured Reinforcement Learning for Instruction Following",
            "url": "https://arxiv.org/pdf/2601.06431"
          }
        ]
      },
      "The search results contain several relevant papers from 2025-2026 that address related topics. Here's what I found:\n\n**Key Results:**\n\n1. **\"Reward Models Identify Consistency, Not Causality\"** - This paper discusses how reward models play a crucial role in enhancing reasoning capabilities and serve as mechanisms to evaluate logical correctness, but they evaluate logical structure rather than verifying causal correctness.\n\n2. **\"Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation for Logical Reading Comprehension\"** - This method improves baselines substantially across two challenging logical reasoning benchmarks (ReClor and LogiQA 2.0).\n\n3. **\"LSRIF: Logic-Structured Reinforcement Learning for Instruction Following\"** - This paper proposes a logic-structured training framework that explicitly models instruction logic with a dataset containing constraint structures such as parallel, sequential, and conditional types, and a structure-aware rewarding method.\n\n4. **\"Boosting Graph Contrastive Learning via Graph Contrastive Saliency\"** - This work uses gradient-based saliency measurements to disentangle semantic and environmental background structures of graphs.\n\n5. **\"MERIt: Meta-Path Guided Contrastive Learning for Logical Reasoning\"** - This method consists of meta-path guided data construction and counterfactual data augmentation to perform automatic instance composition from unlabeled corpus for contrastive learning.\n\nThese papers collectively address themes of contrastive learning, logical reasoning, reward models, and graph/structural analysis relevant to your search query."
    ],
    "durationSeconds": 7.595583528999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ef435bdd-2c24-47f7-8c2c-ead07abb4c99",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-27T08:24:40.277Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EiA7drb6EhafKThYeKanS5`</summary>

```json
{
  "query": "RewardFlow topology-aware reward propagation state graphs agentic arXiv 2603.18859"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd028236-9b71-4d0b-b5d9-59c74622603c",
  "isSidechain": false,
  "requestId": "req_011CbSkdj1CXsUGb2Y4DPpNf",
  "type": "assistant",
  "uuid": "c71ed5dc-aab8-462b-b0c2-fb58c6c3ba53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SZa2uvBRWb8mdS7Rus9fUe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 702,
      "cache_read_input_tokens": 25538,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 702,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 25538,
          "cache_creation_input_tokens": 702,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 702
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

_source line 38 · 2026-05-27T08:24:46.009Z_

<details><summary>↩ Tool result · `toolu_01EiA7drb6EhafKThYeKanS5`</summary>

```text
Web search results for query: "RewardFlow topology-aware reward propagation state graphs agentic arXiv 2603.18859"

Links: [{"title":"[2603.18859] RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/abs/2603.18859"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/html/2603.18859"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models","url":"https://arxiv.org/pdf/2603.18859"},{"title":"GitHub - tmlr-group/RewardFlow: [arXiv:2603.18859] \"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models\" · GitHub","url":"https://github.com/tmlr-group/RewardFlow"},{"title":"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/402860521_RewardFlow_Topology-Aware_Reward_Propagation_on_State_Graphs_for_Agentic_RL_with_Large_Language_Models"}]

I found the paper! Here's what I found about RewardFlow (arXiv 2603.18859):

**Overview:**
RewardFlow is a lightweight method for estimating state-level rewards tailored to agentic reasoning tasks that leverages the intrinsic topological structure of states within reasoning trajectories by constructing state graphs.

**Key Problem it Addresses:**
The inherent sparsity of terminal rewards hinders fine-grained, state-level optimization, and while process reward modeling offers a promising alternative, training dedicated reward models often entails substantial computational costs and scaling difficulties.

**How it Works:**
RewardFlow enables an analysis of state-wise contributions to success, followed by topology-aware graph propagation to quantify contributions and yield objective, state-level rewards.

**Results:**
When integrated as dense rewards for RL optimization, RewardFlow substantially outperforms prior RL baselines across four agentic reasoning benchmarks, demonstrating superior performance, robustness, and training efficiency.

**Availability:**
The implementation of RewardFlow is publicly available at https://github.com/tmlr-group/RewardFlow.

The paper was published on March 19, 2026, and appears to be a significant contribution to reinforcement learning for large language models with agentic reasoning capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c71ed5dc-aab8-462b-b0c2-fb58c6c3ba53",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "e7162783-4f2e-4400-bd2e-cbe99b8f986c",
  "toolUseResult": {
    "query": "RewardFlow topology-aware reward propagation state graphs agentic arXiv 2603.18859",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BcWDPyMJSMzbfb7kBcLRAQ",
        "content": [
          {
            "title": "[2603.18859] RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models",
            "url": "https://arxiv.org/abs/2603.18859"
          },
          {
            "title": "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models",
            "url": "https://arxiv.org/html/2603.18859"
          },
          {
            "title": "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models",
            "url": "https://arxiv.org/pdf/2603.18859"
          },
          {
            "title": "GitHub - tmlr-group/RewardFlow: [arXiv:2603.18859] \"RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models\" · GitHub",
            "url": "https://github.com/tmlr-group/RewardFlow"
          },
          {
            "title": "RewardFlow: Topology-Aware Reward Propagation on State Graphs for Agentic RL with Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/402860521_RewardFlow_Topology-Aware_Reward_Propagation_on_State_Graphs_for_Agentic_RL_with_Large_Language_Models"
          }
        ]
      },
      "I found the paper! Here's what I found about RewardFlow (arXiv 2603.18859):\n\n**Overview:**\nRewardFlow is a lightweight method for estimating state-level rewards tailored to agentic reasoning tasks that leverages the intrinsic topological structure of states within reasoning trajectories by constructing state graphs.\n\n**Key Problem it Addresses:**\nThe inherent sparsity of terminal rewards hinders fine-grained, state-level optimization, and while process reward modeling offers a promising alternative, training dedicated reward models often entails substantial computational costs and scaling difficulties.\n\n**How it Works:**\nRewardFlow enables an analysis of state-wise contributions to success, followed by topology-aware graph propagation to quantify contributions and yield objective, state-level rewards.\n\n**Results:**\nWhen integrated as dense rewards for RL optimization, RewardFlow substantially outperforms prior RL baselines across four agentic reasoning benchmarks, demonstrating superior performance, robustness, and training efficiency.\n\n**Availability:**\nThe implementation of RewardFlow is publicly available at https://github.com/tmlr-group/RewardFlow.\n\nThe paper was published on March 19, 2026, and appears to be a significant contribution to reinforcement learning for large language models with agentic reasoning capabilities."
    ],
    "durationSeconds": 5.727988692999992,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c71ed5dc-aab8-462b-b0c2-fb58c6c3ba53",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains ar…",
  "leafUuid": "e7162783-4f2e-4400-bd2e-cbe99b8f986c",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Tool call

_source line 41 · 2026-05-27T08:24:48.884Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VBQ2LeyfaVbemDnov96oAJ`</summary>

```json
{
  "query": "graph-aware process reward model training structure-aware contrastive PRM math reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7162783-4f2e-4400-bd2e-cbe99b8f986c",
  "isSidechain": false,
  "requestId": "req_011CbSkeMWQh2s7gHhRD9AoE",
  "type": "assistant",
  "uuid": "b7d075d7-a41c-4ab3-b36d-1235a7ab15d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018P7gapyiGzMzRyg7aYgQ3Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 26240,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 762,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 26240,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 762
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

_source line 42 · 2026-05-27T08:24:55.664Z_

<details><summary>↩ Tool result · `toolu_01VBQ2LeyfaVbemDnov96oAJ`</summary>

```text
Web search results for query: "graph-aware process reward model training structure-aware contrastive PRM math reasoning 2025 2026"

Links: [{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"Process Reward Models: Step-Level Feedback for LLMs","url":"https://www.emergentmind.com/topics/process-reward-models-prm"},{"title":"Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner","url":"https://arxiv.org/pdf/2507.23317"},{"title":"Process Reward Models That Think","url":"https://arxiv.org/pdf/2504.16828"},{"title":"GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning","url":"https://arxiv.org/pdf/2508.04088"},{"title":"Process-supervised Reward Models (PRMs)","url":"https://www.emergentmind.com/topics/process-supervised-reward-models-prm"}]

Based on the search results, I found several relevant papers and research on Process Reward Models (PRMs) for mathematical reasoning from 2025-2026. Here are the key findings:

## Recent PRM Developments (2025-2026)

**Generative and Multimodal PRMs:**
GM-PRM is the first multimodal generative PRM, supporting chain generation in multimodal mathematical reasoning tasks. GM-PRM achieves state-of-the-art results on multiple multimodal math benchmarks with remarkable data efficiency, requiring only a 20K-sample training dataset.

**Advanced Training Methodologies:**
Recent PRMs incorporate coarse-to-fine granularity training on variable-length merged steps to mitigate redundancy and improve fine-step sensitivity. Retrieval-enhanced inputs integrating semantically similar examples improve out-of-distribution robustness and model generalization.

**Hierarchical and Error-Aware Approaches:**
Hierarchical models such as PathFinder-PRM explicitly decompose errors into math and consistency dimensions before reward assignment, increasing interpretability and data efficiency.

**Generative Verification Models:**
Generative PRMs show more robustness under domain shifts in contrast with discriminative PRMs.

The research landscape shows a clear shift toward more sophisticated PRM architectures that incorporate structure awareness, multi-dimensional error handling, and improved generalization capabilities for mathematical reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7d075d7-a41c-4ab3-b36d-1235a7ab15d6",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "7c152276-91fa-4fe7-a92d-5ee7ed0faa7e",
  "toolUseResult": {
    "query": "graph-aware process reward model training structure-aware contrastive PRM math reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017sk2H8HYRU57zEf3FA87Fi",
        "content": [
          {
            "title": "A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models",
            "url": "https://arxiv.org/html/2510.08049v3"
          },
          {
            "title": "Process Reward Models: Step-Level Feedback for LLMs",
            "url": "https://www.emergentmind.com/topics/process-reward-models-prm"
          },
          {
            "title": "Good Learners Think Their Thinking: Generative PRM Makes Large Reasoning Model More Efficient Math Learner",
            "url": "https://arxiv.org/pdf/2507.23317"
          },
          {
            "title": "Process Reward Models That Think",
            "url": "https://arxiv.org/pdf/2504.16828"
          },
          {
            "title": "GM-PRM: A Generative Multimodal Process Reward Model for Multimodal Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2508.04088"
          },
          {
            "title": "Process-supervised Reward Models (PRMs)",
            "url": "https://www.emergentmind.com/topics/process-supervised-reward-models-prm"
          }
        ]
      },
      "Based on the search results, I found several relevant papers and research on Process Reward Models (PRMs) for mathematical reasoning from 2025-2026. Here are the key findings:\n\n## Recent PRM Developments (2025-2026)\n\n**Generative and Multimodal PRMs:**\nGM-PRM is the first multimodal generative PRM, supporting chain generation in multimodal mathematical reasoning tasks. GM-PRM achieves state-of-the-art results on multiple multimodal math benchmarks with remarkable data efficiency, requiring only a 20K-sample training dataset.\n\n**Advanced Training Methodologies:**\nRecent PRMs incorporate coarse-to-fine granularity training on variable-length merged steps to mitigate redundancy and improve fine-step sensitivity. Retrieval-enhanced inputs integrating semantically similar examples improve out-of-distribution robustness and model generalization.\n\n**Hierarchical and Error-Aware Approaches:**\nHierarchical models such as PathFinder-PRM explicitly decompose errors into math and consistency dimensions before reward assignment, increasing interpretability and data efficiency.\n\n**Generative Verification Models:**\nGenerative PRMs show more robustness under domain shifts in contrast with discriminative PRMs.\n\nThe research landscape shows a clear shift toward more sophisticated PRM architectures that incorporate structure awareness, multi-dimensional error handling, and improved generalization capabilities for mathematical reasoning tasks."
    ],
    "durationSeconds": 6.774039032000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b7d075d7-a41c-4ab3-b36d-1235a7ab15d6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-27T08:24:59.122Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more targeted search to check if there's any very recent work that directly combines premise/dependency graphs with contrastive training for PRMs - this would be the biggest threat to the novelty claim.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c152276-91fa-4fe7-a92d-5ee7ed0faa7e",
  "isSidechain": false,
  "requestId": "req_011CbSkf5EeCy7FMZg4uLQ1x",
  "type": "assistant",
  "uuid": "f219aa5b-8627-4caa-940d-c000ad61f693",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XabtTrgH9oU6G6Q9FPcizd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 27002,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 27002,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 44 · 2026-05-27T08:25:00.035Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BV1ujh3j8BLkB8R5GN724g`</summary>

```json
{
  "query": "\"graph of verification\" GoV reasoning DAG verification training-free 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f219aa5b-8627-4caa-940d-c000ad61f693",
  "isSidechain": false,
  "requestId": "req_011CbSkf5EeCy7FMZg4uLQ1x",
  "type": "assistant",
  "uuid": "8a149681-2dc3-41d5-870e-37eb0fdba070",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XabtTrgH9oU6G6Q9FPcizd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 703,
      "cache_read_input_tokens": 27002,
      "output_tokens": 131,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 703,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 131,
          "cache_read_input_tokens": 27002,
          "cache_creation_input_tokens": 703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 703
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

_source line 45 · 2026-05-27T08:25:07.199Z_

<details><summary>↩ Tool result · `toolu_01BV1ujh3j8BLkB8R5GN724g`</summary>

```text
Web search results for query: ""graph of verification" GoV reasoning DAG verification training-free 2025 2026"

Links: [{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/html/2506.12509v3"},{"title":"[2506.12509] Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://arxiv.org/abs/2506.12509"},{"title":"Paper page - Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://huggingface.co/papers/2506.12509"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs","url":"https://www.researchgate.net/publication/392735078_Graph_of_Verification_Structured_Verification_of_LLM_Reasoning_with_Directed_Acyclic_Graphs"},{"title":"Graph of Verification: Structured Verification of LLM Reasoning","url":"https://arxiv.org/pdf/2506.12509"},{"title":"GraphReason: Enhancing Reasoning Capabilities of Large Language Models   through A Graph-Based Verification Approach","url":"https://arxiv.org/pdf/2308.09267"},{"title":"NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning","url":"https://arxiv.org/pdf/2510.02816"}]

Based on the search results, here's what I found about Graph of Verification (GoV):

## Overview

The Graph of Verification (GoV) is a novel, training-free framework that models reasoning as a Directed Acyclic Graph and leverages a flexible node block architecture for adaptable, multi-granular verification.

## Key Contributions

GoV offers three key contributions: First, it explicitly models the underlying deductive process as a directed acyclic graph (DAG). Second, it enforces a topological order over the DAG to guide stepwise verification. Third, GoV introduces the notion of customizable node blocks, which flexibly define the verification granularity, from atomic propositions to full paragraphs, while ensuring that all requisite premises derived from the graph are provided as contextual input for each verification unit.

## Verification Process

GoV operationalizes structured validation by first modeling reasoning as a Directed Acyclic Graph (DAG), then a topological sort enforces causal consistency, ensuring premises are verified before conclusions.

## Performance

GoV's adaptive approach significantly outperforms both holistic baselines and other state-of-the-art decomposition-based methods, establishing a new standard for training-free reasoning verification.

The paper was published on arXiv in November 2025 (arXiv:2506.12509) and addresses the challenge of verifying complex, multi-step reasoning in Large Language Models without requiring training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a149681-2dc3-41d5-870e-37eb0fdba070",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "71fe5b70-dd7c-4b32-a78f-5aa671bd2b3a",
  "toolUseResult": {
    "query": "\"graph of verification\" GoV reasoning DAG verification training-free 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CiRAwPFXSdvY2rhXGpjnxN",
        "content": [
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://arxiv.org/html/2506.12509v3"
          },
          {
            "title": "[2506.12509] Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://arxiv.org/abs/2506.12509"
          },
          {
            "title": "Paper page - Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://huggingface.co/papers/2506.12509"
          },
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning with Directed Acyclic Graphs",
            "url": "https://www.researchgate.net/publication/392735078_Graph_of_Verification_Structured_Verification_of_LLM_Reasoning_with_Directed_Acyclic_Graphs"
          },
          {
            "title": "Graph of Verification: Structured Verification of LLM Reasoning",
            "url": "https://arxiv.org/pdf/2506.12509"
          },
          {
            "title": "GraphReason: Enhancing Reasoning Capabilities of Large Language Models   through A Graph-Based Verification Approach",
            "url": "https://arxiv.org/pdf/2308.09267"
          },
          {
            "title": "NCV: A Node-Wise Consistency Verification Approach for Low-Cost Structured Error Localization in LLM Reasoning",
            "url": "https://arxiv.org/pdf/2510.02816"
          }
        ]
      },
      "Based on the search results, here's what I found about Graph of Verification (GoV):\n\n## Overview\n\nThe Graph of Verification (GoV) is a novel, training-free framework that models reasoning as a Directed Acyclic Graph and leverages a flexible node block architecture for adaptable, multi-granular verification.\n\n## Key Contributions\n\nGoV offers three key contributions: First, it explicitly models the underlying deductive process as a directed acyclic graph (DAG). Second, it enforces a topological order over the DAG to guide stepwise verification. Third, GoV introduces the notion of customizable node blocks, which flexibly define the verification granularity, from atomic propositions to full paragraphs, while ensuring that all requisite premises derived from the graph are provided as contextual input for each verification unit.\n\n## Verification Process\n\nGoV operationalizes structured validation by first modeling reasoning as a Directed Acyclic Graph (DAG), then a topological sort enforces causal consistency, ensuring premises are verified before conclusions.\n\n## Performance\n\nGoV's adaptive approach significantly outperforms both holistic baselines and other state-of-the-art decomposition-based methods, establishing a new standard for training-free reasoning verification.\n\nThe paper was published on arXiv in November 2025 (arXiv:2506.12509) and addresses the challenge of verifying complex, multi-step reasoning in Large Language Models without requiring training."
    ],
    "durationSeconds": 7.156226161000028,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "8a149681-2dc3-41d5-870e-37eb0fdba070",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-27T08:25:09.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SjC6PtSAsQCjbj7L9KQbq2`</summary>

```json
{
  "query": "InfoNCE graph contrastive learning node embedding DAG structure-preserving perturbation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71fe5b70-dd7c-4b32-a78f-5aa671bd2b3a",
  "isSidechain": false,
  "requestId": "req_011CbSkfv9ivjWRPVnEcQJwQ",
  "type": "assistant",
  "uuid": "00fb0e73-3367-42eb-9e4b-bcd9813d3c4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8BLKyy4HFPdYyt6XkYYPg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 27705,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 878,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 27705,
          "cache_creation_input_tokens": 878,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 878
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

_source line 47 · 2026-05-27T08:25:18.665Z_

<details><summary>↩ Tool result · `toolu_01SjC6PtSAsQCjbj7L9KQbq2`</summary>

```text
Web search results for query: "InfoNCE graph contrastive learning node embedding DAG structure-preserving perturbation 2025 2026"

Links: [{"title":"(PDF) InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning","url":"https://www.researchgate.net/publication/393356500_InfoNCE_is_a_Free_Lunch_for_Semantically_guided_Graph_Contrastive_Learning"},{"title":"GraphCL: Contrastive Self-Supervised Learning of Graph Representations","url":"https://arxiv.org/pdf/2007.08025"},{"title":"Layer-wise contrastive network for unsupervised graph representation learning - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0925231226001335"},{"title":"[2505.06282] InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning","url":"https://arxiv.org/abs/2505.06282"},{"title":"InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning","url":"https://arxiv.org/html/2505.06282v1"},{"title":"Multi-scale tree-guided contrastive learning for structure-aware graph representation | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-02219-7"},{"title":"Towards Robust Neural Graph Collaborative Filtering via Structure Denoising and Embedding Perturbation | ACM Transactions on Information Systems","url":"https://dl.acm.org/doi/10.1145/3568396"},{"title":"Graph Contrastive Learning with Implicit Augmentations","url":"https://arxiv.org/pdf/2211.03710"},{"title":"A Simplified Framework for Contrastive Learning for Node Representations","url":"https://arxiv.org/pdf/2305.00623"},{"title":"Deep Graph Contrastive Representation Learning Yanqiao Zhu1,2∗ Yichen Xu3∗,†","url":"https://arxiv.org/pdf/2006.04131"}]

Based on the search results, I found relevant research on InfoNCE and graph contrastive learning. Here are the key findings:

## Recent 2025 Research

A recent paper titled "InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning" was presented at the 48th International ACM SIGIR Conference in July 2025. Traditional GCL optimizes InfoNCE by using augmentations to define self-supervised tasks, treating augmented pairs as positive samples and others as negative. The research showed significant improvements in both IID and OOD scenarios, achieving up to a 9.05% improvement.

## Structure-Preserving Perturbation Research (2026)

Existing graph contrastive learning methods typically rely on random perturbations to generate augmented views. However, perturbing structurally central nodes and peripheral nodes with equal intensity may damage critical semantic substructures, thereby compromising the stability and discriminability of the learned embeddings. Most existing works adopt contrastive losses based on global alignment, encouraging consistency between augmented views of the same node (e.g., InfoNCE).

## Node Embedding and Augmentation Approaches

Recent methods exploit latent augmentations that preserve graph topological information, as opposed to classical GCL methods that create augmentations by randomly perturbing edges, nodes or attributes.

The search results focus primarily on graph contrastive learning with InfoNCE loss, though specific research on DAG (Directed Acyclic Graph) structure-preserving perturbations was not prominently featured in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "00fb0e73-3367-42eb-9e4b-bcd9813d3c4c",
  "isSidechain": false,
  "promptId": "3681f6c4-d090-41ad-8b63-a0d4950a3891",
  "type": "user",
  "uuid": "3762e960-767d-463c-b317-1b43c8273441",
  "toolUseResult": {
    "query": "InfoNCE graph contrastive learning node embedding DAG structure-preserving perturbation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MztDb6foC2FDdRQpnH3rjq",
        "content": [
          {
            "title": "(PDF) InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning",
            "url": "https://www.researchgate.net/publication/393356500_InfoNCE_is_a_Free_Lunch_for_Semantically_guided_Graph_Contrastive_Learning"
          },
          {
            "title": "GraphCL: Contrastive Self-Supervised Learning of Graph Representations",
            "url": "https://arxiv.org/pdf/2007.08025"
          },
          {
            "title": "Layer-wise contrastive network for unsupervised graph representation learning - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S0925231226001335"
          },
          {
            "title": "[2505.06282] InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning",
            "url": "https://arxiv.org/abs/2505.06282"
          },
          {
            "title": "InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning",
            "url": "https://arxiv.org/html/2505.06282v1"
          },
          {
            "title": "Multi-scale tree-guided contrastive learning for structure-aware graph representation | Complex & Intelligent Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s40747-025-02219-7"
          },
          {
            "title": "Towards Robust Neural Graph Collaborative Filtering via Structure Denoising and Embedding Perturbation | ACM Transactions on Information Systems",
            "url": "https://dl.acm.org/doi/10.1145/3568396"
          },
          {
            "title": "Graph Contrastive Learning with Implicit Augmentations",
            "url": "https://arxiv.org/pdf/2211.03710"
          },
          {
            "title": "A Simplified Framework for Contrastive Learning for Node Representations",
            "url": "https://arxiv.org/pdf/2305.00623"
          },
          {
            "title": "Deep Graph Contrastive Representation Learning Yanqiao Zhu1,2∗ Yichen Xu3∗,†",
            "url": "https://arxiv.org/pdf/2006.04131"
          }
        ]
      },
      "Based on the search results, I found relevant research on InfoNCE and graph contrastive learning. Here are the key findings:\n\n## Recent 2025 Research\n\nA recent paper titled \"InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning\" was presented at the 48th International ACM SIGIR Conference in July 2025. Traditional GCL optimizes InfoNCE by using augmentations to define self-supervised tasks, treating augmented pairs as positive samples and others as negative. The research showed significant improvements in both IID and OOD scenarios, achieving up to a 9.05% improvement.\n\n## Structure-Preserving Perturbation Research (2026)\n\nExisting graph contrastive learning methods typically rely on random perturbations to generate augmented views. However, perturbing structurally central nodes and peripheral nodes with equal intensity may damage critical semantic substructures, thereby compromising the stability and discriminability of the learned embeddings. Most existing works adopt contrastive losses based on global alignment, encouraging consistency between augmented views of the same node (e.g., InfoNCE).\n\n## Node Embedding and Augmentation Approaches\n\nRecent methods exploit latent augmentations that preserve graph topological information, as opposed to classical GCL methods that create augmentations by randomly perturbing edges, nodes or attributes.\n\nThe search results focus primarily on graph contrastive learning with InfoNCE loss, though specific research on DAG (Directed Acyclic Graph) structure-preserving perturbations was not prominently featured in these results."
    ],
    "durationSeconds": 8.69165752799998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "00fb0e73-3367-42eb-9e4b-bcd9813d3c4c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-27T08:26:06.293Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the research landscape. Let me synthesize my findings and provide my analysis as the 发掘 agent.

Key findings from my research:

1. **The problem is well-documented and real**: "Reward Under Attack" (2026) and "Reward Models Identify Consistency, Not Causality" (2025) clearly document the problem of PRMs being fluency detectors. The 43% stylistic shortcut statistic is from "Reward Under Attack."

2. **PARC/PERL infrastructure is solid**: 90% recall on premise link extraction is well-established at ICML 2025.


3. **"From Chains to DAGs" (Jan 2026)** shows that LLMs encode DAG structure in their intermediate representations, which could bolster the theoretical grounding of the approach. The concurrent work landscape is fairly clear—CPMI handles auto-labeling without DAGs, RewardFlow uses state-transition graphs for agentic tasks without contrastive training, GoV offers training-free verification, and CRM does sequential conditioning without explicit DAG structure. Notably, I haven't found any existing work that merges premise dependency DAGs with contrastive PRM training, so the novelty claim holds up.

4. **Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation** and **Neuro-Symbolic Contrastive Learning for Cross-domain Inference** are both potentially relevant—the former uses premise-oriented augmentation with contrastive learning for logical reading comprehension, while the latter applies contrastive pairs to encode logical relations. These aren't cited and might need differentiation in the related work section.

5. The key question is whether explicit DAG structure actually provides benefits beyond what adversarial training with harder negatives can achieve. APRM already gets +5.3pp OOD improvement through adversarial examples alone, so I need to make a compelling case that the DAG structure captures something fundamentally different that simple harder negatives cannot.

6. There's a real concern about noise propagation—if premise link extraction only achieves 90% recall, then roughly 10% of the contrastive pairs will have incorrect graph annotations during training. I should investigate how sensitive the approach is to this level of noise in the DAG structure.

7. The proposal has genuine strengths: it identifies a well-documented problem with PRM fragility, combines DAGs with contrastive training in a novel way that hasn't been tried before, has the necessary infrastructure ready (PARC extraction and existing datasets), and targets the root cause at training time rather than applying post-hoc fixes.

8. One particularly strong angle is that "From Chains to DAGs" provides direct evidence that LLMs internally encode DAG structure, which means contrastive training could help surface and reinforce this latent capability.

9. The framing could be sharpened by positioning this as learning causally faithful reward representations rather than just disentangling fluency from validity—this connects to the causal inference literature on invariance.

10. The real significance isn't just PRMBench score improvement, but closing the gap between what PRMs actually measure (consistency) and what we need them to measure (causality), which ties more deeply to the literature on reward models identifying consistency rather than causality.

11. The main trivial alternative is adversarial training with harder negatives (APRM), so I need to make a clear argument for why DAG-structured negatives are fundamentally different—the key distinction is that APRM creates harder negatives without structural grounding, whereas DAG-anchored negatives are theoretically grounded in actual logical dependencies, preventing the model from learning spurious APRM-specific patterns instead of genuine logical validity.

12. There's relevant prior work in "Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation" (EMNLP Findings 2024) that constructs contrastive examples through premise structure manipulation in reading comprehension, which I need to differentiate from.

13. The 90% recall assumption was validated on Llama-3.1-8B-Instruct for math reasoning, but I'm using Qwen2.5-Math-7B-Instruct as the PRM backbone—I need to verify whether DAG extraction quality will actually transfer across different model families and instruction-tuned variants.

Now I'm distinguishing between what constitutes genuine discovery versus what's remediation work. My role is sharpening the novelty framing and identifying underexploited connections to related work that could strengthen the contribution, not fixing experimental design issues or adding baselines. The key insight is that "From Chains to DAGs" work already suggests DAG structure is encoded in LLMs, so explicitly training on DAG structure becomes a natural, principled intervention rather than an arbitrary choice. I'm also thinking through how to frame the consistency-to-causality connection as a significance lever.

There are several specific gaps I need to flag: the uncited Thought-Path Contrastive Learning work that uses similar premise-oriented contrastive approaches, the need for a clearer argument distinguishing DAG-anchored negatives from APRM's domain-agnostic adversarial approach, and the fact that the dual-objective design with InfoNCE loss over DAG-anchored embeddings is the most novel technical component but isn't being emphasized for what it actually does—creating a representation space that captures causal structure rather than just harder negatives.

The proposal is actually quite mature with a clear problem statement backed by evidence, comprehensive related work, specific technical approach, concrete evaluation plan, and resource estimates. But there are still 3-4 concrete ways to sharpen the idea's ceiling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3762e960-767d-463c-b317-1b43c8273441",
  "isSidechain": false,
  "requestId": "req_011CbSkgmAmANDqpZA7kt2A8",
  "type": "assistant",
  "uuid": "df594aad-e46a-4f41-9ac3-dc22e3f71b57",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zPxLJYpeCaFAwj6DVDW9h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 988,
      "cache_read_input_tokens": 28583,
      "output_tokens": 5982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5982,
          "cache_read_input_tokens": 28583,
          "cache_creation_input_tokens": 988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 988
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

_source line 49 · 2026-05-27T08:27:26.708Z_

Now I have sufficient research to provide my analysis. Let me synthesize my findings.

---

【状态】: 有发掘空间

【前置调研发现】
- **"Reward Under Attack" (arXiv:2603.06621, Feb 2026)**: 确认了 proposal 引用的核心动机数据——43% reward gains 来自 stylistic shortcuts，PRMs 在 AIME 上 >0.9 score 但 <4% 准确率。数据真实可靠，问题定义站得住脚。
- **"Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619, Feb 2025)**: 从理论层面确认 PRMs 检测的是 consistency 而非 causality。这一发现与 proposal 的目标高度对齐，但 proposal 尚未充分利用这个 framing（详见发掘点）。
- **"From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs" (arXiv:2601.17593, Jan 2026)**: 关键未引用论文。证明了 LLM 隐藏状态中**已经线性编码了 DAG 结构**，可恢复性在中间层达到峰值。这为 PGCT 的 contrastive training 提供了直接的理论支撑——不是在教模型一个全新的东西，而是在显式化模型已经隐含编码但未被奖励信号利用的结构。
- **"Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation for Logical Reading Comprehension" (arXiv:2409.14495, EMNLP Findings 2024)**: 未引用的高度相关工作。通过操纵 premise 结构构造 contrastive examples 用于阅读理解，与 PGCT 的 premise-oriented contrastive pair 构造思路有直接技术相似性，需要明确差异化。
- **CPMI (arXiv:2604.10660, Apr 2026)**: 确认了 proposal 的描述——使用 contrastive mutual information 进行 PRM auto-labeling，但不使用 premise dependency graphs。差异化清晰。
- **RewardFlow (arXiv:2603.18859, Mar 2026)**: 确认了 proposal 的描述——在 state-transition graphs 上做 reward propagation，针对 agentic tasks，无 contrastive training。差异化清晰。
- **GoV (arXiv:2506.12509, 2025)**: Training-free DAG verification framework，topological sort 确保 premises 在 conclusions 之前被验证。与 PGCT 的区别在于 training-free vs. training-time。
- **APRM (arXiv:2511.22888, Nov 2025)**: Adversarial training with harder negatives，+5.3pp OOD。这是 PGCT 最直接的 trivial alternative 威胁——不需要 DAG extraction 就能构造 harder negatives。
- **Neuro-Symbolic Contrastive Learning for Cross-domain Inference (arXiv:2502.09213, 2025)**: 使用 contrastive pairs 将 logical relations 刻入 embedding space，思路上与 PGCT 的 DAG-anchored InfoNCE 有可比性。
- **PathFinder-PRM (2025)**: PRMBench SOTA 67.7，通过 error-type-aware hierarchical supervision 实现，与 PGCT 的 structure-aware 路线互补但不重叠。
- **调研总结**: 当前 PRM robustness 领域的研究者主要从三个角度突破——(1) 后处理校正（CRA, PURE）；(2) 训练时对抗性增强（APRM）；(3) 条件化建模（CRM）。**尚无工作将 premise dependency 的显式逻辑结构融入 PRM 训练信号**，PGCT 的组合在文献中确实是空白。但这个 novelty 的"锋利度"取决于能否与 APRM 的 trivial alternative 拉开清晰差距，以及能否从"组合创新"上升到"insight-driven 创新"。

---

【发掘点 1】
- **维度**: 核心 claim 强化 / significance 提升
- **内容**: Proposal 当前的核心 framing 是"disentangle fluency from validity"，这个说法准确但**缺乏理论锐度**。建议将核心 claim 重新锚定到 **"consistency → causality" 范式转换**上。具体来说：(1) "Reward Models Identify Consistency, Not Causality" 已经明确诊断出 PRM 的根本缺陷不只是"分不清 fluency"，而是**检测的是 consistency（步骤间表面一致性）而非 causality（步骤间逻辑因果性）**；(2) Premise dependency DAGs 恰恰编码的就是 causality——哪个步骤在逻辑上依赖哪个前提；(3) 因此 PGCT 可以被 framed 为**第一个在训练时将 PRM 的优化目标从 consistency-detection 显式转向 causality-detection 的方法**。这个 framing 比"disentangle fluency/validity"更有理论穿透力：它不是在说"我们构造了更好的 contrastive pairs"，而是在说"我们从根本上改变了 PRM 学习的是什么"。
- **价值**: 提升 Significance 和 Novelty 两个维度。"Disentangle fluency/validity"听起来像 engineering trick；"consistency → causality"听起来像 paradigm contribution。审稿人看到后者更可能评价为 "surprising and important" 而非 "incremental"。
- **调研依据**: 直接参考 "Reward Models Identify Consistency, Not Causality" (arXiv:2502.14619) 的核心诊断结论，将 PGCT 定位为该诊断的 prescriptive solution。

【发掘点 2】
- **维度**: novelty 锐化
- **内容**: Proposal **必须引用并整合 "From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs" (arXiv:2601.17593, Jan 2026)**。这篇论文证明了 LLMs 的隐藏状态中**已经线性编码了推理 DAG 结构**（node depth、pairwise distance、adjacency 均可从中间层 probe 出来）。这为 PGCT 提供了一个极有力的理论论证：PGCT 的 contrastive training **不是在强迫模型学习一个外在的、人工定义的结构**，而是在**显式化并放大模型已经隐含编码但被标准 PRM training 忽视的结构表征**。这解决了一个潜在的审稿人质疑——"为什么 DAG 结构对 PRM 有用？模型本来就不理解 DAG"——答案是模型其实已经理解了，只是标准训练没有给予正确的信号去利用这个理解。
- **价值**: Novelty 维度。将 PGCT 从"外部注入结构"提升为"对齐模型内在表征"，显著增强了方法论的理论合理性，降低审稿人质疑"DAG extraction noise 会不会 corrupt training"的概率。
- **调研依据**: 直接参考 "From Chains to DAGs" (arXiv:2601.17593)，该论文的 probing results 是本条建议的核心依据。

【发掘点 3】
- **维度**: trivial alternative 威胁
- **内容**: APRM (Adversarial Training for PRMs, Nov 2025) 构造 harder negatives 实现了 +5.3pp OOD 增益，**不需要任何 DAG extraction**。一个苛刻但合理的审稿人会问："为什么不直接用 adversarial training 构造 harder negatives？你花了大量成本做 DAG extraction，增量收益是什么？" 当前 proposal 的 related work section 列出了 APRM 但没有直接回应这个问题。建议在核心 claim 中**显式论证 DAG-anchored negatives 与 domain-agnostic adversarial negatives 的质性差异**：(1) APRM 的 harder negatives 是通过 adversarial perturbation 搜索出来的，模型学到的是"抵抗 adversarial pattern"，但这些 pattern 没有锚定到逻辑结构上，所以可能对新型 attack 仍然脆弱（Cat-and-mouse problem）；(2) PGCT 的 negatives 是锚定到 premise dependency 断裂上的，模型学到的是"检测逻辑因果链的完整性"，这是一个有明确语义的、transferable 的能力。**换言之：APRM 训练 PRM 对抗特定攻击，PGCT 训练 PRM 理解逻辑结构——后者的泛化性应当更强。** 这个论证如果写清楚，是 contribution statement 中最关键的差异化。
- **价值**: 命中 Novelty 和 Related Work 差异化。如果不回应这个 trivial alternative，审稿人很可能直接以"over-engineered compared to simpler adversarial training"为由 reject。
- **调研依据**: 直接参考 APRM (arXiv:2511.22888) 的方法和结果。

【发掘点 4】
- **维度**: related work 差异化
- **内容**: Proposal 遗漏了一篇高度相关的工作："Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation for Logical Reading Comprehension" (arXiv:2409.14495, EMNLP Findings 2024)。该工作**同样通过操纵 premise 结构构造 contrastive examples**，用于逻辑阅读理解任务。虽然领域不同（reading comprehension vs. math PRM），但技术思路有直接可比性——都是 premise-oriented contrastive augmentation。如果审稿人熟悉这篇工作，会质疑"这不就是把 Thought-Path Contrastive Learning 从 RC 搬到了 PRM 吗？" 建议主动引用并明确差异化：(1) Thought-Path 工作的"premise 操纵"是在自然语言逻辑题的前提-结论结构上做的，本质上是 propositional logic；PGCT 操纵的是 multi-step mathematical reasoning chains 的 dependency DAG，结构更复杂（DAG vs. 简单的前提-结论对）；(2) Thought-Path 的目标是提升 discriminative model 的 reading comprehension accuracy，PGCT 的目标是提升 PRM 的 robustness to reward hacking——问题设定完全不同；(3) PGCT 的 dual objective (step-correctness + InfoNCE) 设计是 Thought-Path 中没有的。
- **价值**: Related Work 差异化维度。主动引用和差异化远好于被审稿人发现遗漏——后者会严重损害论文的 scholarship 评价。
- **调研依据**: 直接参考 "Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation" (arXiv:2409.14495)。

【发掘点 5】
- **维度**: 核心 claim 强化
- **内容**: Proposal 当前将 InfoNCE loss over DAG-anchored step embeddings 描述为一个技术组件，但**没有强调这个设计选择的深层意义**。建议显式论证：标准 PRM training 的 step-correctness loss 只提供 **point-wise supervision**（每个步骤独立判断对错），而 InfoNCE over DAG-anchored embeddings 提供的是 **relational supervision**（步骤之间的逻辑关系结构被编码进表征空间）。这是一个从 point-wise → relational 的 supervision paradigm shift。CRM 通过 sequential conditioning 试图解决 credit assignment，但仍然是 point-wise prediction conditioned on history；PGCT 的 InfoNCE loss 直接在 representation space 中编码了步骤间的 structural relationship，这是更底层的改变。这个论证如果做好，可以将 dual objective 设计从"两个 loss 的简单组合"提升为"point-wise + relational supervision 互补"的有理论支撑的设计。
- **价值**: Novelty 维度。将 dual objective 从 engineering choice 提升为 principled design，增强审稿人对方法论深度的评价。
- **调研依据**: 参考 CRM (arXiv:2509.26578) 的 conditional sequential 建模思路作为对比，以及 "From Chains to DAGs" (arXiv:2601.17593) 关于 representation-level structure encoding 的发现。

---

Sources:
- [Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models](https://arxiv.org/abs/2603.06621)
- [Reward Models Identify Consistency, Not Causality](https://arxiv.org/pdf/2502.14619)
- [PARC/PERL: Premise-Augmented Reasoning Chains Improve Error Identification](https://arxiv.org/abs/2502.02362)
- [From Chains to DAGs: Probing the Graph Structure of Reasoning in LLMs](https://arxiv.org/abs/2601.17593)
- [Thought-Path Contrastive Learning via Premise-Oriented Data Augmentation](https://arxiv.org/pdf/2409.14495)
- [CPMI: Efficient Process Reward Modeling via Contrastive Mutual Information](https://arxiv.org/abs/2604.10660)
- [RewardFlow: Topology-Aware Reward Propagation on State Graphs](https://arxiv.org/abs/2603.18859)
- [Graph of Verification: Structured Verification of LLM Reasoning with DAGs](https://arxiv.org/abs/2506.12509)
- [CRM: Linking Process to Outcome: Conditional Reward Modeling](https://arxiv.org/abs/2509.26578)
- [APRM: Adversarial Training of Reward Models](https://arxiv.org/pdf/2504.06141)
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124)
- [PathFinder-PRM: Error Typing for Smarter Rewards](https://arxiv.org/pdf/2505.19706)
- [Neuro-Symbolic Contrastive Learning for Cross-domain Inference](https://arxiv.org/pdf/2502.09213)
- [InfoNCE is a Free Lunch for Semantically guided Graph Contrastive Learning](https://arxiv.org/abs/2505.06282)
- [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://arxiv.org/abs/2409.13156)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df594aad-e46a-4f41-9ac3-dc22e3f71b57",
  "isSidechain": false,
  "requestId": "req_011CbSkgmAmANDqpZA7kt2A8",
  "type": "assistant",
  "uuid": "31f6e199-a72c-4211-ae80-1560316bd5eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zPxLJYpeCaFAwj6DVDW9h",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 988,
      "cache_read_input_tokens": 28583,
      "output_tokens": 5982,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 988,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5982,
          "cache_read_input_tokens": 28583,
          "cache_creation_input_tokens": 988,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 988
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

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains ar…",
  "leafUuid": "31f6e199-a72c-4211-ae80-1560316bd5eb",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Premise-Graph Contrastive Training for Logic-Grounded Process Reward Models  ## Core Problem  Current process reward models confuse surface fluency with logical validity — 43% of PRM reward gains ar…",
  "leafUuid": "31f6e199-a72c-4211-ae80-1560316bd5eb",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Premise-graph contrastive training for process reward models",
  "sessionId": "21b9d1bb-97a5-4ae9-8693-da25a18e1ec9"
}
```

---
