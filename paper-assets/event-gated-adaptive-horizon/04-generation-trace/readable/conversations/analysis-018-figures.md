# analysis 018 figures

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_analysis_018-figures_20260516T124339.jsonl`
- **Structured JSON:** [`e6c1ba773393d0ea12ea.json`](../../sessions/e6/e6c1ba773393d0ea12ea.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-16T12:45:10.878835+00:00_

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
  "session": "worker_analysis_018-figures_20260516T124339",
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

_source line 2 · 2026-05-16T12:45:10.879331+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T12:45:10.879654+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/logdir/ | grep -E \"018|008|016|baseline\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/logdir/ | grep -E \"018|008|016|baseline\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T12:45:10.879914+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T12:45:10.880158+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/logdir/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/logdir/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T12:45:10.880406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"aggregate_walker.py\\nanalysis_actor_entropy_value_calibration.json\\nanalysis_rssm_prediction_quality.json\\nanalysis_rssm_prediction_quality.py\\nanalyze_entropy.py\\nbaseline_s1\\nbaseline_s1.log\\ncheetah_dryrun_200step\\nevent_gated_s1.log\\nevent_gated_s1_v1_failed\\nevent_gated_s1_v2\\nevent_gated_v4_s1\\nevent_gated_v5_s1\\nexp_008a_fixed_dt2_no_subsample\\nexp_008c_fixed_dt2_no_subsample_h8\\nexp_008d_subsample_on_h8\\nexp_008e_v2_contaminated_20260514_1228\\nexp_008e_v2_dead_20260514_1227\\nexp_008e_v3_subsample_on_dt1_h15\\nexp_008e_v3_walker_s1\\nexp_008e_v3_walker_s2\\nexp_008f_no_dt_embed_subsample_on_h8\\nexp_009a_baseline_walker_s2\\nexp_009b_008d_walker_s2\\nexp_009c_008f_walker_s2\\nexp_009d_baseline_walker_s0\\nexp_009d_baseline_walker_s1\\nexp_009e_008d_walker_s1\\nexp_009f_008f_walker_s1\\nexp_009h_008f_walker_s0\\nexp_010a_cheetah_baseline_s1\\nexp_015b_frozen_dt_emb\\nexp_015b_frozen_dt_emb_bak_1778847895\\nexp_016b_sgs_walker_s1\\nexp_016d_sgs_walker_s1\\nexp_016e_sgs_walker_s1\\nexp_018_full_sgs_walker_s1\\nextract_all_metrics.py\\nfixed_dt2_v1_s1\\nfixed_dt4_diag\\nfixed_dt4_v1_s1\\nfixed_dt4_v2_s1\\nfullsgs_dryrun\\npaper_data_walker_walk.json\\npaper_figure_data.json\\npaper_figure_data_compact.json\\nplan015_dryrun\\nplan017_dryrun\\ntest_cuda1_eval_osmesa\\ntest_full_sgs\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.28}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T12:45:10.880689+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "head -80 /root/autodl-tmp/event-gated-adaptive-horizon/scripts/analyze_018_full_sgs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "head -80 /root/autodl-tmp/event-gated-adaptive-horizon/scripts/analyze_018_full_sgs.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T12:45:10.880986+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Exp-018 Full-SGS analysis: eval curves, NVE trajectories, CIVO verdict.\\n\\nCompares exp_018 (full_sgs=True, 93% gradient detach) against reference\\nexperiments to determine whether CIVO is gradient-level or representation-level.\\n\\nOutputs:\\n  - 018_eval_comparison.{pdf,png}   — learning curves overlay\\n  - 018_nve_comparison.{pdf,png}    — NVE trajectories with 1.5x threshold\\n  - 018_summary.json                — machine-readable results\\n  - stdout summary table\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nfrom collections import OrderedDict\\n\\nimport matplotlib\\nmatplotlib.use(\\\"Agg\\\")\\nimport matplotlib.pyplot as plt\\nimport matplotlib.ticker as ticker\\n\\n\\n# ---------------------------------------------------------------------------\\n# Data loading\\n# ---------------------------------------------------------------------------\\n\\ndef load_metrics_jsonl(logdir):\\n    path = os.path.join(logdir, \\\"metrics.jsonl\\\")\\n    if not os.path.exists(path):\\n        return None, None\\n    eval_returns = {}\\n    value_means = {}\\n    with open(path) as f:\\n        for line in f:\\n            line = line.strip()\\n            if not line:\\n                continue\\n            d = json.loads(line)\\n            step = d.get(\\\"step\\\")\\n            if step is None:\\n                continue\\n            if \\\"eval_return\\\" in d:\\n                eval_returns[step] = d[\\\"eval_return\\\"]\\n            if \\\"value_mean\\\" in d:\\n                value_means[step] = d[\\\"value_mean\\\"]\\n    return eval_returns, value_means\\n\\n\\ndef load_eval_returns(logdir):\\n    er, _ = load_metrics_jsonl(logdir)\\n    if er is None:\\n        print(f\\\"WARNING: no metrics.jsonl in {logdir}\\\", file=sys.stderr)\\n        return {}\\n    return er\\n\\n\\ndef load_ve_data(logdir):\\n    er, vm = load_metrics_jso
…[truncated 782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T12:45:10.881248+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -n \"argparse\\|add_argument\\|parse_args\" /root/autodl-tmp/event-gated-adaptive-horizon/scripts/analyze_018_full_sgs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "grep -n \"argparse\\|add_argument\\|parse_args\" /root/autodl-tmp/event-gated-adaptive-horizon/scripts/analyze_018_full_sgs.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T12:45:10.881452+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T12:45:10.881644+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "grep -n \"add_argument\" /root/autodl-tmp/event-gated-adaptive-horizon/scripts/analyze_018_full_sgs.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "grep -n \"add_argument\" /root/autodl-tmp/event-gated-adaptive-horizon/scripts/analyze_018_full_sgs.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T12:45:10.881870+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"278:    parser.add_argument(\\\"--logdir-018\\\", required=True,\\n280:    parser.add_argument(\\\"--logdir-008d\\\", default=None,\\n282:    parser.add_argument(\\\"--logdir-008f\\\", default=None,\\n284:    parser.add_argument(\\\"--logdir-016e\\\", default=None,\\n286:    parser.add_argument(\\\"--baseline-logdir\\\", required=True,\\n288:    parser.add_argument(\\\"--output-dir\\\", default=\\\".\\\",\\n290:    parser.add_argument(\\\"--nve-threshold\\\", type=float, default=1.5,\\n292:    parser.add_argument(\\\"--min-consecutive\\\", type=int, default=2,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T12:45:10.882148+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "bjb1-45299",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && mkdir -p figures/paper && python scripts/analyze_018_full_sgs.py --logdir-018 logdir/exp_018_full_sgs_walker_s1 --logdir-008d logdir/exp_008d_subsample_on_h8 --logdir-008f logdir/exp_008f_no_dt_embed_subsample_on_h8 --logdir-016e logdir/exp_016e_sgs_walker_s1 --baseline-logdir logdir/baseline_s1 --output-dir figures/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && mkdir -p figures/paper && python scripts/analyze_018_full_sgs.py --logdir-018 logdir/exp_018_full_sgs_walker_s1 --logdir-008d logdir/exp_008d_subsample_on_h8 --logdir-008f logdir/exp_008f_no_dt_embed_subsample_on_h8 --logdir-016e logdir/exp_016e_sgs_walker_s1 --baseline-logdir logdir/baseline_s1 --output-dir figures/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T12:45:10.882394+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\n==========================================================================================\\n  EXP-018 FULL-SGS ANALYSIS\\n==========================================================================================\\n\\n  018 verdict: CIVO_ABSENT\\n  Detail: NVE always <= 1.5x (max 1.000x)\\n\\n  -> CIVO is GRADIENT-LEVEL: removing 93% of gradients eliminates collapse\\n    -> obs decoder gradients are a necessary condition for CIVO\\n    -> Paper claim C2 strengthened\\n\\n==========================================================================================\\n  SUMMARY TABLE\\n==========================================================================================\\n  Exp                             Peak Eval  Final Eval   Max NVE  Verdict\\n  --------------------------------------------------------------------------------------\\n  018                                 915.7       915.7    1.0000  CIVO_ABSENT\\n  008d                                167.2        82.8    4.1292  CIVO_PRESENT\\n  008f                                503.2       503.2    1.0198  CIVO_ABSENT\\n  016e                                326.7        69.0   10.4166  CIVO_PRESENT\\n  baseline                            970.4       970.4    1.0000  CIVO_ABSENT\\n\\nSaved eval curves to figures/paper//018_eval_comparison.{pdf,png}\\nSaved NVE curves to figures/paper//018_nve_comparison.{pdf,png}\\nSaved JSON summary to figures/paper/018_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T12:45:10.882632+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/scripts/plot_018_results.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "ls /root/autodl-tmp/event-gated-adaptive-horizon/scripts/plot_018_results.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T12:45:10.882857+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/event-gated-adaptive-horizon/scripts/plot_018_results.py': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.35}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T12:45:10.883068+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "find /root/autodl-tmp/event-gated-adaptive-horizon/scripts/ -name \"*plot*018*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "find /root/autodl-tmp/event-gated-adaptive-horizon/scripts/ -name \"*plot*018*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T12:45:10.883280+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T12:45:10.883506+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "ls -la /root/autodl-tmp/event-gated-adaptive-horizon/figures/paper/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "ls -la /root/autodl-tmp/event-gated-adaptive-horizon/figures/paper/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T12:45:10.883726+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 228\\ndrwxr-xr-x 2 root root   176 May 16 20:44 .\\ndrwxr-xr-x 3 root root  4096 May 16 20:44 ..\\n-rw-r--r-- 1 root root 19746 May 16 20:44 018_eval_comparison.pdf\\n-rw-r--r-- 1 root root 93195 May 16 20:44 018_eval_comparison.png\\n-rw-r--r-- 1 root root 19630 May 16 20:44 018_nve_comparison.pdf\\n-rw-r--r-- 1 root root 86159 May 16 20:44 018_nve_comparison.png\\n-rw-r--r-- 1 root root  3133 May 16 20:44 018_summary.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.34}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T12:45:10.884070+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-45299",
  "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/figures/paper/018_summary.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-45299",
    "command": "cat /root/autodl-tmp/event-gated-adaptive-horizon/figures/paper/018_summary.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T12:45:10.884435+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"018_full_sgs\\\",\\n  \\\"nve_threshold\\\": 1.5,\\n  \\\"min_consecutive_checkpoints\\\": 2,\\n  \\\"verdict_018\\\": \\\"CIVO_ABSENT\\\",\\n  \\\"verdict_detail\\\": \\\"NVE always <= 1.5x (max 1.000x)\\\",\\n  \\\"interpretation\\\": \\\"gradient-level: Full-SGS eliminates CIVO\\\",\\n  \\\"summaries\\\": [\\n    {\\n      \\\"exp_id\\\": \\\"018\\\",\\n      \\\"peak_eval\\\": 915.67,\\n      \\\"final_eval\\\": 915.67,\\n      \\\"max_NVE\\\": 1.0,\\n      \\\"CIVO_verdict\\\": \\\"CIVO_ABSENT\\\"\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"008d\\\",\\n      \\\"peak_eval\\\": 167.22,\\n      \\\"final_eval\\\": 82.75,\\n      \\\"max_NVE\\\": 4.1292,\\n      \\\"CIVO_verdict\\\": \\\"CIVO_PRESENT\\\"\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"008f\\\",\\n      \\\"peak_eval\\\": 503.21,\\n      \\\"final_eval\\\": 503.21,\\n      \\\"max_NVE\\\": 1.0198,\\n      \\\"CIVO_verdict\\\": \\\"CIVO_ABSENT\\\"\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"016e\\\",\\n      \\\"peak_eval\\\": 326.67,\\n      \\\"final_eval\\\": 69.03,\\n      \\\"max_NVE\\\": 10.4166,\\n      \\\"CIVO_verdict\\\": \\\"CIVO_PRESENT\\\"\\n    },\\n    {\\n      \\\"exp_id\\\": \\\"baseline\\\",\\n      \\\"peak_eval\\\": 970.41,\\n      \\\"final_eval\\\": 970.41,\\n      \\\"max_NVE\\\": 1.0,\\n      \\\"CIVO_verdict\\\": \\\"CIVO_ABSENT\\\"\\n    }\\n  ],\\n  \\\"nve_trajectories\\\": {\\n    \\\"018\\\": {\\n      \\\"5000\\\": 1.0,\\n      \\\"15000\\\": 1.0,\\n      \\\"25000\\\": 1.0,\\n      \\\"35000\\\": 1.0,\\n      \\\"45000\\\": 1.0,\\n      \\\"55000\\\": 1.0,\\n      \\\"65000\\\": 1.0,\\n      \\\"75000\\\": 1.0,\\n      \\\"85000\\\": 1.0,\\n      \\\"95000\\\": 1.0,\\n      \\\"105000\\\": 1.0\\n    },\\n    \\\"008d\\\": {\\n      \\\"5000\\\": 0.796664,\\n      \\\"15000\\\": 0.846407,\\n      \\\"25000\\\": 1.772749,\\n      \\\"35000\\\": 1.70528,\\n      \\\"45000\\\": 2.093256,
…[truncated 2437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_018-figures_20260516T124339",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-16T12:45:10.884797+00:00_

完成。生成的产出：

**文件** (`figures/paper/`):
- `018_eval_comparison.pdf` / `.png` — 学习曲线对比图
- `018_nve_comparison.pdf` / `.png` — NVE 轨迹图
- `018_summary.json` — 机器可读结果

**`plot_018_results.py` 不存在**，已跳过。

---

**018_summary.json 完整内容：**

```json
{
  "experiment": "018_full_sgs",
  "nve_threshold": 1.5,
  "min_consecutive_checkpoints": 2,
  "verdict_018": "CIVO_ABSENT",
  "verdict_detail": "NVE always <= 1.5x (max 1.000x)",
  "interpretation": "gradient-level: Full-SGS eliminates CIVO",
  "summaries": [
    {"exp_id": "018", "peak_eval": 915.67, "final_eval": 915.67, "max_NVE": 1.0, "CIVO_verdict": "CIVO_ABSENT"},
    {"exp_id": "008d", "peak_eval": 167.22, "final_eval": 82.75, "max_NVE": 4.1292, "CIVO_verdict": "CIVO_PRESENT"},
    {"exp_id": "008f", "peak_eval": 503.21, "final_eval": 503.21, "max_NVE": 1.0198, "CIVO_verdict": "CIVO_ABSENT"},
    {"exp_id": "016e", "peak_eval": 326.67, "final_eval": 69.03, "max_NVE": 10.4166, "CIVO_verdict": "CIVO_PRESENT"},
    {"exp_id": "baseline", "peak_eval": 970.41, "final_eval": 970.41, "max_NVE": 1.0, "CIVO_verdict": "CIVO_ABSENT"}
  ],
  "nve_trajectories": {
    "018": {"5000": 1.0, "15000": 1.0, "25000": 1.0, "35000": 1.0, "45000": 1.0, "55000": 1.0, "65000": 1.0, "75000": 1.0, "85000": 1.0, "95000": 1.0, "105000": 1.0},
    "008d": {"5000": 0.797, "15000": 0.846, "25000": 1.773, "35000": 1.705, "45000": 2.093, "55000": 4.129},
    "008f": {"5000": 0.810, "15000": 0.633, "25000": 1.020, "35000": 0.728, "45000": 0.832, "55000": 0.970, "65000": 0.367, "75000": 0.422, "85000": 0.649, "95000": 0.535, "105000": 0.297},
    "016e": {"5000": 0.797, "15000": 0.851, "25000": 1.857, "35000": 1.283, "45000": 1.401, "55000": 1.863, "65000": 0.834, "75000": 0.809, "85000": 1.200, "95000": 10.417, "105000": 3.804},
    "baseline": {"5000": 1.0, ... "505000": 1.0}
  }
}
```

**核心结论**: Exp-018 (Full-SGS, 93% gradient detach) verdict = **CIVO_ABSENT**，NVE 恒为 1.0。CIVO 是 gradient-level 现象——obs decoder 梯度是 CIVO 的必要条件，Paper claim C2 strengthened。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_018-figures_20260516T124339"
}
```

</details>

---
