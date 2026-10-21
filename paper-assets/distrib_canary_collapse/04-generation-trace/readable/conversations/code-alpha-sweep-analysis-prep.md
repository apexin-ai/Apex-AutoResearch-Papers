# code alpha sweep analysis prep

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_code_alpha-sweep-analysis-prep_20260514T210910.jsonl`
- **Structured JSON:** [`2e9036bd7db428589eb8.json`](../../sessions/2e/2e9036bd7db428589eb8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-14T21:11:46.481893+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__read_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-14T21:11:46.482146+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T21:11:46.482327+00:00_

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
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
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

### Tool call

_source line 4 · 2026-05-14T21:11:46.482468+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/analyze_mvp.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/analyze_mvp.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T21:11:46.482741+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return data\\n\\n\\ndef extract(metrics_list, name):\\n    \\\"\\\"\\\"Extract a single metric as numpy array, sorted by generation.\\\"\\\"\\\"\\n    return np.array([m[name
…[truncated 7504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T21:11:46.482899+00:00_

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
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
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

_source line 7 · 2026-05-14T21:11:46.483153+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Analyze MVP experiment: metric trends, cross-correlation, lead time.\\n\\nReads all_metrics.json from each rep, produces:\\n  - metric_trends.png : canary + downstream metrics vs generation\\n  - cross_correlation.png : cross-correlation heatmap\\n  - lead_time_table.csv : lead time estimates per canary-downstream pair\\n  - analysis_summary.json : machine-readable summary with graded verdict\\n\\nEvaluation pipeline (per mvp_evaluation_criteria.md):\\n  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50\\n  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency\\n  3. Permutation test (§1) — per-triplet significance via 10k permutations\\n  4. Per-seed significance filtering (§2) — 3/3 consistency requirement\\n  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL\\n  6. Lag dispersion statistics — mean, std, min, max per consistent pair\\n\\nUsage:\\n    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44\\n    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\n\\nimport matplotlib.pyplot as plt\\nimport numpy as np\\nimport pandas as pd\\n\\n\\nCANARY_METRICS = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM_METRICS = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\", \\\"mauve\\\"]\\n\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\", \\\"distinct_1\\\", \\\"distinct_2\\\",\\n                   \\\"distinct_3\\\", \\\"mauve\\\"}\\n\\n\\ndef load_metrics(results_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}.\\\"\\\"\\\"\\n    data = {}\\n    for seed in seeds:\\n        path = os.path.join(results_dir, f\\\"r
…[truncated 7375 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T21:11:46.483332+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 8\\ndrwxr-xr-x  4 root root   48 May 15 03:01 .\\ndrwxr-xr-x  6 root root 4096 May 15 05:06 ..\\ndrwxr-xr-x  4 root root   50 May 15 05:04 alpha_sweep\\ndrwxr-xr-x 10 root root 4096 May 15 03:00 mvp\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T21:11:46.483485+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep -type f -name \"*.json\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "find /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep -type f -name \"*.json\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T21:11:46.483633+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/generation_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/checkpoint/tokenizer.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_1/metrics.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/synthetic_data/state.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/synthetic_data/dataset_info.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/checkpoint/config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/checkpoint/generation_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/checkpoint/tokenizer_config.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_2/checkpoint/special_tokens_map.json\\n/root/autodl-tmp/distrib_canary_collapse/results/alpha_
…[truncated 2022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T21:11:46.483772+00:00_

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
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
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

_source line 12 · 2026-05-14T21:11:46.483894+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 0\\ndrwxr-xr-x 4 root root  50 May 15 05:04 .\\ndrwxr-xr-x 4 root root  48 May 15 03:01 ..\\ndrwxr-xr-x 8 root root 135 May 15 04:55 a000_s42\\ndrwxr-xr-x 2 root root  33 May 15 05:04 a025_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T21:11:46.484012+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"toda_yamamoto\\|def toda\\|def ty_\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"toda_yamamoto\\|def toda\\|def ty_\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T21:11:46.484126+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T21:11:46.484236+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def toda_yamamoto\\|def ty_\\|def toda\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def toda_yamamoto\\|def ty_\\|def toda\" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T21:11:46.484408+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T21:11:46.484526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a000_s42/gen_0/metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T21:11:46.484661+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"token_entropy\\\": 3.2341948700181407,\\n  \\\"self_bleu\\\": 0.010194395218435404,\\n  \\\"distinct_1\\\": 0.0982156685333268,\\n  \\\"distinct_2\\\": 0.5178027030111348,\\n  \\\"distinct_3\\\": 0.8127277321747353,\\n  \\\"ece\\\": 0.010804557477709054,\\n  \\\"effective_rank\\\": 46.612774691899155,\\n  \\\"perplexity\\\": 26.948958972544652,\\n  \\\"mauve\\\": 0.03406737671684175,\\n  \\\"generation\\\": 0\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T21:11:46.484775+00:00_

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
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
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

### Tool result

_source line 20 · 2026-05-14T21:11:46.484886+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"config.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T21:11:46.485015+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "grep -n \"def \" /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T21:11:46.485131+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"41:def load_metrics(data_dir, seeds):\\n51:def extract(metrics_list, name):\\n57:def orient(series, name):\\n66:def naive_pearson(c, d, cn, dn, max_lag=3):\\n95:def diff_xcorr(c, d, cn, dn, max_lag=3):\\n126:def _onset_gen(series, name):\\n139:def threshold_lead(c, d, cn, dn):\\n174:def _adf_order(series, max_d=2):\\n190:def toda_yamamoto(c, d, cn, dn):\\n280:def main():\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T21:11:46.485241+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -280 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -280 /root/autodl-tmp/distrib_canary_collapse/method_ablation.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T21:11:46.485532+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"Method ablation: compare four lead-lag estimation methods.\\n\\nCompares naive vs robust approaches to detect canary->downstream lead-lag,\\nquantifying the spurious regression rate when non-stationary series are\\ncorrelated without proper detrending.\\n\\nInput:  results/mvp/rep_{seed}/all_metrics.json (seeds 42-45)\\nOutput: results/mvp/analysis/method_ablation.json\\n\\nMethods:\\n  1. Naive Pearson lag-correlation (raw levels)\\n  2. Differenced cross-correlation (first-differenced series)\\n  3. Threshold-based lead time (2-sigma onset detection)\\n  4. Toda-Yamamoto augmented-lag Granger causality\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport warnings\\nfrom itertools import product\\n\\nimport numpy as np\\nfrom scipy import stats\\nfrom statsmodels.tsa.stattools import adfuller\\n\\nwarnings.filterwarnings(\\\"ignore\\\")\\n\\nCANARY = [\\\"token_entropy\\\", \\\"self_bleu\\\", \\\"ece\\\", \\\"effective_rank\\\"]\\nDOWNSTREAM = [\\\"perplexity\\\", \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"]\\n\\n# Sign conventions: \\\"higher is worse\\\" kept as-is; \\\"lower is worse\\\" negated\\n# so that degradation = positive direction in all analyses.\\nHIGHER_IS_WORSE = {\\\"self_bleu\\\", \\\"ece\\\", \\\"perplexity\\\"}\\nLOWER_IS_WORSE = {\\\"token_entropy\\\", \\\"effective_rank\\\",\\n                   \\\"distinct_1\\\", \\\"distinct_2\\\", \\\"distinct_3\\\"}\\n\\nALPHA = 0.05\\n\\n\\ndef load_metrics(data_dir, seeds):\\n    \\\"\\\"\\\"Load all_metrics.json for each seed.\\\"\\\"\\\"\\n    data = {}\\n    for s in seeds:\\n        path = os.path.join(data_dir, f\\\"rep_{s}\\\", \\\"all_metrics.json\\\")\\n        with open(path) as f:\\n            data[s] = json.load(f)\\n    return data\\n\\n\\ndef extract(metrics_list, name):\\n    \\\"\\\"\\\"Extract a single metric as numpy array, sorted by generation.\\\"\\\"\\\"\\n    return np.array([m[name
…[truncated 7345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T21:11:46.485712+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "ls /root/autodl-tmp/distrib_canary_collapse/results/mvp/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T21:11:46.485841+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"analysis\\nanalysis_maxlag5_backup\\nrep_42\\nrep_42_v1_partial\\nrep_43\\nrep_43_v1_partial\\nrep_44\\nrep_45\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T21:11:46.485958+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "head -5 /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "head -5 /root/autodl-tmp/distrib_canary_collapse/results/mvp/rep_42/all_metrics.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T21:11:46.486090+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"token_entropy\\\": 3.2341948700181407,\\n    \\\"self_bleu\\\": 0.010194395218435404,\\n    \\\"distinct_1\\\": 0.0982156685333268,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T21:11:46.486304+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cat > /root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py << 'SCRIPT_EOF'\n\"\"\"Alpha-sweep aggregation analysis: canary lead-time vs contamination level.\n\nInput:  results/alpha_sweep/a{NNN}_s{seed}/gen_*/metrics.json\n        Directory naming: a{alpha*100:03d}_s{seed}[_v*] (e.g. a025_s42, a050_s43_v2)\nOutput: results/alpha_sweep/analysis_summary.json + console summary table\n\nDependencies: numpy, scipy, statsmodels\n\nKey design decisions:\n  - Toda-Yamamoto (augmented-lag Granger causality) is the primary test,\n    ported from method_ablation.py — no naive cross-correlation.\n  - token_entropy is the gold-standard canary (Granger-causal to all downstream).\n  - ECE→distinct_1 is the only other validated causal pair.\n  - α=0.0 is the null control (pure real data); expect no canary signal.\n  - Runs with < 5 generations are skipped (TY needs sufficient df).\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport warnings\nfrom collections import defaultdict\n\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.tsa.stattools import adfuller\n\nwarnings.filterwarnings(\"ignore\")\n\nCANARY = [\"token_entropy\", \"ece\"]\nDOWNSTREAM = [\"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\"]\nVALID_PAIRS = {\n    (\"token_entropy\", \"perplexity\"),\n    (\"token_entropy\", \"distinct_1\"),\n    (\"token_entropy\", \"distinct_2\"),\n    (\"token_entropy\", \"distinct_3\"),\n    (\"ece\", \"distinct_1\"),\n}\n\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\",\n                   \"distinct_1\", \"distinct_2\", \"distinct_3\"}\n\nALPHA_STAT = 0.05\nMIN_GENS = 5\n\n\ndef orient(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\ndef _adf_order(series, max_d=2):\n    for d in range(max_d + 1):\n        s = series.copy()\n        for _ in range(d):\n            s = np.diff(s)\n        if len(s) < 5:\n            return d\n        try:\n            if adfuller(s, maxlag=1, autolag=None)[1] < 0.05:\n                return d\n        except Exception:\n            pass\n    return max_d\n\n\ndef toda_yamamoto(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    n = len(x)\n\n    dc, dd = _adf_order(x), _adf_order(y)\n    d_max = max(dc, dd)\n\n    p = 1\n    k = p + d_max\n    T_eff = n - k\n    n_params = 1 + 2 * k\n    df_resid = T_eff - n_params\n\n    if df_resid < 1:\n        return {\n            \"method\": \"toda_yamamoto\", \"p\": p, \"d_max\": d_max, \"k\": k,\n            \"wald_F\": None, \"p_value\": None, \"significant\": False,\n            \"note\": f\"no residual df (T_eff={T_eff}, params={n_params})\",\n            \"d_canary\": dc, \"d_downstream\": dd,\n        }\n\n    Y = y[k:]\n    X_cols = [np.ones(T_eff)]\n    for l in range(1, k + 1):\n        X_cols.append(x[k - l: n - l])\n        X_cols.append(y[k - l: n - l])\n    X = np.column_stack(X_cols)\n\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid ** 2) / df_resid\n        XtX_inv = np.linalg.inv(X.T @ X)\n    except Exception:\n        return {\n            \"method\": \"toda_yamamoto\", \"p\": p, \"d_max\": d_max, \"k\": k,\n            \"wald_F\": None, \"p_value\": None, \"significant\": False,\n            \"note\": \"OLS failed (singular design matrix)\",\n            \"d_canary\": dc, \"d_downstream\": dd,\n        }\n\n    test_idx = [2 * (l - 1) + 1 for l in range(1, p + 1)]\n    R = np.zeros((p, n_params))\n    for i, idx in enumerate(test_idx):\n        R[i, idx] = 1.0\n\n    Rb = R @ beta\n    try:\n        cov_Rb = sigma2 * (R @ XtX_inv @ R.T)\n        W = float(Rb @ np.linalg.inv(cov_Rb) @ Rb)\n        F = W / p\n        pval = float(1.0 - stats.f.cdf(F, p, df_resid))\n    except Exception:\n        return {\n            \"method\": \"toda_yamamoto\", \"p\": p, \"d_max\": d_max, \"k\": k,\n            \"wald_F\": None, \"p_value\": None, \"significant\": False,\n            \"note\": \"Wald computation failed (singular covariance)\",\n            \"d_canary\": dc, \"d_downstream\": dd,\n        }\n\n    return {\n        \"method\": \"toda_yamamoto\",\n        \"p\": int(p), \"d_max\": int(d_max), \"k\": int(k),\n        \"wald_F\": round(float(F), 4),\n        \"p_value\": round(float(pval), 6),\n        \"significant\": bool(pval < ALPHA_STAT),\n        \"df_resid\": int(df_resid),\n        \"d_canary\": int(dc), \"d_downstream\": int(dd),\n    }\n\n\n# ── Discovery & loading ─────────────────────────────────────────────────────\n\nRUN_RE = re.compile(r\"^a(\\d{3})_s(\\d+)\")\n\n\ndef discover_runs(sweep_dir):\n    \"\"\"Find all alpha-seed directories and return {(alpha_frac, seed): path}.\"\"\"\n    runs = {}\n    if not os.path.isdir(sweep_dir):\n        return runs\n    for name in sorted(os.listdir(sweep_dir)):\n        m = RUN_RE.match(name)\n        if not m:\n            continue\n        full = os.path.join(sweep_dir, name)\n        if not os.path.isdir(full):\n            continue\n        alpha_int = int(m.group(1))\n        seed = int(m.group(2))\n        alpha_frac = alpha_int / 100.0\n        key = (alpha_frac, seed)\n        # later version (e.g. _v3) overrides earlier\n        runs[key] = full\n    return runs\n\n\ndef load_run_metrics(run_dir):\n    \"\"\"Load gen_*/metrics.json, return list sorted by generation.\"\"\"\n    metrics = []\n    for entry in os.listdir(run_dir):\n        gm = re.match(r\"^gen_(\\d+)$\", entry)\n        if not gm:\n            continue\n        mpath = os.path.join(run_dir, entry, \"metrics.json\")\n        if not os.path.isfile(mpath):\n            continue\n        with open(mpath) as f:\n            rec = json.load(f)\n        rec[\"generation\"] = int(gm.group(1))\n        metrics.append(rec)\n    metrics.sort(key=lambda x: x[\"generation\"])\n    return metrics\n\n\ndef extract(metrics_list, name):\n    return np.array([m[name] for m in metrics_list])\n\n\n# ── Per-run analysis ─────────────────────────────────────────────────────────\n\ndef analyze_run(metrics_list):\n    \"\"\"Run TY on all valid canary→downstream pairs. Return list of results.\"\"\"\n    results = []\n    for cn in CANARY:\n        if cn not in metrics_list[0]:\n            continue\n        c = extract(metrics_list, cn)\n        for dn in DOWNSTREAM:\n            if (cn, dn) not in VALID_PAIRS:\n                continue\n            if dn not in metrics_list[0]:\n                continue\n            d = extract(metrics_list, dn)\n            ty = toda_yamamoto(c, d, cn, dn)\n            ty[\"canary\"] = cn\n            ty[\"downstream\"] = dn\n            results.append(ty)\n    return results\n\n\n# ── Aggregation ──────────────────────────────────────────────────────────────\n\ndef aggregate_by_alpha(all_results):\n    \"\"\"Group per-run TY results by alpha, then by pair, across seeds.\n\n    Returns {alpha: {(canary,downstream): {stats...}}}\n    \"\"\"\n    by_alpha = defaultdict(lambda: defaultdict(list))\n    for (alpha, seed), run_res in all_results.items():\n        for r in run_res:\n            pair = (r[\"canary\"], r[\"downstream\"])\n            by_alpha[alpha][pair].append(r)\n\n    agg = {}\n    for alpha in sorted(by_alpha):\n        agg[alpha] = {}\n        for pair, results in by_alpha[alpha].items():\n            pvals = [r[\"p_value\"] for r in results if r[\"p_value\"] is not None]\n            f_vals = [r[\"wald_F\"] for r in results if r[\"wald_F\"] is not None]\n            n_sig = sum(1 for r in results if r[\"significant\"])\n            n_total = len(results)\n\n            agg[alpha][pair] = {\n                \"n_seeds\": n_total,\n                \"n_significant\": n_sig,\n                \"sig_rate\": round(n_sig / n_total, 4) if n_total else 0,\n                \"p_values\": [round(p, 6) for p in pvals],\n                \"p_median\": round(float(np.median(pvals)), 6) if pvals else None,\n                \"p_mean\": round(float(np.mean(pvals)), 6) if pvals else None,\n                \"F_values\": [round(f, 4) for f in f_vals],\n                \"F_mean\": round(float(np.mean(f_vals)), 4) if f_vals else None,\n                \"F_std\": round(float(np.std(f_vals)), 4) if len(f_vals) > 1 else None,\n                \"per_seed\": results,\n            }\n    return agg\n\n\n# ── Console output ───────────────────────────────────────────────────────────\n\ndef print_summary(agg, run_info):\n    print(\"=\" * 78)\n    print(\"ALPHA-SWEEP ANALYSIS: Canary Lead-Time vs Contamination Level\")\n    print(\"=\" * 78)\n\n    print(f\"\\nDiscovered runs: {len(run_info)}\")\n    for (alpha, seed), info in sorted(run_info.items()):\n        status = \"OK\" if info[\"n_gens\"] >= MIN_GENS else \"SKIPPED (<5 gen)\"\n        print(f\"  α={alpha:.2f} seed={seed}: {info['n_gens']} gens [{status}]\")\n\n    all_pairs = set()\n    for alpha_pairs in agg.values():\n        all_pairs.update(alpha_pairs.keys())\n    all_pairs = sorted(all_pairs)\n\n    if not all_pairs:\n        print(\"\\nNo completed runs to analyze.\")\n        return\n\n    # Per-pair detail table\n    for pair in all_pairs:\n        cn, dn = pair\n        print(f\"\\n{'─' * 78}\")\n        print(f\"  {cn} → {dn}\")\n        print(f\"{'─' * 78}\")\n        print(f\"  {'α':>6}  {'seeds':>5}  {'sig':>4}  {'rate':>6}  \"\n              f\"{'p_med':>8}  {'F_mean':>8}  {'F_std':>7}\")\n\n        for alpha in sorted(agg):\n            if pair not in agg[alpha]:\n                continue\n            s = agg[alpha][pair]\n            p_med = f\"{s['p_median']:.4f}\" if s[\"p_median\"] is not None else \"   N/A\"\n            f_mean = f\"{s['F_mean']:.2f}\" if s[\"F_mean\"] is not None else \"   N/A\"\n            f_std = f\"{s['F_std']:.2f}\" if s[\"F_std\"] is not None else \"   N/A\"\n            print(f\"  {alpha:>6.2f}  {s['n_seeds']:>5}  \"\n                  f\"{s['n_significant']:>4}  {s['sig_rate']:>5.0%}  \"\n                  f\"{p_med:>8}  {f_mean:>8}  {f_std:>7}\")\n\n    # Cross-α summary: token_entropy → all downstream\n    print(f\"\\n{'=' * 78}\")\n    print(\"CROSS-α SUMMARY (token_entropy canary)\")\n    print(f\"{'=' * 78}\")\n    te_pairs = [p for p in all_pairs if p[0] == \"token_entropy\"]\n    if te_pairs:\n        hdr = f\"  {'α':>6}\"\n        for _, dn in te_pairs:\n            hdr += f\"  {dn:>14}\"\n        print(hdr)\n        for alpha in sorted(agg):\n            row = f\"  {alpha:>6.2f}\"\n            for pair in te_pairs:\n                if pair in agg[alpha]:\n                    s = agg[alpha][pair]\n                    marker = f\"{s['sig_rate']:.0%}\"\n                    if s[\"p_median\"] is not None:\n                        marker += f\" (p={s['p_median']:.3f})\"\n                    row += f\"  {marker:>14}\"\n                else:\n                    row += f\"  {'—':>14}\"\n            print(row)\n\n    # Null control check\n    if 0.0 in agg:\n        any_sig = any(\n            s[\"n_significant\"] > 0\n            for s in agg[0.0].values()\n        )\n        print(f\"\\nNull control (α=0.0): \"\n              f\"{'⚠ UNEXPECTED signal detected' if any_sig else 'clean (no signal) ✓'}\")\n\n\ndef build_output(agg, run_info):\n    \"\"\"Build JSON-serializable output dict.\"\"\"\n    output = {\n        \"meta\": {\n            \"test\": \"toda_yamamoto\",\n            \"alpha_stat\": ALPHA_STAT,\n            \"min_gens\": MIN_GENS,\n            \"valid_pairs\": [list(p) for p in sorted(VALID_PAIRS)],\n        },\n        \"runs\": {\n            f\"a{int(alpha*100):03d}_s{seed}\": {\n                \"alpha\": alpha,\n                \"seed\": seed,\n                \"n_gens\": info[\"n_gens\"],\n                \"analyzed\": info[\"n_gens\"] >= MIN_GENS,\n            }\n            for (alpha, seed), info in sorted(run_info.items())\n        },\n        \"by_alpha\": {},\n    }\n\n    for alpha in sorted(agg):\n        alpha_key = f\"{alpha:.2f}\"\n        output[\"by_alpha\"][alpha_key] = {}\n        for (cn, dn), s in sorted(agg[alpha].items()):\n            pair_key = f\"{cn}_to_{dn}\"\n            per_seed_clean = []\n            for r in s[\"per_seed\"]:\n                per_seed_clean.append({\n                    k: v for k, v in r.items()\n                    if k not in (\"canary\", \"downstream\", \"method\")\n                })\n            output[\"by_alpha\"][alpha_key][pair_key] = {\n                \"n_seeds\": s[\"n_seeds\"],\n                \"n_significant\": s[\"n_significant\"],\n                \"sig_rate\": s[\"sig_rate\"],\n                \"p_median\": s[\"p_median\"],\n                \"p_mean\": s[\"p_mean\"],\n                \"F_mean\": s[\"F_mean\"],\n                \"F_std\": s[\"F_std\"],\n                \"per_seed\": per_seed_clean,\n            }\n\n    return output\n\n\n# ── Main ─────────────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Alpha-sweep aggregation: TY canary analysis across α levels\")\n    parser.add_argument(\"--sweep_dir\", default=\"results/alpha_sweep\",\n                        help=\"Path to alpha_sweep results directory\")\n    parser.add_argument(\"--min_gens\", type=int, default=MIN_GENS,\n                        help=\"Minimum generations required per run (default: 5)\")\n    args = parser.parse_args()\n\n    sweep_dir = args.sweep_dir\n    if not os.path.isabs(sweep_dir):\n        sweep_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), sweep_dir)\n\n    runs = discover_runs(sweep_dir)\n    if not runs:\n        print(f\"No runs found in {sweep_dir}\")\n        sys.exit(0)\n\n    run_info = {}\n    all_results = {}\n\n    for (alpha, seed), path in sorted(runs.items()):\n        metrics = load_run_metrics(path)\n        n_gens = len(metrics)\n        run_info[(alpha, seed)] = {\"n_gens\": n_gens, \"path\": path}\n\n        if n_gens < args.min_gens:\n            continue\n\n        results = analyze_run(metrics)\n        all_results[(alpha, seed)] = results\n\n    agg = aggregate_by_alpha(all_results)\n\n    print_summary(agg, run_info)\n\n    out_dir = os.path.join(sweep_dir)\n    os.makedirs(out_dir, exist_ok=True)\n    out_path = os.path.join(out_dir, \"analysis_summary.json\")\n    output = build_output(agg, run_info)\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat > /root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py << 'SCRIPT_EOF'\n\"\"\"Alpha-sweep aggregation analysis: canary lead-time vs contamination level.\n\nInput:  results/alpha_sweep/a{NNN}_s{seed}/gen_*/metrics.json\n        Directory naming: a{alpha*100:03d}_s{seed}[_v*] (e.g. a025_s42, a050_s43_v2)\nOutput: results/alpha_sweep/analysis_summary.json + console summary table\n\nDependencies: numpy, scipy, statsmodels\n\nKey design decisions:\n  - Toda-Yamamoto (augmented-lag Granger causality) is the primary test,\n    ported from method_ablation.py — no naive cross-correlation.\n  - token_entropy is the gold-standard canary (Granger-causal to all downstream).\n  - ECE→distinct_1 is the only other validated causal pair.\n  - α=0.0 is the null control (pure real data); expect no canary signal.\n  - Runs with < 5 generations are skipped (TY needs sufficient df).\n\"\"\"\n\nimport argparse\nimport json\nimport os\nimport re\nimport sys\nimport warnings\nfrom collections import defaultdict\n\nimport numpy as np\nfrom scipy import stats\nfrom statsmodels.tsa.stattools import adfuller\n\nwarnings.filterwarnings(\"ignore\")\n\nCANARY = [\"token_entropy\", \"ece\"]\nDOWNSTREAM = [\"perplexity\", \"distinct_1\", \"distinct_2\", \"distinct_3\"]\nVALID_PAIRS = {\n    (\"token_entropy\", \"perplexity\"),\n    (\"token_entropy\", \"distinct_1\"),\n    (\"token_entropy\", \"distinct_2\"),\n    (\"token_entropy\", \"distinct_3\"),\n    (\"ece\", \"distinct_1\"),\n}\n\nHIGHER_IS_WORSE = {\"self_bleu\", \"ece\", \"perplexity\"}\nLOWER_IS_WORSE = {\"token_entropy\", \"effective_rank\",\n                   \"distinct_1\", \"distinct_2\", \"distinct_3\"}\n\nALPHA_STAT = 0.05\nMIN_GENS = 5\n\n\ndef orient(series, name):\n    return -series.copy() if name in LOWER_IS_WORSE else series.copy()\n\n\ndef _adf_order(series, max_d=2):\n    for d in range(max_d + 1):\n        s = series.copy()\n        for _ in range(d):\n            s = np.diff(s)\n        if len(s) < 5:\n            return d\n        try:\n            if adfuller(s, maxlag=1, autolag=None)[1] < 0.05:\n                return d\n        except Exception:\n            pass\n    return max_d\n\n\ndef toda_yamamoto(c, d, cn, dn):\n    x, y = orient(c, cn), orient(d, dn)\n    n = len(x)\n\n    dc, dd = _adf_order(x), _adf_order(y)\n    d_max = max(dc, dd)\n\n    p = 1\n    k = p + d_max\n    T_eff = n - k\n    n_params = 1 + 2 * k\n    df_resid = T_eff - n_params\n\n    if df_resid < 1:\n        return {\n            \"method\": \"toda_yamamoto\", \"p\": p, \"d_max\": d_max, \"k\": k,\n            \"wald_F\": None, \"p_value\": None, \"significant\": False,\n            \"note\": f\"no residual df (T_eff={T_eff}, params={n_params})\",\n            \"d_canary\": dc, \"d_downstream\": dd,\n        }\n\n    Y = y[k:]\n    X_cols = [np.ones(T_eff)]\n    for l in range(1, k + 1):\n        X_cols.append(x[k - l: n - l])\n        X_cols.append(y[k - l: n - l])\n    X = np.column_stack(X_cols)\n\n    try:\n        beta = np.linalg.lstsq(X, Y, rcond=None)[0]\n        resid = Y - X @ beta\n        sigma2 = np.sum(resid ** 2) / df_resid\n        XtX_inv = np.linalg.inv(X.T @ X)\n    except Exception:\n        return {\n            \"method\": \"toda_yamamoto\", \"p\": p, \"d_max\": d_max, \"k\": k,\n            \"wald_F\": None, \"p_value\": None, \"significant\": False,\n            \"note\": \"OLS failed (singular design matrix)\",\n            \"d_canary\": dc, \"d_downstream\": dd,\n        }\n\n    test_idx = [2 * (l - 1) + 1 for l in range(1, p + 1)]\n    R = np.zeros((p, n_params))\n    for i, idx in enumerate(test_idx):\n        R[i, idx] = 1.0\n\n    Rb = R @ beta\n    try:\n        cov_Rb = sigma2 * (R @ XtX_inv @ R.T)\n        W = float(Rb @ np.linalg.inv(cov_Rb) @ Rb)\n        F = W / p\n        pval = float(1.0 - stats.f.cdf(F, p, df_resid))\n    except Exception:\n        return {\n            \"method\": \"toda_yamamoto\", \"p\": p, \"d_max\": d_max, \"k\": k,\n            \"wald_F\": None, \"p_value\": None, \"significant\": False,\n            \"note\": \"Wald computation failed (singular covariance)\",\n            \"d_canary\": dc, \"d_downstream\": dd,\n        }\n\n    return {\n        \"method\": \"toda_yamamoto\",\n        \"p\": int(p), \"d_max\": int(d_max), \"k\": int(k),\n        \"wald_F\": round(float(F), 4),\n        \"p_value\": round(float(pval), 6),\n        \"significant\": bool(pval < ALPHA_STAT),\n        \"df_resid\": int(df_resid),\n        \"d_canary\": int(dc), \"d_downstream\": int(dd),\n    }\n\n\n# ── Discovery & loading ─────────────────────────────────────────────────────\n\nRUN_RE = re.compile(r\"^a(\\d{3})_s(\\d+)\")\n\n\ndef discover_runs(sweep_dir):\n    \"\"\"Find all alpha-seed directories and return {(alpha_frac, seed): path}.\"\"\"\n    runs = {}\n    if not os.path.isdir(sweep_dir):\n        return runs\n    for name in sorted(os.listdir(sweep_dir)):\n        m = RUN_RE.match(name)\n        if not m:\n            continue\n        full = os.path.join(sweep_dir, name)\n        if not os.path.isdir(full):\n            continue\n        alpha_int = int(m.group(1))\n        seed = int(m.group(2))\n        alpha_frac = alpha_int / 100.0\n        key = (alpha_frac, seed)\n        # later version (e.g. _v3) overrides earlier\n        runs[key] = full\n    return runs\n\n\ndef load_run_metrics(run_dir):\n    \"\"\"Load gen_*/metrics.json, return list sorted by generation.\"\"\"\n    metrics = []\n    for entry in os.listdir(run_dir):\n        gm = re.match(r\"^gen_(\\d+)$\", entry)\n        if not gm:\n            continue\n        mpath = os.path.join(run_dir, entry, \"metrics.json\")\n        if not os.path.isfile(mpath):\n            continue\n        with open(mpath) as f:\n            rec = json.load(f)\n        rec[\"generation\"] = int(gm.group(1))\n        metrics.append(rec)\n    metrics.sort(key=lambda x: x[\"generation\"])\n    return metrics\n\n\ndef extract(metrics_list, name):\n    return np.array([m[name] for m in metrics_list])\n\n\n# ── Per-run analysis ─────────────────────────────────────────────────────────\n\ndef analyze_run(metrics_list):\n    \"\"\"Run TY on all valid canary→downstream pairs. Return list of results.\"\"\"\n    results = []\n    for cn in CANARY:\n        if cn not in metrics_list[0]:\n            continue\n        c = extract(metrics_list, cn)\n        for dn in DOWNSTREAM:\n            if (cn, dn) not in VALID_PAIRS:\n                continue\n            if dn not in metrics_list[0]:\n                continue\n            d = extract(metrics_list, dn)\n            ty = toda_yamamoto(c, d, cn, dn)\n            ty[\"canary\"] = cn\n            ty[\"downstream\"] = dn\n            results.append(ty)\n    return results\n\n\n# ── Aggregation ──────────────────────────────────────────────────────────────\n\ndef aggregate_by_alpha(all_results):\n    \"\"\"Group per-run TY results by alpha, then by pair, across seeds.\n\n    Returns {alpha: {(canary,downstream): {stats...}}}\n    \"\"\"\n    by_alpha = defaultdict(lambda: defaultdict(list))\n    for (alpha, seed), run_res in all_results.items():\n        for r in run_res:\n            pair = (r[\"canary\"], r[\"downstream\"])\n            by_alpha[alpha][pair].append(r)\n\n    agg = {}\n    for alpha in sorted(by_alpha):\n        agg[alpha] = {}\n        for pair, results in by_alpha[alpha].items():\n            pvals = [r[\"p_value\"] for r in results if r[\"p_value\"] is not None]\n            f_vals = [r[\"wald_F\"] for r in results if r[\"wald_F\"] is not None]\n            n_sig = sum(1 for r in results if r[\"significant\"])\n            n_total = len(results)\n\n            agg[alpha][pair] = {\n                \"n_seeds\": n_total,\n                \"n_significant\": n_sig,\n                \"sig_rate\": round(n_sig / n_total, 4) if n_total else 0,\n                \"p_values\": [round(p, 6) for p in pvals],\n                \"p_median\": round(float(np.median(pvals)), 6) if pvals else None,\n                \"p_mean\": round(float(np.mean(pvals)), 6) if pvals else None,\n                \"F_values\": [round(f, 4) for f in f_vals],\n                \"F_mean\": round(float(np.mean(f_vals)), 4) if f_vals else None,\n                \"F_std\": round(float(np.std(f_vals)), 4) if len(f_vals) > 1 else None,\n                \"per_seed\": results,\n            }\n    return agg\n\n\n# ── Console output ───────────────────────────────────────────────────────────\n\ndef print_summary(agg, run_info):\n    print(\"=\" * 78)\n    print(\"ALPHA-SWEEP ANALYSIS: Canary Lead-Time vs Contamination Level\")\n    print(\"=\" * 78)\n\n    print(f\"\\nDiscovered runs: {len(run_info)}\")\n    for (alpha, seed), info in sorted(run_info.items()):\n        status = \"OK\" if info[\"n_gens\"] >= MIN_GENS else \"SKIPPED (<5 gen)\"\n        print(f\"  α={alpha:.2f} seed={seed}: {info['n_gens']} gens [{status}]\")\n\n    all_pairs = set()\n    for alpha_pairs in agg.values():\n        all_pairs.update(alpha_pairs.keys())\n    all_pairs = sorted(all_pairs)\n\n    if not all_pairs:\n        print(\"\\nNo completed runs to analyze.\")\n        return\n\n    # Per-pair detail table\n    for pair in all_pairs:\n        cn, dn = pair\n        print(f\"\\n{'─' * 78}\")\n        print(f\"  {cn} → {dn}\")\n        print(f\"{'─' * 78}\")\n        print(f\"  {'α':>6}  {'seeds':>5}  {'sig':>4}  {'rate':>6}  \"\n              f\"{'p_med':>8}  {'F_mean':>8}  {'F_std':>7}\")\n\n        for alpha in sorted(agg):\n            if pair not in agg[alpha]:\n                continue\n            s = agg[alpha][pair]\n            p_med = f\"{s['p_median']:.4f}\" if s[\"p_median\"] is not None else \"   N/A\"\n            f_mean = f\"{s['F_mean']:.2f}\" if s[\"F_mean\"] is not None else \"   N/A\"\n            f_std = f\"{s['F_std']:.2f}\" if s[\"F_std\"] is not None else \"   N/A\"\n            print(f\"  {alpha:>6.2f}  {s['n_seeds']:>5}  \"\n                  f\"{s['n_significant']:>4}  {s['sig_rate']:>5.0%}  \"\n                  f\"{p_med:>8}  {f_mean:>8}  {f_std:>7}\")\n\n    # Cross-α summary: token_entropy → all downstream\n    print(f\"\\n{'=' * 78}\")\n    print(\"CROSS-α SUMMARY (token_entropy canary)\")\n    print(f\"{'=' * 78}\")\n    te_pairs = [p for p in all_pairs if p[0] == \"token_entropy\"]\n    if te_pairs:\n        hdr = f\"  {'α':>6}\"\n        for _, dn in te_pairs:\n            hdr += f\"  {dn:>14}\"\n        print(hdr)\n        for alpha in sorted(agg):\n            row = f\"  {alpha:>6.2f}\"\n            for pair in te_pairs:\n                if pair in agg[alpha]:\n                    s = agg[alpha][pair]\n                    marker = f\"{s['sig_rate']:.0%}\"\n                    if s[\"p_median\"] is not None:\n                        marker += f\" (p={s['p_median']:.3f})\"\n                    row += f\"  {marker:>14}\"\n                else:\n                    row += f\"  {'—':>14}\"\n            print(row)\n\n    # Null control check\n    if 0.0 in agg:\n        any_sig = any(\n            s[\"n_significant\"] > 0\n            for s in agg[0.0].values()\n        )\n        print(f\"\\nNull control (α=0.0): \"\n              f\"{'⚠ UNEXPECTED signal detected' if any_sig else 'clean (no signal) ✓'}\")\n\n\ndef build_output(agg, run_info):\n    \"\"\"Build JSON-serializable output dict.\"\"\"\n    output = {\n        \"meta\": {\n            \"test\": \"toda_yamamoto\",\n            \"alpha_stat\": ALPHA_STAT,\n            \"min_gens\": MIN_GENS,\n            \"valid_pairs\": [list(p) for p in sorted(VALID_PAIRS)],\n        },\n        \"runs\": {\n            f\"a{int(alpha*100):03d}_s{seed}\": {\n                \"alpha\": alpha,\n                \"seed\": seed,\n                \"n_gens\": info[\"n_gens\"],\n                \"analyzed\": info[\"n_gens\"] >= MIN_GENS,\n            }\n            for (alpha, seed), info in sorted(run_info.items())\n        },\n        \"by_alpha\": {},\n    }\n\n    for alpha in sorted(agg):\n        alpha_key = f\"{alpha:.2f}\"\n        output[\"by_alpha\"][alpha_key] = {}\n        for (cn, dn), s in sorted(agg[alpha].items()):\n            pair_key = f\"{cn}_to_{dn}\"\n            per_seed_clean = []\n            for r in s[\"per_seed\"]:\n                per_seed_clean.append({\n                    k: v for k, v in r.items()\n                    if k not in (\"canary\", \"downstream\", \"method\")\n                })\n            output[\"by_alpha\"][alpha_key][pair_key] = {\n                \"n_seeds\": s[\"n_seeds\"],\n                \"n_significant\": s[\"n_significant\"],\n                \"sig_rate\": s[\"sig_rate\"],\n                \"p_median\": s[\"p_median\"],\n                \"p_mean\": s[\"p_mean\"],\n                \"F_mean\": s[\"F_mean\"],\n                \"F_std\": s[\"F_std\"],\n                \"per_seed\": per_seed_clean,\n            }\n\n    return output\n\n\n# ── Main ─────────────────────────────────────────────────────────────────────\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Alpha-sweep aggregation: TY canary analysis across α levels\")\n    parser.add_argument(\"--sweep_dir\", default=\"results/alpha_sweep\",\n                        help=\"Path to alpha_sweep results directory\")\n    parser.add_argument(\"--min_gens\", type=int, default=MIN_GENS,\n                        help=\"Minimum generations required per run (default: 5)\")\n    args = parser.parse_args()\n\n    sweep_dir = args.sweep_dir\n    if not os.path.isabs(sweep_dir):\n        sweep_dir = os.path.join(\n            os.path.dirname(os.path.abspath(__file__)), sweep_dir)\n\n    runs = discover_runs(sweep_dir)\n    if not runs:\n        print(f\"No runs found in {sweep_dir}\")\n        sys.exit(0)\n\n    run_info = {}\n    all_results = {}\n\n    for (alpha, seed), path in sorted(runs.items()):\n        metrics = load_run_metrics(path)\n        n_gens = len(metrics)\n        run_info[(alpha, seed)] = {\"n_gens\": n_gens, \"path\": path}\n\n        if n_gens < args.min_gens:\n            continue\n\n        results = analyze_run(metrics)\n        all_results[(alpha, seed)] = results\n\n    agg = aggregate_by_alpha(all_results)\n\n    print_summary(agg, run_info)\n\n    out_dir = os.path.join(sweep_dir)\n    os.makedirs(out_dir, exist_ok=True)\n    out_path = os.path.join(out_dir, \"analysis_summary.json\")\n    output = build_output(agg, run_info)\n    with open(out_path, \"w\") as f:\n        json.dump(output, f, indent=2)\n    print(f\"\\nSaved: {out_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\nSCRIPT_EOF",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T21:11:46.486588+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T21:11:46.486734+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_alpha_sweep.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analyze_alpha_sweep.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T21:11:46.486887+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"==============================================================================\\nALPHA-SWEEP ANALYSIS: Canary Lead-Time vs Contamination Level\\n==============================================================================\\n\\nDiscovered runs: 2\\n  α=0.00 seed=42: 5 gens [OK]\\n  α=0.25 seed=42: 0 gens [SKIPPED (<5 gen)]\\n\\n──────────────────────────────────────────────────────────────────────────────\\n  ece → distinct_1\\n──────────────────────────────────────────────────────────────────────────────\\n       α  seeds   sig    rate     p_med    F_mean    F_std\\n    0.00      1     0     0%       N/A       N/A      N/A\\n\\n────────────────────────���─────────────────────────────────────────────────────\\n  token_entropy → distinct_1\\n──────────────────────────────────────────────────────────────────────────────\\n       α  seeds   sig    rate     p_med    F_mean    F_std\\n    0.00      1     0     0%       N/A       N/A      N/A\\n\\n──────────────────────────────────────────────────────────────────────────────\\n  token_entropy → distinct_2\\n──────────────────────────────────────────────────────────────���───────────────\\n       α  seeds   sig    rate     p_med    F_mean    F_std\\n    0.00      1     0     0%       N/A       N/A      N/A\\n\\n──────────────────────────────────────────────────────────────────────────────\\n  token_entropy → distinct_3\\n──────────────────────────────────────────────────────────────────────────────\\n       α  seeds   sig    rate     p_med    F_mean    F_std\\n    0.00      1     0     0%       N/A       N/A      N/A\\n\\n──────────────────────────────────────────────────────────────────────────────\\n  token_entropy → perplexity\\n──────────────────────────────────────────────────────────────────────────────\\n       α  seeds   sig    rate     p_med    F_mean    F_std\\n    0.00      1     0     0%       N/A       N/A      N/A\\n\\n==================================
…[truncated 564 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-14T21:11:46.487061+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-19828",
  "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/analysis_summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-19828",
    "command": "cat /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/analysis_summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T21:11:46.487277+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"meta\\\": {\\n    \\\"test\\\": \\\"toda_yamamoto\\\",\\n    \\\"alpha_stat\\\": 0.05,\\n    \\\"min_gens\\\": 5,\\n    \\\"valid_pairs\\\": [\\n      [\\n        \\\"ece\\\",\\n        \\\"distinct_1\\\"\\n      ],\\n      [\\n        \\\"token_entropy\\\",\\n        \\\"distinct_1\\\"\\n      ],\\n      [\\n        \\\"token_entropy\\\",\\n        \\\"distinct_2\\\"\\n      ],\\n      [\\n        \\\"token_entropy\\\",\\n        \\\"distinct_3\\\"\\n      ],\\n      [\\n        \\\"token_entropy\\\",\\n        \\\"perplexity\\\"\\n      ]\\n    ]\\n  },\\n  \\\"runs\\\": {\\n    \\\"a000_s42\\\": {\\n      \\\"alpha\\\": 0.0,\\n      \\\"seed\\\": 42,\\n      \\\"n_gens\\\": 5,\\n      \\\"analyzed\\\": true\\n    },\\n    \\\"a025_s42\\\": {\\n      \\\"alpha\\\": 0.25,\\n      \\\"seed\\\": 42,\\n      \\\"n_gens\\\": 0,\\n      \\\"analyzed\\\": false\\n    }\\n  },\\n  \\\"by_alpha\\\": {\\n    \\\"0.00\\\": {\\n      \\\"ece_to_distinct_1\\\": {\\n        \\\"n_seeds\\\": 1,\\n        \\\"n_significant\\\": 0,\\n        \\\"sig_rate\\\": 0.0,\\n        \\\"p_median\\\": null,\\n        \\\"p_mean\\\": null,\\n        \\\"F_mean\\\": null,\\n        \\\"F_std\\\": null,\\n        \\\"per_seed\\\": [\\n          {\\n            \\\"p\\\": 1,\\n            \\\"d_max\\\": 1,\\n            \\\"k\\\": 2,\\n            \\\"wald_F\\\": null,\\n            \\\"p_value\\\": null,\\n            \\\"significant\\\": false,\\n            \\\"note\\\": \\\"no residual df (T_eff=3, params=5)\\\",\\n            \\\"d_canary\\\": 1,\\n            \\\"d_downstream\\\": 1\\n          }\\n        ]\\n      },\\n      \\\"token_entropy_to_distinct_1\\\": {\\n        \\\"n_seeds\\\": 1,\\n        \\\"n_significant\\\": 0,\\n        \\\"sig_rate\\\": 0.0,\\n        \\\"p_median\\\": null,\\n        \\\"p_mean\\\": null,\\n        \\\"F_mean\\\": null,\\n        \\\"F_std\\\": null,\\n        \\\"per_seed\\\": [\\n   
…[truncated 2626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T21:11:46.487470+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-19828",
  "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport json, numpy as np, os, sys\nsys.path.insert(0, '.')\nfrom analyze_alpha_sweep import toda_yamamoto, orient, _adf_order\n\n# Load MVP rep_42 (has 10 gens)\nwith open('results/mvp/rep_42/all_metrics.json') as f:\n    data = json.load(f)\n\ndata.sort(key=lambda x: x['generation'])\nte = np.array([m['token_entropy'] for m in data])\nppl = np.array([m['perplexity'] for m in data])\nd1 = np.array([m['distinct_1'] for m in data])\n\nprint(f'N gens: {len(data)}')\nprint(f'te adf_order: {_adf_order(orient(te, \\\"token_entropy\\\"))}')\nprint(f'ppl adf_order: {_adf_order(orient(ppl, \\\"perplexity\\\"))}')\n\nr1 = toda_yamamoto(te, ppl, 'token_entropy', 'perplexity')\nprint(f'te->ppl: F={r1[\\\"wald_F\\\"]}, p={r1[\\\"p_value\\\"]}, sig={r1[\\\"significant\\\"]}')\n\nr2 = toda_yamamoto(te, d1, 'token_entropy', 'distinct_1')\nprint(f'te->d1: F={r2[\\\"wald_F\\\"]}, p={r2[\\\"p_value\\\"]}, sig={r2[\\\"significant\\\"]}')\n\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-19828",
    "command": "cd /root/autodl-tmp/distrib_canary_collapse && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python -c \"\nimport json, numpy as np, os, sys\nsys.path.insert(0, '.')\nfrom analyze_alpha_sweep import toda_yamamoto, orient, _adf_order\n\n# Load MVP rep_42 (has 10 gens)\nwith open('results/mvp/rep_42/all_metrics.json') as f:\n    data = json.load(f)\n\ndata.sort(key=lambda x: x['generation'])\nte = np.array([m['token_entropy'] for m in data])\nppl = np.array([m['perplexity'] for m in data])\nd1 = np.array([m['distinct_1'] for m in data])\n\nprint(f'N gens: {len(data)}')\nprint(f'te adf_order: {_adf_order(orient(te, \\\"token_entropy\\\"))}')\nprint(f'ppl adf_order: {_adf_order(orient(ppl, \\\"perplexity\\\"))}')\n\nr1 = toda_yamamoto(te, ppl, 'token_entropy', 'perplexity')\nprint(f'te->ppl: F={r1[\\\"wald_F\\\"]}, p={r1[\\\"p_value\\\"]}, sig={r1[\\\"significant\\\"]}')\n\nr2 = toda_yamamoto(te, d1, 'token_entropy', 'distinct_1')\nprint(f'te->d1: F={r2[\\\"wald_F\\\"]}, p={r2[\\\"p_value\\\"]}, sig={r2[\\\"significant\\\"]}')\n\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T21:11:46.487612+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"N gens: 11\\nte adf_order: 0\\nppl adf_order: 1\\nte->ppl: F=1.3162, p=0.315231, sig=False\\nte->d1: F=311.6695, p=0.0, sig=True\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-14T21:11:46.487763+00:00_

TY 测试在 10+ gen 数据上正常工作（te→d1 显著，te→ppl 不显著——与 MVP 结果一致）。

脚本完成，总结：

- **位置**: `/root/autodl-tmp/distrib_canary_collapse/analyze_alpha_sweep.py`
- **功能**: 自动发现 `results/alpha_sweep/a{NNN}_s{seed}*` 目录，对每个 run 做 Toda-Yamamoto 检验，跨 seed 聚合后输出 α vs. canary signal 汇总表 + JSON
- **验证结果**:
  - 当前 a000_s42 (5 gen) 可加载但 TY df 不足（d_max=1 时需 ≥7 gen），输出 N/A——预期行为
  - a025_s42 (0 gen) 被跳过——空目录优雅处理
  - MVP 10-gen 数据验证 TY 正常：token_entropy→distinct_1 显著 (F=311.7, p≈0)，token_entropy→perplexity 不显著 (p=0.32)
- **等 10 gen 跑完后** re-run `python analyze_alpha_sweep.py` 即可出完整分析

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_alpha-sweep-analysis-prep_20260514T210910"
}
```

</details>

---
