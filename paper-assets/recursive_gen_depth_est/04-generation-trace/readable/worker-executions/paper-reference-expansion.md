# paper reference expansion

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_paper_reference_expansion_20260517T170455.log`
- **Structured JSON:** [`f9df2537193349378c45.json`](../../sessions/f9/f9df2537193349378c45.json)

## Before a recorded user message

60 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est",
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
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
  "uuid": "5151a479-5582-4cf6-996d-e297b595d8aa",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-2-projects-recursive-gen-depth-est/memory/"
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
    "resetsAt": 1779052200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "79ffd52b-1a45-460f-ad91-8d52bde58bfe",
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the current state of the paper's references and related work. I'll read the bib file, related work tex file, and the literature map in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "9d493a88-d7db-46d0-a3bb-d559fbc03464",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pq8PBU6UaEVp27NaGh3o9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13414,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13414
      },
      "output_tokens": 26,
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

I'll start by reading the current bib file, related work, and literature map in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "c3bd28d8-13fb-48e7-ba20-b5ab7547ecd2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pq8PBU6UaEVp27NaGh3o9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13414,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13414
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — Glob · `toolu_017EdiNfGNyztSDJCfNZkkoy`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "e9a4a2e4-291d-49ae-ac96-8b2b5751fa3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pq8PBU6UaEVp27NaGh3o9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13414,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13414
      },
      "output_tokens": 26,
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

_source line 7 · 2026-05-17T17:05:08.079Z_

<details><summary>↩ Tool result · reported error · `toolu_017EdiNfGNyztSDJCfNZkkoy`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "5bfd3536-c2a6-4e3e-bf81-97dfa3d1a124",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est."
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_018JyxKgaeukaaUpW8KaZRTA`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "2e557dd0-5591-4945-8c8a-a21c9b7c45fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pq8PBU6UaEVp27NaGh3o9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13414,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13414
      },
      "output_tokens": 26,
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

_source line 9 · 2026-05-17T17:05:09.041Z_

<details><summary>↩ Tool result · reported error · `toolu_018JyxKgaeukaaUpW8KaZRTA`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "91d7c120-e92f-4fad-8c01-a0507f1d031e",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est."
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01PgGUJSMujCnsVWKJcvtckr`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "c078aa47-b237-4d67-9fc1-627c99d7ae33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Pq8PBU6UaEVp27NaGh3o9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13414,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13414
      },
      "output_tokens": 26,
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

_source line 11 · 2026-05-17T17:05:09.408Z_

<details><summary>↩ Tool result · `toolu_01PgGUJSMujCnsVWKJcvtckr`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "762405f7-bac0-49be-9a2b-315b2f0743d9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The paper directory doesn't exist at that path. Let me find where the paper files actually are.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "05b62f36-9a31-40a8-8528-2f355d745a97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lu5ZxLAHPKDKdoeBeGKh1d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 25255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
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

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01NF2CkiPupUcjG7Ha84mg1y`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "d0979b45-624a-440a-a391-0ee76ce995da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lu5ZxLAHPKDKdoeBeGKh1d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 25255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
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

_source line 14 · 2026-05-17T17:05:12.717Z_

<details><summary>↩ Tool result · `toolu_01NF2CkiPupUcjG7Ha84mg1y`</summary>

```text
artifacts/_project/paper/references.bib
docs/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "30210c36-1ee2-404a-84e3-9e7f373af477",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references.bib",
      "docs/paper/references.bib"
    ],
    "durationMs": 14,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_01QepMytiHBEgMfYVZCPBwFt`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "4020fe69-dce9-4241-884b-937df659fa30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lu5ZxLAHPKDKdoeBeGKh1d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 25255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
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

_source line 16 · 2026-05-17T17:05:13.677Z_

<details><summary>↩ Tool result · `toolu_01QepMytiHBEgMfYVZCPBwFt`</summary>

```text
artifacts/dream_reports/dream_20260514T140607/best/paper.tex
artifacts/dream_reports/dream_20260514T140607/median/paper.tex
artifacts/dream_reports/dream_20260514T140607/worst/paper.tex
docs/paper/main.tex
artifacts/dream_reports/dream_20260517T075852/best/paper.tex
artifacts/dream_reports/dream_20260517T075852/median/paper.tex
artifacts/dream_reports/dream_20260517T075852/worst/paper.tex
docs/paper/related_work.tex
artifacts/_project/paper/theory_draft.tex
docs/paper/atlas.tex
docs/paper/discussion.tex
docs/paper/method.tex
docs/paper/generalization.tex
docs/paper/conclusion.tex
docs/paper/section_appendix.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/theory_draft.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "449e0b9d-b887-4188-92c5-a8eec14ef273",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260514T140607/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T140607/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T140607/worst/paper.tex",
      "docs/paper/main.tex",
      "artifacts/dream_reports/dream_20260517T075852/best/paper.tex",
      "artifacts/dream_reports/dream_20260517T075852/median/paper.tex",
      "artifacts/dream_reports/dream_20260517T075852/worst/paper.tex",
      "docs/paper/related_work.tex",
      "artifacts/_project/paper/theory_draft.tex",
      "docs/paper/atlas.tex",
      "docs/paper/discussion.tex",
      "docs/paper/method.tex",
      "docs/paper/generalization.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/section_appendix.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "artifacts/theory_draft.tex"
    ],
    "durationMs": 19,
    "numFiles": 18,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01B8HZYnVdiAgBALwoFNKJc8`</summary>

```json
{
  "project": "recursive_gen_depth_est",
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
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "92746461-b73a-448d-a3a3-7a5152aa918f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lu5ZxLAHPKDKdoeBeGKh1d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 912,
      "cache_read_input_tokens": 25255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 912
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

_source line 18 · 2026-05-17T17:05:14.063Z_

<details><summary>↩ Tool result · `toolu_01B8HZYnVdiAgBALwoFNKJc8`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml\", \"content\": \"# Literature Map — recursive_gen_depth_est\\n# Last updated: 2026-05-15\\n# Purpose: Systematic reference tracking for EMNLP ARR May 25 submission\\n# Total entries: 43 (35 original + 8 R2-N2 supplement)\\n#\\n# Tags used for cite_in: introduction, related-work, background, method,\\n#   experiments, discussion, limitations, dcol-section\\n\\n# =============================================================\\n# MODEL COLLAPSE — foundational theory & recursive generation\\n# =============================================================\\n\\nshumailov2024_nature:\\n  title: \\\"AI models collapse when trained on recursively generated data\\\"\\n  authors: [Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal]\\n  venue: Nature\\n  year: 2024\\n  doi: \\\"10.1038/s41586-024-07566-y\\\"\\n  tags: [model-collapse, recursive-generation, tail-erosion]\\n  relevance: direct\\n  cite_in: [introduction, related-work, background]\\n  notes: >\\n    Foundational model collapse paper. Tail erosion across recursive generations.\\n    Perplexity monotonically increases over 40 generations. Does NOT compare\\n    sampling strategies—uses standard sampling (T=1).\\n\\nmarchi2024_heat_death:\\n  title: \\\"Heat Death of Generative Models in Closed-Loop Learning\\\"\\n  authors: [Marchi, Soatto, Chaudhari, Tabuada]\\n  venue: ICASSP 2025\\n  year: 2024\\n  arxiv: \\\"2404.02325\\\"\\n  tags: [temperature, convergence, dynamical-systems, mode-collapse]\\n  relevance: direct\\n  cite_in: [discussion]\\n  notes: >\\n    Proves any T!=1 causes asymptotic degeneration. T<1 amplifies probability\\n    differences (mode collapse), T>1 contracts toward uniform. Key theoretical\\n    support for our tau=0.9 accelerated convergence finding.\\n\\ndohmatob2024_tale_of_tails:\\n  title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n  authors: [Dohmatob, Feng, Yang, Charton, Kempe]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2402.07043\\\"\\n  tags: [scaling-laws, tail-narrowing, tail-cutting, temperature, top-p, top-k]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Distinguishes tail narrowing (temperature: q_i^T ~ i^{-beta/T}) from\\n    tail cutting (top-p/top-k: hard truncation). Different degradation patterns.\\n    Explains why temp produces different statistical fingerprint from truncation.\\n\\ndohmatob2025_strong_collapse:\\n  title: \\\"Strong Model Collapse\\\"\\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\\n  venue: ICLR 2025 Spotlight\\n  year: 2025\\n  arxiv: \\\"2410.04840\\\"\\n  tags: [model-collapse, scaling, synthetic-data]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Even 0.1% synthetic data fraction causes collapse. Larger models amplify collapse.\\n    Bias-variance decomposition via random projections.\\n\\ndohmatob2024_demystified:\\n  title: \\\"Model Collapse Demystified: The Case of Regression\\\"\\n  authors: [Dohmatob, Feng, Kempe]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv: \\\"2402.07712\\\"\\n  tags: [model-collapse, regression, random-matrix-theory]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Test error grows linearly with iteration count in regression.\\n    Supports our finding of monotonically evolving features across depths.\\n\\nalemohammad2024_mad:\\n  title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n  authors: [Alemohammad, Casco-Rodriguez, et al.]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2307.01850\\\"\\n  tags: [autophagous, sampling-bias, precision-recall, MAD]\\n  relevance: indirect\\n  cite_in: [introduction, related-work]\\n  notes: >\\n    Biased sampling keeps precision but kills recall. Unbiased causes mode drift.\\n    tau=0.9 maps to their biased sampling regime.\\n\\ngerstgrasser2024_accumulate:\\n  title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n  authors: [Gerstgrasser, Schaeffer, et al.]\\n  venue: arXiv preprint\\n  year: 2024\\n  arxiv: \\\"2404.01413\\\"\\n  tags: [model-collapse, data-accumulation, mitigation]\\n  relevance: indirect\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Data accumulation prevents collapse (bounded test error).\\n    Important caveat: in accumulation regime, depth signal may be weaker.\\n\\ndrayson2025_detection_prevents_collapse:\\n  title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n  authors: [Drayson et al.]\\n  venue: EMNLP 2025 Findings\\n  year: 2025\\n  arxiv: \\\"2502.15654\\\"\\n  tags: [temperature, diversity, recursive-training, detection]\\n  relevance: direct\\n  cite_in: [related-work]\\n  notes: >\\n    Temperature tau=0.9 produces most repetitive outputs; diversity drops ~70%\\n    over 99 recursive generations (GPT-2, SmolLM2). Perplexity degradation more\\n    moderate than deterministic methods. Detection as filter vs our depth estimation.\\n\\nbakshi2026_collapse_improvement:\\n  title: \\\"From Collapse to Improvement: Statistical Perspectives on Iterative Training\\\"\\n  authors: [Bakshi, Chakraborty]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2602.10531\\\"\\n  tags: [model-collapse, non-monotonic, data-mixing]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Iterative training with fresh real data can *improve* performance.\\n    Non-monotonic dynamics complicate simple depth-signal assumptions.\\n\\nwang2026_contamination:\\n  title: \\\"Can Generative AI Survive Data Contamination? Theoretical Guarantees\\\"\\n  authors: [Wang, Niu, Li]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2602.16065\\\"\\n  tags: [model-collapse, contamination, theoretical]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Extends collapse theory beyond Gaussian/discrete to realistic distributions.\\n    Provides theoretical grounding for depth signal existence.\\n\\nfalahati2026_curated:\\n  title: \\\"Curated Synthetic Data Doesn't Have to Collapse\\\"\\n  authors: [Falahati, Amiri, Larson, Golab]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2605.07724\\\"\\n  tags: [curation, collapse-prevention, pluralistic]\\n  relevance: indirect\\n  cite_in: [discussion, limitations]\\n  notes: >\\n    Pluralistic curation prevents collapse. Harder case for our method —\\n    curated pipelines may produce depth-invariant text.\\n\\nknowledge_collapse2025:\\n  title: \\\"Knowledge Collapse in LLMs: Fluency Survives but Facts Fail\\\"\\n  authors: [Keisha, Wu, Wang, Koshiyama, Treleaven]\\n  venue: arXiv preprint\\n  year: 2025\\n  arxiv: \\\"2509.04796\\\"\\n  tags: [knowledge-collapse, fluency, factual-degradation]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Three-stage collapse: factual accuracy degrades while fluency persists.\\n    Surface perplexity features still capture depth signal despite fluency preservation.\\n\\nsynthetic_eggs2026:\\n  title: \\\"Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\\\"\\n  authors: [Schaffelder, Gatt]\\n  venue: ACL 2026 Findings\\n  year: 2026\\n  arxiv: \\\"2511.01490\\\"\\n  tags: [diversity, collapse-mitigation, Self-BLEU]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multi-source synthetic data reduces collapse. Their diversity metrics\\n    (Self-BLEU, lexical diversity) are candidate depth features.\\n\\nmohamed2025_broken_telephone:\\n  title: \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\"\\n  authors: [Mohamed, Geng, Vazirgiannis, Shang]\\n  venue: ACL 2025\\n  year: 2025\\n  arxiv: \\\"2502.20258\\\"\\n  tags: [iterative-generation, information-distortion, translation-chain]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Iterative generation (translation/paraphrase chains) produces monotonically\\n    increasing information distortion. Cross-task evidence that iterated signals\\n    accumulate — supports our depth signal persistence finding.\\n\\nsigma2026_spectral:\\n  title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n  authors: [\\\"(multiple)\\\"]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2601.03385\\\"\\n  tags: [spectral-analysis, gram-matrix, representation-collapse, 50-generations]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Gram matrix spectral analysis tracks representation space contraction over\\n    50 recursive generations. Proposes Sigma-UB metric. Complementary to our\\n    EDD — they measure geometric collapse, we measure statistical distinguishability.\\n    Tests 50 generations but does NOT do inter-generation classification.\\n\\n# --- R2-N2 supplement: model collapse empirical ---\\n\\nshi2025_closer_look:\\n  title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n  authors: [Shi, Wu, Zhang, Zhang, Tao, Qu]\\n  venue: NeurIPS 2025 (Spotlight)\\n  year: 2025\\n  arxiv: \\\"2509.16499\\\"\\n  tags: [model-collapse, entropy, memorization, intrinsic-dimension]\\n  relevance: direct\\n  role: background\\n  verified: true\\n  integration: \\\"整合，entropy ↔ depth signal 支撑特征选择论证\\\"\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Identifies generalization-to-memorization transition during recursive training.\\n    Entropy of training data decreases over iterations, strongly correlated with\\n    model degradation. Entropy decline IS a measurable depth signal — directly\\n    supports our statistical feature approach to depth estimation.\\n\\nyi2026_escaping_collapse:\\n  title: \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\"\\n  authors: [Yi, Liu, Cheng, Xu]\\n  venue: 3rd DATA-FM Workshop @ ICLR 2026\\n  year: 2026\\n  arxiv: \\\"2510.16657\\\"\\n  tags: [model-collapse, verification, synthetic-data, mitigation]\\n  relevance: indirect\\n  role: background\\n  verified: true\\n  integration: \\\"引用但降级——related work 提一句，不支撑核心 claim（workshop paper）\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Verifier-guided retraining prevents collapse. Our depth estimation\\n    can serve AS the verifier — depth score enables graduated filtering\\n    rather than binary accept/reject. NOTE: workshop paper, not main conference.\\n\\n# =============================================================\\n# DECODING STRATEGIES\\n# =============================================================\\n\\nholtzman2020_nucleus:\\n  title: \\\"The Curious Case of Neural Text Degeneration\\\"\\n  authors: [Holtzman, Buys, Du, Forbes, Choi]\\n  venue: ICLR 2020\\n  year: 2020\\n  arxiv: \\\"1904.09751\\\"\\n  tags: [nucleus-sampling, temperature, text-degeneration, unreliable-tail]\\n  relevance: indirect\\n  cite_in: [background, method]\\n  notes: >\\n    Proposes nucleus sampling. Temperature+top-k leads to repetition.\\n    Key concept: unreliable tail of low-probability tokens.\\n\\nfinlayson2024_closing:\\n  title: \\\"Closing the Curious Case of Neural Text Degeneration\\\"\\n  authors: [Finlayson, Hewitt, Koller, Swayamdipta, Sabharwal]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2310.01693\\\"\\n  tags: [softmax-bottleneck, truncation-sampling, precise-sampling]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Truncation sampling eliminates softmax bottleneck errors. Mechanistic\\n    difference between truncation and scaling approaches.\\n\\ngarces_arias2025_decoding_decoded:\\n  title: \\\"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\\\"\\n  authors: [Garces Arias et al.]\\n  venue: COLING 2025\\n  year: 2025\\n  tags: [decoding, hyperparameters, model-dependent]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Confirms optimal decoding configuration is model-dependent.\\n    Directly supports D006 finding (strategy effect is model-dependent).\\n    Key external validation for our interaction effects claim.\\n\\nwiher2022_decoding:\\n  title: \\\"On Decoding Strategies for Neural Text Generators\\\"\\n  authors: [Wiher, Meister, Cotterell]\\n  venue: TACL 2022\\n  year: 2022\\n  tags: [decoding, task-dependent, evaluation]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Decoding strategy effects are task-dependent.\\n    Supports our finding that strategy effects on depth signal vary by model.\\n\\nbasu2021_mirostat:\\n  title: \\\"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\\\"\\n  authors: [Basu, Sachdev, Kamdar, Nishi]\\n  venue: ICLR 2021\\n  year: 2021\\n  tags: [perplexity-control, sampling, cross-entropy]\\n  relevance: indirect\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Perplexity and sampling parameters have non-linear relationship.\\n    Relevant to p90_ppl capturing depth signal better than mean_ppl\\n    under heavy-tailed distributions.\\n\\n# =============================================================\\n# BINARY / ZERO-SHOT DETECTION\\n# =============================================================\\n\\nmitchell2023_detectgpt:\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: [Mitchell, Lee, Khazatsky, Manning, Finn]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv: \\\"2301.11305\\\"\\n  tags: [zero-shot, detection, curvature, perturbation, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Foundational zero-shot detector using log-probability curvature via\\n    random perturbations. Binary only. Fast-DetectGPT improves efficiency.\\n\\nsadasivan2023_paraphrase:\\n  title: \\\"Can AI-Generated Text be Reliably Detected?\\\"\\n  authors: [Sadasivan, Kumar, Balasubramanian, Wang, Feizi]\\n  venue: arXiv preprint\\n  year: 2023\\n  arxiv: \\\"2303.11156\\\"\\n  tags: [detection-limits, paraphrase-attack, impossibility]\\n  relevance: indirect\\n  cite_in: [related-work, limitations]\\n  notes: >\\n    Shows paraphrase attacks evade all detectors; proves impossibility\\n    result when model and human distributions overlap sufficiently.\\n    Important limitation context for our depth estimation approach.\\n\\nbinoculars2024:\\n  title: \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\"\\n  authors: [Hans, Schwarzschild, Manber, et al.]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2401.12070\\\"\\n  tags: [zero-shot, detection, perplexity-ratio, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Two-model perplexity ratio for zero-shot binary detection.\\n    We extend beyond binary to ordinal depth.\\n\\nfast_detectgpt2024:\\n  title: \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\"\\n  authors: [Bao et al.]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2310.05130\\\"\\n  tags: [zero-shot, detection, curvature, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Conditional probability curvature for efficient binary detection.\\n    Cannot distinguish depth levels.\\n\\ndiveye2026:\\n  title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n  authors: [Basani, Chen]\\n  venue: ICLR 2026 / TMLR\\n  year: 2026\\n  arxiv: \\\"2509.18880\\\"\\n  tags: [surprisal-diversity, statistical-features, detection]\\n  relevance: direct\\n  cite_in: [related-work, method]\\n  notes: >\\n    Token-level surprisal diversity features for binary detection.\\n    Feature overlap with our pipeline. We extend similar features\\n    to ordinal depth regression.\\n\\nloki2025:\\n  title: \\\"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\\\"\\n  authors: [Ye, Zhou, Huang, Zhang, Bai, Kang, He, Lin, Wang, Wu, Wu, Chen, Lin, He, Li]\\n  venue: ICLR 2025 Spotlight\\n  year: 2025\\n  arxiv: \\\"2410.09732\\\"\\n  tags: [benchmark, multimodal, detection]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multimodal synthetic data detection benchmark. Binary only, no depth.\\n\\ngehrmann2019_gltr:\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: [Gehrmann, Strobelt, Rush]\\n  venue: ACL 2019\\n  year: 2019\\n  arxiv: \\\"1906.04043\\\"\\n  tags: [detection, statistical-features, perplexity, rank, entropy]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Foundational statistical detection using log-likelihood, rank, entropy.\\n    Our feature system extends this paradigm to recursive depth estimation.\\n\\npudasaini2026_detection_fails:\\n  title: \\\"Why AI-Generated Text Detection Fails: Evidence from Explainable AI\\\"\\n  authors: [Pudasaini et al.]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2603.23146\\\"\\n  tags: [detection-failure, distribution-shift, fragility]\\n  relevance: indirect\\n  cite_in: [limitations]\\n  notes: >\\n    Detection features degrade under distribution shift.\\n    If binary features are domain-fragile, ordinal depth features may be too.\\n\\n# --- R2-N2 supplement: detection methods ---\\n\\ntulchinskii2024_intrinsic_dim:\\n  title: \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\"\\n  authors: [Tulchinskii, Kuznetsov, et al.]\\n  venue: NeurIPS 2023\\n  year: 2023\\n  arxiv: \\\"2306.04723\\\"\\n  tags: [intrinsic-dimension, geometric-features, detection, cross-domain]\\n  relevance: direct\\n  role: method-component\\n  cite_in: [related-work, method]\\n  notes: >\\n    Intrinsic dimension of text embeddings ~9 for human, ~7.5 for AI-generated.\\n    Geometric invariant enables cross-domain, cross-model robust detection.\\n    Complementary feature family to our statistical perplexity features —\\n    intrinsic dimension could serve as additional depth feature.\\n\\nverma2024_ghostbuster:\\n  title: \\\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\\\"\\n  authors: [Verma, Fleisig, Tomlin, Klein]\\n  venue: NAACL 2024\\n  year: 2024\\n  arxiv: \\\"2305.15047\\\"\\n  tags: [detection, structured-search, statistical-features, cross-domain]\\n  relevance: indirect\\n  role: direct-competitor\\n  cite_in: [related-work]\\n  notes: >\\n    Structured search over combinations of weaker LM features for detection.\\n    99.0 F1 cross-domain. Binary only. Feature engineering approach parallels\\n    our multi-feature pipeline but targets binary classification, not ordinal depth.\\n\\nli2024_mage:\\n  title: \\\"MAGE: Machine-generated Text Detection in the Wild\\\"\\n  authors: [Li, Li, et al.]\\n  venue: ACL 2024\\n  year: 2024\\n  arxiv: \\\"2305.13242\\\"\\n  tags: [benchmark, cross-domain, cross-model, detection]\\n  relevance: indirect\\n  role: evaluation\\n  cite_in: [related-work]\\n  notes: >\\n    Cross-domain cross-model detection benchmark. Finds significant OOD\\n    performance degradation — same generalization challenge our cross-model\\n    depth estimation faces. Binary detection only.\\n\\nwu2025_detection_survey:\\n  title: \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\"\\n  authors: [Wu, Yang, Zhan, Yuan, Chao, Wong]\\n  venue: Computational Linguistics, Vol. 51, Issue 1\\n  year: 2025\\n  arxiv: \\\"2310.14724\\\"\\n  tags: [survey, detection-taxonomy, watermarking, statistical, neural]\\n  relevance: indirect\\n  role: background\\n  verified: true\\n  integration: \\\"整合，survey 定位\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Comprehensive survey of detection paradigms: watermarking, statistical,\\n    neural, human-assisted. Positions our work as extending the statistical\\n    paradigm from binary detection to ordinal depth estimation.\\n\\n# =============================================================\\n# ADJACENT TASK — editing extent, attribution\\n# =============================================================\\n\\neditlens2026:\\n  title: \\\"EditLens: Quantifying the Extent of AI Editing in Text\\\"\\n  authors: [Thai et al.]\\n  venue: ICLR 2026\\n  year: 2026\\n  arxiv: \\\"2510.03154\\\"\\n  tags: [editing-extent, continuous-score, mixed-authorship]\\n  relevance: direct\\n  cite_in: [introduction, related-work]\\n  notes: >\\n    Closest conceptual neighbor — both go beyond binary classification.\\n    EditLens = single-pass editing extent; ours = multi-generation depth.\\n\\nuchendu2020_attribution:\\n  title: \\\"Authorship Attribution for Neural Text Generation\\\"\\n  authors: [Uchendu, Le, Shu, Lee]\\n  venue: EMNLP 2020\\n  year: 2020\\n  tags: [attribution, multi-source, authorship]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multi-source attribution (which model?). We solve a different axis\\n    (how many iterations?) — complementary problems.\\n\\npu2026_generator_barrier:\\n  title: \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\"\\n  authors: [Pu, Cheng, Yuan, Wu, Bi]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2604.13692\\\"\\n  tags: [disentanglement, cross-generator, generalization]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Cross-generator generalization via disentanglement.\\n    Analogous to our cross-model generalization challenge.\\n\\n# --- R2-N2 supplement: attribution paradigms ---\\n\\nbevendorff2025_two_paradigms:\\n  title: \\\"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\\\"\\n  authors: [Bevendorff, Wiegmann, Richter, Potthast, Stein]\\n  venue: ACL 2025 Findings\\n  year: 2025\\n  tags: [attribution, verification, detection-paradigm, authorship]\\n  relevance: direct\\n  role: background\\n  verified: true\\n  integration: \\\"整合，'第三范式' framing（attribution/verification 之外的正交第三维度）\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Reframes LLM detection as authorship verification (not attribution).\\n    Our depth estimation is a third paradigm — ordinal characterization\\n    beyond binary verification or multi-class attribution. Key framing\\n    reference for positioning our contribution.\\n\\n# =============================================================\\n# METHOD COMPONENT — ordinal classification\\n# =============================================================\\n\\ncoral2020:\\n  title: \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\"\\n  authors: [Cao, Mirjalili, Raschka]\\n  venue: Pattern Recognition Letters\\n  year: 2020\\n  arxiv: \\\"1901.07884\\\"\\n  tags: [ordinal-classification, rank-consistency, cumulative-logits]\\n  relevance: direct\\n  cite_in: [method, experiments]\\n  notes: >\\n    CORAL ordinal classification framework used in our baseline battery.\\n    Rank-consistent cumulative logits for ordinal targets.\\n\\ncloc2025:\\n  title: \\\"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\\\"\\n  authors: [Pitawela, Carneiro, et al.]\\n  venue: CVPR 2025\\n  year: 2025\\n  arxiv: \\\"2504.17813\\\"\\n  tags: [contrastive-learning, ordinal, multi-margin, N-pair]\\n  relevance: direct\\n  cite_in: [method, dcol-section]\\n  notes: >\\n    DCOL is our adaptation of CLOC to text depth estimation.\\n    Multi-margin N-pair loss for ordinal-aware contrastive learning.\\n    Must cite as methodological basis for DCOL section.\\n\\n# =============================================================\\n# WATERMARKING\\n# =============================================================\\n\\nkirchenbauer2023_watermark:\\n  title: \\\"A Watermark for Large Language Models\\\"\\n  authors: [Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv: \\\"2301.10226\\\"\\n  tags: [watermarking, proactive-detection, green-list]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Proactive detection via watermarking. Complementary —\\n    watermarking requires generator cooperation; our method is post-hoc.\\n\\n# =============================================================\\n# DATA CURATION\\n# =============================================================\\n\\ndsir2023:\\n  title: \\\"Data Selection for Language Models via Importance Resampling\\\"\\n  authors: [Xie, Santurkar, Ma, Liang]\\n  venue: NeurIPS 2023\\n  year: 2023\\n  arxiv: \\\"2302.03169\\\"\\n  tags: [data-selection, importance-resampling, curation]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Quality-based data selection for LM training.\\n    Our depth estimation enables depth-graduated curation (Claim 3 / Discussion).\\n\\nqurating2024:\\n  title: \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\"\\n  authors: [Wettig, Gupta, et al.]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2402.09739\\\"\\n  tags: [quality-rating, data-curation, LLM-judgments]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    LLM-based quality rating for data selection.\\n    Our depth score is a complementary quality axis.\\n\\n# --- R2-N2 supplement: data curation at scale ---\\n\\npenedo2024_fineweb:\\n  title: \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\"\\n  authors: [Penedo, Kydlicek, et al.]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv: \\\"2406.17557\\\"\\n  tags: [data-curation, quality-filtering, deduplication, web-scale]\\n  relevance: indirect\\n  role: background\\n  cite_in: [discussion]\\n  notes: >\\n    15T token dataset with systematic quality filtering pipeline (dedup,\\n    heuristic filters, classifier-based selection). Our depth estimation\\n    adds a synthetic contamination axis complementary to FineWeb-style\\n    quality curation — depth score can flag recursively degraded text\\n    that passes standard quality filters.\\n\\n# =============================================================\\n# COVARIATE SHIFT — technical background\\n# =============================================================\\n\\nsugiyama2007_importance_weighting:\\n  title: \\\"Covariate Shift Adaptation by Importance Weighted Cross Validation\\\"\\n  authors: [Sugiyama, Krauledat, Mueller]\\n  venue: JMLR\\n  year: 2007\\n  tags: [covariate-shift, importance-weighting, domain-adaptation]\\n  relevance: background\\n  cite_in: [discussion]\\n  notes: >\\n    Theoretical foundation for covariate shift correction.\\n    Our z-score normalization is a simplified distribution alignment.\\n\\n# =============================================================\\n# COVERAGE CHECKLIST (paper_framing.md Dream D002 requirements)\\n# =============================================================\\n# [x] watermarking: kirchenbauer2023_watermark\\n# [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,\\n#     dohmatob2024_tale_of_tails, dohmatob2025_strong_collapse,\\n#     dohmatob2024_demystified, gerstgrasser2024_accumulate\\n# [x] model collapse empirical: drayson2025, bakshi2026, marchi2024,\\n#     shi2025_closer_look (VERIFIED), yi2026_escaping_collapse (VERIFIED, workshop)\\n# [x] data curation: dsir2023, qurating2024, penedo2024_fineweb (NEW)\\n# [x] multi-source attribution: uchendu2020_attribution,\\n#     bevendorff2025_two_paradigms (VERIFIED)\\n# [x] binary detectors: mitchell2023_detectgpt, sadasivan2023_paraphrase,\\n#     binoculars2024, fast_detectgpt2024, diveye2026, loki2025,\\n#     tulchinskii2024_intrinsic_dim (NEW), verma2024_ghostbuster (NEW),\\n#     li2024_mage (NEW)\\n# [x] detection survey: wu2025_detection_survey (VERIFIED)\\n# [x] decoding strategy effects: garces_arias2025, holtzman2020_nucleus,\\n#     wiher2022_decoding, basu2021_mirostat, finlayson2024_closing\\n# [x] ordinal classification: coral2020, cloc2025\\n# [x] adjacent tasks: editlens2026\\n# [x] covariate shift: sugiyama2007\\n# [x] statistical detection foundation: gehrmann2019_gltr\\n#\\n# Total unique entries: 43 (35 original + 8 R2-N2 supplement)\\n# 2024-2026 papers: 30/43 (70% recent coverage)\\n# Direct relevance: 12 entries\\n\", \"total_chars\": 26296, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "7d6f84ed-4fff-46e9-8268-8d2123b8a65a",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml\\\", \\\"content\\\": \\\"# Literature Map — recursive_gen_depth_est\\\\n# Last updated: 2026-05-15\\\\n# Purpose: Systematic reference tracking for EMNLP ARR May 25 submission\\\\n# Total entries: 43 (35 original + 8 R2-N2 supplement)\\\\n#\\\\n# Tags used for cite_in: introduction, related-work, background, method,\\\\n#   experiments, discussion, limitations, dcol-section\\\\n\\\\n# =============================================================\\\\n# MODEL COLLAPSE — foundational theory & recursive generation\\\\n# =============================================================\\\\n\\\\nshumailov2024_nature:\\\\n  title: \\\\\\\"AI models collapse when trained on recursively generated data\\\\\\\"\\\\n  authors: [Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal]\\\\n  venue: Nature\\\\n  year: 2024\\\\n  doi: \\\\\\\"10.1038/s41586-024-07566-y\\\\\\\"\\\\n  tags: [model-collapse, recursive-generation, tail-erosion]\\\\n  relevance: direct\\\\n  cite_in: [introduction, related-work, background]\\\\n  notes: >\\\\n    Foundational model collapse paper. Tail erosion across recursive generations.\\\\n    Perplexity monotonically increases over 40 generations. Does NOT compare\\\\n    sampling strategies—uses standard sampling (T=1).\\\\n\\\\nmarchi2024_heat_death:\\\\n  title: \\\\\\\"Heat Death of Generative Models in Closed-Loop Learning\\\\\\\"\\\\n  authors: [Marchi, Soatto, Chaudhari, Tabuada]\\\\n  venue: ICASSP 2025\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2404.02325\\\\\\\"\\\\n  tags: [temperature, convergence, dynamical-systems, mode-collapse]\\\\n  relevance: direct\\\\n  cite_in: [discussion]\\\\n  notes: >\\\\n    Proves any T!=1 causes asymptotic degeneration. T<1 amplifies probability\\\\n    differences (mode collapse), T>1 contracts toward uniform. Key theoretical\\\\n    support for our tau=0.9 accelerated convergence finding.\\\\n\\\\ndohmatob2024_tale_of_tails:\\\\n  title: \\\\\\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\\\\\"\\\\n  authors: [Dohmatob, Feng, Yang, Charton, Kempe]\\\\n  venue: ICML 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2402.07043\\\\\\\"\\\\n  tags: [scaling-laws, tail-narrowing, tail-cutting, temperature, top-p, top-k]\\\\n  relevance: direct\\\\n  cite_in: [related-work, discussion]\\\\n  notes: >\\\\n    Distinguishes tail narrowing (temperature: q_i^T ~ i^{-beta/T}) from\\\\n    tail cutting (top-p/top-k: hard truncation). Different degradation patterns.\\\\n    Explains why temp produces different statistical fingerprint from truncation.\\\\n\\\\ndohmatob2025_strong_collapse:\\\\n  title: \\\\\\\"Strong Model Collapse\\\\\\\"\\\\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\\\\n  venue: ICLR 2025 Spotlight\\\\n  year: 2025\\\\n  arxiv: \\\\\\\"2410.04840\\\\\\\"\\\\n  tags: [model-collapse, scaling, synthetic-data]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Even 0.1% synthetic data fraction causes collapse. Larger models amplify collapse.\\\\n    Bias-variance decomposition via random projections.\\\\n\\\\ndohmatob2024_demystified:\\\\n  title: \\\\\\\"Model Collapse Demystified: The Case of Regression\\\\\\\"\\\\n  authors: [Dohmatob, Feng, Kempe]\\\\n  venue: NeurIPS 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2402.07712\\\\\\\"\\\\n  tags: [model-collapse, regression, random-matrix-theory]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Test error grows linearly with iteration count in regression.\\\\n    Supports our finding of monotonically evolving features across depths.\\\\n\\\\nalemohammad2024_mad:\\\\n  title: \\\\\\\"Self-Consuming Generative Models Go MAD\\\\\\\"\\\\n  authors: [Alemohammad, Casco-Rodriguez, et al.]\\\\n  venue: ICLR 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2307.01850\\\\\\\"\\\\n  tags: [autophagous, sampling-bias, precision-recall, MAD]\\\\n  relevance: indirect\\\\n  cite_in: [introduction, related-work]\\\\n  notes: >\\\\n    Biased sampling keeps precision but kills recall. Unbiased causes mode drift.\\\\n    tau=0.9 maps to their biased sampling regime.\\\\n\\\\ngerstgrasser2024_accumulate:\\\\n  title: \\\\\\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\\\\\"\\\\n  authors: [Gerstgrasser, Schaeffer, et al.]\\\\n  venue: arXiv preprint\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2404.01413\\\\\\\"\\\\n  tags: [model-collapse, data-accumulation, mitigation]\\\\n  relevance: indirect\\\\n  cite_in: [related-work, discussion]\\\\n  notes: >\\\\n    Data accumulation prevents collapse (bounded test error).\\\\n    Important caveat: in accumulation regime, depth signal may be weaker.\\\\n\\\\ndrayson2025_detection_prevents_collapse:\\\\n  title: \\\\\\\"Machine-generated text detection prevents language model collapse\\\\\\\"\\\\n  authors: [Drayson et al.]\\\\n  venue: EMNLP 2025 Findings\\\\n  year: 2025\\\\n  arxiv: \\\\\\\"2502.15654\\\\\\\"\\\\n  tags: [temperature, diversity, recursive-training, detection]\\\\n  relevance: direct\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Temperature tau=0.9 produces most repetitive outputs; diversity drops ~70%\\\\n    over 99 recursive generations (GPT-2, SmolLM2). Perplexity degradation more\\\\n    moderate than deterministic methods. Detection as filter vs our depth estimation.\\\\n\\\\nbakshi2026_collapse_improvement:\\\\n  title: \\\\\\\"From Collapse to Improvement: Statistical Perspectives on Iterative Training\\\\\\\"\\\\n  authors: [Bakshi, Chakraborty]\\\\n  venue: arXiv preprint\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2602.10531\\\\\\\"\\\\n  tags: [model-collapse, non-monotonic, data-mixing]\\\\n  relevance: indirect\\\\n  cite_in: [discussion]\\\\n  notes: >\\\\n    Iterative training with fresh real data can *improve* performance.\\\\n    Non-monotonic dynamics complicate simple depth-signal assumptions.\\\\n\\\\nwang2026_contamination:\\\\n  title: \\\\\\\"Can Generative AI Survive Data Contamination? Theoretical Guarantees\\\\\\\"\\\\n  authors: [Wang, Niu, Li]\\\\n  venue: arXiv preprint\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2602.16065\\\\\\\"\\\\n  tags: [model-collapse, contamination, theoretical]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Extends collapse theory beyond Gaussian/discrete to realistic distributions.\\\\n    Provides theoretical grounding for depth signal existence.\\\\n\\\\nfalahati2026_curated:\\\\n  title: \\\\\\\"Curated Synthetic Data Doesn't Have to Collapse\\\\\\\"\\\\n  authors: [Falahati, Amiri, Larson, Golab]\\\\n  venue: arXiv preprint\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2605.07724\\\\\\\"\\\\n  tags: [curation, collapse-prevention, pluralistic]\\\\n  relevance: indirect\\\\n  cite_in: [discussion, limitations]\\\\n  notes: >\\\\n    Pluralistic curation prevents collapse. Harder case for our method —\\\\n    curated pipelines may produce depth-invariant text.\\\\n\\\\nknowledge_collapse2025:\\\\n  title: \\\\\\\"Knowledge Collapse in LLMs: Fluency Survives but Facts Fail\\\\\\\"\\\\n  authors: [Keisha, Wu, Wang, Koshiyama, Treleaven]\\\\n  venue: arXiv preprint\\\\n  year: 2025\\\\n  arxiv: \\\\\\\"2509.04796\\\\\\\"\\\\n  tags: [knowledge-collapse, fluency, factual-degradation]\\\\n  relevance: indirect\\\\n  cite_in: [discussion]\\\\n  notes: >\\\\n    Three-stage collapse: factual accuracy degrades while fluency persists.\\\\n    Surface perplexity features still capture depth signal despite fluency preservation.\\\\n\\\\nsynthetic_eggs2026:\\\\n  title: \\\\\\\"Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\\\\\\\"\\\\n  authors: [Schaffelder, Gatt]\\\\n  venue: ACL 2026 Findings\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2511.01490\\\\\\\"\\\\n  tags: [diversity, collapse-mitigation, Self-BLEU]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Multi-source synthetic data reduces collapse. Their diversity metrics\\\\n    (Self-BLEU, lexical diversity) are candidate depth features.\\\\n\\\\nmohamed2025_broken_telephone:\\\\n  title: \\\\\\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\\\\\"\\\\n  authors: [Mohamed, Geng, Vazirgiannis, Shang]\\\\n  venue: ACL 2025\\\\n  year: 2025\\\\n  arxiv: \\\\\\\"2502.20258\\\\\\\"\\\\n  tags: [iterative-generation, information-distortion, translation-chain]\\\\n  relevance: indirect\\\\n  cite_in: [discussion]\\\\n  notes: >\\\\n    Iterative generation (translation/paraphrase chains) produces monotonically\\\\n    increasing information distortion. Cross-task evidence that iterated signals\\\\n    accumulate — supports our depth signal persistence finding.\\\\n\\\\nsigma2026_spectral:\\\\n  title: \\\\\\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\\\\\"\\\\n  authors: [\\\\\\\"(multiple)\\\\\\\"]\\\\n  venue: arXiv preprint\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2601.03385\\\\\\\"\\\\n  tags: [spectral-analysis, gram-matrix, representation-collapse, 50-generations]\\\\n  relevance: direct\\\\n  cite_in: [related-work, discussion]\\\\n  notes: >\\\\n    Gram matrix spectral analysis tracks representation space contraction over\\\\n    50 recursive generations. Proposes Sigma-UB metric. Complementary to our\\\\n    EDD — they measure geometric collapse, we measure statistical distinguishability.\\\\n    Tests 50 generations but does NOT do inter-generation classification.\\\\n\\\\n# --- R2-N2 supplement: model collapse empirical ---\\\\n\\\\nshi2025_closer_look:\\\\n  title: \\\\\\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\\\\\"\\\\n  authors: [Shi, Wu, Zhang, Zhang, Tao, Qu]\\\\n  venue: NeurIPS 2025 (Spotlight)\\\\n  year: 2025\\\\n  arxiv: \\\\\\\"2509.16499\\\\\\\"\\\\n  tags: [model-collapse, entropy, memorization, intrinsic-dimension]\\\\n  relevance: direct\\\\n  role: background\\\\n  verified: true\\\\n  integration: \\\\\\\"整合，entropy ↔ depth signal 支撑特征选择论证\\\\\\\"\\\\n  cite_in: [related-work, discussion]\\\\n  notes: >\\\\n    Identifies generalization-to-memorization transition during recursive training.\\\\n    Entropy of training data decreases over iterations, strongly correlated with\\\\n    model degradation. Entropy decline IS a measurable depth signal — directly\\\\n    supports our statistical feature approach to depth estimation.\\\\n\\\\nyi2026_escaping_collapse:\\\\n  title: \\\\\\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\\\\\"\\\\n  authors: [Yi, Liu, Cheng, Xu]\\\\n  venue: 3rd DATA-FM Workshop @ ICLR 2026\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2510.16657\\\\\\\"\\\\n  tags: [model-collapse, verification, synthetic-data, mitigation]\\\\n  relevance: indirect\\\\n  role: background\\\\n  verified: true\\\\n  integration: \\\\\\\"引用但降级——related work 提一句，不支撑核心 claim（workshop paper）\\\\\\\"\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Verifier-guided retraining prevents collapse. Our depth estimation\\\\n    can serve AS the verifier — depth score enables graduated filtering\\\\n    rather than binary accept/reject. NOTE: workshop paper, not main conference.\\\\n\\\\n# =============================================================\\\\n# DECODING STRATEGIES\\\\n# =============================================================\\\\n\\\\nholtzman2020_nucleus:\\\\n  title: \\\\\\\"The Curious Case of Neural Text Degeneration\\\\\\\"\\\\n  authors: [Holtzman, Buys, Du, Forbes, Choi]\\\\n  venue: ICLR 2020\\\\n  year: 2020\\\\n  arxiv: \\\\\\\"1904.09751\\\\\\\"\\\\n  tags: [nucleus-sampling, temperature, text-degeneration, unreliable-tail]\\\\n  relevance: indirect\\\\n  cite_in: [background, method]\\\\n  notes: >\\\\n    Proposes nucleus sampling. Temperature+top-k leads to repetition.\\\\n    Key concept: unreliable tail of low-probability tokens.\\\\n\\\\nfinlayson2024_closing:\\\\n  title: \\\\\\\"Closing the Curious Case of Neural Text Degeneration\\\\\\\"\\\\n  authors: [Finlayson, Hewitt, Koller, Swayamdipta, Sabharwal]\\\\n  venue: ICLR 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2310.01693\\\\\\\"\\\\n  tags: [softmax-bottleneck, truncation-sampling, precise-sampling]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Truncation sampling eliminates softmax bottleneck errors. Mechanistic\\\\n    difference between truncation and scaling approaches.\\\\n\\\\ngarces_arias2025_decoding_decoded:\\\\n  title: \\\\\\\"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\\\\\\\"\\\\n  authors: [Garces Arias et al.]\\\\n  venue: COLING 2025\\\\n  year: 2025\\\\n  tags: [decoding, hyperparameters, model-dependent]\\\\n  relevance: direct\\\\n  cite_in: [related-work, discussion]\\\\n  notes: >\\\\n    Confirms optimal decoding configuration is model-dependent.\\\\n    Directly supports D006 finding (strategy effect is model-dependent).\\\\n    Key external validation for our interaction effects claim.\\\\n\\\\nwiher2022_decoding:\\\\n  title: \\\\\\\"On Decoding Strategies for Neural Text Generators\\\\\\\"\\\\n  authors: [Wiher, Meister, Cotterell]\\\\n  venue: TACL 2022\\\\n  year: 2022\\\\n  tags: [decoding, task-dependent, evaluation]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Decoding strategy effects are task-dependent.\\\\n    Supports our finding that strategy effects on depth signal vary by model.\\\\n\\\\nbasu2021_mirostat:\\\\n  title: \\\\\\\"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\\\\\\\"\\\\n  authors: [Basu, Sachdev, Kamdar, Nishi]\\\\n  venue: ICLR 2021\\\\n  year: 2021\\\\n  tags: [perplexity-control, sampling, cross-entropy]\\\\n  relevance: indirect\\\\n  cite_in: [related-work, discussion]\\\\n  notes: >\\\\n    Perplexity and sampling parameters have non-linear relationship.\\\\n    Relevant to p90_ppl capturing depth signal better than mean_ppl\\\\n    under heavy-tailed distributions.\\\\n\\\\n# =============================================================\\\\n# BINARY / ZERO-SHOT DETECTION\\\\n# =============================================================\\\\n\\\\nmitchell2023_detectgpt:\\\\n  title: \\\\\\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\\\\\"\\\\n  authors: [Mitchell, Lee, Khazatsky, Manning, Finn]\\\\n  venue: ICML 2023\\\\n  year: 2023\\\\n  arxiv: \\\\\\\"2301.11305\\\\\\\"\\\\n  tags: [zero-shot, detection, curvature, perturbation, binary]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Foundational zero-shot detector using log-probability curvature via\\\\n    random perturbations. Binary only. Fast-DetectGPT improves efficiency.\\\\n\\\\nsadasivan2023_paraphrase:\\\\n  title: \\\\\\\"Can AI-Generated Text be Reliably Detected?\\\\\\\"\\\\n  authors: [Sadasivan, Kumar, Balasubramanian, Wang, Feizi]\\\\n  venue: arXiv preprint\\\\n  year: 2023\\\\n  arxiv: \\\\\\\"2303.11156\\\\\\\"\\\\n  tags: [detection-limits, paraphrase-attack, impossibility]\\\\n  relevance: indirect\\\\n  cite_in: [related-work, limitations]\\\\n  notes: >\\\\n    Shows paraphrase attacks evade all detectors; proves impossibility\\\\n    result when model and human distributions overlap sufficiently.\\\\n    Important limitation context for our depth estimation approach.\\\\n\\\\nbinoculars2024:\\\\n  title: \\\\\\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\\\\\"\\\\n  authors: [Hans, Schwarzschild, Manber, et al.]\\\\n  venue: ICML 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2401.12070\\\\\\\"\\\\n  tags: [zero-shot, detection, perplexity-ratio, binary]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Two-model perplexity ratio for zero-shot binary detection.\\\\n    We extend beyond binary to ordinal depth.\\\\n\\\\nfast_detectgpt2024:\\\\n  title: \\\\\\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\\\\\"\\\\n  authors: [Bao et al.]\\\\n  venue: ICLR 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2310.05130\\\\\\\"\\\\n  tags: [zero-shot, detection, curvature, binary]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Conditional probability curvature for efficient binary detection.\\\\n    Cannot distinguish depth levels.\\\\n\\\\ndiveye2026:\\\\n  title: \\\\\\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\\\\\"\\\\n  authors: [Basani, Chen]\\\\n  venue: ICLR 2026 / TMLR\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2509.18880\\\\\\\"\\\\n  tags: [surprisal-diversity, statistical-features, detection]\\\\n  relevance: direct\\\\n  cite_in: [related-work, method]\\\\n  notes: >\\\\n    Token-level surprisal diversity features for binary detection.\\\\n    Feature overlap with our pipeline. We extend similar features\\\\n    to ordinal depth regression.\\\\n\\\\nloki2025:\\\\n  title: \\\\\\\"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\\\\\\\"\\\\n  authors: [Ye, Zhou, Huang, Zhang, Bai, Kang, He, Lin, Wang, Wu, Wu, Chen, Lin, He, Li]\\\\n  venue: ICLR 2025 Spotlight\\\\n  year: 2025\\\\n  arxiv: \\\\\\\"2410.09732\\\\\\\"\\\\n  tags: [benchmark, multimodal, detection]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Multimodal synthetic data detection benchmark. Binary only, no depth.\\\\n\\\\ngehrmann2019_gltr:\\\\n  title: \\\\\\\"GLTR: Statistical Detection and Visualization of Generated Text\\\\\\\"\\\\n  authors: [Gehrmann, Strobelt, Rush]\\\\n  venue: ACL 2019\\\\n  year: 2019\\\\n  arxiv: \\\\\\\"1906.04043\\\\\\\"\\\\n  tags: [detection, statistical-features, perplexity, rank, entropy]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Foundational statistical detection using log-likelihood, rank, entropy.\\\\n    Our feature system extends this paradigm to recursive depth estimation.\\\\n\\\\npudasaini2026_detection_fails:\\\\n  title: \\\\\\\"Why AI-Generated Text Detection Fails: Evidence from Explainable AI\\\\\\\"\\\\n  authors: [Pudasaini et al.]\\\\n  venue: arXiv preprint\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2603.23146\\\\\\\"\\\\n  tags: [detection-failure, distribution-shift, fragility]\\\\n  relevance: indirect\\\\n  cite_in: [limitations]\\\\n  notes: >\\\\n    Detection features degrade under distribution shift.\\\\n    If binary features are domain-fragile, ordinal depth features may be too.\\\\n\\\\n# --- R2-N2 supplement: detection methods ---\\\\n\\\\ntulchinskii2024_intrinsic_dim:\\\\n  title: \\\\\\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\\\\\"\\\\n  authors: [Tulchinskii, Kuznetsov, et al.]\\\\n  venue: NeurIPS 2023\\\\n  year: 2023\\\\n  arxiv: \\\\\\\"2306.04723\\\\\\\"\\\\n  tags: [intrinsic-dimension, geometric-features, detection, cross-domain]\\\\n  relevance: direct\\\\n  role: method-component\\\\n  cite_in: [related-work, method]\\\\n  notes: >\\\\n    Intrinsic dimension of text embeddings ~9 for human, ~7.5 for AI-generated.\\\\n    Geometric invariant enables cross-domain, cross-model robust detection.\\\\n    Complementary feature family to our statistical perplexity features —\\\\n    intrinsic dimension could serve as additional depth feature.\\\\n\\\\nverma2024_ghostbuster:\\\\n  title: \\\\\\\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\\\\\\\"\\\\n  authors: [Verma, Fleisig, Tomlin, Klein]\\\\n  venue: NAACL 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2305.15047\\\\\\\"\\\\n  tags: [detection, structured-search, statistical-features, cross-domain]\\\\n  relevance: indirect\\\\n  role: direct-competitor\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Structured search over combinations of weaker LM features for detection.\\\\n    99.0 F1 cross-domain. Binary only. Feature engineering approach parallels\\\\n    our multi-feature pipeline but targets binary classification, not ordinal depth.\\\\n\\\\nli2024_mage:\\\\n  title: \\\\\\\"MAGE: Machine-generated Text Detection in the Wild\\\\\\\"\\\\n  authors: [Li, Li, et al.]\\\\n  venue: ACL 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2305.13242\\\\\\\"\\\\n  tags: [benchmark, cross-domain, cross-model, detection]\\\\n  relevance: indirect\\\\n  role: evaluation\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Cross-domain cross-model detection benchmark. Finds significant OOD\\\\n    performance degradation — same generalization challenge our cross-model\\\\n    depth estimation faces. Binary detection only.\\\\n\\\\nwu2025_detection_survey:\\\\n  title: \\\\\\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\\\\\"\\\\n  authors: [Wu, Yang, Zhan, Yuan, Chao, Wong]\\\\n  venue: Computational Linguistics, Vol. 51, Issue 1\\\\n  year: 2025\\\\n  arxiv: \\\\\\\"2310.14724\\\\\\\"\\\\n  tags: [survey, detection-taxonomy, watermarking, statistical, neural]\\\\n  relevance: indirect\\\\n  role: background\\\\n  verified: true\\\\n  integration: \\\\\\\"整合，survey 定位\\\\\\\"\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Comprehensive survey of detection paradigms: watermarking, statistical,\\\\n    neural, human-assisted. Positions our work as extending the statistical\\\\n    paradigm from binary detection to ordinal depth estimation.\\\\n\\\\n# =============================================================\\\\n# ADJACENT TASK — editing extent, attribution\\\\n# =============================================================\\\\n\\\\neditlens2026:\\\\n  title: \\\\\\\"EditLens: Quantifying the Extent of AI Editing in Text\\\\\\\"\\\\n  authors: [Thai et al.]\\\\n  venue: ICLR 2026\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2510.03154\\\\\\\"\\\\n  tags: [editing-extent, continuous-score, mixed-authorship]\\\\n  relevance: direct\\\\n  cite_in: [introduction, related-work]\\\\n  notes: >\\\\n    Closest conceptual neighbor — both go beyond binary classification.\\\\n    EditLens = single-pass editing extent; ours = multi-generation depth.\\\\n\\\\nuchendu2020_attribution:\\\\n  title: \\\\\\\"Authorship Attribution for Neural Text Generation\\\\\\\"\\\\n  authors: [Uchendu, Le, Shu, Lee]\\\\n  venue: EMNLP 2020\\\\n  year: 2020\\\\n  tags: [attribution, multi-source, authorship]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Multi-source attribution (which model?). We solve a different axis\\\\n    (how many iterations?) — complementary problems.\\\\n\\\\npu2026_generator_barrier:\\\\n  title: \\\\\\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\\\\\"\\\\n  authors: [Pu, Cheng, Yuan, Wu, Bi]\\\\n  venue: arXiv preprint\\\\n  year: 2026\\\\n  arxiv: \\\\\\\"2604.13692\\\\\\\"\\\\n  tags: [disentanglement, cross-generator, generalization]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Cross-generator generalization via disentanglement.\\\\n    Analogous to our cross-model generalization challenge.\\\\n\\\\n# --- R2-N2 supplement: attribution paradigms ---\\\\n\\\\nbevendorff2025_two_paradigms:\\\\n  title: \\\\\\\"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\\\\\\\"\\\\n  authors: [Bevendorff, Wiegmann, Richter, Potthast, Stein]\\\\n  venue: ACL 2025 Findings\\\\n  year: 2025\\\\n  tags: [attribution, verification, detection-paradigm, authorship]\\\\n  relevance: direct\\\\n  role: background\\\\n  verified: true\\\\n  integration: \\\\\\\"整合，'第三范式' framing（attribution/verification 之外的正交第三维度）\\\\\\\"\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Reframes LLM detection as authorship verification (not attribution).\\\\n    Our depth estimation is a third paradigm — ordinal characterization\\\\n    beyond binary verification or multi-class attribution. Key framing\\\\n    reference for positioning our contribution.\\\\n\\\\n# =============================================================\\\\n# METHOD COMPONENT — ordinal classification\\\\n# =============================================================\\\\n\\\\ncoral2020:\\\\n  title: \\\\\\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\\\\\"\\\\n  authors: [Cao, Mirjalili, Raschka]\\\\n  venue: Pattern Recognition Letters\\\\n  year: 2020\\\\n  arxiv: \\\\\\\"1901.07884\\\\\\\"\\\\n  tags: [ordinal-classification, rank-consistency, cumulative-logits]\\\\n  relevance: direct\\\\n  cite_in: [method, experiments]\\\\n  notes: >\\\\n    CORAL ordinal classification framework used in our baseline battery.\\\\n    Rank-consistent cumulative logits for ordinal targets.\\\\n\\\\ncloc2025:\\\\n  title: \\\\\\\"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\\\\\\\"\\\\n  authors: [Pitawela, Carneiro, et al.]\\\\n  venue: CVPR 2025\\\\n  year: 2025\\\\n  arxiv: \\\\\\\"2504.17813\\\\\\\"\\\\n  tags: [contrastive-learning, ordinal, multi-margin, N-pair]\\\\n  relevance: direct\\\\n  cite_in: [method, dcol-section]\\\\n  notes: >\\\\n    DCOL is our adaptation of CLOC to text depth estimation.\\\\n    Multi-margin N-pair loss for ordinal-aware contrastive learning.\\\\n    Must cite as methodological basis for DCOL section.\\\\n\\\\n# =============================================================\\\\n# WATERMARKING\\\\n# =============================================================\\\\n\\\\nkirchenbauer2023_watermark:\\\\n  title: \\\\\\\"A Watermark for Large Language Models\\\\\\\"\\\\n  authors: [Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein]\\\\n  venue: ICML 2023\\\\n  year: 2023\\\\n  arxiv: \\\\\\\"2301.10226\\\\\\\"\\\\n  tags: [watermarking, proactive-detection, green-list]\\\\n  relevance: indirect\\\\n  cite_in: [related-work]\\\\n  notes: >\\\\n    Proactive detection via watermarking. Complementary —\\\\n    watermarking requires generator cooperation; our method is post-hoc.\\\\n\\\\n# =============================================================\\\\n# DATA CURATION\\\\n# =============================================================\\\\n\\\\ndsir2023:\\\\n  title: \\\\\\\"Data Selection for Language Models via Importance Resampling\\\\\\\"\\\\n  authors: [Xie, Santurkar, Ma, Liang]\\\\n  venue: NeurIPS 2023\\\\n  year: 2023\\\\n  arxiv: \\\\\\\"2302.03169\\\\\\\"\\\\n  tags: [data-selection, importance-resampling, curation]\\\\n  relevance: indirect\\\\n  cite_in: [discussion]\\\\n  notes: >\\\\n    Quality-based data selection for LM training.\\\\n    Our depth estimation enables depth-graduated curation (Claim 3 / Discussion).\\\\n\\\\nqurating2024:\\\\n  title: \\\\\\\"QuRating: Selecting High-Quality Data for Training Language Models\\\\\\\"\\\\n  authors: [Wettig, Gupta, et al.]\\\\n  venue: ICML 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2402.09739\\\\\\\"\\\\n  tags: [quality-rating, data-curation, LLM-judgments]\\\\n  relevance: indirect\\\\n  cite_in: [discussion]\\\\n  notes: >\\\\n    LLM-based quality rating for data selection.\\\\n    Our depth score is a complementary quality axis.\\\\n\\\\n# --- R2-N2 supplement: data curation at scale ---\\\\n\\\\npenedo2024_fineweb:\\\\n  title: \\\\\\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\\\\\"\\\\n  authors: [Penedo, Kydlicek, et al.]\\\\n  venue: NeurIPS 2024\\\\n  year: 2024\\\\n  arxiv: \\\\\\\"2406.17557\\\\\\\"\\\\n  tags: [data-curation, quality-filtering, deduplication, web-scale]\\\\n  relevance: indirect\\\\n  role: background\\\\n  cite_in: [discussion]\\\\n  notes: >\\\\n    15T token dataset with systematic quality filtering pipeline (dedup,\\\\n    heuristic filters, classifier-based selection). Our depth estimation\\\\n    adds a synthetic contamination axis complementary to FineWeb-style\\\\n    quality curation — depth score can flag recursively degraded text\\\\n    that passes standard quality filters.\\\\n\\\\n# =============================================================\\\\n# COVARIATE SHIFT — technical background\\\\n# =============================================================\\\\n\\\\nsugiyama2007_importance_weighting:\\\\n  title: \\\\\\\"Covariate Shift Adaptation by Importance Weighted Cross Validation\\\\\\\"\\\\n  authors: [Sugiyama, Krauledat, Mueller]\\\\n  venue: JMLR\\\\n  year: 2007\\\\n  tags: [covariate-shift, importance-weighting, domain-adaptation]\\\\n  relevance: background\\\\n  cite_in: [discussion]\\\\n  notes: >\\\\n    Theoretical foundation for covariate shift correction.\\\\n    Our z-score normalization is a simplified distribution alignment.\\\\n\\\\n# =============================================================\\\\n# COVERAGE CHECKLIST (paper_framing.md Dream D002 requirements)\\\\n# =============================================================\\\\n# [x] watermarking: kirchenbauer2023_watermark\\\\n# [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,\\\\n#     dohmatob2024_tale_of_tails, dohmatob2025_strong_collapse,\\\\n#     dohmatob2024_demystified, gerstgrasser2024_accumulate\\\\n# [x] model collapse empirical: drayson2025, bakshi2026, marchi2024,\\\\n#     shi2025_closer_look (VERIFIED), yi2026_escaping_collapse (VERIFIED, workshop)\\\\n# [x] data curation: dsir2023, qurating2024, penedo2024_fineweb (NEW)\\\\n# [x] multi-source attribution: uchendu2020_attribution,\\\\n#     bevendorff2025_two_paradigms (VERIFIED)\\\\n# [x] binary detectors: mitchell2023_detectgpt, sadasivan2023_paraphrase,\\\\n#     binoculars2024, fast_detectgpt2024, diveye2026, loki2025,\\\\n#     tulchinskii2024_intrinsic_dim (NEW), verma2024_ghostbuster (NEW),\\\\n#     li2024_mage (NEW)\\\\n# [x] detection survey: wu2025_detection_survey (VERIFIED)\\\\n# [x] decoding strategy effects: garces_arias2025, holtzman2020_nucleus,\\\\n#     wiher2022_decoding, basu2021_mirostat, finlayson2024_closing\\\\n# [x] ordinal classification: coral2020, cloc2025\\\\n# [x] adjacent tasks: editlens2026\\\\n# [x] covariate shift: sugiyama2007\\\\n# [x] statistical detection foundation: gehrmann2019_gltr\\\\n#\\\\n# Total unique entries: 43 (35 original + 8 R2-N2 supplement)\\\\n# 2024-2026 papers: 30/43 (70% recent coverage)\\\\n# Direct relevance: 12 entries\\\\n\\\", \\\"total_chars\\\": 26296, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/literature_map.yaml\", \"content\": \"# Literature Map — recursive_gen_depth_est\\n# Last updated: 2026-05-15\\n# Purpose: Systematic reference tracking for EMNLP ARR May 25 submission\\n# Total entries: 43 (35 original + 8 R2-N2 supplement)\\n#\\n# Tags used for cite_in: introduction, related-work, background, method,\\n#   experiments, discussion, limitations, dcol-section\\n\\n# =============================================================\\n# MODEL COLLAPSE — foundational theory & recursive generation\\n# =============================================================\\n\\nshumailov2024_nature:\\n  title: \\\"AI models collapse when trained on recursively generated data\\\"\\n  authors: [Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal]\\n  venue: Nature\\n  year: 2024\\n  doi: \\\"10.1038/s41586-024-07566-y\\\"\\n  tags: [model-collapse, recursive-generation, tail-erosion]\\n  relevance: direct\\n  cite_in: [introduction, related-work, background]\\n  notes: >\\n    Foundational model collapse paper. Tail erosion across recursive generations.\\n    Perplexity monotonically increases over 40 generations. Does NOT compare\\n    sampling strategies—uses standard sampling (T=1).\\n\\nmarchi2024_heat_death:\\n  title: \\\"Heat Death of Generative Models in Closed-Loop Learning\\\"\\n  authors: [Marchi, Soatto, Chaudhari, Tabuada]\\n  venue: ICASSP 2025\\n  year: 2024\\n  arxiv: \\\"2404.02325\\\"\\n  tags: [temperature, convergence, dynamical-systems, mode-collapse]\\n  relevance: direct\\n  cite_in: [discussion]\\n  notes: >\\n    Proves any T!=1 causes asymptotic degeneration. T<1 amplifies probability\\n    differences (mode collapse), T>1 contracts toward uniform. Key theoretical\\n    support for our tau=0.9 accelerated convergence finding.\\n\\ndohmatob2024_tale_of_tails:\\n  title: \\\"A Tale of Tails: Model Collapse as a Change of Scaling Laws\\\"\\n  authors: [Dohmatob, Feng, Yang, Charton, Kempe]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2402.07043\\\"\\n  tags: [scaling-laws, tail-narrowing, tail-cutting, temperature, top-p, top-k]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Distinguishes tail narrowing (temperature: q_i^T ~ i^{-beta/T}) from\\n    tail cutting (top-p/top-k: hard truncation). Different degradation patterns.\\n    Explains why temp produces different statistical fingerprint from truncation.\\n\\ndohmatob2025_strong_collapse:\\n  title: \\\"Strong Model Collapse\\\"\\n  authors: [Dohmatob, Feng, Subramonian, Kempe]\\n  venue: ICLR 2025 Spotlight\\n  year: 2025\\n  arxiv: \\\"2410.04840\\\"\\n  tags: [model-collapse, scaling, synthetic-data]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Even 0.1% synthetic data fraction causes collapse. Larger models amplify collapse.\\n    Bias-variance decomposition via random projections.\\n\\ndohmatob2024_demystified:\\n  title: \\\"Model Collapse Demystified: The Case of Regression\\\"\\n  authors: [Dohmatob, Feng, Kempe]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv: \\\"2402.07712\\\"\\n  tags: [model-collapse, regression, random-matrix-theory]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Test error grows linearly with iteration count in regression.\\n    Supports our finding of monotonically evolving features across depths.\\n\\nalemohammad2024_mad:\\n  title: \\\"Self-Consuming Generative Models Go MAD\\\"\\n  authors: [Alemohammad, Casco-Rodriguez, et al.]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2307.01850\\\"\\n  tags: [autophagous, sampling-bias, precision-recall, MAD]\\n  relevance: indirect\\n  cite_in: [introduction, related-work]\\n  notes: >\\n    Biased sampling keeps precision but kills recall. Unbiased causes mode drift.\\n    tau=0.9 maps to their biased sampling regime.\\n\\ngerstgrasser2024_accumulate:\\n  title: \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\"\\n  authors: [Gerstgrasser, Schaeffer, et al.]\\n  venue: arXiv preprint\\n  year: 2024\\n  arxiv: \\\"2404.01413\\\"\\n  tags: [model-collapse, data-accumulation, mitigation]\\n  relevance: indirect\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Data accumulation prevents collapse (bounded test error).\\n    Important caveat: in accumulation regime, depth signal may be weaker.\\n\\ndrayson2025_detection_prevents_collapse:\\n  title: \\\"Machine-generated text detection prevents language model collapse\\\"\\n  authors: [Drayson et al.]\\n  venue: EMNLP 2025 Findings\\n  year: 2025\\n  arxiv: \\\"2502.15654\\\"\\n  tags: [temperature, diversity, recursive-training, detection]\\n  relevance: direct\\n  cite_in: [related-work]\\n  notes: >\\n    Temperature tau=0.9 produces most repetitive outputs; diversity drops ~70%\\n    over 99 recursive generations (GPT-2, SmolLM2). Perplexity degradation more\\n    moderate than deterministic methods. Detection as filter vs our depth estimation.\\n\\nbakshi2026_collapse_improvement:\\n  title: \\\"From Collapse to Improvement: Statistical Perspectives on Iterative Training\\\"\\n  authors: [Bakshi, Chakraborty]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2602.10531\\\"\\n  tags: [model-collapse, non-monotonic, data-mixing]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Iterative training with fresh real data can *improve* performance.\\n    Non-monotonic dynamics complicate simple depth-signal assumptions.\\n\\nwang2026_contamination:\\n  title: \\\"Can Generative AI Survive Data Contamination? Theoretical Guarantees\\\"\\n  authors: [Wang, Niu, Li]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2602.16065\\\"\\n  tags: [model-collapse, contamination, theoretical]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Extends collapse theory beyond Gaussian/discrete to realistic distributions.\\n    Provides theoretical grounding for depth signal existence.\\n\\nfalahati2026_curated:\\n  title: \\\"Curated Synthetic Data Doesn't Have to Collapse\\\"\\n  authors: [Falahati, Amiri, Larson, Golab]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2605.07724\\\"\\n  tags: [curation, collapse-prevention, pluralistic]\\n  relevance: indirect\\n  cite_in: [discussion, limitations]\\n  notes: >\\n    Pluralistic curation prevents collapse. Harder case for our method —\\n    curated pipelines may produce depth-invariant text.\\n\\nknowledge_collapse2025:\\n  title: \\\"Knowledge Collapse in LLMs: Fluency Survives but Facts Fail\\\"\\n  authors: [Keisha, Wu, Wang, Koshiyama, Treleaven]\\n  venue: arXiv preprint\\n  year: 2025\\n  arxiv: \\\"2509.04796\\\"\\n  tags: [knowledge-collapse, fluency, factual-degradation]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Three-stage collapse: factual accuracy degrades while fluency persists.\\n    Surface perplexity features still capture depth signal despite fluency preservation.\\n\\nsynthetic_eggs2026:\\n  title: \\\"Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning\\\"\\n  authors: [Schaffelder, Gatt]\\n  venue: ACL 2026 Findings\\n  year: 2026\\n  arxiv: \\\"2511.01490\\\"\\n  tags: [diversity, collapse-mitigation, Self-BLEU]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multi-source synthetic data reduces collapse. Their diversity metrics\\n    (Self-BLEU, lexical diversity) are candidate depth features.\\n\\nmohamed2025_broken_telephone:\\n  title: \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\"\\n  authors: [Mohamed, Geng, Vazirgiannis, Shang]\\n  venue: ACL 2025\\n  year: 2025\\n  arxiv: \\\"2502.20258\\\"\\n  tags: [iterative-generation, information-distortion, translation-chain]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Iterative generation (translation/paraphrase chains) produces monotonically\\n    increasing information distortion. Cross-task evidence that iterated signals\\n    accumulate — supports our depth signal persistence finding.\\n\\nsigma2026_spectral:\\n  title: \\\"SIGMA: Scalable Spectral Insights for LLM Model Collapse\\\"\\n  authors: [\\\"(multiple)\\\"]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2601.03385\\\"\\n  tags: [spectral-analysis, gram-matrix, representation-collapse, 50-generations]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Gram matrix spectral analysis tracks representation space contraction over\\n    50 recursive generations. Proposes Sigma-UB metric. Complementary to our\\n    EDD — they measure geometric collapse, we measure statistical distinguishability.\\n    Tests 50 generations but does NOT do inter-generation classification.\\n\\n# --- R2-N2 supplement: model collapse empirical ---\\n\\nshi2025_closer_look:\\n  title: \\\"A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective\\\"\\n  authors: [Shi, Wu, Zhang, Zhang, Tao, Qu]\\n  venue: NeurIPS 2025 (Spotlight)\\n  year: 2025\\n  arxiv: \\\"2509.16499\\\"\\n  tags: [model-collapse, entropy, memorization, intrinsic-dimension]\\n  relevance: direct\\n  role: background\\n  verified: true\\n  integration: \\\"整合，entropy ↔ depth signal 支撑特征选择论证\\\"\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Identifies generalization-to-memorization transition during recursive training.\\n    Entropy of training data decreases over iterations, strongly correlated with\\n    model degradation. Entropy decline IS a measurable depth signal — directly\\n    supports our statistical feature approach to depth estimation.\\n\\nyi2026_escaping_collapse:\\n  title: \\\"Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence\\\"\\n  authors: [Yi, Liu, Cheng, Xu]\\n  venue: 3rd DATA-FM Workshop @ ICLR 2026\\n  year: 2026\\n  arxiv: \\\"2510.16657\\\"\\n  tags: [model-collapse, verification, synthetic-data, mitigation]\\n  relevance: indirect\\n  role: background\\n  verified: true\\n  integration: \\\"引用但降级——related work 提一句，不支撑核心 claim（workshop paper）\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Verifier-guided retraining prevents collapse. Our depth estimation\\n    can serve AS the verifier — depth score enables graduated filtering\\n    rather than binary accept/reject. NOTE: workshop paper, not main conference.\\n\\n# =============================================================\\n# DECODING STRATEGIES\\n# =============================================================\\n\\nholtzman2020_nucleus:\\n  title: \\\"The Curious Case of Neural Text Degeneration\\\"\\n  authors: [Holtzman, Buys, Du, Forbes, Choi]\\n  venue: ICLR 2020\\n  year: 2020\\n  arxiv: \\\"1904.09751\\\"\\n  tags: [nucleus-sampling, temperature, text-degeneration, unreliable-tail]\\n  relevance: indirect\\n  cite_in: [background, method]\\n  notes: >\\n    Proposes nucleus sampling. Temperature+top-k leads to repetition.\\n    Key concept: unreliable tail of low-probability tokens.\\n\\nfinlayson2024_closing:\\n  title: \\\"Closing the Curious Case of Neural Text Degeneration\\\"\\n  authors: [Finlayson, Hewitt, Koller, Swayamdipta, Sabharwal]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2310.01693\\\"\\n  tags: [softmax-bottleneck, truncation-sampling, precise-sampling]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Truncation sampling eliminates softmax bottleneck errors. Mechanistic\\n    difference between truncation and scaling approaches.\\n\\ngarces_arias2025_decoding_decoded:\\n  title: \\\"Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation\\\"\\n  authors: [Garces Arias et al.]\\n  venue: COLING 2025\\n  year: 2025\\n  tags: [decoding, hyperparameters, model-dependent]\\n  relevance: direct\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Confirms optimal decoding configuration is model-dependent.\\n    Directly supports D006 finding (strategy effect is model-dependent).\\n    Key external validation for our interaction effects claim.\\n\\nwiher2022_decoding:\\n  title: \\\"On Decoding Strategies for Neural Text Generators\\\"\\n  authors: [Wiher, Meister, Cotterell]\\n  venue: TACL 2022\\n  year: 2022\\n  tags: [decoding, task-dependent, evaluation]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Decoding strategy effects are task-dependent.\\n    Supports our finding that strategy effects on depth signal vary by model.\\n\\nbasu2021_mirostat:\\n  title: \\\"Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity\\\"\\n  authors: [Basu, Sachdev, Kamdar, Nishi]\\n  venue: ICLR 2021\\n  year: 2021\\n  tags: [perplexity-control, sampling, cross-entropy]\\n  relevance: indirect\\n  cite_in: [related-work, discussion]\\n  notes: >\\n    Perplexity and sampling parameters have non-linear relationship.\\n    Relevant to p90_ppl capturing depth signal better than mean_ppl\\n    under heavy-tailed distributions.\\n\\n# =============================================================\\n# BINARY / ZERO-SHOT DETECTION\\n# =============================================================\\n\\nmitchell2023_detectgpt:\\n  title: \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\"\\n  authors: [Mitchell, Lee, Khazatsky, Manning, Finn]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv: \\\"2301.11305\\\"\\n  tags: [zero-shot, detection, curvature, perturbation, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Foundational zero-shot detector using log-probability curvature via\\n    random perturbations. Binary only. Fast-DetectGPT improves efficiency.\\n\\nsadasivan2023_paraphrase:\\n  title: \\\"Can AI-Generated Text be Reliably Detected?\\\"\\n  authors: [Sadasivan, Kumar, Balasubramanian, Wang, Feizi]\\n  venue: arXiv preprint\\n  year: 2023\\n  arxiv: \\\"2303.11156\\\"\\n  tags: [detection-limits, paraphrase-attack, impossibility]\\n  relevance: indirect\\n  cite_in: [related-work, limitations]\\n  notes: >\\n    Shows paraphrase attacks evade all detectors; proves impossibility\\n    result when model and human distributions overlap sufficiently.\\n    Important limitation context for our depth estimation approach.\\n\\nbinoculars2024:\\n  title: \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\"\\n  authors: [Hans, Schwarzschild, Manber, et al.]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2401.12070\\\"\\n  tags: [zero-shot, detection, perplexity-ratio, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Two-model perplexity ratio for zero-shot binary detection.\\n    We extend beyond binary to ordinal depth.\\n\\nfast_detectgpt2024:\\n  title: \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\"\\n  authors: [Bao et al.]\\n  venue: ICLR 2024\\n  year: 2024\\n  arxiv: \\\"2310.05130\\\"\\n  tags: [zero-shot, detection, curvature, binary]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Conditional probability curvature for efficient binary detection.\\n    Cannot distinguish depth levels.\\n\\ndiveye2026:\\n  title: \\\"DivEye: Diversity Boosts AI-Generated Text Detection\\\"\\n  authors: [Basani, Chen]\\n  venue: ICLR 2026 / TMLR\\n  year: 2026\\n  arxiv: \\\"2509.18880\\\"\\n  tags: [surprisal-diversity, statistical-features, detection]\\n  relevance: direct\\n  cite_in: [related-work, method]\\n  notes: >\\n    Token-level surprisal diversity features for binary detection.\\n    Feature overlap with our pipeline. We extend similar features\\n    to ordinal depth regression.\\n\\nloki2025:\\n  title: \\\"LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models\\\"\\n  authors: [Ye, Zhou, Huang, Zhang, Bai, Kang, He, Lin, Wang, Wu, Wu, Chen, Lin, He, Li]\\n  venue: ICLR 2025 Spotlight\\n  year: 2025\\n  arxiv: \\\"2410.09732\\\"\\n  tags: [benchmark, multimodal, detection]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multimodal synthetic data detection benchmark. Binary only, no depth.\\n\\ngehrmann2019_gltr:\\n  title: \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\"\\n  authors: [Gehrmann, Strobelt, Rush]\\n  venue: ACL 2019\\n  year: 2019\\n  arxiv: \\\"1906.04043\\\"\\n  tags: [detection, statistical-features, perplexity, rank, entropy]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Foundational statistical detection using log-likelihood, rank, entropy.\\n    Our feature system extends this paradigm to recursive depth estimation.\\n\\npudasaini2026_detection_fails:\\n  title: \\\"Why AI-Generated Text Detection Fails: Evidence from Explainable AI\\\"\\n  authors: [Pudasaini et al.]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2603.23146\\\"\\n  tags: [detection-failure, distribution-shift, fragility]\\n  relevance: indirect\\n  cite_in: [limitations]\\n  notes: >\\n    Detection features degrade under distribution shift.\\n    If binary features are domain-fragile, ordinal depth features may be too.\\n\\n# --- R2-N2 supplement: detection methods ---\\n\\ntulchinskii2024_intrinsic_dim:\\n  title: \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\"\\n  authors: [Tulchinskii, Kuznetsov, et al.]\\n  venue: NeurIPS 2023\\n  year: 2023\\n  arxiv: \\\"2306.04723\\\"\\n  tags: [intrinsic-dimension, geometric-features, detection, cross-domain]\\n  relevance: direct\\n  role: method-component\\n  cite_in: [related-work, method]\\n  notes: >\\n    Intrinsic dimension of text embeddings ~9 for human, ~7.5 for AI-generated.\\n    Geometric invariant enables cross-domain, cross-model robust detection.\\n    Complementary feature family to our statistical perplexity features —\\n    intrinsic dimension could serve as additional depth feature.\\n\\nverma2024_ghostbuster:\\n  title: \\\"Ghostbuster: Detecting Text Ghostwritten by Large Language Models\\\"\\n  authors: [Verma, Fleisig, Tomlin, Klein]\\n  venue: NAACL 2024\\n  year: 2024\\n  arxiv: \\\"2305.15047\\\"\\n  tags: [detection, structured-search, statistical-features, cross-domain]\\n  relevance: indirect\\n  role: direct-competitor\\n  cite_in: [related-work]\\n  notes: >\\n    Structured search over combinations of weaker LM features for detection.\\n    99.0 F1 cross-domain. Binary only. Feature engineering approach parallels\\n    our multi-feature pipeline but targets binary classification, not ordinal depth.\\n\\nli2024_mage:\\n  title: \\\"MAGE: Machine-generated Text Detection in the Wild\\\"\\n  authors: [Li, Li, et al.]\\n  venue: ACL 2024\\n  year: 2024\\n  arxiv: \\\"2305.13242\\\"\\n  tags: [benchmark, cross-domain, cross-model, detection]\\n  relevance: indirect\\n  role: evaluation\\n  cite_in: [related-work]\\n  notes: >\\n    Cross-domain cross-model detection benchmark. Finds significant OOD\\n    performance degradation — same generalization challenge our cross-model\\n    depth estimation faces. Binary detection only.\\n\\nwu2025_detection_survey:\\n  title: \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\"\\n  authors: [Wu, Yang, Zhan, Yuan, Chao, Wong]\\n  venue: Computational Linguistics, Vol. 51, Issue 1\\n  year: 2025\\n  arxiv: \\\"2310.14724\\\"\\n  tags: [survey, detection-taxonomy, watermarking, statistical, neural]\\n  relevance: indirect\\n  role: background\\n  verified: true\\n  integration: \\\"整合，survey 定位\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Comprehensive survey of detection paradigms: watermarking, statistical,\\n    neural, human-assisted. Positions our work as extending the statistical\\n    paradigm from binary detection to ordinal depth estimation.\\n\\n# =============================================================\\n# ADJACENT TASK — editing extent, attribution\\n# =============================================================\\n\\neditlens2026:\\n  title: \\\"EditLens: Quantifying the Extent of AI Editing in Text\\\"\\n  authors: [Thai et al.]\\n  venue: ICLR 2026\\n  year: 2026\\n  arxiv: \\\"2510.03154\\\"\\n  tags: [editing-extent, continuous-score, mixed-authorship]\\n  relevance: direct\\n  cite_in: [introduction, related-work]\\n  notes: >\\n    Closest conceptual neighbor — both go beyond binary classification.\\n    EditLens = single-pass editing extent; ours = multi-generation depth.\\n\\nuchendu2020_attribution:\\n  title: \\\"Authorship Attribution for Neural Text Generation\\\"\\n  authors: [Uchendu, Le, Shu, Lee]\\n  venue: EMNLP 2020\\n  year: 2020\\n  tags: [attribution, multi-source, authorship]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Multi-source attribution (which model?). We solve a different axis\\n    (how many iterations?) — complementary problems.\\n\\npu2026_generator_barrier:\\n  title: \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\"\\n  authors: [Pu, Cheng, Yuan, Wu, Bi]\\n  venue: arXiv preprint\\n  year: 2026\\n  arxiv: \\\"2604.13692\\\"\\n  tags: [disentanglement, cross-generator, generalization]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Cross-generator generalization via disentanglement.\\n    Analogous to our cross-model generalization challenge.\\n\\n# --- R2-N2 supplement: attribution paradigms ---\\n\\nbevendorff2025_two_paradigms:\\n  title: \\\"The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification\\\"\\n  authors: [Bevendorff, Wiegmann, Richter, Potthast, Stein]\\n  venue: ACL 2025 Findings\\n  year: 2025\\n  tags: [attribution, verification, detection-paradigm, authorship]\\n  relevance: direct\\n  role: background\\n  verified: true\\n  integration: \\\"整合，'第三范式' framing（attribution/verification 之外的正交第三维度）\\\"\\n  cite_in: [related-work]\\n  notes: >\\n    Reframes LLM detection as authorship verification (not attribution).\\n    Our depth estimation is a third paradigm — ordinal characterization\\n    beyond binary verification or multi-class attribution. Key framing\\n    reference for positioning our contribution.\\n\\n# =============================================================\\n# METHOD COMPONENT — ordinal classification\\n# =============================================================\\n\\ncoral2020:\\n  title: \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\"\\n  authors: [Cao, Mirjalili, Raschka]\\n  venue: Pattern Recognition Letters\\n  year: 2020\\n  arxiv: \\\"1901.07884\\\"\\n  tags: [ordinal-classification, rank-consistency, cumulative-logits]\\n  relevance: direct\\n  cite_in: [method, experiments]\\n  notes: >\\n    CORAL ordinal classification framework used in our baseline battery.\\n    Rank-consistent cumulative logits for ordinal targets.\\n\\ncloc2025:\\n  title: \\\"CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss\\\"\\n  authors: [Pitawela, Carneiro, et al.]\\n  venue: CVPR 2025\\n  year: 2025\\n  arxiv: \\\"2504.17813\\\"\\n  tags: [contrastive-learning, ordinal, multi-margin, N-pair]\\n  relevance: direct\\n  cite_in: [method, dcol-section]\\n  notes: >\\n    DCOL is our adaptation of CLOC to text depth estimation.\\n    Multi-margin N-pair loss for ordinal-aware contrastive learning.\\n    Must cite as methodological basis for DCOL section.\\n\\n# =============================================================\\n# WATERMARKING\\n# =============================================================\\n\\nkirchenbauer2023_watermark:\\n  title: \\\"A Watermark for Large Language Models\\\"\\n  authors: [Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein]\\n  venue: ICML 2023\\n  year: 2023\\n  arxiv: \\\"2301.10226\\\"\\n  tags: [watermarking, proactive-detection, green-list]\\n  relevance: indirect\\n  cite_in: [related-work]\\n  notes: >\\n    Proactive detection via watermarking. Complementary —\\n    watermarking requires generator cooperation; our method is post-hoc.\\n\\n# =============================================================\\n# DATA CURATION\\n# =============================================================\\n\\ndsir2023:\\n  title: \\\"Data Selection for Language Models via Importance Resampling\\\"\\n  authors: [Xie, Santurkar, Ma, Liang]\\n  venue: NeurIPS 2023\\n  year: 2023\\n  arxiv: \\\"2302.03169\\\"\\n  tags: [data-selection, importance-resampling, curation]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    Quality-based data selection for LM training.\\n    Our depth estimation enables depth-graduated curation (Claim 3 / Discussion).\\n\\nqurating2024:\\n  title: \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\"\\n  authors: [Wettig, Gupta, et al.]\\n  venue: ICML 2024\\n  year: 2024\\n  arxiv: \\\"2402.09739\\\"\\n  tags: [quality-rating, data-curation, LLM-judgments]\\n  relevance: indirect\\n  cite_in: [discussion]\\n  notes: >\\n    LLM-based quality rating for data selection.\\n    Our depth score is a complementary quality axis.\\n\\n# --- R2-N2 supplement: data curation at scale ---\\n\\npenedo2024_fineweb:\\n  title: \\\"The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale\\\"\\n  authors: [Penedo, Kydlicek, et al.]\\n  venue: NeurIPS 2024\\n  year: 2024\\n  arxiv: \\\"2406.17557\\\"\\n  tags: [data-curation, quality-filtering, deduplication, web-scale]\\n  relevance: indirect\\n  role: background\\n  cite_in: [discussion]\\n  notes: >\\n    15T token dataset with systematic quality filtering pipeline (dedup,\\n    heuristic filters, classifier-based selection). Our depth estimation\\n    adds a synthetic contamination axis complementary to FineWeb-style\\n    quality curation — depth score can flag recursively degraded text\\n    that passes standard quality filters.\\n\\n# =============================================================\\n# COVARIATE SHIFT — technical background\\n# =============================================================\\n\\nsugiyama2007_importance_weighting:\\n  title: \\\"Covariate Shift Adaptation by Importance Weighted Cross Validation\\\"\\n  authors: [Sugiyama, Krauledat, Mueller]\\n  venue: JMLR\\n  year: 2007\\n  tags: [covariate-shift, importance-weighting, domain-adaptation]\\n  relevance: background\\n  cite_in: [discussion]\\n  notes: >\\n    Theoretical foundation for covariate shift correction.\\n    Our z-score normalization is a simplified distribution alignment.\\n\\n# =============================================================\\n# COVERAGE CHECKLIST (paper_framing.md Dream D002 requirements)\\n# =============================================================\\n# [x] watermarking: kirchenbauer2023_watermark\\n# [x] model collapse theory: shumailov2024_nature, alemohammad2024_mad,\\n#     dohmatob2024_tale_of_tails, dohmatob2025_strong_collapse,\\n#     dohmatob2024_demystified, gerstgrasser2024_accumulate\\n# [x] model collapse empirical: drayson2025, bakshi2026, marchi2024,\\n#     shi2025_closer_look (VERIFIED), yi2026_escaping_collapse (VERIFIED, workshop)\\n# [x] data curation: dsir2023, qurating2024, penedo2024_fineweb (NEW)\\n# [x] multi-source attribution: uchendu2020_attribution,\\n#     bevendorff2025_two_paradigms (VERIFIED)\\n# [x] binary detectors: mitchell2023_detectgpt, sadasivan2023_paraphrase,\\n#     binoculars2024, fast_detectgpt2024, diveye2026, loki2025,\\n#     tulchinskii2024_intrinsic_dim (NEW), verma2024_ghostbuster (NEW),\\n#     li2024_mage (NEW)\\n# [x] detection survey: wu2025_detection_survey (VERIFIED)\\n# [x] decoding strategy effects: garces_arias2025, holtzman2020_nucleus,\\n#     wiher2022_decoding, basu2021_mirostat, finlayson2024_closing\\n# [x] ordinal classification: coral2020, cloc2025\\n# [x] adjacent tasks: editlens2026\\n# [x] covariate shift: sugiyama2007\\n# [x] statistical detection foundation: gehrmann2019_gltr\\n#\\n# Total unique entries: 43 (35 original + 8 R2-N2 supplement)\\n# 2024-2026 papers: 30/43 (70% recent coverage)\\n# Direct relevance: 12 entries\\n\", \"total_chars\": 26296, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the literature map with 43 entries. Now let me read the current bib file and related_work.tex to understand the current state.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "69c1d95f-66b0-48b6-8919-e326538e72ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM9HHtdddeCz6vsUwqWR7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9935,
      "cache_read_input_tokens": 26167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9935
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

_source line 20_

Now let me read the current bib file and related_work.tex.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "67832bf5-0991-4cef-b1a5-873af4f26bcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM9HHtdddeCz6vsUwqWR7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9935,
      "cache_read_input_tokens": 26167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9935
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

<details open><summary>🔧 Tool call — Read · `toolu_012jvw5du1pdQMzFFhA4b8bS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "4c4e3e28-de28-4972-9cc2-eabb078f4f51",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM9HHtdddeCz6vsUwqWR7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9935,
      "cache_read_input_tokens": 26167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9935
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

_source line 22 · 2026-05-17T17:05:20.447Z_

<details><summary>↩ Tool result · `toolu_012jvw5du1pdQMzFFhA4b8bS`</summary>

```text
1	% ============================================================
2	% Model Collapse Theory
3	% ============================================================
4	
5	@article{shumailov2024_nature,
6	  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
7	  title     = {{AI models collapse when trained on recursively generated data}},
8	  journal   = {Nature},
9	  volume    = {631},
10	  pages     = {755--759},
11	  year      = {2024},
12	  doi       = {10.1038/s41586-024-07566-y},
13	}
14	
15	@inproceedings{dohmatob2024_tale_of_tails,
16	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},
17	  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},
18	  booktitle = {Proceedings of ICML},
19	  year      = {2024},
20	  note      = {arXiv:2402.07043},
21	  url       = {https://arxiv.org/abs/2402.07043},
22	}
23	
24	@inproceedings{dohmatob2025_strong_collapse,
25	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
26	  title     = {{Strong Model Collapse}},
27	  booktitle = {Proceedings of ICLR},
28	  year      = {2025},
29	  note      = {arXiv:2410.04840},
30	  url       = {https://arxiv.org/abs/2410.04840},
31	}
32	
33	@inproceedings{dohmatob2024_demystified,
34	  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},
35	  title     = {{Model Collapse Demystified: The Case of Regression}},
36	  booktitle = {Proceedings of NeurIPS},
37	  year      = {2024},
38	  note      = {arXiv:2402.07712},
39	  url       = {https://arxiv.org/abs/2402.07712},
40	}
41	
42	@inproceedings{alemohammad2024_mad,
43	  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
44	  title     = {{Self-Consuming Generative Models Go MAD}},
45	  booktitle = {Proceedings of ICLR},
46	  year      = {2024},
47	  note      = {arXiv:2307.01850},
48	  url       = {https://arxiv.org/abs/2307.01850},
49	}
50	
51	@misc{gerstgrasser2024_accumulate,
52	  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
53	  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
54	  year      = {2024},
55	  howpublished = {arXiv:2404.01413},
56	  url       = {https://arxiv.org/abs/2404.01413},
57	}
58	
59	@inproceedings{marchi2024_heat_death,
60	  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},
61	  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},
62	  booktitle = {Proceedings of ICASSP},
63	  year      = {2024},
64	  note      = {arXiv:2404.02325},
65	  url       = {https://arxiv.org/abs/2404.02325},
66	}
67	
68	@misc{knowledge_collapse2025,
69	  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},
70	  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},
71	  year      = {2025},
72	  howpublished = {arXiv:2509.04796},
73	  url       = {https://arxiv.org/abs/2509.04796},
74	}
75	
76	@misc{sigma2026_spectral,
77	  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},
78	  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},
79	  year      = {2026},
80	  howpublished = {arXiv:2601.03385},
81	  url       = {https://arxiv.org/abs/2601.03385},
82	}
83	
84	@inproceedings{mohamed2025_broken_telephone,
85	  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
86	  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
87	  booktitle = {Proceedings of ACL},
88	  year      = {2025},
89	  note      = {arXiv:2502.20258},
90	  url       = {https://arxiv.org/abs/2502.20258},
91	}
92	
93	@inproceedings{synthetic_eggs2026,
94	  author    = {Schaffelder, Max and Gatt, Albert},
95	  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},
96	  booktitle = {Findings of ACL},
97	  year      = {2026},
98	  note      = {arXiv:2511.01490},
99	  url       = {https://arxiv.org/abs/2511.01490},
100	}
101	
102	@inproceedings{shi2025_closer_look,
103	  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},
104	  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},
105	  booktitle = {Proceedings of NeurIPS},
106	  year      = {2025},
107	  note      = {Spotlight},
108	}
109	
110	@inproceedings{yi2026_escaping_collapse,
111	  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},
112	  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},
113	  booktitle = {3rd DATA-FM Workshop at ICLR 2026},
114	  year      = {2026},
115	}
116	
117	% --- Model collapse: collapse-can-be-avoided / contamination ---
118	
119	@inproceedings{drayson2025_detection_prevents_collapse,
120	  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},
121	  title     = {{Machine-generated text detection prevents language model collapse}},
122	  booktitle = {Findings of EMNLP},
123	  year      = {2025},
124	  note      = {arXiv:2502.15654},
125	  url       = {https://arxiv.org/abs/2502.15654},
126	}
127	
128	@misc{bakshi2026_collapse_improvement,
129	  author    = {Bakshi, Soham and Chakraborty, Sunrit},
130	  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},
131	  year      = {2026},
132	  howpublished = {arXiv:2602.10531},
133	  url       = {https://arxiv.org/abs/2602.10531},
134	}
135	
136	@misc{wang2026_contamination,
137	  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},
138	  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},
139	  year      = {2026},
140	  howpublished = {arXiv:2602.16065},
141	  url       = {https://arxiv.org/abs/2602.16065},
142	}
143	
144	@misc{falahati2026_curated,
145	  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},
146	  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},
147	  year      = {2026},
148	  howpublished = {arXiv:2605.07724},
149	  url       = {https://arxiv.org/abs/2605.07724},
150	}
151	
152	% ============================================================
153	% AI-Generated Text Detection
154	% ============================================================
155	
156	@article{wu2025_detection_survey,
157	  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
158	  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
159	  journal   = {Computational Linguistics},
160	  volume    = {51},
161	  number    = {1},
162	  pages     = {275--354},
163	  year      = {2025},
164	  publisher = {MIT Press},
165	}
166	
167	% --- Statistical / zero-shot detectors ---
168	
169	@inproceedings{gehrmann2019_gltr,
170	  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
171	  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},
172	  booktitle = {Proceedings of ACL: System Demonstrations},
173	  year      = {2019},
174	  note      = {arXiv:1906.04043},
175	  url       = {https://arxiv.org/abs/1906.04043},
176	}
177	
178	@inproceedings{mitchell2023_detectgpt,
179	  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
180	  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
181	  booktitle = {Proceedings of ICML},
182	  year      = {2023},
183	  note      = {arXiv:2301.11305},
184	  url       = {https://arxiv.org/abs/2301.11305},
185	}
186	
187	@inproceedings{fast_detectgpt2024,
188	  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
189	  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
190	  booktitle = {Proceedings of ICLR},
191	  year      = {2024},
192	  note      = {arXiv:2310.05130},
193	  url       = {https://arxiv.org/abs/2310.05130},
194	}
195	
196	@inproceedings{binoculars2024,
197	  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
198	  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
199	  booktitle = {Proceedings of ICML},
200	  year      = {2024},
201	  note      = {arXiv:2401.12070},
202	  url       = {https://arxiv.org/abs/2401.12070},
203	}
204	
205	@article{diveye2026,
206	  author    = {Basani, Advik Raj and Chen, Pin-Yu},
207	  title     = {{Diversity Boosts AI-Generated Text Detection}},
208	  journal   = {Transactions on Machine Learning Research (TMLR)},
209	  year      = {2026},
210	  note      = {arXiv:2509.18880},
211	  url       = {https://arxiv.org/abs/2509.18880},
212	}
213	
214	% --- Robustness / limitations of detectors ---
215	
216	@misc{sadasivan2023_paraphrase,
217	  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
218	  title     = {{Can AI-Generated Text be Reliably Detected?}},
219	  year      = {2023},
220	  howpublished = {arXiv:2303.11156},
221	  url       = {https://arxiv.org/abs/2303.11156},
222	}
223	
224	@misc{pudasaini2026_detection_fails,
225	  author    = {Pudasaini, Shushanta and Miralles-Pech{\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},
226	  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},
227	  year      = {2026},
228	  howpublished = {arXiv:2603.23146},
229	  url       = {https://arxiv.org/abs/2603.23146},
230	}
231	
232	@misc{pu2026_generator_barrier,
233	  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
234	  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
235	  year      = {2026},
236	  howpublished = {arXiv:2604.13692},
237	  url       = {https://arxiv.org/abs/2604.13692},
238	}
239	
240	% --- Beyond binary: attribution, editing extent, benchmarks ---
241	
242	@inproceedings{bevendorff2025_two_paradigms,
243	  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},
244	  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},
245	  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
246	  pages     = {3762--3787},
247	  year      = {2025},
248	  address   = {Vienna, Austria},
249	}
250	
251	@inproceedings{uchendu2020_attribution,
252	  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
253	  title     = {{Authorship Attribution for Neural Text Generation}},
254	  booktitle = {Proceedings of EMNLP},
255	  year      = {2020},
256	}
257	
258	@inproceedings{editlens2026,
259	  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},
260	  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},
261	  booktitle = {Proceedings of ICLR},
262	  year      = {2026},
263	  note      = {arXiv:2510.03154},
264	  url       = {https://arxiv.org/abs/2510.03154},
265	}
266	
267	@inproceedings{loki2025,
268	  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},
269	  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},
270	  booktitle = {Proceedings of ICLR (Spotlight)},
271	  year      = {2025},
272	  note      = {arXiv:2410.09732},
273	  url       = {https://arxiv.org/abs/2410.09732},
274	}
275	
276	% --- Statistical / feature-based / shared-task detectors ---
277	
278	@inproceedings{verma2024_ghostbuster,
279	  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},
280	  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},
281	  booktitle = {Proceedings of NAACL},
282	  year      = {2024},
283	  note      = {arXiv:2305.15047},
284	  url       = {https://arxiv.org/abs/2305.15047},
285	}
286	
287	@inproceedings{wang2024_m4_semeval,
288	  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
289	  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
290	  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},
291	  year      = {2024},
292	  note      = {arXiv:2404.14183},
293	  url       = {https://arxiv.org/abs/2404.14183},
294	}
295	
296	@inproceedings{yang2024_dnagpt,
297	  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
298	  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
299	  booktitle = {Proceedings of ICLR},
300	  year      = {2024},
301	  note      = {arXiv:2305.17359},
302	  url       = {https://arxiv.org/abs/2305.17359},
303	}
304	
305	% --- Watermarking ---
306	
307	@inproceedings{kirchenbauer2023_watermark,
308	  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
309	  title     = {{A Watermark for Large Language Models}},
310	  booktitle = {Proceedings of ICML},
311	  year      = {2023},
312	  note      = {arXiv:2301.10226},
313	  url       = {https://arxiv.org/abs/2301.10226},
314	}
315	
316	% ============================================================
317	% Decoding Strategies
318	% ============================================================
319	
320	@inproceedings{holtzman2020_nucleus,
321	  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
322	  title     = {{The Curious Case of Neural Text Degeneration}},
323	  booktitle = {Proceedings of ICLR},
324	  year      = {2020},
325	  note      = {arXiv:1904.09751},
326	  url       = {https://arxiv.org/abs/1904.09751},
327	}
328	
329	@inproceedings{finlayson2024_closing,
330	  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},
331	  title     = {{Closing the Curious Case of Neural Text Degeneration}},
332	  booktitle = {Proceedings of ICLR},
333	  year      = {2024},
334	  note      = {arXiv:2310.01693},
335	  url       = {https://arxiv.org/abs/2310.01693},
336	}
337	
338	@inproceedings{garces_arias2025_decoding_decoded,
339	  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},
340	  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},
341	  booktitle = {Proceedings of COLING},
342	  year      = {2025},
343	  note      = {arXiv:2410.06097},
344	  url       = {https://arxiv.org/abs/2410.06097},
345	}
346	
347	@article{wiher2022_decoding,
348	  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},
349	  title     = {{On Decoding Strategies for Neural Text Generators}},
350	  journal   = {Transactions of the Association for Computational Linguistics},
351	  volume    = {10},
352	  pages     = {997--1012},
353	  year      = {2022},
354	}
355	
356	@inproceedings{basu2021_mirostat,
357	  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},
358	  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},
359	  booktitle = {Proceedings of ICLR},
360	  year      = {2021},
361	}
362	
363	% ============================================================
364	% Ordinal Classification / Contrastive Learning
365	% ============================================================
366	
367	@article{coral2020,
368	  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
369	  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
370	  journal   = {Pattern Recognition Letters},
371	  volume    = {140},
372	  pages     = {325--331},
373	  year      = {2020},
374	  note      = {arXiv:1901.07884},
375	  url       = {https://arxiv.org/abs/1901.07884},
376	}
377	
378	@inproceedings{cloc2025,
379	  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},
380	  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},
381	  booktitle = {Proceedings of CVPR},
382	  year      = {2025},
383	  note      = {arXiv:2504.17813},
384	  url       = {https://arxiv.org/abs/2504.17813},
385	}
386	
387	% ============================================================
388	% Foundation Models / Fine-tuning
389	% ============================================================
390	
391	@inproceedings{hu2022lora,
392	  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
393	  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},
394	  booktitle = {Proceedings of ICLR},
395	  year      = {2022},
396	  note      = {arXiv:2106.09685},
397	  url       = {https://arxiv.org/abs/2106.09685},
398	}
399	
400	@inproceedings{he2021_deberta_v3,
401	  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},
402	  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},
403	  booktitle = {Proceedings of ICLR},
404	  year      = {2023},
405	  note      = {arXiv:2111.09543},
406	  url       = {https://arxiv.org/abs/2111.09543},
407	}
408	
409	@article{liu2019_roberta,
410	  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},
411	  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},
412	  journal   = {arXiv preprint arXiv:1907.11692},
413	  year      = {2019},
414	  url       = {https://arxiv.org/abs/1907.11692},
415	}
416	
417	% ============================================================
418	% Data Curation / Selection
419	% ============================================================
420	
421	@inproceedings{dsir2023,
422	  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
423	  title     = {{Data Selection for Language Models via Importance Resampling}},
424	  booktitle = {Proceedings of NeurIPS},
425	  year      = {2023},
426	  note      = {arXiv:2302.03169},
427	  url       = {https://arxiv.org/abs/2302.03169},
428	}
429	
430	@inproceedings{qurating2024,
431	  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
432	  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},
433	  booktitle = {Proceedings of ICML},
434	  year      = {2024},
435	  note      = {arXiv:2402.09739},
436	  url       = {https://arxiv.org/abs/2402.09739},
437	}
438	
439	@article{sugiyama2007_importance_weighting,
440	  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\"u}ller, Klaus-Robert},
441	  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},
442	  journal   = {Journal of Machine Learning Research},
443	  volume    = {8},
444	  pages     = {985--1005},
445	  year      = {2007},
446	}
447	
448	% ============================================================
449	% Large Language Models (cross-scale experiments)
450	% ============================================================
451	
452	@misc{qwen2.5,
453	  author    = {Qwen Team},
454	  title     = {{Qwen2.5: A Party of Foundation Models}},
455	  year      = {2025},
456	  howpublished = {arXiv:2412.15115},
457	  url       = {https://arxiv.org/abs/2412.15115},
458	}
459	
460	@misc{llama3,
461	  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},
462	  title     = {{The Llama 3 Herd of Models}},
463	  year      = {2024},
464	  howpublished = {arXiv:2407.21783},
465	  url       = {https://arxiv.org/abs/2407.21783},
466	}
467	
468	% ============================================================
469	% Additional References (R5-R7 fixes)
470	% ============================================================
471	
472	@article{schaeffer2025,
473	  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},
474	  title     = {{Position: Model Collapse Does Not Mean What You Think}},
475	  journal   = {arXiv preprint arXiv:2503.03150},
476	  year      = {2025},
477	  url       = {https://arxiv.org/abs/2503.03150},
478	}
479	
480	@inproceedings{frank2001,
481	  author    = {Frank, Eibe and Hall, Mark},
482	  title     = {{A Simple Approach to Ordinal Classification}},
483	  booktitle = {Proceedings of ECML},
484	  year      = {2001},
485	  pages     = {145--156},
486	}
487	
488	@inproceedings{rennie2005,
489	  author    = {Rennie, Jason D. M. and Srebro, Nathan},
490	  title     = {{Loss Functions for Preference Levels: Regression with Discrete Ordered Labels}},
491	  booktitle = {Proceedings of IJCAI Workshop on Advances in Preference Handling},
492	  year      = {2005},
493	}
494	
495	@article{mccullagh1980_ordinal,
496	  title={Regression Models for Ordinal Data},
497	  author={McCullagh, Peter},
498	  journal={Journal of the Royal Statistical Society: Series B},
499	  volume={42},
500	  number={2},
501	  pages={109--142},
502	  year={1980}
503	}
504	
505	@inproceedings{wenzek2020_ccnet,
506	  title={{CCNet}: Extracting High Quality Monolingual Datasets from Web Crawl Data},
507	  author={Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
508	  booktitle={Proceedings of LREC},
509	  year={2020}
510	}
511	
512	@inproceedings{dugan2024_raid,
513	  author    = {Dugan, Liam and Hwang, Alyssa and Trhl{\'\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},
514	  title     = {{RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors}},
515	  booktitle = {Proceedings of ACL},
516	  pages     = {12463--12492},
517	  year      = {2024},
518	  note      = {arXiv:2405.07940},
519	  url       = {https://arxiv.org/abs/2405.07940},
520	}
521	
522	% ============================================================
523	% Reviewer-requested citations (MR1--MR5)
524	% ============================================================
525	
526	@inproceedings{guo2024curious,
527	  author    = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo{\'e}},
528	  title     = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
529	  booktitle = {Findings of NAACL},
530	  year      = {2024},
531	  note      = {arXiv:2311.09807},
532	  url       = {https://arxiv.org/abs/2311.09807},
533	}
534	
535	@inproceedings{padmakumar2024diversity,
536	  author    = {Padmakumar, Vishakh and He, He},
537	  title     = {{Does Writing with Language Models Reduce Content Diversity?}},
538	  booktitle = {Proceedings of ICLR},
539	  year      = {2024},
540	  note      = {arXiv:2309.05196},
541	  url       = {https://arxiv.org/abs/2309.05196},
542	}
543	
544	@misc{briesch2024selfconsuming,
545	  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},
546	  title     = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},
547	  year      = {2024},
548	  howpublished = {arXiv:2311.16822},
549	  url       = {https://arxiv.org/abs/2311.16822},
550	}
551	
552	@misc{seddik2024synthetic,
553	  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},
554	  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},
555	  year      = {2024},
556	  howpublished = {arXiv:2404.05090},
557	  url       = {https://arxiv.org/abs/2404.05090},
558	}
559	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "cd510cf6-d239-44c5-871a-d607da83d72e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
      "content": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2025},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n@inproceedings{shi2025_closer_look,\n  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{yi2026_escaping_collapse,\n  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},\n  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},\n  booktitle = {3rd DATA-FM Workshop at ICLR 2026},\n  year      = {2026},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n@article{wu2025_detection_survey,\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  journal   = {Computational Linguistics},\n  volume    = {51},\n  number    = {1},\n  pages     = {275--354},\n  year      = {2025},\n  publisher = {MIT Press},\n}\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{bevendorff2025_two_paradigms,\n  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},\n  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  pages     = {3762--3787},\n  year      = {2025},\n  address   = {Vienna, Austria},\n}\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@article{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  journal   = {arXiv preprint arXiv:1907.11692},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n\n% ============================================================\n% Large Language Models (cross-scale experiments)\n% ============================================================\n\n@misc{qwen2.5,\n  author    = {Qwen Team},\n  title     = {{Qwen2.5: A Party of Foundation Models}},\n  year      = {2025},\n  howpublished = {arXiv:2412.15115},\n  url       = {https://arxiv.org/abs/2412.15115},\n}\n\n@misc{llama3,\n  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},\n  title     = {{The Llama 3 Herd of Models}},\n  year      = {2024},\n  howpublished = {arXiv:2407.21783},\n  url       = {https://arxiv.org/abs/2407.21783},\n}\n\n% ============================================================\n% Additional References (R5-R7 fixes)\n% ============================================================\n\n@article{schaeffer2025,\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  title     = {{Position: Model Collapse Does Not Mean What You Think}},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n@inproceedings{frank2001,\n  author    = {Frank, Eibe and Hall, Mark},\n  title     = {{A Simple Approach to Ordinal Classification}},\n  booktitle = {Proceedings of ECML},\n  year      = {2001},\n  pages     = {145--156},\n}\n\n@inproceedings{rennie2005,\n  author    = {Rennie, Jason D. M. and Srebro, Nathan},\n  title     = {{Loss Functions for Preference Levels: Regression with Discrete Ordered Labels}},\n  booktitle = {Proceedings of IJCAI Workshop on Advances in Preference Handling},\n  year      = {2005},\n}\n\n@article{mccullagh1980_ordinal,\n  title={Regression Models for Ordinal Data},\n  author={McCullagh, Peter},\n  journal={Journal of the Royal Statistical Society: Series B},\n  volume={42},\n  number={2},\n  pages={109--142},\n  year={1980}\n}\n\n@inproceedings{wenzek2020_ccnet,\n  title={{CCNet}: Extracting High Quality Monolingual Datasets from Web Crawl Data},\n  author={Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle={Proceedings of LREC},\n  year={2020}\n}\n\n@inproceedings{dugan2024_raid,\n  author    = {Dugan, Liam and Hwang, Alyssa and Trhl{\\'\\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},\n  title     = {{RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors}},\n  booktitle = {Proceedings of ACL},\n  pages     = {12463--12492},\n  year      = {2024},\n  note      = {arXiv:2405.07940},\n  url       = {https://arxiv.org/abs/2405.07940},\n}\n\n% ============================================================\n% Reviewer-requested citations (MR1--MR5)\n% ============================================================\n\n@inproceedings{guo2024curious,\n  author    = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo{\\'e}},\n  title     = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  booktitle = {Findings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2311.09807},\n  url       = {https://arxiv.org/abs/2311.09807},\n}\n\n@inproceedings{padmakumar2024diversity,\n  author    = {Padmakumar, Vishakh and He, He},\n  title     = {{Does Writing with Language Models Reduce Content Diversity?}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2309.05196},\n  url       = {https://arxiv.org/abs/2309.05196},\n}\n\n@misc{briesch2024selfconsuming,\n  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  title     = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},\n  year      = {2024},\n  howpublished = {arXiv:2311.16822},\n  url       = {https://arxiv.org/abs/2311.16822},\n}\n\n@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n",
      "numLines": 559,
      "startLine": 1,
      "totalLines": 559
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_015zduWAEPoDubKGWD7Mrspx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "212af11e-83c0-4620-a829-fc7f0f6f147e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JM9HHtdddeCz6vsUwqWR7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9935,
      "cache_read_input_tokens": 26167,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9935
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

_source line 24 · 2026-05-17T17:05:20.869Z_

<details><summary>↩ Tool result · `toolu_015zduWAEPoDubKGWD7Mrspx`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Model Collapse Theory.}
5	\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \cite{seddik2024synthetic}, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
6	Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
7	\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.
8	Dohmatob et al.\ predict that recursive training erodes distributional tails as a theoretical scaling law \citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
9	All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.
10	
11	\paragraph{AI Text Detection.}
12	The detection literature \cite{wu2025_detection_survey} spans statistical methods (DetectGPT \cite{mitchell2023_detectgpt}, Fast-DetectGPT \cite{fast_detectgpt2024}, Binoculars \cite{binoculars2024}, DivEye \cite{diveye2026}, GLTR \cite{gehrmann2019_gltr}, Ghostbuster \cite{verma2024_ghostbuster}, DNA-GPT \cite{yang2024_dnagpt}) and watermarking \cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \cite{sadasivan2023_paraphrase}, distribution shift \cite{pudasaini2026_detection_fails}, and generator barriers \cite{pu2026_generator_barrier}.
13	M4-SemEval \cite{wang2024_m4_semeval} and RAID \cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.
14	All these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.
15	
16	\paragraph{Adjacent Tasks.}
17	EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2020_attribution} classify \emph{which} model generated text; LOKI \cite{loki2025} benchmarks synthetic data detection across modalities.
18	\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, characterizing \emph{how} text degrades without classifying which iteration a passage comes from.
19	Our task performs the inverse, ordinal depth estimation from text alone, discriminating between adjacent depths rather than merely detecting aggregate degradation.
20	
21	\paragraph{Ordinal Classification.}
22	Ordinal classification has a long history \cite{mccullagh1980_ordinal}: \citet{frank2001} reduce ordinal problems to nested binary tasks, and \citet{rennie2005} introduce loss functions tailored to discrete ordered labels.
23	CORAL \cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.
24	We adopt both as baselines (\S\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.
25	
26	\paragraph{Decoding Strategy Effects.}
27	Decoding strategies shape text statistics in ways that interact with depth signals \cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.
28	Our Depth Degradation Atlas (\S\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation: temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal, effects beyond single-pass text quality.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "b2b385dd-ce3f-4022-af08-7adcb3403514",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Model Collapse Theory.}\n\\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \\cite{seddik2024synthetic}, \\citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \\cite{alemohammad2024_mad} extends the analysis to self-consuming models.\nSubsequent work addresses mitigation \\cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, convergence \\cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \\cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.\n\\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.\nDohmatob et al.\\ predict that recursive training erodes distributional tails as a theoretical scaling law \\citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.\nAll assume depth is known a priori; we address the inverse problem of estimating depth from text alone.\n\n\\paragraph{AI Text Detection.}\nThe detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}) and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval} and RAID \\cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.\nAll these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.\n\n\\paragraph{Adjacent Tasks.}\nEditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains; \\citet{uchendu2020_attribution} classify \\emph{which} model generated text; LOKI \\cite{loki2025} benchmarks synthetic data detection across modalities.\n\\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, characterizing \\emph{how} text degrades without classifying which iteration a passage comes from.\nOur task performs the inverse, ordinal depth estimation from text alone, discriminating between adjacent depths rather than merely detecting aggregate degradation.\n\n\\paragraph{Ordinal Classification.}\nOrdinal classification has a long history \\cite{mccullagh1980_ordinal}: \\citet{frank2001} reduce ordinal problems to nested binary tasks, and \\citet{rennie2005} introduce loss functions tailored to discrete ordered labels.\nCORAL \\cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \\cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.\nWe adopt both as baselines (\\S\\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.\n\n\\paragraph{Decoding Strategy Effects.}\nDecoding strategies shape text statistics in ways that interact with depth signals \\cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.\nOur Depth Degradation Atlas (\\S\\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation: temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal, effects beyond single-pass text quality.",
      "numLines": 28,
      "startLine": 1,
      "totalLines": 28
    }
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Let me count the current citations in the bib file. I'll enumerate them:

1. shumailov2024_nature
2. dohmatob2024_tale_of_tails
3. dohmatob2025_strong_collapse
4. dohmatob2024_demystified
5. alemohammad2024_mad
6. gerstgrasser2024_accumulate
7. marchi2024_heat_death
8. knowledge_collapse2025
9. sigma2026_spectral


10. mohamed2025_broken_telephone
11. synthetic_eggs2026
12. shi2025_closer_look
13. yi2026_escaping_collapse
14. drayson2025_detection_prevents_collapse
15. bakshi2026_collapse_improvement
16. wang2026_contamination
17. falahati2026_curated
18. wu2025_detection_survey
19. gehrmann2019_gltr
20. mitchell2023_detectgpt
21. fast_detectgpt2024
22. binoculars2024
23. diveye2026
24. sadasivan2023_paraphrase
25. pudasaini2026_detection_fails
26. pu2026_generator_barrier
27. bevendorff2025_two

Continuing through more detection and decoding paradigms...

now I'm seeing the bibliography extends to 59 entries total. Let me verify how many of these are actually cited in the paper itself—the task mentions needing at least 30+ citations for EMNLP submission, so I should check which references are genuinely used versus just listed in the bib file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "f4f29b4b-7354-4fff-a5ab-55d6d663887f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjrRcPuRW2DHGZziVRzZKt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11290,
      "cache_read_input_tokens": 36102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11290
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

_source line 26_

The bib file has 59 entries. Let me check how many are actually cited in the paper text.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "98ce04cb-055d-4a2b-8ec7-762a0a31721d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjrRcPuRW2DHGZziVRzZKt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11290,
      "cache_read_input_tokens": 36102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11290
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

_source line 27_

<details open><summary>🔧 Tool call — Grep · `toolu_017pm6RFT1pC5zgWwyHUzy3s`</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "cd9caa86-adf3-4e0b-9c29-fd610c6ade52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JjrRcPuRW2DHGZziVRzZKt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11290,
      "cache_read_input_tokens": 36102,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11290
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

_source line 28 · 2026-05-17T17:05:40.950Z_

<details><summary>↩ Tool result · `toolu_017pm6RFT1pC5zgWwyHUzy3s`</summary>

```text
docs/paper/related_work.tex:5:\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \cite{seddik2024synthetic}, \citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \cite{alemohammad2024_mad} extends the analysis to self-consuming models.
docs/paper/related_work.tex:6:Subsequent work addresses mitigation \cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \cite{bakshi2026_collapse_improvement}, convergence \cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.
docs/paper/related_work.tex:7:\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.
docs/paper/related_work.tex:8:Dohmatob et al.\ predict that recursive training erodes distributional tails as a theoretical scaling law \citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.
docs/paper/related_work.tex:12:[Omitted long matching line]
docs/paper/related_work.tex:13:M4-SemEval \cite{wang2024_m4_semeval} and RAID \cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.
docs/paper/related_work.tex:17:EditLens \cite{editlens2026} estimates editing extent but does not model recursive chains; \citet{uchendu2020_attribution} classify \emph{which} model generated text; LOKI \cite{loki2025} benchmarks synthetic data detection across modalities.
docs/paper/related_work.tex:18:\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, characterizing \emph{how} text degrades without classifying which iteration a passage comes from.
docs/paper/related_work.tex:22:Ordinal classification has a long history \cite{mccullagh1980_ordinal}: \citet{frank2001} reduce ordinal problems to nested binary tasks, and \citet{rennie2005} introduce loss functions tailored to discrete ordered labels.
docs/paper/related_work.tex:23:CORAL \cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.
docs/paper/related_work.tex:27:Decoding strategies shape text statistics in ways that interact with depth signals \cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.
docs/paper/atlas.tex:62:This transition aligns with model-collapse dynamics~\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).
docs/paper/atlas.tex:164:Temperature ($\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.9\%, OLMo 82.1\%) because uniform logit scaling accelerates convergence to an attractor distribution~\cite{shumailov2024_nature}, amplifying the statistical fingerprint. However, this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\S\ref{sec:generalization}).
docs/paper/conclusion.tex:29:Adversarial paraphrasing \cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.
docs/paper/conclusion.tex:33:However, \citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).
docs/paper/conclusion.tex:54:Detection features degrade under domain shift \cite{pudasaini2026_detection_fails}, and curated synthetic data may not trigger collapse \cite{falahati2026_curated}, attenuating the fingerprints we exploit.
docs/paper/discussion.tex:5:These features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\% (\S\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.
docs/paper/discussion.tex:7:Depth-graduated curation complements binary detection~\cite{dsir2023,qurating2024} and watermarking~\cite{kirchenbauer2023_watermark} as a provenance signal~\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\ref{app:curation_poc}) and adversarial robustness remains untested.
docs/paper/method.tex:24:Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \cite{holtzman2020_nucleus}, temperature sampling ($\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).
docs/paper/method.tex:33:[Omitted long matching line]
docs/paper/method.tex:104:We compare against CORAL ordinal regression \cite{coral2020}, DivEye \cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \S\ref{sec:generalization}.
docs/paper/generalization.tex:10:On Pythia nucleus, CORAL ordinal regression \cite{coral2020} (78.1\%) and DivEye \cite{diveye2026} (78.2\%) match the within-cell RF of Table~\ref{tab:main_matrix} within 0.6\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\%, $p<0.001$) and logistic regression (75.0\%).
docs/paper/generalization.tex:100:To test whether depth signal persists at larger scale, we extend the benchmark to Qwen2.5-7B-Instruct~\cite{qwen2.5} and Llama-3.1-8B-Instruct~\cite{llama3} under 4-bit NF4 QLoRA (nucleus $p{=}0.95$, 500 samples/depth, depths 0--5).
docs/paper/section_appendix.tex:161:DeBERTa-v3-base \cite{he2021_deberta_v3} and RoBERTa-base \cite{liu2019_roberta} finetuned end-to-end achieve 58.3\% ($\pm$4.7\%) and 59.5\% ($\pm$3.2\%) respectively, lagging the RF baseline (78.7\%) by 20.4pp and 19.2pp.
docs/paper/section_appendix.tex:187:DCOL \cite{cloc2025} reached 64.5\% (\S\ref{app:dcol_iterations}); all end-to-end approaches (58--65\%) underperform feature-based methods, suggesting depth estimation benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.
docs/paper/section_appendix.tex:495:Current data curation operates on a binary human-vs-machine distinction \cite{dsir2023,qurating2024}.
docs/paper/section_appendix.tex:498:Importance weighting \cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.
docs/paper/section_appendix.tex:502:Watermarking \cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.
docs/paper/section_appendix.tex:503:Source attribution \cite{uchendu2020_attribution} identifies the generating model but not the generation history.
docs/paper/introduction.tex:5:As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \cite{shumailov2024_nature,alemohammad2024_mad}.
docs/paper/introduction.tex:6:This model$\to$data$\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \cite{dohmatob2024_tale_of_tails}.
docs/paper/introduction.tex:9:Binary detectors such as Binoculars \cite{binoculars2024}, Fast-DetectGPT \cite{fast_detectgpt2024}, and DivEye \cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \geq 1$ into a single category.
docs/paper/introduction.tex:10:Watermarking \cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.
docs/paper/introduction.tex:11:The model collapse literature \cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "d2b5044a-b663-4c4a-a35d-f9b7d65ee9e9",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/related_work.tex:5:\\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \\cite{seddik2024synthetic}, \\citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \\cite{alemohammad2024_mad} extends the analysis to self-consuming models.\ndocs/paper/related_work.tex:6:Subsequent work addresses mitigation \\cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, convergence \\cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \\cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.\ndocs/paper/related_work.tex:7:\\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.\ndocs/paper/related_work.tex:8:Dohmatob et al.\\ predict that recursive training erodes distributional tails as a theoretical scaling law \\citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.\ndocs/paper/related_work.tex:12:[Omitted long matching line]\ndocs/paper/related_work.tex:13:M4-SemEval \\cite{wang2024_m4_semeval} and RAID \\cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.\ndocs/paper/related_work.tex:17:EditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains; \\citet{uchendu2020_attribution} classify \\emph{which} model generated text; LOKI \\cite{loki2025} benchmarks synthetic data detection across modalities.\ndocs/paper/related_work.tex:18:\\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, characterizing \\emph{how} text degrades without classifying which iteration a passage comes from.\ndocs/paper/related_work.tex:22:Ordinal classification has a long history \\cite{mccullagh1980_ordinal}: \\citet{frank2001} reduce ordinal problems to nested binary tasks, and \\citet{rennie2005} introduce loss functions tailored to discrete ordered labels.\ndocs/paper/related_work.tex:23:CORAL \\cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \\cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.\ndocs/paper/related_work.tex:27:Decoding strategies shape text statistics in ways that interact with depth signals \\cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.\ndocs/paper/atlas.tex:62:This transition aligns with model-collapse dynamics~\\cite{shumailov2024_nature}: early recursion narrows the surprisal distribution (captured by its variance), while later steps erode the perplexity tail (captured by upper quantiles and kurtosis).\ndocs/paper/atlas.tex:164:Temperature ($\\tau{=}0.9$) yields the highest accuracy in 2/3 models (GPT-2~XL 85.9\\%, OLMo 82.1\\%) because uniform logit scaling accelerates convergence to an attractor distribution~\\cite{shumailov2024_nature}, amplifying the statistical fingerprint. However, this acceleration creates a boundary reversal risk: temperature depth-$N$ features approximate nucleus/top-$k$ depth-$(N{+}1)$ features, causing cross-strategy classifiers to systematically overpredict depth (\\S\\ref{sec:generalization}).\ndocs/paper/conclusion.tex:29:Adversarial paraphrasing \\cite{sadasivan2023_paraphrase} could disrupt the perplexity tail features that drive classification; depth estimation's robustness under such attacks is untested.\ndocs/paper/conclusion.tex:33:However, \\citet{bakshi2026_collapse_improvement} show that early recursion can temporarily \\emph{improve} model quality, which could produce non-monotonic AUC profiles (e.g., a dip at d1/d2 followed by recovery at d2/d3).\ndocs/paper/conclusion.tex:54:Detection features degrade under domain shift \\cite{pudasaini2026_detection_fails}, and curated synthetic data may not trigger collapse \\cite{falahati2026_curated}, attenuating the fingerprints we exploit.\ndocs/paper/discussion.tex:5:These features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\\% (\\S\\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.\ndocs/paper/discussion.tex:7:Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024} and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.\ndocs/paper/method.tex:24:Each model is paired with three decoding strategies: nucleus sampling ($p{=}0.95$) \\cite{holtzman2020_nucleus}, temperature sampling ($\\tau{=}0.9$), and top-$k$ sampling ($k{=}50$).\ndocs/paper/method.tex:33:[Omitted long matching line]\ndocs/paper/method.tex:104:We compare against CORAL ordinal regression \\cite{coral2020}, DivEye \\cite{diveye2026}, a 2-layer cross-entropy MLP, logistic regression, and a single-feature baseline using mean perplexity alone; results appear in \\S\\ref{sec:generalization}.\ndocs/paper/generalization.tex:10:On Pythia nucleus, CORAL ordinal regression \\cite{coral2020} (78.1\\%) and DivEye \\cite{diveye2026} (78.2\\%) match the within-cell RF of Table~\\ref{tab:main_matrix} within 0.6\\,pp (bootstrap $p>0.05$, Bonferroni-corrected); all feature-based methods significantly outperform CE-MLP (74.9\\%, $p<0.001$) and logistic regression (75.0\\%).\ndocs/paper/generalization.tex:100:To test whether depth signal persists at larger scale, we extend the benchmark to Qwen2.5-7B-Instruct~\\cite{qwen2.5} and Llama-3.1-8B-Instruct~\\cite{llama3} under 4-bit NF4 QLoRA (nucleus $p{=}0.95$, 500 samples/depth, depths 0--5).\ndocs/paper/section_appendix.tex:161:DeBERTa-v3-base \\cite{he2021_deberta_v3} and RoBERTa-base \\cite{liu2019_roberta} finetuned end-to-end achieve 58.3\\% ($\\pm$4.7\\%) and 59.5\\% ($\\pm$3.2\\%) respectively, lagging the RF baseline (78.7\\%) by 20.4pp and 19.2pp.\ndocs/paper/section_appendix.tex:187:DCOL \\cite{cloc2025} reached 64.5\\% (\\S\\ref{app:dcol_iterations}); all end-to-end approaches (58--65\\%) underperform feature-based methods, suggesting depth estimation benefits from targeted statistical features that capture distributional tail properties absent from PLM representations.\ndocs/paper/section_appendix.tex:495:Current data curation operates on a binary human-vs-machine distinction \\cite{dsir2023,qurating2024}.\ndocs/paper/section_appendix.tex:498:Importance weighting \\cite{sugiyama2007_importance_weighting} could further enable continuous depth-aware data selection rather than discrete thresholding.\ndocs/paper/section_appendix.tex:502:Watermarking \\cite{kirchenbauer2023_watermark} provides high-confidence attribution when the generator cooperates but is inapplicable to unwatermarked text.\ndocs/paper/section_appendix.tex:503:Source attribution \\cite{uchendu2020_attribution} identifies the generating model but not the generation history.\ndocs/paper/introduction.tex:5:As synthetic content proliferates across the web, a recursive loop emerges: models trained on web corpora ingest text generated by earlier models, and their outputs feed into the next generation's training data \\cite{shumailov2024_nature,alemohammad2024_mad}.\ndocs/paper/introduction.tex:6:This model$\\to$data$\\to$model cycle is no longer hypothetical; it is already occurring in the wild. Yet we lack the ability to determine how many recursive iterations a given text has undergone, a distinction that matters because first-generation synthetic text may be benign or even beneficial for training, while deeply recursive text drives the distributional collapse that degrades model quality \\cite{dohmatob2024_tale_of_tails}.\ndocs/paper/introduction.tex:9:Binary detectors such as Binoculars \\cite{binoculars2024}, Fast-DetectGPT \\cite{fast_detectgpt2024}, and DivEye \\cite{diveye2026} classify text as human-written or machine-generated, collapsing all depths $d \\geq 1$ into a single category.\ndocs/paper/introduction.tex:10:Watermarking \\cite{kirchenbauer2023_watermark} requires proactive embedding and cannot be applied retroactively.\ndocs/paper/introduction.tex:11:The model collapse literature \\cite{shumailov2024_nature,dohmatob2024_tale_of_tails} assumes depth is known a priori; \\citet{drayson2025_detection_prevents_collapse} filter synthetic data via binary detection without distinguishing depths.",
    "numLines": 34
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the rest of the citations in other files, particularly introduction.tex which might have more.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "e78f6f7c-d1c6-4fc0-9734-5bdd107f80c7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQKkaDVZsKoLKm14SeREDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 47392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3628
      },
      "output_tokens": 10,
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

Let me get the full list of cited keys to compare against the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "3a5162d6-0de5-4df5-b02d-f9e4469cca33",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQKkaDVZsKoLKm14SeREDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 47392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3628
      },
      "output_tokens": 10,
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

<details open><summary>🔧 Tool call — Bash · `toolu_01H3Q2ifbBc8DZk1gYR5sWZW`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper && grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract all unique citation keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "d189d452-011b-4c2a-90f7-7411cedb36a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PQKkaDVZsKoLKm14SeREDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3628,
      "cache_read_input_tokens": 47392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3628
      },
      "output_tokens": 10,
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

_source line 32 · 2026-05-17T17:05:47.745Z_

<details><summary>↩ Tool result · `toolu_01H3Q2ifbBc8DZk1gYR5sWZW`</summary>

```text
alemohammad2024_mad
bakshi2026_collapse_improvement
basu2021_mirostat
bevendorff2025_two_paradigms
binoculars2024
briesch2024selfconsuming
cloc2025
coral2020
diveye2026
dohmatob2024_demystified
dohmatob2024_tale_of_tails
dohmatob2025_strong_collapse
drayson2025_detection_prevents_collapse
dsir2023
dugan2024_raid
editlens2026
falahati2026_curated
fast_detectgpt2024
finlayson2024_closing
frank2001
garces_arias2025_decoding_decoded
gehrmann2019_gltr
gerstgrasser2024_accumulate
guo2024curious
he2021_deberta_v3
holtzman2020_nucleus
hu2022lora
kirchenbauer2023_watermark
knowledge_collapse2025
liu2019_roberta
llama3
loki2025
marchi2024_heat_death
mccullagh1980_ordinal
mitchell2023_detectgpt
mohamed2025_broken_telephone
padmakumar2024diversity
pu2026_generator_barrier
pudasaini2026_detection_fails
qurating2024
qwen2.5
rennie2005
sadasivan2023_paraphrase
schaeffer2025
seddik2024synthetic
shi2025_closer_look
shumailov2024_nature
sigma2026_spectral
sugiyama2007_importance_weighting
synthetic_eggs2026
uchendu2020_attribution
verma2024_ghostbuster
wang2024_m4_semeval
wang2026_contamination
wenzek2020_ccnet
wiher2022_decoding
wu2025_detection_survey
yang2024_dnagpt
yi2026_escaping_collapse
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "17e70485-bd82-4de2-83d8-1eff8e0dc67e",
  "tool_use_result": {
    "stdout": "alemohammad2024_mad\nbakshi2026_collapse_improvement\nbasu2021_mirostat\nbevendorff2025_two_paradigms\nbinoculars2024\nbriesch2024selfconsuming\ncloc2025\ncoral2020\ndiveye2026\ndohmatob2024_demystified\ndohmatob2024_tale_of_tails\ndohmatob2025_strong_collapse\ndrayson2025_detection_prevents_collapse\ndsir2023\ndugan2024_raid\neditlens2026\nfalahati2026_curated\nfast_detectgpt2024\nfinlayson2024_closing\nfrank2001\ngarces_arias2025_decoding_decoded\ngehrmann2019_gltr\ngerstgrasser2024_accumulate\nguo2024curious\nhe2021_deberta_v3\nholtzman2020_nucleus\nhu2022lora\nkirchenbauer2023_watermark\nknowledge_collapse2025\nliu2019_roberta\nllama3\nloki2025\nmarchi2024_heat_death\nmccullagh1980_ordinal\nmitchell2023_detectgpt\nmohamed2025_broken_telephone\npadmakumar2024diversity\npu2026_generator_barrier\npudasaini2026_detection_fails\nqurating2024\nqwen2.5\nrennie2005\nsadasivan2023_paraphrase\nschaeffer2025\nseddik2024synthetic\nshi2025_closer_look\nshumailov2024_nature\nsigma2026_spectral\nsugiyama2007_importance_weighting\nsynthetic_eggs2026\nuchendu2020_attribution\nverma2024_ghostbuster\nwang2024_m4_semeval\nwang2026_contamination\nwenzek2020_ccnet\nwiher2022_decoding\nwu2025_detection_survey\nyang2024_dnagpt\nyi2026_escaping_collapse",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Let me count: 59 unique citation keys. That's already well above 30. But let me check the bib entries and see which from the literature_map are missing. Let me also count the bib entries.

Let me count:
1. alemohammad2024_mad
2. bakshi2026_collapse_improvement
3. basu2021_mirostat
4. bevendorff2025_two_paradigms
5. binoculars2024
6. briesch2024selfconsuming


7. cloc2025
8. coral2020
9. diveye2026
10. dohmatob2024_demystified
11. dohmatob2024_tale_of_tails
12. dohmatob2025_strong_collapse
13. drayson2025_detection_prevents_collapse
14. dsir2023
15. dugan2024_raid
16. editlens2026
17. falahati2026_curated
18. fast_detectgpt2024
19. finlayson2024_closing
20. frank2001
21. garces_arias2025_decoding_decoded
22. gehrmann2019_gltr
23. gerstgrasser2024_accumulate
24. guo2

Continuing through the bibliography entries... I've got 59 citations total, which is well above the 30 minimum. Now I'm cross-referencing the literature map to see which entries are defined but haven't been cited in the paper yet—looks like there are several candidates including some recent work on model collapse and tail behavior that might not have made it into the bibliography. Continuing through the detection literature, I'm verifying each paper against the bibliography and noting a couple of gaps—tulchinskii2024 and li2024 appear in the literature map but are missing from the actual citations, so I'll need to track those down. Looking at the task requirements in Chinese, it's asking to expand the Related Work section with citations and update the .bib file since EMNLP submissions need at least 30+ references. The paper already has 59 citations, so the quantity requirement is met, but I should verify coverage across the key research areas mentioned — model collapse, text detection, data quality, LLM training methods, ordinal regression, statistical features, recursive generation, and benchmarks are all represented, though I should check if there are any notable gaps in the evaluation category. I'm continuing through the bibliography and counting more entries — looks like I'm up to at least 36 sources now, which is getting closer to what's needed for adequate coverage of the synthetic data collapse and detection literature. I'm seeing that I've compiled 59 citations so far, which exceeds the 30-entry requirement. Now I need to identify the three entries from the literature map that aren't yet in the bibliography and integrate them. Looking at the category gaps, I notice that data quality and curation is missing the FineWeb paper from the literature map, so I'll add that along with the other missing entries and ensure all categories are properly represented in the Related Work section. The citation requirement is already satisfied with 59 references, so I just need to add those three missing entries from the literature map and weave them into the related work section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "cd8dcc1f-af5f-4cfb-a4bb-d81bba4b5371",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y24JUphzB8apf7cxDLYigF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 51020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 726
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

_source line 34_

The paper already has **59 unique citations** across all tex files, well above the 30+ target. However, 3 entries from `literature_map.yaml` are missing from the bib and citations:
1. `tulchinskii2024_intrinsic_dim` — intrinsic dimension detection (NeurIPS 2023)
2. `li2024_mage` — MAGE benchmark (ACL 2024)
3. `penedo2024_fineweb` — FineWeb data curation (NeurIPS 2024)

I'll add these 3 missing entries to the bib and integrate them into the related work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "b8ddcc49-0bff-45b0-915d-db1f27efcb52",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y24JUphzB8apf7cxDLYigF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 51020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 726
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

<details open><summary>🔧 Tool call — Edit · `toolu_013NNYK43Gec2QYKzK21Wcga`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "old_string": "% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,",
  "new_string": "% --- Geometric / intrinsic dimension detectors ---\n\n@inproceedings{tulchinskii2024_intrinsic_dim,\n  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},\n  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2306.04723},\n  url       = {https://arxiv.org/abs/2306.04723},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "5f4b2e1e-a9b1-4177-9970-ca36201e6144",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y24JUphzB8apf7cxDLYigF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 726,
      "cache_read_input_tokens": 51020,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 726
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

_source line 36 · 2026-05-17T17:06:38.341Z_

<details><summary>↩ Tool result · `toolu_013NNYK43Gec2QYKzK21Wcga`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "2871ded6-e463-44e0-b999-c1675f876f27",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "oldString": "% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,",
    "newString": "% --- Geometric / intrinsic dimension detectors ---\n\n@inproceedings{tulchinskii2024_intrinsic_dim,\n  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},\n  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2306.04723},\n  url       = {https://arxiv.org/abs/2306.04723},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,",
    "originalFile": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2025},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n@inproceedings{shi2025_closer_look,\n  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{yi2026_escaping_collapse,\n  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},\n  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},\n  booktitle = {3rd DATA-FM Workshop at ICLR 2026},\n  year      = {2026},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n@article{wu2025_detection_survey,\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  journal   = {Computational Linguistics},\n  volume    = {51},\n  number    = {1},\n  pages     = {275--354},\n  year      = {2025},\n  publisher = {MIT Press},\n}\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{bevendorff2025_two_paradigms,\n  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},\n  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  pages     = {3762--3787},\n  year      = {2025},\n  address   = {Vienna, Austria},\n}\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@article{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  journal   = {arXiv preprint arXiv:1907.11692},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n\n% ============================================================\n% Large Language Models (cross-scale experiments)\n% ============================================================\n\n@misc{qwen2.5,\n  author    = {Qwen Team},\n  title     = {{Qwen2.5: A Party of Foundation Models}},\n  year      = {2025},\n  howpublished = {arXiv:2412.15115},\n  url       = {https://arxiv.org/abs/2412.15115},\n}\n\n@misc{llama3,\n  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},\n  title     = {{The Llama 3 Herd of Models}},\n  year      = {2024},\n  howpublished = {arXiv:2407.21783},\n  url       = {https://arxiv.org/abs/2407.21783},\n}\n\n% ============================================================\n% Additional References (R5-R7 fixes)\n% ============================================================\n\n@article{schaeffer2025,\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  title     = {{Position: Model Collapse Does Not Mean What You Think}},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n@inproceedings{frank2001,\n  author    = {Frank, Eibe and Hall, Mark},\n  title     = {{A Simple Approach to Ordinal Classification}},\n  booktitle = {Proceedings of ECML},\n  year      = {2001},\n  pages     = {145--156},\n}\n\n@inproceedings{rennie2005,\n  author    = {Rennie, Jason D. M. and Srebro, Nathan},\n  title     = {{Loss Functions for Preference Levels: Regression with Discrete Ordered Labels}},\n  booktitle = {Proceedings of IJCAI Workshop on Advances in Preference Handling},\n  year      = {2005},\n}\n\n@article{mccullagh1980_ordinal,\n  title={Regression Models for Ordinal Data},\n  author={McCullagh, Peter},\n  journal={Journal of the Royal Statistical Society: Series B},\n  volume={42},\n  number={2},\n  pages={109--142},\n  year={1980}\n}\n\n@inproceedings{wenzek2020_ccnet,\n  title={{CCNet}: Extracting High Quality Monolingual Datasets from Web Crawl Data},\n  author={Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle={Proceedings of LREC},\n  year={2020}\n}\n\n@inproceedings{dugan2024_raid,\n  author    = {Dugan, Liam and Hwang, Alyssa and Trhl{\\'\\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},\n  title     = {{RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors}},\n  booktitle = {Proceedings of ACL},\n  pages     = {12463--12492},\n  year      = {2024},\n  note      = {arXiv:2405.07940},\n  url       = {https://arxiv.org/abs/2405.07940},\n}\n\n% ============================================================\n% Reviewer-requested citations (MR1--MR5)\n% ============================================================\n\n@inproceedings{guo2024curious,\n  author    = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo{\\'e}},\n  title     = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  booktitle = {Findings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2311.09807},\n  url       = {https://arxiv.org/abs/2311.09807},\n}\n\n@inproceedings{padmakumar2024diversity,\n  author    = {Padmakumar, Vishakh and He, He},\n  title     = {{Does Writing with Language Models Reduce Content Diversity?}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2309.05196},\n  url       = {https://arxiv.org/abs/2309.05196},\n}\n\n@misc{briesch2024selfconsuming,\n  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  title     = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},\n  year      = {2024},\n  howpublished = {arXiv:2311.16822},\n  url       = {https://arxiv.org/abs/2311.16822},\n}\n\n@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 273,
        "oldLines": 6,
        "newStart": 273,
        "newLines": 17,
        "lines": [
          "   url       = {https://arxiv.org/abs/2410.09732},",
          " }",
          " ",
          "+% --- Geometric / intrinsic dimension detectors ---",
          "+",
          "+@inproceedings{tulchinskii2024_intrinsic_dim,",
          "+  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},",
          "+  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},",
          "+  booktitle = {Proceedings of NeurIPS},",
          "+  year      = {2023},",
          "+  note      = {arXiv:2306.04723},",
          "+  url       = {https://arxiv.org/abs/2306.04723},",
          "+}",
          "+",
          " % --- Statistical / feature-based / shared-task detectors ---",
          " ",
          " @inproceedings{verma2024_ghostbuster,"
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01414pWtzc3g7r2ckDhBJitB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "old_string": "@inproceedings{yang2024_dnagpt,",
  "new_string": "@inproceedings{li2024_mage,\n  author    = {Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min},\n  title     = {{MAGE: Machine-generated Text Detection in the Wild}},\n  booktitle = {Proceedings of ACL},\n  year      = {2024},\n  note      = {arXiv:2305.13242},\n  url       = {https://arxiv.org/abs/2305.13242},\n}\n\n@inproceedings{yang2024_dnagpt,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "e4bf85c0-5a39-49b8-aade-2dfd3b8d06c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013UQKFVdNyoR5YdUka6u3at",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3548,
      "cache_read_input_tokens": 51746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3548
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

_source line 38 · 2026-05-17T17:06:43.473Z_

<details><summary>↩ Tool result · `toolu_01414pWtzc3g7r2ckDhBJitB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "1df9c98f-97c6-4df5-a568-7d3f69d6f3f8",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "oldString": "@inproceedings{yang2024_dnagpt,",
    "newString": "@inproceedings{li2024_mage,\n  author    = {Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min},\n  title     = {{MAGE: Machine-generated Text Detection in the Wild}},\n  booktitle = {Proceedings of ACL},\n  year      = {2024},\n  note      = {arXiv:2305.13242},\n  url       = {https://arxiv.org/abs/2305.13242},\n}\n\n@inproceedings{yang2024_dnagpt,",
    "originalFile": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2025},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n@inproceedings{shi2025_closer_look,\n  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{yi2026_escaping_collapse,\n  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},\n  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},\n  booktitle = {3rd DATA-FM Workshop at ICLR 2026},\n  year      = {2026},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n@article{wu2025_detection_survey,\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  journal   = {Computational Linguistics},\n  volume    = {51},\n  number    = {1},\n  pages     = {275--354},\n  year      = {2025},\n  publisher = {MIT Press},\n}\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{bevendorff2025_two_paradigms,\n  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},\n  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  pages     = {3762--3787},\n  year      = {2025},\n  address   = {Vienna, Austria},\n}\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Geometric / intrinsic dimension detectors ---\n\n@inproceedings{tulchinskii2024_intrinsic_dim,\n  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},\n  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2306.04723},\n  url       = {https://arxiv.org/abs/2306.04723},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@article{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  journal   = {arXiv preprint arXiv:1907.11692},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n\n% ============================================================\n% Large Language Models (cross-scale experiments)\n% ============================================================\n\n@misc{qwen2.5,\n  author    = {Qwen Team},\n  title     = {{Qwen2.5: A Party of Foundation Models}},\n  year      = {2025},\n  howpublished = {arXiv:2412.15115},\n  url       = {https://arxiv.org/abs/2412.15115},\n}\n\n@misc{llama3,\n  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},\n  title     = {{The Llama 3 Herd of Models}},\n  year      = {2024},\n  howpublished = {arXiv:2407.21783},\n  url       = {https://arxiv.org/abs/2407.21783},\n}\n\n% ============================================================\n% Additional References (R5-R7 fixes)\n% ============================================================\n\n@article{schaeffer2025,\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  title     = {{Position: Model Collapse Does Not Mean What You Think}},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n@inproceedings{frank2001,\n  author    = {Frank, Eibe and Hall, Mark},\n  title     = {{A Simple Approach to Ordinal Classification}},\n  booktitle = {Proceedings of ECML},\n  year      = {2001},\n  pages     = {145--156},\n}\n\n@inproceedings{rennie2005,\n  author    = {Rennie, Jason D. M. and Srebro, Nathan},\n  title     = {{Loss Functions for Preference Levels: Regression with Discrete Ordered Labels}},\n  booktitle = {Proceedings of IJCAI Workshop on Advances in Preference Handling},\n  year      = {2005},\n}\n\n@article{mccullagh1980_ordinal,\n  title={Regression Models for Ordinal Data},\n  author={McCullagh, Peter},\n  journal={Journal of the Royal Statistical Society: Series B},\n  volume={42},\n  number={2},\n  pages={109--142},\n  year={1980}\n}\n\n@inproceedings{wenzek2020_ccnet,\n  title={{CCNet}: Extracting High Quality Monolingual Datasets from Web Crawl Data},\n  author={Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle={Proceedings of LREC},\n  year={2020}\n}\n\n@inproceedings{dugan2024_raid,\n  author    = {Dugan, Liam and Hwang, Alyssa and Trhl{\\'\\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},\n  title     = {{RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors}},\n  booktitle = {Proceedings of ACL},\n  pages     = {12463--12492},\n  year      = {2024},\n  note      = {arXiv:2405.07940},\n  url       = {https://arxiv.org/abs/2405.07940},\n}\n\n% ============================================================\n% Reviewer-requested citations (MR1--MR5)\n% ============================================================\n\n@inproceedings{guo2024curious,\n  author    = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo{\\'e}},\n  title     = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  booktitle = {Findings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2311.09807},\n  url       = {https://arxiv.org/abs/2311.09807},\n}\n\n@inproceedings{padmakumar2024diversity,\n  author    = {Padmakumar, Vishakh and He, He},\n  title     = {{Does Writing with Language Models Reduce Content Diversity?}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2309.05196},\n  url       = {https://arxiv.org/abs/2309.05196},\n}\n\n@misc{briesch2024selfconsuming,\n  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  title     = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},\n  year      = {2024},\n  howpublished = {arXiv:2311.16822},\n  url       = {https://arxiv.org/abs/2311.16822},\n}\n\n@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 304,
        "oldLines": 6,
        "newStart": 304,
        "newLines": 15,
        "lines": [
          "   url       = {https://arxiv.org/abs/2404.14183},",
          " }",
          " ",
          "+@inproceedings{li2024_mage,",
          "+  author    = {Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min},",
          "+  title     = {{MAGE: Machine-generated Text Detection in the Wild}},",
          "+  booktitle = {Proceedings of ACL},",
          "+  year      = {2024},",
          "+  note      = {arXiv:2305.13242},",
          "+  url       = {https://arxiv.org/abs/2305.13242},",
          "+}",
          "+",
          " @inproceedings{yang2024_dnagpt,",
          "   author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},",
          "   title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},"
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

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_012CFUyTFaY2xaGAvmDKDYB6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
  "old_string": "@article{sugiyama2007_importance_weighting,",
  "new_string": "@inproceedings{penedo2024_fineweb,\n  author    = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Lozhkov, Anton and Mitchell, Margaret and Wolf, Thomas and von Werra, Leandro},\n  title     = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2406.17557},\n  url       = {https://arxiv.org/abs/2406.17557},\n}\n\n@article{sugiyama2007_importance_weighting,"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "95aa065d-3db5-4bc3-bdfd-c87ee2ab8ebc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QReZuYS8nc4QPccKGzVPJn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 55294,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

_source line 40 · 2026-05-17T17:06:49.540Z_

<details><summary>↩ Tool result · `toolu_012CFUyTFaY2xaGAvmDKDYB6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "0f542c4d-67d0-4f94-a7f8-bb0eecbc6cd3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib",
    "oldString": "@article{sugiyama2007_importance_weighting,",
    "newString": "@inproceedings{penedo2024_fineweb,\n  author    = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Lozhkov, Anton and Mitchell, Margaret and Wolf, Thomas and von Werra, Leandro},\n  title     = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2406.17557},\n  url       = {https://arxiv.org/abs/2406.17557},\n}\n\n@article{sugiyama2007_importance_weighting,",
    "originalFile": "% ============================================================\n% Model Collapse Theory\n% ============================================================\n\n@article{shumailov2024_nature,\n  author    = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  title     = {{AI models collapse when trained on recursively generated data}},\n  journal   = {Nature},\n  volume    = {631},\n  pages     = {755--759},\n  year      = {2024},\n  doi       = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{dohmatob2024_tale_of_tails,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Yang, Pu and Charton, Francois and Kempe, Julia},\n  title     = {{A Tale of Tails: Model Collapse as a Change of Scaling Laws}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.07043},\n  url       = {https://arxiv.org/abs/2402.07043},\n}\n\n@inproceedings{dohmatob2025_strong_collapse,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  title     = {{Strong Model Collapse}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2025},\n  note      = {arXiv:2410.04840},\n  url       = {https://arxiv.org/abs/2410.04840},\n}\n\n@inproceedings{dohmatob2024_demystified,\n  author    = {Dohmatob, Elvis and Feng, Yunzhen and Kempe, Julia},\n  title     = {{Model Collapse Demystified: The Case of Regression}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2024},\n  note      = {arXiv:2402.07712},\n  url       = {https://arxiv.org/abs/2402.07712},\n}\n\n@inproceedings{alemohammad2024_mad,\n  author    = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  title     = {{Self-Consuming Generative Models Go MAD}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2307.01850},\n  url       = {https://arxiv.org/abs/2307.01850},\n}\n\n@misc{gerstgrasser2024_accumulate,\n  author    = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  title     = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  year      = {2024},\n  howpublished = {arXiv:2404.01413},\n  url       = {https://arxiv.org/abs/2404.01413},\n}\n\n@inproceedings{marchi2024_heat_death,\n  author    = {Marchi, Matteo and Soatto, Stefano and Chaudhari, Pratik and Tabuada, Paulo},\n  title     = {{Heat Death of Generative Models in Closed-Loop Learning}},\n  booktitle = {Proceedings of ICASSP},\n  year      = {2024},\n  note      = {arXiv:2404.02325},\n  url       = {https://arxiv.org/abs/2404.02325},\n}\n\n@misc{knowledge_collapse2025,\n  author    = {Keisha, Figarri and Wu, Zekun and Wang, Ze and Koshiyama, Adriano and Treleaven, Philip},\n  title     = {{Knowledge Collapse in LLMs: When Fluency Survives but Facts Fail under Recursive Synthetic Training}},\n  year      = {2025},\n  howpublished = {arXiv:2509.04796},\n  url       = {https://arxiv.org/abs/2509.04796},\n}\n\n@misc{sigma2026_spectral,\n  author    = {Gu, Yi and Pang, Lingyou and Ye, Xiangkun and Wang, Tianyu and Lin, Jianyu and Priebe, Carey E. and Aue, Alexander},\n  title     = {{SIGMA: Scalable Spectral Insights for LLM Model Collapse}},\n  year      = {2026},\n  howpublished = {arXiv:2601.03385},\n  url       = {https://arxiv.org/abs/2601.03385},\n}\n\n@inproceedings{mohamed2025_broken_telephone,\n  author    = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  title     = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  booktitle = {Proceedings of ACL},\n  year      = {2025},\n  note      = {arXiv:2502.20258},\n  url       = {https://arxiv.org/abs/2502.20258},\n}\n\n@inproceedings{synthetic_eggs2026,\n  author    = {Schaffelder, Max and Gatt, Albert},\n  title     = {{Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning}},\n  booktitle = {Findings of ACL},\n  year      = {2026},\n  note      = {arXiv:2511.01490},\n  url       = {https://arxiv.org/abs/2511.01490},\n}\n\n@inproceedings{shi2025_closer_look,\n  author    = {Shi, Lianghe and Wu, Meng and Zhang, Huijie and Zhang, Zekai and Tao, Molei and Qu, Qing},\n  title     = {{A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2025},\n  note      = {Spotlight},\n}\n\n@inproceedings{yi2026_escaping_collapse,\n  author    = {Yi, Bingji and Liu, Qiyuan and Cheng, Yuwei and Xu, Haifeng},\n  title     = {{Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence}},\n  booktitle = {3rd DATA-FM Workshop at ICLR 2026},\n  year      = {2026},\n}\n\n% --- Model collapse: collapse-can-be-avoided / contamination ---\n\n@inproceedings{drayson2025_detection_prevents_collapse,\n  author    = {Drayson, George and Yilmaz, Emine and Lampos, Vasileios},\n  title     = {{Machine-generated text detection prevents language model collapse}},\n  booktitle = {Findings of EMNLP},\n  year      = {2025},\n  note      = {arXiv:2502.15654},\n  url       = {https://arxiv.org/abs/2502.15654},\n}\n\n@misc{bakshi2026_collapse_improvement,\n  author    = {Bakshi, Soham and Chakraborty, Sunrit},\n  title     = {{From Collapse to Improvement: Statistical Perspectives on the Evolutionary Dynamics of Iterative Training on Contaminated Sources}},\n  year      = {2026},\n  howpublished = {arXiv:2602.10531},\n  url       = {https://arxiv.org/abs/2602.10531},\n}\n\n@misc{wang2026_contamination,\n  author    = {Wang, Kevin and Niu, Hongqian and Li, Didong},\n  title     = {{Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training}},\n  year      = {2026},\n  howpublished = {arXiv:2602.16065},\n  url       = {https://arxiv.org/abs/2602.16065},\n}\n\n@misc{falahati2026_curated,\n  author    = {Falahati, Ali and Mohammadi Amiri, Mohammad and Larson, Kate and Golab, Lukasz},\n  title     = {{Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences}},\n  year      = {2026},\n  howpublished = {arXiv:2605.07724},\n  url       = {https://arxiv.org/abs/2605.07724},\n}\n\n% ============================================================\n% AI-Generated Text Detection\n% ============================================================\n\n@article{wu2025_detection_survey,\n  author    = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  title     = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  journal   = {Computational Linguistics},\n  volume    = {51},\n  number    = {1},\n  pages     = {275--354},\n  year      = {2025},\n  publisher = {MIT Press},\n}\n\n% --- Statistical / zero-shot detectors ---\n\n@inproceedings{gehrmann2019_gltr,\n  author    = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  title     = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  booktitle = {Proceedings of ACL: System Demonstrations},\n  year      = {2019},\n  note      = {arXiv:1906.04043},\n  url       = {https://arxiv.org/abs/1906.04043},\n}\n\n@inproceedings{mitchell2023_detectgpt,\n  author    = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  title     = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.11305},\n  url       = {https://arxiv.org/abs/2301.11305},\n}\n\n@inproceedings{fast_detectgpt2024,\n  author    = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  title     = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.05130},\n  url       = {https://arxiv.org/abs/2310.05130},\n}\n\n@inproceedings{binoculars2024,\n  author    = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  title     = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2401.12070},\n  url       = {https://arxiv.org/abs/2401.12070},\n}\n\n@article{diveye2026,\n  author    = {Basani, Advik Raj and Chen, Pin-Yu},\n  title     = {{Diversity Boosts AI-Generated Text Detection}},\n  journal   = {Transactions on Machine Learning Research (TMLR)},\n  year      = {2026},\n  note      = {arXiv:2509.18880},\n  url       = {https://arxiv.org/abs/2509.18880},\n}\n\n% --- Robustness / limitations of detectors ---\n\n@misc{sadasivan2023_paraphrase,\n  author    = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  title     = {{Can AI-Generated Text be Reliably Detected?}},\n  year      = {2023},\n  howpublished = {arXiv:2303.11156},\n  url       = {https://arxiv.org/abs/2303.11156},\n}\n\n@misc{pudasaini2026_detection_fails,\n  author    = {Pudasaini, Shushanta and Miralles-Pech{\\'u}an, Luis and Lillis, David and Llorens Salvador, Marisa},\n  title     = {{Why AI-Generated Text Detection Fails: Evidence from Explainable AI Beyond Benchmark Accuracy}},\n  year      = {2026},\n  howpublished = {arXiv:2603.23146},\n  url       = {https://arxiv.org/abs/2603.23146},\n}\n\n@misc{pu2026_generator_barrier,\n  author    = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  title     = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  year      = {2026},\n  howpublished = {arXiv:2604.13692},\n  url       = {https://arxiv.org/abs/2604.13692},\n}\n\n% --- Beyond binary: attribution, editing extent, benchmarks ---\n\n@inproceedings{bevendorff2025_two_paradigms,\n  author    = {Bevendorff, Janek and Wiegmann, Matti and Richter, Emmelie and Potthast, Martin and Stein, Benno},\n  title     = {{The Two Paradigms of LLM Detection: Authorship Attribution vs. Authorship Verification}},\n  booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n  pages     = {3762--3787},\n  year      = {2025},\n  address   = {Vienna, Austria},\n}\n\n@inproceedings{uchendu2020_attribution,\n  author    = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  title     = {{Authorship Attribution for Neural Text Generation}},\n  booktitle = {Proceedings of EMNLP},\n  year      = {2020},\n}\n\n@inproceedings{editlens2026,\n  author    = {Thai, Katherine and Emi, Bradley and Masrour, Elyas and Iyyer, Mohit},\n  title     = {{EditLens: Quantifying the Extent of AI Editing in Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2026},\n  note      = {arXiv:2510.03154},\n  url       = {https://arxiv.org/abs/2510.03154},\n}\n\n@inproceedings{loki2025,\n  author    = {Ye, Junyan and Zhou, Baichuan and Huang, Zilong and Zhang, Junan and Bai, Tianyi and Kang, Hengrui and He, Jun and Lin, Honglin and Wang, Zihao and Wu, Tong and Wu, Zhizheng and Chen, Yiping and Lin, Dahua and He, Conghui and Li, Weijia},\n  title     = {{LOKI: A Comprehensive Synthetic Data Detection Benchmark using Large Multimodal Models}},\n  booktitle = {Proceedings of ICLR (Spotlight)},\n  year      = {2025},\n  note      = {arXiv:2410.09732},\n  url       = {https://arxiv.org/abs/2410.09732},\n}\n\n% --- Geometric / intrinsic dimension detectors ---\n\n@inproceedings{tulchinskii2024_intrinsic_dim,\n  author    = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Barannikov, Serguei and Piontkovskaya, Irina and Nikolenko, Sergey and Burnaev, Evgeny},\n  title     = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2306.04723},\n  url       = {https://arxiv.org/abs/2306.04723},\n}\n\n% --- Statistical / feature-based / shared-task detectors ---\n\n@inproceedings{verma2024_ghostbuster,\n  author    = {Verma, Vivek and Fleisig, Eve and Tomlin, Nicholas and Klein, Dan},\n  title     = {{Ghostbuster: Detecting Text Ghostwritten by Large Language Models}},\n  booktitle = {Proceedings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2305.15047},\n  url       = {https://arxiv.org/abs/2305.15047},\n}\n\n@inproceedings{wang2024_m4_semeval,\n  author    = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  title     = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  booktitle = {Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)},\n  year      = {2024},\n  note      = {arXiv:2404.14183},\n  url       = {https://arxiv.org/abs/2404.14183},\n}\n\n@inproceedings{li2024_mage,\n  author    = {Li, Yongkang and Li, Donghao and Yang, Yue and Hu, Baotian and Zhang, Min},\n  title     = {{MAGE: Machine-generated Text Detection in the Wild}},\n  booktitle = {Proceedings of ACL},\n  year      = {2024},\n  note      = {arXiv:2305.13242},\n  url       = {https://arxiv.org/abs/2305.13242},\n}\n\n@inproceedings{yang2024_dnagpt,\n  author    = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  title     = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2305.17359},\n  url       = {https://arxiv.org/abs/2305.17359},\n}\n\n% --- Watermarking ---\n\n@inproceedings{kirchenbauer2023_watermark,\n  author    = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  title     = {{A Watermark for Large Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2023},\n  note      = {arXiv:2301.10226},\n  url       = {https://arxiv.org/abs/2301.10226},\n}\n\n% ============================================================\n% Decoding Strategies\n% ============================================================\n\n@inproceedings{holtzman2020_nucleus,\n  author    = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  title     = {{The Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2020},\n  note      = {arXiv:1904.09751},\n  url       = {https://arxiv.org/abs/1904.09751},\n}\n\n@inproceedings{finlayson2024_closing,\n  author    = {Finlayson, Matthew and Hewitt, John and Koller, Alexander and Swayamdipta, Swabha and Sabharwal, Ashish},\n  title     = {{Closing the Curious Case of Neural Text Degeneration}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2310.01693},\n  url       = {https://arxiv.org/abs/2310.01693},\n}\n\n@inproceedings{garces_arias2025_decoding_decoded,\n  author    = {{Garces Arias}, Esteban and Li, Meimingwei and Heumann, Christian and Assenmacher, Matthias},\n  title     = {{Decoding Decoded: Understanding Hyperparameter Effects in Open-Ended Text Generation}},\n  booktitle = {Proceedings of COLING},\n  year      = {2025},\n  note      = {arXiv:2410.06097},\n  url       = {https://arxiv.org/abs/2410.06097},\n}\n\n@article{wiher2022_decoding,\n  author    = {Wiher, Gian and Meister, Clara and Cotterell, Ryan},\n  title     = {{On Decoding Strategies for Neural Text Generators}},\n  journal   = {Transactions of the Association for Computational Linguistics},\n  volume    = {10},\n  pages     = {997--1012},\n  year      = {2022},\n}\n\n@inproceedings{basu2021_mirostat,\n  author    = {Basu, Sourya and Ramachandran, Govardana Sachitanandam and Keskar, Nitish Shirish and Varshney, Lav R.},\n  title     = {{Mirostat: A Neural Text Decoding Algorithm that Directly Controls Perplexity}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2021},\n}\n\n% ============================================================\n% Ordinal Classification / Contrastive Learning\n% ============================================================\n\n@article{coral2020,\n  author    = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  title     = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  journal   = {Pattern Recognition Letters},\n  volume    = {140},\n  pages     = {325--331},\n  year      = {2020},\n  note      = {arXiv:1901.07884},\n  url       = {https://arxiv.org/abs/1901.07884},\n}\n\n@inproceedings{cloc2025,\n  author    = {Pitawela, Dileepa and Carneiro, Gustavo and Chen, Hsiang-Ting},\n  title     = {{CLOC: Contrastive Learning for Ordinal Classification with Multi-Margin N-pair Loss}},\n  booktitle = {Proceedings of CVPR},\n  year      = {2025},\n  note      = {arXiv:2504.17813},\n  url       = {https://arxiv.org/abs/2504.17813},\n}\n\n% ============================================================\n% Foundation Models / Fine-tuning\n% ============================================================\n\n@inproceedings{hu2022lora,\n  author    = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},\n  title     = {{LoRA: Low-Rank Adaptation of Large Language Models}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2022},\n  note      = {arXiv:2106.09685},\n  url       = {https://arxiv.org/abs/2106.09685},\n}\n\n@inproceedings{he2021_deberta_v3,\n  author    = {He, Pengcheng and Gao, Jianfeng and Chen, Weizhu},\n  title     = {{DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2023},\n  note      = {arXiv:2111.09543},\n  url       = {https://arxiv.org/abs/2111.09543},\n}\n\n@article{liu2019_roberta,\n  author    = {Liu, Yinhan and Ott, Myle and Goyal, Naman and Du, Jingfei and Joshi, Mandar and Chen, Danqi and Levy, Omer and Lewis, Mike and Zettlemoyer, Luke and Stoyanov, Veselin},\n  title     = {{RoBERTa: A Robustly Optimized BERT Pretraining Approach}},\n  journal   = {arXiv preprint arXiv:1907.11692},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1907.11692},\n}\n\n% ============================================================\n% Data Curation / Selection\n% ============================================================\n\n@inproceedings{dsir2023,\n  author    = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  title     = {{Data Selection for Language Models via Importance Resampling}},\n  booktitle = {Proceedings of NeurIPS},\n  year      = {2023},\n  note      = {arXiv:2302.03169},\n  url       = {https://arxiv.org/abs/2302.03169},\n}\n\n@inproceedings{qurating2024,\n  author    = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  title     = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  booktitle = {Proceedings of ICML},\n  year      = {2024},\n  note      = {arXiv:2402.09739},\n  url       = {https://arxiv.org/abs/2402.09739},\n}\n\n@article{sugiyama2007_importance_weighting,\n  author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},\n  title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},\n  journal   = {Journal of Machine Learning Research},\n  volume    = {8},\n  pages     = {985--1005},\n  year      = {2007},\n}\n\n% ============================================================\n% Large Language Models (cross-scale experiments)\n% ============================================================\n\n@misc{qwen2.5,\n  author    = {Qwen Team},\n  title     = {{Qwen2.5: A Party of Foundation Models}},\n  year      = {2025},\n  howpublished = {arXiv:2412.15115},\n  url       = {https://arxiv.org/abs/2412.15115},\n}\n\n@misc{llama3,\n  author    = {Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and Letman, Aiesha and Mathur, Akhil and Schelten, Alan and others},\n  title     = {{The Llama 3 Herd of Models}},\n  year      = {2024},\n  howpublished = {arXiv:2407.21783},\n  url       = {https://arxiv.org/abs/2407.21783},\n}\n\n% ============================================================\n% Additional References (R5-R7 fixes)\n% ============================================================\n\n@article{schaeffer2025,\n  author    = {Schaeffer, Rylan and Kazdan, Joshua and Arulandu, Alvan Caleb and Koyejo, Sanmi},\n  title     = {{Position: Model Collapse Does Not Mean What You Think}},\n  journal   = {arXiv preprint arXiv:2503.03150},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2503.03150},\n}\n\n@inproceedings{frank2001,\n  author    = {Frank, Eibe and Hall, Mark},\n  title     = {{A Simple Approach to Ordinal Classification}},\n  booktitle = {Proceedings of ECML},\n  year      = {2001},\n  pages     = {145--156},\n}\n\n@inproceedings{rennie2005,\n  author    = {Rennie, Jason D. M. and Srebro, Nathan},\n  title     = {{Loss Functions for Preference Levels: Regression with Discrete Ordered Labels}},\n  booktitle = {Proceedings of IJCAI Workshop on Advances in Preference Handling},\n  year      = {2005},\n}\n\n@article{mccullagh1980_ordinal,\n  title={Regression Models for Ordinal Data},\n  author={McCullagh, Peter},\n  journal={Journal of the Royal Statistical Society: Series B},\n  volume={42},\n  number={2},\n  pages={109--142},\n  year={1980}\n}\n\n@inproceedings{wenzek2020_ccnet,\n  title={{CCNet}: Extracting High Quality Monolingual Datasets from Web Crawl Data},\n  author={Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle={Proceedings of LREC},\n  year={2020}\n}\n\n@inproceedings{dugan2024_raid,\n  author    = {Dugan, Liam and Hwang, Alyssa and Trhl{\\'\\i}k, Filip and Zhu, Andrew and Ludan, Josh Magnus and Xu, Hainiu and Ippolito, Daphne and Callison-Burch, Chris},\n  title     = {{RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors}},\n  booktitle = {Proceedings of ACL},\n  pages     = {12463--12492},\n  year      = {2024},\n  note      = {arXiv:2405.07940},\n  url       = {https://arxiv.org/abs/2405.07940},\n}\n\n% ============================================================\n% Reviewer-requested citations (MR1--MR5)\n% ============================================================\n\n@inproceedings{guo2024curious,\n  author    = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo{\\'e}},\n  title     = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  booktitle = {Findings of NAACL},\n  year      = {2024},\n  note      = {arXiv:2311.09807},\n  url       = {https://arxiv.org/abs/2311.09807},\n}\n\n@inproceedings{padmakumar2024diversity,\n  author    = {Padmakumar, Vishakh and He, He},\n  title     = {{Does Writing with Language Models Reduce Content Diversity?}},\n  booktitle = {Proceedings of ICLR},\n  year      = {2024},\n  note      = {arXiv:2309.05196},\n  url       = {https://arxiv.org/abs/2309.05196},\n}\n\n@misc{briesch2024selfconsuming,\n  author    = {Briesch, Martin and Sobania, Dominik and Rothlauf, Franz},\n  title     = {{Large Language Models Suffer From Their Own Output: An Analysis of the Self-Consuming Training Loop}},\n  year      = {2024},\n  howpublished = {arXiv:2311.16822},\n  url       = {https://arxiv.org/abs/2311.16822},\n}\n\n@misc{seddik2024synthetic,\n  author    = {Seddik, Mohamed El Amine and Chen, Suei-Wen and Hayou, Soufiane and Youssef, Pierre and Debbah, Merouane},\n  title     = {{How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse}},\n  year      = {2024},\n  howpublished = {arXiv:2404.05090},\n  url       = {https://arxiv.org/abs/2404.05090},\n}\n",
    "structuredPatch": [
      {
        "oldStart": 456,
        "oldLines": 6,
        "newStart": 456,
        "newLines": 15,
        "lines": [
          "   url       = {https://arxiv.org/abs/2402.09739},",
          " }",
          " ",
          "+@inproceedings{penedo2024_fineweb,",
          "+  author    = {Penedo, Guilherme and Kydl{\\'\\i}{\\v{c}}ek, Hynek and Lozhkov, Anton and Mitchell, Margaret and Wolf, Thomas and von Werra, Leandro},",
          "+  title     = {{The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale}},",
          "+  booktitle = {Proceedings of NeurIPS},",
          "+  year      = {2024},",
          "+  note      = {arXiv:2406.17557},",
          "+  url       = {https://arxiv.org/abs/2406.17557},",
          "+}",
          "+",
          " @article{sugiyama2007_importance_weighting,",
          "   author    = {Sugiyama, Masashi and Krauledat, Matthias and M{\\\"u}ller, Klaus-Robert},",
          "   title     = {{Covariate Shift Adaptation by Importance Weighted Cross Validation}},"
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

_source line 41_

Now integrate these into `related_work.tex`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "bc9221a3-237f-411c-b7a1-0074808817ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QLbbc3q5mshtqPhZv7Bvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 55657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 395
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01NyfG8ZrtqAt5mywMzFjXyA`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
  "old_string": "The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}) and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval} and RAID \\cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.",
  "new_string": "The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \\cite{tulchinskii2024_intrinsic_dim}, and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval}, RAID \\cite{dugan2024_raid}, and MAGE \\cite{li2024_mage} benchmark detection across domains, models, and adversarial conditions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "5376ea4c-1b98-4cf3-866e-018491d9c3fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QLbbc3q5mshtqPhZv7Bvp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 395,
      "cache_read_input_tokens": 55657,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 395
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

_source line 43 · 2026-05-17T17:07:01.258Z_

<details><summary>↩ Tool result · `toolu_01NyfG8ZrtqAt5mywMzFjXyA`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "72412b8c-9d3a-4a5a-8b61-8ab3fdfe2e0b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/related_work.tex",
    "oldString": "The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}) and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval} and RAID \\cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.",
    "newString": "The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \\cite{tulchinskii2024_intrinsic_dim}, and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval}, RAID \\cite{dugan2024_raid}, and MAGE \\cite{li2024_mage} benchmark detection across domains, models, and adversarial conditions.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Model Collapse Theory.}\n\\citet{shumailov2024_nature} demonstrate that recursive training on model outputs erodes distributional tails; \\citet{dohmatob2024_tale_of_tails} formalize this via scaling laws \\cite{seddik2024synthetic}, \\citet{dohmatob2025_strong_collapse} establish strong collapse guarantees, and the MAD framework \\cite{alemohammad2024_mad} extends the analysis to self-consuming models.\nSubsequent work addresses mitigation \\cite{gerstgrasser2024_accumulate,drayson2025_detection_prevents_collapse,yi2026_escaping_collapse,falahati2026_curated,wenzek2020_ccnet}, non-monotonic dynamics \\cite{bakshi2026_collapse_improvement}, convergence \\cite{marchi2024_heat_death,wang2026_contamination,knowledge_collapse2025,dohmatob2024_demystified}, and diversity decline \\cite{guo2024curious,briesch2024selfconsuming,padmakumar2024diversity,sigma2026_spectral,synthetic_eggs2026}.\n\\citet{schaeffer2025} argue that ``model collapse'' conflates multiple distinct phenomena, underscoring the need for operationally precise metrics.\nDohmatob et al.\\ predict that recursive training erodes distributional tails as a theoretical scaling law \\citep{dohmatob2024_tale_of_tails}; we operationalize this prediction into a deployable ordinal classifier, revealing strategy-dependent trajectories and non-monotonic 7B behavior that the theory does not predict.\nAll assume depth is known a priori; we address the inverse problem of estimating depth from text alone.\n\n\\paragraph{AI Text Detection.}\nThe detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}) and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.\nM4-SemEval \\cite{wang2024_m4_semeval} and RAID \\cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.\nAll these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.\n\n\\paragraph{Adjacent Tasks.}\nEditLens \\cite{editlens2026} estimates editing extent but does not model recursive chains; \\citet{uchendu2020_attribution} classify \\emph{which} model generated text; LOKI \\cite{loki2025} benchmarks synthetic data detection across modalities.\n\\citet{mohamed2025_broken_telephone} study iterative generation as a ``broken telephone'' effect, characterizing \\emph{how} text degrades without classifying which iteration a passage comes from.\nOur task performs the inverse, ordinal depth estimation from text alone, discriminating between adjacent depths rather than merely detecting aggregate degradation.\n\n\\paragraph{Ordinal Classification.}\nOrdinal classification has a long history \\cite{mccullagh1980_ordinal}: \\citet{frank2001} reduce ordinal problems to nested binary tasks, and \\citet{rennie2005} introduce loss functions tailored to discrete ordered labels.\nCORAL \\cite{coral2020} enforces rank consistency via ordered binary tasks; CLOC \\cite{cloc2025} extends contrastive learning with multi-margin ordinal losses.\nWe adopt both as baselines (\\S\\ref{sec:generalization}) to confirm the signal is accessible to principled ordinal methods.\n\n\\paragraph{Decoding Strategy Effects.}\nDecoding strategies shape text statistics in ways that interact with depth signals \\cite{holtzman2020_nucleus,finlayson2024_closing,garces_arias2025_decoding_decoded,wiher2022_decoding,basu2021_mirostat}.\nOur Depth Degradation Atlas (\\S\\ref{sec:atlas}) reveals that these strategies induce qualitatively different degradation trajectories under recursive generation: temperature sampling accelerates convergence to a low-entropy attractor while top-$k$ attenuates the depth signal, effects beyond single-pass text quality.",
    "structuredPatch": [
      {
        "oldStart": 9,
        "oldLines": 8,
        "newStart": 9,
        "newLines": 8,
        "lines": [
          " All assume depth is known a priori; we address the inverse problem of estimating depth from text alone.",
          " ",
          " \\paragraph{AI Text Detection.}",
          "-The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}) and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.",
          "-M4-SemEval \\cite{wang2024_m4_semeval} and RAID \\cite{dugan2024_raid} benchmark detection across domains and adversarial conditions.",
          "+The detection literature \\cite{wu2025_detection_survey} spans statistical methods (DetectGPT \\cite{mitchell2023_detectgpt}, Fast-DetectGPT \\cite{fast_detectgpt2024}, Binoculars \\cite{binoculars2024}, DivEye \\cite{diveye2026}, GLTR \\cite{gehrmann2019_gltr}, Ghostbuster \\cite{verma2024_ghostbuster}, DNA-GPT \\cite{yang2024_dnagpt}), geometric approaches based on intrinsic dimensionality \\cite{tulchinskii2024_intrinsic_dim}, and watermarking \\cite{kirchenbauer2023_watermark}, with known limits from paraphrasing \\cite{sadasivan2023_paraphrase}, distribution shift \\cite{pudasaini2026_detection_fails}, and generator barriers \\cite{pu2026_generator_barrier}.",
          "+M4-SemEval \\cite{wang2024_m4_semeval}, RAID \\cite{dugan2024_raid}, and MAGE \\cite{li2024_mage} benchmark detection across domains, models, and adversarial conditions.",
          " All these methods perform binary classification, discarding ordinal depth information; our approach outputs ordinal depth labels, complementing rather than replacing binary detection.",
          " ",
          " \\paragraph{Adjacent Tasks.}"
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

_source line 44_

Now add `penedo2024_fineweb` to the discussion.tex where data curation is mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "f6d36bfb-2374-4ad4-b712-b345727991c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017brfEBYcFLPXYeXNUjZGKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 56052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 836
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Read · `toolu_01DRrjYVFFKZ9rnJAoMv7zi7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "a8373124-85fa-4946-8b7d-2a1d8b1dde19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017brfEBYcFLPXYeXNUjZGKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 56052,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 836
      },
      "output_tokens": 2,
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

_source line 46 · 2026-05-17T17:07:12.267Z_

<details><summary>↩ Tool result · `toolu_01DRrjYVFFKZ9rnJAoMv7zi7`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	We formalized recursive generation depth estimation and showed that perplexity tail statistics achieve 69--86\% four-class accuracy ($\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\% of full performance and classifier-agnostic convergence within $\leq$0.4pp.
5	These features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\% (\S\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.
6	Cross-strategy transfer remains the primary bottleneck; see Limitations for detailed analysis.
7	Depth-graduated curation complements binary detection~\cite{dsir2023,qurating2024} and watermarking~\cite{kirchenbauer2023_watermark} as a provenance signal~\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\ref{app:curation_poc}) and adversarial robustness remains untested.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "d6dfb295-ae07-4b4c-9639-cc4ab19d55f1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nWe formalized recursive generation depth estimation and showed that perplexity tail statistics achieve 69--86\\% four-class accuracy ($\\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\\% of full performance and classifier-agnostic convergence within $\\leq$0.4pp.\nThese features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\\% (\\S\\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.\nCross-strategy transfer remains the primary bottleneck; see Limitations for detailed analysis.\nDepth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024} and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_01SDe5RstECcj9V2vB6hyrDd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
  "old_string": "Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024} and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.",
  "new_string": "Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024}, web-scale quality filtering~\\cite{penedo2024_fineweb}, and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "76022883-b47c-43df-8c16-f8914a8625fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JCFgaxR3EbE1nBVGhU6tSs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 56888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 48 · 2026-05-17T17:07:17.556Z_

<details><summary>↩ Tool result · `toolu_01SDe5RstECcj9V2vB6hyrDd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "1db27361-b138-4994-97e8-5bc300ea8d94",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/discussion.tex",
    "oldString": "Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024} and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.",
    "newString": "Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024}, web-scale quality filtering~\\cite{penedo2024_fineweb}, and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.",
    "originalFile": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\nWe formalized recursive generation depth estimation and showed that perplexity tail statistics achieve 69--86\\% four-class accuracy ($\\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\\% of full performance and classifier-agnostic convergence within $\\leq$0.4pp.\nThese features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\\% (\\S\\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.\nCross-strategy transfer remains the primary bottleneck; see Limitations for detailed analysis.\nDepth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024} and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.\n",
    "structuredPatch": [
      {
        "oldStart": 4,
        "oldLines": 4,
        "newStart": 4,
        "newLines": 4,
        "lines": [
          " We formalized recursive generation depth estimation and showed that perplexity tail statistics achieve 69--86\\% four-class accuracy ($\\mathrm{EDD}_{0.75}{=}4$), with five features sufficing for 97.6\\% of full performance and classifier-agnostic convergence within $\\leq$0.4pp.",
          " These features generalize across model families without retraining, positioning depth estimation as an early-warning signal for model collapse~\\cite{shumailov2024_nature,shi2025_closer_look}; zero-shot LLMs at 30--36\\% (\\S\\ref{sec:gen:baselines}) confirm the signal is inaccessible from surface text alone.",
          " Cross-strategy transfer remains the primary bottleneck; see Limitations for detailed analysis.",
          "-Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024} and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested.",
          "+Depth-graduated curation complements binary detection~\\cite{dsir2023,qurating2024}, web-scale quality filtering~\\cite{penedo2024_fineweb}, and watermarking~\\cite{kirchenbauer2023_watermark} as a provenance signal~\\cite{bevendorff2025_two_paradigms}; pilot results are inconclusive (Appendix~\\ref{app:curation_poc}) and adversarial robustness remains untested."
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

_source line 49_

Now let me verify: no duplicate bib entries, all new `\cite{}` have bib entries, and count the final total.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "d6c37b06-415f-4a00-bbd3-2b965156bfa2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMtKugkNcaj8fFid1jD2hs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 405,
      "cache_read_input_tokens": 57330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 405
      },
      "output_tokens": 4,
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

_source line 50_

<details open><summary>🔧 Tool call — Bash · `toolu_01NT7MhA4Gv5hCrEon6PEG8U`</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u | wc -l",
  "description": "Count total unique citations in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "247603af-f0a9-43f0-b2c8-2d4ab808682f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMtKugkNcaj8fFid1jD2hs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 405,
      "cache_read_input_tokens": 57330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 405
      },
      "output_tokens": 4,
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

_source line 51 · 2026-05-17T17:07:26.114Z_

<details><summary>↩ Tool result · `toolu_01NT7MhA4Gv5hCrEon6PEG8U`</summary>

```text
62
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "783b322a-6099-43fa-8d5d-91ea3a783705",
  "tool_use_result": {
    "stdout": "62",
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_017qaowYWMYgAL3JPiFP7eQa`</summary>

```json
{
  "command": "grep -oP '@\\w+\\{([^,]+),' references.bib | grep -oP '\\{[^,]+' | sed 's/{//' | sort | uniq -d",
  "description": "Check for duplicate bib keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "f4c2764c-9db6-417b-be3f-2a620ec5b93b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMtKugkNcaj8fFid1jD2hs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 405,
      "cache_read_input_tokens": 57330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 405
      },
      "output_tokens": 4,
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

_source line 53 · 2026-05-17T17:07:26.205Z_

<details><summary>↩ Tool result · `toolu_017qaowYWMYgAL3JPiFP7eQa`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "2e4b9f4f-a853-4ce9-821d-2de9fd095a33",
  "tool_use_result": {
    "stdout": "",
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

_source line 54_

<details open><summary>🔧 Tool call — Bash · `toolu_012SQZHLksmu5sFWLavhNmoU`</summary>

```json
{
  "command": "comm -23 <(grep -oP '\\\\cite[tp]?\\{[^}]+\\}' *.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u) <(grep -oP '@\\w+\\{([^,]+),' references.bib | grep -oP '\\{[^,]+' | sed 's/{//' | sort -u)",
  "description": "Find cited keys missing from bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "be014b91-a554-41bd-8618-bedf6752bf34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMtKugkNcaj8fFid1jD2hs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 405,
      "cache_read_input_tokens": 57330,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 405
      },
      "output_tokens": 4,
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

_source line 55 · 2026-05-17T17:07:27.525Z_

<details><summary>↩ Tool result · `toolu_012SQZHLksmu5sFWLavhNmoU`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "67a65ff4-4545-48d5-8f90-d53c50210840",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 56_

Also sync to the artifacts copy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "97c8184a-bb55-4cb4-92c6-357cde015919",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lx2ReGs2VAeUNYYA6dqDc4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 57735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 561
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

_source line 57_

<details open><summary>🔧 Tool call — Bash · `toolu_013Nf1Gw9feLhurHaqgiM7Jy`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/docs/paper/references.bib /home/ubuntu/.agent-ml-research-idea_gen_0513_2/projects/recursive_gen_depth_est/artifacts/_project/paper/references.bib",
  "description": "Sync bib file to artifacts copy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "e761056b-d2b0-4c4f-bd2c-4b25e2aa6459",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lx2ReGs2VAeUNYYA6dqDc4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 561,
      "cache_read_input_tokens": 57735,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 561
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

_source line 58 · 2026-05-17T17:07:31.289Z_

<details><summary>↩ Tool result · `toolu_013Nf1Gw9feLhurHaqgiM7Jy`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "72677266-6988-406f-ae40-233ee41c5588",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Assistant

_source line 59_

验证结果：

- **总引用数：62**（远超 30+ 目标）
- **无重复 bib 条目**
- **所有 `\cite{}` 在 bib 中均有对应条目**
- **无 undefined citation**

新增 3 篇（均来自 literature_map 中已有但 bib 中缺失的条目）：

| 引用键 | 论文 | 会议 | 集成位置 |
|--------|------|------|----------|
| `tulchinskii2024_intrinsic_dim` | Intrinsic Dimension Estimation for Robust Detection | NeurIPS 2023 | Related Work: AI Text Detection 段 |
| `li2024_mage` | MAGE: Machine-generated Text Detection in the Wild | ACL 2024 | Related Work: AI Text Detection 段（benchmark 列表） |
| `penedo2024_fineweb` | The FineWeb Datasets | NeurIPS 2024 | Discussion: data curation 引用链 |

论文已有的 62 篇引用覆盖了任务要求的所有类别。literature_map 中 43 篇条目现已全部在 bib 中有对应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "uuid": "ed9d1ff0-d66a-4960-8dc0-aacce480048c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UQgybutw2raeBQee7nrRea",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 180,
      "cache_read_input_tokens": 58296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 180
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

_source line 60_

验证结果：

- **总引用数：62**（远超 30+ 目标）
- **无重复 bib 条目**
- **所有 `\cite{}` 在 bib 中均有对应条目**
- **无 undefined citation**

新增 3 篇（均来自 literature_map 中已有但 bib 中缺失的条目）：

| 引用键 | 论文 | 会议 | 集成位置 |
|--------|------|------|----------|
| `tulchinskii2024_intrinsic_dim` | Intrinsic Dimension Estimation for Robust Detection | NeurIPS 2023 | Related Work: AI Text Detection 段 |
| `li2024_mage` | MAGE: Machine-generated Text Detection in the Wild | ACL 2024 | Related Work: AI Text Detection 段（benchmark 列表） |
| `penedo2024_fineweb` | The FineWeb Datasets | NeurIPS 2024 | Discussion: data curation 引用链 |

论文已有的 62 篇引用覆盖了任务要求的所有类别。literature_map 中 43 篇条目现已全部在 bib 中有对应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 158889,
  "duration_api_ms": 159863,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "fb547764-24c1-4361-9888-ae7aba133274",
  "total_cost_usd": 0.8269242499999998,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 46635,
    "cache_read_input_tokens": 646775,
    "output_tokens": 8394,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 46635,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 332,
        "cache_read_input_tokens": 58296,
        "cache_creation_input_tokens": 180,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 180
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2018,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002133,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 8394,
      "cacheReadInputTokens": 646775,
      "cacheCreationInputTokens": 46635,
      "webSearchRequests": 0,
      "costUSD": 0.8247912499999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "52eb67c4-62db-4ef1-9a94-b3b36c5f0fdc"
}
```

</details>

---
