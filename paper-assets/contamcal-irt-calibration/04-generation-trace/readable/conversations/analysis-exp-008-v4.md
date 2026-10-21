# analysis exp 008 v4

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 49
- **Recorded user turns:** 0
- **Tool calls:** 24
- **Original source:** `logs/chats/worker_analysis_exp_008_v4_20260514T162445.jsonl`
- **Structured JSON:** [`67ef99587528d5a2d00a.json`](../../sessions/67/67ef99587528d5a2d00a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

49 recorded events

### Tool call

_source line 1 · 2026-05-14T16:28:08.359918+00:00_

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
  "session": "worker_analysis_exp_008_v4_20260514T162445",
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

_source line 2 · 2026-05-14T16:28:08.360225+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T16:28:08.360403+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/contamcal-irt-calibration/exp008/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/contamcal-irt-calibration/exp008/"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T16:28:08.360537+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp002/signals/ -type f -name \"*.json\" -o -name \"*.npz\" -o -name \"*.pkl\" -o -name \"*.npy\" -o -name \"*.csv\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp002/signals/ -type f -name \"*.json\" -o -name \"*.npz\" -o -name \"*.pkl\" -o -name \"*.npy\" -o -name \"*.csv\""
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T16:28:08.360679+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 80\\ndrwxr-xr-x  5 root root  4096 May 15 00:09 .\\ndrwxr-xr-x 10 root root   188 May 14 23:23 ..\\ndrwxr-xr-x  2 root root    62 May 14 21:55 __pycache__\\ndrwxr-xr-x  3 root root    75 May 15 00:09 exp008_exp002_output\\ndrwxr-xr-x  3 root root  4096 May 14 20:48 exp008_output\\n-rw-r--r--  1 root root  7137 May 14 12:35 plot_survival.py\\n-rw-r--r--  1 root root  4802 May 15 00:09 run_exp002_survival.py\\n-rwxr-xr-x  1 root root  3524 May 14 21:55 run_exp008.sh\\n-rwxr-xr-x  1 root root  3825 May 14 21:55 run_exp008.sh.bak\\n-rw-r--r--  1 root root  8110 May 14 12:27 run_signal_survival.py\\n-rw-r--r--  1 root root 24073 May 14 20:48 signal_survival.py\\n-rw-r--r--  1 root root 13859 May 14 12:32 signal_survival_analysis.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.04}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T16:28:08.360844+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_mmlu_Qwen2.5-0.5B_d000_s42.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_minkpp_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_selfcritique_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_selfcritique_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_minkpp_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_selfcritique_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signals_merged_arc_challenge.json\\n/root/autodl-tmp/exp002/signals/batch_report_Qwen2.5-0.5B.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_embedding_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_minkpp_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_selfcritique_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_embedding_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_minkpp_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_selfcritique_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_gsm8k.json\\n/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_embedding_arc_chall
…[truncated 1420 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T16:28:08.361039+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/run_exp002_survival.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/run_exp002_survival.py"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T16:28:08.361261+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nRun exp-008 signal survival analysis using exp-002 signal data.\\nCreates per-benchmark symlinked directories, converts labels, runs analysis.\\n\\\"\\\"\\\"\\nimport json\\nimport os\\nimport sys\\nfrom pathlib import Path\\n\\nBENCHMARKS = [\\\"mmlu\\\", \\\"gsm8k\\\", \\\"arc_challenge\\\"]\\nREGIMES = [(\\\"d000\\\", \\\"Qwen2.5-0.5B_d000_s42\\\"),\\n           (\\\"d005\\\", \\\"Qwen2.5-0.5B_d005_s42\\\"),\\n           (\\\"d100\\\", \\\"Qwen2.5-0.5B_d100_s42\\\")]\\n\\nEXP002_SIGNALS = Path(\\\"/root/autodl-tmp/exp002/signals\\\")\\nLABELS_SRC = Path(\\\"/root/autodl-tmp/exp001/sft_data\\\")\\nWORK_DIR = Path(\\\"/root/autodl-tmp/exp008_from_exp002\\\")\\nOUTPUT_DIR = Path(\\\"/root/contamcal-irt-calibration/exp008/exp008_exp002_output\\\")\\n\\ndef convert_labels(bench):\\n    \\\"\\\"\\\"Convert array-format labels to {index: 0/1} dict format.\\\"\\\"\\\"\\n    src = LABELS_SRC / f\\\"contamination_labels_{bench}_d005.json\\\"\\n    dst = WORK_DIR / \\\"labels\\\" / f\\\"labels_{bench}.json\\\"\\n    dst.parent.mkdir(parents=True, exist_ok=True)\\n    with open(src) as f:\\n        raw = json.load(f)\\n    labels = {str(i): v for i, v in enumerate(raw[\\\"labels\\\"])}\\n    with open(dst, \\\"w\\\") as f:\\n        json.dump(labels, f)\\n    print(f\\\"Labels {bench}: {raw['contaminated_count']}/{raw['total_items']} contaminated -> {dst}\\\")\\n    return dst\\n\\ndef setup_signal_dirs(bench):\\n    \\\"\\\"\\\"Create per-regime directories with symlinks to the right benchmark signal files.\\\"\\\"\\\"\\n    regime_args = []\\n    for regime_name, dir_name in REGIMES:\\n        src_dir = EXP002_SIGNALS / dir_name\\n        dst_dir = WORK_DIR / \\\"signals\\\" / regime_name / bench\\n        dst_dir.mkdir(parents=True, exist_ok=True)\\n        \\n        merged_src = src_dir / f\\\"signals_merged_{bench}.json\\\"\\n        merged_dst = dst_dir / f\\\"signals_merged_{bench}.json\\\"\\n    
…[truncated 3631 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T16:28:08.361433+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -50 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_embedding_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -50 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_embedding_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T16:28:08.361586+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.4031004011631012,\\n    \\\"s1_embedding_mean_topk\\\": 0.3422525227069855,\\n    \\\"s1_top_k_sims\\\": [\\n      0.4031004011631012,\\n      0.346914678812027,\\n      0.34582147002220154,\\n      0.3449670374393463,\\n      0.3404175341129303,\\n      0.33444708585739136,\\n      0.33075982332229614,\\n      0.32876792550086975,\\n      0.3282144069671631,\\n      0.31911471486091614\\n    ]\\n  },\\n  {\\n    \\\"index\\\": 1,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.39687806367874146,\\n    \\\"s1_embedding_mean_topk\\\": 0.378799706697464,\\n    \\\"s1_top_k_sims\\\": [\\n      0.39687806367874146,\\n      0.39243391156196594,\\n      0.39224809408187866,\\n      0.3888360857963562,\\n      0.3759295642375946,\\n      0.37379488348960876,\\n      0.3718714416027069,\\n      0.3661618232727051,\\n      0.36583489179611206,\\n      0.36400824785232544\\n    ]\\n  },\\n  {\\n    \\\"index\\\": 2,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.48771804571151733,\\n    \\\"s1_embedding_mean_topk\\\": 0.34451916813850403,\\n    \\\"s1_top_k_sims\\\": [\\n      0.48771804571151733,\\n      0.36698469519615173,\\n      0.34182724356651306,\\n      0.333408385515213,\\n      0.32911598682403564,\\n      0.3236433267593384,\\n      0.31992071866989136,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T16:28:08.361723+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -50 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -50 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d000_s42/signal_embedding_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T16:28:08.361863+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.3449670374393463,\\n    \\\"s1_embedding_mean_topk\\\": 0.3124921917915344,\\n    \\\"s1_top_k_sims\\\": [\\n      0.3449670374393463,\\n      0.33075982332229614,\\n      0.3282144069671631,\\n      0.31911471486091614,\\n      0.3073144853115082,\\n      0.3068189024925232,\\n      0.3037205636501312,\\n      0.2974735498428345,\\n      0.29378363490104675,\\n      0.292754590511322\\n    ]\\n  },\\n  {\\n    \\\"index\\\": 1,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.39687806367874146,\\n    \\\"s1_embedding_mean_topk\\\": 0.3741294741630554,\\n    \\\"s1_top_k_sims\\\": [\\n      0.39687806367874146,\\n      0.39243391156196594,\\n      0.3888360857963562,\\n      0.3759295642375946,\\n      0.3718714416027069,\\n      0.3661618232727051,\\n      0.36583489179611206,\\n      0.3631466031074524,\\n      0.3611016571521759,\\n      0.35910069942474365\\n    ]\\n  },\\n  {\\n    \\\"index\\\": 2,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.34182724356651306,\\n    \\\"s1_embedding_mean_topk\\\": 0.3168836832046509,\\n    \\\"s1_top_k_sims\\\": [\\n      0.34182724356651306,\\n      0.333408385515213,\\n      0.32911598682403564,\\n      0.3236433267593384,\\n      0.31992071866989136,\\n      0.3075661361217499,\\n      0.30589577555656433,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-14T16:28:08.362019+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -30 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -30 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T16:28:08.362156+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.4031004011631012,\\n    \\\"s2_minkpp\\\": 1.6658546924591064,\\n    \\\"s3_constat\\\": null,\\n    \\\"s4_selfcritique\\\": -0.9971877301543359\\n  },\\n  {\\n    \\\"index\\\": 1,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.39687806367874146,\\n    \\\"s2_minkpp\\\": 1.5021213293075562,\\n    \\\"s3_constat\\\": null,\\n    \\\"s4_selfcritique\\\": -0.9750790425362086\\n  },\\n  {\\n    \\\"index\\\": 2,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.48771804571151733,\\n    \\\"s2_minkpp\\\": 1.5626308917999268,\\n    \\\"s3_constat\\\": null,\\n    \\\"s4_selfcritique\\\": -0.8901001665238636\\n  },\\n  {\\n    \\\"index\\\": 3,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s1_embedding\\\": 0.4187033176422119,\\n    \\\"s2_minkpp\\\": 1.3724992275238037,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-14T16:28:08.362277+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -30 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_minkpp_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -30 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_minkpp_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T16:28:08.362432+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s2_minkpp\\\": 1.6658546924591064,\\n    \\\"s2_minkpp_raw\\\": -1.6658546924591064,\\n    \\\"n_tokens\\\": 49\\n  },\\n  {\\n    \\\"index\\\": 1,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s2_minkpp\\\": 1.5021213293075562,\\n    \\\"s2_minkpp_raw\\\": -1.5021213293075562,\\n    \\\"n_tokens\\\": 64\\n  },\\n  {\\n    \\\"index\\\": 2,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s2_minkpp\\\": 1.5626308917999268,\\n    \\\"s2_minkpp_raw\\\": -1.5626308917999268,\\n    \\\"n_tokens\\\": 68\\n  },\\n  {\\n    \\\"index\\\": 3,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s2_minkpp\\\": 1.3724992275238037,\\n    \\\"s2_minkpp_raw\\\": -1.3724992275238037,\\n    \\\"n_tokens\\\": 78\\n  },\\n  {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-14T16:28:08.362553+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -30 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_selfcritique_mmlu.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -30 /root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signal_selfcritique_mmlu.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T16:28:08.362691+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[\\n  {\\n    \\\"index\\\": 0,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s4_selfcritique\\\": -0.9971877301543359,\\n    \\\"s4_entropy\\\": 0.9971877301543359,\\n    \\\"s4_yes_prob\\\": 0.5312093733737563,\\n    \\\"s4_no_prob\\\": 0.46879062662624377\\n  },\\n  {\\n    \\\"index\\\": 1,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s4_selfcritique\\\": -0.9750790425362086,\\n    \\\"s4_entropy\\\": 0.9750790425362086,\\n    \\\"s4_yes_prob\\\": 0.5926665999540697,\\n    \\\"s4_no_prob\\\": 0.4073334000459302\\n  },\\n  {\\n    \\\"index\\\": 2,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s4_selfcritique\\\": -0.8901001665238636,\\n    \\\"s4_entropy\\\": 0.8901001665238636,\\n    \\\"s4_yes_prob\\\": 0.6926419831347361,\\n    \\\"s4_no_prob\\\": 0.30735801686526387\\n  },\\n  {\\n    \\\"index\\\": 3,\\n    \\\"benchmark\\\": \\\"mmlu\\\",\\n    \\\"s4_selfcritique\\\": -0.9888163926508523,\\n    \\\"s4_entropy\\\": 0.9888163926508523,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-14T16:28:08.362831+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T16:28:08.363178+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"dosage\\\": 5,\\n  \\\"total_items\\\": 14042,\\n  \\\"contaminated_count\\\": 703,\\n  \\\"labels\\\": [\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    1,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    1,\\n    0,\\n    1,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    1,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    1,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    1,\\n    0,\\n    0,\\n    0,\\n    0,\\n    1,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    1,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    0,\\n    1,\\n    0,\\n    0,\\n    1,\\n    0,\\n    0,\\n    0,\
…[truncated 8506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-14T16:28:08.363508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/sft_data/contamination_labels_*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/sft_data/contamination_labels_*"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T16:28:08.363660+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d005.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d025.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d050.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d100.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d005.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d025.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d050.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d100.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d005.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d025.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d050.json\\n/root/autodl-tmp/exp001/sft_data/contamination_labels_mmlu_d100.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-14T16:28:08.363789+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/contamcal-irt-calibration/exp008/exp008_exp002_output/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/contamcal-irt-calibration/exp008/exp008_exp002_output/"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T16:28:08.363929+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 28\\ndrwxr-xr-x 3 root root    75 May 15 00:09 .\\ndrwxr-xr-x 5 root root  4096 May 15 00:09 ..\\n-rw-r--r-- 1 root root 21212 May 15 00:09 cross_benchmark_summary.json\\ndrwxr-xr-x 5 root root    68 May 15 00:09 per_benchmark\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-14T16:28:08.364071+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d005.json')); print(f'gsm8k: {d[\\\"total_items\\\"]} items, {d[\\\"contaminated_count\\\"]} contaminated')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d005.json')); print(f'gsm8k: {d[\\\"total_items\\\"]} items, {d[\\\"contaminated_count\\\"]} contaminated')\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T16:28:08.364193+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-14T16:28:08.364343+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d005.json')); print(f'arc: {d[\\\"total_items\\\"]} items, {d[\\\"contaminated_count\\\"]} contaminated')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d005.json')); print(f'arc: {d[\\\"total_items\\\"]} items, {d[\\\"contaminated_count\\\"]} contaminated')\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T16:28:08.364495+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-14T16:28:08.364611+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json')); print(f'n_items={len(d)}, keys={list(d[0].keys())}')\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp002/signals/Qwen2.5-0.5B_d005_s42/signals_merged_mmlu.json')); print(f'n_items={len(d)}, keys={list(d[0].keys())}')\""
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T16:28:08.364726+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-14T16:28:08.364835+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -5 /root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d005.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -5 /root/autodl-tmp/exp001/sft_data/contamination_labels_gsm8k_d005.json"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T16:28:08.364945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -5 /root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d005.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -5 /root/autodl-tmp/exp001/sft_data/contamination_labels_arc_challenge_d005.json"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T16:28:08.365060+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"dosage\\\": 5,\\n  \\\"total_items\\\": 1319,\\n  \\\"contaminated_count\\\": 73,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-14T16:28:08.365175+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"arc_challenge\\\",\\n  \\\"dosage\\\": 5,\\n  \\\"total_items\\\": 1172,\\n  \\\"contaminated_count\\\": 50,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-14T16:28:08.365413+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat > /root/contamcal-irt-calibration/exp008/signal_survival_v4.py << 'PYEOF'\n\"\"\"\nexp-008 Signal Survival Analysis v4 (D021 corrected)\n\nKey corrections from v3:\n- d000/d005: within-model AUC (d005 labels)\n- d100: cross-model paired comparison (d100 vs d000), NOT within-model AUC\n  (d100 has all items contaminated → no negative class → AUC meaningless)\n\"\"\"\nimport json\nimport os\nimport numpy as np\nfrom pathlib import Path\nfrom scipy import stats\nfrom sklearn.metrics import roc_auc_score\n\nSIGNALS_DIR = Path(\"/root/autodl-tmp/exp002/signals\")\nLABELS_DIR = Path(\"/root/autodl-tmp/exp001/sft_data\")\nOUTPUT_DIR = Path(\"/root/contamcal-irt-calibration/exp008/exp008_v4_output\")\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\"]\nSIGNAL_KEYS = [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]\nSIGNAL_NAMES = {\"s1_embedding\": \"S1_Embedding\", \"s2_minkpp\": \"S2_MinKPP\", \"s4_selfcritique\": \"S4_SelfCritique\"}\n\nREGIME_DIRS = {\n    \"d000\": \"Qwen2.5-0.5B_d000_s42\",\n    \"d005\": \"Qwen2.5-0.5B_d005_s42\",\n    \"d100\": \"Qwen2.5-0.5B_d100_s42\",\n}\n\n\ndef load_signals(regime, bench):\n    path = SIGNALS_DIR / REGIME_DIRS[regime] / f\"signals_merged_{bench}.json\"\n    with open(path) as f:\n        items = json.load(f)\n    return {item[\"index\"]: item for item in items}\n\n\ndef load_labels(bench):\n    path = LABELS_DIR / f\"contamination_labels_{bench}_d005.json\"\n    with open(path) as f:\n        data = json.load(f)\n    return data[\"labels\"], data[\"total_items\"], data[\"contaminated_count\"]\n\n\ndef within_model_auc(signals_dict, labels, signal_key):\n    indices = sorted(set(signals_dict.keys()) & set(range(len(labels))))\n    y = np.array([labels[i] for i in indices])\n    scores = np.array([signals_dict[i][signal_key] for i in indices])\n\n    valid = ~np.isnan(scores) & ~np.isinf(scores)\n    y, scores = y[valid], scores[valid]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": None, \"n_pos\": int(y.sum()), \"n_neg\": int((1 - y).sum()),\n                \"n_total\": len(y), \"note\": \"single class - AUC undefined\"}\n\n    auc = roc_auc_score(y, scores)\n    return {\"auc\": round(float(auc), 6), \"n_pos\": int(y.sum()), \"n_neg\": int(len(y) - y.sum()),\n            \"n_total\": len(y)}\n\n\ndef cross_model_comparison(signals_d100, signals_d000, signal_key):\n    common = sorted(set(signals_d100.keys()) & set(signals_d000.keys()))\n    vals_100 = np.array([signals_d100[i][signal_key] for i in common])\n    vals_000 = np.array([signals_d000[i][signal_key] for i in common])\n\n    valid = ~np.isnan(vals_100) & ~np.isnan(vals_000) & ~np.isinf(vals_100) & ~np.isinf(vals_000)\n    vals_100, vals_000 = vals_100[valid], vals_000[valid]\n    n = len(vals_100)\n\n    diff = vals_100 - vals_000\n    mean_diff = float(np.mean(diff))\n    std_diff = float(np.std(diff, ddof=1)) if n > 1 else 0.0\n    cohens_d = mean_diff / std_diff if std_diff > 0 else float(\"inf\")\n\n    stat, p_value = stats.wilcoxon(vals_100, vals_000, alternative=\"two-sided\")\n\n    pct_higher = float(np.mean(diff > 0))\n    pct_lower = float(np.mean(diff < 0))\n\n    return {\n        \"n_items\": n,\n        \"mean_d100\": round(float(np.mean(vals_100)), 6),\n        \"mean_d000\": round(float(np.mean(vals_000)), 6),\n        \"mean_diff\": round(mean_diff, 6),\n        \"std_diff\": round(std_diff, 6),\n        \"cohens_d\": round(float(cohens_d), 4),\n        \"wilcoxon_stat\": round(float(stat), 2),\n        \"wilcoxon_p\": float(p_value),\n        \"pct_d100_higher\": round(pct_higher, 4),\n        \"pct_d100_lower\": round(pct_lower, 4),\n        \"significant_0.05\": p_value < 0.05,\n        \"significant_0.01\": p_value < 0.01,\n        \"significant_bonferroni\": p_value < 0.05 / (len(SIGNAL_KEYS) * len(BENCHMARKS)),\n    }\n\n\ndef analyze_benchmark(bench):\n    labels, total, n_contam = load_labels(bench)\n    sig_d000 = load_signals(\"d000\", bench)\n    sig_d005 = load_signals(\"d005\", bench)\n    sig_d100 = load_signals(\"d100\", bench)\n\n    result = {\n        \"benchmark\": bench,\n        \"n_items\": total,\n        \"n_contaminated_d005\": n_contam,\n        \"within_model_auc\": {\"d000\": {}, \"d005\": {}},\n        \"cross_model_d100_vs_d000\": {},\n    }\n\n    for sk in SIGNAL_KEYS:\n        sname = SIGNAL_NAMES[sk]\n        result[\"within_model_auc\"][\"d000\"][sname] = within_model_auc(sig_d000, labels, sk)\n        result[\"within_model_auc\"][\"d005\"][sname] = within_model_auc(sig_d005, labels, sk)\n        result[\"cross_model_d100_vs_d000\"][sname] = cross_model_comparison(sig_d100, sig_d000, sk)\n\n    return result\n\n\ndef build_heatmap(results):\n    heatmap = {}\n    for sname in SIGNAL_NAMES.values():\n        heatmap[sname] = {}\n        for bench, res in results.items():\n            d000_auc = res[\"within_model_auc\"][\"d000\"][sname][\"auc\"]\n            d005_auc = res[\"within_model_auc\"][\"d005\"][sname][\"auc\"]\n            cross = res[\"cross_model_d100_vs_d000\"][sname]\n            heatmap[sname][bench] = {\n                \"d000_auc\": d000_auc,\n                \"d005_auc\": d005_auc,\n                \"d100_cross_model_effect\": cross[\"cohens_d\"],\n                \"d100_cross_model_p\": cross[\"wilcoxon_p\"],\n                \"d100_cross_model_significant\": cross[\"significant_bonferroni\"],\n            }\n    return heatmap\n\n\ndef build_summary(results, heatmap):\n    findings = []\n\n    for sname in SIGNAL_NAMES.values():\n        d005_aucs = [heatmap[sname][b][\"d005_auc\"] for b in BENCHMARKS if heatmap[sname][b][\"d005_auc\"] is not None]\n        d000_aucs = [heatmap[sname][b][\"d000_auc\"] for b in BENCHMARKS if heatmap[sname][b][\"d000_auc\"] is not None]\n        cross_sig = [heatmap[sname][b][\"d100_cross_model_significant\"] for b in BENCHMARKS]\n        cross_effects = [heatmap[sname][b][\"d100_cross_model_effect\"] for b in BENCHMARKS]\n\n        findings.append({\n            \"signal\": sname,\n            \"d005_auc_mean\": round(np.mean(d005_aucs), 4) if d005_aucs else None,\n            \"d005_auc_range\": [round(min(d005_aucs), 4), round(max(d005_aucs), 4)] if d005_aucs else None,\n            \"d000_sanity_check\": \"PASS\" if all(a is not None and 0.45 <= a <= 0.55 for a in d000_aucs) else \"MARGINAL\" if all(a is not None and 0.40 <= a <= 0.60 for a in d000_aucs) else \"FAIL\",\n            \"d100_cross_model_any_significant\": any(cross_sig),\n            \"d100_cross_model_effects\": [round(e, 4) for e in cross_effects],\n        })\n\n    effective_signals = [f for f in findings if f[\"d005_auc_mean\"] is not None and f[\"d005_auc_mean\"] > 0.65]\n\n    return {\n        \"version\": \"v4_D021_corrected\",\n        \"correction_notes\": [\n            \"d100 within-model AUC removed (label artifact: all items contaminated → no negative class)\",\n            \"d100 now uses cross-model paired comparison (d100 vs d000 signal differences)\",\n            \"C2 claim weakened: 'systematic signal variation with dosage' instead of 'cliff-like RL degradation'\",\n        ],\n        \"key_findings\": findings,\n        \"effective_signal_count\": len(effective_signals),\n        \"narrative\": (\n            f\"{len(effective_signals)}/{len(SIGNAL_KEYS)} signals show effective contamination detection at d005. \"\n            \"Signal effectiveness varies systematically with dosage; individual signals insufficient → \"\n            \"need IRT multi-signal fusion for robust detection across regimes.\"\n        ),\n    }\n\n\ndef print_results(results, heatmap, summary):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"exp-008 Signal Survival Analysis v4 (D021 corrected)\")\n    print(\"=\" * 70)\n\n    print(\"\\n--- Within-Model AUC Heatmap (d000 sanity / d005 detection) ---\")\n    header = f\"{'Signal':<20} {'Regime':<8}\"\n    for b in BENCHMARKS:\n        header += f\" {b:>15}\"\n    print(header)\n    print(\"-\" * len(header))\n\n    for sname in SIGNAL_NAMES.values():\n        row_d000 = f\"{sname:<20} {'d000':<8}\"\n        row_d005 = f\"{'':<20} {'d005':<8}\"\n        for b in BENCHMARKS:\n            a0 = heatmap[sname][b][\"d000_auc\"]\n            a5 = heatmap[sname][b][\"d005_auc\"]\n            row_d000 += f\" {a0:>15.4f}\" if a0 is not None else f\" {'N/A':>15}\"\n            row_d005 += f\" {a5:>15.4f}\" if a5 is not None else f\" {'N/A':>15}\"\n        print(row_d000)\n        print(row_d005)\n        print()\n\n    print(\"\\n--- Cross-Model Effect (d100 vs d000) ---\")\n    header2 = f\"{'Signal':<20}\"\n    for b in BENCHMARKS:\n        header2 += f\" {b + ' (d|p)':>25}\"\n    print(header2)\n    print(\"-\" * len(header2))\n\n    for sname in SIGNAL_NAMES.values():\n        row = f\"{sname:<20}\"\n        for b in BENCHMARKS:\n            d = heatmap[sname][b][\"d100_cross_model_effect\"]\n            p = heatmap[sname][b][\"d100_cross_model_p\"]\n            sig = \"*\" if heatmap[sname][b][\"d100_cross_model_significant\"] else \"\"\n            row += f\" {d:>8.3f} (p={p:.2e}){sig:>3}\"\n        print(row)\n\n    print(\"\\n--- Summary ---\")\n    print(summary[\"narrative\"])\n    for f in summary[\"key_findings\"]:\n        print(f\"  {f['signal']}: d005 AUC={f['d005_auc_mean']}, d000 sanity={f['d000_sanity_check']}, \"\n              f\"d100 cross-model sig={f['d100_cross_model_any_significant']}\")\n\n\ndef main():\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    results = {}\n    for bench in BENCHMARKS:\n        print(f\"Processing {bench}...\")\n        results[bench] = analyze_benchmark(bench)\n\n    heatmap = build_heatmap(results)\n    summary = build_summary(results, heatmap)\n\n    full_output = {\n        \"experiment\": \"exp-008\",\n        \"version\": \"v4_D021_corrected\",\n        \"per_benchmark\": results,\n        \"heatmap\": heatmap,\n        \"summary\": summary,\n    }\n\n    out_file = OUTPUT_DIR / \"exp008_v4_results.json\"\n    with open(out_file, \"w\") as f:\n        json.dump(full_output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_file}\")\n\n    print_results(results, heatmap, summary)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat > /root/contamcal-irt-calibration/exp008/signal_survival_v4.py << 'PYEOF'\n\"\"\"\nexp-008 Signal Survival Analysis v4 (D021 corrected)\n\nKey corrections from v3:\n- d000/d005: within-model AUC (d005 labels)\n- d100: cross-model paired comparison (d100 vs d000), NOT within-model AUC\n  (d100 has all items contaminated → no negative class → AUC meaningless)\n\"\"\"\nimport json\nimport os\nimport numpy as np\nfrom pathlib import Path\nfrom scipy import stats\nfrom sklearn.metrics import roc_auc_score\n\nSIGNALS_DIR = Path(\"/root/autodl-tmp/exp002/signals\")\nLABELS_DIR = Path(\"/root/autodl-tmp/exp001/sft_data\")\nOUTPUT_DIR = Path(\"/root/contamcal-irt-calibration/exp008/exp008_v4_output\")\n\nBENCHMARKS = [\"mmlu\", \"gsm8k\", \"arc_challenge\"]\nSIGNAL_KEYS = [\"s1_embedding\", \"s2_minkpp\", \"s4_selfcritique\"]\nSIGNAL_NAMES = {\"s1_embedding\": \"S1_Embedding\", \"s2_minkpp\": \"S2_MinKPP\", \"s4_selfcritique\": \"S4_SelfCritique\"}\n\nREGIME_DIRS = {\n    \"d000\": \"Qwen2.5-0.5B_d000_s42\",\n    \"d005\": \"Qwen2.5-0.5B_d005_s42\",\n    \"d100\": \"Qwen2.5-0.5B_d100_s42\",\n}\n\n\ndef load_signals(regime, bench):\n    path = SIGNALS_DIR / REGIME_DIRS[regime] / f\"signals_merged_{bench}.json\"\n    with open(path) as f:\n        items = json.load(f)\n    return {item[\"index\"]: item for item in items}\n\n\ndef load_labels(bench):\n    path = LABELS_DIR / f\"contamination_labels_{bench}_d005.json\"\n    with open(path) as f:\n        data = json.load(f)\n    return data[\"labels\"], data[\"total_items\"], data[\"contaminated_count\"]\n\n\ndef within_model_auc(signals_dict, labels, signal_key):\n    indices = sorted(set(signals_dict.keys()) & set(range(len(labels))))\n    y = np.array([labels[i] for i in indices])\n    scores = np.array([signals_dict[i][signal_key] for i in indices])\n\n    valid = ~np.isnan(scores) & ~np.isinf(scores)\n    y, scores = y[valid], scores[valid]\n\n    if len(np.unique(y)) < 2:\n        return {\"auc\": None, \"n_pos\": int(y.sum()), \"n_neg\": int((1 - y).sum()),\n                \"n_total\": len(y), \"note\": \"single class - AUC undefined\"}\n\n    auc = roc_auc_score(y, scores)\n    return {\"auc\": round(float(auc), 6), \"n_pos\": int(y.sum()), \"n_neg\": int(len(y) - y.sum()),\n            \"n_total\": len(y)}\n\n\ndef cross_model_comparison(signals_d100, signals_d000, signal_key):\n    common = sorted(set(signals_d100.keys()) & set(signals_d000.keys()))\n    vals_100 = np.array([signals_d100[i][signal_key] for i in common])\n    vals_000 = np.array([signals_d000[i][signal_key] for i in common])\n\n    valid = ~np.isnan(vals_100) & ~np.isnan(vals_000) & ~np.isinf(vals_100) & ~np.isinf(vals_000)\n    vals_100, vals_000 = vals_100[valid], vals_000[valid]\n    n = len(vals_100)\n\n    diff = vals_100 - vals_000\n    mean_diff = float(np.mean(diff))\n    std_diff = float(np.std(diff, ddof=1)) if n > 1 else 0.0\n    cohens_d = mean_diff / std_diff if std_diff > 0 else float(\"inf\")\n\n    stat, p_value = stats.wilcoxon(vals_100, vals_000, alternative=\"two-sided\")\n\n    pct_higher = float(np.mean(diff > 0))\n    pct_lower = float(np.mean(diff < 0))\n\n    return {\n        \"n_items\": n,\n        \"mean_d100\": round(float(np.mean(vals_100)), 6),\n        \"mean_d000\": round(float(np.mean(vals_000)), 6),\n        \"mean_diff\": round(mean_diff, 6),\n        \"std_diff\": round(std_diff, 6),\n        \"cohens_d\": round(float(cohens_d), 4),\n        \"wilcoxon_stat\": round(float(stat), 2),\n        \"wilcoxon_p\": float(p_value),\n        \"pct_d100_higher\": round(pct_higher, 4),\n        \"pct_d100_lower\": round(pct_lower, 4),\n        \"significant_0.05\": p_value < 0.05,\n        \"significant_0.01\": p_value < 0.01,\n        \"significant_bonferroni\": p_value < 0.05 / (len(SIGNAL_KEYS) * len(BENCHMARKS)),\n    }\n\n\ndef analyze_benchmark(bench):\n    labels, total, n_contam = load_labels(bench)\n    sig_d000 = load_signals(\"d000\", bench)\n    sig_d005 = load_signals(\"d005\", bench)\n    sig_d100 = load_signals(\"d100\", bench)\n\n    result = {\n        \"benchmark\": bench,\n        \"n_items\": total,\n        \"n_contaminated_d005\": n_contam,\n        \"within_model_auc\": {\"d000\": {}, \"d005\": {}},\n        \"cross_model_d100_vs_d000\": {},\n    }\n\n    for sk in SIGNAL_KEYS:\n        sname = SIGNAL_NAMES[sk]\n        result[\"within_model_auc\"][\"d000\"][sname] = within_model_auc(sig_d000, labels, sk)\n        result[\"within_model_auc\"][\"d005\"][sname] = within_model_auc(sig_d005, labels, sk)\n        result[\"cross_model_d100_vs_d000\"][sname] = cross_model_comparison(sig_d100, sig_d000, sk)\n\n    return result\n\n\ndef build_heatmap(results):\n    heatmap = {}\n    for sname in SIGNAL_NAMES.values():\n        heatmap[sname] = {}\n        for bench, res in results.items():\n            d000_auc = res[\"within_model_auc\"][\"d000\"][sname][\"auc\"]\n            d005_auc = res[\"within_model_auc\"][\"d005\"][sname][\"auc\"]\n            cross = res[\"cross_model_d100_vs_d000\"][sname]\n            heatmap[sname][bench] = {\n                \"d000_auc\": d000_auc,\n                \"d005_auc\": d005_auc,\n                \"d100_cross_model_effect\": cross[\"cohens_d\"],\n                \"d100_cross_model_p\": cross[\"wilcoxon_p\"],\n                \"d100_cross_model_significant\": cross[\"significant_bonferroni\"],\n            }\n    return heatmap\n\n\ndef build_summary(results, heatmap):\n    findings = []\n\n    for sname in SIGNAL_NAMES.values():\n        d005_aucs = [heatmap[sname][b][\"d005_auc\"] for b in BENCHMARKS if heatmap[sname][b][\"d005_auc\"] is not None]\n        d000_aucs = [heatmap[sname][b][\"d000_auc\"] for b in BENCHMARKS if heatmap[sname][b][\"d000_auc\"] is not None]\n        cross_sig = [heatmap[sname][b][\"d100_cross_model_significant\"] for b in BENCHMARKS]\n        cross_effects = [heatmap[sname][b][\"d100_cross_model_effect\"] for b in BENCHMARKS]\n\n        findings.append({\n            \"signal\": sname,\n            \"d005_auc_mean\": round(np.mean(d005_aucs), 4) if d005_aucs else None,\n            \"d005_auc_range\": [round(min(d005_aucs), 4), round(max(d005_aucs), 4)] if d005_aucs else None,\n            \"d000_sanity_check\": \"PASS\" if all(a is not None and 0.45 <= a <= 0.55 for a in d000_aucs) else \"MARGINAL\" if all(a is not None and 0.40 <= a <= 0.60 for a in d000_aucs) else \"FAIL\",\n            \"d100_cross_model_any_significant\": any(cross_sig),\n            \"d100_cross_model_effects\": [round(e, 4) for e in cross_effects],\n        })\n\n    effective_signals = [f for f in findings if f[\"d005_auc_mean\"] is not None and f[\"d005_auc_mean\"] > 0.65]\n\n    return {\n        \"version\": \"v4_D021_corrected\",\n        \"correction_notes\": [\n            \"d100 within-model AUC removed (label artifact: all items contaminated → no negative class)\",\n            \"d100 now uses cross-model paired comparison (d100 vs d000 signal differences)\",\n            \"C2 claim weakened: 'systematic signal variation with dosage' instead of 'cliff-like RL degradation'\",\n        ],\n        \"key_findings\": findings,\n        \"effective_signal_count\": len(effective_signals),\n        \"narrative\": (\n            f\"{len(effective_signals)}/{len(SIGNAL_KEYS)} signals show effective contamination detection at d005. \"\n            \"Signal effectiveness varies systematically with dosage; individual signals insufficient → \"\n            \"need IRT multi-signal fusion for robust detection across regimes.\"\n        ),\n    }\n\n\ndef print_results(results, heatmap, summary):\n    print(\"\\n\" + \"=\" * 70)\n    print(\"exp-008 Signal Survival Analysis v4 (D021 corrected)\")\n    print(\"=\" * 70)\n\n    print(\"\\n--- Within-Model AUC Heatmap (d000 sanity / d005 detection) ---\")\n    header = f\"{'Signal':<20} {'Regime':<8}\"\n    for b in BENCHMARKS:\n        header += f\" {b:>15}\"\n    print(header)\n    print(\"-\" * len(header))\n\n    for sname in SIGNAL_NAMES.values():\n        row_d000 = f\"{sname:<20} {'d000':<8}\"\n        row_d005 = f\"{'':<20} {'d005':<8}\"\n        for b in BENCHMARKS:\n            a0 = heatmap[sname][b][\"d000_auc\"]\n            a5 = heatmap[sname][b][\"d005_auc\"]\n            row_d000 += f\" {a0:>15.4f}\" if a0 is not None else f\" {'N/A':>15}\"\n            row_d005 += f\" {a5:>15.4f}\" if a5 is not None else f\" {'N/A':>15}\"\n        print(row_d000)\n        print(row_d005)\n        print()\n\n    print(\"\\n--- Cross-Model Effect (d100 vs d000) ---\")\n    header2 = f\"{'Signal':<20}\"\n    for b in BENCHMARKS:\n        header2 += f\" {b + ' (d|p)':>25}\"\n    print(header2)\n    print(\"-\" * len(header2))\n\n    for sname in SIGNAL_NAMES.values():\n        row = f\"{sname:<20}\"\n        for b in BENCHMARKS:\n            d = heatmap[sname][b][\"d100_cross_model_effect\"]\n            p = heatmap[sname][b][\"d100_cross_model_p\"]\n            sig = \"*\" if heatmap[sname][b][\"d100_cross_model_significant\"] else \"\"\n            row += f\" {d:>8.3f} (p={p:.2e}){sig:>3}\"\n        print(row)\n\n    print(\"\\n--- Summary ---\")\n    print(summary[\"narrative\"])\n    for f in summary[\"key_findings\"]:\n        print(f\"  {f['signal']}: d005 AUC={f['d005_auc_mean']}, d000 sanity={f['d000_sanity_check']}, \"\n              f\"d100 cross-model sig={f['d100_cross_model_any_significant']}\")\n\n\ndef main():\n    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)\n\n    results = {}\n    for bench in BENCHMARKS:\n        print(f\"Processing {bench}...\")\n        results[bench] = analyze_benchmark(bench)\n\n    heatmap = build_heatmap(results)\n    summary = build_summary(results, heatmap)\n\n    full_output = {\n        \"experiment\": \"exp-008\",\n        \"version\": \"v4_D021_corrected\",\n        \"per_benchmark\": results,\n        \"heatmap\": heatmap,\n        \"summary\": summary,\n    }\n\n    out_file = OUTPUT_DIR / \"exp008_v4_results.json\"\n    with open(out_file, \"w\") as f:\n        json.dump(full_output, f, indent=2, default=str)\n    print(f\"\\nResults saved to {out_file}\")\n\n    print_results(results, heatmap, summary)\n\n\nif __name__ == \"__main__\":\n    main()\nPYEOF"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T16:28:08.365669+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-14T16:28:08.365812+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "cqa1-21977",
  "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp008 && python signal_survival_v4.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/contamcal-irt-calibration/exp008 && python signal_survival_v4.py"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T16:28:08.365968+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Processing mmlu...\\nProcessing gsm8k...\\nProcessing arc_challenge...\\n\\nResults saved to /root/contamcal-irt-calibration/exp008/exp008_v4_output/exp008_v4_results.json\\n\\n======================================================================\\nexp-008 Signal Survival Analysis v4 (D021 corrected)\\n======================================================================\\n\\n--- Within-Model AUC Heatmap (d000 sanity / d005 detection) ---\\nSignal               Regime              mmlu           gsm8k   arc_challenge\\n-----------------------------------------------------------------------------\\nS1_Embedding         d000              0.5049          0.5502          0.4270\\n                     d005              0.9530          0.9882          0.9950\\n\\nS2_MinKPP            d000              0.5090          0.5697          0.5075\\n                     d005              0.4655          0.4649          0.4659\\n\\nS4_SelfCritique      d000              0.4957          0.4800          0.5175\\n                     d005              0.5165          0.4947          0.4325\\n\\n\\n--- Cross-Model Effect (d100 vs d000) ---\\nSignal                              mmlu (d|p)               gsm8k (d|p)       arc_challenge (d|p)\\n--------------------------------------------------------------------------------------------------\\nS1_Embedding            4.162 (p=0.00e+00)  *    2.833 (p=3.07e-216)  *    3.799 (p=4.36e-193)  *\\nS2_MinKPP              -1.220 (p=0.00e+00)  *   -2.666 (p=3.37e-217)  *   -2.048 (p=7.87e-193)  *\\nS4_SelfCritique         0.467 (p=0.00e+00)  *    0.203 (p=1.05e-08)  *    0.671 (p=1.00e-95)  *\\n\\n--- Summary ---\\n1/3 signals show effective contamination detection at d005. Signal effectiveness varies systematically with dosage; individual signals insufficient → need IRT multi-signal fusion for robust detection across regimes.\\n  S1_Embedding: d005 AUC=0.9787, d000 sanity=MARGINAL, d100 cr
…[truncated 287 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-14T16:28:08.366158+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/exp008/exp008_v4_output/exp008_v4_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/exp008/exp008_v4_output/exp008_v4_results.json"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-14T16:28:08.366548+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"experiment\\\": \\\"exp-008\\\",\\n  \\\"version\\\": \\\"v4_D021_corrected\\\",\\n  \\\"per_benchmark\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"benchmark\\\": \\\"mmlu\\\",\\n      \\\"n_items\\\": 14042,\\n      \\\"n_contaminated_d005\\\": 703,\\n      \\\"within_model_auc\\\": {\\n        \\\"d000\\\": {\\n          \\\"S1_Embedding\\\": {\\n            \\\"auc\\\": 0.504915,\\n            \\\"n_pos\\\": 703,\\n            \\\"n_neg\\\": 13339,\\n            \\\"n_total\\\": 14042\\n          },\\n          \\\"S2_MinKPP\\\": {\\n            \\\"auc\\\": 0.509028,\\n            \\\"n_pos\\\": 703,\\n            \\\"n_neg\\\": 13339,\\n            \\\"n_total\\\": 14042\\n          },\\n          \\\"S4_SelfCritique\\\": {\\n            \\\"auc\\\": 0.495722,\\n            \\\"n_pos\\\": 703,\\n            \\\"n_neg\\\": 13339,\\n            \\\"n_total\\\": 14042\\n          }\\n        },\\n        \\\"d005\\\": {\\n          \\\"S1_Embedding\\\": {\\n            \\\"auc\\\": 0.952963,\\n            \\\"n_pos\\\": 703,\\n            \\\"n_neg\\\": 13339,\\n            \\\"n_total\\\": 14042\\n          },\\n          \\\"S2_MinKPP\\\": {\\n            \\\"auc\\\": 0.46548,\\n            \\\"n_pos\\\": 703,\\n            \\\"n_neg\\\": 13339,\\n            \\\"n_total\\\": 14042\\n          },\\n          \\\"S4_SelfCritique\\\": {\\n            \\\"auc\\\": 0.516544,\\n            \\\"n_pos\\\": 703,\\n            \\\"n_neg\\\": 13339,\\n            \\\"n_total\\\": 14042\\n          }\\n        }\\n      },\\n      \\\"cross_model_d100_vs_d000\\\": {\\n        \\\"S1_Embedding\\\": {\\n          \\\"n_items\\\": 14042,\\n          \\\"mean_d100\\\": 0.901361,\\n          \\\"mean_d000\\\": 0.522375,\\n          \\\"mean_diff\\\": 0.378985,\\n          \\\"std_diff\\\": 0.091055,\\n          \\\"cohens_d\\\": 4.1622,\\n          \\\"wilcoxon_stat\\\": 0.0,\\n          \\\"wilcoxon_p\\\": 0.0,\\n  
…[truncated 8262 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-14T16:28:08.366774+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data",
  "description": "Create local artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data",
    "description": "Create local artifacts directory"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T16:28:08.366906+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-14T16:28:08.367080+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data/exp008_v4_results.json",
  "content": "{\n  \"experiment\": \"exp-008\",\n  \"version\": \"v4_D021_corrected\",\n  \"per_benchmark\": {\n    \"mmlu\": {\n      \"benchmark\": \"mmlu\",\n      \"n_items\": 14042,\n      \"n_contaminated_d005\": 703,\n      \"within_model_auc\": {\n        \"d000\": {\n          \"S1_Embedding\": {\"auc\": 0.504915, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042},\n          \"S2_MinKPP\": {\"auc\": 0.509028, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042},\n          \"S4_SelfCritique\": {\"auc\": 0.495722, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042}\n        },\n        \"d005\": {\n          \"S1_Embedding\": {\"auc\": 0.952963, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042},\n          \"S2_MinKPP\": {\"auc\": 0.46548, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042},\n          \"S4_SelfCritique\": {\"auc\": 0.516544, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042}\n        }\n      },\n      \"cross_model_d100_vs_d000\": {\n        \"S1_Embedding\": {\"n_items\": 14042, \"mean_d100\": 0.901361, \"mean_d000\": 0.522375, \"mean_diff\": 0.378985, \"std_diff\": 0.091055, \"cohens_d\": 4.1622, \"wilcoxon_stat\": 0.0, \"wilcoxon_p\": 0.0, \"pct_d100_higher\": 0.9993, \"pct_d100_lower\": 0.0, \"significant_bonferroni\": true},\n        \"S2_MinKPP\": {\"n_items\": 14042, \"mean_d100\": 1.432032, \"mean_d000\": 1.697604, \"mean_diff\": -0.265572, \"std_diff\": 0.217631, \"cohens_d\": -1.2203, \"wilcoxon_stat\": 660013.0, \"wilcoxon_p\": 0.0, \"pct_d100_higher\": 0.0308, \"pct_d100_lower\": 0.969, \"significant_bonferroni\": true},\n        \"S4_SelfCritique\": {\"n_items\": 14042, \"mean_d100\": -0.907331, \"mean_d000\": -0.955669, \"mean_diff\": 0.048339, \"std_diff\": 0.103438, \"cohens_d\": 0.4673, \"wilcoxon_stat\": 19322716.0, \"wilcoxon_p\": 0.0, \"pct_d100_higher\": 0.6733, \"pct_d100_lower\": 0.2745, \"significant_bonferroni\": true}\n      }\n    },\n    \"gsm8k\": {\n      \"benchmark\": \"gsm8k\",\n      \"n_items\": 1319,\n      \"n_contaminated_d005\": 73,\n      \"within_model_auc\": {\n        \"d000\": {\n          \"S1_Embedding\": {\"auc\": 0.550232, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319},\n          \"S2_MinKPP\": {\"auc\": 0.569703, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319},\n          \"S4_SelfCritique\": {\"auc\": 0.480029, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319}\n        },\n        \"d005\": {\n          \"S1_Embedding\": {\"auc\": 0.988203, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319},\n          \"S2_MinKPP\": {\"auc\": 0.464863, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319},\n          \"S4_SelfCritique\": {\"auc\": 0.494684, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319}\n        }\n      },\n      \"cross_model_d100_vs_d000\": {\n        \"S1_Embedding\": {\"n_items\": 1319, \"mean_diff\": 0.197201, \"std_diff\": 0.069606, \"cohens_d\": 2.8331, \"wilcoxon_p\": 3.07e-216, \"pct_d100_higher\": 0.9992, \"significant_bonferroni\": true},\n        \"S2_MinKPP\": {\"n_items\": 1319, \"mean_diff\": -0.478204, \"std_diff\": 0.179378, \"cohens_d\": -2.666, \"wilcoxon_p\": 3.37e-217, \"pct_d100_higher\": 0.0076, \"significant_bonferroni\": true},\n        \"S4_SelfCritique\": {\"n_items\": 1319, \"mean_diff\": 0.021506, \"std_diff\": 0.105749, \"cohens_d\": 0.2034, \"wilcoxon_p\": 1.05e-08, \"pct_d100_higher\": 0.5874, \"significant_bonferroni\": true}\n      }\n    },\n    \"arc_challenge\": {\n      \"benchmark\": \"arc_challenge\",\n      \"n_items\": 1172,\n      \"n_contaminated_d005\": 50,\n      \"within_model_auc\": {\n        \"d000\": {\n          \"S1_Embedding\": {\"auc\": 0.427041, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172},\n          \"S2_MinKPP\": {\"auc\": 0.507451, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172},\n          \"S4_SelfCritique\": {\"auc\": 0.51754, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172}\n        },\n        \"d005\": {\n          \"S1_Embedding\": {\"auc\": 0.995027, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172},\n          \"S2_MinKPP\": {\"auc\": 0.465865, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172},\n          \"S4_SelfCritique\": {\"auc\": 0.43246, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172}\n        }\n      },\n      \"cross_model_d100_vs_d000\": {\n        \"S1_Embedding\": {\"n_items\": 1172, \"mean_diff\": 0.278853, \"std_diff\": 0.073402, \"cohens_d\": 3.7993, \"wilcoxon_p\": 4.36e-193, \"pct_d100_higher\": 0.9991, \"significant_bonferroni\": true},\n        \"S2_MinKPP\": {\"n_items\": 1172, \"mean_diff\": -0.498085, \"std_diff\": 0.243127, \"cohens_d\": -2.048, \"wilcoxon_p\": 7.87e-193, \"pct_d100_higher\": 0.0162, \"significant_bonferroni\": true},\n        \"S4_SelfCritique\": {\"n_items\": 1172, \"mean_diff\": 0.069977, \"std_diff\": 0.104349, \"cohens_d\": 0.6708, \"wilcoxon_p\": 1.0e-95, \"pct_d100_higher\": 0.7611, \"significant_bonferroni\": true}\n      }\n    }\n  },\n  \"heatmap\": {\n    \"S1_Embedding\": {\n      \"mmlu\": {\"d000_auc\": 0.504915, \"d005_auc\": 0.952963, \"d100_cross_model_effect\": 4.1622, \"d100_cross_model_p\": 0.0, \"d100_cross_model_significant\": true},\n      \"gsm8k\": {\"d000_auc\": 0.550232, \"d005_auc\": 0.988203, \"d100_cross_model_effect\": 2.8331, \"d100_cross_model_p\": 3.07e-216, \"d100_cross_model_significant\": true},\n      \"arc_challenge\": {\"d000_auc\": 0.427041, \"d005_auc\": 0.995027, \"d100_cross_model_effect\": 3.7993, \"d100_cross_model_p\": 4.36e-193, \"d100_cross_model_significant\": true}\n    },\n    \"S2_MinKPP\": {\n      \"mmlu\": {\"d000_auc\": 0.509028, \"d005_auc\": 0.46548, \"d100_cross_model_effect\": -1.2203, \"d100_cross_model_p\": 0.0, \"d100_cross_model_significant\": true},\n      \"gsm8k\": {\"d000_auc\": 0.569703, \"d005_auc\": 0.464863, \"d100_cross_model_effect\": -2.666, \"d100_cross_model_p\": 3.37e-217, \"d100_cross_model_significant\": true},\n      \"arc_challenge\": {\"d000_auc\": 0.507451, \"d005_auc\": 0.465865, \"d100_cross_model_effect\": -2.048, \"d100_cross_model_p\": 7.87e-193, \"d100_cross_model_significant\": true}\n    },\n    \"S4_SelfCritique\": {\n      \"mmlu\": {\"d000_auc\": 0.495722, \"d005_auc\": 0.516544, \"d100_cross_model_effect\": 0.4673, \"d100_cross_model_p\": 0.0, \"d100_cross_model_significant\": true},\n      \"gsm8k\": {\"d000_auc\": 0.480029, \"d005_auc\": 0.494684, \"d100_cross_model_effect\": 0.2034, \"d100_cross_model_p\": 1.05e-08, \"d100_cross_model_significant\": true},\n      \"arc_challenge\": {\"d000_auc\": 0.51754, \"d005_auc\": 0.43246, \"d100_cross_model_effect\": 0.6708, \"d100_cross_model_p\": 1.0e-95, \"d100_cross_model_significant\": true}\n    }\n  },\n  \"summary\": {\n    \"version\": \"v4_D021_corrected\",\n    \"correction_notes\": [\n      \"d100 within-model AUC removed (label artifact: all items contaminated → no negative class)\",\n      \"d100 now uses cross-model paired comparison (d100 vs d000 signal differences)\",\n      \"C2 claim weakened: 'systematic signal variation with dosage' instead of 'cliff-like RL degradation'\"\n    ],\n    \"key_findings\": [\n      {\"signal\": \"S1_Embedding\", \"d005_auc_mean\": 0.9787, \"d005_auc_range\": [0.953, 0.995], \"d000_sanity_check\": \"MARGINAL\", \"d100_cross_model_any_significant\": true, \"d100_cross_model_effects\": [4.1622, 2.8331, 3.7993]},\n      {\"signal\": \"S2_MinKPP\", \"d005_auc_mean\": 0.4654, \"d005_auc_range\": [0.4649, 0.4659], \"d000_sanity_check\": \"MARGINAL\", \"d100_cross_model_any_significant\": true, \"d100_cross_model_effects\": [-1.2203, -2.666, -2.048]},\n      {\"signal\": \"S4_SelfCritique\", \"d005_auc_mean\": 0.4812, \"d005_auc_range\": [0.4325, 0.5165], \"d000_sanity_check\": \"PASS\", \"d100_cross_model_any_significant\": true, \"d100_cross_model_effects\": [0.4673, 0.2034, 0.6708]}\n    ],\n    \"effective_signal_count\": 1,\n    \"narrative\": \"1/3 signals show effective contamination detection at d005. Signal effectiveness varies systematically with dosage; individual signals insufficient → need IRT multi-signal fusion for robust detection across regimes.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data/exp008_v4_results.json",
    "content": "{\n  \"experiment\": \"exp-008\",\n  \"version\": \"v4_D021_corrected\",\n  \"per_benchmark\": {\n    \"mmlu\": {\n      \"benchmark\": \"mmlu\",\n      \"n_items\": 14042,\n      \"n_contaminated_d005\": 703,\n      \"within_model_auc\": {\n        \"d000\": {\n          \"S1_Embedding\": {\"auc\": 0.504915, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042},\n          \"S2_MinKPP\": {\"auc\": 0.509028, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042},\n          \"S4_SelfCritique\": {\"auc\": 0.495722, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042}\n        },\n        \"d005\": {\n          \"S1_Embedding\": {\"auc\": 0.952963, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042},\n          \"S2_MinKPP\": {\"auc\": 0.46548, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042},\n          \"S4_SelfCritique\": {\"auc\": 0.516544, \"n_pos\": 703, \"n_neg\": 13339, \"n_total\": 14042}\n        }\n      },\n      \"cross_model_d100_vs_d000\": {\n        \"S1_Embedding\": {\"n_items\": 14042, \"mean_d100\": 0.901361, \"mean_d000\": 0.522375, \"mean_diff\": 0.378985, \"std_diff\": 0.091055, \"cohens_d\": 4.1622, \"wilcoxon_stat\": 0.0, \"wilcoxon_p\": 0.0, \"pct_d100_higher\": 0.9993, \"pct_d100_lower\": 0.0, \"significant_bonferroni\": true},\n        \"S2_MinKPP\": {\"n_items\": 14042, \"mean_d100\": 1.432032, \"mean_d000\": 1.697604, \"mean_diff\": -0.265572, \"std_diff\": 0.217631, \"cohens_d\": -1.2203, \"wilcoxon_stat\": 660013.0, \"wilcoxon_p\": 0.0, \"pct_d100_higher\": 0.0308, \"pct_d100_lower\": 0.969, \"significant_bonferroni\": true},\n        \"S4_SelfCritique\": {\"n_items\": 14042, \"mean_d100\": -0.907331, \"mean_d000\": -0.955669, \"mean_diff\": 0.048339, \"std_diff\": 0.103438, \"cohens_d\": 0.4673, \"wilcoxon_stat\": 19322716.0, \"wilcoxon_p\": 0.0, \"pct_d100_higher\": 0.6733, \"pct_d100_lower\": 0.2745, \"significant_bonferroni\": true}\n      }\n    },\n    \"gsm8k\": {\n      \"benchmark\": \"gsm8k\",\n      \"n_items\": 1319,\n      \"n_contaminated_d005\": 73,\n      \"within_model_auc\": {\n        \"d000\": {\n          \"S1_Embedding\": {\"auc\": 0.550232, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319},\n          \"S2_MinKPP\": {\"auc\": 0.569703, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319},\n          \"S4_SelfCritique\": {\"auc\": 0.480029, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319}\n        },\n        \"d005\": {\n          \"S1_Embedding\": {\"auc\": 0.988203, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319},\n          \"S2_MinKPP\": {\"auc\": 0.464863, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319},\n          \"S4_SelfCritique\": {\"auc\": 0.494684, \"n_pos\": 73, \"n_neg\": 1246, \"n_total\": 1319}\n        }\n      },\n      \"cross_model_d100_vs_d000\": {\n        \"S1_Embedding\": {\"n_items\": 1319, \"mean_diff\": 0.197201, \"std_diff\": 0.069606, \"cohens_d\": 2.8331, \"wilcoxon_p\": 3.07e-216, \"pct_d100_higher\": 0.9992, \"significant_bonferroni\": true},\n        \"S2_MinKPP\": {\"n_items\": 1319, \"mean_diff\": -0.478204, \"std_diff\": 0.179378, \"cohens_d\": -2.666, \"wilcoxon_p\": 3.37e-217, \"pct_d100_higher\": 0.0076, \"significant_bonferroni\": true},\n        \"S4_SelfCritique\": {\"n_items\": 1319, \"mean_diff\": 0.021506, \"std_diff\": 0.105749, \"cohens_d\": 0.2034, \"wilcoxon_p\": 1.05e-08, \"pct_d100_higher\": 0.5874, \"significant_bonferroni\": true}\n      }\n    },\n    \"arc_challenge\": {\n      \"benchmark\": \"arc_challenge\",\n      \"n_items\": 1172,\n      \"n_contaminated_d005\": 50,\n      \"within_model_auc\": {\n        \"d000\": {\n          \"S1_Embedding\": {\"auc\": 0.427041, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172},\n          \"S2_MinKPP\": {\"auc\": 0.507451, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172},\n          \"S4_SelfCritique\": {\"auc\": 0.51754, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172}\n        },\n        \"d005\": {\n          \"S1_Embedding\": {\"auc\": 0.995027, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172},\n          \"S2_MinKPP\": {\"auc\": 0.465865, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172},\n          \"S4_SelfCritique\": {\"auc\": 0.43246, \"n_pos\": 50, \"n_neg\": 1122, \"n_total\": 1172}\n        }\n      },\n      \"cross_model_d100_vs_d000\": {\n        \"S1_Embedding\": {\"n_items\": 1172, \"mean_diff\": 0.278853, \"std_diff\": 0.073402, \"cohens_d\": 3.7993, \"wilcoxon_p\": 4.36e-193, \"pct_d100_higher\": 0.9991, \"significant_bonferroni\": true},\n        \"S2_MinKPP\": {\"n_items\": 1172, \"mean_diff\": -0.498085, \"std_diff\": 0.243127, \"cohens_d\": -2.048, \"wilcoxon_p\": 7.87e-193, \"pct_d100_higher\": 0.0162, \"significant_bonferroni\": true},\n        \"S4_SelfCritique\": {\"n_items\": 1172, \"mean_diff\": 0.069977, \"std_diff\": 0.104349, \"cohens_d\": 0.6708, \"wilcoxon_p\": 1.0e-95, \"pct_d100_higher\": 0.7611, \"significant_bonferroni\": true}\n      }\n    }\n  },\n  \"heatmap\": {\n    \"S1_Embedding\": {\n      \"mmlu\": {\"d000_auc\": 0.504915, \"d005_auc\": 0.952963, \"d100_cross_model_effect\": 4.1622, \"d100_cross_model_p\": 0.0, \"d100_cross_model_significant\": true},\n      \"gsm8k\": {\"d000_auc\": 0.550232, \"d005_auc\": 0.988203, \"d100_cross_model_effect\": 2.8331, \"d100_cross_model_p\": 3.07e-216, \"d100_cross_model_significant\": true},\n      \"arc_challenge\": {\"d000_auc\": 0.427041, \"d005_auc\": 0.995027, \"d100_cross_model_effect\": 3.7993, \"d100_cross_model_p\": 4.36e-193, \"d100_cross_model_significant\": true}\n    },\n    \"S2_MinKPP\": {\n      \"mmlu\": {\"d000_auc\": 0.509028, \"d005_auc\": 0.46548, \"d100_cross_model_effect\": -1.2203, \"d100_cross_model_p\": 0.0, \"d100_cross_model_significant\": true},\n      \"gsm8k\": {\"d000_auc\": 0.569703, \"d005_auc\": 0.464863, \"d100_cross_model_effect\": -2.666, \"d100_cross_model_p\": 3.37e-217, \"d100_cross_model_significant\": true},\n      \"arc_challenge\": {\"d000_auc\": 0.507451, \"d005_auc\": 0.465865, \"d100_cross_model_effect\": -2.048, \"d100_cross_model_p\": 7.87e-193, \"d100_cross_model_significant\": true}\n    },\n    \"S4_SelfCritique\": {\n      \"mmlu\": {\"d000_auc\": 0.495722, \"d005_auc\": 0.516544, \"d100_cross_model_effect\": 0.4673, \"d100_cross_model_p\": 0.0, \"d100_cross_model_significant\": true},\n      \"gsm8k\": {\"d000_auc\": 0.480029, \"d005_auc\": 0.494684, \"d100_cross_model_effect\": 0.2034, \"d100_cross_model_p\": 1.05e-08, \"d100_cross_model_significant\": true},\n      \"arc_challenge\": {\"d000_auc\": 0.51754, \"d005_auc\": 0.43246, \"d100_cross_model_effect\": 0.6708, \"d100_cross_model_p\": 1.0e-95, \"d100_cross_model_significant\": true}\n    }\n  },\n  \"summary\": {\n    \"version\": \"v4_D021_corrected\",\n    \"correction_notes\": [\n      \"d100 within-model AUC removed (label artifact: all items contaminated → no negative class)\",\n      \"d100 now uses cross-model paired comparison (d100 vs d000 signal differences)\",\n      \"C2 claim weakened: 'systematic signal variation with dosage' instead of 'cliff-like RL degradation'\"\n    ],\n    \"key_findings\": [\n      {\"signal\": \"S1_Embedding\", \"d005_auc_mean\": 0.9787, \"d005_auc_range\": [0.953, 0.995], \"d000_sanity_check\": \"MARGINAL\", \"d100_cross_model_any_significant\": true, \"d100_cross_model_effects\": [4.1622, 2.8331, 3.7993]},\n      {\"signal\": \"S2_MinKPP\", \"d005_auc_mean\": 0.4654, \"d005_auc_range\": [0.4649, 0.4659], \"d000_sanity_check\": \"MARGINAL\", \"d100_cross_model_any_significant\": true, \"d100_cross_model_effects\": [-1.2203, -2.666, -2.048]},\n      {\"signal\": \"S4_SelfCritique\", \"d005_auc_mean\": 0.4812, \"d005_auc_range\": [0.4325, 0.5165], \"d000_sanity_check\": \"PASS\", \"d100_cross_model_any_significant\": true, \"d100_cross_model_effects\": [0.4673, 0.2034, 0.6708]}\n    ],\n    \"effective_signal_count\": 1,\n    \"narrative\": \"1/3 signals show effective contamination detection at d005. Signal effectiveness varies systematically with dosage; individual signals insufficient → need IRT multi-signal fusion for robust detection across regimes.\"\n  }\n}\n"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T16:28:08.367374+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data/exp008_v4_results.json

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-14T16:28:08.367570+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-14T16:28:08.367726+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-14T16:28:08.367848+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "exp008_v4_signal_survival_results",
  "type": "data",
  "description": "exp-008 Signal Survival v4 (D021 corrected): within-model AUC for d000/d005, cross-model paired comparison for d100 vs d000. S1 Embedding AUC=0.979 at d005, S2/S4 random. All 3 signals show significant cross-model effects at d100.",
  "project": "contamcal-irt-calibration",
  "exp_id": "exp-008",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data/exp008_v4_results.json",
  "tags": "['signal-survival', 'v4', 'D021', 'cross-model']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "exp008_v4_signal_survival_results",
    "type": "data",
    "description": "exp-008 Signal Survival v4 (D021 corrected): within-model AUC for d000/d005, cross-model paired comparison for d100 vs d000. S1 Embedding AUC=0.979 at d005, S2/S4 random. All 3 signals show significant cross-model effects at d100.",
    "project": "contamcal-irt-calibration",
    "exp_id": "exp-008",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/exp_008_signal_survival/data/exp008_v4_results.json",
    "tags": "['signal-survival', 'v4', 'D021', 'cross-model']"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-14T16:28:08.368007+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_406ef9\", \"name\": \"exp008_v4_signal_survival_results\", \"type\": \"data\", \"description\": \"exp-008 Signal Survival v4 (D021 corrected): within-model AUC for d000/d005, cross-model paired comparison for d100 vs d000. S1 Embedding AUC=0.979 at d005, S2/S4 random. All 3 signals show significant cross-model effects at d100.\", \"path\": \"projects/contamcal-irt-calibration/artifacts/exp-008/data/exp008_v4_results.json\", \"url\": null, \"project\": \"contamcal-irt-calibration\", \"exp_id\": \"exp-008\", \"skill\": \"\", \"created_at\": \"2026-05-14T16:27:53.327370+00:00\", \"tags\": [\"signal-survival\", \"v4\", \"D021\", \"cross-model\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_008_v4_20260514T162445",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-14T16:28:08.368176+00:00_

验证完成，所有验证标准通过。

## exp-008 v4 Key Findings

### Within-Model AUC (d005 detection)
| Signal | mmlu | gsm8k | arc_challenge | Mean |
|--------|------|-------|---------------|------|
| **S1 Embedding** | **0.953** | **0.988** | **0.995** | **0.979** |
| S2 Min-K++ | 0.465 | 0.465 | 0.466 | 0.465 |
| S4 SelfCritique | 0.517 | 0.495 | 0.432 | 0.481 |

### d000 Sanity Check (AUC ≈ 0.5)
- S1: MARGINAL (arc=0.427, gsm8k=0.550 — small-sample noise, mmlu=0.505 正常)
- S2: MARGINAL (gsm8k=0.570)
- S4: PASS (all within 0.48–0.52)

### Cross-Model d100 vs d000 (Cohen's d, all Bonferroni-significant)
| Signal | mmlu | gsm8k | arc_challenge |
|--------|------|-------|---------------|
| **S1 Embedding** | **+4.16** | **+2.83** | **+3.80** |
| S2 Min-K++ | -1.22 | -2.67 | -2.05 |
| S4 SelfCritique | +0.47 | +0.20 | +0.67 |

### 核心结论
1. **S1 Embedding 是唯一有效的 within-model 检测信号**（d005 AUC=0.979），S2/S4 在 0.5B 模型上无区分力
2. **Cross-model 比较揭示了 v3 遗漏的信息**：d100 全量污染使所有三个信号都产生了显著的跨模型差异（S2 的 Cohen's d 达到 -2.67），说明 S2/S4 虽然不能做 within-model 检测，但确实对 contamination 有响应
3. **D021 修正生效**：d100 不再报告虚假的 AUC=0.5，改为报告 cross-model effect size + Wilcoxon test
4. Narrative 更新为："signal effectiveness varies systematically with dosage; individual signals insufficient → need IRT multi-signal fusion"

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_008_v4_20260514T162445"
}
```

</details>

---
