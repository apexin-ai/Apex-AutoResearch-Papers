# analysis null s42 s44 d102

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 79
- **Recorded user turns:** 0
- **Tool calls:** 39
- **Original source:** `logs/chats/worker_analysis_null_s42_s44_d102_20260524T164250.jsonl`
- **Structured JSON:** [`e32bca7ab313b2b64852.json`](../../sessions/e3/e32bca7ab313b2b64852.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

79 recorded events

### Tool call

_source line 1 · 2026-05-24T16:52:32.317537+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__register_artifact",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T16:52:32.317922+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T16:52:32.318101+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/ | grep a000",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/ | grep a000",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T16:52:32.318279+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T16:52:32.318454+00:00_

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
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
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

_source line 6 · 2026-05-24T16:52:32.318608+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"a000_s42\\na000_s43\\na000_s44\\na000_s46_fp32\\na000_s48_fp32\\na000_s51_fp32\\na000_t15_s42_fp32\\na000_t15_s43_fp32\\na010_s42\\na010_s42_fp32\\na010_s43_fp32\\na025_3seed_unified_summary.txt\\na025_s43\\na025_s44\\na048_s43_fp32\\na050_s42\\na050_s43\\na050_s44\\na055_s42_fp32\\na060_s42_bf16\\na075_s42\\na075_s43\\na075_s44\\nalpha_monotonicity.png\\nanalysis\\nanalysis_s44\\nanalysis_summary.json\\nc4_a050_s43_fp32\\nc4_a075_s43_fp32\\npooled_panel_results.json\\npooled_panel_summary.txt\\nty_3seed_a025_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.08}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T16:52:32.318776+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T16:52:32.318927+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\",\\n  \\\"data_dir\\\": \\\"data/wikitext103_5k\\\",\\n  \\\"dataset\\\": \\\"wikitext-103-v1\\\",\\n  \\\"synthetic_ratio\\\": 0.0,\\n  \\\"num_generations\\\": 10,\\n  \\\"steps_per_gen\\\": 5000,\\n  \\\"output_dir\\\": \\\"results/alpha_sweep/a000_s42\\\",\\n  \\\"seed\\\": 42,\\n  \\\"batch_size\\\": 4,\\n  \\\"max_length\\\": 512,\\n  \\\"lr\\\": 5e-05,\\n  \\\"gen_max_new_tokens\\\": 256,\\n  \\\"gen_batch_size\\\": 16,\\n  \\\"top_p\\\": 0.95,\\n  \\\"accumulate\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T16:52:32.319110+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T16:52:32.319269+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T16:52:32.319426+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\",\\n  \\\"data_dir\\\": \\\"data/wikitext103_5k\\\",\\n  \\\"dataset\\\": \\\"wikitext-103-v1\\\",\\n  \\\"synthetic_ratio\\\": 0.0,\\n  \\\"num_generations\\\": 10,\\n  \\\"steps_per_gen\\\": 5000,\\n  \\\"output_dir\\\": \\\"results/alpha_sweep/a000_s43\\\",\\n  \\\"seed\\\": 43,\\n  \\\"batch_size\\\": 4,\\n  \\\"max_length\\\": 512,\\n  \\\"lr\\\": 5e-05,\\n  \\\"gen_max_new_tokens\\\": 256,\\n  \\\"gen_batch_size\\\": 16,\\n  \\\"top_p\\\": 0.95,\\n  \\\"accumulate\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T16:52:32.319573+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\",\\n  \\\"data_dir\\\": \\\"data/wikitext103_5k\\\",\\n  \\\"dataset\\\": \\\"wikitext-103-v1\\\",\\n  \\\"synthetic_ratio\\\": 0.0,\\n  \\\"num_generations\\\": 10,\\n  \\\"steps_per_gen\\\": 5000,\\n  \\\"output_dir\\\": \\\"results/alpha_sweep/a000_s44\\\",\\n  \\\"seed\\\": 44,\\n  \\\"batch_size\\\": 4,\\n  \\\"max_length\\\": 512,\\n  \\\"lr\\\": 5e-05,\\n  \\\"gen_max_new_tokens\\\": 256,\\n  \\\"gen_batch_size\\\": 16,\\n  \\\"top_p\\\": 0.95,\\n  \\\"accumulate\\\": false\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T16:52:32.319743+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s46_fp32/config.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s46_fp32/config.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T16:52:32.319900+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_name\\\": \\\"EleutherAI/pythia-410m\\\",\\n  \\\"data_dir\\\": \\\"data/wikitext103_5k\\\",\\n  \\\"dataset\\\": \\\"wikitext-103-v1\\\",\\n  \\\"synthetic_ratio\\\": 0.0,\\n  \\\"num_generations\\\": 10,\\n  \\\"steps_per_gen\\\": 5000,\\n  \\\"output_dir\\\": \\\"results/alpha_sweep/a000_s46_fp32\\\",\\n  \\\"seed\\\": 46,\\n  \\\"batch_size\\\": 4,\\n  \\\"max_length\\\": 512,\\n  \\\"lr\\\": 5e-05,\\n  \\\"gen_max_new_tokens\\\": 256,\\n  \\\"gen_batch_size\\\": 16,\\n  \\\"top_p\\\": 0.95,\\n  \\\"accumulate\\\": false,\\n  \\\"start_gen\\\": 0,\\n  \\\"gradient_checkpointing\\\": false,\\n  \\\"bf16\\\": false,\\n  \\\"optim\\\": \\\"adamw_torch\\\",\\n  \\\"intervention_mode\\\": \\\"none\\\",\\n  \\\"intervention_metric\\\": \\\"token_entropy\\\",\\n  \\\"intervention_threshold\\\": 0.15,\\n  \\\"intervention_alpha\\\": 0.0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T16:52:32.320045+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -50 /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -50 /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T16:52:32.320217+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"5-method lead-lag analysis: generalized CLI version.\\n\\nUsage:\\n    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43\\n    python run_5method_analysis.py --data_dir results/alpha_sweep/a000_s43 --alpha 0.0 --seed 43 --dry-run\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport glob as glob_module\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nsys.path.insert(0, \\\"/root/autodl-tmp/distrib_canary_collapse\\\")\\nfrom permutation_granger import permutation_granger_test\\n\\nN_PERM = 5000\\nALPHA = 0.05\\n\\nCANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\nDOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"ece\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"}\\n\\n\\ndef load_series(data_dir):\\n    \\\"\\\"\\\"Load metrics - from all_metrics.json if available, else aggregate gen_X/metrics.json.\\\"\\\"\\\"\\n    all_path = os.path.join(data_dir, \\\"all_metrics.json\\\")\\n    if os.path.exists(all_path):\\n        with open(all_path) as f:\\n            data = json.load(f)\\n    else:\\n        # Aggregate from per-generation metrics\\n        gen_dirs = sorted(glob_module.glob(os.path.join(data_dir, \\\"gen_*\\\")),\\n                         key=lambda x: int(os.path.basename(x).split(\\\"_\\\")[1]))\\n        data = []\\n        for gd in gen_dirs:\\n            mp = os.path.join(gd, \\\"metrics.json\\\")\\n            if os.path.exists(mp):\\n                with open(mp) as f:\\n                    data.append(json.load(f))\\n        if not data:\\n            raise FileNotFoundError(f\\\"No metrics found in {data_dir}\\\")\\n    data.sort(key=lambda x: x[\\\"generation\\\"])\\n    out = {}\\n    for k in CANARIES + DOWNSTREA
…[truncated 110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T16:52:32.320455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"CANARIES\\|DOWNSTREAMS\\|argparse\\|add_argument\\|6.pair\\|pairs\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"CANARIES\\|DOWNSTREAMS\\|argparse\\|add_argument\\|6.pair\\|pairs\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T16:52:32.320607+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T16:52:32.320739+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"CANARIES\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"CANARIES\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T16:52:32.320874+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"23:CANARIES = [\\\"token_entropy\\\", \\\"ece\\\"]\\n50:    for k in CANARIES + DOWNSTREAMS:\\n268:    pairs = [{\\\"canary\\\": c, \\\"downstream\\\": d} for c in CANARIES for d in active_downstreams]\\n277:            \\\"canaries\\\": CANARIES,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T16:52:32.321001+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"DOWNSTREAMS\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"DOWNSTREAMS\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T16:52:32.321130+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"24:DOWNSTREAMS = [\\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n50:    for k in CANARIES + DOWNSTREAMS:\\n267:    active_downstreams = [d for d in DOWNSTREAMS if not all(v is None for v in series[d])]\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T16:52:32.321270+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"add_argument\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"add_argument\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T16:52:32.321420+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"455:    parser.add_argument(\\\"--data_dir\\\", required=True, help=\\\"Path to experiment directory (e.g. results/alpha_sweep/a000_s43)\\\")\\n456:    parser.add_argument(\\\"--alpha\\\", type=float, required=True, help=\\\"Alpha value (e.g. 0.0, 0.75)\\\")\\n457:    parser.add_argument(\\\"--seed\\\", type=int, required=True, help=\\\"Random seed\\\")\\n458:    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\", help=\\\"Check data availability without running analysis\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T16:52:32.321601+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"output\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"output\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T16:52:32.321729+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/fpr_transparency_all_seeds.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/fpr_transparency_all_seeds.json"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T16:52:32.321855+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T16:52:32.321975+00:00_

artifacts/_project/data/fpr_transparency_all_seeds.json
artifacts/fpr_transparency_all_seeds.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T16:52:32.322095+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/fpr_transparency_all_seeds.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/fpr_transparency_all_seeds.json"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T16:52:32.322219+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -30 /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -30 /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T16:52:32.322666+00:00_

1	{
2	  "description": "FPR transparency: per-seed per-pair raw p-values for 6 null experiments (alpha=0.00, Pythia-410M, T=10). Analyzed with batch_d102_6pair.py (D102 parameters).",
3	  "model": "pythia-410m",
4	  "alpha": 0.0,
5	  "T": 10,
6	  "n_perm": 5000,
7	  "threshold_criterion": "true_3sigma_d105",
8	  "pair_basis": "6-pair (distinct_1/2/3 only, mauve excluded)",
9	  "methods": [
10	    "perm_granger (BH-FDR across 6 pairs)",
11	    "diff_xcorr (BH-FDR across 6 pairs)",
12	    "threshold_onset (true_3sigma_d105)",
13	    "ty_granger (uncorrected)",
14	    "naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)"
15	  ],
16	  "consensus_rule": "K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.",
17	  "summary": {
18	    "total_seed_pairs": 36,
19	    "K_ge_3_count": 6,
20	    "K_ge_3_fpr": 0.1667,
21	    "per_seed_K_ge_3": {
22	      "s45": 1,
23	      "s46": 1,
24	      "s47": 2,
25	      "s48": 0,
26	      "s49": 0,
27	      "s50": 2
28	    },
29	    "K_ge_3_permg_breakdown": {
30	      "with_permg": 2,
31	      "without_permg": 4,
32	      "detail": "s50 te->d1,d2 include PermG (consensus=[naive,perm,ty]); s45 ece->d2, s46 ece->d2, s47 ece->d1,d2 do not (consensus=[naive,threshold,ty])"
33	    },
34	    "per_seed_permg_fwd_fdr": {
35	      "s45": 2,
36	      "s46": 0,
37	      "s47": 0,
38	      "s48": 0,
39	      "s49": 0,
40	      "s50": 2
41	    }
42	  },
43	  "seeds": [
44	    {
45	      "seed": 45,
46	      "exp_dir": "results/alpha_sweep/a000_s45_fp32",
47	      "T": 10,
48	      "n_gens": 11,
49	      "n_perm": 5000,
50	      "pairs": [
51	        {
52	          "canary": "token_entropy",
53	          "downstream": "distinct_1",
54	          "perm_granger_fwd_p": 0.081184,
55	          "perm_granger_fwd_sig_fdr": false,
56	          "perm_granger
…[truncated 30167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T16:52:32.322892+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    print(f\\\"\\\\nSaved: {json_path}\\\")\\n\\n    # Text summary\\n    summary_path = os.path.join(out_dir, \\\"5method_summary.txt\\\")\\n    with open(summary_path, \\\"w\\\") as f:\\n        f.write(f\\\"5-Method Lead-Lag Analysis Summary\\\\n\\\")\\n        f.write(f\\\"Alpha={alpha_val}, Seed={seed}, Generations={n_gens}\\\\n\\\")\\n        f.write(f\\\"{'='*60}\\\\n\\\\n\\\")\\n        f.write(f\\\"Robust pairs (>=3/5 methods agree): {all_results['summary']['robust_pairs']}/8\\\\n\\\\n\\\")\\n        f.write(f\\\"Per-method forward significance:\\\\n\\\")\\n        f.write(f\\\"  Perm Granger (FDR): {all_results['summary']['perm_granger_fdr_forward_sig']}/8\\\\n\\\")\\n        f.write(f\\\"  Diff XCorr (FDR):   {all_results['summary']['diff_xcorr_fdr_forward_sig']}/8\\\\n\\\")\\n        f.write(f\\\"  Threshold Onset:    {all_results['summary']['threshold_forward_sig']}/8\\\\n\\\")\\n        f.write(f\\\"  TY Granger:         {all_results['summary']['ty_forward_sig']}/8\\\\n\\\\n\\\")\\n        f.write(f\\\"Consensus detail:\\\\n\\\")\\n        for c in consensus:\\n            f.write(f\\\"  {c['pair']:<25} {c['votes']}/5  [{', '.join(c['methods']) if c['methods'] else 'none'}]\\\\n\\\")\\n    print(f\\\"Saved: {summary_path}\\\")\\n\\n    return all_results\\n\\n\\nif __name__ == \\\"__main__\\\":\\n    parser = argparse.ArgumentParser(description=\\\"5-method lead-lag analysis\\\")\\n    parser.add_argument(\\\"--data_dir\\\", required=True, help=\\\"Path to experiment directory (e.g. results/alpha_sweep/a000_s43)\\\")\\n    parser.add_argument(\\\"--alpha\\\", type=float, required=True, help=\\\"Alpha value (e.g. 0.0, 0.75)\\\")\\n    parser.add_argument(\\\"--seed\\\", type=int, required=True, help=\\\"Random seed\\\")\\n    parser.add_argument(\\\"--dry-run\\\", action=\\\"store_true\\\", help=\\\"Check data availability without running analysis\\\")\\n    args = parser.parse_args()\\n    run(arg
…[truncated 109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-24T16:52:32.323124+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"out_dir\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"out_dir\" /root/autodl-tmp/distrib_canary_collapse/run_5method_analysis_d102.py",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T16:52:32.323293+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/batch_d102_6pair.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/batch_d102_6pair.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T16:52:32.323439+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"412:    out_dir = os.path.join(data_dir, \\\"analysis\\\")\\n413:    os.makedirs(out_dir, exist_ok=True)\\n428:    json_path = os.path.join(out_dir, \\\"5method_leadlag.json\\\")\\n434:    summary_path = os.path.join(out_dir, \\\"5method_summary.txt\\\")\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-24T16:52:32.323581+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/distrib_canary_collapse/batch_d102_6pair.py': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-24T16:52:32.323712+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -rn \"mauve\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -rn \"mauve\" /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-24T16:52:32.323856+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"11:    \\\"mauve\\\": 0.03406737671684175,\\n23:    \\\"mauve\\\": 0.03232946507236373,\\n35:    \\\"mauve\\\": 0.029787866232434207,\\n47:    \\\"mauve\\\": 0.02652903668843056,\\n59:    \\\"mauve\\\": 0.027979995177423035,\\n71:    \\\"mauve\\\": 0.026873956511462842,\\n83:    \\\"mauve\\\": 0.027324607058632662,\\n95:    \\\"mauve\\\": 0.02999056483812801,\\n107:    \\\"mauve\\\": 0.027106146146103544,\\n119:    \\\"mauve\\\": 0.028780486018708678,\\n131:    \\\"mauve\\\": 0.030324074201419682,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-24T16:52:32.324030+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-24T16:52:32.324167+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5method_leadlag.json\\n5method_leadlag_pre_tyfix_batch.json\\n5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-24T16:52:32.324315+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T16:52:32.324450+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T16:52:32.324586+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5method_leadlag.json\\n5method_leadlag_pre_tyfix_batch.json\\n5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-24T16:52:32.324715+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"5method_leadlag.json\\n5method_leadlag_pre_tyfix_batch.json\\n5method_summary.txt\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-24T16:52:32.324868+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-24T16:52:32.325264+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.0,\\n    \\\"seed\\\": 42,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -5,\\n          \\\"r\\\": 0.9023,\\n          \\\"p_value\\\": 0.013857,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.9023,\\n              \\\"p\\\": 0.013857\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.7904,\\n              \\\"p\\\": 0.034399\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.694,\\n              \\\"p\\\": 0.056207\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.3609,\\n              \\\"p\\\": 0.339995\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.741,\\n              \\\"p\\\": 0.014202\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.3702,\\n              \\\"p\\\": 0.262357\\n            },\\n        
…[truncated 8553 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-24T16:52:32.325597+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-24T16:52:32.325978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.0,\\n    \\\"seed\\\": 43,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s43\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": 1,\\n          \\\"r\\\": -0.9029,\\n          \\\"p_value\\\": 0.000345,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.3372,\\n              \\\"p\\\": 0.513357\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": 0.6287,\\n              \\\"p\\\": 0.130434\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.1234,\\n              \\\"p\\\": 0.771028\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": 0.0248,\\n              \\\"p\\\": 0.949522\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.5481,\\n              \\\"p\\\": 0.100905\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.1059,\\n              \\\"p\\\": 0.756695\\n            },\\n      
…[truncated 8526 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-24T16:52:32.326161+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/analysis/5method_leadlag.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44/analysis/5method_leadlag.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-24T16:52:32.326566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"alpha\\\": 0.0,\\n    \\\"seed\\\": 44,\\n    \\\"n_gens\\\": 11,\\n    \\\"data_dir\\\": \\\"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s44\\\",\\n    \\\"methods\\\": [\\n      \\\"naive_xcorr\\\",\\n      \\\"diff_xcorr\\\",\\n      \\\"threshold_onset\\\",\\n      \\\"perm_granger\\\",\\n      \\\"ty_granger\\\"\\n    ],\\n    \\\"n_perm\\\": 5000,\\n    \\\"canaries\\\": [\\n      \\\"token_entropy\\\",\\n      \\\"ece\\\"\\n    ],\\n    \\\"downstreams\\\": [\\n      \\\"distinct_1\\\",\\n      \\\"distinct_2\\\",\\n      \\\"distinct_3\\\",\\n      \\\"mauve\\\"\\n    ],\\n    \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\"\\n  },\\n  \\\"pairs\\\": [\\n    {\\n      \\\"canary\\\": \\\"token_entropy\\\",\\n      \\\"downstream\\\": \\\"distinct_1\\\",\\n      \\\"forward\\\": {\\n        \\\"naive_xcorr\\\": {\\n          \\\"method\\\": \\\"naive_xcorr\\\",\\n          \\\"peak_lag\\\": -5,\\n          \\\"r\\\": 0.9144,\\n          \\\"p_value\\\": 0.010676,\\n          \\\"significant\\\": true,\\n          \\\"all_lags\\\": [\\n            {\\n              \\\"lag\\\": -5,\\n              \\\"r\\\": 0.9144,\\n              \\\"p\\\": 0.010676\\n            },\\n            {\\n              \\\"lag\\\": -4,\\n              \\\"r\\\": -0.0427,\\n              \\\"p\\\": 0.927604\\n            },\\n            {\\n              \\\"lag\\\": -3,\\n              \\\"r\\\": 0.1212,\\n              \\\"p\\\": 0.775018\\n            },\\n            {\\n              \\\"lag\\\": -2,\\n              \\\"r\\\": -0.0825,\\n              \\\"p\\\": 0.832956\\n            },\\n            {\\n              \\\"lag\\\": -1,\\n              \\\"r\\\": 0.6004,\\n              \\\"p\\\": 0.066472\\n            },\\n            {\\n              \\\"lag\\\": 0,\\n              \\\"r\\\": 0.2624,\\n              \\\"p\\\": 0.435764\\n            },\\n    
…[truncated 8540 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T16:52:32.326822+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\nDISTINCT_DS = ['distinct_1', 'distinct_2', 'distinct_3']\nseeds_data = []\n\nfor seed, dirname in [(42, 'a000_s42'), (43, 'a000_s43'), (44, 'a000_s44')]:\n    path = f'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json'\n    with open(path) as f:\n        data = json.load(f)\n    \n    seed_entry = {\n        'seed': seed,\n        'exp_dir': f'results/alpha_sweep/{dirname}',\n        'T': 10,\n        'n_gens': data['meta']['n_gens'],\n        'n_perm': data['meta']['n_perm'],\n        'pairs': []\n    }\n    \n    # Build consensus lookup\n    cons_lookup = {}\n    for c in data['consensus']:\n        cons_lookup[c['pair']] = c\n    \n    for pair in data['pairs']:\n        if pair['downstream'] not in DISTINCT_DS:\n            continue\n        \n        fwd = pair['forward']\n        \n        # Extract fields matching fpr_transparency format\n        p = {\n            'canary': pair['canary'],\n            'downstream': pair['downstream'],\n            'perm_granger_fwd_p': fwd['perm_granger']['p_value'],\n            'perm_granger_fwd_sig_fdr': fwd['perm_granger'].get('significant_fdr', False),\n            'perm_granger_rev_p': pair.get('reverse', {}).get('perm_granger', {}).get('p_value', None),\n            'diff_xcorr_fwd_p': fwd['diff_xcorr']['p_value'],\n            'diff_xcorr_fwd_r': fwd['diff_xcorr']['r'],\n            'diff_xcorr_fwd_lag': fwd['diff_xcorr']['peak_lag'],\n            'diff_xcorr_fwd_sig_fdr': fwd['diff_xcorr'].get('significant_fdr', False),\n            'threshold_onset_lead': fwd['threshold_onset'].get('lead_time'),\n            'threshold_onset_sig': fwd['threshold_onset']['significant'],\n            'ty_granger_p': fwd['ty_granger']['p_value'],\n            'ty_granger_sig': fwd['ty_granger']['significant'],\n            'naive_xcorr_r': fwd['naive_xcorr']['r'],\n            'naive_xcorr_lag': fwd['naive_xcorr']['peak_lag'],\n            'naive_xcorr_sig': fwd['naive_xcorr']['significant'],\n        }\n        \n        # Get consensus\n        pair_key = f\\\"{pair['canary']}<{pair['downstream']}\\\"\n        cons = cons_lookup.get(pair_key, {'votes': 0, 'methods': []})\n        p['consensus_votes'] = cons['votes']\n        p['consensus_methods'] = cons['methods']\n        \n        seed_entry['pairs'].append(p)\n    \n    seeds_data.append(seed_entry)\n\n# Compute summary\ntotal_pairs = sum(len(s['pairs']) for s in seeds_data)\nk_ge_3_per_seed = {}\npermg_fwd_per_seed = {}\n\nfor s in seeds_data:\n    sid = f's{s[\\\"seed\\\"]}'\n    k_ge_3_per_seed[sid] = sum(1 for p in s['pairs'] if p['consensus_votes'] >= 3)\n    permg_fwd_per_seed[sid] = sum(1 for p in s['pairs'] if p['perm_granger_fwd_sig_fdr'])\n\nk_ge_3_total = sum(k_ge_3_per_seed.values())\n\nresult = {\n    'description': 'FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Analyzed with run_5method_analysis_d102.py (D102 parameters).',\n    'model': 'pythia-410m',\n    'alpha': 0.0,\n    'T': 10,\n    'n_perm': 5000,\n    'threshold_criterion': 'true_3sigma_d105',\n    'pair_basis': '6-pair (distinct_1/2/3 only, mauve excluded)',\n    'methods': [\n        'perm_granger (BH-FDR across 6 pairs)',\n        'diff_xcorr (BH-FDR across 6 pairs)',\n        'threshold_onset (true_3sigma_d105)',\n        'ty_granger (uncorrected)',\n        'naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)'\n    ],\n    'consensus_rule': 'K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.',\n    'summary': {\n        'total_seed_pairs': total_pairs,\n        'K_ge_3_count': k_ge_3_total,\n        'K_ge_3_fpr': round(k_ge_3_total / total_pairs, 4) if total_pairs > 0 else 0,\n        'per_seed_K_ge_3': k_ge_3_per_seed,\n        'per_seed_permg_fwd_fdr': permg_fwd_per_seed\n    },\n    'seeds': seeds_data\n}\n\nprint(json.dumps(result, indent=2))\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\nDISTINCT_DS = ['distinct_1', 'distinct_2', 'distinct_3']\nseeds_data = []\n\nfor seed, dirname in [(42, 'a000_s42'), (43, 'a000_s43'), (44, 'a000_s44')]:\n    path = f'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json'\n    with open(path) as f:\n        data = json.load(f)\n    \n    seed_entry = {\n        'seed': seed,\n        'exp_dir': f'results/alpha_sweep/{dirname}',\n        'T': 10,\n        'n_gens': data['meta']['n_gens'],\n        'n_perm': data['meta']['n_perm'],\n        'pairs': []\n    }\n    \n    # Build consensus lookup\n    cons_lookup = {}\n    for c in data['consensus']:\n        cons_lookup[c['pair']] = c\n    \n    for pair in data['pairs']:\n        if pair['downstream'] not in DISTINCT_DS:\n            continue\n        \n        fwd = pair['forward']\n        \n        # Extract fields matching fpr_transparency format\n        p = {\n            'canary': pair['canary'],\n            'downstream': pair['downstream'],\n            'perm_granger_fwd_p': fwd['perm_granger']['p_value'],\n            'perm_granger_fwd_sig_fdr': fwd['perm_granger'].get('significant_fdr', False),\n            'perm_granger_rev_p': pair.get('reverse', {}).get('perm_granger', {}).get('p_value', None),\n            'diff_xcorr_fwd_p': fwd['diff_xcorr']['p_value'],\n            'diff_xcorr_fwd_r': fwd['diff_xcorr']['r'],\n            'diff_xcorr_fwd_lag': fwd['diff_xcorr']['peak_lag'],\n            'diff_xcorr_fwd_sig_fdr': fwd['diff_xcorr'].get('significant_fdr', False),\n            'threshold_onset_lead': fwd['threshold_onset'].get('lead_time'),\n            'threshold_onset_sig': fwd['threshold_onset']['significant'],\n            'ty_granger_p': fwd['ty_granger']['p_value'],\n            'ty_granger_sig': fwd['ty_granger']['significant'],\n            'naive_xcorr_r': fwd['naive_xcorr']['r'],\n            'naive_xcorr_lag': fwd['naive_xcorr']['peak_lag'],\n            'naive_xcorr_sig': fwd['naive_xcorr']['significant'],\n        }\n        \n        # Get consensus\n        pair_key = f\\\"{pair['canary']}<{pair['downstream']}\\\"\n        cons = cons_lookup.get(pair_key, {'votes': 0, 'methods': []})\n        p['consensus_votes'] = cons['votes']\n        p['consensus_methods'] = cons['methods']\n        \n        seed_entry['pairs'].append(p)\n    \n    seeds_data.append(seed_entry)\n\n# Compute summary\ntotal_pairs = sum(len(s['pairs']) for s in seeds_data)\nk_ge_3_per_seed = {}\npermg_fwd_per_seed = {}\n\nfor s in seeds_data:\n    sid = f's{s[\\\"seed\\\"]}'\n    k_ge_3_per_seed[sid] = sum(1 for p in s['pairs'] if p['consensus_votes'] >= 3)\n    permg_fwd_per_seed[sid] = sum(1 for p in s['pairs'] if p['perm_granger_fwd_sig_fdr'])\n\nk_ge_3_total = sum(k_ge_3_per_seed.values())\n\nresult = {\n    'description': 'FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Analyzed with run_5method_analysis_d102.py (D102 parameters).',\n    'model': 'pythia-410m',\n    'alpha': 0.0,\n    'T': 10,\n    'n_perm': 5000,\n    'threshold_criterion': 'true_3sigma_d105',\n    'pair_basis': '6-pair (distinct_1/2/3 only, mauve excluded)',\n    'methods': [\n        'perm_granger (BH-FDR across 6 pairs)',\n        'diff_xcorr (BH-FDR across 6 pairs)',\n        'threshold_onset (true_3sigma_d105)',\n        'ty_granger (uncorrected)',\n        'naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)'\n    ],\n    'consensus_rule': 'K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.',\n    'summary': {\n        'total_seed_pairs': total_pairs,\n        'K_ge_3_count': k_ge_3_total,\n        'K_ge_3_fpr': round(k_ge_3_total / total_pairs, 4) if total_pairs > 0 else 0,\n        'per_seed_K_ge_3': k_ge_3_per_seed,\n        'per_seed_permg_fwd_fdr': permg_fwd_per_seed\n    },\n    'seeds': seeds_data\n}\n\nprint(json.dumps(result, indent=2))\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-24T16:52:32.327219+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Analyzed with run_5method_analysis_d102.py (D102 parameters).\\\",\\n  \\\"model\\\": \\\"pythia-410m\\\",\\n  \\\"alpha\\\": 0.0,\\n  \\\"T\\\": 10,\\n  \\\"n_perm\\\": 5000,\\n  \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\",\\n  \\\"pair_basis\\\": \\\"6-pair (distinct_1/2/3 only, mauve excluded)\\\",\\n  \\\"methods\\\": [\\n    \\\"perm_granger (BH-FDR across 6 pairs)\\\",\\n    \\\"diff_xcorr (BH-FDR across 6 pairs)\\\",\\n    \\\"threshold_onset (true_3sigma_d105)\\\",\\n    \\\"ty_granger (uncorrected)\\\",\\n    \\\"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\\\"\\n  ],\\n  \\\"consensus_rule\\\": \\\"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\\\",\\n  \\\"summary\\\": {\\n    \\\"total_seed_pairs\\\": 18,\\n    \\\"K_ge_3_count\\\": 0,\\n    \\\"K_ge_3_fpr\\\": 0.0,\\n    \\\"per_seed_K_ge_3\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    },\\n    \\\"per_seed_permg_fwd_fdr\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    }\\n  },\\n  \\\"seeds\\\": [\\n    {\\n      \\\"seed\\\": 42,\\n      \\\"exp_dir\\\": \\\"results/alpha_sweep/a000_s42\\\",\\n      \\\"T\\\": 10,\\n      \\\"n_gens\\\": 11,\\n      \\\"n_perm\\\": 5000,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"canary\\\": \\\"token_entropy\\\",\\n          \\\"downstream\\\": \\\"distinct_1\\\",\\n          \\\"perm_granger_fwd_p\\\": 0.05139,\\n          \\\"perm_granger_fwd_sig_fdr\\\": false,\\n          \\\"perm_granger_rev_p\\\": 0.795641,\\n          \\\"diff_xcorr_fwd_p\\\": 0.000157,\\n 
…[truncated 8090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-24T16:52:32.327517+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\nDISTINCT_DS = ['distinct_1', 'distinct_2', 'distinct_3']\nseeds_data = []\n\nfor seed, dirname in [(42, 'a000_s42'), (43, 'a000_s43'), (44, 'a000_s44')]:\n    path = f'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json'\n    with open(path) as f:\n        data = json.load(f)\n    \n    seed_entry = {\n        'seed': seed,\n        'exp_dir': f'results/alpha_sweep/{dirname}',\n        'T': 10,\n        'n_gens': data['meta']['n_gens'],\n        'n_perm': data['meta']['n_perm'],\n        'pairs': []\n    }\n    \n    cons_lookup = {}\n    for c in data['consensus']:\n        cons_lookup[c['pair']] = c\n    \n    for pair in data['pairs']:\n        if pair['downstream'] not in DISTINCT_DS:\n            continue\n        fwd = pair['forward']\n        p = {\n            'canary': pair['canary'],\n            'downstream': pair['downstream'],\n            'perm_granger_fwd_p': fwd['perm_granger']['p_value'],\n            'perm_granger_fwd_sig_fdr': fwd['perm_granger'].get('significant_fdr', False),\n            'perm_granger_rev_p': pair.get('reverse', {}).get('perm_granger', {}).get('p_value', None),\n            'diff_xcorr_fwd_p': fwd['diff_xcorr']['p_value'],\n            'diff_xcorr_fwd_r': fwd['diff_xcorr']['r'],\n            'diff_xcorr_fwd_lag': fwd['diff_xcorr']['peak_lag'],\n            'diff_xcorr_fwd_sig_fdr': fwd['diff_xcorr'].get('significant_fdr', False),\n            'threshold_onset_lead': fwd['threshold_onset'].get('lead_time'),\n            'threshold_onset_sig': fwd['threshold_onset']['significant'],\n            'ty_granger_p': fwd['ty_granger']['p_value'],\n            'ty_granger_sig': fwd['ty_granger']['significant'],\n            'naive_xcorr_r': fwd['naive_xcorr']['r'],\n            'naive_xcorr_lag': fwd['naive_xcorr']['peak_lag'],\n            'naive_xcorr_sig': fwd['naive_xcorr']['significant'],\n        }\n        pair_key = f\\\"{pair['canary']}<{pair['downstream']}\\\"\n        cons = cons_lookup.get(pair_key, {'votes': 0, 'methods': []})\n        p['consensus_votes'] = cons['votes']\n        p['consensus_methods'] = cons['methods']\n        seed_entry['pairs'].append(p)\n    \n    seeds_data.append(seed_entry)\n\ntotal_pairs = sum(len(s['pairs']) for s in seeds_data)\nk_ge_3_per_seed = {}\npermg_fwd_per_seed = {}\n\nfor s in seeds_data:\n    sid = f's{s[\\\"seed\\\"]}'\n    k_ge_3_per_seed[sid] = sum(1 for p in s['pairs'] if p['consensus_votes'] >= 3)\n    permg_fwd_per_seed[sid] = sum(1 for p in s['pairs'] if p['perm_granger_fwd_sig_fdr'])\n\nk_ge_3_total = sum(k_ge_3_per_seed.values())\n\nresult = {\n    'description': 'FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Analyzed with run_5method_analysis_d102.py (D102 parameters).',\n    'model': 'pythia-410m',\n    'alpha': 0.0,\n    'T': 10,\n    'n_perm': 5000,\n    'threshold_criterion': 'true_3sigma_d105',\n    'pair_basis': '6-pair (distinct_1/2/3 only, mauve excluded)',\n    'methods': [\n        'perm_granger (BH-FDR across 6 pairs)',\n        'diff_xcorr (BH-FDR across 6 pairs)',\n        'threshold_onset (true_3sigma_d105)',\n        'ty_granger (uncorrected)',\n        'naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)'\n    ],\n    'consensus_rule': 'K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.',\n    'summary': {\n        'total_seed_pairs': total_pairs,\n        'K_ge_3_count': k_ge_3_total,\n        'K_ge_3_fpr': round(k_ge_3_total / total_pairs, 4) if total_pairs > 0 else 0,\n        'per_seed_K_ge_3': k_ge_3_per_seed,\n        'per_seed_permg_fwd_fdr': permg_fwd_per_seed\n    },\n    'seeds': seeds_data\n}\n\nwith open('/tmp/D102_null_s42_s44_fpr.json', 'w') as f:\n    json.dump(result, f, indent=2)\nprint('Saved to /tmp/D102_null_s42_s44_fpr.json')\nprint(f'Size: {len(json.dumps(result))} bytes')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\n\nDISTINCT_DS = ['distinct_1', 'distinct_2', 'distinct_3']\nseeds_data = []\n\nfor seed, dirname in [(42, 'a000_s42'), (43, 'a000_s43'), (44, 'a000_s44')]:\n    path = f'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json'\n    with open(path) as f:\n        data = json.load(f)\n    \n    seed_entry = {\n        'seed': seed,\n        'exp_dir': f'results/alpha_sweep/{dirname}',\n        'T': 10,\n        'n_gens': data['meta']['n_gens'],\n        'n_perm': data['meta']['n_perm'],\n        'pairs': []\n    }\n    \n    cons_lookup = {}\n    for c in data['consensus']:\n        cons_lookup[c['pair']] = c\n    \n    for pair in data['pairs']:\n        if pair['downstream'] not in DISTINCT_DS:\n            continue\n        fwd = pair['forward']\n        p = {\n            'canary': pair['canary'],\n            'downstream': pair['downstream'],\n            'perm_granger_fwd_p': fwd['perm_granger']['p_value'],\n            'perm_granger_fwd_sig_fdr': fwd['perm_granger'].get('significant_fdr', False),\n            'perm_granger_rev_p': pair.get('reverse', {}).get('perm_granger', {}).get('p_value', None),\n            'diff_xcorr_fwd_p': fwd['diff_xcorr']['p_value'],\n            'diff_xcorr_fwd_r': fwd['diff_xcorr']['r'],\n            'diff_xcorr_fwd_lag': fwd['diff_xcorr']['peak_lag'],\n            'diff_xcorr_fwd_sig_fdr': fwd['diff_xcorr'].get('significant_fdr', False),\n            'threshold_onset_lead': fwd['threshold_onset'].get('lead_time'),\n            'threshold_onset_sig': fwd['threshold_onset']['significant'],\n            'ty_granger_p': fwd['ty_granger']['p_value'],\n            'ty_granger_sig': fwd['ty_granger']['significant'],\n            'naive_xcorr_r': fwd['naive_xcorr']['r'],\n            'naive_xcorr_lag': fwd['naive_xcorr']['peak_lag'],\n            'naive_xcorr_sig': fwd['naive_xcorr']['significant'],\n        }\n        pair_key = f\\\"{pair['canary']}<{pair['downstream']}\\\"\n        cons = cons_lookup.get(pair_key, {'votes': 0, 'methods': []})\n        p['consensus_votes'] = cons['votes']\n        p['consensus_methods'] = cons['methods']\n        seed_entry['pairs'].append(p)\n    \n    seeds_data.append(seed_entry)\n\ntotal_pairs = sum(len(s['pairs']) for s in seeds_data)\nk_ge_3_per_seed = {}\npermg_fwd_per_seed = {}\n\nfor s in seeds_data:\n    sid = f's{s[\\\"seed\\\"]}'\n    k_ge_3_per_seed[sid] = sum(1 for p in s['pairs'] if p['consensus_votes'] >= 3)\n    permg_fwd_per_seed[sid] = sum(1 for p in s['pairs'] if p['perm_granger_fwd_sig_fdr'])\n\nk_ge_3_total = sum(k_ge_3_per_seed.values())\n\nresult = {\n    'description': 'FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Analyzed with run_5method_analysis_d102.py (D102 parameters).',\n    'model': 'pythia-410m',\n    'alpha': 0.0,\n    'T': 10,\n    'n_perm': 5000,\n    'threshold_criterion': 'true_3sigma_d105',\n    'pair_basis': '6-pair (distinct_1/2/3 only, mauve excluded)',\n    'methods': [\n        'perm_granger (BH-FDR across 6 pairs)',\n        'diff_xcorr (BH-FDR across 6 pairs)',\n        'threshold_onset (true_3sigma_d105)',\n        'ty_granger (uncorrected)',\n        'naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)'\n    ],\n    'consensus_rule': 'K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.',\n    'summary': {\n        'total_seed_pairs': total_pairs,\n        'K_ge_3_count': k_ge_3_total,\n        'K_ge_3_fpr': round(k_ge_3_total / total_pairs, 4) if total_pairs > 0 else 0,\n        'per_seed_K_ge_3': k_ge_3_per_seed,\n        'per_seed_permg_fwd_fdr': permg_fwd_per_seed\n    },\n    'seeds': seeds_data\n}\n\nwith open('/tmp/D102_null_s42_s44_fpr.json', 'w') as f:\n    json.dump(result, f, indent=2)\nprint('Saved to /tmp/D102_null_s42_s44_fpr.json')\nprint(f'Size: {len(json.dumps(result))} bytes')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-24T16:52:32.327709+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Saved to /tmp/D102_null_s42_s44_fpr.json\\nSize: 10410 bytes\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-24T16:52:32.327848+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /tmp/D102_null_s42_s44_fpr.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /tmp/D102_null_s42_s44_fpr.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-24T16:52:32.328168+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Analyzed with run_5method_analysis_d102.py (D102 parameters).\\\",\\n  \\\"model\\\": \\\"pythia-410m\\\",\\n  \\\"alpha\\\": 0.0,\\n  \\\"T\\\": 10,\\n  \\\"n_perm\\\": 5000,\\n  \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\",\\n  \\\"pair_basis\\\": \\\"6-pair (distinct_1/2/3 only, mauve excluded)\\\",\\n  \\\"methods\\\": [\\n    \\\"perm_granger (BH-FDR across 6 pairs)\\\",\\n    \\\"diff_xcorr (BH-FDR across 6 pairs)\\\",\\n    \\\"threshold_onset (true_3sigma_d105)\\\",\\n    \\\"ty_granger (uncorrected)\\\",\\n    \\\"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\\\"\\n  ],\\n  \\\"consensus_rule\\\": \\\"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\\\",\\n  \\\"summary\\\": {\\n    \\\"total_seed_pairs\\\": 18,\\n    \\\"K_ge_3_count\\\": 0,\\n    \\\"K_ge_3_fpr\\\": 0.0,\\n    \\\"per_seed_K_ge_3\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    },\\n    \\\"per_seed_permg_fwd_fdr\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    }\\n  },\\n  \\\"seeds\\\": [\\n    {\\n      \\\"seed\\\": 42,\\n      \\\"exp_dir\\\": \\\"results/alpha_sweep/a000_s42\\\",\\n      \\\"T\\\": 10,\\n      \\\"n_gens\\\": 11,\\n      \\\"n_perm\\\": 5000,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"canary\\\": \\\"token_entropy\\\",\\n          \\\"downstream\\\": \\\"distinct_1\\\",\\n          \\\"perm_granger_fwd_p\\\": 0.05139,\\n          \\\"perm_granger_fwd_sig_fdr\\\": false,\\n          \\\"perm_granger_rev_p\\\": 0.795641,\\n          \\\"diff_xcorr_fwd_p\\\": 0.000157,\\n 
…[truncated 8089 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-24T16:52:32.328431+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\nimport numpy as np\n\ndef bh_fdr(pvals):\n    \\\"\\\"\\\"BH-FDR correction: returns adjusted p-values.\\\"\\\"\\\"\n    n = len(pvals)\n    order = np.argsort(pvals)\n    adj = np.zeros(n)\n    for i, rank in enumerate(range(1, n+1)):\n        adj[order[i]] = pvals[order[i]] * n / rank\n    # Enforce monotonicity (step-down)\n    for i in range(n-2, -1, -1):\n        adj[order[i]] = min(adj[order[i]], adj[order[i+1]] if i+1 < n else 1.0)\n    return np.clip(adj, 0, 1).tolist()\n\nDISTINCT_DS = ['distinct_1', 'distinct_2', 'distinct_3']\nseeds_data = []\n\nfor seed, dirname in [(42, 'a000_s42'), (43, 'a000_s43'), (44, 'a000_s44')]:\n    path = f'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json'\n    with open(path) as f:\n        data = json.load(f)\n    \n    # Filter to 6 pairs only\n    filtered_pairs = [p for p in data['pairs'] if p['downstream'] in DISTINCT_DS]\n    \n    # Recompute BH-FDR across 6 pairs for permG and diff_xcorr\n    permg_pvals = [p['forward']['perm_granger']['p_value'] for p in filtered_pairs]\n    diffx_pvals = [p['forward']['diff_xcorr']['p_value'] for p in filtered_pairs]\n    \n    permg_fdr = bh_fdr(permg_pvals)\n    diffx_fdr = bh_fdr(diffx_pvals)\n    \n    # Build consensus with corrected FDR\n    seed_entry = {\n        'seed': seed,\n        'exp_dir': f'results/alpha_sweep/{dirname}',\n        'T': 10,\n        'n_gens': data['meta']['n_gens'],\n        'n_perm': data['meta']['n_perm'],\n        'pairs': []\n    }\n    \n    for i, pair in enumerate(filtered_pairs):\n        fwd = pair['forward']\n        \n        permg_sig_fdr = permg_fdr[i] < 0.05\n        diffx_sig_fdr = diffx_fdr[i] < 0.05\n        \n        naive = fwd['naive_xcorr']\n        diff = fwd['diff_xcorr']\n        threshold = fwd['threshold_onset']\n        permg = fwd['perm_granger']\n        ty = fwd['ty_granger']\n        \n        # Recompute consensus with D102 rules:\n        # - xcorr (naive, diff): vote if peak_lag < 0\n        # - PermG: vote if significant_fdr\n        # - TY: vote if significant\n        # - Threshold: vote if significant (canary onset < downstream onset, i.e. lead > 0)\n        methods = []\n        if naive['significant'] and naive['peak_lag'] < 0:\n            methods.append('naive')\n        if diffx_sig_fdr and diff['peak_lag'] < 0:\n            methods.append('diff')\n        if threshold['significant']:\n            methods.append('threshold')\n        if permg_sig_fdr:\n            methods.append('perm')\n        if ty['significant']:\n            methods.append('ty')\n        \n        p = {\n            'canary': pair['canary'],\n            'downstream': pair['downstream'],\n            'perm_granger_fwd_p': round(permg['p_value'], 6),\n            'perm_granger_fwd_sig_fdr': permg_sig_fdr,\n            'perm_granger_rev_p': round(pair.get('reverse', {}).get('perm_granger', {}).get('p_value', 0), 6) if pair.get('reverse') else None,\n            'diff_xcorr_fwd_p': round(diff['p_value'], 6),\n            'diff_xcorr_fwd_r': round(diff['r'], 4),\n            'diff_xcorr_fwd_lag': diff['peak_lag'],\n            'diff_xcorr_fwd_sig_fdr': diffx_sig_fdr,\n            'threshold_onset_lead': threshold.get('lead_time'),\n            'threshold_onset_sig': threshold['significant'],\n            'ty_granger_p': round(ty['p_value'], 6),\n            'ty_granger_sig': ty['significant'],\n            'naive_xcorr_r': round(naive['r'], 4),\n            'naive_xcorr_lag': naive['peak_lag'],\n            'naive_xcorr_sig': naive['significant'],\n            'consensus_votes': len(methods),\n            'consensus_methods': methods\n        }\n        seed_entry['pairs'].append(p)\n    \n    seeds_data.append(seed_entry)\n\n# Summary\ntotal_pairs = sum(len(s['pairs']) for s in seeds_data)\nk_ge_3_per_seed = {}\npermg_fwd_per_seed = {}\nk_ge_3_permg_detail = []\n\nfor s in seeds_data:\n    sid = f's{s[\\\"seed\\\"]}'\n    k_ge_3_per_seed[sid] = sum(1 for p in s['pairs'] if p['consensus_votes'] >= 3)\n    permg_fwd_per_seed[sid] = sum(1 for p in s['pairs'] if p['perm_granger_fwd_sig_fdr'])\n    for p in s['pairs']:\n        if p['consensus_votes'] >= 3:\n            has_permg = 'perm' in p['consensus_methods']\n            k_ge_3_permg_detail.append({\n                'seed': s['seed'],\n                'pair': f\\\"{p['canary']}->{p['downstream']}\\\",\n                'methods': p['consensus_methods'],\n                'has_permg': has_permg\n            })\n\nk_ge_3_total = sum(k_ge_3_per_seed.values())\nk_ge_3_with_permg = sum(1 for d in k_ge_3_permg_detail if d['has_permg'])\n\nresult = {\n    'description': 'FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.',\n    'model': 'pythia-410m',\n    'alpha': 0.0,\n    'T': 10,\n    'n_perm': 5000,\n    'threshold_criterion': 'true_3sigma_d105',\n    'pair_basis': '6-pair (distinct_1/2/3 only, mauve excluded)',\n    'methods': [\n        'perm_granger (BH-FDR across 6 pairs)',\n        'diff_xcorr (BH-FDR across 6 pairs)',\n        'threshold_onset (true_3sigma_d105)',\n        'ty_granger (uncorrected)',\n        'naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)'\n    ],\n    'consensus_rule': 'K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.',\n    'summary': {\n        'total_seed_pairs': total_pairs,\n        'K_ge_3_count': k_ge_3_total,\n        'K_ge_3_fpr': round(k_ge_3_total / total_pairs, 4) if total_pairs > 0 else 0,\n        'per_seed_K_ge_3': k_ge_3_per_seed,\n        'K_ge_3_permg_breakdown': {\n            'with_permg': k_ge_3_with_permg,\n            'without_permg': k_ge_3_total - k_ge_3_with_permg,\n            'detail': '; '.join([f\\\"s{d['seed']} {d['pair']} [{','.join(d['methods'])}]\\\" for d in k_ge_3_permg_detail]) if k_ge_3_permg_detail else 'none'\n        },\n        'per_seed_permg_fwd_fdr': permg_fwd_per_seed\n    },\n    'seeds': seeds_data\n}\n\nwith open('/tmp/D102_null_s42_s44_fpr.json', 'w') as f:\n    json.dump(result, f, indent=2)\n\nprint('=== Summary ===')\nprint(f'Total pairs: {total_pairs}')\nprint(f'K>=3 count: {k_ge_3_total}, FPR: {k_ge_3_total/total_pairs:.4f}')\nprint(f'Per-seed K>=3: {k_ge_3_per_seed}')\nprint(f'Per-seed PermG FDR fwd: {permg_fwd_per_seed}')\nprint()\nfor s in seeds_data:\n    print(f\\\"--- s{s['seed']} ---\\\")\n    for p in s['pairs']:\n        print(f\\\"  {p['canary']}->{p['downstream']}: K={p['consensus_votes']} {p['consensus_methods']}  permg_p={p['perm_granger_fwd_p']:.4f} fdr={p['perm_granger_fwd_sig_fdr']}\\\")\nprint()\nprint('Saved /tmp/D102_null_s42_s44_fpr.json')\n\"\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \"\nimport json\nimport numpy as np\n\ndef bh_fdr(pvals):\n    \\\"\\\"\\\"BH-FDR correction: returns adjusted p-values.\\\"\\\"\\\"\n    n = len(pvals)\n    order = np.argsort(pvals)\n    adj = np.zeros(n)\n    for i, rank in enumerate(range(1, n+1)):\n        adj[order[i]] = pvals[order[i]] * n / rank\n    # Enforce monotonicity (step-down)\n    for i in range(n-2, -1, -1):\n        adj[order[i]] = min(adj[order[i]], adj[order[i+1]] if i+1 < n else 1.0)\n    return np.clip(adj, 0, 1).tolist()\n\nDISTINCT_DS = ['distinct_1', 'distinct_2', 'distinct_3']\nseeds_data = []\n\nfor seed, dirname in [(42, 'a000_s42'), (43, 'a000_s43'), (44, 'a000_s44')]:\n    path = f'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json'\n    with open(path) as f:\n        data = json.load(f)\n    \n    # Filter to 6 pairs only\n    filtered_pairs = [p for p in data['pairs'] if p['downstream'] in DISTINCT_DS]\n    \n    # Recompute BH-FDR across 6 pairs for permG and diff_xcorr\n    permg_pvals = [p['forward']['perm_granger']['p_value'] for p in filtered_pairs]\n    diffx_pvals = [p['forward']['diff_xcorr']['p_value'] for p in filtered_pairs]\n    \n    permg_fdr = bh_fdr(permg_pvals)\n    diffx_fdr = bh_fdr(diffx_pvals)\n    \n    # Build consensus with corrected FDR\n    seed_entry = {\n        'seed': seed,\n        'exp_dir': f'results/alpha_sweep/{dirname}',\n        'T': 10,\n        'n_gens': data['meta']['n_gens'],\n        'n_perm': data['meta']['n_perm'],\n        'pairs': []\n    }\n    \n    for i, pair in enumerate(filtered_pairs):\n        fwd = pair['forward']\n        \n        permg_sig_fdr = permg_fdr[i] < 0.05\n        diffx_sig_fdr = diffx_fdr[i] < 0.05\n        \n        naive = fwd['naive_xcorr']\n        diff = fwd['diff_xcorr']\n        threshold = fwd['threshold_onset']\n        permg = fwd['perm_granger']\n        ty = fwd['ty_granger']\n        \n        # Recompute consensus with D102 rules:\n        # - xcorr (naive, diff): vote if peak_lag < 0\n        # - PermG: vote if significant_fdr\n        # - TY: vote if significant\n        # - Threshold: vote if significant (canary onset < downstream onset, i.e. lead > 0)\n        methods = []\n        if naive['significant'] and naive['peak_lag'] < 0:\n            methods.append('naive')\n        if diffx_sig_fdr and diff['peak_lag'] < 0:\n            methods.append('diff')\n        if threshold['significant']:\n            methods.append('threshold')\n        if permg_sig_fdr:\n            methods.append('perm')\n        if ty['significant']:\n            methods.append('ty')\n        \n        p = {\n            'canary': pair['canary'],\n            'downstream': pair['downstream'],\n            'perm_granger_fwd_p': round(permg['p_value'], 6),\n            'perm_granger_fwd_sig_fdr': permg_sig_fdr,\n            'perm_granger_rev_p': round(pair.get('reverse', {}).get('perm_granger', {}).get('p_value', 0), 6) if pair.get('reverse') else None,\n            'diff_xcorr_fwd_p': round(diff['p_value'], 6),\n            'diff_xcorr_fwd_r': round(diff['r'], 4),\n            'diff_xcorr_fwd_lag': diff['peak_lag'],\n            'diff_xcorr_fwd_sig_fdr': diffx_sig_fdr,\n            'threshold_onset_lead': threshold.get('lead_time'),\n            'threshold_onset_sig': threshold['significant'],\n            'ty_granger_p': round(ty['p_value'], 6),\n            'ty_granger_sig': ty['significant'],\n            'naive_xcorr_r': round(naive['r'], 4),\n            'naive_xcorr_lag': naive['peak_lag'],\n            'naive_xcorr_sig': naive['significant'],\n            'consensus_votes': len(methods),\n            'consensus_methods': methods\n        }\n        seed_entry['pairs'].append(p)\n    \n    seeds_data.append(seed_entry)\n\n# Summary\ntotal_pairs = sum(len(s['pairs']) for s in seeds_data)\nk_ge_3_per_seed = {}\npermg_fwd_per_seed = {}\nk_ge_3_permg_detail = []\n\nfor s in seeds_data:\n    sid = f's{s[\\\"seed\\\"]}'\n    k_ge_3_per_seed[sid] = sum(1 for p in s['pairs'] if p['consensus_votes'] >= 3)\n    permg_fwd_per_seed[sid] = sum(1 for p in s['pairs'] if p['perm_granger_fwd_sig_fdr'])\n    for p in s['pairs']:\n        if p['consensus_votes'] >= 3:\n            has_permg = 'perm' in p['consensus_methods']\n            k_ge_3_permg_detail.append({\n                'seed': s['seed'],\n                'pair': f\\\"{p['canary']}->{p['downstream']}\\\",\n                'methods': p['consensus_methods'],\n                'has_permg': has_permg\n            })\n\nk_ge_3_total = sum(k_ge_3_per_seed.values())\nk_ge_3_with_permg = sum(1 for d in k_ge_3_permg_detail if d['has_permg'])\n\nresult = {\n    'description': 'FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.',\n    'model': 'pythia-410m',\n    'alpha': 0.0,\n    'T': 10,\n    'n_perm': 5000,\n    'threshold_criterion': 'true_3sigma_d105',\n    'pair_basis': '6-pair (distinct_1/2/3 only, mauve excluded)',\n    'methods': [\n        'perm_granger (BH-FDR across 6 pairs)',\n        'diff_xcorr (BH-FDR across 6 pairs)',\n        'threshold_onset (true_3sigma_d105)',\n        'ty_granger (uncorrected)',\n        'naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)'\n    ],\n    'consensus_rule': 'K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.',\n    'summary': {\n        'total_seed_pairs': total_pairs,\n        'K_ge_3_count': k_ge_3_total,\n        'K_ge_3_fpr': round(k_ge_3_total / total_pairs, 4) if total_pairs > 0 else 0,\n        'per_seed_K_ge_3': k_ge_3_per_seed,\n        'K_ge_3_permg_breakdown': {\n            'with_permg': k_ge_3_with_permg,\n            'without_permg': k_ge_3_total - k_ge_3_with_permg,\n            'detail': '; '.join([f\\\"s{d['seed']} {d['pair']} [{','.join(d['methods'])}]\\\" for d in k_ge_3_permg_detail]) if k_ge_3_permg_detail else 'none'\n        },\n        'per_seed_permg_fwd_fdr': permg_fwd_per_seed\n    },\n    'seeds': seeds_data\n}\n\nwith open('/tmp/D102_null_s42_s44_fpr.json', 'w') as f:\n    json.dump(result, f, indent=2)\n\nprint('=== Summary ===')\nprint(f'Total pairs: {total_pairs}')\nprint(f'K>=3 count: {k_ge_3_total}, FPR: {k_ge_3_total/total_pairs:.4f}')\nprint(f'Per-seed K>=3: {k_ge_3_per_seed}')\nprint(f'Per-seed PermG FDR fwd: {permg_fwd_per_seed}')\nprint()\nfor s in seeds_data:\n    print(f\\\"--- s{s['seed']} ---\\\")\n    for p in s['pairs']:\n        print(f\\\"  {p['canary']}->{p['downstream']}: K={p['consensus_votes']} {p['consensus_methods']}  permg_p={p['perm_granger_fwd_p']:.4f} fdr={p['perm_granger_fwd_sig_fdr']}\\\")\nprint()\nprint('Saved /tmp/D102_null_s42_s44_fpr.json')\n\"\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-24T16:52:32.328770+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Encountered a bad command exit code!\\n\\nCommand: 'cd /root/autodl-tmp/distrib_canary_collapse && python3 -c \\\"\\\\nimport json\\\\nimport numpy as np\\\\n\\\\ndef bh_fdr(pvals):\\\\n    \\\\\\\\\\\"\\\\\\\\\\\"\\\\\\\\\\\"BH-FDR correction: returns adjusted p-values.\\\\\\\\\\\"\\\\\\\\\\\"\\\\\\\\\\\"\\\\n    n = len(pvals)\\\\n    order = np.argsort(pvals)\\\\n    adj = np.zeros(n)\\\\n    for i, rank in enumerate(range(1, n+1)):\\\\n        adj[order[i]] = pvals[order[i]] * n / rank\\\\n    # Enforce monotonicity (step-down)\\\\n    for i in range(n-2, -1, -1):\\\\n        adj[order[i]] = min(adj[order[i]], adj[order[i+1]] if i+1 < n else 1.0)\\\\n    return np.clip(adj, 0, 1).tolist()\\\\n\\\\nDISTINCT_DS = [\\\\'distinct_1\\\\', \\\\'distinct_2\\\\', \\\\'distinct_3\\\\']\\\\nseeds_data = []\\\\n\\\\nfor seed, dirname in [(42, \\\\'a000_s42\\\\'), (43, \\\\'a000_s43\\\\'), (44, \\\\'a000_s44\\\\')]:\\\\n    path = f\\\\'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json\\\\'\\\\n    with open(path) as f:\\\\n        data = json.load(f)\\\\n    \\\\n    # Filter to 6 pairs only\\\\n    filtered_pairs = [p for p in data[\\\\'pairs\\\\'] if p[\\\\'downstream\\\\'] in DISTINCT_DS]\\\\n    \\\\n    # Recompute BH-FDR across 6 pairs for permG and diff_xcorr\\\\n    permg_pvals = [p[\\\\'forward\\\\'][\\\\'perm_granger\\\\'][\\\\'p_value\\\\'] for p in filtered_pairs]\\\\n    diffx_pvals = [p[\\\\'forward\\\\'][\\\\'diff_xcorr\\\\'][\\\\'p_value\\\\'] for p in filtered_pairs]\\\\n    \\\\n    permg_fdr = bh_fdr(permg_pvals)\\\\n    diffx_fdr = bh_fdr(diffx_pvals)\\\\n    \\\\n    # Build consensus with corrected FDR\\\\n    seed_entry = {\\\\n        \\\\'seed\\\\': seed,\\\\n        \\\\'exp_dir\\\\': f\\\\'results/alpha_sweep/{dirname}\\\\',\\\\n        \\\\'T\\\\': 10,\\\\n        \\\\'n_gens\\\\': data[\\\\'meta\\\\'][\\\\'n_gens\\\\'],\\\\n        \\\\'n_perm\\\\': data[\\\\'meta\\\\'][\\\\'n
…[truncated 7163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-24T16:52:32.328993+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 << 'PYEOF'\nimport json\nimport numpy as np\n\ndef bh_fdr(pvals):\n    n = len(pvals)\n    order = np.argsort(pvals)\n    adj = np.zeros(n)\n    for i, rank in enumerate(range(1, n+1)):\n        adj[order[i]] = pvals[order[i]] * n / rank\n    for i in range(n-2, -1, -1):\n        adj[order[i]] = min(adj[order[i]], adj[order[i+1]] if i+1 < n else 1.0)\n    return np.clip(adj, 0, 1).tolist()\n\nDISTINCT_DS = ['distinct_1', 'distinct_2', 'distinct_3']\nseeds_data = []\n\nfor seed, dirname in [(42, 'a000_s42'), (43, 'a000_s43'), (44, 'a000_s44')]:\n    path = f'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json'\n    with open(path) as f:\n        data = json.load(f)\n    \n    filtered_pairs = [p for p in data['pairs'] if p['downstream'] in DISTINCT_DS]\n    \n    permg_pvals = [p['forward']['perm_granger']['p_value'] for p in filtered_pairs]\n    diffx_pvals = [p['forward']['diff_xcorr']['p_value'] for p in filtered_pairs]\n    \n    permg_fdr = bh_fdr(permg_pvals)\n    diffx_fdr = bh_fdr(diffx_pvals)\n    \n    seed_entry = {\n        'seed': seed,\n        'exp_dir': f'results/alpha_sweep/{dirname}',\n        'T': 10,\n        'n_gens': data['meta']['n_gens'],\n        'n_perm': data['meta']['n_perm'],\n        'pairs': []\n    }\n    \n    for i, pair in enumerate(filtered_pairs):\n        fwd = pair['forward']\n        \n        permg_sig_fdr = permg_fdr[i] < 0.05\n        diffx_sig_fdr = diffx_fdr[i] < 0.05\n        \n        naive = fwd['naive_xcorr']\n        diff = fwd['diff_xcorr']\n        threshold = fwd['threshold_onset']\n        permg = fwd['perm_granger']\n        ty = fwd['ty_granger']\n        \n        methods = []\n        if naive['significant'] and naive['peak_lag'] < 0:\n            methods.append('naive')\n        if diffx_sig_fdr and diff['peak_lag'] < 0:\n            methods.append('diff')\n        if threshold['significant']:\n            methods.append('threshold')\n        if permg_sig_fdr:\n            methods.append('perm')\n        if ty['significant']:\n            methods.append('ty')\n        \n        rev_permg_p = None\n        if 'reverse' in pair and 'perm_granger' in pair['reverse']:\n            rev_permg_p = round(pair['reverse']['perm_granger']['p_value'], 6)\n        \n        p = {\n            'canary': pair['canary'],\n            'downstream': pair['downstream'],\n            'perm_granger_fwd_p': round(permg['p_value'], 6),\n            'perm_granger_fwd_sig_fdr': permg_sig_fdr,\n            'perm_granger_rev_p': rev_permg_p,\n            'diff_xcorr_fwd_p': round(diff['p_value'], 6),\n            'diff_xcorr_fwd_r': round(diff['r'], 4),\n            'diff_xcorr_fwd_lag': diff['peak_lag'],\n            'diff_xcorr_fwd_sig_fdr': diffx_sig_fdr,\n            'threshold_onset_lead': threshold.get('lead_time'),\n            'threshold_onset_sig': threshold['significant'],\n            'ty_granger_p': round(ty['p_value'], 6),\n            'ty_granger_sig': ty['significant'],\n            'naive_xcorr_r': round(naive['r'], 4),\n            'naive_xcorr_lag': naive['peak_lag'],\n            'naive_xcorr_sig': naive['significant'],\n            'consensus_votes': len(methods),\n            'consensus_methods': methods\n        }\n        seed_entry['pairs'].append(p)\n    \n    seeds_data.append(seed_entry)\n\ntotal_pairs = sum(len(s['pairs']) for s in seeds_data)\nk_ge_3_per_seed = {}\npermg_fwd_per_seed = {}\nk_ge_3_permg_detail = []\n\nfor s in seeds_data:\n    sid = f\"s{s['seed']}\"\n    k_ge_3_per_seed[sid] = sum(1 for p in s['pairs'] if p['consensus_votes'] >= 3)\n    permg_fwd_per_seed[sid] = sum(1 for p in s['pairs'] if p['perm_granger_fwd_sig_fdr'])\n    for p in s['pairs']:\n        if p['consensus_votes'] >= 3:\n            has_permg = 'perm' in p['consensus_methods']\n            k_ge_3_permg_detail.append({\n                'seed': s['seed'],\n                'pair': f\"{p['canary']}->{p['downstream']}\",\n                'methods': p['consensus_methods'],\n                'has_permg': has_permg\n            })\n\nk_ge_3_total = sum(k_ge_3_per_seed.values())\nk_ge_3_with_permg = sum(1 for d in k_ge_3_permg_detail if d['has_permg'])\n\nresult = {\n    'description': 'FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.',\n    'model': 'pythia-410m',\n    'alpha': 0.0,\n    'T': 10,\n    'n_perm': 5000,\n    'threshold_criterion': 'true_3sigma_d105',\n    'pair_basis': '6-pair (distinct_1/2/3 only, mauve excluded)',\n    'methods': [\n        'perm_granger (BH-FDR across 6 pairs)',\n        'diff_xcorr (BH-FDR across 6 pairs)',\n        'threshold_onset (true_3sigma_d105)',\n        'ty_granger (uncorrected)',\n        'naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)'\n    ],\n    'consensus_rule': 'K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.',\n    'summary': {\n        'total_seed_pairs': total_pairs,\n        'K_ge_3_count': k_ge_3_total,\n        'K_ge_3_fpr': round(k_ge_3_total / total_pairs, 4) if total_pairs > 0 else 0,\n        'per_seed_K_ge_3': k_ge_3_per_seed,\n        'K_ge_3_permg_breakdown': {\n            'with_permg': k_ge_3_with_permg,\n            'without_permg': k_ge_3_total - k_ge_3_with_permg,\n            'detail': '; '.join([f\"s{d['seed']} {d['pair']} [{','.join(d['methods'])}]\" for d in k_ge_3_permg_detail]) if k_ge_3_permg_detail else 'none'\n        },\n        'per_seed_permg_fwd_fdr': permg_fwd_per_seed\n    },\n    'seeds': seeds_data\n}\n\nwith open('/tmp/D102_null_s42_s44_fpr.json', 'w') as f:\n    json.dump(result, f, indent=2)\n\nprint('=== Summary ===')\nprint(f'Total pairs: {total_pairs}')\nprint(f'K>=3 count: {k_ge_3_total}, FPR: {k_ge_3_total/total_pairs:.4f}')\nprint(f'Per-seed K>=3: {k_ge_3_per_seed}')\nprint(f'Per-seed PermG FDR fwd: {permg_fwd_per_seed}')\nprint()\nfor s in seeds_data:\n    print(f\"--- s{s['seed']} ---\")\n    for p in s['pairs']:\n        print(f\"  {p['canary']}->{p['downstream']}: K={p['consensus_votes']} {p['consensus_methods']}  permg_p={p['perm_granger_fwd_p']:.4f} fdr={p['perm_granger_fwd_sig_fdr']}\")\nprint()\nprint('Saved /tmp/D102_null_s42_s44_fpr.json')\nPYEOF\n",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/distrib_canary_collapse && python3 << 'PYEOF'\nimport json\nimport numpy as np\n\ndef bh_fdr(pvals):\n    n = len(pvals)\n    order = np.argsort(pvals)\n    adj = np.zeros(n)\n    for i, rank in enumerate(range(1, n+1)):\n        adj[order[i]] = pvals[order[i]] * n / rank\n    for i in range(n-2, -1, -1):\n        adj[order[i]] = min(adj[order[i]], adj[order[i+1]] if i+1 < n else 1.0)\n    return np.clip(adj, 0, 1).tolist()\n\nDISTINCT_DS = ['distinct_1', 'distinct_2', 'distinct_3']\nseeds_data = []\n\nfor seed, dirname in [(42, 'a000_s42'), (43, 'a000_s43'), (44, 'a000_s44')]:\n    path = f'results/alpha_sweep/{dirname}/analysis/5method_leadlag.json'\n    with open(path) as f:\n        data = json.load(f)\n    \n    filtered_pairs = [p for p in data['pairs'] if p['downstream'] in DISTINCT_DS]\n    \n    permg_pvals = [p['forward']['perm_granger']['p_value'] for p in filtered_pairs]\n    diffx_pvals = [p['forward']['diff_xcorr']['p_value'] for p in filtered_pairs]\n    \n    permg_fdr = bh_fdr(permg_pvals)\n    diffx_fdr = bh_fdr(diffx_pvals)\n    \n    seed_entry = {\n        'seed': seed,\n        'exp_dir': f'results/alpha_sweep/{dirname}',\n        'T': 10,\n        'n_gens': data['meta']['n_gens'],\n        'n_perm': data['meta']['n_perm'],\n        'pairs': []\n    }\n    \n    for i, pair in enumerate(filtered_pairs):\n        fwd = pair['forward']\n        \n        permg_sig_fdr = permg_fdr[i] < 0.05\n        diffx_sig_fdr = diffx_fdr[i] < 0.05\n        \n        naive = fwd['naive_xcorr']\n        diff = fwd['diff_xcorr']\n        threshold = fwd['threshold_onset']\n        permg = fwd['perm_granger']\n        ty = fwd['ty_granger']\n        \n        methods = []\n        if naive['significant'] and naive['peak_lag'] < 0:\n            methods.append('naive')\n        if diffx_sig_fdr and diff['peak_lag'] < 0:\n            methods.append('diff')\n        if threshold['significant']:\n            methods.append('threshold')\n        if permg_sig_fdr:\n            methods.append('perm')\n        if ty['significant']:\n            methods.append('ty')\n        \n        rev_permg_p = None\n        if 'reverse' in pair and 'perm_granger' in pair['reverse']:\n            rev_permg_p = round(pair['reverse']['perm_granger']['p_value'], 6)\n        \n        p = {\n            'canary': pair['canary'],\n            'downstream': pair['downstream'],\n            'perm_granger_fwd_p': round(permg['p_value'], 6),\n            'perm_granger_fwd_sig_fdr': permg_sig_fdr,\n            'perm_granger_rev_p': rev_permg_p,\n            'diff_xcorr_fwd_p': round(diff['p_value'], 6),\n            'diff_xcorr_fwd_r': round(diff['r'], 4),\n            'diff_xcorr_fwd_lag': diff['peak_lag'],\n            'diff_xcorr_fwd_sig_fdr': diffx_sig_fdr,\n            'threshold_onset_lead': threshold.get('lead_time'),\n            'threshold_onset_sig': threshold['significant'],\n            'ty_granger_p': round(ty['p_value'], 6),\n            'ty_granger_sig': ty['significant'],\n            'naive_xcorr_r': round(naive['r'], 4),\n            'naive_xcorr_lag': naive['peak_lag'],\n            'naive_xcorr_sig': naive['significant'],\n            'consensus_votes': len(methods),\n            'consensus_methods': methods\n        }\n        seed_entry['pairs'].append(p)\n    \n    seeds_data.append(seed_entry)\n\ntotal_pairs = sum(len(s['pairs']) for s in seeds_data)\nk_ge_3_per_seed = {}\npermg_fwd_per_seed = {}\nk_ge_3_permg_detail = []\n\nfor s in seeds_data:\n    sid = f\"s{s['seed']}\"\n    k_ge_3_per_seed[sid] = sum(1 for p in s['pairs'] if p['consensus_votes'] >= 3)\n    permg_fwd_per_seed[sid] = sum(1 for p in s['pairs'] if p['perm_granger_fwd_sig_fdr'])\n    for p in s['pairs']:\n        if p['consensus_votes'] >= 3:\n            has_permg = 'perm' in p['consensus_methods']\n            k_ge_3_permg_detail.append({\n                'seed': s['seed'],\n                'pair': f\"{p['canary']}->{p['downstream']}\",\n                'methods': p['consensus_methods'],\n                'has_permg': has_permg\n            })\n\nk_ge_3_total = sum(k_ge_3_per_seed.values())\nk_ge_3_with_permg = sum(1 for d in k_ge_3_permg_detail if d['has_permg'])\n\nresult = {\n    'description': 'FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.',\n    'model': 'pythia-410m',\n    'alpha': 0.0,\n    'T': 10,\n    'n_perm': 5000,\n    'threshold_criterion': 'true_3sigma_d105',\n    'pair_basis': '6-pair (distinct_1/2/3 only, mauve excluded)',\n    'methods': [\n        'perm_granger (BH-FDR across 6 pairs)',\n        'diff_xcorr (BH-FDR across 6 pairs)',\n        'threshold_onset (true_3sigma_d105)',\n        'ty_granger (uncorrected)',\n        'naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)'\n    ],\n    'consensus_rule': 'K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.',\n    'summary': {\n        'total_seed_pairs': total_pairs,\n        'K_ge_3_count': k_ge_3_total,\n        'K_ge_3_fpr': round(k_ge_3_total / total_pairs, 4) if total_pairs > 0 else 0,\n        'per_seed_K_ge_3': k_ge_3_per_seed,\n        'K_ge_3_permg_breakdown': {\n            'with_permg': k_ge_3_with_permg,\n            'without_permg': k_ge_3_total - k_ge_3_with_permg,\n            'detail': '; '.join([f\"s{d['seed']} {d['pair']} [{','.join(d['methods'])}]\" for d in k_ge_3_permg_detail]) if k_ge_3_permg_detail else 'none'\n        },\n        'per_seed_permg_fwd_fdr': permg_fwd_per_seed\n    },\n    'seeds': seeds_data\n}\n\nwith open('/tmp/D102_null_s42_s44_fpr.json', 'w') as f:\n    json.dump(result, f, indent=2)\n\nprint('=== Summary ===')\nprint(f'Total pairs: {total_pairs}')\nprint(f'K>=3 count: {k_ge_3_total}, FPR: {k_ge_3_total/total_pairs:.4f}')\nprint(f'Per-seed K>=3: {k_ge_3_per_seed}')\nprint(f'Per-seed PermG FDR fwd: {permg_fwd_per_seed}')\nprint()\nfor s in seeds_data:\n    print(f\"--- s{s['seed']} ---\")\n    for p in s['pairs']:\n        print(f\"  {p['canary']}->{p['downstream']}: K={p['consensus_votes']} {p['consensus_methods']}  permg_p={p['perm_granger_fwd_p']:.4f} fdr={p['perm_granger_fwd_sig_fdr']}\")\nprint()\nprint('Saved /tmp/D102_null_s42_s44_fpr.json')\nPYEOF\n",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-24T16:52:32.329224+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"=== Summary ===\\nTotal pairs: 18\\nK>=3 count: 0, FPR: 0.0000\\nPer-seed K>=3: {'s42': 0, 's43': 0, 's44': 0}\\nPer-seed PermG FDR fwd: {'s42': 0, 's43': 0, 's44': 0}\\n\\n--- s42 ---\\n  token_entropy->distinct_1: K=2 ['naive', 'diff']  permg_p=0.0514 fdr=False\\n  token_entropy->distinct_2: K=2 ['diff', 'threshold']  permg_p=0.0804 fdr=False\\n  token_entropy->distinct_3: K=2 ['diff', 'threshold']  permg_p=0.0756 fdr=False\\n  ece->distinct_1: K=2 ['naive', 'ty']  permg_p=0.9498 fdr=False\\n  ece->distinct_2: K=0 []  permg_p=0.5443 fdr=False\\n  ece->distinct_3: K=1 ['ty']  permg_p=0.3715 fdr=False\\n--- s43 ---\\n  token_entropy->distinct_1: K=1 ['ty']  permg_p=0.0796 fdr=False\\n  token_entropy->distinct_2: K=1 ['diff']  permg_p=0.0702 fdr=False\\n  token_entropy->distinct_3: K=1 ['diff']  permg_p=0.0344 fdr=False\\n  ece->distinct_1: K=1 ['ty']  permg_p=0.5163 fdr=False\\n  ece->distinct_2: K=0 []  permg_p=0.8780 fdr=False\\n  ece->distinct_3: K=0 []  permg_p=0.5755 fdr=False\\n--- s44 ---\\n  token_entropy->distinct_1: K=2 ['naive', 'diff']  permg_p=0.0692 fdr=False\\n  token_entropy->distinct_2: K=2 ['naive', 'diff']  permg_p=0.0300 fdr=False\\n  token_entropy->distinct_3: K=2 ['naive', 'threshold']  permg_p=0.0316 fdr=False\\n  ece->distinct_1: K=0 []  permg_p=0.3743 fdr=False\\n  ece->distinct_2: K=0 []  permg_p=0.8866 fdr=False\\n  ece->distinct_3: K=0 []  permg_p=0.2597 fdr=False\\n\\nSaved /tmp/D102_null_s42_s44_fpr.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.09}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-24T16:52:32.329434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "wc -c /tmp/D102_null_s42_s44_fpr.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "wc -c /tmp/D102_null_s42_s44_fpr.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-24T16:52:32.329583+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"14767 /tmp/D102_null_s42_s44_fpr.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-24T16:52:32.329716+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -200 /tmp/D102_null_s42_s44_fpr.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -200 /tmp/D102_null_s42_s44_fpr.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-24T16:52:32.329966+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.\\\",\\n  \\\"model\\\": \\\"pythia-410m\\\",\\n  \\\"alpha\\\": 0.0,\\n  \\\"T\\\": 10,\\n  \\\"n_perm\\\": 5000,\\n  \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\",\\n  \\\"pair_basis\\\": \\\"6-pair (distinct_1/2/3 only, mauve excluded)\\\",\\n  \\\"methods\\\": [\\n    \\\"perm_granger (BH-FDR across 6 pairs)\\\",\\n    \\\"diff_xcorr (BH-FDR across 6 pairs)\\\",\\n    \\\"threshold_onset (true_3sigma_d105)\\\",\\n    \\\"ty_granger (uncorrected)\\\",\\n    \\\"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\\\"\\n  ],\\n  \\\"consensus_rule\\\": \\\"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\\\",\\n  \\\"summary\\\": {\\n    \\\"total_seed_pairs\\\": 18,\\n    \\\"K_ge_3_count\\\": 0,\\n    \\\"K_ge_3_fpr\\\": 0.0,\\n    \\\"per_seed_K_ge_3\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    },\\n    \\\"K_ge_3_permg_breakdown\\\": {\\n      \\\"with_permg\\\": 0,\\n      \\\"without_permg\\\": 0,\\n      \\\"detail\\\": \\\"none\\\"\\n    },\\n    \\\"per_seed_permg_fwd_fdr\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    }\\n  },\\n  \\\"seeds\\\": [\\n    {\\n      \\\"seed\\\": 42,\\n      \\\"exp_dir\\\": \\\"results/alpha_sweep/a000_s42\\\",\\n      \\\"T\\\": 10,\\n      \\\"n_gens\\\": 11,\\n      \\\"n_perm\\\": 5000,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"canary\\\": \\\"token_entropy\\\",\\n          \\\"downstream\\\": \\\"distinct_1\\\",\\n          \\\"perm_granger
…[truncated 6205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-24T16:52:32.330157+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -200 /tmp/D102_null_s42_s44_fpr.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -200 /tmp/D102_null_s42_s44_fpr.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T16:52:32.330316+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "tail -n +201 /tmp/D102_null_s42_s44_fpr.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "tail -n +201 /tmp/D102_null_s42_s44_fpr.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T16:52:32.330577+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.\\\",\\n  \\\"model\\\": \\\"pythia-410m\\\",\\n  \\\"alpha\\\": 0.0,\\n  \\\"T\\\": 10,\\n  \\\"n_perm\\\": 5000,\\n  \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\",\\n  \\\"pair_basis\\\": \\\"6-pair (distinct_1/2/3 only, mauve excluded)\\\",\\n  \\\"methods\\\": [\\n    \\\"perm_granger (BH-FDR across 6 pairs)\\\",\\n    \\\"diff_xcorr (BH-FDR across 6 pairs)\\\",\\n    \\\"threshold_onset (true_3sigma_d105)\\\",\\n    \\\"ty_granger (uncorrected)\\\",\\n    \\\"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\\\"\\n  ],\\n  \\\"consensus_rule\\\": \\\"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\\\",\\n  \\\"summary\\\": {\\n    \\\"total_seed_pairs\\\": 18,\\n    \\\"K_ge_3_count\\\": 0,\\n    \\\"K_ge_3_fpr\\\": 0.0,\\n    \\\"per_seed_K_ge_3\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    },\\n    \\\"K_ge_3_permg_breakdown\\\": {\\n      \\\"with_permg\\\": 0,\\n      \\\"without_permg\\\": 0,\\n      \\\"detail\\\": \\\"none\\\"\\n    },\\n    \\\"per_seed_permg_fwd_fdr\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    }\\n  },\\n  \\\"seeds\\\": [\\n    {\\n      \\\"seed\\\": 42,\\n      \\\"exp_dir\\\": \\\"results/alpha_sweep/a000_s42\\\",\\n      \\\"T\\\": 10,\\n      \\\"n_gens\\\": 11,\\n      \\\"n_perm\\\": 5000,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"canary\\\": \\\"token_entropy\\\",\\n          \\\"downstream\\\": \\\"distinct_1\\\",\\n          \\\"perm_granger
…[truncated 6205 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-24T16:52:32.330939+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"          \\\"ty_granger_sig\\\": true,\\n          \\\"naive_xcorr_r\\\": -0.9029,\\n          \\\"naive_xcorr_lag\\\": 1,\\n          \\\"naive_xcorr_sig\\\": true,\\n          \\\"consensus_votes\\\": 1,\\n          \\\"consensus_methods\\\": [\\n            \\\"ty\\\"\\n          ]\\n        },\\n        {\\n          \\\"canary\\\": \\\"token_entropy\\\",\\n          \\\"downstream\\\": \\\"distinct_2\\\",\\n          \\\"perm_granger_fwd_p\\\": 0.070186,\\n          \\\"perm_granger_fwd_sig_fdr\\\": false,\\n          \\\"perm_granger_rev_p\\\": 0.030394,\\n          \\\"diff_xcorr_fwd_p\\\": 0.000594,\\n          \\\"diff_xcorr_fwd_r\\\": 0.9127,\\n          \\\"diff_xcorr_fwd_lag\\\": -1,\\n          \\\"diff_xcorr_fwd_sig_fdr\\\": true,\\n          \\\"threshold_onset_lead\\\": null,\\n          \\\"threshold_onset_sig\\\": false,\\n          \\\"ty_granger_p\\\": 0.4004,\\n          \\\"ty_granger_sig\\\": false,\\n          \\\"naive_xcorr_r\\\": -0.9162,\\n          \\\"naive_xcorr_lag\\\": 1,\\n          \\\"naive_xcorr_sig\\\": true,\\n          \\\"consensus_votes\\\": 1,\\n          \\\"consensus_methods\\\": [\\n            \\\"diff\\\"\\n          ]\\n        },\\n        {\\n          \\\"canary\\\": \\\"token_entropy\\\",\\n          \\\"downstream\\\": \\\"distinct_3\\\",\\n          \\\"perm_granger_fwd_p\\\": 0.034393,\\n          \\\"perm_granger_fwd_sig_fdr\\\": false,\\n          \\\"perm_granger_rev_p\\\": 0.088782,\\n          \\\"diff_xcorr_fwd_p\\\": 0.000713,\\n          \\\"diff_xcorr_fwd_r\\\": 0.9079,\\n          \\\"diff_xcorr_fwd_lag\\\": -1,\\n          \\\"diff_xcorr_fwd_sig_fdr\\\": true,\\n          \\\"threshold_onset_lead\\\": null,\\n          \\\"threshold_onset_sig\\\": false,\\n          \\\"ty_granger_p\\\": 0.8147,\\n          \\\"ty_granger_sig\\\": false,\\n          \\\"naive_xcorr_r\\\": -0.8943,\\n          \\\"naive_xcorr_lag\\\": 1,\\n          \\\"naive_xc
…[truncated 8106 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-24T16:52:32.331182+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /tmp/D102_null_s42_s44_fpr.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /tmp/D102_null_s42_s44_fpr.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-24T16:52:32.331544+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"description\\\": \\\"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.\\\",\\n  \\\"model\\\": \\\"pythia-410m\\\",\\n  \\\"alpha\\\": 0.0,\\n  \\\"T\\\": 10,\\n  \\\"n_perm\\\": 5000,\\n  \\\"threshold_criterion\\\": \\\"true_3sigma_d105\\\",\\n  \\\"pair_basis\\\": \\\"6-pair (distinct_1/2/3 only, mauve excluded)\\\",\\n  \\\"methods\\\": [\\n    \\\"perm_granger (BH-FDR across 6 pairs)\\\",\\n    \\\"diff_xcorr (BH-FDR across 6 pairs)\\\",\\n    \\\"threshold_onset (true_3sigma_d105)\\\",\\n    \\\"ty_granger (uncorrected)\\\",\\n    \\\"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\\\"\\n  ],\\n  \\\"consensus_rule\\\": \\\"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\\\",\\n  \\\"summary\\\": {\\n    \\\"total_seed_pairs\\\": 18,\\n    \\\"K_ge_3_count\\\": 0,\\n    \\\"K_ge_3_fpr\\\": 0.0,\\n    \\\"per_seed_K_ge_3\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    },\\n    \\\"K_ge_3_permg_breakdown\\\": {\\n      \\\"with_permg\\\": 0,\\n      \\\"without_permg\\\": 0,\\n      \\\"detail\\\": \\\"none\\\"\\n    },\\n    \\\"per_seed_permg_fwd_fdr\\\": {\\n      \\\"s42\\\": 0,\\n      \\\"s43\\\": 0,\\n      \\\"s44\\\": 0\\n    }\\n  },\\n  \\\"seeds\\\": [\\n    {\\n      \\\"seed\\\": 42,\\n      \\\"exp_dir\\\": \\\"results/alpha_sweep/a000_s42\\\",\\n      \\\"T\\\": 10,\\n      \\\"n_gens\\\": 11,\\n      \\\"n_perm\\\": 5000,\\n      \\\"pairs\\\": [\\n        {\\n          \\\"canary\\\": \\\"token_entropy\\\",\\n          \\\"downstream\\\": \\\"distinct_1\\\",\\n          \\\"perm_granger
…[truncated 8101 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-24T16:52:32.331844+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "D102_null_s42_s44_fpr",
  "type": "data",
  "description": "FPR transparency: 3 null seeds (s42-s44) 6-pair D102 analysis. BH-FDR recomputed across 6 pairs. K>=3 FPR = 0/18, PermG FPR = 0/18.",
  "project": "distrib_canary_collapse",
  "content": "{\n  \"description\": \"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.\",\n  \"model\": \"pythia-410m\",\n  \"alpha\": 0.0,\n  \"T\": 10,\n  \"n_perm\": 5000,\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"pair_basis\": \"6-pair (distinct_1/2/3 only, mauve excluded)\",\n  \"methods\": [\n    \"perm_granger (BH-FDR across 6 pairs)\",\n    \"diff_xcorr (BH-FDR across 6 pairs)\",\n    \"threshold_onset (true_3sigma_d105)\",\n    \"ty_granger (uncorrected)\",\n    \"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\"\n  ],\n  \"consensus_rule\": \"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\",\n  \"summary\": {\n    \"total_seed_pairs\": 18,\n    \"K_ge_3_count\": 0,\n    \"K_ge_3_fpr\": 0.0,\n    \"per_seed_K_ge_3\": {\n      \"s42\": 0,\n      \"s43\": 0,\n      \"s44\": 0\n    },\n    \"K_ge_3_permg_breakdown\": {\n      \"with_permg\": 0,\n      \"without_permg\": 0,\n      \"detail\": \"none\"\n    },\n    \"per_seed_permg_fwd_fdr\": {\n      \"s42\": 0,\n      \"s43\": 0,\n      \"s44\": 0\n    }\n  },\n  \"seeds\": [\n    {\n      \"seed\": 42,\n      \"exp_dir\": \"results/alpha_sweep/a000_s42\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.05139,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.795641,\n          \"diff_xcorr_fwd_p\": 0.000157,\n          \"diff_xcorr_fwd_r\": 0.9408,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.7587,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9023,\n          \"naive_xcorr_lag\": -5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.080384,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.978204,\n          \"diff_xcorr_fwd_p\": 0.009707,\n          \"diff_xcorr_fwd_r\": 0.9184,\n          \"diff_xcorr_fwd_lag\": -4,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.4974,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8262,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"diff\", \"threshold\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.075585,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.985403,\n          \"diff_xcorr_fwd_p\": 0.01191,\n          \"diff_xcorr_fwd_r\": 0.9095,\n          \"diff_xcorr_fwd_lag\": -4,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.9989,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8161,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"diff\", \"threshold\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.94981,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.343131,\n          \"diff_xcorr_fwd_p\": 0.051439,\n          \"diff_xcorr_fwd_r\": -0.7037,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.017,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8166,\n          \"naive_xcorr_lag\": -4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"ty\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.544291,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.353929,\n          \"diff_xcorr_fwd_p\": 0.192837,\n          \"diff_xcorr_fwd_r\": -0.5137,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.565,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7783,\n          \"naive_xcorr_lag\": 4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.371526,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.211758,\n          \"diff_xcorr_fwd_p\": 0.202654,\n          \"diff_xcorr_fwd_r\": 0.5482,\n          \"diff_xcorr_fwd_lag\": -3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.0003,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8257,\n          \"naive_xcorr_lag\": 4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        }\n      ]\n    },\n    {\n      \"seed\": 43,\n      \"exp_dir\": \"results/alpha_sweep/a000_s43\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.079584,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.059788,\n          \"diff_xcorr_fwd_p\": 0.085352,\n          \"diff_xcorr_fwd_r\": -0.7509,\n          \"diff_xcorr_fwd_lag\": 4,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.0076,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.9029,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.070186,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.030394,\n          \"diff_xcorr_fwd_p\": 0.000594,\n          \"diff_xcorr_fwd_r\": 0.9127,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.4004,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.9162,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.034393,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.088782,\n          \"diff_xcorr_fwd_p\": 0.000713,\n          \"diff_xcorr_fwd_r\": 0.9079,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.8147,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8943,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"diff\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.516297,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.472905,\n          \"diff_xcorr_fwd_p\": 0.163821,\n          \"diff_xcorr_fwd_r\": 0.5435,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.026,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8517,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.878024,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.282344,\n          \"diff_xcorr_fwd_p\": 0.260901,\n          \"diff_xcorr_fwd_r\": 0.6237,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.3364,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8123,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.575485,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.214557,\n          \"diff_xcorr_fwd_p\": 0.167261,\n          \"diff_xcorr_fwd_r\": 0.7233,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6744,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7685,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    },\n    {\n      \"seed\": 44,\n      \"exp_dir\": \"results/alpha_sweep/a000_s44\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.069186,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.184496,\n          \"diff_xcorr_fwd_p\": 0.005749,\n          \"diff_xcorr_fwd_r\": 0.9715,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.1862,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9144,\n          \"naive_xcorr_lag\": -5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.029994,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.086983,\n          \"diff_xcorr_fwd_p\": 0.000244,\n          \"diff_xcorr_fwd_r\": 0.9327,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.2306,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8517,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.031594,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.260948,\n          \"diff_xcorr_fwd_p\": 0.044792,\n          \"diff_xcorr_fwd_r\": 0.6779,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.8199,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8241,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"threshold\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.374325,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.14997,\n          \"diff_xcorr_fwd_p\": 0.042819,\n          \"diff_xcorr_fwd_r\": 0.8904,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6129,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8186,\n          \"naive_xcorr_lag\": 5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.886623,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.443711,\n          \"diff_xcorr_fwd_p\": 0.060923,\n          \"diff_xcorr_fwd_r\": 0.861,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.1696,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7374,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.259748,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.778444,\n          \"diff_xcorr_fwd_p\": 0.324673,\n          \"diff_xcorr_fwd_r\": 0.5615,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6238,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.6898,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    }\n  ]\n}",
  "content_filename": "D102_null_s42_s44_fpr.json",
  "tags": "['fpr', 'null', 'd102', '6pair']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "D102_null_s42_s44_fpr",
    "type": "data",
    "description": "FPR transparency: 3 null seeds (s42-s44) 6-pair D102 analysis. BH-FDR recomputed across 6 pairs. K>=3 FPR = 0/18, PermG FPR = 0/18.",
    "project": "distrib_canary_collapse",
    "content": "{\n  \"description\": \"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.\",\n  \"model\": \"pythia-410m\",\n  \"alpha\": 0.0,\n  \"T\": 10,\n  \"n_perm\": 5000,\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"pair_basis\": \"6-pair (distinct_1/2/3 only, mauve excluded)\",\n  \"methods\": [\n    \"perm_granger (BH-FDR across 6 pairs)\",\n    \"diff_xcorr (BH-FDR across 6 pairs)\",\n    \"threshold_onset (true_3sigma_d105)\",\n    \"ty_granger (uncorrected)\",\n    \"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\"\n  ],\n  \"consensus_rule\": \"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\",\n  \"summary\": {\n    \"total_seed_pairs\": 18,\n    \"K_ge_3_count\": 0,\n    \"K_ge_3_fpr\": 0.0,\n    \"per_seed_K_ge_3\": {\n      \"s42\": 0,\n      \"s43\": 0,\n      \"s44\": 0\n    },\n    \"K_ge_3_permg_breakdown\": {\n      \"with_permg\": 0,\n      \"without_permg\": 0,\n      \"detail\": \"none\"\n    },\n    \"per_seed_permg_fwd_fdr\": {\n      \"s42\": 0,\n      \"s43\": 0,\n      \"s44\": 0\n    }\n  },\n  \"seeds\": [\n    {\n      \"seed\": 42,\n      \"exp_dir\": \"results/alpha_sweep/a000_s42\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.05139,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.795641,\n          \"diff_xcorr_fwd_p\": 0.000157,\n          \"diff_xcorr_fwd_r\": 0.9408,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.7587,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9023,\n          \"naive_xcorr_lag\": -5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.080384,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.978204,\n          \"diff_xcorr_fwd_p\": 0.009707,\n          \"diff_xcorr_fwd_r\": 0.9184,\n          \"diff_xcorr_fwd_lag\": -4,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.4974,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8262,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"diff\", \"threshold\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.075585,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.985403,\n          \"diff_xcorr_fwd_p\": 0.01191,\n          \"diff_xcorr_fwd_r\": 0.9095,\n          \"diff_xcorr_fwd_lag\": -4,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.9989,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8161,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"diff\", \"threshold\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.94981,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.343131,\n          \"diff_xcorr_fwd_p\": 0.051439,\n          \"diff_xcorr_fwd_r\": -0.7037,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.017,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8166,\n          \"naive_xcorr_lag\": -4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"ty\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.544291,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.353929,\n          \"diff_xcorr_fwd_p\": 0.192837,\n          \"diff_xcorr_fwd_r\": -0.5137,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.565,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7783,\n          \"naive_xcorr_lag\": 4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.371526,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.211758,\n          \"diff_xcorr_fwd_p\": 0.202654,\n          \"diff_xcorr_fwd_r\": 0.5482,\n          \"diff_xcorr_fwd_lag\": -3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.0003,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8257,\n          \"naive_xcorr_lag\": 4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        }\n      ]\n    },\n    {\n      \"seed\": 43,\n      \"exp_dir\": \"results/alpha_sweep/a000_s43\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.079584,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.059788,\n          \"diff_xcorr_fwd_p\": 0.085352,\n          \"diff_xcorr_fwd_r\": -0.7509,\n          \"diff_xcorr_fwd_lag\": 4,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.0076,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.9029,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.070186,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.030394,\n          \"diff_xcorr_fwd_p\": 0.000594,\n          \"diff_xcorr_fwd_r\": 0.9127,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.4004,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.9162,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.034393,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.088782,\n          \"diff_xcorr_fwd_p\": 0.000713,\n          \"diff_xcorr_fwd_r\": 0.9079,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.8147,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8943,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"diff\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.516297,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.472905,\n          \"diff_xcorr_fwd_p\": 0.163821,\n          \"diff_xcorr_fwd_r\": 0.5435,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.026,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8517,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.878024,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.282344,\n          \"diff_xcorr_fwd_p\": 0.260901,\n          \"diff_xcorr_fwd_r\": 0.6237,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.3364,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8123,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.575485,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.214557,\n          \"diff_xcorr_fwd_p\": 0.167261,\n          \"diff_xcorr_fwd_r\": 0.7233,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6744,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7685,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    },\n    {\n      \"seed\": 44,\n      \"exp_dir\": \"results/alpha_sweep/a000_s44\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.069186,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.184496,\n          \"diff_xcorr_fwd_p\": 0.005749,\n          \"diff_xcorr_fwd_r\": 0.9715,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.1862,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9144,\n          \"naive_xcorr_lag\": -5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.029994,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.086983,\n          \"diff_xcorr_fwd_p\": 0.000244,\n          \"diff_xcorr_fwd_r\": 0.9327,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.2306,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8517,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.031594,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.260948,\n          \"diff_xcorr_fwd_p\": 0.044792,\n          \"diff_xcorr_fwd_r\": 0.6779,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.8199,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8241,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"threshold\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.374325,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.14997,\n          \"diff_xcorr_fwd_p\": 0.042819,\n          \"diff_xcorr_fwd_r\": 0.8904,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6129,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8186,\n          \"naive_xcorr_lag\": 5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.886623,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.443711,\n          \"diff_xcorr_fwd_p\": 0.060923,\n          \"diff_xcorr_fwd_r\": 0.861,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.1696,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7374,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.259748,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.778444,\n          \"diff_xcorr_fwd_p\": 0.324673,\n          \"diff_xcorr_fwd_r\": 0.5615,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6238,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.6898,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    }\n  ]\n}",
    "content_filename": "D102_null_s42_s44_fpr.json",
    "tags": "['fpr', 'null', 'd102', '6pair']"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-24T16:52:32.332126+00:00_

Error executing tool register_artifact: 1 validation error for register_artifactArguments
content
  Input should be a valid string [type=string_type, input_value={'description': 'FPR tran...sensus_methods': []}]}]}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-24T16:52:32.332303+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/",
    "description": "List artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-24T16:52:32.332537+00:00_

A2_naive_baseline_comparison.json
D040
D102_14b_t10_a045_s42_fp32_14b_6pair.json
D102_14b_t10_a045_s42_fp32_d3.json
D102_14b_t10_a045_s44_fp32_14b_6pair.json
D102_14b_t10_a050_s42_fp32_14b_6pair.json
D102_14b_t10_a050_s43_fp32.json
D102_14b_t10_a050_s44_fp32_14b_6pair.json
D102_14b_t10_a050_s44_fp32_d3.json
D102_14b_t10_a060_s42_fp32.json
D102_14b_t10_a060_s42_fp32_14b_6pair.json
D102_14b_t10_a060_s44_fp32_14b_6pair.json
D102_14b_t10_a060_s44_fp32_d3.json
D102_14b_t10_a075_s42_fp32_14b_6pair.json
D102_14b_t10_a075_s44_fp32_14b_6pair.json
D102_14b_t10_a075_s44_fp32_d3.json
D102_14b_t15_a045_s42_fp32_14b_6pair.json
D102_14b_t15_a045_s43_fp32_14b_6pair.json
D102_14b_t15_a045_s43_fp32_d3.json
D102_14b_t15_a050_s42_fp32_14b_6pair.json
D102_14b_t15_a050_s43_fp32_14b_6pair.json
D102_14b_t15_a050_s43_fp32_d3.json
D102_14b_t15_a060_s42_fp32_14b_6pair.json
D102_14b_t15_a060_s42_fp32_v2.json
D102_14b_t15_a060_s43_fp32.json
D102_14b_t15_a060_s43_fp32_14b_6pair.json
D102_14b_t15_a060_s43_fp32_d3.json
D102_14b_t15_a075_s42_fp32.json
D102_14b_t15_a075_s42_fp32_14b_6pair.json
D102_14b_t15_a075_s43_fp32_14b_6pair.json
D102_gpt2m_null_s42_fp32_d3.json
D102_gpt2m_null_s43_fp32_d3.json
D102_null_s46_fp32_d3.json
D102_null_s48_fp32_d3.json
D102_null_s49_fp32_d3.json
D102_null_s50_fp32_d3.json
D102_t10_a075_s43_analysis.md
D102_t10_a075_s43_fp32_analysis.md
D102_t25_a060_s42_fp32_v3.json
D102_t25_a060_v3_analysis.md
D105_3sigma_recompute_combined.json
D170_narrative_drafts.md
D170_t25_absorption_plan.md
D213_14b_s42_6pair_combined.json
D213_14b_s42_6pair_combined_v2.json
D213_14b_s43_t10_6pair_combined.json
_project
a050_fp32_3seed_5method_analysis.md
a050_fp32_3seed_metrics_summary.md
a050_s44_draft_versions.tex
a065_s42_fp32_5method.json
a075_analysis_prep.md
alpha_c_theory
alpha_sweep
alpha_sweep_a000_s43
alpha_sweep_a000_s44
alpha_sweep_a000_s45_fp32
alpha_sweep_a000_s47_fp32
alpha_sweep_a000_s48_fp32
alpha_sweep_a005_s42
alpha_sweep_a010_s42_v2
alpha_sweep_a010_s43
alpha_sweep_a010_
…[truncated 7616 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-24T16:52:32.332785+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D102_null_s42_s44_fpr.json",
  "content": "{\n  \"description\": \"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.\",\n  \"model\": \"pythia-410m\",\n  \"alpha\": 0.0,\n  \"T\": 10,\n  \"n_perm\": 5000,\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"pair_basis\": \"6-pair (distinct_1/2/3 only, mauve excluded)\",\n  \"methods\": [\n    \"perm_granger (BH-FDR across 6 pairs)\",\n    \"diff_xcorr (BH-FDR across 6 pairs)\",\n    \"threshold_onset (true_3sigma_d105)\",\n    \"ty_granger (uncorrected)\",\n    \"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\"\n  ],\n  \"consensus_rule\": \"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\",\n  \"summary\": {\n    \"total_seed_pairs\": 18,\n    \"K_ge_3_count\": 0,\n    \"K_ge_3_fpr\": 0.0,\n    \"per_seed_K_ge_3\": {\n      \"s42\": 0,\n      \"s43\": 0,\n      \"s44\": 0\n    },\n    \"K_ge_3_permg_breakdown\": {\n      \"with_permg\": 0,\n      \"without_permg\": 0,\n      \"detail\": \"none\"\n    },\n    \"per_seed_permg_fwd_fdr\": {\n      \"s42\": 0,\n      \"s43\": 0,\n      \"s44\": 0\n    }\n  },\n  \"seeds\": [\n    {\n      \"seed\": 42,\n      \"exp_dir\": \"results/alpha_sweep/a000_s42\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.05139,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.795641,\n          \"diff_xcorr_fwd_p\": 0.000157,\n          \"diff_xcorr_fwd_r\": 0.9408,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.7587,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9023,\n          \"naive_xcorr_lag\": -5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.080384,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.978204,\n          \"diff_xcorr_fwd_p\": 0.009707,\n          \"diff_xcorr_fwd_r\": 0.9184,\n          \"diff_xcorr_fwd_lag\": -4,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.4974,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8262,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"diff\", \"threshold\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.075585,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.985403,\n          \"diff_xcorr_fwd_p\": 0.01191,\n          \"diff_xcorr_fwd_r\": 0.9095,\n          \"diff_xcorr_fwd_lag\": -4,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.9989,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8161,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"diff\", \"threshold\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.94981,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.343131,\n          \"diff_xcorr_fwd_p\": 0.051439,\n          \"diff_xcorr_fwd_r\": -0.7037,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.017,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8166,\n          \"naive_xcorr_lag\": -4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"ty\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.544291,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.353929,\n          \"diff_xcorr_fwd_p\": 0.192837,\n          \"diff_xcorr_fwd_r\": -0.5137,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.565,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7783,\n          \"naive_xcorr_lag\": 4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.371526,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.211758,\n          \"diff_xcorr_fwd_p\": 0.202654,\n          \"diff_xcorr_fwd_r\": 0.5482,\n          \"diff_xcorr_fwd_lag\": -3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.0003,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8257,\n          \"naive_xcorr_lag\": 4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        }\n      ]\n    },\n    {\n      \"seed\": 43,\n      \"exp_dir\": \"results/alpha_sweep/a000_s43\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.079584,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.059788,\n          \"diff_xcorr_fwd_p\": 0.085352,\n          \"diff_xcorr_fwd_r\": -0.7509,\n          \"diff_xcorr_fwd_lag\": 4,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.0076,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.9029,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.070186,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.030394,\n          \"diff_xcorr_fwd_p\": 0.000594,\n          \"diff_xcorr_fwd_r\": 0.9127,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.4004,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.9162,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.034393,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.088782,\n          \"diff_xcorr_fwd_p\": 0.000713,\n          \"diff_xcorr_fwd_r\": 0.9079,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.8147,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8943,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"diff\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.516297,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.472905,\n          \"diff_xcorr_fwd_p\": 0.163821,\n          \"diff_xcorr_fwd_r\": 0.5435,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.026,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8517,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.878024,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.282344,\n          \"diff_xcorr_fwd_p\": 0.260901,\n          \"diff_xcorr_fwd_r\": 0.6237,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.3364,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8123,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.575485,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.214557,\n          \"diff_xcorr_fwd_p\": 0.167261,\n          \"diff_xcorr_fwd_r\": 0.7233,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6744,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7685,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    },\n    {\n      \"seed\": 44,\n      \"exp_dir\": \"results/alpha_sweep/a000_s44\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.069186,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.184496,\n          \"diff_xcorr_fwd_p\": 0.005749,\n          \"diff_xcorr_fwd_r\": 0.9715,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.1862,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9144,\n          \"naive_xcorr_lag\": -5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.029994,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.086983,\n          \"diff_xcorr_fwd_p\": 0.000244,\n          \"diff_xcorr_fwd_r\": 0.9327,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.2306,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8517,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.031594,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.260948,\n          \"diff_xcorr_fwd_p\": 0.044792,\n          \"diff_xcorr_fwd_r\": 0.6779,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.8199,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8241,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"threshold\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.374325,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.14997,\n          \"diff_xcorr_fwd_p\": 0.042819,\n          \"diff_xcorr_fwd_r\": 0.8904,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6129,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8186,\n          \"naive_xcorr_lag\": 5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.886623,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.443711,\n          \"diff_xcorr_fwd_p\": 0.060923,\n          \"diff_xcorr_fwd_r\": 0.861,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.1696,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7374,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.259748,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.778444,\n          \"diff_xcorr_fwd_p\": 0.324673,\n          \"diff_xcorr_fwd_r\": 0.5615,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6238,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.6898,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    }\n  ]\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D102_null_s42_s44_fpr.json",
    "content": "{\n  \"description\": \"FPR transparency: per-seed per-pair raw p-values for 3 null experiments (s42-s44, alpha=0.00, Pythia-410M, T=10). Extracted from run_5method_analysis_d102.py output, BH-FDR recomputed across 6 pairs.\",\n  \"model\": \"pythia-410m\",\n  \"alpha\": 0.0,\n  \"T\": 10,\n  \"n_perm\": 5000,\n  \"threshold_criterion\": \"true_3sigma_d105\",\n  \"pair_basis\": \"6-pair (distinct_1/2/3 only, mauve excluded)\",\n  \"methods\": [\n    \"perm_granger (BH-FDR across 6 pairs)\",\n    \"diff_xcorr (BH-FDR across 6 pairs)\",\n    \"threshold_onset (true_3sigma_d105)\",\n    \"ty_granger (uncorrected)\",\n    \"naive_xcorr (|r|>0.5, sig requires lag!=0, consensus vote requires lag<0)\"\n  ],\n  \"consensus_rule\": \"K = number of methods voting forward causation. xcorr methods (naive, diff) vote only if peak_lag < 0 (canary leads downstream). PermG and TY vote if significant (after FDR for PermG). Threshold votes if canary_onset < downstream_onset.\",\n  \"summary\": {\n    \"total_seed_pairs\": 18,\n    \"K_ge_3_count\": 0,\n    \"K_ge_3_fpr\": 0.0,\n    \"per_seed_K_ge_3\": {\n      \"s42\": 0,\n      \"s43\": 0,\n      \"s44\": 0\n    },\n    \"K_ge_3_permg_breakdown\": {\n      \"with_permg\": 0,\n      \"without_permg\": 0,\n      \"detail\": \"none\"\n    },\n    \"per_seed_permg_fwd_fdr\": {\n      \"s42\": 0,\n      \"s43\": 0,\n      \"s44\": 0\n    }\n  },\n  \"seeds\": [\n    {\n      \"seed\": 42,\n      \"exp_dir\": \"results/alpha_sweep/a000_s42\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.05139,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.795641,\n          \"diff_xcorr_fwd_p\": 0.000157,\n          \"diff_xcorr_fwd_r\": 0.9408,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.7587,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9023,\n          \"naive_xcorr_lag\": -5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.080384,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.978204,\n          \"diff_xcorr_fwd_p\": 0.009707,\n          \"diff_xcorr_fwd_r\": 0.9184,\n          \"diff_xcorr_fwd_lag\": -4,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.4974,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8262,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"diff\", \"threshold\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.075585,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.985403,\n          \"diff_xcorr_fwd_p\": 0.01191,\n          \"diff_xcorr_fwd_r\": 0.9095,\n          \"diff_xcorr_fwd_lag\": -4,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.9989,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8161,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"diff\", \"threshold\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.94981,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.343131,\n          \"diff_xcorr_fwd_p\": 0.051439,\n          \"diff_xcorr_fwd_r\": -0.7037,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.017,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8166,\n          \"naive_xcorr_lag\": -4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"ty\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.544291,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.353929,\n          \"diff_xcorr_fwd_p\": 0.192837,\n          \"diff_xcorr_fwd_r\": -0.5137,\n          \"diff_xcorr_fwd_lag\": 2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.565,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7783,\n          \"naive_xcorr_lag\": 4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.371526,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.211758,\n          \"diff_xcorr_fwd_p\": 0.202654,\n          \"diff_xcorr_fwd_r\": 0.5482,\n          \"diff_xcorr_fwd_lag\": -3,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": -4,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.0003,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8257,\n          \"naive_xcorr_lag\": 4,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        }\n      ]\n    },\n    {\n      \"seed\": 43,\n      \"exp_dir\": \"results/alpha_sweep/a000_s43\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.079584,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.059788,\n          \"diff_xcorr_fwd_p\": 0.085352,\n          \"diff_xcorr_fwd_r\": -0.7509,\n          \"diff_xcorr_fwd_lag\": 4,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.0076,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": -0.9029,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.070186,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.030394,\n          \"diff_xcorr_fwd_p\": 0.000594,\n          \"diff_xcorr_fwd_r\": 0.9127,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.4004,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.9162,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.034393,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.088782,\n          \"diff_xcorr_fwd_p\": 0.000713,\n          \"diff_xcorr_fwd_r\": 0.9079,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.8147,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": -0.8943,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"diff\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.516297,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.472905,\n          \"diff_xcorr_fwd_p\": 0.163821,\n          \"diff_xcorr_fwd_r\": 0.5435,\n          \"diff_xcorr_fwd_lag\": -2,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.026,\n          \"ty_granger_sig\": true,\n          \"naive_xcorr_r\": 0.8517,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 1,\n          \"consensus_methods\": [\"ty\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.878024,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.282344,\n          \"diff_xcorr_fwd_p\": 0.260901,\n          \"diff_xcorr_fwd_r\": 0.6237,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.3364,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8123,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.575485,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.214557,\n          \"diff_xcorr_fwd_p\": 0.167261,\n          \"diff_xcorr_fwd_r\": 0.7233,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6744,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7685,\n          \"naive_xcorr_lag\": 3,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    },\n    {\n      \"seed\": 44,\n      \"exp_dir\": \"results/alpha_sweep/a000_s44\",\n      \"T\": 10,\n      \"n_gens\": 11,\n      \"n_perm\": 5000,\n      \"pairs\": [\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.069186,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.184496,\n          \"diff_xcorr_fwd_p\": 0.005749,\n          \"diff_xcorr_fwd_r\": 0.9715,\n          \"diff_xcorr_fwd_lag\": -5,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.1862,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.9144,\n          \"naive_xcorr_lag\": -5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.029994,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.086983,\n          \"diff_xcorr_fwd_p\": 0.000244,\n          \"diff_xcorr_fwd_r\": 0.9327,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": true,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.2306,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8517,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"diff\"]\n        },\n        {\n          \"canary\": \"token_entropy\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.031594,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.260948,\n          \"diff_xcorr_fwd_p\": 0.044792,\n          \"diff_xcorr_fwd_r\": 0.6779,\n          \"diff_xcorr_fwd_lag\": -1,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": 4,\n          \"threshold_onset_sig\": true,\n          \"ty_granger_p\": 0.8199,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8241,\n          \"naive_xcorr_lag\": -1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 2,\n          \"consensus_methods\": [\"naive\", \"threshold\"]\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_1\",\n          \"perm_granger_fwd_p\": 0.374325,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.14997,\n          \"diff_xcorr_fwd_p\": 0.042819,\n          \"diff_xcorr_fwd_r\": 0.8904,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6129,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.8186,\n          \"naive_xcorr_lag\": 5,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_2\",\n          \"perm_granger_fwd_p\": 0.886623,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.443711,\n          \"diff_xcorr_fwd_p\": 0.060923,\n          \"diff_xcorr_fwd_r\": 0.861,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.1696,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.7374,\n          \"naive_xcorr_lag\": 1,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        },\n        {\n          \"canary\": \"ece\",\n          \"downstream\": \"distinct_3\",\n          \"perm_granger_fwd_p\": 0.259748,\n          \"perm_granger_fwd_sig_fdr\": false,\n          \"perm_granger_rev_p\": 0.778444,\n          \"diff_xcorr_fwd_p\": 0.324673,\n          \"diff_xcorr_fwd_r\": 0.5615,\n          \"diff_xcorr_fwd_lag\": 5,\n          \"diff_xcorr_fwd_sig_fdr\": false,\n          \"threshold_onset_lead\": null,\n          \"threshold_onset_sig\": false,\n          \"ty_granger_p\": 0.6238,\n          \"ty_granger_sig\": false,\n          \"naive_xcorr_r\": 0.6898,\n          \"naive_xcorr_lag\": 2,\n          \"naive_xcorr_sig\": true,\n          \"consensus_votes\": 0,\n          \"consensus_methods\": []\n        }\n      ]\n    }\n  ]\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-24T16:52:32.333120+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D102_null_s42_s44_fpr.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-24T16:52:32.333290+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "D102_null_s42_s44_fpr",
  "type": "data",
  "description": "FPR transparency: 3 null seeds (s42-s44) 6-pair D102 analysis. BH-FDR recomputed across 6 pairs. K>=3 FPR = 0/18, PermG FPR = 0/18.",
  "project": "distrib_canary_collapse",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D102_null_s42_s44_fpr.json",
  "tags": "['fpr', 'null', 'd102', '6pair']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "D102_null_s42_s44_fpr",
    "type": "data",
    "description": "FPR transparency: 3 null seeds (s42-s44) 6-pair D102 analysis. BH-FDR recomputed across 6 pairs. K>=3 FPR = 0/18, PermG FPR = 0/18.",
    "project": "distrib_canary_collapse",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/D102_null_s42_s44_fpr.json",
    "tags": "['fpr', 'null', 'd102', '6pair']"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-24T16:52:32.333481+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_4514c1\", \"name\": \"D102_null_s42_s44_fpr\", \"type\": \"data\", \"description\": \"FPR transparency: 3 null seeds (s42-s44) 6-pair D102 analysis. BH-FDR recomputed across 6 pairs. K>=3 FPR = 0/18, PermG FPR = 0/18.\", \"path\": \"projects/distrib_canary_collapse/artifacts/_project/data/D102_null_s42_s44_fpr.json\", \"url\": null, \"project\": \"distrib_canary_collapse\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T16:52:18.126114+00:00\", \"tags\": [\"fpr\", \"null\", \"d102\", \"6pair\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-24T16:52:32.333669+00:00_

完成。汇总：

## 配置一致性验证

| 参数 | s42 | s43 | s44 | s45-s50 标准 |
|------|-----|-----|-----|-------------|
| model | pythia-410m | pythia-410m | pythia-410m | pythia-410m |
| data_dir | wikitext103_5k | wikitext103_5k | wikitext103_5k | wikitext103_5k |
| steps_per_gen | 5000 | 5000 | 5000 | 5000 |
| num_generations | 10 | 10 | 10 | 10 |
| synthetic_ratio | 0.0 | 0.0 | 0.0 | 0.0 |
| precision | fp32 (默认, bf16=false) | fp32 | fp32 | fp32 |

配置完全一致。s42-s44 目录名无 `_fp32` 后缀但参数等价。

## 6-pair FPR 结果

| Seed | PermG FP (FDR) | K≥3 FP | Max K |
|------|---------------|--------|-------|
| s42 | 0/6 | 0/6 | 2 |
| s43 | 0/6 | 0/6 | 1 |
| s44 | 0/6 | 0/6 | 2 |
| **合计** | **0/18** | **0/18** | - |

**PermG FPR = 0.00, K≥3 FPR = 0.00**

与 8-pair 结果一致（s42-s44 均为 permg=0/8），6-pair ≤ 8-pair 验证通过。

BH-FDR 已按 6 pairs 重新计算（非原 8-pair FDR），consensus voting 遵循 D102 规则（xcorr 需 peak_lag < 0，C009 方向修正）。

Artifact 已注册：`D102_null_s42_s44_fpr.json` (art_20260524_4514c1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_null_s42_s44_d102_20260524T164250"
}
```

</details>

---
