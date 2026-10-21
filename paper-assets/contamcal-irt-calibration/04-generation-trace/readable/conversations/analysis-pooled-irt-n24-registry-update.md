# analysis pooled irt n24 registry update

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/chats/worker_analysis_pooled-irt-n24-registry-update_20260516T191706.jsonl`
- **Structured JSON:** [`2461dbb3da976dad6af5.json`](../../sessions/24/2461dbb3da976dad6af5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

35 recorded events

### Tool call

_source line 1 · 2026-05-16T19:19:29.787492+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T19:19:29.787838+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T19:19:29.788019+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_006_pooled_2pl_gamma_qwen_n24'}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_006_pooled_2pl_gamma_qwen_n24'}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T19:19:29.788244+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6673}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T19:19:29.788434+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T19:19:29.788622+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"arc_challenge\\ngsm8k\\nmmlu\\npooled_rrf_irt_results.json\\nrun.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T19:19:29.788752+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/pooled_rrf_irt_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/pooled_rrf_irt_results.json"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-16T19:19:29.788874+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/mmlu/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/mmlu/"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-16T19:19:29.789191+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model_type\\\": \\\"2pl_gamma\\\",\\n    \\\"scales\\\": [\\n      \\\"0.5B\\\",\\n      \\\"1.5B\\\",\\n      \\\"Qwen2.5-3B\\\"\\n    ],\\n    \\\"benchmarks\\\": [\\n      \\\"mmlu\\\",\\n      \\\"arc_challenge\\\",\\n      \\\"gsm8k\\\"\\n    ],\\n    \\\"exposure\\\": \\\"rrf_signal\\\",\\n    \\\"exclusions\\\": [\\n      \\\"D045_05B_mmlu_arc\\\"\\n    ],\\n    \\\"stan_config\\\": {\\n      \\\"chains\\\": 4,\\n      \\\"warmup\\\": 1000,\\n      \\\"samples\\\": 1000,\\n      \\\"adapt_delta\\\": 0.95,\\n      \\\"max_treedepth\\\": 12,\\n      \\\"seed\\\": 42\\n    }\\n  },\\n  \\\"per_benchmark\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"benchmark\\\": \\\"mmlu\\\",\\n      \\\"model_type\\\": \\\"2pl_gamma\\\",\\n      \\\"exposure_source\\\": \\\"rrf_signal\\\",\\n      \\\"n_models\\\": 16,\\n      \\\"n_items\\\": 300,\\n      \\\"original_n_items\\\": 14042,\\n      \\\"subsampled\\\": true,\\n      \\\"models\\\": [\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s123_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dosage\\\": 0\\n        },\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dosage\\\": 0\\n        },\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s123_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dosage\\\": 5\\n        },\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dosage\\\": 5\\n        },\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s123_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dosage\\\": 25\\n        },\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s42_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dos
…[truncated 7944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T19:19:29.789387+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"irt_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T19:19:29.789565+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "status",
  "value": "DONE",
  "project": "contamcal-irt-calibration",
  "spec": "{'hypothesis': '2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization', 'command': 'python run_pooled_irt.py --model_type 2pl_gamma --exposure rrf_signal --scales 0.5B,1.5B,3B', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/', 'data_count': 300, 'model_name': '2PL+gamma', 'seed': 42, 'checkpoint_source': 'pooled_irt_fitting', 'parent': 'exp_006_pooled_irt_rrf_n25_v2'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration",
    "spec": "{'hypothesis': '2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization', 'command': 'python run_pooled_irt.py --model_type 2pl_gamma --exposure rrf_signal --scales 0.5B,1.5B,3B', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/', 'data_count': 300, 'model_name': '2PL+gamma', 'seed': 42, 'checkpoint_source': 'pooled_irt_fitting', 'parent': 'exp_006_pooled_irt_rrf_n25_v2'}"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-16T19:19:29.789714+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/arc_challenge/irt_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/arc_challenge/irt_results.json"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T19:19:29.789851+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → DONE. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.613}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T19:19:29.790083+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"arc_challenge\\\",\\n  \\\"model_type\\\": \\\"2pl_gamma\\\",\\n  \\\"exposure_source\\\": \\\"rrf_signal\\\",\\n  \\\"n_models\\\": 16,\\n  \\\"n_items\\\": 300,\\n  \\\"original_n_items\\\": 1172,\\n  \\\"subsampled\\\": true,\\n  \\\"models\\\": [\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 100\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 100\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d000_s123_aligned\\\",\\n      \\\"scale\\\": \\\"Qwen2.5-3B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d000_s42_a32_aligned\\\",\\n      \\\"scale\\\": \\\"Qwen2.5-3B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d005_s123_aligned\\\",\\n      \\\"scale\\\": \\\"Qwen2.5-3B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d005
…[truncated 4283 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T19:19:29.790272+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "status",
  "value": "PENDING",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "status",
    "value": "PENDING",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T19:19:29.790432+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:17:53.488Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.3205}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T19:19:29.790563+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "status",
  "value": "RUNNING",
  "project": "contamcal-irt-calibration",
  "spec": "{'hypothesis': '2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization', 'command': 'python run_pooled_irt.py --model_type 2pl_gamma --exposure rrf_signal --scales 0.5B,1.5B,3B', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/', 'data_count': 300, 'model_name': '2PL+gamma', 'seed': 42}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "status",
    "value": "RUNNING",
    "project": "contamcal-irt-calibration",
    "spec": "{'hypothesis': '2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization', 'command': 'python run_pooled_irt.py --model_type 2pl_gamma --exposure rrf_signal --scales 0.5B,1.5B,3B', 'server': 'cqa1-21977', 'data_path': '/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/', 'data_count': 300, 'model_name': '2PL+gamma', 'seed': 42}"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T19:19:29.790710+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PENDING → RUNNING. Allowed: ['DONE', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 0.6357}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T19:19:29.790835+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "status",
  "value": "DONE",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T19:19:29.790955+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 0.6749}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T19:19:29.791069+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "conclusion",
  "value": "success",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "conclusion",
    "value": "success",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T19:19:29.791188+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:18:09.245Z\", \"conclusion\": \"success\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0589}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T19:19:29.791302+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T19:19:29.791447+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:18:13.683Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9917}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T19:19:29.791562+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "log_path",
  "value": "/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/run.log",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "log_path",
    "value": "/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/run.log",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T19:19:29.791691+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"experiment\": {\"status\": \"PENDING\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:18:14.919Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/run.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0573}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T19:19:29.791883+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "status",
  "value": "DONE",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T19:19:29.792020+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:18:21.760Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/run.log\", \"completed_at\": \"2026-05-16T19:18:21.760Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.8743}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T19:19:29.792157+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "hypothesis",
  "value": "2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "hypothesis",
    "value": "2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T19:19:29.792298+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:18:31.706Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/run.log\", \"completed_at\": \"2026-05-16T19:18:21.760Z\", \"hypothesis\": \"2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.0934}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T19:19:29.792515+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "metrics",
  "value": "{'mmlu': {'N': 16, 'items': 300, 'gamma_mean': 0.6551, 'gamma_ci': [-0.4056, 1.7366], 'rhat': 1.0069, 'ess': 1453, 'ppp': 0.192, 'raw_mae': 0.0155, 'cal_mae': 0.007, 'delta_mae': 0.0085}, 'arc_challenge': {'N': 16, 'items': 300, 'gamma_mean': 0.7269, 'gamma_ci': [0.0207, 1.4433], 'rhat': 1.0072, 'ess': 1449, 'ppp': 0.003, 'raw_mae': 0.0338, 'cal_mae': 0.0201, 'delta_mae': 0.0136}, 'gsm8k': {'N': 24, 'items': 300, 'gamma_mean': 0.0639, 'gamma_ci': [-0.3636, 0.4902], 'rhat': 1.0078, 'ess': 1313, 'ppp': 0.5413, 'raw_mae': 0.1694, 'cal_mae': 0.0062, 'delta_mae': 0.1632}}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "metrics",
    "value": "{'mmlu': {'N': 16, 'items': 300, 'gamma_mean': 0.6551, 'gamma_ci': [-0.4056, 1.7366], 'rhat': 1.0069, 'ess': 1453, 'ppp': 0.192, 'raw_mae': 0.0155, 'cal_mae': 0.007, 'delta_mae': 0.0085}, 'arc_challenge': {'N': 16, 'items': 300, 'gamma_mean': 0.7269, 'gamma_ci': [0.0207, 1.4433], 'rhat': 1.0072, 'ess': 1449, 'ppp': 0.003, 'raw_mae': 0.0338, 'cal_mae': 0.0201, 'delta_mae': 0.0136}, 'gsm8k': {'N': 24, 'items': 300, 'gamma_mean': 0.0639, 'gamma_ci': [-0.3636, 0.4902], 'rhat': 1.0078, 'ess': 1313, 'ppp': 0.5413, 'raw_mae': 0.1694, 'cal_mae': 0.0062, 'delta_mae': 0.1632}}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T19:19:29.792690+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
  "field": "parent",
  "value": "exp_006_pooled_irt_rrf_n25_v2",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_006_pooled_2pl_gamma_qwen_n24",
    "field": "parent",
    "value": "exp_006_pooled_irt_rrf_n25_v2",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-16T19:19:29.792847+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:18:34.813Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/run.log\", \"completed_at\": \"2026-05-16T19:18:21.760Z\", \"hypothesis\": \"2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization\", \"metrics\": {\"mmlu\": {\"N\": 16, \"items\": 300, \"gamma_mean\": 0.6551, \"gamma_ci\": [-0.4056, 1.7366], \"rhat\": 1.0069, \"ess\": 1453, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"cal_mae\": 0.007, \"delta_mae\": 0.0085}, \"arc_challenge\": {\"N\": 16, \"items\": 300, \"gamma_mean\": 0.7269, \"gamma_ci\": [0.0207, 1.4433], \"rhat\": 1.0072, \"ess\": 1449, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136}, \"gsm8k\": {\"N\": 24, \"items\": 300, \"gamma_mean\": 0.0639, \"gamma_ci\": [-0.3636, 0.4902], \"rhat\": 1.0078, \"ess\": 1313, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632}}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3307}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T19:19:29.793010+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_006_pooled_2pl_gamma_qwen_n24\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T19:17:53.487Z\", \"updated_at\": \"2026-05-16T19:18:36.187Z\", \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/\", \"log_path\": \"/root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/run.log\", \"completed_at\": \"2026-05-16T19:18:21.760Z\", \"hypothesis\": \"2PL+γ pooled IRT with RRF exposure signal, Qwen-only N=16-24, fixes 4PL over-parameterization\", \"metrics\": {\"mmlu\": {\"N\": 16, \"items\": 300, \"gamma_mean\": 0.6551, \"gamma_ci\": [-0.4056, 1.7366], \"rhat\": 1.0069, \"ess\": 1453, \"ppp\": 0.192, \"raw_mae\": 0.0155, \"cal_mae\": 0.007, \"delta_mae\": 0.0085}, \"arc_challenge\": {\"N\": 16, \"items\": 300, \"gamma_mean\": 0.7269, \"gamma_ci\": [0.0207, 1.4433], \"rhat\": 1.0072, \"ess\": 1449, \"ppp\": 0.003, \"raw_mae\": 0.0338, \"cal_mae\": 0.0201, \"delta_mae\": 0.0136}, \"gsm8k\": {\"N\": 24, \"items\": 300, \"gamma_mean\": 0.0639, \"gamma_ci\": [-0.3636, 0.4902], \"rhat\": 1.0078, \"ess\": 1313, \"ppp\": 0.5413, \"raw_mae\": 0.1694, \"cal_mae\": 0.0062, \"delta_mae\": 0.1632}}, \"parent\": \"exp_006_pooled_irt_rrf_n25_v2\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.2307}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-16T19:19:29.793220+00:00_

Registry updated: `exp_006_pooled_2pl_gamma_qwen_n24` → DONE/success with full metrics.

---

## 结果解读

**GSM8K** — 最强结果。γ≈0（无污染信号）但 ΔMAE=0.163（96% MAE 降幅），PPP=0.54（完美拟合）。IRT 的 ability + difficulty 参数单独就能把 raw 0.11–0.74 的 accuracy 校准到 MAE=0.006。这是 Claim 2（calibration effectiveness independent of contamination）的 headline evidence。

**MMLU** — γ=0.66 但 95% CI 跨 0。PPP=0.19 模型拟合可接受。γ 不显著符合 D108 domain heterogeneity 假设：14042 items 里 subsample 300, 污染信号被稀释。校准仍有效（ΔMAE=0.009）。

**ARC** — γ=0.73, CI 排除 0（污染信号显著），但 **PPP=0.003 表示严重 model misfit**。观察发现 obs_mean=0.799 vs pred_mean=0.780，模型系统性低估。根因：1.5B (~0.76) 和 3B (~0.83) 形成双峰 ability 分布，N=16 下 2PL 拟合困难。

---

## ARC Misfit 诊断

PPP=0.003 **不是** 3PL 的问题。在 75-83% accuracy 下（4选1 MCQ），guessing floor (25%) 远低于实际表现，加 guessing parameter 不会改善拟合。

真正原因：两个 scale 之间 ability gap 太大且每个 scale 内部 variance 很小，导致 item discrimination 估计不稳定。解决路径：

1. **增加 N（优先）**：加入 0.5B respondents（如果 ARC signals 就绪），N=24 的三层 ability 分布比 N=16 的双峰好拟合得多
2. **多组 IRT**：用 scale 作为 group covariate 的 hierarchical 2PL+γ
3. **接受并报告为 limitation**：ARC cal_MAE=0.020 仍优于 raw_MAE=0.034（40% 降幅），只是统计检验力不足

**不建议跑 3PL+γ**——根据 C008 规则，N=16 已经低于 4PL 的 identifiability 门槛，3PL 多一个参数同样有风险，且 guessing 不是此处的问题。

---

## 对论文的影响

| Claim | 支撑强度 | 来源 |
|-------|---------|------|
| Claim 2: IRT calibration effective | **强** | GSM8K ΔMAE=0.163, PPP=0.54 |
| Claim 1: γ detects contamination | **中** | ARC γ显著但 model misfit; MMLU γ不显著 |

---

## 建议下一步

**最高优先级**：等 0.5B s123 signals 完成后，重跑 ARC pooled IRT（N=24，三个 scale），预期 PPP 显著改善。这同时满足 C007 优先级（0.5B s123 是最高 ROI）和解决 ARC misfit。不需要单独跑 3PL+γ 实验。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_pooled-irt-n24-registry-update_20260516T191706"
}
```

</details>

---
