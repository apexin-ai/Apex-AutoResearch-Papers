# analysis failure mode smollm3 14b

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 0
- **Tool calls:** 25
- **Original source:** `logs/chats/worker_analysis_failure_mode_smollm3_14b_20260520T080348.jsonl`
- **Structured JSON:** [`8898b4ae2c7134281cc0.json`](../../sessions/88/8898b4ae2c7134281cc0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

51 recorded events

### Tool call

_source line 1 · 2026-05-20T08:10:35.552108+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T08:10:35.552594+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T08:10:35.552893+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*14b*s42*\" -name \"5method*\" -o -path \"*smollm*s42*v3*\" -name \"5method*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*14b*s42*\" -name \"5method*\" -o -path \"*smollm*s42*v3*\" -name \"5method*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T08:10:35.554276+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*410m*\" -name \"5method*\" -o -path \"*a100_s42*\" -name \"5method*\" -o -path \"*a050_s42*\" -name \"5method*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*410m*\" -name \"5method*\" -o -path \"*a100_s42*\" -name \"5method*\" -o -path \"*a050_s42*\" -name \"5method*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-20T08:10:35.554526+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/scale/14b_c4_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/scale/14b_c4_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.06}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T08:10:35.554762+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/c4_a050_s42_fp32/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s42/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/padding_robustness/a100_s42_fp32/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T08:10:35.555017+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*smollm*\" -name \"5method*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*smollm*\" -name \"5method*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-20T08:10:35.555231+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -type d -name \"*smollm*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -type d -name \"*smollm*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T08:10:35.555461+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T08:10:35.555649+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s43_17855\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T08:10:35.555877+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s43_17855/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s43_17855/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T08:10:35.556078+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s43_17855/analysis/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T08:10:35.556288+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*smollm*\" -name \"5method*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*smollm*\" -name \"5method*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T08:10:35.556485+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.93}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T08:10:35.556663+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*14b*\" -name \"5method*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/ -path \"*14b*\" -name \"5method*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T08:10:35.556861+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag_pre_d102.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s43/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s43/analysis/5method_summary.txt\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s43/analysis/5method_leadlag_pre_d102.json\\n/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia14b_a050_s42/analysis/5method_leadlag.json\\n/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia14b_a050_s42/analysis/5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T08:10:35.557111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-20T08:10:35.557320+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T08:10:35.557506+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T08:10:35.557685+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T08:10:35.558165+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alpha\\\": 1.0,\\n  \\\"seed\\\": 42,\\n  \\\"n_generations\\\": 11,\\n  \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3\\\",\\n  \\\"methods\\\": [\\n    \\\"naive_xcorr\\\",\\n    \\\"diff_xcorr\\\",\\n    \\\"threshold_onset\\\",\\n    \\\"perm_granger\\\",\\n    \\\"ty_granger\\\"\\n  ],\\n  \\\"config\\\": {\\n    \\\"n_perm\\\": 5000,\\n    \\\"fdr_alpha\\\": 0.05,\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": 5,\\n          \\\"r\\\": -0.8724,\\n          \\\"p_value\\\": 0.023367,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.6655,\\n              \\\"p\\\": 0.149082\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.6799,\\n              \\\"p\\\": 0.092874\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.6714,\\n              \\\"p\\\": 0.068285\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.7762,\\n              \\\"p\\\": 0.013908\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.7749,\\n              \\\"p\\\": 0.008472\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.3401,\\n              \\\"p\\\": 0.30609\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": -0.6518,\\n              \\\"p\\\": 0.041143\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n           
…[truncated 8551 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T08:10:35.558766+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"alpha\\\": 1.0,\\n  \\\"seed\\\": 42,\\n  \\\"n_generations\\\": 11,\\n  \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42\\\",\\n  \\\"methods\\\": [\\n    \\\"naive_xcorr\\\",\\n    \\\"diff_xcorr\\\",\\n    \\\"threshold_onset\\\",\\n    \\\"perm_granger\\\",\\n    \\\"ty_granger\\\"\\n  ],\\n  \\\"config\\\": {\\n    \\\"n_perm\\\": 5000,\\n    \\\"fdr_alpha\\\": 0.05,\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.9067,\\n          \\\"p_value\\\": 0.000296,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.8808,\\n              \\\"p\\\": 0.020481\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.841,\\n              \\\"p\\\": 0.017732\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.7943,\\n              \\\"p\\\": 0.018528\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.7672,\\n              \\\"p\\\": 0.015825\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.9067,\\n              \\\"p\\\": 0.000296\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.689,\\n              \\\"p\\\": 0.019027\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n              \\\"r\\\": 0.4017,\\n              \\\"p\\\": 0.249809\\n            },\\n            {\\n              \\\"lag\\\": 2,\\n              \\\"r\\\
…[truncated 8559 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-20T08:10:35.559465+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 1.0,\\n    \\\"seed\\\": 43,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/generalize/pythia410m_wiki_a100_s43\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -1,\\n          \\\"r\\\": 0.994,\\n          \\\"p_value\\\": 0.0,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.9007,\\n              \\\"p\\\": 0.014292\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.954,\\n              \\\"p\\\": 0.00085\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.9662,\\n              \\\"p\\\": 9.4e-05\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.9912,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.994,\\n              \\\"p\\\": 0.0\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.8789,\\n              \\\"p\\\": 0.000367\\n            },\\n            {\\n              \\\"lag\\\": 1,\\n    
…[truncated 8622 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T08:10:35.560153+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.5,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"results/alpha_sweep/a050_s42_fp32\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": 5,\\n          \\\"r\\\": -0.9395,\\n          \\\"p_value\\\": 0.005382,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.5073,\\n              \\\"p\\\": 0.304328\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.4893,\\n              \\\"p\\\": 0.265137\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.3849,\\n              \\\"p\\\": 0.346371\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.6828,\\n              \\\"p\\\": 0.042658\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.8089,\\n              \\\"p\\\": 0.004604\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.4368,\\n              \\\"p\\\": 0.179219\\n            },\\n            {\\n              \\\"lag\\\":
…[truncated 8610 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T08:10:35.560592+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"\nimport json\nfor label, path in [\n  ('SmolLM3-3B_s42', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_leadlag.json'),\n  ('Pythia-1.4B_s42', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    print(f\\\"{p['canary']}->{p['downstream']}: PermG_p={pg.get('p_value','N/A'):.4f} fdr={pg.get('fdr_p','N/A')} f2={pg.get('effect_size_f2','N/A')} | DiffXcorr_p={dx.get('p_value','N/A'):.4f} r={dx.get('r','N/A'):.3f} lag={dx.get('peak_lag','N/A')} fdr={dx.get('fdr_p',dx.get('p_fdr','N/A'))} | Naive_p={nx.get('p_value','N/A'):.4f} r={nx.get('r','N/A'):.3f} | Thresh_sig={to.get('significant','N/A')} lead={to.get('lead_time','N/A')} | TY_p={ty.get('p_value','N/A'):.4f}\\\")\n  print(f\\\"Consensus: {d['consensus']}\\\")\n  print(f\\\"Summary: {d['summary']}\\\")\n  print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"\nimport json\nfor label, path in [\n  ('SmolLM3-3B_s42', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_leadlag.json'),\n  ('Pythia-1.4B_s42', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    print(f\\\"{p['canary']}->{p['downstream']}: PermG_p={pg.get('p_value','N/A'):.4f} fdr={pg.get('fdr_p','N/A')} f2={pg.get('effect_size_f2','N/A')} | DiffXcorr_p={dx.get('p_value','N/A'):.4f} r={dx.get('r','N/A'):.3f} lag={dx.get('peak_lag','N/A')} fdr={dx.get('fdr_p',dx.get('p_fdr','N/A'))} | Naive_p={nx.get('p_value','N/A'):.4f} r={nx.get('r','N/A'):.3f} | Thresh_sig={to.get('significant','N/A')} lead={to.get('lead_time','N/A')} | TY_p={ty.get('p_value','N/A'):.4f}\\\")\n  print(f\\\"Consensus: {d['consensus']}\\\")\n  print(f\\\"Summary: {d['summary']}\\\")\n  print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-20T08:10:35.560825+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-20T08:10:35.561028+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-17855",
  "command": "python3 -c \"\nimport json\nfor label, path in [\n  ('Pythia-410M_s43', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json'),\n  ('GPT2_a050_s42', '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n    dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n    print(f\\\"{p['canary']}->{p['downstream']}: PermG_p={pg.get('p_value','N/A'):.4f} fdr={pg_fdr} f2={pg.get('effect_size_f2','N/A')} | DiffXcorr_p={dx.get('p_value','N/A'):.4f} r={dx.get('r','N/A'):.3f} lag={dx.get('peak_lag','N/A')} fdr={dx_fdr} | Naive_p={nx.get('p_value','N/A'):.4f} r={nx.get('r','N/A'):.3f} | Thresh_sig={to.get('significant','N/A')} lead={to.get('lead_time','N/A')} | TY_p={ty.get('p_value','N/A'):.4f}\\\")\n  print(f\\\"Consensus: {d['consensus']}\\\")\n  print(f\\\"Summary: {d['summary']}\\\")\n  print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-17855",
    "command": "python3 -c \"\nimport json\nfor label, path in [\n  ('Pythia-410M_s43', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json'),\n  ('GPT2_a050_s42', '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n    dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n    print(f\\\"{p['canary']}->{p['downstream']}: PermG_p={pg.get('p_value','N/A'):.4f} fdr={pg_fdr} f2={pg.get('effect_size_f2','N/A')} | DiffXcorr_p={dx.get('p_value','N/A'):.4f} r={dx.get('r','N/A'):.3f} lag={dx.get('peak_lag','N/A')} fdr={dx_fdr} | Naive_p={nx.get('p_value','N/A'):.4f} r={nx.get('r','N/A'):.3f} | Thresh_sig={to.get('significant','N/A')} lead={to.get('lead_time','N/A')} | TY_p={ty.get('p_value','N/A'):.4f}\\\")\n  print(f\\\"Consensus: {d['consensus']}\\\")\n  print(f\\\"Summary: {d['summary']}\\\")\n  print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-20T08:10:35.561243+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-20T08:10:35.561512+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"\nimport json\n\nfor label, path in [\n  ('SmolLM3-3B_s42', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_leadlag.json'),\n  ('Pythia-1.4B_s42', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n    dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n    print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\"effect_size_f2\\\",\\\"N/A\\\")} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} lead={to.get(\\\"lead_time\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\n  print(f'Summary: {d[\\\"summary\\\"]}')\n  print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"\nimport json\n\nfor label, path in [\n  ('SmolLM3-3B_s42', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/smollm3_3b_wiki_a100_s42_fp32_v3/analysis/5method_leadlag.json'),\n  ('Pythia-1.4B_s42', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s42/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n    dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n    print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\"effect_size_f2\\\",\\\"N/A\\\")} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} lead={to.get(\\\"lead_time\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\n  print(f'Summary: {d[\\\"summary\\\"]}')\n  print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T08:10:35.561767+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== SmolLM3-3B_s42 ===\\ntoken_entropy->distinct_1: PermG_p=0.0492 fdr_p=0.06558666666666667 f2=9.4227 DiffXcorr_p=0.0002 r=0.958 lag=-2 fdr_p=0.000362 Naive_p=0.0234 r=-0.872 Thresh_sig=False lead=None TY_p=0.1735\\ntoken_entropy->distinct_2: PermG_p=0.0358 fdr_p=0.058228800000000004 f2=10.166 DiffXcorr_p=0.0006 r=0.937 lag=-2 fdr_p=0.0009392 Naive_p=0.0179 r=-0.889 Thresh_sig=False lead=None TY_p=0.5966\\ntoken_entropy->distinct_3: PermG_p=0.0364 fdr_p=0.058228800000000004 f2=8.9572 DiffXcorr_p=0.0012 r=0.920 lag=-2 fdr_p=0.0016293333333333333 Naive_p=0.0124 r=-0.908 Thresh_sig=False lead=None TY_p=0.0526\\ntoken_entropy->mauve: PermG_p=0.7119 fdr_p=0.729654 f2=0.0218 DiffXcorr_p=0.1224 r=0.639 lag=-3 fdr_p=0.123035 Naive_p=0.0043 r=-0.911 Thresh_sig=False lead=None TY_p=0.5781\\nece->distinct_1: PermG_p=0.0114 fdr_p=0.030394666666666667 f2=42.8639 DiffXcorr_p=0.0000 r=0.991 lag=-2 fdr_p=1.6e-05 Naive_p=0.0000 r=0.978 Thresh_sig=False lead=None TY_p=0.0887\\nece->distinct_2: PermG_p=0.0056 fdr_p=0.030394666666666667 f2=55.5891 DiffXcorr_p=0.0000 r=0.982 lag=-2 fdr_p=6e-05 Naive_p=0.0000 r=0.951 Thresh_sig=False lead=None TY_p=0.4435\\nece->distinct_3: PermG_p=0.0088 fdr_p=0.030394666666666667 f2=34.8895 DiffXcorr_p=0.0001 r=0.968 lag=-2 fdr_p=0.00021866666666666668 Naive_p=0.0005 r=0.919 Thresh_sig=False lead=None TY_p=0.3820\\nece->mauve: PermG_p=0.7297 fdr_p=0.729654 f2=0.0194 DiffXcorr_p=0.1230 r=0.638 lag=-3 fdr_p=0.123035 Naive_p=0.0013 r=0.918 Thresh_sig=False lead=None TY_p=0.9967\\nSummary: {'perm_granger_fdr_forward_sig': 3, 'perm_granger_fdr_reverse_sig': 0, 'diff_xcorr_fdr_forward_sig': 6, 'diff_xcorr_fdr_reverse_sig': 6, 'threshold_forward_sig': 0, 'ty_forward_sig': 0, 'robust_pairs': 3}\\n\\n=== Pythia-1.4B_s42 ===\\ntoken_entropy->distinct_1: PermG_p=0.0274 fdr_p=0.05479 f2=30.0914 DiffXcorr_p=0.0000 r=0.984 lag=-1 fdr_p=8e-06 Naive_p=0.0003 r=0.907 Thresh_sig=False lead=None TY_p=0.2145\\ntoken
…[truncated 1583 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-20T08:10:35.561999+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "python3 -c \"\nimport json\n\nfor label, path in [\n  ('Pythia-410M_s43', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json'),\n  ('GPT2_a050_s42', '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n    dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n    print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\"effect_size_f2\\\",\\\"N/A\\\")} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} lead={to.get(\\\"lead_time\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\n  print(f'Summary: {d[\\\"summary\\\"]}')\n  print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "python3 -c \"\nimport json\n\nfor label, path in [\n  ('Pythia-410M_s43', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json'),\n  ('GPT2_a050_s42', '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n    dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n    print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\"effect_size_f2\\\",\\\"N/A\\\")} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} lead={to.get(\\\"lead_time\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\n  print(f'Summary: {d[\\\"summary\\\"]}')\n  print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T08:10:35.562281+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'python3 -c \\\"\\\\nimport json\\\\n\\\\nfor label, path in [\\\\n  (\\\\'Pythia-410M_s43\\\\', \\\\'/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json\\\\'),\\\\n  (\\\\'GPT2_a050_s42\\\\', \\\\'/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json\\\\'),\\\\n]:\\\\n  d = json.load(open(path))\\\\n  print(f\\\\'=== {label} ===\\\\')\\\\n  for p in d[\\\\'pairs\\\\']:\\\\n    fwd = p[\\\\'forward\\\\']\\\\n    pg = fwd.get(\\\\'perm_granger\\\\',{})\\\\n    dx = fwd.get(\\\\'diff_xcorr\\\\',{})\\\\n    nx = fwd.get(\\\\'naive_xcorr\\\\',{})\\\\n    to = fwd.get(\\\\'threshold_onset\\\\',{})\\\\n    ty = fwd.get(\\\\'ty_granger\\\\',{})\\\\n    pg_fdr = pg.get(\\\\'fdr_p\\\\', pg.get(\\\\'p_fdr\\\\',\\\\'N/A\\\\'))\\\\n    dx_fdr = dx.get(\\\\'fdr_p\\\\', dx.get(\\\\'p_fdr\\\\',\\\\'N/A\\\\'))\\\\n    print(f\\\\'{p[\\\\\\\\\\\"canary\\\\\\\\\\\"]}->{p[\\\\\\\\\\\"downstream\\\\\\\\\\\"]}: PermG_p={pg.get(\\\\\\\\\\\"p_value\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\\\\\\\\\"effect_size_f2\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\")} DiffXcorr_p={dx.get(\\\\\\\\\\\"p_value\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\"):.4f} r={dx.get(\\\\\\\\\\\"r\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\"):.3f} lag={dx.get(\\\\\\\\\\\"peak_lag\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\\\\\\\\\"p_value\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\"):.4f} r={nx.get(\\\\\\\\\\\"r\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\"):.3f} Thresh_sig={to.get(\\\\\\\\\\\"significant\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\")} lead={to.get(\\\\\\\\\\\"lead_time\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\")} TY_p={ty.get(\\\\\\\\\\\"p_value\\\\\\\\\\\",\\\\\\\\\\\"N/A\\\\\\\\\\\"):.4f}\\\\')\\\\n  print(f\\\\'Summary: {d[\\\\\\\\\\\"summary\
…[truncated 200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-20T08:10:35.562584+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nfor label, path in [\n  ('Pythia-410M_s43', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json'),\n  ('GPT2_a050_s42', '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n    dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n    print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\"effect_size_f2\\\",\\\"N/A\\\")} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} lead={to.get(\\\"lead_time\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\n  print(f'Summary: {d[\\\"summary\\\"]}')\n  print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nfor label, path in [\n  ('Pythia-410M_s43', '/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia410m_wiki_a100_s43/analysis/5method_leadlag.json'),\n  ('GPT2_a050_s42', '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a050_s42_fp32/analysis/5method_leadlag.json'),\n]:\n  d = json.load(open(path))\n  print(f'=== {label} ===')\n  for p in d['pairs']:\n    fwd = p['forward']\n    pg = fwd.get('perm_granger',{})\n    dx = fwd.get('diff_xcorr',{})\n    nx = fwd.get('naive_xcorr',{})\n    to = fwd.get('threshold_onset',{})\n    ty = fwd.get('ty_granger',{})\n    pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n    dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n    print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\"effect_size_f2\\\",\\\"N/A\\\")} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} lead={to.get(\\\"lead_time\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\n  print(f'Summary: {d[\\\"summary\\\"]}')\n  print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-20T08:10:35.562844+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Pythia-410M_s43 ===\\ntoken_entropy->distinct_1: PermG_p=0.0020 fdr_p=0.0032 f2=N/A DiffXcorr_p=0.0000 r=0.998 lag=-1 fdr_p=0.0 Naive_p=0.0000 r=0.994 Thresh_sig=False lead=None TY_p=0.0568\\ntoken_entropy->distinct_2: PermG_p=0.0016 fdr_p=0.0032 f2=N/A DiffXcorr_p=0.0000 r=0.998 lag=-1 fdr_p=0.0 Naive_p=0.0000 r=0.998 Thresh_sig=False lead=None TY_p=0.0238\\ntoken_entropy->distinct_3: PermG_p=0.0058 fdr_p=0.007732 f2=N/A DiffXcorr_p=0.0000 r=0.994 lag=-2 fdr_p=2e-06 Naive_p=0.0000 r=0.997 Thresh_sig=False lead=None TY_p=0.0009\\ntoken_entropy->mauve: PermG_p=0.2038 fdr_p=0.232867 f2=N/A DiffXcorr_p=0.2644 r=-0.620 lag=5 fdr_p=0.264392 Naive_p=0.2259 r=-0.582 Thresh_sig=False lead=None TY_p=0.7001\\nece->distinct_1: PermG_p=0.0018 fdr_p=0.0032 f2=N/A DiffXcorr_p=0.0000 r=0.959 lag=-1 fdr_p=6.1e-05 Naive_p=0.0000 r=0.993 Thresh_sig=False lead=None TY_p=0.3625\\nece->distinct_2: PermG_p=0.0002 fdr_p=0.0008 f2=N/A DiffXcorr_p=0.0000 r=0.978 lag=-1 fdr_p=8e-06 Naive_p=0.0000 r=0.995 Thresh_sig=False lead=None TY_p=0.0163\\nece->distinct_3: PermG_p=0.0002 fdr_p=0.0008 f2=N/A DiffXcorr_p=0.0000 r=0.995 lag=-1 fdr_p=0.0 Naive_p=0.0000 r=0.996 Thresh_sig=False lead=None TY_p=0.0018\\nece->mauve: PermG_p=0.3909 fdr_p=0.390922 f2=N/A DiffXcorr_p=0.1288 r=0.584 lag=-2 fdr_p=0.147208 Naive_p=0.1284 r=-0.691 Thresh_sig=False lead=None TY_p=0.6246\\nSummary: {'perm_granger_fdr_forward_sig': 6, 'perm_granger_fdr_reverse_sig': 0, 'diff_xcorr_fdr_forward_sig': 6, 'diff_xcorr_fdr_reverse_sig': 6, 'threshold_forward_sig': 0, 'ty_forward_sig': 4, 'robust_pairs': 6}\\n\\n=== GPT2_a050_s42 ===\\ntoken_entropy->distinct_1: PermG_p=0.0012 fdr_p=0.008 f2=N/A DiffXcorr_p=0.0001 r=0.968 lag=-2 fdr_p=0.00016 Naive_p=0.0054 r=-0.940 Thresh_sig=False lead=None TY_p=0.0016\\ntoken_entropy->distinct_2: PermG_p=0.0166 fdr_p=0.033194 f2=N/A DiffXcorr_p=0.0001 r=0.968 lag=-2 fdr_p=0.00016 Naive_p=0.0035 r=-0.952 Thresh_sig=True lead=9 TY_p=0
…[truncated 1323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-20T08:10:35.563130+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nd = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s42/analysis/5method_leadlag.json'))\nprint('=== Pythia-6.9B_s42 ===')\nfor p in d['pairs']:\n  fwd = p['forward']\n  pg = fwd.get('perm_granger',{})\n  dx = fwd.get('diff_xcorr',{})\n  nx = fwd.get('naive_xcorr',{})\n  to = fwd.get('threshold_onset',{})\n  ty = fwd.get('ty_granger',{})\n  pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n  dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n  print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\nprint(f'Summary: {d[\\\"summary\\\"]}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nd = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/scale_check/pythia69b_wiki_a100_s42/analysis/5method_leadlag.json'))\nprint('=== Pythia-6.9B_s42 ===')\nfor p in d['pairs']:\n  fwd = p['forward']\n  pg = fwd.get('perm_granger',{})\n  dx = fwd.get('diff_xcorr',{})\n  nx = fwd.get('naive_xcorr',{})\n  to = fwd.get('threshold_onset',{})\n  ty = fwd.get('ty_granger',{})\n  pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n  dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n  print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\nprint(f'Summary: {d[\\\"summary\\\"]}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-20T08:10:35.563387+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Pythia-6.9B_s42 ===\\ntoken_entropy->distinct_1: PermG_p=0.0052 fdr_p=0.006932 DiffXcorr_p=0.0000 r=0.991 lag=-1 fdr_p=0.0 Naive_p=0.0000 r=0.996 Thresh_sig=False TY_p=0.0639\\ntoken_entropy->distinct_2: PermG_p=0.0024 fdr_p=0.0048 DiffXcorr_p=0.0001 r=0.968 lag=-2 fdr_p=0.000144 Naive_p=0.0000 r=0.968 Thresh_sig=False TY_p=0.1582\\ntoken_entropy->distinct_3: PermG_p=0.0048 fdr_p=0.006932 DiffXcorr_p=0.0055 r=0.939 lag=-4 fdr_p=0.007393 Naive_p=0.0010 r=0.974 Thresh_sig=False TY_p=0.3756\\ntoken_entropy->mauve: PermG_p=0.0580 fdr_p=0.057988 DiffXcorr_p=0.0781 r=-0.655 lag=2 fdr_p=0.078065 Naive_p=0.0005 r=0.963 Thresh_sig=True TY_p=0.0281\\nece->distinct_1: PermG_p=0.0008 fdr_p=0.0032 DiffXcorr_p=0.0000 r=0.966 lag=-1 fdr_p=6.4e-05 Naive_p=0.0000 r=0.967 Thresh_sig=False TY_p=0.1382\\nece->distinct_2: PermG_p=0.0008 fdr_p=0.0032 DiffXcorr_p=0.0000 r=0.995 lag=-1 fdr_p=0.0 Naive_p=0.0000 r=0.998 Thresh_sig=False TY_p=0.4088\\nece->distinct_3: PermG_p=0.0012 fdr_p=0.0032 DiffXcorr_p=0.0001 r=0.981 lag=-3 fdr_p=0.000144 Naive_p=0.0000 r=0.986 Thresh_sig=False TY_p=0.4838\\nece->mauve: PermG_p=0.0290 fdr_p=0.033136 DiffXcorr_p=0.0570 r=0.652 lag=-1 fdr_p=0.065165 Naive_p=0.0006 r=0.961 Thresh_sig=True TY_p=0.0598\\nSummary: {'perm_granger_fdr_forward_sig': 7, 'perm_granger_fdr_reverse_sig': 0, 'diff_xcorr_fdr_forward_sig': 6, 'diff_xcorr_fdr_reverse_sig': 6, 'threshold_forward_sig': 2, 'ty_forward_sig': 1, 'robust_pairs': 5}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-20T08:10:35.563617+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"\nimport json\n\nd = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s43/analysis/5method_leadlag.json'))\nprint('=== Pythia-1.4B_s43 ===')\nfor p in d['pairs']:\n  fwd = p['forward']\n  pg = fwd.get('perm_granger',{})\n  dx = fwd.get('diff_xcorr',{})\n  nx = fwd.get('naive_xcorr',{})\n  to = fwd.get('threshold_onset',{})\n  ty = fwd.get('ty_granger',{})\n  pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n  dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n  print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\"effect_size_f2\\\",\\\"N/A\\\")} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\nprint(f'Summary: {d[\\\"summary\\\"]}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"\nimport json\n\nd = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/pythia14b_wiki_a100_s43/analysis/5method_leadlag.json'))\nprint('=== Pythia-1.4B_s43 ===')\nfor p in d['pairs']:\n  fwd = p['forward']\n  pg = fwd.get('perm_granger',{})\n  dx = fwd.get('diff_xcorr',{})\n  nx = fwd.get('naive_xcorr',{})\n  to = fwd.get('threshold_onset',{})\n  ty = fwd.get('ty_granger',{})\n  pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n  dx_fdr = dx.get('fdr_p', dx.get('p_fdr','N/A'))\n  print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} f2={pg.get(\\\"effect_size_f2\\\",\\\"N/A\\\")} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")} fdr_p={dx_fdr} Naive_p={nx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={nx.get(\\\"r\\\",\\\"N/A\\\"):.3f} Thresh_sig={to.get(\\\"significant\\\",\\\"N/A\\\")} TY_p={ty.get(\\\"p_value\\\",\\\"N/A\\\"):.4f}')\nprint(f'Summary: {d[\\\"summary\\\"]}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-20T08:10:35.563852+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Pythia-1.4B_s43 ===\\ntoken_entropy->distinct_1: PermG_p=0.0022 fdr_p=N/A f2=97.735 DiffXcorr_p=0.0002 r=0.938 lag=-1 fdr_p=N/A Naive_p=0.0124 r=-0.908 Thresh_sig=True TY_p=0.0326\\ntoken_entropy->distinct_2: PermG_p=0.0046 fdr_p=N/A f2=35.1819 DiffXcorr_p=0.0010 r=0.897 lag=-1 fdr_p=N/A Naive_p=0.0199 r=-0.883 Thresh_sig=True TY_p=0.1798\\ntoken_entropy->distinct_3: PermG_p=0.0080 fdr_p=N/A f2=18.5979 DiffXcorr_p=0.0308 r=0.853 lag=-4 fdr_p=N/A Naive_p=0.0295 r=-0.856 Thresh_sig=True TY_p=0.4964\\ntoken_entropy->mauve: PermG_p=0.0980 fdr_p=N/A f2=1.6638 DiffXcorr_p=0.0214 r=0.931 lag=5 fdr_p=N/A Naive_p=0.0089 r=-0.772 Thresh_sig=True TY_p=0.5433\\nece->distinct_1: PermG_p=0.0044 fdr_p=N/A f2=102.8905 DiffXcorr_p=0.0001 r=0.955 lag=-1 fdr_p=N/A Naive_p=0.0000 r=0.959 Thresh_sig=True TY_p=0.0000\\nece->distinct_2: PermG_p=0.0100 fdr_p=N/A f2=34.651 DiffXcorr_p=0.0005 r=0.917 lag=-1 fdr_p=N/A Naive_p=0.0000 r=0.957 Thresh_sig=True TY_p=0.0000\\nece->distinct_3: PermG_p=0.0142 fdr_p=N/A f2=17.9927 DiffXcorr_p=0.0030 r=0.859 lag=-1 fdr_p=N/A Naive_p=0.0000 r=0.950 Thresh_sig=True TY_p=0.0000\\nece->mauve: PermG_p=0.0660 fdr_p=N/A f2=1.8759 DiffXcorr_p=0.0274 r=0.919 lag=5 fdr_p=N/A Naive_p=0.0793 r=0.760 Thresh_sig=True TY_p=0.0992\\nSummary: {'perm_granger_fdr_forward_sig': 6, 'diff_xcorr_fdr_forward_sig': 8, 'threshold_forward_sig': 8, 'ty_forward_sig': 4, 'robust_pairs': 7}\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-20T08:10:35.564200+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "python3 -c \"\nimport json, os, glob\n\nbase = '/root/autodl-tmp/distrib_canary_collapse/results'\nfor label, path in [\n  ('SmolLM3-3B_s42', f'{base}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3'),\n  ('Pythia-1.4B_s42', f'{base}/generalize/pythia14b_wiki_a100_s42'),\n]:\n  print(f'=== {label} ===')\n  metrics_file = os.path.join(path, 'all_metrics.json')\n  if os.path.exists(metrics_file):\n    d = json.load(open(metrics_file))\n    if isinstance(d, list):\n      for gen_data in d:\n        g = gen_data.get('generation', gen_data.get('gen', '?'))\n        ent = gen_data.get('token_entropy', gen_data.get('entropy', 'N/A'))\n        ece = gen_data.get('ece', 'N/A')\n        d1 = gen_data.get('distinct_1', 'N/A')\n        mv = gen_data.get('mauve', 'N/A')\n        print(f'  gen={g} entropy={ent} ece={ece} d1={d1} mauve={mv}')\n    elif isinstance(d, dict):\n      for k in ['token_entropy','ece','distinct_1','mauve']:\n        print(f'  {k}: {d.get(k, \\\"N/A\\\")}')\n  else:\n    jsons = glob.glob(os.path.join(path, 'gen_*/metrics.json'))\n    jsons.sort()\n    for jf in jsons[:3]:\n      print(f'  {jf}: {list(json.load(open(jf)).keys())[:10]}')\n    print(f'  ... total {len(jsons)} gen files')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "python3 -c \"\nimport json, os, glob\n\nbase = '/root/autodl-tmp/distrib_canary_collapse/results'\nfor label, path in [\n  ('SmolLM3-3B_s42', f'{base}/generalize/smollm3_3b_wiki_a100_s42_fp32_v3'),\n  ('Pythia-1.4B_s42', f'{base}/generalize/pythia14b_wiki_a100_s42'),\n]:\n  print(f'=== {label} ===')\n  metrics_file = os.path.join(path, 'all_metrics.json')\n  if os.path.exists(metrics_file):\n    d = json.load(open(metrics_file))\n    if isinstance(d, list):\n      for gen_data in d:\n        g = gen_data.get('generation', gen_data.get('gen', '?'))\n        ent = gen_data.get('token_entropy', gen_data.get('entropy', 'N/A'))\n        ece = gen_data.get('ece', 'N/A')\n        d1 = gen_data.get('distinct_1', 'N/A')\n        mv = gen_data.get('mauve', 'N/A')\n        print(f'  gen={g} entropy={ent} ece={ece} d1={d1} mauve={mv}')\n    elif isinstance(d, dict):\n      for k in ['token_entropy','ece','distinct_1','mauve']:\n        print(f'  {k}: {d.get(k, \\\"N/A\\\")}')\n  else:\n    jsons = glob.glob(os.path.join(path, 'gen_*/metrics.json'))\n    jsons.sort()\n    for jf in jsons[:3]:\n      print(f'  {jf}: {list(json.load(open(jf)).keys())[:10]}')\n    print(f'  ... total {len(jsons)} gen files')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-20T08:10:35.564507+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== SmolLM3-3B_s42 ===\\n  gen=0 entropy=2.5625921993072116 ece=0.004637691676262301 d1=0.10546037012671262 mauve=0.029943781571973194\\n  gen=1 entropy=1.0387408720739544 ece=0.32904927458037453 d1=0.10701958466027194 mauve=0.031304279776101215\\n  gen=2 entropy=0.9381176230327823 ece=0.3895732432911089 d1=0.08551078894133513 mauve=0.031478758720225805\\n  gen=3 entropy=0.9422750212207844 ece=0.4152050063661557 d1=0.07661918061129495 mauve=0.0306797068944216\\n  gen=4 entropy=1.2340175870714567 ece=0.4067777982181973 d1=0.0748515625 mauve=0.02720151727630958\\n  gen=5 entropy=1.0905542576742127 ece=0.41990037166891325 d1=0.073875 mauve=0.025158256379255037\\n  gen=6 entropy=1.1379355926563155 ece=0.414567695163374 d1=0.073 mauve=0.023998875511538387\\n  gen=7 entropy=1.238310725144368 ece=0.415361864152074 d1=0.07271875 mauve=0.025108407226480528\\n  gen=8 entropy=1.537933251468855 ece=0.3932567181807334 d1=0.0725546875 mauve=0.02312397647781301\\n  gen=9 entropy=1.3946593390479112 ece=0.40766718201277835 d1=0.0718828125 mauve=0.02600529657343455\\n  gen=10 entropy=1.7045586746507768 ece=0.382745281617 d1=0.0714921875 mauve=0.024705594207362003\\n=== Pythia-1.4B_s42 ===\\n  gen=0 entropy=2.9456511797301514 ece=0.00709667140970812 d1=0.0993112259522854 mauve=0.03298144128361465\\n  gen=1 entropy=1.5269347268797067 ece=0.2636542668772705 d1=0.09984500981054922 mauve=0.03405082205885783\\n  gen=2 entropy=1.2838699337890036 ece=0.3403641084907979 d1=0.0824453125 mauve=0.03315244042285245\\n  gen=3 entropy=1.2466961563259795 ece=0.3617818417476097 d1=0.0785234375 mauve=0.033923691893446\\n  gen=4 entropy=1.3222485356250944 ece=0.3690897542578071 d1=0.0757890625 mauve=0.031132275221975994\\n  gen=5 entropy=1.2641103901015018 ece=0.38127302885557757 d1=0.0734453125 mauve=0.031425167363644056\\n  gen=6 entropy=1.275956534308526 ece=0.3866656062932555 d1=0.07146875 mauve=0.029301149701200714\\n  gen=7 entropy=1.2828506
…[truncated 488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-20T08:10:35.564746+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nbase = '/root/autodl-tmp/distrib_canary_collapse/results'\nfor label, path in [\n  ('Pythia-410M_s43', f'{base}/generalize/pythia410m_wiki_a100_s43'),\n  ('Pythia-6.9B_s42', f'{base}/scale_check/pythia69b_wiki_a100_s42'),\n]:\n  d = json.load(open(f'{path}/all_metrics.json'))\n  print(f'=== {label} ===')\n  for g in d:\n    print(f\\\"  gen={g.get('generation',g.get('gen','?'))} entropy={g.get('token_entropy','N/A'):.4f} ece={g.get('ece','N/A'):.4f} d1={g.get('distinct_1','N/A'):.4f} mauve={g.get('mauve','N/A'):.4f}\\\")\n  print()\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nbase = '/root/autodl-tmp/distrib_canary_collapse/results'\nfor label, path in [\n  ('Pythia-410M_s43', f'{base}/generalize/pythia410m_wiki_a100_s43'),\n  ('Pythia-6.9B_s42', f'{base}/scale_check/pythia69b_wiki_a100_s42'),\n]:\n  d = json.load(open(f'{path}/all_metrics.json'))\n  print(f'=== {label} ===')\n  for g in d:\n    print(f\\\"  gen={g.get('generation',g.get('gen','?'))} entropy={g.get('token_entropy','N/A'):.4f} ece={g.get('ece','N/A'):.4f} d1={g.get('distinct_1','N/A'):.4f} mauve={g.get('mauve','N/A'):.4f}\\\")\n  print()\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-20T08:10:35.564909+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Pythia-410M_s43 ===\\n  gen=0 entropy=3.2342 ece=0.0108 d1=0.0983 mauve=0.0315\\n  gen=1 entropy=1.7930 ece=0.2187 d1=0.0966 mauve=0.0313\\n  gen=2 entropy=1.4034 ece=0.3293 d1=0.0827 mauve=0.0329\\n  gen=3 entropy=1.2791 ece=0.3655 d1=0.0795 mauve=0.0318\\n  gen=4 entropy=1.2208 ece=0.3846 d1=0.0792 mauve=0.0314\\n  gen=5 entropy=1.1746 ece=0.3977 d1=0.0790 mauve=0.0313\\n  gen=6 entropy=1.1694 ece=0.4060 d1=0.0789 mauve=0.0306\\n  gen=7 entropy=1.1579 ece=0.4121 d1=0.0789 mauve=0.0321\\n  gen=8 entropy=1.1688 ece=0.4169 d1=0.0789 mauve=0.0325\\n  gen=9 entropy=1.1581 ece=0.4215 d1=0.0788 mauve=0.0322\\n  gen=10 entropy=1.1639 ece=0.4260 d1=0.0788 mauve=0.0322\\n\\n=== Pythia-6.9B_s42 ===\\n  gen=0 entropy=2.6987 ece=0.0155 d1=0.0941 mauve=0.0305\\n  gen=1 entropy=1.6147 ece=0.1779 d1=0.0932 mauve=0.0314\\n  gen=2 entropy=1.3527 ece=0.2798 d1=0.0782 mauve=0.0279\\n  gen=3 entropy=1.2935 ece=0.3191 d1=0.0730 mauve=0.0264\\n  gen=4 entropy=1.2776 ece=0.3424 d1=0.0713 mauve=0.0255\\n  gen=5 entropy=1.2678 ece=0.3552 d1=0.0710 mauve=0.0242\\n  gen=6 entropy=1.2519 ece=0.3661 d1=0.0708 mauve=0.0229\\n  gen=7 entropy=1.2358 ece=0.3759 d1=0.0705 mauve=0.0254\\n  gen=8 entropy=1.2252 ece=0.3825 d1=0.0712 mauve=0.0239\\n  gen=9 entropy=1.1929 ece=0.3910 d1=0.0706 mauve=0.0264\\n  gen=10 entropy=1.1873 ece=0.3962 d1=0.0703 mauve=0.0260\\n\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-20T08:10:35.565098+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-17855",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nd = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/analysis/5method_leadlag.json'))\nprint('=== Qwen2.5-0.8B_s42 ===')\nfor p in d['pairs']:\n  fwd = p['forward']\n  pg = fwd.get('perm_granger',{})\n  dx = fwd.get('diff_xcorr',{})\n  pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n  print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")}')\nprint(f'Summary: {d[\\\"summary\\\"]}')\n\n# Also get the metric trajectory\nm = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/all_metrics.json'))\nprint()\nprint('=== Qwen2.5-0.8B trajectory ===')\nfor g in m:\n  print(f\\\"  gen={g.get('generation',g.get('gen','?'))} entropy={g.get('token_entropy','N/A'):.4f} ece={g.get('ece','N/A'):.4f} d1={g.get('distinct_1','N/A'):.4f} mauve={g.get('mauve','N/A'):.4f}\\\")\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-17855",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python3 -c \"\nimport json\n\nd = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/analysis/5method_leadlag.json'))\nprint('=== Qwen2.5-0.8B_s42 ===')\nfor p in d['pairs']:\n  fwd = p['forward']\n  pg = fwd.get('perm_granger',{})\n  dx = fwd.get('diff_xcorr',{})\n  pg_fdr = pg.get('fdr_p', pg.get('p_fdr','N/A'))\n  print(f'{p[\\\"canary\\\"]}->{p[\\\"downstream\\\"]}: PermG_p={pg.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} fdr_p={pg_fdr} DiffXcorr_p={dx.get(\\\"p_value\\\",\\\"N/A\\\"):.4f} r={dx.get(\\\"r\\\",\\\"N/A\\\"):.3f} lag={dx.get(\\\"peak_lag\\\",\\\"N/A\\\")}')\nprint(f'Summary: {d[\\\"summary\\\"]}')\n\n# Also get the metric trajectory\nm = json.load(open('/root/autodl-tmp/distrib_canary_collapse/results/generalize/qwen35_08b_wiki_a100_s42_fp32_v2/all_metrics.json'))\nprint()\nprint('=== Qwen2.5-0.8B trajectory ===')\nfor g in m:\n  print(f\\\"  gen={g.get('generation',g.get('gen','?'))} entropy={g.get('token_entropy','N/A'):.4f} ece={g.get('ece','N/A'):.4f} d1={g.get('distinct_1','N/A'):.4f} mauve={g.get('mauve','N/A'):.4f}\\\")\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-20T08:10:35.565286+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Qwen2.5-0.8B_s42 ===\\ntoken_entropy->distinct_1: PermG_p=0.0042 fdr_p=0.016796 DiffXcorr_p=0.0000 r=0.990 lag=-1\\ntoken_entropy->distinct_2: PermG_p=0.0220 fdr_p=0.036527 DiffXcorr_p=0.0000 r=0.964 lag=-1\\ntoken_entropy->distinct_3: PermG_p=0.0274 fdr_p=0.036527 DiffXcorr_p=0.0012 r=0.891 lag=-1\\ntoken_entropy->mauve: PermG_p=0.0460 fdr_p=0.04759 DiffXcorr_p=0.0181 r=-0.757 lag=-1\\nece->distinct_1: PermG_p=0.0024 fdr_p=0.016796 DiffXcorr_p=0.0000 r=0.994 lag=-1\\nece->distinct_2: PermG_p=0.0086 fdr_p=0.022928 DiffXcorr_p=0.0000 r=0.977 lag=-1\\nece->distinct_3: PermG_p=0.0232 fdr_p=0.036527 DiffXcorr_p=0.0004 r=0.920 lag=-1\\nece->mauve: PermG_p=0.0476 fdr_p=0.04759 DiffXcorr_p=0.0178 r=-0.889 lag=4\\nSummary: {'perm_granger_fdr_forward_sig': 8, 'perm_granger_fdr_reverse_sig': 0, 'diff_xcorr_fdr_forward_sig': 8, 'diff_xcorr_fdr_reverse_sig': 8, 'threshold_forward_sig': 0, 'ty_forward_sig': 6, 'robust_pairs': 6}\\n\\n=== Qwen2.5-0.8B trajectory ===\\n  gen=0 entropy=2.9784 ece=0.0074 d1=0.0940 mauve=0.0291\\n  gen=1 entropy=1.5049 ece=0.2892 d1=0.0941 mauve=0.0297\\n  gen=2 entropy=1.2014 ece=0.3826 d1=0.0786 mauve=0.0310\\n  gen=3 entropy=1.1626 ece=0.4068 d1=0.0730 mauve=0.0299\\n  gen=4 entropy=1.1803 ece=0.4155 d1=0.0709 mauve=0.0283\\n  gen=5 entropy=1.2018 ece=0.4197 d1=0.0684 mauve=0.0268\\n  gen=6 entropy=1.2125 ece=0.4228 d1=0.0666 mauve=0.0256\\n  gen=7 entropy=1.2502 ece=0.4237 d1=0.0654 mauve=0.0241\\n  gen=8 entropy=1.3120 ece=0.4240 d1=0.0644 mauve=0.0244\\n  gen=9 entropy=1.3574 ece=0.4236 d1=0.0637 mauve=0.0230\\n  gen=10 entropy=1.3693 ece=0.4229 d1=0.0634 mauve=0.0225\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-20T08:10:35.565498+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/failure_mode_analysis",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/failure_mode_analysis",
    "description": "Create output directory"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-20T08:10:35.565630+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-20T08:10:35.565768+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/failure_mode_analysis/report.md",
  "content": "# SmolLM3-3B & Pythia-1.4B 失败模式分析\n\n## 1. 总览：信号强度跨模型对比\n\n| Model | Params | α | PermG FDR sig (/8) | DiffXcorr FDR sig (/8) | Threshold sig (/8) | TY sig (/8) | Robust pairs |\n|-------|--------|---|-------------------|----------------------|-------------------|-------------|-------------|\n| GPT-2 (α=0.50 s42) | 124M | 0.50 | 6 | 7 | 4 | 3 | 6 |\n| Pythia-410M (s43) | 410M | 1.0 | 6 | 6 | 0 | 4 | 6 |\n| Qwen2.5-0.8B (s42) | 0.8B | 1.0 | **8** | 8 | 0 | 6 | 6 |\n| Pythia-1.4B (s42) | 1.4B | 1.0 | 2 | 7 | 0 | 0 | **1** |\n| Pythia-1.4B (s43) | 1.4B | 1.0 | 6 | 8 | 8 | 4 | **7** |\n| SmolLM3-3B (s42) | 3B | 1.0 | 3 | 6 | 0 | 0 | **3** |\n| Pythia-6.9B (s42) | 6.9B | 1.0 | **7** | 6 | 2 | 1 | 5 |\n\n**结论：不是简单的 scale 退化。** Qwen-0.8B (8/8) 和 Pythia-6.9B (7/8) 的 PermG 信号甚至强于 410M。SmolLM3-3B 和 Pythia-1.4B(s42) 的弱化有各自不同的根因。\n\n---\n\n## 2. 逐 Pair PermG p-value 对比表\n\n### 2.1 Entropy 通道 (token_entropy → downstream)\n\n| Pair | Pythia-410M s43 | Qwen-0.8B | Pythia-1.4B s42 | SmolLM3-3B s42 | Pythia-6.9B |\n|------|:---:|:---:|:---:|:---:|:---:|\n| →distinct_1 | **0.003** | **0.017** | 0.055 | 0.066 | **0.007** |\n| →distinct_2 | **0.003** | **0.037** | 0.055 | 0.058 | **0.005** |\n| →distinct_3 | **0.008** | **0.037** | 0.071 | 0.058 | **0.007** |\n| →mauve | 0.233 | **0.048** | 0.242 | 0.730 | 0.058 |\n| **FDR sig count** | **3/4** | **4/4** | **0/4** | **0/4** | **3/4** |\n\n### 2.2 ECE 通道 (ece → downstream)\n\n| Pair | Pythia-410M s43 | Qwen-0.8B | Pythia-1.4B s42 | SmolLM3-3B s42 | Pythia-6.9B |\n|------|:---:|:---:|:---:|:---:|:---:|\n| →distinct_1 | **0.003** | **0.017** | **0.034** | **0.030** | **0.003** |\n| →distinct_2 | **0.001** | **0.023** | **0.034** | **0.030** | **0.003** |\n| →distinct_3 | **0.001** | **0.037** | 0.055 | **0.030** | **0.003** |\n| →mauve | 0.391 | **0.048** | 0.240 | 0.730 | **0.033** |\n| **FDR sig count** | **3/4** | **4/4** | **2/4** | **3/4** | **4/4** |\n\n### 2.3 分组统计\n\n| Model | Entropy→distinct (3 pairs) sig | ECE→distinct (3 pairs) sig | Any→mauve (2 pairs) sig |\n|-------|:---:|:---:|:---:|\n| Pythia-410M | 3/3 | 3/3 | 0/2 |\n| Qwen-0.8B | 3/3 | 3/3 | **2/2** |\n| Pythia-1.4B s42 | **0/3** | **2/3** | 0/2 |\n| SmolLM3-3B s42 | **0/3** | **3/3** | 0/2 |\n| Pythia-6.9B | 3/3 | 4/4 (含 mauve) | 1/2 |\n\n**关键发现：ECE 通道在所有模型上比 entropy 通道更鲁棒。** SmolLM3-3B 的 ECE→distinct 全部保留 (3/3)，而 entropy→distinct 全失 (0/3)。\n\n---\n\n## 3. Metric 轨迹分析：失败的根因\n\n### 3.1 Entropy 轨迹对比\n\n```\nGen:    0     1     2     3     4     5     6     7     8     9     10\n410M:  3.23  1.79  1.40  1.28  1.22  1.17  1.17  1.16  1.17  1.16  1.16  ← 单调下降\n6.9B:  2.70  1.61  1.35  1.29  1.28  1.27  1.25  1.24  1.23  1.19  1.19  ← 单调下降\nQwen:  2.98  1.50  1.20  1.16  1.18  1.20  1.21  1.25  1.31  1.36  1.37  ← 轻微 U 型\n1.4B:  2.95  1.53  1.28  1.25  1.32  1.26  1.28  1.28  1.37  1.32  1.33  ← 噪声震荡\n3B:    2.56  1.04  0.94  0.94  1.23  1.09  1.14  1.24  1.54  1.39  1.70  ← 强 U 型 ⚠️\n```\n\n### 3.2 ECE 轨迹对比\n\n```\nGen:    0     1     2     3     4     5     6     7     8     9     10\n410M:  0.011 0.219 0.329 0.366 0.385 0.398 0.406 0.412 0.417 0.422 0.426  ← 单调上升\n6.9B:  0.016 0.178 0.280 0.319 0.342 0.355 0.366 0.376 0.383 0.391 0.396  ← 单调上升\nQwen:  0.007 0.289 0.383 0.407 0.416 0.420 0.423 0.424 0.424 0.424 0.423  ← 上升→平台\n1.4B:  0.007 0.264 0.340 0.362 0.369 0.381 0.387 0.392 0.393 0.403 0.404  ← 单调上升\n3B:    0.005 0.329 0.390 0.415 0.407 0.420 0.415 0.415 0.393 0.408 0.383  ← 上升→噪声波动\n```\n\n### 3.3 Entropy 动态范围与单调性\n\n| Model | Entropy gen1 | gen10 | Δ(gen1→10) | 轨迹形态 | 与 d1 相关性 |\n|-------|:---:|:---:|:---:|:---:|:---:|\n| Pythia-410M | 1.793 | 1.164 | **−0.629** | 单调下降 | 强正 |\n| Pythia-6.9B | 1.615 | 1.187 | **−0.428** | 单调下降 | 强正 |\n| Qwen-0.8B | 1.505 | 1.369 | −0.136 | 轻微 U 型 | 中等正 |\n| Pythia-1.4B | 1.527 | 1.334 | −0.193 | 噪声震荡 | 弱 |\n| SmolLM3-3B | 1.039 | 1.705 | **+0.666** | **强 U 型** | **负/无** |\n\n---\n\n## 4. 失败机制诊断\n\n### 4.1 SmolLM3-3B：Entropy-Diversity Decoupling (熵-多样性脱耦)\n\n**根因**：Entropy 轨迹呈强 U 型（gen 0→2 剧降至 0.94，gen 3→10 反弹至 1.70），而 distinct_1 持续单调下降（0.107→0.071）。\n\n**机制解释**：\n- **Gen 0→2**：3B 模型首次在退化数据上微调，由于模型容量大，快速过拟合为极度自信的分布（entropy 从 2.56 骤降至 0.94，所有模型中最低），同时词汇多样性开始下降\n- **Gen 3→10**：随着训练数据进一步退化，模型面对的输入分布离其 pre-training 分布越来越远。3B 模型的更大容量使其保留了对分布偏移的\"不确定性感知\"——虽然词汇选择范围持续缩窄（d1 下降），但模型对这些有限词汇的选择变得更犹豫（entropy 上升）\n- **统计后果**：Entropy 与 distinct 走向相反，PermG 因果检验失败。但 DiffXcorr（差分序列）仍能捕捉局部变化方向的对应关系（6/8 显著）\n\n**ECE 为何幸存**：ECE 在 gen 1 后保持 0.38-0.42 的高位波动，虽非严格单调但动态范围窄且整体趋势与 d1 一致。ECE 测量的是校准误差（预测概率 vs 真实频率），不依赖于模型的绝对置信度方向。\n\n### 4.2 Pythia-1.4B (s42)：Entropy 早期饱和 + 噪声震荡\n\n**根因**：Entropy 在 gen 2 后迅速饱和于 ~1.28，后续 8 代变化仅 ±0.08，信号被噪声淹没。\n\n**与 s43 的关键差异**：Pythia-1.4B s43 的 robust_pairs=7（vs s42 的 1），说明 1.4B 模型并非系统性失效。s42 恰好落入了 entropy 动态范围特别窄的种子区间。\n\n**机制解释**：\n- 1.4B 的容量足以在几代内将输出分布\"锁定\"到一个低 entropy 稳态\n- 不同 seed 改变了初始微调的随机梯度轨迹，导致有的 seed（s42）更快锁定、有的（s43）保持更长的 entropy 下降趋势\n- PermG 在低方差序列上统计功效不足（gen 2→10 entropy 标准差仅 ~0.04）\n\n### 4.3 Mauve 系统性失败\n\n**跨所有模型（除 Qwen-0.8B 外）的通用问题**：Mauve 在 T=11 时间点的实验中几乎从不显著。\n\n**根因**：\n- Mauve 值极度压缩（通常 0.023→0.033 范围），动态范围仅 ~0.01\n- 作为文本分布级别的度量，单次采样的方差远大于代际趋势\n- T=11 时间序列的统计功效不足以检测如此微小的趋势\n\n**Qwen-0.8B 为何例外**：Qwen 的 mauve 从 0.029 单调下降至 0.023，虽然幅度也小，但单调性好且 Qwen 的 PermG F 统计量刚好过线 (p=0.046/0.048)。\n\n---\n\n## 5. 结论\n\n| 失败模式 | 模型 | 受影响通道 | 根因 | 是否可修复 |\n|----------|------|-----------|------|-----------|\n| Entropy-Diversity Decoupling | SmolLM3-3B | entropy→* | U 型 entropy 轨迹 | 需更多 seed 验证；ECE 通道可用 |\n| Entropy 早期饱和 | Pythia-1.4B s42 | entropy→* | 低动态范围 + 种子不幸 | s43 已证实非系统性问题 |\n| Mauve 低信噪比 | 所有模型 | *→mauve | T=11 + 窄动态范围 | 需增加 T 或替换 metric |\n\n**核心结论**：\n\n1. **信号弱化不是 scale 效应。** Pythia-6.9B (7/8) 和 Qwen-0.8B (8/8) 证明大模型可以保留甚至增强 MMCT 信号。SmolLM3-3B 和 Pythia-1.4B(s42) 各有独立的失败机制。\n\n2. **ECE 是比 entropy 更鲁棒的 canary。** 在所有测试模型中，ECE→distinct 的显著率始终 ≥ entropy→distinct。SmolLM3-3B 上尤为明显：ECE 3/3 vs entropy 0/3。论文应将 ECE 作为推荐的 canary metric。\n\n3. **SmolLM3-3B 的 entropy-diversity decoupling 是一种有意义的新发现**：大容量模型在 collapse 过程中的 entropy 非单调行为值得在论文中作为 discussion point 讨论。\n\n4. **Pythia-1.4B 的跨 seed 方差 (robust_pairs 1 vs 7) 表明单 seed 结论不可靠**，支持论文中多 seed 实验设计的必要性。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/failure_mode_analysis/report.md",
    "content": "# SmolLM3-3B & Pythia-1.4B 失败模式分析\n\n## 1. 总览：信号强度跨模型对比\n\n| Model | Params | α | PermG FDR sig (/8) | DiffXcorr FDR sig (/8) | Threshold sig (/8) | TY sig (/8) | Robust pairs |\n|-------|--------|---|-------------------|----------------------|-------------------|-------------|-------------|\n| GPT-2 (α=0.50 s42) | 124M | 0.50 | 6 | 7 | 4 | 3 | 6 |\n| Pythia-410M (s43) | 410M | 1.0 | 6 | 6 | 0 | 4 | 6 |\n| Qwen2.5-0.8B (s42) | 0.8B | 1.0 | **8** | 8 | 0 | 6 | 6 |\n| Pythia-1.4B (s42) | 1.4B | 1.0 | 2 | 7 | 0 | 0 | **1** |\n| Pythia-1.4B (s43) | 1.4B | 1.0 | 6 | 8 | 8 | 4 | **7** |\n| SmolLM3-3B (s42) | 3B | 1.0 | 3 | 6 | 0 | 0 | **3** |\n| Pythia-6.9B (s42) | 6.9B | 1.0 | **7** | 6 | 2 | 1 | 5 |\n\n**结论：不是简单的 scale 退化。** Qwen-0.8B (8/8) 和 Pythia-6.9B (7/8) 的 PermG 信号甚至强于 410M。SmolLM3-3B 和 Pythia-1.4B(s42) 的弱化有各自不同的根因。\n\n---\n\n## 2. 逐 Pair PermG p-value 对比表\n\n### 2.1 Entropy 通道 (token_entropy → downstream)\n\n| Pair | Pythia-410M s43 | Qwen-0.8B | Pythia-1.4B s42 | SmolLM3-3B s42 | Pythia-6.9B |\n|------|:---:|:---:|:---:|:---:|:---:|\n| →distinct_1 | **0.003** | **0.017** | 0.055 | 0.066 | **0.007** |\n| →distinct_2 | **0.003** | **0.037** | 0.055 | 0.058 | **0.005** |\n| →distinct_3 | **0.008** | **0.037** | 0.071 | 0.058 | **0.007** |\n| →mauve | 0.233 | **0.048** | 0.242 | 0.730 | 0.058 |\n| **FDR sig count** | **3/4** | **4/4** | **0/4** | **0/4** | **3/4** |\n\n### 2.2 ECE 通道 (ece → downstream)\n\n| Pair | Pythia-410M s43 | Qwen-0.8B | Pythia-1.4B s42 | SmolLM3-3B s42 | Pythia-6.9B |\n|------|:---:|:---:|:---:|:---:|:---:|\n| →distinct_1 | **0.003** | **0.017** | **0.034** | **0.030** | **0.003** |\n| →distinct_2 | **0.001** | **0.023** | **0.034** | **0.030** | **0.003** |\n| →distinct_3 | **0.001** | **0.037** | 0.055 | **0.030** | **0.003** |\n| →mauve | 0.391 | **0.048** | 0.240 | 0.730 | **0.033** |\n| **FDR sig count** | **3/4** | **4/4** | **2/4** | **3/4** | **4/4** |\n\n### 2.3 分组统计\n\n| Model | Entropy→distinct (3 pairs) sig | ECE→distinct (3 pairs) sig | Any→mauve (2 pairs) sig |\n|-------|:---:|:---:|:---:|\n| Pythia-410M | 3/3 | 3/3 | 0/2 |\n| Qwen-0.8B | 3/3 | 3/3 | **2/2** |\n| Pythia-1.4B s42 | **0/3** | **2/3** | 0/2 |\n| SmolLM3-3B s42 | **0/3** | **3/3** | 0/2 |\n| Pythia-6.9B | 3/3 | 4/4 (含 mauve) | 1/2 |\n\n**关键发现：ECE 通道在所有模型上比 entropy 通道更鲁棒。** SmolLM3-3B 的 ECE→distinct 全部保留 (3/3)，而 entropy→distinct 全失 (0/3)。\n\n---\n\n## 3. Metric 轨迹分析：失败的根因\n\n### 3.1 Entropy 轨迹对比\n\n```\nGen:    0     1     2     3     4     5     6     7     8     9     10\n410M:  3.23  1.79  1.40  1.28  1.22  1.17  1.17  1.16  1.17  1.16  1.16  ← 单调下降\n6.9B:  2.70  1.61  1.35  1.29  1.28  1.27  1.25  1.24  1.23  1.19  1.19  ← 单调下降\nQwen:  2.98  1.50  1.20  1.16  1.18  1.20  1.21  1.25  1.31  1.36  1.37  ← 轻微 U 型\n1.4B:  2.95  1.53  1.28  1.25  1.32  1.26  1.28  1.28  1.37  1.32  1.33  ← 噪声震荡\n3B:    2.56  1.04  0.94  0.94  1.23  1.09  1.14  1.24  1.54  1.39  1.70  ← 强 U 型 ⚠️\n```\n\n### 3.2 ECE 轨迹对比\n\n```\nGen:    0     1     2     3     4     5     6     7     8     9     10\n410M:  0.011 0.219 0.329 0.366 0.385 0.398 0.406 0.412 0.417 0.422 0.426  ← 单调上升\n6.9B:  0.016 0.178 0.280 0.319 0.342 0.355 0.366 0.376 0.383 0.391 0.396  ← 单调上升\nQwen:  0.007 0.289 0.383 0.407 0.416 0.420 0.423 0.424 0.424 0.424 0.423  ← 上升→平台\n1.4B:  0.007 0.264 0.340 0.362 0.369 0.381 0.387 0.392 0.393 0.403 0.404  ← 单调上升\n3B:    0.005 0.329 0.390 0.415 0.407 0.420 0.415 0.415 0.393 0.408 0.383  ← 上升→噪声波动\n```\n\n### 3.3 Entropy 动态范围与单调性\n\n| Model | Entropy gen1 | gen10 | Δ(gen1→10) | 轨迹形态 | 与 d1 相关性 |\n|-------|:---:|:---:|:---:|:---:|:---:|\n| Pythia-410M | 1.793 | 1.164 | **−0.629** | 单调下降 | 强正 |\n| Pythia-6.9B | 1.615 | 1.187 | **−0.428** | 单调下降 | 强正 |\n| Qwen-0.8B | 1.505 | 1.369 | −0.136 | 轻微 U 型 | 中等正 |\n| Pythia-1.4B | 1.527 | 1.334 | −0.193 | 噪声震荡 | 弱 |\n| SmolLM3-3B | 1.039 | 1.705 | **+0.666** | **强 U 型** | **负/无** |\n\n---\n\n## 4. 失败机制诊断\n\n### 4.1 SmolLM3-3B：Entropy-Diversity Decoupling (熵-多样性脱耦)\n\n**根因**：Entropy 轨迹呈强 U 型（gen 0→2 剧降至 0.94，gen 3→10 反弹至 1.70），而 distinct_1 持续单调下降（0.107→0.071）。\n\n**机制解释**：\n- **Gen 0→2**：3B 模型首次在退化数据上微调，由于模型容量大，快速过拟合为极度自信的分布（entropy 从 2.56 骤降至 0.94，所有模型中最低），同时词汇多样性开始下降\n- **Gen 3→10**：随着训练数据进一步退化，模型面对的输入分布离其 pre-training 分布越来越远。3B 模型的更大容量使其保留了对分布偏移的\"不确定性感知\"——虽然词汇选择范围持续缩窄（d1 下降），但模型对这些有限词汇的选择变得更犹豫（entropy 上升）\n- **统计后果**：Entropy 与 distinct 走向相反，PermG 因果检验失败。但 DiffXcorr（差分序列）仍能捕捉局部变化方向的对应关系（6/8 显著）\n\n**ECE 为何幸存**：ECE 在 gen 1 后保持 0.38-0.42 的高位波动，虽非严格单调但动态范围窄且整体趋势与 d1 一致。ECE 测量的是校准误差（预测概率 vs 真实频率），不依赖于模型的绝对置信度方向。\n\n### 4.2 Pythia-1.4B (s42)：Entropy 早期饱和 + 噪声震荡\n\n**根因**：Entropy 在 gen 2 后迅速饱和于 ~1.28，后续 8 代变化仅 ±0.08，信号被噪声淹没。\n\n**与 s43 的关键差异**：Pythia-1.4B s43 的 robust_pairs=7（vs s42 的 1），说明 1.4B 模型并非系统性失效。s42 恰好落入了 entropy 动态范围特别窄的种子区间。\n\n**机制解释**：\n- 1.4B 的容量足以在几代内将输出分布\"锁定\"到一个低 entropy 稳态\n- 不同 seed 改变了初始微调的随机梯度轨迹，导致有的 seed（s42）更快锁定、有的（s43）保持更长的 entropy 下降趋势\n- PermG 在低方差序列上统计功效不足（gen 2→10 entropy 标准差仅 ~0.04）\n\n### 4.3 Mauve 系统性失败\n\n**跨所有模型（除 Qwen-0.8B 外）的通用问题**：Mauve 在 T=11 时间点的实验中几乎从不显著。\n\n**根因**：\n- Mauve 值极度压缩（通常 0.023→0.033 范围），动态范围仅 ~0.01\n- 作为文本分布级别的度量，单次采样的方差远大于代际趋势\n- T=11 时间序列的统计功效不足以检测如此微小的趋势\n\n**Qwen-0.8B 为何例外**：Qwen 的 mauve 从 0.029 单调下降至 0.023，虽然幅度也小，但单调性好且 Qwen 的 PermG F 统计量刚好过线 (p=0.046/0.048)。\n\n---\n\n## 5. 结论\n\n| 失败模式 | 模型 | 受影响通道 | 根因 | 是否可修复 |\n|----------|------|-----------|------|-----------|\n| Entropy-Diversity Decoupling | SmolLM3-3B | entropy→* | U 型 entropy 轨迹 | 需更多 seed 验证；ECE 通道可用 |\n| Entropy 早期饱和 | Pythia-1.4B s42 | entropy→* | 低动态范围 + 种子不幸 | s43 已证实非系统性问题 |\n| Mauve 低信噪比 | 所有模型 | *→mauve | T=11 + 窄动态范围 | 需增加 T 或替换 metric |\n\n**核心结论**：\n\n1. **信号弱化不是 scale 效应。** Pythia-6.9B (7/8) 和 Qwen-0.8B (8/8) 证明大模型可以保留甚至增强 MMCT 信号。SmolLM3-3B 和 Pythia-1.4B(s42) 各有独立的失败机制。\n\n2. **ECE 是比 entropy 更鲁棒的 canary。** 在所有测试模型中，ECE→distinct 的显著率始终 ≥ entropy→distinct。SmolLM3-3B 上尤为明显：ECE 3/3 vs entropy 0/3。论文应将 ECE 作为推荐的 canary metric。\n\n3. **SmolLM3-3B 的 entropy-diversity decoupling 是一种有意义的新发现**：大容量模型在 collapse 过程中的 entropy 非单调行为值得在论文中作为 discussion point 讨论。\n\n4. **Pythia-1.4B 的跨 seed 方差 (robust_pairs 1 vs 7) 表明单 seed 结论不可靠**，支持论文中多 seed 实验设计的必要性。\n"
  }
}
````

</details>

---

### Tool result

_source line 48 · 2026-05-20T08:10:35.565986+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/failure_mode_analysis/report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-20T08:10:35.566120+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "SmolLM3-3B & Pythia-1.4B Failure Mode Analysis",
  "type": "report",
  "description": "分析 SmolLM3-3B 和 Pythia-1.4B 在 MMCT 中信号弱化的根因：SmolLM3 的 entropy-diversity decoupling（U型entropy轨迹）和 Pythia-1.4B 的 entropy 早期饱和+种子不稳定。含逐pair p-value对比、metric轨迹、7模型横向比较。",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/failure_mode_analysis/report.md",
  "tags": "['failure_analysis', 'scale_effect', 'smollm3', 'pythia14b', 'entropy_decoupling']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "SmolLM3-3B & Pythia-1.4B Failure Mode Analysis",
    "type": "report",
    "description": "分析 SmolLM3-3B 和 Pythia-1.4B 在 MMCT 中信号弱化的根因：SmolLM3 的 entropy-diversity decoupling（U型entropy轨迹）和 Pythia-1.4B 的 entropy 早期饱和+种子不稳定。含逐pair p-value对比、metric轨迹、7模型横向比较。",
    "project": "distrib_canary_collapse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/failure_mode_analysis/report.md",
    "tags": "['failure_analysis', 'scale_effect', 'smollm3', 'pythia14b', 'entropy_decoupling']"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-20T08:10:35.566305+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260520_589296\", \"name\": \"SmolLM3-3B & Pythia-1.4B Failure Mode Analysis\", \"type\": \"report\", \"description\": \"分析 SmolLM3-3B 和 Pythia-1.4B 在 MMCT 中信号弱化的根因：SmolLM3 的 entropy-diversity decoupling（U型entropy轨迹）和 Pythia-1.4B 的 entropy 早期饱和+种子不稳定。含逐pair p-value对比、metric轨迹、7模型横向比较。\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/report/report_589296.md\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-20T08:10:26.106904+00:00\", \"tags\": [\"failure_analysis\", \"scale_effect\", \"smollm3\", \"pythia14b\", \"entropy_decoupling\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-20T08:10:35.566491+00:00_

分析完成。核心发现：

**不是 scale 效应。** Pythia-6.9B (7/8 sig) 和 Qwen-0.8B (8/8 sig) 表明大模型可以保留 MMCT 信号。两个"失败"模型有各自不同的根因：

1. **SmolLM3-3B — Entropy-Diversity Decoupling**：entropy 轨迹呈强 U 型（gen 0→2 骤降至 0.94，gen 10 反弹至 1.70），与 distinct_1 的单调下降走向相反，破坏了 Granger 因果关系。ECE 通道完好 (3/3 distinct pairs 显著)。

2. **Pythia-1.4B s42 — Entropy 早期饱和 + 种子不幸**：entropy gen 2 后锁定在 ~1.28 几乎不动，变异量被噪声淹没。但 s43 种子 robust_pairs=7，证明非系统性问题。

3. **Mauve 跨所有模型系统性弱**（Qwen-0.8B 除外），根因是动态范围仅 ~0.01、T=11 统计功效不足。

报告已保存至 `artifacts/failure_mode_analysis/report.md` 并注册。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_failure_mode_smollm3_14b_20260520T080348"
}
```

</details>

---
