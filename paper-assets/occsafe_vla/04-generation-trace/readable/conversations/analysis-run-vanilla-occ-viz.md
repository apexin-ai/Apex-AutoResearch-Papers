# analysis run vanilla occ viz

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_analysis_run-vanilla-occ-viz_20260521T193235.jsonl`
- **Structured JSON:** [`0cac47298d43de36a810.json`](../../sessions/0c/0cac47298d43de36a810.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-21T19:35:05.146902+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T19:35:05.147281+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T19:35:05.147472+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/occsafe_vla/eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/occsafe_vla/eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-21T19:35:05.147611+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/occsafe_vla/openvla-oft/analysis/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/occsafe_vla/openvla-oft/analysis/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-21T19:35:05.147809+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1200\\ndrwxr-xr-x  2 root root   4096 May 21 21:50 .\\ndrwxr-xr-x 14 root root   4096 May 21 21:27 ..\\n-rw-r--r--  1 root root    220 May 21 12:39 monitor_status.txt\\n-rw-r--r--  1 root root  96862 May 21 16:35 occ_s0_50000.json\\n-rw-r--r--  1 root root  24830 May 21 16:35 occ_s0_50000.log\\n-rw-r--r--  1 root root  24834 May 21 15:39 occ_s0_eval.log\\n-rw-r--r--  1 root root  96837 May 21 15:39 occ_s0_final.json\\n-rw-r--r--  1 root root  24911 May 21 19:27 occ_s1_30000.log\\n-rw-r--r--  1 root root  24911 May 21 19:29 occ_s1_35000.log\\n-rw-r--r--  1 root root  24911 May 21 19:33 occ_s1_40000.log\\n-rw-r--r--  1 root root  24910 May 21 21:03 occ_s1_45000.log\\n-rw-r--r--  1 root root  24910 May 21 22:08 occ_s1_50000_20r.log\\n-rw-r--r--  1 root root  96789 May 21 16:36 occ_s2_50000.json\\n-rw-r--r--  1 root root  24830 May 21 16:36 occ_s2_50000.log\\n-rw-r--r--  1 root root  24834 May 21 15:40 occ_s2_eval.log\\n-rw-r--r--  1 root root  96783 May 21 15:40 occ_s2_final.json\\n-rw-r--r--  1 root root 236170 May 21 18:20 vanilla_s0_50r.json\\n-rw-r--r--  1 root root  44942 May 21 18:20 vanilla_s0_50r.log\\n-rw-r--r--  1 root root 236310 May 21 18:23 vanilla_s1_50r.json\\n-rw-r--r--  1 root root  44942 May 21 18:23 vanilla_s1_50r.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.03}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T19:35:05.147970+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 348\\ndrwxr-xr-x 4 root root   4096 May 22 03:03 .\\ndrwxr-xr-x 8 root root   4096 May 22 02:53 ..\\ndrwxr-xr-x 2 root root     48 May 22 03:03 __pycache__\\n-rw-r--r-- 1 root root   6351 May 22 03:03 ablation_diagnostic.py\\n-rw-r--r-- 1 root root   8780 May 22 02:54 bootstrap_ci.py\\n-rw-r--r-- 1 root root   3034 May 22 03:02 eval_utils.py\\ndrwxr-xr-x 2 root root   4096 May 22 03:03 output\\n-rw-r--r-- 1 root root   2689 May 22 02:55 per_task_ci.csv\\n-rw-r--r-- 1 root root   2507 May 22 02:55 per_task_ci.tex\\n-rw-r--r-- 1 root root  45105 May 22 02:55 per_task_comparison.pdf\\n-rw-r--r-- 1 root root 244359 May 22 02:55 per_task_comparison.png\\n-rw-r--r-- 1 root root   5520 May 22 03:03 per_task_comparison.py\\n-rw-r--r-- 1 root root   4493 May 22 03:03 seed_instability.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T19:35:05.148155+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "head -80 /root/occsafe_vla/openvla-oft/analysis/per_task_comparison.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "head -80 /root/occsafe_vla/openvla-oft/analysis/per_task_comparison.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T19:35:05.148333+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\nimport argparse\\nimport json\\nfrom itertools import combinations\\nfrom pathlib import Path\\nimport numpy as np\\nfrom eval_utils import (\\n    TASK_SHORT, pool_binary, bootstrap_ci, bootstrap_diff_test,\\n    get_task_ids, parse_condition, setup_style,\\n)\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser()\\n    parser.add_argument(\\\"--conditions\\\", nargs=\\\"+\\\", required=True,\\n                        help=\\\"label:file1,file2,...\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=\\\"./output/\\\")\\n    parser.add_argument(\\\"--n_bootstrap\\\", type=int, default=10000)\\n    args = parser.parse_args()\\n\\n    plt = setup_style()\\n    outdir = Path(args.output_dir)\\n    outdir.mkdir(parents=True, exist_ok=True)\\n\\n    conditions = [parse_condition(c) for c in args.conditions]\\n    all_paths = [p for _, paths in conditions for p in paths]\\n    task_ids = get_task_ids(all_paths)\\n    labels = [l for l, _ in conditions]\\n    colors = plt.cm.tab10(np.linspace(0, 1, max(len(labels), 10)))[:len(labels)]\\n\\n    results = {}\\n    for label, paths in conditions:\\n        results[label] = {}\\n        for tid in task_ids:\\n            safe = pool_binary(paths, tid, \\\"safe_binary\\\")\\n            succ = pool_binary(paths, tid, \\\"success_binary\\\")\\n            tsr_m, tsr_lo, tsr_hi = bootstrap_ci(succ, args.n_bootstrap)\\n            car_m, car_lo, car_hi = bootstrap_ci(safe, args.n_bootstrap)\\n            results[label][tid] = dict(\\n                tsr_mean=tsr_m, tsr_lo=tsr_lo, tsr_hi=tsr_hi,\\n                car_mean=car_m, car_lo=car_lo, car_hi=car_hi,\\n            )\\n        print(f\\\"  [{label}] computed {len(task_ids)} tasks\\\")\\n\\n    def plot_grouped_bar(metric, ylabel, filename):\\n        fig, ax = plt.subplots(figsize=(14, 5))\\n        n_conds = len(labels)\\n        width = 0.8 / n_conds\\n        x = np.arange(len(
…[truncated 1698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T19:35:05.148483+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "head -80 /root/occsafe_vla/openvla-oft/analysis/seed_instability.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "head -80 /root/occsafe_vla/openvla-oft/analysis/seed_instability.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T19:35:05.148683+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\nimport argparse\\nimport json\\nfrom pathlib import Path\\nimport numpy as np\\nfrom eval_utils import (\\n    TASK_SHORT, seed_level_metric, get_task_ids, setup_style,\\n)\\n\\n\\ndef main():\\n    parser = argparse.ArgumentParser()\\n    parser.add_argument(\\\"--vanilla\\\", required=True, help=\\\"comma-separated JSON paths\\\")\\n    parser.add_argument(\\\"--occ\\\", required=True, help=\\\"comma-separated JSON paths\\\")\\n    parser.add_argument(\\\"--output_dir\\\", default=\\\"./output/\\\")\\n    args = parser.parse_args()\\n\\n    plt = setup_style()\\n    outdir = Path(args.output_dir)\\n    outdir.mkdir(parents=True, exist_ok=True)\\n\\n    van_paths = [p.strip() for p in args.vanilla.split(\\\",\\\") if p.strip()]\\n    occ_paths = [p.strip() for p in args.occ.split(\\\",\\\") if p.strip()]\\n    task_ids = get_task_ids(van_paths + occ_paths)\\n\\n    van_n = len(van_paths)\\n    occ_n = len(occ_paths)\\n\\n    van_stds, occ_stds = [], []\\n    stats = {}\\n    for tid in task_ids:\\n        v = seed_level_metric(van_paths, tid, \\\"car\\\")\\n        o = seed_level_metric(occ_paths, tid, \\\"car\\\")\\n        vs = float(np.std(v, ddof=1)) if len(v) > 1 else 0.0\\n        os_ = float(np.std(o, ddof=1)) if len(o) > 1 else 0.0\\n        ratio = os_ / vs if vs > 1e-9 else (float(\\\"inf\\\") if os_ > 1e-9 else float(\\\"nan\\\"))\\n        van_stds.append(vs)\\n        occ_stds.append(os_)\\n\\n        lev_p = float(\\\"nan\\\")\\n        try:\\n            from scipy.stats import levene\\n            if len(v) >= 2 and len(o) >= 2:\\n                _, lev_p = levene(v, o)\\n                lev_p = float(lev_p)\\n        except ImportError:\\n            pass\\n\\n        stats[TASK_SHORT[tid]] = dict(\\n            vanilla_std=round(vs, 4), occ_std=round(os_, 4),\\n            ratio=round(ratio, 4) if np.isfinite(ratio) else str(ratio),\\n            levene_p=round(lev_p,
…[truncated 1510 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T19:35:05.148867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "head -5 /root/occsafe_vla/eval_results/occ_s0_50000.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "head -5 /root/occsafe_vla/eval_results/occ_s0_50000.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T19:35:05.149007+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"checkpoint\\\": \\\"/root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\\",\\n    \\\"task_suite\\\": \\\"libero_spatial\\\",\\n    \\\"num_rollouts\\\": 20,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T19:35:05.149132+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "head -5 /root/occsafe_vla/eval_results/vanilla_s0_50r.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "head -5 /root/occsafe_vla/eval_results/vanilla_s0_50r.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T19:35:05.149261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"checkpoint\\\": \\\"/root/autodl-tmp/checkpoints/vanilla_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\\",\\n    \\\"task_suite\\\": \\\"libero_spatial\\\",\\n    \\\"num_rollouts\\\": 50,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T19:35:05.149420+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "head -5 /root/occsafe_vla/eval_results/occ_s0_final.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "head -5 /root/occsafe_vla/eval_results/occ_s0_final.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T19:35:05.149555+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"checkpoint\\\": \\\"/root/autodl-tmp/checkpoints/occ_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt\\\",\\n    \\\"task_suite\\\": \\\"libero_spatial\\\",\\n    \\\"num_rollouts\\\": 20,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T19:35:05.149695+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "head -5 /root/occsafe_vla/eval_results/occ_s2_50000.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "head -5 /root/occsafe_vla/eval_results/occ_s2_50000.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T19:35:05.149829+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"checkpoint\\\": \\\"/root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--50000_chkpt\\\",\\n    \\\"task_suite\\\": \\\"libero_spatial\\\",\\n    \\\"num_rollouts\\\": 20,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T19:35:05.149956+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "cat /root/occsafe_vla/openvla-oft/analysis/eval_utils.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "cat /root/occsafe_vla/openvla-oft/analysis/eval_utils.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T19:35:05.150124+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"import json\\nimport numpy as np\\n\\nTASK_SHORT = {i: f\\\"T{i}\\\" for i in range(10)}\\n\\n_cache = {}\\n\\n\\ndef load_eval_json(path):\\n    if path in _cache:\\n        return _cache[path]\\n    with open(path) as f:\\n        data = json.load(f)\\n    result = {}\\n    for task_name, task_data in data[\\\"tasks\\\"].items():\\n        tid = task_data[\\\"task_id\\\"]\\n        eps = task_data[\\\"episodes\\\"]\\n        result[tid] = {\\n            \\\"task_name\\\": task_name,\\n            \\\"tsr\\\": task_data[\\\"tsr\\\"],\\n            \\\"car\\\": task_data[\\\"car\\\"],\\n            \\\"n\\\": task_data[\\\"n\\\"],\\n            \\\"success_binary\\\": [int(e[\\\"success\\\"]) for e in eps],\\n            \\\"safe_binary\\\": [1 - int(e[\\\"collision\\\"]) for e in eps],\\n        }\\n    _cache[path] = result\\n    return result\\n\\n\\ndef pool_binary(json_paths, task_id, metric=\\\"safe_binary\\\"):\\n    pooled = []\\n    for p in json_paths:\\n        data = load_eval_json(p)\\n        if task_id in data:\\n            pooled.extend(data[task_id][metric])\\n    return np.array(pooled, dtype=float)\\n\\n\\ndef seed_level_metric(json_paths, task_id, metric=\\\"car\\\"):\\n    vals = []\\n    for p in json_paths:\\n        data = load_eval_json(p)\\n        if task_id in data:\\n            vals.append(data[task_id][metric])\\n    return np.array(vals)\\n\\n\\ndef bootstrap_ci(arr, n_bootstrap=10000, ci=0.95):\\n    arr = np.asarray(arr, dtype=float)\\n    n = len(arr)\\n    if n == 0:\\n        return np.nan, np.nan, np.nan\\n    rng = np.random.default_rng(42)\\n    idx = rng.integers(0, n, size=(n_bootstrap, n))\\n    boots = arr[idx].mean(axis=1)\\n    alpha = (1 - ci) / 2\\n    return float(arr.mean()), float(np.percentile(boots, alpha * 100)), float(np.percentile(boots, (1 - alpha) * 100))\\n\\n\\ndef bootstrap_diff_test(arr1, arr2, n_bootstrap=10000):\\n    arr1, arr2 = np.asarray(arr1
…[truncated 1594 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T19:35:05.150305+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "head -5 /root/occsafe_vla/eval_results/occ_s2_final.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "head -5 /root/occsafe_vla/eval_results/occ_s2_final.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T19:35:05.150440+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"checkpoint\\\": \\\"/root/autodl-tmp/checkpoints/occ_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--47500_chkpt\\\",\\n    \\\"task_suite\\\": \\\"libero_spatial\\\",\\n    \\\"num_rollouts\\\": 20,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T19:35:05.150620+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34685",
  "command": "cd /root/occsafe_vla/openvla-oft/analysis/ && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python per_task_comparison.py \\\n  --conditions \\\n    \"vanilla:/root/occsafe_vla/eval_results/vanilla_s0_50r.json,/root/occsafe_vla/eval_results/vanilla_s1_50r.json\" \\\n    \"occ_47500:/root/occsafe_vla/eval_results/occ_s0_final.json,/root/occsafe_vla/eval_results/occ_s2_final.json\" \\\n  --output_dir ./output/ \\\n  --n_bootstrap 10000",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34685",
    "command": "cd /root/occsafe_vla/openvla-oft/analysis/ && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python per_task_comparison.py \\\n  --conditions \\\n    \"vanilla:/root/occsafe_vla/eval_results/vanilla_s0_50r.json,/root/occsafe_vla/eval_results/vanilla_s1_50r.json\" \\\n    \"occ_47500:/root/occsafe_vla/eval_results/occ_s0_final.json,/root/occsafe_vla/eval_results/occ_s2_final.json\" \\\n  --output_dir ./output/ \\\n  --n_bootstrap 10000",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T19:35:05.150792+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [vanilla] computed 10 tasks\\n  [occ_47500] computed 10 tasks\\n  Saved per_task_tsr.pdf/png\\n  Saved per_task_car.pdf/png\\n  Saved hard_tasks.pdf/png\\n  Saved comparison_stats.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.99}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T19:35:05.150956+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-34685",
  "command": "cd /root/occsafe_vla/openvla-oft/analysis/ && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python seed_instability.py \\\n  --vanilla \"/root/occsafe_vla/eval_results/vanilla_s0_50r.json,/root/occsafe_vla/eval_results/vanilla_s1_50r.json\" \\\n  --occ \"/root/occsafe_vla/eval_results/occ_s0_final.json,/root/occsafe_vla/eval_results/occ_s2_final.json\" \\\n  --output_dir ./output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-34685",
    "command": "cd /root/occsafe_vla/openvla-oft/analysis/ && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python seed_instability.py \\\n  --vanilla \"/root/occsafe_vla/eval_results/vanilla_s0_50r.json,/root/occsafe_vla/eval_results/vanilla_s1_50r.json\" \\\n  --occ \"/root/occsafe_vla/eval_results/occ_s0_final.json,/root/occsafe_vla/eval_results/occ_s2_final.json\" \\\n  --output_dir ./output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T19:35:05.151091+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Saved seed_variance_heatmap.pdf/png\\n  Saved variance_ratio.pdf/png\\n  Saved instability_stats.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T19:35:05.151235+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "ls -la /root/occsafe_vla/openvla-oft/analysis/output/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "ls -la /root/occsafe_vla/openvla-oft/analysis/output/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T19:35:05.151372+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1032\\ndrwxr-xr-x 2 root root   4096 May 22 03:03 .\\ndrwxr-xr-x 4 root root   4096 May 22 03:03 ..\\n-rw-r--r-- 1 root root  22680 May 22 03:03 ablation_car_comparison.pdf\\n-rw-r--r-- 1 root root  90700 May 22 03:03 ablation_car_comparison.png\\n-rw-r--r-- 1 root root  22481 May 22 03:03 ablation_tsr_comparison.pdf\\n-rw-r--r-- 1 root root  87951 May 22 03:03 ablation_tsr_comparison.png\\n-rw-r--r-- 1 root root   2546 May 22 03:34 comparison_stats.json\\n-rw-r--r-- 1 root root  25275 May 22 03:03 diagnostic_matrix.pdf\\n-rw-r--r-- 1 root root 180933 May 22 03:03 diagnostic_matrix.png\\n-rw-r--r-- 1 root root   2191 May 22 03:03 diagnostic_report.json\\n-rw-r--r-- 1 root root  16623 May 22 03:34 hard_tasks.pdf\\n-rw-r--r-- 1 root root  66231 May 22 03:34 hard_tasks.png\\n-rw-r--r-- 1 root root   1390 May 22 03:34 instability_stats.json\\n-rw-r--r-- 1 root root  17453 May 22 03:34 per_task_car.pdf\\n-rw-r--r-- 1 root root  78645 May 22 03:34 per_task_car.png\\n-rw-r--r-- 1 root root  17202 May 22 03:34 per_task_tsr.pdf\\n-rw-r--r-- 1 root root  76268 May 22 03:34 per_task_tsr.png\\n-rw-r--r-- 1 root root  26854 May 22 03:34 seed_variance_heatmap.pdf\\n-rw-r--r-- 1 root root 148674 May 22 03:34 seed_variance_heatmap.png\\n-rw-r--r-- 1 root root  25183 May 22 03:34 variance_ratio.pdf\\n-rw-r--r-- 1 root root  89055 May 22 03:34 variance_ratio.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T19:35:05.151501+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "cat /root/occsafe_vla/openvla-oft/analysis/output/comparison_stats.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "cat /root/occsafe_vla/openvla-oft/analysis/output/comparison_stats.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-21T19:35:05.151616+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34685",
  "command": "cat /root/occsafe_vla/openvla-oft/analysis/output/instability_stats.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34685",
    "command": "cat /root/occsafe_vla/openvla-oft/analysis/output/instability_stats.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-21T19:35:05.151843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"T0\\\": {\\n    \\\"vanilla_vs_occ_47500\\\": {\\n      \\\"tsr_diff\\\": 0.0,\\n      \\\"tsr_ci\\\": [\\n        0.0,\\n        0.0\\n      ],\\n      \\\"tsr_p\\\": 1.0,\\n      \\\"car_diff\\\": 0.03,\\n      \\\"car_ci\\\": [\\n        -0.03,\\n        0.115\\n      ],\\n      \\\"car_p\\\": 0.5519\\n    }\\n  },\\n  \\\"T1\\\": {\\n    \\\"vanilla_vs_occ_47500\\\": {\\n      \\\"tsr_diff\\\": 0.065,\\n      \\\"tsr_ci\\\": [\\n        -0.04,\\n        0.185\\n      ],\\n      \\\"tsr_p\\\": 0.5033,\\n      \\\"car_diff\\\": 0.005,\\n      \\\"car_ci\\\": [\\n        -0.085,\\n        0.105\\n      ],\\n      \\\"car_p\\\": 0.9621\\n    }\\n  },\\n  \\\"T2\\\": {\\n    \\\"vanilla_vs_occ_47500\\\": {\\n      \\\"tsr_diff\\\": 0.035,\\n      \\\"tsr_ci\\\": [\\n        -0.045,\\n        0.13\\n      ],\\n      \\\"tsr_p\\\": 0.5665,\\n      \\\"car_diff\\\": 0.035,\\n      \\\"car_ci\\\": [\\n        -0.075,\\n        0.155\\n      ],\\n      \\\"car_p\\\": 0.6265\\n    }\\n  },\\n  \\\"T3\\\": {\\n    \\\"vanilla_vs_occ_47500\\\": {\\n      \\\"tsr_diff\\\": 0.025,\\n      \\\"tsr_ci\\\": [\\n        0.0,\\n        0.075\\n      ],\\n      \\\"tsr_p\\\": 0.6406,\\n      \\\"car_diff\\\": 0.095,\\n      \\\"car_ci\\\": [\\n        -0.075,\\n        0.265\\n      ],\\n      \\\"car_p\\\": 0.5333\\n    }\\n  },\\n  \\\"T4\\\": {\\n    \\\"vanilla_vs_occ_47500\\\": {\\n      \\\"tsr_diff\\\": -0.04,\\n      \\\"tsr_ci\\\": [\\n        -0.15,\\n        0.08\\n      ],\\n      \\\"tsr_p\\\": 0.6026,\\n      \\\"car_diff\\\": -0.01,\\n      \\\"car_ci\\\": [\\n        -0.03,\\n        0.0\\n      ],\\n      \\\"car_p\\\": 0.6316\\n    }\\n  },\\n  \\\"T5\\\": {\\n    \\\"vanilla_vs_occ_47500\\\": {\\n      \\\"tsr_diff\\\": -0.125,\\n      \\\"tsr_ci\\\": [\\n        -0.305,\\n        0.06\\n      ],\\n      \\\"tsr_p\\\": 0.5129,\\n      \\\"car_diff\\\": -0.08,\\n      \\\"car_ci\\\": [\\n        -0.2
…[truncated 1508 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T19:35:05.152056+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"T0\\\": {\\n    \\\"vanilla_std\\\": 0.0,\\n    \\\"occ_std\\\": 0.0,\\n    \\\"ratio\\\": \\\"nan\\\",\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T1\\\": {\\n    \\\"vanilla_std\\\": 0.0424,\\n    \\\"occ_std\\\": 0.1061,\\n    \\\"ratio\\\": 2.5,\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T2\\\": {\\n    \\\"vanilla_std\\\": 0.0141,\\n    \\\"occ_std\\\": 0.0354,\\n    \\\"ratio\\\": 2.5,\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T3\\\": {\\n    \\\"vanilla_std\\\": 0.1556,\\n    \\\"occ_std\\\": 0.1061,\\n    \\\"ratio\\\": 0.6818,\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T4\\\": {\\n    \\\"vanilla_std\\\": 0.0141,\\n    \\\"occ_std\\\": 0.0,\\n    \\\"ratio\\\": 0.0,\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T5\\\": {\\n    \\\"vanilla_std\\\": 0.0141,\\n    \\\"occ_std\\\": 0.0707,\\n    \\\"ratio\\\": 5.0,\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T6\\\": {\\n    \\\"vanilla_std\\\": 0.0424,\\n    \\\"occ_std\\\": 0.0707,\\n    \\\"ratio\\\": 1.6667,\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T7\\\": {\\n    \\\"vanilla_std\\\": 0.0424,\\n    \\\"occ_std\\\": 0.0,\\n    \\\"ratio\\\": 0.0,\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T8\\\": {\\n    \\\"vanilla_std\\\": 0.0,\\n    \\\"occ_std\\\": 0.0,\\n    \\\"ratio\\\": \\\"nan\\\",\\n    \\\"levene_p\\\": null,\\n    \\\"vanilla_n\\\": 2,\\n    \\\"occ_n\\\": 2\\n  },\\n  \\\"T9\\\": {\\n    \\\"vanilla_std\\\": 0.0,\\n    \\\"occ_std\\\": 0.0,\\n    \\\"ratio\\\": \\\"nan\\\",\\n    \\\"levene_p\\\": null,\\n    \\\"vani
…[truncated 150 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-21T19:35:05.152259+00:00_

所有脚本运行完毕。汇总如下：

## 产出文件

`/root/occsafe_vla/openvla-oft/analysis/output/` 下新生成 10 个文件，均 >10KB：

| 文件 | 大小 |
|------|------|
| per_task_tsr.pdf/png | 17KB / 76KB |
| per_task_car.pdf/png | 17KB / 79KB |
| hard_tasks.pdf/png | 17KB / 66KB |
| seed_variance_heatmap.pdf/png | 27KB / 149KB |
| variance_ratio.pdf/png | 25KB / 89KB |
| comparison_stats.json | 2.5KB |
| instability_stats.json | 1.4KB |

## comparison_stats.json 关键发现

**没有任何 task 的 TSR 或 CAR 差异达到统计显著性**（所有 p > 0.49）。

方向性趋势（不显著）：
- **T6 CAR**: OCC 比 vanilla 高 +0.25（CI [0.075, 0.42]）— 最大的 CAR 改善信号，但 p=0.52
- **T5 TSR**: OCC 比 vanilla 低 -0.125（CI [-0.305, 0.06]）— 最大的 TSR 下降信号
- **T7 TSR**: OCC 比 vanilla 低 -0.06（CI [-0.11, -0.02]）
- T0/T8/T9 CAR 差异为 0 或接近 0（天花板效应，两组都近 1.0）

## instability_stats.json 关键发现

N=2 per group，Levene 检验全部无法计算（样本太小）。

OCC vs Vanilla 方差比（ratio = occ_std / vanilla_std）：
- **T5**: ratio=5.0（OCC 方差远高于 vanilla）
- **T1, T2**: ratio=2.5
- **T6**: ratio=1.67
- **T3**: ratio=0.68（OCC 方差反而更低）
- **T4, T7**: ratio=0.0（OCC std=0）
- **T0, T8, T9**: ratio=nan（两组 std=0）

## 数据局限

- **Vanilla 缺 s2**，仅 2 seeds（s0, s1 各 50r）
- **OCC 仅 20r/seed**（非 50r），且仅 2 seeds（s0, s2 at ckpt 47500）
- 每组仅 N=2 seeds，方差估计和显著性检验统计功效极低，所有结论需谨慎解读

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_run-vanilla-occ-viz_20260521T193235"
}
```

</details>

---
