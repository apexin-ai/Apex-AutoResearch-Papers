# analysis a025 s42 fp32 5method padding

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/chats/worker_analysis_a025_s42_fp32_5method_padding_20260519T121959.jsonl`
- **Structured JSON:** [`7a7be48d2944580591cd.json`](../../sessions/7a/7a7be48d2944580591cd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

65 recorded events

### Tool call

_source line 1 · 2026-05-19T12:22:38.469066+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T12:22:38.469353+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T12:22:38.469534+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/lead_lag_analysis.py /root/autodl-tmp/distrib_canary_collapse/analysis.py /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py 2>&1",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls -la /root/autodl-tmp/distrib_canary_collapse/lead_lag_analysis.py /root/autodl-tmp/distrib_canary_collapse/analysis.py /root/autodl-tmp/distrib_canary_collapse/permutation_granger.py 2>&1",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T12:22:38.469676+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T12:22:38.469800+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42_fp32/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42_fp32/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-19T12:22:38.469922+00:00_

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
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
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

_source line 7 · 2026-05-19T12:22:38.470043+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42_fp32/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T12:22:38.470195+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/metrics.py\\n/root/autodl-tmp/distrib_canary_collapse/iterative_train.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_data.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_mvp.py\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation.py\\n/root/autodl-tmp/distrib_canary_collapse/dmax_sensitivity.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py\\n/root/autodl-tmp/distrib_canary_collapse/bootstrap_ty_validation.py\\n/root/autodl-tmp/distrib_canary_collapse/detrending_utils.py\\n/root/autodl-tmp/distrib_canary_collapse/permutation_granger.py\\n/root/autodl-tmp/distrib_canary_collapse/run_lag_sensitivity.py\\n/root/autodl-tmp/distrib_canary_collapse/analyze_extended.py\\n/root/autodl-tmp/distrib_canary_collapse/pooled_panel_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/extract_drift.py\\n/root/autodl-tmp/distrib_canary_collapse/gen_dose_response.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_v3_analysis.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4.py\\n/root/autodl-tmp/distrib_canary_collapse/consensus_framework.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v2.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v3.py\\n/root/autodl-tmp/distrib_canary_collapse/prepare_c4_v4.py\\n/root/autodl-tmp/distrib_canary_collapse/method_ablation_phase2.py\\n/root/autodl-tmp/distrib_canary_collapse/cross_alpha_analysis_v4.py\\n/root/autodl-tmp/distrib_canary_collapse/resume_plan006_s42.py\\n/root/autodl-tmp/distrib_canary_collapse/leadlag_gpt2m_s42.py\\n/root/autodl-tmp/distrib_canary_collapse/window_sensitivity.py\\n/root/autodl-tmp/distrib_canary_collapse/debug_ty.py\\n/root/autodl-tmp/distrib_canary_collapse/window_sensitivity_v2.py\\n/root/autodl-tmp/distrib_canary_collapse/window_sensitivity_v3.py\\n/root/autodl-tmp/distrib_canary_coll
…[truncated 2641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T12:22:38.470391+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -maxdepth 2 -type d -name \"a025*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -maxdepth 2 -type d -name \"a025*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T12:22:38.470522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T12:22:38.470640+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -80 /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T12:22:38.470795+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"5-method lead-lag analysis: generalized CLI version.\\n\\nUsage:\\n    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43\\n    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43 --dry-run\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport glob as glob_module\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\nfrom permutation_granger import permutation_granger_test\\n\\nN_PERM = 5000\\nALPHA = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\n\\ndef load_series(data_dir):\\n    \\\"\\\"\\\"Load metrics - from all_metrics.json if available, else aggregate gen_X/metrics.json.\\\"\\\"\\\"\\n    all_path = os.path.join(data_dir, \\\"all_metrics.json\\\")\\n    if os.path.exists(all_path):\\n        with open(all_path) as f:\\n            data = json.load(f)\\n    else:\\n        # Aggregate from per-generation metrics\\n        gen_dirs = sorted(glob_module.glob(os.path.join(data_dir, \\\"gen_*\\\")),\\n                         key=lambda x: int(os.path.basename(x).split(\\\"_\\\")[1]))\\n        data = []\\n        for gd in gen_dirs:\\n            mp = os.path.join(gd, \\\"metrics.json\\\")\\n            if os.path.exists(mp):\\n                with open(mp) as f:\\n                    data.append(json.load(f))\\n        if not data:\\n            raise FileNotFoundError(f\\\"No metrics found in {data_dir}\\\")\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in CANARIES +
…[truncated 1127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T12:22:38.470943+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -maxdepth 1 -type d",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -maxdepth 1 -type d",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T12:22:38.471075+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis\\n/root/autodl-tmp/distrib_canary_collapse/results/detrending\\n/root/autodl-tmp/distrib_canary_collapse/results/analysis\\n/root/autodl-tmp/distrib_canary_collapse/results/rebuttal\\n/root/autodl-tmp/distrib_canary_collapse/results/generalize\\n/root/autodl-tmp/distrib_canary_collapse/results/intervention\\n/root/autodl-tmp/distrib_canary_collapse/results/scale_check\\n/root/autodl-tmp/distrib_canary_collapse/results/gen_wiki_gpt2m_a100_s43\\n/root/autodl-tmp/distrib_canary_collapse/results/lag_sensitivity\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T12:22:38.471217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T12:22:38.471367+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42\\na000_s43\\na000_s44\\na010_s42\\na010_s42_fp32\\na010_s43_fp32\\na025_3seed_unified_summary.txt\\na025_s43\\na025_s44\\na050_s42\\na050_s43\\na050_s44\\na060_s42_bf16\\na075_s42\\na075_s43\\na075_s44\\nalpha_monotonicity.png\\nanalysis\\nanalysis_s44\\nanalysis_summary.json\\npooled_panel_results.json\\npooled_panel_summary.txt\\nty_3seed_a025_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T12:22:38.471486+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -name \"*a025*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -name \"*a025*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T12:22:38.471602+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T12:22:38.471721+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/runs/distrib_canary_collapse -name \"*a025*s42*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/runs/distrib_canary_collapse -name \"*a025*s42*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-19T12:22:38.471840+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/distrib_canary_collapse/alpha_sweep_a025_s42.log\\n/root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v2.log\\n/root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log\\n/root/runs/distrib_canary_collapse/gen_wiki_gpt2m_a025_s42.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-19T12:22:38.471999+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -name \"*a025_s42*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results -type d -name \"*a025_s42*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T12:22:38.472121+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T12:22:38.472234+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -30 /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -30 /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T12:22:38.472440+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\r 64%|██████▍   | 3200/5000 [03:21<01:52, 15.95it/s]\\r 64%|██████▍   | 3202/5000 [03:21<01:52, 15.95it/s]\\r 64%|██████▍   | 3204/5000 [03:21<01:52, 15.95it/s]\\r 64%|██████▍   | 3206/5000 [03:21<01:52, 15.94it/s]\\r 64%|██████▍   | 3208/5000 [03:21<01:52, 15.94it/s]\\r 64%|██████▍   | 3210/5000 [03:21<01:52, 15.95it/s]\\r 64%|██████▍   | 3212/5000 [03:21<01:52, 15.95it/s]\\r 64%|██████▍   | 3214/5000 [03:22<01:52, 15.94it/s]\\r 64%|██████▍   | 3216/5000 [03:22<01:51, 15.95it/s]\\r 64%|██████▍   | 3218/5000 [03:22<01:51, 15.94it/s]\\r 64%|██████▍   | 3220/5000 [03:22<01:51, 15.94it/s]\\r 64%|██████▍   | 3222/5000 [03:22<01:51, 15.94it/s]\\r 64%|██████▍   | 3224/5000 [03:22<01:51, 15.95it/s]\\r 65%|██████▍   | 3226/5000 [03:22<01:51, 15.95it/s]\\r 65%|██████▍   | 3228/5000 [03:22<01:51, 15.95it/s]\\r 65%|█���████▍   | 3230/5000 [03:23<01:51, 15.94it/s]\\r 65%|██████▍   | 3232/5000 [03:23<01:50, 15.93it/s]\\r 65%|██████▍   | 3234/5000 [03:23<01:50, 15.94it/s]\\r 65%|██████▍   | 3236/5000 [03:23<01:50, 15.95it/s]\\r 65%|██████▍   | 3238/5000 [03:23<01:50, 15.95it/s]\\r 65%|██████▍   | 3240/5000 [03:23<01:50, 15.94it/s]\\r 65%|██████▍   | 3242/5000 [03:23<01:50, 15.94it/s]\\r 65%|██████▍   | 3244/5000 [03:23<01:50, 15.95it/s]\\r 65%|██████▍   | 3246/5000 [03:24<01:49, 15.95it/s]\\r 65%|██████▍   | 3248/5000 [03:24<01:49, 15.95it/s]\\r 65%|██████▌   | 3250/5000 [03:24<01:49, 15.95it/s]\\r 65%|██████▌   | 3252/5000 [03:24<01:49, 15.95it/s]\\r 65%|██████▌   | 3254/5000 [03:24<01:49, 15.94it/s]\\r 65%|██████▌   | 3256/5000 [03:24<01:49, 15.95it/s]\\r 65%|██████▌   | 3258/5000 [03:24<01:49, 15.95it/s]\\r 65%|████��█▌   | 3260/5000 [03:24<01:49, 15.95it/s]\\r 65%|██████▌   | 3262/5000 [03:25<01:48, 15.95it/s]\\r 65%|██████▌   | 3264/5000 [03:25<01:48, 15.95it/s]\\r 65%|██████▌   | 3266/5000 [03:25<01:48, 15.94it/s]\\r 65%|██████▌   | 3268/5000 [03:25<01:48, 15.95it/s]\\r 65%|██████▌   | 3270/5000 [03:25<01:48, 15.93it
…[truncated 6480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T12:22:38.472596+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -l \"a025_s42\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis/*.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -l \"a025_s42\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis/*.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T12:22:38.472724+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep_analysis/phase_diagram.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T12:22:38.472872+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T12:22:38.472993+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -120 /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -120 /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T12:22:38.473113+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s42/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T12:22:38.473297+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"5-method lead-lag analysis: generalized CLI version.\\n\\nUsage:\\n    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43\\n    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43 --dry-run\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport glob as glob_module\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\nfrom permutation_granger import permutation_granger_test\\n\\nN_PERM = 5000\\nALPHA = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"perplexity\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\n\\ndef load_series(data_dir):\\n    \\\"\\\"\\\"Load metrics - from all_metrics.json if available, else aggregate gen_X/metrics.json.\\\"\\\"\\\"\\n    all_path = os.path.join(data_dir, \\\"all_metrics.json\\\")\\n    if os.path.exists(all_path):\\n        with open(all_path) as f:\\n            data = json.load(f)\\n    else:\\n        # Aggregate from per-generation metrics\\n        gen_dirs = sorted(glob_module.glob(os.path.join(data_dir, \\\"gen_*\\\")),\\n                         key=lambda x: int(os.path.basename(x).split(\\\"_\\\")[1]))\\n        data = []\\n        for gd in gen_dirs:\\n            mp = os.path.join(gd, \\\"metrics.json\\\")\\n            if os.path.exists(mp):\\n                with open(mp) as f:\\n                    data.append(json.load(f))\\n        if not data:\\n            raise FileNotFoundError(f\\\"No metrics found in {data_dir}\\\")\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in CANARIES +
…[truncated 2595 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-19T12:22:38.473481+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root -type f -name \"all_metrics.json\" -path \"*a025_s42*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root -type f -name \"all_metrics.json\" -path \"*a025_s42*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-19T12:22:38.473609+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.64}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-19T12:22:38.473736+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root -type d -name \"a025_s42*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root -type d -name \"a025_s42*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-19T12:22:38.473898+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-19T12:22:38.474021+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep \"results_dir\\|output_dir\\|results/\" /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep \"results_dir\\|output_dir\\|results/\" /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-19T12:22:38.474146+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-19T12:22:38.474330+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-19T12:22:38.474477+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE\\nall_metrics.json\\nanalysis\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-19T12:22:38.474598+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep \"results_dir\" /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep \"results_dir\" /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-19T12:22:38.474717+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-19T12:22:38.474831+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -20 /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -20 /root/runs/distrib_canary_collapse/alpha_sweep_a025_s42_v3.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-19T12:22:38.474966+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading model: EleutherAI/pythia-410m\\nLoading data from data/wikitext103_5k\\n============================================================\\nGeneration 0 (baseline)\\n============================================================\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.\\nA decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left
…[truncated 1017 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-19T12:22:38.475151+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-19T12:22:38.475297+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5method_leadlag.json\\n5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-19T12:22:38.475422+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-19T12:22:38.475577+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"EXIT_CODE\\nall_metrics.json\\nanalysis\\nconfig.json\\ngen_0\\ngen_1\\ngen_10\\ngen_2\\ngen_3\\ngen_4\\ngen_5\\ngen_6\\ngen_7\\ngen_8\\ngen_9\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-19T12:22:38.475734+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os\nbasedir = 'results/alpha_sweep'\nexps = ['a025_s43', 'a025_s44', 'a075_s42', 'a075_s43', 'a075_s44',\n        'a050_s42', 'a050_s43', 'a050_s44',\n        'a010_s42', 'a010_s42_fp32', 'a010_s43_fp32',\n        'a060_s42_bf16', 'a000_s42', 'a000_s43', 'a000_s44']\nfor exp in exps:\n    path = f'{basedir}/{exp}/all_metrics.json'\n    if os.path.exists(path):\n        with open(path) as f:\n            d = json.load(f)\n        g0 = d[0] if isinstance(d, list) else d.get('gen_0', d.get('0', None))\n        if isinstance(d, list):\n            g0 = [x for x in d if x.get('generation') == 0]\n            g0 = g0[0] if g0 else None\n        if g0:\n            d1 = g0.get('distinct_1', 'N/A')\n            te = g0.get('token_entropy', 'N/A')\n            print(f'{exp}: gen_0 d1={d1}, entropy={te}')\n        else:\n            print(f'{exp}: gen_0 not found in data')\n    else:\n        print(f'{exp}: all_metrics.json NOT FOUND')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json, os\nbasedir = 'results/alpha_sweep'\nexps = ['a025_s43', 'a025_s44', 'a075_s42', 'a075_s43', 'a075_s44',\n        'a050_s42', 'a050_s43', 'a050_s44',\n        'a010_s42', 'a010_s42_fp32', 'a010_s43_fp32',\n        'a060_s42_bf16', 'a000_s42', 'a000_s43', 'a000_s44']\nfor exp in exps:\n    path = f'{basedir}/{exp}/all_metrics.json'\n    if os.path.exists(path):\n        with open(path) as f:\n            d = json.load(f)\n        g0 = d[0] if isinstance(d, list) else d.get('gen_0', d.get('0', None))\n        if isinstance(d, list):\n            g0 = [x for x in d if x.get('generation') == 0]\n            g0 = g0[0] if g0 else None\n        if g0:\n            d1 = g0.get('distinct_1', 'N/A')\n            te = g0.get('token_entropy', 'N/A')\n            print(f'{exp}: gen_0 d1={d1}, entropy={te}')\n        else:\n            print(f'{exp}: gen_0 not found in data')\n    else:\n        print(f'{exp}: all_metrics.json NOT FOUND')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-19T12:22:38.475890+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a025_s43: gen_0 d1=0.09833431219002871, entropy=3.2341948700181407\\na025_s44: gen_0 d1=0.09808801064406446, entropy=3.2341948700181407\\na075_s42: gen_0 d1=0.0982156685333268, entropy=3.2341948700181407\\na075_s43: gen_0 d1=0.09833431219002871, entropy=3.2341948700181407\\na075_s44: gen_0 d1=0.09808801064406446, entropy=3.2341948700181407\\na050_s42: gen_0 d1=0.0982156685333268, entropy=3.2341948700181407\\na050_s43: gen_0 d1=0.09833431219002871, entropy=3.2341948700181407\\na050_s44: gen_0 d1=0.09808801064406446, entropy=3.2341948700181407\\na010_s42: gen_0 d1=0.0982156685333268, entropy=3.2341948700181407\\na010_s42_fp32: gen_0 d1=0.09162095491577137, entropy=3.23419483150593\\na010_s43_fp32: gen_0 d1=0.09290117352320675, entropy=3.23419483150593\\na060_s42_bf16: gen_0 d1=0.09144189307053367, entropy=3.2574140627143287\\na000_s42: gen_0 d1=0.0982156685333268, entropy=3.2341948700181407\\na000_s43: gen_0 d1=0.09833431219002871, entropy=3.2341948700181407\\na000_s44: gen_0 d1=0.09808801064406446, entropy=3.2341948700181407\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-19T12:22:38.476026+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "echo \"=== Padding Side Check ===\" && for exp in a025_s42 a025_s42_v2 a025_s42_v3 a025_s43 a025_s44 a075_s42 a075_s43 a075_s44 a050_s42 a050_s43 a050_s44 a010_s42 a010_s42_fp32 a010_s43_fp32 a060_s42_bf16 a000_s42 a000_s43 a000_s44; do logfile=\"/root/runs/distrib_canary_collapse/alpha_sweep_${exp}.log\"; if [ -f \"$logfile\" ]; then rp_count=$(grep -c \"right-padding\" \"$logfile\" 2>/dev/null || echo 0); echo \"$exp: right-padding warnings = $rp_count\"; else echo \"$exp: log NOT FOUND\"; fi; done",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "echo \"=== Padding Side Check ===\" && for exp in a025_s42 a025_s42_v2 a025_s42_v3 a025_s43 a025_s44 a075_s42 a075_s43 a075_s44 a050_s42 a050_s43 a050_s44 a010_s42 a010_s42_fp32 a010_s43_fp32 a060_s42_bf16 a000_s42 a000_s43 a000_s44; do logfile=\"/root/runs/distrib_canary_collapse/alpha_sweep_${exp}.log\"; if [ -f \"$logfile\" ]; then rp_count=$(grep -c \"right-padding\" \"$logfile\" 2>/dev/null || echo 0); echo \"$exp: right-padding warnings = $rp_count\"; else echo \"$exp: log NOT FOUND\"; fi; done",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-19T12:22:38.476158+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Padding Side Check ===\\na025_s42: right-padding warnings = 1375\\na025_s42_v2: right-padding warnings = 986\\na025_s42_v3: right-padding warnings = 3443\\na025_s43: right-padding warnings = 3443\\na025_s44: right-padding warnings = 3443\\na075_s42: right-padding warnings = 3443\\na075_s43: right-padding warnings = 2504\\na075_s44: right-padding warnings = 1252\\na050_s42: right-padding warnings = 3443\\na050_s43: right-padding warnings = 3443\\na050_s44: right-padding warnings = 3443\\na010_s42: log NOT FOUND\\na010_s42_fp32: log NOT FOUND\\na010_s43_fp32: log NOT FOUND\\na060_s42_bf16: log NOT FOUND\\na000_s42: right-padding warnings = 3443\\na000_s43: right-padding warnings = 3443\\na000_s44: right-padding warnings = 3443\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-19T12:22:38.476329+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/analysis/5method_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s43/analysis/5method_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-19T12:22:38.476491+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5-Method Lead-Lag Analysis Summary\\nAlpha=0.25, Seed=43, Generations=11\\n============================================================\\n\\nRobust pairs (>=3/5 methods agree): 0/8\\n\\nPer-method forward significance:\\n  Perm Granger (FDR): 0/8\\n  Diff XCorr (FDR):   3/8\\n  Threshold Onset:    0/8\\n  TY Granger:         0/8\\n\\nConsensus detail:\\n  token_entropy→distinct_1  2/5  [naive, diff]\\n  token_entropy→distinct_2  1/5  [naive]\\n  token_entropy→distinct_3  1/5  [naive]\\n  token_entropy→perplexity  1/5  [diff]\\n  ece→distinct_1            2/5  [naive, diff]\\n  ece→distinct_2            1/5  [naive]\\n  ece→distinct_3            1/5  [naive]\\n  ece→perplexity            0/5  [none]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-19T12:22:38.476627+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/runs/distrib_canary_collapse -name \"*a010*\" -o -name \"*a060*\" -o -name \"*padding*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/runs/distrib_canary_collapse -name \"*a010*\" -o -name \"*a060*\" -o -name \"*padding*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-19T12:22:38.476752+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/distrib_canary_collapse/alpha_sweep_a010_s42_v2.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-19T12:22:38.476872+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n# Check padding_robustness\nimport os\nfor d in ['results/intervention', 'results/generalize', 'results/scale_check']:\n    if os.path.exists(d):\n        for sub in os.listdir(d):\n            path = os.path.join(d, sub, 'all_metrics.json')\n            if os.path.exists(path):\n                with open(path) as f:\n                    data = json.load(f)\n                g0 = [x for x in data if x.get('generation') == 0][0] if isinstance(data, list) else None\n                if g0:\n                    print(f'{d}/{sub}: gen_0 d1={g0.get(\\\"distinct_1\\\",\\\"N/A\\\")}')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n# Check padding_robustness\nimport os\nfor d in ['results/intervention', 'results/generalize', 'results/scale_check']:\n    if os.path.exists(d):\n        for sub in os.listdir(d):\n            path = os.path.join(d, sub, 'all_metrics.json')\n            if os.path.exists(path):\n                with open(path) as f:\n                    data = json.load(f)\n                g0 = [x for x in data if x.get('generation') == 0][0] if isinstance(data, list) else None\n                if g0:\n                    print(f'{d}/{sub}: gen_0 d1={g0.get(\\\"distinct_1\\\",\\\"N/A\\\")}')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-19T12:22:38.477002+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"results/intervention/reactive_d1_s42: gen_0 d1=0.0982156685333268\\nresults/intervention/predictive_te_s42: gen_0 d1=0.0982156685333268\\nresults/generalize/pythia410m_wiki_a100_s42: gen_0 d1=0.0982156685333268\\nresults/generalize/opt1b_wiki_a100_s42: gen_0 d1=0.10402947839808178\\nresults/generalize/pythia1b_c4_a100_s42: gen_0 d1=0.11433895431310172\\nresults/generalize/pythia14b_wiki_a100_s42: gen_0 d1=0.0993112259522854\\nresults/generalize/pythia1b_c4_a100_s43: gen_0 d1=0.1161791496236208\\nresults/generalize/gpt2m_wiki_a100_s42: gen_0 d1=0.10438217196075171\\nresults/generalize/pythia14b_wiki_a100_s43: gen_0 d1=0.09991346656217345\\nresults/scale_check/pythia14b_a050_s42: gen_0 d1=0.0993112259522854\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-19T12:22:38.477150+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-19T12:22:38.477291+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5method_leadlag.json\\n5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-19T12:22:38.477414+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -5 /root/runs/distrib_canary_collapse/alpha_sweep_a010_s42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -5 /root/runs/distrib_canary_collapse/alpha_sweep_a010_s42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-19T12:22:38.477530+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -c \"right-padding\" /root/runs/distrib_canary_collapse/alpha_sweep_a010_s42_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -c \"right-padding\" /root/runs/distrib_canary_collapse/alpha_sweep_a010_s42_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-19T12:22:38.477647+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading model: EleutherAI/pythia-410m\\nLoading data from data/wikitext103_5k\\n============================================================\\nGeneration 0 (baseline)\\n============================================================\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-19T12:22:38.477762+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"3443\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-19T12:22:38.477872+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/analysis/5method_summary.txt",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a025_s44/analysis/5method_summary.txt",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-19T12:22:38.478003+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5-Method Lead-Lag Analysis Summary\\nAlpha=0.25, Seed=44, Generations=11\\n============================================================\\n\\nRobust pairs (>=3/5 methods agree): 0/8\\n\\nPer-method forward significance:\\n  Perm Granger (FDR): 0/8\\n  Diff XCorr (FDR):   1/8\\n  Threshold Onset:    0/8\\n  TY Granger:         2/8\\n\\nConsensus detail:\\n  token_entropy→distinct_1  1/5  [naive]\\n  token_entropy→distinct_2  1/5  [naive]\\n  token_entropy→distinct_3  1/5  [naive]\\n  token_entropy→perplexity  1/5  [diff]\\n  ece→distinct_1            1/5  [naive]\\n  ece→distinct_2            2/5  [naive, ty]\\n  ece→distinct_3            0/5  [none]\\n  ece→perplexity            1/5  [ty]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-19T12:22:38.478195+00:00_

All data collected. Here's the full report:

---

## Part 1: 5-method 分析 (a025_s42)

**无法执行** — `results/alpha_sweep/a025_s42/` 目录已从磁盘删除。`alpha_sweep_a025_s42_v3.log` 确认实验完成（11 gens, EXIT_CODE=0），但结果文件不存在。需要重跑实验才能分析。

参考现有 a025 分析：

| Method | a025_s43 fwd | a025_s44 fwd |
|--------|-------------|-------------|
| PermG (FDR) | 0/8 | 0/8 |
| Diff XCorr (FDR) | 3/8 | 1/8 |
| Threshold Onset | 0/8 | 0/8 |
| TY Granger | 0/8 | 2/8 |
| K≥3 consensus | 0/8 | 0/8 |

两个 seed 都是 PermG=0/8，符合预期（α=0.25 过渡点在 [0.25, 0.50] 区间）。

---

## Part 2: Padding Side 状态

gen_0 d1 清晰分成两组，与 right-padding 警告完全对应：

| exp_id | right-padding warnings | gen_0 d1 | padding version |
|--------|----------------------|----------|----------------|
| a000_s42/s43/s44 | 3443 | 0.0982/0.0983/0.0981 | **right (pre-D093)** |
| a010_s42 (v2 log) | 3443 | 0.0982 | **right (pre-D093)** |
| a010_s42_fp32 | log NOT FOUND | 0.0916 | **left (post-D093)** |
| a010_s43_fp32 | log NOT FOUND | 0.0929 | **left (post-D093)** |
| a025_s42 (v3 log) | 3443 | results deleted | **right (pre-D093)** |
| a025_s43 | 3443 | 0.0983 | **right (pre-D093)** |
| a025_s44 | 3443 | 0.0981 | **right (pre-D093)** |
| a050_s42/s43/s44 | 3443 | 0.0982/0.0983/0.0981 | **right (pre-D093)** |
| a060_s42_bf16 | log NOT FOUND | 0.0914 | **left (post-D093)** |
| a075_s42/s43/s44 | 3443 | 0.0982/0.0983/0.0981 | **right (pre-D093)** |

**规律**: `_fp32`/`_bf16` 后缀实验 = post-D093 left-padding (d1 ≈ 0.091-0.093)。无后缀实验 = pre-D093 right-padding (d1 ≈ 0.098)。差异 ~7% 稳定复现。

**关键发现**: 当前所有 a025 实验（s42/s43/s44）都是 right-padding 版本。如果要与 post-D093 fp32 实验对比，a025 需要用 left-padding 重跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_a025_s42_fp32_5method_padding_20260519T121959"
}
```

</details>

---
