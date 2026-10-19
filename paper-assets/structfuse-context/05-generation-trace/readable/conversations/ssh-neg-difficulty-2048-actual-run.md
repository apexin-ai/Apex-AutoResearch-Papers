# ssh neg difficulty 2048 actual run

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 41
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/chats/worker_ssh_neg_difficulty_2048_actual_run_20260513T224719.jsonl`
- **Structured JSON:** [`381e93351de01940094a.json`](../../sessions/38/381e93351de01940094a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

41 recorded events

### Tool call

_source line 1 · 2026-05-13T22:48:55.349155+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-13T22:48:55.349496+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-13T22:48:55.349703+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -name \"negative_difficulty*\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -name \"negative_difficulty*\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-13T22:48:55.349859+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-13T22:48:55.349992+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -name \"stats_v*\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -name \"stats_v*\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-13T22:48:55.350118+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-13T22:48:55.350238+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp -name \"stats_v*\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp -name \"stats_v*\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-13T22:48:55.350356+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-13T22:48:55.350501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -name \"negative_difficulty*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -name \"negative_difficulty*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T22:48:55.350638+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -name \"stats_v*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -name \"stats_v*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-13T22:48:55.350765+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.12}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T22:48:55.350891+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp -name \"stats_v*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp -name \"stats_v*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-13T22:48:55.351009+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-13T22:48:55.351121+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T22:48:55.351258+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/negative_difficulty*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/negative_difficulty*"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T22:48:55.351371+00:00_

artifacts/_project/chart/negative_difficulty_charts_index.txt
artifacts/_project/data/negative_difficulty_stats.txt
artifacts/_project/chart/negative_difficulty_margin_charts_index.txt
artifacts/_project/data/negative_difficulty_stats_v2.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T22:48:55.351510+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/stats_v*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/stats_v*"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T22:48:55.351708+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-13T22:48:55.351842+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/structfuse/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-13T22:48:55.351972+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis\\nartifacts\\nauto_start_dataflow.sh\\neval_checkpoint.py\\nevaluation\\nextraction\\nmvp_phase1.py\\nmvp_phase1.py.bak\\nrequirements.txt\\nresults\\nrun_m2_early_pilot.sh\\nrun_m2_embed_verify.sh\\nrun_m2_embed_verify_continuation.sh\\nrun_m2_full_qwen.sh\\nrun_m2_full_starcoder.sh\\nrun_plan013_dataflow_retry.sh\\nrun_plan013_starcoder.sh\\nrun_starcoder_data_build.sh\\nscripts\\ntea_debug.log\\ntraining\\nwandb\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-13T22:48:55.352120+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/structfuse -name \"*.py\" -path \"*negative*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/structfuse -name \"*.py\" -path \"*negative*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T22:48:55.352242+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-13T22:48:55.352394+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats_v2.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats_v2.txt"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-13T22:48:55.352518+00:00_

1	Full stats JSON saved at bjb1-42106:/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json
2	
3	Summary table:
4	Strategy             Encoder     Pos Sim  Neg Sim  Margin  Margin Std  %Pos>Neg
5	Random               Qwen        0.9804   0.8988   0.0816  0.2299      77.8%
6	Random               StarCoder   0.7568   0.5529   0.2039  0.3237      72.8%
7	Embedding Distance   Qwen        0.9804   0.9595   0.0209  0.1149      60.7%
8	Embedding Distance   StarCoder   0.7838   0.6679   0.1159  0.2559      59.2%
9	Dataflow-Aware       Qwen        0.9805   0.9496   0.0309  0.1406      67.4%
10	Dataflow-Aware       StarCoder   0.7609   0.6587   0.1022  0.2574      62.8%
11	
12	StarCoder/Qwen margin ratio: Random 2.50x, Embedding 5.54x, Dataflow 3.30x

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-13T22:48:55.352668+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats.txt"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-13T22:48:55.352804+00:00_

1	Negative Difficulty Stats (pretrained encoders, bfloat16, max_length=128, seed=42)
2	
3	QWEN2.5-Coder-3B:
4	  random:             n=905, mean=0.8988, std=0.2297, median=0.9672, [p25=0.9420, p75=0.9786]
5	  embedding_distance: n=905, mean=0.9595, std=0.1142, median=0.9774, [p25=0.9654, p75=0.9858]
6	  dataflow_aware:     n=872, mean=0.9496, std=0.1403, median=0.9749, [p25=0.9617, p75=0.9830]
7	
8	STARCODER2-3B:
9	  random:             n=905, mean=0.5529, std=0.2845, median=0.6150, [p25=0.3879, p75=0.7649]
10	  embedding_distance: n=905, mean=0.6679, std=0.2670, median=0.7335, [p25=0.5416, p75=0.8573]
11	  dataflow_aware:     n=872, mean=0.6587, std=0.2535, median=0.7022, [p25=0.5317, p75=0.8457]
12	
13	CROSS-ENCODER DELTA (StarCoder - Qwen):
14	  random:             -0.3459
15	  embedding_distance: -0.2915
16	  dataflow_aware:     -0.2909
17	
18	Full JSON on server: bjb1-42106:/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-13T22:48:55.352926+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/scripts/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/structfuse/scripts/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-13T22:48:55.353053+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\nbuild_full_m2_data.sh\\nbuild_m1_training_data.py\\nbuild_m1_training_data.py.bak\\nbuild_p2b_data.py\\nclone_repos.sh\\ncollect_p2b_results.py\\ncompute_full_z_percent.py\\ndownload_metadata.py\\neval_p2b.py\\neval_p2b_pooled.py\\neval_swebench.py\\nfix_metadata.py\\nfix_metadata_arrow.py\\nmigrate_m1_data.sh\\nprepare_m1_rerun.py\\nrerun_m1_failed.sh\\nrun_50repo_overlap.py\\nrun_eval_5missing.sh\\nrun_eval_all.sh\\nrun_eval_p50.sh\\nrun_full_m2_training.sh\\nrun_m1_extraction.sh\\nrun_m2_pilot.sh\\nrun_p2b_all.sh\\nschedule_m2_runs.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-13T22:48:55.353177+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/evaluation/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/structfuse/evaluation/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-13T22:48:55.353291+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "ls /root/structfuse/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "ls /root/structfuse/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-13T22:48:55.353405+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"eval_retrieval.py\\neval_swebench.py\\neval_swebench.py.bak\\nlinear_proxy.py\\nlinear_proxy_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-13T22:48:55.353519+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"negative_difficulty.py\\nnegative_difficulty_margin.py\\nnegative_difficulty_margin_v2.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-13T22:48:55.353710+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/structfuse/analysis/negative_difficulty_margin_v2.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/structfuse/analysis/negative_difficulty_margin_v2.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-13T22:48:55.353996+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Negative difficulty margin analysis — MAX_LENGTH=2048 version.\\n\\nSame analysis as negative_difficulty_margin.py but with MAX_LENGTH=2048\\n(matching training config) instead of 128 to avoid ceiling effects.\\nCPU only — no GPU usage.\\n\\\"\\\"\\\"\\n\\nimport json\\nimport os\\nimport random\\nimport sys\\nimport time\\nfrom pathlib import Path\\n\\nimport numpy as np\\nimport torch\\nimport torch.nn.functional as F\\nfrom transformers import AutoModel, AutoTokenizer\\n\\nSTRATEGIES = [\\\"random\\\", \\\"embedding_distance\\\", \\\"dataflow_aware\\\"]\\nSTRATEGY_LABELS = {\\n    \\\"random\\\": \\\"Random\\\",\\n    \\\"embedding_distance\\\": \\\"Embedding Distance\\\",\\n    \\\"dataflow_aware\\\": \\\"Dataflow-Aware\\\",\\n}\\nSTRATEGY_COLORS = {\\n    \\\"random\\\": \\\"#4C72B0\\\",\\n    \\\"embedding_distance\\\": \\\"#DD8452\\\",\\n    \\\"dataflow_aware\\\": \\\"#55A868\\\",\\n}\\n\\nQWEN_DATA_DIR = \\\"/root/autodl-tmp/structfuse/full_m2_training_data\\\"\\nSTARCODER_DATA_DIR = \\\"/root/autodl-tmp/structfuse/full_m2_starcoder_data\\\"\\nQWEN_MODEL = \\\"/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B\\\"\\nSTARCODER_MODEL = \\\"/root/autodl-tmp/models/bigcode/starcoder2-3b/bigcode/starcoder2-3b\\\"\\nARTIFACT_DIR = \\\"/root/autodl-tmp/structfuse/artifacts\\\"\\n\\nMAX_LENGTH = 2048\\nDTYPE = torch.bfloat16\\n\\n\\ndef load_triplets(data_dir, strategy, n_queries, n_negs, seed=42):\\n    path = Path(data_dir) / f\\\"train_{strategy}_s{seed}.jsonl\\\"\\n    rng = random.Random(seed)\\n\\n    query_texts = []\\n    pos_texts = []\\n    neg_texts = []\\n    triplets = []\\n\\n    with open(path) as f:\\n        lines = f.readlines()\\n\\n    sampled_indices = rng.sample(range(len(lines)), min(n_queries, len(lines)))\\n\\n    for idx in sampled_indices:\\n        row = json.loads(lines[idx])\\n        q_text = row[\\\"query_tokens\\\"]\\n        p_text = row[\\\"pos_tokens\\\"]\\
…[truncated 7266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-13T22:48:55.354160+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "find /root/autodl-tmp/structfuse/artifacts -name \"negative_difficulty*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "find /root/autodl-tmp/structfuse/artifacts -name \"negative_difficulty*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-13T22:48:55.354308+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats.json\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_qwen.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_qwen.png\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_starcoder.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_starcoder.png\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_comparison.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_comparison.png\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_distribution.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_distribution.png\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_bars.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_bars.png\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_violin.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_violin.png\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_2048_distribution.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_2048_distribution.png\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_2048_bars.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_2048_bars.png\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_2048_violin.pdf\\n/root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_2048_violin.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-13T22:48:55.354468+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v3_2048.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-13T22:48:55.354680+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"qwen\\\": {\\n    \\\"random\\\": {\\n      \\\"n_pairs\\\": 905,\\n      \\\"max_length\\\": 2048,\\n      \\\"pos_sim_mean\\\": 0.98547,\\n      \\\"pos_sim_std\\\": 0.01104,\\n      \\\"pos_sim_median\\\": 0.98982,\\n      \\\"neg_sim_mean\\\": 0.91113,\\n      \\\"neg_sim_std\\\": 0.23157,\\n      \\\"neg_sim_median\\\": 0.9759,\\n      \\\"margin_mean\\\": 0.07434,\\n      \\\"margin_std\\\": 0.23218,\\n      \\\"margin_median\\\": 0.00987,\\n      \\\"margin_p25\\\": 0.00214,\\n      \\\"margin_p75\\\": 0.02424,\\n      \\\"margin_min\\\": -0.03052,\\n      \\\"margin_max\\\": 0.99731,\\n      \\\"pct_positive_margin\\\": 81.77\\n    },\\n    \\\"embedding_distance\\\": {\\n      \\\"n_pairs\\\": 905,\\n      \\\"max_length\\\": 2048,\\n      \\\"pos_sim_mean\\\": 0.98547,\\n      \\\"pos_sim_std\\\": 0.01104,\\n      \\\"pos_sim_median\\\": 0.98982,\\n      \\\"neg_sim_mean\\\": 0.96845,\\n      \\\"neg_sim_std\\\": 0.11347,\\n      \\\"neg_sim_median\\\": 0.98534,\\n      \\\"margin_mean\\\": 0.01703,\\n      \\\"margin_std\\\": 0.114,\\n      \\\"margin_median\\\": 0.00155,\\n      \\\"margin_p25\\\": -0.00284,\\n      \\\"margin_p75\\\": 0.00869,\\n      \\\"margin_min\\\": -0.03845,\\n      \\\"margin_max\\\": 0.99517,\\n      \\\"pct_positive_margin\\\": 58.78\\n    },\\n    \\\"dataflow_aware\\\": {\\n      \\\"n_pairs\\\": 872,\\n      \\\"max_length\\\": 2048,\\n      \\\"pos_sim_mean\\\": 0.98558,\\n      \\\"pos_sim_std\\\": 0.01069,\\n      \\\"pos_sim_median\\\": 0.98915,\\n      \\\"neg_sim_mean\\\": 0.9563,\\n      \\\"neg_sim_std\\\": 0.14011,\\n      \\\"neg_sim_median\\\": 0.98051,\\n      \\\"margin_mean\\\": 0.02928,\\n      \\\"margin_std\\\": 0.14073,\\n      \\\"margin_median\\\": 0.00573,\\n      \\\"margin_p25\\\": -0.00035,\\n      \\\"margin_p75\\\": 0.01492,\\n      \\\"margin_min\\\": -0.03052,\\n      \\\"margin_max\\\": 0.99731,\\n      \\\"pct_positive_margin\\\":
…[truncated 2098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-13T22:48:55.354842+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-42106",
  "command": "cat /root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-42106",
    "command": "cat /root/autodl-tmp/structfuse/artifacts/negative_difficulty_stats_v2.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-13T22:48:55.355028+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"qwen\\\": {\\n    \\\"random\\\": {\\n      \\\"n_pairs\\\": 905,\\n      \\\"pos_sim_mean\\\": 0.98038,\\n      \\\"pos_sim_std\\\": 0.01123,\\n      \\\"pos_sim_median\\\": 0.98321,\\n      \\\"neg_sim_mean\\\": 0.89876,\\n      \\\"neg_sim_std\\\": 0.2297,\\n      \\\"neg_sim_median\\\": 0.96722,\\n      \\\"margin_mean\\\": 0.08162,\\n      \\\"margin_std\\\": 0.22994,\\n      \\\"margin_median\\\": 0.01363,\\n      \\\"margin_p25\\\": 0.00133,\\n      \\\"margin_p75\\\": 0.03747,\\n      \\\"margin_min\\\": -0.0438,\\n      \\\"margin_max\\\": 0.99378,\\n      \\\"pct_positive_margin\\\": 77.79\\n    },\\n    \\\"embedding_distance\\\": {\\n      \\\"n_pairs\\\": 905,\\n      \\\"pos_sim_mean\\\": 0.98038,\\n      \\\"pos_sim_std\\\": 0.01123,\\n      \\\"pos_sim_median\\\": 0.98321,\\n      \\\"neg_sim_mean\\\": 0.95948,\\n      \\\"neg_sim_std\\\": 0.11424,\\n      \\\"neg_sim_median\\\": 0.97736,\\n      \\\"margin_mean\\\": 0.0209,\\n      \\\"margin_std\\\": 0.11491,\\n      \\\"margin_median\\\": 0.00355,\\n      \\\"margin_p25\\\": -0.00358,\\n      \\\"margin_p75\\\": 0.01353,\\n      \\\"margin_min\\\": -0.0438,\\n      \\\"margin_max\\\": 0.99378,\\n      \\\"pct_positive_margin\\\": 60.66\\n    },\\n    \\\"dataflow_aware\\\": {\\n      \\\"n_pairs\\\": 872,\\n      \\\"pos_sim_mean\\\": 0.98052,\\n      \\\"pos_sim_std\\\": 0.011,\\n      \\\"pos_sim_median\\\": 0.98321,\\n      \\\"neg_sim_mean\\\": 0.94958,\\n      \\\"neg_sim_std\\\": 0.1403,\\n      \\\"neg_sim_median\\\": 0.97495,\\n      \\\"margin_mean\\\": 0.03094,\\n      \\\"margin_std\\\": 0.14055,\\n      \\\"margin_median\\\": 0.00596,\\n      \\\"margin_p25\\\": -0.00154,\\n      \\\"margin_p75\\\": 0.0176,\\n      \\\"margin_min\\\": -0.0438,\\n      \\\"margin_max\\\": 0.99378,\\n      \\\"pct_positive_margin\\\": 67.43\\n    }\\n  },\\n  \\\"starcoder\\\": {\\n    \\\"random\\\": {\\n      \\\"n_pairs\\\": 905,\\n    
…[truncated 1889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-13T22:48:55.355251+00:00_

数据齐全，`stats_v3_2048.json` 实际已存在。以下是完整对比分析。

---

## 128 vs 2048 Token 对比结果

### 1. 完整 2048-Token 结果

| Strategy | Encoder | Pos Sim | Neg Sim | Margin | Margin Std | %Pos>Neg |
|---|---|---|---|---|---|---|
| Random | Qwen | **0.9855** | 0.9111 | 0.0743 | 0.2322 | 81.8% |
| Random | StarCoder | 0.7985 | 0.6045 | 0.1940 | 0.2788 | 78.0% |
| Embedding Distance | Qwen | **0.9855** | 0.9685 | 0.0170 | 0.1140 | 58.8% |
| Embedding Distance | StarCoder | 0.8079 | 0.7409 | 0.0670 | 0.2056 | 55.0% |
| Dataflow-Aware | Qwen | **0.9856** | 0.9563 | 0.0293 | 0.1407 | 73.9% |
| Dataflow-Aware | StarCoder | 0.8009 | 0.6818 | 0.1192 | 0.2264 | 70.4% |

### 2. 关键对比：Qwen pos_sim

| Strategy | 128-token | 2048-token | Delta |
|---|---|---|---|
| Random | 0.9804 | **0.9855** | **+0.0051** |
| Embedding Distance | 0.9804 | **0.9855** | **+0.0051** |
| Dataflow-Aware | 0.9805 | **0.9856** | **+0.0051** |

### 3. Margin 对比

| Strategy | Encoder | 128-token | 2048-token | Delta |
|---|---|---|---|---|
| Random | Qwen | 0.0816 | 0.0743 | -0.0073 |
| Random | StarCoder | 0.2039 | 0.1940 | -0.0099 |
| Embedding Distance | Qwen | 0.0209 | 0.0170 | -0.0039 |
| Embedding Distance | StarCoder | 0.1159 | 0.0670 | **-0.0489** |
| Dataflow-Aware | Qwen | 0.0309 | 0.0293 | -0.0016 |
| Dataflow-Aware | StarCoder | 0.1022 | 0.1192 | +0.0170 |

### 4. StarCoder/Qwen Margin Ratio

| Strategy | 128-token | 2048-token |
|---|---|---|
| Random | 2.50x | 2.61x |
| Embedding Distance | 5.54x | 3.94x |
| Dataflow-Aware | 3.30x | 4.07x |

---

## 核心结论

**Qwen pos_sim 在 2048 tokens 下为 0.9855，比 128-token 的 0.9804 反而更高（+0.005）。**

这明确回答了核心问题：

- Ceiling **不是**截断 artifact。增加 token 长度到 2048 后 pos_sim 不降反升。
- Ceiling 是 **Qwen 表征的结构性特征**——Qwen2.5-Coder-3B 的 pretrained representation space 将同仓库代码片段映射到极其接近的区域（cos_sim > 0.985），无论截断长度如何。
- 作为对照，StarCoder pos_sim 从 0.757-0.784（128t）上升到 0.799-0.808（2048t），变化幅度更大（+0.02~0.04），但绝对值远低于 Qwen，说明两个编码器的表征几何结构根本不同。

**对 D021 结论的影响**：

2048-token 结果**加强**了原有结论——Qwen 的 similarity ceiling 是其 pretrained representation 的内在属性，不是分析方法的 artifact。这使得 StructFuse 在 Qwen 上的 margin improvement 更有意义：在一个 pretrained space 几乎无法区分同仓库代码的编码器上，训练仍然能拉开正负样本距离。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ssh_neg_difficulty_2048_actual_run_20260513T224719"
}
```

</details>

---
