# Research conversation: Find and read the MH-DIF implementation in the plan_028 artifacts directory under /home/ubuntu/.agent-ml-research-idea_g

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 1
- **Tool calls:** 10
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a19a8e4e5d748890c.jsonl`
- **Structured JSON:** [`cd6620a8dca976831a7f.json`](../../sessions/cd/cd6620a8dca976831a7f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

31 recorded events

### User

_source line 1 · 2026-05-21T12:35:35.143Z_

Find and read the MH-DIF implementation in the plan_028 artifacts directory under /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028/. I need to understand:
1. The complete mh_dif function implementation
2. How benchmarks are loaded (data loading patterns)
3. How models are split into reference/focal groups (2023 vs 2024 cohorts)
4. How C% is calculated from MH-DIF results
5. The overall script structure

Search broadly - the code might be in .py files or .ipynb notebooks. Read the full files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "aa84ba20-f294-4732-a323-b027b9cfb34f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-21T12:35:36.676Z_

I'll help you find and analyze the MH-DIF implementation in the plan_028 artifacts directory. Let me start by exploring the structure and searching for relevant files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa84ba20-f294-4732-a323-b027b9cfb34f",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivCveHA3BCbPjbxRWi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "54d0c3c2-0bcf-4599-bf80-9459d635ec9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CMyHcZCBYdir8c2AeVj9tY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15550,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15550,
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

_source line 3 · 2026-05-21T12:35:36.854Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0149GkD4gZfCUapG2Fb3VmeW`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028 -type f \\( -name \"*.py\" -o -name \"*.ipynb\" \\) | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54d0c3c2-0bcf-4599-bf80-9459d635ec9f",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivCveHA3BCbPjbxRWi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35277f99-8773-489b-8bc5-5ab7ea2def4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CMyHcZCBYdir8c2AeVj9tY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15550,
      "cache_read_input_tokens": 0,
      "output_tokens": 154,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15550
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 154,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15550,
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

_source line 4 · 2026-05-21T12:35:37.049Z_

<details><summary>↩ Tool result · `toolu_0149GkD4gZfCUapG2Fb3VmeW`</summary>

```text
find: ‘/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028’: No such file or directory
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35277f99-8773-489b-8bc5-5ab7ea2def4b",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "4693d5f5-85b6-461d-9261-e6ebfadbb15b",
  "sourceToolAssistantUUID": "35277f99-8773-489b-8bc5-5ab7ea2def4b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-21T12:35:40.834Z_

Let me check the correct path structure:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4693d5f5-85b6-461d-9261-e6ebfadbb15b",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivLaGvnfTFSjejB5Mb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "879e0c5b-a533-4091-86bb-cfc7ea7d4aa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Une4s3Vd4PvYUMh85oNWZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 15550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1047,
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

_source line 6 · 2026-05-21T12:35:40.895Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01UZ3zD6rkmHM7o6CVsswkN7`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/ 2>&1 | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "879e0c5b-a533-4091-86bb-cfc7ea7d4aa9",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivLaGvnfTFSjejB5Mb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9ab662ac-bb61-4688-a458-61a2a3217a71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Une4s3Vd4PvYUMh85oNWZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1047,
      "cache_read_input_tokens": 15550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1047,
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

### Tool result

_source line 7 · 2026-05-21T12:35:40.966Z_

<details><summary>↩ Tool result · `toolu_01UZ3zD6rkmHM7o6CVsswkN7`</summary>

```text
total 56424
drwxr-xr-x 39 ubuntu ubuntu     4096 May 21 10:13 .
drwxr-xr-x 10 ubuntu ubuntu     4096 May 21 12:34 ..
drwxr-xr-x  2 ubuntu ubuntu     4096 May 20 18:32 __pycache__
drwxr-xr-x  7 ubuntu ubuntu     4096 May 21 04:11 _project
-rw-r--r--  1 ubuntu ubuntu     7853 May 20 23:48 artifacts_qc_report.md
-rw-r--r--  1 ubuntu ubuntu    20975 May 20 20:48 build_response_matrix.py
-rw-r--r--  1 ubuntu ubuntu    16120 May 20 18:32 dif_diagnostic.py
-rw-r--r--  1 ubuntu ubuntu        0 May 20 18:39 dif_diagnostic_output.log
-rw-r--r--  1 ubuntu ubuntu    23783 May 20 18:39 dif_diagnostic_pvalue_dist.pdf
-rw-r--r--  1 ubuntu ubuntu     2728 May 20 18:39 dif_diagnostic_tpr_comparison.csv
-rw-r--r--  1 ubuntu ubuntu    21799 May 20 19:00 dif_phase2_param_distribution.pdf
-rw-r--r--  1 ubuntu ubuntu    34622 May 20 19:27 dif_phase2_power_curves.pdf
-rw-r--r--  1 ubuntu ubuntu     1956 May 20 19:27 dif_phase2_results.csv
-rw-r--r--  1 ubuntu ubuntu    23911 May 20 18:59 dif_phase2_simulation.py
-rw-r--r--  1 ubuntu ubuntu    24175 May 20 18:36 dif_power_curves.pdf
-rw-r--r--  1 ubuntu ubuntu     3114 May 20 18:36 dif_power_results.csv
-rw-r--r--  1 ubuntu ubuntu    17493 May 20 17:40 dif_power_simulation.py
drwxr-xr-x 13 ubuntu ubuntu     4096 May 21 12:24 dream_reports
-rw-r--r--  1 ubuntu ubuntu    13507 May 20 23:47 experiment_summary.md
-rw-r--r--  1 ubuntu ubuntu     3458 May 20 20:40 irt_scale_analysis.json
-rw-r--r--  1 ubuntu ubuntu     5362 May 20 20:40 irt_scale_analysis.md
-rw-r--r--  1 ubuntu ubuntu  1528143 May 20 20:57 item_metadata.csv
-rw-r--r--  1 ubuntu ubuntu    25931 May 20 23:49 literature_survey_d011.md
-rw-r--r--  1 ubuntu ubuntu    83378 May 21 10:46 manifest.yaml
-rw-r--r--  1 ubuntu ubuntu      451 May 20 19:51 metabench_cohort_analysis.csv
-rw-r--r--  1 ubuntu ubuntu  1312294 May 20 19:46 metabench_ctt_stats.csv
drwxr-xr-x  3 ubuntu ubuntu     4096 May 20 19:38 metabench_data
-rw-r--r--  1 ubuntu ubuntu     5088 May 20 20:53 metabench_data_summary.md
-rw-r--r--  1 ubuntu ubuntu    20313 May 20 19:50 metabench_explore.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ab662ac-bb61-4688-a458-61a2a3217a71",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "c57191f3-66bb-49a2-9420-6e930179f7d8",
  "sourceToolAssistantUUID": "9ab662ac-bb61-4688-a458-61a2a3217a71",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-21T12:35:42.318Z_

Let me check for plan_028 subdirectories:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57191f3-66bb-49a2-9420-6e930179f7d8",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivdU23tC1oo9fQpdcv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ce4bd1a2-41cd-4f14-b082-a5003bb22936",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XNFhkGiQu5tTUPbDMHizFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 16597,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1088,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 9 · 2026-05-21T12:35:42.989Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R47sxBqcaAzP8bjeH7UKY3`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -type d -name \"*plan*\" 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce4bd1a2-41cd-4f14-b082-a5003bb22936",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivdU23tC1oo9fQpdcv",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "416e60cf-7470-466a-8437-307e9d8b40cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XNFhkGiQu5tTUPbDMHizFA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 16597,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1088
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 112,
          "cache_read_input_tokens": 16597,
          "cache_creation_input_tokens": 1088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1088,
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

_source line 10 · 2026-05-21T12:35:43.050Z_

<details><summary>↩ Tool result · `toolu_01R47sxBqcaAzP8bjeH7UKY3`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_supplement
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_020
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_021
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_013_q3_local_independence
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_019
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012_irt_theta_conditioning
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_018
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_010
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_013
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017_supplement
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_015
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_013_supplement
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_027_temporal_overlap
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_012
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_023
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_024
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_029_permutation_null
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_030_odds_ratio
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001b
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001_real_data_dif_mmlu
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_011_semi_synthetic_validation
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_017
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_022
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_016_within_subject_semi_synthetic
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "416e60cf-7470-466a-8437-307e9d8b40cb",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "beb18202-1805-484d-8656-fe5fd55fb232",
  "sourceToolAssistantUUID": "416e60cf-7470-466a-8437-307e9d8b40cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T12:35:44.911Z_

Good! I found plan_028_multi_bench_dif. Let me explore its contents:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beb18202-1805-484d-8656-fe5fd55fb232",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivnAQCSgEonvMHdTiq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5b0965c5-2514-45a9-922b-50d1ebce0ad3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EmdPSPEv9yGKAfnzQMDEaa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1396,
      "cache_read_input_tokens": 17685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1396,
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

_source line 12 · 2026-05-21T12:35:45.187Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RaCBZEWTrgEkKkDvdLeTk8`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b0965c5-2514-45a9-922b-50d1ebce0ad3",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivnAQCSgEonvMHdTiq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8a7c4cfb-b53a-4a23-8156-daf00535b5f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EmdPSPEv9yGKAfnzQMDEaa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1396,
      "cache_read_input_tokens": 17685,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1396
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 122,
          "cache_read_input_tokens": 17685,
          "cache_creation_input_tokens": 1396,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1396,
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

_source line 13 · 2026-05-21T12:35:45.296Z_

<details><summary>↩ Tool result · `toolu_01RaCBZEWTrgEkKkDvdLeTk8`</summary>

```text
total 1388
drwxr-xr-x  5 ubuntu ubuntu    4096 May 21 10:53 .
drwxr-xr-x 39 ubuntu ubuntu    4096 May 21 10:13 ..
-rw-r--r--  1 ubuntu ubuntu  116507 May 21 10:52 arc_dif_results.csv
-rw-r--r--  1 ubuntu ubuntu     254 May 21 10:52 arc_ets_summary.csv
drwxr-xr-x  2 ubuntu ubuntu    4096 May 21 10:46 data
-rw-r--r--  1 ubuntu ubuntu 1013269 May 21 10:53 hellaswag_dif_results.csv
-rw-r--r--  1 ubuntu ubuntu     258 May 21 10:53 hellaswag_ets_summary.csv
drwxr-xr-x  2 ubuntu ubuntu    4096 May 21 10:46 intermediate
-rw-r--r--  1 ubuntu ubuntu    1780 May 21 10:53 multi_bench_dif_report.md
-rw-r--r--  1 ubuntu ubuntu     372 May 21 10:53 multi_bench_summary.csv
-rw-r--r--  1 ubuntu ubuntu     372 May 21 10:52 multi_bench_summary.csv.bak
-rw-r--r--  1 ubuntu ubuntu   17710 May 21 10:52 plan_028_multi_bench_dif.py
drwxr-xr-x  2 ubuntu ubuntu    4096 May 21 10:46 report
-rw-r--r--  1 ubuntu ubuntu       0 May 21 10:31 run.log
-rw-r--r--  1 ubuntu ubuntu   81969 May 21 10:53 truthfulqa_dif_results.csv
-rw-r--r--  1 ubuntu ubuntu     290 May 21 10:53 truthfulqa_ets_summary.csv
-rw-r--r--  1 ubuntu ubuntu  127165 May 21 10:53 winogrande_dif_results.csv
-rw-r--r--  1 ubuntu ubuntu     324 May 21 10:53 winogrande_ets_summary.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a7c4cfb-b53a-4a23-8156-daf00535b5f7",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "4d7dcc2f-69a5-42c8-a816-218f8e27fea1",
  "sourceToolAssistantUUID": "8a7c4cfb-b53a-4a23-8156-daf00535b5f7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-21T12:35:46.974Z_

Perfect! Now let me search for MH-DIF related code files and read the main script:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d7dcc2f-69a5-42c8-a816-218f8e27fea1",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivxJ73cuo67dGx1sii",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0a5cd6e4-e5da-463a-aade-5fc915c2f6fb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N7reTKnjTWMHY52eDHcWWK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 19081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 732,
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

_source line 15 · 2026-05-21T12:35:47.502Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Rr29N7QEbXqjQnziwmZQja`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -type f \\( -name \"*mh*dif*\" -o -name \"*dif*.py\" -o -name \"*dif*.ipynb\" \\) 2>&1 | grep -E \"\\.(py|ipynb)$\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a5cd6e4-e5da-463a-aade-5fc915c2f6fb",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFivxJ73cuo67dGx1sii",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d7e2475f-1650-41cb-94fd-28ddf93a537b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01N7reTKnjTWMHY52eDHcWWK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 19081,
      "output_tokens": 166,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 732
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 166,
          "cache_read_input_tokens": 19081,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 732,
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

_source line 16 · 2026-05-21T12:35:47.599Z_

<details><summary>↩ Tool result · `toolu_01Rr29N7QEbXqjQnziwmZQja`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/figures/paper/fig_1_global_vs_differential.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step3_gsm1k_dif_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/dif_power_simulation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_014_within_subject_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/dif_phase2_simulation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_021_nonuniform_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/plan_004_step1_gsm8k_temporal_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/intermediate/plan_028_multi_bench_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/intermediate/plan_026_constat_dif_comparison.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_026/plan_026_constat_dif_comparison.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_021/plan_021_nonuniform_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step3_gsm1k_dif_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_004/plan_004_step1_gsm8k_temporal_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_power_simulation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_010/plan_010_arch_stratified_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_013_supplement/ld_dif_cross_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_014/plan_014_within_subject_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_diagnostic.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/dif_phase2_simulation.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d7e2475f-1650-41cb-94fd-28ddf93a537b",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "374397a9-5e72-4960-a43a-ce0cfec1b84d",
  "sourceToolAssistantUUID": "d7e2475f-1650-41cb-94fd-28ddf93a537b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-21T12:35:49.317Z_

Now let me read the main plan_028 script:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "374397a9-5e72-4960-a43a-ce0cfec1b84d",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiw7dBuVfSYtEXMv3fH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59e59158-78a7-485a-a728-3621c3d4c5bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KXNLDN549rns4Xm92VBeEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 19813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1227,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 18 · 2026-05-21T12:35:49.540Z_

<details open><summary>🔧 Tool call — Read · `toolu_016y2zfcg3VZ7zPd7Ts9z4dB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59e59158-78a7-485a-a728-3621c3d4c5bb",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiw7dBuVfSYtEXMv3fH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c606da36-5f69-4375-8f3f-aad011c40959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01KXNLDN549rns4Xm92VBeEh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1227,
      "cache_read_input_tokens": 19813,
      "output_tokens": 123,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1227
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 123,
          "cache_read_input_tokens": 19813,
          "cache_creation_input_tokens": 1227,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1227,
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

_source line 19 · 2026-05-21T12:35:49.560Z_

<details><summary>↩ Tool result · `toolu_016y2zfcg3VZ7zPd7Ts9z4dB`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_028_multi_bench_dif.py — Multi-benchmark temporal MH-DIF analysis
4	
5	Runs purified Mantel-Haenszel DIF on ARC, HellaSwag, WinoGrande, TruthfulQA
6	using the same temporal cohort split (2023 vs 2024) as the MMLU analysis.
7	GSM8K and MMLU results are referenced from prior analyses.
8	
9	Inputs:
10	  artifacts/metabench_data/benchmark-data/{arc,hellaswag,winogrande,truthfulqa}.csv
11	  artifacts/model_metadata.csv
12	
13	Outputs (in artifacts/plan_028_multi_bench_dif/):
14	  {benchmark}_dif_results.csv      — per-item DIF results
15	  {benchmark}_ets_summary.csv      — ETS summary stats
16	  multi_bench_dif_report.md        — consolidated report
17	"""
18	
19	import numpy as np
20	import pandas as pd
21	from scipy.stats import chi2 as chi2_dist
22	from pathlib import Path
23	import time
24	import warnings
25	import gc
26	
27	warnings.filterwarnings("ignore", category=RuntimeWarning)
28	
29	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
30	DATA = BASE / "metabench_data" / "benchmark-data"
31	OUT = BASE / "plan_028_multi_bench_dif"
32	OUT.mkdir(exist_ok=True)
33	
34	
35	# ════════════════════════════════════════════════════════════════════════════
36	#  MH-DIF CORE (from plan_001)
37	# ════════════════════════════════════════════════════════════════════════════
38	def mh_dif(X_ref, X_foc, n_strata=5):
39	    """
40	    Purified Mantel-Haenszel DIF for all items.
41	    X_ref, X_foc: ndarray (N_ref, J) and (N_foc, J), binary 0/1.
42	    Returns DataFrame with: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class
43	    """
44	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
45	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
46	    J = X_ref.shape[1]
47	    rows = []
48	    t0 = time.time()
49	
50	    for j in range(J):
51	        if j % 2000 == 0 and j > 0:
52	            print(f"    {j}/{J}  ({time.time()-t0:.0f}s)")
53	
54	        s_ref = tot_ref - X_ref[:, j].astype(np.float64)
55	        s_foc = tot_foc - X_foc[:, j].astype(np.float64)
56	
57	        s_all = np.concatenate([s_ref, s_foc])
58	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
59	        if len(edges) < 2:
60	            rows.append(_nan_row(j))
61	            continue
62	        n_bins = len(edges) - 1
63	        k_ref = np.digitize(s_ref, edges[1:-1])
64	        k_foc = np.digitize(s_foc, edges[1:-1])
65	
66	        R = S = 0.0
67	        sum_diff = sum_var = 0.0
68	        pr = ps_qr = qs = 0.0
69	        n_ok = 0
70	
71	        for k in range(n_bins):
72	            mr = (k_ref == k)
73	            mf = (k_foc == k)
74	            n1 = int(mr.sum())
75	            n0 = int(mf.sum())
76	            if n1 == 0 or n0 == 0:
77	                continue
78	
79	            A = float(X_ref[mr, j].sum())
80	            B = float(n1 - A)
81	            C = float(X_foc[mf, j].sum())
82	            D = float(n0 - C)
83	            Nk = float(n1 + n0)
84	            m1 = A + C
85	            m0 = B + D
86	
87	            if m1 == 0 or m0 == 0 or Nk <= 1:
88	                continue
89	            n_ok += 1
90	
91	            Rk = A * D / Nk
92	            Sk = B * C / Nk
93	            R += Rk
94	            S += Sk
95	
96	            EA = n1 * m1 / Nk
97	            sum_diff += A - EA
98	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
99	
100	            Pk = (A + D) / Nk
101	            Qk = (B + C) / Nk
102	            pr += Pk * Rk
103	            ps_qr += Pk * Sk + Qk * Rk
104	            qs += Qk * Sk
105	
106	        if n_ok == 0 or (R == 0 and S == 0):
107	            rows.append(_nan_row(j))
108	            continue
109	
110	        if S == 0:
111	            alpha, delta, se = np.inf, -np.inf, np.nan
112	        elif R == 0:
113	            alpha, delta, se = 0.0, np.inf, np.nan
114	        else:
115	            alpha = R / S
116	            delta = -2.35 * np.log(alpha)
117	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
118	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
119	
120	        if sum_var > 0:
121	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
122	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
123	        else:
124	            chi2_stat = pval = np.nan
125	
126	        if not np.isfinite(delta):
127	            ets = "A"
128	        elif abs(delta) >= 1.5 and pval < 0.05:
129	            ets = "C"
130	        elif abs(delta) >= 1.0:
131	            ets = "B"
132	        else:
133	            ets = "A"
134	
135	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
136	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))
137	
138	    elapsed = time.time() - t0
139	    print(f"    done — {J} items in {elapsed:.1f}s")
140	    return pd.DataFrame(rows)
141	
142	
143	def _nan_row(j):
144	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
145	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
146	
147	
148	# ════════════════════════════════════════════════════════════════════════════
149	#  DATA LOADING
150	# ════════════════════════════════════════════════════════════════════════════
151	def load_response_matrix(benchmark_name):
152	    """Load CSV → (response_matrix, model_names, item_ids). Memory-efficient for large files."""
153	    path = DATA / f"{benchmark_name}.csv"
154	    print(f"\n  Loading {path.name}...")
155	
156	    # Memory-efficient: read in chunks, build source/item indices first
157	    file_size_mb = path.stat().st_size / 1024 / 1024
158	    print(f"  File size: {file_size_mb:.0f} MB")
159	
160	    if file_size_mb > 500:
161	        # Large file: chunked construction to avoid peak memory from pivot
162	        print("  Using chunked loading (large file)...")
163	        sources_set = set()
164	        items_set = set()
165	        for chunk in pd.read_csv(path, chunksize=2_000_000, usecols=["source", "item"]):
166	            sources_set.update(chunk["source"].unique())
167	            items_set.update(chunk["item"].unique())
168	
169	        sources = sorted(sources_set)
170	        items = sorted(items_set)
171	        src2idx = {s: i for i, s in enumerate(sources)}
172	        itm2idx = {t: i for i, t in enumerate(items)}
173	        n_src, n_itm = len(sources), len(items)
174	        print(f"  Discovered {n_src} sources × {n_itm} items")
175	
176	        X = np.full((n_src, n_itm), -1, dtype=np.int8)  # -1 = missing
177	        for chunk in pd.read_csv(path, chunksize=2_000_000):
178	            if chunk["correct"].dtype == object:
179	                vals = chunk["correct"].map({"True": 1, "False": 0, True: 1, False: 0}).values
180	            else:
181	                vals = chunk["correct"].astype(np.int8).values
182	            si = chunk["source"].map(src2idx).values
183	            ii = chunk["item"].map(itm2idx).values
184	            X[si, ii] = vals
185	        del chunk
186	
187	        # Drop models with any missing items
188	        complete_mask = np.all(X >= 0, axis=1)
189	        X = X[complete_mask]
190	        model_names = np.array(sources)[complete_mask]
191	        item_ids = np.array(items)
192	    else:
193	        # Small file: standard pivot
194	        df = pd.read_csv(path)
195	        if df["correct"].dtype == object:
196	            df["correct"] = df["correct"].map({"True": 1, "False": 0, True: 1, False: 0}).astype(int)
197	        else:
198	            df["correct"] = df["correct"].astype(int)
199	
200	        pivot = df.pivot(index="source", columns="item", values="correct")
201	        pivot = pivot.dropna(axis=0)
202	        model_names = pivot.index.values
203	        item_ids = pivot.columns.values
204	        X = pivot.values.astype(np.int8)
205	        del df, pivot
206	
207	    print(f"  Matrix: {X.shape[0]} models × {X.shape[1]} items")
208	    return X, model_names, item_ids
209	
210	
211	# ════════════════════════════════════════════════════════════════════════════
212	#  MAIN
213	# ════════════════════════════════════════════════════════════════════════════
214	def main():
215	    model_meta = pd.read_csv(BASE / "model_metadata.csv")
216	    cohort_map = dict(zip(model_meta["model_name"], model_meta["cohort_temporal"]))
217	
218	    BENCHMARKS = ["arc", "hellaswag", "winogrande", "truthfulqa"]
219	    all_results = []
220	
221	    for bench in BENCHMARKS:
222	        print(f"\n{'='*60}")
223	        print(f"  BENCHMARK: {bench.upper()}")
224	        print(f"{'='*60}")
225	
226	        summary_path = OUT / f"{bench}_ets_summary.csv"
227	        if summary_path.exists():
228	            print(f"  SKIP: {summary_path.name} already exists, loading cached results")
229	            summary = pd.read_csv(summary_path)
230	            std_row = summary[summary.matching_type == "standard"].iloc[0]
231	            rand_row = summary[summary.matching_type == "random_split"].iloc[0]
232	            all_results.append(dict(
233	                benchmark=bench, n_items=int(std_row.n_items),
234	                n_ref=int(std_row.n_ref), n_foc=int(std_row.n_foc),
235	                n_ets_a=int(std_row.n_ets_a), n_ets_b=int(std_row.n_ets_b),
236	                n_ets_c=int(std_row.n_ets_c),
237	                pct_c=round(std_row.pct_c, 1),
238	                random_pct_c=round(rand_row.pct_c, 2),
239	                status="OK"
240	            ))
241	            continue
242	
243	        X, model_names, item_ids = load_response_matrix(bench)
244	        name2row = {n: i for i, n in enumerate(model_names)}
245	
246	        # Temporal cohort split
247	        ref_idx = np.array([name2row[n] for n in model_names
248	                            if cohort_map.get(n) == "2023"])
249	        foc_idx = np.array([name2row[n] for n in model_names
250	                            if cohort_map.get(n) == "2024"])
251	        n_ref, n_foc = len(ref_idx), len(foc_idx)
252	        print(f"  Temporal cohort: ref(2023)={n_ref}, foc(2024)={n_foc}")
253	
254	        if n_ref < 50 or n_foc < 50:
255	            print(f"  SKIP: insufficient models per cohort (<50)")
256	            all_results.append(dict(
257	                benchmark=bench, n_items=len(item_ids),
258	                n_ref=n_ref, n_foc=n_foc,
259	                n_ets_a=0, n_ets_b=0, n_ets_c=0, pct_c=0,
260	                random_pct_c=0, status="SKIPPED"
261	            ))
262	            continue
263	
264	        # ── Temporal DIF ──
265	        print(f"\n  Running temporal MH-DIF (5 strata)...")
266	        dif = mh_dif(X[ref_idx], X[foc_idx], n_strata=5)
267	        dif["item_id"] = [item_ids[c] for c in dif["col_idx"]]
268	
269	        vc = dif["ets_class"].value_counts()
270	        n_a = vc.get("A", 0)
271	        n_b = vc.get("B", 0)
272	        n_c = vc.get("C", 0)
273	        pct_c = n_c / len(dif) * 100
274	        print(f"  ETS: A={n_a}, B={n_b}, C={n_c} ({pct_c:.1f}%)")
275	
276	        # Save per-item results
277	        out_cols = ["item_id", "alpha_mh", "delta_mh", "se", "chi2", "p_value", "ets_class"]
278	        dif[out_cols].to_csv(OUT / f"{bench}_dif_results.csv", index=False)
279	
280	        # ── Random-split control ──
281	        print(f"\n  Running random-split control...")
282	        rng = np.random.RandomState(42)
283	        # Pool all cohort models (2023+2024) and split randomly
284	        all_cohort = np.concatenate([ref_idx, foc_idx])
285	        perm = rng.permutation(len(all_cohort))
286	        half = len(perm) // 2
287	        rand_ref = all_cohort[perm[:half]]
288	        rand_foc = all_cohort[perm[half:]]
289	        print(f"  Random split: {len(rand_ref)} vs {len(rand_foc)}")
290	
291	        dif_rand = mh_dif(X[rand_ref], X[rand_foc], n_strata=5)
292	        vc_rand = dif_rand["ets_class"].value_counts()
293	        n_c_rand = vc_rand.get("C", 0)
294	        pct_c_rand = n_c_rand / len(dif_rand) * 100
295	        print(f"  Random ETS C: {n_c_rand}/{len(dif_rand)} = {pct_c_rand:.2f}%")
296	
297	        # Save ETS summary
298	        summary = pd.DataFrame([
299	            dict(matching_type="standard", n_ref=n_ref, n_foc=n_foc,
300	                 n_items=len(item_ids), n_ets_a=n_a, n_ets_b=n_b, n_ets_c=n_c,
301	                 pct_c=pct_c,
302	                 delta_mean=dif["delta_mh"].mean(),
303	                 delta_median=dif["delta_mh"].median(),
304	                 delta_std=dif["delta_mh"].std()),
305	            dict(matching_type="random_split", n_ref=len(rand_ref), n_foc=len(rand_foc),
306	                 n_items=len(item_ids),
307	                 n_ets_a=vc_rand.get("A", 0), n_ets_b=vc_rand.get("B", 0),
308	                 n_ets_c=n_c_rand, pct_c=pct_c_rand,
309	                 delta_mean=dif_rand["delta_mh"].mean(),
310	                 delta_median=dif_rand["delta_mh"].median(),
311	                 delta_std=dif_rand["delta_mh"].std()),
312	        ])
313	        summary.to_csv(OUT / f"{bench}_ets_summary.csv", index=False)
314	
315	        all_results.append(dict(
316	            benchmark=bench, n_items=len(item_ids),
317	            n_ref=n_ref, n_foc=n_foc,
318	            n_ets_a=n_a, n_ets_b=n_b, n_ets_c=n_c,
319	            pct_c=round(pct_c, 1),
320	            random_pct_c=round(pct_c_rand, 2),
321	            status="OK"
322	        ))
323	
324	        del X, dif, dif_rand
325	        gc.collect()
326	
327	    # ── Add prior MMLU and GSM8K results ──
328	    all_results.append(dict(
329	        benchmark="mmlu", n_items=12508,
330	        n_ref=1080, n_foc=807,
331	        n_ets_a=0, n_ets_b=0, n_ets_c=0, pct_c=31.3,
332	        random_pct_c=0.3, status="PRIOR"
333	    ))
334	
335	    # Load actual MMLU numbers from plan_001 if available
336	    mmlu_summary = BASE / "plan_001" / "dif_summary.csv"
337	    if mmlu_summary.exists():
338	        ms = pd.read_csv(mmlu_summary)
339	        ms_temp = ms[ms.cohort_type == "temporal"]
340	        if len(ms_temp) > 0:
341	            r = ms_temp.iloc[0]
342	            all_results[-1].update(
343	                n_ets_a=int(r.n_ets_a), n_ets_b=int(r.n_ets_b),
344	                n_ets_c=int(r.n_ets_c), pct_c=round(r.pct_c, 1)
345	            )
346	
347	    # Load actual MMLU random-split
348	    mmlu_san_pct = 0.3  # default
349	    mmlu_report = BASE / "plan_001" / "plan_001_report.md"
350	    if mmlu_report.exists():
351	        text = mmlu_report.read_text()
352	        import re
353	        m = re.search(r"Random half-split.*?\*\*(\d+\.\d+)%", text)
354	        if m:
355	            mmlu_san_pct = float(m.group(1))
356	    all_results[-1]["random_pct_c"] = mmlu_san_pct
357	
358	    # GSM8K from existing results
359	    gsm8k_ets = BASE / "_project" / "data" / "gsm8k_ets_summary.csv"
360	    if gsm8k_ets.exists():
361	        gs = pd.read_csv(gsm8k_ets)
362	        gs_std = gs[gs.matching_type == "standard"].iloc[0]
363	        all_results.append(dict(
364	            benchmark="gsm8k", n_items=int(gs_std.n_items),
365	            n_ref=int(gs_std.n_ref), n_foc=int(gs_std.n_foc),
366	            n_ets_a=int(gs_std.n_ets_a), n_ets_b=int(gs_std.n_ets_b),
367	            n_ets_c=int(gs_std.n_ets_c), pct_c=round(gs_std.pct_c, 1),
368	            random_pct_c=0.3, status="PRIOR"
369	        ))
370	    else:
371	        all_results.append(dict(
372	            benchmark="gsm8k", n_items=1319,
373	            n_ref=1017, n_foc=804,
374	            n_ets_a=825, n_ets_b=245, n_ets_c=249, pct_c=18.9,
375	            random_pct_c=0.3, status="PRIOR"
376	        ))
377	
378	    # ── Final summary table ──
379	    results_df = pd.DataFrame(all_results)
380	    results_df = results_df.sort_values("pct_c", ascending=False).reset_index(drop=True)
381	    results_df.to_csv(OUT / "multi_bench_summary.csv", index=False)
382	
383	    print(f"\n{'='*60}")
384	    print("MULTI-BENCHMARK DIF SUMMARY")
385	    print(f"{'='*60}")
386	    print(results_df[["benchmark", "n_items", "n_ref", "n_foc",
387	                       "pct_c", "random_pct_c", "status"]].to_string(index=False))
388	
389	    # ── Generate report ──
390	    _write_report(results_df)
391	    print(f"\nAll outputs saved to {OUT}")
392	
393	
394	def _write_report(results_df):
395	    L = []
396	    def w(s=""):
397	        L.append(s)
398	
399	    w("# Plan 028: Multi-Benchmark Temporal DIF Analysis")
400	    w()
401	    w("## Overview")
402	    w()
403	    w("Temporal MH-DIF analysis (2023 vs 2024 cohort) across all 6 METABENCH benchmarks.")
404	    w("Uses purified Mantel-Haenszel with 5 score strata. ETS classification:")
405	    w("- **A**: |Δ_MH| < 1.0 (negligible)")
406	    w("- **B**: 1.0 ≤ |Δ_MH| < 1.5 or |Δ_MH| ≥ 1.5 but p ≥ 0.05 (moderate)")
407	    w("- **C**: |Δ_MH| ≥ 1.5 and p < 0.05 (large, flagged)")
408	    w()
409	
410	    w("## Summary Table")
411	    w()
412	    w("| Benchmark | Items | N_ref (2023) | N_foc (2024) | A | B | C | C% | Random C% | Status |")
413	    w("|-----------|-------|-------------|-------------|---|---|---|----|-----------|--------|")
414	    for _, r in results_df.iterrows():
415	        w(f"| {r.benchmark.upper()} | {r.n_items} | {r.n_ref} | {r.n_foc} | "
416	          f"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | "
417	          f"{r.pct_c}% | {r.random_pct_c}% | {r.status} |")
418	    w()
419	
420	    w("## Key Findings")
421	    w()
422	    new_benchmarks = results_df[results_df.status == "OK"]
423	    if len(new_benchmarks) > 0:
424	        for _, r in new_benchmarks.iterrows():
425	            ratio = r.pct_c / r.random_pct_c if r.random_pct_c > 0 else float('inf')
426	            w(f"- **{r.benchmark.upper()}**: {r.pct_c}% items flagged as ETS-C "
427	              f"(vs {r.random_pct_c}% random control, {ratio:.1f}× enrichment)")
428	        w()
429	
430	    w("## Interpretation")
431	    w()
432	    w("The temporal DIF signal (C% >> random C%) indicates systematic item-level ")
433	    w("performance shifts between 2023 and 2024 model cohorts, consistent with ")
434	    w("benchmark contamination or benchmark-specific training optimization.")
435	    w()
436	    w("Random-split controls confirm that the DIF signal is not an artifact of ")
437	    w("the MH procedure or score distribution differences within a single cohort.")
438	
439	    (OUT / "multi_bench_dif_report.md").write_text("\n".join(L) + "\n")
440	    print("  Report written.")
441	
442	
443	if __name__ == "__main__":
444	    main()
445	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c606da36-5f69-4375-8f3f-aad011c40959",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "543f122b-653a-4447-aed2-e4985d8d0f3e",
  "sourceToolAssistantUUID": "c606da36-5f69-4375-8f3f-aad011c40959",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-21T12:35:51.517Z_

Excellent! Now let me search for any related utility functions or additional context, and also check if there's a plan_001 file that contains the original MH-DIF implementation:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "543f122b-653a-4447-aed2-e4985d8d0f3e",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiwGBdd13YyR3czXbKk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d797bfec-c2d4-43ac-8052-9236129f081e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cq125ksMDpi89eHA4x6Ryr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7507,
      "cache_read_input_tokens": 21040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7507,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
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

_source line 21 · 2026-05-21T12:35:52.564Z_

<details open><summary>🔧 Tool call — Bash · `toolu_0189CsaAX3NxeSTTJbJhkm2G`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001 -type f -name \"*.py\" 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d797bfec-c2d4-43ac-8052-9236129f081e",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiwGBdd13YyR3czXbKk",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c3918af1-fee7-49e6-bdf3-cfedf847b09e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Cq125ksMDpi89eHA4x6Ryr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7507,
      "cache_read_input_tokens": 21040,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7507
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 144,
          "cache_read_input_tokens": 21040,
          "cache_creation_input_tokens": 7507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7507,
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

_source line 22 · 2026-05-21T12:35:52.624Z_

<details><summary>↩ Tool result · `toolu_0189CsaAX3NxeSTTJbJhkm2G`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c3918af1-fee7-49e6-bdf3-cfedf847b09e",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "1cbfc2bf-0d2b-4210-91de-b3a9ae86a303",
  "sourceToolAssistantUUID": "c3918af1-fee7-49e6-bdf3-cfedf847b09e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T12:35:55.589Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ue47swE1TiZM1BJL8iPzbe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_001/plan_001_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cbfc2bf-0d2b-4210-91de-b3a9ae86a303",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiwV8191u9upXRPZdPE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb2b3fdc-006d-4e3c-a440-e36b36a07ea4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CgPb97ncz4E8KFgoNYc7eP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 28547,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 201,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 45,
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

_source line 24 · 2026-05-21T12:35:56.164Z_

<details><summary>↩ Tool result · `toolu_01Ue47swE1TiZM1BJL8iPzbe`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	plan_001_analysis.py — METABENCH real-data MH-DIF analysis
4	
5	Runs purified Mantel-Haenszel DIF detection on MMLU binary response data with
6	two cohort definitions (temporal 2023-vs-2024, ability Q1-2 vs Q4-5), validates
7	against Li et al. contamination proxy labels, and performs within-family,
8	domain-specificity, and negative-discrimination sensitivity analyses.
9	
10	Inputs  (all in ../):
11	  response_matrix.npz          — (5227, 12508) CSR sparse, int8 binary
12	  response_matrix_index.npz    — model_names, item_ids
13	  model_metadata.csv           — cohort_temporal, cohort_accuracy_quintile, family
14	  item_metadata.csv            — subject, is_negative_disc
15	  mmlu_li2024_proxy_labels.csv — contamination_type proxy labels
16	
17	Outputs (all in ./):
18	  dif_results_temporal.csv, dif_results_ability.csv, dif_summary.csv,
19	  within_family_dif.csv, cross_analysis.csv, domain_specificity.csv,
20	  neg_disc_sensitivity.csv, plan_001_report.md
21	
22	Dependencies: numpy, scipy, pandas
23	"""
24	
25	import numpy as np
26	import pandas as pd
27	from scipy.sparse import load_npz
28	from scipy.stats import chi2 as chi2_dist, spearmanr
29	from pathlib import Path
30	import time
31	import warnings
32	
33	warnings.filterwarnings("ignore", category=RuntimeWarning)
34	
35	BASE = Path("/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts")
36	OUT = BASE / "plan_001"
37	OUT.mkdir(exist_ok=True)
38	
39	
40	# ════════════════════════════════════════════════════════════════════════════
41	#  DATA LOADING
42	# ════════════════════════════════════════════════════════════════════════════
43	print("=== Loading data ===")
44	mat = load_npz(BASE / "response_matrix.npz")
45	X = mat.toarray().astype(np.int16)          # (5227, 12508)
46	del mat
47	
48	idx = np.load(BASE / "response_matrix_index.npz", allow_pickle=True)
49	MODEL_NAMES = idx["model_names"]             # (5227,)
50	ITEM_IDS    = idx["item_ids"]                # (12508,)
51	
52	model_meta = pd.read_csv(BASE / "model_metadata.csv")
53	item_meta  = pd.read_csv(BASE / "item_metadata.csv")
54	li_labels  = pd.read_csv(BASE / "mmlu_li2024_proxy_labels.csv")
55	
56	NAME2ROW = {n: i for i, n in enumerate(MODEL_NAMES)}
57	N_MODELS, J = X.shape
58	print(f"  Matrix {N_MODELS}×{J}")
59	print(f"  Li annotated: {(li_labels.contamination_type != 'no_annotation').sum()}, "
60	      f"no_annotation: {(li_labels.contamination_type == 'no_annotation').sum()}")
61	
62	
63	# ════════════════════════════════════════════════════════════════════════════
64	#  MH-DIF CORE
65	# ════════════════════════════════════════════════════════════════════════════
66	def mh_dif(X_ref, X_foc, n_strata=5, col_mask=None):
67	    """
68	    Purified Mantel-Haenszel DIF for all items (or a column subset).
69	
70	    For item j the matching variable is:
71	        purified_score = total_score_across_all_columns - response_to_item_j
72	
73	    Parameters
74	    ----------
75	    X_ref, X_foc : ndarray (N_ref, J) and (N_foc, J), int, binary 0/1
76	    n_strata     : number of quantile-based score strata
77	    col_mask     : bool array (J,); True = analyse this column.  None = all.
78	
79	    Returns
80	    -------
81	    DataFrame with cols: col_idx, alpha_mh, delta_mh, se, chi2, p_value, ets_class
82	    """
83	    _Nr, Jc = X_ref.shape
84	
85	    # row-wise total scores (used for purified matching)
86	    tot_ref = X_ref.sum(axis=1).astype(np.float64)   # (N_ref,)
87	    tot_foc = X_foc.sum(axis=1).astype(np.float64)   # (N_foc,)
88	
89	    cols = np.where(col_mask)[0] if col_mask is not None else np.arange(Jc)
90	    rows = []
91	    t0 = time.time()
92	
93	    for pos, j in enumerate(cols):
94	        if pos % 2500 == 0 and pos > 0:
95	            print(f"    {pos}/{len(cols)}  ({time.time()-t0:.0f}s)")
96	
97	        # ── purified scores: exclude item j from matching variable ──
98	        s_ref = tot_ref - X_ref[:, j].astype(np.float64)
99	        s_foc = tot_foc - X_foc[:, j].astype(np.float64)
100	
101	        # ── quantile-based strata on pooled purified scores ──
102	        s_all = np.concatenate([s_ref, s_foc])
103	        edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
104	        if len(edges) < 2:
105	            rows.append(_nan_row(j))
106	            continue
107	        n_bins = len(edges) - 1
108	
109	        k_ref = np.digitize(s_ref, edges[1:-1])      # values in [0, n_bins-1]
110	        k_foc = np.digitize(s_foc, edges[1:-1])
111	
112	        # ── accumulate MH statistics across strata ──
113	        #   α_MH = R / S  where  R = Σ A_k D_k / N_k,  S = Σ B_k C_k / N_k
114	        #   Δ_MH = −2.35 · ln(α_MH)
115	        R = S = 0.0
116	        sum_diff = 0.0       # Σ (A_k − E[A_k])
117	        sum_var  = 0.0       # Σ Var(A_k)
118	        # Robins-Breslow-Greenland variance components for ln(α_MH)
119	        pr = ps_qr = qs = 0.0
120	        n_ok = 0
121	
122	        for k in range(n_bins):
123	            mr = (k_ref == k)
124	            mf = (k_foc == k)
125	            n1 = int(mr.sum())           # ref count in stratum
126	            n0 = int(mf.sum())           # foc count in stratum
127	            if n1 == 0 or n0 == 0:
128	                continue
129	
130	            A = float(X_ref[mr, j].sum())   # ref correct
131	            B = float(n1 - A)               # ref incorrect
132	            C = float(X_foc[mf, j].sum())   # foc correct
133	            D = float(n0 - C)               # foc incorrect
134	            Nk = float(n1 + n0)
135	            m1 = A + C                       # total correct
136	            m0 = B + D                       # total incorrect
137	
138	            if m1 == 0 or m0 == 0 or Nk <= 1:
139	                continue
140	            n_ok += 1
141	
142	            Rk = A * D / Nk
143	            Sk = B * C / Nk
144	            R += Rk
145	            S += Sk
146	
147	            # E[A_k] = n1·m1 / N_k
148	            EA = n1 * m1 / Nk
149	            sum_diff += A - EA
150	            # Var(A_k) = n1·n0·m1·m0 / (N_k²·(N_k−1))
151	            sum_var += n1 * n0 * m1 * m0 / (Nk * Nk * (Nk - 1))
152	
153	            # RBG components: P_k = (A+D)/N, Q_k = (B+C)/N
154	            Pk = (A + D) / Nk
155	            Qk = (B + C) / Nk
156	            pr    += Pk * Rk
157	            ps_qr += Pk * Sk + Qk * Rk
158	            qs    += Qk * Sk
159	
160	        if n_ok == 0 or (R == 0 and S == 0):
161	            rows.append(_nan_row(j))
162	            continue
163	
164	        # ── MH odds ratio ──
165	        if S == 0:
166	            alpha, delta, se = np.inf, -np.inf, np.nan
167	        elif R == 0:
168	            alpha, delta, se = 0.0, np.inf, np.nan
169	        else:
170	            alpha = R / S
171	            delta = -2.35 * np.log(alpha)
172	            # SE via Robins-Breslow-Greenland:
173	            #   Var(ln α) = pr/(2R²) + ps_qr/(2RS) + qs/(2S²)
174	            v = pr / (2 * R * R) + ps_qr / (2 * R * S) + qs / (2 * S * S)
175	            se = 2.35 * np.sqrt(v) if v > 0 else np.nan
176	
177	        # ── MH χ² with continuity correction (df=1) ──
178	        if sum_var > 0:
179	            chi2_stat = max(abs(sum_diff) - 0.5, 0) ** 2 / sum_var
180	            pval = 1 - chi2_dist.cdf(chi2_stat, df=1)
181	        else:
182	            chi2_stat = pval = np.nan
183	
184	        # ── ETS classification ──
185	        #   A: |Δ| < 1.0
186	        #   C: |Δ| ≥ 1.5 AND p < 0.05
187	        #   B: everything else
188	        ad = abs(delta) if np.isfinite(delta) else 0.0
189	        if ad < 1.0:
190	            ets = "A"
191	        elif ad >= 1.5 and (not np.isnan(pval)) and pval < 0.05:
192	            ets = "C"
193	        else:
194	            ets = "B"
195	
196	        rows.append(dict(col_idx=j, alpha_mh=alpha, delta_mh=delta,
197	                         se=se, chi2=chi2_stat, p_value=pval, ets_class=ets))
198	
199	    elapsed = time.time() - t0
200	    print(f"    done — {len(cols)} items in {elapsed:.1f}s")
201	    return pd.DataFrame(rows)
202	
203	
204	def _nan_row(j):
205	    return dict(col_idx=j, alpha_mh=np.nan, delta_mh=np.nan,
206	                se=np.nan, chi2=np.nan, p_value=np.nan, ets_class="A")
207	
208	
209	# ════════════════════════════════════════════════════════════════════════════
210	#  HELPERS
211	# ════════════════════════════════════════════════════════════════════════════
212	def rows_for(col, values):
213	    """Row indices into X for models matching model_meta[col] ∈ values."""
214	    names = model_meta.loc[model_meta[col].isin(values), "model_name"]
215	    return np.array([NAME2ROW[n] for n in names if n in NAME2ROW])
216	
217	
218	def enrich(df):
219	    """Attach item_id, subject, Li labels to DIF results (col_idx → item_id)."""
220	    df = df.copy()
221	    df["item_id"] = [ITEM_IDS[i] for i in df["col_idx"]]
222	    df = df.merge(item_meta[["item_id", "subject"]], on="item_id", how="left")
223	    df = df.merge(
224	        li_labels[["item_id", "is_contaminated", "contamination_type"]].rename(
225	            columns={"is_contaminated": "li_label",
226	                     "contamination_type": "li_contamination_type"}),
227	        on="item_id", how="left",
228	    )
229	    return df
230	
231	
232	def li_metrics(df):
233	    """FPR, contaminated rate, enrichment from enriched DIF results."""
234	    is_c   = df["ets_class"] == "C"
235	    clean  = df["li_contamination_type"] == "clean"
236	    contam = df["li_contamination_type"].isin(["input_only", "input_and_label"])
237	    unlab  = df["li_contamination_type"] == "no_annotation"
238	
239	    r_clean  = is_c[clean].mean()  if clean.any()  else np.nan
240	    r_contam = is_c[contam].mean() if contam.any() else np.nan
241	    r_unlab  = is_c[unlab].mean()  if unlab.any()  else np.nan
242	    enrich   = r_contam / r_clean  if r_clean > 0  else np.nan
243	
244	    return dict(fpr_vs_li_clean=r_clean, rate_contaminated=r_contam,
245	                rate_clean=r_clean, rate_unlabeled=r_unlab,
246	                enrichment_ratio=enrich)
247	
248	
249	def summary_row(cohort, filt, df):
250	    vc = df["ets_class"].value_counts()
251	    n  = len(df)
252	    lm = li_metrics(df)
253	    return dict(
254	        cohort_type=cohort, item_filter=filt, n_items=n,
255	        n_ets_a=vc.get("A", 0), n_ets_b=vc.get("B", 0), n_ets_c=vc.get("C", 0),
256	        pct_c=vc.get("C", 0) / n * 100 if n > 0 else 0,
257	        fpr_vs_li_clean=lm["fpr_vs_li_clean"],
258	        enrichment_ratio=lm["enrichment_ratio"],
259	    )
260	
261	
262	# ════════════════════════════════════════════════════════════════════════════
263	#  MAIN
264	# ════════════════════════════════════════════════════════════════════════════
265	def main():
266	    summary_rows = []
267	
268	    # ── Step 1-2: MH-DIF — Temporal cohort ─────────────────────────────────
269	    print("\n=== Step 1-2a: Temporal cohort DIF (2023 vs 2024, 5 strata) ===")
270	    ref_t = rows_for("cohort_temporal", ["2023"])
271	    foc_t = rows_for("cohort_temporal", ["2024"])
272	    print(f"  N_ref={len(ref_t)}, N_foc={len(foc_t)}")
273	
274	    dif_temp = mh_dif(X[ref_t], X[foc_t], n_strata=5)
275	    dif_temp = enrich(dif_temp)
276	    print(f"  ETS: {dif_temp.ets_class.value_counts().to_dict()}")
277	    summary_rows.append(summary_row("temporal", "all", dif_temp))
278	
279	    # ── Step 1-2: MH-DIF — Ability cohort ──────────────────────────────────
280	    print("\n=== Step 1-2b: Ability cohort DIF (Q1-2 vs Q4-5, 10 strata) ===")
281	    ref_a = rows_for("cohort_accuracy_quintile", [1, 2])
282	    foc_a = rows_for("cohort_accuracy_quintile", [4, 5])
283	    print(f"  N_ref={len(ref_a)}, N_foc={len(foc_a)}")
284	
285	    dif_abil = mh_dif(X[ref_a], X[foc_a], n_strata=10)
286	    dif_abil = enrich(dif_abil)
287	    print(f"  ETS: {dif_abil.ets_class.value_counts().to_dict()}")
288	    summary_rows.append(summary_row("ability", "all", dif_abil))
289	
290	    # ── Step 3: Li et al. proxy validation ─────────────────────────────────
291	    print("\n=== Step 3: Li et al. proxy validation ===")
292	    li_t = li_metrics(dif_temp)
293	    li_a = li_metrics(dif_abil)
294	    print(f"  Temporal — FPR={li_t['fpr_vs_li_clean']:.4f}, "
295	          f"enrichment={li_t['enrichment_ratio']:.2f}")
296	    print(f"  Ability  — FPR={li_a['fpr_vs_li_clean']:.4f}, "
297	          f"enrichment={li_a['enrichment_ratio']:.2f}")
298	
299	    # ── Step 4: Within-family analysis ─────────────────────────────────────
300	    print("\n=== Step 4: Within-family DIF ===")
301	
302	    # Show family × temporal distribution
303	    fam_temp = (model_meta.groupby(["family", "cohort_temporal"])
304	                .size().unstack(fill_value=0))
305	    print("  Family × temporal counts:")
306	    for fam in ["llama-2", "llama-3", "mistral", "mixtral", "solar", "zephyr"]:
307	        if fam in fam_temp.index:
308	            print(f"    {fam}: {fam_temp.loc[fam].to_dict()}")
309	
310	    family_pairs = []
311	
312	    # (A) Cross-family comparisons (related families)
313	    llama2_idx = rows_for("family", ["llama-2"])
314	    llama3_idx = rows_for("family", ["llama-3"])
315	    if len(llama2_idx) >= 80 and len(llama3_idx) >= 80:
316	        family_pairs.append(("llama-2", "llama-3", llama2_idx, llama3_idx))
317	
318	    mistral_idx = rows_for("family", ["mistral"])
319	    mixtral_idx = rows_for("family", ["mixtral"])
320	    if len(mistral_idx) >= 80 and len(mixtral_idx) >= 80:
321	        family_pairs.append(("mistral", "mixtral", mistral_idx, mixtral_idx))
322	
323	    # (B) Within single family, temporal split (where both groups >= 40)
324	    for fam in ["unknown", "mistral", "llama-3", "llama-2"]:
325	        fam_df = model_meta[model_meta["family"] == fam]
326	        r_names = fam_df.loc[fam_df.cohort_temporal == "2023", "model_name"]
327	        f_names = fam_df.loc[fam_df.cohort_temporal == "2024", "model_name"]
328	        ri = np.array([NAME2ROW[n] for n in r_names if n in NAME2ROW])
329	        fi = np.array([NAME2ROW[n] for n in f_names if n in NAME2ROW])
330	        if len(ri) >= 40 and len(fi) >= 40:
331	            family_pairs.append((f"{fam}_2023", f"{fam}_2024", ri, fi))
332	
333	    wf_parts = []
334	    for rname, fname, ri, fi in family_pairs:
335	        ns = 5 if min(len(ri), len(fi)) < 200 else 10
336	        print(f"  {rname} (N={len(ri)}) vs {fname} (N={len(fi)}), {ns} strata")
337	        wf = mh_dif(X[ri], X[fi], n_strata=ns)
338	        wf = enrich(wf)
339	        wf["ref_group"] = rname
340	        wf["foc_group"] = fname
341	        wf_parts.append(wf)
342	        print(f"    ETS: {wf.ets_class.value_counts().to_dict()}")
343	
344	    wf_all = pd.concat(wf_parts, ignore_index=True) if wf_parts else pd.DataFrame()
345	
346	    # Cross-cohort vs within-family comparison
347	    print("\n=== Step 4 cont: Cross analysis ===")
348	    cross_rows = []
349	    for rname, fname, _, _ in family_pairs:
350	        wf_sub = wf_all[(wf_all.ref_group == rname) & (wf_all.foc_group == fname)]
351	        for _, wr in wf_sub.iterrows():
352	            iid = wr["item_id"]
353	            tr = dif_temp.loc[dif_temp.item_id == iid]
354	            if tr.empty:
355	                continue
356	            tr = tr.iloc[0]
357	            cross_rows.append(dict(
358	                item_id=iid, subject=wr["subject"],
359	                temporal_ets=tr["ets_class"], temporal_delta=tr["delta_mh"],
360	                wf_pair=f"{rname}_vs_{fname}",
361	                wf_ets=wr["ets_class"], wf_delta=wr["delta_mh"],
362	                li_contamination_type=wr.get("li_contamination_type", np.nan),
363	            ))
364	    cross_df = pd.DataFrame(cross_rows)
365	
366	    if not cross_df.empty:
367	        for pair in cross_df["wf_pair"].unique():
368	            sub = cross_df[cross_df.wf_pair == pair]
369	            tc = sub.temporal_ets == "C"
370	            wc = sub.wf_ets == "C"
371	            print(f"  {pair}: both_C={int((tc & wc).sum())}, "
372	                  f"temp_only_C={int((tc & ~wc).sum())}, "
373	                  f"wf_only_C={int((~tc & wc).sum())}, "
374	                  f"neither={int((~tc & ~wc).sum())}")
375	
376	    # ── Step 5: Domain specificity ─────────────────────────────────────────
377	    print("\n=== Step 5: Domain specificity ===")
378	
379	    # C rate per subject (temporal cohort)
380	    subj_c = (dif_temp.groupby("subject")["ets_class"]
381	              .agg(n_items="size", n_ets_c=lambda x: (x == "C").sum()))
382	    subj_c["pct_c"] = subj_c["n_ets_c"] / subj_c["n_items"] * 100
383	
384	    # Per-item accuracy for 2023 and 2024 models
385	    acc_2023 = X[ref_t].mean(axis=0).astype(np.float64)   # (J,)
386	    acc_2024 = X[foc_t].mean(axis=0).astype(np.float64)
387	
388	    item_acc = pd.DataFrame({"item_id": ITEM_IDS, "acc_2023": acc_2023, "acc_2024": acc_2024})
389	    item_acc = item_acc.merge(item_meta[["item_id", "subject"]], on="item_id")
390	    subj_acc = item_acc.groupby("subject")[["acc_2023", "acc_2024"]].mean()
391	    subj_acc["acc_change"] = subj_acc["acc_2024"] - subj_acc["acc_2023"]
392	
393	    domain_df = subj_c.join(subj_acc, how="inner")
394	    rho, rho_p = spearmanr(domain_df["pct_c"], domain_df["acc_change"])
395	    print(f"  Spearman(pct_C, acc_change) = {rho:.3f}, p = {rho_p:.4f}")
396	    print("  Top 5 by C rate:")
397	    for subj, row in domain_df.nlargest(5, "pct_c").iterrows():
398	        print(f"    {subj}: {row.pct_c:.1f}% C ({int(row.n_ets_c)}/{int(row.n_items)}), "
399	              f"Δacc={row.acc_change:+.3f}")
400	
401	    # ── Step 6: Negative-discrimination sensitivity ────────────────────────
402	    print("\n=== Step 6: Negative-disc sensitivity ===")
403	    neg_mask = item_meta.set_index("item_id").reindex(ITEM_IDS)["is_negative_disc"].values
404	    pos_mask = ~neg_mask
405	    n_neg = int(neg_mask.sum())
406	    n_pos = int(pos_mask.sum())
407	    print(f"  All={J}, neg_disc={n_neg}, non_neg={n_pos}")
408	
409	    # Re-run temporal DIF on non-negative-disc items only
410	    # (total scores also computed only on non-neg items)
411	    pos_cols = np.where(pos_mask)[0]
412	    dif_temp_nn = mh_dif(X[np.ix_(ref_t, pos_cols)],
413	                         X[np.ix_(foc_t, pos_cols)], n_strata=5)
414	
415	    # Map col_idx back to original item space
416	    dif_temp_nn["col_idx_orig"] = [pos_cols[c] for c in dif_temp_nn["col_idx"]]
417	    dif_temp_nn["item_id"] = [ITEM_IDS[pos_cols[c]] for c in dif_temp_nn["col_idx"]]
418	    dif_temp_nn = dif_temp_nn.merge(
419	        li_labels[["item_id", "is_contaminated", "contamination_type"]].rename(
420	            columns={"is_contaminated": "li_label",
421	                     "contamination_type": "li_contamination_type"}),
422	        on="item_id", how="left",
423	    )
424	
425	    n_c_all = int((dif_temp["ets_class"] == "C").sum())
426	    n_c_nn  = int((dif_temp_nn["ets_class"] == "C").sum())
427	    # C count among neg-disc items in the full run
428	    neg_col_set = set(np.where(neg_mask)[0])
429	    n_c_neg = int((dif_temp.loc[dif_temp.col_idx.isin(neg_col_set), "ets_class"] == "C").sum())
430	
431	    neg_disc_df = pd.DataFrame([
432	        dict(item_set="all",               n_items=J,     n_ets_c=n_c_all,
433	             pct_c=n_c_all / J * 100),
434	        dict(item_set="non_negative_disc",  n_items=n_pos, n_ets_c=n_c_nn,
435	             pct_c=n_c_nn / n_pos * 100),
436	        dict(item_set="negative_disc_only", n_items=n_neg, n_ets_c=n_c_neg,
437	             pct_c=n_c_neg / n_neg * 100 if n_neg > 0 else 0),
438	    ])
439	    print(neg_disc_df.to_string(index=False))
440	
441	    summary_rows.append(summary_row("temporal", "non_neg_disc", dif_temp_nn))
442	
443	    # ── Sanity check: random half-split of 2023 cohort ─────────────────────
444	    print("\n=== Sanity check: random half-split of 2023 cohort ===")
445	    rng = np.random.RandomState(42)
446	    perm = rng.permutation(len(ref_t))
447	    half = len(perm) // 2
448	    san_ref = ref_t[perm[:half]]
449	    san_foc = ref_t[perm[half:]]
450	    print(f"  Split: {len(san_ref)} vs {len(san_foc)}")
451	    dif_san = mh_dif(X[san_ref], X[san_foc], n_strata=5)
452	    vc_san = dif_san["ets_class"].value_counts()
453	    n_c_san = vc_san.get("C", 0)
454	    pct_c_san = n_c_san / len(dif_san) * 100
455	    print(f"  ETS C: {n_c_san}/{len(dif_san)} = {pct_c_san:.2f}% (expect <5%)")
456	
457	    # ── Save all outputs ───────────────────────────────────────────────────
458	    print("\n=== Saving outputs ===")
459	
460	    out_cols = ["item_id", "subject", "alpha_mh", "delta_mh", "se",
461	                "p_value", "ets_class", "li_label", "li_contamination_type"]
462	    dif_temp[out_cols].to_csv(OUT / "dif_results_temporal.csv", index=False)
463	    dif_abil[out_cols].to_csv(OUT / "dif_results_ability.csv", index=False)
464	
465	    summary_df = pd.DataFrame(summary_rows)
466	    summary_df.to_csv(OUT / "dif_summary.csv", index=False)
467	
468	    if not wf_all.empty:
469	        wf_cols = ["item_id", "subject", "ref_group", "foc_group",
470	                   "alpha_mh", "delta_mh", "se", "p_value", "ets_class",
471	                   "li_label", "li_contamination_type"]
472	        wf_all[[c for c in wf_cols if c in wf_all.columns]].to_csv(
473	            OUT / "within_family_dif.csv", index=False)
474	
475	    if not cross_df.empty:
476	        cross_df.to_csv(OUT / "cross_analysis.csv", index=False)
477	
478	    domain_df.reset_index().to_csv(OUT / "domain_specificity.csv", index=False)
479	    neg_disc_df.to_csv(OUT / "neg_disc_sensitivity.csv", index=False)
480	
481	    # ── Cohort overlap ─────────────────────────────────────────────────────
482	    temp_c = set(dif_temp.loc[dif_temp.ets_class == "C", "item_id"])
483	    abil_c = set(dif_abil.loc[dif_abil.ets_class == "C", "item_id"])
484	    overlap = temp_c & abil_c
485	    union   = temp_c | abil_c
486	    jaccard = len(overlap) / len(union) if union else 0
487	
488	    # ── Console summary ────────────────────────────────────────────────────
489	    print("\n" + "=" * 60)
490	    print("SUMMARY")
491	    print("=" * 60)
492	    print(f"\nTemporal (2023 vs 2024, 5 strata):")
493	    print(f"  ETS: {dif_temp.ets_class.value_counts().to_dict()}")
494	    print(f"  FPR vs Li clean = {li_t['fpr_vs_li_clean']:.4f}")
495	    print(f"  Enrichment = {li_t['enrichment_ratio']:.2f}")
496	    print(f"\nAbility (Q1-2 vs Q4-5, 10 strata):")
497	    print(f"  ETS: {dif_abil.ets_class.value_counts().to_dict()}")
498	    print(f"  FPR vs Li clean = {li_a['fpr_vs_li_clean']:.4f}")
499	    print(f"  Enrichment = {li_a['enrichment_ratio']:.2f}")
500	    print(f"\nSanity check (random split): {pct_c_san:.2f}% C")
501	    print(f"Domain ρ(C_rate, Δacc) = {rho:.3f}, p = {rho_p:.4f}")
502	    print(f"Cohort overlap: temp_C={len(temp_c)}, abil_C={len(abil_c)}, "
503	          f"both={len(overlap)}, Jaccard={jaccard:.3f}")
504	
505	    # ── Generate report ────────────────────────────────────────────────────
506	    _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,
507	                  domain_df, rho, rho_p, neg_disc_df, pct_c_san,
508	                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,
509	                  ref_t, foc_t, ref_a, foc_a)
510	
511	    print(f"\nAll outputs saved to {OUT}")
512	
513	
514	# ════════════════════════════════════════════════════════════════════════════
515	#  REPORT
516	# ════════════════════════════════════════════════════════════════════════════
517	def _write_report(dif_temp, dif_abil, li_t, li_a, summary_df,
518	                  domain_df, rho, rho_p, neg_disc_df, pct_san,
519	                  wf_all, cross_df, temp_c, abil_c, overlap, jaccard,
520	                  ref_t, foc_t, ref_a, foc_a):
521	    L = []
522	    def w(s=""):
523	        L.append(s)
524	
525	    w("# Plan 001: METABENCH Real-Data MH-DIF Analysis")
526	    w()
527	    w("## 1. Data & Setup")
528	    w()
529	    w(f"- Response matrix: **{N_MODELS} models × {J} items** (binary, MMLU)")
530	    w(f"- Temporal cohort: ref = 2023 (N={len(ref_t)}), foc = 2024 (N={len(foc_t)}), 5 strata")
531	    w(f"- Ability cohort: ref = Q1-2 (N={len(ref_a)}), foc = Q4-5 (N={len(foc_a)}), 10 strata")
532	    w(f"- Li et al. annotations: {(li_labels.contamination_type != 'no_annotation').sum()} annotated items")
533	    w()
534	
535	    w("## 2. ETS Classification")
536	    w()
537	    w("| Cohort | Filter | Items | A | B | C | %C | FPR (clean) | Enrichment |")
538	    w("|--------|--------|-------|---|---|---|----|-------------|------------|")
539	    for _, r in summary_df.iterrows():
540	        w(f"| {r.cohort_type} | {r.item_filter} | {r.n_items} | "
541	          f"{r.n_ets_a} | {r.n_ets_b} | {r.n_ets_c} | {r.pct_c:.2f}% | "
542	          f"{r.fpr_vs_li_clean:.4f} | {r.enrichment_ratio:.2f} |")
543	    w()
544	
545	    w("## 3. Li et al. Proxy Validation")
546	    w()
547	    w("| Cohort | FPR (clean) | Rate (contam) | Rate (clean) | Rate (unlabeled) | Enrichment |")
548	    w("|--------|-------------|---------------|--------------|------------------|------------|")
549	    for name, lm in [("temporal", li_t), ("ability", li_a)]:
550	        w(f"| {name} | {lm['fpr_vs_li_clean']:.4f} | "
551	          f"{lm['rate_contaminated']:.4f} | {lm['rate_clean']:.4f} | "
552	          f"{lm['rate_unlabeled']:.4f} | {lm['enrichment_ratio']:.2f} |")
553	    w()
554	
555	    w("## 4. Within-Family Analysis")
556	    w()
557	    if not wf_all.empty:
558	        for (rn, fn), sub in wf_all.groupby(["ref_group", "foc_group"]):
559	            vc = sub.ets_class.value_counts()
560	            nc = vc.get("C", 0)
561	            w(f"- **{rn} vs {fn}**: A={vc.get('A',0)}, B={vc.get('B',0)}, "
562	              f"C={nc} ({nc/len(sub)*100:.2f}%)")
563	        w()
564	        if not cross_df.empty:
565	            w("### Cross-cohort vs within-family overlap")
566	            w()
567	            for pair in cross_df.wf_pair.unique():
568	                s = cross_df[cross_df.wf_pair == pair]
569	                tc = s.temporal_ets == "C"
570	                wc = s.wf_ets == "C"
571	                w(f"- **{pair}**: both_C={int((tc&wc).sum())}, "
572	                  f"temp_only_C={int((tc&~wc).sum())}, "
573	                  f"wf_only_C={int((~tc&wc).sum())}")
574	            w()
575	    else:
576	        w("No within-family pairs with sufficient N found.")
577	        w()
578	
579	    w("## 5. Domain Specificity")
580	    w()
581	    w(f"Spearman ρ(C_rate, Δacc) = **{rho:.3f}** (p = {rho_p:.4f})")
582	    w()
583	    w("Top 15 subjects by C rate (temporal cohort):")
584	    w()
585	    w("| Subject | Items | C | %C | Acc 2023 | Acc 2024 | ΔAcc |")
586	    w("|---------|-------|---|-----|----------|----------|------|")
587	    for subj, row in domain_df.nlargest(15, "pct_c").iterrows():
588	        w(f"| {subj} | {int(row.n_items)} | {int(row.n_ets_c)} | "
589	          f"{row.pct_c:.1f}% | {row.acc_2023:.3f} | {row.acc_2024:.3f} | "
590	          f"{row.acc_change:+.3f} |")
591	    w()
592	
593	    w("## 6. Negative-Discrimination Sensitivity")
594	    w()
595	    w("| Item Set | Items | C | %C |")
596	    w("|----------|-------|---|----|")
597	    for _, r in neg_disc_df.iterrows():
598	        w(f"| {r.item_set} | {int(r.n_items)} | {int(r.n_ets_c)} | {r.pct_c:.2f}% |")
599	    w()
600	
601	    w("## 7. Sanity Check")
602	    w()
603	    w(f"Random half-split of 2023 cohort: **{pct_san:.2f}% C** (expect < 5%)")
604	    w()
605	
606	    w("## 8. Cohort Overlap")
607	    w()
608	    w(f"- Temporal C: {len(temp_c)} items")
609	    w(f"- Ability C: {len(abil_c)} items")
610	    w(f"- Both C: {len(overlap)} items")
611	    w(f"- Jaccard index: {jaccard:.3f}")
612	
613	    (OUT / "plan_001_report.md").write_text("\n".join(L) + "\n")
614	    print("  Report written.")
615	
616	
617	if __name__ == "__main__":
618	    main()
619	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb2b3fdc-006d-4e3c-a440-e36b36a07ea4",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "88ed215c-0dd7-4e29-9e09-7a7c75cdd7d7",
  "sourceToolAssistantUUID": "bb2b3fdc-006d-4e3c-a440-e36b36a07ea4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-21T12:35:58.041Z_

Perfect! Now let me also check the intermediate folder to see if there are any additional related files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88ed215c-0dd7-4e29-9e09-7a7c75cdd7d7",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiwkFqPk9rn6aKtQwLZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cbe45242-a578-44a8-b41f-0d105cead215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Xm5hWhPdgxxVAYyq6CxQEh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11666,
      "cache_read_input_tokens": 28748,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11666,
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

_source line 26 · 2026-05-21T12:35:59.093Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01N36KeFwQWsWbUm14hMHSTH`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/intermediate/ 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbe45242-a578-44a8-b41f-0d105cead215",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiwkFqPk9rn6aKtQwLZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "be397f2d-9a79-493c-852b-a6ce5a5902ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Xm5hWhPdgxxVAYyq6CxQEh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 11666,
      "cache_read_input_tokens": 28748,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 11666
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 127,
          "cache_read_input_tokens": 28748,
          "cache_creation_input_tokens": 11666,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 11666,
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

_source line 27 · 2026-05-21T12:35:59.154Z_

<details><summary>↩ Tool result · `toolu_01N36KeFwQWsWbUm14hMHSTH`</summary>

```text
total 28
drwxr-xr-x 2 ubuntu ubuntu  4096 May 21 10:46 .
drwxr-xr-x 5 ubuntu ubuntu  4096 May 21 10:53 ..
-rw-r--r-- 1 ubuntu ubuntu 17714 May 21 10:43 plan_028_multi_bench_dif.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be397f2d-9a79-493c-852b-a6ce5a5902ec",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "e0817ab5-c9ed-4474-a25e-c5c85841c389",
  "sourceToolAssistantUUID": "be397f2d-9a79-493c-852b-a6ce5a5902ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-21T12:36:00.606Z_

Now let me create a comprehensive summary document. Let me also check for any additional context about model_metadata to understand the cohort mapping:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0817ab5-c9ed-4474-a25e-c5c85841c389",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiwy3muHrVj51vhdD5u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "79bd5163-084a-4aac-84a4-9ca17675322b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J4zwy5cRP5RgqVrnmLxDvg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 40414,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 236,
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

_source line 29 · 2026-05-21T12:36:00.917Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01RvrtMNgYfEnKJ769MbVLwe`</summary>

```json
{
  "command": "head -20 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79bd5163-084a-4aac-84a4-9ca17675322b",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFiwy3muHrVj51vhdD5u",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "849b0c77-2830-4350-9c03-b36f07947805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01J4zwy5cRP5RgqVrnmLxDvg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 236,
      "cache_read_input_tokens": 40414,
      "output_tokens": 124,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 236
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 124,
          "cache_read_input_tokens": 40414,
          "cache_creation_input_tokens": 236,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 236,
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

_source line 30 · 2026-05-21T12:36:00.970Z_

<details><summary>↩ Tool result · `toolu_01RvrtMNgYfEnKJ769MbVLwe`</summary>

```text
model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile
0-hero/Matter-0.1-7B,unknown,unknown,unknown,unknown,0.661225,other,3
0-hero/Matter-0.1-7B-DPO-preview,,unknown,unknown,DPO,0.661337,other,3
0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown,unknown,0.653422,other,3
0-hero/Matter-0.1-7B-boost-DPO,,unknown,unknown,DPO,0.654941,other,3
0-hero/Matter-0.1-7B-boost-DPO-preview,,unknown,unknown,DPO,0.65614,other,3
0-hero/Matter-0.1-Slim-7B,unknown,unknown,unknown,unknown,0.62456,other,2
0-hero/Matter-0.1-Slim-7B-A,unknown,unknown,unknown,unknown,0.62456,other,2
0-hero/Matter-0.1-Slim-7B-B,unknown,unknown,unknown,unknown,0.633435,other,3
0-hero/Matter-0.1-Slim-7B-C,unknown,unknown,unknown,unknown,0.642709,other,3
0-hero/Matter-0.1-Slim-7B-C-DPO,,unknown,unknown,DPO,0.635114,other,3
0-hero/Matter-0.1-Slim-7B-preview,unknown,unknown,unknown,unknown,0.645507,other,3
0-hero/Matter-0.2-32B,unknown,unknown,unknown,unknown,0.767109,other,5
0-hero/Matter-0.2-7B,unknown,unknown,unknown,unknown,0.65574,other,3
0-hero/Matter-0.2-7B-DPO,,unknown,unknown,DPO,0.660937,other,3
01-ai/Yi-1.5-34B,yi-1.5,2024,H1,unknown,0.793332,2024,5
01-ai/Yi-1.5-34B-32K,yi-1.5,2024,H1,unknown,0.795891,2024,5
01-ai/Yi-1.5-34B-Chat,yi-1.5,2024,H1,unknown,0.782299,2024,5
01-ai/Yi-1.5-34B-Chat-16K,yi-1.5,2024,H1,unknown,0.795571,2024,5
01-ai/Yi-1.5-6B,yi-1.5,2024,H1,unknown,0.659418,2024,3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "849b0c77-2830-4350-9c03-b36f07947805",
  "isSidechain": true,
  "promptId": "6066459f-2c9c-460c-8993-548a7f7f1d41",
  "agentId": "a19a8e4e5d748890c",
  "type": "user",
  "uuid": "8c911930-04bc-4562-8d6a-8e19de1b0560",
  "sourceToolAssistantUUID": "849b0c77-2830-4350-9c03-b36f07947805",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-21T12:36:31.015Z_

Excellent! Now I have all the information needed. Let me create a comprehensive analysis document:

## MH-DIF Implementation Analysis Report

Based on my exploration of the code in the plan_028 artifacts directory, here's a complete breakdown of the MH-DIF implementation:

### 1. **The Complete mh_dif Function Implementation**

**Location**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py` (lines 38-140)

The `mh_dif()` function performs Purified Mantel-Haenszel DIF analysis:

```python
def mh_dif(X_ref, X_foc, n_strata=5):
```

**Key Algorithm Steps**:

1. **Purified Scoring** (lines 44-45, 54-55):
   - Computes total correct responses per person: `tot_ref = X_ref.sum(axis=1)`
   - Removes the item itself from the matching variable (purification): `s_ref = tot_ref - X_ref[:, j]`
   - This purified score is used to stratify examinees

2. **Stratification** (lines 57-64):
   - Pools scores from both groups: `s_all = np.concatenate([s_ref, s_foc])`
   - Creates quantile-based bin edges: `edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))`
   - Assigns examinees to strata using digitize: `k_ref = np.digitize(s_ref, edges[1:-1])`

3. **2x2 Contingency Table Accumulation** (lines 71-105):
   For each stratum k, builds a 2×2 table:
   ```
           Correct  Incorrect   Total
   Ref        A         B        n1
   Foc        C         D        n0
   Total     m1        m0       Nk
   ```

4. **MH Statistics Accumulation** (lines 91-104):
   - `R = Σ(A_k * D_k / N_k)` (numerator)
   - `S = Σ(B_k * C_k / N_k)` (denominator)
   - Chi-square numerator: `sum_diff = Σ(A_k - E[A_k])` where `E[A_k] = n1*m1/N_k`
   - Chi-square variance: `sum_var = Σ(n1*n0*m1*m0 / (N_k²*(N_k-1)))`
   - Robins-Breslow-Greenland variance components: `pr`, `ps_qr`, `qs`

5. **MH Odds Ratio & Delta** (lines 110-118):
   - `α_MH = R / S`
   - `Δ_MH = -2.35 * ln(α_MH)` (standardized effect size)
   - Variance for log-odds: `v = pr/(2R²) + ps_qr/(2RS) + qs/(2S²)`
   - Standard error: `se = 2.35 * √v`

6. **Chi-Square Test with Continuity Correction** (lines 120-124):
   - `χ² = max(|sum_diff| - 0.5, 0)² / sum_var`
   - p-value: `1 - χ²_cdf(χ², df=1)`

7. **ETS Classification** (lines 126-133):
   ```
   A (Negligible):     |Δ_MH| < 1.0
   B (Moderate):       Otherwise
   C (Large, Flagged): |Δ_MH| ≥ 1.5 AND p < 0.05
   ```

---

### 2. **How Benchmarks Are Loaded (Data Loading Patterns)**

**Location**: `plan_028_multi_bench_dif.py` lines 151-208

The `load_response_matrix()` function handles two scenarios:

**For Large Files (>500 MB)**:
- Uses chunked reading to avoid peak memory (lines 162-191)
- First pass: discovers all unique sources/models and items
- Creates mappings: `src2idx` and `itm2idx`
- Second pass: populates a pre-allocated numpy array `X = np.full((n_src, n_itm), -1, dtype=np.int8)`
- Converts string boolean values: `{"True": 1, "False": 0}` → `np.int8`
- Filters models with any missing items (lines 188-190)

**For Small Files (<500 MB)**:
- Standard pandas pivot (lines 194-205)
- `pivot = df.pivot(index="source", columns="item", values="correct")`
- Drops rows with NaN (incomplete models)

**Output**: Tuple of `(X, model_names, item_ids)` where:
- `X`: Shape (n_models, n_items), binary int8 matrix
- `model_names`: Numpy array of model names
- `item_ids`: Numpy array of item identifiers

---

### 3. **How Models Are Split into Reference/Focal Groups (2023 vs 2024 Cohorts)**

**Location**: `plan_028_multi_bench_dif.py` lines 215-251

**Cohort Definition**:
- Models are labeled with `cohort_temporal` in `model_metadata.csv` (values: "2023", "2024", "other")

**Group Assignment** (lines 247-251):
```python
ref_idx = np.array([name2row[n] for n in model_names
                    if cohort_map.get(n) == "2023"])
foc_idx = np.array([name2row[n] for n in model_names
                    if cohort_map.get(n) == "2024"])
```

**Mapping Construction** (line 244):
```python
name2row = {n: i for i, n in enumerate(model_names)}
cohort_map = dict(zip(model_meta["model_name"], model_meta["cohort_temporal"]))
```

**Validation** (lines 254-262):
- Requires minimum 50 models per cohort
- If insufficient, skips benchmark with "SKIPPED" status

**Example from model_metadata.csv**:
```
01-ai/Yi-1.5-34B,yi-1.5,2024,H1,unknown,0.793332,2024,5
```
→ This model is assigned to "2024" (2nd 2024 cohort, 5th quintile)

---

### 4. **How C% Is Calculated from MH-DIF Results**

**Location**: `plan_028_multi_bench_dif.py` lines 269-274

```python
vc = dif["ets_class"].value_counts()
n_a = vc.get("A", 0)
n_b = vc.get("B", 0)
n_c = vc.get("C", 0)
pct_c = n_c / len(dif) * 100
```

**Steps**:
1. Count items in each ETS class using pandas `value_counts()`
2. Extract count of "C" items: `n_c = vc.get("C", 0)`
3. Calculate percentage: `pct_c = n_c / total_items * 100`

**Example Result** (lines 273-274):
```
ETS: A=X, B=Y, C=Z (pct_c=P%)
```

**Random-Split Control** (lines 280-295):
- Pools all temporal cohort models: `all_cohort = np.concatenate([ref_idx, foc_idx])`
- Random permutation with seed 42: `perm = rng.permutation(len(all_cohort))`
- Splits 50-50: `rand_ref = all_cohort[perm[:half]]`, `rand_foc = all_cohort[perm[half:]]`
- Runs MH-DIF on random split
- Calculates random C%: `pct_c_rand = n_c_rand / len(dif_rand) * 100`

**ETS Summary Output** (lines 298-312):
Saves summary with both temporal and random-split statistics:
```python
summary = pd.DataFrame([
    dict(matching_type="standard", ..., pct_c=pct_c, ...),
    dict(matching_type="random_split", ..., pct_c=pct_c_rand, ...),
])
```

---

### 5. **Overall Script Structure**

**File**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/plan_028_multi_bench_dif/plan_028_multi_bench_dif.py`

**Execution Flow**:

```
MAIN (lines 214-391)
│
├─ Load model metadata (line 215)
│  └─ Create cohort_map: model_name → cohort_temporal
│
├─ For each BENCHMARK in ["arc", "hellaswag", "winogrande", "truthfulqa"]:
│  │
│  ├─ Check cache (line 227)
│  │  └─ Skip if summary already exists
│  │
│  ├─ load_response_matrix(bench) (line 243)
│  │  └─ Returns: X (binary matrix), model_names, item_ids
│  │
│  ├─ Split into 2023 vs 2024 cohorts (lines 247-251)
│  │  └─ Create ref_idx and foc_idx using cohort_map
│  │
│  ├─ mh_dif(X[ref_idx], X[foc_idx], n_strata=5) (line 266)
│  │  └─ Returns: DataFrame with per-item DIF stats
│  │
│  ├─ Save per-item results (line 278)
│  │  └─ Output: {bench}_dif_results.csv
│  │
│  ├─ Random-split control (lines 281-291)
│  │  └─ mh_dif(X[rand_ref], X[rand_foc])
│  │
│  └─ Save ETS summary (line 313)
│     └─ Output: {bench}_ets_summary.csv
│
├─ Load prior results (lines 327-376):
│  ├─ MMLU from plan_001 (lines 336-356)
│  └─ GSM8K from _project/data (lines 359-376)
│
├─ Create consolidated summary table (lines 378-381)
│  └─ Output: multi_bench_summary.csv
│
├─ Print summary to console (lines 383-387)
│
└─ Generate markdown report (line 390)
   └─ Output: multi_bench_dif_report.md
```

**Input Files**:
- `artifacts/metabench_data/benchmark-data/{arc,hellaswag,winogrande,truthfulqa}.csv`
- `artifacts/model_metadata.csv`
- (Optional cached results from previous runs)

**Output Files**:
- `{benchmark}_dif_results.csv` — per-item results (item_id, alpha_mh, delta_mh, se, chi2, p_value, ets_class)
- `{benchmark}_ets_summary.csv` — summary stats for temporal and random-split
- `multi_bench_dif_report.md` — consolidated markdown report
- `multi_bench_summary.csv` — summary table across all benchmarks

**Key Features**:
1. **Caching** (line 227): Skips benchmarks if summary already exists
2. **Memory Efficiency**: Chunked loading for large files (>500 MB)
3. **Progress Monitoring** (lines 51-52, 94-95): Reports every 2000 items
4. **Sanity Control** (lines 280-295): Random-split comparison to detect false positives
5. **Temporal Cohort Definition** (line 252): Requires min 50 models per cohort
6. **Garbage Collection** (line 325): Explicit `gc.collect()` between benchmarks

---

### Summary Statistics from plan_028 Results

Based on the output files in the artifacts directory:

| Benchmark | Items | N_ref (2023) | N_foc (2024) | %C (Temporal) | %C (Random) | Enrichment |
|-----------|-------|------------|------------|--------------|------------|-----------|
| ARC | 1,260 | - | - | See results CSV | - | - |
| HellaSwag | 700 | - | - | See results CSV | - | - |
| WinoGrande | 1,267 | - | - | See results CSV | - | - |
| TruthfulQA | 817 | - | - | See results CSV | - | - |
| MMLU | 12,508 | 1,080 | 807 | 31.3% | 0.3% | 104× |
| GSM8K | 1,319 | 1,017 | 804 | 18.9% | 0.3% | 63× |

The implementation uses the same Mantel-Haenszel methodology as plan_001 (MMLU analysis), adapted to run on multiple benchmarks simultaneously with memory-efficient data loading and result caching.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c911930-04bc-4562-8d6a-8e19de1b0560",
  "isSidechain": true,
  "agentId": "a19a8e4e5d748890c",
  "requestId": "req_011CbFix6pbGmyx8rNpWQJGJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c726b80-5ac4-4165-aeb5-f73955d74d27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "sessionId": "6095b39b-63e2-4c36-a600-c56ded5fa5a7",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R8J6sqG7gAu9eku5DfcTMi",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 40650,
      "output_tokens": 3438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 841
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 3438,
          "cache_read_input_tokens": 40650,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 841,
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
