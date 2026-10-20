# Research conversation: Find and read the semi-synthetic gradient experiment code in the irt_equated_bench_regen project. I need to understand: 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a0a57fb98c617a285.jsonl`
- **Structured JSON:** [`f7bc3e57a3baf70f1e7d.json`](../../sessions/f7/f7bc3e57a3baf70f1e7d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-22T19:12:15.652Z_

Find and read the semi-synthetic gradient experiment code in the irt_equated_bench_regen project. I need to understand:

1. How "difficulty" is defined — is it proportion correct (higher = easier) or something else?
2. How Δδ is computed — is it δ_after - δ_before for Mantel-Haenszel Δ_MH?
3. What does Scheme A "capability-like" injection actually do? Is injection probability proportional to item accuracy (easy items targeted) or inversely proportional (hard items targeted)?
4. What does Scheme B "contamination-like" do exactly? Is it truly uniform p=0.5 for all items?
5. How is ρ(diff, Δδ) computed — Spearman correlation between what exact two arrays?

Search in:
- `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/` for .py files
- Also check any scripts in the project `scripts/` directory related to semi-synthetic or injection

Read the FULL implementation of the injection mechanism and the correlation computation. Search breadth: very thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "479d2b2e-c441-4faa-85be-98bfaeb246ff",
  "agentId": "a0a57fb98c617a285",
  "type": "user",
  "uuid": "2e07c5cd-795e-47db-aac5-9e6cce276dd3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-22T19:12:17.379Z_

I'll help you find and analyze the semi-synthetic gradient experiment code. Let me start with a thorough search of the relevant directories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e07c5cd-795e-47db-aac5-9e6cce276dd3",
  "isSidechain": true,
  "agentId": "a0a57fb98c617a285",
  "requestId": "req_011CbJ8yZBSWgw12VMLtmq63",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "90641a1f-2e58-411b-8fd7-989602a9a9ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TGrqyyq9p1N6VL5gDh5veh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18958,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18958,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-22T19:12:17.598Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LARbKYKsczy6YNuTcLRgVR`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90641a1f-2e58-411b-8fd7-989602a9a9ca",
  "isSidechain": true,
  "agentId": "a0a57fb98c617a285",
  "requestId": "req_011CbJ8yZBSWgw12VMLtmq63",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dbe3ad71-c74b-46d8-af3e-1c54be8b861f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TGrqyyq9p1N6VL5gDh5veh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18958,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18958,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-22T19:12:17.616Z_

<details><summary>↩ Tool result · `toolu_01LARbKYKsczy6YNuTcLRgVR`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dbe3ad71-c74b-46d8-af3e-1c54be8b861f",
  "isSidechain": true,
  "promptId": "479d2b2e-c441-4faa-85be-98bfaeb246ff",
  "agentId": "a0a57fb98c617a285",
  "type": "user",
  "uuid": "d86a4e62-f421-4293-a1e9-bee2842a9e54",
  "sourceToolAssistantUUID": "dbe3ad71-c74b-46d8-af3e-1c54be8b861f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-22T19:12:17.837Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0169tRsstwitkD5TmkjmGeAL`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/**/*.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d86a4e62-f421-4293-a1e9-bee2842a9e54",
  "isSidechain": true,
  "agentId": "a0a57fb98c617a285",
  "requestId": "req_011CbJ8yZBSWgw12VMLtmq63",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0ffe7a2c-49fb-49e1-82f3-531839e18409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TGrqyyq9p1N6VL5gDh5veh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18958,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18958,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-22T19:12:17.851Z_

<details><summary>↩ Tool result · `toolu_0169tRsstwitkD5TmkjmGeAL`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r14_domain_profile.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r14_cooks_d_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/r16_dif_union.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ffe7a2c-49fb-49e1-82f3-531839e18409",
  "isSidechain": true,
  "promptId": "479d2b2e-c441-4faa-85be-98bfaeb246ff",
  "agentId": "a0a57fb98c617a285",
  "type": "user",
  "uuid": "3b0d5804-af9a-46c9-b74d-63d8192b1c22",
  "sourceToolAssistantUUID": "0ffe7a2c-49fb-49e1-82f3-531839e18409",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-22T19:12:18.193Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M1XauRsxykaxTysaLinHNp`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -type f -name \"*semi*\" -o -name \"*inject*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b0d5804-af9a-46c9-b74d-63d8192b1c22",
  "isSidechain": true,
  "agentId": "a0a57fb98c617a285",
  "requestId": "req_011CbJ8yZBSWgw12VMLtmq63",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8fbaea73-442c-4f32-8156-6643eef5f660",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TGrqyyq9p1N6VL5gDh5veh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18958,
      "cache_read_input_tokens": 0,
      "output_tokens": 292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18958
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 292,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18958,
            "ephemeral_1h_input_tokens": 0
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

_source line 8 · 2026-05-22T19:12:18.397Z_

<details><summary>↩ Tool result · `toolu_01M1XauRsxykaxTysaLinHNp`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_plan_011_semi_synthetic_20260520T213716_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_plan_016_within_subject_injection_20260520T223139.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_plan_016_within_subject_injection_20260520T223139_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_plan_034_multi_subject_injection_20260521T154505_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r19_semisynthetic_gradient_20260522T184822.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r19_semisynthetic_gradient_20260522T184822_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_plan_034_multi_subject_injection_20260521T154505.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_plan_011_semi_synthetic_20260520T213716.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/chats/worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/chats/worker_code_plan_004_step2_gsm8k_semi_synthetic_20260521T005157.lock
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/checkpoints/plan_011_semi_synthetic_validation_DONE_20260520T215454.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/checkpoints/plan_016_within_subject_semi_synthetic_RUNNING_20260520T223718.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/checkpoints/plan_016_within_subject_semi_synthetic_RUNNING_20260520T223726.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/checkpoints/plan_034_multi_subject_injection_PREPARING_20260521T160217.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/checkpoints/plan_016_within_subject_semi_synthetic_QUEUED_20260520T223707.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/checkpoints/plan_011_semi_synthetic_validation_ALLOCATED_20260520T215140.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/checkpoints/plan_016_within_subject_semi_synthetic_DONE_20260520T223739.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/checkpoints/plan_034_multi_subject_injection_ANALYZING_20260521T160250.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fbaea73-442c-4f32-8156-6643eef5f660",
  "isSidechain": true,
  "promptId": "479d2b2e-c441-4faa-85be-98bfaeb246ff",
  "agentId": "a0a57fb98c617a285",
  "type": "user",
  "uuid": "1580b09f-6eb7-474f-80a1-f938b5f2da33",
  "sourceToolAssistantUUID": "8fbaea73-442c-4f32-8156-6643eef5f660",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-22T19:12:19.569Z_

Great! I found the main file. Let me read it thoroughly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1580b09f-6eb7-474f-80a1-f938b5f2da33",
  "isSidechain": true,
  "agentId": "a0a57fb98c617a285",
  "requestId": "req_011CbJ8ykdWqzmy2FWvHiATH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3fdf43ea-0b1d-4365-b87c-995e45b27871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CQm8Q6g6NNaYu4GGQZwV9Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 18958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2620,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-22T19:12:19.893Z_

<details open><summary>🔧 Tool call — Read · `toolu_01L647qFvvZYA58nAum9QjbX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3fdf43ea-0b1d-4365-b87c-995e45b27871",
  "isSidechain": true,
  "agentId": "a0a57fb98c617a285",
  "requestId": "req_011CbJ8ykdWqzmy2FWvHiATH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cf847c93-66a7-477f-a8fe-fdbc5e908231",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CQm8Q6g6NNaYu4GGQZwV9Y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2620,
      "cache_read_input_tokens": 18958,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2620
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 120,
          "cache_read_input_tokens": 18958,
          "cache_creation_input_tokens": 2620,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2620,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-22T19:12:19.913Z_

<details><summary>↩ Tool result · `toolu_01L647qFvvZYA58nAum9QjbX`</summary>

```text
1	"""
2	R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection
3	Tests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.
4	"""
5	
6	import numpy as np
7	import pandas as pd
8	from scipy import sparse, stats
9	from scipy.stats import chi2 as chi2_dist
10	import time, os, sys
11	
12	ROOT = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
13	OUT = os.path.join(ROOT, "r19_semisynthetic_gradient")
14	
15	N_SEEDS = 5
16	N_STRATA = 5
17	FOC_INJECT_FRAC = 0.30
18	ITEM_INJECT_FRAC = 0.24
19	
20	# ════════════════════════════════════════════════════════════════════════════
21	#  VECTORIZED MH-DIF — returns per-item results
22	# ════════════════════════════════════════════════════════════════════════════
23	def mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):
24	    """Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction."""
25	    n_ref, J = X_ref.shape
26	    n_foc = X_foc.shape[0]
27	
28	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
29	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
30	    s_all = np.concatenate([tot_ref, tot_foc])
31	
32	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
33	    n_bins = len(edges) - 1
34	    if n_bins < 1:
35	        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)
36	
37	    k_ref = np.digitize(tot_ref, edges[1:-1])
38	    k_foc = np.digitize(tot_foc, edges[1:-1])
39	
40	    n1 = np.zeros(n_bins, dtype=np.float64)
41	    n0 = np.zeros(n_bins, dtype=np.float64)
42	    A = np.zeros((n_bins, J), dtype=np.float64)
43	    C_mat = np.zeros((n_bins, J), dtype=np.float64)
44	
45	    for k in range(n_bins):
46	        mr = (k_ref == k)
47	        mf = (k_foc == k)
48	        n1[k] = mr.sum()
49	        n0[k] = mf.sum()
50	        if mr.any():
51	            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)
52	        if mf.any():
53	            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)
54	
55	    B = n1[:, None] - A
56	    D = n0[:, None] - C_mat
57	    Nk = (n1 + n0)[:, None]
58	    m1 = A + C_mat
59	    m0 = B + D
60	
61	    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &
62	             (Nk > 1) & (m1 > 0) & (m0 > 0))
63	
64	    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
65	    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)
66	
67	    finite_mask = (Rj > 0) & (Sj > 0)
68	
69	    with np.errstate(divide="ignore", invalid="ignore"):
70	        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
71	
72	    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
73	    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)
74	
75	    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
76	    sum_var = np.where(
77	        valid,
78	        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),
79	        0,
80	    ).sum(axis=0)
81	
82	    chi2_j = np.where(
83	        sum_var > 0,
84	        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
85	        0,
86	    )
87	    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)
88	
89	    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)
90	
91	    return delta_j, pval_j, is_c
92	
93	
94	# ════════════════════════════════════════════════════════════════════════════
95	#  LOAD DATA
96	# ════════════════════════════════════════════════════════════════════════════
97	print("Loading data...")
98	rm = np.load(f"{ROOT}/response_matrix.npz")
99	X_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))
100	idx = np.load(f"{ROOT}/response_matrix_index.npz", allow_pickle=True)
101	model_names = idx['model_names']
102	item_ids = idx['item_ids']
103	
104	meta = pd.read_csv(f"{ROOT}/model_metadata.csv")
105	name_to_row = {n: i for i, n in enumerate(model_names)}
106	
107	ref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values
108	foc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values
109	
110	ref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])
111	foc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])
112	
113	N_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)
114	N_inject_models = int(N_foc * FOC_INJECT_FRAC)
115	N_inject_items = int(J * ITEM_INJECT_FRAC)
116	
117	print(f"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}")
118	print(f"  Injection targets: {N_inject_models} models, {N_inject_items} items")
119	
120	# Densify the ref/foc submatrices
121	X_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)
122	X_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)
123	
124	# Ref cohort accuracy per item (= item difficulty proxy)
125	item_difficulty = X_ref_base.mean(axis=0)  # shape (J,)
126	
127	print(f"  Item difficulty: mean={item_difficulty.mean():.3f}, "
128	      f"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}")
129	
130	# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)
131	item_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])
132	unique_subjects = np.unique(item_subjects)
133	print(f"  Unique subjects: {len(unique_subjects)}")
134	
135	
136	# ════════════════════════════════════════════════════════════════════════════
137	#  INJECTION SCHEMES
138	# ════════════════════════════════════════════════════════════════════════════
139	def inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):
140	    """Capability-like: injection probability ∝ difficulty (easy items more likely flipped)."""
141	    X = X_foc.copy()
142	    n_flipped = 0
143	    for j in inject_item_idx:
144	        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
145	        for i in np.where(inject_model_mask)[0]:
146	            if X[i, j] == 0 and rng.random() < p_inject:
147	                X[i, j] = 1
148	                n_flipped += 1
149	    return X, n_flipped
150	
151	
152	def inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):
153	    """Contamination-like: uniform injection probability, restricted to 5 random subjects."""
154	    X = X_foc.copy()
155	    n_flipped = 0
156	    for j in inject_item_idx:
157	        for i in np.where(inject_model_mask)[0]:
158	            if X[i, j] == 0 and rng.random() < p_const:
159	                X[i, j] = 1
160	                n_flipped += 1
161	    return X, n_flipped
162	
163	
164	def inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,
165	                    item_diff, rng, p_const=0.5):
166	    """Mixed: half items use scheme A, half use scheme B."""
167	    X = X_foc.copy()
168	    n_flipped = 0
169	    # Scheme A half
170	    for j in inject_item_idx_a:
171	        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
172	        for i in np.where(inject_model_mask)[0]:
173	            if X[i, j] == 0 and rng.random() < p_inject:
174	                X[i, j] = 1
175	                n_flipped += 1
176	    # Scheme B half
177	    for j in inject_item_idx_b:
178	        for i in np.where(inject_model_mask)[0]:
179	            if X[i, j] == 0 and rng.random() < p_const:
180	                X[i, j] = 1
181	                n_flipped += 1
182	    return X, n_flipped
183	
184	
185	# ════════════════════════════════════════════════════════════════════════════
186	#  BASELINE (no injection)
187	# ════════════════════════════════════════════════════════════════════════════
188	print("\n=== Baseline (no injection) ===")
189	delta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)
190	c_idx_base = np.where(is_c_base)[0]
191	rho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])
192	n_c_base = is_c_base.sum()
193	# δ > 0 = focal-favoring, δ < 0 = ref-favoring
194	n_focal_base = (is_c_base & (delta_base > 0)).sum()
195	n_ref_base = (is_c_base & (delta_base < 0)).sum()
196	print(f"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, "
197	      f"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}")
198	
199	
200	# ════════════════════════════════════════════════════════════════════════════
201	#  RUN EXPERIMENTS
202	# ════════════════════════════════════════════════════════════════════════════
203	print("\n=== Running experiments ===")
204	results = []
205	t0 = time.time()
206	
207	for seed in range(1, N_SEEDS + 1):
208	    rng = np.random.RandomState(seed * 42)
209	
210	    # Select injection models and items (shared across schemes within seed)
211	    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)
212	    inject_model_mask = np.zeros(N_foc, dtype=bool)
213	    inject_model_mask[inject_model_idx] = True
214	
215	    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)
216	
217	    # Scheme B: select 5 random subjects, pick injection items from those subjects
218	    selected_subjects = rng.choice(unique_subjects, 5, replace=False)
219	    subject_mask = np.isin(item_subjects, selected_subjects)
220	    subject_item_pool = np.where(subject_mask)[0]
221	    n_b_items = min(N_inject_items, len(subject_item_pool))
222	    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)
223	
224	    # Scheme C: split A items in half
225	    half = N_inject_items // 2
226	    inject_item_idx_c_a = inject_item_idx_all[:half]
227	    # For scheme C's B half, pick from 5 random subjects
228	    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)
229	    subject_mask_c = np.isin(item_subjects, selected_subjects_c)
230	    subject_pool_c = np.where(subject_mask_c)[0]
231	    # Exclude items already used by A half
232	    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)
233	    n_c_b = min(half, len(subject_pool_c))
234	    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)
235	
236	    schemes = {
237	        'A_capability': lambda: inject_scheme_a(
238	            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),
239	        'B_contamination': lambda: inject_scheme_b(
240	            X_foc_base, inject_model_mask, inject_item_idx_b, rng),
241	        'C_mixed': lambda: inject_scheme_c(
242	            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,
243	            item_difficulty, rng),
244	    }
245	
246	    for scheme_name, inject_fn in schemes.items():
247	        t1 = time.time()
248	
249	        X_foc_inj, n_flipped = inject_fn()
250	
251	        # Determine which items were injected for this scheme
252	        if scheme_name == 'A_capability':
253	            injected_items = set(inject_item_idx_all)
254	        elif scheme_name == 'B_contamination':
255	            injected_items = set(inject_item_idx_b)
256	        else:  # C_mixed
257	            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)
258	
259	        # Run MH-DIF
260	        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)
261	
262	        # Delta change from baseline (isolates injection effect)
263	        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive
264	        ddelta = delta_j - delta_base
265	
266	        # C% among all / injected / non-injected items
267	        inj_arr = np.array(sorted(injected_items))
268	        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))
269	        c_pct_all = is_c.sum() / J * 100
270	        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0
271	        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100
272	
273	        # ρ(difficulty, δ) among all C items
274	        c_idx = np.where(is_c)[0]
275	        rho_all = np.nan
276	        if len(c_idx) >= 3:
277	            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])
278	
279	        # ρ(difficulty, δ) among injected C items
280	        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)
281	        c_inj_idx = np.where(c_inj_mask)[0]
282	        rho_inj = np.nan
283	        if len(c_inj_idx) >= 3:
284	            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])
285	
286	        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal
287	        rho_ddelta_inj = np.nan
288	        if len(inj_arr) >= 3:
289	            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])
290	
291	        # ρ(difficulty, Δδ) among all items
292	        rho_ddelta_all = np.nan
293	        if J >= 3:
294	            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)
295	
296	        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring
297	        n_c_total = is_c.sum()
298	        n_focal_favoring = (is_c & (delta_j > 0)).sum()
299	        n_ref_favoring = (is_c & (delta_j < 0)).sum()
300	        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0
301	
302	        # Direction among injected C items
303	        n_c_inj = c_inj_mask.sum()
304	        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()
305	        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0
306	
307	        # Newly flagged items (C after injection but not in baseline)
308	        newly_c = is_c & ~is_c_base
309	        n_newly_c = newly_c.sum()
310	        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)
311	        n_newly_c_inj = newly_c_inj.sum()
312	
313	        # Mean Δδ among injected items (injection effect magnitude)
314	        mean_ddelta_inj = ddelta[inj_arr].mean()
315	
316	        # Per-quintile analysis
317	        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])
318	        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])
319	        quintile_data = {}
320	        for q in range(5):
321	            q_mask = (quintile_labels == q)
322	            q_items = np.where(q_mask)[0]
323	            q_inj_items = np.intersect1d(q_items, inj_arr)
324	            q_c = is_c[q_items].sum()
325	            q_total = len(q_items)
326	            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0
327	            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()
328	            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0
329	            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0
330	            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0
331	            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0
332	            quintile_data[f'q{q+1}_c_pct'] = q_c_pct
333	            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal
334	            quintile_data[f'q{q+1}_n_c'] = q_c
335	            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj
336	            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)
337	            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta
338	
339	        elapsed = time.time() - t1
340	        row = dict(
341	            scheme=scheme_name, seed=seed,
342	            n_inject_models=N_inject_models,
343	            n_inject_items=len(injected_items),
344	            n_flipped=n_flipped,
345	            c_pct_all=c_pct_all,
346	            c_pct_inj=c_pct_inj,
347	            c_pct_noninj=c_pct_noninj,
348	            n_c_total=n_c_total,
349	            n_c_inj=n_c_inj,
350	            rho_all=rho_all,
351	            rho_inj=rho_inj,
352	            rho_ddelta_inj=rho_ddelta_inj,
353	            rho_ddelta_all=rho_ddelta_all,
354	            pct_focal=pct_focal,
355	            pct_focal_inj=pct_focal_inj,
356	            n_focal_favoring=n_focal_favoring,
357	            n_ref_favoring=n_ref_favoring,
358	            n_newly_c=n_newly_c,
359	            n_newly_c_inj=n_newly_c_inj,
360	            mean_ddelta_inj=mean_ddelta_inj,
361	            elapsed_sec=elapsed,
362	        )
363	        row.update(quintile_data)
364	        results.append(row)
365	        print(f"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, "
366	              f"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, "
367	              f"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s")
368	
369	total_time = time.time() - t0
370	print(f"\nTotal time: {total_time:.0f}s")
371	
372	
373	# ════════════════════════════════════════════════════════════════════════════
374	#  SAVE RESULTS
375	# ════════════════════════════════════════════════════════════════════════════
376	df = pd.DataFrame(results)
377	df.to_csv(os.path.join(OUT, "semisynthetic_results.csv"), index=False)
378	print(f"\nSaved: semisynthetic_results.csv ({len(df)} rows)")
379	
380	
381	# ════════════════════════════════════════════════════════════════════════════
382	#  GENERATE REPORT
383	# ════════════════════════════════════════════════════════════════════════════
384	report_lines = ["# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\n"]
385	report_lines.append(f"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n")
386	report_lines.append(f"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), "
387	                    f"{N_foc} foc models (2024), {J} items\n")
388	report_lines.append(f"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), "
389	                    f"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\n")
390	
391	report_lines.append(f"\n## Baseline (no injection)\n")
392	report_lines.append(f"- C%: {n_c_base/J*100:.2f}%")
393	report_lines.append(f"- ρ(difficulty, δ_MH) among C: {rho_base:.3f}")
394	report_lines.append(f"- % focal-favoring (δ>0): {n_focal_base/n_c_base*100:.1f}%")
395	report_lines.append(f"- % ref-favoring (δ<0): {n_ref_base/n_c_base*100:.1f}%")
396	report_lines.append(f"- N DIF-C: {n_c_base}")
397	
398	for scheme in ['A_capability', 'B_contamination', 'C_mixed']:
399	    sub = df[df['scheme'] == scheme]
400	    report_lines.append(f"\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\n")
401	
402	    report_lines.append(f"| Metric | Mean ± SD |")
403	    report_lines.append(f"|--------|-----------|")
404	    report_lines.append(f"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |")
405	    report_lines.append(f"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |")
406	    report_lines.append(f"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |")
407	    report_lines.append(f"| ρ(diff, δ) all C | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |")
408	    report_lines.append(f"| ρ(diff, δ) injected C | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} |")
409	    report_lines.append(f"| **ρ(diff, Δδ) injected items** | **{sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f}** |")
410	    report_lines.append(f"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |")
411	    report_lines.append(f"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |")
412	    report_lines.append(f"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |")
413	    report_lines.append(f"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |")
414	    report_lines.append(f"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |")
415	    report_lines.append(f"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |")
416	    report_lines.append(f"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |")
417	    report_lines.append(f"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |")
418	    report_lines.append(f"| Items injected | {sub['n_inject_items'].mean():.0f} |")
419	
420	    report_lines.append(f"\n### Quintile Breakdown\n")
421	    report_lines.append(f"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |")
422	    report_lines.append(f"|----------|----------|----------|---------|---------------|-----|-------|")
423	    for q in range(1, 6):
424	        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}
425	        if cols['c_pct'] in sub.columns:
426	            report_lines.append(
427	                f"| Q{q} | {sub[cols['c_pct']].mean():.1f} | "
428	                f"{sub[cols['c_pct_inj']].mean():.1f} | "
429	                f"{sub[cols['pct_focal']].mean():.1f} | "
430	                f"{sub[cols['mean_ddelta']].mean():.3f} | "
431	                f"{sub[cols['n_c']].mean():.0f} | "
432	                f"{sub[cols['n_inj']].mean():.0f} |")
433	
434	report_lines.append(f"\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\n")
435	report_lines.append("Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\n")
436	report_lines.append(f"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |")
437	report_lines.append(f"|--------|---------------------|-----------------|----------|")
438	for scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),
439	                         ('B_contamination', '≈ 0 (uniform)'),
440	                         ('C_mixed', 'intermediate')]:
441	    sub = df[df['scheme'] == scheme]
442	    report_lines.append(f"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | "
443	                       f"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |")
444	
445	report_lines.append(f"\n## Interpretation\n")
446	report_lines.append("**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. "
447	                    "Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.\n")
448	report_lines.append("### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures\n")
449	report_lines.append("1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. "
450	                    "Injection probability ∝ item accuracy → easy items receive more flips → "
451	                    "larger focal-favoring Δδ on easy items. Strong positive correlation.")
452	report_lines.append("2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). "
453	                    "Uniform p=0.5 injection gives equal probability per response, but hard items "
454	                    "have more 0→1 flippable responses (ceiling effect). "
455	                    "Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.")
456	report_lines.append("3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, "
457	                    "as expected from mixing both injection mechanisms.\n")
458	report_lines.append("### Ceiling effect insight\n")
459	report_lines.append("The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability "
460	                    "does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → "
461	                    "small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. "
462	                    "This ceiling effect is an inherent property of binary response matrices and means "
463	                    "the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' "
464	                    "but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.\n")
465	report_lines.append("### Discriminability\n")
466	report_lines.append("- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds")
467	report_lines.append("- A vs C separation: Δρ ≈ 0.38, clear but smaller")
468	report_lines.append("- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone")
469	
470	report_text = "\n".join(report_lines) + "\n"
471	
472	with open(os.path.join(OUT, "semisynthetic_gradient_report.md"), "w") as f:
473	    f.write(report_text)
474	
475	print(f"Saved: semisynthetic_gradient_report.md")
476	print("\n" + report_text)
477	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf847c93-66a7-477f-a8fe-fdbc5e908231",
  "isSidechain": true,
  "promptId": "479d2b2e-c441-4faa-85be-98bfaeb246ff",
  "agentId": "a0a57fb98c617a285",
  "type": "user",
  "uuid": "4f60810b-f3d9-4813-935f-bdc299bc9af1",
  "sourceToolAssistantUUID": "cf847c93-66a7-477f-a8fe-fdbc5e908231",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-22T19:12:39.123Z_

Perfect! I have the complete code. Let me now provide you with detailed answers to all five questions based on the implementation:

## Summary of Semi-Synthetic Gradient Experiment

### 1. **How "difficulty" is defined**

**Difficulty = proportion correct (higher = easier)**

Line 125:
```python
item_difficulty = X_ref_base.mean(axis=0)  # shape (J,)
```

This is the mean accuracy of the reference cohort (2023 models) per item. Higher values mean easier items (more correct responses), which is why the code uses the term "difficulty" (standard IRT convention where difficulty is often inversely labeled, but here it's directly accuracy).

---

### 2. **How Δδ is computed**

**Δδ = δ_after - δ_baseline (Mantel-Haenszel Δ_MH)**

Lines 262-264:
```python
delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)

# Delta change from baseline (isolates injection effect)
# δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive
ddelta = delta_j - delta_base
```

The MH-DIF statistic δ_MH is computed per item in the `mh_dif_vec()` function (line 70):
```python
delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
```

This is the standard Mantel-Haenszel log-odds formula. Then Δδ isolates the injection-induced shift by subtracting the baseline delta.

---

### 3. **Scheme A "capability-like" injection**

**Injection probability is PROPORTIONAL to item accuracy (easy items targeted)**

Lines 139-149:
```python
def inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):
    """Capability-like: injection probability ∝ difficulty (easy items more likely flipped)."""
    X = X_foc.copy()
    n_flipped = 0
    for j in inject_item_idx:
        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
        for i in np.where(inject_model_mask)[0]:
            if X[i, j] == 0 and rng.random() < p_inject:
                X[i, j] = 1
                n_flipped += 1
    return X, n_flipped
```

The key line is:
```python
p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
```

This is a **linear scaling**:
- When `item_diff[j] = 0.2` (hard item): `p_inject = 0`
- When `item_diff[j] = 0.8` (easy item): `p_inject = 1`
- For intermediate difficulties, probability scales linearly

**Interpretation**: Easy items (high accuracy) have HIGH injection probability. Hard items have LOW injection probability. This simulates a "capability" pattern where easier items are more likely to be affected.

---

### 4. **Scheme B "contamination-like"**

**Uniform p=0.5 for ALL items (with subject restriction)**

Lines 152-161:
```python
def inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):
    """Contamination-like: uniform injection probability, restricted to 5 random subjects."""
    X = X_foc.copy()
    n_flipped = 0
    for j in inject_item_idx:
        for i in np.where(inject_model_mask)[0]:
            if X[i, j] == 0 and rng.random() < p_const:
                X[i, j] = 1
                n_flipped += 1
    return X, n_flipped
```

The injection uses **constant p=0.5** for every item-model pair where the response is 0 (needs flipping). However, there's a restriction applied earlier (lines 218-222):

```python
# Scheme B: select 5 random subjects, pick injection items from those subjects
selected_subjects = rng.choice(unique_subjects, 5, replace=False)
subject_mask = np.isin(item_subjects, selected_subjects)
subject_item_pool = np.where(subject_mask)[0]
n_b_items = min(N_inject_items, len(subject_item_pool))
inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)
```

So Scheme B targets items from **5 random MMLU subjects** with **uniform p=0.5**, not truly "all items." The contamination is domain-restricted.

**Important insight from the report** (lines 452-455): Despite uniform p=0.5, the correlation ρ(diff, Δδ) is **≈ −0.52, NOT ≈ 0**. This is due to **ceiling effects**: hard items have more 0s to flip, so they accumulate larger Δδ values, creating a negative correlation with difficulty.

---

### 5. **How ρ(diff, Δδ) is computed**

**Spearman correlation between item_difficulty and ddelta for INJECTED ITEMS ONLY**

Lines 286-289:
```python
# ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal
rho_ddelta_inj = np.nan
if len(inj_arr) >= 3:
    rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])
```

And for all items (lines 291-294):
```python
# ρ(difficulty, Δδ) among all items
rho_ddelta_all = np.nan
if J >= 3:
    rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)
```

**The exact two arrays being correlated**:
- **X-axis**: `item_difficulty[inj_arr]` — reference cohort accuracy for each injected item
- **Y-axis**: `ddelta[inj_arr]` — MH-DIF shift (δ_after - δ_baseline) for each injected item

This computes the Spearman rank correlation (scipy.stats.spearmanr) between these two vectors. The KEY metric reported is **ρ(diff, Δδ) for injected items**, which isolates the injection signal by only looking at items where injection actually occurred.

---

## Final Summary Table

| Question | Answer |
|----------|--------|
| **1. Difficulty definition** | Proportion correct (higher = easier), computed as mean accuracy of ref cohort |
| **2. Δδ computation** | δ_after - δ_baseline, where δ = MH log-odds ratio (-2.35 × log(Rj/Sj)) |
| **3. Scheme A injection** | Probability ∝ item accuracy: p = max(0, min(1, (accuracy - 0.2) / 0.6)). Easy items targeted. |
| **4. Scheme B injection** | Uniform p=0.5 for all items in 5 random MMLU subjects, BUT produces negative ρ due to ceiling effects |
| **5. ρ(diff, Δδ) computation** | Spearman rank correlation of (item_difficulty[injected_items], ddelta[injected_items]) |

The experiment reveals that **ρ(diff, Δδ)** is a powerful discriminator:
- **Scheme A**: ρ ≈ +0.77 (positive, easy items shift more focal)
- **Scheme B**: ρ ≈ −0.52 (negative, hard items shift more due to ceiling)
- **Scheme C**: ρ ≈ +0.39 (intermediate, mixed mechanism)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4f60810b-f3d9-4813-935f-bdc299bc9af1",
  "isSidechain": true,
  "agentId": "a0a57fb98c617a285",
  "requestId": "req_011CbJ8ysPKRkHHNnUzHWBe1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0dd62c67-b952-4da8-b85b-36ce084ff342",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/.claude/sessions/reviewer_430cd31d",
  "sessionId": "409e18c4-561a-427e-a5fd-fc805d831b1d",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "mutable-booping-popcorn",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LXq4pPbhhKGyMEXp6yb1g8",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 10128,
      "cache_read_input_tokens": 21578,
      "output_tokens": 2058,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10128
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2058,
          "cache_read_input_tokens": 21578,
          "cache_creation_input_tokens": 10128,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10128,
            "ephemeral_1h_input_tokens": 0
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
