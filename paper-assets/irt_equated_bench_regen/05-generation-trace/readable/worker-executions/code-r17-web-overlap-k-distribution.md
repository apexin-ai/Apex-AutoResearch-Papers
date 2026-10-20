# code r17 web overlap k distribution

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_code_r17_web_overlap_k_distribution_20260523T120838.log`
- **Structured JSON:** [`c75fbcef25789eae6bc1.json`](../../sessions/c7/c75fbcef25789eae6bc1.json)

## Before a recorded user message

21 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
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
  "uuid": "64df1bc9-ae21-436a-9765-199a4f9e21b4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779540600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "aeaa60ee-84fb-434d-9e19-637ce809b516",
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the data file to understand its structure, then write the analysis script.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "957be22f-f7f1-48a2-8d5b-cc6733f3129d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsSUmhvUwisZgHDCo5k1rd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
      },
      "output_tokens": 9,
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01ShwvgKP5uotjsAKep5kJM1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mmlu_li2024_proxy_labels.csv",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "04b3b5af-13f1-44f1-a41d-a33bf4891cd8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsSUmhvUwisZgHDCo5k1rd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
      },
      "output_tokens": 9,
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

_source line 6 · 2026-05-23T12:08:50.380Z_

<details><summary>↩ Tool result · `toolu_01ShwvgKP5uotjsAKep5kJM1`</summary>

```text
1	item_id,subject,is_contaminated,contamination_type,similarity_score,source
2	abstract_algebra.1,abstract_algebra,False,clean,0.4089,li_etal_2024_emnlp
3	abstract_algebra.2,abstract_algebra,True,input_only,0.8496,li_etal_2024_emnlp
4	abstract_algebra.3,abstract_algebra,False,clean,0.0244,li_etal_2024_emnlp
5	abstract_algebra.4,abstract_algebra,False,clean,0.4760,li_etal_2024_emnlp
6	abstract_algebra.5,abstract_algebra,False,clean,0.0417,li_etal_2024_emnlp
7	abstract_algebra.6,abstract_algebra,False,clean,0.0341,li_etal_2024_emnlp
8	abstract_algebra.7,abstract_algebra,False,clean,0.1375,li_etal_2024_emnlp
9	abstract_algebra.8,abstract_algebra,False,clean,0.4366,li_etal_2024_emnlp
10	abstract_algebra.9,abstract_algebra,True,input_only,0.7585,li_etal_2024_emnlp
11	abstract_algebra.10,abstract_algebra,False,clean,0.0109,li_etal_2024_emnlp
12	abstract_algebra.11,abstract_algebra,False,clean,0.2601,li_etal_2024_emnlp
13	abstract_algebra.12,abstract_algebra,False,clean,0.4933,li_etal_2024_emnlp
14	abstract_algebra.13,abstract_algebra,False,clean,0.3947,li_etal_2024_emnlp
15	abstract_algebra.14,abstract_algebra,False,clean,0.6577,li_etal_2024_emnlp
16	abstract_algebra.15,abstract_algebra,False,clean,0.2290,li_etal_2024_emnlp
17	abstract_algebra.16,abstract_algebra,False,clean,0.0000,li_etal_2024_emnlp
18	abstract_algebra.17,abstract_algebra,False,clean,0.4791,li_etal_2024_emnlp
19	abstract_algebra.18,abstract_algebra,True,input_and_label,0.9544,li_etal_2024_emnlp
20	abstract_algebra.20,abstract_algebra,False,clean,0.1297,li_etal_2024_emnlp
21	abstract_algebra.21,abstract_algebra,False,clean,0.5043,li_etal_2024_emnlp
22	abstract_algebra.22,abstract_algebra,False,clean,0.1927,li_etal_2024_emnlp
23	abstract_algebra.23,abstract_algebra,True,input_and_label,0.7084,li_etal_2024_emnlp
24	abstract_algebra.24,abstract_algebra,False,clean,0.0667,li_etal_2024_emnlp
25	abstract_algebra.25,abstract_algebra,True,input_only,0.8518,li_etal_2024_emnlp
26	abstract_algebra.26,abstract_algebra,False,clean,0.4302,li_etal_2024_emnlp
27	abstract_algebra.27,abstract_algebra,False,clean,0.6216,li_etal_2024_emnlp
28	abstract_algebra.28,abstract_algebra,False,clean,0.0641,li_etal_2024_emnlp
29	abstract_algebra.29,abstract_algebra,False,clean,0.0962,li_etal_2024_emnlp
30	abstract_algebra.30,abstract_algebra,False,clean,0.0326,li_etal_2024_emnlp
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "bc329928-8aa8-454e-a452-e316fa893ce9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mmlu_li2024_proxy_labels.csv",
      "content": "item_id,subject,is_contaminated,contamination_type,similarity_score,source\nabstract_algebra.1,abstract_algebra,False,clean,0.4089,li_etal_2024_emnlp\nabstract_algebra.2,abstract_algebra,True,input_only,0.8496,li_etal_2024_emnlp\nabstract_algebra.3,abstract_algebra,False,clean,0.0244,li_etal_2024_emnlp\nabstract_algebra.4,abstract_algebra,False,clean,0.4760,li_etal_2024_emnlp\nabstract_algebra.5,abstract_algebra,False,clean,0.0417,li_etal_2024_emnlp\nabstract_algebra.6,abstract_algebra,False,clean,0.0341,li_etal_2024_emnlp\nabstract_algebra.7,abstract_algebra,False,clean,0.1375,li_etal_2024_emnlp\nabstract_algebra.8,abstract_algebra,False,clean,0.4366,li_etal_2024_emnlp\nabstract_algebra.9,abstract_algebra,True,input_only,0.7585,li_etal_2024_emnlp\nabstract_algebra.10,abstract_algebra,False,clean,0.0109,li_etal_2024_emnlp\nabstract_algebra.11,abstract_algebra,False,clean,0.2601,li_etal_2024_emnlp\nabstract_algebra.12,abstract_algebra,False,clean,0.4933,li_etal_2024_emnlp\nabstract_algebra.13,abstract_algebra,False,clean,0.3947,li_etal_2024_emnlp\nabstract_algebra.14,abstract_algebra,False,clean,0.6577,li_etal_2024_emnlp\nabstract_algebra.15,abstract_algebra,False,clean,0.2290,li_etal_2024_emnlp\nabstract_algebra.16,abstract_algebra,False,clean,0.0000,li_etal_2024_emnlp\nabstract_algebra.17,abstract_algebra,False,clean,0.4791,li_etal_2024_emnlp\nabstract_algebra.18,abstract_algebra,True,input_and_label,0.9544,li_etal_2024_emnlp\nabstract_algebra.20,abstract_algebra,False,clean,0.1297,li_etal_2024_emnlp\nabstract_algebra.21,abstract_algebra,False,clean,0.5043,li_etal_2024_emnlp\nabstract_algebra.22,abstract_algebra,False,clean,0.1927,li_etal_2024_emnlp\nabstract_algebra.23,abstract_algebra,True,input_and_label,0.7084,li_etal_2024_emnlp\nabstract_algebra.24,abstract_algebra,False,clean,0.0667,li_etal_2024_emnlp\nabstract_algebra.25,abstract_algebra,True,input_only,0.8518,li_etal_2024_emnlp\nabstract_algebra.26,abstract_algebra,False,clean,0.4302,li_etal_2024_emnlp\nabstract_algebra.27,abstract_algebra,False,clean,0.6216,li_etal_2024_emnlp\nabstract_algebra.28,abstract_algebra,False,clean,0.0641,li_etal_2024_emnlp\nabstract_algebra.29,abstract_algebra,False,clean,0.0962,li_etal_2024_emnlp\nabstract_algebra.30,abstract_algebra,False,clean,0.0326,li_etal_2024_emnlp",
      "numLines": 30,
      "startLine": 1,
      "totalLines": 12510
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01CJZGzfsLbttg47uwQeSGPH`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mmlu_li2024_proxy_labels.csv && head -1 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mmlu_li2024_proxy_labels.csv",
  "description": "Check CSV row count and header"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "6d4ad879-3dbb-42f0-9a00-ac629fc556ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsSUmhvUwisZgHDCo5k1rd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
      },
      "output_tokens": 9,
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

_source line 8 · 2026-05-23T12:08:51.917Z_

<details><summary>↩ Tool result · `toolu_01CJZGzfsLbttg47uwQeSGPH`</summary>

```text
12509 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mmlu_li2024_proxy_labels.csv
item_id,subject,is_contaminated,contamination_type,similarity_score,source
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "0a504e8c-8cf5-4433-bfc0-82bb19cc21e0",
  "tool_use_result": {
    "stdout": "12509 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mmlu_li2024_proxy_labels.csv\nitem_id,subject,is_contaminated,contamination_type,similarity_score,source",
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

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_012wQ9L78oXMC79XbAhBa8Jw`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/ 2>/dev/null || echo \"DIR_NOT_EXISTS\"",
  "description": "Check if r17_evidence directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "e790957e-b803-4eba-90cd-777d55cb2ed7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DsSUmhvUwisZgHDCo5k1rd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13095
      },
      "output_tokens": 9,
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

_source line 10 · 2026-05-23T12:08:52.948Z_

<details><summary>↩ Tool result · `toolu_012wQ9L78oXMC79XbAhBa8Jw`</summary>

```text
weighted_mean_downstream.json
weighted_mean_downstream.md
weighted_mean_downstream.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "1bc35e96-a0e8-4f2f-9cbe-2640c69aa704",
  "tool_use_result": {
    "stdout": "weighted_mean_downstream.json\nweighted_mean_downstream.md\nweighted_mean_downstream.py",
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_01KQGB9fjfXCz6TicDCQCtB3`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\ndf = pd.read_csv('artifacts/mmlu_li2024_proxy_labels.csv')\nprint('contamination_type values:', df['contamination_type'].value_counts().to_dict())\nprint('is_contaminated values:', df['is_contaminated'].value_counts().to_dict())\nprint('n subjects:', df['subject'].nunique())\n\"",
  "description": "Explore contamination type distribution"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "d8807052-e623-455b-a191-797938d97be8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014TN8PT8RZ3YPvCLedusjsF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1627,
      "cache_read_input_tokens": 24936,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1627
      },
      "output_tokens": 63,
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

_source line 12 · 2026-05-23T12:08:57.774Z_

<details><summary>↩ Tool result · `toolu_01KQGB9fjfXCz6TicDCQCtB3`</summary>

```text
contamination_type values: {'clean': 5584, 'no_annotation': 3279, 'input_and_label': 3043, 'input_only': 602}
is_contaminated values: {False: 5584, True: 3645}
n subjects: 57
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "69fe7419-ef2a-45b7-b15e-107958ebc9fd",
  "tool_use_result": {
    "stdout": "contamination_type values: {'clean': 5584, 'no_annotation': 3279, 'input_and_label': 3043, 'input_only': 602}\nis_contaminated values: {False: 5584, True: 3645}\nn subjects: 57",
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

_source line 13_

Data checks out: 57 subjects, 12508 items, clear contamination type categories. Writing the analysis script and report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "ab410fac-c2d3-4717-8703-08b9f4c18995",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011rhFeRnHC56nsibYDcDU6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 26563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 253
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

_source line 14_

<details open><summary>🔧 Tool call — Write · `toolu_01CAosvWz3ubFT9eMmSLna9T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.py",
  "content": "\"\"\"R17 Task 2: Web-overlap per-subject k distribution from Li et al. (2024).\"\"\"\n\nimport pandas as pd\nimport numpy as np\nfrom pathlib import Path\n\nDATA = Path(__file__).parent.parent / \"mmlu_li2024_proxy_labels.csv\"\nOUT = Path(__file__).parent / \"web_overlap_k_distribution.md\"\n\ndf = pd.read_csv(DATA)\n\n# --- Exclude no_annotation items ---\nno_ann = df[df[\"contamination_type\"] == \"no_annotation\"]\ndf_ann = df[df[\"contamination_type\"] != \"no_annotation\"].copy()\n\n# --- Per-subject stats ---\nrecords = []\nfor subj, g in df_ann.groupby(\"subject\"):\n    n_total = len(g)\n    n_contam = g[\"is_contaminated\"].sum()\n    prevalence = n_contam / n_total * 100\n    records.append({\n        \"subject\": subj,\n        \"n_items_total\": n_total,\n        \"n_contaminated\": int(n_contam),\n        \"prevalence_pct\": round(prevalence, 1),\n    })\n\ntbl = pd.DataFrame(records).sort_values(\"prevalence_pct\", ascending=False).reset_index(drop=True)\n\n# --- Summary stats ---\nprev = tbl[\"prevalence_pct\"]\nsummary = {\n    \"n_subjects_with_data\": len(tbl),\n    \"mean\": round(prev.mean(), 1),\n    \"median\": round(prev.median(), 1),\n    \"std\": round(prev.std(), 1),\n    \"Q25\": round(prev.quantile(0.25), 1),\n    \"Q75\": round(prev.quantile(0.75), 1),\n    \"min\": round(prev.min(), 1),\n    \"max\": round(prev.max(), 1),\n    \"n_prev_gt50\": int((prev > 50).sum()),\n    \"n_prev_gt25\": int((prev > 25).sum()),\n    \"n_prev_gt10\": int((prev > 10).sum()),\n    \"n_prev_eq0\": int((prev == 0).sum()),\n    \"n_prev_gt0\": int((prev > 0).sum()),\n}\n\n# --- Check subjects missing entirely (all no_annotation) ---\nall_subjects = df[\"subject\"].unique()\nannotated_subjects = df_ann[\"subject\"].unique()\nmissing_subjects = sorted(set(all_subjects) - set(annotated_subjects))\n\n# --- Write report ---\nlines = []\nlines.append(\"# Web-Overlap Per-Subject Contamination Distribution (Li et al. 2024)\")\nlines.append(\"\")\nlines.append(\"## Data\")\nlines.append(f\"- Source: `mmlu_li2024_proxy_labels.csv` (Li et al. 2024, EMNLP)\")\nlines.append(f\"- Total items: {len(df)}\")\nlines.append(f\"- Items with annotation: {len(df_ann)} (excluded {len(no_ann)} `no_annotation`)\")\nlines.append(f\"- Subjects with annotated data: {len(tbl)} / 57\")\nlines.append(\"\")\n\nif missing_subjects:\n    lines.append(\"### Subjects with no annotated items (all `no_annotation`)\")\n    for s in missing_subjects:\n        lines.append(f\"- {s}\")\n    lines.append(\"\")\n\nlines.append(\"## Per-Subject Table (sorted by prevalence descending)\")\nlines.append(\"\")\nlines.append(\"| # | Subject | n_items | n_contam | prevalence% |\")\nlines.append(\"|---|---------|---------|----------|-------------|\")\nfor i, row in tbl.iterrows():\n    lines.append(f\"| {i+1} | {row['subject']} | {row['n_items_total']} | {row['n_contaminated']} | {row['prevalence_pct']:.1f}% |\")\nlines.append(\"\")\n\nlines.append(\"## Summary Statistics\")\nlines.append(\"\")\nlines.append(\"| Metric | Value |\")\nlines.append(\"|--------|-------|\")\nlines.append(f\"| Subjects with data | {summary['n_subjects_with_data']} |\")\nlines.append(f\"| Mean prevalence | {summary['mean']}% |\")\nlines.append(f\"| Median prevalence | {summary['median']}% |\")\nlines.append(f\"| Std | {summary['std']}% |\")\nlines.append(f\"| Q25 | {summary['Q25']}% |\")\nlines.append(f\"| Q75 | {summary['Q75']}% |\")\nlines.append(f\"| Min | {summary['min']}% |\")\nlines.append(f\"| Max | {summary['max']}% |\")\nlines.append(f\"| Subjects with prevalence > 50% | {summary['n_prev_gt50']} |\")\nlines.append(f\"| Subjects with prevalence > 25% | {summary['n_prev_gt25']} |\")\nlines.append(f\"| Subjects with prevalence > 10% | {summary['n_prev_gt10']} |\")\nlines.append(f\"| Subjects with prevalence = 0% | {summary['n_prev_eq0']} |\")\nlines.append(\"\")\n\nlines.append(\"## k-Parameter Constraint\")\nlines.append(\"\")\nlines.append(f\"In `plan_034_multi_subject_injection`, k = number of simultaneously contaminated subjects.\")\nlines.append(\"\")\nlines.append(f\"From Li et al. web-overlap data:\")\nlines.append(f\"- **{summary['n_prev_gt0']} / 57 subjects** show contamination evidence (prevalence > 0%)\")\nlines.append(f\"- This provides an empirical upper bound of **k ≤ {summary['n_prev_gt0']}**\")\nlines.append(f\"- However, prevalence varies widely: median {summary['median']}%, range [{summary['min']}%, {summary['max']}%]\")\nlines.append(f\"- {summary['n_prev_gt50']} subjects have majority-contaminated items (>50%)\")\nlines.append(f\"- {summary['n_prev_gt25']} subjects have substantial contamination (>25%)\")\nlines.append(\"\")\nlines.append(\"The distribution suggests that contamination is **pervasive across subjects** rather than concentrated in a few, \")\nlines.append(\"supporting the use of high k values (k ≥ 30) in multi-subject injection simulations.\")\n\nOUT.write_text(\"\\n\".join(lines) + \"\\n\")\nprint(f\"Report written to {OUT}\")\nprint()\nprint(\"=== SUMMARY ===\")\nfor k, v in summary.items():\n    print(f\"  {k}: {v}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "8a7440bb-086f-4f8a-b65b-17689e753246",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011rhFeRnHC56nsibYDcDU6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 253,
      "cache_read_input_tokens": 26563,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 253
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

_source line 15 · 2026-05-23T12:09:25.657Z_

<details><summary>↩ Tool result · `toolu_01CAosvWz3ubFT9eMmSLna9T`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "03ebecba-b14e-4e0e-b310-c2cee2692986",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.py",
    "content": "\"\"\"R17 Task 2: Web-overlap per-subject k distribution from Li et al. (2024).\"\"\"\n\nimport pandas as pd\nimport numpy as np\nfrom pathlib import Path\n\nDATA = Path(__file__).parent.parent / \"mmlu_li2024_proxy_labels.csv\"\nOUT = Path(__file__).parent / \"web_overlap_k_distribution.md\"\n\ndf = pd.read_csv(DATA)\n\n# --- Exclude no_annotation items ---\nno_ann = df[df[\"contamination_type\"] == \"no_annotation\"]\ndf_ann = df[df[\"contamination_type\"] != \"no_annotation\"].copy()\n\n# --- Per-subject stats ---\nrecords = []\nfor subj, g in df_ann.groupby(\"subject\"):\n    n_total = len(g)\n    n_contam = g[\"is_contaminated\"].sum()\n    prevalence = n_contam / n_total * 100\n    records.append({\n        \"subject\": subj,\n        \"n_items_total\": n_total,\n        \"n_contaminated\": int(n_contam),\n        \"prevalence_pct\": round(prevalence, 1),\n    })\n\ntbl = pd.DataFrame(records).sort_values(\"prevalence_pct\", ascending=False).reset_index(drop=True)\n\n# --- Summary stats ---\nprev = tbl[\"prevalence_pct\"]\nsummary = {\n    \"n_subjects_with_data\": len(tbl),\n    \"mean\": round(prev.mean(), 1),\n    \"median\": round(prev.median(), 1),\n    \"std\": round(prev.std(), 1),\n    \"Q25\": round(prev.quantile(0.25), 1),\n    \"Q75\": round(prev.quantile(0.75), 1),\n    \"min\": round(prev.min(), 1),\n    \"max\": round(prev.max(), 1),\n    \"n_prev_gt50\": int((prev > 50).sum()),\n    \"n_prev_gt25\": int((prev > 25).sum()),\n    \"n_prev_gt10\": int((prev > 10).sum()),\n    \"n_prev_eq0\": int((prev == 0).sum()),\n    \"n_prev_gt0\": int((prev > 0).sum()),\n}\n\n# --- Check subjects missing entirely (all no_annotation) ---\nall_subjects = df[\"subject\"].unique()\nannotated_subjects = df_ann[\"subject\"].unique()\nmissing_subjects = sorted(set(all_subjects) - set(annotated_subjects))\n\n# --- Write report ---\nlines = []\nlines.append(\"# Web-Overlap Per-Subject Contamination Distribution (Li et al. 2024)\")\nlines.append(\"\")\nlines.append(\"## Data\")\nlines.append(f\"- Source: `mmlu_li2024_proxy_labels.csv` (Li et al. 2024, EMNLP)\")\nlines.append(f\"- Total items: {len(df)}\")\nlines.append(f\"- Items with annotation: {len(df_ann)} (excluded {len(no_ann)} `no_annotation`)\")\nlines.append(f\"- Subjects with annotated data: {len(tbl)} / 57\")\nlines.append(\"\")\n\nif missing_subjects:\n    lines.append(\"### Subjects with no annotated items (all `no_annotation`)\")\n    for s in missing_subjects:\n        lines.append(f\"- {s}\")\n    lines.append(\"\")\n\nlines.append(\"## Per-Subject Table (sorted by prevalence descending)\")\nlines.append(\"\")\nlines.append(\"| # | Subject | n_items | n_contam | prevalence% |\")\nlines.append(\"|---|---------|---------|----------|-------------|\")\nfor i, row in tbl.iterrows():\n    lines.append(f\"| {i+1} | {row['subject']} | {row['n_items_total']} | {row['n_contaminated']} | {row['prevalence_pct']:.1f}% |\")\nlines.append(\"\")\n\nlines.append(\"## Summary Statistics\")\nlines.append(\"\")\nlines.append(\"| Metric | Value |\")\nlines.append(\"|--------|-------|\")\nlines.append(f\"| Subjects with data | {summary['n_subjects_with_data']} |\")\nlines.append(f\"| Mean prevalence | {summary['mean']}% |\")\nlines.append(f\"| Median prevalence | {summary['median']}% |\")\nlines.append(f\"| Std | {summary['std']}% |\")\nlines.append(f\"| Q25 | {summary['Q25']}% |\")\nlines.append(f\"| Q75 | {summary['Q75']}% |\")\nlines.append(f\"| Min | {summary['min']}% |\")\nlines.append(f\"| Max | {summary['max']}% |\")\nlines.append(f\"| Subjects with prevalence > 50% | {summary['n_prev_gt50']} |\")\nlines.append(f\"| Subjects with prevalence > 25% | {summary['n_prev_gt25']} |\")\nlines.append(f\"| Subjects with prevalence > 10% | {summary['n_prev_gt10']} |\")\nlines.append(f\"| Subjects with prevalence = 0% | {summary['n_prev_eq0']} |\")\nlines.append(\"\")\n\nlines.append(\"## k-Parameter Constraint\")\nlines.append(\"\")\nlines.append(f\"In `plan_034_multi_subject_injection`, k = number of simultaneously contaminated subjects.\")\nlines.append(\"\")\nlines.append(f\"From Li et al. web-overlap data:\")\nlines.append(f\"- **{summary['n_prev_gt0']} / 57 subjects** show contamination evidence (prevalence > 0%)\")\nlines.append(f\"- This provides an empirical upper bound of **k ≤ {summary['n_prev_gt0']}**\")\nlines.append(f\"- However, prevalence varies widely: median {summary['median']}%, range [{summary['min']}%, {summary['max']}%]\")\nlines.append(f\"- {summary['n_prev_gt50']} subjects have majority-contaminated items (>50%)\")\nlines.append(f\"- {summary['n_prev_gt25']} subjects have substantial contamination (>25%)\")\nlines.append(\"\")\nlines.append(\"The distribution suggests that contamination is **pervasive across subjects** rather than concentrated in a few, \")\nlines.append(\"supporting the use of high k values (k ≥ 30) in multi-subject injection simulations.\")\n\nOUT.write_text(\"\\n\".join(lines) + \"\\n\")\nprint(f\"Report written to {OUT}\")\nprint()\nprint(\"=== SUMMARY ===\")\nfor k, v in summary.items():\n    print(f\"  {k}: {v}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01PyrmPGsU9ff1N7ZpKFmz5r`</summary>

```json
{
  "command": "python3 artifacts/r17_evidence/web_overlap_k_distribution.py",
  "description": "Run the analysis script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "edbad2d0-275f-417c-bd4e-223e84bafcb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FUPdG23sYXaY7J3iGRUefU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1900,
      "cache_read_input_tokens": 26816,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1900
      },
      "output_tokens": 62,
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

_source line 17 · 2026-05-23T12:09:28.797Z_

<details><summary>↩ Tool result · `toolu_01PyrmPGsU9ff1N7ZpKFmz5r`</summary>

```text
Report written to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.md

=== SUMMARY ===
  n_subjects_with_data: 57
  mean: 38.4
  median: 39.8
  std: 20.8
  Q25: 23.4
  Q75: 54.4
  min: 0.0
  max: 76.4
  n_prev_gt50: 16
  n_prev_gt25: 41
  n_prev_gt10: 50
  n_prev_eq0: 3
  n_prev_gt0: 54
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "39e47967-397d-4e24-b575-267bf622c238",
  "tool_use_result": {
    "stdout": "Report written to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.md\n\n=== SUMMARY ===\n  n_subjects_with_data: 57\n  mean: 38.4\n  median: 39.8\n  std: 20.8\n  Q25: 23.4\n  Q75: 54.4\n  min: 0.0\n  max: 76.4\n  n_prev_gt50: 16\n  n_prev_gt25: 41\n  n_prev_gt10: 50\n  n_prev_eq0: 3\n  n_prev_gt0: 54",
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

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01VivjYLL5QzHhvw1JpkTjZ6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "c9e3ac6a-c9d7-4edd-82e4-7c4335514b54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y9so59koyvp8pLBvwwHWgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 286,
      "cache_read_input_tokens": 28716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 286
      },
      "output_tokens": 61,
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

_source line 19 · 2026-05-23T12:09:30.709Z_

<details><summary>↩ Tool result · `toolu_01VivjYLL5QzHhvw1JpkTjZ6`</summary>

```text
1	# Web-Overlap Per-Subject Contamination Distribution (Li et al. 2024)
2	
3	## Data
4	- Source: `mmlu_li2024_proxy_labels.csv` (Li et al. 2024, EMNLP)
5	- Total items: 12508
6	- Items with annotation: 9229 (excluded 3279 `no_annotation`)
7	- Subjects with annotated data: 57 / 57
8	
9	## Per-Subject Table (sorted by prevalence descending)
10	
11	| # | Subject | n_items | n_contam | prevalence% |
12	|---|---------|---------|----------|-------------|
13	| 1 | college_physics | 72 | 55 | 76.4% |
14	| 2 | high_school_physics | 121 | 87 | 71.9% |
15	| 3 | philosophy | 254 | 180 | 70.9% |
16	| 4 | professional_accounting | 241 | 163 | 67.6% |
17	| 5 | conceptual_physics | 201 | 135 | 67.2% |
18	| 6 | high_school_microeconomics | 219 | 143 | 65.3% |
19	| 7 | management | 91 | 58 | 63.7% |
20	| 8 | moral_disputes | 259 | 165 | 63.7% |
21	| 9 | high_school_macroeconomics | 269 | 171 | 63.6% |
22	| 10 | high_school_psychology | 282 | 179 | 63.5% |
23	| 11 | anatomy | 121 | 72 | 59.5% |
24	| 12 | college_chemistry | 81 | 47 | 58.0% |
25	| 13 | business_ethics | 91 | 51 | 56.0% |
26	| 14 | high_school_statistics | 180 | 100 | 55.6% |
27	| 15 | high_school_biology | 261 | 142 | 54.4% |
28	| 16 | high_school_geography | 183 | 98 | 53.6% |
29	| 17 | marketing | 222 | 110 | 49.5% |
30	| 18 | medical_genetics | 83 | 40 | 48.2% |
31	| 19 | electrical_engineering | 126 | 59 | 46.8% |
32	| 20 | high_school_chemistry | 180 | 84 | 46.7% |
33	| 21 | sociology | 185 | 86 | 46.5% |
34	| 22 | high_school_government_and_politics | 188 | 87 | 46.3% |
35	| 23 | jurisprudence | 100 | 46 | 46.0% |
36	| 24 | elementary_mathematics | 239 | 109 | 45.6% |
37	| 25 | econometrics | 102 | 44 | 43.1% |
38	| 26 | computer_security | 86 | 37 | 43.0% |
39	| 27 | prehistory | 248 | 106 | 42.7% |
40	| 28 | college_mathematics | 71 | 29 | 40.8% |
41	| 29 | nutrition | 259 | 103 | 39.8% |
42	| 30 | virology | 149 | 56 | 37.6% |
43	| 31 | high_school_computer_science | 93 | 35 | 37.6% |
44	| 32 | machine_learning | 86 | 32 | 37.2% |
45	| 33 | international_law | 103 | 38 | 36.9% |
46	| 34 | college_medicine | 157 | 57 | 36.3% |
47	| 35 | high_school_mathematics | 196 | 69 | 35.2% |
48	| 36 | clinical_knowledge | 240 | 83 | 34.6% |
49	| 37 | college_biology | 132 | 45 | 34.1% |
50	| 38 | public_relations | 97 | 33 | 34.0% |
51	| 39 | college_computer_science | 84 | 26 | 31.0% |
52	| 40 | formal_logic | 108 | 29 | 26.9% |
53	| 41 | us_foreign_policy | 95 | 25 | 26.3% |
54	| 42 | astronomy | 135 | 32 | 23.7% |
55	| 43 | world_religions | 158 | 37 | 23.4% |
56	| 44 | security_studies | 229 | 52 | 22.7% |
57	| 45 | professional_medicine | 213 | 40 | 18.8% |
58	| 46 | logical_fallacies | 150 | 28 | 18.7% |
59	| 47 | miscellaneous | 286 | 47 | 16.4% |
60	| 48 | human_sexuality | 115 | 16 | 13.9% |
61	| 49 | abstract_algebra | 90 | 12 | 13.3% |
62	| 50 | professional_psychology | 279 | 31 | 11.1% |
63	| 51 | global_facts | 82 | 8 | 9.8% |
64	| 52 | human_aging | 202 | 14 | 6.9% |
65	| 53 | professional_law | 358 | 12 | 3.4% |
66	| 54 | high_school_world_history | 60 | 2 | 3.3% |
67	| 55 | high_school_european_history | 39 | 0 | 0.0% |
68	| 56 | high_school_us_history | 40 | 0 | 0.0% |
69	| 57 | moral_scenarios | 238 | 0 | 0.0% |
70	
71	## Summary Statistics
72	
73	| Metric | Value |
74	|--------|-------|
75	| Subjects with data | 57 |
76	| Mean prevalence | 38.4% |
77	| Median prevalence | 39.8% |
78	| Std | 20.8% |
79	| Q25 | 23.4% |
80	| Q75 | 54.4% |
81	| Min | 0.0% |
82	| Max | 76.4% |
83	| Subjects with prevalence > 50% | 16 |
84	| Subjects with prevalence > 25% | 41 |
85	| Subjects with prevalence > 10% | 50 |
86	| Subjects with prevalence = 0% | 3 |
87	
88	## k-Parameter Constraint
89	
90	In `plan_034_multi_subject_injection`, k = number of simultaneously contaminated subjects.
91	
92	From Li et al. web-overlap data:
93	- **54 / 57 subjects** show contamination evidence (prevalence > 0%)
94	- This provides an empirical upper bound of **k ≤ 54**
95	- However, prevalence varies widely: median 39.8%, range [0.0%, 76.4%]
96	- 16 subjects have majority-contaminated items (>50%)
97	- 41 subjects have substantial contamination (>25%)
98	
99	The distribution suggests that contamination is **pervasive across subjects** rather than concentrated in a few, 
100	supporting the use of high k values (k ≥ 30) in multi-subject injection simulations.
101	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "6dfe458f-e34d-4ac4-9140-122263fc252e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r17_evidence/web_overlap_k_distribution.md",
      "content": "# Web-Overlap Per-Subject Contamination Distribution (Li et al. 2024)\n\n## Data\n- Source: `mmlu_li2024_proxy_labels.csv` (Li et al. 2024, EMNLP)\n- Total items: 12508\n- Items with annotation: 9229 (excluded 3279 `no_annotation`)\n- Subjects with annotated data: 57 / 57\n\n## Per-Subject Table (sorted by prevalence descending)\n\n| # | Subject | n_items | n_contam | prevalence% |\n|---|---------|---------|----------|-------------|\n| 1 | college_physics | 72 | 55 | 76.4% |\n| 2 | high_school_physics | 121 | 87 | 71.9% |\n| 3 | philosophy | 254 | 180 | 70.9% |\n| 4 | professional_accounting | 241 | 163 | 67.6% |\n| 5 | conceptual_physics | 201 | 135 | 67.2% |\n| 6 | high_school_microeconomics | 219 | 143 | 65.3% |\n| 7 | management | 91 | 58 | 63.7% |\n| 8 | moral_disputes | 259 | 165 | 63.7% |\n| 9 | high_school_macroeconomics | 269 | 171 | 63.6% |\n| 10 | high_school_psychology | 282 | 179 | 63.5% |\n| 11 | anatomy | 121 | 72 | 59.5% |\n| 12 | college_chemistry | 81 | 47 | 58.0% |\n| 13 | business_ethics | 91 | 51 | 56.0% |\n| 14 | high_school_statistics | 180 | 100 | 55.6% |\n| 15 | high_school_biology | 261 | 142 | 54.4% |\n| 16 | high_school_geography | 183 | 98 | 53.6% |\n| 17 | marketing | 222 | 110 | 49.5% |\n| 18 | medical_genetics | 83 | 40 | 48.2% |\n| 19 | electrical_engineering | 126 | 59 | 46.8% |\n| 20 | high_school_chemistry | 180 | 84 | 46.7% |\n| 21 | sociology | 185 | 86 | 46.5% |\n| 22 | high_school_government_and_politics | 188 | 87 | 46.3% |\n| 23 | jurisprudence | 100 | 46 | 46.0% |\n| 24 | elementary_mathematics | 239 | 109 | 45.6% |\n| 25 | econometrics | 102 | 44 | 43.1% |\n| 26 | computer_security | 86 | 37 | 43.0% |\n| 27 | prehistory | 248 | 106 | 42.7% |\n| 28 | college_mathematics | 71 | 29 | 40.8% |\n| 29 | nutrition | 259 | 103 | 39.8% |\n| 30 | virology | 149 | 56 | 37.6% |\n| 31 | high_school_computer_science | 93 | 35 | 37.6% |\n| 32 | machine_learning | 86 | 32 | 37.2% |\n| 33 | international_law | 103 | 38 | 36.9% |\n| 34 | college_medicine | 157 | 57 | 36.3% |\n| 35 | high_school_mathematics | 196 | 69 | 35.2% |\n| 36 | clinical_knowledge | 240 | 83 | 34.6% |\n| 37 | college_biology | 132 | 45 | 34.1% |\n| 38 | public_relations | 97 | 33 | 34.0% |\n| 39 | college_computer_science | 84 | 26 | 31.0% |\n| 40 | formal_logic | 108 | 29 | 26.9% |\n| 41 | us_foreign_policy | 95 | 25 | 26.3% |\n| 42 | astronomy | 135 | 32 | 23.7% |\n| 43 | world_religions | 158 | 37 | 23.4% |\n| 44 | security_studies | 229 | 52 | 22.7% |\n| 45 | professional_medicine | 213 | 40 | 18.8% |\n| 46 | logical_fallacies | 150 | 28 | 18.7% |\n| 47 | miscellaneous | 286 | 47 | 16.4% |\n| 48 | human_sexuality | 115 | 16 | 13.9% |\n| 49 | abstract_algebra | 90 | 12 | 13.3% |\n| 50 | professional_psychology | 279 | 31 | 11.1% |\n| 51 | global_facts | 82 | 8 | 9.8% |\n| 52 | human_aging | 202 | 14 | 6.9% |\n| 53 | professional_law | 358 | 12 | 3.4% |\n| 54 | high_school_world_history | 60 | 2 | 3.3% |\n| 55 | high_school_european_history | 39 | 0 | 0.0% |\n| 56 | high_school_us_history | 40 | 0 | 0.0% |\n| 57 | moral_scenarios | 238 | 0 | 0.0% |\n\n## Summary Statistics\n\n| Metric | Value |\n|--------|-------|\n| Subjects with data | 57 |\n| Mean prevalence | 38.4% |\n| Median prevalence | 39.8% |\n| Std | 20.8% |\n| Q25 | 23.4% |\n| Q75 | 54.4% |\n| Min | 0.0% |\n| Max | 76.4% |\n| Subjects with prevalence > 50% | 16 |\n| Subjects with prevalence > 25% | 41 |\n| Subjects with prevalence > 10% | 50 |\n| Subjects with prevalence = 0% | 3 |\n\n## k-Parameter Constraint\n\nIn `plan_034_multi_subject_injection`, k = number of simultaneously contaminated subjects.\n\nFrom Li et al. web-overlap data:\n- **54 / 57 subjects** show contamination evidence (prevalence > 0%)\n- This provides an empirical upper bound of **k ≤ 54**\n- However, prevalence varies widely: median 39.8%, range [0.0%, 76.4%]\n- 16 subjects have majority-contaminated items (>50%)\n- 41 subjects have substantial contamination (>25%)\n\nThe distribution suggests that contamination is **pervasive across subjects** rather than concentrated in a few, \nsupporting the use of high k values (k ≥ 30) in multi-subject injection simulations.\n",
      "numLines": 101,
      "startLine": 1,
      "totalLines": 101
    }
  }
}
```

</details>

---

### Assistant

_source line 20_

分析完成。

**结果概要：**

- 57 个 subject 全部有标注数据，其中 **54 个** 检出 contamination（prevalence > 0%），仅 3 个为 0%（high_school_european_history, high_school_us_history, moral_scenarios）
- Prevalence 分布：mean 38.4%, median 39.8%, 范围 [0%, 76.4%]，标准差 20.8%
- 16 个 subject 超过 50%，41 个超过 25%，50 个超过 10%
- **k 参数约束**：经验上界 k ≤ 54，contamination 跨 subject 分布极广泛，支持在模拟中使用高 k 值（k ≥ 30）

输出文件：
- `artifacts/r17_evidence/web_overlap_k_distribution.py` — 分析脚本
- `artifacts/r17_evidence/web_overlap_k_distribution.md` — 完整报告

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "uuid": "73e326c3-74e3-43ae-9b78-403411901783",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0197FsXqgHXkaBfNw2Qdd1hr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2233,
      "cache_read_input_tokens": 29002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2233
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

_source line 21_

分析完成。

**结果概要：**

- 57 个 subject 全部有标注数据，其中 **54 个** 检出 contamination（prevalence > 0%），仅 3 个为 0%（high_school_european_history, high_school_us_history, moral_scenarios）
- Prevalence 分布：mean 38.4%, median 39.8%, 范围 [0%, 76.4%]，标准差 20.8%
- 16 个 subject 超过 50%，41 个超过 25%，50 个超过 10%
- **k 参数约束**：经验上界 k ≤ 54，contamination 跨 subject 分布极广泛，支持在模拟中使用高 k 值（k ≥ 30）

输出文件：
- `artifacts/r17_evidence/web_overlap_k_distribution.py` — 分析脚本
- `artifacts/r17_evidence/web_overlap_k_distribution.md` — 完整报告

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 50177,
  "duration_api_ms": 49927,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "89cb2f44-5f1a-425b-abf9-f93a47c54076",
  "total_cost_usd": 0.2706765,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 19394,
    "cache_read_input_tokens": 147874,
    "output_tokens": 2970,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19394,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 282,
        "cache_read_input_tokens": 29002,
        "cache_creation_input_tokens": 2233,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2233
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1132,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001237,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 2970,
      "cacheReadInputTokens": 147874,
      "cacheCreationInputTokens": 19394,
      "webSearchRequests": 0,
      "costUSD": 0.2694395,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5953f90f-4da2-4a2b-a339-6d3d45493b20"
}
```

</details>

---
