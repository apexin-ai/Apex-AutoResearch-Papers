# analysis bootstrap gemma2 rerun

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 81
- **Recorded user turns:** 0
- **Tool calls:** 40
- **Original source:** `logs/chats/worker_analysis_bootstrap-gemma2-rerun_20260521T070853.jsonl`
- **Structured JSON:** [`26f6c68e8b64fdd9545f.json`](../../sessions/26/26f6c68e8b64fdd9545f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

81 recorded events

### Tool call

_source line 1 · 2026-05-21T07:12:04.766246+00:00_

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
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
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

_source line 2 · 2026-05-21T07:12:04.766814+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T07:12:04.767069+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration -name \"*bootstrap*\" -type f 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration -name \"*bootstrap*\" -type f 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T07:12:04.767269+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T07:12:04.767481+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration -name \"*bootstrap*\" -type d 2>/dev/null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration -name \"*bootstrap*\" -type d 2>/dev/null"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T07:12:04.767663+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T07:12:04.767894+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration -name \"*bootstrap*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration -name \"*bootstrap*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-21T07:12:04.768108+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.88}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-21T07:12:04.768351+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/gemma2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/gemma2/"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T07:12:04.768555+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/results/arc_eval/gemma2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/results/arc_eval/gemma2/"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T07:12:04.768739+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/contamcal-irt-calibration/results/mmlu_eval/gemma2/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T07:12:04.768929+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/contamcal-irt-calibration/results/arc_eval/gemma2/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.74}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T07:12:04.769141+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/results -type d -name \"gemma2\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/results -type d -name \"gemma2\""
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T07:12:04.769345+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T07:12:04.769526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/results/"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-21T07:12:04.769697+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -80 /root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -80 /root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-21T07:12:04.769881+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"gsm8k\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-21T07:12:04.770142+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Bootstrap item-level analysis for dose-response profile stability.\\n\\nAnalyses:\\n1. Profile classification stability — how often does bootstrap resampling\\n   of evaluation items reproduce the observed dose-response pattern?\\n2. Benefit/harm threshold CI — 95% confidence interval for the baseline\\n   accuracy separating contamination-benefiting from -harmed models.\\n\\nData layout:\\n    {data_dir}/{model}_{dosage}[{suffix}]/correctness_matrix.json\\n    or  .../item_responses.json\\n\\nUsage:\\n    python bootstrap_profile_stability.py \\\\\\n        --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \\\\\\n        --benchmark mmlu --n-bootstrap 10000\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport time\\nfrom collections import Counter\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\n# ── Registry ────────────────────────────────────────────────────────\\n\\nMODELS = {\\n    'phi4':    'Phi-4 14.7B',\\n    'qwen14b': 'Qwen2.5-14B',\\n    'qwen7b':  'Qwen2.5-7B',\\n    'gemma2':  'Gemma-2 9B',\\n    'olmo2':   'OLMo-2 7B',\\n}\\n\\nDOSAGES = ['d000', 'd005', 'd025', 'd050', 'd100']\\nDOSE_LABELS = ['0%', '5%', '25%', '50%', '100%']\\n\\n# ── Data loading ────────────────────────────────────────────────────\\n\\ndef load_responses(data_dir, model, dosage, benchmark, suffix=''):\\n    \\\"\\\"\\\"Load boolean correctness array for one model x dosage x benchmark.\\n\\n    Tries correctness_matrix.json first (compact), falls back to\\n    item_responses.json.\\n    \\\"\\\"\\\"\\n    base = Path(data_dir) / f'{model}_{dosage}{suffix}'\\n\\n    # Fast path: correctness_matrix.json\\n    cm = base / 'correctness_matrix.json'\\n    if cm.exists():\\n        with open(cm) as f:\\n            data = json.load(f)\\n        if benchmark in data:\\n            return np.array(data[benchmark], dtype=np.int8)\\n\\n    # Fallback: item_re
…[truncated 773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T07:12:04.770472+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-21T07:12:04.770682+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration -name \"correctness_matrix.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration -name \"correctness_matrix.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-21T07:12:04.771014+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"#!/usr/bin/env python3\\n\\\"\\\"\\\"Bootstrap item-level analysis for dose-response profile stability.\\n\\nAnalyses:\\n1. Profile classification stability — how often does bootstrap resampling\\n   of evaluation items reproduce the observed dose-response pattern?\\n2. Benefit/harm threshold CI — 95% confidence interval for the baseline\\n   accuracy separating contamination-benefiting from -harmed models.\\n\\nData layout:\\n    {data_dir}/{model}_{dosage}[{suffix}]/correctness_matrix.json\\n    or  .../item_responses.json\\n\\nUsage:\\n    python bootstrap_profile_stability.py \\\\\\n        --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \\\\\\n        --benchmark mmlu --n-bootstrap 10000\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport json\\nimport os\\nimport sys\\nimport time\\nfrom collections import Counter\\nfrom pathlib import Path\\n\\nimport numpy as np\\n\\n# ── Registry ────────────────────────────────────────────────────────\\n\\nMODELS = {\\n    'phi4':    'Phi-4 14.7B',\\n    'qwen14b': 'Qwen2.5-14B',\\n    'qwen7b':  'Qwen2.5-7B',\\n    'gemma2':  'Gemma-2 9B',\\n    'olmo2':   'OLMo-2 7B',\\n}\\n\\nDOSAGES = ['d000', 'd005', 'd025', 'd050', 'd100']\\nDOSE_LABELS = ['0%', '5%', '25%', '50%', '100%']\\n\\n# ── Data loading ────────────────────────────────────────────────────\\n\\ndef load_responses(data_dir, model, dosage, benchmark, suffix=''):\\n    \\\"\\\"\\\"Load boolean correctness array for one model x dosage x benchmark.\\n\\n    Tries correctness_matrix.json first (compact), falls back to\\n    item_responses.json.\\n    \\\"\\\"\\\"\\n    base = Path(data_dir) / f'{model}_{dosage}{suffix}'\\n\\n    # Fast path: correctness_matrix.json\\n    cm = base / 'correctness_matrix.json'\\n    if cm.exists():\\n        with open(cm) as f:\\n            data = json.load(f)\\n        if benchmark in data:\\n            return np.array(data[benchmark], dtype=np.int8)\\n\\n    # Fallback: item_re
…[truncated 6876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T07:12:04.771263+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d000_s42/correctness_matrix.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d100_s42/correctness_matrix.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d005_s42/correctness_matrix.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d025_s42/correctness_matrix.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d050_s42/correctness_matrix.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d000_s123/correctness_matrix.json\\n/root/contamcal-irt-calibration/results/gsm8k/qwen7b_d100_s123/correctness_matrix.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T07:12:04.771488+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root -maxdepth 3 -name \"eval_results*\" -type d"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root -maxdepth 3 -name \"eval_results*\" -type d"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T07:12:04.771678+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/structfuse/eval_results\\n/root/autodl-tmp/exp001/eval_results\\n/root/autodl-tmp/exp001/eval_results_cross_family\\n/root/autodl-tmp/exp001/eval_results_v2\\n/root/autodl-tmp/exp008/eval_results\\n/root/autodl-tmp/exp009/eval_results\\n/root/contamcal-irt-calibration/exp001/eval_results\\n/root/contamcal-irt-calibration/outputs/eval_results\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T07:12:04.771900+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp001/eval_results_v2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp001/eval_results_v2/"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T07:12:04.772094+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"qwen7b_d000_s0\\nqwen7b_d000_s123\\nqwen7b_d000_s123_old_20260520\\nqwen7b_d000_s42_v2\\nqwen7b_d005_s0\\nqwen7b_d005_s123\\nqwen7b_d005_s123_old_20260520\\nqwen7b_d005_s42_v2\\nqwen7b_d025_s0\\nqwen7b_d025_s123\\nqwen7b_d025_s123_old_20260520\\nqwen7b_d025_s42_v2\\nqwen7b_d050_s0\\nqwen7b_d050_s123\\nqwen7b_d050_s123_old_20260520\\nqwen7b_d050_s42_v2\\nqwen7b_d100_s0\\nqwen7b_d100_s123\\nqwen7b_d100_s123_old_20260520\\nqwen7b_d100_s42_v2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T07:12:04.772289+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/contamcal-irt-calibration/outputs/eval_results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/contamcal-irt-calibration/outputs/eval_results/"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T07:12:04.772507+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T07:12:04.772681+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root -maxdepth 4 -name \"correctness_matrix.json\" -path \"*gemma2*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root -maxdepth 4 -name \"correctness_matrix.json\" -path \"*gemma2*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T07:12:04.772857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T07:12:04.773067+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T07:12:04.773254+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"arc_eval\\neval_results_v2\\ngsm8k\\ngsm8k_eval\\nmmlu_eval\\nqwen14b_d050_s0_arc\\nqwen14b_d050_s0_mmlu\\nqwen14b_d100_s0_arc\\nqwen14b_d100_s0_mmlu\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.07}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T07:12:04.773476+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/gemma2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/gemma2/"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T07:12:04.773658+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s0\\nd000_s123\\nd005_s0\\nd005_s123\\nd025_s0\\nd025_s123\\nd050_s0\\nd050_s123\\nd100_s0\\nd100_s123\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T07:12:04.773829+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/arc_eval/gemma2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/arc_eval/gemma2/"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T07:12:04.774009+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s0\\nd000_s123\\nd000_s42\\nd005_s0\\nd005_s123\\nd005_s42\\nd025_s0\\nd025_s0_rerun\\nd025_s123\\nd025_s42\\nd050_s0\\nd050_s123\\nd050_s42\\nd100_s0\\nd100_s123\\nd100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T07:12:04.774197+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration -name \"*bootstrap*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration -name \"*bootstrap*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T07:12:04.774422+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/analysis/results/bootstrap_delta_mmlu.png\\n/root/contamcal-irt-calibration/analysis/results/bootstrap_dose_response_mmlu.png\\n/root/contamcal-irt-calibration/analysis/results/bootstrap_results_mmlu.json\\n/root/contamcal-irt-calibration/analysis/results/bootstrap_delta_arc_challenge.png\\n/root/contamcal-irt-calibration/analysis/results/bootstrap_dose_response_arc_challenge.png\\n/root/contamcal-irt-calibration/analysis/results/bootstrap_results_arc_challenge.json\\n/root/contamcal-irt-calibration/analysis/bootstrap_profile_stability.py\\n/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py\\n/root/contamcal-irt-calibration/analysis/bootstrap_results.txt\\n/root/contamcal-irt-calibration/analysis/bootstrap_table.tex\\n/root/contamcal-irt-calibration/analysis/analysis/bootstrap_results.txt\\n/root/contamcal-irt-calibration/analysis/analysis/bootstrap_table.tex\\n/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py.bak_d188\\n/root/contamcal-irt-calibration/analysis/__pycache__/bootstrap_triple_seed.cpython-312.pyc\\n/root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py.bak\\n/root/contamcal-irt-calibration/analysis/bootstrap_results_mmlu.txt\\n/root/contamcal-irt-calibration/analysis/bootstrap_table_mmlu.tex\\n/root/contamcal-irt-calibration/analysis/bootstrap_results_arc.txt\\n/root/contamcal-irt-calibration/analysis/bootstrap_table_arc.tex\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T07:12:04.774616+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T07:12:04.774787+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/arc_eval/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/arc_eval/"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T07:12:04.774973+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"gemma2\\nolmo2\\nphi4\\nqwen14b\\nqwen7b\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T07:12:04.775141+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"gemma2\\nolmo2\\nphi4\\nqwen14b\\nqwen7b\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-21T07:12:04.775378+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_triple_seed.py"
  }
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-21T07:12:04.775680+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_results.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_results.txt"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T07:12:04.776046+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nTriple-seed bootstrap CI analysis for MMLU dose-response patterns.\\n\\nReads MMLU accuracy data from multiple sources (JSON result files + CSV summaries),\\ncomputes bootstrap confidence intervals for contamination effects (Δ accuracy),\\nclassifies dose-response patterns, and measures cross-seed pattern stability.\\n\\nInputs:\\n  - results/mmlu_eval/{family}/d{dosage}_s{seed}/mmlu_results.json\\n  - analysis/results/gsm8k/mmlu_summary.csv (legacy s42 data)\\nOutputs:\\n  - analysis/bootstrap_results.txt  (formatted tables)\\n  - analysis/bootstrap_table.tex    (LaTeX table for paper)\\n\\nDependencies: numpy, scipy\\n\\\"\\\"\\\"\\n\\nimport argparse\\nimport csv\\nimport json\\nimport os\\nimport sys\\nfrom collections import defaultdict\\nfrom itertools import combinations\\nfrom pathlib import Path\\n\\nimport numpy as np\\nfrom scipy.stats import spearmanr\\n\\n# ── Constants ─────────────────────────────────────────────────────���────────\\n\\nFAMILIES = [\\\"Phi-4\\\", \\\"Qwen2.5-14B\\\", \\\"Qwen2.5-7B\\\", \\\"Gemma-2-9B\\\", \\\"OLMo-2-7B\\\"]\\nDOSAGES = [\\\"d000\\\", \\\"d005\\\", \\\"d025\\\", \\\"d050\\\", \\\"d100\\\"]\\nSEEDS = [42, 123, 0]\\n\\nDISPLAY_TO_DIR = {\\n    \\\"Phi-4\\\": \\\"phi4\\\",\\n    \\\"Qwen2.5-14B\\\": \\\"qwen14b\\\",\\n    \\\"Qwen2.5-7B\\\": \\\"qwen7b\\\",\\n    \\\"Gemma-2-9B\\\": \\\"gemma2\\\",\\n    \\\"OLMo-2-7B\\\": \\\"olmo2\\\",\\n}\\nDIR_TO_DISPLAY = {v: k for k, v in DISPLAY_TO_DIR.items()}\\n\\nN_BOOTSTRAP = 10000\\nCI_LEVEL = 0.95\\nRNG_SEED = 42\\n\\nBENCHMARK_CONFIG = {\\n    \\\"mmlu\\\": {\\\"eval_dir\\\": \\\"mmlu_eval\\\", \\\"result_file\\\": \\\"mmlu_results.json\\\", \\\"label\\\": \\\"MMLU\\\"},\\n    \\\"arc\\\": {\\\"eval_dir\\\": \\\"arc_eval\\\", \\\"result_file\\\": \\\"arc_challenge_results.json\\\", \\\"label\\\": \\\"ARC-Challenge\\\"},\\n}\\n\\n\\n# ── Data loading ───────────────────────────────────────────────────────
…[truncated 7424 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-21T07:12:04.776373+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"==========================================================================================\\nBOOTSTRAP CI: ACCURACY BY DOSAGE (mean ± 95% CI across seeds)\\n==========================================================================================\\nFamily            n                d000                d005                d025                d050                d100\\n-----------------------------------------------------------------------------------------------------------------------\\nPhi-4             3  76.40 [76.31,76.44](boot)  76.24 [75.92,76.41](boot)  76.91 [76.72,77.01](boot)  77.11 [76.75,77.30](boot)  77.12 [76.27,77.74](boot)\\nQwen2.5-14B       2  69.05 [64.12,73.99](t)  69.93 [58.30,81.56](t)  62.86 [52.41,73.31](t)  60.20 [50.15,70.24](t)  58.00 [31.71,84.29](t)\\nQwen2.5-7B        2  66.35 [63.27,69.43](t)  64.06 [55.37,72.74](t)  63.90 [52.23,75.57](t)  64.03 [51.77,76.29](t)  65.46 [51.11,79.80](t)\\nGemma-2-9B        2  63.85 [38.61,89.10](t)  64.61 [49.41,79.82](t)  63.79 [53.97,73.61](t)  65.38 [48.00,82.75](t)  66.48 [55.66,77.29](t)\\nOLMo-2-7B         3  54.93 [53.79,55.55](boot)  56.30 [56.14,56.46](boot)  55.89 [54.97,56.41](boot)  56.48 [55.92,56.92](boot)  56.28 [55.11,56.91](boot)\\n\\n==========================================================================================\\nBOOTSTRAP CI: Δ(d100) = acc(d100) - acc(d000)  [percentage points]\\n==========================================================================================\\nFamily            n  Baseline  Δ(d100) mean                95% CI    p(Δ=0)\\n---------------------------------------------------------------------------\\nPhi-4             3    76.40%        +0.72pp        [-0.17, +1.39](boot)     0.039\\nQwen2.5-14B       2    69.05%       -11.05pp         [-32.41, +10.30](t)     0.000\\nQwen2.5-7B        2    66.35%        -0.89pp         [-12.16, +10.37](t)     0.000\\nGemma-2-9B        2    63.85%        +2.6
…[truncated 2881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-21T07:12:04.776653+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/phi4/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/phi4/"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-21T07:12:04.776857+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s0\\nd000_s123\\nd005_s0\\nd005_s123\\nd025_s0\\nd025_s123\\nd050_s0\\nd050_s123\\nd100_s0\\nd100_s123\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-21T07:12:04.777043+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/qwen14b/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/qwen14b/"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-21T07:12:04.777218+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/qwen7b/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/qwen7b/"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T07:12:04.777425+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s0\\nd000_s123\\nd000_s42\\nd005_s0\\nd005_s123\\nd005_s42\\nd025_s0\\nd025_s123\\nd025_s42\\nd050_s123\\nd050_s42\\nd100_s123\\nd100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-21T07:12:04.777610+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s123\\nd005_s123\\nd025_s123\\nd050_s123\\nd100_s123\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-21T07:12:04.777815+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/olmo2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/olmo2/"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-21T07:12:04.777985+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s0\\nd000_s123\\nd005_s0\\nd005_s123\\nd025_s0\\nd025_s123\\nd050_s0\\nd050_s123\\nd100_s0\\nd100_s123\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-21T07:12:04.778149+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/arc_eval/phi4/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/arc_eval/phi4/"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-21T07:12:04.778341+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s0\\nd000_s123\\nd000_s42\\nd005_s0\\nd005_s123\\nd005_s42\\nd025_s0\\nd025_s123\\nd025_s42\\nd050_s0\\nd050_s123\\nd050_s42\\nd100_s0\\nd100_s123\\nd100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-21T07:12:04.778525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/arc_eval/qwen14b/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/arc_eval/qwen14b/"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-21T07:12:04.778699+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s0\\nd000_s123\\nd000_s42\\nd005_s0\\nd005_s123\\nd005_s42\\nd025_s0\\nd025_s123\\nd025_s42\\nd050_s123\\nd050_s42\\nd100_s0\\nd100_s123\\nd100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-21T07:12:04.778861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/arc_eval/qwen7b/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/arc_eval/qwen7b/"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-21T07:12:04.779028+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/arc_eval/olmo2/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/arc_eval/olmo2/"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-21T07:12:04.779205+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s123\\nd000_s42\\nd005_s123\\nd005_s42\\nd025_s123\\nd025_s42\\nd050_s123\\nd050_s42\\nd100_s123\\nd100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-21T07:12:04.779406+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"d000_s0\\nd000_s123\\nd000_s42\\nd005_s0\\nd005_s123\\nd005_s42\\nd025_s0\\nd025_s123\\nd025_s42\\nd050_s0\\nd050_s123\\nd050_s42\\nd100_s0\\nd100_s123\\nd100_s42\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-21T07:12:04.779634+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_results_arc.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_results_arc.txt"
  }
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-21T07:12:04.779891+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"==========================================================================================\\nBOOTSTRAP CI: ACCURACY BY DOSAGE (mean ± 95% CI across seeds)\\n==========================================================================================\\nFamily            n                d000                d005                d025                d050                d100\\n-----------------------------------------------------------------------------------------------------------------------\\nPhi-4             3  91.92 [91.81,92.06](boot)  92.09 [91.81,92.35](boot)  92.38 [92.24,92.49](boot)  92.61 [92.41,92.75](boot)  92.58 [92.32,92.72](boot)\\nQwen2.5-14B       2  90.74 [86.95,94.54](t)  90.91 [83.87,97.96](t)  89.33 [83.91,94.76](t)  88.18 [81.14,95.23](t)  87.88 [80.29,95.47](t)\\nQwen2.5-7B        2  87.50 [82.62,92.38](t)  84.26 [60.95,107.57](t)  84.60 [77.55,91.65](t)  84.81 [81.56,88.06](t)  84.85 [83.23,86.48](t)\\nGemma-2-9B        1   85.84pp (pt)         83.36pp (pt)         85.67pp (pt)         85.24pp (pt)         88.57pp (pt)      \\nOLMo-2-7B         3  76.28 [75.85,76.62](boot)  76.88 [76.62,77.08](boot)  77.79 [76.62,78.44](boot)  79.10 [78.50,79.47](boot)  79.72 [79.35,79.95](boot)\\n\\n==========================================================================================\\nBOOTSTRAP CI: Δ(d100) = acc(d100) - acc(d000)  [percentage points]\\n==========================================================================================\\nFamily            n  Baseline  Δ(d100) mean                95% CI    p(Δ=0)\\n---------------------------------------------------------------------------\\nPhi-4             3    91.92%        +0.65pp        [+0.51, +0.77](boot)     0.000\\nQwen2.5-14B       2    90.74%        -2.86pp           [-6.65, +0.94](t)     0.000\\nQwen2.5-7B        2    87.50%        -2.65pp           [-5.90, +0.61](t)     0.000\\nGemma-2-9B        1    85.84%        +2.73pp          [
…[truncated 2849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-21T07:12:04.780091+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_results_mmlu.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "cat /root/contamcal-irt-calibration/analysis/bootstrap_results_mmlu.txt"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-21T07:12:04.780291+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "find /root/contamcal-irt-calibration -name \"mmlu_summary.csv\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "find /root/contamcal-irt-calibration -name \"mmlu_summary.csv\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-21T07:12:04.780566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"==========================================================================================\\nBOOTSTRAP CI: ACCURACY BY DOSAGE (mean ± 95% CI across seeds)\\n==========================================================================================\\nFamily            n                d000                d005                d025                d050                d100\\n-----------------------------------------------------------------------------------------------------------------------\\nPhi-4             3  76.40 [76.31,76.44](boot)  76.24 [75.92,76.41](boot)  76.91 [76.72,77.01](boot)  77.11 [76.75,77.30](boot)  77.12 [76.27,77.74](boot)\\nQwen2.5-14B       2  69.05 [64.12,73.99](t)  69.93 [58.30,81.56](t)  62.86 [52.41,73.31](t)  60.20 [50.15,70.24](t)  58.00 [31.71,84.29](t)\\nQwen2.5-7B        2  66.35 [63.27,69.43](t)  64.06 [55.37,72.74](t)  63.90 [52.23,75.57](t)  64.03 [51.77,76.29](t)  65.46 [51.11,79.80](t)\\nGemma-2-9B        2  63.85 [38.61,89.10](t)  64.61 [49.41,79.82](t)  63.79 [53.97,73.61](t)  65.38 [48.00,82.75](t)  66.48 [55.66,77.29](t)\\nOLMo-2-7B         3  54.93 [53.79,55.55](boot)  56.30 [56.14,56.46](boot)  55.89 [54.97,56.41](boot)  56.48 [55.92,56.92](boot)  56.28 [55.11,56.91](boot)\\n\\n==========================================================================================\\nBOOTSTRAP CI: Δ(d100) = acc(d100) - acc(d000)  [percentage points]\\n==========================================================================================\\nFamily            n  Baseline  Δ(d100) mean                95% CI    p(Δ=0)\\n---------------------------------------------------------------------------\\nPhi-4             3    76.40%        +0.72pp        [-0.17, +1.39](boot)     0.039\\nQwen2.5-14B       2    69.05%       -11.05pp         [-32.41, +10.30](t)     0.000\\nQwen2.5-7B        2    66.35%        -0.89pp         [-12.16, +10.37](t)     0.000\\nGemma-2-9B        2    63.85%        +2.6
…[truncated 2881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-21T07:12:04.780785+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/contamcal-irt-calibration/analysis/results/gsm8k/mmlu_summary.csv\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-21T07:12:04.781010+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "grep -i gemma /root/contamcal-irt-calibration/analysis/results/gsm8k/mmlu_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "grep -i gemma /root/contamcal-irt-calibration/analysis/results/gsm8k/mmlu_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-21T07:12:04.781194+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Gemma-2-9B,d000,0.000000,42,0.618644,0.000000\\nGemma-2-9B,d005,0.500000,42,0.634169,0.015525\\nGemma-2-9B,d025,2.500000,42,0.645635,0.026990\\nGemma-2-9B,d050,5.000000,42,0.640080,0.021436\\nGemma-2-9B,d100,10.000000,42,0.656246,0.037601\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-21T07:12:04.781386+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "head -1 /root/contamcal-irt-calibration/analysis/results/gsm8k/mmlu_summary.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "head -1 /root/contamcal-irt-calibration/analysis/results/gsm8k/mmlu_summary.csv"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-21T07:12:04.781572+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"model_display,dosage,dosage_pct,seed,accuracy,delta_acc\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-21T07:12:04.781780+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/gemma2/d000_s0/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/mmlu_eval/gemma2/d000_s0/"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-21T07:12:04.781958+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"correctness_matrix.json\\neval_results.json\\nitem_responses.json\\nmmlu_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-21T07:12:04.782128+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-29999",
  "command": "ls /root/contamcal-irt-calibration/results/arc_eval/gemma2/d000_s42/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-29999",
    "command": "ls /root/contamcal-irt-calibration/results/arc_eval/gemma2/d000_s42/"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-21T07:12:04.782299+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"arc_challenge_results.json\\ncorrectness_matrix.json\\neval_results.json\\nitem_responses.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-21T07:12:04.782519+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "cd /root/contamcal-irt-calibration && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analysis/bootstrap_triple_seed.py --results-dir results/ --output-dir analysis/ --benchmark mmlu --dry-run --seeds 42,123,0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "cd /root/contamcal-irt-calibration && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analysis/bootstrap_triple_seed.py --results-dir results/ --output-dir analysis/ --benchmark mmlu --dry-run --seeds 42,123,0"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-21T07:12:04.782763+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Results dir: /root/contamcal-irt-calibration/results\\nOutput dir:  /root/contamcal-irt-calibration/analysis\\nSeeds:       [42, 123, 0]\\nDry-run:     True\\nBootstrap:   10000 resamples\\n\\nBenchmark:   mmlu\\n========================================================================\\nDATA COVERAGE\\n========================================================================\\nFamily               s42    s123      s0\\n----------------------------------------\\nPhi-4              ✓ 5/5   ✓ 5/5   ✓ 5/5\\nQwen2.5-14B        ✓ 5/5   ✓ 5/5   △ 3/5\\nQwen2.5-7B         ✓ 5/5   ✓ 5/5   — 0/5\\nGemma-2-9B         ✓ 5/5   ✓ 5/5   ✓ 5/5\\nOLMo-2-7B          ✓ 5/5   ✓ 5/5   ✓ 5/5\\n----------------------------------------\\nTotal: 68/75 cells found\\n\\n==========================================================================================\\nBOOTSTRAP CI: ACCURACY BY DOSAGE (mean ± 95% CI across seeds)\\n==========================================================================================\\nFamily            n                d000                d005                d025                d050                d100\\n-----------------------------------------------------------------------------------------------------------------------\\nPhi-4             3  76.40 [76.31,76.44](boot)  76.24 [75.92,76.41](boot)  76.91 [76.72,77.01](boot)  77.11 [76.75,77.30](boot)  77.12 [76.27,77.74](boot)\\nQwen2.5-14B       3  68.98 [68.67,69.24](boot)  69.57 [68.86,70.23](boot)  63.59 [62.04,64.60](boot)  60.20 [50.15,70.24](t)  58.00 [31.71,84.29](t)\\nQwen2.5-7B        2  66.35 [63.27,69.43](t)  64.06 [55.37,72.74](t)  63.90 [52.23,75.57](t)  64.03 [51.77,76.29](t)  65.46 [51.11,79.80](t)\\nGemma-2-9B        3  64.20 [61.86,65.84](boot)  64.46 [63.66,65.81](boot)  64.16 [63.02,64.80](boot)  64.61 [63.09,65.83](boot)  66.58 [65.62,67.15](boot)\\nOLMo-2-7B         3  54.93 [53.79,55.55](boot)  56.30 [56.14,56.46](boot)  55.89 [54.97,56
…[truncated 3843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-21T07:12:04.783027+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-29999",
  "command": "cd /root/contamcal-irt-calibration && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analysis/bootstrap_triple_seed.py --results-dir results/ --output-dir analysis/ --benchmark arc --dry-run --seeds 42,123,0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-29999",
    "command": "cd /root/contamcal-irt-calibration && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python analysis/bootstrap_triple_seed.py --results-dir results/ --output-dir analysis/ --benchmark arc --dry-run --seeds 42,123,0"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-21T07:12:04.783292+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Results dir: /root/contamcal-irt-calibration/results\\nOutput dir:  /root/contamcal-irt-calibration/analysis\\nSeeds:       [42, 123, 0]\\nDry-run:     True\\nBootstrap:   10000 resamples\\n\\nBenchmark:   arc\\n========================================================================\\nDATA COVERAGE\\n========================================================================\\nFamily               s42    s123      s0\\n----------------------------------------\\nPhi-4              ✓ 5/5   ✓ 5/5   ✓ 5/5\\nQwen2.5-14B        ✓ 5/5   ✓ 5/5   △ 4/5\\nQwen2.5-7B         ✓ 5/5   ✓ 5/5   — 0/5\\nGemma-2-9B         ✓ 5/5   ✓ 5/5   ✓ 5/5\\nOLMo-2-7B          ✓ 5/5   ✓ 5/5   ✓ 5/5\\n----------------------------------------\\nTotal: 69/75 cells found\\n\\n==========================================================================================\\nBOOTSTRAP CI: ACCURACY BY DOSAGE (mean ± 95% CI across seeds)\\n==========================================================================================\\nFamily            n                d000                d005                d025                d050                d100\\n-----------------------------------------------------------------------------------------------------------------------\\nPhi-4             3  91.92 [91.81,92.06](boot)  92.09 [91.81,92.35](boot)  92.38 [92.24,92.49](boot)  92.61 [92.41,92.75](boot)  92.58 [92.32,92.72](boot)\\nQwen2.5-14B       3  90.64 [90.44,90.84](boot)  90.67 [90.19,91.10](boot)  89.53 [88.91,89.87](boot)  88.18 [81.14,95.23](t)  85.61 [81.06,88.08](boot)\\nQwen2.5-7B        2  87.50 [82.62,92.38](t)  84.26 [60.95,107.57](t)  84.60 [77.55,91.65](t)  84.81 [81.56,88.06](t)  84.85 [83.23,86.48](t)\\nGemma-2-9B        3  85.89 [85.84,85.95](boot)  82.65 [77.82,85.64](boot)  79.29 [64.85,86.80](boot)  80.60 [71.08,85.41](boot)  85.75 [83.87,87.32](boot)\\nOLMo-2-7B         3  76.28 [75.85,76.62](boot)  76.88 [76.62,77.08](boot)  77.79 [76.62
…[truncated 3845 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 81 · 2026-05-21T07:12:04.783622+00:00_

两个 benchmark 的 bootstrap 都完成了。以下是汇总。

---

## Updated Bootstrap CI Results (2026-05-21)

### MMLU

| Family | n | Baseline | Mean Δ(d100) | 95% CI | Method | Significant? |
|--------|---|----------|-------------|--------|--------|-------------|
| Phi-4 | 3 | 76.40% | +0.72pp | [-0.17, +1.39] | boot | No (marginal) |
| Qwen2.5-14B | 2* | 68.98% | -11.05pp | [-32.41, +10.30] | t | No |
| Qwen2.5-7B | 2 | 66.35% | -0.89pp | [-12.16, +10.37] | t | No |
| **Gemma-2-9B** | **3** | **64.20%** | **+2.38pp** | **[+1.49, +3.14]** | **boot** | **Yes** |
| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | boot | No (marginal) |

### ARC-Challenge

| Family | n | Baseline | Mean Δ(d100) | 95% CI | Method | Significant? |
|--------|---|----------|-------------|--------|--------|-------------|
| Phi-4 | 3 | 91.92% | +0.65pp | [+0.51, +0.77] | boot | Yes |
| **Qwen2.5-14B** | **3*** | **90.64%** | **-5.03pp** | **[-9.39, -2.76]** | **boot** | **Yes** |
| Qwen2.5-7B | 2 | 87.50% | -2.65pp | [-5.90, +0.61] | t | No |
| **Gemma-2-9B** | **3** | **85.89%** | **-0.14pp** | **[-1.96, +1.42]** | **boot** | **No (p=0.371)** |
| OLMo-2-7B | 3 | 76.28% | +3.44pp | [+2.90, +3.78] | boot | Yes |

---

### Key changes from previous run

**Gemma-2-9B:**
- **MMLU**: n=2→3. CI collapsed from [-11.81, +17.06](t) to **[+1.49, +3.14](boot)** — now statistically significant positive effect (+2.38pp). s0 pattern = V-recovery (differs from s42=Benefit-sat, s123=Benefit).
- **ARC**: n=1→3. Went from point estimate +2.73pp (Benefit) to **[-1.96, +1.42](boot), not significant** (p=0.371, mean -0.14pp). Two of 3 seeds show V-recovery pattern. Cross-seed ρ = -0.167 (very low stability).

**Qwen2.5-14B (also changed):**
- **MMLU**: s0 added 3/5 dosages (d000,d005,d025). d000-d025 now use bootstrap (n=3); d050/d100 still t (n=2). Baseline shifted slightly 69.05%→68.98%.
- **ARC**: s0 added 4/5 dosages (missing d050). Δ(d100) went from -2.86pp CI[-6.65,+0.94](t) to **-5.03pp CI[-9.39,-2.76](boot) — now statistically significant harm**.

**Qwen2.5-7B**: unchanged (n=2 for both, no s0 data found).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_bootstrap-gemma2-rerun_20260521T070853"
}
```

</details>

---
