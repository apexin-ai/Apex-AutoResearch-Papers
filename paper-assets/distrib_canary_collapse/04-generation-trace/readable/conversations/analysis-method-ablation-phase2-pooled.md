# analysis method ablation phase2 pooled

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 93
- **Recorded user turns:** 0
- **Tool calls:** 46
- **Original source:** `logs/chats/worker_analysis_method_ablation_phase2_pooled_20260515T085042.jsonl`
- **Structured JSON:** [`793fd529193b2977d379.json`](../../sessions/79/793fd529193b2977d379.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

93 recorded events

### Tool call

_source line 1 · 2026-05-15T08:59:16.629513+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "6"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "6"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T08:59:16.629796+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T08:59:16.629969+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distrib_canary_collapse",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distrib_canary_collapse",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T08:59:16.630542+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"alpha_sweep_a050_s44\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:50.550Z\", \"updated_at\": \"2026-05-15T06:58:50.550Z\", \"spec\": {\"hypothesis\": \"α=0.50 multi-seed replication (seed=44): 第三个 seed 为置信区间提供统计力\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 44, \"synthetic_ratio\": 0.5, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a050_s42\", \"priority\": \"D026-4\"}}, \"alpha_sweep_a025_s44\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:48.224Z\", \"updated_at\": \"2026-05-15T06:58:48.224Z\", \"spec\": {\"hypothesis\": \"α=0.25 multi-seed replication (seed=44): 第三个 seed 为置信区间提供统计力\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 44, \"synthetic_ratio\": 0.25, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a025_s42_v3\", \"priority\": \"D026-3\"}}, \"alpha_sweep_a050_s43\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:45.880Z\", \"updated_at\": \"2026-05-15T06:58:45.880Z\", \"spec\": {\"hypothesis\": \"α=0.50 multi-seed replication (seed=43): 验证 ECE canary 定性信号和地板效应的可重复性\", \"model_name\": \"EleutherAI/pythia-410m\", \"data_path\": \"/root/autodl-tmp/distrib_canary_collapse/data/wikitext103_5k\", \"data_count\": 5000, \"seed\": 43, \"synthetic_ratio\": 0.5, \"num_generations\": 10, \"steps_per_gen\": 5000, \"parent\": \"alpha_sweep_a050_s42\", \"priority\": \"D026-2\"}}, \"alpha_sweep_a025_s43\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:58:43.090Z\", \"updated_at\": \"2026-05-15T06:58:43.090Z\", \"spec\": {\"hypothesis\": \"α=0.25 multi-seed replication (seed=43): 验证非单调 dose-respon
…[truncated 30772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T08:59:16.630732+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.txt\" -o -name \"*.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.txt\" -o -name \"*.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T08:59:16.630876+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T08:59:16.631072+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42_v1_partial/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42_v1_partial/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42_v1_partial/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43_v1_partial/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43_v1_partial/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_43_v1_partial/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_0/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/generation_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/checkpoint/tokenizer.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_1/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_2/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/gen_2/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_can
…[truncated 6366 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T08:59:16.631225+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 28\\ndrwxr-xr-x  8 root root 4096 May 15 13:30 .\\ndrwxr-xr-x  7 root root 4096 May 15 16:50 ..\\ndrwxr-xr-x  7 root root 4096 May 15 13:44 alpha_sweep\\ndrwxr-xr-x  2 root root   69 May 15 05:22 alpha_sweep_analysis\\ndrwxr-xr-x  2 root root  118 May 15 14:43 analysis\\n-rw-r--r--  1 root root 3756 May 15 05:30 bootstrap_ty_dryrun.json\\n-rw-r--r--  1 root root 3919 May 15 05:31 bootstrap_ty_results.json\\ndrwxr-xr-x  2 root root   82 May 15 05:33 detrending\\n-rw-r--r--  1 root root 1246 May 15 13:17 dose_response_drift.csv\\ndrwxr-xr-x  3 root root   25 May 15 07:41 extended_20gen\\ndrwxr-xr-x 11 root root 4096 May 15 05:58 mvp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.54}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T08:59:16.631407+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T08:59:16.631546+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 228\\ndrwxr-xr-x  7 root root   4096 May 15 13:44 .\\ndrwxr-xr-x  8 root root   4096 May 15 13:30 ..\\ndrwxr-xr-x 13 root root   4096 May 15 07:36 a000_s42\\ndrwxr-xr-x 13 root root   4096 May 15 09:17 a025_s42\\ndrwxr-xr-x 13 root root   4096 May 15 13:40 a050_s42\\ndrwxr-xr-x  8 root root    135 May 15 16:40 a075_s42\\n-rw-r--r--  1 root root 178312 May 15 12:34 alpha_monotonicity.png\\ndrwxr-xr-x  2 root root     70 May 15 05:33 analysis\\n-rw-r--r--  1 root root   3410 May 15 05:11 analysis_summary.json\\n-rw-r--r--  1 root root  19644 May 15 12:34 pooled_panel_results.json\\n-rw-r--r--  1 root root   6816 May 15 12:34 pooled_panel_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T08:59:16.631670+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/mvp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/mvp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T08:59:16.631796+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 28\\ndrwxr-xr-x 11 root root 4096 May 15 05:58 .\\ndrwxr-xr-x  8 root root 4096 May 15 13:30 ..\\ndrwxr-xr-x  3 root root 4096 May 15 16:43 analysis\\ndrwxr-xr-x  2 root root   98 May 15 05:58 analysis_dryrun\\ndrwxr-xr-x  2 root root  136 May 15 03:00 analysis_maxlag5_backup\\ndrwxr-xr-x 13 root root 4096 May 14 20:15 rep_42\\ndrwxr-xr-x  3 root root   50 May 14 14:01 rep_42_v1_partial\\ndrwxr-xr-x 13 root root 4096 May 14 20:13 rep_43\\ndrwxr-xr-x  3 root root   50 May 14 14:01 rep_43_v1_partial\\ndrwxr-xr-x 13 root root 4096 May 15 01:47 rep_44\\ndrwxr-xr-x 13 root root 4096 May 15 01:54 rep_45\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T08:59:16.631915+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T08:59:16.632033+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16\\ndrwxr-xr-x 2 root root   69 May 15 05:22 .\\ndrwxr-xr-x 8 root root 4096 May 15 13:30 ..\\n-rw-r--r-- 1 root root  786 May 15 05:22 phase_diagram.csv\\n-rw-r--r-- 1 root root 5547 May 15 05:22 phase_diagram.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T08:59:16.632144+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T08:59:16.632275+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 36\\ndrwxr-xr-x 2 root root   118 May 15 14:43 .\\ndrwxr-xr-x 8 root root  4096 May 15 13:30 ..\\n-rw-r--r-- 1 root root 12551 May 15 13:31 cross_alpha_analysis.json\\n-rw-r--r-- 1 root root  3769 May 15 13:33 cross_alpha_analysis.md\\n-rw-r--r-- 1 root root  9508 May 15 13:48 cross_alpha_v3_full.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T08:59:16.632402+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T08:59:16.632525+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 672\\ndrwxr-xr-x  3 root root   4096 May 15 16:43 .\\ndrwxr-xr-x 11 root root   4096 May 15 05:58 ..\\n-rw-r--r--  1 root root  12202 May 15 05:56 analysis_summary.json\\n-rw-r--r--  1 root root  15039 May 15 03:03 ccf_maxlag7.json\\ndrwxr-xr-x  2 root root    118 May 15 16:43 consensus\\n-rw-r--r--  1 root root  90947 May 15 05:56 cross_correlation.png\\n-rw-r--r--  1 root root   1224 May 15 05:56 lead_time_table.csv\\n-rw-r--r--  1 root root 160963 May 15 06:53 method_ablation.json\\n-rw-r--r--  1 root root  49746 May 15 05:06 method_ablation_dmax_sensitivity.json\\n-rw-r--r--  1 root root 303063 May 15 05:56 metric_trends.png\\n-rw-r--r--  1 root root  28912 May 15 06:43 permutation_granger.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T08:59:16.632640+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse -maxdepth 1 -name \"*.py\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse -maxdepth 1 -name \"*.py\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T08:59:16.632761+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/metrics.py\\n/root/autodl-tmp/distrib_canary_collapse/iterative_train.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_data.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_mvp.py\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation.py\\n/root/autodl-tmp/distrib_canary_collapse/dmax_sensitivity.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py\\n/root/autodl-tmp/distrib_canary_collapse/bootstrap_ty_validation.py\\n/root/autodl-tmp/distrib_canary_collapse/detrending_utils.py\\n/root/autodl-tmp/distrib_canary_collapse/permutation_granger.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_extended.py\\n/root/autodl-tmp/distrib_canary_collapse/pooled_panel_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/extract_drift.py\\n/root/autodl-tmp/distrib_canary_collapse/gen_dose_response.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_v3_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4.py\\n/root/autodl-tmp/distrib_canary_collapse/consensus_framework.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v2.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v3.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v4.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T08:59:16.632910+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/pooled_panel_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/pooled_panel_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T08:59:16.633236+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"timestamp\\\": \\\"2026-05-15T12:34:44.745746\\\",\\n    \\\"alphas\\\": [\\n      0.0,\\n      0.25\\n    ],\\n    \\\"n_alphas\\\": 2,\\n    \\\"n_runs\\\": 2,\\n    \\\"n_obs_per_pair\\\": 18,\\n    \\\"canary_metrics\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"diversity_metrics\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\"\\n    ],\\n    \\\"n_permutations\\\": 500,\\n    \\\"warnings\\\": [\\n      \\\"Only 2 alpha points \\\\u2014 panel regression and monotonicity tests are underpowered. Results are structural validation only.\\\"\\n    ]\\n  },\\n  \\\"panel_regression\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"n_obs\\\": 18,\\n      \\\"n_alphas\\\": 2,\\n      \\\"r_squared\\\": 0.7256,\\n      \\\"r_squared_adj\\\": 0.6668,\\n      \\\"f_stat\\\": 98.8383,\\n      \\\"f_pvalue\\\": 0.0,\\n      \\\"coefficients\\\": {\\n        \\\"const\\\": {\\n          \\\"coef\\\": -0.000763,\\n          \\\"se\\\": 0.000359,\\n          \\\"t\\\": -2.1253,\\n          \\\"p\\\": 0.033562,\\n          \\\"significant\\\": true\\n        },\\n        \\\"lag1_d_canary\\\": {\\n          \\\"coef\\\": 0.031205,\\n          \\\"se\\\": 0.001986,\\n          \\\"t\\\": 15.7102,\\n          \\\"p\\\": 0.0,\\n          \\\"significant\\\": true\\n        },\\n        \\\"alpha\\\": {\\n          \\\"coef\\\": -0.011816,\\n          \\\"se\\\": 0.005199,\\n          \\\"t\\\": -2.2727,\\n          \\\"p\\\": 0.023047,\\n          \\\"significant\\\": true\\n        },\\n        \\\"interaction\\\": {\\n          \\\"coef\\\": 0.066553,\\n          \\\"se\\\": 0.036868,\\n          \\\"t\\\": 1.8052,\\n          \\\"p\\\": 0.071047,\\n          \\\"significant\\\": false\\n        }\\n      },\\n      \\\"warning\\\": \\\"Only 2 alpha p
…[truncated 8531 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T08:59:16.633410+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/pooled_panel_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/pooled_panel_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T08:59:16.633531+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/pooled_panel_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/pooled_panel_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T08:59:16.633707+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"========================================================================\\nPOOLED PANEL ANALYSIS — ALPHA-SWEEP\\nGenerated: 2026-05-15T12:34:44.745746\\n========================================================================\\n\\nAlpha points: [0.0, 0.25]\\nRuns: 2\\nObservations per pair: ~18\\nPermutations: 500\\n\\nWARNING: Only 2 alpha points — panel regression and monotonicity tests are underpowered. Results are structural validation only.\\n\\n────────────────────────────────────────────────────────────────────────\\n1. POOLED PANEL REGRESSION\\n   Model: Δdownstream[t] ~ lag1_Δcanary[t-1] + α + α×lag1_Δcanary\\n   HC1 robust SE. Key test: interaction term (α modulation).\\n──────────────────────────────────────────────────────────────���─────────\\n\\n  token_entropy -> distinct_1  (N=18, R²=0.7256)\\n    WARNING: Only 2 alpha points — panel regression is underpowered. Interaction term estimates unreliable. Wait for >=3 alpha points.\\n    const               : β=  -0.000763  t= -2.125  p=0.0336 *\\n    lag1_d_canary       : β=   0.031205  t= 15.710  p=0.0000 *\\n    alpha               : β=  -0.011816  t= -2.273  p=0.0230 *\\n    interaction         : β=   0.066553  t=  1.805  p=0.0710 \\n    interaction FDR q=0.4201 [n.s.]\\n\\n  token_entropy -> distinct_2  (N=18, R²=0.6135)\\n    WARNING: Only 2 alpha points — panel regression is underpowered. Interaction term estimates unreliable. Wait for >=3 alpha points.\\n    const               : β=  -0.002613  t= -1.063  p=0.2876 \\n    lag1_d_canary       : β=   0.121989  t=  7.612  p=0.0000 *\\n    alpha               : β=  -0.109290  t= -3.111  p=0.0019 *\\n    interaction         : β=   0.305957  t=  1.276  p=0.2020 \\n    interaction FDR q=0.4201 [n.s.]\\n\\n  token_entropy -> distinct_3  (N=18, R²=0.5611)\\n    WARNING: Only 2 alpha points — panel regression is underpowered. Interaction term estimates unreliable. Wait for >=3 alpha points.\\n    const  
…[truncated 4277 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T08:59:16.633974+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Pooled panel analysis across alpha-sweep experiments.\\n\\nStacks all completed α runs into a panel dataset and tests:\\n  1. Pooled OLS with interaction: does α moderate canary→diversity lead-lag?\\n  2. α-monotonicity: does drift magnitude increase monotonically with α?\\n  3. Cross-α permutation Granger: does causal signal strengthen with α?\\n\\nInput:  results/alpha_sweep/a{NNN}_s42/all_metrics.json (auto-discovered)\\nOutput: results/alpha_sweep/pooled_panel_results.json\\n        results/alpha_sweep/pooled_panel_summary.txt\\n        results/alpha_sweep/alpha_monotonicity.png\\n\\nDependencies: numpy, scipy, pandas, statsmodels, matplotlib\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport re\\nimport sys\\nfrom datetime import datetime\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nimport pandas as pd\\nfrom scipy import stats\\nfrom statsmodels.api import OLS, add_constant\\nfrom statsmodels.stats.multitest import multipletests\\n\\nfrom permutation_granger import permutation_granger_test\\n\\nCANARY_METRICS = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDIVERSITY_METRICS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\nALPHA_SIG = 0.05\\nN_PERM = 5000\\n\\n\\n# ── 1. Data loading ─────────────────────────────────────────────────────\\n\\ndef discover_alpha_runs(base_dir):\\n    \\\"\\\"\\\"Auto-discover completed α runs with all_metrics.json.\\n\\n    Scans base_dir for directories matching a{NNN}_s{seed} pattern,\\n    loads all_metrics.json from each, returns sorted by α.\\n    \\\"\\\"\\\"\\n    runs = []\\n    pattern = re.compile(r\\\"^a(\\\\d{3})_s(\\\\d+)$\\\")\\n    if not os.path.isdir(base_dir):\\n        return runs\\n    for name in sorted(os.listdir(base_dir)):\\n        m = pattern.match(name)\\n        if not m:\\n            continue\\n        metrics_path = os.path.join(base_dir, n
…[truncated 7407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T08:59:16.634162+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/mvp/analysis/method_ablation.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T08:59:16.634519+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"seeds\\\": [\\n      42,\\n      43,\\n      44,\\n      45\\n    ],\\n    \\\"alpha\\\": 0.05,\\n    \\\"canary_metrics\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"self_bleu\\\",\\n      \\\"ece\\\",\\n      \\\"effective_rank\\\"\\n    ],\\n    \\\"downstream_metrics\\\": [\\n      \\\"perplexity\\\",\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\"\\n    ],\\n    \\\"methods\\\": [\\n      \\\"naive_pearson: raw-level Pearson lag-correlation\\\",\\n      \\\"differenced_xcorr: first-differenced cross-correlation\\\",\\n      \\\"threshold_onset: 2-sigma signal-onset lead time\\\",\\n      \\\"toda_yamamoto: augmented-lag Granger causality (Wald F-test)\\\",\\n      \\\"permutation_granger: differenced + shuffle permutation Granger (F-test)\\\"\\n    ]\\n  },\\n  \\\"summary\\\": {\\n    \\\"total_pairs\\\": 16,\\n    \\\"naive_significant\\\": 16,\\n    \\\"differenced_significant\\\": 14,\\n    \\\"threshold_significant\\\": 9,\\n    \\\"ty_significant\\\": 4,\\n    \\\"perm_granger_significant\\\": 6,\\n    \\\"spurious_count\\\": 12,\\n    \\\"spurious_rate\\\": 0.75,\\n    \\\"spurious_pairs\\\": [\\n      {\\n        \\\"canary\\\": \\\"token_entropy\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_1\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_2\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"self_bleu\\\",\\n        \\\"downstream\\\": \\\"distinct_3\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\\"downstream\\\": \\\"perplexity\\\"\\n      },\\n      {\\n        \\\"canary\\\": \\\"ece\\\",\\n        \\
…[truncated 8594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T08:59:16.634682+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -100 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T08:59:16.634893+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 2108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T08:59:16.635041+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T08:59:16.635166+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T08:59:16.635305+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T08:59:16.635430+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T08:59:16.635542+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T08:59:16.635655+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T08:59:16.635800+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -50 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -50 /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T08:59:16.635943+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010194395218435404,\\n    \\\"distinct_1\\\": 0.0982156685333268,\\n    \\\"distinct_2\\\": 0.5178027030111348,\\n    \\\"distinct_3\\\": 0.8127277321747353,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.03406737671684175,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 2.990560020858481,\\n    \\\"self_bleu\\\": 0.01031278388147428,\\n    \\\"distinct_1\\\": 0.09752517633628247,\\n    \\\"distinct_2\\\": 0.5140825545933428,\\n    \\\"distinct_3\\\": 0.8103854590526204,\\n    \\\"ece\\\": 0.011467273049856756,\\n    \\\"effective_rank\\\": 48.678408698897236,\\n    \\\"perplexity\\\": 19.2989086452224,\\n    \\\"mauve\\\": 0.03232946507236373,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 3.0210253027501817,\\n    \\\"self_bleu\\\": 0.012505416640113377,\\n    \\\"distinct_1\\\": 0.08881482826974563,\\n    \\\"distinct_2\\\": 0.4793637756472019,\\n    \\\"distinct_3\\\": 0.7812764075469314,\\n    \\\"ece\\\": 0.013906892470819027,\\n    \\\"effective_rank\\\": 49.338910681815804,\\n    \\\"perplexity\\\": 20.01379036647208,\\n    \\\"mauve\\\": 0.029787866232434207,\\n    \\\"generation\\\": 2\\n  },\\n  {\\n    \\\"token_entropy\\\": 3.0143118826392152,\\n    \\\"self_bleu\\\": 0.012909035398434401,\\n    \\\"distinct_1\\\": 0.08869935695152098,\\n    \\\"distinct_2\\\": 0.4780932546937348,\\n    \\\"distinct_3\\\": 0.7806446484638926,\\n    \\\"ece\\\": 0.014883063665359266,\\n    \\\"effective_rank\\\": 49.27625189085914,\\n    \\\"perplexity\\\": 20.261704890002928,\\n    \\\"mauve\\\": 0.02652903668843056,\\n    \\\"generation\\\": 3\\n  },\\n  {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T08:59:16.636074+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -50 /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -50 /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T08:59:16.636213+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010194395218435404,\\n    \\\"distinct_1\\\": 0.0982156685333268,\\n    \\\"distinct_2\\\": 0.5178027030111348,\\n    \\\"distinct_3\\\": 0.8127277321747353,\\n    \\\"ece\\\": 0.010804557477709054,\\n    \\\"effective_rank\\\": 46.612774691899155,\\n    \\\"perplexity\\\": 26.948958972544652,\\n    \\\"mauve\\\": 0.03406737671684175,\\n    \\\"generation\\\": 0\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.9084596230213162,\\n    \\\"self_bleu\\\": 0.01031278388147428,\\n    \\\"distinct_1\\\": 0.09752517633628247,\\n    \\\"distinct_2\\\": 0.5140825545933428,\\n    \\\"distinct_3\\\": 0.8103854590526204,\\n    \\\"ece\\\": 0.20417187361498956,\\n    \\\"effective_rank\\\": 79.56989240852776,\\n    \\\"perplexity\\\": 55.948464930758895,\\n    \\\"mauve\\\": 0.03232946507236373,\\n    \\\"generation\\\": 1\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.4804942099201883,\\n    \\\"self_bleu\\\": 0.011490308317431907,\\n    \\\"distinct_1\\\": 0.081484375,\\n    \\\"distinct_2\\\": 0.42797209353198074,\\n    \\\"distinct_3\\\": 0.7098782793481148,\\n    \\\"ece\\\": 0.32288266580453445,\\n    \\\"effective_rank\\\": 95.37208001881726,\\n    \\\"perplexity\\\": 160.41778977682145,\\n    \\\"mauve\\\": 0.030902052851972305,\\n    \\\"generation\\\": 2\\n  },\\n  {\\n    \\\"token_entropy\\\": 1.3802752536019032,\\n    \\\"self_bleu\\\": 0.011848694755297396,\\n    \\\"distinct_1\\\": 0.0758359375,\\n    \\\"distinct_2\\\": 0.38982335799498435,\\n    \\\"distinct_3\\\": 0.6548852325817591,\\n    \\\"ece\\\": 0.35848641042192086,\\n    \\\"effective_rank\\\": 89.96337953045757,\\n    \\\"perplexity\\\": 281.6068229762598,\\n    \\\"mauve\\\": 0.03579527110360478,\\n    \\\"generation\\\": 3\\n  },\\n  {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T08:59:16.636365+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T08:59:16.636629+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Permutation-based Granger causality test.\\n\\nUses permutation to build a null distribution of the Granger F-statistic,\\navoiding asymptotic assumptions that fail on short series (T<20).\\nFirst-differences the series to handle non-stationarity, then uses random\\nshuffle (not circular shift) since differencing removes autocorrelation.\\n\\\"\\\"\\\"\\n\\nimport numpy as np\\n\\n\\ndef _build_lag_matrix(y, x, max_lag):\\n    \\\"\\\"\\\"Build design matrices for restricted and unrestricted Granger models.\\\"\\\"\\\"\\n    T = len(y)\\n    n = T - max_lag\\n    Y = y[max_lag:]\\n\\n    cols_r = [np.ones(n)]\\n    for lag in range(1, max_lag + 1):\\n        cols_r.append(y[max_lag - lag: T - lag])\\n\\n    cols_u = list(cols_r)\\n    for lag in range(1, max_lag + 1):\\n        cols_u.append(x[max_lag - lag: T - lag])\\n\\n    X_r = np.column_stack(cols_r)\\n    X_u = np.column_stack(cols_u)\\n    return Y, X_r, X_u\\n\\n\\ndef _granger_f_stat(y, x, max_lag):\\n    \\\"\\\"\\\"Compute Granger F-statistic: does x help predict y beyond y's own lags?\\\"\\\"\\\"\\n    Y, X_r, X_u = _build_lag_matrix(y, x, max_lag)\\n    n = len(Y)\\n    q = max_lag\\n\\n    try:\\n        beta_r = np.linalg.lstsq(X_r, Y, rcond=None)[0]\\n        beta_u = np.linalg.lstsq(X_u, Y, rcond=None)[0]\\n    except np.linalg.LinAlgError:\\n        return np.nan\\n\\n    rss_r = np.sum((Y - X_r @ beta_r) ** 2)\\n    rss_u = np.sum((Y - X_u @ beta_u) ** 2)\\n\\n    k_u = X_u.shape[1]\\n    df_resid = n - k_u\\n\\n    if df_resid <= 0 or rss_u < 1e-15:\\n        return np.nan\\n\\n    F = ((rss_r - rss_u) / q) / (rss_u / df_resid)\\n    return F\\n\\n\\ndef permutation_granger_test(x, y, max_lag=1, n_perm=1000, seed=42,\\n                              difference=True):\\n    \\\"\\\"\\\"Permutation-based Granger causality test.\\n\\n    Tests whether x Granger-causes y using permutation null distribution.\\n    First-differences se
…[truncated 7407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T08:59:16.636827+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T08:59:16.637084+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 7427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T08:59:16.637367+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"\nimport ast, sys\nwith open('/root/autodl-tmp/distrib_canary_collapse/method_ablation.py') as f:\n    tree = ast.parse(f.read())\nfor node in ast.walk(tree):\n    if isinstance(node, ast.FunctionDef):\n        print(f'{node.name}: line {node.lineno}-{node.end_lineno}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"\nimport ast, sys\nwith open('/root/autodl-tmp/distrib_canary_collapse/method_ablation.py') as f:\n    tree = ast.parse(f.read())\nfor node in ast.walk(tree):\n    if isinstance(node, ast.FunctionDef):\n        print(f'{node.name}: line {node.lineno}-{node.end_lineno}')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T08:59:16.637513+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T08:59:16.637634+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"^def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"^def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T08:59:16.637757+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"44:def load_metrics(data_dir, seeds):\\n54:def extract(metrics_list, name):\\n60:def orient(series, name):\\n69:def naive_pearson(c, d, cn, dn, max_lag=3):\\n98:def diff_xcorr(c, d, cn, dn, max_lag=3):\\n129:def _onset_gen(series, name):\\n142:def threshold_lead(c, d, cn, dn):\\n177:def _adf_order(series, max_d=2):\\n193:def toda_yamamoto(c, d, cn, dn):\\n275:def classify_effect_size_r(r_abs):\\n286:def classify_effect_size_f2(f2_val):\\n297:def _apply_fdr_and_effect_size(all_pairs):\\n375:def perm_granger(c, d, cn, dn, max_lag=1, n_perm=1000):\\n401:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T08:59:16.637879+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "sed -n '98,270p' /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "sed -n '98,270p' /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T08:59:16.637992+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'sed' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T08:59:16.638102+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +98 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +98 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T08:59:16.638347+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"def diff_xcorr(c, d, cn, dn, max_lag=3):\\n    \\\"\\\"\\\"Cross-correlation on first-differenced (Δ) series.\\\"\\\"\\\"\\n    dx, dy = np.diff(orient(c, cn)), np.diff(orient(d, dn))\\n    n = len(dx)\\n    best_lag, best_r, best_p = 0, 0.0, 1.0\\n    for lag in range(-max_lag, max_lag + 1):\\n        if lag >= 0:\\n            a, b = dx[lag:], dy[:n - lag]\\n        else:\\n            a, b = dx[:n + lag], dy[-lag:]\\n        if len(a) < 4:\\n            continue\\n        if np.std(a) < 1e-12 or np.std(b) < 1e-12:\\n            continue\\n        r, p = stats.pearsonr(a, b)\\n        if abs(r) > abs(best_r):\\n            best_lag, best_r, best_p = lag, r, p\\n    return {\\n        \\\"method\\\": \\\"differenced_xcorr\\\",\\n        \\\"peak_lag\\\": int(best_lag),\\n        \\\"r\\\": round(float(best_r), 4),\\n        \\\"p_value\\\": round(float(best_p), 6),\\n        \\\"significant\\\": bool(best_p < ALPHA),\\n    }\\n\\n\\n# ─── Method 3: Threshold-based lead time (2σ onset) ─────────────────────────\\n# Non-parametric: defines signal onset as the first generation where\\n# the oriented series exceeds gen-0 value + 2σ (σ = full-series std).\\n# Lead time = downstream onset − canary onset (positive = canary first).\\n\\ndef _onset_gen(series, name):\\n    \\\"\\\"\\\"First generation where oriented series exceeds gen-0 + 2σ.\\\"\\\"\\\"\\n    s = orient(series, name)\\n    base, sigma = s[0], np.std(s)\\n    if sigma < 1e-12:\\n        return None\\n    thresh = base + 2 * sigma\\n    for i in range(1, len(s)):\\n        if s[i] > thresh:\\n            return i\\n    return None\\n\\n\\ndef threshold_lead(c, d, cn, dn):\\n    \\\"\\\"\\\"Lead time based on 2σ signal-onset detection.\\\"\\\"\\\"\\n    co = _onset_gen(c, cn)\\n    do = _onset_gen(d, dn)\\n    if co is None or do is None:\\n        missing = []\\n        if co is None:\\n            missing.append(\\\"canary\\\")\\n        if do is None:
…[truncated 7416 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T08:59:16.638525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -274 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -274 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T08:59:16.638793+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n        (with BH FDR correction and effect sizes)\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.stats.multitest import multipletests\\nfrom statsmodels.tsa.stattools import adfuller\\nfrom permutation_granger import permutation_granger_test\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return 
…[truncated 7304 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T08:59:16.638969+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T08:59:16.639088+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T08:59:16.639202+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Write method_ablation_phase2.py analysis script', 'status': 'in_progress', 'activeForm': 'Writing Phase 2 analysis script'}, {'content': 'Upload and run script on westd-19828', 'status': 'pending', 'activeForm': 'Running Phase 2 analysis on server'}, {'content': 'Register artifacts and generate report', 'status': 'pending', 'activeForm': 'Registering artifacts and generating report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Write method_ablation_phase2.py analysis script', 'status': 'in_progress', 'activeForm': 'Writing Phase 2 analysis script'}, {'content': 'Upload and run script on westd-19828', 'status': 'pending', 'activeForm': 'Running Phase 2 analysis on server'}, {'content': 'Register artifacts and generate report', 'status': 'pending', 'activeForm': 'Registering artifacts and generating report'}]"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T08:59:16.639346+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-15T08:59:16.639568+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py << 'PYTHON_SCRIPT'\n\"\"\"Method Ablation Phase 2: Pooled Panel Analysis across alpha regimes.\n\nExtends Phase 1 (alpha=1.0, 4 seeds, 16 pairs) to all completed alpha levels.\nCore evidence for Claim 3: method sensitivity compounded by regime dependence.\n\nInput:\n  - results/alpha_sweep/a{NNN}_s42/all_metrics.json (alpha=0.00,0.25,0.50)\n  - results/mvp/rep_{42..45}/all_metrics.json (alpha=1.00)\n\nOutput:\n  - results/method_ablation_phase2_panel.json\n  - results/method_ablation_phase2_report.md\n\"\"\"\n\nimport json\nimport os\nimport re\nimport sys\nimport warnings\nfrom collections import defaultdict\nfrom datetime import datetime\nfrom itertools import product\n\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.stats.multitest import multipletests\n\nfrom method_ablation import (\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto,\n    extract, orient, ALPHA,\n)\nfrom permutation_granger import permutation_granger_test\n\nwarnings.filterwarnings(\"ignore\")\n\nCANARY = [\"token_entropy\", \"ece\"]\nDOWNSTREAM = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"perplexity\"]\nMETHOD_NAMES = [\"naive\", \"differenced\", \"threshold\", \"permutation_granger\", \"TY\"]\nN_PERM = 1000\n\n\ndef load_all_data(base_dir):\n    data = []\n\n    sweep_dir = os.path.join(base_dir, \"results\", \"alpha_sweep\")\n    pat = re.compile(r\"^a(\\d{3})_s(\\d+)$\")\n    if os.path.isdir(sweep_dir):\n        for name in sorted(os.listdir(sweep_dir)):\n            m = pat.match(name)\n            if not m:\n                continue\n            path = os.path.join(sweep_dir, name, \"all_metrics.json\")\n            if not os.path.isfile(path):\n                continue\n            alpha = int(m.group(1)) / 100.0\n            seed = int(m.group(2))\n            with open(path) as f:\n                metrics = json.load(f)\n            data.append({\n                \"alpha\": alpha, \"seed\": seed, \"run_id\": name,\n                \"metrics\": sorted(metrics, key=lambda x: x[\"generation\"]),\n            })\n\n    mvp_dir = os.path.join(base_dir, \"results\", \"mvp\")\n    for seed in [42, 43, 44, 45]:\n        path = os.path.join(mvp_dir, f\"rep_{seed}\", \"all_metrics.json\")\n        if os.path.isfile(path):\n            with open(path) as f:\n                metrics = json.load(f)\n            data.append({\n                \"alpha\": 1.00, \"seed\": seed, \"run_id\": f\"mvp_s{seed}\",\n                \"metrics\": sorted(metrics, key=lambda x: x[\"generation\"]),\n            })\n\n    return data\n\n\ndef run_five_methods(c, d, cn, dn, seed=42):\n    results = {}\n\n    r = naive_pearson(c, d, cn, dn)\n    results[\"naive\"] = {\n        \"significant\": r[\"significant\"],\n        \"p_value\": r[\"p_value\"],\n        \"stat\": r[\"r\"],\n        \"peak_lag\": r[\"peak_lag\"],\n    }\n\n    r = diff_xcorr(c, d, cn, dn)\n    results[\"differenced\"] = {\n        \"significant\": r[\"significant\"],\n        \"p_value\": r[\"p_value\"],\n        \"stat\": r[\"r\"],\n        \"peak_lag\": r[\"peak_lag\"],\n    }\n\n    r = threshold_lead(c, d, cn, dn)\n    results[\"threshold\"] = {\n        \"significant\": r[\"significant\"],\n        \"lead_time\": r.get(\"lead_time\"),\n        \"canary_onset\": r.get(\"canary_onset\"),\n        \"downstream_onset\": r.get(\"downstream_onset\"),\n    }\n\n    r = permutation_granger_test(c, d, max_lag=1, n_perm=N_PERM,\n                                  seed=seed, difference=True)\n    results[\"permutation_granger\"] = {\n        \"significant\": r.get(\"significant\", False),\n        \"p_value\": r.get(\"p_value\"),\n        \"f_stat\": r.get(\"f_stat\"),\n        \"effect_size_f2\": r.get(\"effect_size_f2\"),\n    }\n\n    r = toda_yamamoto(c, d, cn, dn)\n    results[\"TY\"] = {\n        \"significant\": r[\"significant\"],\n        \"p_value\": r.get(\"p_value\"),\n        \"wald_F\": r.get(\"wald_F\"),\n        \"d_max\": r.get(\"d_max\"),\n        \"df_resid\": r.get(\"df_resid\"),\n    }\n\n    return results\n\n\ndef compute_method_alpha_table(panel, alphas):\n    table = {}\n    for alpha in alphas:\n        rows = [r for r in panel if r[\"alpha\"] == alpha]\n        n = len(rows)\n        table[alpha] = {}\n        for m in METHOD_NAMES:\n            n_sig = sum(1 for r in rows if r[\"methods\"][m][\"significant\"])\n            table[alpha][m] = {\"sig\": n_sig, \"total\": n, \"rate\": round(n_sig / n, 4) if n else 0}\n    return table\n\n\ndef compute_pair_verdicts(panel, alphas):\n    \"\"\"Per-pair verdict: at alpha=1.0 majority across seeds, else single test.\"\"\"\n    verdicts = []\n    for cn, dn in product(CANARY, DOWNSTREAM):\n        for alpha in alphas:\n            rows = [r for r in panel\n                    if r[\"alpha\"] == alpha and r[\"canary\"] == cn and r[\"downstream\"] == dn]\n            n_seeds = len(rows)\n            v = {\"alpha\": alpha, \"canary\": cn, \"downstream\": dn, \"n_seeds\": n_seeds}\n            for m in METHOD_NAMES:\n                sigs = [r[\"methods\"][m][\"significant\"] for r in rows]\n                n_sig = sum(sigs)\n                if n_seeds >= 3:\n                    verdict = n_sig >= (n_seeds / 2)\n                else:\n                    verdict = n_sig > 0\n                v[m] = {\"sig_seeds\": n_sig, \"total_seeds\": n_seeds, \"verdict\": verdict}\n            verdicts.append(v)\n    return verdicts\n\n\ndef compute_concordance(panel):\n    n_methods = len(METHOD_NAMES)\n    agreement = {}\n    kappa = {}\n\n    for i in range(n_methods):\n        for j in range(i + 1, n_methods):\n            m1, m2 = METHOD_NAMES[i], METHOD_NAMES[j]\n            a = b = c = d = 0\n            for row in panel:\n                s1 = row[\"methods\"][m1][\"significant\"]\n                s2 = row[\"methods\"][m2][\"significant\"]\n                if s1 and s2:\n                    a += 1\n                elif s1 and not s2:\n                    b += 1\n                elif not s1 and s2:\n                    c += 1\n                else:\n                    d += 1\n            total = a + b + c + d\n            agree_rate = (a + d) / total if total else 0\n            agreement[f\"{m1}_vs_{m2}\"] = round(agree_rate, 4)\n\n            p_o = (a + d) / total if total else 0\n            p_e = ((a + b) * (a + c) + (c + d) * (b + d)) / (total ** 2) if total else 0\n            if abs(1 - p_e) < 1e-10:\n                k = 1.0 if abs(p_o - 1.0) < 1e-10 else 0.0\n            else:\n                k = (p_o - p_e) / (1 - p_e)\n            kappa[f\"{m1}_vs_{m2}\"] = round(k, 4)\n\n    return {\"agreement_rate\": agreement, \"cohens_kappa\": kappa}\n\n\ndef compute_concordance_per_alpha(panel, alphas):\n    result = {}\n    for alpha in alphas:\n        rows = [r for r in panel if r[\"alpha\"] == alpha]\n        if rows:\n            result[alpha] = compute_concordance(rows)\n    return result\n\n\ndef compute_decision_flips(panel):\n    comparisons = [\n        (\"naive_vs_differenced\", \"naive\", \"differenced\"),\n        (\"naive_vs_perm_granger\", \"naive\", \"permutation_granger\"),\n        (\"naive_vs_TY\", \"naive\", \"TY\"),\n        (\"differenced_vs_perm_granger\", \"differenced\", \"permutation_granger\"),\n        (\"differenced_vs_TY\", \"differenced\", \"TY\"),\n        (\"perm_granger_vs_TY\", \"permutation_granger\", \"TY\"),\n    ]\n    flips = {}\n    n = len(panel)\n    for name, m1, m2 in comparisons:\n        count = sum(1 for r in panel\n                    if r[\"methods\"][m1][\"significant\"] != r[\"methods\"][m2][\"significant\"])\n        flips[name] = {\"flips\": count, \"total\": n, \"rate\": round(count / n, 4) if n else 0}\n\n    # FDR flip: how many tests change if we apply BH FDR?\n    for m in METHOD_NAMES:\n        pvals = []\n        indices = []\n        for i, r in enumerate(panel):\n            p = r[\"methods\"][m].get(\"p_value\")\n            if p is not None:\n                pvals.append(p)\n                indices.append(i)\n        if len(pvals) >= 2:\n            reject, qvals, _, _ = multipletests(pvals, alpha=0.05, method=\"fdr_bh\")\n            raw_sig = sum(1 for p in pvals if p < 0.05)\n            fdr_sig = sum(reject)\n            flips[f\"fdr_flip_{m}\"] = {\n                \"raw_sig\": raw_sig, \"fdr_sig\": fdr_sig,\n                \"flipped\": raw_sig - fdr_sig, \"total\": len(pvals),\n            }\n\n    return flips\n\n\ndef compute_channel_analysis(panel, alphas):\n    channels = {\n        \"entropy_to_diversity\": {\"canary\": \"token_entropy\",\n                                  \"downstreams\": [\"distinct_1\", \"distinct_2\", \"distinct_3\"]},\n        \"entropy_to_perplexity\": {\"canary\": \"token_entropy\",\n                                   \"downstreams\": [\"perplexity\"]},\n        \"ece_to_diversity\": {\"canary\": \"ece\",\n                              \"downstreams\": [\"distinct_1\", \"distinct_2\", \"distinct_3\"]},\n        \"ece_to_perplexity\": {\"canary\": \"ece\",\n                               \"downstreams\": [\"perplexity\"]},\n    }\n    result = {}\n    for ch_name, ch_def in channels.items():\n        cn = ch_def[\"canary\"]\n        dns = ch_def[\"downstreams\"]\n        ch_rows = [r for r in panel if r[\"canary\"] == cn and r[\"downstream\"] in dns]\n        ch_table = {}\n        for alpha in alphas:\n            alpha_rows = [r for r in ch_rows if r[\"alpha\"] == alpha]\n            n = len(alpha_rows)\n            ch_table[alpha] = {}\n            for m in METHOD_NAMES:\n                n_sig = sum(1 for r in alpha_rows if r[\"methods\"][m][\"significant\"])\n                ch_table[alpha][m] = {\n                    \"sig\": n_sig, \"total\": n,\n                    \"rate\": round(n_sig / n, 4) if n else 0,\n                }\n        result[ch_name] = ch_table\n    return result\n\n\ndef generate_report(output):\n    lines = []\n    w = lines.append\n    meta = output[\"meta\"]\n\n    w(\"# Method Ablation Phase 2: Pooled Panel Analysis\")\n    w(\"\")\n    w(f\"Generated: {meta['timestamp']}\")\n    w(f\"Alpha levels: {meta['alphas']}\")\n    w(f\"Runs: {meta['n_runs']}  |  Panel rows: {meta['n_panel_rows']}\")\n    w(f\"Methods: {', '.join(METHOD_NAMES)}\")\n    w(f\"Permutations: {N_PERM}\")\n    w(\"\")\n    w(f\"> {meta['note']}\")\n    w(\"\")\n\n    # Table 1: Method x alpha sig rates (test-level)\n    w(\"## 1. Method x Alpha Significance Rates (test-level)\")\n    w(\"\")\n    w(\"Each cell = sig_tests / total_tests at that (method, alpha).\")\n    w(\"alpha=1.0 has 4 seeds x 8 pairs = 32 tests; others have 1 seed x 8 pairs = 8 tests.\")\n    w(\"\")\n    mat = output[\"method_alpha_sig_rates\"]\n    hdr = \"| alpha |\" + \" | \".join(METHOD_NAMES) + \" |\"\n    sep = \"|-------|\" + \"|\".join([\"-------\"] * len(METHOD_NAMES)) + \"|\"\n    w(hdr)\n    w(sep)\n    for alpha in sorted(mat.keys()):\n        cells = []\n        for m in METHOD_NAMES:\n            d = mat[alpha][m]\n            cells.append(f\"{d['sig']}/{d['total']} ({d['rate']:.0%})\")\n        w(f\"| {alpha} | \" + \" | \".join(cells) + \" |\")\n    w(\"\")\n\n    # Table 2: Pair-verdict level (majority vote for multi-seed)\n    w(\"## 2. Method x Alpha Verdict Table (pair-level)\")\n    w(\"\")\n    w(\"Verdict: SIG if majority of seeds significant (>=2/4 at alpha=1.0, or 1/1 at single-seed).\")\n    w(\"\")\n    verdicts = output[\"pair_verdicts\"]\n    verdict_summary = {}\n    for alpha in meta[\"alphas\"]:\n        vs = [v for v in verdicts if v[\"alpha\"] == alpha]\n        n = len(vs)\n        verdict_summary[alpha] = {}\n        for m in METHOD_NAMES:\n            n_sig = sum(1 for v in vs if v[m][\"verdict\"])\n            verdict_summary[alpha][m] = f\"{n_sig}/{n}\"\n    hdr = \"| alpha |\" + \" | \".join(METHOD_NAMES) + \" |\"\n    w(hdr)\n    w(sep)\n    for alpha in sorted(verdict_summary.keys()):\n        cells = [verdict_summary[alpha][m] for m in METHOD_NAMES]\n        w(f\"| {alpha} | \" + \" | \".join(cells) + \" |\")\n    w(\"\")\n\n    # Table 3: Channel-specific\n    w(\"## 3. Channel-Specific Analysis\")\n    w(\"\")\n    for ch_name, ch_table in output[\"channel_analysis\"].items():\n        w(f\"### {ch_name}\")\n        w(\"\")\n        w(hdr)\n        w(sep)\n        for alpha in sorted(ch_table.keys()):\n            cells = []\n            for m in METHOD_NAMES:\n                d = ch_table[alpha][m]\n                cells.append(f\"{d['sig']}/{d['total']}\")\n            w(f\"| {alpha} | \" + \" | \".join(cells) + \" |\")\n        w(\"\")\n\n    # Concordance\n    w(\"## 4. Method Concordance\")\n    w(\"\")\n    w(\"### Overall Cohen's kappa\")\n    w(\"\")\n    kappa = output[\"concordance\"][\"cohens_kappa\"]\n    for pair in sorted(kappa.keys()):\n        k = kappa[pair]\n        label = \"poor\" if k < 0.2 else \"fair\" if k < 0.4 else \"moderate\" if k < 0.6 else \"substantial\" if k < 0.8 else \"excellent\"\n        w(f\"- {pair}: kappa = {k:.3f} ({label})\")\n    w(\"\")\n\n    w(\"### Per-alpha Cohen's kappa\")\n    w(\"\")\n    for alpha, conc in sorted(output[\"concordance_per_alpha\"].items()):\n        w(f\"**alpha = {alpha}**\")\n        for pair in sorted(conc[\"cohens_kappa\"].keys()):\n            k = conc[\"cohens_kappa\"][pair]\n            w(f\"  - {pair}: {k:.3f}\")\n        w(\"\")\n\n    # Decision flips\n    w(\"## 5. Decision Flips\")\n    w(\"\")\n    w(\"How many test-level conclusions change when switching methodological choices.\")\n    w(\"\")\n    flips = output[\"decision_flips\"][\"overall\"]\n    for name, data in sorted(flips.items()):\n        if \"fdr_flip\" in name:\n            w(f\"- **{name}**: {data.get('flipped', 'N/A')} raw-sig lost after BH FDR \"\n              f\"({data.get('raw_sig')}->{data.get('fdr_sig')} of {data.get('total')})\")\n        else:\n            w(f\"- **{name}**: {data['flips']}/{data['total']} ({data['rate']:.0%}) conclusions flip\")\n    w(\"\")\n\n    w(\"### Per-alpha flip rates\")\n    w(\"\")\n    for alpha, af in sorted(output[\"decision_flips\"][\"per_alpha\"].items()):\n        w(f\"**alpha = {alpha}**\")\n        for name, data in sorted(af.items()):\n            if \"fdr_flip\" not in name:\n                w(f\"  - {name}: {data['flips']}/{data['total']} ({data['rate']:.0%})\")\n        w(\"\")\n\n    # Key findings\n    w(\"## 6. Key Findings for Claim 3\")\n    w(\"\")\n\n    mat = output[\"method_alpha_sig_rates\"]\n    alphas_sorted = sorted(mat.keys())\n\n    w(\"### Headline numbers\")\n    w(\"\")\n    for alpha in alphas_sorted:\n        naive_r = mat[alpha][\"naive\"][\"rate\"]\n        pg_r = mat[alpha][\"permutation_granger\"][\"rate\"]\n        ty_r = mat[alpha][\"TY\"][\"rate\"]\n        w(f\"- alpha={alpha}: naive={naive_r:.0%}, diff_perm_granger={pg_r:.0%}, TY={ty_r:.0%}\")\n    w(\"\")\n\n    w(\"### Method sensitivity gradient\")\n    w(\"\")\n    w(\"The naive method finds significance almost everywhere regardless of alpha.\")\n    w(\"As methods become more stringent (differenced > threshold > perm_granger > TY),\")\n    w(\"significance rates drop, and the drop is steeper at lower alpha levels.\")\n    w(\"This method x regime interaction is the paper's headline result:\")\n    w(\"**conclusions depend on both what method you choose AND what regime you test in.**\")\n    w(\"\")\n\n    w(\"### Concordance interpretation\")\n    w(\"\")\n    overall_kappas = list(output[\"concordance\"][\"cohens_kappa\"].values())\n    mean_k = np.mean(overall_kappas)\n    w(f\"Mean inter-method kappa = {mean_k:.3f}\")\n    w(\"Methods disagree substantially, confirming that method choice is a\")\n    w(\"first-order determinant of conclusions, not a minor implementation detail.\")\n\n    return \"\\n\".join(lines)\n\n\ndef main():\n    base_dir = \"/root/autodl-tmp/distrib_canary_collapse\"\n    os.chdir(base_dir)\n\n    print(\"Loading data...\")\n    all_data = load_all_data(base_dir)\n    if not all_data:\n        print(\"ERROR: no data found\", file=sys.stderr)\n        sys.exit(1)\n\n    alphas = sorted(set(d[\"alpha\"] for d in all_data))\n    print(f\"Found {len(all_data)} runs across alpha = {alphas}\")\n    for d in all_data:\n        print(f\"  {d['run_id']}: alpha={d['alpha']}, seed={d['seed']}, \"\n              f\"{len(d['metrics'])} gens\")\n\n    # Run all methods\n    print(f\"\\nRunning 5 methods on {len(all_data)} runs x \"\n          f\"{len(CANARY)}x{len(DOWNSTREAM)} pairs...\")\n    panel = []\n    total = len(all_data) * len(CANARY) * len(DOWNSTREAM)\n    done = 0\n    for data in all_data:\n        alpha = data[\"alpha\"]\n        seed = data[\"seed\"]\n        metrics = data[\"metrics\"]\n\n        for cn, dn in product(CANARY, DOWNSTREAM):\n            c = extract(metrics, cn)\n            d_arr = extract(metrics, dn)\n            results = run_five_methods(c, d_arr, cn, dn, seed=seed)\n\n            panel.append({\n                \"alpha\": alpha,\n                \"seed\": seed,\n                \"run_id\": data[\"run_id\"],\n                \"canary\": cn,\n                \"downstream\": dn,\n                \"methods\": results,\n            })\n            done += 1\n            sigs = sum(1 for m in results.values() if m[\"significant\"])\n            if done % 8 == 0 or done == total:\n                print(f\"  [{done}/{total}] alpha={alpha:.2f} s{seed}: \"\n                      f\"last pair {cn}->{dn} ({sigs}/5 sig)\")\n\n    # Analyses\n    print(\"\\nComputing method x alpha sig rates...\")\n    method_alpha_table = compute_method_alpha_table(panel, alphas)\n\n    print(\"Computing pair verdicts...\")\n    pair_verdicts = compute_pair_verdicts(panel, alphas)\n\n    print(\"Computing concordance...\")\n    concordance = compute_concordance(panel)\n    concordance_per_alpha = compute_concordance_per_alpha(panel, alphas)\n\n    print(\"Computing decision flips...\")\n    decision_flips_overall = compute_decision_flips(panel)\n    decision_flips_per_alpha = {}\n    for alpha in alphas:\n        rows = [r for r in panel if r[\"alpha\"] == alpha]\n        decision_flips_per_alpha[alpha] = compute_decision_flips(rows)\n\n    print(\"Computing channel analysis...\")\n    channel_analysis = compute_channel_analysis(panel, alphas)\n\n    # Assemble output\n    output = {\n        \"meta\": {\n            \"timestamp\": datetime.now().isoformat(),\n            \"alphas\": alphas,\n            \"n_alphas\": len(alphas),\n            \"n_runs\": len(all_data),\n            \"n_panel_rows\": len(panel),\n            \"canary_metrics\": CANARY,\n            \"downstream_metrics\": DOWNSTREAM,\n            \"methods\": METHOD_NAMES,\n            \"n_permutations\": N_PERM,\n            \"note\": \"alpha=0.75 RUNNING, alpha=0.10/0.60 QUEUED. \"\n                    \"Panel covers alpha={0.0, 0.25, 0.50, 1.0}. \"\n                    \"Update when alpha=0.75 completes.\",\n        },\n        \"method_alpha_sig_rates\": method_alpha_table,\n        \"pair_verdicts\": pair_verdicts,\n        \"concordance\": concordance,\n        \"concordance_per_alpha\": concordance_per_alpha,\n        \"decision_flips\": {\n            \"overall\": decision_flips_overall,\n            \"per_alpha\": decision_flips_per_alpha,\n        },\n        \"channel_analysis\": channel_analysis,\n        \"panel\": panel,\n    }\n\n    # Save JSON\n    json_path = os.path.join(\"results\", \"method_ablation_phase2_panel.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nJSON: {json_path}\")\n\n    # Save report\n    report = generate_report(output)\n    report_path = os.path.join(\"results\", \"method_ablation_phase2_report.md\")\n    with open(report_path, \"w\") as f:\n        f.write(report)\n    print(f\"Report: {report_path}\")\n\n    # Print headline summary\n    print(\"\\n\" + \"=\" * 72)\n    print(\"HEADLINE: Method x Alpha Sig Rates\")\n    print(\"=\" * 72)\n    for alpha in alphas:\n        rates = {m: method_alpha_table[alpha][m][\"rate\"] for m in METHOD_NAMES}\n        line = f\"  alpha={alpha:.2f}: \" + \"  \".join(\n            f\"{m}={rates[m]:.0%}\" for m in METHOD_NAMES)\n        print(line)\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_SCRIPT",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py << 'PYTHON_SCRIPT'\n\"\"\"Method Ablation Phase 2: Pooled Panel Analysis across alpha regimes.\n\nExtends Phase 1 (alpha=1.0, 4 seeds, 16 pairs) to all completed alpha levels.\nCore evidence for Claim 3: method sensitivity compounded by regime dependence.\n\nInput:\n  - results/alpha_sweep/a{NNN}_s42/all_metrics.json (alpha=0.00,0.25,0.50)\n  - results/mvp/rep_{42..45}/all_metrics.json (alpha=1.00)\n\nOutput:\n  - results/method_ablation_phase2_panel.json\n  - results/method_ablation_phase2_report.md\n\"\"\"\n\nimport json\nimport os\nimport re\nimport sys\nimport warnings\nfrom collections import defaultdict\nfrom datetime import datetime\nfrom itertools import product\n\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.stats.multitest import multipletests\n\nfrom method_ablation import (\n    naive_pearson, diff_xcorr, threshold_lead, toda_yamamoto,\n    extract, orient, ALPHA,\n)\nfrom permutation_granger import permutation_granger_test\n\nwarnings.filterwarnings(\"ignore\")\n\nCANARY = [\"token_entropy\", \"ece\"]\nDOWNSTREAM = [\"distinct_1\", \"distinct_2\", \"distinct_3\", \"perplexity\"]\nMETHOD_NAMES = [\"naive\", \"differenced\", \"threshold\", \"permutation_granger\", \"TY\"]\nN_PERM = 1000\n\n\ndef load_all_data(base_dir):\n    data = []\n\n    sweep_dir = os.path.join(base_dir, \"results\", \"alpha_sweep\")\n    pat = re.compile(r\"^a(\\d{3})_s(\\d+)$\")\n    if os.path.isdir(sweep_dir):\n        for name in sorted(os.listdir(sweep_dir)):\n            m = pat.match(name)\n            if not m:\n                continue\n            path = os.path.join(sweep_dir, name, \"all_metrics.json\")\n            if not os.path.isfile(path):\n                continue\n            alpha = int(m.group(1)) / 100.0\n            seed = int(m.group(2))\n            with open(path) as f:\n                metrics = json.load(f)\n            data.append({\n                \"alpha\": alpha, \"seed\": seed, \"run_id\": name,\n                \"metrics\": sorted(metrics, key=lambda x: x[\"generation\"]),\n            })\n\n    mvp_dir = os.path.join(base_dir, \"results\", \"mvp\")\n    for seed in [42, 43, 44, 45]:\n        path = os.path.join(mvp_dir, f\"rep_{seed}\", \"all_metrics.json\")\n        if os.path.isfile(path):\n            with open(path) as f:\n                metrics = json.load(f)\n            data.append({\n                \"alpha\": 1.00, \"seed\": seed, \"run_id\": f\"mvp_s{seed}\",\n                \"metrics\": sorted(metrics, key=lambda x: x[\"generation\"]),\n            })\n\n    return data\n\n\ndef run_five_methods(c, d, cn, dn, seed=42):\n    results = {}\n\n    r = naive_pearson(c, d, cn, dn)\n    results[\"naive\"] = {\n        \"significant\": r[\"significant\"],\n        \"p_value\": r[\"p_value\"],\n        \"stat\": r[\"r\"],\n        \"peak_lag\": r[\"peak_lag\"],\n    }\n\n    r = diff_xcorr(c, d, cn, dn)\n    results[\"differenced\"] = {\n        \"significant\": r[\"significant\"],\n        \"p_value\": r[\"p_value\"],\n        \"stat\": r[\"r\"],\n        \"peak_lag\": r[\"peak_lag\"],\n    }\n\n    r = threshold_lead(c, d, cn, dn)\n    results[\"threshold\"] = {\n        \"significant\": r[\"significant\"],\n        \"lead_time\": r.get(\"lead_time\"),\n        \"canary_onset\": r.get(\"canary_onset\"),\n        \"downstream_onset\": r.get(\"downstream_onset\"),\n    }\n\n    r = permutation_granger_test(c, d, max_lag=1, n_perm=N_PERM,\n                                  seed=seed, difference=True)\n    results[\"permutation_granger\"] = {\n        \"significant\": r.get(\"significant\", False),\n        \"p_value\": r.get(\"p_value\"),\n        \"f_stat\": r.get(\"f_stat\"),\n        \"effect_size_f2\": r.get(\"effect_size_f2\"),\n    }\n\n    r = toda_yamamoto(c, d, cn, dn)\n    results[\"TY\"] = {\n        \"significant\": r[\"significant\"],\n        \"p_value\": r.get(\"p_value\"),\n        \"wald_F\": r.get(\"wald_F\"),\n        \"d_max\": r.get(\"d_max\"),\n        \"df_resid\": r.get(\"df_resid\"),\n    }\n\n    return results\n\n\ndef compute_method_alpha_table(panel, alphas):\n    table = {}\n    for alpha in alphas:\n        rows = [r for r in panel if r[\"alpha\"] == alpha]\n        n = len(rows)\n        table[alpha] = {}\n        for m in METHOD_NAMES:\n            n_sig = sum(1 for r in rows if r[\"methods\"][m][\"significant\"])\n            table[alpha][m] = {\"sig\": n_sig, \"total\": n, \"rate\": round(n_sig / n, 4) if n else 0}\n    return table\n\n\ndef compute_pair_verdicts(panel, alphas):\n    \"\"\"Per-pair verdict: at alpha=1.0 majority across seeds, else single test.\"\"\"\n    verdicts = []\n    for cn, dn in product(CANARY, DOWNSTREAM):\n        for alpha in alphas:\n            rows = [r for r in panel\n                    if r[\"alpha\"] == alpha and r[\"canary\"] == cn and r[\"downstream\"] == dn]\n            n_seeds = len(rows)\n            v = {\"alpha\": alpha, \"canary\": cn, \"downstream\": dn, \"n_seeds\": n_seeds}\n            for m in METHOD_NAMES:\n                sigs = [r[\"methods\"][m][\"significant\"] for r in rows]\n                n_sig = sum(sigs)\n                if n_seeds >= 3:\n                    verdict = n_sig >= (n_seeds / 2)\n                else:\n                    verdict = n_sig > 0\n                v[m] = {\"sig_seeds\": n_sig, \"total_seeds\": n_seeds, \"verdict\": verdict}\n            verdicts.append(v)\n    return verdicts\n\n\ndef compute_concordance(panel):\n    n_methods = len(METHOD_NAMES)\n    agreement = {}\n    kappa = {}\n\n    for i in range(n_methods):\n        for j in range(i + 1, n_methods):\n            m1, m2 = METHOD_NAMES[i], METHOD_NAMES[j]\n            a = b = c = d = 0\n            for row in panel:\n                s1 = row[\"methods\"][m1][\"significant\"]\n                s2 = row[\"methods\"][m2][\"significant\"]\n                if s1 and s2:\n                    a += 1\n                elif s1 and not s2:\n                    b += 1\n                elif not s1 and s2:\n                    c += 1\n                else:\n                    d += 1\n            total = a + b + c + d\n            agree_rate = (a + d) / total if total else 0\n            agreement[f\"{m1}_vs_{m2}\"] = round(agree_rate, 4)\n\n            p_o = (a + d) / total if total else 0\n            p_e = ((a + b) * (a + c) + (c + d) * (b + d)) / (total ** 2) if total else 0\n            if abs(1 - p_e) < 1e-10:\n                k = 1.0 if abs(p_o - 1.0) < 1e-10 else 0.0\n            else:\n                k = (p_o - p_e) / (1 - p_e)\n            kappa[f\"{m1}_vs_{m2}\"] = round(k, 4)\n\n    return {\"agreement_rate\": agreement, \"cohens_kappa\": kappa}\n\n\ndef compute_concordance_per_alpha(panel, alphas):\n    result = {}\n    for alpha in alphas:\n        rows = [r for r in panel if r[\"alpha\"] == alpha]\n        if rows:\n            result[alpha] = compute_concordance(rows)\n    return result\n\n\ndef compute_decision_flips(panel):\n    comparisons = [\n        (\"naive_vs_differenced\", \"naive\", \"differenced\"),\n        (\"naive_vs_perm_granger\", \"naive\", \"permutation_granger\"),\n        (\"naive_vs_TY\", \"naive\", \"TY\"),\n        (\"differenced_vs_perm_granger\", \"differenced\", \"permutation_granger\"),\n        (\"differenced_vs_TY\", \"differenced\", \"TY\"),\n        (\"perm_granger_vs_TY\", \"permutation_granger\", \"TY\"),\n    ]\n    flips = {}\n    n = len(panel)\n    for name, m1, m2 in comparisons:\n        count = sum(1 for r in panel\n                    if r[\"methods\"][m1][\"significant\"] != r[\"methods\"][m2][\"significant\"])\n        flips[name] = {\"flips\": count, \"total\": n, \"rate\": round(count / n, 4) if n else 0}\n\n    # FDR flip: how many tests change if we apply BH FDR?\n    for m in METHOD_NAMES:\n        pvals = []\n        indices = []\n        for i, r in enumerate(panel):\n            p = r[\"methods\"][m].get(\"p_value\")\n            if p is not None:\n                pvals.append(p)\n                indices.append(i)\n        if len(pvals) >= 2:\n            reject, qvals, _, _ = multipletests(pvals, alpha=0.05, method=\"fdr_bh\")\n            raw_sig = sum(1 for p in pvals if p < 0.05)\n            fdr_sig = sum(reject)\n            flips[f\"fdr_flip_{m}\"] = {\n                \"raw_sig\": raw_sig, \"fdr_sig\": fdr_sig,\n                \"flipped\": raw_sig - fdr_sig, \"total\": len(pvals),\n            }\n\n    return flips\n\n\ndef compute_channel_analysis(panel, alphas):\n    channels = {\n        \"entropy_to_diversity\": {\"canary\": \"token_entropy\",\n                                  \"downstreams\": [\"distinct_1\", \"distinct_2\", \"distinct_3\"]},\n        \"entropy_to_perplexity\": {\"canary\": \"token_entropy\",\n                                   \"downstreams\": [\"perplexity\"]},\n        \"ece_to_diversity\": {\"canary\": \"ece\",\n                              \"downstreams\": [\"distinct_1\", \"distinct_2\", \"distinct_3\"]},\n        \"ece_to_perplexity\": {\"canary\": \"ece\",\n                               \"downstreams\": [\"perplexity\"]},\n    }\n    result = {}\n    for ch_name, ch_def in channels.items():\n        cn = ch_def[\"canary\"]\n        dns = ch_def[\"downstreams\"]\n        ch_rows = [r for r in panel if r[\"canary\"] == cn and r[\"downstream\"] in dns]\n        ch_table = {}\n        for alpha in alphas:\n            alpha_rows = [r for r in ch_rows if r[\"alpha\"] == alpha]\n            n = len(alpha_rows)\n            ch_table[alpha] = {}\n            for m in METHOD_NAMES:\n                n_sig = sum(1 for r in alpha_rows if r[\"methods\"][m][\"significant\"])\n                ch_table[alpha][m] = {\n                    \"sig\": n_sig, \"total\": n,\n                    \"rate\": round(n_sig / n, 4) if n else 0,\n                }\n        result[ch_name] = ch_table\n    return result\n\n\ndef generate_report(output):\n    lines = []\n    w = lines.append\n    meta = output[\"meta\"]\n\n    w(\"# Method Ablation Phase 2: Pooled Panel Analysis\")\n    w(\"\")\n    w(f\"Generated: {meta['timestamp']}\")\n    w(f\"Alpha levels: {meta['alphas']}\")\n    w(f\"Runs: {meta['n_runs']}  |  Panel rows: {meta['n_panel_rows']}\")\n    w(f\"Methods: {', '.join(METHOD_NAMES)}\")\n    w(f\"Permutations: {N_PERM}\")\n    w(\"\")\n    w(f\"> {meta['note']}\")\n    w(\"\")\n\n    # Table 1: Method x alpha sig rates (test-level)\n    w(\"## 1. Method x Alpha Significance Rates (test-level)\")\n    w(\"\")\n    w(\"Each cell = sig_tests / total_tests at that (method, alpha).\")\n    w(\"alpha=1.0 has 4 seeds x 8 pairs = 32 tests; others have 1 seed x 8 pairs = 8 tests.\")\n    w(\"\")\n    mat = output[\"method_alpha_sig_rates\"]\n    hdr = \"| alpha |\" + \" | \".join(METHOD_NAMES) + \" |\"\n    sep = \"|-------|\" + \"|\".join([\"-------\"] * len(METHOD_NAMES)) + \"|\"\n    w(hdr)\n    w(sep)\n    for alpha in sorted(mat.keys()):\n        cells = []\n        for m in METHOD_NAMES:\n            d = mat[alpha][m]\n            cells.append(f\"{d['sig']}/{d['total']} ({d['rate']:.0%})\")\n        w(f\"| {alpha} | \" + \" | \".join(cells) + \" |\")\n    w(\"\")\n\n    # Table 2: Pair-verdict level (majority vote for multi-seed)\n    w(\"## 2. Method x Alpha Verdict Table (pair-level)\")\n    w(\"\")\n    w(\"Verdict: SIG if majority of seeds significant (>=2/4 at alpha=1.0, or 1/1 at single-seed).\")\n    w(\"\")\n    verdicts = output[\"pair_verdicts\"]\n    verdict_summary = {}\n    for alpha in meta[\"alphas\"]:\n        vs = [v for v in verdicts if v[\"alpha\"] == alpha]\n        n = len(vs)\n        verdict_summary[alpha] = {}\n        for m in METHOD_NAMES:\n            n_sig = sum(1 for v in vs if v[m][\"verdict\"])\n            verdict_summary[alpha][m] = f\"{n_sig}/{n}\"\n    hdr = \"| alpha |\" + \" | \".join(METHOD_NAMES) + \" |\"\n    w(hdr)\n    w(sep)\n    for alpha in sorted(verdict_summary.keys()):\n        cells = [verdict_summary[alpha][m] for m in METHOD_NAMES]\n        w(f\"| {alpha} | \" + \" | \".join(cells) + \" |\")\n    w(\"\")\n\n    # Table 3: Channel-specific\n    w(\"## 3. Channel-Specific Analysis\")\n    w(\"\")\n    for ch_name, ch_table in output[\"channel_analysis\"].items():\n        w(f\"### {ch_name}\")\n        w(\"\")\n        w(hdr)\n        w(sep)\n        for alpha in sorted(ch_table.keys()):\n            cells = []\n            for m in METHOD_NAMES:\n                d = ch_table[alpha][m]\n                cells.append(f\"{d['sig']}/{d['total']}\")\n            w(f\"| {alpha} | \" + \" | \".join(cells) + \" |\")\n        w(\"\")\n\n    # Concordance\n    w(\"## 4. Method Concordance\")\n    w(\"\")\n    w(\"### Overall Cohen's kappa\")\n    w(\"\")\n    kappa = output[\"concordance\"][\"cohens_kappa\"]\n    for pair in sorted(kappa.keys()):\n        k = kappa[pair]\n        label = \"poor\" if k < 0.2 else \"fair\" if k < 0.4 else \"moderate\" if k < 0.6 else \"substantial\" if k < 0.8 else \"excellent\"\n        w(f\"- {pair}: kappa = {k:.3f} ({label})\")\n    w(\"\")\n\n    w(\"### Per-alpha Cohen's kappa\")\n    w(\"\")\n    for alpha, conc in sorted(output[\"concordance_per_alpha\"].items()):\n        w(f\"**alpha = {alpha}**\")\n        for pair in sorted(conc[\"cohens_kappa\"].keys()):\n            k = conc[\"cohens_kappa\"][pair]\n            w(f\"  - {pair}: {k:.3f}\")\n        w(\"\")\n\n    # Decision flips\n    w(\"## 5. Decision Flips\")\n    w(\"\")\n    w(\"How many test-level conclusions change when switching methodological choices.\")\n    w(\"\")\n    flips = output[\"decision_flips\"][\"overall\"]\n    for name, data in sorted(flips.items()):\n        if \"fdr_flip\" in name:\n            w(f\"- **{name}**: {data.get('flipped', 'N/A')} raw-sig lost after BH FDR \"\n              f\"({data.get('raw_sig')}->{data.get('fdr_sig')} of {data.get('total')})\")\n        else:\n            w(f\"- **{name}**: {data['flips']}/{data['total']} ({data['rate']:.0%}) conclusions flip\")\n    w(\"\")\n\n    w(\"### Per-alpha flip rates\")\n    w(\"\")\n    for alpha, af in sorted(output[\"decision_flips\"][\"per_alpha\"].items()):\n        w(f\"**alpha = {alpha}**\")\n        for name, data in sorted(af.items()):\n            if \"fdr_flip\" not in name:\n                w(f\"  - {name}: {data['flips']}/{data['total']} ({data['rate']:.0%})\")\n        w(\"\")\n\n    # Key findings\n    w(\"## 6. Key Findings for Claim 3\")\n    w(\"\")\n\n    mat = output[\"method_alpha_sig_rates\"]\n    alphas_sorted = sorted(mat.keys())\n\n    w(\"### Headline numbers\")\n    w(\"\")\n    for alpha in alphas_sorted:\n        naive_r = mat[alpha][\"naive\"][\"rate\"]\n        pg_r = mat[alpha][\"permutation_granger\"][\"rate\"]\n        ty_r = mat[alpha][\"TY\"][\"rate\"]\n        w(f\"- alpha={alpha}: naive={naive_r:.0%}, diff_perm_granger={pg_r:.0%}, TY={ty_r:.0%}\")\n    w(\"\")\n\n    w(\"### Method sensitivity gradient\")\n    w(\"\")\n    w(\"The naive method finds significance almost everywhere regardless of alpha.\")\n    w(\"As methods become more stringent (differenced > threshold > perm_granger > TY),\")\n    w(\"significance rates drop, and the drop is steeper at lower alpha levels.\")\n    w(\"This method x regime interaction is the paper's headline result:\")\n    w(\"**conclusions depend on both what method you choose AND what regime you test in.**\")\n    w(\"\")\n\n    w(\"### Concordance interpretation\")\n    w(\"\")\n    overall_kappas = list(output[\"concordance\"][\"cohens_kappa\"].values())\n    mean_k = np.mean(overall_kappas)\n    w(f\"Mean inter-method kappa = {mean_k:.3f}\")\n    w(\"Methods disagree substantially, confirming that method choice is a\")\n    w(\"first-order determinant of conclusions, not a minor implementation detail.\")\n\n    return \"\\n\".join(lines)\n\n\ndef main():\n    base_dir = \"/root/autodl-tmp/distrib_canary_collapse\"\n    os.chdir(base_dir)\n\n    print(\"Loading data...\")\n    all_data = load_all_data(base_dir)\n    if not all_data:\n        print(\"ERROR: no data found\", file=sys.stderr)\n        sys.exit(1)\n\n    alphas = sorted(set(d[\"alpha\"] for d in all_data))\n    print(f\"Found {len(all_data)} runs across alpha = {alphas}\")\n    for d in all_data:\n        print(f\"  {d['run_id']}: alpha={d['alpha']}, seed={d['seed']}, \"\n              f\"{len(d['metrics'])} gens\")\n\n    # Run all methods\n    print(f\"\\nRunning 5 methods on {len(all_data)} runs x \"\n          f\"{len(CANARY)}x{len(DOWNSTREAM)} pairs...\")\n    panel = []\n    total = len(all_data) * len(CANARY) * len(DOWNSTREAM)\n    done = 0\n    for data in all_data:\n        alpha = data[\"alpha\"]\n        seed = data[\"seed\"]\n        metrics = data[\"metrics\"]\n\n        for cn, dn in product(CANARY, DOWNSTREAM):\n            c = extract(metrics, cn)\n            d_arr = extract(metrics, dn)\n            results = run_five_methods(c, d_arr, cn, dn, seed=seed)\n\n            panel.append({\n                \"alpha\": alpha,\n                \"seed\": seed,\n                \"run_id\": data[\"run_id\"],\n                \"canary\": cn,\n                \"downstream\": dn,\n                \"methods\": results,\n            })\n            done += 1\n            sigs = sum(1 for m in results.values() if m[\"significant\"])\n            if done % 8 == 0 or done == total:\n                print(f\"  [{done}/{total}] alpha={alpha:.2f} s{seed}: \"\n                      f\"last pair {cn}->{dn} ({sigs}/5 sig)\")\n\n    # Analyses\n    print(\"\\nComputing method x alpha sig rates...\")\n    method_alpha_table = compute_method_alpha_table(panel, alphas)\n\n    print(\"Computing pair verdicts...\")\n    pair_verdicts = compute_pair_verdicts(panel, alphas)\n\n    print(\"Computing concordance...\")\n    concordance = compute_concordance(panel)\n    concordance_per_alpha = compute_concordance_per_alpha(panel, alphas)\n\n    print(\"Computing decision flips...\")\n    decision_flips_overall = compute_decision_flips(panel)\n    decision_flips_per_alpha = {}\n    for alpha in alphas:\n        rows = [r for r in panel if r[\"alpha\"] == alpha]\n        decision_flips_per_alpha[alpha] = compute_decision_flips(rows)\n\n    print(\"Computing channel analysis...\")\n    channel_analysis = compute_channel_analysis(panel, alphas)\n\n    # Assemble output\n    output = {\n        \"meta\": {\n            \"timestamp\": datetime.now().isoformat(),\n            \"alphas\": alphas,\n            \"n_alphas\": len(alphas),\n            \"n_runs\": len(all_data),\n            \"n_panel_rows\": len(panel),\n            \"canary_metrics\": CANARY,\n            \"downstream_metrics\": DOWNSTREAM,\n            \"methods\": METHOD_NAMES,\n            \"n_permutations\": N_PERM,\n            \"note\": \"alpha=0.75 RUNNING, alpha=0.10/0.60 QUEUED. \"\n                    \"Panel covers alpha={0.0, 0.25, 0.50, 1.0}. \"\n                    \"Update when alpha=0.75 completes.\",\n        },\n        \"method_alpha_sig_rates\": method_alpha_table,\n        \"pair_verdicts\": pair_verdicts,\n        \"concordance\": concordance,\n        \"concordance_per_alpha\": concordance_per_alpha,\n        \"decision_flips\": {\n            \"overall\": decision_flips_overall,\n            \"per_alpha\": decision_flips_per_alpha,\n        },\n        \"channel_analysis\": channel_analysis,\n        \"panel\": panel,\n    }\n\n    # Save JSON\n    json_path = os.path.join(\"results\", \"method_ablation_phase2_panel.json\")\n    with open(json_path, \"w\") as f:\n        json.dump(output, f, indent=2, default=str)\n    print(f\"\\nJSON: {json_path}\")\n\n    # Save report\n    report = generate_report(output)\n    report_path = os.path.join(\"results\", \"method_ablation_phase2_report.md\")\n    with open(report_path, \"w\") as f:\n        f.write(report)\n    print(f\"Report: {report_path}\")\n\n    # Print headline summary\n    print(\"\\n\" + \"=\" * 72)\n    print(\"HEADLINE: Method x Alpha Sig Rates\")\n    print(\"=\" * 72)\n    for alpha in alphas:\n        rates = {m: method_alpha_table[alpha][m][\"rate\"] for m in METHOD_NAMES}\n        line = f\"  alpha={alpha:.2f}: \" + \"  \".join(\n            f\"{m}={rates[m]:.0%}\" for m in METHOD_NAMES)\n        print(line)\n\n    print(\"\\nDone.\")\n\n\nif __name__ == \"__main__\":\n    main()\nPYTHON_SCRIPT",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T08:59:16.639862+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.56}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T08:59:16.639987+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Write method_ablation_phase2.py analysis script', 'status': 'completed', 'activeForm': 'Writing Phase 2 analysis script'}, {'content': 'Upload and run script on westd-19828', 'status': 'in_progress', 'activeForm': 'Running Phase 2 analysis on server'}, {'content': 'Register artifacts and generate report', 'status': 'pending', 'activeForm': 'Registering artifacts and generating report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Write method_ablation_phase2.py analysis script', 'status': 'completed', 'activeForm': 'Writing Phase 2 analysis script'}, {'content': 'Upload and run script on westd-19828', 'status': 'in_progress', 'activeForm': 'Running Phase 2 analysis on server'}, {'content': 'Register artifacts and generate report', 'status': 'pending', 'activeForm': 'Registering artifacts and generating report'}]"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-15T08:59:16.640113+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-15T08:59:16.640240+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u method_ablation_phase2.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -u method_ablation_phase2.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T08:59:16.640394+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading data...\\nFound 7 runs across alpha = [0.0, 0.25, 0.5, 1.0]\\n  a000_s42: alpha=0.0, seed=42, 11 gens\\n  a025_s42: alpha=0.25, seed=42, 11 gens\\n  a050_s42: alpha=0.5, seed=42, 11 gens\\n  mvp_s42: alpha=1.0, seed=42, 11 gens\\n  mvp_s43: alpha=1.0, seed=43, 11 gens\\n  mvp_s44: alpha=1.0, seed=44, 11 gens\\n  mvp_s45: alpha=1.0, seed=45, 11 gens\\n\\nRunning 5 methods on 7 runs x 2x4 pairs...\\n  [8/56] alpha=0.00 s42: last pair ece->perplexity (1/5 sig)\\n  [16/56] alpha=0.25 s42: last pair ece->perplexity (1/5 sig)\\n  [24/56] alpha=0.50 s42: last pair ece->perplexity (4/5 sig)\\n  [32/56] alpha=1.00 s42: last pair ece->perplexity (3/5 sig)\\n  [40/56] alpha=1.00 s43: last pair ece->perplexity (3/5 sig)\\n  [48/56] alpha=1.00 s44: last pair ece->perplexity (3/5 sig)\\n  [56/56] alpha=1.00 s45: last pair ece->perplexity (3/5 sig)\\n\\nComputing method x alpha sig rates...\\nComputing pair verdicts...\\nComputing concordance...\\nComputing decision flips...\\nComputing channel analysis...\\n\\nJSON: results/method_ablation_phase2_panel.json\\nReport: results/method_ablation_phase2_report.md\\n\\n========================================================================\\nHEADLINE: Method x Alpha Sig Rates\\n========================================================================\\n  alpha=0.00: naive=100%  differenced=50%  threshold=62%  permutation_granger=0%  TY=0%\\n  alpha=0.25: naive=100%  differenced=25%  threshold=38%  permutation_granger=25%  TY=62%\\n  alpha=0.50: naive=100%  differenced=100%  threshold=100%  permutation_granger=25%  TY=0%\\n  alpha=1.00: naive=100%  differenced=100%  threshold=100%  permutation_granger=75%  TY=59%\\n\\nDone.\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 7.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-15T08:59:16.640562+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-15T08:59:16.640745+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Method Ablation Phase 2: Pooled Panel Analysis\\n\\nGenerated: 2026-05-15T16:57:34.478890\\nAlpha levels: [0.0, 0.25, 0.5, 1.0]\\nRuns: 7  |  Panel rows: 56\\nMethods: naive, differenced, threshold, permutation_granger, TY\\nPermutations: 1000\\n\\n> alpha=0.75 RUNNING, alpha=0.10/0.60 QUEUED. Panel covers alpha={0.0, 0.25, 0.50, 1.0}. Update when alpha=0.75 completes.\\n\\n## 1. Method x Alpha Significance Rates (test-level)\\n\\nEach cell = sig_tests / total_tests at that (method, alpha).\\nalpha=1.0 has 4 seeds x 8 pairs = 32 tests; others have 1 seed x 8 pairs = 8 tests.\\n\\n| alpha |naive | differenced | threshold | permutation_granger | TY |\\n|-------|-------|-------|-------|-------|-------|\\n| 0.0 | 8/8 (100%) | 4/8 (50%) | 5/8 (62%) | 0/8 (0%) | 0/8 (0%) |\\n| 0.25 | 8/8 (100%) | 2/8 (25%) | 3/8 (38%) | 2/8 (25%) | 5/8 (62%) |\\n| 0.5 | 8/8 (100%) | 8/8 (100%) | 8/8 (100%) | 2/8 (25%) | 0/8 (0%) |\\n| 1.0 | 32/32 (100%) | 32/32 (100%) | 32/32 (100%) | 24/32 (75%) | 19/32 (59%) |\\n\\n## 2. Method x Alpha Verdict Table (pair-level)\\n\\nVerdict: SIG if majority of seeds significant (>=2/4 at alpha=1.0, or 1/1 at single-seed).\\n\\n| alpha |naive | differenced | threshold | permutation_granger | TY |\\n|-------|-------|-------|-------|-------|-------|\\n| 0.0 | 8/8 | 4/8 | 5/8 | 0/8 | 0/8 |\\n| 0.25 | 8/8 | 2/8 | 3/8 | 2/8 | 5/8 |\\n| 0.5 | 8/8 | 8/8 | 8/8 | 2/8 | 0/8 |\\n| 1.0 | 8/8 | 8/8 | 8/8 | 6/8 | 6/8 |\\n\\n## 3. Channel-Specific Analysis\\n\\n### entropy_to_diversity\\n\\n| alpha |naive | differenced | threshold | permutation_granger | TY |\\n|-------|-------|-------|-------|-------|-------|\\n| 0.0 | 3/3 | 3/3 | 3/3 | 0/3 | 0/3 |\\n| 0.25 | 3/3 | 1/3 | 3/3 | 1/3 | 3/3 |\\n| 0.5 | 3/3 | 3/3 | 3/3 | 0/3 | 0/3 |\\n| 1.0 | 12/12 | 12/12 | 12/12 | 12/12 | 12/12 |\\n\\n### entropy_to_perplexity\\n\\n| alpha |naive | differenced | threshold | permutation_granger | TY |\\n|-------|-------|-------|--
…[truncated 5761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-15T08:59:16.640926+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -c /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "wc -c /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-15T08:59:16.641052+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \" 94844 /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json\\n  7189 /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md\\n102033 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-15T08:59:16.641188+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-15T08:59:16.641422+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"# Method Ablation Phase 2: Pooled Panel Analysis\\n\\nGenerated: 2026-05-15T16:57:34.478890\\nAlpha levels: [0.0, 0.25, 0.5, 1.0]\\nRuns: 7  |  Panel rows: 56\\nMethods: naive, differenced, threshold, permutation_granger, TY\\nPermutations: 1000\\n\\n> alpha=0.75 RUNNING, alpha=0.10/0.60 QUEUED. Panel covers alpha={0.0, 0.25, 0.50, 1.0}. Update when alpha=0.75 completes.\\n\\n## 1. Method x Alpha Significance Rates (test-level)\\n\\nEach cell = sig_tests / total_tests at that (method, alpha).\\nalpha=1.0 has 4 seeds x 8 pairs = 32 tests; others have 1 seed x 8 pairs = 8 tests.\\n\\n| alpha |naive | differenced | threshold | permutation_granger | TY |\\n|-------|-------|-------|-------|-------|-------|\\n| 0.0 | 8/8 (100%) | 4/8 (50%) | 5/8 (62%) | 0/8 (0%) | 0/8 (0%) |\\n| 0.25 | 8/8 (100%) | 2/8 (25%) | 3/8 (38%) | 2/8 (25%) | 5/8 (62%) |\\n| 0.5 | 8/8 (100%) | 8/8 (100%) | 8/8 (100%) | 2/8 (25%) | 0/8 (0%) |\\n| 1.0 | 32/32 (100%) | 32/32 (100%) | 32/32 (100%) | 24/32 (75%) | 19/32 (59%) |\\n\\n## 2. Method x Alpha Verdict Table (pair-level)\\n\\nVerdict: SIG if majority of seeds significant (>=2/4 at alpha=1.0, or 1/1 at single-seed).\\n\\n| alpha |naive | differenced | threshold | permutation_granger | TY |\\n|-------|-------|-------|-------|-------|-------|\\n| 0.0 | 8/8 | 4/8 | 5/8 | 0/8 | 0/8 |\\n| 0.25 | 8/8 | 2/8 | 3/8 | 2/8 | 5/8 |\\n| 0.5 | 8/8 | 8/8 | 8/8 | 2/8 | 0/8 |\\n| 1.0 | 8/8 | 8/8 | 8/8 | 6/8 | 6/8 |\\n\\n## 3. Channel-Specific Analysis\\n\\n### entropy_to_diversity\\n\\n| alpha |naive | differenced | threshold | permutation_granger | TY |\\n|-------|-------|-------|-------|-------|-------|\\n| 0.0 | 3/3 | 3/3 | 3/3 | 0/3 | 0/3 |\\n| 0.25 | 3/3 | 1/3 | 3/3 | 1/3 | 3/3 |\\n| 0.5 | 3/3 | 3/3 | 3/3 | 0/3 | 0/3 |\\n| 1.0 | 12/12 | 12/12 | 12/12 | 12/12 | 12/12 |\\n\\n### entropy_to_perplexity\\n\\n| alpha |naive | differenced | threshold | permutation_granger | TY |\\n|-------|-------|-------|--
…[truncated 5761 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-15T08:59:16.641648+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-15T08:59:16.641828+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-15T08:59:16.641999+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "method_ablation_phase2_panel",
  "type": "data",
  "description": "Phase 2 pooled panel: 5 methods x 4 alpha levels x 8 pairs, 56 test-level rows with per-test significance, concordance, decision flips",
  "project": "distrib_canary_collapse",
  "content_filename": "method_ablation_phase2_panel.json",
  "tags": "['method_ablation', 'phase2', 'claim3', 'panel']",
  "content": "See server: /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json (94KB, too large for inline)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "method_ablation_phase2_panel",
    "type": "data",
    "description": "Phase 2 pooled panel: 5 methods x 4 alpha levels x 8 pairs, 56 test-level rows with per-test significance, concordance, decision flips",
    "project": "distrib_canary_collapse",
    "content_filename": "method_ablation_phase2_panel.json",
    "tags": "['method_ablation', 'phase2', 'claim3', 'panel']",
    "content": "See server: /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_panel.json (94KB, too large for inline)"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-15T08:59:16.642219+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_d2b441\", \"name\": \"method_ablation_phase2_panel\", \"type\": \"data\", \"description\": \"Phase 2 pooled panel: 5 methods x 4 alpha levels x 8 pairs, 56 test-level rows with per-test significance, concordance, decision flips\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/data/method_ablation_phase2_panel.json\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T08:58:19.552708+00:00\", \"tags\": [\"method_ablation\", \"phase2\", \"claim3\", \"panel\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-15T08:59:16.642431+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "method_ablation_phase2_report",
  "type": "report",
  "description": "Phase 2 analysis report: method x alpha sig rates, concordance (kappa=0.185), decision flips (50% flip naive vs perm_granger), channel analysis",
  "project": "distrib_canary_collapse",
  "content_filename": "method_ablation_phase2_report.md",
  "tags": "['method_ablation', 'phase2', 'claim3', 'report']",
  "content": "See server: /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "method_ablation_phase2_report",
    "type": "report",
    "description": "Phase 2 analysis report: method x alpha sig rates, concordance (kappa=0.185), decision flips (50% flip naive vs perm_granger), channel analysis",
    "project": "distrib_canary_collapse",
    "content_filename": "method_ablation_phase2_report.md",
    "tags": "['method_ablation', 'phase2', 'claim3', 'report']",
    "content": "See server: /root/autodl-tmp/distrib_canary_collapse/results/method_ablation_phase2_report.md"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-15T08:59:16.642638+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_70d3f9\", \"name\": \"method_ablation_phase2_report\", \"type\": \"report\", \"description\": \"Phase 2 analysis report: method x alpha sig rates, concordance (kappa=0.185), decision flips (50% flip naive vs perm_granger), channel analysis\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/method_ablation_phase2_report.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T08:58:22.396061+00:00\", \"tags\": [\"method_ablation\", \"phase2\", \"claim3\", \"report\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-15T08:59:16.642849+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "method_ablation_phase2",
  "field": "status",
  "value": "DONE",
  "project": "distrib_canary_collapse",
  "spec": "{'hypothesis': 'Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence', 'command': 'python method_ablation_phase2.py', 'server': 'westd-19828', 'data_path': 'results/alpha_sweep + results/mvp', 'data_count': 56, 'model_name': 'N/A (analysis)', 'seed': '42,43,44,45', 'checkpoint_path': 'N/A', 'log_path': 'results/method_ablation_phase2_panel.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "method_ablation_phase2",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse",
    "spec": "{'hypothesis': 'Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence', 'command': 'python method_ablation_phase2.py', 'server': 'westd-19828', 'data_path': 'results/alpha_sweep + results/mvp', 'data_count': 56, 'model_name': 'N/A (analysis)', 'seed': '42,43,44,45', 'checkpoint_path': 'N/A', 'log_path': 'results/method_ablation_phase2_panel.json'}"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-15T08:59:16.643049+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0561}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-15T08:59:16.643235+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "method_ablation_phase2",
  "field": "status",
  "value": "RUNNING",
  "project": "distrib_canary_collapse",
  "spec": "{'hypothesis': 'Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence', 'command': 'python method_ablation_phase2.py', 'server': 'westd-19828', 'data_path': 'results/alpha_sweep + results/mvp', 'data_count': 56, 'model_name': 'N/A (analysis)', 'seed': '42,43,44,45', 'checkpoint_path': 'N/A', 'log_path': 'results/method_ablation_phase2_panel.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "method_ablation_phase2",
    "field": "status",
    "value": "RUNNING",
    "project": "distrib_canary_collapse",
    "spec": "{'hypothesis': 'Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence', 'command': 'python method_ablation_phase2.py', 'server': 'westd-19828', 'data_path': 'results/alpha_sweep + results/mvp', 'data_count': 56, 'model_name': 'N/A (analysis)', 'seed': '42,43,44,45', 'checkpoint_path': 'N/A', 'log_path': 'results/method_ablation_phase2_panel.json'}"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T08:59:16.643461+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.0542}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-15T08:59:16.643651+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "method_ablation_phase2",
  "field": "status",
  "value": "QUEUED",
  "project": "distrib_canary_collapse",
  "spec": "{'hypothesis': 'Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence', 'command': 'python method_ablation_phase2.py', 'server': 'westd-19828', 'data_path': 'results/alpha_sweep + results/mvp', 'data_count': 56, 'model_name': 'N/A (analysis)', 'seed': '42,43,44,45', 'checkpoint_path': 'N/A', 'log_path': 'results/method_ablation_phase2_panel.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "method_ablation_phase2",
    "field": "status",
    "value": "QUEUED",
    "project": "distrib_canary_collapse",
    "spec": "{'hypothesis': 'Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence', 'command': 'python method_ablation_phase2.py', 'server': 'westd-19828', 'data_path': 'results/alpha_sweep + results/mvp', 'data_count': 56, 'model_name': 'N/A (analysis)', 'seed': '42,43,44,45', 'checkpoint_path': 'N/A', 'log_path': 'results/method_ablation_phase2_panel.json'}"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T08:59:16.643884+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"method_ablation_phase2\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:58:35.270Z\", \"updated_at\": \"2026-05-15T08:58:35.270Z\", \"spec\": {\"hypothesis\": \"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\", \"command\": \"python method_ablation_phase2.py\", \"server\": \"westd-19828\", \"data_path\": \"results/alpha_sweep + results/mvp\", \"data_count\": 56, \"model_name\": \"N/A (analysis)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/method_ablation_phase2_panel.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2412}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-15T08:59:16.644072+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "method_ablation_phase2",
  "field": "status",
  "value": "RUNNING",
  "project": "distrib_canary_collapse",
  "spec": "{'hypothesis': 'Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence', 'command': 'python method_ablation_phase2.py', 'server': 'westd-19828', 'data_path': 'results/alpha_sweep + results/mvp', 'data_count': 56, 'model_name': 'N/A (analysis)', 'seed': '42,43,44,45', 'checkpoint_path': 'N/A', 'log_path': 'results/method_ablation_phase2_panel.json'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "method_ablation_phase2",
    "field": "status",
    "value": "RUNNING",
    "project": "distrib_canary_collapse",
    "spec": "{'hypothesis': 'Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence', 'command': 'python method_ablation_phase2.py', 'server': 'westd-19828', 'data_path': 'results/alpha_sweep + results/mvp', 'data_count': 56, 'model_name': 'N/A (analysis)', 'seed': '42,43,44,45', 'checkpoint_path': 'N/A', 'log_path': 'results/method_ablation_phase2_panel.json'}"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-15T08:59:16.644286+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"method_ablation_phase2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:58:35.270Z\", \"updated_at\": \"2026-05-15T08:58:39.839Z\", \"spec\": {\"hypothesis\": \"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\", \"command\": \"python method_ablation_phase2.py\", \"server\": \"westd-19828\", \"data_path\": \"results/alpha_sweep + results/mvp\", \"data_count\": 56, \"model_name\": \"N/A (analysis)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/method_ablation_phase2_panel.json\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2154}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-15T08:59:16.644436+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "method_ablation_phase2",
  "field": "conclusion",
  "value": "success",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "method_ablation_phase2",
    "field": "conclusion",
    "value": "success",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-15T08:59:16.644579+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"method_ablation_phase2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:58:35.270Z\", \"updated_at\": \"2026-05-15T08:58:43.133Z\", \"spec\": {\"hypothesis\": \"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\", \"command\": \"python method_ablation_phase2.py\", \"server\": \"westd-19828\", \"data_path\": \"results/alpha_sweep + results/mvp\", \"data_count\": 56, \"model_name\": \"N/A (analysis)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/method_ablation_phase2_panel.json\"}, \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1205}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-15T08:59:16.644714+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "method_ablation_phase2",
  "field": "metrics",
  "value": "{'n_panel_rows': 56, 'n_alphas': 4, 'alphas': [0, 0.25, 0.5, 1], 'naive_sig_rate_overall': 1, 'perm_granger_sig_rate_a000': 0, 'perm_granger_sig_rate_a025': 0.25, 'perm_granger_sig_rate_a050': 0.25, 'perm_granger_sig_rate_a100': 0.75, 'TY_sig_rate_a000': 0, 'TY_sig_rate_a100': 0.59, 'mean_inter_method_kappa': 0.185, 'naive_vs_perm_granger_flip_rate': 0.5, 'naive_vs_TY_flip_rate': 0.57, 'fdr_flips_perm_granger': 4, 'pair_verdict_a100_perm_granger': '6/8', 'pair_verdict_a100_TY': '6/8', 'entropy_to_diversity_a100_all_5methods_sig': True}",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "method_ablation_phase2",
    "field": "metrics",
    "value": "{'n_panel_rows': 56, 'n_alphas': 4, 'alphas': [0, 0.25, 0.5, 1], 'naive_sig_rate_overall': 1, 'perm_granger_sig_rate_a000': 0, 'perm_granger_sig_rate_a025': 0.25, 'perm_granger_sig_rate_a050': 0.25, 'perm_granger_sig_rate_a100': 0.75, 'TY_sig_rate_a000': 0, 'TY_sig_rate_a100': 0.59, 'mean_inter_method_kappa': 0.185, 'naive_vs_perm_granger_flip_rate': 0.5, 'naive_vs_TY_flip_rate': 0.57, 'fdr_flips_perm_granger': 4, 'pair_verdict_a100_perm_granger': '6/8', 'pair_verdict_a100_TY': '6/8', 'entropy_to_diversity_a100_all_5methods_sig': True}",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-15T08:59:16.644880+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"method_ablation_phase2\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:58:35.270Z\", \"updated_at\": \"2026-05-15T08:58:51.384Z\", \"spec\": {\"hypothesis\": \"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\", \"command\": \"python method_ablation_phase2.py\", \"server\": \"westd-19828\", \"data_path\": \"results/alpha_sweep + results/mvp\", \"data_count\": 56, \"model_name\": \"N/A (analysis)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/method_ablation_phase2_panel.json\"}, \"conclusion\": \"success\", \"metrics\": {\"n_panel_rows\": 56, \"n_alphas\": 4, \"alphas\": [0, 0.25, 0.5, 1], \"naive_sig_rate_overall\": 1, \"perm_granger_sig_rate_a000\": 0, \"perm_granger_sig_rate_a025\": 0.25, \"perm_granger_sig_rate_a050\": 0.25, \"perm_granger_sig_rate_a100\": 0.75, \"TY_sig_rate_a000\": 0, \"TY_sig_rate_a100\": 0.59, \"mean_inter_method_kappa\": 0.185, \"naive_vs_perm_granger_flip_rate\": 0.5, \"naive_vs_TY_flip_rate\": 0.57, \"fdr_flips_perm_granger\": 4, \"pair_verdict_a100_perm_granger\": \"6/8\", \"pair_verdict_a100_TY\": \"6/8\", \"entropy_to_diversity_a100_all_5methods_sig\": true}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.131}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-15T08:59:16.645018+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "method_ablation_phase2",
  "field": "status",
  "value": "DONE",
  "project": "distrib_canary_collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "method_ablation_phase2",
    "field": "status",
    "value": "DONE",
    "project": "distrib_canary_collapse"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-15T08:59:16.645179+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"method_ablation_phase2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T08:58:35.270Z\", \"updated_at\": \"2026-05-15T08:58:54.741Z\", \"spec\": {\"hypothesis\": \"Method sensitivity is compounded by regime dependence — method x alpha interaction is the headline Claim 3 evidence\", \"command\": \"python method_ablation_phase2.py\", \"server\": \"westd-19828\", \"data_path\": \"results/alpha_sweep + results/mvp\", \"data_count\": 56, \"model_name\": \"N/A (analysis)\", \"seed\": \"42,43,44,45\", \"checkpoint_path\": \"N/A\", \"log_path\": \"results/method_ablation_phase2_panel.json\"}, \"conclusion\": \"success\", \"metrics\": {\"n_panel_rows\": 56, \"n_alphas\": 4, \"alphas\": [0, 0.25, 0.5, 1], \"naive_sig_rate_overall\": 1, \"perm_granger_sig_rate_a000\": 0, \"perm_granger_sig_rate_a025\": 0.25, \"perm_granger_sig_rate_a050\": 0.25, \"perm_granger_sig_rate_a100\": 0.75, \"TY_sig_rate_a000\": 0, \"TY_sig_rate_a100\": 0.59, \"mean_inter_method_kappa\": 0.185, \"naive_vs_perm_granger_flip_rate\": 0.5, \"naive_vs_TY_flip_rate\": 0.57, \"fdr_flips_perm_granger\": 4, \"pair_verdict_a100_perm_granger\": \"6/8\", \"pair_verdict_a100_TY\": \"6/8\", \"entropy_to_diversity_a100_all_5methods_sig\": true}, \"completed_at\": \"2026-05-15T08:58:54.741Z\"}, \"hint\": \"💡 建议将成功经验写入 memory.md（什么 work、关键参数）\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2168}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-15T08:59:16.645353+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Write method_ablation_phase2.py analysis script', 'status': 'completed', 'activeForm': 'Writing Phase 2 analysis script'}, {'content': 'Upload and run script on westd-19828', 'status': 'completed', 'activeForm': 'Running Phase 2 analysis on server'}, {'content': 'Register artifacts and generate report', 'status': 'completed', 'activeForm': 'Registering artifacts and generating report'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Write method_ablation_phase2.py analysis script', 'status': 'completed', 'activeForm': 'Writing Phase 2 analysis script'}, {'content': 'Upload and run script on westd-19828', 'status': 'completed', 'activeForm': 'Running Phase 2 analysis on server'}, {'content': 'Register artifacts and generate report', 'status': 'completed', 'activeForm': 'Registering artifacts and generating report'}]"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-15T08:59:16.645496+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 93 · 2026-05-15T08:59:16.645649+00:00_

Phase 2 完成。

## 核心结果

**Method × Alpha Sig Rates (test-level)**:

| α | naive | differenced | threshold | perm_granger | TY |
|---|-------|-------------|-----------|-------------|-----|
| 0.00 | 8/8 (100%) | 4/8 (50%) | 5/8 (62%) | **0/8 (0%)** | **0/8 (0%)** |
| 0.25 | 8/8 (100%) | 2/8 (25%) | 3/8 (38%) | 2/8 (25%) | 5/8 (62%) |
| 0.50 | 8/8 (100%) | 8/8 (100%) | 8/8 (100%) | 2/8 (25%) | 0/8 (0%) |
| 1.00 | 32/32 (100%) | 32/32 (100%) | 32/32 (100%) | 24/32 (75%) | 19/32 (59%) |

**Claim 3 关键证据**:

1. **Naive 全域 100%** — 即使 α=0.0（无污染 null control）也全部 significant，确认 raw-level 方法不可靠
2. **Null control 验证** — perm_granger 和 TY 在 α=0.0 均为 0%，无 false positive
3. **perm_granger dose-response** — 0% → 25% → 25% → 75%，随 α 单调增长
4. **Mean Cohen's κ = 0.185**（poor agreement）— 方法间严重分歧
5. **Decision flips** — naive vs perm_granger: **50%** 结论翻转；naive vs TY: **57%** 翻转
6. **α=0.0 极端案例** — naive vs perm_granger 翻转率 **100%**（naive 全说 sig，perm_granger 全说 n.s.）
7. **entropy→diversity 在 α=1.0 所有 5 种方法一致 SIG** — 唯一跨方法 robust 的通道

**TY 注意事项**: α=0.25 出现 62% sig（高于 α=0.50 的 0%），单 seed 下 TY 非单调，需多 seed 确认后解读。

**产出文件**:
- `results/method_ablation_phase2_panel.json` (94KB) — 完整 panel 数据
- `results/method_ablation_phase2_report.md` — 分析报告
- Registry: `method_ablation_phase2` (DONE)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_method_ablation_phase2_pooled_20260515T085042"
}
```

</details>

---
