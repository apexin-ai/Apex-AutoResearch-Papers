# verify raw data files

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_verify_raw_data_files_20260515T030412.jsonl`
- **Structured JSON:** [`15d7f1675540c82a31cd.json`](../../sessions/15/15d7f1675540c82a31cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-15T03:05:17.426815+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T03:05:17.427171+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T03:05:17.427384+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_inference/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_inference/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T03:05:17.427528+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_inference/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_inference/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T03:05:17.427663+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_inference/samples.jsonl': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.84}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T03:05:17.427794+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"wc: /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_inference/samples.jsonl: No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T03:05:17.427918+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T03:05:17.428037+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 6.4M May 15 02:59 /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T03:05:17.428171+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T03:05:17.428294+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_n16/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T03:05:17.428415+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T03:05:17.428531+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 9.1M May 15 01:41 /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T03:05:17.428642+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T03:05:17.428754+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3453 /root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T03:05:17.428877+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T03:05:17.429029+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 3.7M May 15 06:17 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T03:05:17.429161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T03:05:17.429284+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T03:05:17.429395+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T03:05:17.429540+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"bootstrap_ci_nscaling\\nbootstrap_ci_summary.json\\nbootstrap_ci_tables.tex\\nconditional_filter_diagnosis.json\\nexp001_n16_seed123\\nexp001_n16_seed123_200only\\nexp001_n16_seed123_200only_backup\\nexp001_n16_seed123_full\\nexp001_n16_seed123_run.log\\nexp001_n16_seed42\\nexp001_n16_seed42_200only_backup\\nexp001_n16_seed42_run.log\\nexp001_n16_seed456\\nexp001_n16_seed456_200only\\nexp001_seed123_t10_full\\nexp001_seed123_t10_full.log\\nexp001_seed456_t10_full\\nexp001_seed456_t10_full.log\\nexp002_conll2003\\nexp003_wnut17_dryrun\\nexp003_wnut17_eval\\nexp003_wnut17_eval.log\\nexp003_wnut17_pilot\\nexp003_wnut17_pilot.log\\nexp004_re_diagnostic\\nexp004v2_re_diagnostic\\nexp007_llama_dryrun\\nexp007_llama_inference\\nexp008_re_n16\\nexp008_re_n16_200only\\nexp008_re_n16_t10_full\\nexp008_re_n16_t10_full.log\\nexp009_stratification_results.json\\nexp010_selection_curves\\nexp016_signal_ensemble\\nexp_001_seed123_v2\\nexp_001_seed123_v2_r1024\\nexp_001_seed42_v2\\nexp_001_seed42_v2_r1024\\nexp_001_seed456_v2\\nexp_001_seed456_v2_ner\\nexp_001_seed456_v2_ner.log\\nexp_001_seed456_v2_ner_r1024\\nexp_002_conll_n16\\nexp_002_conll_n16.log\\nexp_002_conll_n16_r1024\\nexp_003_wnut17_v2_infer\\nexp_005_v2_temperature\\nexp_006_v2\\nexp_006_v2_run.log\\nexp_007_llama_n16\\nexp_007_llama_n16.log\\nexp_007_llama_n16_r1024\\nexp_007_llama_seed123\\nexp_007_llama_seed456\\nexp_008_re_n16_v2\\nexp_008_re_seed123\\nexp_009_v2\\nexp_009_v2_re_rerun\\nexp_009_v2_run.log\\nexp_012_logprob\\nexp_012_rerun_1024\\nexp_015_unified\\nexp_015_v2\\nexp_016_rerun_1024\\nexp_016_v2\\nexp_017_llama_conll_infer\\nexp_017_llama_conll_infer.log\\nexp_017_llama_conll_n16\\nexp_017_llama_conll_n16_s123\\nexp_017_llama_conll_n16_s123.log\\nexp_017_llama_conll_n16_s123_r1024\\nexp_017_llama_conll_n16_s456\\nexp_017_llama_conll_n16_s456.log\\nexp_017_llama_conll_n16_s456_r1024\\ngate0_all_predictions.jsonl\\ngate0_ft002v2\\ngate0_ft002v2_ckpt4
…[truncated 443 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T03:05:17.429684+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T03:05:17.429847+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4.6M\\n-rw-r--r-- 1 root root 1.8K May 14 21:50 report.json\\n-rw-r--r-- 1 root root 4.6M May 14 21:50 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T03:05:17.430038+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_016_rerun_1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T03:05:17.430253+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*.py\" -maxdepth 3",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "find /root/autodl-tmp/struct_self_consist_ie/ -name \"*.py\" -maxdepth 3",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T03:05:17.430451+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 192K\\n-rw-r--r-- 1 root root  49K May 15 07:16 correlation_matrix.json\\n-rw-r--r-- 1 root root  11K May 15 07:16 linear_combo_grid.json\\n-rw-r--r-- 1 root root  15K May 15 07:16 logistic_ensemble.json\\n-rw-r--r-- 1 root root  537 May 15 07:16 selection_f1_comparison.json\\n-rw-r--r-- 1 root root 104K May 15 07:16 selection_f1_full.json\\n-rw-r--r-- 1 root root 2.1K May 15 07:16 summary.md\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T03:05:17.430708+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/downsample_train.py\\n/root/autodl-tmp/struct_self_consist_ie/output/exp010_selection_curves/plot_selection_curves.py\\n/root/autodl-tmp/struct_self_consist_ie/code/data_utils.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_to_llamafactory.py\\n/root/autodl-tmp/struct_self_consist_ie/code/evaluation.py\\n/root/autodl-tmp/struct_self_consist_ie/code/consistency.py\\n/root/autodl-tmp/struct_self_consist_ie/code/sampling.py\\n/root/autodl-tmp/struct_self_consist_ie/code/run_mvp_pilot.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_diagnose.py\\n/root/autodl-tmp/struct_self_consist_ie/code/gate0_realign_eval.py\\n/root/autodl-tmp/struct_self_consist_ie/code/mvp_pilot.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_component_wise_re.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_wnut17.py\\n/root/autodl-tmp/struct_self_consist_ie/code/convert_conll2003.py\\n/root/autodl-tmp/struct_self_consist_ie/code/extract_logprobs.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_logprob_baseline.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exact_match_voting.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_entity_voting.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp015_unified.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp004_re_diagnostic.py\\n/root/autodl-tmp/struct_self_consist_ie/code/exp001_postprocess.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp016_ensemble.py\\n/root/autodl-tmp/struct_self_consist_ie/code/diagnose_logprob_rho.py\\n/root/autodl-tmp/struct_self_consist_ie/code/analyze_exp002_conll2003.py\\n/root/autodl-tmp/struct_self_consist_ie/code/_backup_cond_fix/run_mvp_pilot.py\\n/root/autodl-tmp/struct_self_consist_ie/code/_backup_cond_fix/analyze_exp015_unified.py\\n/root/autodl-tmp/struct_
…[truncated 2677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T03:05:17.430932+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/src/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/src/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T03:05:17.431291+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/src/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T03:05:17.431574+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T03:05:17.431782+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 3.6M\\n-rw-r--r-- 1 root root 3.3K May 14 21:58 report.json\\n-rw-r--r-- 1 root root 3.6M May 14 21:58 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T03:05:17.431959+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll2003/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll2003/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T03:05:17.432154+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll2003/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T03:05:17.432335+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T03:05:17.432520+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 9.4M\\n-rw-r--r-- 1 root root 3.8K May 14 20:39 exp002_5signal_report.json\\n-rw-r--r-- 1 root root 1.7K May 14 20:36 report.json\\n-rw-r--r-- 1 root root 9.4M May 14 20:36 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T03:05:17.432701+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T03:05:17.432904+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"1287 /root/autodl-tmp/struct_self_consist_ie/output/exp003_wnut17_eval/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T03:05:17.433075+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T03:05:17.433273+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 6.6M\\n-rw-r--r-- 1 root root 3.0K May 15 05:15 all_signals_report.json\\n-rw-r--r-- 1 root root 3.0K May 15 05:37 re_all_signals_report.json\\n-rw-r--r-- 1 root root 1.7K May 14 22:43 report.json\\n-rw-r--r-- 1 root root 105K May 14 22:43 run.log\\n-rw-r--r-- 1 root root 6.5M May 14 22:43 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T03:05:17.433465+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_dryrun/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_dryrun/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T03:05:17.433605+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 16K\\n-rw-r--r-- 1 root root 2.2K May 14 21:54 report.json\\n-rw-r--r-- 1 root root 8.3K May 14 21:54 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T03:05:17.433760+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T03:05:17.433886+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp007_llama_inference/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T03:05:17.434004+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T03:05:17.434143+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3453 /root/autodl-tmp/struct_self_consist_ie/output/exp002_conll2003/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T03:05:17.434312+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "wc -l /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T03:05:17.434440+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"551 /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T03:05:17.434556+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2_r1024/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls -lh /root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2_r1024/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T03:05:17.434682+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 6.7M\\n-rw-r--r-- 1 root root 1.7K May 15 06:28 report.json\\n-rw-r--r-- 1 root root 104K May 15 06:28 run.log\\n-rw-r--r-- 1 root root 6.6M May 15 06:28 samples.jsonl\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T03:05:17.434798+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "autodl-5090",
  "command": "ls /root/autodl-tmp/struct_self_consist_ie/code/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "autodl-5090",
    "command": "ls /root/autodl-tmp/struct_self_consist_ie/code/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-15T03:05:17.435152+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"__pycache__\\n_backup_cond_fix\\nanalyze_3seed_5signal.py\\nanalyze_component_wise_re.py\\nanalyze_entity_voting.py\\nanalyze_exact_match_voting.py\\nanalyze_exp002_conll2003.py\\nanalyze_exp004_re_diagnostic.py\\nanalyze_exp004_v2_re_diagnostic.py\\nanalyze_exp005_v2_temperature.py\\nanalyze_exp012_rerun_5signal.py\\nanalyze_exp015_unified.py\\nanalyze_exp015_v2_metrics.py\\nanalyze_exp016_ensemble.py\\nanalyze_exp017_5signal.py\\nanalyze_exp017_llama_conll_n16.py\\nanalyze_exp017_llama_conll_n16_s123.py\\nanalyze_logprob_baseline.py\\ncompute_re_conditional.py\\nconsistency.py\\nconvert_conll2003.py\\nconvert_to_llamafactory.py\\nconvert_wnut17.py\\ndata_utils.py\\ndiagnose_logprob_rho.py\\neval_exp012_rerun_auroc.py\\neval_n16_5signal.py\\neval_n8_5signal.py\\neval_s456_5signal.py\\nevaluation.py\\nexp001_3seed_all_signals.py\\nexp001_postprocess.py\\nexp009_stratification_analysis.py\\nexp010_selection_curves.py\\nexp_006_v2_selection.py\\nexp_009_v2_re_rerun.py\\nexp_009_v2_stratification.py\\nexp_016_v2_ensemble.py\\nextract_logprobs.py\\ngate0_diagnose.py\\ngate0_eval.py\\ngate0_realign_eval.py\\ngen_reliability_1024.py\\nmvp_pilot.py\\nplot_reliability_1024.py\\nplot_selection_gap_1024.py\\nrun_mvp_pilot.py\\nsampling.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_verify_raw_data_files_20260515T030412",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-15T03:05:17.435394+00:00_

汇总结果：

## 文件检查汇总

| Task | 文件路径 | 状态 | 大小 | 行数 | 备注 |
|------|---------|------|------|------|------|
| **A1** LLaMA SciERC N=8 | `exp007_llama_inference/samples.jsonl` | ✅ 存在 | 3.6M | 551 | 注意实际目录名无下划线：`exp007_llama_inference` 而非 `exp_007_llama_inference` |
| **A2** LLaMA SciERC N=16 | `exp_007_llama_n16/samples.jsonl` | ✅ 存在 | 6.4M | 551 | |
| **A3** Qwen CoNLL N=8 | `exp002_conll2003/samples.jsonl` | ✅ 存在 | 9.4M | 3453 | 实际目录名 `exp002_conll2003`（无下划线） |
| **A4** LLaMA CoNLL N=8 | `exp_017_llama_conll_infer/samples.jsonl` | ✅ 存在 | 9.1M | 3453 | |
| **B** WNUT-17 | `exp003_wnut17_eval/samples.jsonl` | ✅ 存在 | 4.6M | 1287 | 目录还含 `report.json` (1.8K) |
| **C** Qwen SciERC N=8 seed=42 | `exp_012_rerun_1024/samples.jsonl` | ✅ 存在 | 3.7M | 551 | `exp_001_seed42_v2/samples.jsonl` 也存在 (6.5M, 551行) |
| **D** exp_016 RE selection | `exp_016_rerun_1024/` | ✅ 存在 | ~192K | — | 含 6 个 JSON 文件 + summary.md，**无 samples.jsonl**（这是分析结果目录） |
| **E1** 代码目录 | `code/` | ✅ 存在 | — | — | 47 个 .py 文件，含 `consistency.py`, `evaluation.py`, `sampling.py` 等核心模块。无 `src/` 目录 |

**关键发现：**
- 所有 raw sample 文件均存在，无缺失
- 命名不一致：旧实验用 `expNNN`（无下划线），新实验用 `exp_NNN`
- CoNLL 数据集 (3453行) 远大于 SciERC (551行)
- `exp_016_rerun_1024` 是 RE selection 分析结果，不含 raw samples

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_verify_raw_data_files_20260515T030412"
}
```

</details>

---
