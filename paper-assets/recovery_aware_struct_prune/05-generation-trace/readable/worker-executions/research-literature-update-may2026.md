# research literature update may2026

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 0
- **Tool calls:** 34
- **Original source:** `logs/workers/worker_research_literature_update_may2026_20260514T132612.log`
- **Structured JSON:** [`28ef6612988b1dce0715.json`](../../sessions/28/28ef6612988b1dce0715.json)

## Before a recorded user message

89 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "e309cc73-b75c-4631-8694-931005495457",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778782800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "aebd7e18-03a3-4a3e-bc92-0d766c938825",
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task into steps:

1. First, read the current literature_map.yaml to understand existing entries
2. Search arXiv for new papers using the specified keyword combinations
3. Evaluate found papers against existing entries
4. Add new relevant papers to literature_map.yaml
5. Write related_work_notes.md

Let me start by reading the current literature_map.yaml and searching for papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "7ce0009e-c894-477b-95da-c7cc37d59296",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSru5nPJe41eG7hoE6iZSF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11887,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11887
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

先读取现有 literature_map.yaml，同时启动文献搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "eb353c97-546c-4a6a-b7e0-09625af1239a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSru5nPJe41eG7hoE6iZSF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11887,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11887
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GTFsubNP3n3sZTxtFe7aP9`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,TodoWrite",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "7a00de5b-45d0-4664-a538-80c2dad93022",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MSru5nPJe41eG7hoE6iZSF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11887,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11887
      },
      "output_tokens": 31,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T13:26:26.851Z_

<details><summary>↩ Tool result · `toolu_01GTFsubNP3n3sZTxtFe7aP9`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "4d55f05a-a7bf-4152-ae08-9aebba732124",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__append_idea",
      "WebSearch",
      "TodoWrite"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__append_idea,WebSearch,TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the current literature_map.yaml and setting up the todo list, then launch the web searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "e53d731a-ff99-4675-9ae9-cc5c65427c44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZZjjSKQ6AWL7kEB7za6tP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 23728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3895
      },
      "output_tokens": 30,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_013c4Lb7SqdXwTFudkp5Pto2`</summary>

```json
{
  "todos": [
    {
      "content": "Read current literature_map.yaml",
      "status": "in_progress",
      "activeForm": "Reading current literature_map.yaml"
    },
    {
      "content": "Search arXiv for new papers (6 keyword groups)",
      "status": "pending",
      "activeForm": "Searching arXiv for new papers"
    },
    {
      "content": "Evaluate and add new papers to literature_map.yaml",
      "status": "pending",
      "activeForm": "Evaluating and adding new papers"
    },
    {
      "content": "Write related_work_notes.md",
      "status": "pending",
      "activeForm": "Writing related work notes"
    },
    {
      "content": "Register artifact",
      "status": "pending",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "60a530ff-07cc-41dd-90a2-b7824486345a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZZjjSKQ6AWL7kEB7za6tP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 23728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3895
      },
      "output_tokens": 30,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T13:26:32.986Z_

<details><summary>↩ Tool result · `toolu_013c4Lb7SqdXwTFudkp5Pto2`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "0028a6b5-bf3d-4a99-a548-67653fef0825",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "in_progress",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "pending",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "pending",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "pending",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Szhy2voKs22TKkTA3vsGVX`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "602e89da-406f-438c-9b77-dcb23687b19c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TZZjjSKQ6AWL7kEB7za6tP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3895,
      "cache_read_input_tokens": 23728,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3895
      },
      "output_tokens": 30,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T13:26:33.192Z_

<details><summary>↩ Tool result · `toolu_01Szhy2voKs22TKkTA3vsGVX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml\", \"content\": \"papers:\\n  # === Direct Competitors ===\\n  - id: self_healing_2025\\n    title: \\\"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\\\"\\n    year: 2025\\n    venue: \\\"under review\\\"\\n    category: direct-competitor\\n    role: \\\"RLVR recovery baseline\\\"\\n    relevance: 9\\n    key_finding: \\\"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%\\\"\\n    our_relation: \\\"We extend beyond single sparsity ratio and add CKA-guided pruning selection\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: resp_2025\\n    title: \\\"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\\\"\\n    year: 2025\\n    venue: \\\"arXiv Dec 2025\\\"\\n    category: direct-competitor\\n    role: \\\"Structured pruning for reasoning without recovery\\\"\\n    relevance: 8\\n    key_finding: \\\"GSM8K 81.3% at 40% sparsity via self-reflective importance\\\"\\n    our_relation: \\\"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: grasprune_2026\\n    title: \\\"GRASPrune: Global Gating-based Structural Pruning for LLMs\\\"\\n    year: 2026\\n    venue: \\\"ACL 2026 Main\\\"\\n    category: direct-competitor\\n    role: \\\"SOTA budgeted structural pruning\\\"\\n    relevance: 8\\n    key_finding: \\\"Global gating achieves best structured pruning under budget constraints\\\"\\n    our_relation: \\\"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: opsd_2026\\n    title: \\\"OPSD: One-shot Post-RL Structured Distillation\\\"\\n    year: 2026\\n    venue: \\\"arXiv May 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Post-RL compression via distillation\\\"\\n    relevance: 7\\n    key_finding: \\\"Compress post-RL model in one shot via structured distillation\\\"\\n    our_relation: \\\"Distillation-based vs our pruning+recovery approach; complementary\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: doing_more_with_less_2026\\n    title: \\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\"\\n    year: 2026\\n    venue: \\\"arXiv Apr 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Pruning improves test-time scaling\\\"\\n    relevance: 7\\n    key_finding: \\\"Unstructured pruning can augment test-time scaling; structured pruning degrades it\\\"\\n    our_relation: \\\"Motivates why structured pruning needs recovery; we address this gap with RLVR\\\"\\n    arxiv_id: \\\"2604.25098\\\"\\n\\n  - id: gprune_llm_2026\\n    title: \\\"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Cross-distribution generalization-aware pruning\\\"\\n    relevance: 6\\n    key_finding: \\\"Accounts for neuron cross-distribution behavior; reduces calibration bias\\\"\\n    our_relation: \\\"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\\\"\\n    arxiv_id: \\\"2603.13418\\\"\\n\\n  # === Method Components ===\\n  - id: mpruner_2024\\n    title: \\\"MPruner: CKA-based Inter-layer Pruning for LLMs\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    category: method-component\\n    role: \\\"CKA for layer importance estimation\\\"\\n    relevance: 8\\n    key_finding: \\\"CKA similarity between layers identifies redundant layers for removal\\\"\\n    our_relation: \\\"We adapt CKA from layer-level to width-level functional overlap prediction\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: lachance_thesis_2024\\n    title: \\\"CKA Layer Similarity for Neural Network Pruning\\\"\\n    year: 2024\\n    venue: \\\"URI Master's Thesis\\\"\\n    category: method-component\\n    role: \\\"CKA-based pruning theoretical foundation\\\"\\n    relevance: 6\\n    key_finding: \\\"CKA layer similarity correlates with pruning recoverability\\\"\\n    our_relation: \\\"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: bonsai_2025\\n    title: \\\"Bonsai: Gradient-Free Structured Pruning for LLMs\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: method-component\\n    role: \\\"Gradient-free structured pruning alternative\\\"\\n    relevance: 6\\n    key_finding: \\\"Achieves competitive structured pruning without backprop\\\"\\n    our_relation: \\\"Alternative pruning strategy; our CKA metric is also gradient-free\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: pat_2025\\n    title: \\\"PAT: Pruning-Aware Tuning for LLMs\\\"\\n    year: 2025\\n    venue: \\\"AAAI 2025\\\"\\n    category: method-component\\n    role: \\\"Joint pruning and tuning framework\\\"\\n    relevance: 6\\n    key_finding: \\\"Co-optimizing pruning mask and fine-tuning improves recovery\\\"\\n    our_relation: \\\"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: rac_2025\\n    title: \\\"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    category: method-component\\n    role: \\\"CoT reconstruction post-pruning\\\"\\n    relevance: 7\\n    key_finding: \\\"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\\\"\\n    our_relation: \\\"Complementary recovery strategy; could combine with our RLVR approach\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: paser_2025\\n    title: \\\"PASER: Data Selection for Pruning Recovery\\\"\\n    year: 2025\\n    venue: \\\"under review\\\"\\n    category: method-component\\n    role: \\\"Recovery training data selection\\\"\\n    relevance: 6\\n    key_finding: \\\"Selective data for recovery training improves efficiency\\\"\\n    our_relation: \\\"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  # === Background / Theory ===\\n  - id: rl_squeezes_2026\\n    title: \\\"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026 Poster\\\"\\n    category: background\\n    role: \\\"Theoretical basis for why RLVR works differently from SFT\\\"\\n    relevance: 8\\n    key_finding: \\\"RLVR compresses representation while SFT expands; different inductive biases\\\"\\n    our_relation: \\\"Explains why RLVR recovery succeeds where SFT fails post-pruning\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: from_llms_to_lrms_2026\\n    title: \\\"From LLMs to LRMs: Width Pruning is More Robust for Reasoning\\\"\\n    year: 2026\\n    venue: \\\"arXiv Jan 2026\\\"\\n    category: background\\n    role: \\\"Width vs depth pruning for reasoning\\\"\\n    relevance: 7\\n    key_finding: \\\"Width pruning preserves reasoning better than depth pruning\\\"\\n    our_relation: \\\"Motivates our focus on width-level structured pruning\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: p2_law_2025\\n    title: \\\"P² Law: Scaling Law for Pruning Recovery Training\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    category: background\\n    role: \\\"Theoretical scaling of recovery compute\\\"\\n    relevance: 7\\n    key_finding: \\\"Recovery training follows predictable scaling with compute and data\\\"\\n    our_relation: \\\"Informs our recovery budget estimation; we extend to RLVR-specific scaling\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: mipp_2024\\n    title: \\\"MIPP: Mutual Information Preserving Pruning\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    category: background\\n    role: \\\"Information-theoretic pruning criterion\\\"\\n    relevance: 5\\n    key_finding: \\\"Preserving mutual information between layers reduces pruning damage\\\"\\n    our_relation: \\\"Related theoretical motivation; CKA captures similar functional redundancy\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: redundancy_aware_cnn_2020\\n    title: \\\"Redundancy-Aware Pruning of Convolutional Neural Networks\\\"\\n    year: 2020\\n    venue: \\\"Neural Computation\\\"\\n    category: background\\n    role: \\\"Pioneer of redundancy-based pruning\\\"\\n    relevance: 4\\n    key_finding: \\\"Redundancy metrics guide pruning decisions in CNNs\\\"\\n    our_relation: \\\"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: self_distilled_rlvr_2026\\n    title: \\\"Self-Distilled RLVR\\\"\\n    year: 2026\\n    venue: \\\"arXiv Apr 2026\\\"\\n    category: background\\n    role: \\\"RLVR training efficiency improvement\\\"\\n    relevance: 5\\n    key_finding: \\\"Self-distillation stabilizes RLVR training and improves sample efficiency\\\"\\n    our_relation: \\\"Could improve our RLVR recovery phase efficiency\\\"\\n    arxiv_id: \\\"2604.03128\\\"\\n\\n  - id: diet_2026\\n    title: \\\"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: background\\n    role: \\\"Dimension-wise importance for width pruning\\\"\\n    relevance: 5\\n    key_finding: \\\"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\\\"\\n    our_relation: \\\"Alternative width importance metric; we use CKA overlap instead\\\"\\n    arxiv_id: \\\"2603.23985\\\"\\n\", \"total_chars\": 8275, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "56760694-432c-4b12-be87-5c957489f5ba",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  # === Direct Competitors ===\\\\n  - id: self_healing_2025\\\\n    title: \\\\\\\"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"under review\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: \\\\\\\"RLVR recovery baseline\\\\\\\"\\\\n    relevance: 9\\\\n    key_finding: \\\\\\\"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%\\\\\\\"\\\\n    our_relation: \\\\\\\"We extend beyond single sparsity ratio and add CKA-guided pruning selection\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: resp_2025\\\\n    title: \\\\\\\"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv Dec 2025\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: \\\\\\\"Structured pruning for reasoning without recovery\\\\\\\"\\\\n    relevance: 8\\\\n    key_finding: \\\\\\\"GSM8K 81.3% at 40% sparsity via self-reflective importance\\\\\\\"\\\\n    our_relation: \\\\\\\"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: grasprune_2026\\\\n    title: \\\\\\\"GRASPrune: Global Gating-based Structural Pruning for LLMs\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"ACL 2026 Main\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: \\\\\\\"SOTA budgeted structural pruning\\\\\\\"\\\\n    relevance: 8\\\\n    key_finding: \\\\\\\"Global gating achieves best structured pruning under budget constraints\\\\\\\"\\\\n    our_relation: \\\\\\\"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: opsd_2026\\\\n    title: \\\\\\\"OPSD: One-shot Post-RL Structured Distillation\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv May 2026\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: \\\\\\\"Post-RL compression via distillation\\\\\\\"\\\\n    relevance: 7\\\\n    key_finding: \\\\\\\"Compress post-RL model in one shot via structured distillation\\\\\\\"\\\\n    our_relation: \\\\\\\"Distillation-based vs our pruning+recovery approach; complementary\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: doing_more_with_less_2026\\\\n    title: \\\\\\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv Apr 2026\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: \\\\\\\"Pruning improves test-time scaling\\\\\\\"\\\\n    relevance: 7\\\\n    key_finding: \\\\\\\"Unstructured pruning can augment test-time scaling; structured pruning degrades it\\\\\\\"\\\\n    our_relation: \\\\\\\"Motivates why structured pruning needs recovery; we address this gap with RLVR\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2604.25098\\\\\\\"\\\\n\\\\n  - id: gprune_llm_2026\\\\n    title: \\\\\\\"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv Mar 2026\\\\\\\"\\\\n    category: direct-competitor\\\\n    role: \\\\\\\"Cross-distribution generalization-aware pruning\\\\\\\"\\\\n    relevance: 6\\\\n    key_finding: \\\\\\\"Accounts for neuron cross-distribution behavior; reduces calibration bias\\\\\\\"\\\\n    our_relation: \\\\\\\"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2603.13418\\\\\\\"\\\\n\\\\n  # === Method Components ===\\\\n  - id: mpruner_2024\\\\n    title: \\\\\\\"MPruner: CKA-based Inter-layer Pruning for LLMs\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"CKA for layer importance estimation\\\\\\\"\\\\n    relevance: 8\\\\n    key_finding: \\\\\\\"CKA similarity between layers identifies redundant layers for removal\\\\\\\"\\\\n    our_relation: \\\\\\\"We adapt CKA from layer-level to width-level functional overlap prediction\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: lachance_thesis_2024\\\\n    title: \\\\\\\"CKA Layer Similarity for Neural Network Pruning\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"URI Master's Thesis\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"CKA-based pruning theoretical foundation\\\\\\\"\\\\n    relevance: 6\\\\n    key_finding: \\\\\\\"CKA layer similarity correlates with pruning recoverability\\\\\\\"\\\\n    our_relation: \\\\\\\"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: bonsai_2025\\\\n    title: \\\\\\\"Bonsai: Gradient-Free Structured Pruning for LLMs\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Gradient-free structured pruning alternative\\\\\\\"\\\\n    relevance: 6\\\\n    key_finding: \\\\\\\"Achieves competitive structured pruning without backprop\\\\\\\"\\\\n    our_relation: \\\\\\\"Alternative pruning strategy; our CKA metric is also gradient-free\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: pat_2025\\\\n    title: \\\\\\\"PAT: Pruning-Aware Tuning for LLMs\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"AAAI 2025\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Joint pruning and tuning framework\\\\\\\"\\\\n    relevance: 6\\\\n    key_finding: \\\\\\\"Co-optimizing pruning mask and fine-tuning improves recovery\\\\\\\"\\\\n    our_relation: \\\\\\\"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: rac_2025\\\\n    title: \\\\\\\"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"CoT reconstruction post-pruning\\\\\\\"\\\\n    relevance: 7\\\\n    key_finding: \\\\\\\"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\\\\\\\"\\\\n    our_relation: \\\\\\\"Complementary recovery strategy; could combine with our RLVR approach\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: paser_2025\\\\n    title: \\\\\\\"PASER: Data Selection for Pruning Recovery\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"under review\\\\\\\"\\\\n    category: method-component\\\\n    role: \\\\\\\"Recovery training data selection\\\\\\\"\\\\n    relevance: 6\\\\n    key_finding: \\\\\\\"Selective data for recovery training improves efficiency\\\\\\\"\\\\n    our_relation: \\\\\\\"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  # === Background / Theory ===\\\\n  - id: rl_squeezes_2026\\\\n    title: \\\\\\\"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"ICLR 2026 Poster\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Theoretical basis for why RLVR works differently from SFT\\\\\\\"\\\\n    relevance: 8\\\\n    key_finding: \\\\\\\"RLVR compresses representation while SFT expands; different inductive biases\\\\\\\"\\\\n    our_relation: \\\\\\\"Explains why RLVR recovery succeeds where SFT fails post-pruning\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: from_llms_to_lrms_2026\\\\n    title: \\\\\\\"From LLMs to LRMs: Width Pruning is More Robust for Reasoning\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv Jan 2026\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Width vs depth pruning for reasoning\\\\\\\"\\\\n    relevance: 7\\\\n    key_finding: \\\\\\\"Width pruning preserves reasoning better than depth pruning\\\\\\\"\\\\n    our_relation: \\\\\\\"Motivates our focus on width-level structured pruning\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: p2_law_2025\\\\n    title: \\\\\\\"P² Law: Scaling Law for Pruning Recovery Training\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ACL 2025\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Theoretical scaling of recovery compute\\\\\\\"\\\\n    relevance: 7\\\\n    key_finding: \\\\\\\"Recovery training follows predictable scaling with compute and data\\\\\\\"\\\\n    our_relation: \\\\\\\"Informs our recovery budget estimation; we extend to RLVR-specific scaling\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: mipp_2024\\\\n    title: \\\\\\\"MIPP: Mutual Information Preserving Pruning\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Information-theoretic pruning criterion\\\\\\\"\\\\n    relevance: 5\\\\n    key_finding: \\\\\\\"Preserving mutual information between layers reduces pruning damage\\\\\\\"\\\\n    our_relation: \\\\\\\"Related theoretical motivation; CKA captures similar functional redundancy\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: redundancy_aware_cnn_2020\\\\n    title: \\\\\\\"Redundancy-Aware Pruning of Convolutional Neural Networks\\\\\\\"\\\\n    year: 2020\\\\n    venue: \\\\\\\"Neural Computation\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Pioneer of redundancy-based pruning\\\\\\\"\\\\n    relevance: 4\\\\n    key_finding: \\\\\\\"Redundancy metrics guide pruning decisions in CNNs\\\\\\\"\\\\n    our_relation: \\\\\\\"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\\\\\\\"\\\\n    arxiv_id: \\\\\\\"\\\\\\\"\\\\n\\\\n  - id: self_distilled_rlvr_2026\\\\n    title: \\\\\\\"Self-Distilled RLVR\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv Apr 2026\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"RLVR training efficiency improvement\\\\\\\"\\\\n    relevance: 5\\\\n    key_finding: \\\\\\\"Self-distillation stabilizes RLVR training and improves sample efficiency\\\\\\\"\\\\n    our_relation: \\\\\\\"Could improve our RLVR recovery phase efficiency\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2604.03128\\\\\\\"\\\\n\\\\n  - id: diet_2026\\\\n    title: \\\\\\\"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv Mar 2026\\\\\\\"\\\\n    category: background\\\\n    role: \\\\\\\"Dimension-wise importance for width pruning\\\\\\\"\\\\n    relevance: 5\\\\n    key_finding: \\\\\\\"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\\\\\\\"\\\\n    our_relation: \\\\\\\"Alternative width importance metric; we use CKA overlap instead\\\\\\\"\\\\n    arxiv_id: \\\\\\\"2603.23985\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 8275, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml\", \"content\": \"papers:\\n  # === Direct Competitors ===\\n  - id: self_healing_2025\\n    title: \\\"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\\\"\\n    year: 2025\\n    venue: \\\"under review\\\"\\n    category: direct-competitor\\n    role: \\\"RLVR recovery baseline\\\"\\n    relevance: 9\\n    key_finding: \\\"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%\\\"\\n    our_relation: \\\"We extend beyond single sparsity ratio and add CKA-guided pruning selection\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: resp_2025\\n    title: \\\"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\\\"\\n    year: 2025\\n    venue: \\\"arXiv Dec 2025\\\"\\n    category: direct-competitor\\n    role: \\\"Structured pruning for reasoning without recovery\\\"\\n    relevance: 8\\n    key_finding: \\\"GSM8K 81.3% at 40% sparsity via self-reflective importance\\\"\\n    our_relation: \\\"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: grasprune_2026\\n    title: \\\"GRASPrune: Global Gating-based Structural Pruning for LLMs\\\"\\n    year: 2026\\n    venue: \\\"ACL 2026 Main\\\"\\n    category: direct-competitor\\n    role: \\\"SOTA budgeted structural pruning\\\"\\n    relevance: 8\\n    key_finding: \\\"Global gating achieves best structured pruning under budget constraints\\\"\\n    our_relation: \\\"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: opsd_2026\\n    title: \\\"OPSD: One-shot Post-RL Structured Distillation\\\"\\n    year: 2026\\n    venue: \\\"arXiv May 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Post-RL compression via distillation\\\"\\n    relevance: 7\\n    key_finding: \\\"Compress post-RL model in one shot via structured distillation\\\"\\n    our_relation: \\\"Distillation-based vs our pruning+recovery approach; complementary\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: doing_more_with_less_2026\\n    title: \\\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\\\"\\n    year: 2026\\n    venue: \\\"arXiv Apr 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Pruning improves test-time scaling\\\"\\n    relevance: 7\\n    key_finding: \\\"Unstructured pruning can augment test-time scaling; structured pruning degrades it\\\"\\n    our_relation: \\\"Motivates why structured pruning needs recovery; we address this gap with RLVR\\\"\\n    arxiv_id: \\\"2604.25098\\\"\\n\\n  - id: gprune_llm_2026\\n    title: \\\"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: direct-competitor\\n    role: \\\"Cross-distribution generalization-aware pruning\\\"\\n    relevance: 6\\n    key_finding: \\\"Accounts for neuron cross-distribution behavior; reduces calibration bias\\\"\\n    our_relation: \\\"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\\\"\\n    arxiv_id: \\\"2603.13418\\\"\\n\\n  # === Method Components ===\\n  - id: mpruner_2024\\n    title: \\\"MPruner: CKA-based Inter-layer Pruning for LLMs\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    category: method-component\\n    role: \\\"CKA for layer importance estimation\\\"\\n    relevance: 8\\n    key_finding: \\\"CKA similarity between layers identifies redundant layers for removal\\\"\\n    our_relation: \\\"We adapt CKA from layer-level to width-level functional overlap prediction\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: lachance_thesis_2024\\n    title: \\\"CKA Layer Similarity for Neural Network Pruning\\\"\\n    year: 2024\\n    venue: \\\"URI Master's Thesis\\\"\\n    category: method-component\\n    role: \\\"CKA-based pruning theoretical foundation\\\"\\n    relevance: 6\\n    key_finding: \\\"CKA layer similarity correlates with pruning recoverability\\\"\\n    our_relation: \\\"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: bonsai_2025\\n    title: \\\"Bonsai: Gradient-Free Structured Pruning for LLMs\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025\\\"\\n    category: method-component\\n    role: \\\"Gradient-free structured pruning alternative\\\"\\n    relevance: 6\\n    key_finding: \\\"Achieves competitive structured pruning without backprop\\\"\\n    our_relation: \\\"Alternative pruning strategy; our CKA metric is also gradient-free\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: pat_2025\\n    title: \\\"PAT: Pruning-Aware Tuning for LLMs\\\"\\n    year: 2025\\n    venue: \\\"AAAI 2025\\\"\\n    category: method-component\\n    role: \\\"Joint pruning and tuning framework\\\"\\n    relevance: 6\\n    key_finding: \\\"Co-optimizing pruning mask and fine-tuning improves recovery\\\"\\n    our_relation: \\\"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: rac_2025\\n    title: \\\"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    category: method-component\\n    role: \\\"CoT reconstruction post-pruning\\\"\\n    relevance: 7\\n    key_finding: \\\"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\\\"\\n    our_relation: \\\"Complementary recovery strategy; could combine with our RLVR approach\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: paser_2025\\n    title: \\\"PASER: Data Selection for Pruning Recovery\\\"\\n    year: 2025\\n    venue: \\\"under review\\\"\\n    category: method-component\\n    role: \\\"Recovery training data selection\\\"\\n    relevance: 6\\n    key_finding: \\\"Selective data for recovery training improves efficiency\\\"\\n    our_relation: \\\"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  # === Background / Theory ===\\n  - id: rl_squeezes_2026\\n    title: \\\"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\\\"\\n    year: 2026\\n    venue: \\\"ICLR 2026 Poster\\\"\\n    category: background\\n    role: \\\"Theoretical basis for why RLVR works differently from SFT\\\"\\n    relevance: 8\\n    key_finding: \\\"RLVR compresses representation while SFT expands; different inductive biases\\\"\\n    our_relation: \\\"Explains why RLVR recovery succeeds where SFT fails post-pruning\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: from_llms_to_lrms_2026\\n    title: \\\"From LLMs to LRMs: Width Pruning is More Robust for Reasoning\\\"\\n    year: 2026\\n    venue: \\\"arXiv Jan 2026\\\"\\n    category: background\\n    role: \\\"Width vs depth pruning for reasoning\\\"\\n    relevance: 7\\n    key_finding: \\\"Width pruning preserves reasoning better than depth pruning\\\"\\n    our_relation: \\\"Motivates our focus on width-level structured pruning\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: p2_law_2025\\n    title: \\\"P² Law: Scaling Law for Pruning Recovery Training\\\"\\n    year: 2025\\n    venue: \\\"ACL 2025\\\"\\n    category: background\\n    role: \\\"Theoretical scaling of recovery compute\\\"\\n    relevance: 7\\n    key_finding: \\\"Recovery training follows predictable scaling with compute and data\\\"\\n    our_relation: \\\"Informs our recovery budget estimation; we extend to RLVR-specific scaling\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: mipp_2024\\n    title: \\\"MIPP: Mutual Information Preserving Pruning\\\"\\n    year: 2024\\n    venue: \\\"arXiv\\\"\\n    category: background\\n    role: \\\"Information-theoretic pruning criterion\\\"\\n    relevance: 5\\n    key_finding: \\\"Preserving mutual information between layers reduces pruning damage\\\"\\n    our_relation: \\\"Related theoretical motivation; CKA captures similar functional redundancy\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: redundancy_aware_cnn_2020\\n    title: \\\"Redundancy-Aware Pruning of Convolutional Neural Networks\\\"\\n    year: 2020\\n    venue: \\\"Neural Computation\\\"\\n    category: background\\n    role: \\\"Pioneer of redundancy-based pruning\\\"\\n    relevance: 4\\n    key_finding: \\\"Redundancy metrics guide pruning decisions in CNNs\\\"\\n    our_relation: \\\"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\\\"\\n    arxiv_id: \\\"\\\"\\n\\n  - id: self_distilled_rlvr_2026\\n    title: \\\"Self-Distilled RLVR\\\"\\n    year: 2026\\n    venue: \\\"arXiv Apr 2026\\\"\\n    category: background\\n    role: \\\"RLVR training efficiency improvement\\\"\\n    relevance: 5\\n    key_finding: \\\"Self-distillation stabilizes RLVR training and improves sample efficiency\\\"\\n    our_relation: \\\"Could improve our RLVR recovery phase efficiency\\\"\\n    arxiv_id: \\\"2604.03128\\\"\\n\\n  - id: diet_2026\\n    title: \\\"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\\\"\\n    year: 2026\\n    venue: \\\"arXiv Mar 2026\\\"\\n    category: background\\n    role: \\\"Dimension-wise importance for width pruning\\\"\\n    relevance: 5\\n    key_finding: \\\"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\\\"\\n    our_relation: \\\"Alternative width importance metric; we use CKA overlap instead\\\"\\n    arxiv_id: \\\"2603.23985\\\"\\n\", \"total_chars\": 8275, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the full literature_map.yaml. Now let me launch the 6 keyword group searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "88b3535c-9694-4df9-a9ae-9bae2c1d60cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 14_

已读取 19 篇现有论文。开始 6 组关键词搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "b0264156-48b4-465f-aad9-aafe73bdc611",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_018F2WMpBWMgwP5ZeoartDX4`</summary>

```json
{
  "todos": [
    {
      "content": "Read current literature_map.yaml",
      "status": "completed",
      "activeForm": "Reading current literature_map.yaml"
    },
    {
      "content": "Search arXiv for new papers (6 keyword groups)",
      "status": "in_progress",
      "activeForm": "Searching arXiv for new papers"
    },
    {
      "content": "Evaluate and add new papers to literature_map.yaml",
      "status": "pending",
      "activeForm": "Evaluating and adding new papers"
    },
    {
      "content": "Write related_work_notes.md",
      "status": "pending",
      "activeForm": "Writing related work notes"
    },
    {
      "content": "Register artifact",
      "status": "pending",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "13c61f27-e061-4990-b221-f32a67232203",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T13:26:38.280Z_

<details><summary>↩ Tool result · `toolu_018F2WMpBWMgwP5ZeoartDX4`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "eba92903-eafe-4b9b-ae5a-1e5386f203d3",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "in_progress",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "pending",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "pending",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "pending",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "in_progress",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "pending",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "pending",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MMnJsJwMcb82V2y4ijnjRm`</summary>

```json
{
  "query": "arxiv 2026 \"structured pruning\" reasoning LLM",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com",
    "semanticscholar.org",
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "72d71fff-42ee-4313-869a-1c74115d5f44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011jbmT4CkaDKzs82CDp7HnK`</summary>

```json
{
  "query": "arxiv 2026 RLVR pruning OR compression language model",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com",
    "semanticscholar.org",
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "ef325f89-2b80-4de0-956c-0a175e973852",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019gP8fKm37t8Yw9CFGb8E4f`</summary>

```json
{
  "query": "arxiv 2024 2025 2026 CKA pruning neural network",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com",
    "semanticscholar.org",
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "1643ffff-4ade-4ae0-ab77-bdb2b8ba3d0e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PiwQTwKikfo3PhAsyRHJRP`</summary>

```json
{
  "query": "arxiv 2025 2026 \"recovery\" \"structured pruning\" language model",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com",
    "semanticscholar.org",
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "94a24200-962d-4cb0-aeb0-92af11b2cc5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NG6Z5pVKijzA4UjLqfdS2x`</summary>

```json
{
  "query": "arxiv 2026 GRPO pruning OR compression LLM",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com",
    "semanticscholar.org",
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "908c9c08-7944-4f26-b871-a4380ebb42bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S8fX4oXTVuDAkFEwPpxCtt`</summary>

```json
{
  "query": "arxiv 2026 \"test-time compute\" pruning language model",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com",
    "semanticscholar.org",
    "huggingface.co"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "fcc42bff-f072-4634-89fa-2e6d2a218a05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ESZ4xgKAX1ZtVyrTJrgfgK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3820,
      "cache_read_input_tokens": 27623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3820
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T13:26:46.879Z_

<details><summary>↩ Tool result · `toolu_01MMnJsJwMcb82V2y4ijnjRm`</summary>

```text
Web search results for query: "arxiv 2026 "structured pruning" reasoning LLM"

Links: [{"title":"STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/html/2605.13165"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/pdf/2603.13418"},{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"[2603.13418] GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.13418"},{"title":"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/html/2604.25098"},{"title":"[2603.08065] Deterministic Differentiable Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.08065"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"[2305.11627] LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://arxiv.org/abs/2305.11627"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models Xinyin Ma","url":"https://arxiv.org/pdf/2305.11627"}]

I found several recent arxiv papers (from 2026) related to structured pruning and reasoning LLMs. Here are the key results:

## Recent Papers on Structured Pruning for Reasoning LLMs

1. **STOP: Structured On-Policy Pruning** - This paper uses structured reasoning interfaces and annotation, segmenting traces into semantically coherent reasoning nodes using discourse and formatting rules.

2. **GPrune-LLM: Generalization-Aware Structured Pruning** - Structured pruning is widely used to compress LLMs, yet its effectiveness depends heavily on neuron importance estimation, and most existing methods estimate neuron importance from activation statistics on a single calibration dataset, which introduces calibration bias and degrades downstream cross-task generalization. The paper proposes GPrune-LLM, a generalization-aware structured pruning framework that explicitly accounts for neuron differences in cross-distribution behavior.

3. **Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling** - Specific to reasoning LLMs, prior work has shown that structured pruning (methods which removes entire set of layer blocks), significantly degrades TTS reasoning performance. However, extensive experiments across four reasoning benchmarks on two reasoning LLMs: s1.1-7B and Qwen3-8B, consistently show that unstructured pruning augments TTS performance compared to structured pruning.

4. **Deterministic Differentiable Structured Pruning** - Structured pruning reduces LLM inference cost by removing low-importance architectural components, which can be viewed as learning a multiplicative gate for each component under an l0 sparsity constraint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "46120459-cc85-45b2-bb00-0e04fcaa3a4b",
  "tool_use_result": {
    "query": "arxiv 2026 \"structured pruning\" reasoning LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01E6WXd24NwiXo64Kq2KQYC9",
        "content": [
          {
            "title": "STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes",
            "url": "https://arxiv.org/html/2605.13165"
          },
          {
            "title": "GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/pdf/2603.13418"
          },
          {
            "title": "[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling",
            "url": "https://arxiv.org/abs/2604.25098"
          },
          {
            "title": "Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
            "url": "https://arxiv.org/html/2604.24380"
          },
          {
            "title": "[2603.13418] GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/abs/2603.13418"
          },
          {
            "title": "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling",
            "url": "https://arxiv.org/html/2604.25098"
          },
          {
            "title": "[2603.08065] Deterministic Differentiable Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/abs/2603.08065"
          },
          {
            "title": "Pruning Large Language Models by Identifying and Preserving Functional Networks",
            "url": "https://arxiv.org/html/2508.05239v1"
          },
          {
            "title": "[2305.11627] LLM-Pruner: On the Structural Pruning of Large Language Models",
            "url": "https://arxiv.org/abs/2305.11627"
          },
          {
            "title": "LLM-Pruner: On the Structural Pruning of Large Language Models Xinyin Ma",
            "url": "https://arxiv.org/pdf/2305.11627"
          }
        ]
      },
      "I found several recent arxiv papers (from 2026) related to structured pruning and reasoning LLMs. Here are the key results:\n\n## Recent Papers on Structured Pruning for Reasoning LLMs\n\n1. **STOP: Structured On-Policy Pruning** - This paper uses structured reasoning interfaces and annotation, segmenting traces into semantically coherent reasoning nodes using discourse and formatting rules.\n\n2. **GPrune-LLM: Generalization-Aware Structured Pruning** - Structured pruning is widely used to compress LLMs, yet its effectiveness depends heavily on neuron importance estimation, and most existing methods estimate neuron importance from activation statistics on a single calibration dataset, which introduces calibration bias and degrades downstream cross-task generalization. The paper proposes GPrune-LLM, a generalization-aware structured pruning framework that explicitly accounts for neuron differences in cross-distribution behavior.\n\n3. **Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling** - Specific to reasoning LLMs, prior work has shown that structured pruning (methods which removes entire set of layer blocks), significantly degrades TTS reasoning performance. However, extensive experiments across four reasoning benchmarks on two reasoning LLMs: s1.1-7B and Qwen3-8B, consistently show that unstructured pruning augments TTS performance compared to structured pruning.\n\n4. **Deterministic Differentiable Structured Pruning** - Structured pruning reduces LLM inference cost by removing low-importance architectural components, which can be viewed as learning a multiplicative gate for each component under an l0 sparsity constraint."
    ],
    "durationSeconds": 7.647860166999999
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T13:26:47.423Z_

<details><summary>↩ Tool result · `toolu_019gP8fKm37t8Yw9CFGb8E4f`</summary>

```text
Web search results for query: "arxiv 2024 2025 2026 CKA pruning neural network"

Links: [{"title":"MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning","url":"https://arxiv.org/html/2408.13482v1"},{"title":"[2408.13482] MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning","url":"https://arxiv.org/abs/2408.13482"},{"title":"arXiv:2506.04513v1 [cs.CV] 4 Jun 2025","url":"https://arxiv.org/pdf/2506.04513"},{"title":"A Survey on Deep Neural Network Pruning","url":"https://arxiv.org/pdf/2308.06767"},{"title":"Integrating Pruning with Quantization for Efficient Deep Neural Networks Compression","url":"https://arxiv.org/html/2509.04244v1"},{"title":"Enhanced Pruning Strategy for Multi-Component Neural Architectures","url":"https://arxiv.org/pdf/2504.13296"},{"title":"A Paradigm for Density Discovery in Sparse Neural Networks","url":"https://arxiv.org/pdf/2509.25665"},{"title":"[2101.09671] Pruning and Quantization for Deep Neural Network Acceleration: A Survey","url":"https://arxiv.org/abs/2101.09671"},{"title":"Pruning vs Quantization: Which is Better?","url":"https://arxiv.org/pdf/2307.02973"},{"title":"Pruning and Quantization Impact on Graph Neural Networks","url":"https://arxiv.org/html/2510.22058v1"}]

I found several relevant papers on arXiv related to CKA-based pruning of neural networks. Here are the key findings:

## Recent CKA-Based Pruning Research

**1. MPruner (2024)**
MPruner utilizes layer clustering with the Centered Kernel Alignment (CKA) similarity metric, allowing incorporation of global information from the neural network for more precise and efficient layer-wise pruning. MPruner achieved up to a 50% reduction in parameters and memory usage for CNN and transformer-based models, with minimal to no loss in accuracy.

**2. CKA-Based Pruning Strategy (2025)**
A more recent paper from June 2025 describes using Centered Kernel Alignment (CKA) as a similarity metric to evaluate resulting subnetworks to determine and select the one that better preserves the representation of its parent. On ResNet56 and ResNet110, the approach achieves a milestone of 86.37% and 95.82% FLOPs reduction.

**3. Representation Comparison Studies**
Research also shows that for pruning, the representations tend to become closer to the original representation during fine-tuning, as measured by CKA distance.

These recent papers demonstrate the growing use of CKA as a metric for evaluating and guiding neural network pruning decisions, particularly for achieving high compression rates while maintaining model performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "b6d74c99-0019-4cef-9ae4-a1ef8760f04e",
  "tool_use_result": {
    "query": "arxiv 2024 2025 2026 CKA pruning neural network",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LcUGWhUGnBns277f329ZMD",
        "content": [
          {
            "title": "MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning",
            "url": "https://arxiv.org/html/2408.13482v1"
          },
          {
            "title": "[2408.13482] MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning",
            "url": "https://arxiv.org/abs/2408.13482"
          },
          {
            "title": "arXiv:2506.04513v1 [cs.CV] 4 Jun 2025",
            "url": "https://arxiv.org/pdf/2506.04513"
          },
          {
            "title": "A Survey on Deep Neural Network Pruning",
            "url": "https://arxiv.org/pdf/2308.06767"
          },
          {
            "title": "Integrating Pruning with Quantization for Efficient Deep Neural Networks Compression",
            "url": "https://arxiv.org/html/2509.04244v1"
          },
          {
            "title": "Enhanced Pruning Strategy for Multi-Component Neural Architectures",
            "url": "https://arxiv.org/pdf/2504.13296"
          },
          {
            "title": "A Paradigm for Density Discovery in Sparse Neural Networks",
            "url": "https://arxiv.org/pdf/2509.25665"
          },
          {
            "title": "[2101.09671] Pruning and Quantization for Deep Neural Network Acceleration: A Survey",
            "url": "https://arxiv.org/abs/2101.09671"
          },
          {
            "title": "Pruning vs Quantization: Which is Better?",
            "url": "https://arxiv.org/pdf/2307.02973"
          },
          {
            "title": "Pruning and Quantization Impact on Graph Neural Networks",
            "url": "https://arxiv.org/html/2510.22058v1"
          }
        ]
      },
      "I found several relevant papers on arXiv related to CKA-based pruning of neural networks. Here are the key findings:\n\n## Recent CKA-Based Pruning Research\n\n**1. MPruner (2024)**\nMPruner utilizes layer clustering with the Centered Kernel Alignment (CKA) similarity metric, allowing incorporation of global information from the neural network for more precise and efficient layer-wise pruning. MPruner achieved up to a 50% reduction in parameters and memory usage for CNN and transformer-based models, with minimal to no loss in accuracy.\n\n**2. CKA-Based Pruning Strategy (2025)**\nA more recent paper from June 2025 describes using Centered Kernel Alignment (CKA) as a similarity metric to evaluate resulting subnetworks to determine and select the one that better preserves the representation of its parent. On ResNet56 and ResNet110, the approach achieves a milestone of 86.37% and 95.82% FLOPs reduction.\n\n**3. Representation Comparison Studies**\nResearch also shows that for pruning, the representations tend to become closer to the original representation during fine-tuning, as measured by CKA distance.\n\nThese recent papers demonstrate the growing use of CKA as a metric for evaluating and guiding neural network pruning decisions, particularly for achieving high compression rates while maintaining model performance."
    ],
    "durationSeconds": 6.306712934000003
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T13:26:47.869Z_

<details><summary>↩ Tool result · `toolu_011jbmT4CkaDKzs82CDp7HnK`</summary>

```text
Web search results for query: "arxiv 2026 RLVR pruning OR compression language model"

Links: [{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130"},{"title":"UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation","url":"https://arxiv.org/html/2602.09130"},{"title":"[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/abs/2604.24380"},{"title":"[2601.09694] LLMs can Compress LLMs: Adaptive Pruning by Agents","url":"https://arxiv.org/abs/2601.09694"},{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/abs/2603.24840"},{"title":"[2602.09130v2] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation","url":"https://arxiv.org/abs/2602.09130v2"},{"title":"LLMs can Compress LLMs: Adaptive Pruning by Agents","url":"https://arxiv.org/pdf/2601.09694"},{"title":"One-for-All Pruning: A Universal Model for Customized Compression of Large Language Models","url":"https://arxiv.org/html/2505.12216"}]

The web search has returned several relevant results about language model compression, pruning, and related techniques from 2026. Here are the key findings:

## Main Results

**RLVR-related paper:**
A paper titled "Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR" introduces arrol (Accelerating RLVR via online Rollout Pruning), an online rollout pruning method that prunes rollouts during generation while explicitly steering the surviving ones more correctness-balanced to enhance learning signals.

**Compression Evaluation:**
UniComp evaluates compressed models along three dimensions: performance, reliability, and efficiency, and through evaluation of six compression techniques across 40 datasets, observes a consistent knowledge bias, where factual recall is largely preserved while multi-step reasoning, multilingual, and instruction-following capabilities degrade, and that task-specific calibration can yield up to 50% relative improvement of reasoning performance in pruned models.

**Other Notable Work:**
Agent-guided pruning introduces a method where a foundation model acts as an adaptive pruning agent to intelligently select which layers to prune at each iteration while preserving critical knowledge pathways.

A method called CAP uses RPCA to decompose each weight matrix into low-rank and sparse components, and subsequently prunes these components in a probabilistic manner, without heuristic thresholds or backpropagation through the original LLM weights.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "0450bbf7-b50a-409f-8053-63599dea6d62",
  "tool_use_result": {
    "query": "arxiv 2026 RLVR pruning OR compression language model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CZL47ewWAQWxG9NpwS8bTa",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION",
            "url": "https://arxiv.org/pdf/2505.03801"
          },
          {
            "title": "[2602.09130] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation",
            "url": "https://arxiv.org/abs/2602.09130"
          },
          {
            "title": "UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization, and Distillation",
            "url": "https://arxiv.org/html/2602.09130"
          },
          {
            "title": "[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
            "url": "https://arxiv.org/abs/2604.24380"
          },
          {
            "title": "[2601.09694] LLMs can Compress LLMs: Adaptive Pruning by Agents",
            "url": "https://arxiv.org/abs/2601.09694"
          },
          {
            "title": "Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
            "url": "https://arxiv.org/html/2604.24380"
          },
          {
            "title": "[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR",
            "url": "https://arxiv.org/abs/2603.24840"
          },
          {
            "title": "[2602.09130v2] UniComp: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation",
            "url": "https://arxiv.org/abs/2602.09130v2"
          },
          {
            "title": "LLMs can Compress LLMs: Adaptive Pruning by Agents",
            "url": "https://arxiv.org/pdf/2601.09694"
          },
          {
            "title": "One-for-All Pruning: A Universal Model for Customized Compression of Large Language Models",
            "url": "https://arxiv.org/html/2505.12216"
          }
        ]
      },
      "The web search has returned several relevant results about language model compression, pruning, and related techniques from 2026. Here are the key findings:\n\n## Main Results\n\n**RLVR-related paper:**\nA paper titled \"Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR\" introduces arrol (Accelerating RLVR via online Rollout Pruning), an online rollout pruning method that prunes rollouts during generation while explicitly steering the surviving ones more correctness-balanced to enhance learning signals.\n\n**Compression Evaluation:**\nUniComp evaluates compressed models along three dimensions: performance, reliability, and efficiency, and through evaluation of six compression techniques across 40 datasets, observes a consistent knowledge bias, where factual recall is largely preserved while multi-step reasoning, multilingual, and instruction-following capabilities degrade, and that task-specific calibration can yield up to 50% relative improvement of reasoning performance in pruned models.\n\n**Other Notable Work:**\nAgent-guided pruning introduces a method where a foundation model acts as an adaptive pruning agent to intelligently select which layers to prune at each iteration while preserving critical knowledge pathways.\n\nA method called CAP uses RPCA to decompose each weight matrix into low-rank and sparse components, and subsequently prunes these components in a probabilistic manner, without heuristic thresholds or backpropagation through the original LLM weights."
    ],
    "durationSeconds": 7.696014526999999
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T13:26:49.512Z_

<details><summary>↩ Tool result · `toolu_01PiwQTwKikfo3PhAsyRHJRP`</summary>

```text
Web search results for query: "arxiv 2025 2026 "recovery" "structured pruning" language model"

Links: [{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/abs/2604.24380"},{"title":"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression","url":"https://arxiv.org/html/2509.14230v1"},{"title":"From Local to Global: Revisiting Structured Pruning Paradigms for Large Language Models","url":"https://arxiv.org/html/2510.18030"},{"title":"[2505.22689] SlimLLM: Accurate Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2505.22689"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"[2507.20749] Investigating Structural Pruning and Recovery Techniques for Compressing Multimodal Large Language Models: An Empirical Study","url":"https://arxiv.org/abs/2507.20749"},{"title":"Investigating Structural Pruning and Recovery Techniques ...","url":"https://arxiv.org/pdf/2507.20749"},{"title":"[2510.07782] RCPU: Rotation-Constrained Error Compensation for Structured Pruning of Large Language Models","url":"https://arxiv.org/abs/2510.07782"},{"title":"Deterministic Differentiable Structured Pruning for Large Language Models","url":"https://arxiv.org/html/2603.08065"}]

Based on the search results, I found several recent arXiv papers (2025-2026) on structured pruning of language models with a focus on recovery techniques:

## Key Papers Found:

1. **Structural Pruning of Large Vision Language Models** - Published April 27, 2026 (arxiv 2604.24380), this comprehensive study investigates layerwise and widthwise pruning paired with supervised finetuning and knowledge distillation. The paper examines recovery methods including knowledge distillation which allows the pruned model to regain lost performance by mimicking the decision-making process of the more capable teacher.

2. **NIRVANA: Structured Pruning Reimagined** - Evaluated on Llama3.1-8B, Llama3.2-3B, Qwen2.5-7B, and T5-base, with both zero-shot results and performance after recovery fine-tuning reported.

3. **SlimLLM: Accurate Structured Pruning** - Proposes an effective structured pruning method and designs a simple linear regression strategy for the output matrix to quickly recover performance.

4. **RCPU: Rotation-Constrained Error Compensation** - Updated February 26, 2026, proposes a rotation-constrained compensation method to address errors introduced by structured pruning of LLMs.

5. **Deterministic Differentiable Structured Pruning** - A lightweight mask-only structured pruning framework that learns structured sparsity patterns via gradient-based optimization.

These papers represent the latest research on combining structured pruning techniques with various recovery and compensation methods for language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "5c63103c-f5ce-45ae-a339-af9cfc85bce5",
  "tool_use_result": {
    "query": "arxiv 2025 2026 \"recovery\" \"structured pruning\" language model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Movz72TwFnVfZhuSvNU3tw",
        "content": [
          {
            "title": "Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
            "url": "https://arxiv.org/html/2604.24380"
          },
          {
            "title": "[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
            "url": "https://arxiv.org/abs/2604.24380"
          },
          {
            "title": "NIRVANA: Structured Pruning Reimagined for Large Language Models Compression",
            "url": "https://arxiv.org/html/2509.14230v1"
          },
          {
            "title": "From Local to Global: Revisiting Structured Pruning Paradigms for Large Language Models",
            "url": "https://arxiv.org/html/2510.18030"
          },
          {
            "title": "[2505.22689] SlimLLM: Accurate Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/abs/2505.22689"
          },
          {
            "title": "Pruning Large Language Models by Identifying and Preserving Functional Networks",
            "url": "https://arxiv.org/html/2508.05239v1"
          },
          {
            "title": "[2507.20749] Investigating Structural Pruning and Recovery Techniques for Compressing Multimodal Large Language Models: An Empirical Study",
            "url": "https://arxiv.org/abs/2507.20749"
          },
          {
            "title": "Investigating Structural Pruning and Recovery Techniques ...",
            "url": "https://arxiv.org/pdf/2507.20749"
          },
          {
            "title": "[2510.07782] RCPU: Rotation-Constrained Error Compensation for Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/abs/2510.07782"
          },
          {
            "title": "Deterministic Differentiable Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/html/2603.08065"
          }
        ]
      },
      "Based on the search results, I found several recent arXiv papers (2025-2026) on structured pruning of language models with a focus on recovery techniques:\n\n## Key Papers Found:\n\n1. **Structural Pruning of Large Vision Language Models** - Published April 27, 2026 (arxiv 2604.24380), this comprehensive study investigates layerwise and widthwise pruning paired with supervised finetuning and knowledge distillation. The paper examines recovery methods including knowledge distillation which allows the pruned model to regain lost performance by mimicking the decision-making process of the more capable teacher.\n\n2. **NIRVANA: Structured Pruning Reimagined** - Evaluated on Llama3.1-8B, Llama3.2-3B, Qwen2.5-7B, and T5-base, with both zero-shot results and performance after recovery fine-tuning reported.\n\n3. **SlimLLM: Accurate Structured Pruning** - Proposes an effective structured pruning method and designs a simple linear regression strategy for the output matrix to quickly recover performance.\n\n4. **RCPU: Rotation-Constrained Error Compensation** - Updated February 26, 2026, proposes a rotation-constrained compensation method to address errors introduced by structured pruning of LLMs.\n\n5. **Deterministic Differentiable Structured Pruning** - A lightweight mask-only structured pruning framework that learns structured sparsity patterns via gradient-based optimization.\n\nThese papers represent the latest research on combining structured pruning techniques with various recovery and compensation methods for language models."
    ],
    "durationSeconds": 7.421186137999998
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T13:26:51.633Z_

<details><summary>↩ Tool result · `toolu_01S8fX4oXTVuDAkFEwPpxCtt`</summary>

```text
Web search results for query: "arxiv 2026 "test-time compute" pruning language model"

Links: [{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"ICLR 2026 Test-Time Updates (TTU) Workshop","url":"https://arxiv.org/pdf/2603.19296"},{"title":"[2602.01070] What If We Allocate Test-Time Compute Adaptively?","url":"https://arxiv.org/abs/2602.01070"},{"title":"The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/html/2512.02008v1"},{"title":"[2512.02008] The Art of Scaling Test-Time Compute for Large Language Models","url":"https://arxiv.org/abs/2512.02008"},{"title":"LLMOrbit: A Circular Taxonomy of Large Language Models","url":"https://arxiv.org/pdf/2601.14053"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"[2502.05171] Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach","url":"https://arxiv.org/abs/2502.05171"},{"title":"Beyond Test-Time Compute Strategies: Advocating Energy-per-Token in LLM Inference","url":"https://arxiv.org/html/2603.20224"},{"title":"[2603.20224] Beyond Test-Time Compute Strategies: Advocating Energy-per-Token in LLM Inference","url":"https://arxiv.org/abs/2603.20224"}]

Based on the search results, here are the relevant papers on test-time compute, pruning, and language models from arXiv in 2026:

## Key Papers Found:

**1. "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling"** (2604.25098)

While current Large Language Models (LLMs) exhibit remarkable reasoning capabilities through test-time compute scaling (TTS), their massive parameter counts and high inference costs have motivated the development of pruning methods that can reduce model size without sacrificing performance. Experiments across four reasoning benchmarks on two reasoning LLMs (s1.1-7B and Qwen3-8B) show that unstructured pruning augments TTS performance compared to structured pruning, and at times can even outperform the unpruned full-weight LLMs.

**2. "What If We Allocate Test-Time Compute Adaptively?"** (2602.01070)

A process reward model (PRM) serves as a unified control signal where within each iteration, step-level PRM scores are aggregated to guide pruning and expansion during generation, and across iterations, aggregated trajectory rewards are used to select the final response.

**3. "Beyond Test-Time Compute Strategies: Advocating Energy-per-Token in LLM Inference"** (2603.20224)

The analysis examines trade-offs in test-time compute strategies for smaller models compared to larger ones using the MMLU benchmark, and explores the input-output token dynamics of transformer architectures.

These papers represent recent research at the intersection of test-time compute scaling and pruning methods for language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "d7da5d02-c200-4c76-8dca-80765e2fdb60",
  "tool_use_result": {
    "query": "arxiv 2026 \"test-time compute\" pruning language model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JDkW4UkvVMeN8YHpLWmJvB",
        "content": [
          {
            "title": "[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling",
            "url": "https://arxiv.org/abs/2604.25098"
          },
          {
            "title": "ICLR 2026 Test-Time Updates (TTU) Workshop",
            "url": "https://arxiv.org/pdf/2603.19296"
          },
          {
            "title": "[2602.01070] What If We Allocate Test-Time Compute Adaptively?",
            "url": "https://arxiv.org/abs/2602.01070"
          },
          {
            "title": "The Art of Scaling Test-Time Compute for Large Language Models",
            "url": "https://arxiv.org/html/2512.02008v1"
          },
          {
            "title": "[2512.02008] The Art of Scaling Test-Time Compute for Large Language Models",
            "url": "https://arxiv.org/abs/2512.02008"
          },
          {
            "title": "LLMOrbit: A Circular Taxonomy of Large Language Models",
            "url": "https://arxiv.org/pdf/2601.14053"
          },
          {
            "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
            "url": "https://arxiv.org/html/2408.03314v1"
          },
          {
            "title": "[2502.05171] Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach",
            "url": "https://arxiv.org/abs/2502.05171"
          },
          {
            "title": "Beyond Test-Time Compute Strategies: Advocating Energy-per-Token in LLM Inference",
            "url": "https://arxiv.org/html/2603.20224"
          },
          {
            "title": "[2603.20224] Beyond Test-Time Compute Strategies: Advocating Energy-per-Token in LLM Inference",
            "url": "https://arxiv.org/abs/2603.20224"
          }
        ]
      },
      "Based on the search results, here are the relevant papers on test-time compute, pruning, and language models from arXiv in 2026:\n\n## Key Papers Found:\n\n**1. \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\"** (2604.25098)\n\nWhile current Large Language Models (LLMs) exhibit remarkable reasoning capabilities through test-time compute scaling (TTS), their massive parameter counts and high inference costs have motivated the development of pruning methods that can reduce model size without sacrificing performance. Experiments across four reasoning benchmarks on two reasoning LLMs (s1.1-7B and Qwen3-8B) show that unstructured pruning augments TTS performance compared to structured pruning, and at times can even outperform the unpruned full-weight LLMs.\n\n**2. \"What If We Allocate Test-Time Compute Adaptively?\"** (2602.01070)\n\nA process reward model (PRM) serves as a unified control signal where within each iteration, step-level PRM scores are aggregated to guide pruning and expansion during generation, and across iterations, aggregated trajectory rewards are used to select the final response.\n\n**3. \"Beyond Test-Time Compute Strategies: Advocating Energy-per-Token in LLM Inference\"** (2603.20224)\n\nThe analysis examines trade-offs in test-time compute strategies for smaller models compared to larger ones using the MMLU benchmark, and explores the input-output token dynamics of transformer architectures.\n\nThese papers represent recent research at the intersection of test-time compute scaling and pruning methods for language models."
    ],
    "durationSeconds": 8.015272062000003
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T13:26:51.920Z_

<details><summary>↩ Tool result · `toolu_01NG6Z5pVKijzA4UjLqfdS2x`</summary>

```text
Web search results for query: "arxiv 2026 GRPO pruning OR compression LLM"

Links: [{"title":"[2603.04135] Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization","url":"https://arxiv.org/abs/2603.04135"},{"title":"Compute Where it Counts: Self Optimizing Language Models","url":"https://arxiv.org/html/2605.10875"},{"title":"Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs","url":"https://arxiv.org/html/2604.05643v2"},{"title":"Compressing Chain-of-Thought in LLMs via Step Entropy","url":"https://arxiv.org/html/2508.03346v1"},{"title":"[2603.13418] GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.13418"},{"title":"Making Slow Thinking Faster: Compressing LLM Chain-of-Thought via Step Entropy","url":"https://arxiv.org/html/2508.03346"},{"title":"Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION","url":"https://arxiv.org/pdf/2505.03801"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/html/2603.13418"},{"title":"Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization","url":"https://arxiv.org/html/2602.10048"},{"title":"LLMs can Compress LLMs: Adaptive Pruning by Agents","url":"https://arxiv.org/pdf/2601.09694"}]

Here are the search results for your query about GRPO, pruning, and LLM compression from arXiv in 2026:

## Key Papers Found:

1. **Dynamic Pruning Policy Optimization (DPPO)** - A framework that enables dynamic pruning while preserving unbiased gradient estimation through importance sampling-based correction, significantly accelerating GRPO training without altering the optimization objective. On Qwen3-4B trained on MATH, DPPO achieves 2.37× training speedup and outperforms GRPO by 3.36% in average accuracy across six mathematical reasoning benchmarks.

2. **Self-Optimizing Language Models (SOL)** - Each action instantiates a compute regime by controlling token-level attention sparsity, structured MLP activation pruning, and/or activation quantization bit-width, while leaving base model weights unchanged. The policy is trained using group-relative policy optimization (GRPO) with teacher-forced episodes.

3. **Graph-Based Chain-of-Thought Pruning** - Uses GRPO with length penalty, employing final-answer correctness as the primary signal while jointly optimizing reasoning efficiency to compress redundant steps at inference time.

4. **Compressing CoT via Step Entropy** - The SFT stage teaches models to predict when to use [SKIP] tokens based on entropy-compressed training data, while GRPO optimizes a composite reward function balancing accuracy, compression ratio, and response length.

5. **GPrune-LLM** - A generalization-aware structured pruning framework that explicitly accounts for neuron differences in cross-distribution behavior.

6. **Fine-Grained Group Policy Optimization (FGO)** - Extends GRPO while addressing two inherent limitations: inefficient data utilization and entropy collapse.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "0bde1e11-e5f5-4370-8b78-70f9ffd8d985",
  "tool_use_result": {
    "query": "arxiv 2026 GRPO pruning OR compression LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_0146yVXBopuJz2hDDcCuAEnN",
        "content": [
          {
            "title": "[2603.04135] Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization",
            "url": "https://arxiv.org/abs/2603.04135"
          },
          {
            "title": "Compute Where it Counts: Self Optimizing Language Models",
            "url": "https://arxiv.org/html/2605.10875"
          },
          {
            "title": "Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs",
            "url": "https://arxiv.org/html/2604.05643v2"
          },
          {
            "title": "Compressing Chain-of-Thought in LLMs via Step Entropy",
            "url": "https://arxiv.org/html/2508.03346v1"
          },
          {
            "title": "[2603.13418] GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/abs/2603.13418"
          },
          {
            "title": "Making Slow Thinking Faster: Compressing LLM Chain-of-Thought via Step Entropy",
            "url": "https://arxiv.org/html/2508.03346"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 LARGE LANGUAGE MODEL COMPRESSION",
            "url": "https://arxiv.org/pdf/2505.03801"
          },
          {
            "title": "GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/html/2603.13418"
          },
          {
            "title": "Long Chain-of-Thought Compression via Fine-Grained Group Policy Optimization",
            "url": "https://arxiv.org/html/2602.10048"
          },
          {
            "title": "LLMs can Compress LLMs: Adaptive Pruning by Agents",
            "url": "https://arxiv.org/pdf/2601.09694"
          }
        ]
      },
      "Here are the search results for your query about GRPO, pruning, and LLM compression from arXiv in 2026:\n\n## Key Papers Found:\n\n1. **Dynamic Pruning Policy Optimization (DPPO)** - A framework that enables dynamic pruning while preserving unbiased gradient estimation through importance sampling-based correction, significantly accelerating GRPO training without altering the optimization objective. On Qwen3-4B trained on MATH, DPPO achieves 2.37× training speedup and outperforms GRPO by 3.36% in average accuracy across six mathematical reasoning benchmarks.\n\n2. **Self-Optimizing Language Models (SOL)** - Each action instantiates a compute regime by controlling token-level attention sparsity, structured MLP activation pruning, and/or activation quantization bit-width, while leaving base model weights unchanged. The policy is trained using group-relative policy optimization (GRPO) with teacher-forced episodes.\n\n3. **Graph-Based Chain-of-Thought Pruning** - Uses GRPO with length penalty, employing final-answer correctness as the primary signal while jointly optimizing reasoning efficiency to compress redundant steps at inference time.\n\n4. **Compressing CoT via Step Entropy** - The SFT stage teaches models to predict when to use [SKIP] tokens based on entropy-compressed training data, while GRPO optimizes a composite reward function balancing accuracy, compression ratio, and response length.\n\n5. **GPrune-LLM** - A generalization-aware structured pruning framework that explicitly accounts for neuron differences in cross-distribution behavior.\n\n6. **Fine-Grained Group Policy Optimization (FGO)** - Extends GRPO while addressing two inherent limitations: inefficient data utilization and entropy collapse."
    ],
    "durationSeconds": 8.856991633999998
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the search results and identify new papers that are NOT already in the literature_map.yaml. Let me cross-reference:

Already in literature_map (19 papers):
1. self_healing_2025
2. resp_2025
3. grasprune_2026
4. opsd_2026
5. doing_more_with_less_2026
6. gprune_llm_2026
7. mpruner_2024
8. lachance_thesis_2024


9. bonsai_2025
10. pat_2025
11. rac_2025
12. paser_2025
13. rl_squeezes_2026
14. from_llms_to_lrms_2026
15. p2_law_2025
16. mipp_2024
17. redundancy_aware_cnn_2020
18. self_distilled_rlvr_2026
19. diet_2026

Now I'm looking at the new papers that appeared in the search results and checking which ones aren't already documented. I can see STOP is starting to come through as a new entry. it's at the intersection of RLVR and pruning. Looking at more recent work, there's a unified evaluation framework for LLM compression, dynamic pruning specifically for GRPO training which seems directly applicable, and several structured pruning approaches with recovery mechanisms like SlimLLM and NIRVANA. I'm also seeing error compensation techniques for structured pruning that could be relevant to maintaining performance during the pruning process.

Now I'm filtering through these papers to identify which ones have sufficient relevance to RASP. STOP is about pruning reasoning traces during training rather than model weights themselves, so while it touches on pruning in a reinforcement learning context, it's a different type of pruning than what we're focusing on here—I'd rate that around 4 in relevance.

The structural pruning work on vision-language models is more directly applicable since it covers recovery techniques like supervised fine-tuning and knowledge distillation that could inform our comparison. Deterministic differentiable structured pruning for LLMs is another solid candidate as an alternative approach to the pruning methodology. Prune as You Generate is interesting because it sits at the intersection of RLVR and pruning, though again it's about pruning rollouts rather than model weights—still worth considering at relevance 5. UniComp provides a broader evaluation framework for compression techniques that could be useful context, though it's slightly less directly relevant.

Looking at the more recent papers, Dynamic Pruning for GRPO is similar to the rollout pruning concept but applied to GRPO training, making it relevant for the RLVR+pruning intersection. SlimLLM uses structured pruning with linear regression for recovery, which is an alternative method worth noting. NIRVANA and RCPU both address aspects of structured pruning—one with error compensation and one from September 2025—though they're slightly less central to the core comparison. CKA Enhanced Pruning from April 2025 applies CKA metrics to pruning multi-component architectures, which could be relevant for understanding pruning strategies across different model components.

I should do a few more targeted searches to make sure I'm not missing key papers, particularly around Self-Healing pruning approaches and any newer CKA-based pruning methods for LLMs that might have emerged recently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "e8632b45-06ae-43bb-9303-d22c33e06e8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRs4wPHTAAkWXov7r6GV5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 31443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 30_

找到多篇候选新论文。需要进一步确认几篇关键论文的细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "1a82807a-7d1b-4157-b157-4a22dab06f98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRs4wPHTAAkWXov7r6GV5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 31443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WQhYraMQyosvAHUCkc8iVG`</summary>

```json
{
  "query": "arxiv 2605.13165 STOP structured on-policy pruning reasoning",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "80f4a9c7-c101-4605-9c46-be5115e2c51e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRs4wPHTAAkWXov7r6GV5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 31443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017rJSfyAKPbaKkq7unPn1hS`</summary>

```json
{
  "query": "arxiv 2603.04135 DPPO unbiased dynamic pruning GRPO",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "14cc4811-9c49-4796-b199-fe0d3eb391d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRs4wPHTAAkWXov7r6GV5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 31443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CCNyCabkKUNL9zCqPCmaTa`</summary>

```json
{
  "query": "arxiv 2604.24380 structural pruning vision language models recovery",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "d17f79ee-b98e-45ee-b5c5-22f5f9d2a732",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRs4wPHTAAkWXov7r6GV5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 31443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JpNXsgm1zTGELDtHatAimA`</summary>

```json
{
  "query": "arxiv 2603.24840 \"prune as you generate\" online rollout RLVR",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "8657410f-b110-4510-b395-522a5ee4f1a7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRs4wPHTAAkWXov7r6GV5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 31443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0163GJGuLBYdc4sudZRRJSuL`</summary>

```json
{
  "query": "arxiv 2603.08065 deterministic differentiable structured pruning LLM",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "0e60afe8-821e-48b6-bf10-4b50a2aa60bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRs4wPHTAAkWXov7r6GV5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 31443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gm6oUSiR2YCCyh9NEFueNb`</summary>

```json
{
  "query": "arxiv 2504.13296 CKA enhanced pruning multi-component neural architectures",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "c299de0c-95dc-4077-9f51-454a9396ad21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRs4wPHTAAkWXov7r6GV5k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 901,
      "cache_creation_input_tokens": 5330,
      "cache_read_input_tokens": 31443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5330
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T13:27:26.537Z_

<details><summary>↩ Tool result · `toolu_01CCNyCabkKUNL9zCqPCmaTa`</summary>

```text
Web search results for query: "arxiv 2604.24380 structural pruning vision language models recovery"

Links: [{"title":"[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/abs/2604.24380"},{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"Rethinking Pruning for Vision-Language Models: Strategies for Effective Sparsity and Performance Restoration","url":"https://arxiv.org/html/2404.02424v2"},{"title":"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/html/2604.27115"},{"title":"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression","url":"https://arxiv.org/html/2509.14230v1"},{"title":"Hierarchical Safety Realignment: Lightweight Restoration of Safety in Pruned Large Vision-Language Models","url":"https://arxiv.org/html/2505.16104v1"},{"title":"[2404.02424] Rethinking Pruning for Vision-Language Models: Strategies for Effective Sparsity and Performance Restoration","url":"https://arxiv.org/abs/2404.02424"},{"title":"[2604.16557] S-GRPO: Unified Post-Training for Large Vision-Language Models","url":"https://arxiv.org/abs/2604.16557"},{"title":"[2604.09687] Grid2Matrix: Revealing Digital Agnosia in Vision-Language Models","url":"https://arxiv.org/abs/2604.09687"},{"title":"[2604.14629] Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models","url":"https://arxiv.org/abs/2604.14629"}]

Based on the search results, I found the paper you're looking for. arXiv:2604.24380 is titled "Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency", with authors Yiran Huang, Lukas Thede, Massimiliano Mancini, Wenjia Xu, and Zeynep Akata.

The paper addresses how Large Vision Language Models (LVLMs) demonstrate impressive capabilities, but their substantial computational and memory requirements pose deployment challenges on resource-constrained edge devices. The researchers study a complementary route: compressing existing LVLMs by applying structured pruning to the language model backbone, followed by lightweight recovery training.

The paper investigates two structural pruning paradigms: layerwise and widthwise pruning, and pairs them with supervised finetuning and knowledge distillation on logits and hidden states.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "f97d28e8-5713-435f-b6dc-7b420e9431e9",
  "tool_use_result": {
    "query": "arxiv 2604.24380 structural pruning vision language models recovery",
    "results": [
      {
        "tool_use_id": "srvtoolu_01A8eKyT2DonbAGnRSW3m1Qv",
        "content": [
          {
            "title": "[2604.24380] Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
            "url": "https://arxiv.org/abs/2604.24380"
          },
          {
            "title": "Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
            "url": "https://arxiv.org/html/2604.24380"
          },
          {
            "title": "Rethinking Pruning for Vision-Language Models: Strategies for Effective Sparsity and Performance Restoration",
            "url": "https://arxiv.org/html/2404.02424v2"
          },
          {
            "title": "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models",
            "url": "https://arxiv.org/html/2604.27115"
          },
          {
            "title": "NIRVANA: Structured Pruning Reimagined for Large Language Models Compression",
            "url": "https://arxiv.org/html/2509.14230v1"
          },
          {
            "title": "Hierarchical Safety Realignment: Lightweight Restoration of Safety in Pruned Large Vision-Language Models",
            "url": "https://arxiv.org/html/2505.16104v1"
          },
          {
            "title": "[2404.02424] Rethinking Pruning for Vision-Language Models: Strategies for Effective Sparsity and Performance Restoration",
            "url": "https://arxiv.org/abs/2404.02424"
          },
          {
            "title": "[2604.16557] S-GRPO: Unified Post-Training for Large Vision-Language Models",
            "url": "https://arxiv.org/abs/2604.16557"
          },
          {
            "title": "[2604.09687] Grid2Matrix: Revealing Digital Agnosia in Vision-Language Models",
            "url": "https://arxiv.org/abs/2604.09687"
          },
          {
            "title": "[2604.14629] Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models",
            "url": "https://arxiv.org/abs/2604.14629"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. arXiv:2604.24380 is titled \"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency\", with authors Yiran Huang, Lukas Thede, Massimiliano Mancini, Wenjia Xu, and Zeynep Akata.\n\nThe paper addresses how Large Vision Language Models (LVLMs) demonstrate impressive capabilities, but their substantial computational and memory requirements pose deployment challenges on resource-constrained edge devices. The researchers study a complementary route: compressing existing LVLMs by applying structured pruning to the language model backbone, followed by lightweight recovery training.\n\nThe paper investigates two structural pruning paradigms: layerwise and widthwise pruning, and pairs them with supervised finetuning and knowledge distillation on logits and hidden states."
    ],
    "durationSeconds": 5.2330299570000065
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T13:27:26.819Z_

<details><summary>↩ Tool result · `toolu_01WQhYraMQyosvAHUCkc8iVG`</summary>

```text
Web search results for query: "arxiv 2605.13165 STOP structured on-policy pruning reasoning"

Links: [{"title":"[2605.13165] STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/abs/2605.13165"},{"title":"STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/html/2605.13165"},{"title":"Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning","url":"https://arxiv.org/html/2605.07804v1"},{"title":"Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction","url":"https://arxiv.org/html/2509.12464v1"},{"title":"Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning","url":"https://arxiv.org/html/2604.16029"},{"title":"Structured Pruning for Diverse Best-of-𝑁 Reasoning Optimization","url":"https://arxiv.org/html/2506.03978v1"},{"title":"Post Reasoning: Improving the Performance of Non-Thinking Models at No Cost","url":"https://arxiv.org/html/2605.06165v1"},{"title":"Think Clearly: Improving Reasoning via Redundant Token Pruning","url":"https://arxiv.org/html/2507.08806v1"},{"title":"Think, Prune, Train, Improve: Scaling Reasoning Without Scaling Models","url":"https://arxiv.org/html/2504.18116v1"},{"title":"Optimization-based Structural Pruning for Large Language Models without Back-Propagation","url":"https://arxiv.org/html/2406.10576v1"}]

Based on the search results, I found information about the paper arxiv 2605.13165 on STOP (Structured On-Policy Pruning).

## Overview

STOP (Structured On-policy Pruning) is an on-policy algorithm for analyzing and pruning long-form reasoning traces.

## Problem Being Addressed

Long chain-of-thought (Long CoT) reasoning improves performance on multi-step problems, but it also induces overthinking: models often generate low-yield reasoning that increases inference cost and latency. This inefficiency is especially problematic in low-data fine-tuning regimes, where real applications adapt reasoning models with limited supervision and cannot rely on large-scale teacher distillation or heavy test-time control.

## Methodology

STOP constructs self-distilled traces from the model. Then it maps each trace into a structured reasoning interface through node segmentation, taxonomy annotation, and reasoning-tree construction.

## Authors and Details

The paper was submitted on May 13, 2026 and authored by Chenjun Xu, Zhennan Zhou, Zhan Su, Bill Howe, Lucy Lu Wang, and Bingbing Wen.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "8a588035-9f7c-4c8d-ba90-9981ef039d7c",
  "tool_use_result": {
    "query": "arxiv 2605.13165 STOP structured on-policy pruning reasoning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CGxYmhB2aXpMfvuzTN38hq",
        "content": [
          {
            "title": "[2605.13165] STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes",
            "url": "https://arxiv.org/abs/2605.13165"
          },
          {
            "title": "STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes",
            "url": "https://arxiv.org/html/2605.13165"
          },
          {
            "title": "Prune-OPD: Efficient and Reliable On-Policy Distillation for Long-Horizon Reasoning",
            "url": "https://arxiv.org/html/2605.07804v1"
          },
          {
            "title": "Reasoning Models Can Be Accurately Pruned via Chain-of-Thought Reconstruction",
            "url": "https://arxiv.org/html/2509.12464v1"
          },
          {
            "title": "Cut Your Losses! Learning to Prune Paths Early for Efficient Parallel Reasoning",
            "url": "https://arxiv.org/html/2604.16029"
          },
          {
            "title": "Structured Pruning for Diverse Best-of-𝑁 Reasoning Optimization",
            "url": "https://arxiv.org/html/2506.03978v1"
          },
          {
            "title": "Post Reasoning: Improving the Performance of Non-Thinking Models at No Cost",
            "url": "https://arxiv.org/html/2605.06165v1"
          },
          {
            "title": "Think Clearly: Improving Reasoning via Redundant Token Pruning",
            "url": "https://arxiv.org/html/2507.08806v1"
          },
          {
            "title": "Think, Prune, Train, Improve: Scaling Reasoning Without Scaling Models",
            "url": "https://arxiv.org/html/2504.18116v1"
          },
          {
            "title": "Optimization-based Structural Pruning for Large Language Models without Back-Propagation",
            "url": "https://arxiv.org/html/2406.10576v1"
          }
        ]
      },
      "Based on the search results, I found information about the paper arxiv 2605.13165 on STOP (Structured On-Policy Pruning).\n\n## Overview\n\nSTOP (Structured On-policy Pruning) is an on-policy algorithm for analyzing and pruning long-form reasoning traces.\n\n## Problem Being Addressed\n\nLong chain-of-thought (Long CoT) reasoning improves performance on multi-step problems, but it also induces overthinking: models often generate low-yield reasoning that increases inference cost and latency. This inefficiency is especially problematic in low-data fine-tuning regimes, where real applications adapt reasoning models with limited supervision and cannot rely on large-scale teacher distillation or heavy test-time control.\n\n## Methodology\n\nSTOP constructs self-distilled traces from the model. Then it maps each trace into a structured reasoning interface through node segmentation, taxonomy annotation, and reasoning-tree construction.\n\n## Authors and Details\n\nThe paper was submitted on May 13, 2026 and authored by Chenjun Xu, Zhennan Zhou, Zhan Su, Bill Howe, Lucy Lu Wang, and Bingbing Wen."
    ],
    "durationSeconds": 6.9779013449999985
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T13:27:27.574Z_

<details><summary>↩ Tool result · `toolu_017rJSfyAKPbaKkq7unPn1hS`</summary>

```text
Web search results for query: "arxiv 2603.04135 DPPO unbiased dynamic pruning GRPO"

Links: [{"title":"[2603.04135] Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization","url":"https://arxiv.org/abs/2603.04135"},{"title":"Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization","url":"https://arxiv.org/html/2603.04135"},{"title":"Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models","url":"https://arxiv.org/html/2512.15347v1"},{"title":"A Glimpse to Compress: Dynamic Visual Token Pruning for Large Vision-Language Models","url":"https://arxiv.org/html/2508.01548"},{"title":"OPERA: Online Data Pruning for Efficient Retrieval Model Adaptation","url":"https://arxiv.org/html/2603.17205"},{"title":"Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/html/2603.24840"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/abs/2603.24840"},{"title":"Large-scale Dataset Pruning with Dynamic Uncertainty","url":"https://arxiv.org/html/2306.05175v3"},{"title":"[2512.15347] Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models","url":"https://arxiv.org/abs/2512.15347"}]

I found the paper arxiv 2603.04135. Here are the key details:

**Title:** Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization

**Main Contribution:** DPPO is a framework that enables dynamic pruning while preserving unbiased gradient estimation through importance sampling-based correction. By incorporating mathematically derived rescaling factors, DPPO significantly accelerates GRPO training without altering the optimization objective of the full-batch baseline.

**Problem Addressed:** Group Relative Policy Optimization (GRPO) effectively scales LLM reasoning but incurs prohibitive computational costs due to its extensive group-based sampling requirement. While recent selective data utilization methods can mitigate this overhead, they could induce estimation bias by altering the underlying sampling distribution.

**Additional Features:** To mitigate the data sparsity induced by pruning, the authors introduce Dense Prompt Packing, a window-based greedy strategy that maximizes valid token density and hardware utilization.

**Results:** On Qwen3-4B trained on MATH, DPPO achieves 2.37× training speedup and outperforms GRPO by 3.36% in average accuracy across six mathematical reasoning benchmarks.

The paper was published on March 4, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "6f77c481-7628-4a30-8e28-e765b41a1f28",
  "tool_use_result": {
    "query": "arxiv 2603.04135 DPPO unbiased dynamic pruning GRPO",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DtUhdDR8QeitwC5unbLPbq",
        "content": [
          {
            "title": "[2603.04135] Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization",
            "url": "https://arxiv.org/abs/2603.04135"
          },
          {
            "title": "Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization",
            "url": "https://arxiv.org/html/2603.04135"
          },
          {
            "title": "Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models",
            "url": "https://arxiv.org/html/2512.15347v1"
          },
          {
            "title": "A Glimpse to Compress: Dynamic Visual Token Pruning for Large Vision-Language Models",
            "url": "https://arxiv.org/html/2508.01548"
          },
          {
            "title": "OPERA: Online Data Pruning for Efficient Retrieval Model Adaptation",
            "url": "https://arxiv.org/html/2603.17205"
          },
          {
            "title": "Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR",
            "url": "https://arxiv.org/html/2603.24840"
          },
          {
            "title": "DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed",
            "url": "https://arxiv.org/pdf/2503.14476"
          },
          {
            "title": "[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR",
            "url": "https://arxiv.org/abs/2603.24840"
          },
          {
            "title": "Large-scale Dataset Pruning with Dynamic Uncertainty",
            "url": "https://arxiv.org/html/2306.05175v3"
          },
          {
            "title": "[2512.15347] Expand and Prune: Maximizing Trajectory Diversity for Effective GRPO in Generative Models",
            "url": "https://arxiv.org/abs/2512.15347"
          }
        ]
      },
      "I found the paper arxiv 2603.04135. Here are the key details:\n\n**Title:** Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\n\n**Main Contribution:** DPPO is a framework that enables dynamic pruning while preserving unbiased gradient estimation through importance sampling-based correction. By incorporating mathematically derived rescaling factors, DPPO significantly accelerates GRPO training without altering the optimization objective of the full-batch baseline.\n\n**Problem Addressed:** Group Relative Policy Optimization (GRPO) effectively scales LLM reasoning but incurs prohibitive computational costs due to its extensive group-based sampling requirement. While recent selective data utilization methods can mitigate this overhead, they could induce estimation bias by altering the underlying sampling distribution.\n\n**Additional Features:** To mitigate the data sparsity induced by pruning, the authors introduce Dense Prompt Packing, a window-based greedy strategy that maximizes valid token density and hardware utilization.\n\n**Results:** On Qwen3-4B trained on MATH, DPPO achieves 2.37× training speedup and outperforms GRPO by 3.36% in average accuracy across six mathematical reasoning benchmarks.\n\nThe paper was published on March 4, 2026."
    ],
    "durationSeconds": 6.8230152919999965
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T13:27:28.698Z_

<details><summary>↩ Tool result · `toolu_01Gm6oUSiR2YCCyh9NEFueNb`</summary>

```text
Web search results for query: "arxiv 2504.13296 CKA enhanced pruning multi-component neural architectures"

Links: [{"title":"[2504.13296] Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis","url":"https://arxiv.org/abs/2504.13296"},{"title":"Enhanced Pruning Strategy for Multi-Component Neural Architectures","url":"https://arxiv.org/pdf/2504.13296"},{"title":"Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis","url":"https://arxiv.org/html/2504.13296"},{"title":"Machine Learning Apr 2025","url":"https://www.arxiv.org/list/cs.LG/2025-04?skip=900&show=2000"},{"title":"MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning","url":"https://arxiv.org/html/2408.13482v1"},{"title":"Component-Aware Pruning Framework for Neural Network Controllers via Gradient-Based Importance Estimation","url":"https://arxiv.org/html/2601.19794v1"},{"title":"Pruning Everything, Everywhere, All at Once","url":"https://arxiv.org/html/2506.04513"},{"title":"Effective Layer Pruning Through Similarity Metric Perspective","url":"https://arxiv.org/html/2405.17081v2"},{"title":"[2408.13482] MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning","url":"https://arxiv.org/abs/2408.13482"},{"title":"[2601.19794] Component-Aware Pruning Framework for Neural Network Controllers via Gradient-Based Importance Estimation","url":"https://arxiv.org/abs/2601.19794"}]

Based on the search results, I found the paper you're looking for:

arXiv paper 2504.13296 is titled "Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis". The paper was submitted on April 17, 2025, with a revised version (v2) on July 20, 2025, and is authored by Ganesh Sundaram, Jonas Ulmen, and Daniel Görges.

The paper addresses how comprehensive structured pruning frameworks based on parameter dependency analysis can reduce model size while maintaining performance, but when applied to Multi-Component Neural Architectures (MCNAs), they risk network integrity by removing large parameter groups. The authors introduce a component-aware pruning strategy that extends dependency graphs to isolate individual components and inter-component flows. This approach creates smaller, targeted pruning groups that conserve functional integrity.

The paper is 6 pages long and was published in IFAC J3C 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "88415a5a-196d-4fca-8eda-e54d9fa68f02",
  "tool_use_result": {
    "query": "arxiv 2504.13296 CKA enhanced pruning multi-component neural architectures",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GqkZGHc1is59XvVn5Lhzo1",
        "content": [
          {
            "title": "[2504.13296] Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis",
            "url": "https://arxiv.org/abs/2504.13296"
          },
          {
            "title": "Enhanced Pruning Strategy for Multi-Component Neural Architectures",
            "url": "https://arxiv.org/pdf/2504.13296"
          },
          {
            "title": "Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis",
            "url": "https://arxiv.org/html/2504.13296"
          },
          {
            "title": "Machine Learning Apr 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-04?skip=900&show=2000"
          },
          {
            "title": "MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning",
            "url": "https://arxiv.org/html/2408.13482v1"
          },
          {
            "title": "Component-Aware Pruning Framework for Neural Network Controllers via Gradient-Based Importance Estimation",
            "url": "https://arxiv.org/html/2601.19794v1"
          },
          {
            "title": "Pruning Everything, Everywhere, All at Once",
            "url": "https://arxiv.org/html/2506.04513"
          },
          {
            "title": "Effective Layer Pruning Through Similarity Metric Perspective",
            "url": "https://arxiv.org/html/2405.17081v2"
          },
          {
            "title": "[2408.13482] MPruner: Optimizing Neural Network Size with CKA-Based Mutual Information Pruning",
            "url": "https://arxiv.org/abs/2408.13482"
          },
          {
            "title": "[2601.19794] Component-Aware Pruning Framework for Neural Network Controllers via Gradient-Based Importance Estimation",
            "url": "https://arxiv.org/abs/2601.19794"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\narXiv paper 2504.13296 is titled \"Enhanced Pruning Strategy for Multi-Component Neural Architectures Using Component-Aware Graph Analysis\". The paper was submitted on April 17, 2025, with a revised version (v2) on July 20, 2025, and is authored by Ganesh Sundaram, Jonas Ulmen, and Daniel Görges.\n\nThe paper addresses how comprehensive structured pruning frameworks based on parameter dependency analysis can reduce model size while maintaining performance, but when applied to Multi-Component Neural Architectures (MCNAs), they risk network integrity by removing large parameter groups. The authors introduce a component-aware pruning strategy that extends dependency graphs to isolate individual components and inter-component flows. This approach creates smaller, targeted pruning groups that conserve functional integrity.\n\nThe paper is 6 pages long and was published in IFAC J3C 2025."
    ],
    "durationSeconds": 5.673715251000002
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T13:27:29.722Z_

<details><summary>↩ Tool result · `toolu_01JpNXsgm1zTGELDtHatAimA`</summary>

```text
Web search results for query: "arxiv 2603.24840 "prune as you generate" online rollout RLVR"

Links: [{"title":"[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/abs/2603.24840"},{"title":"Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR","url":"https://arxiv.org/html/2603.24840"},{"title":"Thinking in Streaming Video","url":"https://arxiv.org/html/2603.12938"},{"title":"Matching Features, Not Tokens: Energy-Based Fine-Tuning of Language Models","url":"https://arxiv.org/html/2603.12248"},{"title":"Towards High Data Efficiency in Reinforcement Learning with Verifiable Reward","url":"https://arxiv.org/html/2509.01321"},{"title":"Part II: ROLL Flash – Accelerating RLVR and Agentic Training with Asynchrony","url":"https://arxiv.org/html/2510.11345v1"},{"title":"Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse","url":"https://arxiv.org/html/2509.25808v1"},{"title":"Reaching Beyond the Mode: RL for Distributional Reasoning in Language Models","url":"https://arxiv.org/html/2603.24844"},{"title":"Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning","url":"https://arxiv.org/html/2603.09803"},{"title":"Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning","url":"https://arxiv.org/html/2602.14338"}]

Based on the search results, I found the arXiv paper 2603.24840. Here's what the paper is about:

## Paper Overview

ARRoL (Accelerating RLVR via online RoLlout Pruning) is an online rollout pruning method that prunes rollouts during generation while explicitly steering the surviving ones more correctness-balanced to enhance learning signals.

## Key Problems Addressed

Methods such as GRPO and DAPO suffer from substantial computational cost since they rely on sampling many rollouts for each prompt. Moreover, in RLVR the relative advantage is often sparse: many samples become nearly all-correct or all-incorrect, yielding low within-group reward variance and thus weak learning signals.

## Main Technical Approach

ARRoL trains a lightweight quality head on-the-fly to predict the success probability of partial rollouts and uses it to make early pruning decisions.

## Performance Results

ARRoL shows consistent speedups in wall-clock time comparison between ARRoL and GRPO across different model backbones, and improves average accuracy over GRPO.

The paper was submitted on March 25, 2026, and is authored by researchers from the University of Illinois at Urbana-Champaign and Amazon.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "82040de9-88c3-44ad-9cd4-d712e0bcb1e9",
  "tool_use_result": {
    "query": "arxiv 2603.24840 \"prune as you generate\" online rollout RLVR",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XViUoetEbz6nwBNp58U8Ly",
        "content": [
          {
            "title": "[2603.24840] Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR",
            "url": "https://arxiv.org/abs/2603.24840"
          },
          {
            "title": "Prune as You Generate: Online Rollout Pruning for Faster and Better RLVR",
            "url": "https://arxiv.org/html/2603.24840"
          },
          {
            "title": "Thinking in Streaming Video",
            "url": "https://arxiv.org/html/2603.12938"
          },
          {
            "title": "Matching Features, Not Tokens: Energy-Based Fine-Tuning of Language Models",
            "url": "https://arxiv.org/html/2603.12248"
          },
          {
            "title": "Towards High Data Efficiency in Reinforcement Learning with Verifiable Reward",
            "url": "https://arxiv.org/html/2509.01321"
          },
          {
            "title": "Part II: ROLL Flash – Accelerating RLVR and Agentic Training with Asynchrony",
            "url": "https://arxiv.org/html/2510.11345v1"
          },
          {
            "title": "Improving Sampling Efficiency in RLVR through Adaptive Rollout and Response Reuse",
            "url": "https://arxiv.org/html/2509.25808v1"
          },
          {
            "title": "Reaching Beyond the Mode: RL for Distributional Reasoning in Language Models",
            "url": "https://arxiv.org/html/2603.24844"
          },
          {
            "title": "Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning",
            "url": "https://arxiv.org/html/2603.09803"
          },
          {
            "title": "Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning",
            "url": "https://arxiv.org/html/2602.14338"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper 2603.24840. Here's what the paper is about:\n\n## Paper Overview\n\nARRoL (Accelerating RLVR via online RoLlout Pruning) is an online rollout pruning method that prunes rollouts during generation while explicitly steering the surviving ones more correctness-balanced to enhance learning signals.\n\n## Key Problems Addressed\n\nMethods such as GRPO and DAPO suffer from substantial computational cost since they rely on sampling many rollouts for each prompt. Moreover, in RLVR the relative advantage is often sparse: many samples become nearly all-correct or all-incorrect, yielding low within-group reward variance and thus weak learning signals.\n\n## Main Technical Approach\n\nARRoL trains a lightweight quality head on-the-fly to predict the success probability of partial rollouts and uses it to make early pruning decisions.\n\n## Performance Results\n\nARRoL shows consistent speedups in wall-clock time comparison between ARRoL and GRPO across different model backbones, and improves average accuracy over GRPO.\n\nThe paper was submitted on March 25, 2026, and is authored by researchers from the University of Illinois at Urbana-Champaign and Amazon."
    ],
    "durationSeconds": 7.540654209
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T13:27:30.028Z_

<details><summary>↩ Tool result · `toolu_0163GJGuLBYdc4sudZRRJSuL`</summary>

```text
Web search results for query: "arxiv 2603.08065 deterministic differentiable structured pruning LLM"

Links: [{"title":"[2603.08065] Deterministic Differentiable Structured Pruning for Large Language Models","url":"https://arxiv.org/abs/2603.08065"},{"title":"Deterministic Differentiable Structured Pruning for Large Language Models","url":"https://arxiv.org/html/2603.08065"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/html/2603.13418"},{"title":"Learnable Permutation for Structured Sparsity on Transformer Models","url":"https://arxiv.org/html/2601.22980"},{"title":"[2603.23985] Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score","url":"https://arxiv.org/abs/2603.23985"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"Optimization-based Structural Pruning for Large Language Models without Back-Propagation","url":"https://arxiv.org/html/2406.10576v1"},{"title":"Systematic Characterization of Minimal Deep Learning Architectures: A Unified Analysis of Convergence, Pruning, and Quantization","url":"https://arxiv.org/html/2601.17987"},{"title":"Greedy Output Approximation: Towards Efficient Structured Pruning for LLMs Without Retraining","url":"https://arxiv.org/html/2407.19126v1"},{"title":"Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score","url":"https://arxiv.org/html/2603.23985"}]

I found the paper! Here's what I can tell you about arXiv 2603.08065:

## Paper Overview

The paper is titled "Deterministic Differentiable Structured Pruning for Large Language Models" and was submitted on March 9, 2026 by authors including Weiyu Huang, Pengle Zhang, Xiaolu Zhang, Jun Zhou, Jun Zhu, and Jianfei Chen.

## Main Contribution

Structured pruning reduces LLM inference cost by removing low-importance architectural components. This can be viewed as learning a multiplicative gate for each component under an l0 sparsity constraint.

The paper addresses a key limitation of previous approaches: Prior work typically adopts stochastic hard-concrete relaxations to enable differentiable optimization; however, this stochasticity can introduce a train-test mismatch when sampled masks are discretized for deployment and restricts masks to a bounded, near-binary range.

## Proposed Solution

The authors propose Deterministic Differentiable Pruning (DDP), a mask-only optimization method that eliminates stochasticity by directly optimizing a deterministic soft surrogate of the discrete l0 constraint. The key insight is that mask-only optimization provides a practical middle ground between heuristic one-shot pruning and full weight tuning, where all pre-trained weights are frozen and only the masks are optimized.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "ca0545ca-229c-4567-840c-ed6d52301655",
  "tool_use_result": {
    "query": "arxiv 2603.08065 deterministic differentiable structured pruning LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_017dHj9ULq2oHGBHkWg1rN1M",
        "content": [
          {
            "title": "[2603.08065] Deterministic Differentiable Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/abs/2603.08065"
          },
          {
            "title": "Deterministic Differentiable Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/html/2603.08065"
          },
          {
            "title": "GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/html/2603.13418"
          },
          {
            "title": "Learnable Permutation for Structured Sparsity on Transformer Models",
            "url": "https://arxiv.org/html/2601.22980"
          },
          {
            "title": "[2603.23985] Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score",
            "url": "https://arxiv.org/abs/2603.23985"
          },
          {
            "title": "Pruning Large Language Models by Identifying and Preserving Functional Networks",
            "url": "https://arxiv.org/html/2508.05239v1"
          },
          {
            "title": "Optimization-based Structural Pruning for Large Language Models without Back-Propagation",
            "url": "https://arxiv.org/html/2406.10576v1"
          },
          {
            "title": "Systematic Characterization of Minimal Deep Learning Architectures: A Unified Analysis of Convergence, Pruning, and Quantization",
            "url": "https://arxiv.org/html/2601.17987"
          },
          {
            "title": "Greedy Output Approximation: Towards Efficient Structured Pruning for LLMs Without Retraining",
            "url": "https://arxiv.org/html/2407.19126v1"
          },
          {
            "title": "Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score",
            "url": "https://arxiv.org/html/2603.23985"
          }
        ]
      },
      "I found the paper! Here's what I can tell you about arXiv 2603.08065:\n\n## Paper Overview\n\nThe paper is titled \"Deterministic Differentiable Structured Pruning for Large Language Models\" and was submitted on March 9, 2026 by authors including Weiyu Huang, Pengle Zhang, Xiaolu Zhang, Jun Zhou, Jun Zhu, and Jianfei Chen.\n\n## Main Contribution\n\nStructured pruning reduces LLM inference cost by removing low-importance architectural components. This can be viewed as learning a multiplicative gate for each component under an l0 sparsity constraint.\n\nThe paper addresses a key limitation of previous approaches: Prior work typically adopts stochastic hard-concrete relaxations to enable differentiable optimization; however, this stochasticity can introduce a train-test mismatch when sampled masks are discretized for deployment and restricts masks to a bounded, near-binary range.\n\n## Proposed Solution\n\nThe authors propose Deterministic Differentiable Pruning (DDP), a mask-only optimization method that eliminates stochasticity by directly optimizing a deterministic soft surrogate of the discrete l0 constraint. The key insight is that mask-only optimization provides a practical middle ground between heuristic one-shot pruning and full weight tuning, where all pre-trained weights are frozen and only the masks are optimized."
    ],
    "durationSeconds": 7.374409477000008
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Let me also search for a couple more that might be relevant but I might have missed:
- SlimLLM
- The "Self-Healing" paper's arxiv ID
- Any new papers about functional network preservation during pruning

Actually, let me also check a few more from the search results that looked potentially interesting:
- "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery" (2604.27115)
- "SlimLLM" (2505.22689)

Let me also search for any very recent (May 2026) papers on structured pruning + LLM.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "a9a792d2-7515-4da2-86b4-fa3c9c9ebcb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVvnS2suuLn7PVFvfLDhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 36773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7074
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 44_

让我再搜索几篇可能遗漏的重要论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "5ad2689d-a569-487b-9dbf-86e07042567d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVvnS2suuLn7PVFvfLDhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 36773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7074
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LYGcn1AiH7CsQzQ42jmJYN`</summary>

```json
{
  "query": "arxiv 2604.27115 task-specific neurons model collapse recovery pruning",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "df870c76-aa62-46e2-860d-5fcfdf422473",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVvnS2suuLn7PVFvfLDhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 36773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7074
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BdWi9SE3uz9eBN2vJtTsB5`</summary>

```json
{
  "query": "arxiv 2026 \"structured pruning\" LLM reasoning recovery May April new",
  "allowed_domains": [
    "arxiv.org"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "ad541cfb-ebdd-4f16-b286-5a6df266245a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVvnS2suuLn7PVFvfLDhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 36773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7074
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ljuu8qFCg2wSeaU4pVExd1`</summary>

```json
{
  "query": "arxiv 2026 \"functional overlap\" OR \"functional similarity\" pruning LLM",
  "allowed_domains": [
    "arxiv.org",
    "scholar.google.com"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "a9dbba9f-7c44-46f0-80fd-ec908e182df9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016SVvnS2suuLn7PVFvfLDhr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 723,
      "cache_creation_input_tokens": 7074,
      "cache_read_input_tokens": 36773,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7074
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T13:27:42.150Z_

<details><summary>↩ Tool result · `toolu_01Ljuu8qFCg2wSeaU4pVExd1`</summary>

```text
Web search results for query: "arxiv 2026 "functional overlap" OR "functional similarity" pruning LLM"

Links: [{"title":"[2311.03366] Functional Overlap Reranking for Neural Code Generation","url":"https://arxiv.org/abs/2311.03366"}]

I found one result related to "functional overlap," though it's focused on neural code generation rather than LLM pruning. The search returned:

A paper on functional overlap reranking that quantifies the functional overlap between solution clusters to provide a better ranking strategy for code solutions.

However, this result (arxiv 2311.03366) is from 2023, not 2026, and appears to be about code generation rather than pruning language models. The search query you provided may not have many results available yet, as 2026 papers may still be limited in the arxiv database. If you're looking for more recent work on functional similarity or overlap in LLM pruning specifically, you might try searching with different keywords or without the specific year constraint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "8ce0e664-4776-41cc-9ea0-1d6a05371ea0",
  "tool_use_result": {
    "query": "arxiv 2026 \"functional overlap\" OR \"functional similarity\" pruning LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_018N7fbDSDVVCoWJUdATL3sq",
        "content": [
          {
            "title": "[2311.03366] Functional Overlap Reranking for Neural Code Generation",
            "url": "https://arxiv.org/abs/2311.03366"
          }
        ]
      },
      "I found one result related to \"functional overlap,\" though it's focused on neural code generation rather than LLM pruning. The search returned:\n\nA paper on functional overlap reranking that quantifies the functional overlap between solution clusters to provide a better ranking strategy for code solutions.\n\nHowever, this result (arxiv 2311.03366) is from 2023, not 2026, and appears to be about code generation rather than pruning language models. The search query you provided may not have many results available yet, as 2026 papers may still be limited in the arxiv database. If you're looking for more recent work on functional similarity or overlap in LLM pruning specifically, you might try searching with different keywords or without the specific year constraint."
    ],
    "durationSeconds": 3.73545429899999
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-14T13:27:43.720Z_

<details><summary>↩ Tool result · `toolu_01LYGcn1AiH7CsQzQ42jmJYN`</summary>

```text
Web search results for query: "arxiv 2604.27115 task-specific neurons model collapse recovery pruning"

Links: [{"title":"[2604.27115] Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/abs/2604.27115"},{"title":"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models","url":"https://arxiv.org/html/2604.27115"},{"title":"Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks","url":"https://arxiv.org/html/2604.24637"},{"title":"The Exploration of Neural Collapse under Imbalanced Data","url":"https://arxiv.org/html/2411.17278v1"},{"title":"Neural Collapse in Cumulative Link Models for Ordinal Regression: An Analysis with Unconstrained Feature Model","url":"https://arxiv.org/html/2506.05801"},{"title":"The Persistence of Neural Collapse Despite Low-Rank Bias: An Analytic Perspective Through Unconstrained Features","url":"https://arxiv.org/html/2410.23169v1"},{"title":"Linguistic Collapse: Neural Collapse in (Large) Language Models","url":"https://arxiv.org/html/2405.17767v1"},{"title":"[2604.24637] Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks","url":"https://arxiv.org/abs/2604.24637"},{"title":"Exploring The Neural Burden In Pruned Models: An Insight Inspired By Neuroscience","url":"https://arxiv.org/html/2407.16716v1"},{"title":"Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers","url":"https://arxiv.org/html/2505.15239v1"}]

Based on the search results, I found the paper you're looking for. Here's what arxiv 2604.27115 is about:

## Paper Overview

The paper is titled "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models", authored by M. K. Khalidi Siam and colleagues from BRAC University.

## Research Focus

The paper addresses whether neurons in task-specific models contribute uniformly to task performance through a systematic pruning study on language models specialized for mathematical reasoning and code generation.

## Key Methodology

The researchers introduce an activation-based selectivity metric to identify neurons with low contribution to the target task and prune them while preserving target-task accuracy, and compare selective pruning with random pruning.

## Main Findings

- Selective pruning consistently outperforms random pruning, indicating that activation-based selectivity provides a systematic advantage
- Removing a small subset of highly task-specific neurons (~10%) causes complete performance collapse, suggesting the existence of task-specific neurons
- Experiments on both 1.5B and 7B models reveal a robustness threshold around 15-20% pruning, beyond which accuracy loss and generation failures increase sharply
- Fine-tuning substantially recovers performance across pruning levels, particularly for aggressively pruned models


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "cbbdf09e-e456-4b44-98a2-f622d91d1d8a",
  "tool_use_result": {
    "query": "arxiv 2604.27115 task-specific neurons model collapse recovery pruning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WoCkFuN7vnDeLSdzJSVueX",
        "content": [
          {
            "title": "[2604.27115] Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models",
            "url": "https://arxiv.org/abs/2604.27115"
          },
          {
            "title": "Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models",
            "url": "https://arxiv.org/html/2604.27115"
          },
          {
            "title": "Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks",
            "url": "https://arxiv.org/html/2604.24637"
          },
          {
            "title": "The Exploration of Neural Collapse under Imbalanced Data",
            "url": "https://arxiv.org/html/2411.17278v1"
          },
          {
            "title": "Neural Collapse in Cumulative Link Models for Ordinal Regression: An Analysis with Unconstrained Feature Model",
            "url": "https://arxiv.org/html/2506.05801"
          },
          {
            "title": "The Persistence of Neural Collapse Despite Low-Rank Bias: An Analytic Perspective Through Unconstrained Features",
            "url": "https://arxiv.org/html/2410.23169v1"
          },
          {
            "title": "Linguistic Collapse: Neural Collapse in (Large) Language Models",
            "url": "https://arxiv.org/html/2405.17767v1"
          },
          {
            "title": "[2604.24637] Cortex-Inspired Continual Learning: Unsupervised Instantiation and Recovery of Functional Task Networks",
            "url": "https://arxiv.org/abs/2604.24637"
          },
          {
            "title": "Exploring The Neural Burden In Pruned Models: An Insight Inspired By Neuroscience",
            "url": "https://arxiv.org/html/2407.16716v1"
          },
          {
            "title": "Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers",
            "url": "https://arxiv.org/html/2505.15239v1"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what arxiv 2604.27115 is about:\n\n## Paper Overview\n\nThe paper is titled \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific Large Language Models\", authored by M. K. Khalidi Siam and colleagues from BRAC University.\n\n## Research Focus\n\nThe paper addresses whether neurons in task-specific models contribute uniformly to task performance through a systematic pruning study on language models specialized for mathematical reasoning and code generation.\n\n## Key Methodology\n\nThe researchers introduce an activation-based selectivity metric to identify neurons with low contribution to the target task and prune them while preserving target-task accuracy, and compare selective pruning with random pruning.\n\n## Main Findings\n\n- Selective pruning consistently outperforms random pruning, indicating that activation-based selectivity provides a systematic advantage\n- Removing a small subset of highly task-specific neurons (~10%) causes complete performance collapse, suggesting the existence of task-specific neurons\n- Experiments on both 1.5B and 7B models reveal a robustness threshold around 15-20% pruning, beyond which accuracy loss and generation failures increase sharply\n- Fine-tuning substantially recovers performance across pruning levels, particularly for aggressively pruned models"
    ],
    "durationSeconds": 6.940447705000013
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-14T13:27:44.949Z_

<details><summary>↩ Tool result · `toolu_01BdWi9SE3uz9eBN2vJtTsB5`</summary>

```text
Web search results for query: "arxiv 2026 "structured pruning" LLM reasoning recovery May April new"

Links: [{"title":"Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency","url":"https://arxiv.org/html/2604.24380"},{"title":"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models","url":"https://arxiv.org/pdf/2603.13418"},{"title":"STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes","url":"https://arxiv.org/html/2605.13165"},{"title":"Pruning Large Language Models by Identifying and Preserving Functional Networks","url":"https://arxiv.org/html/2508.05239v1"},{"title":"[2305.11627] LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://arxiv.org/abs/2305.11627"},{"title":"NIRVANA: Structured Pruning Reimagined for Large Language Models Compression","url":"https://arxiv.org/html/2509.14230v1"},{"title":"LLM-Pruner: On the Structural Pruning of Large Language Models Xinyin Ma","url":"https://arxiv.org/pdf/2305.11627"},{"title":"Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs","url":"https://arxiv.org/html/2604.05643v2"},{"title":"[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling","url":"https://arxiv.org/abs/2604.25098"},{"title":"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models","url":"https://arxiv.org/html/2601.18091"}]

Based on the search results, I found several recent arxiv papers from 2026 related to structured pruning, LLM reasoning, and recovery. Here are the most relevant findings:

## Key Papers on Structured Pruning and LLM Reasoning Recovery (2026)

1. **"Structural Pruning of Large Vision Language Models"** (April 2026)
   This paper disentangles the effects of pruning on modality alignment versus core language reasoning, and investigates recovery strategies including supervised finetuning (SFT) of the multimodal projector and joint SFT of both the projector and the LLM.

2. **"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling"** (April 2026)
   This work examines how structured pruning significantly degrades test-time scaling reasoning performance, while unstructured pruning can augment TTS performance and even outperform unpruned full-weight LLMs.

3. **"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models"** (January 2026)
   This paper conducts a controlled study comparing pruning for instruction-following and reasoning-augmented models, aligning pruning calibration and post-pruning recovery data with the model's original training distribution.

4. **"GPrune-LLM: Generalization-Aware Structured Pruning"** (March 2026)
   This framework accounts for neuron differences in cross-distribution behavior by partitioning neurons into behavior-consistent modules, evaluating activation-based metric reliability per module, and adaptively learning module-wise sparsity.

These papers collectively explore challenges in preserving reasoning capabilities during LLM pruning and propose various recovery strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "0e5c4fc2-cd2e-4501-ae28-aa4bb30f902e",
  "tool_use_result": {
    "query": "arxiv 2026 \"structured pruning\" LLM reasoning recovery May April new",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CgmyTx5yEAdVmph5R6QYR9",
        "content": [
          {
            "title": "Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
            "url": "https://arxiv.org/html/2604.24380"
          },
          {
            "title": "GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models",
            "url": "https://arxiv.org/pdf/2603.13418"
          },
          {
            "title": "STOP: Structured On-Policy Pruning of Long-Form Reasoning in Low-Data Regimes",
            "url": "https://arxiv.org/html/2605.13165"
          },
          {
            "title": "Pruning Large Language Models by Identifying and Preserving Functional Networks",
            "url": "https://arxiv.org/html/2508.05239v1"
          },
          {
            "title": "[2305.11627] LLM-Pruner: On the Structural Pruning of Large Language Models",
            "url": "https://arxiv.org/abs/2305.11627"
          },
          {
            "title": "NIRVANA: Structured Pruning Reimagined for Large Language Models Compression",
            "url": "https://arxiv.org/html/2509.14230v1"
          },
          {
            "title": "LLM-Pruner: On the Structural Pruning of Large Language Models Xinyin Ma",
            "url": "https://arxiv.org/pdf/2305.11627"
          },
          {
            "title": "Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs",
            "url": "https://arxiv.org/html/2604.05643v2"
          },
          {
            "title": "[2604.25098] Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling",
            "url": "https://arxiv.org/abs/2604.25098"
          },
          {
            "title": "From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models",
            "url": "https://arxiv.org/html/2601.18091"
          }
        ]
      },
      "Based on the search results, I found several recent arxiv papers from 2026 related to structured pruning, LLM reasoning, and recovery. Here are the most relevant findings:\n\n## Key Papers on Structured Pruning and LLM Reasoning Recovery (2026)\n\n1. **\"Structural Pruning of Large Vision Language Models\"** (April 2026)\n   This paper disentangles the effects of pruning on modality alignment versus core language reasoning, and investigates recovery strategies including supervised finetuning (SFT) of the multimodal projector and joint SFT of both the projector and the LLM.\n\n2. **\"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\"** (April 2026)\n   This work examines how structured pruning significantly degrades test-time scaling reasoning performance, while unstructured pruning can augment TTS performance and even outperform unpruned full-weight LLMs.\n\n3. **\"From LLMs to LRMs: Rethinking Pruning for Reasoning-Centric Models\"** (January 2026)\n   This paper conducts a controlled study comparing pruning for instruction-following and reasoning-augmented models, aligning pruning calibration and post-pruning recovery data with the model's original training distribution.\n\n4. **\"GPrune-LLM: Generalization-Aware Structured Pruning\"** (March 2026)\n   This framework accounts for neuron differences in cross-distribution behavior by partitioning neurons into behavior-consistent modules, evaluating activation-based metric reliability per module, and adaptively learning module-wise sparsity.\n\nThese papers collectively explore challenges in preserving reasoning capabilities during LLM pruning and propose various recovery strategies."
    ],
    "durationSeconds": 7.184986034999994
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Now let me compile all my findings and evaluate which papers are new and relevant.

Existing papers (19):
1. self_healing_2025
2. resp_2025
3. grasprune_2026
4. opsd_2026
5. doing_more_with_less_2026
6. gprune_llm_2026
7. mpruner_2024
8. lachance_thesis_2024
9. bonsai_2025
10. pat_2025
11. rac_2025


12. paser_2025
13. rl_squeezes_2026
14. from_llms_to_lrms_2026
15. p2_law_2025
16. mipp_2024
17. redundancy_aware_cnn_2020
18. self_distilled_rlvr_2026
19. diet_2026

I'm now identifying papers that aren't already in my collection and assessing their relevance to the research area. I found DPPO (Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization) from March 2026, which appears to be highly relevant based on its focus on efficient pruning methods. ance: 7 — Directly accelerates GRPO training via rollout pruning with importance sampling. Relevant because RASP uses GRPO for recovery.
   - Category: method-component
   - Relation: Could be applied to speed up our RLVR/GRPO recovery phase

2. **Structural Pruning of Large VLMs** (2604.24380, Apr 2026)  
   - Relevance: 6 — Comprehensive study on pruning dynamics and recovery for VLMs. Width vs layer pruning analysis + recovery strategies are directly comparable to our work.
   - Category: background
   - Relation: Recovery methodology comparison; validates width pruning + KD recovery paradigm

3. **DDP: Deterministic Differentiable Structured Pruning** (2603.08065, Mar 2026)
   - Relevance: 5 — Alternative structured pruning method. Mask-only optimization without stochasticity.
   - Category: background
   - Relation: Alternative pruning backbone; complementary to our CKA-guided selection

4. **ARRoL: Prune as You Generate** (2603.24840, Mar 2026)
   - Relevance: 6 — Online rollout pruning for RLVR training efficiency rather than model pruning itself.
   - Category: background
   - Relation: Could improve our RLVR recovery efficiency within the same domain

5. **Task-Specific Neurons & Recovery** (2604.27115, Apr 2026)
   - Relevance: 6 — Examines task-specific neurons and recovery after pruning in reasoning models, identifying a 15-20% robustness threshold and fine-tuning recovery patterns.
   - Category: background
   - Relation: Supports our premise that recovery is needed and identifies task-specific neural properties

Now I'm filtering through the lower-relevance papers—UniComp is just a general benchmark, STOP focuses on reasoning traces rather than model weights, Enhanced Pruning targets MCNAs instead of LLMs, and SlimLLM appears to be cut off but likely falls below our threshold as well.

Let me refocus on the papers that actually matter for this work. I'm zeroing in on the ones with relevance scores of 5 or higher: DPPO on dynamic pruning for GRPO, ARRoL's generate-as-you-prune approach, structural pruning of vision language models, task-specific neurons and model collapse recovery, and deterministic differentiable structured pruning methods.

Now I need to be more careful about what goes into the literature map. DPPO is relevant because it accelerates GRPO training through rollout pruning, which connects to RASP's use of GRPO for recovery, though it's focused on training efficiency rather than model pruning itself. ARRoL sits in a similar space with online rollout pruning for reinforcement learning. The structural pruning work on vision language models is worth including as well.

For the task-specific neurons paper, it directly addresses how pruning affects model recovery in the context of math reasoning, which is methodologically relevant. DDP offers another structured pruning approach that meets the threshold. I'm less certain about SlimLLM since the details are sparse and it's from May 2025, so I'll leave that one out for now.

I should verify whether the existing "from_llms_to_lrms_2026" entry already covers the language-to-reasoning model transition aspect before finalizing the list.

Actually, looking back at DPPO and ARRoL more carefully — these are about pruning rollouts during training rather than pruning the model itself. DPPO maintains unbiased gradient estimation while pruning samples during GRPO, and ARRoL does similar rollout pruning during RLVR. Both could accelerate the recovery phase in RASP, so they're relevant at a level 5. Now I need to finalize the relevance scores and add these papers to the literature map. I'm realizing that literature_map.yaml isn't in the whitelist for the save_project_file tool, so I'll need to use the Write tool directly instead to update it with the new entries while preserving the existing content. I'm finishing up the first entry about dynamic pruning for GRPO, then moving on to add entries about online rollout pruning for RLVR and structural pruning of vision language models to the bibliography. Pruning Dynamics, Recovery, and Data Efficiency"
    year: 2026
    venue: "arXiv Apr 2026"
    category: background
    role: "Comprehensive pruning + recovery study for VLMs"
    relevance: 5
    key_finding: "Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; recovery data efficiency matters"
    our_relation: "Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability"
    arxiv_id: "2604.24380"

This next paper identifies task-specific neurons and shows that removing just 10% of them causes model collapse, with a robustness threshold around 15-20% that fine-tuning can substantially recover from—which supports the need for recovery-aware pruning strategies that my CKA method can help predict. There's also a differentiable structured pruning approach using deterministic soft surrogates that eliminates the train-test mismatch problem in mask-based pruning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "967d7e1f-339f-44af-96df-91e7911c8885",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195rggk7dr18KUMfrPuwuBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 288,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 43847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2959
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 52_

搜索完成，找到 5 篇新的相关论文（relevance ≥ 5）。现在更新 literature_map.yaml 并写 related work 笔记。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "d482cc81-4e0f-4820-8ed7-5e3ad1938449",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195rggk7dr18KUMfrPuwuBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 288,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 43847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2959
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01946JFomLCEX18HxffMFVhe`</summary>

```json
{
  "todos": [
    {
      "content": "Read current literature_map.yaml",
      "status": "completed",
      "activeForm": "Reading current literature_map.yaml"
    },
    {
      "content": "Search arXiv for new papers (6 keyword groups)",
      "status": "completed",
      "activeForm": "Searching arXiv for new papers"
    },
    {
      "content": "Evaluate and add new papers to literature_map.yaml",
      "status": "in_progress",
      "activeForm": "Evaluating and adding new papers"
    },
    {
      "content": "Write related_work_notes.md",
      "status": "pending",
      "activeForm": "Writing related work notes"
    },
    {
      "content": "Register artifact",
      "status": "pending",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "4619445d-64d1-4e33-9e20-992bda4d36c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195rggk7dr18KUMfrPuwuBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 288,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 43847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2959
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T13:28:46.391Z_

<details><summary>↩ Tool result · `toolu_01946JFomLCEX18HxffMFVhe`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "9a28b45f-3bdb-4ae0-ae53-7506cf11308e",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "in_progress",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "pending",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "pending",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "completed",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "in_progress",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "pending",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_01RDvgPHS6pnh1FwVpiekt7r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "c8292b28-aded-4ed6-af1e-25f0dec9f43b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0195rggk7dr18KUMfrPuwuBW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 288,
      "cache_creation_input_tokens": 2959,
      "cache_read_input_tokens": 43847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2959
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-14T13:28:46.659Z_

<details><summary>↩ Tool result · `toolu_01RDvgPHS6pnh1FwVpiekt7r`</summary>

```text
1	papers:
2	  # === Direct Competitors ===
3	  - id: self_healing_2025
4	    title: "Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning"
5	    year: 2025
6	    venue: "under review"
7	    category: direct-competitor
8	    role: "RLVR recovery baseline"
9	    relevance: 9
10	    key_finding: "RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%"
11	    our_relation: "We extend beyond single sparsity ratio and add CKA-guided pruning selection"
12	    arxiv_id: ""
13	
14	  - id: resp_2025
15	    title: "RESP: Self-Reflective Structured Pruning for Reasoning LLMs"
16	    year: 2025
17	    venue: "arXiv Dec 2025"
18	    category: direct-competitor
19	    role: "Structured pruning for reasoning without recovery"
20	    relevance: 8
21	    key_finding: "GSM8K 81.3% at 40% sparsity via self-reflective importance"
22	    our_relation: "No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity"
23	    arxiv_id: ""
24	
25	  - id: grasprune_2026
26	    title: "GRASPrune: Global Gating-based Structural Pruning for LLMs"
27	    year: 2026
28	    venue: "ACL 2026 Main"
29	    category: direct-competitor
30	    role: "SOTA budgeted structural pruning"
31	    relevance: 8
32	    key_finding: "Global gating achieves best structured pruning under budget constraints"
33	    our_relation: "GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top"
34	    arxiv_id: ""
35	
36	  - id: opsd_2026
37	    title: "OPSD: One-shot Post-RL Structured Distillation"
38	    year: 2026
39	    venue: "arXiv May 2026"
40	    category: direct-competitor
41	    role: "Post-RL compression via distillation"
42	    relevance: 7
43	    key_finding: "Compress post-RL model in one shot via structured distillation"
44	    our_relation: "Distillation-based vs our pruning+recovery approach; complementary"
45	    arxiv_id: ""
46	
47	  - id: doing_more_with_less_2026
48	    title: "Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling"
49	    year: 2026
50	    venue: "arXiv Apr 2026"
51	    category: direct-competitor
52	    role: "Pruning improves test-time scaling"
53	    relevance: 7
54	    key_finding: "Unstructured pruning can augment test-time scaling; structured pruning degrades it"
55	    our_relation: "Motivates why structured pruning needs recovery; we address this gap with RLVR"
56	    arxiv_id: "2604.25098"
57	
58	  - id: gprune_llm_2026
59	    title: "GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models"
60	    year: 2026
61	    venue: "arXiv Mar 2026"
62	    category: direct-competitor
63	    role: "Cross-distribution generalization-aware pruning"
64	    relevance: 6
65	    key_finding: "Accounts for neuron cross-distribution behavior; reduces calibration bias"
66	    our_relation: "Complementary importance metric; our CKA captures functional overlap vs their generalization gap"
67	    arxiv_id: "2603.13418"
68	
69	  # === Method Components ===
70	  - id: mpruner_2024
71	    title: "MPruner: CKA-based Inter-layer Pruning for LLMs"
72	    year: 2024
73	    venue: "arXiv"
74	    category: method-component
75	    role: "CKA for layer importance estimation"
76	    relevance: 8
77	    key_finding: "CKA similarity between layers identifies redundant layers for removal"
78	    our_relation: "We adapt CKA from layer-level to width-level functional overlap prediction"
79	    arxiv_id: ""
80	
81	  - id: lachance_thesis_2024
82	    title: "CKA Layer Similarity for Neural Network Pruning"
83	    year: 2024
84	    venue: "URI Master's Thesis"
85	    category: method-component
86	    role: "CKA-based pruning theoretical foundation"
87	    relevance: 6
88	    key_finding: "CKA layer similarity correlates with pruning recoverability"
89	    our_relation: "Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery"
90	    arxiv_id: ""
91	
92	  - id: bonsai_2025
93	    title: "Bonsai: Gradient-Free Structured Pruning for LLMs"
94	    year: 2025
95	    venue: "ICML 2025"
96	    category: method-component
97	    role: "Gradient-free structured pruning alternative"
98	    relevance: 6
99	    key_finding: "Achieves competitive structured pruning without backprop"
100	    our_relation: "Alternative pruning strategy; our CKA metric is also gradient-free"
101	    arxiv_id: ""
102	
103	  - id: pat_2025
104	    title: "PAT: Pruning-Aware Tuning for LLMs"
105	    year: 2025
106	    venue: "AAAI 2025"
107	    category: method-component
108	    role: "Joint pruning and tuning framework"
109	    relevance: 6
110	    key_finding: "Co-optimizing pruning mask and fine-tuning improves recovery"
111	    our_relation: "Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery"
112	    arxiv_id: ""
113	
114	  - id: rac_2025
115	    title: "RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models"
116	    year: 2025
117	    venue: "NeurIPS 2025"
118	    category: method-component
119	    role: "CoT reconstruction post-pruning"
120	    relevance: 7
121	    key_finding: "Reconstructing CoT improves unstructured/2:4 pruned reasoning models"
122	    our_relation: "Complementary recovery strategy; could combine with our RLVR approach"
123	    arxiv_id: ""
124	
125	  - id: paser_2025
126	    title: "PASER: Data Selection for Pruning Recovery"
127	    year: 2025
128	    venue: "under review"
129	    category: method-component
130	    role: "Recovery training data selection"
131	    relevance: 6
132	    key_finding: "Selective data for recovery training improves efficiency"
133	    our_relation: "Orthogonal contribution; can apply PASER data selection to our RLVR recovery"
134	    arxiv_id: ""
135	
136	  # === Background / Theory ===
137	  - id: rl_squeezes_2026
138	    title: "RL Squeezes, SFT Expands: Different Mechanisms in Post-Training"
139	    year: 2026
140	    venue: "ICLR 2026 Poster"
141	    category: background
142	    role: "Theoretical basis for why RLVR works differently from SFT"
143	    relevance: 8
144	    key_finding: "RLVR compresses representation while SFT expands; different inductive biases"
145	    our_relation: "Explains why RLVR recovery succeeds where SFT fails post-pruning"
146	    arxiv_id: ""
147	
148	  - id: from_llms_to_lrms_2026
149	    title: "From LLMs to LRMs: Width Pruning is More Robust for Reasoning"
150	    year: 2026
151	    venue: "arXiv Jan 2026"
152	    category: background
153	    role: "Width vs depth pruning for reasoning"
154	    relevance: 7
155	    key_finding: "Width pruning preserves reasoning better than depth pruning"
156	    our_relation: "Motivates our focus on width-level structured pruning"
157	    arxiv_id: ""
158	
159	  - id: p2_law_2025
160	    title: "P² Law: Scaling Law for Pruning Recovery Training"
161	    year: 2025
162	    venue: "ACL 2025"
163	    category: background
164	    role: "Theoretical scaling of recovery compute"
165	    relevance: 7
166	    key_finding: "Recovery training follows predictable scaling with compute and data"
167	    our_relation: "Informs our recovery budget estimation; we extend to RLVR-specific scaling"
168	    arxiv_id: ""
169	
170	  - id: mipp_2024
171	    title: "MIPP: Mutual Information Preserving Pruning"
172	    year: 2024
173	    venue: "arXiv"
174	    category: background
175	    role: "Information-theoretic pruning criterion"
176	    relevance: 5
177	    key_finding: "Preserving mutual information between layers reduces pruning damage"
178	    our_relation: "Related theoretical motivation; CKA captures similar functional redundancy"
179	    arxiv_id: ""
180	
181	  - id: redundancy_aware_cnn_2020
182	    title: "Redundancy-Aware Pruning of Convolutional Neural Networks"
183	    year: 2020
184	    venue: "Neural Computation"
185	    category: background
186	    role: "Pioneer of redundancy-based pruning"
187	    relevance: 4
188	    key_finding: "Redundancy metrics guide pruning decisions in CNNs"
189	    our_relation: "Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning"
190	    arxiv_id: ""
191	
192	  - id: self_distilled_rlvr_2026
193	    title: "Self-Distilled RLVR"
194	    year: 2026
195	    venue: "arXiv Apr 2026"
196	    category: background
197	    role: "RLVR training efficiency improvement"
198	    relevance: 5
199	    key_finding: "Self-distillation stabilizes RLVR training and improves sample efficiency"
200	    our_relation: "Could improve our RLVR recovery phase efficiency"
201	    arxiv_id: "2604.03128"
202	
203	  - id: diet_2026
204	    title: "DieT: Dimension-wise Global Pruning via Task-specific Importance Score"
205	    year: 2026
206	    venue: "arXiv Mar 2026"
207	    category: background
208	    role: "Dimension-wise importance for width pruning"
209	    relevance: 5
210	    key_finding: "Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity"
211	    our_relation: "Alternative width importance metric; we use CKA overlap instead"
212	    arxiv_id: "2603.23985"
213	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "91bb8802-0456-4653-85cf-b29632e64ea0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
      "content": "papers:\n  # === Direct Competitors ===\n  - id: self_healing_2025\n    title: \"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\"\n    year: 2025\n    venue: \"under review\"\n    category: direct-competitor\n    role: \"RLVR recovery baseline\"\n    relevance: 9\n    key_finding: \"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%\"\n    our_relation: \"We extend beyond single sparsity ratio and add CKA-guided pruning selection\"\n    arxiv_id: \"\"\n\n  - id: resp_2025\n    title: \"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: direct-competitor\n    role: \"Structured pruning for reasoning without recovery\"\n    relevance: 8\n    key_finding: \"GSM8K 81.3% at 40% sparsity via self-reflective importance\"\n    our_relation: \"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\"\n    arxiv_id: \"\"\n\n  - id: grasprune_2026\n    title: \"GRASPrune: Global Gating-based Structural Pruning for LLMs\"\n    year: 2026\n    venue: \"ACL 2026 Main\"\n    category: direct-competitor\n    role: \"SOTA budgeted structural pruning\"\n    relevance: 8\n    key_finding: \"Global gating achieves best structured pruning under budget constraints\"\n    our_relation: \"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\"\n    arxiv_id: \"\"\n\n  - id: opsd_2026\n    title: \"OPSD: One-shot Post-RL Structured Distillation\"\n    year: 2026\n    venue: \"arXiv May 2026\"\n    category: direct-competitor\n    role: \"Post-RL compression via distillation\"\n    relevance: 7\n    key_finding: \"Compress post-RL model in one shot via structured distillation\"\n    our_relation: \"Distillation-based vs our pruning+recovery approach; complementary\"\n    arxiv_id: \"\"\n\n  - id: doing_more_with_less_2026\n    title: \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: direct-competitor\n    role: \"Pruning improves test-time scaling\"\n    relevance: 7\n    key_finding: \"Unstructured pruning can augment test-time scaling; structured pruning degrades it\"\n    our_relation: \"Motivates why structured pruning needs recovery; we address this gap with RLVR\"\n    arxiv_id: \"2604.25098\"\n\n  - id: gprune_llm_2026\n    title: \"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: direct-competitor\n    role: \"Cross-distribution generalization-aware pruning\"\n    relevance: 6\n    key_finding: \"Accounts for neuron cross-distribution behavior; reduces calibration bias\"\n    our_relation: \"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\"\n    arxiv_id: \"2603.13418\"\n\n  # === Method Components ===\n  - id: mpruner_2024\n    title: \"MPruner: CKA-based Inter-layer Pruning for LLMs\"\n    year: 2024\n    venue: \"arXiv\"\n    category: method-component\n    role: \"CKA for layer importance estimation\"\n    relevance: 8\n    key_finding: \"CKA similarity between layers identifies redundant layers for removal\"\n    our_relation: \"We adapt CKA from layer-level to width-level functional overlap prediction\"\n    arxiv_id: \"\"\n\n  - id: lachance_thesis_2024\n    title: \"CKA Layer Similarity for Neural Network Pruning\"\n    year: 2024\n    venue: \"URI Master's Thesis\"\n    category: method-component\n    role: \"CKA-based pruning theoretical foundation\"\n    relevance: 6\n    key_finding: \"CKA layer similarity correlates with pruning recoverability\"\n    our_relation: \"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: bonsai_2025\n    title: \"Bonsai: Gradient-Free Structured Pruning for LLMs\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: method-component\n    role: \"Gradient-free structured pruning alternative\"\n    relevance: 6\n    key_finding: \"Achieves competitive structured pruning without backprop\"\n    our_relation: \"Alternative pruning strategy; our CKA metric is also gradient-free\"\n    arxiv_id: \"\"\n\n  - id: pat_2025\n    title: \"PAT: Pruning-Aware Tuning for LLMs\"\n    year: 2025\n    venue: \"AAAI 2025\"\n    category: method-component\n    role: \"Joint pruning and tuning framework\"\n    relevance: 6\n    key_finding: \"Co-optimizing pruning mask and fine-tuning improves recovery\"\n    our_relation: \"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: rac_2025\n    title: \"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    category: method-component\n    role: \"CoT reconstruction post-pruning\"\n    relevance: 7\n    key_finding: \"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\"\n    our_relation: \"Complementary recovery strategy; could combine with our RLVR approach\"\n    arxiv_id: \"\"\n\n  - id: paser_2025\n    title: \"PASER: Data Selection for Pruning Recovery\"\n    year: 2025\n    venue: \"under review\"\n    category: method-component\n    role: \"Recovery training data selection\"\n    relevance: 6\n    key_finding: \"Selective data for recovery training improves efficiency\"\n    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  # === Background / Theory ===\n  - id: rl_squeezes_2026\n    title: \"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\"\n    year: 2026\n    venue: \"ICLR 2026 Poster\"\n    category: background\n    role: \"Theoretical basis for why RLVR works differently from SFT\"\n    relevance: 8\n    key_finding: \"RLVR compresses representation while SFT expands; different inductive biases\"\n    our_relation: \"Explains why RLVR recovery succeeds where SFT fails post-pruning\"\n    arxiv_id: \"\"\n\n  - id: from_llms_to_lrms_2026\n    title: \"From LLMs to LRMs: Width Pruning is More Robust for Reasoning\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Width vs depth pruning for reasoning\"\n    relevance: 7\n    key_finding: \"Width pruning preserves reasoning better than depth pruning\"\n    our_relation: \"Motivates our focus on width-level structured pruning\"\n    arxiv_id: \"\"\n\n  - id: p2_law_2025\n    title: \"P² Law: Scaling Law for Pruning Recovery Training\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Theoretical scaling of recovery compute\"\n    relevance: 7\n    key_finding: \"Recovery training follows predictable scaling with compute and data\"\n    our_relation: \"Informs our recovery budget estimation; we extend to RLVR-specific scaling\"\n    arxiv_id: \"\"\n\n  - id: mipp_2024\n    title: \"MIPP: Mutual Information Preserving Pruning\"\n    year: 2024\n    venue: \"arXiv\"\n    category: background\n    role: \"Information-theoretic pruning criterion\"\n    relevance: 5\n    key_finding: \"Preserving mutual information between layers reduces pruning damage\"\n    our_relation: \"Related theoretical motivation; CKA captures similar functional redundancy\"\n    arxiv_id: \"\"\n\n  - id: redundancy_aware_cnn_2020\n    title: \"Redundancy-Aware Pruning of Convolutional Neural Networks\"\n    year: 2020\n    venue: \"Neural Computation\"\n    category: background\n    role: \"Pioneer of redundancy-based pruning\"\n    relevance: 4\n    key_finding: \"Redundancy metrics guide pruning decisions in CNNs\"\n    our_relation: \"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\"\n    arxiv_id: \"\"\n\n  - id: self_distilled_rlvr_2026\n    title: \"Self-Distilled RLVR\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"RLVR training efficiency improvement\"\n    relevance: 5\n    key_finding: \"Self-distillation stabilizes RLVR training and improves sample efficiency\"\n    our_relation: \"Could improve our RLVR recovery phase efficiency\"\n    arxiv_id: \"2604.03128\"\n\n  - id: diet_2026\n    title: \"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Dimension-wise importance for width pruning\"\n    relevance: 5\n    key_finding: \"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\"\n    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"\n",
      "numLines": 213,
      "startLine": 1,
      "totalLines": 213
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

<details><summary>Logged reasoning block</summary>

```text
Now I need to append the 5 new entries. I'll use Edit to append before the end of the file. Let me add them to the appropriate sections.

New papers to add:
1. dppo_2026 → method-component (rollout pruning for GRPO)
2. arrol_2026 → method-component (rollout pruning for RLVR) 
3. task_neurons_2026 → background (task-specific neurons and recovery)
4. ddp_2026 → background (alternative structured pruning)


5. pruning_vlm_recovery_2026 → background (comprehensive pruning + recovery study)

I'll insert the method-component entries after paser_2025 and the background entries after diet_2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "08df9522-fde8-4928-8126-309e377827e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcyJeKcfNdHHksMkCYVDfi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6979,
      "cache_read_input_tokens": 46806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6979
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_013tPqu6dkedPkKa2DWvzQHz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
  "old_string": "    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  # === Background / Theory ===",
  "new_string": "    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: dppo_2026\n    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Rollout pruning to accelerate GRPO training\"\n    relevance: 5\n    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"\n    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"\n    arxiv_id: \"2603.04135\"\n\n  - id: arrol_2026\n    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Online rollout pruning for RLVR efficiency\"\n    relevance: 5\n    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"\n    our_relation: \"Complementary technique for speeding up RLVR recovery training\"\n    arxiv_id: \"2603.24840\"\n\n  # === Background / Theory ==="
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "bbf4fc93-27fb-481c-b117-9e7e5149e244",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XcyJeKcfNdHHksMkCYVDfi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6979,
      "cache_read_input_tokens": 46806,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6979
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-14T13:29:00.505Z_

<details><summary>↩ Tool result · `toolu_013tPqu6dkedPkKa2DWvzQHz`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "f5bd1200-feef-42ad-b080-98e4add43f08",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
    "oldString": "    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  # === Background / Theory ===",
    "newString": "    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: dppo_2026\n    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Rollout pruning to accelerate GRPO training\"\n    relevance: 5\n    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"\n    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"\n    arxiv_id: \"2603.04135\"\n\n  - id: arrol_2026\n    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Online rollout pruning for RLVR efficiency\"\n    relevance: 5\n    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"\n    our_relation: \"Complementary technique for speeding up RLVR recovery training\"\n    arxiv_id: \"2603.24840\"\n\n  # === Background / Theory ===",
    "originalFile": "papers:\n  # === Direct Competitors ===\n  - id: self_healing_2025\n    title: \"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\"\n    year: 2025\n    venue: \"under review\"\n    category: direct-competitor\n    role: \"RLVR recovery baseline\"\n    relevance: 9\n    key_finding: \"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%\"\n    our_relation: \"We extend beyond single sparsity ratio and add CKA-guided pruning selection\"\n    arxiv_id: \"\"\n\n  - id: resp_2025\n    title: \"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: direct-competitor\n    role: \"Structured pruning for reasoning without recovery\"\n    relevance: 8\n    key_finding: \"GSM8K 81.3% at 40% sparsity via self-reflective importance\"\n    our_relation: \"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\"\n    arxiv_id: \"\"\n\n  - id: grasprune_2026\n    title: \"GRASPrune: Global Gating-based Structural Pruning for LLMs\"\n    year: 2026\n    venue: \"ACL 2026 Main\"\n    category: direct-competitor\n    role: \"SOTA budgeted structural pruning\"\n    relevance: 8\n    key_finding: \"Global gating achieves best structured pruning under budget constraints\"\n    our_relation: \"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\"\n    arxiv_id: \"\"\n\n  - id: opsd_2026\n    title: \"OPSD: One-shot Post-RL Structured Distillation\"\n    year: 2026\n    venue: \"arXiv May 2026\"\n    category: direct-competitor\n    role: \"Post-RL compression via distillation\"\n    relevance: 7\n    key_finding: \"Compress post-RL model in one shot via structured distillation\"\n    our_relation: \"Distillation-based vs our pruning+recovery approach; complementary\"\n    arxiv_id: \"\"\n\n  - id: doing_more_with_less_2026\n    title: \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: direct-competitor\n    role: \"Pruning improves test-time scaling\"\n    relevance: 7\n    key_finding: \"Unstructured pruning can augment test-time scaling; structured pruning degrades it\"\n    our_relation: \"Motivates why structured pruning needs recovery; we address this gap with RLVR\"\n    arxiv_id: \"2604.25098\"\n\n  - id: gprune_llm_2026\n    title: \"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: direct-competitor\n    role: \"Cross-distribution generalization-aware pruning\"\n    relevance: 6\n    key_finding: \"Accounts for neuron cross-distribution behavior; reduces calibration bias\"\n    our_relation: \"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\"\n    arxiv_id: \"2603.13418\"\n\n  # === Method Components ===\n  - id: mpruner_2024\n    title: \"MPruner: CKA-based Inter-layer Pruning for LLMs\"\n    year: 2024\n    venue: \"arXiv\"\n    category: method-component\n    role: \"CKA for layer importance estimation\"\n    relevance: 8\n    key_finding: \"CKA similarity between layers identifies redundant layers for removal\"\n    our_relation: \"We adapt CKA from layer-level to width-level functional overlap prediction\"\n    arxiv_id: \"\"\n\n  - id: lachance_thesis_2024\n    title: \"CKA Layer Similarity for Neural Network Pruning\"\n    year: 2024\n    venue: \"URI Master's Thesis\"\n    category: method-component\n    role: \"CKA-based pruning theoretical foundation\"\n    relevance: 6\n    key_finding: \"CKA layer similarity correlates with pruning recoverability\"\n    our_relation: \"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: bonsai_2025\n    title: \"Bonsai: Gradient-Free Structured Pruning for LLMs\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: method-component\n    role: \"Gradient-free structured pruning alternative\"\n    relevance: 6\n    key_finding: \"Achieves competitive structured pruning without backprop\"\n    our_relation: \"Alternative pruning strategy; our CKA metric is also gradient-free\"\n    arxiv_id: \"\"\n\n  - id: pat_2025\n    title: \"PAT: Pruning-Aware Tuning for LLMs\"\n    year: 2025\n    venue: \"AAAI 2025\"\n    category: method-component\n    role: \"Joint pruning and tuning framework\"\n    relevance: 6\n    key_finding: \"Co-optimizing pruning mask and fine-tuning improves recovery\"\n    our_relation: \"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: rac_2025\n    title: \"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    category: method-component\n    role: \"CoT reconstruction post-pruning\"\n    relevance: 7\n    key_finding: \"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\"\n    our_relation: \"Complementary recovery strategy; could combine with our RLVR approach\"\n    arxiv_id: \"\"\n\n  - id: paser_2025\n    title: \"PASER: Data Selection for Pruning Recovery\"\n    year: 2025\n    venue: \"under review\"\n    category: method-component\n    role: \"Recovery training data selection\"\n    relevance: 6\n    key_finding: \"Selective data for recovery training improves efficiency\"\n    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  # === Background / Theory ===\n  - id: rl_squeezes_2026\n    title: \"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\"\n    year: 2026\n    venue: \"ICLR 2026 Poster\"\n    category: background\n    role: \"Theoretical basis for why RLVR works differently from SFT\"\n    relevance: 8\n    key_finding: \"RLVR compresses representation while SFT expands; different inductive biases\"\n    our_relation: \"Explains why RLVR recovery succeeds where SFT fails post-pruning\"\n    arxiv_id: \"\"\n\n  - id: from_llms_to_lrms_2026\n    title: \"From LLMs to LRMs: Width Pruning is More Robust for Reasoning\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Width vs depth pruning for reasoning\"\n    relevance: 7\n    key_finding: \"Width pruning preserves reasoning better than depth pruning\"\n    our_relation: \"Motivates our focus on width-level structured pruning\"\n    arxiv_id: \"\"\n\n  - id: p2_law_2025\n    title: \"P² Law: Scaling Law for Pruning Recovery Training\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Theoretical scaling of recovery compute\"\n    relevance: 7\n    key_finding: \"Recovery training follows predictable scaling with compute and data\"\n    our_relation: \"Informs our recovery budget estimation; we extend to RLVR-specific scaling\"\n    arxiv_id: \"\"\n\n  - id: mipp_2024\n    title: \"MIPP: Mutual Information Preserving Pruning\"\n    year: 2024\n    venue: \"arXiv\"\n    category: background\n    role: \"Information-theoretic pruning criterion\"\n    relevance: 5\n    key_finding: \"Preserving mutual information between layers reduces pruning damage\"\n    our_relation: \"Related theoretical motivation; CKA captures similar functional redundancy\"\n    arxiv_id: \"\"\n\n  - id: redundancy_aware_cnn_2020\n    title: \"Redundancy-Aware Pruning of Convolutional Neural Networks\"\n    year: 2020\n    venue: \"Neural Computation\"\n    category: background\n    role: \"Pioneer of redundancy-based pruning\"\n    relevance: 4\n    key_finding: \"Redundancy metrics guide pruning decisions in CNNs\"\n    our_relation: \"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\"\n    arxiv_id: \"\"\n\n  - id: self_distilled_rlvr_2026\n    title: \"Self-Distilled RLVR\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"RLVR training efficiency improvement\"\n    relevance: 5\n    key_finding: \"Self-distillation stabilizes RLVR training and improves sample efficiency\"\n    our_relation: \"Could improve our RLVR recovery phase efficiency\"\n    arxiv_id: \"2604.03128\"\n\n  - id: diet_2026\n    title: \"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Dimension-wise importance for width pruning\"\n    relevance: 5\n    key_finding: \"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\"\n    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"\n",
    "structuredPatch": [
      {
        "oldStart": 133,
        "oldLines": 6,
        "newStart": 133,
        "newLines": 28,
        "lines": [
          "     our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"",
          "     arxiv_id: \"\"",
          " ",
          "+  - id: dppo_2026",
          "+    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"",
          "+    year: 2026",
          "+    venue: \"arXiv Mar 2026\"",
          "+    category: method-component",
          "+    role: \"Rollout pruning to accelerate GRPO training\"",
          "+    relevance: 5",
          "+    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"",
          "+    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"",
          "+    arxiv_id: \"2603.04135\"",
          "+",
          "+  - id: arrol_2026",
          "+    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"",
          "+    year: 2026",
          "+    venue: \"arXiv Mar 2026\"",
          "+    category: method-component",
          "+    role: \"Online rollout pruning for RLVR efficiency\"",
          "+    relevance: 5",
          "+    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"",
          "+    our_relation: \"Complementary technique for speeding up RLVR recovery training\"",
          "+    arxiv_id: \"2603.24840\"",
          "+",
          "   # === Background / Theory ===",
          "   - id: rl_squeezes_2026",
          "     title: \"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01Fpmk7RvZBgF22NVFjbJAJL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
  "old_string": "    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"",
  "new_string": "    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"\n\n  - id: task_neurons_2026\n    title: \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Task-specific neuron identification and pruning recovery dynamics\"\n    relevance: 6\n    key_finding: \"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\"\n    our_relation: \"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\"\n    arxiv_id: \"2604.27115\"\n\n  - id: ddp_2026\n    title: \"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Differentiable mask-only structured pruning\"\n    relevance: 5\n    key_finding: \"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\"\n    our_relation: \"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\"\n    arxiv_id: \"2603.08065\"\n\n  - id: pruning_vlm_recovery_2026\n    title: \"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Comprehensive pruning + recovery study for VLMs\"\n    relevance: 5\n    key_finding: \"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; recovery data efficiency matters\"\n    our_relation: \"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\"\n    arxiv_id: \"2604.24380\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "da83b599-c055-45fc-b24e-80743cded6db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSttVnYXrNU73dQynBf8o6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 865,
      "cache_read_input_tokens": 53785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 865
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T13:29:12.622Z_

<details><summary>↩ Tool result · `toolu_01Fpmk7RvZBgF22NVFjbJAJL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "052f2276-4f1a-4f8d-9560-1193f7d1b484",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/literature_map.yaml",
    "oldString": "    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"",
    "newString": "    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"\n\n  - id: task_neurons_2026\n    title: \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Task-specific neuron identification and pruning recovery dynamics\"\n    relevance: 6\n    key_finding: \"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\"\n    our_relation: \"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\"\n    arxiv_id: \"2604.27115\"\n\n  - id: ddp_2026\n    title: \"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Differentiable mask-only structured pruning\"\n    relevance: 5\n    key_finding: \"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\"\n    our_relation: \"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\"\n    arxiv_id: \"2603.08065\"\n\n  - id: pruning_vlm_recovery_2026\n    title: \"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"Comprehensive pruning + recovery study for VLMs\"\n    relevance: 5\n    key_finding: \"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; recovery data efficiency matters\"\n    our_relation: \"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\"\n    arxiv_id: \"2604.24380\"",
    "originalFile": "papers:\n  # === Direct Competitors ===\n  - id: self_healing_2025\n    title: \"Self-Healing: Recovering Pruned Large Reasoning Models via Reinforcement Learning\"\n    year: 2025\n    venue: \"under review\"\n    category: direct-competitor\n    role: \"RLVR recovery baseline\"\n    relevance: 9\n    key_finding: \"RLVR recovers 95%+ at 25% compression; SFT only reaches ~80%\"\n    our_relation: \"We extend beyond single sparsity ratio and add CKA-guided pruning selection\"\n    arxiv_id: \"\"\n\n  - id: resp_2025\n    title: \"RESP: Self-Reflective Structured Pruning for Reasoning LLMs\"\n    year: 2025\n    venue: \"arXiv Dec 2025\"\n    category: direct-competitor\n    role: \"Structured pruning for reasoning without recovery\"\n    relevance: 8\n    key_finding: \"GSM8K 81.3% at 40% sparsity via self-reflective importance\"\n    our_relation: \"No RLVR recovery; we show recovery-aware pruning outperforms at same sparsity\"\n    arxiv_id: \"\"\n\n  - id: grasprune_2026\n    title: \"GRASPrune: Global Gating-based Structural Pruning for LLMs\"\n    year: 2026\n    venue: \"ACL 2026 Main\"\n    category: direct-competitor\n    role: \"SOTA budgeted structural pruning\"\n    relevance: 8\n    key_finding: \"Global gating achieves best structured pruning under budget constraints\"\n    our_relation: \"GRASPrune as pruning backbone; we add CKA overlap + RLVR recovery on top\"\n    arxiv_id: \"\"\n\n  - id: opsd_2026\n    title: \"OPSD: One-shot Post-RL Structured Distillation\"\n    year: 2026\n    venue: \"arXiv May 2026\"\n    category: direct-competitor\n    role: \"Post-RL compression via distillation\"\n    relevance: 7\n    key_finding: \"Compress post-RL model in one shot via structured distillation\"\n    our_relation: \"Distillation-based vs our pruning+recovery approach; complementary\"\n    arxiv_id: \"\"\n\n  - id: doing_more_with_less_2026\n    title: \"Doing More With Less: Revisiting the Effectiveness of LLM Pruning for Test-Time Scaling\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: direct-competitor\n    role: \"Pruning improves test-time scaling\"\n    relevance: 7\n    key_finding: \"Unstructured pruning can augment test-time scaling; structured pruning degrades it\"\n    our_relation: \"Motivates why structured pruning needs recovery; we address this gap with RLVR\"\n    arxiv_id: \"2604.25098\"\n\n  - id: gprune_llm_2026\n    title: \"GPrune-LLM: Generalization-Aware Structured Pruning for Large Language Models\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: direct-competitor\n    role: \"Cross-distribution generalization-aware pruning\"\n    relevance: 6\n    key_finding: \"Accounts for neuron cross-distribution behavior; reduces calibration bias\"\n    our_relation: \"Complementary importance metric; our CKA captures functional overlap vs their generalization gap\"\n    arxiv_id: \"2603.13418\"\n\n  # === Method Components ===\n  - id: mpruner_2024\n    title: \"MPruner: CKA-based Inter-layer Pruning for LLMs\"\n    year: 2024\n    venue: \"arXiv\"\n    category: method-component\n    role: \"CKA for layer importance estimation\"\n    relevance: 8\n    key_finding: \"CKA similarity between layers identifies redundant layers for removal\"\n    our_relation: \"We adapt CKA from layer-level to width-level functional overlap prediction\"\n    arxiv_id: \"\"\n\n  - id: lachance_thesis_2024\n    title: \"CKA Layer Similarity for Neural Network Pruning\"\n    year: 2024\n    venue: \"URI Master's Thesis\"\n    category: method-component\n    role: \"CKA-based pruning theoretical foundation\"\n    relevance: 6\n    key_finding: \"CKA layer similarity correlates with pruning recoverability\"\n    our_relation: \"Validates CKA as signal for pruning decisions; we extend to predict RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: bonsai_2025\n    title: \"Bonsai: Gradient-Free Structured Pruning for LLMs\"\n    year: 2025\n    venue: \"ICML 2025\"\n    category: method-component\n    role: \"Gradient-free structured pruning alternative\"\n    relevance: 6\n    key_finding: \"Achieves competitive structured pruning without backprop\"\n    our_relation: \"Alternative pruning strategy; our CKA metric is also gradient-free\"\n    arxiv_id: \"\"\n\n  - id: pat_2025\n    title: \"PAT: Pruning-Aware Tuning for LLMs\"\n    year: 2025\n    venue: \"AAAI 2025\"\n    category: method-component\n    role: \"Joint pruning and tuning framework\"\n    relevance: 6\n    key_finding: \"Co-optimizing pruning mask and fine-tuning improves recovery\"\n    our_relation: \"Related idea of pruning-tuning interaction; we separate pruning and RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: rac_2025\n    title: \"RAC: Chain-of-Thought Reconstruction for Pruned Reasoning Models\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    category: method-component\n    role: \"CoT reconstruction post-pruning\"\n    relevance: 7\n    key_finding: \"Reconstructing CoT improves unstructured/2:4 pruned reasoning models\"\n    our_relation: \"Complementary recovery strategy; could combine with our RLVR approach\"\n    arxiv_id: \"\"\n\n  - id: paser_2025\n    title: \"PASER: Data Selection for Pruning Recovery\"\n    year: 2025\n    venue: \"under review\"\n    category: method-component\n    role: \"Recovery training data selection\"\n    relevance: 6\n    key_finding: \"Selective data for recovery training improves efficiency\"\n    our_relation: \"Orthogonal contribution; can apply PASER data selection to our RLVR recovery\"\n    arxiv_id: \"\"\n\n  - id: dppo_2026\n    title: \"DPPO: Unbiased Dynamic Pruning for Efficient Group-Based Policy Optimization\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Rollout pruning to accelerate GRPO training\"\n    relevance: 5\n    key_finding: \"Importance-sampling-based rollout pruning achieves 2.37x GRPO speedup with 3.36% accuracy gain on Qwen3-4B\"\n    our_relation: \"Could accelerate our GRPO-based RLVR recovery phase\"\n    arxiv_id: \"2603.04135\"\n\n  - id: arrol_2026\n    title: \"ARRoL: Prune as You Generate — Online Rollout Pruning for Faster and Better RLVR\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: method-component\n    role: \"Online rollout pruning for RLVR efficiency\"\n    relevance: 5\n    key_finding: \"Lightweight quality head predicts rollout success probability for early pruning during RLVR\"\n    our_relation: \"Complementary technique for speeding up RLVR recovery training\"\n    arxiv_id: \"2603.24840\"\n\n  # === Background / Theory ===\n  - id: rl_squeezes_2026\n    title: \"RL Squeezes, SFT Expands: Different Mechanisms in Post-Training\"\n    year: 2026\n    venue: \"ICLR 2026 Poster\"\n    category: background\n    role: \"Theoretical basis for why RLVR works differently from SFT\"\n    relevance: 8\n    key_finding: \"RLVR compresses representation while SFT expands; different inductive biases\"\n    our_relation: \"Explains why RLVR recovery succeeds where SFT fails post-pruning\"\n    arxiv_id: \"\"\n\n  - id: from_llms_to_lrms_2026\n    title: \"From LLMs to LRMs: Width Pruning is More Robust for Reasoning\"\n    year: 2026\n    venue: \"arXiv Jan 2026\"\n    category: background\n    role: \"Width vs depth pruning for reasoning\"\n    relevance: 7\n    key_finding: \"Width pruning preserves reasoning better than depth pruning\"\n    our_relation: \"Motivates our focus on width-level structured pruning\"\n    arxiv_id: \"\"\n\n  - id: p2_law_2025\n    title: \"P² Law: Scaling Law for Pruning Recovery Training\"\n    year: 2025\n    venue: \"ACL 2025\"\n    category: background\n    role: \"Theoretical scaling of recovery compute\"\n    relevance: 7\n    key_finding: \"Recovery training follows predictable scaling with compute and data\"\n    our_relation: \"Informs our recovery budget estimation; we extend to RLVR-specific scaling\"\n    arxiv_id: \"\"\n\n  - id: mipp_2024\n    title: \"MIPP: Mutual Information Preserving Pruning\"\n    year: 2024\n    venue: \"arXiv\"\n    category: background\n    role: \"Information-theoretic pruning criterion\"\n    relevance: 5\n    key_finding: \"Preserving mutual information between layers reduces pruning damage\"\n    our_relation: \"Related theoretical motivation; CKA captures similar functional redundancy\"\n    arxiv_id: \"\"\n\n  - id: redundancy_aware_cnn_2020\n    title: \"Redundancy-Aware Pruning of Convolutional Neural Networks\"\n    year: 2020\n    venue: \"Neural Computation\"\n    category: background\n    role: \"Pioneer of redundancy-based pruning\"\n    relevance: 4\n    key_finding: \"Redundancy metrics guide pruning decisions in CNNs\"\n    our_relation: \"Conceptual ancestor; we apply redundancy-awareness to LLM structured pruning\"\n    arxiv_id: \"\"\n\n  - id: self_distilled_rlvr_2026\n    title: \"Self-Distilled RLVR\"\n    year: 2026\n    venue: \"arXiv Apr 2026\"\n    category: background\n    role: \"RLVR training efficiency improvement\"\n    relevance: 5\n    key_finding: \"Self-distillation stabilizes RLVR training and improves sample efficiency\"\n    our_relation: \"Could improve our RLVR recovery phase efficiency\"\n    arxiv_id: \"2604.03128\"\n\n  - id: diet_2026\n    title: \"DieT: Dimension-wise Global Pruning via Task-specific Importance Score\"\n    year: 2026\n    venue: \"arXiv Mar 2026\"\n    category: background\n    role: \"Dimension-wise importance for width pruning\"\n    relevance: 5\n    key_finding: \"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\"\n    our_relation: \"Alternative width importance metric; we use CKA overlap instead\"\n    arxiv_id: \"2603.23985\"\n",
    "structuredPatch": [
      {
        "oldStart": 232,
        "oldLines": 3,
        "newStart": 232,
        "newLines": 36,
        "lines": [
          "     key_finding: \"Task-specific dimension importance outperforms activation-based metrics at 20-40% sparsity\"",
          "     our_relation: \"Alternative width importance metric; we use CKA overlap instead\"",
          "     arxiv_id: \"2603.23985\"",
          "+",
          "+  - id: task_neurons_2026",
          "+    title: \"Exploring the Limits of Pruning: Task-Specific Neurons, Model Collapse, and Recovery in Task-Specific LLMs\"",
          "+    year: 2026",
          "+    venue: \"arXiv Apr 2026\"",
          "+    category: background",
          "+    role: \"Task-specific neuron identification and pruning recovery dynamics\"",
          "+    relevance: 6",
          "+    key_finding: \"10% task-specific neuron removal causes collapse; 15-20% robustness threshold; fine-tuning substantially recovers\"",
          "+    our_relation: \"Supports need for recovery-aware pruning; our CKA predicts which neurons are functionally critical\"",
          "+    arxiv_id: \"2604.27115\"",
          "+",
          "+  - id: ddp_2026",
          "+    title: \"DDP: Deterministic Differentiable Structured Pruning for Large Language Models\"",
          "+    year: 2026",
          "+    venue: \"arXiv Mar 2026\"",
          "+    category: background",
          "+    role: \"Differentiable mask-only structured pruning\"",
          "+    relevance: 5",
          "+    key_finding: \"Deterministic soft surrogate of l0 constraint eliminates train-test mismatch in differentiable pruning\"",
          "+    our_relation: \"Alternative pruning backbone; mask-only optimization complementary to our CKA-guided selection\"",
          "+    arxiv_id: \"2603.08065\"",
          "+",
          "+  - id: pruning_vlm_recovery_2026",
          "+    title: \"Structural Pruning of Large Vision Language Models: Pruning Dynamics, Recovery, and Data Efficiency\"",
          "+    year: 2026",
          "+    venue: \"arXiv Apr 2026\"",
          "+    category: background",
          "+    role: \"Comprehensive pruning + recovery study for VLMs\"",
          "+    relevance: 5",
          "+    key_finding: \"Width pruning + KD recovery outperforms layer pruning + SFT on VLMs; recovery data efficiency matters\"",
          "+    our_relation: \"Validates width pruning + recovery paradigm; our CKA-guided approach adds prediction of recoverability\"",
          "+    arxiv_id: \"2604.24380\""
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 62_

literature_map.yaml 已更新（+5 篇）。现在写 related_work_notes.md。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "4dd3b5da-a5ea-406a-91bd-68a9dd366faf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkJnuCLyo5cGMbaFYSmooY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 54650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 769
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_015B5ZLpUbMeDxMpryWhk5JQ`</summary>

```json
{
  "todos": [
    {
      "content": "Read current literature_map.yaml",
      "status": "completed",
      "activeForm": "Reading current literature_map.yaml"
    },
    {
      "content": "Search arXiv for new papers (6 keyword groups)",
      "status": "completed",
      "activeForm": "Searching arXiv for new papers"
    },
    {
      "content": "Evaluate and add new papers to literature_map.yaml",
      "status": "completed",
      "activeForm": "Evaluating and adding new papers"
    },
    {
      "content": "Write related_work_notes.md",
      "status": "in_progress",
      "activeForm": "Writing related work notes"
    },
    {
      "content": "Register artifact",
      "status": "pending",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "5f75da60-71ae-4b39-a6e6-6d998419373d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkJnuCLyo5cGMbaFYSmooY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 54650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 769
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-14T13:29:17.922Z_

<details><summary>↩ Tool result · `toolu_015B5ZLpUbMeDxMpryWhk5JQ`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "3d2f80b0-45f9-4834-838c-62246222b492",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "completed",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "in_progress",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "pending",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "completed",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "completed",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "in_progress",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_016nRvYeEGW6BpXRmvoVrT9b`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "ae6f8631-8f90-47e0-9b6b-347b5cb692be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XkJnuCLyo5cGMbaFYSmooY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 54650,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 769
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-14T13:29:18.714Z_

<details><summary>↩ Tool result · `toolu_016nRvYeEGW6BpXRmvoVrT9b`</summary>

```text
_project
correlation_analysis.py
manifest.yaml
mvp_progress_20260514.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "039032a4-9da3-41fd-9620-62fdd1057987",
  "tool_use_result": {
    "stdout": "_project\ncorrelation_analysis.py\nmanifest.yaml\nmvp_progress_20260514.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Write · `toolu_01RayTmDAfYVMbMPNgznuP6g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/related_work_notes.md",
  "content": "# Related Work Notes — RASP (Recovery-Aware Structured Pruning)\n\n> Prepared 2026-05-14. Literature map: 24 papers. Target: EMNLP 2026 ARR May 25.\n\n---\n\n## 1. Structured Pruning for LLMs\n\n**Core methods.** LLM-Pruner (Ma et al., 2023) established the structured pruning pipeline for LLMs: dependency-graph-based group identification → importance scoring → one-shot removal → LoRA recovery. GRASPrune [`grasprune_2026`] advances this with global gating under budget constraints, achieving SOTA at ACL 2026 — we use it as our pruning backbone. GPrune-LLM [`gprune_llm_2026`] addresses calibration bias via cross-distribution neuron behavior partitioning. DieT [`diet_2026`] proposes dimension-wise task-specific importance for width pruning at 20–40% sparsity. DDP [`ddp_2026`] introduces deterministic differentiable mask optimization, eliminating the stochastic train-test mismatch of hard-concrete relaxations. Bonsai [`bonsai_2025`] shows competitive gradient-free structured pruning.\n\n**Pruning for reasoning models.** RESP [`resp_2025`] achieves GSM8K 81.3% at 40% structured sparsity via self-reflective importance, but applies no post-pruning recovery. From LLMs to LRMs [`from_llms_to_lrms_2026`] demonstrates that width pruning preserves reasoning better than depth pruning — motivating our width-level focus. Doing More With Less [`doing_more_with_less_2026`] shows that structured pruning significantly degrades test-time scaling (TTS) performance while unstructured pruning can augment it, directly motivating why structured pruning needs a recovery mechanism.\n\n**Usable claims:**\n- Structured pruning degrades reasoning more than general NLP tasks → [`doing_more_with_less_2026`, `resp_2025`]\n- Width pruning > depth pruning for reasoning preservation → [`from_llms_to_lrms_2026`]\n- Global importance scoring outperforms local → [`grasprune_2026`, `gprune_llm_2026`]\n- Current methods lack recovery-awareness in the pruning decision itself → gap we fill\n\n---\n\n## 2. Post-Pruning Recovery\n\n**RLVR recovery.** Self-Healing [`self_healing_2025`] is our primary baseline: RLVR recovers 95%+ reasoning at 25% compression where SFT only reaches ~80%. This is the first work to apply RL-based recovery to pruned reasoning models, but it operates at a single sparsity ratio without predicting recoverability.\n\n**Alternative recovery strategies.** RAC [`rac_2025`] reconstructs chain-of-thought for pruned reasoning models (NeurIPS 2025), showing CoT-targeted recovery works for unstructured/2:4 sparsity. PASER [`paser_2025`] demonstrates that selective training data improves recovery efficiency. PAT [`pat_2025`] co-optimizes pruning mask and fine-tuning jointly (AAAI 2025). The VLM pruning study [`pruning_vlm_recovery_2026`] finds that width pruning + KD recovery outperforms layer pruning + SFT, validating our paradigm choice.\n\n**Scaling and theory.** P² Law [`p2_law_2025`] establishes predictable scaling for recovery compute/data (ACL 2025) — we extend this to RLVR-specific scaling. RL Squeezes, SFT Expands [`rl_squeezes_2026`] (ICLR 2026) provides the theoretical basis: RLVR compresses representations while SFT expands them, explaining why RLVR is the superior recovery mechanism post-pruning.\n\n**Task-specific neuron dynamics.** Task-specific neuron analysis [`task_neurons_2026`] finds that removing just ~10% of task-critical neurons causes complete performance collapse, with a robustness threshold at 15–20%. Fine-tuning substantially recovers performance across pruning levels — supporting the need for recovery-aware pruning that identifies which neurons are critical.\n\n**Usable claims:**\n- RLVR >> SFT for post-pruning recovery → [`self_healing_2025`]\n- RLVR compresses representations (theoretical justification) → [`rl_squeezes_2026`]\n- Recovery compute follows scaling laws → [`p2_law_2025`]\n- Task-specific neurons exist; small removal causes collapse → [`task_neurons_2026`]\n- No prior work predicts recoverability before pruning → gap we fill\n\n---\n\n## 3. CKA in Neural Networks\n\n**Layer-level CKA for pruning.** MPruner [`mpruner_2024`] uses CKA similarity between consecutive layers to identify redundant layers for removal, achieving 50% parameter reduction with minimal accuracy loss. Lachance's thesis [`lachance_thesis_2024`] provides theoretical grounding that CKA layer similarity correlates with pruning recoverability. MIPP [`mipp_2024`] uses mutual information (related to CKA) as a pruning criterion.\n\n**Our extension.** We adapt CKA from layer-level redundancy detection to width-level functional overlap prediction. Specifically, we compute CKA between pre- and post-pruning intermediate representations to predict whether RLVR can recover the pruned model — a novel application of CKA as a recoverability signal rather than an importance signal.\n\n**Usable claims:**\n- CKA identifies redundant layers → [`mpruner_2024`]\n- CKA correlates with recoverability → [`lachance_thesis_2024`]\n- No prior work uses CKA for width-level recoverability prediction → our contribution\n\n---\n\n## 4. RLVR / Reasoning Enhancement\n\n**RLVR foundations.** RL Squeezes [`rl_squeezes_2026`] shows RLVR and SFT have fundamentally different mechanisms (compression vs expansion). Self-Distilled RLVR [`self_distilled_rlvr_2026`] improves RLVR training stability and sample efficiency via self-distillation. OPSD [`opsd_2026`] compresses post-RL models via one-shot structured distillation — a complementary approach to our pruning+recovery pipeline.\n\n**RLVR training efficiency.** DPPO [`dppo_2026`] achieves 2.37× GRPO speedup via importance-sampling-based rollout pruning while preserving unbiased gradients. ARRoL [`arrol_2026`] uses a lightweight quality head to predict and prune low-value rollouts during RLVR generation. Both are complementary to our work — they could accelerate the GRPO recovery phase in RASP.\n\n**Usable claims:**\n- RLVR compresses while SFT expands → [`rl_squeezes_2026`]\n- GRPO training can be accelerated 2× without accuracy loss → [`dppo_2026`, `arrol_2026`]\n- Post-RL distillation is complementary to pruning+recovery → [`opsd_2026`]\n\n---\n\n## 5. Our Positioning: RASP Fills the Gap\n\n### Gap analysis\n\nThe literature reveals a clear gap at the intersection of three directions:\n\n1. **Structured pruning for LLMs** is mature (GRASPrune, GPrune-LLM, Bonsai, DDP) but no method accounts for post-pruning recoverability when making pruning decisions.\n2. **Post-pruning recovery** via RLVR is demonstrated (Self-Healing) but operates as a black-box second stage — the pruning step is unaware of whether the removed structures can be recovered.\n3. **CKA-based analysis** has been applied to layer-level redundancy (MPruner) but never to predict width-level recoverability under RLVR.\n\n### RASP's contribution\n\nRASP bridges these three threads by introducing CKA functional overlap as a predictive signal for RLVR recoverability. Concretely:\n\n- **Before pruning:** We compute CKA overlap between candidate pruning configurations and the full model to estimate how much functional capacity is preserved. High CKA overlap → the pruned model retains the representational substrate that RLVR can rebuild upon.\n- **During pruning:** CKA scores guide which structures to remove, preferring configurations that maximize predicted recoverability at the target sparsity ratio.\n- **After pruning:** RLVR (specifically GRPO) recovers reasoning capability, and we show that CKA-guided pruning requires less recovery compute than importance-only pruning.\n\nThis is distinct from: (a) Self-Healing, which uses RLVR recovery but with standard importance-based pruning; (b) RESP/GRASPrune, which optimize pruning quality without considering recovery; (c) MPruner, which uses CKA for layer redundancy, not width-level recoverability.\n\n### Narrative for Related Work section\n\nWe position RASP as the first method to close the loop between pruning and recovery by making the pruning decision recovery-aware. While prior work treats pruning and recovery as independent stages (prune first, recover later), RASP shows that predicting recoverability — via CKA functional overlap — at the pruning stage yields better final accuracy at the same sparsity ratio and recovery budget. This is analogous to how PAT co-optimizes pruning and tuning, but RASP operates at a higher level: it does not require joint optimization, instead using CKA as a cheap predictive proxy that can be computed before any training begins.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "45262faf-33b5-4f9b-8eab-34fa06121110",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bnxfic5q9T6Dxyzg9Dew5M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 55419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 446
      },
      "output_tokens": 70,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T13:30:12.261Z_

<details><summary>↩ Tool result · `toolu_01RayTmDAfYVMbMPNgznuP6g`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/related_work_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "1a0dc453-b995-4f33-bdbd-5734d3b4a93f",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/related_work_notes.md",
    "content": "# Related Work Notes — RASP (Recovery-Aware Structured Pruning)\n\n> Prepared 2026-05-14. Literature map: 24 papers. Target: EMNLP 2026 ARR May 25.\n\n---\n\n## 1. Structured Pruning for LLMs\n\n**Core methods.** LLM-Pruner (Ma et al., 2023) established the structured pruning pipeline for LLMs: dependency-graph-based group identification → importance scoring → one-shot removal → LoRA recovery. GRASPrune [`grasprune_2026`] advances this with global gating under budget constraints, achieving SOTA at ACL 2026 — we use it as our pruning backbone. GPrune-LLM [`gprune_llm_2026`] addresses calibration bias via cross-distribution neuron behavior partitioning. DieT [`diet_2026`] proposes dimension-wise task-specific importance for width pruning at 20–40% sparsity. DDP [`ddp_2026`] introduces deterministic differentiable mask optimization, eliminating the stochastic train-test mismatch of hard-concrete relaxations. Bonsai [`bonsai_2025`] shows competitive gradient-free structured pruning.\n\n**Pruning for reasoning models.** RESP [`resp_2025`] achieves GSM8K 81.3% at 40% structured sparsity via self-reflective importance, but applies no post-pruning recovery. From LLMs to LRMs [`from_llms_to_lrms_2026`] demonstrates that width pruning preserves reasoning better than depth pruning — motivating our width-level focus. Doing More With Less [`doing_more_with_less_2026`] shows that structured pruning significantly degrades test-time scaling (TTS) performance while unstructured pruning can augment it, directly motivating why structured pruning needs a recovery mechanism.\n\n**Usable claims:**\n- Structured pruning degrades reasoning more than general NLP tasks → [`doing_more_with_less_2026`, `resp_2025`]\n- Width pruning > depth pruning for reasoning preservation → [`from_llms_to_lrms_2026`]\n- Global importance scoring outperforms local → [`grasprune_2026`, `gprune_llm_2026`]\n- Current methods lack recovery-awareness in the pruning decision itself → gap we fill\n\n---\n\n## 2. Post-Pruning Recovery\n\n**RLVR recovery.** Self-Healing [`self_healing_2025`] is our primary baseline: RLVR recovers 95%+ reasoning at 25% compression where SFT only reaches ~80%. This is the first work to apply RL-based recovery to pruned reasoning models, but it operates at a single sparsity ratio without predicting recoverability.\n\n**Alternative recovery strategies.** RAC [`rac_2025`] reconstructs chain-of-thought for pruned reasoning models (NeurIPS 2025), showing CoT-targeted recovery works for unstructured/2:4 sparsity. PASER [`paser_2025`] demonstrates that selective training data improves recovery efficiency. PAT [`pat_2025`] co-optimizes pruning mask and fine-tuning jointly (AAAI 2025). The VLM pruning study [`pruning_vlm_recovery_2026`] finds that width pruning + KD recovery outperforms layer pruning + SFT, validating our paradigm choice.\n\n**Scaling and theory.** P² Law [`p2_law_2025`] establishes predictable scaling for recovery compute/data (ACL 2025) — we extend this to RLVR-specific scaling. RL Squeezes, SFT Expands [`rl_squeezes_2026`] (ICLR 2026) provides the theoretical basis: RLVR compresses representations while SFT expands them, explaining why RLVR is the superior recovery mechanism post-pruning.\n\n**Task-specific neuron dynamics.** Task-specific neuron analysis [`task_neurons_2026`] finds that removing just ~10% of task-critical neurons causes complete performance collapse, with a robustness threshold at 15–20%. Fine-tuning substantially recovers performance across pruning levels — supporting the need for recovery-aware pruning that identifies which neurons are critical.\n\n**Usable claims:**\n- RLVR >> SFT for post-pruning recovery → [`self_healing_2025`]\n- RLVR compresses representations (theoretical justification) → [`rl_squeezes_2026`]\n- Recovery compute follows scaling laws → [`p2_law_2025`]\n- Task-specific neurons exist; small removal causes collapse → [`task_neurons_2026`]\n- No prior work predicts recoverability before pruning → gap we fill\n\n---\n\n## 3. CKA in Neural Networks\n\n**Layer-level CKA for pruning.** MPruner [`mpruner_2024`] uses CKA similarity between consecutive layers to identify redundant layers for removal, achieving 50% parameter reduction with minimal accuracy loss. Lachance's thesis [`lachance_thesis_2024`] provides theoretical grounding that CKA layer similarity correlates with pruning recoverability. MIPP [`mipp_2024`] uses mutual information (related to CKA) as a pruning criterion.\n\n**Our extension.** We adapt CKA from layer-level redundancy detection to width-level functional overlap prediction. Specifically, we compute CKA between pre- and post-pruning intermediate representations to predict whether RLVR can recover the pruned model — a novel application of CKA as a recoverability signal rather than an importance signal.\n\n**Usable claims:**\n- CKA identifies redundant layers → [`mpruner_2024`]\n- CKA correlates with recoverability → [`lachance_thesis_2024`]\n- No prior work uses CKA for width-level recoverability prediction → our contribution\n\n---\n\n## 4. RLVR / Reasoning Enhancement\n\n**RLVR foundations.** RL Squeezes [`rl_squeezes_2026`] shows RLVR and SFT have fundamentally different mechanisms (compression vs expansion). Self-Distilled RLVR [`self_distilled_rlvr_2026`] improves RLVR training stability and sample efficiency via self-distillation. OPSD [`opsd_2026`] compresses post-RL models via one-shot structured distillation — a complementary approach to our pruning+recovery pipeline.\n\n**RLVR training efficiency.** DPPO [`dppo_2026`] achieves 2.37× GRPO speedup via importance-sampling-based rollout pruning while preserving unbiased gradients. ARRoL [`arrol_2026`] uses a lightweight quality head to predict and prune low-value rollouts during RLVR generation. Both are complementary to our work — they could accelerate the GRPO recovery phase in RASP.\n\n**Usable claims:**\n- RLVR compresses while SFT expands → [`rl_squeezes_2026`]\n- GRPO training can be accelerated 2× without accuracy loss → [`dppo_2026`, `arrol_2026`]\n- Post-RL distillation is complementary to pruning+recovery → [`opsd_2026`]\n\n---\n\n## 5. Our Positioning: RASP Fills the Gap\n\n### Gap analysis\n\nThe literature reveals a clear gap at the intersection of three directions:\n\n1. **Structured pruning for LLMs** is mature (GRASPrune, GPrune-LLM, Bonsai, DDP) but no method accounts for post-pruning recoverability when making pruning decisions.\n2. **Post-pruning recovery** via RLVR is demonstrated (Self-Healing) but operates as a black-box second stage — the pruning step is unaware of whether the removed structures can be recovered.\n3. **CKA-based analysis** has been applied to layer-level redundancy (MPruner) but never to predict width-level recoverability under RLVR.\n\n### RASP's contribution\n\nRASP bridges these three threads by introducing CKA functional overlap as a predictive signal for RLVR recoverability. Concretely:\n\n- **Before pruning:** We compute CKA overlap between candidate pruning configurations and the full model to estimate how much functional capacity is preserved. High CKA overlap → the pruned model retains the representational substrate that RLVR can rebuild upon.\n- **During pruning:** CKA scores guide which structures to remove, preferring configurations that maximize predicted recoverability at the target sparsity ratio.\n- **After pruning:** RLVR (specifically GRPO) recovers reasoning capability, and we show that CKA-guided pruning requires less recovery compute than importance-only pruning.\n\nThis is distinct from: (a) Self-Healing, which uses RLVR recovery but with standard importance-based pruning; (b) RESP/GRASPrune, which optimize pruning quality without considering recovery; (c) MPruner, which uses CKA for layer redundancy, not width-level recoverability.\n\n### Narrative for Related Work section\n\nWe position RASP as the first method to close the loop between pruning and recovery by making the pruning decision recovery-aware. While prior work treats pruning and recovery as independent stages (prune first, recover later), RASP shows that predicting recoverability — via CKA functional overlap — at the pruning stage yields better final accuracy at the same sparsity ratio and recovery budget. This is analogous to how PAT co-optimizes pruning and tuning, but RASP operates at a higher level: it does not require joint optimization, instead using CKA as a cheap predictive proxy that can be computed before any training begins.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 69_

Now registering the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "2f8a339c-68c7-47ea-a4e1-013a3fbece6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsppRvxzxnyVxCbk5ajgch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 55865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2542
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Gdw46HV4xaSW3dg6fXNszR`</summary>

```json
{
  "todos": [
    {
      "content": "Read current literature_map.yaml",
      "status": "completed",
      "activeForm": "Reading current literature_map.yaml"
    },
    {
      "content": "Search arXiv for new papers (6 keyword groups)",
      "status": "completed",
      "activeForm": "Searching arXiv for new papers"
    },
    {
      "content": "Evaluate and add new papers to literature_map.yaml",
      "status": "completed",
      "activeForm": "Evaluating and adding new papers"
    },
    {
      "content": "Write related_work_notes.md",
      "status": "completed",
      "activeForm": "Writing related work notes"
    },
    {
      "content": "Register artifact",
      "status": "in_progress",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "7baa4aac-a07b-41fa-a4a3-e3afc1132019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsppRvxzxnyVxCbk5ajgch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 55865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2542
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-14T13:30:16.232Z_

<details><summary>↩ Tool result · `toolu_01Gdw46HV4xaSW3dg6fXNszR`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "5d505e11-a2dc-4c70-bea6-53d169cf87d2",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "completed",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "completed",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "in_progress",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "pending",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "completed",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "completed",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "completed",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "in_progress",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DeAbuNsuE1GUeCdqQ3s31h`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "d16f9b16-d2eb-49bb-9cf2-24b1a2915abf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TsppRvxzxnyVxCbk5ajgch",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2542,
      "cache_read_input_tokens": 55865,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2542
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T13:30:16.539Z_

<details><summary>↩ Tool result · `toolu_01DeAbuNsuE1GUeCdqQ3s31h`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "d61a9529-ae26-4940-9c8d-c7c9ce5edf5c",
  "tool_use_result": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01FUPFR1UuW1Rtt1AYUiS7bZ`</summary>

```json
{
  "query": "register artifact",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "8d29f347-0160-441d-b650-1a11b1599864",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUeaiWxnLmAvkLR1pFtmfo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 388,
      "cache_read_input_tokens": 58407,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 388
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-14T13:30:18.983Z_

<details><summary>↩ Tool result · `toolu_01FUPFR1UuW1Rtt1AYUiS7bZ`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "0a2157fa-79e7-42c4-b109-ff492092d36b",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QtHKWhigDNUDotdCkQMfQm`</summary>

```json
{
  "query": "artifact register save project",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "e3f615d5-15ae-473e-b3da-c23d0682835e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C9BjuU8Dd57TnrUnt55u6m",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 91,
      "cache_read_input_tokens": 58795,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 91
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-14T13:30:21.985Z_

<details><summary>↩ Tool result · `toolu_01QtHKWhigDNUDotdCkQMfQm`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "EnterWorktree"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "de7e1eee-cf38-4583-9199-429440190209",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file",
      "EnterWorktree",
      "TodoWrite",
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "artifact register save project",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
The `register_artifact` tool doesn't seem to be available as a deferred tool. Let me check the manifest.yaml to see how artifacts are registered, or try to find the tool another way.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "8ad99c3e-842b-4007-bd0a-e4106f06d5c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9RdUmdvEjHFGrhjwJWrxF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4013,
      "cache_read_input_tokens": 58886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4013
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KGnewyfQvfNeHWhLbXiFiy`</summary>

```json
{
  "query": "register",
  "max_results": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "7f6aa970-00ce-4914-b2b7-5cad1284586d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9RdUmdvEjHFGrhjwJWrxF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4013,
      "cache_read_input_tokens": 58886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4013
      },
      "output_tokens": 0,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-14T13:30:26.305Z_

<details><summary>↩ Tool result · `toolu_01KGnewyfQvfNeHWhLbXiFiy`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "70b944f4-0dda-44f5-9640-4c9ae5859bc6",
  "tool_use_result": {
    "matches": [],
    "query": "register",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Read · `toolu_01L53bRzFWZQSYj1ya25HrXT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "23ddff3f-305f-44a8-96ef-961f41f242fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L2abLA3dDxMx6b6Zh3a4YB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 149,
      "cache_read_input_tokens": 62899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 149
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-14T13:30:30.393Z_

<details><summary>↩ Tool result · `toolu_01L53bRzFWZQSYj1ya25HrXT`</summary>

```text
1	- id: art_20260514_40be48
2	  name: model_utils.py
3	  type: intermediate
4	  description: 通用剪枝模型加载函数，处理非均匀 MLP 维度，eval/train/analysis 共用
5	  path: projects/recovery_aware_struct_prune/artifacts/_project/intermediate/model_utils_info.txt
6	  url: null
7	  project: recovery_aware_struct_prune
8	  exp_id: null
9	  skill: ''
10	  created_at: '2026-05-14T06:44:40.783508+00:00'
11	  tags: []
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "661f1978-d2e9-416b-afb1-825f76e55a34",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml",
      "content": "- id: art_20260514_40be48\n  name: model_utils.py\n  type: intermediate\n  description: 通用剪枝模型加载函数，处理非均匀 MLP 维度，eval/train/analysis 共用\n  path: projects/recovery_aware_struct_prune/artifacts/_project/intermediate/model_utils_info.txt\n  url: null\n  project: recovery_aware_struct_prune\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Assistant

_source line 83_

<details><summary>Logged reasoning block</summary>

```text
I see the manifest.yaml format. I'll append an entry for the related_work_notes.md artifact. Let me add it to the manifest.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "866fbdf4-f910-4c71-a370-d0e4c3fc123b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hte1iD9wbWnog6uZQkuS4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 63048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Edit · `toolu_01NEJL4soq4cAupem1WV3bJY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml",
  "old_string": "  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []",
  "new_string": "  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []\n- id: art_20260514_rw_notes\n  name: related_work_notes.md\n  type: document\n  description: Related Work 素材笔记，按5个主题组织24篇文献，含可用claims和RASP定位narrative\n  path: projects/recovery_aware_struct_prune/artifacts/related_work_notes.md\n  url: null\n  project: recovery_aware_struct_prune\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T12:00:00.000000+00:00'\n  tags: [literature, related-work, writing]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "72af184f-a28d-4345-b5ae-35519b90a822",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hte1iD9wbWnog6uZQkuS4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 63048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-14T13:30:37.691Z_

<details><summary>↩ Tool result · `toolu_01NEJL4soq4cAupem1WV3bJY`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "5ca035fd-190c-44d3-8cdb-a5c23d426f1d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/artifacts/manifest.yaml",
    "oldString": "  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []",
    "newString": "  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []\n- id: art_20260514_rw_notes\n  name: related_work_notes.md\n  type: document\n  description: Related Work 素材笔记，按5个主题组织24篇文献，含可用claims和RASP定位narrative\n  path: projects/recovery_aware_struct_prune/artifacts/related_work_notes.md\n  url: null\n  project: recovery_aware_struct_prune\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T12:00:00.000000+00:00'\n  tags: [literature, related-work, writing]",
    "originalFile": "- id: art_20260514_40be48\n  name: model_utils.py\n  type: intermediate\n  description: 通用剪枝模型加载函数，处理非均匀 MLP 维度，eval/train/analysis 共用\n  path: projects/recovery_aware_struct_prune/artifacts/_project/intermediate/model_utils_info.txt\n  url: null\n  project: recovery_aware_struct_prune\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-14T06:44:40.783508+00:00'\n  tags: []\n",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 3,
        "newStart": 9,
        "newLines": 14,
        "lines": [
          "   skill: ''",
          "   created_at: '2026-05-14T06:44:40.783508+00:00'",
          "   tags: []",
          "+- id: art_20260514_rw_notes",
          "+  name: related_work_notes.md",
          "+  type: document",
          "+  description: Related Work 素材笔记，按5个主题组织24篇文献，含可用claims和RASP定位narrative",
          "+  path: projects/recovery_aware_struct_prune/artifacts/related_work_notes.md",
          "+  url: null",
          "+  project: recovery_aware_struct_prune",
          "+  exp_id: null",
          "+  skill: ''",
          "+  created_at: '2026-05-14T12:00:00.000000+00:00'",
          "+  tags: [literature, related-work, writing]"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01XDcUhVPUF6PscuFPb83HAU`</summary>

```json
{
  "todos": [
    {
      "content": "Read current literature_map.yaml",
      "status": "completed",
      "activeForm": "Reading current literature_map.yaml"
    },
    {
      "content": "Search arXiv for new papers (6 keyword groups)",
      "status": "completed",
      "activeForm": "Searching arXiv for new papers"
    },
    {
      "content": "Evaluate and add new papers to literature_map.yaml",
      "status": "completed",
      "activeForm": "Evaluating and adding new papers"
    },
    {
      "content": "Write related_work_notes.md",
      "status": "completed",
      "activeForm": "Writing related work notes"
    },
    {
      "content": "Register artifact",
      "status": "completed",
      "activeForm": "Registering artifact"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "d3752ccb-eedf-4f6e-b14f-ac4d1448e74b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01URRrG4wFovHLUyv2NGDwPE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 466,
      "cache_read_input_tokens": 63327,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 466
      },
      "output_tokens": 39,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-14T13:30:41.958Z_

<details><summary>↩ Tool result · `toolu_01XDcUhVPUF6PscuFPb83HAU`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "43ab82d1-3c61-4e1b-95ca-7b7846746a48",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "completed",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "completed",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "completed",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "in_progress",
        "activeForm": "Registering artifact"
      }
    ],
    "newTodos": [
      {
        "content": "Read current literature_map.yaml",
        "status": "completed",
        "activeForm": "Reading current literature_map.yaml"
      },
      {
        "content": "Search arXiv for new papers (6 keyword groups)",
        "status": "completed",
        "activeForm": "Searching arXiv for new papers"
      },
      {
        "content": "Evaluate and add new papers to literature_map.yaml",
        "status": "completed",
        "activeForm": "Evaluating and adding new papers"
      },
      {
        "content": "Write related_work_notes.md",
        "status": "completed",
        "activeForm": "Writing related work notes"
      },
      {
        "content": "Register artifact",
        "status": "completed",
        "activeForm": "Registering artifact"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 88_

完成。总结：

### literature_map.yaml 更新（19 → 24 篇）

新增 5 篇论文：

| ID | 标题 | 年份 | 类别 | 相关度 |
|---|---|---|---|---|
| `dppo_2026` | DPPO: Unbiased Dynamic Pruning for GRPO | 2026.03 | method-component | 5 |
| `arrol_2026` | ARRoL: Online Rollout Pruning for RLVR | 2026.03 | method-component | 5 |
| `task_neurons_2026` | Task-Specific Neurons, Model Collapse, and Recovery | 2026.04 | background | 6 |
| `ddp_2026` | Deterministic Differentiable Structured Pruning | 2026.03 | background | 5 |
| `pruning_vlm_recovery_2026` | Structural Pruning of VLMs: Dynamics, Recovery, Data Efficiency | 2026.04 | background | 5 |

**未入选但值得关注的论文：**
- STOP (2605.13165) — 剪裁推理 trace 而非模型权重，与 RASP 问题不同
- UniComp (2602.09130) — 通用压缩评估框架，relevance 4
- SlimLLM (2505.22689) — 结构化剪枝+线性回归恢复，2025 年 5 月，信息不足未入

**搜索未发现的空白：** 无论文同时使用 CKA + width pruning + RLVR recovery，确认 RASP 的 novelty 仍然成立。

### 产出文件
- `literature_map.yaml` — 已更新
- `artifacts/related_work_notes.md` — 5 个 subsection + usable claims + RASP 定位 narrative

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "uuid": "7d9f55fe-3b6f-4a9c-94df-5467356b1991",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VUqPkjAmSPugFHkMQJiniu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 255,
      "cache_read_input_tokens": 63793,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 255
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 89_

完成。总结：

### literature_map.yaml 更新（19 → 24 篇）

新增 5 篇论文：

| ID | 标题 | 年份 | 类别 | 相关度 |
|---|---|---|---|---|
| `dppo_2026` | DPPO: Unbiased Dynamic Pruning for GRPO | 2026.03 | method-component | 5 |
| `arrol_2026` | ARRoL: Online Rollout Pruning for RLVR | 2026.03 | method-component | 5 |
| `task_neurons_2026` | Task-Specific Neurons, Model Collapse, and Recovery | 2026.04 | background | 6 |
| `ddp_2026` | Deterministic Differentiable Structured Pruning | 2026.03 | background | 5 |
| `pruning_vlm_recovery_2026` | Structural Pruning of VLMs: Dynamics, Recovery, Data Efficiency | 2026.04 | background | 5 |

**未入选但值得关注的论文：**
- STOP (2605.13165) — 剪裁推理 trace 而非模型权重，与 RASP 问题不同
- UniComp (2602.09130) — 通用压缩评估框架，relevance 4
- SlimLLM (2505.22689) — 结构化剪枝+线性回归恢复，2025 年 5 月，信息不足未入

**搜索未发现的空白：** 无论文同时使用 CKA + width pruning + RLVR recovery，确认 RASP 的 novelty 仍然成立。

### 产出文件
- `literature_map.yaml` — 已更新
- `artifacts/related_work_notes.md` — 5 个 subsection + usable claims + RASP 定位 narrative

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 275217,
  "duration_api_ms": 357801,
  "num_turns": 35,
  "stop_reason": "end_turn",
  "session_id": "7ebab749-9e79-4cc0-bdcb-ff6af6ba58d2",
  "total_cost_usd": 1.53402025,
  "usage": {
    "input_tokens": 1933,
    "cache_creation_input_tokens": 52207,
    "cache_read_input_tokens": 870935,
    "output_tokens": 13499,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 52207,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 518,
        "cache_read_input_tokens": 63793,
        "cache_creation_input_tokens": 255,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 255
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 241039,
      "outputTokens": 6816,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 15,
      "costUSD": 0.425119,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1933,
      "outputTokens": 13499,
      "cacheReadInputTokens": 870935,
      "cacheCreationInputTokens": 52207,
      "webSearchRequests": 0,
      "costUSD": 1.10890125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "89b9c1cd-7323-4e56-86a8-c7a5900cf064"
}
```

</details>

---
